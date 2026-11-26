import re,sys
import os
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
sys.path.insert(0,os.path.dirname(__file__))
from aaaparse import fld,cut,region_ort,demak
def nk(x): return re.sub(r'[^a-z0-9]','',x.lower())
def blocks(t):
    out=[]
    for m in re.finditer(r'(?ms)^## (\d+(?:/\d+)?)\.? (.*?)\n(.*?)(?=^## |\Z)',t): out.append((nk(m.group(2)),m.group(3)))
    return out
def find(bl,firma):
    k=nk(firma)[:9]
    for h,b in bl:
        if k and k in h: return b
    return ''
D=ROOT+'/agraria-2026/ergebnisse/'
BADHOST=('agriculture-xprt','agriexpo','agritechnica','galabau','landwirt.com','herold','wko.at','firmenabc','compass','topagrar','mascus','traktorpool','tractorhouse','machineryzone','agrarheute','ktm','firmenbuch','evi.gv','agroscope','goodip','ipqwery','justia','patents.google','espacenet','semi.org','bayern-international','electronica','northdata','wikipedia','linkedin','provenexpert','handelsregister','opencorporates','kompass','europages','dnb.com','firmenwissen','wlw.de','xing','openregister','metoree','german-pavilion','medtec','facebook','google','techpilot','indeed','stepstone')
def _web(w):
    for m in re.finditer(r'https?://[^\s)\],;"]+|(?<![\w@.])www\.[\w.-]+\.[a-z]{2,}[^\s)\],;"]*',w or ''):
        u=m.group(0).rstrip('.')
        h=re.sub(r'^https?://','',u).split('/')[0].lower()
        if not any(b in h for b in BADHOST): return re.sub(r'^https?://','',h)
    return ''
def load():
    rows=[];warn=[]
    for n in range(1,34):
        tom=open(f'{D}tom_batch_{n:02d}.md').read(); tina=open(f'{D}tina_batch_{n:02d}.md').read()
        tb=blocks(tom); nb=blocks(tina)
        seen=set()
        for l in tina.split('\n'):
            if not l.startswith('|'): continue
            c=[x.strip() for x in l.strip().strip('|').split('|')]
            if len(c)<5 or not re.fullmatch(r'\d+(/\d+)?',c[0]): continue
            ai=next((j for j,x in enumerate(c) if re.match(r'\**(GRÜN|GELB|ROT)\b',x,re.I)),None)
            if ai is None: continue
            i=c[0]; fs=c[1]
            if i in seen: continue
            seen.add(i)
            sm=re.match(r'(.*?)\s*\((?:Stand\s+)?([^()]*)\)\s*$',fs)
            firma,stand=(sm.group(1),sm.group(2)) if sm else (fs,'')
            a=c[ai].replace('*','')
            amp=re.match(r'(GRÜN|GELB|ROT)',a,re.I).group(1).upper(); zus=a[len(amp):].strip()
            zt=c[ai+1] if ai+1<len(c) else ''
            zm=re.match(r'\d',zt); zeile=int(zm.group()) if zm else 7
            t=find(tb,firma); k=find(nb,firma)
            if not t: warn.append((n,i,'kein Tom-Block'))
            mm=re.search(r'(?m)^- \**Nachrecherche[^:]*:\**\s*(.*)$',k); nach=mm.group(1).strip() if mm else ''
            if not nach and amp=='GELB': warn.append((n,i,'kein Nachrecherche'))
            reg,ort=region_ort(fld(3,t))
            rows.append(dict(amp=amp,zus=zus+' '+zt,zeile=zeile,stich=c[-1],firma=firma.replace('*','').strip(),stand=stand,reg=reg,ort=ort,
              seg=fld(2,t),crm=fld(12,t),was=fld(6,t),nach=nach,b=n,nr=i,web=_web(fld(5,t)),sitz=fld(4,t),gebiet=fld(3,t),nicht=(lambda m:m.group(1).strip() if m else '')(re.search(r'(?m)^- \**Nicht verwendbare Aussagen[^:]*:\**\s*(.*)$',k)),ferti=fld(7,t),verg=fld(8,t)))
        
    return rows,warn
if __name__=='__main__':
    r,w=load(); from collections import Counter
    print(len(r),Counter(x['amp'] for x in r)); print(w[:40],len(w))

# Regeln von Jey (2026-10-22)
VERBAND=[]
CRM_KEEP=[]
ANLAGEN=[]
def classify(x):
    f=x['firma'].lower(); c=x['crm'].lower()
    if any(v in f for v in VERBAND): return 'Verband / Prüfdienstleister / Forschung'
    if (c.startswith('bekannt') or c.startswith('unklar')) and not any(k in f for k in CRM_KEEP): return 'Im CRM (gleicher oder sehr ähnlicher Name)'
    return ''

import glob
def load_browser():
    out={}
    for f in sorted([]):
        t=open(f,encoding='utf-8').read()
        for m in re.finditer(r'(?ms)^## (\d+)\. (.*?)\n(.*?)(?=^## |\Z)',t):
            body=m.group(3); a=re.search(r'(?m)^- Ampel neu: (GRÜN|GELB|ROT)([^\n]*)',body)
            if not a: continue
            firma=re.sub(r'\s*\([^()]*\)\s*$','',m.group(2)).strip()
            z=re.search(r'Tabellenzeile D: (\d)',a.group(2))
            par=re.search(r'\(([^()]*(?:\([^()]*\))?[^()]*)\)',a.group(2).split('Tabellenzeile D')[0]+ (a.group(2).split('Tabellenzeile D')[1] if 'Tabellenzeile D' in a.group(2) else ''))
            au=re.search(r'(?mi)^- (?:OFFENER AUFTRAG|Offener Auftrag)[^:]*:\s*(.*)$',body)
            idl=re.search(r'(?m)^- Identität[^\n]*?(https?://[^\s)"]+)',body); web=_web(idl.group(1)) if idl else ''
            out[nk(firma)[:10]]=dict(web=web,amp=a.group(1),zeile=int(z.group(1)) if z else 7,begr=a.group(2).strip(),auftrag=au.group(1).strip() if au else '',firma=firma)
    return out
