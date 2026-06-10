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

- `assets/mcheli/models/` - model files for blocks, bullets, helicopters, planes, ships, tanks, throwables, and vehicles.
- `assets/mcheli/textures/` - GUI, item, vehicle, bullet, particle, and block textures.
- `assets/mcheli/sounds/` - sound files used by weapons and vehicles.
- `assets/mcheli/lang/` - localization.
- `assets/mcheli/hud/` - HUD scripts loaded by vehicles/seats.
- `assets/mcheli/shaders/` - shader programs and post effects.

## Vehicle configuration concepts

Vehicle text files describe what the item is, how it moves, where seats/cameras are located, what weapons it carries, and what HUD each seat uses.

Common concepts found in the included asset readmes and configs:

- `DisplayName` and `AddDisplayName` for localization.
- `AddTexture` for alternate skins.
- `CameraPosition` and `CameraZoom` for viewpoints and optics.
- `HUD` per seat, with fallback defaults by vehicle class.
- `EnableGunnerMode`, `EnableNightVision`, and `EnableEntityRadar` where supported.
- Movement parameters such as `Speed`, `MotionFactor`, `Gravity`, `MobilityYaw`, `MobilityPitch`, and `MobilityRoll`.
- Seat definitions such as `AddSeat`, `AddGunnerSeat`, and `AddFixRotSeat`.
- Carrier/rack behavior such as `AddRack`, `RideRack`, and `ExclusionSeat`.

The Overdrive plane set also uses extended flight-model tuning fields documented in [Plane Flight Tuning Audit](plane_flight_tuning.md), including throttle response, drag, stall/compressibility speeds, torque, damping, and class-based balancing.

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
