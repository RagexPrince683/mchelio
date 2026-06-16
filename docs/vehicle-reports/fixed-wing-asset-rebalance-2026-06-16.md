# Fixed-wing new-flight asset rebalance (2026-06-16)

Reference: this pass used `docs/vehicle-config/planes.md`, especially the current new-flight formulas for throttle response, AoA/stall recovery, drag/energy exchange, physical mass/thrust, takeoff distance multiplier, and combat flaps.

Scope: audited all 125 plane configs that explicitly set `UseNewMobilitySystem = true`. Legacy aircraft that do not opt in were not modified.

## Global tuning themes

- Added explicit `TakeoffDistanceMultiplier` to every new-flight plane so runway behavior is tuned directly instead of hiding takeoff problems in stall speed, thrust, or lift values.
- Re-centered thrust-to-weight by role: WW2 fighters and modern fighters recover energy faster, attackers remain workmanlike, and bombers/transports retain heavy acceleration and climb behavior.
- Rebalanced stalls around the corrected aerodynamic model. WW2 fighters now have stronger buffet and pitch-break recovery, heavy aircraft use lower instability and gentler lift loss, and jets punish low-speed/high-AoA abuse without making normal high-speed maneuvering feel unstable.
- Normalized drag and energy values by role so hard turns cost energy, climbs bleed speed, dives restore energy, and high-performance jets retain energy better than lower-performance props or heavy aircraft.
- Reworked throttle response by era: prop aircraft respond quickly, early jets spool slower, modern jets retain strong but manageable throttle response, and heavy aircraft no longer carry excessive idle acceleration.
- Reviewed combat flaps on all enabled aircraft, increasing low-speed tactical value while raising drag and lowering overspeed thresholds enough to discourage high-speed abuse.
- Nudged handling slightly snappier for fighters and jets while reducing bomber/transport mobility so role separation is clearer.

## Aircraft requiring significant retuning

- WW2 and prop fighters: A6M2, A6M2-N, Bf 109, F1M, F8F, Ju 87, MiG-3, N1K1, P-51D, and Spitfire Mk.Vb.
- Early jets and early attack jets: A-4, A-6, A-7, F-80/QF-80, F-86F, F-104, F-5E, F-4A, Il-28Sh, J-8, MiG-15/17/19/21/23/25, Mirage IIIE, Q-5D, and Yak-38 variants.
- Modern fighters and fighter-bombers: Eurofighter, F-15E/F-15S MTD, F-35 variants, F-14 variants, F-16C, F/A-18E variants, FA-50, F-22A, J-11B/J-15, JAS 39, KF-21, Mirage 2000 variants, MiG-29/MiG-31 variants, Rafale M, Su-27/Su-33/Su-34/Su-35/Su-57, Tornado variants, and X-47B.
- Heavy aircraft: B-1, B-2, B-29/Tu-4, B-52, C-5, A400M, C-47/AC-47, AC-130/MC-130, E-767, H6K/H8K, Il-76, MD-90, Mirage IV, Tu-22M3, Tu-95/Tu-142, Tu-160, Victor B.2, and related payload variants.
- Low-speed utility/UAV/special aircraft: An-2, AU-23A, Bayraktar TB2, EMB 314, Geran-2, MQ-9, MQM-170, OV-10A, PZL M18, Skylark, BQM-74E, and SR-71.

## Aircraft requiring only minor adjustments

These aircraft were already close to the intended new-flight envelope and primarily received consistency tuning, takeoff multiplier coverage, throttle/drag normalization, or small handling/stall refinements:

- F-22A, Su-57, Eurofighter Typhoon loadouts, Rafale M, JAS 39, KF-21, F-16C, and F-35 variants.
- B-52H/D loadouts, Tu-95/Tu-142 variants, C-5/C-5M, A400M, E-767, and MC-130/MC-130J.
- P-51D, Spitfire Mk.Vb, Bf 109, A6M2, and F8F.
- SR-71, BQM-74E, MQM-170, Bayraktar TB2, Skylark, and Geran-2.

## Notes for future validation

Use `DebugFlightControl` logging from the current flight model to validate takeoff roll, `netForward`, effective takeoff threshold, lift-to-weight, thrust-to-weight, stall demand, stall severity, drag, and combat-flap state in representative runway, climb, turn, stall, and dive tests.
