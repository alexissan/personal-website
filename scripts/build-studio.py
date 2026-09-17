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
        'index_note': 'Tres casos detallados para mantenimiento, reservas y administración. Después vendrán propiedades y servicios profesionales.',
        'home_title': 'Mira cómo funcionaría.',
        'home_intro': 'Casos visuales, paso a paso, de IA integrada en operaciones reales.',
        'case_name': 'Nexo Mantenimiento',
        'case_title': 'Del primer mensaje al trabajo facturado.',
        'case_intro': 'Una solución integrada para recibir una incidencia, entenderla, organizar la visita y preparar toda la documentación sin perder el control humano.',
        'case_short': 'De un mensaje del cliente a una visita completada, con informe y factura listos para revisar.',
        'explore': 'Explorar el caso',
        'back': 'Todas las demostraciones',
        'eyebrow': 'IA aplicada a operaciones de campo',
        'how': 'Un solo flujo.<br>Seis pasos conectados.',
        'how_intro': 'La IA organiza la información y propone el siguiente paso. Una persona confirma las decisiones que afectan al cliente, al técnico o al cobro.',
        'product_title': 'Así se vería<br>el software.',
        'product_intro': 'Una mesa de operaciones para coordinar el trabajo y una app móvil sencilla para el técnico. Todo comparte la misma información.',
        'desktop_label': 'Panel de operaciones',
        'mobile_label': 'App del técnico',
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
        'index_note': 'Three detailed cases across maintenance, bookings and administration. Property management and professional services come next.',
        'home_title': 'See how it could work.',
        'home_intro': 'Visual, step-by-step cases of AI integrated into real operations.',
        'case_name': 'Nexo Maintenance',
        'case_title': 'From the first message to an invoiced job.',
        'case_intro': 'An integrated solution that receives a fault report, understands it, organises the visit and prepares the paperwork while people retain control.',
        'case_short': 'From a customer message to a completed visit, with the report and invoice ready for review.',
        'explore': 'Explore the case',
        'back': 'All showcase cases',
        'eyebrow': 'AI for field operations',
        'how': 'One workflow.<br>Six connected steps.',
        'how_intro': 'AI organises the information and proposes the next step. A person confirms decisions that affect the customer, technician or payment.',
        'product_title': 'What the software<br>could look like.',
        'product_intro': 'An operations desk for coordinating the work and a focused mobile app for the technician. Both share the same information.',
        'desktop_label': 'Operations dashboard',
        'mobile_label': 'Technician app',
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

RESTAURANT = {
    'es': {
        'label': 'Caso ficticio',
        'name': 'Mesa Clara',
        'eyebrow': 'IA para reservas y sala',
        'title': 'De un mensaje a una mesa preparada.',
        'intro': 'Una solución conectada que entiende la petición del cliente, consulta disponibilidad, protege las decisiones delicadas y prepara al equipo antes del servicio.',
        'short': 'Reservas atendidas al momento, preferencias bien registradas y un servicio de sala que empieza con contexto.',
        'explore': 'Explorar el caso',
        'how': 'Cada reserva,<br>lista para recibir.',
        'how_intro': 'La IA resuelve lo repetitivo y mantiene las excepciones visibles. El equipo controla la sala, los cambios importantes y cualquier necesidad especial.',
        'product_title': 'La reserva y la sala,<br>en la misma vista.',
        'product_intro': 'Un panel para recepción y una experiencia móvil para confirmar los detalles con el cliente.',
        'before': 'Antes',
        'before_text': 'Llamadas perdidas, mensajes pendientes, notas en distintos sitios y alergias que llegan tarde al equipo.',
        'after': 'Con Mesa Clara',
        'after_text': 'Disponibilidad actualizada, confirmaciones automáticas y un briefing claro antes de cada servicio.',
        'result_items': ['Más solicitudes atendidas sin interrumpir el servicio', 'Preferencias y alergias llegan al equipo adecuado', 'Las excepciones se revisan antes de confirmar'],
        'stages': [
            ('request', '01', 'Petición recibida', 'Un mensaje pide mesa para cuatro el sábado.'),
            ('understood', '02', 'Detalles entendidos', 'La IA identifica fecha, hora, personas y preferencias.'),
            ('availability', '03', 'Disponibilidad consultada', 'La sala ofrece dos horarios que encajan.'),
            ('review', '04', 'Excepción revisada', 'Una alergia queda visible antes de confirmar.'),
            ('confirmed', '05', 'Reserva confirmada', 'El cliente recibe los detalles y puede modificarlos.'),
            ('briefing', '06', 'Sala preparada', 'El equipo recibe el briefing antes del servicio.'),
        ],
    },
    'en': {
        'label': 'Fictional case',
        'name': 'Mesa Clara',
        'eyebrow': 'AI for bookings and service',
        'title': 'From a message to a table ready for guests.',
        'intro': 'A connected solution that understands the guest’s request, checks availability, protects sensitive decisions and prepares the team before service.',
        'short': 'Booking requests handled immediately, preferences recorded properly and a front-of-house team that starts with context.',
        'explore': 'Explore the case',
        'how': 'Every booking,<br>ready to welcome.',
        'how_intro': 'AI handles repetitive work and keeps exceptions visible. The team controls the room, important changes and every special requirement.',
        'product_title': 'Bookings and service,<br>in the same view.',
        'product_intro': 'A front-of-house dashboard and a mobile experience that confirms every detail with the guest.',
        'before': 'Before',
        'before_text': 'Missed calls, pending messages, notes in different places and allergy information reaching the team too late.',
        'after': 'With Mesa Clara',
        'after_text': 'Live availability, automatic confirmations and a clear briefing before every service.',
        'result_items': ['More requests handled without interrupting service', 'Preferences and allergies reach the right team', 'Exceptions are reviewed before confirmation'],
        'stages': [
            ('request', '01', 'Request received', 'A message asks for a table for four on Saturday.'),
            ('understood', '02', 'Details understood', 'AI identifies the date, time, party and preferences.'),
            ('availability', '03', 'Availability checked', 'The room offers two suitable times.'),
            ('review', '04', 'Exception reviewed', 'An allergy stays visible before confirmation.'),
            ('confirmed', '05', 'Booking confirmed', 'The guest receives the details and can amend them.'),
            ('briefing', '06', 'Team prepared', 'The team receives the briefing before service.'),
        ],
    },
}

INVOICES = {
    'es': {
        'label': 'Caso ficticio',
        'name': 'Ladera Norte',
        'eyebrow': 'IA para facturas y compras',
        'title': 'De una factura adjunta a un registro preparado.',
        'intro': 'Una solución que recibe documentos, extrae los datos, cruza cada factura con pedidos y proveedores y deja las diferencias en manos del equipo.',
        'short': 'Facturas organizadas al llegar, datos comprobados y excepciones claras antes de registrar nada.',
        'explore': 'Explorar el caso',
        'how': 'Cada factura,<br>con contexto y control.',
        'how_intro': 'La IA lee y organiza. Las reglas comparan importes, pedidos y proveedores. Cuando algo no encaja, una persona decide antes de que el dato llegue a contabilidad.',
        'product_title': 'El documento y sus datos,<br>lado a lado.',
        'product_intro': 'Una bandeja para el equipo financiero, revisión visual del documento y aprobaciones rápidas cuando aparece una diferencia.',
        'before': 'Antes',
        'before_text': 'Adjuntos repartidos entre correos, datos copiados a mano y diferencias descubiertas cuando el cierre ya está encima.',
        'after': 'Con Ladera Norte',
        'after_text': 'Cada factura entra en una cola, conserva su documento original y muestra exactamente qué necesita revisión.',
        'result_items': ['La información se captura una sola vez', 'Cada excepción explica qué regla no encaja', 'El registro final sigue necesitando aprobación humana'],
        'stages': [
            ('received', '01', 'Factura recibida', 'El adjunto entra en una bandeja única.'),
            ('extracted', '02', 'Datos extraídos', 'La IA identifica proveedor, fechas, impuestos e importe.'),
            ('matched', '03', 'Proveedor encontrado', 'La factura se vincula con su ficha y pedido.'),
            ('checked', '04', 'Reglas comprobadas', 'NIF, duplicados y totales se revisan automáticamente.'),
            ('exception', '05', 'Diferencia revisada', 'Un importe distinto queda pendiente de una persona.'),
            ('ready', '06', 'Registro preparado', 'La entrada queda lista para aprobar y sincronizar.'),
        ],
    },
    'en': {
        'label': 'Fictional case',
        'name': 'Ladera Norte',
        'eyebrow': 'AI for invoices and purchasing',
        'title': 'From an invoice attachment to a prepared entry.',
        'intro': 'A solution that receives documents, extracts the data, matches every invoice with suppliers and purchase orders, and leaves discrepancies with the team.',
        'short': 'Invoices organised on arrival, data checked and clear exceptions before anything is recorded.',
        'explore': 'Explore the case',
        'how': 'Every invoice,<br>with context and control.',
        'how_intro': 'AI reads and organises. Rules compare amounts, orders and suppliers. When something does not match, a person decides before the data reaches the accounting system.',
        'product_title': 'The document and its data,<br>side by side.',
        'product_intro': 'An inbox for the finance team, visual document review and quick approvals when a discrepancy appears.',
        'before': 'Before',
        'before_text': 'Attachments spread across inboxes, fields copied by hand and discrepancies discovered when the month-end deadline is already close.',
        'after': 'With Ladera Norte',
        'after_text': 'Every invoice enters one queue, keeps its original document and shows exactly what needs attention.',
        'result_items': ['Information is captured once', 'Every exception explains which rule failed', 'The final entry still requires human approval'],
        'stages': [
            ('received', '01', 'Invoice received', 'The attachment enters one shared inbox.'),
            ('extracted', '02', 'Data extracted', 'AI identifies the supplier, dates, tax and amount.'),
            ('matched', '03', 'Supplier matched', 'The invoice connects to its supplier and purchase order.'),
            ('checked', '04', 'Rules checked', 'Tax ID, duplicates and totals are checked automatically.'),
            ('exception', '05', 'Difference reviewed', 'A mismatched amount waits for a person.'),
            ('ready', '06', 'Entry prepared', 'The entry is ready to approve and sync.'),
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


def product_mockup(lang):
    s = SHOWCASE[lang]
    es = lang == 'es'
    return f'''<section class="product-showcase"><div class="wrap product-showcase-intro"><div><span class="showcase-kicker">{'PRODUCTO' if es else 'PRODUCT'}</span><h2>{s['product_title']}</h2></div><p>{s['product_intro']}</p></div><div class="wrap device-stage"><div class="desktop-device"><div class="desktop-bar"><span></span><span></span><span></span><b>NEXO / {s['desktop_label']}</b></div><div class="desktop-screen"><aside><strong>NEXO</strong><nav><span class="active">{'Resumen' if es else 'Overview'}</span><span>{'Trabajos' if es else 'Jobs'} <i>12</i></span><span>{'Calendario' if es else 'Schedule'}</span><span>{'Clientes' if es else 'Customers'}</span><span>{'Informes' if es else 'Reports'}</span></nav><small>Alexis · Admin</small></aside><main><header><div><small>{'MIÉRCOLES, 18 SEP' if es else 'WEDNESDAY, 18 SEP'}</small><h3>{'Buenos días, Alexis' if es else 'Good morning, Alexis'}</h3></div><button>{'Crear trabajo' if es else 'Create job'} ＋</button></header><div class="dashboard-stats"><article><span>{'ABIERTOS' if es else 'OPEN'}</span><b>12</b><small>↑ 3 {'esta semana' if es else 'this week'}</small></article><article><span>{'HOY' if es else 'TODAY'}</span><b>5</b><small>4 {'en curso' if es else 'in progress'}</small></article><article><span>{'POR REVISAR' if es else 'TO REVIEW'}</span><b>2</b><small>{'IA preparada' if es else 'AI prepared'}</small></article></div><section class="jobs-board"><div class="jobs-heading"><h4>{'Trabajos de hoy' if es else 'Today’s jobs'}</h4><span>{'Ver agenda' if es else 'View schedule'} →</span></div><div class="job-row featured"><span class="job-time">10:30</span><div><b>#NX-2048 · Costa Azul</b><small>{'Fuga bajo lavabo · Daniel R.' if es else 'Leak under sink · Daniel R.'}</small></div><em>{'EN CURSO' if es else 'IN PROGRESS'}</em></div><div class="job-row"><span class="job-time">12:00</span><div><b>#NX-2049 · La Brisa</b><small>{'Revisión de climatización' if es else 'Air conditioning check'}</small></div><em>{'PROGRAMADO' if es else 'SCHEDULED'}</em></div><div class="job-row"><span class="job-time">15:30</span><div><b>#NX-2050 · Cumbre</b><small>{'Persiana bloqueada' if es else 'Blocked shutter'}</small></div><em>{'PROGRAMADO' if es else 'SCHEDULED'}</em></div></section><section class="ai-brief"><span class="ai-mark">✦</span><div><b>{'Resumen preparado por IA' if es else 'AI-prepared brief'}</b><p>{'Dos trabajos necesitan revisión. La factura de Costa Azul estará lista cuando Daniel complete la prueba final.' if es else 'Two jobs need review. The Costa Azul invoice will be ready when Daniel completes the final check.'}</p></div><button>{'Revisar' if es else 'Review'} →</button></section></main></div></div><div class="phone-device"><div class="phone-speaker"></div><div class="phone-screen"><header><span>9:41</span><b>NEXO</b><span>•••</span></header><div class="phone-job-head"><small>#NX-2048 · {'EN CURSO' if es else 'IN PROGRESS'}</small><h3>{'Fuga bajo lavabo' if es else 'Leak under sink'}</h3><p>Costa Azul · Local 04</p></div><div class="phone-client"><span>MC</span><div><b>Marta C.</b><small>{'Cliente · 09:42' if es else 'Customer · 09:42'}</small></div><button>↗</button></div><div class="phone-evidence"><div><img src="/assets/showcase/nexo/evidence-before.webp" alt="" width="1020" height="765"><small>{'ANTES' if es else 'BEFORE'}</small></div><div><img src="/assets/showcase/nexo/evidence-after.webp" alt="" width="1020" height="765"><small>{'DESPUÉS' if es else 'AFTER'}</small></div></div><ul><li><span>✓</span>{'Conexión sustituida' if es else 'Connector replaced'}</li><li><span>✓</span>{'Prueba sin fugas' if es else 'Leak test passed'}</li><li><span>✓</span>{'Fotos añadidas' if es else 'Photos added'}</li></ul><button class="phone-complete">{'Completar trabajo' if es else 'Complete job'} →</button></div></div><div class="device-caption desktop-caption"><span>01</span><b>{s['desktop_label']}</b></div><div class="device-caption phone-caption"><span>02</span><b>{s['mobile_label']}</b></div></div></section>'''


def restaurant_layers(lang):
    es = lang == 'es'
    return f'''
    <div class="stage-layer" data-stage-panel="request"><div class="message-card restaurant-message"><span class="avatar">LR</span><div><b>Lucía R.</b><p>{'Hola, ¿tenéis mesa para 4 este sábado sobre las 21:00? Una persona es alérgica a los frutos secos.' if es else 'Hi, do you have a table for 4 this Saturday around 9pm? One guest has a nut allergy.'}</p><span class="message-meta">18:16 · {'MENSAJE' if es else 'MESSAGE'}</span></div></div></div>
    <div class="stage-layer" data-stage-panel="understood"><div class="extract-card restaurant-extract"><span class="ui-kicker">{'IA · PETICIÓN ENTENDIDA' if es else 'AI · REQUEST UNDERSTOOD'}</span><dl><div><dt>{'Fecha' if es else 'Date'}</dt><dd>21 SEP</dd></div><div><dt>{'Personas' if es else 'Guests'}</dt><dd>4</dd></div><div><dt>{'Hora ideal' if es else 'Preferred time'}</dt><dd>21:00</dd></div><div><dt>{'Atención' if es else 'Attention'}</dt><dd class="restaurant-alert">{'Alergia' if es else 'Allergy'}</dd></div></dl></div></div>
    <div class="stage-layer" data-stage-panel="availability"><div class="availability-card"><span class="ui-kicker">{'DISPONIBILIDAD EN SALA' if es else 'ROOM AVAILABILITY'}</span><h3>{'Sábado, 21 septiembre' if es else 'Saturday, 21 September'}</h3><div><span>20:30</span><span class="suggested">21:00</span><span>21:30</span></div><p>4 {'personas · Interior' if es else 'guests · Inside'}</p></div></div>
    <div class="stage-layer" data-stage-panel="review"><div class="allergy-card"><span class="allergy-icon">!</span><span class="ui-kicker">{'REVISIÓN NECESARIA' if es else 'REVIEW REQUIRED'}</span><h3>{'Alergia a frutos secos' if es else 'Nut allergy'}</h3><p>{'Confirmar protocolo de cocina antes de aceptar la reserva.' if es else 'Confirm the kitchen protocol before accepting the booking.'}</p><button type="button">{'Revisar con cocina' if es else 'Review with kitchen'} →</button></div></div>
    <div class="stage-layer" data-stage-panel="confirmed"><div class="booking-confirmed"><span class="confirmation-mark">✓</span><span class="ui-kicker">{'RESERVA CONFIRMADA' if es else 'BOOKING CONFIRMED'}</span><h3>Lucía · 4 {'personas' if es else 'guests'}</h3><b>21 SEP · 21:00</b><p>{'Mesa 08 · Interior' if es else 'Table 08 · Inside'}</p></div></div>
    <div class="stage-layer" data-stage-panel="briefing"><div class="service-brief"><span class="ui-kicker">{'BRIEFING DE SERVICIO' if es else 'SERVICE BRIEFING'}</span><div><b>21:00</b><span>{'Mesa 08 · 4 personas' if es else 'Table 08 · 4 guests'}</span></div><ul><li>● {'Alergia señalada' if es else 'Allergy flagged'}</li><li>● {'Cumpleaños' if es else 'Birthday'}</li><li>● {'Trona no necesaria' if es else 'No high chair needed'}</li></ul><small>{'Compartido con sala y cocina' if es else 'Shared with front of house and kitchen'}</small></div></div>'''


def restaurant_mosaic(lang, context='case'):
    s = RESTAURANT[lang]
    controls = ''.join(f'''<button class="stage-control" type="button" data-stage="{stage}" data-status="{escape(title, quote=True)} — {escape(description, quote=True)}"><span class="stage-number">{number}</span><span><b>{title}</b><small>{description}</small></span><span class="stage-arrow" aria-hidden="true">↗</span></button>''' for stage, number, title, description in s['stages'])
    return f'''<div class="showcase-mosaic restaurant-mosaic" data-showcase data-active-stage="request"><div class="showcase-panel"><img src="/assets/showcase/mesa-clara/restaurant.webp" alt="" width="1536" height="1024" loading="{'eager' if context == 'case' else 'lazy'}"><div class="panel-shade"></div>{restaurant_layers(lang)}<p class="showcase-status" aria-live="polite">{s['stages'][0][2]} — {s['stages'][0][3]}</p></div><div class="showcase-stage-list">{controls}</div></div>'''


def restaurant_product_mockup(lang):
    s = RESTAURANT[lang]
    es = lang == 'es'
    return f'''<section class="product-showcase restaurant-product"><div class="wrap product-showcase-intro"><div><span class="showcase-kicker">{'PRODUCTO' if es else 'PRODUCT'}</span><h2>{s['product_title']}</h2></div><p>{s['product_intro']}</p></div><div class="wrap restaurant-devices"><div class="restaurant-desktop"><div class="desktop-bar"><span></span><span></span><span></span><b>MESA CLARA / {'SALA' if es else 'FLOOR'}</b></div><div class="host-screen"><aside><strong>MESA<br>CLARA</strong><nav><span class="active">{'Sala' if es else 'Floor'}</span><span>{'Reservas' if es else 'Bookings'} <i>34</i></span><span>{'Lista de espera' if es else 'Waitlist'} <i>3</i></span><span>{'Clientes' if es else 'Guests'}</span></nav><small>{'Servicio de cena' if es else 'Dinner service'} · 68%</small></aside><main><header><div><small>{'SÁBADO, 21 SEP' if es else 'SATURDAY, 21 SEP'}</small><h3>{'Servicio de cena' if es else 'Dinner service'}</h3></div><div class="service-switch"><span>19:00</span><b>21:00</b><span>22:30</span></div></header><div class="floor-layout"><div class="table t1"><b>01</b><span>2</span></div><div class="table t2 occupied"><b>04</b><span>4</span></div><div class="table t3"><b>06</b><span>2</span></div><div class="table t4 reserved"><b>08</b><span>4</span><i>21:00</i></div><div class="table t5 occupied"><b>10</b><span>6</span></div><div class="table t6"><b>12</b><span>4</span></div><div class="room-label">{'TERRAZA' if es else 'TERRACE'}</div></div><aside class="booking-rail"><header><b>21:00</b><span>12 {'reservas' if es else 'bookings'}</span></header><article class="highlight"><div><b>Lucía R.</b><small>4 · Mesa 08</small></div><em>!</em><p>{'Alergia · Cumpleaños' if es else 'Allergy · Birthday'}</p></article><article><div><b>Mario D.</b><small>2 · Mesa 06</small></div><p>{'Confirmada' if es else 'Confirmed'}</p></article><article><div><b>Sara P.</b><small>6 · Mesa 10</small></div><p>{'Confirmada' if es else 'Confirmed'}</p></article><button>{'Nueva reserva' if es else 'New booking'} ＋</button></aside></main></div></div><div class="booking-phone"><div class="phone-speaker"></div><div class="booking-phone-screen"><header><span>9:41</span><b>MESA CLARA</b><span>•••</span></header><div class="booking-success"><span>✓</span><small>{'RESERVA CONFIRMADA' if es else 'BOOKING CONFIRMED'}</small><h3>{'Nos vemos el sábado' if es else 'See you on Saturday'}</h3></div><dl><div><dt>{'FECHA' if es else 'DATE'}</dt><dd>21 SEP</dd></div><div><dt>{'HORA' if es else 'TIME'}</dt><dd>21:00</dd></div><div><dt>{'PERSONAS' if es else 'GUESTS'}</dt><dd>4</dd></div><div><dt>{'MESA' if es else 'TABLE'}</dt><dd>08</dd></div></dl><div class="booking-note"><b>{'Hemos anotado tu alergia' if es else 'We’ve noted your allergy'}</b><p>{'El equipo de cocina la revisará antes del servicio.' if es else 'The kitchen team will review it before service.'}</p></div><button>{'Modificar reserva' if es else 'Manage booking'} →</button><small class="booking-address">Mesa Clara · {'Costa de Tenerife' if es else 'Tenerife coast'}</small></div></div></div></section>'''


def invoice_layers(lang):
    es = lang == 'es'
    return f'''
    <div class="stage-layer" data-stage-panel="received"><div class="invoice-mail"><span class="invoice-file">PDF</span><div><span class="ui-kicker">{'FACTURA RECIBIDA' if es else 'INVOICE RECEIVED'}</span><h3>factura_AE-1842.pdf</h3><p>Atlántico Envases · 09:18</p></div><b>1.384,20 €</b></div></div>
    <div class="stage-layer" data-stage-panel="extracted"><div class="invoice-extract"><span class="ui-kicker">{'IA · DATOS EXTRAÍDOS' if es else 'AI · DATA EXTRACTED'}</span><div><label>{'Proveedor' if es else 'Supplier'}<b>Atlántico Envases</b></label><label>{'Factura' if es else 'Invoice'}<b>AE-1842</b></label><label>{'Fecha' if es else 'Date'}<b>17 SEP 2026</b></label><label>{'Total' if es else 'Total'}<b>1.384,20 €</b></label></div><small>12 {'campos detectados · listos para revisar' if es else 'fields detected · ready to review'}</small></div></div>
    <div class="stage-layer" data-stage-panel="matched"><div class="supplier-match"><span class="match-mark">✓</span><span class="ui-kicker">{'PROVEEDOR ENCONTRADO' if es else 'SUPPLIER MATCHED'}</span><h3>Atlántico Envases S.L.</h3><p>ES B76340128 · {'Activo' if es else 'Active'}</p><dl><div><dt>{'Pedido' if es else 'Purchase order'}</dt><dd>PO-0931</dd></div><div><dt>{'Centro' if es else 'Cost centre'}</dt><dd>{'Almacén Norte' if es else 'North warehouse'}</dd></div></dl></div></div>
    <div class="stage-layer" data-stage-panel="checked"><div class="rule-checks"><span class="ui-kicker">{'COMPROBACIONES' if es else 'CHECKS'}</span><ul><li><span>✓</span>{'NIF del proveedor' if es else 'Supplier tax ID'}<b>{'Válido' if es else 'Valid'}</b></li><li><span>✓</span>{'Factura duplicada' if es else 'Duplicate invoice'}<b>{'No encontrada' if es else 'Not found'}</b></li><li><span>✓</span>{'Cálculo de impuestos' if es else 'Tax calculation'}<b>{'Correcto' if es else 'Correct'}</b></li><li class="warning"><span>!</span>{'Importe del pedido' if es else 'Purchase order amount'}<b>{'Diferencia' if es else 'Mismatch'}</b></li></ul></div></div>
    <div class="stage-layer" data-stage-panel="exception"><div class="invoice-exception"><span class="ui-kicker">{'REVISIÓN HUMANA' if es else 'HUMAN REVIEW'}</span><h3>{'El total no coincide' if es else 'The total does not match'}</h3><div><span>PO-0931<b>1.284,20 €</b></span><i>+100,00 €</i><span>AE-1842<b>1.384,20 €</b></span></div><p>{'Posible cargo de transporte no incluido en el pedido.' if es else 'Possible delivery charge not included in the order.'}</p><button type="button">{'Revisar factura' if es else 'Review invoice'} →</button></div></div>
    <div class="stage-layer" data-stage-panel="ready"><div class="entry-ready"><span class="entry-mark">✓</span><span class="ui-kicker">{'REGISTRO PREPARADO' if es else 'ENTRY PREPARED'}</span><h3>AE-1842 · 1.384,20 €</h3><p>{'Aprobado por Laura M. · 10:04' if es else 'Approved by Laura M. · 10:04'}</p><div><span>{'Cuenta' if es else 'Account'}<b>600200</b></span><span>{'Vencimiento' if es else 'Due date'}<b>17 OCT</b></span></div><button type="button">{'Sincronizar con contabilidad' if es else 'Sync to accounting'} →</button></div></div>'''


def invoice_mosaic(lang, context='case'):
    s = INVOICES[lang]
    controls = ''.join(f'''<button class="stage-control" type="button" data-stage="{stage}" data-status="{escape(title, quote=True)} — {escape(description, quote=True)}"><span class="stage-number">{number}</span><span><b>{title}</b><small>{description}</small></span><span class="stage-arrow" aria-hidden="true">↗</span></button>''' for stage, number, title, description in s['stages'])
    return f'''<div class="showcase-mosaic invoice-mosaic" data-showcase data-active-stage="received"><div class="showcase-panel"><img src="/assets/showcase/ladera-norte/finance-desk.webp" alt="" width="1536" height="1024" loading="{'eager' if context == 'case' else 'lazy'}"><div class="panel-shade"></div>{invoice_layers(lang)}<p class="showcase-status" aria-live="polite">{s['stages'][0][2]} — {s['stages'][0][3]}</p></div><div class="showcase-stage-list">{controls}</div></div>'''


def invoice_product_mockup(lang):
    s = INVOICES[lang]
    es = lang == 'es'
    return f'''<section class="product-showcase invoice-product"><div class="wrap product-showcase-intro"><div><span class="showcase-kicker">{'PRODUCTO' if es else 'PRODUCT'}</span><h2>{s['product_title']}</h2></div><p>{s['product_intro']}</p></div><div class="wrap invoice-devices"><div class="invoice-desktop"><div class="desktop-bar"><span></span><span></span><span></span><b>LADERA NORTE / {'FACTURAS' if es else 'INVOICES'}</b></div><div class="finance-screen"><aside><strong>LADERA<br>NORTE</strong><nav><span class="active">{'Bandeja' if es else 'Inbox'} <i>18</i></span><span>{'Por revisar' if es else 'To review'} <i>3</i></span><span>{'Preparadas' if es else 'Prepared'} <i>12</i></span><span>{'Proveedores' if es else 'Suppliers'}</span></nav><small>{'Cierre de septiembre' if es else 'September close'}</small></aside><main><header><div><small>AE-1842 · {'RECIBIDA HOY' if es else 'RECEIVED TODAY'}</small><h3>Atlántico Envases</h3></div><span class="review-pill">{'REVISIÓN' if es else 'REVIEW'}</span></header><div class="invoice-workspace"><section class="document-preview"><div class="paper-brand"><span>AE</span><div><b>ATLÁNTICO</b><small>ENVASES</small></div></div><p>FACTURA · AE-1842</p><dl><div><dt>{'FECHA' if es else 'DATE'}</dt><dd>17.09.2026</dd></div><div><dt>{'PEDIDO' if es else 'ORDER'}</dt><dd>PO-0931</dd></div></dl><div class="invoice-lines"><i></i><i></i><i></i><i></i></div><div class="paper-total"><span>TOTAL</span><b>1.384,20 €</b></div></section><section class="field-review"><div class="field-review-head"><span>✦</span><div><b>{'Datos preparados por IA' if es else 'AI-prepared data'}</b><small>12 {'campos · revisa la diferencia' if es else 'fields · review the discrepancy'}</small></div></div><dl><div><dt>{'Proveedor' if es else 'Supplier'}</dt><dd>Atlántico Envases S.L. <span>✓</span></dd></div><div><dt>{'N.º factura' if es else 'Invoice no.'}</dt><dd>AE-1842 <span>✓</span></dd></div><div><dt>{'Pedido' if es else 'Purchase order'}</dt><dd>PO-0931 <span>✓</span></dd></div><div class="field-warning"><dt>{'Total' if es else 'Total'}</dt><dd>1.384,20 € <span>!</span></dd><small>100,00 € {'sobre el pedido' if es else 'above order'}</small></div><div><dt>{'Vencimiento' if es else 'Due date'}</dt><dd>17 OCT 2026 <span>✓</span></dd></div></dl><footer><button>{'Enviar al proveedor' if es else 'Ask supplier'}</button><button class="approve-invoice">{'Aprobar diferencia' if es else 'Approve difference'} →</button></footer></section></div></main></div></div><div class="approval-phone"><div class="phone-speaker"></div><div class="approval-screen"><header><span>9:41</span><b>LADERA</b><span>•••</span></header><div class="approval-head"><small>{'REQUIERE TU REVISIÓN' if es else 'NEEDS YOUR REVIEW'}</small><h3>Atlántico Envases</h3><p>AE-1842 · 1.384,20 €</p></div><div class="approval-difference"><span>{'DIFERENCIA' if es else 'DIFFERENCE'}</span><b>+100,00 €</b><p>{'Cargo de transporte detectado' if es else 'Delivery charge detected'}</p></div><dl><div><dt>{'Pedido' if es else 'Order'}</dt><dd>1.284,20 €</dd></div><div><dt>{'Factura' if es else 'Invoice'}</dt><dd>1.384,20 €</dd></div></dl><button>{'Aprobar' if es else 'Approve'} →</button><a>{'Ver documento' if es else 'View document'}</a></div></div></div></section>'''


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
    restaurant_url = '/showcase/mesa-clara/' if es else '/en/showcase/mesa-clara/'
    invoice_url = '/showcase/ladera-norte/' if es else '/en/showcase/ladera-norte/'
    restaurant = RESTAURANT[lang]
    invoice = INVOICES[lang]
    header, footer = showcase_shell_parts(lang, '/showcase/', '/en/showcase/')
    head = shared_head(lang, s['index_title'], s['index_intro'], canonical, alternate)
    return f'''{head}<body id="top"><a class="skip" href="#main">{COPY[lang]['skip']}</a>{header}<main id="main" class="showcase-page"><section class="showcase-index-hero wrap"><span class="showcase-kicker">AlexisSantos.dev / {s['nav']}</span><h1>{s['index_title']}.</h1><div><p>{s['index_intro']}</p><small>{s['index_note']}</small></div></section><section class="wrap showcase-feature"><div class="showcase-feature-head"><div><span class="fictional-label">{s['label']}</span><span>{s['eyebrow']}</span></div><h2>{s['case_name']}</h2><p>{s['case_short']}</p><a class="text-link" href="{case_url}">{s['explore']} {ARROW}</a></div>{showcase_mosaic(lang, 'index')}</section><section class="wrap showcase-feature restaurant-feature"><div class="showcase-feature-head"><div><span class="fictional-label">{restaurant['label']}</span><span>{restaurant['eyebrow']}</span></div><h2>{restaurant['name']}</h2><p>{restaurant['short']}</p><a class="text-link" href="{restaurant_url}">{restaurant['explore']} {ARROW}</a></div>{restaurant_mosaic(lang, 'index')}</section><section class="wrap showcase-feature invoice-feature"><div class="showcase-feature-head"><div><span class="fictional-label">{invoice['label']}</span><span>{invoice['eyebrow']}</span></div><h2>{invoice['name']}</h2><p>{invoice['short']}</p><a class="text-link" href="{invoice_url}">{invoice['explore']} {ARROW}</a></div>{invoice_mosaic(lang, 'index')}</section><section class="showcase-future wrap"><span>{'Próximamente' if es else 'Coming next'}</span><p>{'Gestión de propiedades · Servicios profesionales' if es else 'Property management · Professional services'}</p></section></main>{footer}</body></html>'''


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
    return f'''{head}<body id="top"><a class="skip" href="#main">{COPY[lang]['skip']}</a>{header}<main id="main" class="showcase-page"><section class="case-hero wrap"><a class="case-back" href="{index_url}">← {s['back']}</a><div class="case-heading"><div><span class="fictional-label">{s['label']}</span><span>{s['eyebrow']}</span></div><h1>{s['case_name']}</h1><p>{s['case_title']} {s['case_intro']}</p></div></section><section class="wrap case-demo">{showcase_mosaic(lang, 'case')}</section><section class="case-explainer wrap"><div><span class="showcase-kicker">{'EL FLUJO' if es else 'THE WORKFLOW'}</span><h2>{s['how']}</h2></div><p>{s['how_intro']}</p></section>{product_mockup(lang)}<section class="before-after wrap"><article><span>01 / {s['before'].upper()}</span><h3>{s['before']}</h3><p>{s['before_text']}</p></article><article><span>02 / {s['after'].upper()}</span><h3>{s['after']}</h3><p>{s['after_text']}</p></article></section><section class="case-results"><div class="wrap"><div><span class="showcase-kicker">{'RESULTADO' if es else 'OUTCOME'}</span><h2>{s['result']}.</h2></div><ol>{results}</ol></div></section><section class="case-cta wrap"><h2>{s['cta_title']}</h2><div><p>{s['cta_text']}</p><a class="button" href="{contact_url}">{s['cta']} {ARROW}</a></div></section></main>{footer}</body></html>'''


def build_restaurant_page(lang):
    s = RESTAURANT[lang]
    es = lang == 'es'
    canonical = '/showcase/mesa-clara/' if es else '/en/showcase/mesa-clara/'
    alternate = '/en/showcase/mesa-clara/' if es else '/showcase/mesa-clara/'
    index_url = '/showcase/' if es else '/en/showcase/'
    contact_url = '/#contact' if es else '/en/#contact'
    header, footer = showcase_shell_parts(lang, '/showcase/mesa-clara/', '/en/showcase/mesa-clara/')
    head = shared_head(lang, s['name'], s['intro'], canonical, alternate, '/assets/showcase/mesa-clara/restaurant.webp')
    results = ''.join(f'<li><span>0{i}</span>{item}</li>' for i, item in enumerate(s['result_items'], 1))
    return f'''{head}<body id="top"><a class="skip" href="#main">{COPY[lang]['skip']}</a>{header}<main id="main" class="showcase-page restaurant-case"><section class="case-hero wrap"><a class="case-back" href="{index_url}">← {'Todas las demostraciones' if es else 'All showcase cases'}</a><div class="case-heading"><div><span class="fictional-label">{s['label']}</span><span>{s['eyebrow']}</span></div><h1>{s['name']}</h1><p>{s['title']} {s['intro']}</p></div></section><section class="wrap case-demo">{restaurant_mosaic(lang, 'case')}</section><section class="case-explainer wrap"><div><span class="showcase-kicker">{'EL FLUJO' if es else 'THE WORKFLOW'}</span><h2>{s['how']}</h2></div><p>{s['how_intro']}</p></section>{restaurant_product_mockup(lang)}<section class="before-after wrap"><article><span>01 / {s['before'].upper()}</span><h3>{s['before']}</h3><p>{s['before_text']}</p></article><article><span>02 / {s['after'].upper()}</span><h3>{s['after']}</h3><p>{s['after_text']}</p></article></section><section class="case-results"><div class="wrap"><div><span class="showcase-kicker">{'RESULTADO' if es else 'OUTCOME'}</span><h2>{'Lo que cambia' if es else 'What changes'}.</h2></div><ol>{results}</ol></div></section><section class="case-cta wrap"><h2>{'¿Tu equipo pierde tiempo gestionando reservas?' if es else 'Does your team lose time managing bookings?'}</h2><div><p>{'Diseño el flujo alrededor de tu sala, horarios y forma de atender al cliente.' if es else 'I design the workflow around your room, opening hours and the way you serve guests.'}</p><a class="button" href="{contact_url}">{'Cuéntame cómo trabajas' if es else 'Tell me how you work'} {ARROW}</a></div></section></main>{footer}</body></html>'''


def build_invoice_page(lang):
    s = INVOICES[lang]
    es = lang == 'es'
    canonical = '/showcase/ladera-norte/' if es else '/en/showcase/ladera-norte/'
    alternate = '/en/showcase/ladera-norte/' if es else '/showcase/ladera-norte/'
    index_url = '/showcase/' if es else '/en/showcase/'
    contact_url = '/#contact' if es else '/en/#contact'
    header, footer = showcase_shell_parts(lang, '/showcase/ladera-norte/', '/en/showcase/ladera-norte/')
    head = shared_head(lang, s['name'], s['intro'], canonical, alternate, '/assets/showcase/ladera-norte/finance-desk.webp')
    results = ''.join(f'<li><span>0{i}</span>{item}</li>' for i, item in enumerate(s['result_items'], 1))
    return f'''{head}<body id="top"><a class="skip" href="#main">{COPY[lang]['skip']}</a>{header}<main id="main" class="showcase-page invoice-case"><section class="case-hero wrap"><a class="case-back" href="{index_url}">← {'Todas las demostraciones' if es else 'All showcase cases'}</a><div class="case-heading"><div><span class="fictional-label">{s['label']}</span><span>{s['eyebrow']}</span></div><h1>{s['name']}</h1><p>{s['title']} {s['intro']}</p></div></section><section class="wrap case-demo">{invoice_mosaic(lang, 'case')}</section><section class="case-explainer wrap"><div><span class="showcase-kicker">{'EL FLUJO' if es else 'THE WORKFLOW'}</span><h2>{s['how']}</h2></div><p>{s['how_intro']}</p></section>{invoice_product_mockup(lang)}<section class="before-after wrap"><article><span>01 / {s['before'].upper()}</span><h3>{s['before']}</h3><p>{s['before_text']}</p></article><article><span>02 / {s['after'].upper()}</span><h3>{s['after']}</h3><p>{s['after_text']}</p></article></section><section class="case-results"><div class="wrap"><div><span class="showcase-kicker">{'RESULTADO' if es else 'OUTCOME'}</span><h2>{'Lo que cambia' if es else 'What changes'}.</h2></div><ol>{results}</ol></div></section><section class="case-cta wrap"><h2>{'¿Las facturas todavía pasan por demasiadas manos?' if es else 'Do invoices still pass through too many hands?'}</h2><div><p>{'Adapto el flujo a tus proveedores, reglas, aprobaciones y programa de contabilidad.' if es else 'I adapt the workflow to your suppliers, rules, approvals and accounting software.'}</p><a class="button" href="{contact_url}">{'Cuéntame cómo las gestionas' if es else 'Tell me how you handle them'} {ARROW}</a></div></section></main>{footer}</body></html>'''
for lang,t in COPY.items():
 url='/' if lang=='es' else '/en/'
 nav=f'<a href="#solutions">{t["nav"][0]}</a><a href="{'/showcase/' if lang=='es' else '/en/showcase/'}">{SHOWCASE[lang]['nav']}</a>'
 nav+=f'<a href="#projects">{t["nav"][1]}</a><a href="#studio">{t["nav"][2]}</a>'
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
<section id="showcase" class="section wrap home-showcase"><div class="section-head showcase-home-head"><div><span class="fictional-label">{SHOWCASE[lang]['label']}</span><h2>{SHOWCASE[lang]['home_title']}</h2></div><div><p>{SHOWCASE[lang]['home_intro']}</p><a class="text-link" href="{'/showcase/' if lang=='es' else '/en/showcase/'}">{'Ver todas las demos' if lang=='es' else 'View all cases'} {ARROW}</a></div></div>{showcase_mosaic(lang, 'home')}<a class="home-case-teaser" href="{'/showcase/mesa-clara/' if lang=='es' else '/en/showcase/mesa-clara/'}"><img src="/assets/showcase/mesa-clara/restaurant.webp" alt="" width="1536" height="1024" loading="lazy"><span class="fictional-label">{RESTAURANT[lang]['label']}</span><div><small>{RESTAURANT[lang]['eyebrow']}</small><h3>Mesa Clara</h3><p>{RESTAURANT[lang]['short']}</p><b>{RESTAURANT[lang]['explore']} {ARROW}</b></div></a><a class="home-case-teaser invoice-teaser" href="{'/showcase/ladera-norte/' if lang=='es' else '/en/showcase/ladera-norte/'}"><img src="/assets/showcase/ladera-norte/finance-desk.webp" alt="" width="1536" height="1024" loading="lazy"><span class="fictional-label">{INVOICES[lang]['label']}</span><div><small>{INVOICES[lang]['eyebrow']}</small><h3>Ladera Norte</h3><p>{INVOICES[lang]['short']}</p><b>{INVOICES[lang]['explore']} {ARROW}</b></div></a></section>
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
    restaurant_path = ROOT / ('showcase/mesa-clara/index.html' if lang == 'es' else 'en/showcase/mesa-clara/index.html')
    invoice_path = ROOT / ('showcase/ladera-norte/index.html' if lang == 'es' else 'en/showcase/ladera-norte/index.html')
    showcase_path.parent.mkdir(parents=True, exist_ok=True)
    case_path.parent.mkdir(parents=True, exist_ok=True)
    restaurant_path.parent.mkdir(parents=True, exist_ok=True)
    invoice_path.parent.mkdir(parents=True, exist_ok=True)
    showcase_path.write_text(build_showcase_page(lang))
    case_path.write_text(build_nexo_page(lang))
    restaurant_path.write_text(build_restaurant_page(lang))
    invoice_path.write_text(build_invoice_page(lang))

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

public_paths = ["/", "/en/", "/showcase/", "/en/showcase/", "/showcase/nexo-mantenimiento/", "/en/showcase/nexo-maintenance/", "/showcase/mesa-clara/", "/en/showcase/mesa-clara/", "/showcase/ladera-norte/", "/en/showcase/ladera-norte/", "/articles/", "/en/articles/"] + [f"/articles/{entry[0]}/" for entry in entries]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(f"  <url><loc>https://alexissantos.dev{path}</loc></url>" for path in public_paths) + "\n</urlset>\n"
(ROOT / "sitemap.xml").write_text(sitemap)
