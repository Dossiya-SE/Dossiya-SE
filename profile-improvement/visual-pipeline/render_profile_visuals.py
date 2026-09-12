#!/usr/bin/env python3
from __future__ import annotations
import json, math, subprocess, sys
from html import escape
from pathlib import Path
from render_research_state import render_research_state

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
DATA=HERE/'synthetic_profile_data.json'
SOURCE=HERE/'generate_synthetic_math.py'
OUT=ROOT/'assets'/'math-art'
if not DATA.exists(): subprocess.run([sys.executable,str(SOURCE)],cwd=ROOT,check=True)
M=json.loads(DATA.read_text(encoding='utf-8'))['models']; OUT.mkdir(parents=True,exist_ok=True)
INK='#111318'; MUTED='#5F6670'; HAIR='#D9DDE2'; SOFT='#F7F7F5'; GOLD='#B58A37'; GOLD2='#F2EAD8'; GRID='#CDD3DA'
FONT="'DejaVu Sans', Arial, Helvetica, sans-serif"
SERIF="Georgia, 'Times New Roman', serif"

def esc(x): return escape(str(x))
def pts(seq): return ' '.join(f'{x:.1f},{y:.1f}' for x,y in seq)
def polyline(seq,stroke=INK,w=2,fill='none',dash=None):
 d=f' stroke-dasharray="{dash}"' if dash else ''
 return f'<polyline points="{pts(seq)}" fill="{fill}" stroke="{stroke}" stroke-width="{w}"{d}/>'
def path(seq,stroke=INK,w=2,fill='none',dash=None):
 d='M '+' L '.join(f'{x:.1f} {y:.1f}' for x,y in seq); ds=f' stroke-dasharray="{dash}"' if dash else ''
 return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{w}"{ds}/>'
def text(x,y,s,size=20,anchor='start',weight='400',style='',fill=INK,family=None):
 fam=family or FONT
 return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="{fam}" font-size="{size}" font-weight="{weight}" font-style="{style}" fill="{fill}">{esc(s)}</text>'
def line(x1,y1,x2,y2,stroke=INK,w=2,dash=None):
 d=f' stroke-dasharray="{dash}"' if dash else ''
 return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{w}"{d}/>'
def circle(x,y,r=5,fill=INK,stroke='none',w=1): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{w}"/>'
def rect(x,y,w,h,fill='none',stroke=HAIR,sw=1,rx=0): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def arrow(x1,y1,x2,y2,stroke=INK,w=2,dash=None): return line(x1,y1,x2,y2,stroke,w,dash)+f'<path d="M {x2-9} {y2-5} L {x2} {y2} L {x2-9} {y2+5}" fill="none" stroke="{stroke}" stroke-width="{w}"/>'
def chain(cx,y,labels,size=14,gap=34,fill=INK):
 widths=[max(60,len(s)*size*.58) for s in labels]; total=sum(widths)+gap*(len(labels)-1); x=cx-total/2; out=[]
 for i,(lab,wid) in enumerate(zip(labels,widths)):
  out.append(text(x+wid/2,y,lab,size,'middle','600',fill=fill)); x+=wid
  if i<len(labels)-1:
   out.append(arrow(x+6,y-5,x+gap-6,y-5,GOLD,1.1)); x+=gap
 return ''.join(out)
def header(w,h,title,desc,meta):
 return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{esc(title)}</title><desc id="desc">{esc(desc)}</desc><metadata>{esc(meta)}</metadata><style>:root{{--bg:#FFFFFF;--ink:{INK};}}@media(prefers-color-scheme:dark){{:root{{--bg:#FFFFFF;--ink:{INK};color-scheme:light;}}}}text{{font-family:{FONT};}}</style><rect width="100%" height="100%" fill="#FFFFFF"/>'''
def close(): return '</svg>\n'
def write(name,body): (OUT/name).write_text(body,encoding='utf-8')

def map_xy(data,x0,y0,w,h):
 xs=[p[0] for p in data]; ys=[p[1] for p in data]; xmin,xmax=min(xs),max(xs); ymin,ymax=min(ys),max(ys)
 return [(x0+(x-xmin)/(xmax-xmin)*w, y0+h-(y-ymin)/(ymax-ymin)*h) for x,y in data]

def layer_graph(x0,y0,w,h,show_labels=True):
 g=M['multilayer_graph']; layers=g['layers']; by={L:[] for L in layers}
 for n in g['nodes']: by[n['layer']].append(n)
 labels=['Power','Transportation','Information','Organization']; out=[]; ys=[y0+24,y0+68,y0+112,y0+156]
 left=x0+(100 if show_labels else 8); span=w-(118 if show_labels else 20); xs=[left+j*span/4 for j in range(5)]
 for L,lab,yy in zip(layers,labels,ys):
  nodes=sorted(by[L],key=lambda n:n['x']); base=round(nodes[0]['y']); offs=[n['y']-base for n in nodes]; Y=[yy-o*180 for o in offs]
  plane=[(left-18,yy-18),(left+span-10,yy-24),(left+span+22,yy-3),(left+6,yy+4)]; out.append(f'<polygon points="{pts(plane)}" fill="{SOFT}" stroke="{HAIR}" stroke-width="1"/>')
  out.append(polyline(list(zip(xs,Y)),w=1.5));
  if show_labels: out.append(text(x0,yy+5,lab.upper(),14,weight='700'))
  for xx,yyy in zip(xs,Y): out.append(circle(xx,yyy,4.2))
 for j,x in enumerate(xs): out.append(line(x,ys[0]-8,x,ys[-1]+8,GOLD,1.0,'5 5'))
 return ''.join(out)

def viability(x0,y0,w,h,labels=True):
 data=map_xy(M['viability_boundary']['data'],x0+28,y0+28,w-120,h-56); out=[path(data,INK,1.8,GOLD2)]
 out += [arrow(x0+18,y0+h-18,x0+w-18,y0+h-18,INK,1.4),arrow(x0+28,y0+h-10,x0+28,y0+12,INK,1.4)]
 px,py=x0+w*.45,y0+h*.57; qx,qy=x0+w*.70,y0+h*.34
 out += [circle(px,py,5),circle(qx,qy,5,GOLD),line(px,py,qx,qy,GOLD,1.8,'6 5')]
 if labels:
  out += [text(x0+w*.42,y0+h*.48,'V',28,weight='700'),text(qx+10,qy-5,'boundary ∂V',14),text(x0+w*.78,y0+h*.48,'ρ(x) = d(x, ∂V)',16),text(x0+w*.78,y0+h*.60,'distance to loss of viability',12,style='italic',fill=MUTED)]
 return ''.join(out)

def hero():
 W,H=2048,640; b=[header(W,H,'Dossiya Dakou — Mathematical Sustainable Engineering for Sustainable Resilience','White-canvas mathematical research identity with multilayer infrastructure, canonical interdependency object, viability geometry, synthetic nonlinear dynamics and state-space geometry.','MATHEMATICAL SUSTAINABLE ENGINEERING | SUSTAINABILITY · RESILIENCE · OPTIMIZATION | ẋ = f(x,u,η) | ρ(x)=d(x,∂V) | EVIDENCE → MODEL → COMPUTE → VERIFY → VALIDATE → DECIDE | synthetic illustrative data, not empirical evidence.')]
 b += [text(35,34,'Multilayer structure',19,weight='700'),layer_graph(35,44,445,205)]
 b += [rect(550,24,900,190,SOFT,HAIR,1.2,14),text(1000,54,'Canonical interdependency object',19,'middle','700'),text(1000,105,'I_ij^(αβ) = (E_i^α, E_j^β, M_ij, w_ij, δ_ij, τ_ij, a_ij, m, H_t)',24,'middle'),line(590,130,1410,130,HAIR,1),text(700,170,'ẋ = f(x,u,η)',18,'middle'),text(1000,170,'V ⊂ K',18,'middle'),text(1300,170,'ρ(x) = d(x, ∂V)',18,'middle'),text(700,195,'coupled dynamics',12,'middle',fill=MUTED),text(1000,195,'admissible viability',12,'middle',fill=MUTED),text(1300,195,'geometric margin',12,'middle',fill=MUTED)]
 b += [text(1690,35,'Viability geometry',19,weight='700'),viability(1640,48,365,165,True)]
 b += [line(400,266,650,266,HAIR,1),line(1398,266,1648,266,HAIR,1),text(1024,325,'Dossiya Dakou',72,'middle','700',family=SERIF),text(1024,363,'Mathematical Sustainable Engineering for Sustainable Resilience',25,'middle',style='italic',family=SERIF),text(1024,392,'POWER · TRANSPORTATION · INFORMATION · ORGANIZATION',15,'middle','700')]
 pot=M['potential']['data']; colors=[HAIR,MUTED,GOLD]; keys=['mu=-0.3','mu=+0.0','mu=+0.3']; b += [text(38,425,'Synthetic nonlinear dynamics',19,weight='700'),text(38,448,'V(x; μ)=¼x⁴ − ½x² − μx · illustrative, not empirical data',12,fill=MUTED,style='italic'),arrow(55,590,650,590,INK,1.2),arrow(75,602,75,438,INK,1.2)]
 for k,c in zip(keys,colors): b.append(path(map_xy(pot[k],85,462,545,110),c,1.8))
 mani=M['manifold_centerline']['data']; base=map_xy(mani,760,448,1190,92); b += [text(760,425,'State-space geometry',19,weight='700'),text(760,448,'synthetic manifold coordinate view · tangent + trajectory',12,fill=MUTED,style='italic')]
 for dy in range(-42,43,9): b.append(path([(x,y+dy) for x,y in base],GRID,.7))
 for i in range(0,len(base),12): x,y=base[i]; b.append(line(x,y-42,x,y+42,GRID,.6))
 p=base[len(base)//2]; b += [line(p[0]-170,p[1]+42,p[0]+170,p[1]-40,GOLD,2),circle(p[0],p[1],5),text(p[0]+13,p[1]-8,'p',14),text(p[0]-120,p[1]-52,'T_p M',15,fill=GOLD),path(base[len(base)//2:len(base)//2+65],INK,2),text(1870,485,'gamma(s)',14),text(825,580,'M',30,weight='700')]
 b += [chain(1024,624,['EVIDENCE','MODEL','COMPUTE','VERIFY','VALIDATE','DECIDE'],13),close()]; write('profile-header-v5.svg',''.join(b))

def research():
 W,H=1920,760; b=[header(W,H,'Research Operating System','Seven-stage mathematical sustainable-engineering architecture from multilayer structure through sustainable transformation pathways.','Conceptual architecture; not empirical validation. SYSTEMS × MATHEMATICS × DATA × HUMAN & PLANETARY WELL-BEING.'),text(960,48,'Research Operating System',44,'middle','700'),text(960,78,'Structure · mechanisms · dynamics · control · viability · transformation',18,'middle',style='italic',fill=MUTED),rect(70,105,1780,110,SOFT,HAIR,1.2,12),text(350,150,'I_ij^(αβ) = (E_i^α,E_j^β,M_ij,w_ij,δ_ij,τ_ij,a_ij,m,H_t)',18,'middle'),text(960,150,'dY/dt = F_G(Y,u,η;θ)',21,'middle'),text(1540,150,'rho_g(Y) = d_g(Y, boundary V_sus)',19,'middle'),text(350,188,'interdependency semantics',12,'middle',fill=MUTED),text(960,188,'coupled hybrid dynamics',12,'middle',fill=MUTED),text(1540,188,'geometric viability margin',12,'middle',fill=MUTED)]
 titles=[('1','Multilayer\nStructure'),('2','Causal\nMechanisms'),('3','Hybrid Multiscale\nDynamics'),('4','Feedback\n& Control'),('5','Viability'),('6','Resilience to\nSustainability'),('7','Transformation\nPathways')]; x0=38; cw=263
 for i,(num,ttl) in enumerate(titles):
  x=x0+i*cw; b += [text(x,265,num,28,weight='700',fill=GOLD)]; lines=ttl.split('\n'); b += [text(x+38,258+22*j,L,18,weight='700') for j,L in enumerate(lines)]
  if i<6: b.append(arrow(x+224,380,x+252,380,HAIR,1.2))
  if i==0: b.append(layer_graph(x+12,310,205,165,False))
  elif i==1:
   P=[(x+62,390),(x+130,340),(x+130,440),(x+198,390)]; b += [circle(a,c,16,'none',INK,1.2) for a,c in P]; b += [arrow(*P[0],*P[1],INK,1),arrow(*P[0],*P[2],INK,1),arrow(*P[1],*P[3],INK,1),arrow(*P[2],*P[3],INK,1)]
  elif i==2:
   for j,c in enumerate([INK,MUTED,HAIR]): b.append(path([(x+30+k*4,355+j*45+22*math.sin(.12*k+j)) for k in range(48)],c,1.5))
  elif i==3: b += [rect(x+62,350,112,70,'none',INK,1),text(x+118,390,'System G',13,'middle'),arrow(x+20,385,x+62,385),arrow(x+174,385,x+220,385),line(x+196,385,x+196,470,GOLD,1.2),line(x+196,470,x+40,470,GOLD,1.2),line(x+40,470,x+40,414,GOLD,1.2)]
  elif i==4: b.append(viability(x+22,330,205,170,False))
  elif i==5:
   seq=[(x+35+k*4,390+68*math.sin(.08*k)) for k in range(48)]; b += [path(seq,MUTED,1.5),circle(x+70,350,5),circle(x+190,435,5,GOLD),arrow(x+78,356,x+183,430,GOLD,1.2,'6 5')]
  else:
   seq=[(x+30+k*4,460-70*(k/48)**1.4-15*math.sin(.18*k)) for k in range(48)]; b += [path(seq,INK,1.7),circle(x+30,seq[0][1],4,GOLD),circle(x+110,seq[20][1],4,GOLD),circle(x+190,seq[40][1],4,GOLD)]
 formulas=['G=(V,E,W,L)','P(Y|do(X))','dY/dt = F_G(Y,u,η;θ)','u=π(Y)','V_sus ⊂ K','absorb · adapt · transform','robust desirable futures']
 for i,f in enumerate(formulas): b.append(text(x0+i*cw+112,535,f,13,'middle'))
 b += [chain(960,650,['EVIDENCE','DEFINITIONS','ASSUMPTIONS','MODEL','COMPUTATION','VERIFICATION','VALIDATION','DECISION'],12),arrow(1660,690,260,690,GOLD,1.2),text(960,716,'new evidence · learning · model refinement · adaptive decisions',12,'middle',style='italic',fill=MUTED),close()]; write('research-operating-system-v5.svg',''.join(b))

def geometry():
 W,H=1920,760; b=[header(W,H,'Differential Geometry Foundations','Five-panel mathematical plate linking manifold structure, metric, geodesics, curvature and viability geometry for resilient systems.','Mathematical foundations are separated from engineering interpretation and empirical validation.'),text(960,50,'Differential Geometry Foundations',44,'middle','700'),text(960,82,'Intrinsic geometry for state spaces, trajectories and viability',18,'middle',style='italic',fill=MUTED)]
 titles=['1. Manifold & tangent','2. Metric','3. Geodesics','4. Curvature','5. Viability geometry']; eqs=[('phi: U ⊂ M -> R^n','T_x M'),('g = g_ij du^i du^j','ds^2 = g_ij dx^i dx^j'),('nabla_gamma gamma = 0','d_g(p,q) = inf L(gamma)'),('R(X,Y)Z','K(p)'),('rho_g(x) = d_g(x,','boundary V_sus)')]; meanings=['local coordinates + admissible directions','intrinsic length + angle','shortest adaptation trajectories','how local geometry bends','distance to loss of viability']; cw=365; x0=40
 for i in range(5):
  x=x0+i*cw; b += [text(x,145,titles[i],19,weight='700'),line(x,165,x+320,165,HAIR,1)]
  base=[(x+20+k*5,350+28*math.sin(.08*k)) for k in range(55)]; b += [path([(a,c-70) for a,c in base],GRID,.8),path([(a,c+70) for a,c in base],GRID,.8)]
  if i==0: b += [f'<polygon points="{pts([(x+92,250),(x+240,230),(x+290,285),(x+135,307)])}" fill="{GOLD2}" stroke="{GOLD}"/>',circle(x+190,270,5),arrow(x+190,270,x+255,220,GOLD,1.4),arrow(x+190,270,x+170,190,INK,1.4)]
  elif i==1: b += [f'<ellipse cx="{x+185}" cy="280" rx="105" ry="70" fill="none" stroke="{INK}" stroke-width="1.5"/>',f'<ellipse cx="{x+185}" cy="280" rx="60" ry="38" fill="none" stroke="{GOLD}" stroke-width="1.4"/>',circle(x+185,280,5),line(x+185,280,x+275,245,INK,1.3),line(x+185,280,x+142,200,GOLD,1.3)]
  elif i==2:
   seq=[(x+60+k*5,330-72*math.sin(math.pi*k/45)) for k in range(46)]; b += [path(seq,INK,2.3),circle(*seq[0],5),circle(*seq[-1],5,GOLD),arrow(*seq[-8],*seq[-1],INK,1.3)]
  elif i==3: b += [f'<ellipse cx="{x+185}" cy="285" rx="100" ry="68" transform="rotate(12 {x+185} 285)" fill="none" stroke="{INK}" stroke-width="1.5"/>',f'<ellipse cx="{x+185}" cy="285" rx="62" ry="38" transform="rotate(12 {x+185} 285)" fill="none" stroke="{GOLD}" stroke-width="1.4"/>',arrow(x+185,285,x+260,235,INK,1.2),arrow(x+185,285,x+140,215,GOLD,1.2)]
  else: b.append(viability(x+70,215,240,190,False))
  b += [text(x+160,466,eqs[i][0],13,'middle'),text(x+160,490,eqs[i][1],13,'middle'),text(x+160,550,meanings[i],12,'middle',style='italic',fill=MUTED)]
 b += [text(960,650,'GEOMETRY CHAIN',12,'middle','700',fill=MUTED),chain(960,682,['MANIFOLD','TANGENT SPACE','METRIC','GEODESICS','CURVATURE','VIABILITY'],13),text(960,715,'Geometry is an engineering claim only after the state space, metric and validity domain are formally justified.',12,'middle',style='italic',fill=MUTED),close()]; write('differential-geometry-foundations-v5.svg',''.join(b))

if __name__=='__main__': hero(); research(); geometry(); render_research_state(); print('generated canonical and dynamic profile SVGs')
