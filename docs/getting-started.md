# Getting Started Guide

This guide is for players installing MC Helicopter Overdrive+ for the first time.

## 1. Confirm your version

MC Helicopter Overdrive+ in this repository is packaged for:

- Minecraft `1.7.10`
- Minecraft Forge for `1.7.10`
- Mod id `mcheli`
- Packaged version `1.9.23`

Do not install this package into a modern Minecraft instance unless you are using a compatibility layer specifically made for 1.7.10 Forge mods.

## 2. Install the mod

1. Install Minecraft 1.7.10.
2. Install Forge for Minecraft 1.7.10.
3. Download MC Helicopter Overdrive+ from the project's CurseForge, Modrinth, Nexus Mods, or itch.io page.
4. Install the required `hbm`/Ragex Nuclear Tech dependency expected by your release.
5. Put the supplied mod package in `.minecraft/mods` or your launcher profile's `mods` directory.
6. Start the game once so `config/mcheli.cfg` is generated.

## 3. Start with creative testing

The content set is large. For a first session, use a creative test world before adding the mod to an existing survival world.

Suggested first checks:

1. Open the MC Helicopter creative tabs.
2. Place or craft a Drafting Table.
3. Spawn one simple ground vehicle and one simple helicopter.
4. Verify sounds, textures, keybinds, weapons, and HUDs work.
5. Open `Options > Controls` and adjust conflicting keys.

## 4. Learn the core loop

Most gameplay follows this flow:

1. **Craft components** such as frames, mechanic parts, cannon parts, engines, or armor components.
2. **Use the Drafting Table** to craft vehicles and support items.
3. **Fuel vehicles** if fuel is enabled.
4. **Load ammunition** or use configured weapon reload behavior.
5. **Mount the vehicle**, switch weapon groups, use zoom/camera modes, and operate countermeasures or support systems.
6. **Repair vehicles** with the wrench/maintenance systems if damage and repair settings are enabled.

## 5. Default keybind areas

Exact key values are stored in `mcheli.cfg` as LWJGL key/mouse codes. The most important default bindings include movement keys, mouse weapon controls, weapon switching, zoom, camera mode, unmount, flares/chaff, maintenance, APS, landing gear, rack controls, scoreboard, and multiplayer manager.

If another mod uses the same keys, change MC Helicopter bindings in Minecraft controls or in `mcheli.cfg`.

## 6. Recommended first server settings

For public or semi-public servers, review these settings before launch:

- `EnableCommand`
- `CommandPermission`
- `Explosion_DestroyBlock`
- `Explosion_FlamingBlock`
- `Collision_DestroyBlock`
- `InfinityAmmo`
- `InfinityFuel`
- `KillPassengersWhenDestroyed`
- `AutoRepairHP` and `AutoRepairEnabled`
- Speed multipliers such as `AllPlaneSpeed`, `AllHeliSpeed`, `AllTankSpeed`, and `AllShipSpeed`

See [Server Administration](server-administration.md) for recommended policies.
