#!/usr/bin/env python3
"""Apply seeker- and era-aware guidance values to every AAMissile definition.

Ranges are gameplay-compressed blocks (roughly metres), while guidance lives are
20 Hz ticks.  Public performance figures identify relative capability; exact
classified seeker behavior is intentionally represented by conservative bands.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WEAPONS = ROOT / "assets" / "mcheli" / "weapons"

@dataclass(frozen=True)
class Profile:
    range: int
    countermeasure_ticks: int
    active_radar: bool
    scan_ticks: int
    locks_missiles: bool
    bvr: bool
    heat: bool
    radar: bool
    homing_ticks: int
    turn_limit: int

# The engine's range is in blocks and cannot use literal 100+ km engagement
# ranges sensibly. These bands preserve real-world ordering at about 1:100.
IR_EARLY = Profile(80, 0, False, 8, False, False, True, False, 360, 32)
IR_REAR = Profile(120, 4, False, 6, False, False, True, False, 440, 42)
IR_ALL = Profile(180, 10, False, 4, False, False, True, False, 520, 58)
IR_IRCCM = Profile(240, 24, False, 2, False, False, True, False, 640, 82)
IR_HOBS = Profile(280, 36, False, 1, False, False, True, False, 700, 100)
MANPADS = Profile(100, 18, False, 4, False, False, True, False, 420, 55)
SARH_EARLY = Profile(240, 3, False, 8, False, True, False, True, 700, 32)
SARH = Profile(450, 8, False, 5, False, True, False, True, 1000, 45)
SARH_LONG = Profile(650, 12, False, 4, False, True, False, True, 1400, 42)
ARH = Profile(800, 18, True, 3, False, True, False, True, 1500, 58)
ARH_MODERN = Profile(1050, 28, True, 2, False, True, False, True, 1800, 65)
DUAL_ARH = Profile(750, 30, True, 2, False, True, True, True, 1400, 68)
SAM_COMMAND = Profile(300, 4, False, 6, False, True, False, False, 900, 46)
SAM_IR = Profile(150, 20, False, 3, False, False, True, False, 520, 62)
SAM_RADAR = Profile(600, 14, False, 4, False, True, False, True, 1400, 48)
SAM_ARH = Profile(950, 24, True, 2, True, True, False, True, 1900, 58)
POINT_DEFENSE = Profile(260, 28, True, 1, True, False, True, True, 700, 78)
ABM = Profile(1400, 36, True, 1, True, True, False, True, 2600, 28)


def profile_for(name: str, display: str) -> Profile:
    key = f"{name} {display}".lower()
    # Exo-atmospheric/strategic interceptors and modern naval area defense.
    if any(x in key for x in ("77h6h", "77n6", "rim-161", "sm-3", "sm3")):
        return ABM
    if any(x in key for x in ("sm-6", "rim-174", "mim-104", "patriot", "sm-2er", "rim-156")):
        return SAM_ARH
    if any(x in key for x in ("ram116", "rim-116", "searam", "essm", "rim-162")):
        return POINT_DEFENSE
    # Active-radar air-to-air families.
    if "mica ir" in key or "micair" in key:
        return IR_HOBS
    if any(x in key for x in ("meteor", "r77m", "r-77m", "aam-4")):
        return ARH_MODERN
    if any(x in key for x in ("aim120", "amraam", "pl-12", "r-77", "r77-1", "r27ae", "r-27ae")):
        return ARH
    if "mica" in key:
        return DUAL_ARH
    if any(x in key for x in ("aim54", "phoenix")):
        return ARH_MODERN
    # Semi-active radar AAMs.
    if any(x in key for x in ("r33", "r-33", "r24", "r-24", "r27", "r-27", "r-40")):
        return SARH_LONG
    if any(x in key for x in ("aim7", "sparrow", "r530", "r.530")):
        return SARH
    if any(x in key for x in ("k5", "k-5", "alkali")):
        return SARH_EARLY
    # Ground/naval systems. Command-guided weapons are deliberately neither IR
    # nor radar seekers even when their launcher uses tracking radar.
    if any(x in key for x in ("sa-2", "guideline", "3m9", "hawk", "rim-66", "sm-2", "dggsm2", "arlsm2", "rim-24", "sa8", "9m33")):
        return SAM_RADAR
    if any(x in key for x in ("57e6", "9m311", "vt-1", "roland", "9m113", "hy-6", "mim-146")):
        return SAM_COMMAND
    if any(x in key for x in ("stinger", "aim92", "fim92", "igla", "9k38", "grom", "qw-2", "type 91", "sam2", "ty-90")):
        return SAM_IR
    # Imaging-IR/high-off-boresight dogfight missiles.
    if any(x in key for x in ("aim-9x", "aim9x", "iris-t", "asraam", "aam-5", "r-73m2")):
        return IR_HOBS
    if any(x in key for x in ("r-73", "r73", "pl-9")):
        return IR_IRCCM
    if any(x in key for x in ("aim-9m", "aim9_m", "aim9m", "magic ii", "r550_2", "pl-8")):
        return IR_IRCCM
    if any(x in key for x in ("aim-9l", "aim9_l", "aim9l", "r-60m", "r60m")):
        return IR_ALL
    if any(x in key for x in ("r-60", "r60", "magic", "r550")):
        return IR_ALL
    if any(x in key for x in ("aim-9b", "aim9b", "aim-9e", "aim9e", "k-13", "r-3", "r3s", "pl-2")):
        return IR_EARLY
    if "sidewinder" in key or "aim9" in key:
        return IR_REAR
    raise ValueError(f"No realism profile for {name}: {display}")

FIELDS = (
    "MaxLockOnRange", "AntiFlareCount", "ActiveRadar", "ScanInterval",
    "CanLockMissile", "EnableBVR", "IsHeatSeekerMissile", "IsRadarMissile",
    "TickEndHoming", "MaxDegreeOfMissile",
)

def bool_text(value: bool) -> str:
    return str(value).lower()

def update(path: Path) -> None:
    text = path.read_text(encoding="latin-1")
    if not re.search(r"(?im)^\s*Type\s*=\s*AAMissile\s*$", text):
        return
    display_match = re.search(r"(?im)^\s*DisplayName\s*=\s*(.+)$", text)
    display = display_match.group(1).strip() if display_match else path.stem
    p = profile_for(path.name, display)
    values = {
        "MaxLockOnRange": str(p.range),
        "AntiFlareCount": str(p.countermeasure_ticks),
        "ActiveRadar": bool_text(p.active_radar),
        "ScanInterval": str(p.scan_ticks),
        "CanLockMissile": bool_text(p.locks_missiles),
        "EnableBVR": bool_text(p.bvr),
        "IsHeatSeekerMissile": bool_text(p.heat),
        "IsRadarMissile": bool_text(p.radar),
        "TickEndHoming": str(p.homing_ticks),
        "MaxDegreeOfMissile": str(p.turn_limit),
    }
    lines = text.splitlines()
    filtered = []
    field_names = {field.lower() for field in FIELDS}
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(";") or "=" not in stripped:
            filtered.append(line)
            continue
        if stripped.split("=", 1)[0].strip().lower() not in field_names:
            filtered.append(line)
    insert_at = next(i for i, line in enumerate(filtered) if re.match(r"(?i)^\s*SpeedDependsAircraft\s*=", line))
    tuning = [f"{field} = {values[field]}" for field in FIELDS]
    filtered[insert_at:insert_at] = tuning
    path.write_text("\n".join(filtered) + "\n", encoding="latin-1")


def main() -> None:
    paths = sorted(WEAPONS.glob("*.txt"))
    aam = [p for p in paths if re.search(r"(?im)^\s*Type\s*=\s*AAMissile\s*$", p.read_text(encoding="latin-1"))]
    for path in aam:
        update(path)
    print(f"Updated {len(aam)} AAMissile definitions")

if __name__ == "__main__":
    main()
