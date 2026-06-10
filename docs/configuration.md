# Configuration Reference

The main configuration file is generated as `config/mcheli.cfg` when the mod starts. Defaults below were verified from the compiled `mcheli.MCH_Config` class in this repository.

## How to edit safely

1. Stop the server or exit the world.
2. Back up `config/mcheli.cfg`.
3. Change one group of settings at a time.
4. Restart the game/server, or use `/mcheli reconfig` for server-side settings that can be reloaded.
5. Test destructive settings in a copy of the world.

## Booleans and numeric values

Most settings are one of:

- `true` / `false`
- integer values
- decimal values
- comma-separated block/material/item lists
- command permission entries

Some client-only settings are sent to clients by the server or only affect local rendering/input.

## Commands and permissions

| Option | Default | Purpose |
| --- | ---: | --- |
| `EnableCommand` | `true` | Enables `/mcheli` commands. |
| `CommandPermission` | generated list | Maps `/mcheli` subcommands to allowed player names. |

See [Command and Permission Reference](commands.md).

## Gameplay and survival settings

| Option | Default | Purpose |
| --- | ---: | --- |
| `ItemDamage` | `true` | Enables item/vehicle damage behavior. |
| `ItemFuel` | `true` | Enables fuel behavior. |
| `AutoRepairHP` | `0.0` | Automatic repair threshold/amount behavior used by repair systems. |
| `AutoRepairEnabled` | see generated config | Enables/disables the Overdrive auto-repair system. |
| `InfinityAmmo` | see generated config | Toggles unlimited ammo behavior. |
| `InfinityFuel` | see generated config | Toggles unlimited fuel behavior. |
| `DropItemInCreativeMode` | see generated config | Controls item drops while in creative mode. |
| `PreventingBroken` | see generated config | Prevents configured breakage behavior. |
| `BreakableOnlyPickaxe` | see generated config | Restricts breaking to pickaxe-like behavior where used. |
| `wrenchdropitem` | see generated config | Overdrive wrench drop behavior. |
| `placetimer` | see generated config | Overdrive placement timer. |

## Explosions, collisions, and block damage

| Option | Default | Purpose |
| --- | ---: | --- |
| `Collision_DestroyBlock` | `true` | Allows collision-based block destruction. |
| `Explosion_DestroyBlock` | `true` | Allows explosions to destroy blocks. |
| `Explosion_FlamingBlock` | `true` | Allows explosions to ignite blocks. |
| `Collision_EntityDamage` | `true` | Allows collision damage to entities. |
| `Collision_EntityTankDamage` | `false` | Allows tank collision damage to entities. |
| `BulletBreakableBlock` | default list | Blocks bullets can break. |
| `Collision_Car_BreakableBlock` | `double_plant, glass_pane,stained_glass_pane` | Blocks cars can break on collision. |
| `Collision_Car_NoBreakBlock` | `torch` | Blocks cars should not break despite other rules. |
| `Collision_Car_BreakableMaterial` | `cactus, cake, gourd, leaves, vine, plants` | Materials cars can break. |
| `Collision_Tank_BreakableBlock` | `nether_brick_fence` | Blocks tanks can break. |
| `Collision_Tank_NoBreakBlock` | `torch, glowstone` | Blocks tanks should not break despite other rules. |
| `Collision_Tank_BreakableMaterial` | `cactus, cake, carpet, circuits, glass, gourd, leaves, vine, wood, plants` | Materials tanks can break. |
| `DefaultExplosionParticle` | see generated config | Controls default explosion particle behavior. |
| `delayrangeloader` | see generated config | Overdrive delayed range-loader behavior. |
| `bombletloader` | see generated config | Overdrive bomblet loader behavior. |

For public servers, consider disabling block destruction and fire until you have tested the pack's weapons.

## Damage scaling

The config exposes damage factors for broad target classes and external damage:

- `DamageVsEntity`
- `DamageVsLiving`
- `DamageVsPlayer`
- `DamageVsMCHeliAircraft`
- `DamageVsMCHeliTank`
- `DamageVsMCHeliVehicle`
- `DamageVsMCHeliOther`
- `DamageAircraftByExternal`
- `DamageTankByExternal`
- `DamageVehicleByExternal`
- `DamageOtherByExternal`

It also supports `IgnoreBulletHitItem` and an ignore list for bullet-hit handling.

## Mounting, passengers, and vehicle lifecycle

| Option | Purpose |
| --- | --- |
| `DismountAll` | Dismount behavior for all passengers. |
| `MountMinecartHeli` | Allows/disallows minecart mounting for helicopters. |
| `MountMinecartPlane` | Allows/disallows minecart mounting for planes. |
| `MountMinecartShip` | Allows/disallows minecart mounting for ships. |
| `MountMinecartVehicle` | Allows/disallows minecart mounting for vehicles. |
| `MountMinecartTank` | Allows/disallows minecart mounting for tanks. |
| `EnablePutRackInFlying` | Allows rack loading while flying. |
| `DespawnCount` | Despawn timing/count behavior. |
| `HitBoxDelayTick` | Hitbox update delay. |
| `FixVehicleAtPlacedPoint` | Fixes supported vehicles at their placed position. |
| `KillPassengersWhenDestroyed` | Kills passengers when the vehicle is destroyed. |

## Movement and speed multipliers

| Option | Purpose |
| --- | --- |
| `AllPlaneSpeed` | Global plane speed multiplier. |
| `AllHeliSpeed` | Global helicopter speed multiplier. |
| `AllTankSpeed` | Global tank speed multiplier. |
| `AllShipSpeed` | Global ship speed multiplier. |
| `AutoThrottleDownHeli` | Auto-throttle-down behavior for helicopters. |
| `AutoThrottleDownPlane` | Auto-throttle-down behavior for planes. |
| `AutoThrottleDownShip` | Auto-throttle-down behavior for ships. |
| `AutoThrottleDownTank` | Auto-throttle-down behavior for tanks. |

## Rendering, HUD, and client settings

| Option | Purpose |
| --- | --- |
| `DisableItemRender` | Disables item rendering behavior. |
| `RenderDistanceWeight` | Vehicle render-distance multiplier. |
| `EnableAircraftLODRender` | Enables aircraft LOD rendering. |
| `AircraftLODStartDistance` | Distance at which LOD begins. |
| `AircraftLODFarDistance` | Far LOD distance. |
| `MobRenderDistanceWeight` | Mob render-distance multiplier. |
| `DisableShader` | Disables shader effects. |
| `SmoothShading` | Enables/disables smooth shading. |
| `EnableModEntityRender` | Enables/disables mod entity render hooks. |
| `DisableRenderLivingSpecials` | Disables living-entity special-name rendering behavior. |
| `DisplayHUDThirdPerson` | Shows HUD in third-person where supported. |
| `DisableCameraDistChange` | Prevents camera-distance changes. |
| `EnableReplaceTextureManager` | Enables texture-manager replacement hook. |
| `ReplaceRenderViewEntity` | Enables render-view-entity replacement hook. |
| `MultiThreadedModelLoading` | `true`; loads models using multiple threads. |

## Markers, range finders, and targeting

| Option | Purpose |
| --- | --- |
| `DisplayEntityMarker` | Entity marker display behavior. |
| `EntityMarkerSize` | Entity marker size. |
| `BlockMarkerSize` | Block marker size. |
| `DisplayMarkThroughWall` | Allows markers through walls. |
| `StingerLockRange` | Lock range for stinger-style weapons. |
| `RangeFinderSpotDist` | Range-finder spotting distance. |
| `RangeFinderSpotTime` | Range-finder spotting duration. |
| `RangeFinderConsume` | Range-finder consume/ammo behavior. |
| `EnableDebugBoundingBox` | Debug bounding-box rendering; can be toggled by `/mcheli showboundingbox`. |

## Rotation and gunner limits

| Option | Purpose |
| --- | --- |
| `EnableRotationLimit` | Enables global rotation limits. |
| `PitchLimitMax` | Maximum pitch limit. |
| `PitchLimitMin` | Minimum pitch limit. |
| `RollLimit` | Roll limit. |
| `RangeOfGunner_VsMonster_Vertical` | Gunner vertical range against monsters. |
| `RangeOfGunner_VsMonster_Horizontal` | Gunner horizontal range against monsters. |
| `RangeOfGunner_VsPlayer_Vertical` | Gunner vertical range against players. |
| `RangeOfGunner_VsPlayer_Horizontal` | Gunner horizontal range against players. |

## Input settings

Keybind settings use LWJGL integer key codes and mouse-button codes. Important entries include:

| Option | Default code | Common meaning |
| --- | ---: | --- |
| `KeyUp` | `17` | Forward/throttle up (`W`). |
| `KeyDown` | `31` | Back/throttle down (`S`). |
| `KeySubmarineAscend` | `200` | Arrow up. |
| `KeySubmarineDescend` | `208` | Arrow down. |
| `KeyRight` | `32` | Right (`D`). |
| `KeyLeft` | `30` | Left (`A`). |
| `KeySwitchGunner` | `35` | Switch gunner/mode (`H`). |
| `KeySwitchHovering` | `57` | Space. |
| `KeyEjectHeli` | `54` | Right Shift. |
| `KeyAttack` | `-100` | Mouse button code. |
| `KeyUseWeapon` | `-99` | Mouse button code. |
| `KeyCurrentWeaponLock` | `-100` | Mouse button code. |
| `KeySwitchWeapon1` | `-98` | Mouse button code. |
| `KeySwitchWeapon2` | see generated config | Weapon switching. |
| `KeySwWeaponMode` | see generated config | Weapon mode switch. |
| `KeyZoom` | see generated config | Zoom. |
| `KeyCameraMode` | see generated config | Camera mode. |
| `KeyUnmount` | see generated config | Unmount. |
| `KeyFlare` | see generated config | Flares. |
| `KeyChaff` | see generated config | Chaff. |
| `KeyMaintenance` | see generated config | Maintenance. |
| `KeyAPS` | see generated config | Active protection system. |
| `KeyExtra` | see generated config | Extra action. |
| `KeyCameraDistUp` | see generated config | Increase camera distance. |
| `KeyCameraDistDown` | see generated config | Decrease camera distance. |
| `KeyFreeLook` | see generated config | Free look. |
| `KeyGUI` | see generated config | Vehicle/supply GUI. |
| `KeyGearUpDown` | see generated config | Landing gear. |
| `KeyPutToRack` | see generated config | Put to rack/carrier. |
| `KeyDownFromRack` | see generated config | Unload from rack/carrier. |
| `KeyScoreboard` | `38` | Scoreboard (`L`). |
| `KeyMultiplayManager` | `50` | Multiplayer manager (`M`). |

Mouse/input behavior options include:

- `InvertMouse`
- `MouseSensitivity`
- `MouseControlStickModeHeli`
- `MouseControlStickModePlane`
- `MouseControlFlightSimMode`
- `SwitchWeaponWithMouseWheel`
- `HideKeybind`

## Creative tab icons

The config includes icon selectors for:

- `CreativeTabIcon`
- `CreativeTabIconHeli`
- `CreativeTabIconPlane`
- `CreativeTabIconShip`
- `CreativeTabIconTank`
- `CreativeTabIconVehicle`

## Legacy item and block IDs

Minecraft 1.7.10 still uses legacy ID-sensitive systems in some contexts. The config contains IDs for fuel, GLTD, chain, parachute, container, stinger, missiles, UAV stations, invisible item, drafting table, wrench, range finder, and drafting table blocks.

Examples verified from the class:

| Option | Default |
| --- | ---: |
| `ItemID_Stinger` | `28900` |
| `ItemID_StingerMissile` | `28901` |
| `BlockID_DraftingTable` | `3450` |
| `BlockID_DraftingTableON` | `3451` |

## Recipe toggles

Recipe enable/disable entries exist for fuel, GLTD, chain, parachute, container, stinger, stinger missile, Javelin, Javelin missile, RPG, RPG missile, UAV stations, drafting table, wrench, and range finder.

## Notes on exact defaults

This repository does not include a generated sample `mcheli.cfg`. Some defaults are easy to verify from bytecode and are listed above; others require launching the mod in a 1.7.10 Forge runtime and saving the generated config. See [Documentation Audit Notes](documentation-audit.md) for gaps that still need a runtime-generated sample config.
