from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
COPY = {
'es': {
 'title':'AlexisSantos.dev — Estudio de desarrollo web, apps e IA', 'description':'Diseño y desarrollo web, aplicaciones e inteligencia artificial para negocios locales. Un estudio independiente en Tenerife, liderado por Alexis Santos.',
 'nav':['Proyectos','Servicios','Estudio','Hablemos'], 'skip':'Ir al contenido', 'menu':'Menú',
 'hero':'Diseño con intención.<br>Tecnología con impacto.', 'intro':'Webs, aplicaciones e inteligencia artificial para hacer crecer tu negocio.', 'cta':'Cuéntame tu idea', 'explore':'Explora los proyectos', 'location':'Un estudio independiente. Desde Tenerife.',
 'work':'Ideas que ya están<br>en tus manos.', 'workintro':'Productos propios, hechos con la misma atención al detalle que pondré en el tuyo.',
 'bcat':'Bienestar / iOS', 'bdesc':'Un momento para parar.<br>Y volver a empezar.', 'bdetail':'Respiración guiada para iPhone. Elige un patrón, respira a tu ritmo y encuentra un momento de calma entre una cosa y la siguiente.',
 'lcat':'Fotografía / iOS', 'ldesc':'Menos distracciones.<br>Más mundo.', 'ldetail':'Una cámara minimalista para iPhone. Menos decisiones entre lo que ves y la foto que quieres hacer.', 'view':'Descubrir la app', 'store':'Ver en el App Store', 'close':'Cerrar',
 'services':'Tecnología que<br>trabaja contigo.', 'serviceintro':'Empezamos por lo que necesita tu negocio. Después elegimos las herramientas.',
 'serviceitems': [('Webs que convierten','Una web que explica lo que haces, transmite confianza y facilita que te contacten.','Web corporativa · Tienda online · Reservas'),('Apps a medida','Una herramienta pensada para tus clientes o tu equipo. Sencilla de usar, hecha para tu forma de trabajar.','Aplicaciones iOS · Aplicaciones web'),('IA útil, de verdad','Menos tiempo copiando datos y respondiendo lo mismo. Más tiempo para las personas que hacen crecer tu negocio.','Asistentes · Automatización · Integraciones')],
 'demo':'Tu negocio, en la práctica.', 'demointro':'Aquí podrás probar ejemplos de webs, apps y herramientas de IA para negocios como el tuyo.', 'soon':'Demos en preparación', 'democopy':'Estoy preparando las primeras experiencias interactivas. Mientras tanto, podemos hablar de lo que te gustaría resolver.',
 'process':'De una conversación<br>a algo que funciona.', 'steps':[('Entender','Me cuentas cómo funciona tu negocio, qué te frena y qué quieres conseguir.'),('Dar forma','Definimos una propuesta, el alcance y un primer resultado que puedas ver y probar.'),('Construir y mejorar','Diseño, desarrollo y pruebo contigo. Después del lanzamiento, acordamos los siguientes pasos.')],
 'about':'Detrás del estudio,<br>una persona.', 'abouttext':'Soy Alexis Santos, ingeniero de software y creador de productos. He trabajado como Staff iOS Engineer y Engineering Manager. Hoy combino esa experiencia con herramientas de IA para crear software cuidado, útil y a medida.', 'abouttext2':'Hablarás directamente con la persona que diseña y construye tu proyecto. Desde la primera idea hasta los últimos detalles.', 'abouttag':'Alexis Santos / Tenerife, España',
 'articles':'Ideas desde el taller.', 'articleintro':'Lo que aprendo construyendo productos, trabajando con IA y llevando ideas a la práctica.', 'allarticles':'Todos los artículos', 'english':'Artículo en inglés',
 'contact':'Las buenas ideas<br>empiezan hablando.', 'contactintro':'Cuéntame qué haces y qué te gustaría mejorar. No necesitas tener un documento técnico ni todas las respuestas.', 'name':'Tu nombre', 'business':'Tu negocio', 'need':'¿Qué te gustaría crear o mejorar?', 'placeholder':'Por ejemplo: una web para mi restaurante con reservas, o una herramienta para reducir tareas administrativas.', 'send':'Preparar email', 'emailnote':'Se abrirá tu aplicación de correo con el mensaje preparado. Tú decides cuándo enviarlo.', 'direct':'O escríbeme directamente', 'status':'Tu mensaje está preparado. Si no se ha abierto tu correo, usa el enlace de email de al lado.', 'required':'Nombre y mensaje son obligatorios.', 'footer':'Diseño, código y criterio.', 'back':'Volver arriba', 'privacy':'Este formulario no envía ni almacena tus datos en la web.',
 'subject':'Una idea para mi negocio', 'emailbody':['Hola Alexis,','Soy','Mi negocio es','Me gustaría hablar sobre:'],
},
'en': {
 'title':'AlexisSantos.dev — Web, app & AI development studio', 'description':'Websites, apps and practical AI tools for local businesses. An independent studio in Tenerife, led by Alexis Santos.',
 'nav':['Projects','Services','Studio','Let’s talk'], 'skip':'Skip to content', 'menu':'Menu',
 'hero':'Design with purpose.<br>Technology with impact.', 'intro':'Websites, apps and AI tools to help your business grow.', 'cta':'Tell me about your idea', 'explore':'Explore the projects', 'location':'An independent studio. From Tenerife.',
 'work':'Ideas, brought<br>to life.', 'workintro':'My own products, made with the same attention to detail I’ll bring to yours.',
 'bcat':'Wellbeing / iOS', 'bdesc':'A moment to pause.<br>And start again.', 'bdetail':'Guided breathing for iPhone. Choose a pattern, find your rhythm and make a little room between one thing and the next.',
 'lcat':'Photography / iOS', 'ldesc':'Fewer distractions.<br>More to see.', 'ldetail':'A minimal camera for iPhone. Fewer decisions between what you see and the photo you want to take.', 'view':'Explore the app', 'store':'View on the App Store', 'close':'Close',
 'services':'Technology that<br>works for you.', 'serviceintro':'We start with what your business needs. Then we choose the tools.',
 'serviceitems':[('Websites that convert','A website that explains what you do, builds trust and makes it easy to get in touch.','Business websites · Online stores · Bookings'),('Apps built around you','A tool for your customers or your team. Simple to use, built around the way you work.','iOS apps · Web applications'),('AI with a purpose','Less time copying data and answering the same questions. More time for the people who grow your business.','Assistants · Automation · Integrations')],
 'demo':'Your business, in practice.', 'demointro':'A place to try websites, apps and AI tools built around businesses like yours.', 'soon':'Demos in the making', 'democopy':'I’m preparing the first interactive experiences. In the meantime, we can talk about what you’d like to solve.',
 'process':'From a conversation<br>to something that works.', 'steps':[('Understand','Tell me how your business works, what gets in the way and what you want to achieve.'),('Shape','We agree on a proposal, a scope and a first version you can see and try.'),('Build and improve','I design, develop and test with you. After launch, we agree on the next steps.')],
 'about':'An independent studio.<br>A personal approach.', 'abouttext':'I’m Alexis Santos, a software engineer and product maker. I’ve worked as a Staff iOS Engineer and Engineering Manager. Today I combine that experience with AI tools to build thoughtful, useful software around real needs.', 'abouttext2':'You’ll speak directly with the person designing and building your project. From the first idea to the finishing touches.', 'abouttag':'Alexis Santos / Tenerife, Spain',
 'articles':'Notes from the studio.', 'articleintro':'What I learn building products, working with AI and turning ideas into something real.', 'allarticles':'All articles', 'english':'Article in English',
 'contact':'Good ideas<br>start with a conversation.', 'contactintro':'Tell me what you do and what you’d like to improve. You don’t need a technical brief or all the answers.', 'name':'Your name', 'business':'Your business', 'need':'What would you like to build or improve?', 'placeholder':'For example: a restaurant website with bookings, or a tool to cut down on admin.', 'send':'Prepare email', 'emailnote':'This opens your email app with a draft. You choose when to send it.', 'direct':'Or email me directly', 'status':'Your message is ready. If your email app didn’t open, use the email link alongside the form.', 'required':'Name and message are required.', 'footer':'Design, code and care.', 'back':'Back to top', 'privacy':'This form does not send or store your data on this website.',
 'subject':'An idea for my business', 'emailbody':['Hi Alexis,','My name is','My business is','I’d like to talk about:'],
}}
ARROW='<span aria-hidden="true">↗</span>'
ICONS=['<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c5 5 5 13 0 18-5-5-5-13 0-18Z"/>','<rect x="6" y="2" width="12" height="20" rx="3"/><path d="M10 18h4"/>','<path d="m12 2 3 7 7 3-7 3-3 7-3-7-7-3 7-3Z"/>']
for lang,t in COPY.items():
 url='/' if lang=='es' else '/en/'
 nav=''.join(f'<a href="#{anchor}">{text}</a>' for anchor,text in zip(['projects','services','studio'],t['nav'][:3]))
 services=''.join(f'<article><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[i]}</svg><h3>{name}</h3><p>{desc}</p><small>{tags}</small></article>' for i,(name,desc,tags) in enumerate(t['serviceitems']))
 steps=''.join(f'<li><span class="step-number">0{i+1}</span><h3>{name}</h3><p>{desc}</p></li>' for i,(name,desc) in enumerate(t['steps']))
 html=f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t['title']}</title><meta name="description" content="{t['description']}">
<link rel="canonical" href="https://alexissantos.dev{url}"><link rel="alternate" hreflang="es" href="https://alexissantos.dev/"><link rel="alternate" hreflang="en" href="https://alexissantos.dev/en/"><link rel="alternate" hreflang="x-default" href="https://alexissantos.dev/">
<meta property="og:title" content="{t['title']}"><meta property="og:description" content="{t['description']}"><meta property="og:type" content="website"><meta property="og:url" content="https://alexissantos.dev{url}"><meta property="og:image" content="https://alexissantos.dev/assets/studio/hero.jpg"><meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#f5f6f8">
<link rel="icon" href="/assets/studio/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/studio/studio.css"><script src="/assets/studio/studio.js" defer></script>
</head>
<body id="top"><a class="skip" href="#main">{t['skip']}</a>
<header class="header wrap"><a class="wordmark" href="{url}" aria-label="AlexisSantos.dev"><img src="/assets/studio/logo.svg" alt="AlexisSantos.dev" width="645" height="82"></a><nav class="desktop-nav" aria-label="{'Principal' if lang=='es' else 'Main'}">{nav}</nav><div class="header-actions"><div class="languages" aria-label="{'Idioma' if lang=='es' else 'Language'}"><a href="/" lang="es" aria-label="Español" {'aria-current="page"' if lang=='es' else ''}>ES</a><span>/</span><a href="/en/" lang="en" aria-label="English" {'aria-current="page"' if lang=='en' else ''}>EN</a></div><a class="button small header-cta" href="#contact">{t['nav'][3]}</a><button class="menu-toggle" aria-expanded="false" aria-controls="mobile-nav">{t['menu']} <span aria-hidden="true">＋</span></button></div><nav id="mobile-nav" hidden>{nav}<a href="#contact">{t['nav'][3]}</a></nav></header>
<main id="main"><section class="hero"><div class="hero-inner wrap"><div class="hero-copy"><h1>{t['hero']}</h1><p>{t['intro']}</p><div class="hero-actions"><a class="button" href="#contact">{t['cta']} {ARROW}</a><a class="text-link" href="#projects">{t['explore']} {ARROW}</a></div></div><img class="hero-art" src="/assets/studio/hero.jpg" alt="" width="1536" height="1024" fetchpriority="high"><p class="hero-foot">{t['location']}</p></div></section>
<section id="projects" class="section wrap"><div class="section-head"><h2>{t['work']}</h2><p>{t['workintro']}</p></div><div class="projects"><article class="project breathe"><img class="product-scene" src="/assets/studio/breathe-scene.jpg" alt="" loading="lazy" width="1448" height="1086"><div class="product-copy"><small>{t['bcat']}</small><h3>Breathe Now</h3><p>{t['bdesc']}</p><button class="project-open" aria-label="{t['view']}: Breathe Now" data-dialog="breathe-detail">{t['view']} {ARROW}</button></div><span class="product-bottom">{'Respira. Para. Vuelve.' if lang=='es' else 'Breathe. Reset. Begin again.'}</span></article><article class="project camera"><img class="product-scene" src="/assets/studio/camera-scene.jpg" alt="" loading="lazy" width="1448" height="1086"><div class="product-copy"><small>{t['lcat']}</small><h3>Lean Cam</h3><p>{t['ldesc']}</p><button class="project-open" aria-label="{t['view']}: Lean Cam" data-dialog="camera-detail">{t['view']} {ARROW}</button></div><span class="product-bottom">{'Mira más. Decide menos.' if lang=='es' else 'See more. Do less.'}</span></article></div></section>
<section id="services" class="section wrap services"><div class="section-head"><h2>{t['services']}</h2><p>{t['serviceintro']}</p></div><div class="service-grid">{services}</div></section>
<section class="demo-section"><div class="wrap demo-inner"><div><span class="status-pill"><span></span>{t['soon']}</span><h2>{t['demo']}</h2><p>{t['demointro']}</p></div><div class="demo-note"><div class="demo-shape" aria-hidden="true"><span></span><span></span><span></span></div><p>{t['democopy']}</p><a class="text-link" href="#contact">{t['cta']} {ARROW}</a></div></div></section>
<section class="section wrap process"><h2>{t['process']}</h2><ol>{steps}</ol></section>
<section id="studio" class="section wrap about"><div class="portrait"><img src="/photo.jpg" alt="Alexis Santos" loading="lazy" width="600" height="700"><span>{t['abouttag']}</span></div><div class="about-copy"><h2>{t['about']}</h2><p>{t['abouttext']}</p><p>{t['abouttext2']}</p><div class="social"><a href="https://www.linkedin.com/in/asantosp/">LinkedIn {ARROW}</a><a href="https://github.com/alexissan">GitHub {ARROW}</a><a href="https://x.com/deepfirstsearch">X {ARROW}</a></div></div></section>
<section id="contact" class="contact-section"><div class="wrap contact-grid"><div><h2>{t['contact']}</h2><p class="contact-intro">{t['contactintro']}</p><div class="direct-email"><span>{t['direct']}</span><a href="mailto:alexis.santos.perez@gmail.com">alexis.santos.perez@gmail.com {ARROW}</a></div></div><form id="brief-form"><div class="form-row"><label>{t['name']}<input name="name" autocomplete="name" required maxlength="100"></label><label>{t['business']}<input name="business" autocomplete="organization" maxlength="150"></label></div><label>{t['need']}<textarea name="message" rows="4" required maxlength="3000" placeholder="{t['placeholder']}"></textarea></label><button class="button" type="submit">{t['send']} {ARROW}</button><p class="form-note">{t['emailnote']}</p><p class="privacy-note">{t['privacy']}</p><p id="form-status" role="status"></p><noscript><p>{t['direct']}: <a href="mailto:alexis.santos.perez@gmail.com">alexis.santos.perez@gmail.com</a></p></noscript></form></div></section>
</main><footer class="wrap footer"><div><a class="wordmark" href="{url}"><img src="/assets/studio/logo.svg" alt="AlexisSantos.dev" width="645" height="82"></a><p>{t['footer']}</p></div><span>© 2026 Alexis Santos</span><nav class="footer-links" aria-label="{'Más información' if lang=='es' else 'More information'}"><a href="{'/articles/' if lang=='es' else '/en/articles/'}">{'Artículos' if lang=='es' else 'Articles'}</a><a href="#top">{t['back']} ↑</a></nav></footer>
<dialog id="breathe-detail" aria-labelledby="breathe-title"><button class="dialog-close" aria-label="{t['close']}">×</button><img class="app-icon" src="/breathe-now/icon.png" alt="" width="80" height="80"><small>{t['bcat']}</small><h2 id="breathe-title">Breathe Now</h2><p>{t['bdetail']}</p><a class="button" href="https://apps.apple.com/app/id6757527807">{t['store']} {ARROW}</a></dialog>
<dialog id="camera-detail" aria-labelledby="camera-title"><button class="dialog-close" aria-label="{t['close']}">×</button><small>{t['lcat']}</small><h2 id="camera-title">Lean Cam</h2><p>{t['ldetail']}</p><img class="dialog-photo" src="/lean-cam/photo-1.JPG" alt="{'Fotografía tomada con Lean Cam' if lang=='es' else 'Photography from Lean Cam'}" loading="lazy"><a class="button" href="https://apps.apple.com/app/id6755633580">{t['store']} {ARROW}</a></dialog>
<script type="application/json" id="contact-copy">{json.dumps({k:t[k] for k in ['subject','emailbody','status']},ensure_ascii=False)}</script>
</body></html>'''
 target=ROOT/('index.html' if lang=='es' else 'en/index.html')
 target.parent.mkdir(parents=True, exist_ok=True)
 target.write_text(html)

import re
from html import unescape

english_home = (ROOT / 'en/index.html').read_text()
english_header = re.search(r'<header class="header wrap">.*?</header>', english_home, re.S).group(0)
english_header = english_header.replace('href="#', 'href="/en/#')
english_footer = re.search(r'<footer class="wrap footer">.*?</footer>', english_home, re.S).group(0)
entries = []
for source in sorted((ROOT / 'articles').glob('*/index.html')):
    original = source.read_text()
    slug = source.parent.name
    article = re.search(r'<article>(.*?)</article>', original, re.S).group(1)
    title = unescape(re.sub('<[^>]+>', '', re.search(r'<h1>(.*?)</h1>', article, re.S).group(1)))
    description_match = re.search(r'<meta name="description" content="([^"]+)"', original)
    description = unescape(description_match.group(1)) if description_match else title
    article = re.sub(r'src="(?!https?:|/)([^"]+)"', lambda m: f'src="/articles/{slug}/{m.group(1)}"', article)
    article = re.sub(r'href="/articles([^\"]*)"', r'href="/en/articles\1"', article)
    article = article.replace('href="/"', 'href="/en/"')
    cover = next(source.parent.glob('cover.*'))
    entries.append((slug, title, description, '/articles/' + slug + '/' + cover.name))
    path = f'/en/articles/{slug}/'
    head = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} — AlexisSantos.dev</title><meta name="description" content="{escape(description, quote=True)}"><link rel="canonical" href="https://alexissantos.dev/articles/{slug}/"><meta property="og:title" content="{escape(title, quote=True)}"><meta property="og:type" content="article"><meta property="og:image" content="https://alexissantos.dev/articles/{slug}/{cover.name}"><link rel="icon" href="/assets/studio/favicon.svg"><link rel="stylesheet" href="/assets/studio/studio.css"><script src="/assets/studio/studio.js" defer></script></head>'''
    page = f'{head}<body id="top"><a class="skip" href="#main">Skip to content</a>{english_header}<main id="main" class="reading-page wrap"><a class="text-link" href="/en/articles/">← All articles</a><article class="reading-article">{article}</article><div class="reading-end"><a class="text-link" href="/en/articles/">Explore more articles ↗</a><a class="text-link" href="/en/#contact">Talk about your project ↗</a></div></main>{english_footer}</body></html>'
    destination = ROOT / path.strip('/') / 'index.html'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(page)

order = ['ios-claude-skills-open-source', 'building-is-the-easy-part', '6-apps-3-months-solo-dev', 'claude-code-changed-how-i-ship', 'mcp-at-work', 'evals-for-agents', 'multi-agent-orchestration', 'production-guardrails', 'remote-work']
entries.sort(key=lambda item: order.index(item[0]))
for lang in ['es', 'en']:
    is_es = lang == 'es'
    home_url = '/' if is_es else '/en/'
    archive_url = '/articles/' if is_es else '/en/articles/'
    home = (ROOT / ('index.html' if is_es else 'en/index.html')).read_text()
    header = re.search(r'<header class="header wrap">.*?</header>', home, re.S).group(0).replace('href="#', f'href="{home_url}#')
    header = header.replace('href="/" lang="es"', 'href="/articles/" lang="es"').replace('href="/en/" lang="en"', 'href="/en/articles/" lang="en"')
    footer = re.search(r'<footer class="wrap footer">.*?</footer>', home, re.S).group(0)
    cards = ''.join(f'<a class="article archive-card" href="{archive_url}{slug}/"><img src="{cover}" alt="" loading="lazy" width="600" height="338"><small>{"Artículo en inglés" if is_es else "Article"}</small><h2 lang="en">{escape(title)} ↗</h2></a>' for slug,title,description,cover in entries)
    title = 'Ideas desde el taller' if is_es else 'Notes from the studio'
    intro = COPY[lang]['articleintro']
    back = 'Volver al estudio' if is_es else 'Back to the studio'
    archive = f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} — AlexisSantos.dev</title><meta name="description" content="{intro}"><link rel="canonical" href="https://alexissantos.dev{archive_url}"><link rel="alternate" hreflang="es" href="https://alexissantos.dev/articles/"><link rel="alternate" hreflang="en" href="https://alexissantos.dev/en/articles/"><link rel="icon" href="/assets/studio/favicon.svg"><link rel="stylesheet" href="/assets/studio/studio.css"><script src="/assets/studio/studio.js" defer></script></head><body id="top"><a class="skip" href="#main">{COPY[lang]['skip']}</a>{header}<main id="main" class="wrap archive-page"><div class="archive-intro"><a class="text-link" href="{home_url}">← {back}</a><h1>{title}.</h1><p>{intro}</p></div><div class="article-grid">{cards}</div></main>{footer}</body></html>'''
    (ROOT / archive_url.strip('/') / 'index.html').write_text(archive)

public_paths = ["/", "/en/", "/articles/", "/en/articles/"] + [f"/articles/{entry[0]}/" for entry in entries]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(f"  <url><loc>https://alexissantos.dev{path}</loc></url>" for path in public_paths) + "\n</urlset>\n"
(ROOT / "sitemap.xml").write_text(sitemap)
