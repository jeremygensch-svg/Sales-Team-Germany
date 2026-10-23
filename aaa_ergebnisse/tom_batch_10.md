# Tom Batch 10 – all about automation Düsseldorf 2026 (aaa, Messemodus Regel N)
Erstellt: 2026-10-15 (Tom, Stufe 1, Version 2, getrennter Agent, nur Tom-Rolle). Eingabe: aaa_batches_v2/pruef_09.md, 10 Firmen. Halle ist in der Liste nicht angegeben, Feld 1 trägt nur die Standnummer.
Alle Abrufdaten: 2026-10-15. Belegstufen: V = selbst gelesen (Browser), S = nur Websuche-Snippet oder Messe-Beschreibungstext (Seite nachlesen), A = aus Produkttyp abgeleitet, ? = angenommen.
WICHTIG zur Umgebung: WebFetch und Chrome standen NICHT zur Verfügung, Websuche-Budget 30 Abfragen. Es gibt deshalb in diesem Batch KEINE Aussage mit Stufe V. Alle Websuchen waren Standard-Websuchen (keine direkte Abfrage von Google Patents, Espacenet oder DEPATISnet). Triage-Angaben (Sitz, Produkte) sind unverifiziert und als Stufe A bzw. S geführt.
Messe-Signal (Regel N2): Grep auf aaa_duesseldorf_2026.csv (Wettbewerber/Materialhersteller aus Regel E1: Scheugenpflug, DOPAG, Nordson, ViscoTec, bdtronic, RAMPF, Sonderhoff, Hilger u. Kern, Musashi, GONANO, Marco, Henkel, DELO, ELANTAS, Wacker, Sika, Graco, Atlas Copco, Panacol, EPOXONIC, WEVO, Lohmann, OTTO-CHEMIE, Hexion): kein Treffer. Keine dieser Firmen stellt auf der aaa aus.
CRM-Abgleich: `python3 crm_abgleich.py` je Firma mit Konzern-/Altnamen ausgeführt (Ergebnis je Firma in Feld 12).

## 1. P+K Maschinen- und Anlagenbau GmbH
1. Firma: P+K Maschinen- und Anlagenbau GmbH (Messe: all about automation Düsseldorf 2026, Stand 700, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: kein klarer Bereich (Sondermaschinenbau); Randfall Electrical Insulation (verbaute Antriebe, Sensorik, Steuerung)
3. Gebiet: Rest Deutschland+Niederlande (Solingen, NRW, laut Messeliste)
4. Sitz und Fertigungsort: Solingen (42653) laut Messeliste, Stufe A/S; laut Triage "Sitz unbestätigt". Fertigende Einheit nicht belegt.
5. Website: unbekannt (nicht gefunden)
6. Was wird gebaut: "special and testing machines, poka-yoke systems, ... assembly and welding machines, camera, robot and assembly systems" (S, Messe-Beschreibungstext, Suchsnippet https://www.duesseldorf.allaboutautomation.de/en/exhibitors/pk-maschinen-und-anlagenbau-gmbh-223397). Typisch vergossen/verklebt/gedichtet (A, Endprodukt-Regel): in den Maschinen verbaute Antriebe/Servomotoren, Sensorik, Steuerungs-Netzteile, Kabel/Stecker. Das Produkt selbst (Maschine) wird nicht vergossen.
7. Fertigung DE/AT/NL: Mittel, Stufe A. Begründung: Sondermaschinenbauer (eigene Produkte) mit Sitz Solingen laut Messeliste, aber Sitz in der Triage unbestätigt und keine Standortseite gefunden; Sitzregel daher nicht voll anwendbar.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A (Einschätzung aus Produkttyp). Einzelbewertung: verbaute Servo-/Antriebsmotoren Mittel (A), Sensorik/Kamera Mittel (A), Schaltschrank-/Steuerungselektronik Mittel (A), Mechanik/Gestell Niedrig (A). Maschinenbauer sind kein Vergießer, Endprodukt-Regel hebt nur auf Mittel.
9. Patentrecherche (Pflicht, mind. 2 Suchen):
- Suche 1: Websuche "P+K Maschinen- und Anlagenbau Solingen Patent OR Gebrauchsmuster Anmelder": keine Treffer für den Anmelder (nur unzusammenhängende Archiv-/Patent-Leaderboard-Seiten). Datenbank: Websuche (kein direkter DB-Zugriff).
- Suche 2: NICHT ausgeführt (Budget; Google Patents/Espacenet/DEPATISnet nicht direkt abfragbar). Feld 9 daher UNVOLLSTÄNDIG: Nachholen Google Patents Anmelder "P+K Maschinen", Espacenet pa="p k maschinen", DEPATISnet.
- Ergebnis: keine Treffer gefunden; kein Gegenbeweis.
10. Einstufung Tom: prüfenswert (Fertigung Mittel A, Verguss Mittel A)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "P+K Maschinen- und Anlagenbau GmbH": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Identität (Firmenwebsite, Impressum, Handelsregister Wuppertal/Solingen) klären; Wird in Solingen gefertigt, welche Bauteile (Antriebe, Sensorik, Steuerungen) stecken in den Prüf-/Montageautomaten? Patentsuche vollständig nachholen. Aktion: nicht kontaktieren, bis Identität belegt.
14. Quellen:
- https://www.duesseldorf.allaboutautomation.de/en/exhibitors/pk-maschinen-und-anlagenbau-gmbh-223397 (S, Suchsnippet/Messetext, Regel N5): "special and testing machines, poka-yoke systems"; Abruf 2026-10-15.
- aaa_duesseldorf_2026.csv: "P+K Maschinen- und Anlagenbau GmbH;700;42653;SOLINGEN"; 2026-10-15.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep: kein Eintrag P+K); Websuche "Klefinghaus OR P+K Maschinen Dosieranlage OR Klebeanlage OR Vergussanlage Kunde Referenz Nordson OR Scheugenpflug OR DOPAG OR ViscoTec" (kein Treffer zu P+K). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: NICHT belegt. Firmenname laut Messeeintrag; Website, Impressum, Rechtsform-Register und Adresse nicht gefunden (Websuche liefert nur den Messeeintrag). Sitz Solingen nur aus Messeliste. Tina: Tabellenzeile 2 prüfen.

## 2. Peakboard GmbH
1. Firma: Peakboard GmbH (Messe: all about automation Düsseldorf 2026, Stand 308, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: kein klarer Bereich (Visualisierungs-Software mit eigener Hardware "Peakboard Box"); Randfall Electrical Insulation (Embedded-Box)
3. Gebiet: Baden-Württemberg (Stuttgart)
4. Sitz und Fertigungsort: Sitz Friedrichstraße, Stuttgart (S, Suchsnippet peakboard.com/en/imprint; Triage: Friedrichstr. 13). Fertigungsort der Hardware: nicht belegt.
5. Website: https://peakboard.com
6. Was wird gebaut: Low-Code-Software "Peakboard Designer", Hardware "Peakboard Box" ("Intel Celeron N5105, 8 GB RAM, ... Gehäuse aus Aluminium", S, https://peakboard.com/en-us/product/peakboard-box) und BYOD-Option. Typisch vergossen/verklebt/gedichtet (A): Embedded-Box im Alu-Gehäuse, lüfterlos (Wärmeleit-Pads, Gehäusedichtung, Block B, Einschätzung); Software keine Teile. Ob Hardware selbst gefertigt oder zugekauft wird, ist unbelegt.
7. Fertigung DE/AT/NL: Niedrig, Stufe ?. Begründung: Softwarehaus, Fertigungsort der Box unbekannt, Hardware vermutlich zugekauft (angenommen).
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A. Einzelbewertung: Peakboard Box (Industrie-PC) Niedrig (A), Software keine Teile.
9. Patentrecherche (Pflicht, mind. 2 Suchen):
- Suche 1: Websuche "Peakboard GmbH Patent Anmelder Visualisierung Patent": keine Patent-Treffer.
- Suche 2: NICHT ausgeführt (Budget). Feld 9 UNVOLLSTÄNDIG: Google Patents/Espacenet/DEPATISnet Anmelder "Peakboard" nachholen.
- Ergebnis: keine Treffer gefunden; kein Gegenbeweis.
10. Einstufung Tom: unwahrscheinlich (Fertigung Niedrig ?, Verguss Niedrig A); möglicher Ausschluss E2 (Software), Tina entscheidet
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "Peakboard GmbH" und "Theobald Software": kein Treffer). Früher Tochter von Theobald Software, seit 2022 eigenständig (Triage und Suchsnippet S).
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Wo und von wem wird die Peakboard Box gefertigt (Datenblatt, CE-Konformität, Hersteller-Adresse)? Wenn Zukauf: "kein Fertiger" an Tina. Aktion: nicht weiter verfolgen, Entscheidung Tina.
14. Quellen:
- https://peakboard.com/en-us/product/peakboard-box (S, Suchsnippet): "Gehäuse aus Aluminium"; Abruf 2026-10-15.
- https://peakboard.com/en/imprint (S, Suchsnippet): Stuttgart, ausgegliedert 2022 von Theobald Software; Abruf 2026-10-15.
15. Größe/Umsatz: rund 35 Beschäftigte an drei Standorten (Suchsnippet Herstellerseite, S)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Peakboard/Theobald); Websuche "Peakboard Box Hardware hergestellt Fertigung Gehäuse Stuttgart" (kein Hinweis auf Dosier-/Vergusstechnik oder Wettbewerber). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: weitgehend übereinstimmend (S): Peakboard GmbH, Friedrichstraße, Stuttgart, laut Imprint-Snippet. Registernummer/Impressum nicht im Volltext gelesen. Messeliste 70174 Stuttgart passt. Keine Abweichung gefunden.

## 3. Pfannenberg*
1. Firma: Pfannenberg* (Messe: all about automation Düsseldorf 2026, Stand 435, Halle nicht angegeben; Sternchen und gemeinsamer Stand mit Printec-DS HMI Solutions* laut Liste, Sitz in der Liste Wülfrath 42489)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Signalgeber, Steuerelektronik der Kühlgeräte, Lüfter), LED Encapsulation (LED-Signalleuchten), nachrangig Gasketing/Sealing (Schaltschrank-Kühlgeräte, Filterlüfter, Dichtungen)
3. Gebiet: Rest Deutschland+Niederlande (Hamburg; Messeliste Wülfrath NRW)
4. Sitz und Fertigungsort: Hauptsitz Hamburg, Werner-Witt-Straße 1 (S, Suchsnippet pfannenberg.com). Produktionsstandorte "in Germany, Italy, the United States and China" (S, Eigenangabe pfannenberg.com global-set-up); ob Hamburg selbst produziert und welche Produkte dort entstehen, ist NICHT belegt (Lehre 4/5). Sitz Wülfrath: NICHT belegt.
5. Website: https://www.pfannenberg.com
6. Was wird gebaut: "Thermomanagement-Produkte, Flüssigkühllösungen und Signaltechnik" (S): Schaltschrank-Kühlgeräte, Filterlüfter, Kühlaggregate, Signalleuchten, Signalhörner, kombinierte Signalgeber, Signalsäulen (IP54/IP66, Xenon/LED). Typisch vergossen/verklebt/gedichtet (A): LED-/Xenon-Signalleuchten (IP66, Block A Signalleuchten), Signalgeber-Elektronik (Block A), Kühlgeräte-Steuerelektronik (Block B), Lüfter-/EC-Motoren (Block A), Gehäusedichtungen/Filtermatten (Block B). Welches Produkt in welchem Werk entsteht, ist nicht belegt.
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Konzern/Gruppe mit mehreren Werken (DE, IT, US, CN), daher Stufe V nötig; nur Eigenangabe "production facilities in Germany" als Snippet, Hamburg als Fertigungsort nicht belegt.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Signalleuchten/Signalgeber, Einschätzung aus Produkttyp). Einzelbewertung: LED-Signalleuchten Hoch (A), Signalhörner/-geber-Elektronik Hoch (A), Lüfter/EC-Motor Mittel (A), Kühlgeräte-Steuerelektronik Mittel (A), Gehäuse/Dichtungen Mittel (A).
9. Patentrecherche (Pflicht, mind. 2 Suchen):
- Suche 1: Websuche "patents.google.com Pfannenberg GmbH Anmelder Signalleuchte Vergussmasse OR potting": keine Pfannenberg-Patente, nur Produktlisten (RS Components).
- Suche 2: Websuche "Pfannenberg GmbH Patent Espacenet Signalgerät OR Kühlgerät OR Lüfter Anmelder Pfannenberg": Treffer über Justia (US-Patente, Anmelder Pfannenberg GmbH, Erfinder Andreas Pfannenberg): US 8727842 "filter fan with spring-clip quick fastening" (erteilt 20.05.2014), US 9883609 (erteilt 30.01.2018, Fortsetzung), US 9889397 / Anm. 20140215981 "air passage device with swivelling design cover" (2014), US 9677571 "filter fan with blower, aeration grid and filter mat". Quelle https://patents.justia.com/assignee/pfannenberg-gmbh?page=2 (S, Rechtsstand nicht geprüft). Alle Lüfter/Gehäuse, kein Verguss-Bezug. Datenbank: Justia über Websuche; Google Patents, Espacenet und DEPATISnet nicht direkt abgefragt.
- Ergebnis: Patente der Firma vorhanden (Filterlüfter), keines mit Verguss als Kern; Signalgeber-Patente nicht gefunden (nicht gesucht per Anmelder-Datenbank).
10. Einstufung Tom: prüfenswert (Fertigung Mittel S, Verguss Hoch A)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "Pfannenberg", "Pfannenberg Europe", "Pfannenberg Group": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Identität: Welche Einheit stellt aus (Pfannenberg Europe GmbH Hamburg? Wülfrath-Bezug?) und wer teilt Stand 435 mit Printec-DS? Impressum pfannenberg.com und Messeeintrag lesen. (b) Werden Signalleuchten/Signalgeber in Hamburg gefertigt oder nur in IT/US/CN (pfannenberg.com global-set-up, Stellenanzeigen Hamburg Produktion/Montage)? (c) Wird in Hamburg vergossen (Stellenanzeigen, Signaltechnik-Produktion)? Aktion: Beobachtung, bis (b) geklärt.
14. Quellen:
- https://www.pfannenberg.com/en/know-how/thermal-management/trust-in-the-best-solutions/global-set-up/ (S, Suchsnippet): Produktionsstandorte "in Germany, Italy, the United States and China"; Abruf 2026-10-15.
- https://www.chemie.de/firmen/11887/pfannenberg-gmbh.html (S, Suchsnippet): Adresse Hamburg; Abruf 2026-10-15.
- https://patents.justia.com/assignee/pfannenberg-gmbh?page=2 (S, Suchsnippet): Filterlüfter-Patente; Abruf 2026-10-15.
15. Größe/Umsatz: rund 470 Beschäftigte an vier Produktionsstandorten (Trumpf-Kundenbericht, undatiert, Suchsnippet S); Umsatz unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Pfannenberg); Websuche "Pfannenberg Kunde Referenz Dosieranlage OR Klebstoff OR Vergussmasse OR Sonderhoff OR Nordson OR DOPAG OR Henkel Signalgeber Fertigung" (keine Treffer zu Pfannenberg). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: ABWEICHUNG/unklar. Vorgabe "Pfannenberg*, 42489 Wülfrath". Gefunden: Pfannenberg GmbH, Werner-Witt-Straße 1, Hamburg (S, chemie.de). Kein Beleg für einen Standort Wülfrath (Suche nach Wülfrath ohne Treffer). Stand 435 wird mit Printec-DS HMI Solutions geteilt (Sternchen/Wülfrath-Sitz vermutlich Vertretung oder Listenfehler, Triage-Hinweis, nicht belegt). Rechtsform/Register nicht gelesen. Tina: Tabellenzeile 2, höchstens Gelb bis Jey bestätigt.

## 4. Pilz GmbH & Co. KG
1. Firma: Pilz GmbH & Co. KG (Messe: all about automation Düsseldorf 2026, Stand 725, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Sicherheitsrelais, Elektronikbaugruppen, Sensoren, Antriebe), nachrangig Gasketing (Gehäuse)
3. Gebiet: Baden-Württemberg (Ostfildern)
4. Sitz und Fertigungsort: Sitz Ostfildern (73760); "Neben dem Werk am Stammsitz in Ostfildern produziert Pilz auch in Betschdorf (Frankreich)" und Jintan (China) (S, Suchsnippet industrial-production.de). Fertigende Einheit für DE: Ostfildern.
5. Website: https://www.pilz.com
6. Was wird gebaut: Sicherheitsrelais PNOZ, Sicherheitsschaltgeräte, Sicherheitssensoren, Steuerungen, Antriebstechnik (S, pilz.com Suchsnippet "Safety relay/safety relays PNOZ"). Typisch vergossen/verklebt/gedichtet (A): Elektronikbaugruppen und Relais-Module (Block A/B), Sicherheitssensoren (Block A), Antriebselektronik/Servoverstärker (Block A), Gehäuse/Dichtungen (Block B). Welches Produkt in welchem Werk gefertigt wird, ist nicht belegt (PNOZ auch in Jintan und Betschdorf).
7. Fertigung DE/AT/NL: Hoch, Stufe S. Begründung: Familienunternehmen mit Produktions- und Logistikzentrum am Sitz Ostfildern laut Fachpresse-Snippet; mehrere Werke, daher V nötig (fehlt, nicht im Browser gelesen). Quelle laut Triage 2011-2014, Lehre 17: aktuelle Quelle fehlt.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Sicherheitsrelais/Elektronikbaugruppen, Sensoren, Antriebe; Produkttyp). Einzelbewertung: Sicherheitsrelais PNOZ Hoch (A), Sicherheitssensoren Hoch (A), Antriebselektronik Hoch (A), Steuerungen (Elektronikbaugruppen) Mittel (A), Gehäuse/Dichtungen Mittel (A).
9. Patentrecherche (Pflicht, mind. 2 Suchen):
- Suche 1: Websuche "Pilz Ostfildern Produktion Sicherheitsrelais PNOZ Vergussmasse Patent": Pilz selbst nennt Patent 1987 auf Not-Halt-Relais; kein Vergussmassen-Patent gefunden.
- Suche 2: Websuche "patents.google.com Pilz GmbH Anmelder Gehäuse Elektronik vergossen OR Vergussmasse OR potting": einziger Pilz-Treffer Designpatent D402965 "Modular housing for electrical circuits", Anmelder Pilz GmbH & Co (Justia, S, Jahr/Rechtsstand nicht geprüft), kein Verguss. Patente "Housing-side separating layer for the stress decoupling of potted electronics" (US 9622372): Anmelder im Snippet nicht genannt, nicht zuordenbar, nicht verwendet. Datenbank: Websuche, Google Patents/Espacenet/DEPATISnet nicht direkt abgefragt.
- Ergebnis: kein belegtes Verguss-Patent der Firma; kein Gegenbeweis.
10. Einstufung Tom: interessant (Fertigung Hoch S, Verguss Hoch A), mit Vorbehalt: Fertigungsbeleg nur Stufe S und alt
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "Pilz GmbH & Co. KG" und "Pilz": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Aktuelle V-Quelle (2025/2026) für Fertigung in Ostfildern (Produktseite, Standortseite pilz.com, Stellenanzeigen Elektronikfertigung/Montage Ostfildern) im Browser lesen; Impressum der Pilz GmbH & Co. KG lesen; wird in Ostfildern vergossen (Stellenanzeigen)? Patente Pilz (Anmelder-Schreibweise "Pilz GmbH & Co. KG") in Espacenet/DEPATISnet mit Vergussmasse-Suche nachholen. Aktion: Kandidat für Grün bei V-Beleg.
14. Quellen:
- https://www.industrial-production.de/steuerungstechnik/sicherheitsrelais-fuer-den-chinesischen-markt---pilz-eroeffnet-fertigung-in-jintan.htm (S, Suchsnippet): „Neben dem Werk am Stammsitz in Ostfildern produziert Pilz auch in Betschdorf“; Abruf 2026-10-15.
- https://www.computer-automation.de/safety-und-security/neues-produktions-und-logistikzentrum-eroeffnet.htm (S, aus Triage, nicht abgerufen): Produktions- und Logistikzentrum Ostfildern; Zitat aus Triage nicht selbst geprüft.
- https://www.pilz.com/en-LI/products/relay-modules/safety-relays-protection-relays (S, Suchsnippet): PNOZ Sicherheitsrelais; Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt (Familienunternehmen, Triage; nicht gesucht)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Pilz); Websuche "Pilz Anwenderbericht OR Referenz Dosieren Verguss Klebstoff Nordson OR Scheugenpflug OR DOPAG OR Henkel Ostfildern Fertigung Elektronik" (keine Treffer zu Pilz GmbH). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: stimmt weitgehend überein (S): Pilz GmbH & Co. KG, Ostfildern; Messeliste 73760 Ostfildern passt. Impressum/Register nicht gelesen. Gleichnamige Treffer (Dieter Pilz/Siemens, Pilzmittel) ausgeschlossen.

## 5. Pressluft Klefinghaus GmbH
1. Firma: Pressluft Klefinghaus GmbH (Messe: all about automation Düsseldorf 2026, Stand 415, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Steuerungs-/Schaltschrankbau, pneumatische/elektrische Antriebe), nachrangig Gasketing/Sealing (Hubtüren)
3. Gebiet: Rest Deutschland+Niederlande (Lüdenscheid, NRW)
4. Sitz und Fertigungsort: Lüdenscheid (58513), "owner-operated business ... 40 employees at the Luedenscheid site" (S, Messe-/Firmenprofil-Snippet). Fertigung der Hubtüren am Standort laut Eigenangabe (S).
5. Website: https://www.klefinghaus.de
6. Was wird gebaut: Händler (FESTO Official Partner, item, BOGE) mit Eigenfertigung: "KLEFINGHAUS designs, produces and distributes Lift Gates with pneumatic and electric actuators" (S, https://friedrichshafen.allaboutautomation.de/en/products/lift-gates), Steuerungstechnik-Abteilung seit 1978 (S), Druckluftsysteme. Typisch vergossen/verklebt/gedichtet (A): Antriebe (zugekaufte Festo-Komponenten, verbaut; Endprodukt-Regel), Steuerungen/Schaltschränke, Dichtungen an Hubtüren, Magnetventile (Block A). Eigener Schaltschrankbau nicht belegt (nur Messe-Kategorietags).
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Eigenfertigung Hubtüren am Sitz laut Eigenangabe (Snippet), aber überwiegend Händler (Ausschluss E2 nur bei fehlender Fertigung); Sitzregel greift nicht (Händler-Mischform).
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Magnetventile/Antriebe verbaut Mittel (A), Steuerungs-/Schaltschrankelektronik Mittel (A), Hubtür-Dichtungen Niedrig bis Mittel (A), Mechanik Niedrig (A).
9. Patentrecherche (Pflicht, mind. 2 Suchen):
- Suche 1: Websuche "Klefinghaus Hubtür Patent OR Gebrauchsmuster Anmelder Pressluft Klefinghaus GmbH": keine Patente oder Gebrauchsmuster des Anmelders gefunden.
- Suche 2: NICHT ausgeführt (Budget). Feld 9 UNVOLLSTÄNDIG: Google Patents/Espacenet/DEPATISnet Anmelder "Klefinghaus" nachholen.
- Ergebnis: keine Treffer gefunden; kein Gegenbeweis.
10. Einstufung Tom: prüfenswert (Fertigung Mittel S, Verguss Mittel A), mit Vorbehalt Händleranteil (E2)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "Pressluft Klefinghaus GmbH" und "Klefinghaus": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Welcher Anteil ist Eigenfertigung (Hubtüren, Steuerungsbau)? Steuerungstechnik-Broschüre 2024 (https://www.klefinghaus.de/download/steuerungstechnikbroschuere_2024-09.pdf) und Produktseiten lesen; Stellenanzeigen (Montage, Schaltschrankbau). Wenn überwiegend Handel: "kein Fertiger" an Tina.
14. Quellen:
- https://friedrichshafen.allaboutautomation.de/en/products/lift-gates (S, Suchsnippet/Messetext): "designs, produces and distributes Lift Gates with pneumatic and electric actuators"; Abruf 2026-10-15.
- https://www.klefinghaus.de/home.html und Steuerungstechnik-Broschüre (S, Suchsnippet): Abteilung Steuerungstechnik 1978, ca. 40 Mitarbeiter; Abruf 2026-10-15.
15. Größe/Umsatz: ca. 40 Mitarbeiter am Standort Lüdenscheid (Eigenangabe, S); Umsatz unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Klefinghaus); Websuche "Klefinghaus OR P+K Maschinen Dosieranlage OR Klebeanlage OR Vergussanlage Kunde Referenz Nordson OR Scheugenpflug OR DOPAG OR ViscoTec" (kein Hinweis auf Klefinghaus als Anwender). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: stimmt weitgehend überein (S): Pressluft Klefinghaus GmbH, Lüdenscheid (Firmenprofil-Snippet; Gründung 1937/1938 laut Quellen widersprüchlich). Impressum/Register nicht gelesen. Messeliste 58513 Lüdenscheid passt.

## 6. Printec-DS HMI Solutions*
1. Firma: Printec-DS HMI Solutions* (Messe: all about automation Düsseldorf 2026, Stand 435, Halle nicht angegeben; Sternchen und gemeinsamer Stand mit Pfannenberg*, Sitz in der Liste Wülfrath 42489)
2. Segment / Demak-Geschäftsbereich: Optical Bonding (Touch-Systeme/Displays, falls Bonding), Electrical Insulation (Tastatur-/Folienschalter-Elektronik), Gasketing/Sealing (IP65-Edelstahl-/Kunststofftastaturen)
3. Gebiet: Baden-Württemberg (Steißlingen)
4. Sitz und Fertigungsort: Zeppelinstraße 11, 78256 Steißlingen (S, embedded-world.de-Aussteller-Listing und MECSPE-Profil); "manufacturing sites in Germany and Taiwan / China" (S, Profil-Snippet). Welche Produkte in Steißlingen entstehen, ist nicht belegt.
5. Website: unbekannt (laut Snippet printecds.com, nicht verifiziert)
6. Was wird gebaut: "standard and customer-specific long-stroke keyboards, foil and silicone keyboards with special surfaces", Edelstahl-/Kunststofftastaturen "protect against dirt, moisture, vandalism", Touch-Systeme; Märkte Industrieautomation, Marine, Medizin, Selbstbedienung (S, embedded-world.de/MECSPE Snippets). Touch-Displays/Folientastaturen teils vom italienischen Partner Camax DS srl (S, MECSPE-Snippet). Typisch vergossen/verklebt/gedichtet (A): Folientastaturen (Verklebung/Laminat, Block B), Touch/Displays (Optical Bonding, Block B; Bonding bei Printec nicht belegt, Optical Bonding wird in den Treffern nur bei SCHURTER genannt), Elektronik-Tastaturen IP65 (Block B), Edelstahlgehäuse (Dichtung).
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Eigene Produkte, Sitz Steißlingen; Hinweise auf Fertigung auch in Taiwan/China und Zukauf von Displays in Italien (Hinweis auf Auslagerung), daher Sitzregel nicht anwendbar, V nötig (fehlt).
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Folientastaturen (Klebung) Mittel (A), Touch-Systeme/Displays Mittel (A, Optical Bonding unbelegt), Tastaturelektronik IP65 Mittel (A), Gehäuse Niedrig (A).
9. Patentrecherche (Pflicht, mind. 2 Suchen):
- Suche 1: Websuche "Printec-DS HMI Solutions Steißlingen Touch Folientastatur Optical Bonding Fertigung" (Produktsuche, kein Patenttreffer).
- Suche 2: Websuche "Printec-DS HMI Solutions GmbH Patent OR Gebrauchsmuster Folientastatur Verguss OR Dichtung": keine Patente oder Gebrauchsmuster gefunden. Hinweis: frühere Firmierung "PRINTEC DS Keyboard GmbH" (Vorgänger DS Keyboard Technic GmbH), unter diesen Namen nicht gesondert gesucht.
- Datenbank: Websuche, keine direkte Abfrage von Google Patents/Espacenet/DEPATISnet. Ergebnis: keine Treffer; kein Gegenbeweis.
10. Einstufung Tom: prüfenswert (Fertigung Mittel S, Verguss Mittel A)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "Printec-DS HMI Solutions" und "Printec": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Identität: Sitz Steißlingen oder Wülfrath, Stand-Partner Pfannenberg? Impressum der Firma lesen. (b) Wird in Steißlingen gefertigt (Folientastaturen, Montage) und bietet die Firma Optical Bonding an? Produkt-/Karriereseiten lesen. (c) Rolle von Camax DS srl (Italien). Patente unter "Printec DS Keyboard"/"DS Keyboard Technic" nachholen.
14. Quellen:
- https://www.embedded-world.de/en/exhibitors/printec-ds-hmi-solutions-gmbh-2461892 (S, Suchsnippet): „Zeppelinstraße 11“ Steißlingen, „input systems, touch systems, industrial keyboards“; Abruf 2026-10-15.
- https://mecspe.com/portal/en/printec-ds-hmi-solutions-gmbh (S, Suchsnippet): „manufacturing sites in Germany and Taiwan / China“; Camax DS srl; Abruf 2026-10-15.
- https://www.duesseldorf.allaboutautomation.de/en/exhibitors/printec-ds-hmi-solutions-247454/ (S, Messe-Beschreibungstext, Regel N5); Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Printec); Websuche "Printec-DS Folientastatur Klebstoff OR Dosieranlage OR Optical Bonding Lieferant Steißlingen Camax DS" (kein Hinweis auf Klebstoff-/Dosierlieferanten). Messe-Signal: keine Wettbewerber auf der aaa. Hinweis: Optical-Bonding-Treffer betrafen nur SCHURTER (andere Firma, nicht verwechseln).
17. Identität: ABWEICHUNG. Vorgabe "Printec-DS HMI Solutions*, 42489 Wülfrath". Gefunden: Printec-DS HMI Solutions GmbH, Zeppelinstraße 11, 78256 Steißlingen (S, embedded-world.de und MECSPE), früher PRINTEC DS Keyboard GmbH. Wülfrath nicht belegt. Registerauszug/Impressum nicht gelesen. Stand-Partner Pfannenberg* (Triage). Tina: Tabellenzeile 2, höchstens Gelb.

## 7. QuickMOVE GmbH
1. Firma: QuickMOVE GmbH (Messe: all about automation Düsseldorf 2026, Stand 716, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (dezentrale Antriebe, Motoren mit Elektronik, Sensorik), nachrangig Gasketing
3. Gebiet: Rest Deutschland+Niederlande (Köln laut Messeliste, NRW)
4. Sitz und Fertigungsort: Köln (50676) laut Messeliste (A/S); im Suchlauf nicht bestätigt (Messelisting nennt keine Stadt). Fertigungsort unbekannt.
5. Website: quick-move.de (laut Suchtreffer, nicht verifiziert)
6. Was wird gebaut: Fördersystem aus Aluminium-Strangprofil als Führungsbahn mit "Zügen" aus Trägern und Gelenkstangen, angetrieben durch "motors with toothed belts mounted decentrally on the guideway", SPS-Steuerung; QuickMOVE Evolution (kleiner, leichter, günstiger); Retail-Lösungen, Sondermaschinen (S, Messe-Produkttexte). Typisch vergossen/verklebt/gedichtet (A, Endprodukt-Regel): Antriebsmotoren und deren Elektronik (Block A), Sensorik/Endschalter (Block A), Steuerung/Netzteile (Block A/B), Kabel/Stecker (Block A). Ob die Antriebe selbst gefertigt oder zugekauft sind, ist unbelegt.
7. Fertigung DE/AT/NL: Mittel, Stufe ?. Begründung: Hersteller laut Messeeintrag (Kategorien Montagesysteme, Antriebstechnik, Sondermaschinenbau), aber Standort und Fertigungsort nicht belegt; Sitzregel nicht anwendbar, solange Köln unbestätigt.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: dezentrale Motoren/Antriebselektronik Mittel (A), Sensorik Mittel (A), Steuerung Mittel (A), Aluminiumprofil/Mechanik Niedrig (A).
9. Patentrecherche (Pflicht, mind. 2 Suchen):
- Suche 1: Websuche "QuickMOVE GmbH Patent Fördersystem Anmelder Google Patents": kein Patent mit Anmelder QuickMOVE; Treffer waren Fremdpatente (z. B. DE2014728A1, DE4439106C1), Anmelder nicht QuickMOVE, aussortiert.
- Suche 2: NICHT ausgeführt (Budget). Feld 9 UNVOLLSTÄNDIG: Google Patents/Espacenet/DEPATISnet Anmelder "QuickMove"/"Quick-Move"/"Quick MOVE" nachholen.
- Ergebnis: keine Treffer gefunden; kein Gegenbeweis.
10. Einstufung Tom: prüfenswert (Fertigung Mittel ?, Verguss Mittel A)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "QuickMOVE GmbH" und "Quick-Move": kein Treffer). Gleichnamige/ähnliche Firmen (Movinga, Quick Moove BE, UK-Firmen) ausgeschlossen.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Identität (Impressum quick-move.de, Handelsregister Köln), Fertigungsort (wer baut Profile, Antriebe, Steuerungen? Stellenanzeigen Montage), Antriebsmotoren selbst gefertigt? Patente vollständig nachholen.
14. Quellen:
- https://www.berlin.allaboutautomation.de/en/products/decentralised-drives-we-drive-the-conveyor-chains-with-a-toothed-belt-either-as-a-circulating-chain-or-as-in-the-case-of-the-railway-with-trains-what-do-you-need-233802/ (S, Messe-Produkttext, Regel N5): dezentrale Antriebe mit Zahnriemen; Abruf 2026-10-15.
- https://www.duesseldorf.allaboutautomation.de/en/exhibitors/quickmove-gmbh-223385/ (S, Suchsnippet): "QuickMOVE GmbH Stand: 716 Assembly systems ... Drive Technology"; Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag QuickMOVE); Websuche "QuickMOVE Evolution Hersteller Montage Köln Wettbewerber Klebstoff Dosieranlage ..." (kein Hinweis). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: NICHT belegt. Messeliste: QuickMOVE GmbH, 50676 Köln. Websuche fand weder Impressum noch Handelsregistereintrag noch die Stadt im Messelisting (Suche "QuickMOVE Köln Impressum ... Handelsregister" ohne Treffer zur Firma). Domain quick-move.de nur laut Triage.

## 8. R+W Antriebselemente GmbH
1. Firma: R+W Antriebselemente GmbH (Messe: all about automation Düsseldorf 2026, Stand 718, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Sensorkupplungen mit Elektronik), nachrangig Gasketing/Klebung (Kupplungs-Metallmechanik)
3. Gebiet: Bayern (Wörth am Main)
4. Sitz und Fertigungsort: Wörth am Main (63939) Hauptsitz, neues Gebäude "mit mehr Platz für Produktion und Verwaltung" (S, Suchsnippet); Töchter USA, China, Italien, Frankreich, Slowakei (S). Ein Verzeichnis nennt abweichend Klingenberg (PLZ 63929), Widerspruch ungeklärt.
5. Website: https://www.rw-kupplungen.de
6. Was wird gebaut: Präzisions- und Sicherheitskupplungen, Balgkupplungen, Lamellenkupplungen, Gelenkwellen; "intelligente Kupplung" mit integrierter Sensorik (misst Drehmoment, Drehzahl, Beschleunigung; interne Elektronik, Funk) (S, industrial-production.de-Snippets). "Mehr als 60.000 Kupplungen pro Jahr" (S). Typisch vergossen/verklebt/gedichtet (A): Sensor-/Elektronikmodul der intelligenten Kupplung (Block A/B, falls rotierend montiert vergossen), Metallbalgkupplungen mit Klemmnabe: laut Betriebsanleitung Klemmverbindung, kein Kleber (S); Verklebung Balg/Nabe nicht belegt.
7. Fertigung DE/AT/NL: Hoch, Stufe S. Begründung: Eigene Produkte, "develops and produces individual drive elements" (Stellenanzeigen-Snippet) am Sitz Wörth; Gruppe mit Auslandstöchtern (V nötig laut Sitzregel, fehlt), Auslagerung nicht gezielt geprüft.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Sensorik-Elektronik intelligente Kupplung Mittel (A), Balg-/Lamellenkupplungen Niedrig (A, Klemmverbindung belegt als Snippet), Gelenkwellen Niedrig (A), Sicherheitskupplungen (Mechanik) Niedrig (A).
9. Patentrecherche (Pflicht, mind. 2 Suchen):
- Suche 1: Websuche "R+W Antriebselemente GmbH Patent Kupplung Sensor Drehmoment Anmelder Espacenet": keine Patentdatenbank-Treffer, nur Fachpresse zur Sensorkupplung.
- Suche 2: NICHT ausgeführt (Budget). Feld 9 UNVOLLSTÄNDIG: Google Patents/Espacenet/DEPATISnet Anmelder "R+W Antriebselemente" mit Stichwörtern Sensor/Verguss nachholen.
- Ergebnis: keine Treffer gefunden; kein Gegenbeweis.
10. Einstufung Tom: prüfenswert (Fertigung Hoch S, Verguss Mittel A)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "R+W Antriebselemente GmbH" und "R+W": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Wird die Sensorkupplung (Elektronik) in Wörth gefertigt und wie ist das Sensormodul geschützt (vergossen, verklebt)? Produktseite "Intelligente Kupplung", Datenblatt, Stellenanzeigen Wörth (Montage, Elektronik). Aktuelle V-Quelle Fertigung Wörth. Widerspruch Wörth/Klingenberg im Impressum klären.
14. Quellen:
- https://www.industrial-production.de/antriebstechnik/integrierte-sensorik-ersetzt-drehmomentaufnehmer.htm (S, Suchsnippet): „R+W thereby offers an alternative to a torque transducer“; Abruf 2026-10-15.
- https://www.industrial-production.de/firma/r---w-antriebselemente-gmbh.htm (S, Suchsnippet): Hauptsitz „Wörth am Main“, Töchter US/CN/IT/FR/SK; Abruf 2026-10-15.
- https://bjg.cloud14.structpim.com/media/wwwn34kc/bk-mk-einbau-betriebsanleitung-de.pdf (S, Suchsnippet): Klemmverbindung Welle-Nabe; Abruf 2026-10-15.
15. Größe/Umsatz: über 250 bis über 300 Mitarbeiter (Verzeichnisangaben widersprüchlich, S)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag R+W); Websuche "R+W Kupplungen Klebstoff Balgkupplung Verklebung Henkel OR Loctite OR DELO OR 3M Anwender" (kein Hinweis auf Klebstofflieferanten, Klemmverbindung belegt). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: stimmt weitgehend überein (S): R+W Antriebselemente GmbH, Wörth am Main (industrial-production.de Firmenprofil); Messeliste 63939 passt. Abweichung in Verzeichnis: Klingenberg/PLZ 63929. Impressum/Register nicht gelesen.

## 9. red cable robots*
1. Firma: red cable robots* (Messe: all about automation Düsseldorf 2026, Stand 818, Halle nicht angegeben; Sternchen in der Liste, Sitz laut Liste Hoppstädten-Weiersbach 55768)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Winden-/Antriebselektronik), nachrangig E-Mobility/Sensorik (Randfall)
3. Gebiet: Rest Deutschland+Niederlande (Duisburg, NRW; Liste Hoppstädten-Weiersbach, Rheinland-Pfalz)
4. Sitz und Fertigungsort: Duisburg (Spin-off Uni Duisburg-Essen, S: uni-due.de, bouncewatch/Verzeichnis, KEBA-Success-Story "Duisburg start-up"). Fertigungsort: nicht belegt.
5. Website: unbekannt
6. Was wird gebaut: "industrial cable-driven robots for large workspaces" für Palettieren/Depalettieren, Bau, Logistik, Luftfahrt (Plattform an Seilen, Winden), Steuerung/Bedienung KEBA (S, https://www.keba.com/en/news/industrial-automation/success-story-red-cable, https://accelerator.high-tech.nrw/en/?p=1159). Typisch vergossen/verklebt/gedichtet (A): Winden-/Servoantriebe mit Elektronik (Block A, vermutlich zugekauft), Steuerung/HMI (zugekauft KEBA), Sensorik (Block A). Eigene Fertigung offen.
7. Fertigung DE/AT/NL: Mittel, Stufe ?. Begründung: Start-up (~5 Mitarbeiter laut Verzeichnis, S) mit Entwicklung/Team Duisburg; ob und wo gefertigt/montiert wird, unbekannt. Sitz unbestätigt.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Winden/Servoantriebe Mittel (A), Sensorik Mittel (A), Steuerung (zugekauft) Mittel (A), Seile/Mechanik Niedrig (A).
9. Patentrecherche (Pflicht, mind. 2 Suchen):
- Suche 1: Websuche "red cable robots GmbH Patent Seilroboter Anmelder Patent Cable robot": kein Patent der Firma; EP4066337 "Seilroboter ... Stromleitung" Anmelder nicht erkennbar, nicht zugeordnet, nicht verwendet.
- Suche 2: NICHT ausgeführt (Budget). Feld 9 UNVOLLSTÄNDIG: Google Patents/Espacenet/DEPATISnet Anmelder "red cable robots" nachholen.
- Ergebnis: keine Treffer gefunden; kein Gegenbeweis.
10. Einstufung Tom: prüfenswert (Fertigung Mittel ?, Verguss Mittel A), schwach: Start-up, Fertigung offen
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "red cable robots" und "red cable robots GmbH": kein Treffer). Hinweis: KEBA Group AG [AT/DE] und KEBA Industrial Automation Germany GmbH [DE] stehen im CRM (bekannte_firmen_DE-AT-NL.txt Zeilen 1273-1274); KEBA ist nur Steuerungs-Lieferant von red cable robots, kein Konzernbezug, daher kein CRM-Bezug der Firma.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Identität: Handelsregister, Impressum (red cable robots GmbH, Sitz Duisburg oder Hoppstädten-Weiersbach?). (b) Wo werden Winden/Plattform gefertigt oder montiert (Eigenfertigung oder Lohnfertiger)? (c) Patente nachholen.
14. Quellen:
- https://www.keba.com/en/news/industrial-automation/success-story-red-cable (S, Suchsnippet): „Red Cable Robots, a Duisburg start-up“, KEBA-HMI, Palettieren; Abruf 2026-10-15.
- https://accelerator.high-tech.nrw/en/?p=1159 (S, Suchsnippet): „industrial cable-driven robots for large workspaces“; Ausgründung Uni Duisburg-Essen; Abruf 2026-10-15.
- https://www.uni-due.de/guide/team_redcablerobots.php (S, Suchsnippet); Abruf 2026-10-15.
15. Größe/Umsatz: rund 5 Mitarbeiter, gegründet 2023 (Verzeichnis bouncewatch, Sekundärquelle, S)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag); Websuche "red cable robots KEBA Success Story Steuerung Seilroboter Palettieren Hersteller Windenfertigung" (nur Steuerungs-Lieferant KEBA, keine Dosier-/Klebe-Wettbewerber). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: ABWEICHUNG. Vorgabe "red cable robots*, 55768 Hoppstädten-Weiersbach". Gefunden: red cable robots GmbH, Duisburg (S, Uni-Spin-off, KEBA-Story). Hoppstädten-Weiersbach nicht belegt (Suche ohne Treffer). Impressum/Register nicht gefunden. Tina: Tabellenzeile 2.

## 10. REFACTUM GmbH
1. Firma: REFACTUM GmbH (Messe: all about automation Düsseldorf 2026, Stand 412, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: unbekannt (laut Triage evtl. Retrofit/Automation, nicht belegt)
3. Gebiet: Rest Deutschland+Niederlande (Kaiserslautern laut Messeliste, nicht belegt)
4. Sitz und Fertigungsort: Kaiserslautern (67663) laut Messeliste; Firma per Suche nicht auffindbar. Fertigungsort unbekannt.
5. Website: unbekannt
6. Was wird gebaut: unbekannt. Keine Angabe gefunden; "Retrofit/Automation" ist nur Vermutung der Triage (?). Typisch vergossene Teile: nicht ableitbar.
7. Fertigung DE/AT/NL: Niedrig, Stufe ?. Begründung: keine Informationen; angenommen, nicht belegt.
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe ? (kein Produkt bekannt). Einzelbewertung nicht möglich.
9. Patentrecherche (Pflicht, mind. 2 Suchen):
- Suche 1: Websuche "REFACTUM GmbH Kaiserslautern": kein Treffer zur Firma (weder Website noch Register).
- Suche 2: Websuche "Refactum Retrofit Automation Kaiserslautern": kein Treffer zur Firma.
- Beide Suchen waren Identitäts-/Firmensuchen; eine Patent-Datenbankabfrage (Google Patents/Espacenet/DEPATISnet, Anmelder "Refactum") wurde NICHT ausgeführt. Feld 9 UNVOLLSTÄNDIG: nachholen.
- Ergebnis: keine Patente gefunden; kein Gegenbeweis.
10. Einstufung Tom: kein Fertiger (vorläufig; Firma nicht auffindbar, Identität nicht belegt, Tina entscheidet)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "REFACTUM GmbH": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Identität: Existiert REFACTUM GmbH in Kaiserslautern (Handelsregister, Messeprofil im Browser unter https://www.duesseldorf.allaboutautomation.de, Schreibvarianten "Refactum", "Re-Factum")? Was bietet die Firma an? Aktion: nicht kontaktieren, bis Identität und Produkt geklärt.
14. Quellen:
- https://www.duesseldorf.allaboutautomation.de (Messeliste, Datei aaa_duesseldorf_2026.csv): „REFACTUM GmbH;412;67663;Kaiserslautern“; 2026-10-15.
- Websuche "REFACTUM GmbH Kaiserslautern" und "Refactum Retrofit Automation Kaiserslautern": keine Treffer zur Firma; 2026-10-15.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag); keine eigene Websuche möglich, da Firma/Produkt unbekannt (Suchen zu Firma ohne Treffer, siehe Feld 9). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: NICHT belegt. Firma weder auffindbar noch durch Website, Impressum oder Register bestätigt. Nur Messeliste (67663 Kaiserslautern). Tina: Tabellenzeile 2, Gelb "Auftrag Identität".

## nicht aufgenommen (bereits bekannt / unklar)
Keine der 10 Firmen ist im CRM BEKANNT (crm_abgleich.py je Firma und Konzern-/Altname ausgeführt, kein Treffer). Vermerke:
- red cable robots: kein Bezug, aber KEBA Group AG [AT/DE] und KEBA Industrial Automation Germany GmbH [DE] stehen im CRM (Lieferant der Steuerung, nicht Konzern).
- Peakboard GmbH: ehemals Theobald Software (kein CRM-Treffer).
- Pfannenberg* und Printec-DS HMI Solutions*: Sitz laut Liste Wülfrath widerspricht den Funden (Hamburg bzw. Steißlingen), Identität offen.
Anzahl BEKANNT: 0.

## Einschränkungen
- WebFetch und Chrome standen nicht zur Verfügung (erwartet). Daher keine Stufe-V-Aussage in diesem Batch, kein Browser-Gegenlesen (Regel H), keine Impressum-Volltexte gelesen. Alle Belege sind Suchsnippets (S) oder Ableitungen aus Produkttyp (A); Tina muss jede tragende Aussage im Browser nachlesen.
- Websuche-Budget: genau 30 Standard-Websuchen, ca. 3 je Firma. Die Patentrecherche (F5) ist für KEINE Firma vollständig: Google Patents, Espacenet und DEPATISnet wurden nie direkt abgefragt, sondern nur per Websuche (Justia-Treffer bei Pfannenberg und Pilz). Zwei getrennte Patentsuchen wurden nur für Pfannenberg, Pilz und Printec-DS ausgeführt (dort Websuche, nicht Datenbank). Bei P+K, Peakboard, Pressluft Klefinghaus, QuickMOVE, R+W und red cable robots lief nur eine Patentsuche, bei REFACTUM nur Firmensuchen. Das Feld 9 ist dort ausdrücklich UNVOLLSTÄNDIG; ein "keine Treffer" ist kein Gegenbeweis. Vorgänger-/Altnamen (PRINTEC DS Keyboard, DS Keyboard Technic) und Konzernvarianten wurden nicht gesondert gesucht. Rechtsstand der Justia-/Design-Patente nicht geprüft.
- Wettbewerbereinsatz (Feld 16): je Firma maximal eine Websuche plus Abgleich mit wettbewerber_referenzen.md (Grep nach den Firmennamen: kein Eintrag, da die Referenzliste Wettbewerber-Kunden nur unvollständig enthält). Für P+K, Peakboard, Pressluft Klefinghaus, QuickMOVE, REFACTUM wurden die Wettbewerbersuchen mit anderen Firmen kombiniert (Sammelabfragen) und sind daher schwächer. "Kein Hinweis" ist kein Gegenbeweis. Messe-Signal per Grep vollständig.
- Fertigung (Feld 7) und Identität (Feld 17) für fast alle Firmen nur Stufe S oder ?. Bei Pilz, Pfannenberg, R+W und Printec-DS (Konzerne/mehrere Werke bzw. Hinweise auf Auslandsfertigung) wäre Stufe V nötig und fehlt. Sitz-Abweichungen zur Messeliste bei Pfannenberg*, Printec-DS*, red cable robots* nicht aufgelöst; REFACTUM und P+K ohne auffindbare Website; QuickMOVE-Standort unbestätigt.
- Größe/Umsatz nur nebenbei aus Suchsnippets (Feld 15). Triage-Angaben (Typ, Sitz, Bauteilpotenzial) wurden nicht als Beleg übernommen, sondern als Stufe A/S gekennzeichnet; Produkttyp-Ableitungen (Stufe A) sind Einschätzungen aus der Wissensbasis, nicht Fakten.
- Keine Suche nach Ansprechpartnern, E-Mail-Adressen oder Kontaktformularen (Regel K). Nicht committet.
