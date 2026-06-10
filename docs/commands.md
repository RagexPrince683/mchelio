# Command and Permission Reference

MC Helicopter Overdrive+ registers one root command:

```text
/mcheli <subcommand> ...
```

Commands are enabled by `EnableCommand=true` in `config/mcheli.cfg`. The compiled command class exposes the following subcommands:

```text
sendss, modlist, reconfig, title, fill, status, killentity, removeentity, attackentity, showboundingbox, list
```

## Permissions

Command access is controlled by `CommandPermission` entries in `mcheli.cfg`.

Important behavior verified from the command implementation:

- If a sender cannot use a subcommand, the command returns Minecraft's generic permission error.
- Permission checks compare the subcommand name and player names from the config.
- Server operators should not assume all `/mcheli` subcommands are harmless; several are destructive or diagnostic tools.

## Command list

### `/mcheli list`

Prints the available MC Helicopter subcommands.

```text
/mcheli list
```

### `/mcheli reconfig`

Reloads `mcheli.cfg` through the mod proxy. On a dedicated server it also sends updated server settings to clients.

```text
/mcheli reconfig
```

Use this after changing reloadable server-side settings. A full restart is still safer after large config or modpack changes.

### `/mcheli showboundingbox <true|false>`

Toggles `EnableDebugBoundingBox` and sends updated server settings to clients.

```text
/mcheli showboundingbox true
/mcheli showboundingbox false
```

When enabled, the command reports `Enabled bounding box [F3 + b]`.

### `/mcheli title <timeSeconds> <position> <jsonMessage>`

Sends a JSON chat-component title packet to clients.

```text
/mcheli title 5 2 {"text":"Mission start","color":"gold"}
```

Verified constraints:

- `timeSeconds` is clamped from `1` to `180`.
- The implementation accepts positions starting at `0` and clamps high values to `5`, although its error text says `position[0~4]`.
- `jsonMessage` must be valid Minecraft JSON chat-component syntax.

### `/mcheli status <entity|tile> [minNum]`

Prints grouped server-loaded entity or tile-entity counts.

```text
/mcheli status entity
/mcheli status entity 10
/mcheli status tile
/mcheli status tile 5
```

Use this for lag investigations or to find unexpectedly numerous entity classes.

### `/mcheli killentity <entityClassNameFragment>`

Kills loaded entities whose class name contains the supplied string.

```text
/mcheli killentity EntityBat
/mcheli killentity minecraft.entity.passive
```

This is destructive. Test with `/mcheli status entity` first.

### `/mcheli removeentity <entityClassNameFragment>`

Removes loaded entities whose class name contains the supplied string.

```text
/mcheli removeentity EntityItem
/mcheli removeentity mcheli.weapon
```

This bypasses normal combat/death behavior and should be limited to trusted administrators.

### `/mcheli attackentity <entityClassNameFragment> <damage> [damageSource]`

Applies damage to matching loaded entities.

```text
/mcheli attackentity EntityZombie 10 generic
/mcheli attackentity EntityPlayer 2 magic
```

Recognized damage sources include:

```text
player, anvil, cactus, drown, fall, fallingblock, generic, infire, inwall, lava, magic, onfire, starve, wither
```

If `player` is used by a player sender, the damage source is attributed to that player.

### `/mcheli fill <x1> <y1> <z1> <x2> <y2> <z2> <blockName> [metadata] [oldBlockHandling] [dataTag]`

A mod-provided fill command similar to Minecraft setblock/fill behavior.

```text
/mcheli fill ~-5 ~ ~-5 ~5 ~3 ~5 minecraft:air 0 destroy
/mcheli fill 0 64 0 10 70 10 minecraft:stone 0 replace
```

Verified behavior:

- Supports relative coordinates.
- Supports `replace`, `keep`, `destroy`, and `override` handling.
- Supports optional tile-entity NBT data tags.
- Refuses very large operations above the implementation's block limit (`327680`).

This is destructive and should be restricted.

### `/mcheli sendss <playerName>`

Sends a client packet to the named player. The command name and packet id indicate screenshot/request behavior.

```text
/mcheli sendss PlayerName
```

Because the repository only includes compiled classes, the exact client-side result could not be fully documented without runtime testing.

### `/mcheli modlist <playerName>`

Requests or displays mod-list information for the named player via the multiplayer packet handler.

```text
/mcheli modlist PlayerName
```

Because the repository only includes compiled classes, the exact client-side UI/report format could not be fully documented without runtime testing.

## Recommended permission policy

For public servers:

- Give `list`, `status`, and possibly `modlist` only to moderators/admins.
- Give `reconfig` only to owners or senior admins.
- Give `fill`, `killentity`, `removeentity`, `attackentity`, and `showboundingbox` only to trusted technical admins.
- Avoid giving `sendss` to general staff unless your community rules clearly disclose what it does.
