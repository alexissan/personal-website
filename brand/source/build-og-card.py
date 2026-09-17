import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

B = Path(__file__).resolve().parents[1]
ROOT = B.parent
OUT = Path(os.environ.get('OG_OUT', ROOT / 'assets/studio'))
VARIANT = os.environ.get('OG_VARIANT', 'dark')
W, H = 1200, 630
SCALE = 2

INK = '#20242B'; PEARL = '#F5F6F8'; SLATE = '#606977'; BLUE = '#496F99'; MIST = '#DCE0E6'
THEMES = {
    'light': dict(bg=PEARL, motif='#E7EAEF', logo='logo-charcoal.png', headline=INK, sub=SLATE, url=INK),
    'dark': dict(bg=INK, motif='#2A2F38', logo='logo-white.png', headline='#FFFFFF', sub=MIST, url=PEARL),
}
COPY = {
    'es': dict(lines=['IA integrada.', 'Software a medida.'], sub='Consultoría y desarrollo · Entre Tenerife y Londres'),
    'en': dict(lines=['Integrated AI.', 'Custom software.'], sub='Consulting and development · Between Tenerife and London'),
}


def font(name, size):
    return ImageFont.truetype(str(B / 'fonts' / name), size * SCALE)


def tinted(path, color, height):
    mark = Image.open(path).convert('RGBA')
    ratio = height / mark.height
    mark = mark.resize((round(mark.width * ratio), height), Image.LANCZOS)
    fill = Image.new('RGBA', mark.size, color)
    fill.putalpha(mark.getchannel('A'))
    return fill


def card(lang, theme):
    t = THEMES[theme]
    c = COPY[lang]
    img = Image.new('RGB', (W * SCALE, H * SCALE), t['bg'])
    motif = tinted(B / 'logos/symbol-charcoal.png', t['motif'], 760 * SCALE)
    img.paste(motif, (600 * SCALE, 150 * SCALE), motif)
    logo = Image.open(B / 'logos' / t['logo']).convert('RGBA')
    logo = logo.resize((round(logo.width * 80 * SCALE / logo.height), 80 * SCALE), Image.LANCZOS)
    img.paste(logo, (80 * SCALE, 76 * SCALE), logo)
    d = ImageDraw.Draw(img)
    display = font('Manrope-800.ttf', 88)
    y = 318
    for line in c['lines']:
        d.text((78 * SCALE, y * SCALE), line, font=display, fill=t['headline'], anchor='ls')
        y += 100
    d.text((80 * SCALE, 492 * SCALE), c['sub'], font=font('DMSans-400.ttf', 25), fill=t['sub'], anchor='ls')
    d.text((80 * SCALE, 556 * SCALE), 'alexissantos.dev', font=font('DMSans-600.ttf', 26), fill=t['url'], anchor='ls')
    d.ellipse([(1096 * SCALE, 539 * SCALE), (1120 * SCALE, 563 * SCALE)], fill=BLUE)
    return img.resize((W, H), Image.LANCZOS)


OUT.mkdir(parents=True, exist_ok=True)
for lang in sys.argv[1:] or COPY:
    path = OUT / f'og-{lang}.jpg'
    card(lang, VARIANT).save(path, 'JPEG', quality=90, optimize=True, progressive=True)
    print(path, path.stat().st_size, 'bytes')
