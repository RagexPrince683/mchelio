# New-flight asset and gameplay validation pass - 2026-06-12

## Scope

- Re-audited every plane config in `assets/mcheli/planes` with `UseNewMobilitySystem = true`.
- Left legacy aircraft untouched.
- Used `docs/vehicle-config/planes.md` and the current new-flight gravity/lift/stall formula as the validation reference.
- No captured `DebugFlightControl` runtime logs were present in the repository, so this pass is a config/static validation plus targeted risk tuning. Manual test notes below list the debug fields to capture for any remaining problem aircraft.

## Validation criteria

A new-flight plane is considered config-ready when it has all of the following fields and their ratios match its class:

- `GravityStrength`
- `LiftGravityCompensation`
- `StallSpeed`
- `StallSpeedFactor`
- `StallRecoverySpeed`
- `StallLiftLoss`
- `StallNoseDownForce`
- `StallNoseDownMinSpeed`
- `NewFlightEngineBrakeDrag`
- `GroundBounceDamping`
- `GroundVerticalVelocityClamp`
- `MaxLevelSpeed`
- `BaseDrag`
- `InducedDrag`
- `ControlSurfaceDrag`

The most important takeoff gate is that a conventional fixed-wing aircraft needs enough airspeed, lift factor, throttle/effective throttle, non-severe stall state, and rotation attitude before the ground clamp allows upward velocity. For that reason, heavy and special aircraft now keep realistic high stall speeds and slow rotation, but still have enough `LiftGravityCompensation` headroom to leave the ground when the takeoff gate is truly valid.

## Aircraft modified

### Takeoff lift headroom

These aircraft had `LiftGravityCompensation` below 1.0 while using the new explicit gravity model. That could make valid takeoff/climb marginal even after reaching rotation speed, especially with ground clamp active. They were raised only to modest class-appropriate values instead of being made floaty:

| Aircraft configs | Change | Expected effect |
| --- | --- | --- |
| `ac-130`, `b52`, `b52d`, `b52n`, `mc130`, `mc130j`, `tu142real`, `tu95k22`, `tu95ms`, `tu95org` | `LiftGravityCompensation` to `1.01` | Heavy transports/bombers can rotate and leave ground when validTakeoff is met while retaining high gravity, low clamp, and long takeoff roll. |
| `b-1`, `b-1nuclear`, `b-2a`, `b-2a2`, `b-2a3`, `b-2a4`, `mig25`, `mig31`, `mig31k`, `mirageiv`, `sr71`, `tu160m`, `tu160mmsl`, `tu22m3` | `LiftGravityCompensation` to `1.01` | Fast/heavy jets keep poor low-speed manners but gain enough healthy-flight lift margin to avoid ground-clamp blocking a real takeoff. |
| `a400m`, `c5`, `c5m`, `e767`, `f-104`, `f117`, `f117gbu27`, `f117nuc`, `il76ua`, `md90`, `victor_b2` | `LiftGravityCompensation` to `1.02` | Large aircraft and low-lift jets get slightly more takeoff margin without idle hover. |
| `ac-47`, `c-47`, `h6k` | `LiftGravityCompensation` to `1.03` | Older prop transports/flying boats retain moderate gravity but get more forgiving low-speed lift. |
| `bqm_74e` | `LiftGravityCompensation` to `1.01` | Target drone can climb in fixed-wing mode without adopting fighter-like lift. |

### Stall-speed and recovery consistency

These aircraft had stall/recovery values that were out of proportion to `Speed`/`MaxLevelSpeed`, or an explicit recovery speed below the stall threshold. Values were corrected so stall recovery requires enough speed and lower AoA instead of instantly clearing the stall state.

| Aircraft configs | Change | Expected effect |
| --- | --- | --- |
| `f-15e` | `StallRecoverySpeed` `0.502` | Recovery now occurs at about 1.2x stall speed instead of below stall speed. |
| `f-35a`, `f-35b`, `f-35c` | `StallRecoverySpeed` `0.460` | Lightning variants require real speed recovery and should still descend at idle/low speed. |
| `f16c`, `fa18e` | `StallRecoverySpeed` `0.438` | Recovery threshold now matches the configured stall speed. |
| `f14d` | `StallSpeed` `0.346`, `StallSpeedFactor` `0.108`, `StallRecoverySpeed` `0.415` | Removes unrealistically low Tomcat stall threshold while preserving variable-wing/high-speed identity. |
| `jas39` | `StallSpeed` `0.326`, `StallSpeedFactor` `0.102`, `StallRecoverySpeed` `0.391` | Canard fighter no longer has a prop-like stall threshold. |
| `f-104` | `StallSpeed` `0.365`, `StallSpeedFactor` `0.099`, `StallRecoverySpeed` `0.438` | Starfighter now has appropriately weak low-speed behavior and higher takeoff speed. |
| `mig31` | `StallSpeed` `0.487`, `StallSpeedFactor` `0.122`, `StallRecoverySpeed` `0.584`, `StallLiftLoss` `0.74` | Foxhound now behaves like a heavy interceptor with high rotation/recovery speed rather than a low-speed fighter. |
| `bayraktar tb 2` | `StallSpeed` `0.115`, `StallSpeedFactor` `0.298`, `StallRecoverySpeed` `0.138` | Small UAV gets a plausible low-speed takeoff instead of stalling at almost half of max speed. |
| `geran2`, `mqm170` | `StallSpeed` `0.105`, `StallSpeedFactor` `0.326`, `StallRecoverySpeed` `0.126` | Tiny/loitering aircraft can fly slowly without being permanently stall-gated. |
| `skylark` | `StallSpeed` `0.052`, `StallSpeedFactor` `0.325`, `StallRecoverySpeed` `0.062` | Hand-launch-sized UAV keeps low-speed behavior and avoids excessive stall ratio. |
| `pzl-m18` | `StallSpeed` `0.125`, `StallSpeedFactor` `0.287`, `StallRecoverySpeed` `0.150` | Agricultural prop can rotate at plausible low speed without hover-like lift. |

### Explicit fallback fields added

- Added missing `StallRecoverySpeed` to all remaining new-flight configs that only relied on the implicit `StallSpeed * 1.2` default. This makes the recovery target explicit for asset review and future tuning.
- Added missing `StallSpeedFactor` to `a-10`, `f-86f`, and `p-51d` so all new-flight configs now have an auditable derived-stall fallback.

## Aircraft expected to take off after this pass

Static validation indicates all 125 new-flight configs have enough configured lift headroom and no longer have missing required audit fields. The following groups are expected to take off normally when the pilot holds sufficient throttle, reaches rotation speed, and applies a sane rotation attitude:

- WW2 props and light props: `a6m2`, `a6m2n`, `an2`, `au23`, `bf109`, `bv138`, `emb314`, `f1m`, `f8f`, `ju87`, `mig3`, `n1k1`, `ov-10a`, `p-51d`, `pzl-m18`, `spitfire-mkvb`.
- Modern fighters/attack jets: `a-10`, `a4`, `a6`, `a7`, `eurofighter_typhoon_2`, `eurofighter_typhoon_2_t`, `f-15e`, `f-15s_mtd`, `f-35a`, `f-35c`, `f14`, `f14d`, `f16c`, `f22a`, `fa18e`, `fa18fold`, `fa50`, `jas39`, `j15`, `kf-21`, `m2000-5`, `m2000c`, `mig29`, `rafalem`, `su-33`, `su27bru`, `su34`, `su34b`, `su34n`, `su37`, `su57`, `tornado-gr4`, `tornado-ids`.
- Older/early jets and interceptors: `f-104`, `f-5e`, `f-80`, `f-86f`, `f4a`, `il28sh`, `j8`, `mig-15`, `mig-19s`, `mig-21pf`, `mig17f`, `mig21`, `mig23`, `mig25`, `mig31`, `mig31k`, `mirage3e`, `mirageiv`, `q-5d`, `qf-80`, `sr71`.
- Heavy bombers/transports: `a400m`, `ac-130`, `ac-47`, `b-1`, `b-1nuclear`, `b-2a`, `b-2a2`, `b-2a3`, `b-2a4`, `b29`, `b29sp`, `b52`, `b52d`, `b52n`, `c-47`, `c5`, `c5m`, `e767`, `h6k`, `h8k`, `il76ua`, `mc130`, `mc130j`, `md90`, `tu142real`, `tu160m`, `tu160mmsl`, `tu22m3`, `tu4`, `tu4light`, `tu95k22`, `tu95ms`, `tu95org`, `victor_b2`.
- UAVs/special: `bayraktar tb 2`, `bqm_74e`, `geran2`, `mq-9`, `mqm170`, `skylark`, `x-47b`.

## Aircraft still needing manual testing

These are not known-bad after static validation, but they should be prioritized because class-specific behavior is hard to prove without runtime debug logs:

- VTOL/STOVL/tiltrotor: `f-35b`, `harrier`, `harrier_en`, `mv-22`, `yak38`, `yak38_r60`, `yak38_upk`, `yak38_x23`.
- Very large and ground-clearance-sensitive aircraft: `a400m`, `ac-130`, `c5`, `c5m`, `mc130`, `mc130j`, `b52`, `b52d`, `b52n`, `tu95k22`, `tu95ms`, `tu95org`, `tu142real`.
- Extreme-speed / low-lift aircraft: `f-104`, `mig25`, `mig31`, `mig31k`, `sr71`, `tu160m`, `tu160mmsl`, `tu22m3`.
- Tiny UAVs and loitering aircraft: `bayraktar tb 2`, `geran2`, `mqm170`, `skylark`.

## Suspicious configs resolved or intentionally retained

- Resolved: no new-flight config is now missing any of the requested audit fields.
- Resolved: no explicit `StallRecoverySpeed` remains below its matching `StallSpeed`.
- Resolved: conventional/heavy fixed-wing configs that were below `LiftGravityCompensation = 1.0` now have enough valid-takeoff headroom.
- Intentionally retained: `geran2` remains at `LiftGravityCompensation = 0.98` because it is a loitering munition and should not climb like a conventional powered plane without enough throttle/airspeed.
- Intentionally retained: `mv-22` remains at `LiftGravityCompensation = 0.98` because VTOL/tiltrotor lift is special-case behavior and should not be blindly fixed with conventional fixed-wing lift.
- Intentionally retained: heavy bombers/transports keep high `GravityStrength` and tight `GroundVerticalVelocityClamp` values to suppress touchdown/post-exit upward drift; the lift changes were kept small to avoid reintroducing hover-like behavior.

## Debug notes for runtime validation

If any aircraft still fails takeoff, bounces after landing, drifts upward after pilot exit, or has unrecoverable stalls, capture these `DebugFlightControl` values at the moment of failure:

- airspeed at rotation
- throttle and effectiveThrottle
- liftFactor
- validTakeoff state
- groundClampApplied
- bounceDampingApplied
- stallSeverity
- motionY
- pitch attitude

Recommended pass/fail signs:

- Takeoff: `validTakeoff = true`, airspeed at least about `StallSpeed * 0.85`, `liftFactor >= 0.45`, and ground clamp no longer holding positive `motionY` down.
- Throttle cut: effectiveThrottle decays, drag rises through `NewFlightEngineBrakeDrag`, airspeed decays, `liftFactor` falls, and `motionY` trends negative instead of level-hovering.
- Landing/post-exit: `groundClampApplied` or `bounceDampingApplied` appears during invalid upward motion; no-pilot state should prevent stale throttle/lift from creating a climb.
- Stall recovery: `stallSeverity` rises with low speed or excessive AoA, lift loss increases sink, `StallNoseDownForce` creates a recovery tendency above `StallNoseDownMinSpeed`, and recovery does not clear until speed reaches `StallRecoverySpeed` with low AoA.
