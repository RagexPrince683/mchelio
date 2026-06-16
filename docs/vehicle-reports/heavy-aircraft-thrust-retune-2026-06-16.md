# Heavy aircraft thrust retune (2026-06-16)

This pass fixes heavy new-flight aircraft that could fail to lift off because their configured `EngineThrust` was numerically lower than `PhysicalMass`, leaving too little forward acceleration after drag, ground roll, and lift-to-weight checks.

## Scaling method

- Kept the existing `PhysicalMass` values as the scaled real-life weight class anchor.
- Recomputed heavy-aircraft `EngineThrust` as a role-scaled multiple of physical mass so every affected heavy airframe has thrust greater than mass.
- Used conservative scaled ratios by real-world aircraft role instead of fighter-like values: large airliners/cargo aircraft at about 1.05-1.08, heavy turboprops and gunships at about 1.08-1.10, strategic bombers at about 1.10-1.12, and supersonic bombers at about 1.16-1.18.
- Preserved heavy-aircraft identity by leaving mass, stall, drag, inertia, and takeoff-distance values unchanged; the change only restores enough engine force for practical takeoff and climb in Minecraft-scale runways.

## Aircraft updated

Updated A400M, AC-130, B-1 variants, B-2 variants, B-29 variants, B-52 variants, C-5 variants, E-767, H6K, Il-76, MC-130 variants, MD-90, MV-22, Tu-4 variants, Tu-22M3, Tu-95/Tu-142 variants, Tu-160 variants, and Victor B.2.

## Validation notes

After this change, the affected heavy aircraft all have `EngineThrust > PhysicalMass`. Use `DebugFlightControl` to confirm takeoff roll, `netForward`, thrust-to-weight, lift-to-weight, and climb behavior in-game without changing stall or takeoff-distance multipliers.
