#!/usr/bin/env python3
"""
MCHeli Overdrive asset realistifier.

Run from the repository root:
  python tools/realistify_mchelio_assets.py --apply
  python tools/realistify_mchelio_assets.py --dry-run

This updates known aircraft/vehicle definition files using stable real-world-ish
values and the balancing formulas from the MCHO documentation. It is intentionally
conservative: geometry, seats, weapons mounts, recipes, textures, and model parts
are left untouched.
"""
from __future__ import annotations

import argparse
import difflib
import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, MutableMapping, Optional, Tuple

ROOT = Path("assets/mcheli")

# Project scale formulas from the MCHO notes:
#   ground speed: kph / 74.16
#   aircraft revised speed: (kph / 1000) * 1.74
#   fuel: MaxFuel = real fuel liters * 4, FuelConsumption = MaxFuel / range_km
# The fuel formula intentionally keeps values practical in-game while preserving
# real capacity/range ratios.
GROUND_KPH_PER_SPEED = 74.16
AIRCRAFT_SCALE = 1.74 / 1000.0
FUEL_SCALE = 4.0

@dataclass(frozen=True)
class VehicleSpec:
    path: str
    kind: str  # tank, car, ship, plane, heli, drone
    top_speed_kph: float
    fuel_liters: Optional[float] = None
    range_km: Optional[float] = None
    mass_tonnes: Optional[float] = None
    armor_front_mm: Optional[float] = None
    armor_side_mm: Optional[float] = None
    armor_rear_mm: Optional[float] = None
    armor_min_mm: Optional[float] = None
    max_hp: Optional[int] = None
    notes: str = ""
    extra: Mapping[str, str] = field(default_factory=dict)


def ground_speed(kph: float) -> float:
    return round(kph / GROUND_KPH_PER_SPEED, 3)


def aircraft_speed(kph: float) -> float:
    return round(kph * AIRCRAFT_SCALE, 3)


def fuel_values(fuel_liters: Optional[float], range_km: Optional[float]) -> Tuple[Optional[int], Optional[float]]:
    if not fuel_liters or not range_km or range_km <= 0:
        return None, None
    max_fuel = int(round(fuel_liters * FUEL_SCALE))
    consumption = round(max_fuel / range_km, 3)
    return max_fuel, consumption


def hp_from_mass(mass_tonnes: Optional[float], kind: str) -> Optional[int]:
    if mass_tonnes is None:
        return None
    # Keep survivability playable but anchored to weight/class.
    mult = {
        "tank": 18,
        "car": 10,
        "ship": 8,
        "plane": 5,
        "heli": 6,
        "drone": 3,
    }.get(kind, 10)
    return int(round(max(80, mass_tonnes * mult) / 10.0) * 10)


def armor_factor(thickness_mm: Optional[float], reference_mm: float = 300.0) -> Optional[float]:
    if thickness_mm is None:
        return None
    return round(max(0.02, min(1.0, thickness_mm / reference_mm)), 3)


def armor_min_damage(spec: VehicleSpec) -> Optional[int]:
    # MCHO note: under 100 mm effective armor should stay default-ish; otherwise
    # use actual thickness as the threshold basis.
    thickness = spec.armor_min_mm or spec.armor_side_mm or spec.armor_front_mm
    if thickness is None:
        return None
    if thickness < 100:
        return 1
    return int(round(thickness))


def armor_max_damage(spec: VehicleSpec) -> Optional[int]:
    if spec.armor_front_mm is None:
        return None
    return int(round(max(100, spec.armor_front_mm)))


# Seed set: files that were discovered in the attached repo search and have safe,
# reasonably stable real-world public specs. Add more entries over time; unknown
# files are left unchanged rather than guessed.
SPECS: List[VehicleSpec] = [
    VehicleSpec("assets/mcheli/tanks/t-90a.txt", "tank", 60, 1600, 550, 46.5, 550, 80, 45, 80, notes="T-90A road speed/range/capacity class; composite front normalized to effective rating."),
    VehicleSpec("assets/mcheli/tanks/m2.txt", "tank", 66, 662, 480, 30.0, 80, 35, 25, 25, notes="M2 Bradley family; aluminum/composite armor kept below MBT class."),
    VehicleSpec("assets/mcheli/tanks/2s19.txt", "tank", 60, 840, 500, 42.0, 15, 15, 15, 15, notes="2S19 Msta-S: 15 mm all-around armor, 60 km/h road speed."),
    VehicleSpec("assets/mcheli/tanks/m163.txt", "tank", 68, 360, 480, 12.3, 38, 38, 38, 38, notes="M163/M113 aluminum armor class; thin but resistant to small arms."),
    VehicleSpec("assets/mcheli/tanks/gepard.txt", "tank", 65, 985, 550, 47.5, 70, 30, 25, 25, notes="Flakpanzer Gepard, Leopard 1 chassis class."),
    VehicleSpec("assets/mcheli/tanks/type74.txt", "tank", 53, 950, 400, 38.0, 189, 35, 25, 25, notes="Type 74 MBT; steel armor normalized conservatively."),
    VehicleSpec("assets/mcheli/tanks/btr90.txt", "tank", 100, 300, 800, 20.9, 14, 9, 7, 7, notes="BTR-90 wheeled APC; high road speed, light armor."),
    VehicleSpec("assets/mcheli/tanks/m1129.txt", "tank", 100, 200, 530, 18.8, 14, 14, 14, 14, notes="M1129 Stryker mortar carrier class."),
    VehicleSpec("assets/mcheli/tanks/c1.txt", "tank", 65, 1270, 550, 54.0, 500, 80, 45, 80, notes="Ariete C1 MBT class; composite effective front approximation."),
    VehicleSpec("assets/mcheli/tanks/c2.txt", "tank", 65, 1300, 450, 62.5, 550, 90, 50, 90, notes="Leopard C2/Leo 1 upgrade class; front effective approximation."),
    VehicleSpec("assets/mcheli/tanks/m4.txt", "tank", 40, 660, 160, 30.3, 76, 38, 38, 38, notes="M4 Sherman gasoline variant class."),
    VehicleSpec("assets/mcheli/tanks/m4a1.txt", "tank", 40, 660, 160, 30.6, 76, 38, 38, 38, notes="M4A1 Sherman class."),
    VehicleSpec("assets/mcheli/planes/f8f.txt", "plane", 678, 700, 1778, 4.4, max_hp=180, notes="F8F Bearcat max speed; piston fighter."),
    VehicleSpec("assets/mcheli/planes/bf109.txt", "plane", 640, 400, 850, 3.2, max_hp=150, notes="Bf 109 late-war fighter class."),
    VehicleSpec("assets/mcheli/planes/a6m2.txt", "plane", 533, 518, 3100, 2.4, max_hp=120, notes="A6M2 Zero ferry range/fuel class."),
    VehicleSpec("assets/mcheli/planes/mig23.txt", "plane", 2445, 4700, 1150, 16.7, max_hp=260, notes="MiG-23 maximum speed; capped only by config if desired."),
    VehicleSpec("assets/mcheli/planes/su24.txt", "plane", 1654, 11700, 2850, 39.7, max_hp=360, notes="Su-24 strike aircraft."),
    VehicleSpec("assets/mcheli/planes/m2000c.txt", "plane", 2336, 3160, 1550, 13.8, max_hp=240, notes="Mirage 2000C class."),
    VehicleSpec("assets/mcheli/planes/harrier.txt", "plane", 1176, 3500, 2200, 10.4, max_hp=240, notes="Harrier/AV-8 VTOL class.", extra={"EnableVtol":"true", "DefaultVtol":"false", "VtolYaw":"0.30", "VtolPitch":"0.22"}),
    VehicleSpec("assets/mcheli/planes/yak38.txt", "plane", 1280, 2750, 1300, 11.3, max_hp=220, notes="Yak-38 VTOL class.", extra={"EnableVtol":"true", "DefaultVtol":"false", "VtolYaw":"0.28", "VtolPitch":"0.20"}),
    VehicleSpec("assets/mcheli/planes/a6.txt", "plane", 1040, 6940, 5200, 27.5, max_hp=300, notes="A-6 Intruder strike aircraft."),
    VehicleSpec("assets/mcheli/planes/j8.txt", "plane", 2339, 4500, 2200, 17.8, max_hp=260, notes="J-8 interceptor class."),
    VehicleSpec("assets/mcheli/planes/geran2.txt", "drone", 185, 50, 1800, 0.2, max_hp=40, notes="Geran-2/Shahed-136 loitering munition class."),
    VehicleSpec("assets/mcheli/planes/mqm170.txt", "drone", 185, 50, 1800, 0.2, max_hp=40, notes="MQM/target drone fallback using loitering-drone class values."),
    VehicleSpec("assets/mcheli/ships/mark5.txt", "ship", 83, 1900, 926, 57.0, max_hp=450, notes="Mk V SOC patrol boat class; speed converted from knots."),
]

KEY_RE = re.compile(r"^(?P<key>[A-Za-z][A-Za-z0-9_]*)\s*=.*$", re.M)


def format_value(v) -> str:
    if isinstance(v, float):
        s = f"{v:.3f}".rstrip("0").rstrip(".")
        return s if s else "0"
    return str(v)


def update_or_insert(text: str, key: str, value, insert_after: Optional[str] = None) -> str:
    value_s = format_value(value)
    pattern = re.compile(rf"^({re.escape(key)}\s*=).*$", re.I | re.M)
    if pattern.search(text):
        return pattern.sub(rf"\1 {value_s}", text, count=1)
    lines = text.splitlines()
    insert_at = 0
    if insert_after:
        for i, line in enumerate(lines):
            if re.match(rf"^{re.escape(insert_after)}\s*=", line, flags=re.I):
                insert_at = i + 1
                break
    else:
        for i, line in enumerate(lines):
            if line.strip() and not line.lstrip().startswith(";"):
                insert_at = i + 1
                break
    lines.insert(insert_at, f"{key} = {value_s}")
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def apply_spec(path: Path, spec: VehicleSpec) -> Tuple[bool, str, str]:
    old = path.read_text(encoding="utf-8-sig", errors="replace")
    new = old

    if spec.kind in ("plane", "heli", "drone"):
        speed = aircraft_speed(spec.top_speed_kph)
    else:
        speed = ground_speed(spec.top_speed_kph)
    new = update_or_insert(new, "Speed", speed, "MaxHp")

    hp = spec.max_hp if spec.max_hp is not None else hp_from_mass(spec.mass_tonnes, spec.kind)
    if hp is not None:
        new = update_or_insert(new, "MaxHp", hp, "DisplayName")

    max_fuel, fuel_consumption = fuel_values(spec.fuel_liters, spec.range_km)
    if max_fuel is not None:
        new = update_or_insert(new, "MaxFuel", max_fuel, "ArmorDamageFactor")
    if fuel_consumption is not None:
        new = update_or_insert(new, "FuelConsumption", fuel_consumption, "MaxFuel")

    if spec.kind == "tank":
        amin = armor_min_damage(spec)
        amax = armor_max_damage(spec)
        if amin is not None:
            new = update_or_insert(new, "ArmorMinDamage", amin, "StepHeight")
        if amax is not None:
            new = update_or_insert(new, "ArmorMaxDamage", amax, "ArmorMinDamage")
        # Do not rewrite existing BoundingBox geometry. Only add a realistic note
        # and armor scaling fields; bounding boxes depend on the model mesh.
        if spec.armor_front_mm:
            new = update_or_insert(new, "ArmorDamageFactor", round(min(1.0, max(0.15, spec.armor_front_mm / 600.0)), 3), "DamageFactor")

    if spec.kind in ("plane", "drone"):
        # Enable the new model conservatively and derive values from speed.
        new = update_or_insert(new, "EnableRealisticFlightModel", "true", "Category")
        new = update_or_insert(new, "MaxLevelSpeed", speed, "EnableRealisticFlightModel")
        new = update_or_insert(new, "StallSpeedFactor", 0.22 if spec.kind == "plane" else 0.18, "MaxLevelSpeed")
        new = update_or_insert(new, "CriticalAoA", 18.0 if spec.kind == "plane" else 16.0, "StallSpeedFactor")
        new = update_or_insert(new, "BaseDrag", 0.0018 if spec.kind == "plane" else 0.0035, "CriticalAoA")
        new = update_or_insert(new, "InducedDrag", 0.0065 if spec.kind == "plane" else 0.004, "BaseDrag")
        new = update_or_insert(new, "IdleDrag", 0.0045 if spec.kind == "plane" else 0.006, "InducedDrag")
        if spec.kind == "plane":
            new = update_or_insert(new, "MaxComfortableG", 7.5, "IdleDrag")
            new = update_or_insert(new, "MaxStructuralG", 9.0, "MaxComfortableG")
            new = update_or_insert(new, "DiveSpeedMultiplier", 1.18, "MaxStructuralG")
        else:
            new = update_or_insert(new, "MaxComfortableG", 3.0, "IdleDrag")
            new = update_or_insert(new, "MaxStructuralG", 5.0, "MaxComfortableG")
            new = update_or_insert(new, "DiveSpeedMultiplier", 1.05, "MaxStructuralG")

    for k, v in spec.extra.items():
        new = update_or_insert(new, k, v, "ThrottleUpDown")

    marker = "; RealismSource = MCHO scripted pass"
    if marker not in new:
        new = new.rstrip() + f"\n\n{marker}; {spec.notes}\n"

    return old != new, old, new


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Repository root")
    ap.add_argument("--apply", action="store_true", help="Write files")
    ap.add_argument("--dry-run", action="store_true", help="Print diffs only")
    args = ap.parse_args()

    repo = Path(args.root)
    changed = 0
    missing = []
    for spec in SPECS:
        path = repo / spec.path
        if not path.exists():
            missing.append(spec.path)
            continue
        is_changed, old, new = apply_spec(path, spec)
        if not is_changed:
            continue
        changed += 1
        if args.dry_run or not args.apply:
            print(f"\n--- {spec.path}")
            print("".join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile=spec.path, tofile=spec.path)))
        if args.apply:
            path.write_text(new, encoding="utf-8")

    print(f"\nChanged candidates: {changed}")
    if missing:
        print(f"Missing mapped files: {len(missing)}")
        for m in missing[:20]:
            print(f"  - {m}")
        if len(missing) > 20:
            print("  ...")
    if not args.apply:
        print("Dry run only. Re-run with --apply to write changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
