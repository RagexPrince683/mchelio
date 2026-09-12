# MC Helicopter Overdrive+ ASSET REPO

NOTICE: THIS REPOSITORY IS DEPRICIATED. ALL FUTURE AND CURRENT ASSET WORK IS NOW IN THE MCH-MOCMASTER REPO https://github.com/RagexPrince683/MCH-mocmaster

MC Helicopter Overdrive+ (`mcheli-overdrive`, mod id `mcheli`) is a content-heavy continuation and expansion of the classic **MC Helicopter** mod for **Minecraft 1.7.10 Forge**. It adds playable military and civilian aircraft, armored vehicles, ships, weapons, support equipment, custom HUDs, recipes, sounds, and asset configuration files.

This repository is primarily the packaged asset/mod tree: compiled mod classes live under `mcheli/`, while configurable content lives under `assets/mcheli/`.

## Who is this for?

- Players who want a large vehicle-and-weapons sandbox for Minecraft 1.7.10.
- Modpack authors building military, survival, war, or roleplay packs.
- Server owners who need configurable damage, collision, command, and performance settings.
- Asset authors who want examples for aircraft, vehicle, weapon, HUD, and item definitions.

## What the mod adds

The current asset tree contains:

| Content type | Location | Count |
| --- | --- | ---: |
| Helicopters and rotary-wing aircraft | `assets/mcheli/helicopters/` | 59 |
| Fixed-wing aircraft | `assets/mcheli/planes/` | 127 |
| Tanks, cars, and ground systems | `assets/mcheli/tanks/` | 247 |
| Static/ground vehicles and emplacements | `assets/mcheli/vehicles/` | 50 |
| Ships and boats | `assets/mcheli/ships/` | 14 |
| Weapon definitions | `assets/mcheli/weapons/` | 2,053 |
| Throwable items | `assets/mcheli/throwable/` | 7 |
| Crafting/component items | `assets/mcheli/item/` | 70 |
| HUD definitions | `assets/mcheli/hud/` | 89 |

Major features include:

- Flyable helicopters, jets, prop aircraft, drones, transports, and gunships.
- Drivable tanks, armored vehicles, civilian vehicles, emplacements, ships, and small boats.
- Vehicle-mounted weapons including machine guns, cannons, rockets, bombs, torpedoes, missiles, targeting pods, dispensers, and smoke systems.
- Handheld/support equipment such as stinger-style launchers, range finders, chains, parachutes, containers, fuel, wrenches, and UAV stations.
- Drafting table recipe flow for crafting mod content.
- Multi-seat vehicles, gunner seats, racks/carriers, UAV-style control, cameras, zoom, night vision, radar, RWR/lock warning, countermeasures, APS, maintenance, and custom HUD layouts where configured by an asset.
- Server-side command tools for reloading config, diagnostics, titles, entity cleanup/testing, and bounding-box debugging.
- Extensive text-based asset configuration for content authors.

> **Screenshots:** none are tracked in this repository. Add current screenshots under `docs/images/` or link release-page galleries when publishing.

## Compatibility and requirements

| Requirement | Details |
| --- | --- |
| Minecraft | 1.7.10 |
| Mod loader | Minecraft Forge for 1.7.10 |
| Mod id | `mcheli` |
| Current packaged version | `1.9.23` |
| Declared dependency | `hbm` in `mcmod.info`; current public releases commonly use Ragex's Nuclear Tech / HBM-compatible Nuclear Tech forks for nuclear weapon integration. |
| Client/server | Install on both client and dedicated server for multiplayer. Clients need the same mod/assets as the server to render and interact with vehicles correctly. |

### Known incompatibilities and caveats

The project README previously listed these caveats, which are still useful to check first when troubleshooting:

- **CMDcam** may conflict.
- **OptiFine Fast Render** may break thermal/vision effects.
- Disabling **Dynamic FOV** can break zoom behavior.
- Skin-port style mods may affect the dummy entity skin.
- Fisk's Superheroes slow-motion vision is unverified.
- Speedometer-style mods may report unstable speeds because MC Helicopter movement uses partial tick/interpolation behavior.

## Installation

### Recommended loader-mod installation

1. Install **Minecraft 1.7.10**.
2. Install **Forge for Minecraft 1.7.10**.
3. Download the latest MC Helicopter Overdrive+ release from one of the project pages below.
4. Install required dependencies for your release, especially the `hbm`/Ragex Nuclear Tech dependency if your pack uses the nuclear weapon integrations.
5. Place the release file/folder exactly as supplied by the release package into your Minecraft `mods` folder.
6. Start Minecraft once, then review the generated `config/mcheli.cfg` before joining servers or distributing a pack.

### Manual package-layout check

If you are handling the raw package manually, the mod root must expose compiled classes and assets together. A valid package contains at least:

```text
mcheli/                 # compiled mod classes
assets/mcheli/          # models, textures, sounds, lang, HUDs, and txt asset configs
mcmod.info              # Forge metadata
```

Do **not** separate the compiled `mcheli/` classes from `assets/mcheli/`; the mod needs both.

## Basic usage

1. Start a world with the mod installed.
2. Craft or obtain the **Drafting Table**.
3. Use the drafting table to browse and craft mod items/vehicles.
4. Fuel, arm, and repair vehicles using the configured items if `ItemFuel` and `ItemDamage` are enabled.
5. Enter a vehicle and use the configured keybinds for throttle, weapon selection, camera modes, HUD/supply GUI, landing gear, racks, countermeasures, APS, maintenance, and multiplayer screens.

See [`docs/getting-started.md`](docs/getting-started.md) for a practical first-session checklist.

## Configuration

The main runtime configuration is `config/mcheli.cfg`, generated by the mod. Important categories include:

- Commands and command permissions.
- Damage multipliers and external damage scaling.
- Explosion, collision, and block-breaking behavior.
- Fuel, ammo, item damage, repairs, and creative-mode drops.
- Keybind defaults.
- Client rendering, shaders, LOD, HUD, markers, camera behavior, and mouse controls.
- Vehicle speed multipliers and passenger/despawn behavior.
- Legacy item/block IDs for 1.7.10-era compatibility.
- Extended Overdrive options such as multi-threaded model loading, delayed range loader, bomblet loader, wrench drops, auto repair toggle, and placement timer.

Read the full reference in [`docs/configuration.md`](docs/configuration.md).

## Commands

The mod registers `/mcheli` with subcommands for administration, diagnostics, and debugging. Commands must be enabled by `EnableCommand=true` and are controlled by `CommandPermission` entries in `mcheli.cfg`.

Common examples:

```text
/mcheli list
/mcheli reconfig
/mcheli showboundingbox true
/mcheli status entity 10
/mcheli title 5 2 {"text":"Mission start","color":"gold"}
```

See [`docs/commands.md`](docs/commands.md) for syntax, permissions, and safety notes.

## Documentation

- [Getting Started Guide](docs/getting-started.md)
- [Configuration Reference](docs/configuration.md)
- [Command and Permission Reference](docs/commands.md)
- [Content and Asset Guide](docs/content-and-assets.md)
- [Server Administration Guide](docs/server-administration.md)
- [Troubleshooting and FAQ](docs/troubleshooting.md)
- [Documentation Audit Notes](docs/documentation-audit.md)
- [Plane Flight Tuning Audit](docs/plane_flight_tuning.md)

Legacy asset-author references are also included in `assets/mcheli/readme_aircraftEN.txt`, `assets/mcheli/readme_weaponEN.txt`, and `assets/mcheli/readme_hudEN.txt`.

## Project links

- CurseForge: <https://www.curseforge.com/minecraft/mc-mods/mcheli-overdrive-loader-mod>
- Modrinth: <https://modrinth.com/mod/mcheli-o>
- Nexus Mods: <https://www.nexusmods.com/minecraft/mods/375>
- itch.io: <https://ragexprince683.itch.io/mcheli-overdrive>
- GitHub/source/issues: <https://github.com/RagexPrince683/MCH-mocmaster/>
- Project site from metadata: <https://ragexprince.wordpress.com/>
- Discord/community: <https://discord.gg/uQK6QF2TeA>
- Ragecraft server Discord: <https://discord.gg/EfrnP8WJtj>

## Troubleshooting quick checks

- Confirm you are running **Minecraft 1.7.10 Forge**.
- Confirm the mod is installed on both client and server.
- Confirm dependency mods are installed and match your release.
- Disable OptiFine Fast Render if thermal/vision effects look broken.
- Keep Dynamic FOV enabled if zoom does not behave correctly.
- Use `/mcheli reconfig` after server-side config changes that can be reloaded.
- For content edits, use the in-game development reload tools described in the asset readme files.

More help is available in [`docs/troubleshooting.md`](docs/troubleshooting.md).

## Security and responsible use

This mod includes weapons, explosions, entity-management commands, and block-destruction settings. Server owners should review permissions and destructive options before opening a public server. See [`SECURITY.md`](SECURITY.md) and [`docs/server-administration.md`](docs/server-administration.md).

## Credits

Original MC Helicopter work by EMB4 with many contributors. Current package metadata credits EMB4, Ragex, Fureniu/Fureniku, Zealot, Rainwind, Grzybek, RitPennachio, Grig, Woyl/krftv, Hamzah, Edwardg2, Moc, Heinrich112, TehNIck, TheBobcat, TV90, DTC10E, Nuclear Steve, AcronixUA, W_K workshop, Naxgeneral, Mr_Iron_Golum, MyserFoxy234, YAKI-IMO, and many others.
