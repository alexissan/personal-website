from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
import qrcode

ROOT = Path(__file__).resolve().parents[2]
BRAND = ROOT / 'brand'
CAMPAIGN = BRAND / 'campaigns/local-business-es'

for name, file in [('Display', 'Manrope-800.ttf'), ('Body', 'DMSans-400.ttf'), ('Medium', 'DMSans-600.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(BRAND / 'fonts' / file)))

W, H = 148.5 * mm, 210 * mm
SITE = 'https://alexissantos.dev/'
WHATSAPP = 'https://wa.me/34681159057'


def text(c, value, x, top, size=11, font='Body', gray=0):
    c.setFont(font, size)
    c.setFillGray(gray)
    c.drawString(x, H - top, value)


def qr(c, value, x, top, size):
    code = qrcode.QRCode(border=4, error_correction=qrcode.constants.ERROR_CORRECT_M)
    code.add_data(value)
    code.make(fit=True)
    matrix = code.get_matrix()
    unit = size / len(matrix)
    c.setFillGray(0)
    for row, values in enumerate(matrix):
        for col, on in enumerate(values):
            if on:
                c.rect(x + col * unit, H - top - (row + 1) * unit, unit, unit, fill=1, stroke=0)
    c.linkURL(value, (x, H - top - size, x + size, H - top), relative=0, thickness=0)


def small_icon(c, kind, x, top):
    c.saveState()
    c.translate(x, H - top)
    c.setLineWidth(1.2)
    c.setStrokeGray(0)
    if kind == 'process':
        c.roundRect(0, -18, 18, 18, 2, stroke=1, fill=0)
        c.line(4, -5, 14, -5)
        c.line(4, -9, 11, -9)
        c.line(4, -13, 13, -13)
    elif kind == 'connect':
        c.circle(3, -9, 2.5, stroke=1, fill=0)
        c.circle(17, -3, 2.5, stroke=1, fill=0)
        c.circle(17, -15, 2.5, stroke=1, fill=0)
        c.line(5.5, -8, 14.5, -4)
        c.line(5.5, -10, 14.5, -14)
    else:
        c.line(0, -9, 7, -3)
        c.line(0, -9, 7, -15)
        c.line(18, -9, 11, -3)
        c.line(18, -9, 11, -15)
    c.restoreState()


def flyer(c):
    c.saveState()
    c.setFillGray(1)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.drawImage(str(CAMPAIGN / 'background.png'), 0, H - 270, width=W, height=270, mask='auto')

    c.drawImage(str(BRAND / 'logos/logo-black.png'), 29, H - 48, width=245, height=31, mask='auto')

    text(c, 'INTEGRACIÓN DE IA PARA NEGOCIOS', 31, 73, 8.5, 'Medium')
    text(c, 'La IA hace', 28, 116, 38, 'Display')
    text(c, 'el trabajo', 28, 158, 38, 'Display')
    text(c, 'repetitivo.', 28, 200, 38, 'Display')
    text(c, 'Facturas, documentos, informes y procesos internos.', 31, 238, 10.5, 'Medium')

    c.setFillGray(.92)
    c.roundRect(29, H - 307, W - 58, 38, 4, fill=1, stroke=0)
    text(c, 'DOCUMENTO  →  IA  →  REVISIÓN  →  RESULTADO', 43, 291, 9, 'Medium')

    text(c, 'Soluciones hechas para tu forma de trabajar.', 31, 340, 16, 'Display')
    rows = [
        (374, 'process', 'Automatizo procesos repetitivos'),
        (410, 'connect', 'Integro IA con tus herramientas'),
        (446, 'software', 'Creo la web o app que haga falta'),
    ]
    for top, kind, heading in rows:
        small_icon(c, kind, 32, top - 3)
        text(c, heading, 68, top + 8, 13, 'Medium')

    c.setStrokeGray(0)
    c.setLineWidth(1.2)
    c.line(31, H - 475, W - 31, H - 475)
    text(c, '¿Qué tarea te quita tiempo?', 31, 506, 17, 'Display')
    text(c, '+34 681 159 057', 31, 535, 21, 'Display')
    text(c, 'Llamadas y WhatsApp', 31, 553, 9.5)
    text(c, 'alexissantos.dev', 31, 580, 15, 'Display')
    qr(c, WHATSAPP, 315, 493, 75)
    text(c, 'WhatsApp', 329, 580, 8.5, 'Medium')

    c.linkURL('tel:+34681159057', (31, H - 541, 250, H - 516), relative=0, thickness=0)
    c.linkURL(SITE, (31, H - 586, 224, H - 565), relative=0, thickness=0)
    c.restoreState()


for name, two_up in [('flyer-a5-es-blanco-negro.pdf', False), ('imprimir-a4-dos-flyers.pdf', True)]:
    size = (297 * mm, H) if two_up else (W, H)
    c = canvas.Canvas(str(CAMPAIGN / name), pagesize=size)
    c.setTitle('Integración de IA para negocios | AlexisSantos.dev')
    c.setAuthor('Alexis Santos')
    flyer(c)
    if two_up:
        c.saveState()
        c.translate(W, 0)
        flyer(c)
        c.restoreState()
        c.setStrokeGray(.6)
        c.setLineWidth(.3)
        c.setDash(2, 4)
        c.line(W, 5 * mm, W, H - 5 * mm)
    c.showPage()
    c.save()

print(CAMPAIGN)
