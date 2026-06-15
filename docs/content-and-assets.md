# Content and Asset Guide

MC Helicopter Overdrive+ is highly data-driven. Most gameplay content is represented by text configuration files under `assets/mcheli/`, with matching models, textures, sounds, language entries, recipes, and HUD files.

## Current content inventory

| Content type | Directory | Files |
| --- | --- | ---: |
| Helicopters | `assets/mcheli/helicopters/` | 59 |
| Planes | `assets/mcheli/planes/` | 127 |
| Tanks/cars/ground systems | `assets/mcheli/tanks/` | 247 |
| Vehicles/emplacements | `assets/mcheli/vehicles/` | 50 |
| Ships/boats | `assets/mcheli/ships/` | 14 |
| Weapons | `assets/mcheli/weapons/` | 2,053 |
| Throwable items | `assets/mcheli/throwable/` | 7 |
| Items/components | `assets/mcheli/item/` | 70 |
| HUDs | `assets/mcheli/hud/` | 89 |

## Important asset folders

For a packaged install, the mod jar and matching content pack normally live under `mods/`. In the development run directory, content is expected under `build/run/mods/mcheli/`. A complete content pack should provide the category folders listed in the inventory above plus shared resources such as `assets/mcheli/models/`, `assets/mcheli/textures/`, `assets/mcheli/sounds/`, and `assets/mcheli/sounds.json`.

- `assets/mcheli/models/` - model files for blocks, bullets, helicopters, planes, ships, tanks, throwables, and vehicles.
- `assets/mcheli/textures/` - GUI, item, vehicle, bullet, particle, and block textures.
- `assets/mcheli/sounds/` - sound files used by weapons and vehicles.
- `assets/mcheli/lang/` - localization.
- `assets/mcheli/hud/` - HUD scripts loaded by vehicles/seats.
- `assets/mcheli/shaders/` - shader programs and post effects.
- `assets/mcheli/sounds.json` - sound event registration used alongside the sound files.

## Vehicle configuration concepts

Vehicle text files describe what the item is, how it moves, where seats/cameras are located, what weapons it carries, and what HUD each seat uses. The legacy `assets/mcheli/vehicles/` folder is not the shared base-vehicle folder; it loads turret/static-weapon definitions. Shared vehicle parsing applies across helicopters, planes, ships, tanks, and turret/static-weapon definitions.

Every vehicle config must have enough data to pass validation: at least one seat, at least one texture, and a usable item/model from the content loader. Normal configs satisfy the texture requirement because the loader adds the file name as the initial texture unless reload logic clears it.

Common concepts found in the included asset readmes, configs, and parser-audited code docs:

- `DisplayName` and `AddDisplayName` for localization.
- `AddTexture` for alternate skins.
- `Category` for creative/category sorting; punctuation is normalized by the parser.
- `CameraPosition` and `CameraZoom` for viewpoints and optics. `CameraPosition` can also carry `alwaysCameraView`, `fixRot`, and `fixYaw` options.
- `HUD` per seat, with fallback defaults by vehicle class.
- `EnableGunnerMode`, `EnableNightVision`, and `EnableEntityRadar` where supported.
- Movement parameters such as `Speed`, `MotionFactor`, `Gravity`, `GravityInWater`, `MobilityYaw`, `MobilityPitch`, `MobilityRoll`, throttle factors, and ground-movement gates.
- Seat definitions such as `AddSeat`, `AddGunnerSeat`, and `AddFixRotSeat`; seats and racks share a combined limit of 500 entries.
- Carrier/rack behavior such as `AddRack`, `RideRack`, and `ExclusionSeat`.
- Support and survivability fields such as `MaxFuel`, `FuelConsumption`, `AmmoSupplyRange`, `FuelSupplyRange`, `RepairOtherVehicles`, armor fields, flares, chaff, maintenance, and APS.
- Detection and targeting metadata such as `Stealth`, `RadarType`, `RWRType`, and radar display-name fields.
- Visual and effect parts such as weapon parts, weapon bays, searchlights, camera parts, splash/sea-surface particles, sounds, and smooth-shading options.

The Overdrive plane set also uses extended flight-model tuning fields documented in [Plane Flight Tuning Audit](plane_flight_tuning.md), including throttle response, drag, stall/compressibility speeds, torque, damping, G-load, overspeed, level/dive energy tuning, and class-based balancing. Keep these fixed-wing aerodynamic keys in plane configs; helicopter, ship, tank, and turret/static-weapon configs should not inherit plane-only flight-model fields.

For a parser-level inventory of supported vehicle keys, value formats, defaults, and clamping behavior, see [MCHeli Vehicle Configuration Reference](code-docs/vehicle-config-reference.md) and the per-family pages under [Vehicle config](vehicle-config/base.md).

## Weapon configuration concepts

Weapon text files define display names, weapon type, damage, projectile behavior, reload behavior, targeting, sights, zoom levels, explosions, and block damage.

Weapon types documented by the bundled `readme_weaponEN.txt` include:

- `MachineGun1`
- `MachineGun2`
- `Torpedo`
- `CAS`
- `Rocket`
- `ASMissile`
- `AAMissile`
- `TVMissile`
- `ATMissile`
- `Bomb`
- `MkRocket`
- `Dummy`
- `Smoke`
- `Dispenser`
- `TargetingPod`

Common weapon fields include `Power`, `DamageFactor`, `Acceleration`, `Explosion`, `ExplosionBlock`, `DelayFuse`, `TimeFuse`, `Flaming`, `Sight`, `Zoom`, `Group`, `Delay`, `ReloadTime`, and `Round`.

## Creative tabs and recipe-facing content

Loaded content appears in the mod's creative tabs: `MCHeliO Item`, `MCHeliO Recipe Items`, `MCHeliO Helicopters`, `MCHeliO Planes`, `MCHeliO Ships`, `MCHeliO Tanks`, and `MCHeliO Vehicles`. Empty tabs or missing vehicles usually indicate that the matching asset folder is missing or one or more definitions failed to load.

The Drafting Table is the main recipe interface for MCHeli content when recipes are enabled. Vehicle and item configs may define shaped or shapeless recipes with legacy MCHeli recipe syntax; server packs should verify recipes after changing content or `mcheli.cfg` recipe settings.

## Reloading asset edits in-game

The bundled asset readmes describe development reload flows:

- Aircraft/config reload: mount the aircraft, open the supply/MOD option screen, then use the development reload option.
- Weapon reload: mount a vehicle, open the supply/MOD option screen, then use the development option to reload all weapons.
- Textures/sounds: use Minecraft's resource-pack reload flow from the options menu.

These tools are intended for development/testing. Restarting the game/server remains the safest way to validate release builds.

## Asset-author references

Use these bundled references when editing content:

- `assets/mcheli/readme_aircraftEN.txt`
- `assets/mcheli/readme_weaponEN.txt`
- `assets/mcheli/readme_hudEN.txt`
- `assets/mcheli/mcheli_parameterlist.ja.en.pdf`
- `assets/mcheli/mcheli_parameterlist.pdf`
