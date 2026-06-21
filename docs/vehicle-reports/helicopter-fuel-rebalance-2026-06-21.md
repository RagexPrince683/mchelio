# Helicopter fuel rebalance (2026-06-21)

Scope: audited every helicopter config in `assets/mcheli/helicopters` and retuned `MaxFuel` plus `FuelConsumption` without modifying any class files.

## Method

- `MaxFuel` now represents a realistic internal fuel load target for crewed helicopters, using approximate full internal fuel weight in pounds where public aircraft data is commonly expressed that way.
- `FuelConsumption` is derived as `MaxFuel / enduranceSeconds`, matching the convention already used by the fixed-wing fuel pass where the cap and consumption together set realistic endurance.
- Variant families share the same values when the airframe and fuel system are effectively the same, such as UH-60/MH-60/SH-60, Mi-24 variants, Ka-27/Ka-29, Ka-50/Ka-52, and BK117/BK117 police variants.
- Small RC, quadcopter, and FPV drones use low battery-equivalent fuel caps with endurance-scaled drain instead of full-size aircraft fuel weights.

## Tuning notes

- Heavy-lift helicopters received substantially larger fuel caps and higher burn rates, preserving multi-hour endurance while reflecting much larger onboard fuel loads.
- Attack helicopters moved away from the old uniform `1200`/`1.0` pattern into airframe-specific capacities and endurance drains.
- Utility helicopters now separate light piston/turbine aircraft, medium utility platforms, and large transport rotorcraft more clearly.
- Tiny drones and RC helicopters now have short battery-like endurance instead of oversized fuel reserves.
