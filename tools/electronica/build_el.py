import re
from openpyxl import Workbook
from openpyxl.styles import Font,PatternFill,Alignment,Border,Side
from openpyxl.worksheet.table import Table
import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
from aaaparse import cut,demak
from elparse import load as _l
import json
from elparse import load_browser,nk as _nkk
_B=load_browser()
def load():
    out=[]
    for d in _l()[0]:
        b=_B.get(_nkk(d['firma'])[:10])
        if b:
            d['amp']=b['amp']; d['zeile']=b['zeile']; d['zus']=''; d['browser']=b
            if b.get('web'): d['web']=b['web']
        out.append(d)
    return out
def first_sentence(s,n):
    s=re.sub(r'\(Stufe [^)]*\)|\((?:V|A|S|\?)(?:,[^)]*)?\)','',s); s=re.sub(r'\s+',' ',s).strip()
    m=re.match(r'(.+?[.;])\s',s+' '); s=m.group(1) if m else s
    return cut(s,n)
rows=[]
from elparse import classify,ANLAGEN
for d in load():
    zus=d['zus']; z=d['zeile']; amp=d['amp']
    prio='A' if amp=='GRÜN' else ('–' if amp=='ROT' else ('C' if ('Rot-Kandidat' in zus or z in (2,3)) else 'B'))
    nach=re.sub(r'^\(?\d\)?\s*','',d['nach'])
    nach=re.split(r'\s*(?:Wo nachsehen|Aktion):',nach)[0].strip()
    nach=re.sub(r'^\(a\)\s*','',nach)
    c0=d['crm'].lower()
    crmk='Bestandskunde im CRM' if c0.startswith('bekannt') else ('Konzern-/ähnlicher Name im CRM – vor Kontakt intern klären' if c0.startswith('unklar') else 'kein CRM-Treffer')
    ort=re.sub(r'^(GmbH|Zentrale|Werk)\s+in\s+','',d['ort']); ort=re.sub(r'\s+laut Recherche$','',ort)
    reg=d['reg'].replace('Rest Deutschland+Niederlande','Rest DE / NL')
    b=d.get('browser'); pruef='vorläufig (nur Websuche, Sitz/Produkttyp)'
    if b:
        bg=re.sub(r'Tabellenzeile D: \d\.?','',b['begr']).strip(' .')
        pruef='Browser geprüft 22.10.: '+('Grün bestätigt' if b['amp']=='GRÜN' and 'schwach' not in b['begr'] else ('Grün (schwach)' if b['amp']=='GRÜN' else 'Gelb – offen'))
        nach=b['auftrag'] if b['amp']=='GELB' else ''
        if b['amp']=='GRÜN': nach='Im Gespräch erfragen: Verguss/Klebung/Dichtung am Produkt'
    rows.append(dict(web=d.get('web',''),amp=amp,prio=prio,firma=d['firma'],stand=d['stand'],reg=reg,ort=ort,
        was=re.sub(r'\s*\((?:Triage|Verzeichnis)[^)]*\)','',re.sub(r'^(Verzeichnis nennt|Laut Verzeichnis:?)\s*','',first_sentence(d['was'],170))),bereich=demak(d['seg']),
        klaeren=cut(nach,230) if nach else ('Fertigung vor Ort und Verguss im Gespräch erfragen (nur Sitz und Produkttyp belegt)' if amp=='GRÜN' else ''),
        crm=crmk,raus=classify(d),pruef=pruef,seg=d['seg']))

import glob
def _nk(x): return re.sub(r'[^a-z0-9]','',x.lower())
_plz={}
for f in glob.glob('electronica/batches_v2/pruef_*.md'):
    for l in open(f,encoding='utf-8'):
        m=re.match(r'- \d+ \| (.*?) \| .*? \| (\d{5}) ([^|]*) \|',l)
        if m: _plz[_nk(m.group(1))[:10]]=(m.group(2),m.group(3).strip())
_P2={}
def _a(land,*pre):
    for p in pre: _P2[p]=land
_a('Sachsen','01','02','04','08','09'); _a('Brandenburg','03','14','15','16'); _a('Sachsen-Anhalt','06','39'); _a('Thüringen','07','98','99'); _a('Berlin','10','12','13')
_a('Mecklenburg-Vorpommern','17','18','19'); _a('Hamburg','20','21','22'); _a('Schleswig-Holstein','23','24','25'); _a('Niedersachsen','26','27','29','30','31','37','38','49'); _a('Bremen','28')
_a('Nordrhein-Westfalen','32','33','40','41','42','44','45','46','47','48','50','51','52','53','57','58','59'); _a('Hessen','34','35','36','60','61','63','64','65'); _a('Rheinland-Pfalz','54','55','56','67'); _a('Saarland','66')
_a('Baden-Württemberg','68','69','70','71','72','73','74','75','76','77','78','79'); _a('Bayern','80','81','82','83','84','85','86','87','90','91','92','93','94','95','96','97'); _a('Baden-Württemberg/Bayern (prüfen)','88','89')
def _land(r,plz):
    if r['reg'] in ('Baden-Württemberg','Bayern'): return r['reg']
    if plz: 
        l=_P2.get(plz[:2],'')
        if l and not l.startswith('Baden') and l!='Bayern': return l
        if l: return l
    return {'Rest DE / NL':'Rest DE / NL','außerhalb':'Ausland / außerhalb'}.get(r['reg'],r['reg'])
for r in rows:
    k=_nk(r['firma'])[:10]; plz,ort2=_plz.get(k,('',''))
    if plz and not r['ort'] : r['ort']=ort2
    if plz and r['ort'] and not r['ort'].startswith(plz): r['ort']=plz+' '+r['ort']
import re as _re
def _stand(x):
    x=x or ''
    m=_re.search(r'Halle\s+([A-C]\d),\s*Stand\s+(\d+)',x)
    if m: return m.group(1)+'.'+m.group(2)
    m=_re.search(r'[A-C]\d\.[\dA-Z/]+',x)
    return m.group(0) if m else x
for r in rows:
    r.setdefault('pruef','Bestandskunde laut CRM-Namensabgleich'); r.setdefault('web','')
    b_=r.get('bereich','')
    q=[]
    if 'Verguss' in b_: q.append('Werden Elektronik-Baugruppen/Sensoren bei Ihnen vergossen (Vergussmasse, Dosieranlage)?')
    if 'Verklebung' in b_: q.append('Wie werden Displays/Touch/Sensoren verklebt (Optical Bonding)?')
    if 'Dichtung' in b_ and not q: q.append('Wie werden Gehäuse abgedichtet (Schaumdichtung, Dichtraupe)?')
    r['frage']=' '.join(q) if q else 'Gibt es Eigenfertigung am Standort, bei der Teile vergossen, verklebt oder abgedichtet werden?'
    if r.get('raus'): r['klaeren']=r['raus']; r['prio']='–'
    r['stand']=_stand(r['stand']); r['reg']=r['reg'].replace('Sitz Rest DE / NL','Rest DE / NL')
    if r['prio'] in 'BC' and r['bereich']=='kein klarer Bereich' and not any(a in r['firma'].lower() for a in ANLAGEN): r['prio']='D'
order={'A':0,'B':1,'C':2,'D':3,'–':4}
def _clean(t):
    t=t or ''
    for a,b in [(r'(?:An )?Jey(?:/Tina|/CRM|/Vertrieb)?:','Intern klären:'),(r'Jey bestätigt','intern bestätigen'),(r'Jey/Vertrieb','dem Vertrieb'),(r'Jeys Entscheidung','interner Entscheidung'),(r'Jey/Excel','Excel'),(r'\s*\((?:Stufe )?V(?: für [^)]*)?\)',''),(r'\(Regel M\)','(Konzern?)'),(r'in Stufe V',' belegt'),(r'\(Stufe V\)','(belegt)'),(r'Stufe V','Beleg'),(r'\s+\.',' .'),(r'\s+\.$','.'),(r'\s{2,}',' ')]:
        t=re.sub(a,b,t)
    return t.strip()
for r in rows:
    r['was']=_clean(r['was']); r['klaeren']=_clean(r['klaeren'])
    r['reg']={'Baden-Württemberg':'Baden-Württemberg (Stefan)','Bayern':'Bayern (Dietmar)','Rest DE / NL':'Rest DE / NL (Manuel)'}.get(r['reg'],r['reg'])
rows.sort(key=lambda r:(order[r['prio']],r['firma'].lower()))
F='Arial'
navy='1F3864'; thin=Side(style='thin',color='BFBFBF'); bd=Border(top=thin,bottom=thin,left=thin,right=thin)
fills={'A':'A9D18E','B':'FFEB84','C':'F8CBAD','D':'E7E6E6','–':'D9D9D9'}
wb=Workbook()
def sheet(ws,data,cols,widths,title):
    ws.sheet_view.showGridLines=False
    ws['A1']=title; ws['A1'].font=Font(name=F,size=14,bold=True,color=navy)
    ws['A2']='Messe electronica 2026 München · Stand 21.10.2026 · Ergebnisse vorläufig (siehe Blatt "Hinweise")'; ws['A2'].font=Font(name=F,size=9,italic=True,color='595959')
    hr=4
    for c,(h,_) in enumerate(cols,1):
        x=ws.cell(hr,c,h); x.font=Font(name=F,bold=True,color='FFFFFF',size=10); x.fill=PatternFill('solid',fgColor=navy); x.alignment=Alignment(wrap_text=True,vertical='center',horizontal='center' if h in('Prio','Stand') else 'left'); x.border=bd
        ws.column_dimensions[x.column_letter].width=widths[c-1]
    ws.row_dimensions[hr].height=28
    for r,d in enumerate(data,hr+1):
        for c,(h,key) in enumerate(cols,1):
            v=d[key] if key else ''
            x=ws.cell(r,c,v); x.font=Font(name=F,size=10,bold=(key=='firma' or key=='prio'),color='0563C1' if (key=='web' and v) else '000000',underline='single' if (key=='web' and v) else None)
            if key=='web' and v: x.hyperlink='https://'+v
            x.alignment=Alignment(wrap_text=True,vertical='top',horizontal='center' if h in('Prio','Stand') else 'left'); x.border=bd
            if key=='prio': x.fill=PatternFill('solid',fgColor=fills[d['prio']])
        # leichte Zebra-Streifen
        if (r-hr)%2==0:
            for c,(h,key) in enumerate(cols,1):
                if key!='prio': ws.cell(r,c).fill=PatternFill('solid',fgColor='F2F5FA')
    ws.freeze_panes=ws.cell(hr+1,3)
    ws.auto_filter.ref=f'A{hr}:{ws.cell(hr+len(data),len(cols)).coordinate}'
    ws.page_setup.orientation='landscape'; ws.page_setup.fitToWidth=1; ws.page_setup.fitToHeight=0
    ws.sheet_properties.pageSetUpPr.fitToPage=True; ws.print_title_rows=f'{hr}:{hr}'
    ws.page_margins.left=ws.page_margins.right=0.4
for k in json.load(open('electronica/crm_bekannt.json'))['known']:
    rows.append(dict(amp='ROT',prio='–',pruef='Bestandskunde laut CRM-Namensabgleich',web='',frage='',firma=k['name'],stand=k['stand'],reg='',ort=(k['plz']+' '+k['ort']).strip(),was=k.get('hint',''),bereich='',klaeren='Bestandskunde laut CRM-Namensabgleich – nicht ansprechen, Zuständigen im Haus fragen',crm='Bestandskunde im CRM'))
rows.sort(key=lambda r:(order[r['prio']],r['firma'].lower()))
act=[r for r in rows if r['prio'] in 'ABC']; eher=[r for r in rows if r['prio']=='D']; rot=[r for r in rows if r['prio']=='–']
cols=[('Prio','prio'),('Firma','firma'),('Stand','stand'),('Vertriebsgebiet','reg'),('Ort','ort'),('Website','web'),('Was wird gebaut','was'),('Demak-Bereich','bereich'),('Prüfstand','pruef'),('Gesprächsfrage','frage'),('Vor dem Kontakt klären','klaeren'),('CRM-Hinweis','crm'),('Besuch / Kontakt am',None),('Ergebnis / Notiz',None)]
w=[6,30,8,18,18,24,42,22,28,40,52,30,14,30]
ws=wb.active; ws.title='Zielfirmen'; sheet(ws,act,cols,w,'Außendienst – Zielfirmen electronica 2026 München')
ws3=wb.create_sheet('Eher nicht (kein Bereich)'); sheet(ws3,eher,cols[:11],w[:11],'Eher nicht ansprechen – kein Demak-Bereich erkennbar')
for r in rows:
    r['reg']={'Baden-Württemberg':'Baden-Württemberg (Stefan)','Bayern':'Bayern (Dietmar)','Rest DE / NL':'Rest DE / NL (Manuel)'}.get(r['reg'],r['reg'])
lands={}
for r in act: lands.setdefault(r['reg'] or 'unbekannt',[]).append(r)
pri=['Baden-Württemberg (Stefan)','Bayern (Dietmar)','Rest DE / NL (Manuel)','Österreich']
for land in pri+sorted(l for l in lands if l not in pri):
    if land not in lands: continue
    w_=wb.create_sheet(land[:31].replace('/','-')); sheet(w_,lands[land],cols,w,'Zielfirmen electronica 2026 – '+land)
ws2=wb.create_sheet('Nicht ansprechen'); sheet(ws2,rot,cols[:11],w[:11],'Nicht ansprechen / bereits Bestandskunde')
h=wb.create_sheet('Hinweise'); h.sheet_view.showGridLines=False; h.column_dimensions['A'].width=22; h.column_dimensions['B'].width=120
h['A1']='Hinweise zur Liste'; h['A1'].font=Font(name=F,size=14,bold=True,color=navy)
items=[('Prioritäten',''),
('A (grün)','Sitz in DE/AT/NL als erkennbarer Hersteller, Produkt enthält typisch Vergossenes/Verklebtes. Zuerst ansprechen.'),
('B (gelb)','Grundsätzlich passend, ein Punkt vor dem Kontakt klären (Spalte "Vor dem Kontakt klären").'),
('C (orange)','Zuerst Identität oder CRM-Bezug klären (z. B. Konzern im CRM, Sitz unklar). Nicht ohne interne Rückmeldung kontaktieren.'),
('Demak-Bereich','Verguss = Electrical Insulation / E-Mobility Potting / LED Encapsulation (Vergussmasse, Dosier- und Vergussanlagen). Verklebung = Optical Bonding (Displays/Touch). Dichtung = FIPFG/Gasketing (Schaumdichtung). Mehrere Begriffe: in dieser Reihenfolge nach Bedeutung. Filter: Spalte "Demak-Bereich" nach "Verguss" filtern.'),
('D (grau)','Blatt "Eher nicht": Händler, Dienstleister, Verbände, Software u. ä. ohne erkennbaren Demak-Bereich. Nur ansprechen, wenn sich im Gespräch eigene Fertigung zeigt.'),
('Nicht ansprechen','Alles, was nicht angesprochen wird: (1) Firmen im CRM mit gleichem oder sehr ähnlichem Namen (88 Namensabgleich-Treffer plus Treffer aus der Recherche inkl. Konzernname), (2) Verbände, Prüfdienstleister, Forschungsorganisationen, (3) Anlagenbauer ohne Verguss-/Demak-Anlage. Grund steht in Spalte "Vor dem Kontakt klären".'),
('',''),
('Belastbarkeit',''),
('Prüfstand','Spalte "Prüfstand": Die 46 aussichtsreichsten Firmen (frühere Grün-Liste) wurden am 22.10.2026 im Browser nachgeprüft (Impressum/Handelsregister, Fertigung am Sitz, Patente in Google Patents und Espacenet, Wettbewerber-Referenzen, CRM). "Grün bestätigt" = Sitz und Fertigung belegt. Bei allen anderen Firmen beruht die Einstufung nur auf Websuche-Treffern (vorläufig); dort sind Fertigung und Verguss aus Sitz und Produkttyp abgeleitet.'),
('Für Gespräche','Verguss/Verklebung nur als Frage formulieren ("in Sensoren stecken typischerweise vergossene Bauteile"), nicht als Tatsache über die Firma.'),
('Patente','Patente nur bei den 46 Browser-geprüften Firmen (Google Patents, Espacenet) gesucht. Eigenfertigung und Wettbewerbereinsatz im Gespräch erfragen.'),
('Vertriebsgebiete','Pro Vertriebsgebiet ein Blatt (Baden-Württemberg, Bayern, Rest DE / NL, ggf. Österreich/außerhalb; nur Prio A/B/C). Gebiet nach Fertigungs- bzw. Firmensitz laut Recherche. Zuständig: Stefan = Baden-Württemberg, Dietmar = Bayern, Manuel = Rest DE / NL. Das Blatt "Zielfirmen" enthält alle zusammen.'),
('Messe','Stand = Halle.Stand laut Ausstellerliste (Export 03.07.2026).')]
for i,(a,b) in enumerate(items,3):
    h.cell(i,1,a).font=Font(name=F,size=10,bold=True,color=navy if b=='' else '000000'); x=h.cell(i,2,b); x.font=Font(name=F,size=10); x.alignment=Alignment(wrap_text=True,vertical='top')
    h.cell(i,1).alignment=Alignment(vertical='top')
    if a=='D (grau)': h.cell(i,1).fill=PatternFill('solid',fgColor=fills['D'])
    if a=='A (grün)': h.cell(i,1).fill=PatternFill('solid',fgColor=fills['A'])
    if a=='B (gelb)': h.cell(i,1).fill=PatternFill('solid',fgColor=fills['B'])
    if a=='C (orange)': h.cell(i,1).fill=PatternFill('solid',fgColor=fills['C'])
ov=wb.create_sheet('Übersicht',0); ov.sheet_view.showGridLines=False
ov['A1']='electronica 2026 München – Übersicht Außendienst'; ov['A1'].font=Font(name=F,size=14,bold=True,color=navy)
ov['A2']='Stand 23.10.2026 · Ergebnisse siehe Blatt "Hinweise"'; ov['A2'].font=Font(name=F,size=9,italic=True,color='595959')
gebs=['Baden-Württemberg (Stefan)','Bayern (Dietmar)','Rest DE / NL (Manuel)','Österreich','außerhalb']
hd=['Vertriebsgebiet','Prio A','Prio B','Prio C','Zielfirmen gesamt','davon im Browser geprüft']
for c,h in enumerate(hd,1):
    x=ov.cell(4,c,h); x.font=Font(name=F,bold=True,color='FFFFFF',size=10); x.fill=PatternFill('solid',fgColor=navy); x.border=bd; x.alignment=Alignment(horizontal='center' if c>1 else 'left',wrap_text=True)
    ov.column_dimensions[x.column_letter].width=30 if c==1 else 16
for i,g in enumerate(gebs,5):
    ov.cell(i,1,g)
    for j,pr in enumerate('ABC',2): ov.cell(i,j,sum(1 for r in act if r['reg']==g and r['prio']==pr))
    ov.cell(i,5,sum(1 for r in act if r['reg']==g)); ov.cell(i,6,sum(1 for r in act if r['reg']==g and r['pruef'].startswith('Browser')))
n=len(gebs)+5
ov.cell(n,1,'Gesamt')
for j in range(2,7): ov.cell(n,j,sum(ov.cell(i,j).value for i in range(5,n)))
for i in range(5,n+1):
    for j in range(1,7):
        x=ov.cell(i,j); x.font=Font(name=F,size=10,bold=(i==n)); x.border=bd; x.alignment=Alignment(horizontal='center' if j>1 else 'left')
ov.page_setup.orientation='landscape'; ov.page_setup.fitToWidth=1; ov.page_setup.fitToHeight=0; ov.sheet_properties.pageSetUpPr.fitToPage=True
ov.cell(n+2,1,'Weitere Blätter').font=Font(name=F,bold=True,size=10,color=navy)
for k,t in enumerate([f'Eher nicht (kein Bereich): {len(eher)} Firmen ohne erkennbaren Demak-Bereich',f'Nicht ansprechen: {len(rot)} Firmen (Bestandskunden/CRM, Verbände, Prüfdienstleister, Forschung)','Hinweise: Prioritäten, Prüfstand, Gesprächsführung'],n+3):
    ov.cell(k,1,t).font=Font(name=F,size=10)
wb._sheets=[x for x in wb._sheets if x.title not in ('Eher nicht (kein Bereich)','Nicht ansprechen','Hinweise')]+[wb['Eher nicht (kein Bereich)'],wb['Nicht ansprechen'],wb['Hinweise']]
wb._sheets=[wb['Übersicht']]+[x for x in wb._sheets if x.title!='Übersicht']
wb.active=0
wb.save('aussendienst/electronica_2026_Aussendienst.xlsx')
from collections import Counter
print(Counter(r['prio'] for r in rows))
