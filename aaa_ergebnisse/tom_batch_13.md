# Tom Batch 13 – all about automation Düsseldorf 2026 (aaa, Stand der Liste 29.07.2026)
Erstellt: 2026-10-15 (Tom, Stufe 1, Version 2, getrennter Agent, keine Ampel). Eingabe: aaa_batches_v2/pruef_12.md, 7 Firmen. Halle ist in der Liste nicht angegeben, Feld 1 trägt nur die Standnummer.
Alle Abrufdaten: 2026-10-15. Belegstufen: V = selbst gelesene Quelle (in diesem Lauf nirgends erreicht, siehe Einschränkungen), S = nur Suchsnippet/Suchzusammenfassung (Seite nachlesen), A = aus Produkttyp abgeleitet (Triage und Produkttyp-Ableitung = Stufe A), ? = angenommen.
Umgebung: WebFetch und Chrome nicht genutzt/nicht verfügbar, nur WebSearch (29 Abfragen). Es gibt in diesem Batch KEINE Stufe-V-Aussage. Patent-Suchen liefen nur als Websuche-Abfragen auf Patentseiten, nicht als Direktabfrage in Google Patents, Espacenet oder DEPATISnet (siehe Einschränkungen).
Messe-Signal (Regel N2): Grep auf aaa_duesseldorf_2026.csv nach Scheugenpflug, DOPAG, Nordson, ViscoTec, RAMPF, bdtronic, Sonderhoff, Hilger, Musashi, Henkel, DELO, Elantas, Wacker, Sika, GONANO, Marco, EPOXONIC, WEVO, Panacol, Lohmann, OTTO-CHEMIE, Hexion: kein Treffer (2026-10-15). Kein Wettbewerber derselben Messe.
CRM-Abgleich: crm_abgleich.py mit Firmen-, Konzern- und Altnamen je Firma ausgeführt (2026-10-15), zusätzlich Grep auf Katt/Württembergische/Yaskawa/Motoman/Gessmann/Wachendorff in beiden CRM-Dateien.
Tabelle BEKANNT: 0 Firmen BEKANNT, 2 unklar/CRM-Bezug (Wagner GmbH, WEG Germany GmbH), 5 neu.

## 1. W. Gessmann GmbH
1. Firma: W. Gessmann GmbH (Messe: all about automation Düsseldorf 2026, Stand 806, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Joystick-Sensorik, Steuerelektronik), nachrangig Gasketing (IP67-Griffe)
3. Gebiet: Baden-Württemberg (Leingarten)
4. Sitz und Fertigungsort: Eppingerstr. 221, 74211 Leingarten (S, Katalog/Verzeichnis); laut Triage Entwicklung, Teilmontage, CNC, THT/SMD im Werk Leingarten (S, plantautomation-technology.com, nicht erneut gelesen). Tochter Gessmann China Ltd. (Shanghai) laut Triage: Fertigungsrolle der Tochter nicht geprüft.
5. Website: https://www.gessmann.com
6. Was wird gebaut: Joysticks (Griffe B20/B24/B26/B32/B33/B34 mit Schutzart bis IP67, Betriebstemperatur -40 bis +85 Grad, S, directindustry.com), kontaktlose Hall-Sensorik (S, directindustry/eurosensor), Mehrachs-Mastercontroller V-Serie, Pedale, Kranfernsteuerungen, Bedienpulte, Lichtsignaleinrichtung für fahrerlose Transportsysteme (Patentliste, S). Typisch vergossen/verklebt/gedichtet: Hall-Sensorik und Elektronik in IP67-Griffen (A, Block A Sensoren/Block B Bedienelemente IP65-IP69K), Mehrachs-Controller-Elektronik (A, Block B), Gehäusedichtungen der Griffe (A, Block B FIPFG/Dichtung). Welches Teil in Leingarten vergossen wird, ist NICHT belegt.
7. Fertigung DE/AT/NL: Hoch, Stufe A (Sitzregel: Industriegerätebauer mit eigenen Produkten und erkennbarem Standort; Katalogaussage "complete in-house production" als Stütze, S; Tochter China als Auslagerungsrisiko nicht geprüft). Keine V-Quelle.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Produkttyp: Joystick mit Hall-Sensorik und Schutzart IP67, Block A Sensoren). Einzelbewertung: Hall-Sensorik/Elektronik im Griff Hoch (A), Mehrachs-Controller-Elektronik Mittel (A), IP67-Gehäuse/Griffdichtung Mittel (A), Mechanik/Gestänge Niedrig (A). Kein Gegenbeleg.
9. Patentrecherche (Pflicht): Datenbanken Google Patents und Espacenet, DEPATISnet (alle drei nur über Websuche-Abfragen, nicht direkt; siehe Einschränkungen).
- Suche 1 (Websuche auf Google Patents): "Gessmann joystick Vergussmasse OR potting OR Verguss": kein Patent mit Anmelder Gessmann zu Verguss. Einziger Google-Patents-Treffer AT235579B (Silikon-Vergussmasse, Priorität 1960): Anmelder nicht erkennbar, nicht zuordenbar, aussortiert.
- Suche 2 (Websuche Espacenet/Patentliste): "Espacenet Gessmann W GmbH Patent Joystick Anmelder": Sekundärquelle trea.com listet für W. Gessmann GmbH US 8,967,014 "Multiple-axis manual control device" (erteilt 2015-03-03), US 8,207,805 (Taster, 2012) und US 11,904,766 (Lichtsignaleinrichtung für fahrerloses Transportsystem, 2024). Alle ohne erkennbaren Verguss-Bezug. Rechtsstand (aktiv/erloschen) NICHT geprüft. Quelle S.
- Ergebnis: 3 Patente (Sekundärliste, S), keines mit Verguss als Kern; eigene Entwicklung von Bedienelementen belegt. Kein Gegenbeweis für Verguss. DEPATISnet nicht abgefragt.
10. Einstufung Tom: interessant (Fertigung Hoch A, Verguss Hoch A), mit Vorbehalt: keine V-Quelle für die Fertigung, Tochter China
11. Ampel: 
12. CRM-Status: neu (crm_abgleich.py "W. Gessmann GmbH": kein Treffer; Grep "gessmann" in beiden CRM-Dateien: kein Treffer). Gessmann China Ltd. nicht als Konzernname im CRM.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Fertigungsbeleg V: Karriereseite/Stellenanzeige Leingarten (Montage, Elektronik) und gessmann.com Unternehmensseite im Browser lesen. (b) Werden Hall-Elektronik oder Griffe vergossen oder abgedichtet (Datenblatt Schutzart, Stellenanzeige "Vergießen")? (c) Welche Produkte fertigt die Tochter in China im Vergleich zu Leingarten? Aktion: vorerst keine Ansprache.
14. Quellen:
- https://www.directindustry.com/product-manufacturer/gessmann-ip67-joystick-154570-136402.html (S, Suchsnippet): „Degree of protection Control element up to IP67“; Abruf 2026-10-15.
- https://www.plantautomation-technology.com/suppliers/w-gessmann-gmbh (S, Triage-Quelle, nicht neu gelesen): Entwicklung, Teilmontage, CNC, THT/SMD im Werk; Abruf 2026-10-15.
- https://pdf.directindustry.com/pdf/w-gessmann-gmbh/joysticks/25091-1124792.html (S, Suchsnippet): „COMPLETE IN-HOUSE PRODUCTION“ mit Adresse Eppingerstr. 221, 74211 Leingarten; Abruf 2026-10-15.
- https://trea.com/organization/w-gessmann-gmbh/f612fc08-5513-4130-b036-724be78ce7f7 (S, Patentliste Sekundärquelle): „Multiple-axis manual control device“, US 8,967,014; Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Gessmann; Grep 2026-10-15); Websuche "Gessmann Leingarten Kunde Referenz Dosieranlage OR Klebstoff OR Vergussmasse OR Nordson OR Henkel OR DELO" (keine Treffer zu Gessmann). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: Name und Ort stimmen mit der Vorgabe überein (S): "W. Gessmann GmbH, Eppingerstr. 221, 74211 Leingarten" (directindustry-PDF, Suchsnippet). Rechtsform GmbH, Register und Impressum NICHT gelesen. Keine Abweichung zur Liste. Gessmann China Ltd. ist eine andere Einheit.

## 2. W.E.S.T Elektronik GmbH*
1. Firma: W.E.S.T Elektronik GmbH* (Messe: all about automation Düsseldorf 2026, Stand 523, Halle nicht angegeben; Liste: 78549 Spaichingen)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Ventil-/Leistungsverstärker, Regelkarten für Hydraulik)
3. Gebiet: Rest Deutschland+Niederlande (Niederkrüchten, NRW laut Recherche); laut Liste Spaichingen = Baden-Württemberg. Abweichung, siehe Feld 17.
4. Sitz und Fertigungsort: laut Verzeichnis (S) W.E.St. Elektronik GmbH, Gewerbering 31, 41372 Niederkrüchten; Fertigungsort nicht belegt. Spaichingen laut Liste unbelegt (Schuhmacher Technologies & Hydraulics GmbH nennt sich Generalvertretung von WEST, Adresse nicht erkennbar, S).
5. Website: unbekannt (w-e-st.de als Domain nur vermutet, ? , nicht geprüft)
6. Was wird gebaut: Entwicklung und Herstellung elektronischer Steuerungen für die Hydraulik (S, automa.net): Ventilverstärker (Hutschiene oder direkt am Ventil), Druck-/Pumpenregler, Positionierregler mit Mehrachs-Synchronisation, p/Q-Pressensteuerungen. Typisch vergossen/verklebt: Ventilverstärker im Ventilstecker- oder Hutschienengehäuse (A, Block B Gehäuse-Elektronik, Block A Magnetventil-Ansteuerung), Regelkarten (A, Block B Schutzlack/Teilverguss), Leistungsverstärker (A, Block A Leistungselektronik). Kein Beleg für Eigenverguss.
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Verzeichnis nennt "design and production" mit rund 10 Mitarbeitern (S); Standort wegen Ortsabweichung Liste/Recherche nicht eindeutig, Sitzregel daher nicht sicher anwendbar. Keine V-Quelle.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A (Einschätzung aus Produkttyp: Ansteuerelektronik für Magnetventile, Gehäuse-Elektronik). Einzelbewertung: Ventilverstärker im Steckergehäuse Mittel (A), Leistungsverstärker Mittel (A), Regelkarten/Pressensteuerung (Schaltschrank-Einbau) Niedrig (A). Kein Beleg zu IP-Schutzart (Datenblatt-Suche ergab keine Treffer zu WEST).
9. Patentrecherche (Pflicht): Datenbanken Google Patents, Espacenet und DEPATISnet (nur Websuche-Abfragen, nicht direkt).
- Suche 1 (Websuche mit Zielquellen DEPATISnet/Espacenet): Patent "W.E.St. Elektronik" OR "WEST Elektronik GmbH" Niederkrüchten Anmelder: keine Patente dieser Firma gefunden. Einziger Treffer DE3739705A1 (Prüfen elektronischer Leiterplatten, 1987) gehört WE ELECTRONIC GmbH: andere Firma, aussortiert.
- Suche 2 (Websuche Google Patents): keine weitere Abfrage möglich; Hauptabfrage der Firma lieferte nichts. Zweite Datenbank nicht direkt befragt.
- Ergebnis: keine Treffer gefunden, ausdrücklich nur Websuche (UNVOLLSTÄNDIG im Sinne der Direktabfrage, siehe Einschränkungen). Kein Gegenbeweis.
10. Einstufung Tom: prüfenswert (Fertigung Mittel S, Verguss Mittel A), Identität zuerst klären
11. Ampel: 
12. CRM-Status: neu (crm_abgleich.py mit "W.E.S.T Elektronik GmbH" und "W.E.St. Elektronik GmbH": beide kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Identität: Ist die Messefirma (Liste Spaichingen, Sternchen) dieselbe wie W.E.St. Elektronik GmbH Niederkrüchten? Impressum der Firmenwebsite und Handelsregister (Amtsgericht Mönchengladbach/Krefeld bzw. Spaichingen/Tuttlingen) lesen, Messeprofil auf duesseldorf.allaboutautomation.de ?p=330164 im Browser lesen. (b) Wo wird gefertigt (Eigenfertigung, Lohnfertigung)? Aktion: nicht kontaktieren, bis Identität geklärt.
14. Quellen:
- https://automa.net/company/west-elektronik-gmbh-de (S, Suchzusammenfassung): „development and manufacture of electronic controls for hydraulics“, Gewerbering 31, 41372 Niederkrüchten; Abruf 2026-10-15.
- https://duesseldorf.allaboutautomation.de/en/?p=330164 (S, Messeprofil, nicht gelesen): Eintrag „W.E.St. Elektronik GmbH“; Abruf 2026-10-15.
- https://friedrichshafen.allaboutautomation.de/en/?p=455438 (S): Schuhmacher Technologies & Hydraulics GmbH als „general representative of WEST Elektronik GmbH“; Abruf 2026-10-15.
15. Größe/Umsatz: rund 10 bis 11 Mitarbeiter, gegründet 1999 (Verzeichnisse 2024, S, Sekundärquelle); Umsatz unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag WEST; Grep 2026-10-15); Websuche "W.E.St. Elektronik Niederkrüchten Hydraulik Regelkarten Fertigung eigene Elektronikfertigung Bestückung Verguss" und Websuche "W.E.St. Elektronik Niederkrüchten Leistungsverstärker Ventilverstärker Gehäuse vergossen IP65 Datenblatt" (beide ohne Treffer zu Vergussanlagen oder Massen der Wettbewerber). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: ABWEICHUNG/unklar. Vorgabe: "W.E.S.T Elektronik GmbH*", 78549 Spaichingen (Liste). Gefunden (S): "W.E.St. Elektronik GmbH", Gewerbering 31, 41372 Niederkrüchten, gegründet 1999. Die Düsseldorfer Messeseite führt die Firma als "W.E.St. Elektronik GmbH"; weitere aaa-Messen führen "W.E.S.T Elektronik GmbH". Registerangaben nicht gelesen. Ob Spaichingen ein Vertriebs-/Servicestandort ist, ist nicht belegt. Ampel höchstens Gelb (Tabellenzeile 2).

## 3. Wachendorff Prozesstechnik GmbH & Co. KG
1. Firma: Wachendorff Prozesstechnik GmbH & Co. KG (Messe: all about automation Düsseldorf 2026, Stand 623, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Encoder, Elektronik, Magnetsensorik), nachrangig Optical Bonding (Displays/Mobile HMI) und Gasketing
3. Gebiet: Rest Deutschland+Niederlande (Geisenheim, Hessen)
4. Sitz und Fertigungsort: Industriestr. 7, 65366 Geisenheim; laut Verzeichnis Management, Entwicklung, Lager und Produktion (S, automationindiaexpo.com, Wachendorff Automation GmbH & Co. KG). Fertigende Einheit für Encoder: vermutlich Wachendorff Automation GmbH & Co. KG (Gruppe), siehe Feld 17.
5. Website: https://www.wachendorff-automation.com
6. Was wird gebaut: Inkremental- und Absolut-Encoder (Beispiel WDGP36J Inkremental IP67 + IP69K, WDGA Absolut-/Multiturn-Encoder mit patentierter EnDra-Technik, S), Seilzug-Systeme, Anzeigen/Zähler, Mobile-HMI/Bedienpanel (S, computer-automation.de). Typisch vergossen/verklebt/gedichtet: Encoder-Elektronik und Magnetsensorik für raue Umgebung (A, Block A Drehgeber/Encoder), IP67/IP69K-Gehäuse (A, Dichtung), Mobile-HMI-Displays (A, Block B Optical Bonding), Prozessanzeigen (A, Block B).
7. Fertigung DE/AT/NL: Hoch, Stufe S. Begründung: Verzeichnis nennt Produktion am Sitz Geisenheim und "all core products developed and manufactured in Germany" (Selbstaussage, S). Gruppe mit mehreren Gesellschaften, daher eigentlich V nötig (Konzernregel); Quelle auf der Firmenseite nachlesen.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Produkttyp Encoder, Block A; Schutzart IP67 + IP69K als Indikator, S). Einzelbewertung: Encoder-Elektronik/Magnetsensorik Hoch (A), Mobile-HMI-Display Mittel (A), Anzeigen/Zähler Mittel (A), Seilzug-Mechanik Niedrig (A). Kein Beleg für Eigenverguss.
9. Patentrecherche (Pflicht): Datenbanken Google Patents, Espacenet und DEPATISnet (nur Websuche-Abfragen, nicht direkt).
- Suche 1 (Websuche Patente): "patent Wachendorff Prozesstechnik Drehgeber Vergussmasse OR Verguss OR potting Anmelder": kein Patent mit Verguss-Bezug gefunden. Hinweis auf "patented EnDra technology" (Multiturn ohne Getriebe und Batterie), Patentnummer und Anmelder nicht gefunden.
- Suche 2 (Websuche Espacenet/Patentliste): "Wachendorff EnDra patent Multiturn Drehgeber EP Anmelder Wachendorff Automation GmbH": EP 2335028 B1 "Multiturn rotary encoder" erschien in den Treffern, Anmelder nicht erkennbar, Zuordnung zu Wachendorff NICHT belegt, Rechtsstand nicht geprüft. Nicht verwendet.
- Ergebnis: EnDra-Patent existiert laut Firmenangabe (S), Nummer/Status unbekannt; kein Verguss-Patent gefunden. Kein Gegenbeweis.
10. Einstufung Tom: interessant (Fertigung Hoch S, Verguss Hoch A), mit Vorbehalt: Fertigung nur S, Gruppe mit mehreren Einheiten
11. Ampel: 
12. CRM-Status: neu (crm_abgleich.py mit "Wachendorff Prozesstechnik GmbH & Co. KG" und "Wachendorff Automation": kein Treffer; Grep "wachendorff": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Fertigung V: Impressum/Standortseite wachendorff-automation.com und Karriereseite (Produktion/Montage Geisenheim) im Browser lesen. (b) Welche Gesellschaft der Wachendorff-Gruppe (Prozesstechnik, Automation, ggf. weitere) fertigt Encoder und ist die Messefirma? Handelsregister Wiesbaden/Geisenheim. (c) EnDra-Patentnummer, Anmelder und Rechtsstand auf Espacenet/Google Patents ermitteln. Aktion: noch nicht kontaktieren.
14. Quellen:
- https://www.automationindiaexpo.com/ShowPreview/wachendorff-automation-gmbh-co-kg (S, Suchsnippet): „Industriestr. 7“ in 65366 Geisenheim mit „production and all central services“; Abruf 2026-10-15.
- https://www.industrialautomationindia.in/newsitm/13368/Robust-36-mm-encoder-from-Wachendorff-for-harsh-environments/news (S, Suchsnippet): „rated IP67 + IP69K“ für WDGP36J; Abruf 2026-10-15.
- https://www.computer-automation.de/sensoren/multiturn-drehgeber-ohne-getriebe-und-batterie.htm (S, Suchsnippet): „patented EnDra technology replaces the gearbox“; Abruf 2026-10-15.
- https://www.wachendorff-automation.com/wachendorff-automation/ (S, Triage-Quelle, nicht neu gelesen); Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Wachendorff; Grep 2026-10-15); Websuche "Wachendorff Automation Geisenheim Dosieranlage OR Vergussanlage OR Vergussmasse OR Klebstoff Scheugenpflug OR Nordson OR Elantas OR Henkel" (nur ViscoTec/RAMPF/Tartler allgemein, kein Wachendorff-Bezug). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: teilweise belegt (S). Vorgabe "Wachendorff Prozesstechnik GmbH & Co. KG" (65366 Geisenheim). Suchtreffer: Encoder-Geschäft läuft über "Wachendorff Automation GmbH & Co. KG" (Marke, Domain wachendorff-automation.com), Prozesstechnik wird separat geführt (wachendorff-prozesstechnik.de, "Wachendorff Group"). Adresse Industriestr. 7, 65366 Geisenheim passt zur Liste. Register/Impressum nicht gelesen. Abweichung: fertigende Einheit eventuell Automation GmbH & Co. KG, nicht Prozesstechnik.

## 4. Wagner GmbH
1. Firma: Wagner GmbH (Messe: all about automation Düsseldorf 2026, Stand 435, Halle nicht angegeben; Liste: 42489 Wülfrath)
2. Segment / Demak-Geschäftsbereich: keiner erkennbar (Industrievertretung für Komponenten)
3. Gebiet: Rest Deutschland+Niederlande (Wülfrath, NRW)
4. Sitz und Fertigungsort: Robert-Bosch-Str. 35, Wülfrath (S, StepStone/Cylex). Keine Fertigung belegt.
5. Website: unbekannt (keine offizielle Website gefunden)
6. Was wird gebaut: Nichts belegt. Verzeichnis (Cylex, S) beschreibt die Firma als Industrievertretung mit Schwerpunkten Sonderheizung, Schaltschrankklimatisierung, Prozesskühlung, Signaltechnik, Sensorik, Kabelmanagement für Maschinen-/Anlagenbau, Chemie, Food, Automotive. Die Branchenzuordnung "Maschinen- und Anlagenbau" auf StepStone bezieht sich auf die Kundenbranche (S). Typisch vergossene Teile: keine als eigene Fertigung (A, Handel/Vertretung).
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Verzeichnisse beschreiben Industrievertretung, keine Fertigung (12 Mitarbeiter als Industrievertreter, S).
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A (Handel/Vertretung ohne belegte Eigenfertigung, Wissensbasis Block C). Keine Bauteile belegt.
9. Patentrecherche (Pflicht): Datenbanken Google Patents, Espacenet und DEPATISnet (nur Websuche-Abfragen, nicht direkt).
- Suche 1 (Websuche mit Zielquellen Espacenet/DEPATISnet): "Patent Anmelder Rothermundt Mönchengladbach OR Wagner GmbH Wülfrath Espacenet DEPATISnet": keine Patentdatensätze zu Wagner GmbH Wülfrath.
- Suche 2: Anmelder-Abfrage zu Wagner ist wegen des Allerweltsnamens unscharf (viele gleichnamige Firmen, z. B. Wagner Group Langenhagen); keine Zuordnung möglich, keine Treffer verwendet.
- Ergebnis: keine Treffer gefunden, nur Websuche. Kein Gegenbeweis.
10. Einstufung Tom: kein Fertiger (Industrievertretung, möglicher Ausschluss E2 Händler/Vertrieb, Tina entscheidet; Stufe S)
11. Ampel: 
12. CRM-Status: unklar. crm_abgleich.py "Wagner GmbH": PRAEFIX-Treffer bekannte_firmen_DE-AT-NL.txt Zeile 2531 "Wagner eCommerce Group GmbH [DE]". Ort/Branche im CRM nicht angegeben; vermutlich andere Firma (Namensähnlichkeit, Kern-Name nur "wagner"), nicht als neu bestätigt. Von Wagner Group (Langenhagen, Brandschutz) und Wagner Spritztechnik (Farbspritzgeräte) zu unterscheiden, beide ohne Verbindung belegt.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Identität: Handelsregister (Amtsgericht Düsseldorf/Wuppertal) für "Wagner GmbH, Robert-Bosch-Str. 35, Wülfrath" und Impressum der Firmenwebsite; Messeprofil duesseldorf.allaboutautomation.de ?p=353369 im Browser lesen. (b) Gibt es Eigenfertigung (z. B. Schaltschrank-Heizungen, Kabelmanagement)? (c) CRM: Ist "Wagner eCommerce Group GmbH" dieselbe Einheit (Ort im CRM prüfen)? Aktion: zurückstellen.
14. Quellen:
- https://web2.cylex.de/firma-home/wagner-gmbh-1476957.html (S, Suchsnippet): „industrial representative“ für Sonderheizung, Schaltschrankklimatisierung, Sensorik; Abruf 2026-10-15.
- https://www.stepstone.de/cmp/de/wagner-gmbh-386162/jobs (S, Suchsnippet): „Robert-Bosch-Strasse 35“ Wülfrath, 11–50 Mitarbeiter; Abruf 2026-10-15.
- bekannte_firmen_DE-AT-NL.txt Zeile 2531: „Wagner eCommerce Group GmbH [DE]“ (CRM-Namensähnlichkeit); Abruf 2026-10-15.
15. Größe/Umsatz: 11–50 Mitarbeiter (StepStone, S); Cylex nennt zwölf Industrievertreter am Standort (S); Umsatz unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Wagner GmbH Wülfrath; Grep 2026-10-15); keine eigene Websuche zu Wettbewerbern, da keine Fertigung belegt (Budget-Entscheidung, Lücke); Suchen zur Identität: Websuche "Wagner GmbH Wülfrath Robert-Bosch-Straße 35 Maschinenbau Anlagenbau" und "Wagner GmbH Wülfrath Industrievertretung Schaltschrankklimatisierung Heizung Website" (kein Wettbewerberbezug). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: nicht belegt. Vorgabe "Wagner GmbH, Wülfrath". Verzeichnisse (S) nennen "WAGNER GmbH, Robert-Bosch-Str. 35, Wülfrath" als Industrievertretung; Webauftritt, Register und Impressum nicht gefunden. Gleichnamige Firmen nicht vermischt (Wagner Group Langenhagen, Klimatechnik Wagner Neusäß, Maschinen-Wagner Renchen). Ampel höchstens Gelb (Tabellenzeile 2).

## 5. Walter Rothermundt GmbH & Co. KG
1. Firma: Walter Rothermundt GmbH & Co. KG (Messe: all about automation Düsseldorf 2026, Stand 716, Halle nicht angegeben; Liste: 41199 Mönchengladbach)
2. Segment / Demak-Geschäftsbereich: kein klarer Bereich (Antriebstechnik, PU-Zahnriemen); Gasketing/Doming nur theoretisch
3. Gebiet: Rest Deutschland+Niederlande (Mönchengladbach, NRW, laut Liste; Ort in Quelle nicht bestätigt)
4. Sitz und Fertigungsort: Mönchengladbach laut Liste (Stufe ?, keine Quelle zum Ort gefunden). Fertigungsort nicht belegt.
5. Website: unbekannt
6. Was wird gebaut: Firmenselbstbeschreibung im Messeprofil (S): "Experten für Antriebs- und Fertigungstechnik" mit Produkten und Lösungen für verschiedene Anforderungen; Partner der Mulco Europe EWIV (13 Partner, Pioniere der Polyurethan-Zahnriementechnik, S). Hersteller- oder Händleranteil nicht geklärt. Typisch vergossen/verklebt/gedichtet: Zahnriemen und Antriebselemente (A, Wissensbasis Block C/D: mechanische Antriebselemente, kein typischer Verguss; PU-Gießen von Riemen ist Gießen im Formenbau, nicht belegt und nicht als Demak-Verguss gewertet). Unbekannt, ob Elektronik oder Baugruppen vorkommen.
7. Fertigung DE/AT/NL: Niedrig, Stufe ?. Begründung: weder Fertigung noch Standort belegt; Selbstbeschreibung "manufacturer and sales partner" (S, Messeprofil über Suchzusammenfassung) lässt Händleranteil offen.
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A (Produkttyp mechanische Antriebselemente/Zahnriemen). Einzelbewertung: Zahnriemen Niedrig (A), Antriebselemente/Mechanik Niedrig (A). Falls Elektronik oder Antriebskomponenten im Programm sind, wäre neu zu bewerten (offen).
9. Patentrecherche (Pflicht): Datenbanken Google Patents, Espacenet und DEPATISnet (nur Websuche-Abfragen, nicht direkt).
- Suche 1 (Websuche mit Zielquellen Espacenet/DEPATISnet): "Patent Anmelder Rothermundt Mönchengladbach ...": keine Patentdatensätze zu Rothermundt (Treffer waren Anwaltskanzleien und Archivlisten, nicht verwendbar).
- Suche 2 (Websuche Google Patents/Produkt): "Rothermundt Mulco Polyurethan Zahnriemen Mönchengladbach Herstellung Gießen Patent": keine Treffer zu Rothermundt, nur zur Mulco-Gruppe allgemein.
- Ergebnis: keine Treffer gefunden, nur Websuche. Kein Gegenbeweis.
10. Einstufung Tom: unwahrscheinlich (Fertigung Niedrig ?, Verguss Niedrig A); Rolle (Hersteller oder Händler) offen
11. Ampel: 
12. CRM-Status: neu. crm_abgleich.py "Walter Rothermundt GmbH & Co. KG": nur GLEICHE WORTWURZEL zu "Walter Kraus GmbH" (bekannte_firmen_DE-AT-NL.txt Zeile 2534); nur der Vorname "Walter" gleich, andere Firma, kein Namensbezug. Kein Konzern bekannt.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Identität/Ort: Messeprofil duesseldorf.allaboutautomation.de ?p=353453 im Browser lesen, Impressum und Handelsregister (Amtsgericht Mönchengladbach). (b) Was stellt die Firma selbst her (Zahnriemen konfektionieren/gießen, Antriebsbaugruppen) und was handelt sie nur? (c) Gibt es Elektronik/Sensorik im Programm? Aktion: nicht weiter verfolgen, bis (b) beantwortet ist.
14. Quellen:
- https://www.duesseldorf.allaboutautomation.de/en/?p=353453 (S, Suchsnippet Messeprofil): „experts in drive and manufacturing technology“ und „Mulco Europe EWIV“; Abruf 2026-10-15.
- aaa_duesseldorf_2026.csv: „Walter Rothermundt GmbH & Co. KG;716;41199;Mönchengladbach;Deutschland“ (Messeliste, Stand 716); Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Rothermundt; Grep 2026-10-15); Websuche "Walter Rothermundt GmbH Mönchengladbach" und "Rothermundt Mönchengladbach Firma Produkte Hersteller" (keine Quelle zu Anlagen oder Massen von Wettbewerbern). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: nicht belegt. Vorgabe "Walter Rothermundt GmbH & Co. KG, 41199 Mönchengladbach" stammt aus der Messeliste (csv). Das Messeprofil (S) bestätigt den Firmennamen und die Branche Antriebstechnik, nicht Adresse, Rechtsform und Register. Kein Impressum gelesen. Ampel höchstens Gelb (Tabellenzeile 2), falls Tina nicht Rot (kein Fertiger) setzt.

## 6. WEG Germany GmbH
1. Firma: WEG Germany GmbH (Messe: all about automation Düsseldorf 2026, Stand 421, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Statorwicklungen, Motorelektronik, Umrichter), E-Mobility Potting nachrangig
3. Gebiet: Rest Deutschland+Niederlande (Kerpen, NRW); weitere DE-Standorte Unna, Balingen (Baden-Württemberg), Homberg (Hessen)
4. Sitz und Fertigungsort: Industriegebiet Türnich 3, Röntgenstraße 36-38, 50169 Kerpen-Türnich (S, weg.net laut Suchzusammenfassung). Fertigende Einheit: Kerpen (Stellenanzeige Fertigungsmitarbeiter Antriebskomponenten, S), Balingen (Württembergische Elektromotoren, übernommen, Getriebe/Motoren/Servomotoren bis 1000 Watt, Quelle 2014, S), Homberg (KATT Antriebstechnik, S). Welches Produkt wo gefertigt wird, ist NICHT belegt. Konzern WEG S.A., Brasilien.
5. Website: https://www.weg.net
6. Was wird gebaut: Elektromotoren, Getriebe, Servo, Antriebe, Automation (Triage, S); Balingen: Getriebe, Dreh-, Wechsel-, Gleichstrommotoren bis 1000 Watt, Kleinservomotoren (S). Typisch vergossen/verklebt/gedichtet: Statorwicklungen (A, Block A Elektromotoren/Wicklung, Imprägnierung), Motorelektronik und Umrichter (A, Block A Leistungselektronik), Servomotoren mit Elektronik (A, Block A), Getriebe-Dichtungen (A, Dichtung, Mittel).
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Konzern mit mehreren Werken (V nötig, nicht erreicht). Belege nur S: Stellenanzeige "Mechatroniker/Elektroniker als Fertigungsmitarbeiter für Antriebskomponenten" Kerpen (Aggregator-Snippet, undatiert), Übernahmemeldung Balingen 2014 mit "manufacturing plants in Balingen". Einheitenzuordnung offen: Kerpen könnte vorwiegend Montage/Applikation sein.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Produkttyp Elektromotoren/Statorwicklung und Umrichter, Block A). Einzelbewertung: Statorwicklung (Imprägnierung/Verguss) Hoch (A), Umrichter/Motorelektronik Hoch (A), Servomotoren mit Elektronik Hoch (A), Getriebe/Dichtungen Mittel (A). Kein Beleg zu Eigenverguss gefunden (Suche nach Referenzen von bdtronic/Henkel/Elantas mit WEG ohne Treffer).
9. Patentrecherche (Pflicht): Datenbanken Google Patents, Espacenet und DEPATISnet (nur Websuche-Abfragen, nicht direkt).
- Suche 1 (Websuche Patente): "patent WEG Equipamentos Eletricos potting OR encapsulation OR Vergussmasse stator resin": kein Patent mit Anmelder WEG gefunden; angezeigte Statorverguss-Patente gehören anderen Anmeldern (z. B. Moteurs Leroy-Somer US 2015/0145351), aussortiert.
- Suche 2: Anmelder-Varianten WEG S.A., WEG Equipamentos Elétricos, WEG Drives & Controls, Württembergische Elektromotoren nur teilweise über Websuche berücksichtigt; keine Treffer. WEG ist ein Konzern mit sehr großer Patentliste: eine enge Direktabfrage fehlt, daher kein Aussagewert.
- Ergebnis: keine Treffer gefunden, nur Websuche, Konzernpatente nicht ausgewertet. Kein Gegenbeweis, eher Lücke.
10. Einstufung Tom: prüfenswert (Fertigung Mittel S, Verguss Hoch A); CRM-Konzernbezug (Feld 12) beachten
11. Ampel: 
12. CRM-Status: unklar, CRM-Konzernbezug (Regel M). crm_abgleich.py "WEG Germany GmbH" und "WEG": kein Treffer. Aber: WEG hat laut Fachpresse (S) KATT Antriebstechnik (Homberg) übernommen ("Jetzt fünf Filialen in Deutschland: WEG übernimmt Katt Antriebstechnik", industrial-production.de), und bekannte_firmen_DE-AT-NL.txt führt "Antriebstechnik KATT Hessen GmbH [DE]" und "AKH ANTRIEBSTECHNIK KATT HESSEN [DE]". Ob dies dieselbe Einheit/Schwester ist, ist offen (Jey bestätigt, Regel M).
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Ist "Antriebstechnik KATT Hessen GmbH" (CRM) die von WEG übernommene KATT Antriebstechnik (Homberg)? Fertigungsstandort und Gesellschaft klären, Jey bestätigt die Einheit. (b) Was fertigt WEG Germany GmbH in Kerpen (Antriebskomponenten, Umrichter, Motoren)? Karriereseite und Impressum weg.net im Browser lesen, Handelsregister Köln. (c) Werden in Balingen/Kerpen Statoren imprägniert oder vergossen (Stellenanzeigen, Datenblätter Schutzart)? Aktion: nicht kontaktieren, bis (a) geklärt ist.
14. Quellen:
- https://www.industrial-production.de/antriebstechnik/jetzt-fuenf-filialen-in-deutschland-weg-uebernimmt-katt-antriebstechnik.htm (S, Suchsnippet): „Jetzt fünf Filialen in Deutschland: WEG übernimmt Katt Antriebstechnik“; Abruf 2026-10-15.
- https://jobjump.net/jobs/logistikmitarbeiter-mwd-e7bbd629-0482-588b-9963-8fccd3bbd399 und StepStone-Aggregator (S, Suchzusammenfassung): „Fertigungsmitarbeiter für Antriebskomponenten“ bei WEG Germany, Kerpen; Abruf 2026-10-15.
- https://www.industrial-production.de/wirtschaft---unternehmen/weg-uebernimmt-wuerttembergische-elektromotoren.htm (S, Suchsnippet): „manufacturing plants in Balingen“ (Meldung ca. 2014); Abruf 2026-10-15.
- bekannte_firmen_DE-AT-NL.txt (CRM): „Antriebstechnik KATT Hessen GmbH [DE]“; Abruf 2026-10-15.
15. Größe/Umsatz: Balingen 2013 etwa 80 Mitarbeiter, Umsatz rund 7 Mio EUR (S, alt); WEG Germany: Bilanzsumme rund 100 Mio EUR laut implisense (S, Sekundärquelle). Beides unsicher.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag WEG; Grep 2026-10-15); Websuche "WEG motors stator impregnation OR potting customer reference Scheugenpflug OR bdtronic OR Elantas OR Nordson OR Henkel" (keine Referenz mit WEG; nur anonyme bdtronic-/Henkel-Fälle). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: teilweise belegt (S). Vorgabe "WEG Germany GmbH, 50169 Kerpen" passt zur WEG-Adresse Kerpen-Türnich (weg.net laut Suchzusammenfassung). Handelsregister/Impressum nicht gelesen, Register-Nr. unbekannt. Verwechslung ausgeschlossen mit WEG Holding GmbH (Wien) und easy WEG GmbH (Bad Staffelstein). Konzern WEG S.A. (Brasilien).

## 7. Yaskawa Europe GmbH - Drives Motion Controls Division
1. Firma: Yaskawa Europe GmbH - Drives Motion Controls Division (Messe: all about automation Düsseldorf 2026, Stand 630, Halle nicht angegeben; Liste: 65795 Hattersheim am Main)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Servo- und Umrichter-Leistungselektronik); E-Mobility Potting nachrangig
3. Gebiet: Rest Deutschland+Niederlande (Hattersheim, Hessen) für den Sitz; Fertigung der Drives laut Fachpresse außerhalb (Schottland, Slowenien)
4. Sitz und Fertigungsort: Sitz Hattersheim (Europazentrale, Bürogebäude mit Training Center und Innovation Center, kein Produktionsbetrieb belegt, S). Drive-Fertigung Europa: Cumbernauld (Schottland) und geplante Werke in Slowenien (Kočevje, Meldung 2018, Stand unbekannt); Roboterwerk Kočevje (S).
5. Website: https://yaskawa.eu.com
6. Was wird gebaut: Frequenzumrichter, Servoantriebe, SPS, HMI (Triage, S). In Hattersheim laut Meldung "3.450 m² Bürofläche für ca. 220 Mitarbeiter", Training und Innovation Center (S). Typisch vergossen/verklebt/gedichtet (Produkttyp, nicht für Hattersheim): Servoverstärker/Umrichter-Leistungselektronik (A, Block A), Servomotoren (A, Block A), SPS/HMI (A, Block B).
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Hattersheim ist laut Fachpresse Zentrale/Büro/Training; Drive-Fertigung in Europa Cumbernauld und Slowenien, also außerhalb DE/AT/NL (harter Ausschlussgrund E3 für diese Einheit möglich, Tina entscheidet). Robotics-Sparte separat (Allershausen), nicht Teil dieser Division.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Produkttyp Servoantriebe/Umrichter, Block A), aber am Standort Hattersheim ohne Fertigungsbeleg. Einzelbewertung: Servoverstärker/Umrichter Hoch (A), Servomotoren Hoch (A), SPS/HMI Mittel (A).
9. Patentrecherche (Pflicht): Datenbanken Google Patents, Espacenet und DEPATISnet (nur Websuche-Abfragen, nicht direkt).
- Suche 1 (Websuche Google Patents): "patent Yaskawa Electric potting OR encapsulated OR sealing resin servo amplifier OR inverter Yaskawa Denki": keine Patente in den Treffern (nur Händlerlisten).
- Suche 2: Anmelder-Varianten (Kabushiki Kaisha Yaskawa Denki, Yaskawa Electric Corp, Yaskawa Europe) nicht direkt abgefragt. Yaskawa Electric hat als Konzern erfahrungsgemäß sehr viele Patente, hier nicht ausgewertet.
- Ergebnis: keine Treffer gefunden, Lücke (Konzernpatente nicht ausgewertet, nur Websuche). Kein Gegenbeweis.
10. Einstufung Tom: unwahrscheinlich (Fertigung Niedrig S: Zentrale ohne belegte Produktion in DE/AT/NL, Verguss Hoch A nur für Produkttyp)
11. Ampel: 
12. CRM-Status: neu (crm_abgleich.py "Yaskawa Europe GmbH" und "Yaskawa Electric": kein Treffer; Grep "yaskawa|motoman" in beiden CRM-Dateien: kein Treffer). Yaskawa Europe Robotics (Allershausen) separate Einheit, ebenfalls nicht im CRM.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Fertigt Yaskawa Europe in Hattersheim, Allershausen oder an einem anderen DE-Standort Drives/Umrichter (Impressum, Standortseite, Stellenanzeigen Produktion)? Aktuelle Quelle 2025/2026, da die Slowenien-Meldungen von 2018 stammen. (b) Aktueller Stand Slowenien/Cumbernauld für Drives. Aktion: Beobachtung; Ansprache eher nicht, außer Fertigung DE wird belegt.
14. Quellen:
- https://yaskawa.eu.com/header-meta/news-events/article/yaskawa-opens-new-european-headquarters-in-hattersheim_n19580 (S, Suchsnippet): „European headquarters in Hattersheim“ mit Training Center und Innovation Center; Abruf 2026-10-15.
- https://www.computer-automation.de/drives-en/production-of-drive-technology-in-slovenia.htm (S, Suchsnippet): „frequency inverters, servo drives and servo motors“ in Slowenien geplant (Meldung ca. 2018); Abruf 2026-10-15.
- https://www.industrial-production.de/wirtschaft---unternehmen/yaskawa-eroeffnet-neue-produktionsstandorte-in-slowenien.htm (S, Suchsnippet): Cumbernauld-Werk für Servo und Umrichter bleibt bestehen; Abruf 2026-10-15.
15. Größe/Umsatz: Yaskawa Europe ca. 2.000 Mitarbeiter in EMEA, fünf Produktionsstandorte (Suchzusammenfassung yaskawa.eu.com, S); Hattersheim ca. 220 Arbeitsplätze (S).
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Yaskawa; Grep 2026-10-15); Websuche "Yaskawa servo drive production Europe potting OR dispensing OR Vergussmasse Nordson OR Scheugenpflug OR Henkel OR Elantas customer" (keine Treffer zu Yaskawa mit Wettbewerbern). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: stimmt weitgehend überein (S). Yaskawa Europe GmbH hat Sitz Hattersheim (Pressemeldung Eröffnung der Europazentrale, S). Der Zusatz "Drives Motion Controls Division" ist eine Sparte der Yaskawa Europe GmbH, keine eigene Gesellschaft (Annahme aus Firmenaufbau, ?). Impressum und Register nicht gelesen. Konzern Yaskawa Electric (Japan); Robotics-Sparte in Allershausen separat.

## nicht aufgenommen (bereits bekannt / unklar)
Keine Firma des Batches ist BEKANNT. Der Liste bleibt vollständig; unklar/CRM-Bezug:
| Firma (Vorgabe) | CRM-Schreibweise | gefundene Schreibweise | Status |
|---|---|---|---|
| Wagner GmbH | Wagner eCommerce Group GmbH [DE] (bekannte_firmen Zeile 2531) | WAGNER GmbH, Wülfrath (Industrievertretung) | unklar, Namensähnlichkeit, Einheit klären |
| WEG Germany GmbH | Antriebstechnik KATT Hessen GmbH [DE] / AKH ANTRIEBSTECHNIK KATT HESSEN [DE] | WEG Germany GmbH, Kerpen (WEG hat KATT Antriebstechnik übernommen, S) | CRM-Konzernbezug, Einheit klären (Regel M) |
| Walter Rothermundt GmbH & Co. KG | Walter Kraus GmbH [DE] (Zeile 2534) | Walter Rothermundt GmbH & Co. KG | neu, nur Vorname gleich, andere Firma |

## Einschränkungen (ehrlich)
- Umgebung: Nur WebSearch (29 Abfragen) genutzt. WebFetch nicht aufgerufen, Chrome-Werkzeuge standen nicht zur Verfügung. Deshalb ist KEINE Aussage in diesem Batch Stufe V: alle Fertigungs- und Produktangaben sind S (Suchzusammenfassung/Snippet) oder A (Produkttyp). Alle Zitate in Feld 14 stammen aus Suchzusammenfassungen und sind nicht am Original gegengelesen. Die Triage-URLs (plantautomation-technology.com, jobjump.net, yaskawa.eu.com/Hattersheim, stepstone) wurden nicht erneut gelesen.
- Patentrecherche (Feld 9): Google Patents, Espacenet und DEPATISnet wurden NICHT direkt abgefragt (keine Browser-Anmelderfilter, keine Espacenet-Direkt-URL, kein DEPATISnet). Es lief je Firma nur 1 bis 2 Websuche-Abfragen mit Patentbegriffen. Folge: Zahl der Treffer, Rechtsstand und Anmelder-Varianten (Konzern, Vorgänger) sind nicht belegt, "keine Treffer" ist nur ein Websuche-Ergebnis. Der Batch ist für Feld 9 in diesem Sinne schwach; Patentrecherche muss im Browser nachgeholt werden (besonders WEG, Yaskawa, Wachendorff EnDra, Gessmann 3 Sekundärpatente).
- Wettbewerbereinsatz (Feld 16): je Firma nur 1 bis 2 gezielte Abfragen plus Abgleich mit wettbewerber_referenzen.md (Grep nach Firmennamen, nur der gelesene Teil bis Zeile 378 und Namenssuche über die ganze Datei). Für Wagner GmbH und Rothermundt keine eigene Wettbewerberabfrage (keine Fertigung belegt, Budget). "Kein Hinweis" ist kein Gegenbeweis.
- Schwach oder nicht gesucht: Register/Impressum aller sieben Firmen (Feld 17 nur S); Stellenanzeigen nur über Aggregator-Snippets (WEG Kerpen); aktuelle (2025/2026) Fertigungsquellen für Balingen/Kerpen und Yaskawa-Slowenien (Quellen 2014 und 2018); Größe/Umsatz nur nebenbei; Wachendorff-Gruppenstruktur; Rothermundt Ort und Rolle (Hersteller/Händler) gar nicht belegt.
- Stufe-A-Aussagen (Triage und Produkttyp-Ableitung) sind als solche gekennzeichnet; der Produkttyp von Wagner GmbH und Rothermundt ist nur aus Verzeichnis-/Messeprofilen abgeleitet.
- Keine Kontaktsuche (Regel K). Nicht committet.

## Zusammenfassung Einstufung
interessant: 2 (Gessmann, Wachendorff; beide mit Vorbehalt, Fertigung nicht V). prüfenswert: 2 (W.E.S.T Elektronik, WEG Germany). unwahrscheinlich: 2 (Rothermundt, Yaskawa Europe). kein Fertiger: 1 (Wagner GmbH). Wettbewerber/Lieferant: 0. BEKANNT: 0 (unklar/CRM-Bezug: 2, Wagner GmbH und WEG Germany GmbH).
