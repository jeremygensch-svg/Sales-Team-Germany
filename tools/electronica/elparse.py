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
D=ROOT+'/electronica/ergebnisse/'
def load():
    rows=[];warn=[]
    for n in range(1,63):
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
              seg=fld(2,t),crm=fld(12,t),was=fld(6,t),nach=nach,b=n,nr=i,sitz=fld(4,t),gebiet=fld(3,t),nicht=(lambda m:m.group(1).strip() if m else '')(re.search(r'(?m)^- \**Nicht verwendbare Aussagen[^:]*:\**\s*(.*)$',k)),ferti=fld(7,t),verg=fld(8,t)))
        
    return rows,warn
if __name__=='__main__':
    r,w=load(); from collections import Counter
    print(len(r),Counter(x['amp'] for x in r)); print(w[:40],len(w))

# Regeln von Jey (2026-10-22)
VERBAND=['catalonia trade','csa group','christlicher techniker','esz ag','forschungsvereinigung','global electronics association','intertek','leg thüringen','leistungszentrum terahertz','silicon saxony','smart systems hub','tüv süd','ul international','vde prüf','white horse','wirtschaftsförderung land','fraunhofer','testequity']
CRM_KEEP=['ai-energy','aumovio','bühler alzenau','das environmental','drees & sommer','et system','heiden power','hera laborsysteme','itk engineering','keenfinity','leonhard kurz','lutronic','mair elektronik','pailot','protec gmbh','sei interconnect','se spezial','sinto','stemas','tt electronics']
ANLAGEN=['aes motomation','aprotech','ap&s international','arias gmbh','asmpt','accretech','acculogic','bühler alzenau','camtek','diener electronic','disco hi-tec','e+h metrology','element 3-5','esmo ag','faeth','finetech','kelington','kitec','koh young','kokusai','kurt j. lesker','kurtz ersa','lab14','walter lemmen','mattson','mcd elektronik','m-o-t ','obducat','rena technologies','rorze','screen spe','sentech','singulus','suss microtec','ulvac','unitemp','veeco','viscom','vistec','werner lieb','intego','scia systems','ptw asia','puerstinger','atecare','atv systems','ramgraber','mk versuchsanlagen','fixtest','crs prüftechnik','cts gmbh clima','göpel electronic']
def classify(x):
    f=x['firma'].lower(); c=x['crm'].lower()
    if any(v in f for v in VERBAND): return 'Verband / Prüfdienstleister / Forschung'
    if (c.startswith('bekannt') or c.startswith('unklar')) and not any(k in f for k in CRM_KEEP): return 'Im CRM (gleicher oder sehr ähnlicher Name)'
    return ''

import glob
def load_browser():
    out={}
    for f in sorted(glob.glob(ROOT+'/electronica/ergebnisse_browser/gruen_*.md')+glob.glob(ROOT+'/electronica/ergebnisse_browser/rest_*.md')):
        t=open(f,encoding='utf-8').read()
        for m in re.finditer(r'(?ms)^## (\d+)\. (.*?)\n(.*?)(?=^## |\Z)',t):
            body=m.group(3); a=re.search(r'(?m)^- Ampel neu: (GRÜN|GELB|ROT)([^\n]*)',body)
            if not a: continue
            firma=re.sub(r'\s*\([^()]*\)\s*$','',m.group(2)).strip()
            z=re.search(r'Tabellenzeile D: (\d)',a.group(2))
            par=re.search(r'\(([^()]*(?:\([^()]*\))?[^()]*)\)',a.group(2).split('Tabellenzeile D')[0]+ (a.group(2).split('Tabellenzeile D')[1] if 'Tabellenzeile D' in a.group(2) else ''))
            au=re.search(r'(?mi)^- (?:OFFENER AUFTRAG|Offener Auftrag)[^:]*:\s*(.*)$',body)
            out[nk(firma)[:10]]=dict(amp=a.group(1),zeile=int(z.group(1)) if z else 7,begr=a.group(2).strip(),auftrag=au.group(1).strip() if au else '',firma=firma)
    return out
