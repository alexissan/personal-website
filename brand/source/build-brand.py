from pathlib import Path
from html import escape
import io, json, shutil, subprocess
from fontTools.ttLib import TTFont as FTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.units import mm
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
import qrcode

B=Path(__file__).resolve().parents[1]
ROOT=B.parent
INK='#20242B'; PAPER='#F5F6F8'; BLUE='#496F99'; SLATE='#606977'; MIST='#DCE0E6'
for filename,weight,alias in [('Manrope',800,'Display'),('DMSans',400,'Body'),('DMSans',600,'Medium')]:
 f=FTFont(B/'fonts'/f'{filename}-Variable.ttf')
 axes={'wght':weight}
 if 'opsz' in [a.axisTag for a in f['fvar'].axes]:axes['opsz']=14
 f=instantiateVariableFont(f,axes,inplace=True)
 path=B/'fonts'/f'{filename}-{weight}.ttf';f.save(path)
 pdfmetrics.registerFont(TTFont(alias,str(path)))
pdfmetrics.registerFont(TTFont('DM Sans',str(B/'fonts/DMSans-400.ttf')))
pdfmetrics.registerFont(TTFont('DM Sans-Bold',str(B/'fonts/DMSans-600.ttf')))
pdfmetrics.registerFontFamily('DM Sans',normal='DM Sans',bold='DM Sans-Bold',italic='DM Sans',boldItalic='DM Sans-Bold')
for name in ['Manrope','DMSans']:
 f=FTFont(B/'fonts'/f'{name}-Variable.ttf');f.flavor='woff2';f.save(ROOT/'assets/studio'/f'{name}.woff2')
font=FTFont(B/'fonts/Manrope-800.ttf');glyphs=font.getGlyphSet();cmap=font.getBestCmap();upm=font['head'].unitsPerEm

def text_paths(text,size=64,x=0,y=72,color=INK):
 out=[];cursor=x;scale=size/upm
 for ch in text:
  name=cmap[ord(ch)];pen=SVGPathPen(glyphs);glyphs[name].draw(pen)
  out.append(f'<path fill="{color}" transform="translate({cursor:.3f} {y}) scale({scale:.6f} {-scale:.6f})" d="{pen.getCommands()}"/>')
  cursor+=(font['hmtx'][name][0]*scale-size*.045)
 return ''.join(out),cursor-x

def symbol(color=INK,accent=BLUE):
 return f'<g transform="translate(5 25) scale(.205)"><path fill="{color}" d="M0 215L173 20Q184 8 207 8H242L226 94L201 108L208 55L52 215Z M113 176L231 115L225 162H313Q335 162 335 145Q335 131 316 131H287Q253 131 247 103L293 83H321Q382 83 394 125Q415 173 372 202Q353 215 322 215H203L209 176Z M238 86C221 56 246 7 290 5L419 0Z"/></g>'

def svg(body,w,h):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="AlexisSantos.dev">{body}</svg>'
logos={}
for variant,color,accent in [('charcoal',INK,BLUE),('white','#FFFFFF','#FFFFFF'),('black','#000000','#000000')]:
 word,width=text_paths('AlexisSantos.dev',64,0,66,color)
 word+=f'<circle cx="{width+10}" cy="61" r="4.5" fill="{accent}"/>'
 logos[f'wordmark-{variant}']=svg(word,round(width+22),82)
 logos[f'symbol-{variant}']=svg(symbol(color,accent),96,96)
 mark=f'<g transform="translate(0 -18) scale(1.2)">{symbol(color,accent)}</g>'
 text,width=text_paths('AlexisSantos.dev',64,130,66,color)
 logos[f'logo-{variant}']=svg(mark+text,round(width+139),82)
 stacked1,w1=text_paths('Alexis',100,0,90,color);stacked2,w2=text_paths('Santos.dev',100,0,185,color)
 logos[f'stacked-{variant}']=svg(stacked1+stacked2,max(round(w1),round(w2))+5,206)
for name,content in logos.items():(B/'logos'/f'{name}.svg').write_text(content)
shutil.copyfile(B/'logos/wordmark-charcoal.svg',ROOT/'assets/studio/wordmark.svg')
shutil.copyfile(B/'logos/logo-charcoal.svg',ROOT/'assets/studio/logo.svg')
(ROOT/'assets/studio/favicon.svg').write_text(svg(f'<rect width="96" height="96" rx="18" fill="{INK}"/><g transform="translate(10 10) scale(.79)">{symbol("#FFFFFF","#A3BEDB")}</g>',96,96))

def draw_svg(c,content,x,y,w):
 d=svg2rlg(io.BytesIO(content.encode()));factor=w/d.width
 c.saveState();c.translate(x,y);c.scale(factor,factor);renderPDF.draw(d,c,0,0);c.restoreState()
 return d.height*factor

def txt(c,s,x,y,size=12,font='Body',color=INK):
 c.setFont(font,size);c.setFillColor(HexColor(color));c.drawString(x,y,s)

def para(c,text,x,y,width,size=12,leading=19,color=SLATE):
 line=''
 for word in text.split():
  trial=(line+' '+word).strip()
  if pdfmetrics.stringWidth(trial,'Body',size)>width and line:
   txt(c,line,x,y,size,color=color);y-=leading;line=word
  else:line=trial
 if line:txt(c,line,x,y,size,color=color);y-=leading
 return y

def bg(c,w,h,color):
 c.setFillColor(HexColor(color));c.rect(0,0,w,h,fill=1,stroke=0)

def qr_svg(url,x,y,size):
 q=qrcode.QRCode(border=4,error_correction=qrcode.constants.ERROR_CORRECT_M);q.add_data(url);q.make(fit=True)
 matrix=q.get_matrix();unit=size/len(matrix)
 out=[f'<rect x="{x}" y="{y}" width="{size}" height="{size}" fill="white"/>']
 for row,values in enumerate(matrix):
  for col,on in enumerate(values):
   if on:out.append(f'<rect x="{x+col*unit}" y="{y+row*unit}" width="{unit+.02}" height="{unit+.02}" fill="{INK}"/>')
 return ''.join(out)

def template_svg(body,w,h):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w/10}mm" height="{h/10}mm" viewBox="0 0 {w} {h}">{body}</svg>'

def st(text,x,y,size=26,weight=400,color=INK):
 return f'<text x="{x}" y="{y}" font-family="DM Sans" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(text)}</text>'

def place_logo(name,x,y,width):
 source=logos[name];vw,vh=[float(v) for v in source.split('viewBox="')[1].split('"')[0].split()[2:]]
 body=source.split('>',1)[1].rsplit('</svg>',1)[0]
 return f'<g transform="translate({x} {y}) scale({width/vw})">{body}</g>'

def symbol_pattern(x,y,scale,color):
 return f'<g transform="translate({x} {y}) scale({scale})">{symbol(color,color)}</g>'

cards=[];flyers=[]
for lang in ['es','en']:
 front=f'<rect width="910" height="610" fill="{INK}"/>'+symbol_pattern(505,-105,5,'#2A3038')+place_logo('stacked-white',85,100,580)
 front+=st('Diseño. Código. Criterio.' if lang=='es' else 'Design. Code. Care.',90,500,23,color='#CFD6DF')
 front+=f'<path d="M760 510L796 490H812L776 510Z" fill="#A3BEDB"/>'
 back=f'<rect width="910" height="610" fill="{PAPER}"/>'+place_logo('logo-charcoal',80,80,590)
 back+=st('Alexis Santos',80,260,41,600)+st('Fundador · Diseño y desarrollo' if lang=='es' else 'Founder · Design & development',80,300,22)
 back+=st('alexis.santos.perez@gmail.com',80,382,25)+st('alexissantos.dev',80,420,25,600)+st('Tenerife, España' if lang=='es' else 'Tenerife, Spain',80,475,21,color=SLATE)
 back+=qr_svg('https://alexissantos.dev/'+('en/' if lang=='en' else ''),655,315,165)
 for side,body in [('front',front),('back',back)]:
  path=B/'templates'/f'business-card-{lang}-{side}.svg';path.write_text(template_svg(body,910,610));cards.append(path)
 w,h=1540,2160
 body=f'<rect width="{w}" height="{h}" fill="{PAPER}"/>'+place_logo('logo-charcoal',120,120,950)
 body+=symbol_pattern(800,1000,8,'#E4E9EF')
 lines=['Tu negocio.','Su próxima','gran versión.'] if lang=='es' else ['Your business.','Its next','big chapter.']
 y=480
 for line in lines:
  p,_=text_paths(line,143,120,y);body+=p;y+=164
 body+=st('Webs, aplicaciones e IA para negocios locales.' if lang=='es' else 'Websites, apps and AI for local businesses.',120,1040,40)
 lines=['Una web que atraiga clientes.','Una app que simplifique tu trabajo.','IA que te quite tareas de encima.'] if lang=='es' else ['A website that brings in customers.','An app that makes work simpler.','AI that takes tasks off your plate.']
 for i,line in enumerate(lines):body+=st(line,120,1190+i*70,35)
 body+=f'<path d="M120 1450H1420" stroke="#BEC8D4" stroke-width="2"/>'
 body+=st('Cuéntame tu idea.' if lang=='es' else 'Tell me about your idea.',120,1610,64,600)
 body+=st('alexissantos.dev',120,1715,48,600)+st('alexis.santos.perez@gmail.com',120,1790,33)
 body+=st('Alexis Santos · Tenerife',120,1920,31,color=SLATE)
 body+=qr_svg('https://alexissantos.dev/'+('en/' if lang=='en' else ''),1120,1600,300)
 path=B/'templates'/f'flyer-a5-{lang}.svg';path.write_text(template_svg(body,w,h));flyers.append(path)

for files,name,trim in [(cards,'business-cards-es-en.pdf',(85,55)),(flyers,'flyers-a5-es-en.pdf',(148,210))]:
 full=((trim[0]+6)*mm,(trim[1]+6)*mm);temp=Path('/tmp')/name
 c=canvas.Canvas(str(temp),pagesize=full);c.setTitle(name.replace('-',' ').replace('.pdf',''));c.setAuthor('Alexis Santos')
 for file in files:
  drawing=svg2rlg(str(file));factor=full[0]/drawing.width;c.saveState();c.scale(factor,factor);renderPDF.draw(drawing,c,0,0);c.restoreState();c.showPage()
 c.save();reader=PdfReader(temp);writer=PdfWriter()
 for page in reader.pages:
  page.trimbox=RectangleObject([3*mm,3*mm,full[0]-3*mm,full[1]-3*mm]);page.bleedbox=RectangleObject([0,0,*full]);writer.add_page(page)
 with (B/'print'/name).open('wb') as handle:writer.write(handle)

W,H=960,640
c=canvas.Canvas(str(B/'brand-guide.pdf'),pagesize=(W,H));c.setTitle('AlexisSantos.dev | Brand system v2');c.setAuthor('Alexis Santos')
def page(title,n):
 bg(c,W,H,PAPER);txt(c,'AlexisSantos.dev / Brand system v2',45,602,11,'Medium');txt(c,f'{n:02}',895,602,11,'Medium');txt(c,title,45,530,43,'Display')
def finish():c.showPage()
bg(c,W,H,INK);draw_svg(c,logos['symbol-white'],700,370,190);draw_svg(c,logos['stacked-white'],55,245,580);txt(c,'An independent studio. A bold, practical identity.',60,155,22,color='#CAD4DF');txt(c,'Websites / Applications / Artificial intelligence',60,116,14,color='#CAD4DF');txt(c,'Brand system v2    |    September 2026',60,48,11,color='#CAD4DF');finish()
page('One identity. Different formats.',2)
draw_svg(c,logos['logo-charcoal'],55,380,610);txt(c,'Primary logo',55,345,13,'Medium');para(c,'Use for stationery, flyers, proposals and introductions. The AS monogram and name always keep their supplied proportions.',55,320,540)
draw_svg(c,logos['wordmark-charcoal'],55,205,430);txt(c,'Wordmark / small horizontal spaces',55,175,12,'Medium')
draw_svg(c,logos['symbol-charcoal'],735,375,100);txt(c,'Symbol',730,345,13,'Medium');para(c,'For avatars, favicons and supporting graphic elements. Pair it with the name on first contact.',690,320,200)
bgx=680;c.setFillColor(HexColor(INK));c.roundRect(bgx,85,225,140,8,fill=1,stroke=0);draw_svg(c,logos['logo-white'],700,135,185)
para(c,'Charcoal on pearl. White on charcoal. Solid black for one-colour printing. Do not add shadows, stretch the logo or rebuild it with typed text.',55,100,540,size=12);finish()
page('Room to breathe. Built to last.',3)
draw_svg(c,logos['logo-charcoal'],95,355,700);c.setStrokeColor(HexColor(BLUE));c.setDash(4,4);c.rect(70,323,750,140,fill=0,stroke=1);c.setDash();txt(c,'Clear space = at least 1/4 of the symbol height on all sides.',70,288,14,'Medium')
para(c,'Minimum sizes: full logo 180 px / 38 mm. Wordmark 140 px / 30 mm. Symbol 32 px / 8 mm. For a 16 px favicon, use the supplied simplified favicon, not the full logo.',70,242,750,size=15,leading=24)
para(c,'The custom AS monogram joins Alexis and Santos into a forward-leaning silhouette. A diagonal cut gives the letters space and direction. Keep that cut open at every size; never add a surrounding frame.',70,140,750,size=15,leading=24)
finish()
page('Quiet colour. Confident type.',4)
colors=[('Charcoal',INK),('Pearl',PAPER),('Slate',SLATE),('Studio blue',BLUE),('Mist',MIST)]
for i,(name,value) in enumerate(colors):
 x=45+i*178;c.setFillColor(HexColor(value));c.setStrokeColor(HexColor(MIST));c.rect(x,355,155,112,fill=1,stroke=1);txt(c,name,x,330,13,'Medium');txt(c,value,x,308,12)
txt(c,'Manrope ExtraBold',45,245,34,'Display');txt(c,'Headlines and the outlined wordmark.',45,212,14)
txt(c,'DM Sans',520,245,34,'Body');txt(c,'Body text, labels and contact details.',520,212,14)
para(c,'Use charcoal and pearl for most of a composition. Blue is a small accent, not a background theme. Product photography may introduce its own colours. Never rely on the accent alone to communicate meaning.',45,140,850,size=14,leading=22)
para(c,'Both font families are bundled under the SIL Open Font License. Print masters use embedded fonts or outlines. HEX/RGB are the digital masters; ask the printer for its ICC profile before a final CMYK conversion.',45,70,850,size=11,leading=16);finish()
page('The voice belongs to a person.',5)
txt(c,'ES',45,454,12,'Medium',BLUE);txt(c,'Diseño con intención.',45,410,29,'Display');txt(c,'Tecnología con impacto.',45,373,29,'Display')
txt(c,'EN',520,454,12,'Medium',BLUE);txt(c,'Design with purpose.',520,410,29,'Display');txt(c,'Technology with impact.',520,373,29,'Display')
para(c,'Speak in the first person. Alexis is the person who designs and builds. Explain what changes for the business: more enquiries, simpler bookings, less admin. Avoid claiming a large team, guaranteed results or clients that do not exist.',45,290,400,size=14,leading=23)
para(c,'Keep the writing direct and human. Spanish should sound natural in Spain; English should read as original copy. Use the full brand name AlexisSantos.dev. Product brands Breathe Now and Lean Cam keep their own identities.',520,290,385,size=14,leading=23)
para(c,'Imagery: natural light, tactile materials, architecture and real product context. Silver and frosted glass support the identity; they are not the logo. Generated device scenes are illustrative, not literal app screenshots.',45,115,850,size=14,leading=22);finish()
page('Ready for the next conversation.',6)
for file,x,y in [(cards[0],45,255),(cards[1],505,255)]:
 d=svg2rlg(str(file));scale=370/d.width;c.saveState();c.translate(x,y);clip=c.beginPath();clip.rect(0,0,370,d.height*scale);c.clipPath(clip,stroke=0,fill=0);c.scale(scale,scale);renderPDF.draw(d,c,0,0);c.restoreState()
para(c,'Business cards: 85 x 55 mm finished, plus 3 mm bleed. PDF pages: Spanish front/back, English front/back. The source SVGs remain editable.',45,235,400,size=14,leading=22)
para(c,'A5 flyers: 148 x 210 mm finished, plus 3 mm bleed. PDF pages: Spanish, then English. QR codes point to the language-specific website.',490,235,400,size=14,leading=22)
para(c,'Print at 100%. Keep the TrimBox and BleedBox. Ask your printer for its stock, colour profile and PDF/X requirements; these are vector print masters, not a certified PDF/X press proof. There is no need to invent a telephone number or address.',45,118,850,size=13,leading=21)
finish();c.save()

tokens={'brand':'AlexisSantos.dev','version':'2.0','colors':{'charcoal':INK,'pearl':PAPER,'slate':SLATE,'blue':BLUE,'mist':MIST},'typography':{'display':{'family':'Manrope','weight':800},'body':{'family':'DM Sans','weight':400}},'logo':{'primary':'logos/logo-charcoal.svg','reverse':'logos/logo-white.svg','mono':'logos/logo-black.svg','wordmark':'logos/wordmark-charcoal.svg','symbol':'logos/symbol-charcoal.svg'},'tagline':{'es':'Diseño con intención. Tecnología con impacto.','en':'Design with purpose. Technology with impact.'}}
(B/'tokens.json').write_text(json.dumps(tokens,indent=2,ensure_ascii=False)+'\n')
for name in ['logo-charcoal','logo-white','symbol-charcoal','symbol-white','wordmark-charcoal']:
 d=svg2rlg(str(B/'logos'/f'{name}.svg'));renderPDF.drawToFile(d,f'/tmp/{name}.pdf')
print('Created 12 outlined SVG logos, fonts, 6 editable templates and 3 PDFs.')
