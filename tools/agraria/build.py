#!/usr/bin/env python3
"""agraria 2026 (Wels): Ausstellerliste über die Länder-Filter DE/AT/NL der Messeseite (api/exhibitors?country=...) laden,
mit dem CRM abgleichen und als Excel/CSV nach agraria-2026/ schreiben. Nur Standardbibliothek + openpyxl."""
import json,urllib.request,urllib.parse,os,sys,re,csv,difflib
ROOT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..')); sys.path.insert(0,ROOT)
import crm_abgleich as C
from openpyxl import Workbook
from openpyxl.styles import Font,PatternFill,Alignment,Border,Side
LAENDER=[('Deutschland','DE'),('Österreich','AT'),('Niederlande','NL')]
def get(params):
    r=urllib.request.urlopen('https://agraria.at/api/exhibitors?'+urllib.parse.urlencode(params),timeout=40)
    return json.load(r),int(r.headers.get('x-total-count',0))
rows=[]
for land,code in LAENDER:
    p=1;got=[]
    while True:
        d,t=get({'country':land,'limit':100,'page':p}); got+=d
        if len(got)>=t or not d: break
        p+=1
    print(land,t,len(got))
    for x in got:
        b=x.get('boothes') or [{}]
        m=b[0]
        rows.append(dict(land=code,firma=x['details']['name'],halle=m.get('hall',''),stand=m.get('booth',''),
            weitere='; '.join(f"{y.get('hall','')} {y.get('booth','')}" for y in b[1:]),mit='ja' if any(y.get('co_exhibitor') for y in b) else '',
            produkte='; '.join(x.get('products_services') or []),bereich=x.get('area','')))
crm=C.load()
def crm_status(name):
    nq=C.norm(name)
    best=None
    for f,i,raw,n in crm:
        if not n or not nq: continue
        sc=difflib.SequenceMatcher(None,nq,n).ratio(); first=n.split(' ')[0]
        if n==nq: k=0
        elif len(nq)>=5 and (n.startswith(nq) or (nq.startswith(n) and len(n)>=5)): k=1
        elif len(nq)>=5 and nq in ' '+n+' ': k=2
        elif len(first)>=5 and first==nq.split(' ')[0]: k=3
        elif sc>=0.88: k=4
        else: continue
        if best is None or k<best[0]: best=(k,raw.split('\t')[0])
    if not best: return 'kein CRM-Treffer'
    return {0:'Bestandskunde im CRM (gleicher Name)',1:'im CRM (sehr ähnlicher Name)',2:'im CRM (sehr ähnlicher Name)',3:'ähnlicher Name im CRM – prüfen',4:'ähnlicher Name im CRM – prüfen'}[best[0]]+f': {best[1][:50]}'
for r in rows: r['crm']=crm_status(r['firma'])
out=os.path.join(ROOT,'agraria-2026'); os.makedirs(out,exist_ok=True)
with open(out+'/agraria_2026_aussteller_DE-AT-NL.csv','w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f,delimiter=';'); w.writerow(['Land','Firma','Halle','Stand','Weitere Stände','Mitaussteller','Produkte/Services','CRM-Hinweis'])
    for r in rows: w.writerow([r['land'],r['firma'],r['halle'],r['stand'],r['weitere'],r['mit'],r['produkte'],r['crm']])
F='Arial';navy='1F3864';thin=Side(style='thin',color='BFBFBF');bd=Border(top=thin,bottom=thin,left=thin,right=thin)
wb=Workbook()
def sheet(ws,data,title):
    ws.sheet_view.showGridLines=False
    ws['A1']=title;ws['A1'].font=Font(name=F,size=14,bold=True,color=navy)
    ws['A2']='Quelle: agraria.at/aussteller (Länderfilter), Stand '+__import__('datetime').date.today().isoformat()+' · Messe Wels 25.–28.11.2026';ws['A2'].font=Font(name=F,size=9,italic=True,color='595959')
    hd=['Land','Firma','Halle','Stand','Produkte / Services','CRM-Hinweis','Notiz']; wd=[6,38,14,12,70,44,30]
    for c,(h,wi) in enumerate(zip(hd,wd),1):
        x=ws.cell(4,c,h);x.font=Font(name=F,bold=True,color='FFFFFF',size=10);x.fill=PatternFill('solid',fgColor=navy);x.border=bd;x.alignment=Alignment(wrap_text=True,vertical='center')
        ws.column_dimensions[x.column_letter].width=wi
    for i,r in enumerate(data,5):
        for c,v in enumerate([r['land'],r['firma'],r['halle'],r['stand'],r['produkte'],r['crm'],''],1):
            x=ws.cell(i,c,v);x.font=Font(name=F,size=10,bold=(c==2));x.alignment=Alignment(wrap_text=True,vertical='top');x.border=bd
            if i%2==0: x.fill=PatternFill('solid',fgColor='F2F5FA')
    ws.freeze_panes='C5';ws.auto_filter.ref=f'A4:G{4+len(data)}'
    ws.page_setup.orientation='landscape';ws.page_setup.fitToWidth=1;ws.page_setup.fitToHeight=0;ws.sheet_properties.pageSetUpPr.fitToPage=True;ws.print_title_rows='4:4'
ws=wb.active;ws.title='Alle DE-AT-NL';sheet(ws,rows,'agraria 2026 – Aussteller aus Deutschland, Österreich, Niederlande')
for land,code in LAENDER:
    sheet(wb.create_sheet(code),[r for r in rows if r['land']==code],f'agraria 2026 – Aussteller {land}')
wb.save(out+'/agraria_2026_Aussteller_DE-AT-NL.xlsx')
from collections import Counter
print(Counter(r['land'] for r in rows),Counter(r['crm'].split(':')[0] for r in rows))
