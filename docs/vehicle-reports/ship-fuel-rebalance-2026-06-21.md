# Ship fuel rebalance (2026-06-21)

Scope: audited every ship config in `assets/mcheli/ships` and retuned `MaxFuel` plus `FuelConsumption` without modifying any class files.

## Method

- `MaxFuel` now tracks a realistic onboard fuel-capacity scale for the vessel class where conventional fuel is relevant.
- `FuelConsumption` is calculated as `MaxFuel / enduranceSeconds`, matching the documented MCHeli convention that flight or run time in seconds is `MaxFuel / FuelConsumption`.
- Small craft use gasoline/diesel tank-size approximations and multi-hour endurance; large combatants use bunker-fuel scale capacities with multi-day endurance so they no longer drain like short-range boats.
- Nuclear-powered vessels use a very large reactor-equivalent cap and zero configured fuel drain, representing propulsion endurance that is not meaningfully limited by ordinary fuel items in gameplay.

## Updated values

| Config | Vessel | MaxFuel | FuelConsumption | Intended endurance |
| --- | --- | ---: | ---: | --- |
| `zodiac.txt` | Small Zodiac Boat | 6 | 0.001 | ~1.7 h |
| `rhib.txt` | NSW 11-meter RHIB | 250 | 0.009 | ~7.7 h |
| `rhib_hmg.txt` | NSW 11-meter RHIB HMG | 250 | 0.009 | ~7.7 h |
| `lcvp.txt` | LCVP | 150 | 0.017 | ~2.5 h |
| `stinger_390x.txt` | Chris Craft Stinger 390x | 300 | 0.021 | ~4.0 h |
| `cb90.txt` | CB90 Combat Boat | 660 | 0.023 | ~8.0 h |
| `mark5.txt` | Mk.5 Special Operations Craft | 2600 | 0.060 | ~12.0 h |
| `project1204.txt` | Project 1204 Shmel Patrol Boat | 3000 | 0.028 | ~29.8 h |
| `lcac.txt` | LCAC | 5000 | 0.278 | ~5.0 h |
| `hsv-x1.txt` | HSV-X1 Joint Venture | 250000 | 3.472 | ~20.0 h |
| `arleigh.txt` | DDG-51 Arleigh Burke Destroyer | 1000000 | 0.579 | ~20.0 d |
| `dgg1000_zumwalt.txt` | DDG-1000 Zumwalt Destroyer | 1000000 | 0.579 | ~20.0 d |
| `mc-aircraft_carrier.txt` | CVN-68 Nimitz Aircraft Carrier | 100000000 | 0.000 | Nuclear/no ordinary drain |
| `project941.txt` | Project 941UM Dmitry Donskoy | 100000000 | 0.000 | Nuclear/no ordinary drain |
| `project941og.txt` | Project 941 Akula | 100000000 | 0.000 | Nuclear/no ordinary drain |

## Gameplay impact

- Boats now separate by mission profile: inflatables and landing craft have limited patrol time, while RHIBs, CB90s, and special-operations craft can operate for longer periods.
- Destroyers and high-speed sealift no longer share the same small fuel-cap range as boats.
- Nuclear carrier and submarine configs remain effectively fuel-independent without relying on class-code changes.
