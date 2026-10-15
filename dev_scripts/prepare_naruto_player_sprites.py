"""Pack supplied Naruto frames for the player-sprite test (requires Pillow).

Run from any directory. Source reference PNGs are never modified.
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'references/naruto_rpg/processed'
# Emerald order: south/north/west idle, then two steps in each direction.
# East uses the engine's horizontal flip. Running reuses these steps at its
# existing faster timing; no separate running artwork is supplied.
FRAMES = (
    'x013_y020', 'x013_y132', 'x015_y057',
    'x033_y021', 'x069_y021', 'x034_y133',
    'x071_y133', 'x033_y058', 'x071_y058',
)


def indexed(image):
    """Reserve index zero for transparency and preserve source colors exactly."""
    pixels = list(image.getdata())
    colors = sorted({p[:3] for p in pixels if p[3]})
    if len(colors) > 15:
        raise ValueError(f'Expected at most 15 opaque colors, got {len(colors)}')
    palette = [(0, 0, 0)] + colors
    palette += [(0, 0, 0)] * (16 - len(palette))
    lookup = {color: i + 1 for i, color in enumerate(colors)}
    result = Image.new('P', image.size, 0)
    result.putpalette([channel for color in palette for channel in color])
    result.putdata([lookup[p[:3]] if p[3] else 0 for p in pixels])
    result.info['transparency'] = 0
    return result, palette


def save(image, png_path, pal_path):
    result, palette = indexed(image)
    png_path.parent.mkdir(parents=True, exist_ok=True)
    pal_path.parent.mkdir(parents=True, exist_ok=True)
    result.save(png_path, bits=4, transparency=0)
    pal_path.write_text('JASC-PAL\n0100\n16\n' + ''.join(
        f'{r} {g} {b}\n' for r, g, b in palette), encoding='ascii')
    print(f'{png_path.relative_to(ROOT)}: {result.size}, {len(set(result.getdata()))} indices')


def main():
    sheet = Image.new('RGBA', (32 * 18, 32))
    for i, frame in enumerate(FRAMES * 2):
        sprite = Image.open(SOURCE / 'overworld_sprites/naruto' /
                            f'naruto_overworld_pose_{frame}.png').convert('RGBA')
        assert sprite.width <= 32 and sprite.height <= 32
        # Bottom alignment keeps foot placement stable across the source crops.
        sheet.paste(sprite, (i * 32 + (32 - sprite.width) // 2, 32 - sprite.height))
    save(sheet, ROOT / 'graphics/object_events/pics/people/naruto/walking_running.png',
         ROOT / 'graphics/object_events/palettes/naruto.pal')

    pose = Image.open(SOURCE / 'battle_sprites/naruto/naruto_battle_pose_x600_y020.png').convert('RGBA')
    # Fit the complete pose inside the 64x64 introduction slot without smoothing.
    pose = pose.resize((35, 56), Image.Resampling.NEAREST)
    intro = Image.new('RGBA', (64, 64))
    intro.paste(pose, ((64 - pose.width) // 2, 64 - pose.height))
    save(intro, ROOT / 'graphics/trainers/front_pics/naruto.png',
         ROOT / 'graphics/trainers/palettes/naruto.pal')


if __name__ == '__main__':
    main()
