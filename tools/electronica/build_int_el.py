import sys,os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
from aaaparse import cut,demak
from elparse import load as _l
load=lambda:_l()[0]
from openpyxl import Workbook
from openpyxl.styles import Font,PatternFill,Alignment,Border,Side
from elparse import classify
rows=load(); order={'GRÜN':0,'GELB':1,'ROT':2}
rows.sort(key=lambda r:(order[r['amp']],r['firma'].lower()))
wb=Workbook(); ws=wb.active; ws.title='electronica 2026'
hdr=['Nr','Firma','Stand','Ampel (vorläufig)','Sitz / Gebiet','Fertigung DE/AT/NL','Verguss (höchstes Bauteil)','Demak-Bereich','CRM-Status','Nachrecherche-Auftrag / Klärung','Nicht verwenden','Stichprobe Jey','Jey-Regel (22.10.)']
widths=[5,34,8,16,38,38,38,30,34,60,50,10,34]; F='Arial'
fills={'GRÜN':'A9D18E','GELB':'FFEB84','ROT':'F4A6A6'}; thin=Side(style='thin',color='BFBFBF'); bd=Border(top=thin,bottom=thin,left=thin,right=thin)
for c,h in enumerate(hdr,1):
    x=ws.cell(1,c,h); x.font=Font(name=F,bold=True,color='FFFFFF',size=10); x.fill=PatternFill('solid',fgColor='1F3864'); x.alignment=Alignment(wrap_text=True,vertical='center'); ws.column_dimensions[x.column_letter].width=widths[c-1]
ws.row_dimensions[1].height=32
for i,r in enumerate(rows,1):
    amp=r['amp']+((' ('+r['zus'].strip(' ()')+')') if r['zus'] else '')
    v=[i,r['firma'],r['stand'],amp,cut(r['sitz'] or r['gebiet'],260),cut(r['ferti'],330),cut(r['verg'],330),demak(r['seg']),cut(r['crm'],260),cut(r['nach'],520),cut(r['nicht'],420),r['stich'],classify(r)]
    for c,val in enumerate(v,1):
        x=ws.cell(i+1,c,val); x.font=Font(name=F,size=10); x.alignment=Alignment(wrap_text=True,vertical='top'); x.border=bd
    ws.cell(i+1,4).fill=PatternFill('solid',fgColor=fills[r['amp']]); ws.cell(i+1,4).font=Font(name=F,size=10,bold=True)
ws.freeze_panes='C2'; ws.auto_filter.ref=f'A1:M{len(rows)+1}'
h=wb.create_sheet('Hinweise'); h.column_dimensions['A'].width=150
for i,t in enumerate(["Interne Detailansicht (Tom/Tina v2). Für den Außendienst: aussendienst/electronica_2026_Aussendienst.xlsx.","Stand 2026-10-21, electronica 2026 München. 615 Zeilen aus 62 Batches (Export 03.07.2026, 708 Aussteller; 88 CRM-identische Firmen separat, nicht durch Tom/Tina geprüft). Alle Ampeln vorläufig (kein Browser, keine Patentdatenbank, nur Websuche-Treffer, Suchlimit der Sitzung teils früh erreicht).","GRÜN = Sitzregel + Produkttyp, Eigenfertigung/Eigenverguss nicht belegt. Patentrecherche (F5) offen. CRM-Konzernbezug und Identität vor Kontakt durch Jey klären."],1):
    x=h.cell(i,1,t); x.font=Font(name=F,size=10); x.alignment=Alignment(wrap_text=True)
wb.save('electronica/electronica_Aussteller_Ampel.xlsx'); print(len(rows))
