import re
REG=['Baden-Württemberg','Bayern','Österreich','Rest Deutschland+Niederlande','außerhalb']
def blocks(t):
    p=re.split(r'(?m)^## (\d+)\. ',t); return {int(p[i]):p[i+1] for i in range(1,len(p),2)}
def fld(n,t):
    m=re.search(r'(?m)^%d\. [^:]*:\s*(.*)$'%n,t); return m.group(1).strip() if m else ''
def cut(s,n):
    s=re.sub(r'\s+',' ',s).strip(); return s if len(s)<=n else s[:n].rsplit(' ',1)[0].rstrip(',;:.')+' …'
def region_ort(g):
    reg=next((r for r in REG if g.startswith(r)),g.split('(')[0].strip())
    m=re.search(r'\(([^()]*(?:\([^()]*\))?[^()]*)\)',g[len(reg):] if g.startswith(reg) else g)
    ort=m.group(1) if m else ''
    ort=re.sub(r'^(Sitz|Hauptsitz)[: ]*','',ort).strip()
    return reg,cut(ort,60)
def load():
    rows=[]
    for n in range(1,14):
        tom=open(f'aaa_ergebnisse/tom_batch_{n:02d}.md').read(); tina=open(f'aaa_ergebnisse/tina_batch_{n:02d}.md').read()
        tb=blocks(tom); nb=blocks(tina)
        for l in tina.split('\n'):
            if not l.startswith('|'): continue
            c=[x.strip() for x in l.strip().strip('|').split('|')]
            if len(c)<5 or not re.fullmatch(r'\d+',c[0]): continue
            ai=next((j for j,x in enumerate(c) if re.match(r'(GRÜN|GELB|ROT)\b',x)),None)
            if ai is None: continue
            i=int(c[0]); fs=c[1]
            sm=re.match(r'(.*?)\s*\((?:Stand\s+)?([^()]*)\)\s*$',fs)
            firma,stand=(sm.group(1),sm.group(2)) if sm else (fs,'')
            amp=re.match(r'(GRÜN|GELB|ROT)',c[ai]).group(1); zus=c[ai][len(amp):].strip()
            zt=c[ai+1] if ai+1<len(c) else ''
            zm=re.match(r'\d',zt); zeile=int(zm.group()) if zm else 7
            stich=c[-1]
            t=tb.get(i,''); k=nb.get(i,'')
            mm=re.search(r'(?m)^- Nachrecherche[^:]*:\s*(.*)$',k); nach=mm.group(1).strip() if mm else ''
            mn=re.search(r'(?m)^- Nicht verwendbare Aussagen[^:]*:\s*(.*)$',k); nicht=mn.group(1).strip() if mn else ''
            reg,ort=region_ort(fld(3,t))
            rows.append(dict(amp=amp,zus=zus,zeile=zeile,stich=stich,firma=firma.replace('*','').strip(),stand=stand,reg=reg,ort=ort,gebiet=fld(3,t),
                sitz=fld(4,t),ferti=fld(7,t),verg=fld(8,t),seg=fld(2,t),crm=fld(12,t),was=fld(6,t),nach=nach,nicht=nicht,b=n,nr=i))
    return rows
if __name__=='__main__':
    r=load(); print(len(r))
    from collections import Counter; print(Counter(x['amp'] for x in r)); print(sum(1 for x in r if not x['stand']))
    for x in r:
        if x['b'] in (6,13) and x['nr']<3 or x['firma'].startswith('Kaiser'): print(x['firma'],'|',x['stand'],'|',x['reg'],'|',x['ort'],'|',x['zeile'])

def _strip_par(t):
    prev=None
    while prev!=t:
        prev=t; t=re.sub(r'\([^()]*\)','',t)
    return t
def demak(seg):
    s=re.sub(r'\s+',' ',seg)
    parts=re.split(r'(?i)\bnachrangig\b|\bsekundär\b|;',s,maxsplit=1)
    prim=_strip_par(parts[0]); sec=_strip_par(parts[1]) if len(parts)>1 else ''
    def terms(t):
        out=[]
        if re.search(r'(?i)electrical insulation|e-mobility|potting|led encapsulation',t): out.append('Verguss')
        if re.search(r'(?i)optical bonding|klebung',t): out.append('Verklebung')
        if re.search(r'(?i)fipfg|gasketing|sealing|dichtung',t): out.append('Dichtung')
        return out
    if re.match(r'(?i)\s*(kein|nicht|unbekannt)',prim): return 'kein klarer Bereich'
    p=terms(prim)
    if not p: return 'kein klarer Bereich'
    extra=[x for x in terms(sec[:90]) if x not in p]
    return ' + '.join(p+extra)
