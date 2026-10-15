# Naruto-GBA agent instructions

## Purpose and current scope

Naruto-GBA is a planned turn-based Naruto RPG built on Pokéemerald Expansion.
The current phase is repository initialization only. Wait for explicit development
instructions before implementing gameplay or making technical design decisions.

During initialization:
- Add only missing documentation placeholders and reference directories.
- Do not change existing source code, mechanics, assets, configuration, or build files.
- Do not implement chakra natures, shinobi, jutsu, recruitment, or other game features.
- Do not install dependencies or rename or reorganize existing directories.
- Keep existing Pokéemerald Expansion files and functionality unchanged.

## Repository organization

Reuse the engine's existing structure rather than introducing parallel systems:
- `src/`: C engine and battle logic; `src/data/` also contains game data.
- `include/`: headers, including configuration in `include/config/` and constants
  in `include/constants/`.
- `data/`: maps, layouts, scripts, text, tilesets, and assembly data.
- `graphics/` and `sound/`: visual and audio assets.
- `test/`: existing tests, including battle and compression tests.
- `asm/`, `constants/`, and `libagbsyscall/`: existing engine support files.
- `tools/`, `dev_scripts/`, and `migration_scripts/`: existing tooling.
- `docs/`: upstream documentation and Naruto-specific planning placeholders.
- `references/naruto_rpg/`, `references/konoha_senki/`, and
  `references/ninja_council/`: reserved reference-asset locations.

Keep `.gitkeep` files in otherwise empty reference directories so Git can retain
them. These directories are not currently integrated into the game build.

## Conventions for subsequent authorized work

- Read applicable repository instructions and the relevant existing files first.
- Follow nearby code, naming, data, and asset conventions; avoid unrelated edits.
- Consult `README.md`, `INSTALL.md`, `CONTRIBUTING.md`, and existing documentation
  for upstream workflows. Preserve upstream credits and configuration.
- Preserve build compatibility. Use existing build and test workflows appropriate
  to authorized changes; report checks performed and any unverified results.
- Keep `docs/GAME_DESIGN.md` and `docs/ARCHITECTURE.md` as placeholders until
  decisions are explicitly established. Do not invent mechanics or architecture.
- Do not change Git remotes merely because a folder or project name differs.
- Check `.gitignore` and Makefile cleanup rules before adding reference assets:
  some asset extensions are globally ignored or matched by recursive cleanup.
