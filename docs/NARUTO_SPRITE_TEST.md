# Naruto player sprite test

Branch: `codex/naruto-player-sprite-test`.

The male new-game introduction uses a separate 64x64 Naruto trainer picture.
The male player on foot uses Naruto frames in 32x32 cells, preserving the source
pixel detail. May, the Brendan rival, and all original graphics remain intact.
The new trainer picture is appended to the registry, preserving existing IDs.

## Source artwork

All sources are under `references/naruto_rpg/processed/`:
- Introduction: `battle_sprites/naruto/naruto_battle_pose_x600_y020.png`.
- Overworld: nine frames from `overworld_sprites/naruto/`, listed in
  `dev_scripts/prepare_naruto_player_sprites.py` in engine animation order.

The preparation script preserves source colors, reserves palette index zero for
transparency, and emits four-bit indexed PNGs with matching 16-entry JASC palettes.
The introduction pose is resized with nearest-neighbor sampling to 35x56 pixels
and placed inside the existing 64x64 slot. Walking frames retain native resolution.
The prepared PNGs and palettes build with the existing engine tools; Pillow is
needed only to regenerate them. The source reference files are not modified.

## Test scope

Running reuses walking frames with the existing faster animation timing.
Bike, surfing, fishing, field-move, and battle-back sprites remain Brendan for
this initial on-foot/intro test. No game mechanics or gender-selection logic changes.

Build with `make -j4` in the Ubuntu checkout. In an emulator, start a new game,
toggle between male and female during the introduction, and verify Naruto and
unchanged May respectively. Select male and check idle, walking, turning, and
running in all four directions; select female in a separate new game to verify
her normal sprites. Existing saves can test movement but skip the introduction.

## Validation performed

- Ubuntu `make -j4` completed and produced `pokeemerald.gba`.
- Both generated PNGs use four-bit indexed color with transparent index zero
  and matching 16-entry palettes.
- Compiled tile bytes were decoded and matched pixel-for-pixel to the indexed PNGs.
- All pre-existing graphics files match Git HEAD, including all female artwork.
- `git diff --check` passed. Emulator playthrough has not been performed.
