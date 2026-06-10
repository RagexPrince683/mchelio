# Server Administration Guide

MC Helicopter Overdrive+ can be server-friendly, but its vehicle count, projectile count, explosions, and administrative commands require deliberate configuration.

## Install requirements

- Run a Minecraft 1.7.10 Forge server.
- Install the same MC Helicopter Overdrive+ package on the server and all clients.
- Install required dependencies on both sides.
- Distribute the same asset/config pack to clients when running a curated server.

## First-launch checklist

1. Start the server once to generate `config/mcheli.cfg`.
2. Stop the server.
3. Review destructive options:
   - `Explosion_DestroyBlock`
   - `Explosion_FlamingBlock`
   - `Collision_DestroyBlock`
   - car/tank breakable block and material lists
4. Review economy/survival options:
   - `ItemFuel`
   - `ItemDamage`
   - `InfinityAmmo`
   - `InfinityFuel`
   - recipe toggles
5. Review command access:
   - `EnableCommand`
   - `CommandPermission`
6. Restart and test with a small group before opening the server.

## Destructive gameplay controls

If your world should not be heavily griefable, consider:

- Disable explosion block damage.
- Disable explosion fire.
- Disable collision block destruction.
- Restrict vehicles/weapons through recipes, permissions, claims, or external protection mods.
- Keep administrative entity commands restricted.

## Performance controls

Potentially high-impact systems include:

- Large numbers of projectiles and bomblets.
- Many vehicles with active weapons, radar, or AI/seat entities.
- Long render distances and high LOD settings on clients.
- Large `/mcheli fill` operations.
- Entity accumulation from battles.

Useful tools/settings:

- `/mcheli status entity [minNum]`
- `/mcheli status tile [minNum]`
- `/mcheli removeentity <classFragment>` for emergency cleanup
- `EnableAircraftLODRender`
- `AircraftLODStartDistance`
- `AircraftLODFarDistance`
- `RenderDistanceWeight`
- `MobRenderDistanceWeight`
- `DespawnCount`

## Multiplayer command policy

Recommended access:

| Staff role | Suggested commands |
| --- | --- |
| Helper | none, or `list` only |
| Moderator | `list`, `status` |
| Admin | `list`, `status`, `reconfig`, `showboundingbox` |
| Technical owner | all commands, including destructive commands |

Be especially careful with `fill`, `killentity`, `removeentity`, and `attackentity`.

## Client expectations

Players should be told to:

- Use the exact modpack version required by the server.
- Keep Dynamic FOV enabled for zoom behavior.
- Disable OptiFine Fast Render if thermal/vision effects break.
- Report key conflicts and remap controls before combat events.

## Updating a server

1. Back up the world, configs, and current mod files.
2. Read release notes for dependency changes.
3. Replace the mod on server and clients together.
4. Compare new generated config options against your existing `mcheli.cfg`.
5. Test recipes, critical vehicles, and major weapons in a staging world.
