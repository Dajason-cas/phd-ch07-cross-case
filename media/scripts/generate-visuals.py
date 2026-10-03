"""Rebuild chapter figures offline. Requires reportlab (and Pillow for raster panels).
Run with Python from any working directory. PDF core Helvetica is safely referenced;
no proprietary font file is bundled. All diagrams are conceptual, not experiment outputs.
Solid arrows show processing/dependency; dashed arrows/boxes show an undocumented
interface or unresolved relationship. See FIGURE_PLAN.md for exact evidence provenance.
"""
from pathlib import Path
import math, textwrap
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.lib.utils import ImageReader
from PIL import Image

MEDIA = Path(__file__).resolve().parents[1]
INK = HexColor('#243746')
BLUE = HexColor('#e6eff6')
TEAL = HexColor('#e4f1ee')
GREY = HexColor('#f0f2f4')
ORANGE = HexColor('#f9eee0')

def start(name, height=360):
    c = canvas.Canvas(str(MEDIA/name), pagesize=(540, height), invariant=1)
    c.setTitle(name.removesuffix('.pdf')); c.setAuthor('Thesis visual workflow')
    return c

def txt(c, x, y, text, size=11, align='center', bold=False, leading=None):
    c.setFillColor(INK);c.setFont('Helvetica-Bold' if bold else 'Helvetica',size)
    for i,line in enumerate(text.split('\n')):
        getattr(c, {'center':'drawCentredString','left':'drawString','right':'drawRightString'}[align])(x,y-i*(leading or size*1.25),line)

def box(c,x,y,w,h,text,fill=GREY,dashed=False,size=11):
    c.setStrokeColor(INK);c.setFillColor(fill);c.setLineWidth(1)
    c.setDash(4,3) if dashed else c.setDash()
    c.roundRect(x,y,w,h,5,stroke=1,fill=1);c.setDash()
    lines=text.split('\n');font='Helvetica'
    from reportlab.pdfbase.pdfmetrics import stringWidth
    assert all(stringWidth(line,font,size) <= w-10 for line in lines), (text,w)
    assert len(lines)*size*1.25 <= h-8, (text,h)
    txt(c,x+w/2,y+h/2+(len(lines)-1)*size*0.625-size*0.32,text,size)

def arrow(c,x,y,a,b,dashed=False):
    c.setStrokeColor(INK);c.setFillColor(INK);c.setLineWidth(1.2)
    c.setDash(4,3) if dashed else c.setDash();c.line(x,y,a,b);c.setDash()
    ang=math.atan2(b-y,a-x);p=c.beginPath();p.moveTo(a,b)
    p.lineTo(a-6*math.cos(ang-.45),b-6*math.sin(ang-.45))
    p.lineTo(a-6*math.cos(ang+.45),b-6*math.sin(ang+.45));p.close();c.drawPath(p,fill=1,stroke=0)

def chain(c,labels,y=180,h=56,fill=GREY,size=11):
    n=len(labels);gap=16;w=(510-gap*(n-1))/n
    for i,s in enumerate(labels):
        x=15+i*(w+gap);box(c,x,y,w,h,s,fill,size=size)
        if i<n-1:arrow(c,x+w,y+h/2,x+w+gap,y+h/2)

def note(c,text,y=20):txt(c,270,y,text,10)
def finish(c):c.showPage();c.save()

def panels(name, items, columns=2, cell_height=170):
    # Preserve complete raster evidence: aspect fit, no contrast/palette alteration.
    rows=(len(items)+columns-1)//columns;H=rows*cell_height+20;c=start(name,H)
    cw=510/columns
    for k,(file,label) in enumerate(items):
        x=15+(k%columns)*cw;y=H-15-(k//columns)*cell_height
        txt(c,x+cw/2,y,label,10)
        with Image.open(MEDIA/file) as im:
            iw,ih=im.size;factor=min((cw-12)/iw,(cell_height-28)/ih)
            w,h=iw*factor,ih*factor
            c.drawImage(ImageReader(im),x+(cw-w)/2,y-18-h,w,h,mask='auto')
    finish(c)

def score_plot(name, classes, metrics, values, paired=False):
    # Exact source rows only. No interpolation, error bars, or significance encoding.
    panel_h=len(classes)*28+48;H=panel_h*3+60;c=start(name,H)
    if paired:
        txt(c,270,H-15,'Open circle: standard   /   Filled square: temperature-aware',10)
    else:txt(c,270,H-15,'Source-reported EL class rows',12,bold=True)
    for m,title in enumerate(metrics):
        top=H-42-m*panel_h;txt(c,15,top,title,12,'left',True)
        for tick in [0,.2,.4,.6,.8,1.]:
            x=125+tick*280;c.setStrokeColor(GREY);c.line(x,top-12,x,top-18-len(classes)*28)
            txt(c,x,top-32-len(classes)*28,f'{tick:.1f}',9)
        for k,label in enumerate(classes):
            y=top-26-k*28;txt(c,15,y-3,label,10,'left')
            a=values[k][m];x=125+a*280;c.setStrokeColor(INK);c.setFillColor(white)
            c.circle(x,y,3.3,fill=1,stroke=1)
            if paired:
                b=values[k][m+3];z=125+b*280;c.line(x,y,z,y);c.setFillColor(INK);c.rect(z-3,y-3,6,6,fill=1,stroke=0)
                txt(c,525,y-3,f'{a:.3f} / {b:.3f}',10,'right')
            else:txt(c,460,y-3,f'{a:.3f}',11,'left')
    note(c,'Score (0-1). Source protocol and limitations remain in the caption.',15);finish(c)


c=start('fig-ch07-01-cross-case-information-model.pdf',475)
stages=['Sensor\nevidence','Domain-relevant\nrepresentation','Localized\nprediction','Structural\nassociation','Interpretation\n/ policy','Traceable\noutput']
thermal=['UAV thermal','Rendered + T','Boxes / masks','Module / row','Candidate group','Map / retrieval']
el=['EL module','Module + cells','Defect / cells','Affected cells','Coverage policy','Module report']
txt(c,200,450,'Shared function',12,bold=True);txt(c,350,450,'Thermal realization',11,bold=True);txt(c,480,450,'EL realization',11,bold=True)
for i,s in enumerate(stages):
 y=370-i*57;box(c,95,y,170,45,s,GREY)
 if i<5:arrow(c,180,y,180,y-12)
 box(c,280,y,125,45,thermal[i],BLUE,size=10);box(c,420,y,110,45,el[i],TEAL,size=10)
 # Column alignment maps the two realizations to the shared function;
 # no arrow runs between the thermal and EL implementations.
txt(c,50,230,'Evidence',10);txt(c,50,211,'retained',10)
c.setStrokeColor(INK);c.line(55,390,55,100);arrow(c,55,100,95,100)
note(c,'Rows align shared functions with two distinct case realizations.',46)
note(c,'Distinct software, datasets and validation; no universal architecture or ranking.',25)
finish(c)

c=start('fig-ch07-02-stage-wise-dependability.pdf',500)
txt(c,270,478,'Stage-specific evidence gates and error propagation',13,bold=True)
labels=['Acquisition','Representation','Localization','Structural association','Interpretation / policy','Reporting / retrieval']
examples=[('Sensor / conditions','Excitation / exposure'),('Temperature alignment','Module / cell geometry'),('Bounded detector metrics','Protocol incomplete'),('Geometric grouping only','Association rule unknown'),('Candidate, not diagnosis','Policy, not physical severity'),('Coverage != position error','Report correctness unbenchmarked')]
for i,s in enumerate(labels):
 y=398-i*58;box(c,15,y,180,46,s,GREY,size=11)
 txt(c,215,y+30,examples[i][0],10,'left');txt(c,215,y+11,examples[i][1],10,'left')
 if i<5:
  arrow(c,105,y,105,y-12)
  c.setStrokeColor(INK);c.setDash(3,3);c.line(200,y-6,525,y-6);c.setDash()
txt(c,360,455,'Thermal example / EL example',10)
note(c,'Dashed gates: each transition needs evidence beyond its upstream component.',48)
note(c,'Errors can propagate. No end-to-end metric, maturity score or case ranking.',26)
finish(c)
