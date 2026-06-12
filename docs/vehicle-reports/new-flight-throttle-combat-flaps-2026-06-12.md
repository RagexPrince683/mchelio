# New flight-model throttle and combat-flap configuration report

Date: 2026-06-12

## Scope and source documentation

- Reviewed `docs/vehicle-config/planes.md`, especially the new-flight throttle keys, combat-flap keys, and the `useNewMobilitySystem = true` gate.
- Reviewed all `assets/mcheli/planes/*.txt` aircraft configs and only modified aircraft already opted into the new mobility/flight model.
- Moved historical vehicle reports out of `docs/vehicle-config/` into this `docs/vehicle-reports/` folder so config documentation and audit reports are separated.

## New-flight-model aircraft identified

Total new-flight-model aircraft: **125**. Identification criterion: `UseNewMobilitySystem = true`.

- `a-10.txt`, `a4.txt`, `a400m.txt`, `a6.txt`, `a6m2.txt`
- `a6m2n.txt`, `a7.txt`, `ac-130.txt`, `ac-47.txt`, `an2.txt`
- `au23.txt`, `b-1.txt`, `b-1nuclear.txt`, `b-2a.txt`, `b-2a2.txt`
- `b-2a3.txt`, `b-2a4.txt`, `b29.txt`, `b29sp.txt`, `b52.txt`
- `b52d.txt`, `b52n.txt`, `bayraktar tb 2.txt`, `bf109.txt`, `bqm_74e.txt`
- `bv138.txt`, `c-47.txt`, `c5.txt`, `c5m.txt`, `e767.txt`
- `emb314.txt`, `eurofighter_typhoon_2.txt`, `eurofighter_typhoon_2_t.txt`, `f-104.txt`, `f-15e.txt`
- `f-15s_mtd.txt`, `f-35a.txt`, `f-35b.txt`, `f-35c.txt`, `f-5e.txt`
- `f-80.txt`, `f-86f.txt`, `f117.txt`, `f117gbu27.txt`, `f117nuc.txt`
- `f14.txt`, `f14d.txt`, `f16c.txt`, `f1m.txt`, `f22a.txt`
- `f4a.txt`, `f8f.txt`, `fa18e.txt`, `fa18fold.txt`, `fa50.txt`
- `geran2.txt`, `h6k.txt`, `h8k.txt`, `harrier.txt`, `harrier_en.txt`
- `il28sh.txt`, `il76ua.txt`, `j11b.txt`, `j15.txt`, `j8.txt`
- `jas39.txt`, `ju87.txt`, `kf-21.txt`, `m2000-5.txt`, `m2000c.txt`
- `mc130.txt`, `mc130j.txt`, `md90.txt`, `mig-15.txt`, `mig-19s.txt`
- `mig-21pf.txt`, `mig17f.txt`, `mig21.txt`, `mig23.txt`, `mig25.txt`
- `mig29.txt`, `mig3.txt`, `mig31.txt`, `mig31k.txt`, `mirage3e.txt`
- `mirageiv.txt`, `mq-9.txt`, `mqm170.txt`, `mv-22.txt`, `n1k1.txt`
- `ov-10a.txt`, `p-51d.txt`, `pzl-m18.txt`, `q-5d.txt`, `qf-80.txt`
- `rafalem.txt`, `skylark.txt`, `spitfire-mkvb.txt`, `sr71.txt`, `su-33.txt`
- `su24.txt`, `su25.txt`, `su27bru.txt`, `su34.txt`, `su34b.txt`
- `su34n.txt`, `su37.txt`, `su57.txt`, `tornado-gr4.txt`, `tornado-ids.txt`
- `tu142real.txt`, `tu160m.txt`, `tu160mmsl.txt`, `tu22m3.txt`, `tu4.txt`
- `tu4light.txt`, `tu95k22.txt`, `tu95ms.txt`, `tu95org.txt`, `victor_b2.txt`
- `x-47b.txt`, `yak38.txt`, `yak38_r60.txt`, `yak38_upk.txt`, `yak38_x23.txt`

## Aircraft updated

Updated all **125** identified new-flight-model aircraft with the expanded throttle block:

- `NewFlightThrottleResponse`
- `NewFlightThrottleChangeRateUp` / `NewFlightThrottleChangeRateDown`
- `NewFlightIdleThrottle`
- `NewFlightEngineBrakeDrag`
- `NewFlightLowThrottleLiftRetention`
- `NewFlightThrottleControlAuthorityScale`
- `NewFlightThrottleHudDisplay`
- `NewFlightCombatFlaps` and, where enabled, lift/drag/control/overspeed values

Throttle values were tuned by role instead of copied globally: WW2 fighters received quick throttle travel and high partial-throttle lift retention; heavy bombers and transports received slower throttle travel, higher inertia-compatible authority penalties, and stable low-power behavior; early jets received slower spool-like response and weaker low-throttle lift; modern fighters received faster throttle response with high-speed energy management; STOL/utility aircraft received strong low-speed control and partial-throttle lift retention.

## Aircraft given combat flaps

Total with combat flaps: **65**.

- `a-10.txt`, `a4.txt`, `a6.txt`, `a6m2.txt`, `a6m2n.txt`
- `a7.txt`, `bf109.txt`, `eurofighter_typhoon_2.txt`, `eurofighter_typhoon_2_t.txt`, `f-15e.txt`
- `f-15s_mtd.txt`, `f-35a.txt`, `f-35b.txt`, `f-35c.txt`, `f-5e.txt`
- `f-80.txt`, `f-86f.txt`, `f14.txt`, `f14d.txt`, `f16c.txt`
- `f1m.txt`, `f22a.txt`, `f4a.txt`, `f8f.txt`, `fa18e.txt`
- `fa18fold.txt`, `fa50.txt`, `harrier.txt`, `harrier_en.txt`, `j11b.txt`
- `j15.txt`, `jas39.txt`, `ju87.txt`, `kf-21.txt`, `m2000-5.txt`
- `m2000c.txt`, `mig-15.txt`, `mig-19s.txt`, `mig-21pf.txt`, `mig17f.txt`
- `mig21.txt`, `mig23.txt`, `mig29.txt`, `mig3.txt`, `mirage3e.txt`
- `n1k1.txt`, `p-51d.txt`, `q-5d.txt`, `rafalem.txt`, `spitfire-mkvb.txt`
- `su-33.txt`, `su24.txt`, `su25.txt`, `su27bru.txt`, `su34.txt`
- `su34b.txt`, `su34n.txt`, `su37.txt`, `su57.txt`, `tornado-gr4.txt`
- `tornado-ids.txt`, `yak38.txt`, `yak38_r60.txt`, `yak38_upk.txt`, `yak38_x23.txt`

Combat-flap tuning groups:

- WW2 fighters/dive attack: higher low-speed lift and drag, lower overspeed multipliers to support dogfighting without allowing high-speed abuse.
- Carrier and cold-war fighters/attack jets: moderate lift/control help with meaningful drag and conservative overspeed limits.
- Modern fighters: smaller lift/control boosts and lighter drag, preserving high-speed energy while avoiding unrealistic turn-rate spikes.
- CAS/VTOL attack jets: moderate lift/control boost biased toward low-speed attack handling and approach turns.

## Aircraft intentionally not given combat flaps

Total without combat flaps: **60**.

- `a400m.txt` — transport, gunship, AWACS, or tilt-rotor; flap use should favor lift/approach rather than temporary turn-rate boosts.
- `ac-130.txt` — transport, gunship, AWACS, or tilt-rotor; flap use should favor lift/approach rather than temporary turn-rate boosts.
- `ac-47.txt` — transport, gunship, AWACS, or tilt-rotor; flap use should favor lift/approach rather than temporary turn-rate boosts.
- `an2.txt` — STOL, utility, trainer, or COIN prop; low-speed throttle/lift tuning was improved without adding unrealistic combat flaps.
- `au23.txt` — STOL, utility, trainer, or COIN prop; low-speed throttle/lift tuning was improved without adding unrealistic combat flaps.
- `b-1.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `b-1nuclear.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `b-2a.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `b-2a2.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `b-2a3.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `b-2a4.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `b29.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `b29sp.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `b52.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `b52d.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `b52n.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `bayraktar tb 2.txt` — UAV/target drone/one-way drone; no pilot combat-flap maneuvering system modeled.
- `bqm_74e.txt` — UAV/target drone/one-way drone; no pilot combat-flap maneuvering system modeled.
- `bv138.txt` — not selected after role/history review.
- `c-47.txt` — transport, gunship, AWACS, or tilt-rotor; flap use should favor lift/approach rather than temporary turn-rate boosts.
- `c5.txt` — transport, gunship, AWACS, or tilt-rotor; flap use should favor lift/approach rather than temporary turn-rate boosts.
- `c5m.txt` — transport, gunship, AWACS, or tilt-rotor; flap use should favor lift/approach rather than temporary turn-rate boosts.
- `e767.txt` — transport, gunship, AWACS, or tilt-rotor; flap use should favor lift/approach rather than temporary turn-rate boosts.
- `emb314.txt` — STOL, utility, trainer, or COIN prop; low-speed throttle/lift tuning was improved without adding unrealistic combat flaps.
- `f-104.txt` — high-speed interceptor/reconnaissance design where flap deployment in combat turns would be inappropriate or overspeed-prone.
- `f117.txt` — stealth attack aircraft; flap use not treated as a maneuvering combat-flap system.
- `f117gbu27.txt` — stealth attack aircraft; flap use not treated as a maneuvering combat-flap system.
- `f117nuc.txt` — stealth attack aircraft; flap use not treated as a maneuvering combat-flap system.
- `geran2.txt` — UAV/target drone/one-way drone; no pilot combat-flap maneuvering system modeled.
- `h6k.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `h8k.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `il28sh.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `il76ua.txt` — transport, gunship, AWACS, or tilt-rotor; flap use should favor lift/approach rather than temporary turn-rate boosts.
- `j8.txt` — high-speed interceptor/reconnaissance design where flap deployment in combat turns would be inappropriate or overspeed-prone.
- `mc130.txt` — transport, gunship, AWACS, or tilt-rotor; flap use should favor lift/approach rather than temporary turn-rate boosts.
- `mc130j.txt` — transport, gunship, AWACS, or tilt-rotor; flap use should favor lift/approach rather than temporary turn-rate boosts.
- `md90.txt` — transport, gunship, AWACS, or tilt-rotor; flap use should favor lift/approach rather than temporary turn-rate boosts.
- `mig25.txt` — high-speed interceptor/reconnaissance design where flap deployment in combat turns would be inappropriate or overspeed-prone.
- `mig31.txt` — high-speed interceptor/reconnaissance design where flap deployment in combat turns would be inappropriate or overspeed-prone.
- `mig31k.txt` — high-speed interceptor/reconnaissance design where flap deployment in combat turns would be inappropriate or overspeed-prone.
- `mirageiv.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `mq-9.txt` — UAV/target drone/one-way drone; no pilot combat-flap maneuvering system modeled.
- `mqm170.txt` — UAV/target drone/one-way drone; no pilot combat-flap maneuvering system modeled.
- `mv-22.txt` — transport, gunship, AWACS, or tilt-rotor; flap use should favor lift/approach rather than temporary turn-rate boosts.
- `ov-10a.txt` — STOL, utility, trainer, or COIN prop; low-speed throttle/lift tuning was improved without adding unrealistic combat flaps.
- `pzl-m18.txt` — STOL, utility, trainer, or COIN prop; low-speed throttle/lift tuning was improved without adding unrealistic combat flaps.
- `qf-80.txt` — UAV/target drone/one-way drone; no pilot combat-flap maneuvering system modeled.
- `skylark.txt` — UAV/target drone/one-way drone; no pilot combat-flap maneuvering system modeled.
- `sr71.txt` — high-speed interceptor/reconnaissance design where flap deployment in combat turns would be inappropriate or overspeed-prone.
- `tu142real.txt` — transport, gunship, AWACS, or tilt-rotor; flap use should favor lift/approach rather than temporary turn-rate boosts.
- `tu160m.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `tu160mmsl.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `tu22m3.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `tu4.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `tu4light.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `tu95k22.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `tu95ms.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `tu95org.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `victor_b2.txt` — heavy bomber/large patrol platform; flaps reserved for takeoff/landing stability, not maneuver combat.
- `x-47b.txt` — UAV/target drone/one-way drone; no pilot combat-flap maneuvering system modeled.

## Missing or suspicious configuration values discovered

- After this pass, every new-flight-model aircraft has flight ceiling, ceiling range, stall speed, maximum level speed, maximum safe speed, and the expanded new-flight throttle/combat-flap keys populated.
- `bqm_74e.txt` was the only new-flight aircraft missing explicit `StallSpeed` and `MaxSafeSpeed`; this pass added drone-appropriate values plus stall recovery/safe-speed data.
- No legacy-flight-model aircraft were modified.

## Aircraft that may need future manual tuning

- `bqm_74e.txt` — target-drone stall and safe-speed values were inferred from its speed class and may need in-game validation.
- `f14d.txt` — existing stall speed is much lower than the base `f14.txt`; verify that carrier landing behavior and swept-wing handling remain intended.
- `mig31.txt` — existing stall speed is very low for a very heavy interceptor; verify high-altitude/high-speed energy behavior.
- `mv-22.txt` — tilt-rotor behavior sits between fixed-wing and VTOL transport; verify transition/approach throttle feel.
- `x-47b.txt` — UCAV throttle and no-combat-flap choice should be validated if autonomous maneuvering behavior changes later.

## Consistency and balance notes

- Heavy bombers/transports now share slow, stable throttle schedules but differ between piston/turboprop and jet bomber families.
- WW2 fighters and carrier/cold-war fighters have combat-flap overspeed penalties lower than modern fighters so flaps are useful in low-speed fights but risky at high speed.
- Modern fighter flap bonuses are deliberately smaller because existing thrust, G, roll, and high-speed safe-speed values already give strong maneuverability.
- STOL/utility aircraft received low-speed throttle/lift improvements without combat flaps, preserving landing/utility character without adding a dogfight mechanic.
