# Prop aircraft handling balance pass - 2026-06-11

Source documentation used: `docs/vehicle-config/base.md` for legacy `MobilityYaw`, `MobilityPitch`, and `MobilityRoll` axis multipliers, and `docs/vehicle-config/planes.md` for `UseNewMobilitySystem`, torque/damping/inertia, stall, drag, G-control, and speed-scaled flight-model keys.

## Scope and audit result

- Reviewed all 127 files in `assets/mcheli/planes` for propeller-driven handling outliers and for relative separation from jets.
- Adjusted 37 propeller-driven or rotor/propeller aircraft configs.
- Did not broadly buff jet configs; the pass creates separation by moving prop fighters above the previous generic fighter response band while leaving bombers, transports, and attack aircraft restrained.
- Left `fuel_truck.txt` and `mq-9debug.txt` out of tuning because the prior audit classifies them as non-plane support / legacy manual-review configs.

## Aircraft adjusted

### Dedicated turn fighters and lightweight prop fighters

These aircraft now have the strongest pitch/yaw authority, faster stall recovery, lower G-control fade, reduced turn drag, and higher low-speed controllability:

- `a6m2.txt` - A6M Zero: dedicated turn-fighter profile.
- `spitfire-mkvb.txt` - Spitfire Mk.Vb: dedicated turn-fighter profile.
- `n1k1.txt` - N1K: agile fighter profile.
- `a6m2n.txt` - A6M2-N Rufe: float-fighter profile with reduced roll versus land fighters.
- `f1m.txt` - F1M Pete: float-fighter profile with modest G limits.

### Energy fighters

These aircraft gained noticeably better authority than jets in low-speed dogfights but retain higher energy-fighter drag/G penalties than pure turn fighters:

- `bf109.txt` - Bf 109.
- `p-51d.txt` - P-51D Mustang.
- `mig3.txt` - MiG-3.
- `f8f.txt` - F8F Bearcat, tuned as a high-roll-rate energy/light fighter rather than a pure sustained-turn platform.

### Prop attack aircraft and utility aircraft

These aircraft gained low-speed control and stall consistency without becoming front-line turn fighters:

- `ju87.txt` - Ju 87 Stuka.
- `ov-10a.txt` - OV-10A Bronco.
- `emb314.txt` - EMB 314 Super Tucano.
- `au23.txt` - AU-23A Peacemaker.
- `an2.txt` - An-2.
- `pzl-m18.txt` - PZL M-18.

### Heavy prop aircraft, transports, bombers, and turboprops

These aircraft were only lightly adjusted for consistency, stability, and predictable stall recovery. They remain much less agile than dedicated fighters:

- `c-47.txt` - C-47 Skytrain.
- `ac-47.txt` - AC-47 Spooky.
- `a400m.txt` - A400M Atlas.
- `bv138.txt` - BV 138.
- `h8k.txt` - H8K Emily.
- `b29.txt` - B-29 Superfortress.
- `b29sp.txt` - B-29 Silverplate.
- `tu4.txt` - Tu-4A.
- `tu4light.txt` - Tu-4.
- `tu95org.txt` - Tu-95 Bear.
- `tu95ms.txt` - Tu-95MSM.
- `tu95k22.txt` - Tu-95K-22.
- `tu142real.txt` - Tu-142.
- `mc130.txt` - MC-130H.
- `mc130j.txt` - MC-130J.
- `ac-130.txt` - AC-130H.
- `mv-22.txt` - MV-22 Osprey.

### Propeller drones

Drone props received only moderate response improvements and lower stall violence; they should remain stable ISR/UCAV platforms rather than dogfighters:

- `bayraktar tb 2.txt` - Bayraktar TB2.
- `mq-9.txt` - MQ-9 Reaper.
- `mqm170.txt` - MQM-170.
- `skylark.txt` - Skylark.
- `geran2.txt` - Geran 2.

## Summary of maneuverability changes

- Added or retuned `MobilityYaw`, `MobilityPitch`, and `MobilityRoll` where prop fighters were missing clear axis multipliers or were below jet response bands.
- Increased `PitchTorque`, `RollTorque`, and `YawTorque` for light fighters so they initiate turns and reversals more quickly.
- Reduced fighter `PitchDamping`, `RollDamping`, `YawDamping`, and `InertiaMultiplier` so props no longer feel overly stiff in close-range maneuvering.
- Added `StallRecoverySpeed` to the adjusted prop aircraft so low-speed authority returns earlier and more consistently after aggressive maneuvers.
- Raised `CriticalAoA` and reduced `StallLiftLoss` / `StallInstability` for turn fighters, making sustained low-speed turns more controllable.
- Reduced fighter `InducedDrag` and `ControlSurfaceDrag` enough to help sustained turns without giving attack aircraft and bombers the same advantage.
- Lowered `GControlPenalty` on turn fighters and energy fighters so they keep meaningful control authority under dogfight loads.
- Kept bombers, transports, and large turboprops on low mobility, high inertia, and heavier damping so they stay stable but do not become agile.

## Combat flap additions and tuning

No parser-supported combat-flap configuration key exists in the documented plane schema or the current `MCP_PlaneInfo` class fields. Because of that, this pass did **not** add unknown always-on flap keys to plane configs. Instead, aircraft historically known for flap-assisted/low-speed turning were approximated with documented values only:

- A6M Zero, Spitfire, N1K, A6M2-N, and F1M received the strongest low-speed/stall-control tuning.
- Energy fighters received improved controllability but retained more drag and G-control penalty than turn fighters.
- Attack aircraft and bombers received limited low-speed stability only.

A separate code/config feature should be added before true deployable combat flaps can be balanced. That feature should include lift gain, drag gain, stall-speed reduction, authority gain, speed limits, and damage/lockout behavior so flaps do not become a permanent always-on buff.

## Aircraft still requiring manual review

- `h6k.txt`: existing naming/spec identity is ambiguous (`Xi'an H-6K` jet bomber naming versus legacy H6K/H8K prop/flying-boat-style asset naming in older audit data). It was not included in the prop buff until identity is confirmed.
- `mq-9debug.txt`: remains a legacy/manual drone config and was not migrated to the new mobility model.
- `fuel_truck.txt`: non-plane support asset.
- True combat flaps: requires runtime/config support before per-aircraft flap balancing can be safely implemented.
- Aircraft named in the request but not present in `assets/mcheli/planes`: Ki-43, P-38, Mosquito, Me-410, and Fw-190.
