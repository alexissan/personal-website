from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
COPY = {
'es': {
 'title':'AlexisSantos.dev — Integración de IA y software a medida', 'description':'Consultoría, integración de inteligencia artificial y software a medida para automatizar procesos reales en empresas y negocios.',
 'nav':['Soluciones','Proyectos','Sobre mí','Hablemos'], 'skip':'Ir al contenido', 'menu':'Menú',
 'hero':'Integro la IA<br>en tu negocio.', 'intro':'Estudio cómo trabajas y construyo una solución a medida: automatización, asistentes, validaciones, informes o software conectado a tus herramientas.', 'cta':'Cuéntame qué quieres mejorar', 'explore':'Ver soluciones', 'location':'Consultoría y desarrollo · Entre Tenerife y Londres',
 'work':'Productos reales.<br>Experiencia aplicada.', 'workintro':'También creo productos propios. Son una muestra de cómo convierto una idea en software útil, cuidado y listo para usar.',
 'bcat':'Bienestar / iOS', 'bdesc':'Un momento para parar.<br>Y volver a empezar.', 'bdetail':'Respiración guiada para iPhone. Elige un patrón, respira a tu ritmo y encuentra un momento de calma entre una cosa y la siguiente.',
 'lcat':'Fotografía / iOS', 'ldesc':'Menos distracciones.<br>Más mundo.', 'ldetail':'Una cámara minimalista para iPhone. Menos decisiones entre lo que ves y la foto que quieres hacer.', 'view':'Descubrir la app', 'store':'Ver en el App Store', 'close':'Cerrar',
 'services':'IA que encaja<br>en tu trabajo.', 'serviceintro':'No empiezo con una herramienta. Empiezo con el proceso que te quita tiempo, genera errores o limita tu negocio.',
 'serviceitems': [('Automatización de procesos','Facturas, documentos, informes y tareas repetitivas que hoy dependen de copiar, revisar y volver a comprobar.','Extracción de datos · Reglas · Validaciones'),('Herramientas inteligentes','Asistentes y agentes que consultan tu información, preparan respuestas y ayudan a tomar decisiones con control humano.','Asistentes internos · Búsqueda · Agentes'),('Software conectado','Cuando hace falta una interfaz, construyo la web o aplicación y la conecto con tus sistemas, datos y servicios de IA.','Aplicaciones web · iOS · Integraciones')],
 'demo':'De una factura<br>a un proceso automático.', 'demointro':'La IA puede leer el documento, extraer los datos, comprobarlos con tus reglas y dejar el resultado preparado para revisión.', 'soon':'Ejemplo de solución', 'democopy':'La solución se integra con las herramientas que ya usas. Los casos dudosos los revisa una persona; lo repetitivo ocurre solo.',
 'flow':['Documento','IA','Reglas','Revisión','Resultado'],
 'process':'Entender. Construir.<br>Integrar.', 'steps':[('Entender el proceso','Veo cómo trabajas hoy, dónde se pierde tiempo y qué decisiones necesitan seguir en manos de una persona.'),('Construir la solución','Creo un primer flujo real con tus documentos, reglas y herramientas. Lo pruebas antes de ampliar el alcance.'),('Integrar y acompañar','Conecto la solución, mido el resultado y la ajusto cuando cambian tus necesidades o tu forma de trabajar.')],
 'about':'Consultoría directa.<br>Ejecución real.', 'abouttext':'Soy Alexis Santos, ingeniero de software y creador de productos. He trabajado como Staff iOS Engineer y Engineering Manager, construyendo sistemas y equipos alrededor de problemas complejos.', 'abouttext2':'Analizo el proceso, diseño la solución y desarrollo el software. Hablarás con la misma persona desde la primera conversación hasta la integración.', 'abouttag':'Alexis Santos / Tenerife · London',
 'articles':'Ideas desde el taller.', 'articleintro':'Lo que aprendo construyendo productos, trabajando con IA y llevando ideas a la práctica.', 'allarticles':'Todos los artículos', 'english':'Artículo en inglés',
 'contact':'¿Qué proceso<br>te quita tiempo?', 'contactintro':'Descríbeme el trabajo repetitivo, lento o difícil de controlar. No necesitas saber qué tecnología hace falta.', 'name':'Tu nombre', 'business':'Empresa o actividad', 'need':'¿Qué proceso quieres mejorar?', 'placeholder':'Por ejemplo: recibimos facturas por email, copiamos los datos y revisamos cada documento a mano antes de registrarlo.', 'send':'Preparar consulta', 'emailnote':'Se abrirá tu aplicación de correo con la consulta preparada. Tú decides cuándo enviarla.', 'direct':'O escríbeme directamente', 'status':'Tu consulta está preparada. Si no se ha abierto tu correo, usa el enlace de email de al lado.', 'required':'Nombre y mensaje son obligatorios.', 'footer':'IA integrada. Software a medida.', 'back':'Volver arriba', 'privacy':'Este formulario no envía ni almacena tus datos en la web.',
 'subject':'Un proceso que quiero mejorar', 'emailbody':['Hola Alexis,','Soy','Mi empresa o actividad es','El proceso que quiero mejorar es:'],
},
'en': {
 'title':'AlexisSantos.dev — AI integration and custom software', 'description':'AI integration, consulting and custom software that automates real processes for companies and independent businesses.',
 'nav':['Solutions','Projects','About','Let’s talk'], 'skip':'Skip to content', 'menu':'Menu',
 'hero':'AI, integrated<br>into your business.', 'intro':'I study how you work and build the right solution: automation, assistants, validation, reporting or software connected to your existing tools.', 'cta':'Tell me what you want to improve', 'explore':'See the solutions', 'location':'Consulting and development · Between Tenerife and London',
 'work':'Real products.<br>Applied experience.', 'workintro':'I also build my own products. They show how I turn an idea into useful, considered software that is ready to use.',
 'bcat':'Wellbeing / iOS', 'bdesc':'A moment to pause.<br>And start again.', 'bdetail':'Guided breathing for iPhone. Choose a pattern, find your rhythm and make a little room between one thing and the next.',
 'lcat':'Photography / iOS', 'ldesc':'Fewer distractions.<br>More to see.', 'ldetail':'A minimal camera for iPhone. Fewer decisions between what you see and the photo you want to take.', 'view':'Explore the app', 'store':'View on the App Store', 'close':'Close',
 'services':'AI that fits<br>the way you work.', 'serviceintro':'I do not start with a tool. I start with the process that wastes time, causes errors or limits the business.',
 'serviceitems':[('Process automation','Invoices, documents, reports and repetitive tasks that currently depend on copying, reviewing and checking again.','Data extraction · Rules · Validation'),('Intelligent tools','Assistants and agents that work with your information, prepare answers and support decisions with human oversight.','Internal assistants · Search · Agents'),('Connected software','When the solution needs an interface, I build the website or app and connect it to your systems, data and AI services.','Web applications · iOS · Integrations')],
 'demo':'From an invoice<br>to an automated process.', 'demointro':'AI can read the document, extract the data, check it against your rules and prepare the result for review.', 'soon':'Solution example', 'democopy':'The solution connects to the tools you already use. A person reviews uncertain cases; the repetitive work happens automatically.',
 'flow':['Document','AI','Rules','Review','Result'],
 'process':'Understand. Build.<br>Integrate.', 'steps':[('Understand the process','I look at how the work happens today, where time is lost and which decisions must remain with a person.'),('Build the solution','I create a working first flow using your documents, rules and tools. You test it before the scope grows.'),('Integrate and support','I connect the solution, measure the result and adjust it as your needs and working methods change.')],
 'about':'Direct consulting.<br>Real execution.', 'abouttext':'I’m Alexis Santos, a software engineer and product maker. I’ve worked as a Staff iOS Engineer and Engineering Manager, building systems and teams around complex problems.', 'abouttext2':'I analyse the process, design the solution and build the software. You work with the same person from the first conversation through integration.', 'abouttag':'Alexis Santos / Tenerife · London',
 'articles':'Notes from the studio.', 'articleintro':'What I learn building products, working with AI and turning ideas into something real.', 'allarticles':'All articles', 'english':'Article in English',
 'contact':'Which process<br>is costing you time?', 'contactintro':'Describe the repetitive, slow or difficult-to-control work. You do not need to know which technology it requires.', 'name':'Your name', 'business':'Company or activity', 'need':'Which process do you want to improve?', 'placeholder':'For example: invoices arrive by email, we copy the data and check each document manually before recording it.', 'send':'Prepare enquiry', 'emailnote':'This opens your email app with the enquiry prepared. You choose when to send it.', 'direct':'Or email me directly', 'status':'Your enquiry is ready. If your email app did not open, use the email link alongside the form.', 'required':'Name and message are required.', 'footer':'Integrated AI. Custom software.', 'back':'Back to top', 'privacy':'This form does not send or store your data on this website.',
 'subject':'A process I want to improve', 'emailbody':['Hi Alexis,','My name is','My company or activity is','The process I want to improve is:'],
}}
ARROW='<span aria-hidden="true">↗</span>'
ICONS=['<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/>','<path d="m12 2 3 7 7 3-7 3-3 7-3-7-7-3 7-3Z"/>','<circle cx="5" cy="12" r="2.5"/><circle cx="19" cy="6" r="2.5"/><circle cx="19" cy="18" r="2.5"/><path d="m7.3 10.9 9.4-3.8M7.3 13.1l9.4 3.8"/>']
SHOWCASE = {
    'es': {
        'label': 'Caso ficticio',
        'nav': 'Demos',
        'index_title': 'Demostraciones',
        'index_intro': 'Así puede funcionar una solución de IA cuando se diseña alrededor del trabajo real de un negocio.',
        'index_note': 'Un primer caso en detalle. Después vendrán reservas, facturas, gestión de propiedades y servicios profesionales.',
        'home_title': 'Mira cómo funcionaría.',
        'home_intro': 'Un caso visual, paso a paso, de IA integrada en un negocio de mantenimiento.',
        'case_name': 'Nexo Mantenimiento',
        'case_title': 'Del primer mensaje al trabajo facturado.',
        'case_intro': 'Una solución integrada para recibir una incidencia, entenderla, organizar la visita y preparar toda la documentación sin perder el control humano.',
        'case_short': 'De un mensaje del cliente a una visita completada, con informe y factura listos para revisar.',
        'explore': 'Explorar el caso',
        'back': 'Todas las demostraciones',
        'eyebrow': 'IA aplicada a operaciones de campo',
        'how': 'Un solo flujo.<br>Seis pasos conectados.',
        'how_intro': 'La IA organiza la información y propone el siguiente paso. Una persona confirma las decisiones que afectan al cliente, al técnico o al cobro.',
        'before': 'Antes',
        'before_text': 'Mensajes dispersos, datos copiados a mano, fotos sin ordenar y documentos preparados al final del día.',
        'after': 'Con Nexo',
        'after_text': 'Una solicitud estructurada, una agenda clara y la evidencia conectada al informe y a la factura.',
        'result': 'Lo que cambia',
        'result_items': ['Menos tiempo copiando información', 'Cada trabajo conserva su contexto y evidencia', 'Las decisiones sensibles siguen en manos de una persona'],
        'cta_title': '¿Tienes un proceso parecido?',
        'cta_text': 'Lo adapto a tus clientes, reglas y herramientas. Empezamos por un flujo pequeño que puedas probar.',
        'cta': 'Cuéntame cómo trabajas',
        'review': 'Revisión humana',
        'ready': 'Listo para revisar',
        'stages': [
            ('request', '01', 'Solicitud recibida', 'Mensaje, foto o nota de voz en un solo lugar.'),
            ('understood', '02', 'Solicitud entendida', 'La IA extrae cliente, dirección, problema y urgencia.'),
            ('created', '03', 'Trabajo creado', 'Se genera una orden clara con contexto y prioridad.'),
            ('scheduled', '04', 'Visita programada', 'Se propone técnico y horario para confirmación.'),
            ('validated', '05', 'Trabajo validado', 'Fotos y checklist confirman lo realizado.'),
            ('documents', '06', 'Documentos preparados', 'Informe y factura quedan listos para revisar.'),
        ],
    },
    'en': {
        'label': 'Fictional case',
        'nav': 'Showcase',
        'index_title': 'Showcase',
        'index_intro': 'See how an AI solution can work when it is designed around the real operations of a business.',
        'index_note': 'One detailed case to begin with. Restaurant bookings, invoice processing, property management and professional services come next.',
        'home_title': 'See how it could work.',
        'home_intro': 'A visual, step-by-step case of AI integrated into a maintenance business.',
        'case_name': 'Nexo Maintenance',
        'case_title': 'From the first message to an invoiced job.',
        'case_intro': 'An integrated solution that receives a fault report, understands it, organises the visit and prepares the paperwork while people retain control.',
        'case_short': 'From a customer message to a completed visit, with the report and invoice ready for review.',
        'explore': 'Explore the case',
        'back': 'All showcase cases',
        'eyebrow': 'AI for field operations',
        'how': 'One workflow.<br>Six connected steps.',
        'how_intro': 'AI organises the information and proposes the next step. A person confirms decisions that affect the customer, technician or payment.',
        'before': 'Before',
        'before_text': 'Scattered messages, manually copied details, unorganised photos and paperwork prepared at the end of the day.',
        'after': 'With Nexo',
        'after_text': 'One structured request, a clear schedule and evidence connected to the report and invoice.',
        'result': 'What changes',
        'result_items': ['Less time spent copying information', 'Every job keeps its context and evidence', 'Sensitive decisions remain with a person'],
        'cta_title': 'Do you have a process like this?',
        'cta_text': 'I adapt it to your customers, rules and tools. We start with a small workflow you can test.',
        'cta': 'Tell me how you work',
        'review': 'Human review',
        'ready': 'Ready for review',
        'stages': [
            ('request', '01', 'Request received', 'A message, photo or voice note in one place.'),
            ('understood', '02', 'Request understood', 'AI extracts the customer, address, problem and urgency.'),
            ('created', '03', 'Job created', 'A clear work order is generated with context and priority.'),
            ('scheduled', '04', 'Visit scheduled', 'A technician and time are proposed for confirmation.'),
            ('validated', '05', 'Work validated', 'Photos and a checklist confirm what was completed.'),
            ('documents', '06', 'Documents prepared', 'The report and invoice are ready for review.'),
        ],
    },
}


def shared_head(lang, title, description, canonical, alternate, image='/assets/showcase/nexo/field-service.webp'):
    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} — AlexisSantos.dev</title><meta name="description" content="{escape(description, quote=True)}"><link rel="canonical" href="https://alexissantos.dev{canonical}"><link rel="alternate" hreflang="es" href="https://alexissantos.dev{canonical if lang == 'es' else alternate}"><link rel="alternate" hreflang="en" href="https://alexissantos.dev{alternate if lang == 'es' else canonical}"><link rel="alternate" hreflang="x-default" href="https://alexissantos.dev{canonical if lang == 'es' else alternate}"><meta property="og:title" content="{escape(title, quote=True)}"><meta property="og:description" content="{escape(description, quote=True)}"><meta property="og:type" content="website"><meta property="og:url" content="https://alexissantos.dev{canonical}"><meta property="og:image" content="https://alexissantos.dev{image}"><meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#f5f6f8"><link rel="icon" href="/assets/studio/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/studio/studio.css"><link rel="stylesheet" href="/assets/showcase/showcase.css"><script src="/assets/studio/studio.js" defer></script><script src="/assets/showcase/showcase.js" defer></script></head>'''


def interface_layers(lang):
    s = SHOWCASE[lang]
    es = lang == 'es'
    return f'''
    <div class="stage-layer" data-stage-panel="request"><div class="message-card"><span class="avatar">MC</span><div><b>{'Marta · Costa Azul' if es else 'Marta · Costa Azul'}</b><p>{'La tubería del lavabo pierde agua. ¿Podéis venir mañana?' if es else 'The pipe under the sink is leaking. Could you come tomorrow?'}</p><span class="message-meta">09:42 · {'Foto adjunta' if es else 'Photo attached'}</span></div></div></div>
    <div class="stage-layer" data-stage-panel="understood"><div class="extract-card"><span class="ui-kicker">{'IA · DATOS EXTRAÍDOS' if es else 'AI · EXTRACTED DETAILS'}</span><dl><div><dt>{'Cliente' if es else 'Customer'}</dt><dd>Marta C.</dd></div><div><dt>{'Lugar' if es else 'Location'}</dt><dd>Costa Azul · Local 04</dd></div><div><dt>{'Incidencia' if es else 'Issue'}</dt><dd>{'Fuga bajo lavabo' if es else 'Leak under sink'}</dd></div><div><dt>{'Prioridad' if es else 'Priority'}</dt><dd class="priority">{'Media' if es else 'Medium'}</dd></div></dl></div></div>
    <div class="stage-layer" data-stage-panel="created"><div class="work-card"><div><span class="ui-kicker">{'ORDEN DE TRABAJO' if es else 'WORK ORDER'}</span><strong>#NX-2048</strong></div><h3>{'Revisar fuga y sustituir conexión' if es else 'Inspect leak and replace connector'}</h3><ul><li>{'Cerrar suministro' if es else 'Shut off supply'}</li><li>{'Revisar sifón y juntas' if es else 'Inspect trap and seals'}</li><li>{'Documentar antes y después' if es else 'Document before and after'}</li></ul></div></div>
    <div class="stage-layer" data-stage-panel="scheduled"><div class="schedule-card"><span class="ui-kicker">{'VISITA PROPUESTA' if es else 'PROPOSED VISIT'}</span><div class="schedule-time"><b>18</b><span>SEP<br>10:30</span></div><p>Daniel R. · {'Técnico de zona' if es else 'Local technician'}</p><button type="button">{s['review']} →</button></div></div>
    <div class="stage-layer" data-stage-panel="validated"><div class="evidence-card"><span class="ui-kicker">{'EVIDENCIA DEL TRABAJO' if es else 'JOB EVIDENCE'}</span><div class="photo-pair"><figure><img src="/assets/showcase/nexo/evidence-before.webp" alt="{'Conexión antigua con una pequeña fuga' if es else 'Old connector with a small leak'}" width="1020" height="765" loading="lazy"><figcaption>{'ANTES' if es else 'BEFORE'}</figcaption></figure><figure><img src="/assets/showcase/nexo/evidence-after.webp" alt="{'Conexión nueva, reparada y seca' if es else 'New connector, repaired and dry'}" width="1020" height="765" loading="lazy"><figcaption>{'DESPUÉS' if es else 'AFTER'}</figcaption></figure></div><ul><li>✓ {'Conexión sustituida' if es else 'Connector replaced'}</li><li>✓ {'Prueba sin fugas' if es else 'Leak test passed'}</li><li>✓ {'Fotos verificadas' if es else 'Photos verified'}</li></ul></div></div>
    <div class="stage-layer" data-stage-panel="documents"><div class="document-stack"><div class="report-sheet"><span class="ui-kicker">{'INFORME' if es else 'REPORT'}</span><strong>#NX-2048</strong><i></i><i></i><i></i><span class="approved">{s['ready']}</span></div><div class="invoice-sheet"><span class="ui-kicker">{'BORRADOR DE FACTURA' if es else 'INVOICE DRAFT'}</span><b>128,00 €</b><p>{'Pendiente de aprobación' if es else 'Awaiting approval'}</p></div></div></div>'''


def showcase_mosaic(lang, context='case'):
    s = SHOWCASE[lang]
    controls = ''.join(f'''<button class="stage-control" type="button" data-stage="{stage}" data-status="{escape(title, quote=True)} — {escape(description, quote=True)}"><span class="stage-number">{number}</span><span><b>{title}</b><small>{description}</small></span><span class="stage-arrow" aria-hidden="true">↗</span></button>''' for stage, number, title, description in s['stages'])
    image_loading = 'eager' if context == 'case' else 'lazy'
    return f'''<div class="showcase-mosaic" data-showcase data-active-stage="request"><div class="showcase-panel"><img src="/assets/showcase/nexo/field-service.webp" alt="" width="1536" height="1024" loading="{image_loading}"><div class="panel-shade"></div>{interface_layers(lang)}<p class="showcase-status" aria-live="polite">{s['stages'][0][2]} — {s['stages'][0][3]}</p></div><div class="showcase-stage-list">{controls}</div></div>'''


def showcase_shell_parts(lang, es_href, en_href):
    home_path = 'index.html' if lang == 'es' else 'en/index.html'
    home_url = '/' if lang == 'es' else '/en/'
    home = (ROOT / home_path).read_text()
    import re
    header = re.search(r'<header class="header wrap">.*?</header>', home, re.S).group(0).replace('href="#', f'href="{home_url}#')
    header = re.sub(r'<div class="languages".*?</div>', f'''<div class="languages" aria-label="{'Idioma' if lang == 'es' else 'Language'}"><a href="{es_href}" lang="es" aria-label="Español" {'aria-current="page"' if lang == 'es' else ''}>ES</a><span>/</span><a href="{en_href}" lang="en" aria-label="English" {'aria-current="page"' if lang == 'en' else ''}>EN</a></div>''', header, flags=re.S)
    footer = re.search(r'<footer class="wrap footer">.*?</footer>', home, re.S).group(0).replace('href="#top"', 'href="#top"')
    return header, footer


def build_showcase_page(lang):
    s = SHOWCASE[lang]
    es = lang == 'es'
    canonical = '/showcase/' if es else '/en/showcase/'
    alternate = '/en/showcase/' if es else '/showcase/'
    case_url = '/showcase/nexo-mantenimiento/' if es else '/en/showcase/nexo-maintenance/'
    header, footer = showcase_shell_parts(lang, '/showcase/', '/en/showcase/')
    head = shared_head(lang, s['index_title'], s['index_intro'], canonical, alternate)
    return f'''{head}<body id="top"><a class="skip" href="#main">{COPY[lang]['skip']}</a>{header}<main id="main" class="showcase-page"><section class="showcase-index-hero wrap"><span class="showcase-kicker">AlexisSantos.dev / {s['nav']}</span><h1>{s['index_title']}.</h1><div><p>{s['index_intro']}</p><small>{s['index_note']}</small></div></section><section class="wrap showcase-feature"><div class="showcase-feature-head"><div><span class="fictional-label">{s['label']}</span><span>{s['eyebrow']}</span></div><h2>{s['case_name']}</h2><p>{s['case_short']}</p><a class="text-link" href="{case_url}">{s['explore']} {ARROW}</a></div>{showcase_mosaic(lang, 'index')}</section><section class="showcase-future wrap"><span>{'Próximamente' if es else 'Coming next'}</span><p>{'Reservas de restaurantes · Facturas · Gestión de propiedades · Servicios profesionales' if es else 'Restaurant bookings · Invoice processing · Property management · Professional services'}</p></section></main>{footer}</body></html>'''


def build_nexo_page(lang):
    s = SHOWCASE[lang]
    es = lang == 'es'
    canonical = '/showcase/nexo-mantenimiento/' if es else '/en/showcase/nexo-maintenance/'
    alternate = '/en/showcase/nexo-maintenance/' if es else '/showcase/nexo-mantenimiento/'
    index_url = '/showcase/' if es else '/en/showcase/'
    contact_url = '/#contact' if es else '/en/#contact'
    header, footer = showcase_shell_parts(lang, '/showcase/nexo-mantenimiento/', '/en/showcase/nexo-maintenance/')
    head = shared_head(lang, s['case_name'], s['case_intro'], canonical, alternate)
    results = ''.join(f'<li><span>0{i}</span>{item}</li>' for i, item in enumerate(s['result_items'], 1))
    return f'''{head}<body id="top"><a class="skip" href="#main">{COPY[lang]['skip']}</a>{header}<main id="main" class="showcase-page"><section class="case-hero wrap"><a class="case-back" href="{index_url}">← {s['back']}</a><div class="case-heading"><div><span class="fictional-label">{s['label']}</span><span>{s['eyebrow']}</span></div><h1>{s['case_name']}</h1><p>{s['case_title']} {s['case_intro']}</p></div></section><section class="wrap case-demo">{showcase_mosaic(lang, 'case')}</section><section class="case-explainer wrap"><div><span class="showcase-kicker">{'EL FLUJO' if es else 'THE WORKFLOW'}</span><h2>{s['how']}</h2></div><p>{s['how_intro']}</p></section><section class="before-after wrap"><article><span>01 / {s['before'].upper()}</span><h3>{s['before']}</h3><p>{s['before_text']}</p></article><article><span>02 / {s['after'].upper()}</span><h3>{s['after']}</h3><p>{s['after_text']}</p></article></section><section class="case-results"><div class="wrap"><div><span class="showcase-kicker">{'RESULTADO' if es else 'OUTCOME'}</span><h2>{s['result']}.</h2></div><ol>{results}</ol></div></section><section class="case-cta wrap"><h2>{s['cta_title']}</h2><div><p>{s['cta_text']}</p><a class="button" href="{contact_url}">{s['cta']} {ARROW}</a></div></section></main>{footer}</body></html>'''
for lang,t in COPY.items():
 url='/' if lang=='es' else '/en/'
 nav=''.join(f'<a href="#{anchor}">{text}</a>' for anchor,text in zip(['solutions','projects','studio'],t['nav'][:3]))
 nav+=f'<a href="{'/showcase/' if lang=='es' else '/en/showcase/'}">{SHOWCASE[lang]['nav']}</a>'
 nav+=f'<a href="{'/articles/' if lang=='es' else '/en/articles/'}">{'Artículos' if lang=='es' else 'Articles'}</a>'
 services=''.join(f'<article><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[i]}</svg><h3>{name}</h3><p>{desc}</p><small>{tags}</small></article>' for i,(name,desc,tags) in enumerate(t['serviceitems']))
 steps=''.join(f'<li><span class="step-number">0{i+1}</span><h3>{name}</h3><p>{desc}</p></li>' for i,(name,desc) in enumerate(t['steps']))
 flow=''.join(f'<li>{item}</li>' for item in t['flow'])
 html=f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t['title']}</title><meta name="description" content="{t['description']}">
<link rel="canonical" href="https://alexissantos.dev{url}"><link rel="alternate" hreflang="es" href="https://alexissantos.dev/"><link rel="alternate" hreflang="en" href="https://alexissantos.dev/en/"><link rel="alternate" hreflang="x-default" href="https://alexissantos.dev/">
<meta property="og:title" content="{t['title']}"><meta property="og:description" content="{t['description']}"><meta property="og:type" content="website"><meta property="og:url" content="https://alexissantos.dev{url}"><meta property="og:image" content="https://alexissantos.dev/assets/studio/hero.jpg"><meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#f5f6f8">
<link rel="icon" href="/assets/studio/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/studio/studio.css"><link rel="stylesheet" href="/assets/showcase/showcase.css"><script src="/assets/studio/studio.js" defer></script><script src="/assets/showcase/showcase.js" defer></script>
</head>
<body id="top"><a class="skip" href="#main">{t['skip']}</a>
<header class="header wrap"><a class="wordmark" href="{url}" aria-label="AlexisSantos.dev"><img src="/assets/studio/logo.svg" alt="AlexisSantos.dev" width="645" height="82"></a><nav class="desktop-nav" aria-label="{'Principal' if lang=='es' else 'Main'}">{nav}</nav><div class="header-actions"><div class="languages" aria-label="{'Idioma' if lang=='es' else 'Language'}"><a href="/" lang="es" aria-label="Español" {'aria-current="page"' if lang=='es' else ''}>ES</a><span>/</span><a href="/en/" lang="en" aria-label="English" {'aria-current="page"' if lang=='en' else ''}>EN</a></div><a class="button small header-cta" href="#contact">{t['nav'][3]}</a><button class="menu-toggle" aria-expanded="false" aria-controls="mobile-nav">{t['menu']} <span aria-hidden="true">＋</span></button></div><nav id="mobile-nav" hidden>{nav}<a href="#contact">{t['nav'][3]}</a></nav></header>
<main id="main"><section class="hero"><div class="hero-inner wrap"><div class="hero-copy"><h1>{t['hero']}</h1><p>{t['intro']}</p><div class="hero-actions"><a class="button" href="#contact">{t['cta']} {ARROW}</a><a class="text-link" href="#solutions">{t['explore']} {ARROW}</a></div></div><img class="hero-art" src="/assets/studio/hero.jpg" alt="" width="1536" height="1024" fetchpriority="high"><p class="hero-foot">{t['location']}</p></div></section>
<section id="solutions" class="section wrap services"><div class="section-head"><h2>{t['services']}</h2><p>{t['serviceintro']}</p></div><div class="service-grid">{services}</div></section>
<section class="demo-section"><div class="wrap demo-inner"><div><span class="status-pill"><span></span>{t['soon']}</span><h2>{t['demo']}</h2><p>{t['demointro']}</p></div><div class="demo-note"><ol class="integration-flow">{flow}</ol><p>{t['democopy']}</p><a class="text-link" href="#contact">{t['cta']} {ARROW}</a></div></div></section>
<section class="section wrap process"><h2>{t['process']}</h2><ol>{steps}</ol></section>
<section id="showcase" class="section wrap home-showcase"><div class="section-head showcase-home-head"><div><span class="fictional-label">{SHOWCASE[lang]['label']}</span><h2>{SHOWCASE[lang]['home_title']}</h2></div><div><p>{SHOWCASE[lang]['home_intro']}</p><a class="text-link" href="{'/showcase/nexo-mantenimiento/' if lang=='es' else '/en/showcase/nexo-maintenance/'}">{SHOWCASE[lang]['explore']} {ARROW}</a></div></div>{showcase_mosaic(lang, 'home')}</section>
<section id="projects" class="section wrap product-proof"><div class="section-head"><h2>{t['work']}</h2><p>{t['workintro']}</p></div><div class="projects"><article class="project breathe"><img class="product-scene" src="/assets/studio/breathe-scene.jpg" alt="" loading="lazy" width="1448" height="1086"><div class="product-copy"><small>{t['bcat']}</small><h3>Breathe Now</h3><p>{t['bdesc']}</p><button class="project-open" aria-label="{t['view']}: Breathe Now" data-dialog="breathe-detail">{t['view']} {ARROW}</button></div><span class="product-bottom">{'Respira. Para. Vuelve.' if lang=='es' else 'Breathe. Reset. Begin again.'}</span></article><article class="project camera"><img class="product-scene" src="/assets/studio/camera-scene.jpg" alt="" loading="lazy" width="1448" height="1086"><div class="product-copy"><small>{t['lcat']}</small><h3>Lean Cam</h3><p>{t['ldesc']}</p><button class="project-open" aria-label="{t['view']}: Lean Cam" data-dialog="camera-detail">{t['view']} {ARROW}</button></div><span class="product-bottom">{'Mira más. Decide menos.' if lang=='es' else 'See more. Do less.'}</span></article></div></section>
<section id="studio" class="section wrap about"><div class="portrait"><img src="/photo.jpg" alt="Alexis Santos" loading="lazy" width="600" height="700"><span>{t['abouttag']}</span></div><div class="about-copy"><h2>{t['about']}</h2><p>{t['abouttext']}</p><p>{t['abouttext2']}</p><div class="social"><a href="https://www.linkedin.com/in/asantosp/">LinkedIn {ARROW}</a><a href="https://github.com/alexissan">GitHub {ARROW}</a><a href="https://x.com/deepfirstsearch">X {ARROW}</a></div></div></section>
<section id="contact" class="contact-section"><div class="wrap contact-grid"><div><h2>{t['contact']}</h2><p class="contact-intro">{t['contactintro']}</p><div class="direct-email"><span>{t['direct']}</span><a href="mailto:alexis.santos.perez@gmail.com">alexis.santos.perez@gmail.com {ARROW}</a></div></div><form id="brief-form"><div class="form-row"><label>{t['name']}<input name="name" autocomplete="name" required maxlength="100"></label><label>{t['business']}<input name="business" autocomplete="organization" maxlength="150"></label></div><label>{t['need']}<textarea name="message" rows="4" required maxlength="3000" placeholder="{t['placeholder']}"></textarea></label><button class="button" type="submit">{t['send']} {ARROW}</button><p class="form-note">{t['emailnote']}</p><p class="privacy-note">{t['privacy']}</p><p id="form-status" role="status"></p><noscript><p>{t['direct']}: <a href="mailto:alexis.santos.perez@gmail.com">alexis.santos.perez@gmail.com</a></p></noscript></form></div></section>
</main><footer class="wrap footer"><div><a class="wordmark" href="{url}"><img src="/assets/studio/logo.svg" alt="AlexisSantos.dev" width="645" height="82"></a><p>{t['footer']}</p></div><span>© 2026 Alexis Santos</span><nav class="footer-links" aria-label="{'Más información' if lang=='es' else 'More information'}"><a href="{'/showcase/' if lang=='es' else '/en/showcase/'}">{SHOWCASE[lang]['nav']}</a><a href="{'/articles/' if lang=='es' else '/en/articles/'}">{'Artículos' if lang=='es' else 'Articles'}</a><a href="#top">{t['back']} ↑</a></nav></footer>
<dialog id="breathe-detail" aria-labelledby="breathe-title"><button class="dialog-close" aria-label="{t['close']}">×</button><img class="app-icon" src="/breathe-now/icon.png" alt="" width="80" height="80"><small>{t['bcat']}</small><h2 id="breathe-title">Breathe Now</h2><p>{t['bdetail']}</p><a class="button" href="https://apps.apple.com/app/id6757527807">{t['store']} {ARROW}</a></dialog>
<dialog id="camera-detail" aria-labelledby="camera-title"><button class="dialog-close" aria-label="{t['close']}">×</button><small>{t['lcat']}</small><h2 id="camera-title">Lean Cam</h2><p>{t['ldetail']}</p><img class="dialog-photo" src="/lean-cam/photo-1.JPG" alt="{'Fotografía tomada con Lean Cam' if lang=='es' else 'Photography from Lean Cam'}" loading="lazy"><a class="button" href="https://apps.apple.com/app/id6755633580">{t['store']} {ARROW}</a></dialog>
<script type="application/json" id="contact-copy">{json.dumps({k:t[k] for k in ['subject','emailbody','status']},ensure_ascii=False)}</script>
</body></html>'''
 target=ROOT/('index.html' if lang=='es' else 'en/index.html')
 target.parent.mkdir(parents=True, exist_ok=True)
 target.write_text(html)

for lang in ['es', 'en']:
    showcase_path = ROOT / ('showcase/index.html' if lang == 'es' else 'en/showcase/index.html')
    case_path = ROOT / ('showcase/nexo-mantenimiento/index.html' if lang == 'es' else 'en/showcase/nexo-maintenance/index.html')
    showcase_path.parent.mkdir(parents=True, exist_ok=True)
    case_path.parent.mkdir(parents=True, exist_ok=True)
    showcase_path.write_text(build_showcase_page(lang))
    case_path.write_text(build_nexo_page(lang))

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
    title = 'Artículos' if is_es else 'Articles'
    intro = COPY[lang]['articleintro']
    back = 'Volver' if is_es else 'Back'
    archive = f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} — AlexisSantos.dev</title><meta name="description" content="{intro}"><link rel="canonical" href="https://alexissantos.dev{archive_url}"><link rel="alternate" hreflang="es" href="https://alexissantos.dev/articles/"><link rel="alternate" hreflang="en" href="https://alexissantos.dev/en/articles/"><link rel="icon" href="/assets/studio/favicon.svg"><link rel="stylesheet" href="/assets/studio/studio.css"><script src="/assets/studio/studio.js" defer></script></head><body id="top"><a class="skip" href="#main">{COPY[lang]['skip']}</a>{header}<main id="main" class="wrap archive-page"><div class="archive-intro"><a class="text-link" href="{home_url}">← {back}</a><h1>{title}.</h1><p>{intro}</p></div><div class="article-grid">{cards}</div></main>{footer}</body></html>'''
    (ROOT / archive_url.strip('/') / 'index.html').write_text(archive)

public_paths = ["/", "/en/", "/showcase/", "/en/showcase/", "/showcase/nexo-mantenimiento/", "/en/showcase/nexo-maintenance/", "/articles/", "/en/articles/"] + [f"/articles/{entry[0]}/" for entry in entries]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(f"  <url><loc>https://alexissantos.dev{path}</loc></url>" for path in public_paths) + "\n</urlset>\n"
(ROOT / "sitemap.xml").write_text(sitemap)
