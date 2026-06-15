# New-flight-model gravity rebalance (2026-06-15)

This pass retunes every aircraft config that explicitly opts into `UseNewMobilitySystem = true` after the fixed-wing model began applying real downward gravity. Legacy planes without the new mobility flag were not changed.

## Documentation referenced

- `docs/vehicle-config/planes.md` for new-flight throttle, gravity, stall, drag, energy, G-force, compressibility, overspeed, and combat-flap formulas.
- `docs/vehicle-config/base.md` for shared gravity, speed, mobility, and ceiling key meanings.
- `docs/code-docs/vehicle-config-reference.md` for the config key reference and documented per-aircraft gravity aliases.

## Edited aircraft

- `a-10.txt`
- `a4.txt`
- `a400m.txt`
- `a6.txt`
- `a6m2.txt`
- `a6m2n.txt`
- `a7.txt`
- `ac-130.txt`
- `ac-47.txt`
- `an2.txt`
- `au23.txt`
- `b-1.txt`
- `b-1nuclear.txt`
- `b-2a.txt`
- `b-2a2.txt`
- `b-2a3.txt`
- `b-2a4.txt`
- `b29.txt`
- `b29sp.txt`
- `b52.txt`
- `b52d.txt`
- `b52n.txt`
- `bayraktar tb 2.txt`
- `bf109.txt`
- `bqm_74e.txt`
- `bv138.txt`
- `c-47.txt`
- `c5.txt`
- `c5m.txt`
- `e767.txt`
- `emb314.txt`
- `eurofighter_typhoon_2.txt`
- `eurofighter_typhoon_2_t.txt`
- `f-104.txt`
- `f-15e.txt`
- `f-15s_mtd.txt`
- `f-35a.txt`
- `f-35b.txt`
- `f-35c.txt`
- `f-5e.txt`
- `f-80.txt`
- `f-86f.txt`
- `f117.txt`
- `f117gbu27.txt`
- `f117nuc.txt`
- `f14.txt`
- `f14d.txt`
- `f16c.txt`
- `f1m.txt`
- `f22a.txt`
- `f4a.txt`
- `f8f.txt`
- `fa18e.txt`
- `fa18fold.txt`
- `fa50.txt`
- `geran2.txt`
- `h6k.txt`
- `h8k.txt`
- `harrier.txt`
- `harrier_en.txt`
- `il28sh.txt`
- `il76ua.txt`
- `j11b.txt`
- `j15.txt`
- `j8.txt`
- `jas39.txt`
- `ju87.txt`
- `kf-21.txt`
- `m2000-5.txt`
- `m2000c.txt`
- `mc130.txt`
- `mc130j.txt`
- `md90.txt`
- `mig-15.txt`
- `mig-19s.txt`
- `mig-21pf.txt`
- `mig17f.txt`
- `mig21.txt`
- `mig23.txt`
- `mig25.txt`
- `mig29.txt`
- `mig3.txt`
- `mig31.txt`
- `mig31k.txt`
- `mirage3e.txt`
- `mirageiv.txt`
- `mq-9.txt`
- `mqm170.txt`
- `mv-22.txt`
- `n1k1.txt`
- `ov-10a.txt`
- `p-51d.txt`
- `pzl-m18.txt`
- `q-5d.txt`
- `qf-80.txt`
- `rafalem.txt`
- `skylark.txt`
- `spitfire-mkvb.txt`
- `sr71.txt`
- `su-33.txt`
- `su24.txt`
- `su25.txt`
- `su27bru.txt`
- `su34.txt`
- `su34b.txt`
- `su34n.txt`
- `su37.txt`
- `su57.txt`
- `tornado-gr4.txt`
- `tornado-ids.txt`
- `tu142real.txt`
- `tu160m.txt`
- `tu160mmsl.txt`
- `tu22m3.txt`
- `tu4.txt`
- `tu4light.txt`
- `tu95k22.txt`
- `tu95ms.txt`
- `tu95org.txt`
- `victor_b2.txt`
- `x-47b.txt`
- `yak38.txt`
- `yak38_r60.txt`
- `yak38_upk.txt`
- `yak38_x23.txt`

## Gravity balance approach

- Kept global new-flight gravity meaningful and avoided using a blanket low-gravity workaround.
- Added or normalized per-aircraft `NewFlightGravity` only by role: standard fighters and most jets use the documented global baseline, heavy bombers/transports use slightly stronger gravity to preserve weight, and very light drones/special aircraft use small justified deviations.
- Recomputed stall and recovery speeds so `StallRecoverySpeed` is consistently above `StallSpeed`, preventing aircraft from recovering while still below the stall threshold.
- Tuned drag and energy exchange by role so climbing costs speed, diving restores energy, and low-energy aircraft naturally descend under gravity.
- Retuned throttle response, idle power, low-throttle lift retention, and throttle-based authority penalties within documented ranges to avoid the old floaty behavior while preserving landings and approaches.
- Preserved combat-flap enablement choices already present in configs and normalized flap lift, drag, control, and overspeed penalties by role.

## Role targets

- WW2 and utility props: stronger low-speed handling, higher induced/AoA drag, moderate gravity baseline, and earlier stalls/recovery to support dogfighting without hovering.
- Heavy bombers/transports: stronger gravity, higher drag/load penalties, lower G limits, slower throttle response, and longer recovery margins to feel heavy.
- Early jets: better energy retention than props, higher speed limits, less turn authority at high speed, and more compressibility penalty than modern fighters.
- Modern jets: strong high-speed energy, improved high-speed authority, lower drag, and high but bounded G/overspeed margins.
- Attack/special aircraft: assigned by doctrine, with strike aircraft between fighters and bombers and SR-71/drone-style aircraft tuned for stability and energy rather than turn performance.

## Analytical validation

Validation was limited to documentation compliance, formula review, config consistency, and outlier checks; no gameplay testing was available. Checks verified that all edited files remain opted into the new mobility system, contain no duplicate managed keys, use documented key names only for the normalized flight block, keep `StallRecoverySpeed > StallSpeed`, keep `MaxSafeSpeed > CompressibilitySpeed`, and keep numeric values inside documented ranges.

## Future in-game validation priorities

- Heavy bombers and transports (`b-1*`, `b-2a*`, `b52*`, `c5*`, `tu95*`, `tu160*`) need climb-rate, takeoff, and landing validation because their stronger gravity and drag changes should feel heavy without becoming unflyable.
- VTOL/special aircraft (`harrier*`, `yak38*`, `mv-22.txt`, `f-35b.txt`) need transition and approach testing because fixed-wing gravity tuning cannot validate nozzle-mode behavior.
- Very fast aircraft (`sr71.txt`, `mig31*.txt`, modern fighters) need overspeed/compressibility testing at altitude.
- Small drones and loitering munitions (`skylark.txt`, `geran2.txt`, `bayraktar tb 2.txt`, `mq-9.txt`) need low-speed descent and recovery validation.

## Undocumented values and assumptions

No new undocumented keys were introduced. The documentation does not expose an explicit standalone wing-lift coefficient; lift balance is therefore performed through documented gravity, throttle/lift-retention, stall, drag, ceiling, and control-authority values. `TakeoffSpeed` and explicit climb-rate keys were not documented in the plane config reference, so takeoff and climb behavior were tuned indirectly through stall speed, thrust/throttle response, drag, climb energy loss, and gravity.
