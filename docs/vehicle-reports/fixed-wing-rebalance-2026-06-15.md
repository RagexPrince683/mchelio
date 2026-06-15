# Fixed-wing flight-model rebalance - 2026-06-15

This audit retuned the MCHeli Overdrive fixed-wing roster around the documented new-flight-model relationships rather than the previous legacy category scales. The pass used `docs/vehicle-config/planes.md` as the authoritative source for how mass, thrust, gravity, stall, drag, vertical energy exchange, compressibility, and angular response interact.

## Method

- Treated `PhysicalMass` as translational aircraft mass for acceleration, lift-to-weight, drag response, climb, and takeoff roll.
- Treated `EngineThrust` as physical force applied through `EngineThrust / PhysicalMass`, not as a top-speed proxy.
- Kept `NewFlightGravity` close to the documented global baseline, using small role-based deviations only for heavy bombers/transports, light UAVs, and other cases where the override supports identity rather than replacing mass.
- Recomputed stall and recovery speeds from each aircraft's level-speed envelope and role, ensuring recovery speed remains above stall speed.
- Retuned drag and energy values by role so turns, climbs, dives, and throttle cuts create distinct energy behavior.
- Retuned torque, damping, and inertia only after physical identity was set, so handling differences support mass/thrust/drag tuning rather than masking it.

## Role outcomes

- WWII fighters now sit in a light-to-medium mass band with strong control authority, high AoA tolerance, low top speed, and meaningful energy loss when over-pulled.
- Heavy fighters, patrol aircraft, and prop bombers retain momentum better but climb and turn more slowly due to higher mass, higher damping, and greater induced/control drag.
- Attack and CAS aircraft are heavier, steadier gun platforms with stronger low-altitude drive than transports but more maneuver energy loss than fighters.
- Early jets now keep speed well in dives and level flight but have weaker low-speed AoA margins and less forgiving recovery than props.
- Interceptors emphasize thrust-to-weight, climb, and vertical recovery while using lower critical AoA and heavier damping to avoid dogfighter-like sustained turning.
- Modern fighters now split into lightweight, heavyweight, and agile fifth-generation profiles with distinct mass, thrust, stall, and control-response behavior.
- Bombers and transports now use mass and drag to create long takeoff rolls, broad turns, stable climb, and strong momentum retention.
- Recon/superfast aircraft emphasize high ceiling, speed retention, and heavy high-speed handling rather than close-in maneuverability.

## Static validation

Validation was limited to static configuration review. The game was not launched and no gameplay testing was performed. Checks verified that every edited fixed-wing aircraft remains opted into the new mobility system, managed keys are present exactly once, `StallRecoverySpeed` is greater than `StallSpeed`, and the primary documented values remain inside the documented ranges.
