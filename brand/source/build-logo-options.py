from pathlib import Path
import re
B=Path(__file__).resolve().parents[1]
(B/'explorations').mkdir(exist_ok=True)
word=(B/'logos/wordmark-charcoal.svg').read_text()
word=re.sub(r'<circle[^>]*/>','',word)
options=[
('01','Soft a','A rounded initial. Simple, personal and easy to recognise.', '<path d="M73 48a25 25 0 1 0-25 25c14 0 25-11 25-25V27v39q0 12 12 12"/>'),
('02','Continuous s','One flowing stroke. A softer signature for Santos.', '<path d="M77 25C64 12 30 13 25 32C19 54 75 40 74 62C73 83 37 88 21 71"/>'),
('03','Open orbit','An open circle with a small starting point. Quiet and spacious.', '<path d="M76 67a33 33 0 1 1 2-35"/><circle cx="79" cy="48" r="7" fill="currentColor" stroke="none"/>'),
('04','Rising a','An arched initial with a round crossbar. Bold at small sizes.', '<path d="M19 78L36 28Q48 8 60 28L77 78"/><path d="M32 59H65"/>'),
('05','Twin loops','Two linked curves. A more expressive studio symbol.', '<path d="M48 48C21 10 6 31 17 49C24 62 38 53 48 48C75 10 90 31 79 49C72 62 58 53 48 48C21 86 6 65 17 47C24 34 38 43 48 48C75 86 90 65 79 47C72 34 58 43 48 48Z" stroke-width="9"/>'),
('06','Wave','Two rounded waves. An abstract nod to movement and the islands.', '<path d="M16 39C27 18 39 18 50 39S73 60 84 39M12 64C23 43 35 43 46 64S69 85 80 64"/>')]
cards=[]
for num,name,desc,body in options:
 mark=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96" fill="none" stroke="currentColor" stroke-width="12" stroke-linecap="round" stroke-linejoin="round" aria-label="{name}">{body}</svg>'
 (B/'explorations'/f'{num}-symbol.svg').write_text(mark.replace('currentColor','#20242B'))
 wordinner=word.split('>',1)[1].rsplit('</svg>',1)[0]
 vb=re.search(r'viewBox="([^"]+)"',word).group(1)
 lockup=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 100"><g color="#20242B">{mark}</g></svg>'
 (B/'explorations'/f'{num}-logo.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 100"><svg x="0" y="4" width="90" height="90" viewBox="0 0 96 96" fill="none" stroke="#20242B" stroke-width="12" stroke-linecap="round" stroke-linejoin="round">{body.replace("currentColor","#20242B")}</svg><svg x="120" y="10" width="690" height="82" viewBox="{vb}">{wordinner}</svg></svg>')
 cards.append(f'<article><div class="top"><span>{num}</span><h2>{name}</h2></div><div class="hero">{mark}</div><img class="lockup" src="{num}-logo.svg" alt="{name} with AlexisSantos.dev"><div class="samples"><div class="reverse">{mark}</div><div class="small">{mark}</div><a href="{num}-logo.svg" download>Download SVG</a></div><p>{desc}</p></article>')
html='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Six logo directions · AlexisSantos.dev</title><style>
@font-face{font-family:Manrope;src:url('/assets/studio/Manrope.woff2');font-weight:200 800}@font-face{font-family:DM;src:url('/assets/studio/DMSans.woff2');font-weight:100 1000}*{box-sizing:border-box}body{margin:0;background:#f5f6f8;color:#20242b;font:16px/1.5 DM,sans-serif}header,main,footer{max-width:1440px;margin:auto;padding:30px 48px}header{display:flex;justify-content:space-between;align-items:center}header img{width:225px}a{color:inherit;text-underline-offset:5px}h1{font:800 clamp(36px,5vw,68px)/1.08 Manrope,sans-serif;letter-spacing:-.055em;margin:12px 0 20px}.intro{color:#606977;max-width:620px;margin-bottom:40px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}article{background:#fff;padding:25px 28px 20px;border-radius:18px}.top{display:flex;gap:12px;align-items:center}.top span{color:#606977;font-size:13px}h2{font:800 19px Manrope,sans-serif;letter-spacing:-.03em;margin:0}.hero{height:155px;display:grid;place-items:center}.hero svg{width:112px;height:112px}.lockup{display:block;width:100%;height:42px;object-fit:contain}.samples{display:flex;align-items:center;gap:20px;margin-top:22px}.reverse{background:#20242b;color:white;width:55px;height:55px;border-radius:50%;display:grid;place-items:center}.reverse svg{width:35px;height:35px}.small svg{width:22px;height:22px;display:block}.samples a{margin-left:auto;font-size:11px;color:#606977}article p{font-size:13px;line-height:1.5;color:#606977;margin:18px 0 0;min-height:40px}footer{font-size:13px;color:#606977;padding-top:10px;padding-bottom:40px}a:focus-visible{outline:2px solid #496f99;outline-offset:5px}@media(max-width:950px){.grid{grid-template-columns:repeat(2,1fr)}header,main,footer{padding-left:24px;padding-right:24px}}@media(max-width:580px){.grid{grid-template-columns:1fr}header img{width:175px}header a{font-size:12px}.hero{height:170px}}
</style></head><body><header><img src="../logos/wordmark-charcoal.svg" alt="AlexisSantos.dev"><a href="../">Brand kit</a></header><main><h1>Less square.<br>More personality.</h1><p class="intro">Six directions for the studio. Each one shown on its own, with the name, in reverse and at a small size.</p><div class="grid">'''+''.join(cards)+'''</div></main><footer>Logo studies · September 2026 · The current brand kit is unchanged.</footer></body></html>'''
(B/'explorations/index.html').write_text(html)
