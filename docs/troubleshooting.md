# Troubleshooting and FAQ

## The game crashes or the mod does not load

Check these first:

1. Are you using Minecraft 1.7.10?
2. Are you using Forge for Minecraft 1.7.10?
3. Is the dependency mod required by your release installed?
4. Is the package layout intact, with both `mcheli/` classes and `assets/mcheli/` assets available?
5. Are client and server using the same mod version?

## Vehicles are invisible or missing textures

- Confirm `assets/mcheli/models/` and `assets/mcheli/textures/` are present.
- Confirm the asset folder was not separated from the compiled classes.
- Try Minecraft's resource-pack reload flow.
- Check for missing or renamed texture references in the vehicle text file.

## Sounds do not play

- Confirm `assets/mcheli/sounds/` and `assets/mcheli/sounds.json` exist.
- Some weapon sound files are optional according to the bundled weapon readme, but missing vehicle sounds may still reduce immersion.
- Restart the client after replacing sound files.

## Zoom or optics feel broken

- Keep Minecraft Dynamic FOV enabled.
- Check keybind conflicts for zoom and camera controls.
- If using OptiFine, disable Fast Render when thermal or visual effects break.

## Thermal/night vision effects are broken

- Disable OptiFine Fast Render.
- Test without shader/resource-pack changes.
- Check whether the specific vehicle asset actually enables night vision or special HUD behavior.

## I cannot use `/mcheli` commands

- Confirm `EnableCommand=true` in `mcheli.cfg`.
- Confirm your player name is allowed by the relevant `CommandPermission` entry.
- Use `/mcheli list` to verify command registration.

## Explosions or collisions are damaging too much terrain

Review:

- `Explosion_DestroyBlock`
- `Explosion_FlamingBlock`
- `Collision_DestroyBlock`
- `Collision_Car_BreakableBlock`
- `Collision_Car_BreakableMaterial`
- `Collision_Tank_BreakableBlock`
- `Collision_Tank_BreakableMaterial`
- Weapon-specific `ExplosionBlock` values in `assets/mcheli/weapons/`

## Server TPS drops during battles

- Use `/mcheli status entity 10` to find high-count entities.
- Clean up problematic entity classes with `/mcheli removeentity <classFragment>` only when you are certain what will be removed.
- Reduce destructive projectile spam through recipes, rules, or weapon availability.
- Consider client render/LOD settings for FPS issues.

## Crafting recipes do not appear or are not desired

- Check the recipe toggles in `mcheli.cfg`.
- Confirm the Drafting Table is available and enabled.
- For curated packs, consider using external recipe-management mods compatible with Minecraft 1.7.10.

## Can I install this only on the client?

No for normal multiplayer gameplay. The server needs the mod for entities, weapons, recipes, commands, and gameplay logic. Clients need it for controls, rendering, HUDs, sounds, and assets.

## Can I use this in a modpack?

Review the distribution terms of the release page you downloaded from and any dependency mods. This repository documents technical setup, not legal redistribution permissions.
