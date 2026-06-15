# New-flight plane stall retune - 2026-06-15

This pass covers the 125 plane configs that explicitly opt into `UseNewMobilitySystem = true`. A case-insensitive audit found no plane config with clear new-flight-model values missing the opt-in flag after this pass.

## Class-wide tuning conventions

- WW2/light props retain low stall speeds and responsive handling, but use stronger AoA drag, higher lift loss, larger recovery margins, and higher stall strength so hard pull/high-nose abuse bleeds energy and produces a visible break.
- Heavy fighters, attackers, drones, and utility aircraft are tuned with lower critical AoA, stronger lift loss, more control/induced drag, and higher climb energy loss than light fighters.
- Bombers and transports use the harshest conventional fixed-wing stall behavior: lower critical AoA, high lift loss, high AoA/turn drag, slower recovery, substantially lower low-throttle lift retention, and stronger G-control penalties.
- Early jets and high-speed interceptors now punish low-speed/high-AoA climbing harder than props through lower critical AoA, higher recovery speeds, stronger sink/pitch-break strength, and increased climb/turn drag.
- Modern jets retain better AoA tolerance than older jets, but no longer use high thrust, flap lift, low AoA drag, or weak stall strength to bypass the stall model. Thrust-to-mass ratios were capped where they made normal fixed-wing aircraft effectively vertical-climb capable.
- VTOL/nozzle-capable aircraft keep their VTOL identity separate; their conventional fixed-wing tuning no longer uses fixed-wing thrust or lift retention to fake hover behavior; VTOL-capable fixed-wing retention is now the lowest class band.

## Changed config set

All files under `assets/mcheli/planes/` with `UseNewMobilitySystem = true` were retuned. The changed set includes light props, attackers, drones, early jets, modern fighters, VTOL-capable aircraft, bombers, transports, and strategic/supersonic aircraft.

## Low-throttle lift-retention follow-up

A follow-up pass lowered `NewFlightLowThrottleLiftRetention` on every new-flight plane from the previous high bands into aggressive stall-visible bands: `0.520` for VTOL/nozzle-capable aircraft, `0.560` for jets/interceptors, `0.580` for attackers/drones, `0.600` for light props, and `0.620` for bombers/transports. This keeps throttle chop, high-AoA pull, and low-speed climb abuse from retaining enough asset-side lift to bypass stall sink and pitch break.

## Takeoff thrust follow-up

A takeoff-focused follow-up restored minimum thrust-to-mass headroom for heavy planes and attack craft after the retention reductions: conventional bombers/transports now target at least `0.85`, supersonic heavy bombers at least `0.90`, attack aircraft at least `1.02`, and small attack drones at least `0.95`. These floors are intended to preserve runway takeoff and loaded attack-aircraft usability while keeping heavy aircraft below fixed-wing vertical-climb thrust-to-weight.

## Human flight-feel review notes

No gameplay/manual verification was performed. Aircraft that should receive focused human feel review are the edge cases where identity depends on high performance or alternate lift modes: Harrier/Yak-38/F-35B/MV-22 VTOL behavior, F-22/Su-57/F-15S MTD high-AoA behavior, SR-71/MiG-25/MiG-31 high-speed interceptor energy bleed, and B-1/B-2/Tu-160 heavy high-speed bomber climb behavior.

## Intentionally unchanged configs

Legacy plane configs without `UseNewMobilitySystem = true` were left unchanged. Non-plane assets and unrelated vehicle, weapon, HUD, texture, recipe, seat, and visual-part values were not modified.
