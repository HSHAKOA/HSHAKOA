from pathlib import Path
import re,runpy
from PIL import ImageColor
p=Path(__file__).parent
s=(p/'build.py').read_text()
def gray(m):
 r,g,b=ImageColor.getrgb(m.group());v=round(.2126*r+.7152*g+.0722*b);return '#'+f'{v:02x}'*3
s=re.sub(r'#[0-9a-fA-F]{6}',gray,s)
s=s.replace("(8+int(5*v),28+int(13*v),43+int(15*v))","(12+int(12*v),12+int(12*v),12+int(12*v))")
s=s.replace('DA FÁBRICA','FROM THE').replace('AO DIGITAL.','SHOP FLOOR.').replace('Engenharia de Processos · Desenvolvimento de Sistemas','Process Engineering · Software Development').replace('Fundador da NADA Studio','Founder of NADA Studio').replace('PROCESSOS → PRODUTOS DIGITAIS','ENGINEERING → DIGITAL PRODUCTS').replace('ENGENHARIA\'','ENGINEERING\'').replace('AUTOMAÇÃO\'','AUTOMATION\'')
# Keep oversized typography inside the left column.
s=s.replace("'FROM THE',font=F(66,True)","'FROM THE SHOP FLOOR.',font=F(38,True)").replace("'SHOP FLOOR.',font=F(66,True)","'TO SOFTWARE.',font=F(58,True)")
exec(compile(s,str(p/'build_v3.py'),'exec'), {'__file__': str(p/'build_v3.py')})
A=p/'assets'
# The metric refers only to the packing-list task, not total productivity.
(A/'impact.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300"><rect width="1200" height="300" rx="16" fill="#f3f3f3"/><text x="44" y="43" font-family="monospace" font-size="16" fill="#555">SELECTED RESULT / INDUSTRIAL PACKING LIST</text><text x="38" y="157" font-family="sans-serif" font-weight="700" font-size="90" fill="#111">7 min → 1 min</text><text x="44" y="211" font-family="sans-serif" font-size="23" fill="#444">6 minutes saved per packing list · ~86% less preparation time</text><path d="M820 74 V235" stroke="#bbb"/><text x="858" y="153" font-family="sans-serif" font-weight="700" font-size="76" fill="#111">−86%</text><text x="861" y="195" font-family="monospace" font-size="14" fill="#555">TASK PREPARATION TIME</text><text x="44" y="270" font-family="monospace" font-size="13" fill="#666">Reported operational result · Internal application · Source code and operational data remain private</text></svg>''')
def case(file,num,title,sub,lines,stack,tag):
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="580" height="340" viewBox="0 0 580 340"><rect width="580" height="340" rx="14" fill="#141414"/><rect x="1" y="1" width="578" height="338" rx="13" fill="none" stroke="#424242"/><text x="28" y="37" font-family="monospace" font-size="13" fill="#bcbcbc">{num} / {tag}</text><text x="28" y="88" font-family="sans-serif" font-weight="700" font-size="32" fill="#fff">{title}</text><text x="28" y="121" font-family="sans-serif" font-size="16" fill="#bbb">{sub}</text>'
 for i,line in enumerate(lines):svg+=f'<text x="28" y="{174+i*30}" font-family="sans-serif" font-size="18" fill="#e6e6e6">{line}</text>'
 svg+=f'<path d="M28 275 H550" stroke="#444"/><text x="28" y="310" font-family="monospace" font-size="12" fill="#bcbcbc">{stack}</text></svg>'
 (A/(file+'.svg')).write_text(svg)
case('case-packing','01','Packing List','Industrial document workflow',['7 → 1 minute preparation','Forms, reports and traceability','Internal application · Private source'],'PROCESS AUTOMATION · INDUSTRIAL SOFTWARE','OPERATIONAL IMPACT')
case('case-extruda','02','Extruda','Production planning and control',['PVC extrusion operations','Orders, materials and quality','Internal application · Private source'],'PRODUCTION · TRACEABILITY · DATA','INDUSTRIAL SYSTEM')
case('case-apqp','03','APQP / PPAP','Quality and product development',['Project stages and deliverables','Process governance and documentation','Private project · In development'],'QUALITY · ENGINEERING · WORKFLOWS','PRODUCT DEVELOPMENT')
case('case-studio','04','NADA Studio','The company I am building',['Websites and business systems','Automation and service integrations','Public website and company profile'],'FOUNDER · DEVELOPMENT · DIGITAL BUSINESS','COMPANY')
case('case-transcriber','05','Meeting Transcriber','Python audio application',['Audio capture and transcription','Chunk-based processing and exports','Public source · Apache-2.0'],'PYTHON · AUDIO PROCESSING · DOCUMENTATION','OPEN SOURCE')
case('case-barcode','06','Academic Barcode','A public engineering demonstration',['Code 128 production entries','Inventory and transaction history','Fictional data · Public repository'],'PYTHON · SQLITE · TKINTER','ACADEMIC PROJECT')
(A/'studio-band.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="230" viewBox="0 0 1200 230"><rect width="1200" height="230" rx="16" fill="#f4f4f4"/><text x="45" y="46" font-family="monospace" font-size="15" fill="#555">INDEPENDENT THINKING. PRACTICAL SOFTWARE.</text><text x="39" y="137" font-family="sans-serif" font-size="80" font-weight="700" fill="#111">NADA Studio.</text><text x="45" y="188" font-family="sans-serif" font-size="23" fill="#444">Websites · Systems · Automation</text><circle cx="1100" cy="115" r="48" fill="#111"/><path d="M1082 133 L1118 97 M1082 97 H1118 V133" fill="none" stroke="#fff" stroke-width="5"/></svg>''')
print('Monochrome assets built')
