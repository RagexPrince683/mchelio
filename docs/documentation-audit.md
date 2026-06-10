# Documentation Audit Notes

This file records what was discovered during the documentation pass and what could not be fully completed from the repository alone.

## Sources inspected

- `README.md`
- `mcmod.info`
- `mcheli/MCH_Config.class`
- `mcheli/command/MCH_Command.class`
- `assets/mcheli/readme_aircraftEN.txt`
- `assets/mcheli/readme_weaponEN.txt`
- `assets/mcheli/readme_hudEN.txt`
- Asset directories under `assets/mcheli/`
- Existing `docs/plane_flight_tuning.md`

## Undocumented or under-documented features discovered

The previous README focused mostly on download links and old manual installation notes. The following systems are now documented at least at a user/admin level:

- `/mcheli` command tree: `sendss`, `modlist`, `reconfig`, `title`, `fill`, `status`, `killentity`, `removeentity`, `attackentity`, `showboundingbox`, and `list`.
- Command permission control through `CommandPermission` and `EnableCommand`.
- Debug bounding-box toggle through `/mcheli showboundingbox` and `EnableDebugBoundingBox`.
- Entity and tile-entity diagnostics with `/mcheli status`.
- Destructive entity maintenance commands for attack/kill/remove.
- MC Helicopter fill command and its block limit.
- Server-side reload command `/mcheli reconfig`.
- JSON title broadcast command.
- Client/server expectation that both sides need the mod/assets.
- Large asset inventory counts by category.
- Extended asset-author entry points for vehicle, weapon, HUD, and plane flight tuning files.
- Overdrive-specific configuration fields visible in the compiled config class, including multi-threaded model loading, delayed range loader, bomblet loader, wrench drop behavior, auto repair toggle, and placement timer.
- LOD/rendering settings and marker/range-finder settings exposed by config fields.
- Rack/carrier and multi-seat asset concepts from the included aircraft readme.
- Weapon groups, sights, target pods, dispensers, and multiple projectile/munition types from the included weapon readme.

## Documentation gaps that remain

These gaps require runtime testing, original source comments, or a generated config file from a working Minecraft 1.7.10 Forge instance:

1. **Exact generated `mcheli.cfg` comments and ordering.** The repository contains compiled classes but not a generated config sample.
2. **Exact default values for every config field.** Many defaults were verified from bytecode, but not every value was practical to decode cleanly without source/decompiler support.
3. **Client-side behavior of `/mcheli sendss`.** The command sends a client packet, but the precise user-facing result needs runtime verification.
4. **Client-side report format of `/mcheli modlist`.** The command path is visible, but final display/output needs runtime verification.
5. **Complete keybind name mapping for all LWJGL codes.** Common defaults were documented, but a complete control screen export would be more user-friendly.
6. **Full crafting progression.** Item and recipe config files exist, but an end-to-end survival crafting guide needs in-game verification.
7. **Dependency matrix.** `mcmod.info` declares `hbm`; exact compatible versions for Ragex Nuclear Tech / HBM forks should be maintained per release.
8. **Screenshots.** No current screenshots are tracked in the repository.
9. **Known incompatibilities.** Existing caveats were preserved, but each should be retested against current third-party mod versions.
10. **Complete API/developer documentation.** The repository contains compiled classes and asset configs, not full Java source suitable for stable API docs.

## Recommended follow-up work

- Add a generated `docs/examples/mcheli.cfg` from a clean 1.7.10 Forge launch.
- Add screenshots under `docs/images/` and reference them from the README.
- Add a concise survival crafting progression guide after testing recipes in game.
- Add a compatibility table for dependency versions used by each published release.
- If Java source becomes available, generate complete config and API docs from source comments.
