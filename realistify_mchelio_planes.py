#!/usr/bin/env python3
"""
Plane-first MCHeli Overdrive asset realistifier.

Run from the repository root:
  python tools/realistify_mchelio_planes.py --dry-run
  python tools/realistify_mchelio_planes.py --apply

This is intentionally focused on assets/mcheli/planes/*.txt. It updates only
plane/drone/VTOL tuning values and leaves model geometry, weapon mounts, seats,
recipes, textures, sounds, HUD names, and other artist-authored declarations alone.

Formula basis from MCHO documentation:
  - Aircraft speed: Speed = real_kph * (1.74 / 1000)
  - If a value is missing, MCHeli keeps safe defaults; realistic flight is opt-in
    through EnableRealisticFlightModel = true.
  - Fuel is game-balanced from real fuel capacity/range:
      MaxFuel = real_liters * 4
      FuelConsumption = MaxFuel / range_km
"""
from __future__ import annotations

import argparse
import difflib
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Mapping, Optional, Tuple

AIRCRAFT_SCALE = 1.74 / 1000.0
FUEL_SCALE = 4.0


@dataclass(frozen=True)
class PlaneSpec:
    path: str
    role: str
    top_speed_kph: float
    stall_kph: Optional[float] = None
    fuel_liters: Optional[float] = None
    range_km: Optional[float] = None
    mass_tonnes: Optional[float] = None
    max_hp: Optional[int] = None
    comfortable_g: float = 7.5
    structural_g: float = 9.0
    critical_aoa: float = 18.0
    dive_multiplier: float = 1.18
    base_drag: float = 0.0018
    induced_drag: float = 0.0065
    idle_drag: float = 0.0045
    control_surface_drag: float = 0.0025
    climb_loss: float = 0.006
    dive_gain: float = 0.008
    throttle_accel: float = 0.018
    engine_drag: float = 0.012
    inertia: float = 1.0
    torque: float = 0.35
    damping: float = 0.35
    vtol: bool = False
    drone: bool = False
    notes: str = ""
    extra: Mapping[str, str] = field(default_factory=dict)


def scaled_speed(kph: float) -> float:
    return round(kph * AIRCRAFT_SCALE, 3)


def fuel_values(liters: Optional[float], range_km: Optional[float]) -> Tuple[Optional[int], Optional[float]]:
    if not liters or not range_km or range_km <= 0:
        return None, None
    max_fuel = int(round(liters * FUEL_SCALE))
    return max_fuel, round(max_fuel / range_km, 3)


def hp_from_mass(mass_tonnes: Optional[float], role: str, drone: bool = False) -> Optional[int]:
    if mass_tonnes is None:
        return None
    if drone:
        return int(round(max(30, mass_tonnes * 18) / 10.0) * 10)
    if role in ("heavy_bomber", "transport", "maritime"):
        mult = 7.0
    elif role in ("bomber", "strike"):
        mult = 8.0
    else:
        mult = 12.0
    return int(round(max(100, mass_tonnes * mult) / 10.0) * 10)


def stall_factor(spec: PlaneSpec) -> float:
    # Prefer actual stall speed if known. Otherwise use reasonable category defaults.
    if spec.stall_kph and spec.top_speed_kph > 0:
        return round(max(0.12, min(0.38, spec.stall_kph / spec.top_speed_kph)), 3)
    if spec.drone:
        return 0.18
    if spec.role in ("ww2_fighter", "prop", "attacker_prop"):
        return 0.24
    if spec.role in ("heavy_bomber", "transport", "maritime"):
        return 0.20
    if spec.role in ("bomber", "strike"):
        return 0.22
    return 0.21


def insert_or_replace(text: str, key: str, value, after: Optional[str] = None) -> str:
    value_s = fmt(value)
    pattern = re.compile(rf"^({re.escape(key)}\s*=).*$", re.I | re.M)
    if pattern.search(text):
        return pattern.sub(rf"\1 {value_s}", text, count=1)
    lines = text.splitlines()
    idx = 0
    if after:
        for i, line in enumerate(lines):
            if re.match(rf"^{re.escape(after)}\s*=", line, flags=re.I):
                idx = i + 1
                break
    else:
        for i, line in enumerate(lines):
            if line.strip() and not line.lstrip().startswith(";"):
                idx = i + 1
                break
    lines.insert(idx, f"{key} = {value_s}")
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def fmt(value) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, float):
        return f"{value:.3f}".rstrip("0").rstrip(".")
    return str(value)


# Plane definitions discovered in the attached repo search. Values are conservative
# public-spec anchors; add/adjust entries as exact variants are confirmed.
SPECS: List[PlaneSpec] = [
    PlaneSpec("assets/mcheli/planes/f8f.txt", "ww2_fighter", 678, 154, 700, 1778, 4.4, max_hp=180, comfortable_g=7.5, structural_g=11.0, notes="F8F Bearcat."),
    PlaneSpec("assets/mcheli/planes/bf109.txt", "ww2_fighter", 640, 150, 400, 850, 3.2, max_hp=150, comfortable_g=7.5, structural_g=11.0, notes="Bf 109 late-war class."),
    PlaneSpec("assets/mcheli/planes/a6m2.txt", "ww2_fighter", 533, 110, 518, 3100, 2.4, max_hp=120, comfortable_g=7.0, structural_g=10.0, notes="A6M2 Zero."),
    PlaneSpec("assets/mcheli/planes/n1k1.txt", "ww2_fighter", 584, 150, 600, 1430, 3.9, max_hp=150, comfortable_g=7.0, structural_g=10.0, notes="N1K1-J Shiden class."),
    PlaneSpec("assets/mcheli/planes/ju87.txt", "attacker_prop", 390, 108, 500, 500, 4.3, max_hp=140, comfortable_g=5.5, structural_g=8.0, base_drag=0.0024, induced_drag=0.0075, notes="Ju 87 Stuka."),
    PlaneSpec("assets/mcheli/planes/b29.txt", "heavy_bomber", 574, 170, 35800, 5230, 60.6, max_hp=420, comfortable_g=3.0, structural_g=5.0, critical_aoa=15.0, base_drag=0.0022, induced_drag=0.008, idle_drag=0.0055, inertia=2.2, torque=0.22, damping=0.48, notes="B-29 Superfortress."),
    PlaneSpec("assets/mcheli/planes/h6k.txt", "maritime", 385, 115, 7760, 6700, 17.5, max_hp=260, comfortable_g=3.2, structural_g=5.5, critical_aoa=15.0, base_drag=0.0025, inertia=1.8, torque=0.24, damping=0.46, notes="H6K flying boat."),
    PlaneSpec("assets/mcheli/planes/h8k.txt", "maritime", 465, 125, 13400, 7150, 24.5, max_hp=300, comfortable_g=3.2, structural_g=5.5, critical_aoa=15.0, base_drag=0.0024, inertia=2.0, torque=0.23, damping=0.48, notes="H8K flying boat."),
    PlaneSpec("assets/mcheli/planes/ac-47.txt", "transport", 360, 110, 3000, 2400, 12.7, max_hp=220, comfortable_g=3.0, structural_g=5.0, critical_aoa=15.0, base_drag=0.0023, inertia=1.7, torque=0.25, damping=0.45, notes="AC-47/DC-3 class."),
    PlaneSpec("assets/mcheli/planes/qf-80.txt", "early_jet", 956, 170, 1665, 1328, 5.8, max_hp=180, comfortable_g=6.0, structural_g=8.0, notes="F/QF-80 Shooting Star."),
    PlaneSpec("assets/mcheli/planes/mig-15.txt", "early_jet", 1076, 174, 1450, 1200, 5.0, max_hp=180, comfortable_g=6.5, structural_g=8.5, notes="MiG-15."),
    PlaneSpec("assets/mcheli/planes/f-5e.txt", "fighter", 1700, 225, 2560, 1405, 11.2, max_hp=220, comfortable_g=7.3, structural_g=9.0, notes="F-5E Tiger II."),
    PlaneSpec("assets/mcheli/planes/f4a.txt", "fighter", 2370, 250, 7549, 2600, 18.8, max_hp=260, comfortable_g=7.3, structural_g=9.0, notes="F-4 Phantom II class."),
    PlaneSpec("assets/mcheli/planes/f-15e.txt", "fighter", 2655, 240, 6100, 3900, 31.8, max_hp=320, comfortable_g=9.0, structural_g=12.0, critical_aoa=20.0, notes="F-15E Strike Eagle."),
    PlaneSpec("assets/mcheli/planes/f-15s_mtd.txt", "fighter", 2655, 220, 6100, 3900, 31.8, max_hp=320, comfortable_g=9.0, structural_g=12.0, critical_aoa=24.0, base_drag=0.0017, notes="F-15 STOL/MTD experimental class."),
    PlaneSpec("assets/mcheli/planes/fa18fold.txt", "fighter", 1915, 248, 4930, 2346, 21.3, max_hp=280, comfortable_g=7.5, structural_g=9.0, critical_aoa=25.0, notes="F/A-18 carrier fighter."),
    PlaneSpec("assets/mcheli/planes/rafalem.txt", "fighter", 1912, 213, 4700, 3700, 24.5, max_hp=290, comfortable_g=9.0, structural_g=11.0, critical_aoa=24.0, notes="Rafale M."),
    PlaneSpec("assets/mcheli/planes/fa50.txt", "fighter", 1837, 200, 2655, 1850, 12.3, max_hp=230, comfortable_g=8.0, structural_g=9.5, notes="FA-50/T-50 class."),
    PlaneSpec("assets/mcheli/planes/mirage3e.txt", "fighter", 2350, 213, 3335, 1200, 13.7, max_hp=230, comfortable_g=7.5, structural_g=9.0, notes="Mirage IIIE."),
    PlaneSpec("assets/mcheli/planes/m2000c.txt", "fighter", 2336, 213, 3160, 1550, 13.8, max_hp=240, comfortable_g=9.0, structural_g=11.0, critical_aoa=22.0, notes="Mirage 2000C."),
    PlaneSpec("assets/mcheli/planes/m2000-5.txt", "fighter", 2336, 213, 3160, 1550, 13.8, max_hp=245, comfortable_g=9.0, structural_g=11.0, critical_aoa=22.0, notes="Mirage 2000-5."),
    PlaneSpec("assets/mcheli/planes/mig23.txt", "fighter", 2445, 260, 4700, 1150, 16.7, max_hp=260, comfortable_g=8.5, structural_g=10.0, notes="MiG-23."),
    PlaneSpec("assets/mcheli/planes/mig31k.txt", "interceptor", 3000, 280, 16350, 3000, 46.8, max_hp=360, comfortable_g=5.0, structural_g=7.0, critical_aoa=16.0, base_drag=0.0016, inertia=1.8, torque=0.25, damping=0.46, notes="MiG-31K heavy interceptor."),
    PlaneSpec("assets/mcheli/planes/j8.txt", "interceptor", 2339, 230, 4500, 2200, 17.8, max_hp=260, comfortable_g=8.0, structural_g=9.5, notes="J-8 interceptor."),
    PlaneSpec("assets/mcheli/planes/a6.txt", "strike", 1040, 190, 6940, 5200, 27.5, max_hp=300, comfortable_g=6.5, structural_g=8.0, critical_aoa=17.0, base_drag=0.002, inertia=1.5, torque=0.30, damping=0.42, notes="A-6 Intruder."),
    PlaneSpec("assets/mcheli/planes/su24.txt", "strike", 1654, 240, 11700, 2850, 39.7, max_hp=360, comfortable_g=6.5, structural_g=8.5, critical_aoa=17.0, inertia=1.7, torque=0.28, damping=0.44, notes="Su-24."),
    PlaneSpec("assets/mcheli/planes/su34.txt", "strike", 1900, 230, 12100, 4000, 45.1, max_hp=380, comfortable_g=7.0, structural_g=9.0, critical_aoa=20.0, inertia=1.7, torque=0.30, damping=0.43, notes="Su-34."),
    PlaneSpec("assets/mcheli/planes/q-5d.txt", "strike", 1210, 210, 2200, 2000, 11.8, max_hp=220, comfortable_g=7.0, structural_g=8.5, notes="Q-5 Fantan class."),
    PlaneSpec("assets/mcheli/planes/tornado-ids.txt", "strike", 2400, 250, 4663, 1390, 20.4, max_hp=280, comfortable_g=7.5, structural_g=9.0, notes="Tornado IDS."),
    PlaneSpec("assets/mcheli/planes/harrier.txt", "vtol", 1176, 210, 3500, 2200, 10.4, max_hp=240, comfortable_g=7.0, structural_g=9.0, critical_aoa=22.0, vtol=True, notes="Harrier/AV-8 VTOL."),
    PlaneSpec("assets/mcheli/planes/harrier_en.txt", "vtol", 1176, 210, 3500, 2200, 10.4, max_hp=240, comfortable_g=7.0, structural_g=9.0, critical_aoa=22.0, vtol=True, notes="Harrier export/alt config."),
    PlaneSpec("assets/mcheli/planes/yak38.txt", "vtol", 1280, 230, 2750, 1300, 11.3, max_hp=220, comfortable_g=6.5, structural_g=8.0, vtol=True, notes="Yak-38 VTOL."),
    PlaneSpec("assets/mcheli/planes/yak38_r60.txt", "vtol", 1280, 230, 2750, 1300, 11.3, max_hp=220, comfortable_g=6.5, structural_g=8.0, vtol=True, notes="Yak-38 R-60 loadout."),
    PlaneSpec("assets/mcheli/planes/il28sh.txt", "bomber", 902, 170, 7908, 2400, 21.2, max_hp=260, comfortable_g=4.0, structural_g=6.0, critical_aoa=16.0, inertia=1.5, torque=0.28, damping=0.44, notes="Il-28Sh."),
    PlaneSpec("assets/mcheli/planes/mirageiv.txt", "bomber", 2340, 260, 14000, 4000, 33.5, max_hp=330, comfortable_g=5.5, structural_g=7.0, critical_aoa=16.0, inertia=1.6, torque=0.27, damping=0.45, notes="Mirage IV."),
    PlaneSpec("assets/mcheli/planes/b-1nuclear.txt", "heavy_bomber", 1335, 260, 120000, 9400, 86.2, max_hp=520, comfortable_g=3.0, structural_g=5.0, critical_aoa=15.0, base_drag=0.0019, inertia=2.6, torque=0.20, damping=0.52, notes="B-1B class."),
    PlaneSpec("assets/mcheli/planes/b52.txt", "heavy_bomber", 1047, 220, 181610, 14200, 83.3, max_hp=520, comfortable_g=2.5, structural_g=4.5, critical_aoa=14.0, base_drag=0.0022, inertia=3.0, torque=0.18, damping=0.55, notes="B-52 Stratofortress."),
    PlaneSpec("assets/mcheli/planes/b52n.txt", "heavy_bomber", 1047, 220, 181610, 14200, 83.3, max_hp=520, comfortable_g=2.5, structural_g=4.5, critical_aoa=14.0, base_drag=0.0022, inertia=3.0, torque=0.18, damping=0.55, notes="B-52 nuclear/alt config."),
    PlaneSpec("assets/mcheli/planes/b-2a2.txt", "heavy_bomber", 1010, 250, 75750, 11100, 71.7, max_hp=500, comfortable_g=3.0, structural_g=5.0, critical_aoa=17.0, base_drag=0.0017, inertia=2.7, torque=0.20, damping=0.52, notes="B-2A Spirit alt config."),
    PlaneSpec("assets/mcheli/planes/b-2a3.txt", "heavy_bomber", 1010, 250, 75750, 11100, 71.7, max_hp=500, comfortable_g=3.0, structural_g=5.0, critical_aoa=17.0, base_drag=0.0017, inertia=2.7, torque=0.20, damping=0.52, notes="B-2A Spirit alt config."),
    PlaneSpec("assets/mcheli/planes/b-2a4.txt", "heavy_bomber", 1010, 250, 75750, 11100, 71.7, max_hp=500, comfortable_g=3.0, structural_g=5.0, critical_aoa=17.0, base_drag=0.0017, inertia=2.7, torque=0.20, damping=0.52, notes="B-2A Spirit alt config."),
    PlaneSpec("assets/mcheli/planes/tu95k22.txt", "maritime", 920, 180, 87000, 15000, 90.0, max_hp=520, comfortable_g=2.8, structural_g=4.8, critical_aoa=14.0, base_drag=0.0022, inertia=3.0, torque=0.18, damping=0.55, notes="Tu-95K-22 Bear."),
    PlaneSpec("assets/mcheli/planes/tu142real.txt", "maritime", 925, 180, 87000, 12550, 90.0, max_hp=520, comfortable_g=2.8, structural_g=4.8, critical_aoa=14.0, base_drag=0.0022, inertia=3.0, torque=0.18, damping=0.55, notes="Tu-142 maritime patrol."),
    PlaneSpec("assets/mcheli/planes/tu160m.txt", "heavy_bomber", 2220, 260, 148000, 12300, 110.0, max_hp=600, comfortable_g=3.5, structural_g=5.5, critical_aoa=15.0, base_drag=0.0017, inertia=3.1, torque=0.18, damping=0.55, notes="Tu-160M."),
    PlaneSpec("assets/mcheli/planes/tu160mmsl.txt", "heavy_bomber", 2220, 260, 148000, 12300, 110.0, max_hp=600, comfortable_g=3.5, structural_g=5.5, critical_aoa=15.0, base_drag=0.0017, inertia=3.1, torque=0.18, damping=0.55, notes="Tu-160M missile loadout."),
    PlaneSpec("assets/mcheli/planes/c5.txt", "transport", 856, 205, 150815, 4440, 172.4, max_hp=650, comfortable_g=2.5, structural_g=4.0, critical_aoa=14.0, base_drag=0.0023, inertia=3.3, torque=0.16, damping=0.58, notes="C-5 Galaxy."),
    PlaneSpec("assets/mcheli/planes/il76ua.txt", "transport", 900, 220, 109500, 4400, 92.0, max_hp=540, comfortable_g=2.7, structural_g=4.5, critical_aoa=14.0, base_drag=0.0022, inertia=2.8, torque=0.18, damping=0.55, notes="Il-76 class."),
    PlaneSpec("assets/mcheli/planes/e767.txt", "transport", 850, 210, 90770, 10370, 175.0, max_hp=620, comfortable_g=2.5, structural_g=4.0, critical_aoa=14.0, base_drag=0.0021, inertia=3.1, torque=0.17, damping=0.56, notes="E-767/Boeing 767 AWACS."),
    PlaneSpec("assets/mcheli/planes/skylark.txt", "uav", 92, 45, 3, 40, 0.006, max_hp=30, comfortable_g=2.5, structural_g=4.0, critical_aoa=14.0, base_drag=0.0045, induced_drag=0.0045, idle_drag=0.007, inertia=0.25, torque=0.42, damping=0.30, drone=True, notes="Skylark small UAV."),
    PlaneSpec("assets/mcheli/planes/geran2.txt", "uav", 185, 90, 50, 1800, 0.2, max_hp=40, comfortable_g=3.0, structural_g=5.0, critical_aoa=16.0, base_drag=0.0035, induced_drag=0.004, idle_drag=0.006, inertia=0.5, torque=0.32, damping=0.36, drone=True, notes="Geran-2/Shahed-136 loitering munition."),
    PlaneSpec("assets/mcheli/planes/mqm170.txt", "uav", 185, 90, 50, 1800, 0.2, max_hp=40, comfortable_g=3.0, structural_g=5.0, critical_aoa=16.0, base_drag=0.0035, induced_drag=0.004, idle_drag=0.006, inertia=0.5, torque=0.32, damping=0.36, drone=True, notes="Target drone class."),
    PlaneSpec("assets/mcheli/planes/mq-9.txt", "uav", 482, 100, 1800, 1900, 2.2, max_hp=120, comfortable_g=3.0, structural_g=5.5, critical_aoa=16.0, base_drag=0.003, induced_drag=0.0045, idle_drag=0.006, inertia=0.8, torque=0.30, damping=0.38, drone=True, notes="MQ-9 Reaper."),
    PlaneSpec("assets/mcheli/planes/x-47b.txt", "uav", 1100, 210, 6500, 3900, 20.2, max_hp=240, comfortable_g=6.0, structural_g=8.0, critical_aoa=18.0, base_drag=0.0019, inertia=1.4, torque=0.30, damping=0.42, drone=True, notes="X-47B UCAV."),
]


def apply_spec(path: Path, spec: PlaneSpec) -> Tuple[bool, str, str]:
    old = path.read_text(encoding="utf-8-sig", errors="replace")
    new = old

    speed = scaled_speed(spec.top_speed_kph)
    max_fuel, fuel_consumption = fuel_values(spec.fuel_liters, spec.range_km)
    hp = spec.max_hp if spec.max_hp is not None else hp_from_mass(spec.mass_tonnes, spec.role, spec.drone)

    # Basic vehicle values.
    new = insert_or_replace(new, "Speed", speed, "MaxHp")
    if hp is not None:
        new = insert_or_replace(new, "MaxHp", hp, "DisplayName")
    if max_fuel is not None:
        new = insert_or_replace(new, "MaxFuel", max_fuel, "MotionFactor")
    if fuel_consumption is not None:
        new = insert_or_replace(new, "FuelConsumption", fuel_consumption, "MaxFuel")

    # Realistic fixed-wing model. These keys are parsed only when enabled.
    new = insert_or_replace(new, "EnableRealisticFlightModel", True, "Category")
    new = insert_or_replace(new, "MaxLevelSpeed", speed, "EnableRealisticFlightModel")
    new = insert_or_replace(new, "StallSpeedFactor", stall_factor(spec), "MaxLevelSpeed")
    if spec.stall_kph:
        new = insert_or_replace(new, "StallSpeed", scaled_speed(spec.stall_kph), "StallSpeedFactor")
    new = insert_or_replace(new, "CriticalAoA", spec.critical_aoa, "StallSpeed")
    new = insert_or_replace(new, "StallLiftLoss", 0.70 if not spec.drone else 0.60, "CriticalAoA")
    new = insert_or_replace(new, "AoADragMultiplier", 1.65 if not spec.drone else 1.35, "StallLiftLoss")
    new = insert_or_replace(new, "StallInstability", 0.38 if not spec.drone else 0.18, "AoADragMultiplier")
    new = insert_or_replace(new, "BaseDrag", spec.base_drag, "StallInstability")
    new = insert_or_replace(new, "InducedDrag", spec.induced_drag, "BaseDrag")
    new = insert_or_replace(new, "ControlSurfaceDrag", spec.control_surface_drag, "InducedDrag")
    new = insert_or_replace(new, "ClimbEnergyLoss", spec.climb_loss, "ControlSurfaceDrag")
    new = insert_or_replace(new, "DiveEnergyGain", spec.dive_gain, "ClimbEnergyLoss")
    new = insert_or_replace(new, "IdleDrag", spec.idle_drag, "DiveEnergyGain")
    new = insert_or_replace(new, "DiveSpeedMultiplier", spec.dive_multiplier, "IdleDrag")
    new = insert_or_replace(new, "MaxComfortableG", spec.comfortable_g, "DiveSpeedMultiplier")
    new = insert_or_replace(new, "MaxStructuralG", spec.structural_g, "MaxComfortableG")
    new = insert_or_replace(new, "GControlPenalty", 0.70 if not spec.drone else 0.45, "MaxStructuralG")
    new = insert_or_replace(new, "CompressibilitySpeed", round(speed * 0.88, 3), "GControlPenalty")
    new = insert_or_replace(new, "CompressibilityPitchPenalty", 0.60 if spec.top_speed_kph > 900 else 0.35, "CompressibilitySpeed")
    new = insert_or_replace(new, "MaxSafeSpeed", round(speed * 1.12, 3), "CompressibilityPitchPenalty")
    new = insert_or_replace(new, "OverspeedDamageRate", 0.15 if not spec.drone else 0.05, "MaxSafeSpeed")

    # Angular response: heavy aircraft turn slowly; fighters stay crisp.
    new = insert_or_replace(new, "PitchTorque", spec.torque, "OverspeedDamageRate")
    new = insert_or_replace(new, "RollTorque", round(spec.torque * (1.15 if spec.role == "fighter" else 1.0), 3), "PitchTorque")
    new = insert_or_replace(new, "YawTorque", round(spec.torque * 0.75, 3), "RollTorque")
    new = insert_or_replace(new, "PitchDamping", spec.damping, "YawTorque")
    new = insert_or_replace(new, "RollDamping", round(spec.damping * 0.9, 3), "PitchDamping")
    new = insert_or_replace(new, "YawDamping", round(spec.damping * 1.1, 3), "RollDamping")
    new = insert_or_replace(new, "InertiaMultiplier", spec.inertia, "YawDamping")
    new = insert_or_replace(new, "ThrottleAcceleration", spec.throttle_accel, "InertiaMultiplier")
    new = insert_or_replace(new, "EngineDrag", spec.engine_drag, "ThrottleAcceleration")

    if spec.vtol:
        new = insert_or_replace(new, "EnableVtol", True, "EngineDrag")
        new = insert_or_replace(new, "DefaultVtol", False, "EnableVtol")
        new = insert_or_replace(new, "VtolYaw", 0.30, "DefaultVtol")
        new = insert_or_replace(new, "VtolPitch", 0.22, "VtolYaw")

    for key, value in spec.extra.items():
        new = insert_or_replace(new, key, value, "EngineDrag")

    marker = "; RealismSource = MCHO plane scripted pass"
    if marker not in new:
        new = new.rstrip() + f"\n\n{marker}; {spec.notes}\n"

    return old != new, old, new


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--apply", action="store_true", help="Write changes")
    parser.add_argument("--dry-run", action="store_true", help="Print diffs")
    args = parser.parse_args()

    repo = Path(args.root)
    changed = 0
    missing: List[str] = []

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
        print(f"Missing mapped plane files: {len(missing)}")
        for item in missing[:50]:
            print(f"  - {item}")
        if len(missing) > 50:
            print("  ...")
    if not args.apply:
        print("Dry run only. Re-run with --apply to write changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
