from PIL import Image,ImageDraw,ImageFont
import math, pathlib, json, base64
root=pathlib.Path(__file__).parent
A=root/'assets'
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
mono='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
def F(n,b=False):return ImageFont.truetype(bold if b else font,n)
frames=[]
for k in range(48):
 t=k/48*2*math.pi
 im=Image.new('RGB',(1200,600),'#081c2b');d=ImageDraw.Draw(im)
 for y in range(600):
  v=y/600;d.line((0,y,1200,y),fill=(8+int(5*v),28+int(13*v),43+int(15*v)))
 for x in range(760,1200,36):d.line((x,65,x,515),fill='#173b4d')
 for y in range(80,530,36):d.line((750,y,1180,y),fill='#173b4d')
 cx,cy=970,287
 for rad in [95,145,193]:
  d.ellipse((cx-rad,cy-rad,cx+rad,cy+rad),outline='#285369',width=1)
  pts=[]
  for j in range(34):
   a=t*(1 if rad==145 else -.5)+j*.018
   pts.append((cx+rad*math.cos(a),cy+rad*math.sin(a)))
  d.line(pts,fill='#66e3dc',width=3)
 for j in range(6):
  a=j*math.pi/3-.4; x=cx+145*math.cos(a);y=cy+145*math.sin(a)
  d.line((cx,cy,x,y),fill='#2c6275',width=1)
  p=(k/48+j/6)%1;px=cx+(x-cx)*p;py=cy+(y-cy)*p
  d.ellipse((px-3,py-3,px+3,py+3),fill='#a1f6ef')
  d.rounded_rectangle((x-16,y-16,x+16,y+16),radius=8,fill='#153b4b',outline='#4dabb0')
 d.rounded_rectangle((cx-49,cy-49,cx+49,cy+49),radius=23,fill='#63e0d6')
 d.text((cx-32,cy-27),'JP',font=F(40,True),fill='#092536')
 d.text((52,37),'HSHAKOA',font=F(18,True),fill='#e5f6f5');d.text((820,37),'ENGINEERING × SOFTWARE',font=ImageFont.truetype(mono,14),fill='#8fb3c0')
 d.line((52,80,1148,80),fill='#2c4c5b')
 d.text((48,112),'DA FÁBRICA',font=F(66,True),fill='#f1f6f5')
 d.text((48,187),'AO DIGITAL.',font=F(66,True),fill='#6ce3d9')
 d.text((53,296),'João Paulo Araújo Passos',font=F(29,True),fill='#f2f6f5')
 d.text((53,347),'Engenharia de Processos · Desenvolvimento de Sistemas',font=F(18),fill='#bfd1d8')
 d.text((53,378),'Fundador da NADA Studio',font=F(18),fill='#bfd1d8')
 d.rounded_rectangle((53,442,361,485),radius=21,fill='#d0efea');d.text((74,453),'PROCESSOS → PRODUTOS DIGITAIS',font=F(14,True),fill='#0e3444')
 d.line((52,529,1148,529),fill='#2c4c5b')
 for x,n,s in [(53,'01','ENGENHARIA'),(347,'02','SOFTWARE'),(641,'03','AUTOMAÇÃO'),(934,'04','NADA STUDIO')]:
  d.text((x,551),n,font=F(12),fill='#6ce3d9');d.text((x+32,547),s,font=F(16,True),fill='#c5d8dc')
 frames.append(im)
frames[0].save(A/'hero.gif',save_all=True,append_images=frames[1:],duration=90,loop=0,optimize=True)
frames[0].save(A/'hero-static.png')
def svgcard(name,num,title,desc,stack,color,kind):
 W,H=580,350
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="580" height="350" viewBox="0 0 580 350"><rect width="580" height="350" rx="18" fill="#102a3b"/><rect x="1" y="1" width="578" height="348" rx="17" fill="none" stroke="#315468"/><text x="30" y="39" fill="{color}" font-family="monospace" font-size="13">{num} / {kind}</text><text x="30" y="89" fill="#f1f5f5" font-family="sans-serif" font-size="32" font-weight="700">{title}</text><text x="30" y="124" fill="#c0d4db" font-family="sans-serif" font-size="16">{desc}</text>'''
 if name=='transcritor':
  svg+='<path d="M30 204 H550" stroke="#35586d"/>'
  for i in range(55):
   h=8+abs(math.sin(i*.72)*math.cos(i*.23))*66;x=32+i*9.3
   svg+=f'<rect x="{x}" y="{204-h/2}" width="4" height="{h}" rx="2" fill="{color}"/>'
 elif name=='barcode':
  for i in range(60):
   x=34+i*5;w=1+(i*7%3);h=60
   svg+=f'<rect x="{x}" y="170" width="{w}" height="{h}" fill="{color}"/>'
  svg+='<rect x="385" y="166" width="160" height="70" rx="9" fill="#1c3e50"/><text x="403" y="195" font-family="monospace" font-size="13" fill="#dcebea">Code 128</text><text x="403" y="219" font-family="monospace" font-size="13" fill="#8fded4">SQLite / WAL</text>'
 elif name=='gestos':
  for i,(x,y) in enumerate([(80,230),(125,198),(170,215),(205,166),(247,203),(286,178)]):
   if i:svg+=f'<path d="M{px} {py} L{x} {y}" stroke="{color}" stroke-width="2"/>'
   svg+=f'<circle cx="{x}" cy="{y}" r="7" fill="{color}"/>';px,py=x,y
  svg+='<text x="360" y="207" font-family="monospace" font-size="16" fill="#c0d4db">OpenCV</text><text x="360" y="232" font-family="monospace" font-size="16" fill="#c0d4db">MediaPipe</text>'
 else:
  svg+='<rect x="31" y="159" width="516" height="95" rx="9" fill="#193b4d"/><path d="M31 181 H547" stroke="#35586d"/><circle cx="43" cy="170" r="3" fill="#77d9d0"/><rect x="47" y="194" width="142" height="43" rx="4" fill="#3d797e"/><path d="M208 200 H400 M208 214 H509 M208 228 H465" stroke="#82b8c2" stroke-width="5"/>'
 svg+=f'<path d="M30 280 H550" stroke="#315468"/><text x="30" y="316" fill="{color}" font-family="monospace" font-size="13">{stack}</text><text x="520" y="318" fill="#f1f5f5" font-family="sans-serif" font-size="25">↗</text></svg>'
 (A/(name+'.svg')).write_text(svg)
svgcard('studio','01','NADA Studio','Sites, sistemas e automações para empresas.','NEXT.JS · REACT · TYPESCRIPT','#70e5d7','EMPRESA')
svgcard('transcritor','02','Transcritor de reuniões','Áudio transformado em conteúdo consultável.','PYTHON · ÁUDIO · APACHE-2.0','#8bc6ff','PROJETO ABERTO')
svgcard('barcode','03','Barcode acadêmico','Produção, estoque e histórico por leitura.','PYTHON · TKINTER · SQLITE','#ffcd87','ENGENHARIA APLICADA')
svgcard('gestos','04','Visão computacional','Reconhecimento de gestos em tempo real.','PYTHON · OPENCV · MEDIAPIPE','#a5d7ad','EXPERIMENTAÇÃO')
(A/'studio-band.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="230" viewBox="0 0 1200 230"><rect width="1200" height="230" rx="18" fill="#c9eee5"/><text x="45" y="49" font-family="monospace" font-size="15" fill="#23535d">CONHEÇA A EMPRESA QUE ESTOU CONSTRUINDO</text><text x="40" y="137" font-family="sans-serif" font-size="78" font-weight="700" fill="#123b49">NADA Studio.</text><text x="45" y="188" font-family="sans-serif" font-size="22" fill="#23535d">Desenvolvimento com visão de processo e de negócio.</text><circle cx="1100" cy="115" r="48" fill="#123b49"/><path d="M1082 133 L1118 97 M1082 97 H1118 V133" fill="none" stroke="#c9eee5" stroke-width="5"/></svg>''')
print(json.dumps({p.name:p.stat().st_size for p in A.iterdir()}))
