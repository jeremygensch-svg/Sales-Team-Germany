# Tom Batch 02 – all about automation Düsseldorf 2026 (aaa, Stand der Liste laut Triage)
Erstellt: 2026-10-15 (Tom, Stufe 1, Version 2, Messemodus Regel N). Eingabe: aaa_batches_v2/pruef_01.md, 10 Firmen. Halle ist in der Liste nicht angegeben, Feld 1 trägt nur die Standnummer. Sitz-/Stand-Hinweise der Triage sind unverifiziert übernommen und in Feld 17 geprüft.
Alle Abrufdaten: 2026-10-15. Belegstufen: V = selbst gelesen (Seite im Browser/Original), S = nur Suchsnippet oder Kurzfassung (Seite nachlesen), A = aus Produkttyp abgeleitet, ? = angenommen.
WICHTIG zur Belegtiefe: In diesem Lauf waren WebFetch (DNS-Fehler "ENOTFOUND" auf allen Hosts) und die Chrome-Werkzeuge (mcp__claude-in-chrome__*: "Browser nicht verfügbar") NICHT nutzbar, und das WebSearch-Budget (200 Aufrufe je Turn, geteilt mit anderen Agenten) war nach rund 30 Abfragen erschöpft. Alle Aussagen stützen sich deshalb ausschließlich auf Suchsnippets bzw. Suchzusammenfassungen: keine einzige Aussage ist Stufe V. Kein Impressum wurde selbst gelesen. Details unter "Einschränkungen".
Messe-Signal (Regel N2): Grep auf aaa_duesseldorf_2026.csv (Wettbewerber-Namen aus Regel E1 und Wissensbasis D: Scheugenpflug, DOPAG, ViscoTec, Nordson, bdtronic, RAMPF, Sonderhoff, Hilger u. Kern, Musashi, Marco, GONANO, Henkel, DELO, Elantas, Wacker, Sika, Panacol, Lohmann, OTTO-CHEMIE, Hexion, EPOXONIC, WEVO, Atlas Copco, Graco, Dymax, 3M u. a.): kein Wettbewerber in der Ausstellerliste. Der einzige Rohtreffer (Panasonic Industry Europe GmbH, Stand 314, Ottobrunn) entstand nur durch die Zeichenfolge "otto" in "Ottobrunn" und ist kein Wettbewerber im Sinne von E1.
CRM-Abgleich: crm_abgleich.py je Firma mit Firmen-, Konzern- und Schreibvarianten ausgeführt (2026-10-15). Ergebnis: kein Treffer für alle 10 Firmen und ihre Konzernnamen (Asyril SA, CPA, AUTEC Gruppe, BluhmWeber, Berghof Group, Camozzi Group, Benedict, BWH). Einziger Rohtreffer: Suchbegriff "Weber Marking Systems" (Marke der BluhmWeber-Gruppe) fand "Weber GmbH & Co. KG [DE]" (Zeile 2549) und "Weber Elektronik GmbH [DE]" (Zeile 2548) in bekannte_firmen_DE-AT-NL.txt: nur Präfix/gleiche Wortwurzel "Weber", keine erkennbare Verbindung zu BluhmWeber; unklar, nicht als CRM-Konzernbezug gewertet (Tina/Jey bei Bedarf prüfen). Anzahl BEKANNT: 0.

## 1. Asyril GmbH
1. Firma: Asyril GmbH (Messe: all about automation Düsseldorf 2026, Stand 524, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Antriebs-/Vibrationselektronik, Steuerungen), nachrangig Optical-/Kameramodule
3. Gebiet: Baden-Württemberg (GmbH in Offenburg); Hersteller-Mutter außerhalb (Schweiz)
4. Sitz und Fertigungsort: Asyril GmbH, Max-Planck-Straße 1, Offenburg = Technikzentrum/Showroom seit Oktober 2023 (S). Fertigende Einheit laut Snippets: Asyril SA, Z.I. du Vivier 22, 1690 Villaz-St-Pierre (Schweiz). Fertigung der Asycube in Offenburg: nicht belegt.
5. Website: https://asyril.com
6. Was wird gebaut -> Bauteile: Flexible Zuführsysteme (Asycube-Vibrationsplattformen, Asyfeed, EYE+ Steuerung) für Teile von 0,1 bis 150 mm (S). Typisch vergossen/verklebt/gedichtet (A, abgeleitet aus Produkttyp): Antriebs-/Vibrationselektronik (Piezo-/Spulenantriebe) Mittel, Steuerungen Mittel, Kameramodule Niedrig bis Mittel, Gehäuse/Dichtungen Niedrig. Kein direkter Beleg.
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Offenburg ist laut Snippet ein Technikzentrum mit Showroom und Machbarkeitstests; Snippet "develops, produces and markets" bezieht sich auf die Schweizer Asyril SA. Konzern-/Tochterfall, daher wäre Stufe V nötig; sie fehlt. Nachzulesen: https://asyril.com/news/strengthened-presence-in-germany/.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A (Einschätzung aus Produkttyp: Antriebselektronik der Vibrationsplattform, Steuerung). Einzelbewertung: Vibrationsantrieb/Elektronik Mittel (A), Steuerung/Controller Mittel (A), Kameramodul Niedrig (A), Gehäusedichtung Niedrig (A). Kein Gegenbeleg gefunden.
9. Patentrecherche (Pflicht): Datenbanken Google Patents, Espacenet, DEPATISnet; direkter Datenbankzugriff war nicht möglich, die Abfragen liefen nur als Websuche (Suchmaschinen-Snippets), daher schwacher Befund.
- Websuche 1: "site:patents.google.com Asyril SA feeding vibration platform patent" (Google Patents): kein Treffer auf patents.google.com; Produktseiten nennen ein "patentiertes" 3-Achsen-Vibrationssystem (Forschung Northwestern, Lynch-Labor) (Stufe S), Nummern nicht ermittelt.
- Websuche 2: "Asyril SA Patent Vergussmasse OR potting OR encapsulation OR Dichtung Espacenet DEPATISnet": 0 Treffer mit Anmelder Asyril; angezeigte Patente (US6355881B1, US10834827B2 Hella u. a.) gehören anderen Anmeldern und werden nicht gezählt.
- Ergebnis: Anzahl Verguss-Patente von Asyril: 0 gefunden; Anmelder-Varianten (Asyril SA, Asyril GmbH) nicht direkt in den Datenbanken abgefragt. Schweizer Mutter: Rechtsstand nicht prüfbar. LÜCKE: Direktabfrage Google Patents/Espacenet/DEPATISnet fehlt.
10. Einstufung Tom: kein Fertiger (Offenburg: Technikzentrum/Showroom, Fertigung vermutlich Schweiz, Stufe S; harter Ausschluss E3 möglich, entscheidet Tina)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py: "Asyril GmbH", "Asyril SA", "CPA": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag an Tina): Wird die Asycube (Vibrationsplattform, Elektronik) in Offenburg montiert oder nur in Villaz-St-Pierre (CH)? Asyril-News und Karriereseite, Impressum der Asyril GmbH lesen; Stellenanzeigen Offenburg (Montage/Produktion?). Zugehörigkeit zur CPA-Gruppe (laut Triage, industrial-production.de) belegen. Aktion: nicht kontaktieren, bis Fertigungsort DE belegt.
14. Quellen:
- https://asyril.com/news/strengthened-presence-in-germany/ (S, Suchsnippet, nicht selbst gelesen): „opened Asyril GmbH in Offenburg in October 2023 as a new technical center“ (sinngemäß aus Suchzusammenfassung); Abruf 2026-10-15.
- https://onlineinfo.ch/company/asyril-sa---che-113-748-605/pdf (S): „develops, produces and markets high-performance flexible feeding systems“ (Suchzusammenfassung); Abruf 2026-10-15.
- https://www.db.cleanmanufacturing.fraunhofer.de/en/manufacturer/1075 (S): Asyril SA, Z.I. du Vivier 22, 1690 Villaz-St-Pierre; Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep Asyril/CPA: kein Eintrag). Einzelsuche nach Wettbewerber-Anlagen/-Massen bei Asyril NICHT ausgeführt (WebSearch-Budget erschöpft). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: teilweise belegt (S). Triage: Asyril GmbH Offenburg, Mutter Asyril SA (CH). Snippets: Asyril SA, Z.I. du Vivier 22, 1690 Villaz-St-Pierre, UID CHE-113.748.605, AG, Stammkapital CHF 500.000 (onlineinfo.ch); Eintrag einer Asyril GmbH im Handelsregister Offenburg nicht gefunden. Impressum/Register der GmbH nicht gelesen. Messeliste: 77656 Offenburg, passt zum Showroom. Abweichung: Fertigende Einheit ist die Schweizer Mutter, nicht die gelistete GmbH.

## 2. ATEG Automation GmbH
1. Firma: ATEG Automation GmbH (Messe: all about automation Düsseldorf 2026, Stand 123, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Bedienterminals/HMI-Elektronik), nachrangig Gasketing/Sealing (Folientastaturen, Gehäuse)
3. Gebiet: Rest Deutschland+Niederlande (Remscheid, NRW)
4. Sitz und Fertigungsort: Intzestraße 50, 42859 Remscheid (Verzeichnisse, S). Fertigungsort: nicht belegt.
5. Website: https://www.ateg.de
6. Was wird gebaut -> Bauteile: Verzeichnis nennt Industrieterminals und -tastaturen, Digital-Anzeigegeräte, Tastenschalter, Folientastaturen, Bedienterminals/HMI (S). Gegründet 1995 als Vertriebsgesellschaft für Komponenten der Automatisierungstechnik, Zweck laut einem Verzeichnis Handel mit Steuerungs-, Mess- und Regelkomponenten (S). Ob eigene Produkte gefertigt werden: unbekannt. Falls eigen: HMI-Elektronik und Folientastaturen (A) mit Dichtung/Verklebung typisch Mittel.
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Gründung als Vertriebsgesellschaft, Zweck Handel, keine Quelle für Eigenfertigung; Sitzregel nicht anwendbar, solange nicht als Gerätebauer belegt.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A (Einschätzung aus Produkttyp, nur falls Eigenfertigung). Einzelbewertung: Bedienterminal-Elektronik Mittel (A), Folientastatur (Verklebung/Dichtung) Mittel (A), Gateways Niedrig (A), Beratung/Handelsware Niedrig (A).
9. Patentrecherche (Pflicht): Datenbanken Google Patents, Espacenet, DEPATISnet; nur über Websuche abgefragt, keine Direktabfrage.
- Websuche 1: "site:patents.google.com "ATEG Automation" OR "Ateg Automation GmbH" Folientastatur Bedienterminal" (Google Patents): keine Patente mit Anmelder ATEG. Fremde Treffer (DE10321663A1 Bedientafel; EP0803887A3 Folientastatur, Würth Elektronik) nicht zugeordnet.
- Websuche 2: "ATEG Automation Remscheid Patent Gebrauchsmuster DEPATISnet Espacenet Anmelder": keine Patent-/Gebrauchsmusterdatensätze.
- Ergebnis: 0 Treffer gefunden; Datenbanken nicht direkt abgefragt, "keine Treffer" ist kein Gegenbeweis. LÜCKE: Direktabfrage fehlt.
10. Einstufung Tom: unwahrscheinlich (Fertigung Niedrig; möglicherweise kein Fertiger, falls reine Vertriebsgesellschaft, siehe Nachrecherche)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "ATEG Automation GmbH": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag an Tina): Fertigt ATEG eigene Terminals/Tastaturen in Remscheid oder handelt/konfektioniert ATEG nur? Website-Produktseiten (Eigenmarke?) und Impressum lesen, Stellenanzeigen (Montage/Produktion) prüfen. Ergibt sich nur Handel: "kein Fertiger" (E2). Aktion: nicht kontaktieren.
14. Quellen:
- https://www.it-in-germany.de/firma/ATEG+Automation+GmbH/5016098/3569/eng (S, Suchsnippet): „Industrieterminals und -tastaturen, Digital-Anzeigegeräte, Tastenschalter, Folientastaturen“ (Suchzusammenfassung); Abruf 2026-10-15.
- https://implisense.com/en/companies/ateg-automation-gmbh-remscheid-DE9MF19TTQ18 (S): „ATEG Automation GmbH“ Remscheid; Abruf 2026-10-15.
- https://www.duesseldorf.allaboutautomation.de/en/exhibitor/ateg-automation-gmbh/ (S, Messeprofil, Regel N5): Eintrag vorhanden; Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep ATEG: kein Eintrag). Einzelsuche NICHT ausgeführt (WebSearch-Budget erschöpft). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: teilweise belegt (S, Verzeichnis, Impressum nicht gelesen): ATEG Automation GmbH, Intzestraße 50, 42859 Remscheid, laut Verzeichnis HRB 11800 Amtsgericht Wuppertal, Geschäftsführung Stefan Glaubitz. Messeliste 42859 Remscheid passt. Keine Abweichung erkennbar, Quelle aber nur Verzeichnis.

## 3. Autec Sondermaschinenbau GmbH
1. Firma: Autec Sondermaschinenbau GmbH (Messe: all about automation Düsseldorf 2026, Stand 226, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation / E-Mobility Potting (Endprodukt: Montage-/Prüfautomaten mit verbauten Antrieben, Sensorik, Steuerungen); Kundenbranchen Automotive/Elektro/Medizin
3. Gebiet: Bayern (Amberg)
4. Sitz und Fertigungsort: Amberg, An den Franzosenäckern 11, 92224 Amberg (ProvenExpert, Bayern International, S). Fertigende Einheit: AUTEC Sondermaschinenbau GmbH (Teil der inhabergeführten AUTEC Gruppe, Hauptsitz Amberg, S).
5. Website: https://www.autec-gmbh.de (laut Triage unbestätigt; nicht geprüft)
6. Was wird gebaut -> Bauteile: Sondermaschinen für Montage, Prüfen, Zuführtechnik (Wendelförderer), Roboterzellen, Lasermarkieren; "cutting, joining, measuring, testing and marking" (S, Messeprofil). Typisch vergossen/verklebt/gedichtet (A, Endprodukt-Regel Maschinen): verbaute Antriebe/Servomotoren, Sensorik, Steuerungselektronik, Kabel/Stecker, Magnete. Eigenverguss nicht belegt.
7. Fertigung DE/AT/NL: Mittel, Stufe A. Begründung: Sondermaschinenbauer mit erkennbarem Standort Amberg, gegründet 1990 (Bayern International, S); Sitzregel würde Stufe A genügen, aber die AUTEC Gruppe hat mehrere Einheiten (Konzernfall, V nötig), und die Zuordnung der GmbH zur Gruppe ist nicht geklärt.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A (Einschätzung aus Produkttyp, Endprodukt-Regel). Einzelbewertung: Servoantriebe/Motoren Mittel (A), Sensorik Mittel (A), Steuerungs-/Schaltschrankelektronik Mittel (A), Kabelkonfektion Mittel (A), Rahmen/Mechanik Niedrig (A). Kein Hinweis auf Eigenverguss.
9. Patentrecherche (Pflicht): Datenbanken Google Patents, Espacenet, DEPATISnet; nur über Websuche, keine Direktabfrage.
- Websuche 1: "site:patents.google.com AUTEC Sondermaschinenbau Amberg Patent" (Google Patents): kein Patent mit Anmelder AUTEC. Einziger Google-Patents-Treffer (AT6726B) gehört einem anderen Anmelder (Vereinigte Maschinenfabrik Augsburg) und wird nicht gezählt.
- Websuche 2: ""Autec Sondermaschinenbau" Anmelder Patent Espacenet DEPATISnet Vergussmasse OR Verguss OR Kleben OR Dichtung": keine Patentdatensätze, nur Firmenprofile und Dritte (SM Klebetechnik, Sonderhoff).
- Ergebnis: 0 Treffer gefunden, Anmelder-Varianten (AUTEC GmbH, AUTEC Gruppe) nicht direkt abgefragt. LÜCKE: Direktabfrage fehlt.
10. Einstufung Tom: prüfenswert (Fertigung Mittel A, Verguss Mittel A, kein Niedrig)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "Autec Sondermaschinenbau GmbH", "AUTEC Gruppe": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag an Tina): (a) Fertigung am Sitz Amberg belegen: Montage-/Produktionsstellen (Elektriker, Monteur) oder Standortseite der AUTEC Gruppe lesen. (b) Welche Einheit der AUTEC Gruppe ist die GmbH (Gruppe mehrere Gesellschaften?). (c) Adresse klären (siehe Feld 17). (d) Wird Schaltschrank-/Elektronikbau mit Dichten/Kleben im Haus gemacht? Aktion: nicht kontaktieren.
14. Quellen:
- https://bayern-international.de/en/company-database/company-details/autec-sondermaschinenbau-gmbh-16594 (S, Suchsnippet): „Autec Sondermaschinenbau GmbH“, An den Franzosenäckern 11, Amberg, gegründet 1990, DIN EN ISO 9001; Abruf 2026-10-15.
- https://allaboutautomation.de/en/?p=332240 (S, Messeprofil, Regel N5): „cutting, joining, measuring, testing and marking“ (Suchzusammenfassung); Abruf 2026-10-15.
- https://www.provenexpert.com/autec-sondermaschinenbau-gmbh/ (S): Adresse An den Franzosenäckern 11, 92224 Amberg; Abruf 2026-10-15.
15. Größe/Umsatz: ca. 40 Mitarbeiter laut Triage (Bayern International, S, nicht erneut geprüft)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep Autec: kein Eintrag); Websuche ""Autec Sondermaschinenbau" ... Vergussmasse OR Verguss OR Kleben OR Dichtung" (Treffer nur zu Sonderhoff/SM Klebetechnik allgemein, ohne Autec-Bezug). Referenzsuche mit Wettbewerbernamen NICHT ausgeführt (Budget erschöpft). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: ABWEICHUNG/unklar (S). Triage: Autec Sondermaschinenbau GmbH, Amberg. Snippets: Adresse An den Franzosenäckern 11, 92224 Amberg (ProvenExpert, Bayern International). Registerdienst OpenRegister-Snippet nennt dagegen unter dem verkürzten Namen "Sondermaschinenbau GmbH" die Adresse Oskar-von-Miller-Straße 7, 92224 Amberg (HRA/HRB-Einträge, Datum 28.08.2026, widersprüchlich, unzuverlässig). Es kann sich um eine Schwester/Neugründung handeln. Impressum/Register nicht gelesen. Ampel höchstens Gelb (Tabellenzeile 2), bis Jey/Tina die Einheit bestätigt.

## 4. Bahrmann GmbH
1. Firma: Bahrmann GmbH (Messe: all about automation Düsseldorf 2026, Stand 239, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Sensorik, Ex-Schutz-Systeme) – nur falls Eigenfertigung
3. Gebiet: Baden-Württemberg (Gärtringen)
4. Sitz und Fertigungsort: Max-Planck-Straße 34, 71116 Gärtringen (Verzeichnis, S). Fertigungsort: nicht belegt.
5. Website: https://www.bahrmann.de (laut Triage unbestätigt; nicht geprüft)
6. Was wird gebaut -> Bauteile: Systemanbieter für Messtechnik (Schwingungs-, Drehzahl-, Drehmoment-, Wegmessung, Ex-Schutz). Portfolio enthält Produkte der Vertriebspartner METRIX (USA), Ono Sokki (Japan), Dr. E. Horn (DE) (S). Eigene Produkte: nicht belegt. Falls Systeme zusammengestellt werden: Sensorik/Ex-Schutz-Elemente sind Block A (A), kommen aber von Partnern.
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Selbstbeschreibung "system provider" mit Vertriebspartnern; keine Quelle für Eigenfertigung; Sitzregel nicht anwendbar, da Händler-/Systemhauscharakter nicht ausgeschlossen.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A (bedingt: Sensorik/Ex-Schutz-Systeme, nur bei Eigenfertigung/Systemaufbau). Einzelbewertung: Vibrations-/Drehzahlsensoren (Partnerware) Hoch (A, nicht eigen), Ex-Schutz-Auswertegeräte Mittel (A), Systemintegration/Schaltschrank Mittel (A), Beratung Niedrig (A). Gewicht gering wegen fehlender Fertigung.
9. Patentrecherche (Pflicht): Datenbanken Google Patents, Espacenet, DEPATISnet; nur über Websuche.
- Websuche: "Bahrmann GmbH Gärtringen Patent Anmelder Google Patents Espacenet DEPATISnet": keine Patentdatensätze; fremde Treffer (EP0105123, Archivportal) nicht zugeordnet.
- Ergebnis: 0 Treffer gefunden; nur eine Websuche, zweite Abfrage (Direktabfrage Espacenet/DEPATISnet) nicht möglich. LÜCKE: Patentrecherche unvollständig (Regel F5 verlangt zwei getrennte Suchen).
10. Einstufung Tom: unwahrscheinlich (Fertigung Niedrig; möglicherweise kein Fertiger/Händler)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "Bahrmann GmbH": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag an Tina): Entwickelt/fertigt Bahrmann eigene Messsysteme/Ex-Schutz-Geräte in Gärtringen oder wird nur vertrieben (Partnerprodukte)? Website-Produktseiten und Stellenanzeigen (Montage/Produktion) lesen. Nur Handel: "kein Fertiger" (E2). Aktion: nicht kontaktieren.
14. Quellen:
- https://www.diedeutscheindustrie.de/firma/bahrmann%20gmbh%20bahrmann%20gmbh/4055365/55552/eng (S, Suchsnippet): „system provider for industrial measurement technology“ und „distribution partners METRIX / USA, Ono Sokki / Japan“; Abruf 2026-10-15.
- https://friedrichshafen.allaboutautomation.de/en/?p=494110 (S, Messeprofil, Regel N5): Bahrmann GmbH, Messtechnik; Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt (gegründet 1980 laut Verzeichnis, S)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep Bahrmann: kein Eintrag). Einzelsuche NICHT ausgeführt (Budget erschöpft). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: teilweise belegt (S, Verzeichnis, Impressum nicht gelesen): Bahrmann GmbH, Max-Planck-Straße 34, 71116 Gärtringen, laut Verzeichnis HRB 241415 Amtsgericht Stuttgart, Geschäftsführung M. Janssen. Messeliste 71116 Gärtringen passt. Keine Abweichung erkennbar.

## 5. BAT Maschinenbau GmbH
1. Firma: BAT Maschinenbau GmbH (Messe: all about automation Düsseldorf 2026, Stand 418, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation / E-Mobility Potting (Endprodukt: Zuführ-/Montagemaschinen mit verbauten Antrieben, Sensorik, Steuerungen)
3. Gebiet: Rest Deutschland+Niederlande (Meinerzhagen, NRW)
4. Sitz und Fertigungsort: BAT Maschinenbau GmbH, Darmcher Grund 5, 58540 Meinerzhagen (Verzeichnis cylex/implisense, S). Fertigende Einheit: dieselbe (Sondermaschinenbauer, kein Konzern erkennbar).
5. Website: https://www.batmaschinenbau.de
6. Was wird gebaut -> Bauteile: Sondermaschinen, Zuführtechnik (Schraub-/Mutternzuführung), Montageautomaten, Rundtische, Bildverarbeitung, Laserbeschriftung; Branchen Automotive/E-Mobility/Medizin (S, Messeprofil, "manufactures high-performance industrial feeders"). Typisch vergossen/verklebt (A, Endprodukt-Regel Maschinen): verbaute Antriebe, Sensorik, Steuerungselektronik, Kabel/Stecker. Eigenverguss nicht belegt.
7. Fertigung DE/AT/NL: Hoch, Stufe A (Sitzregel: Maschinenbauer mit erkennbarem Standort, eigene Produkte, kein Händler, kein Konzern, keine Hinweise auf Auslagerung). Begründung: Gründung 1999 durch Jörg Biermann (industrial-production.de, S); Messeprofil "manufactures ... feeders" (S).
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A (Einschätzung aus Produkttyp). Einzelbewertung: Antriebe/Motoren Mittel (A), Sensorik Mittel (A), Steuerungselektronik Mittel (A), Zuführelektronik/Wendelförder-Steuerung Mittel (A), Rahmen/Mechanik Niedrig (A).
9. Patentrecherche (Pflicht): Datenbanken Google Patents, Espacenet, DEPATISnet; nur über Websuche.
- Websuche: ""BAT Maschinenbau" Meinerzhagen Patent OR Gebrauchsmuster Anmelder Google Patents Espacenet DEPATISnet": keine Patent-/Gebrauchsmusterdatensätze, nur Firmenlisten und allgemeine Artikel.
- Ergebnis: 0 Treffer gefunden; nur eine Websuche, Direktabfrage nicht möglich. LÜCKE: Patentrecherche unvollständig (Regel F5).
10. Einstufung Tom: prüfenswert (Fertigung Hoch A, Verguss Mittel A, kein Niedrig)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "BAT Maschinenbau GmbH": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag an Tina): (a) Impressum/Register lesen (Name, Adresse, Amtsgericht). (b) Werden Elektrik/Steuerungen im Haus aufgebaut (Stellenanzeigen Elektroniker/Monteur), werden Zuführelektroniken selbst gefertigt oder zugekauft? Aktion: nicht kontaktieren.
14. Quellen:
- https://www.berlin.allaboutautomation.de/en/exhibitors/bat-maschinenbau-gmbh-238582/ (S, Messeprofil, Regel N5): „high-performance industrial feeders“ (Suchzusammenfassung); Abruf 2026-10-15.
- https://www.industrial-production.de/handhabungstechnik/handhabungstechnik---mutternschliessanlage.htm (S, Suchsnippet): „1999 von Jörg Biermann gegründet“ (Suchzusammenfassung); Abruf 2026-10-15.
- https://implisense.com/en/companies/bat-maschinenbau-gmbh-meinerzhagen-DEPFNPI2M054 (S): Maschinenbau, Sondermaschinen, Zuführtechnik; Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep BAT: kein Eintrag). Einzelsuche NICHT ausgeführt (Budget erschöpft). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: teilweise belegt (S, Impressum nicht gelesen): BAT Maschinenbau GmbH, Darmcher Grund 5, 58540 Meinerzhagen (Verzeichnis); Register nicht belegt. Messeliste 58540 Meinerzhagen passt. Keine Abweichung erkennbar.

## 6. Benedict*
1. Firma: Benedict* (Messe: all about automation Düsseldorf 2026, Stand 435, Halle nicht angegeben; Messeliste: 42489 Wülfrath)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Schütze, Schaltgeräte, Magnetsysteme/Spulen), nachrangig E-Mobility/PV-DC-Trenner
3. Gebiet: Österreich (Wien); Messeliste nennt Wülfrath, siehe Feld 17
4. Sitz und Fertigungsort: BENEDICT GmbH, Lieblgasse 7, 1220 Wien (Wirtschaftskammer-/Advantage-Austria- und Firmenbuch-Snippet, S). Ein Profil nennt "headquarters and production lines located in Vienna" (S). Wülfrath: kein Beleg.
5. Website: https://www.benedict.at
6. Was wird gebaut -> Bauteile: Elektromechanische Niederspannungs-Schaltgeräte seit 1920: Schütze, Nockenschalter, Hauptschalter, PV-DC-Trenner, Drucktaster (S). Typisch vergossen/verklebt/gedichtet (A, Block A): Schützspulen/Magnetsysteme (Spulen, Relais/Schütze) Hoch, Schaltgerätegehäuse mit Dichtung Mittel, PV-DC-Trenner (Gehäuse/Dichtung, Kontaktsysteme) Mittel.
7. Fertigung DE/AT/NL: Hoch, Stufe A (Sitzregel: eigener Gerätebauer mit erkennbarem Standort, Familien-GmbH 100 Prozent im Familienbesitz (S), eigene Produkte, kein Händler; kein Hinweis auf Auslagerung). Ergänzend S: "headquarters and production lines located in Vienna". Hinweis: Ein Konzern- oder Mehrwerkscharakter ist nicht belegt; falls doch, wäre Stufe V nötig.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (abgeleitet aus Produkttyp: Schütze und Magnetspulen, Wissensbasis Block A). Einzelbewertung: Schützspulen/Magnetsysteme Hoch (A), Relais-/Schützelektronik (z. B. Ansteuerung) Mittel (A), PV-DC-Trenner Mittel (A), Gehäusedichtung Mittel (A), Nockenschalter (mechanisch) Niedrig (A). Kein Gegenbeleg gefunden.
9. Patentrecherche (Pflicht): Datenbanken Google Patents, Espacenet, DEPATISnet; nur über Websuche, keine Direktabfrage.
- Websuche: "Benedict GmbH Wien patent applicant Schütz Nockenschalter Google Patents Espacenet Vergussmasse": Google-Patents-Treffer zu Nockenschaltern (DE1059078B, DE1665409C3, AT190135B, AT234808B) ohne sichtbaren Anmelder, daher NICHT Benedict zugeordnet und nicht gezählt. Keine Vergussmassen-Patente mit Benedict als Anmelder.
- Ergebnis: 0 gesicherte Treffer; Anmelder-Zuordnung der Nockenschalter-Patente (historisch, AT/DE) offen; nur eine Websuche, Direktabfrage nicht möglich. LÜCKE: Patentrecherche unvollständig (Regel F5), Anmelder Benedict & Co. u. ä. nachprüfen.
10. Einstufung Tom: interessant (Fertigung Hoch A, Verguss Hoch A), mit Vorbehalt Identität (Feld 17, Wien statt Wülfrath) und fehlender Stufe V
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "Benedict GmbH", "Benedict", "Benedict Wülfrath": kein Treffer in beiden Dateien)
13. Nachrecherche-Auftrag und Aktion (Vorschlag an Tina): (a) Identität: Ist der Aussteller "Benedict*" mit Sitz Wülfrath (Messeliste) die BENEDICT GmbH Wien oder eine deutsche Vertriebs-/Schwestergesellschaft? Impressum benedict.at und Messeprofil (aaa-Seite Benedict GmbH*) lesen, Jey bestätigt die Einheit. (b) Fertigungsort Wien mit V belegen (Firmenseite "Über uns"/Produktion, Stellenanzeigen Montage/Wicklerei Wien). (c) Wird in Wülfrath produziert? Aktion: nicht kontaktieren, bis Einheit geklärt.
14. Quellen:
- https://www.advantageaustria.org/ae/company/en/benedict-gmbh (S, Suchsnippet): „Lieblgasse 7, 1220 Wien“; Abruf 2026-10-15.
- https://www.evi.gv.at/f/67832d (S, Firmenbuch-Snippet): „Benedict GmbH“ Firmenbuch 67832d, Gesellschaft mit beschränkter Haftung; Abruf 2026-10-15.
- https://staatswappen.at/?p=17059 (S): Profil „headquarters and production lines“ in Wien (Suchzusammenfassung, Wortlaut sinngemäß); Abruf 2026-10-15.
- https://energy-utilities.com/benedict-gmbh-comp285958.html (S): „electromechanical low-voltage switching devices since 1920“ (Suchzusammenfassung); Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt (Familienunternehmen, S)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep Benedict: kein Eintrag); Websuche "Benedict Schaltgeräte Wien Fertigung Spulen Verguss Dosieranlage Klebstoff Referenz" (Treffer nur zu Scheugenpflug/bdtronic/Nordson allgemein, ohne Benedict-Bezug). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: ABWEICHUNG. Vorgabe/Messeliste: "Benedict*, 42489 Wülfrath". Gefunden (S): BENEDICT GmbH, Lieblgasse 7, 1220 Wien, Firmenbuch 67832d, Geschäftsführer Alexander Benedict (Register-Snippet). Bezug zu Wülfrath in keiner Quelle gefunden. Das Sternchen im Messenamen ("Benedict*") ist nicht aufgelöst. Impressum nicht gelesen. Ampel höchstens Gelb (Tabellenzeile 2), bis Jey die Firma bestätigt.

## 7. Berghof Automation GmbH
1. Firma: Berghof Automation GmbH (Messe: all about automation Düsseldorf 2026, Stand 223, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Steuerungs-/Panel-Elektronik), nachrangig Gasketing/Sealing (IP-Gehäuse), Optical Bonding (Panels/Displays)
3. Gebiet: Baden-Württemberg (Eningen unter Achalm)
4. Sitz und Fertigungsort: Arbachtalstraße 26, 72800 Eningen (Verzeichnisse, S); ältere Adresse Harretstraße 1 (Berghof Automationstechnik GmbH). Katalog 2024 laut Suchzusammenfassung: Entwicklung, Produktion und Test am Hauptsitz Eningen gebündelt (S). Fertigende Einheit: Berghof Automation GmbH innerhalb der Berghof Group.
5. Website: https://www.berghof-automation.com
6. Was wird gebaut -> Bauteile: Modulare und Safety-Steuerungen, Industrie-PCs, Bedienpanels, I/O-Systeme, Prüf-/Testsysteme für Automotive (S). Typisch vergossen/verklebt/gedichtet (A, Block B): Steuerungselektronik/Leiterplatten mit Schutzlack/Teilverguss Mittel, Bedienpanels/Displays (Verklebung, Dichtung für IP-Klasse, Optical Bonding) Mittel, Netzteil-/I/O-Module Mittel, Testsysteme mit Sensorik Mittel. Kein direkter Beleg.
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Suchzusammenfassung des Katalogs nennt die gebündelte Prozesskette in Eningen; Berghof Group ist ein Konzern mit mehreren Einheiten (Familienunternehmen gegründet 1966), daher wäre Stufe V einer Quelle zur fertigenden Einheit nötig. Katalog/Firmenseite nachlesen.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A (Einschätzung aus Produkttyp). Einzelbewertung: Steuerungs-/I/O-Elektronik Mittel (A), Bedienpanel/Display-Verklebung Mittel (A), Gehäusedichtung IP Mittel (A), Netzteile Mittel (A), Testsysteme Niedrig bis Mittel (A).
9. Patentrecherche (Pflicht): Datenbanken Google Patents, Espacenet, DEPATISnet; nur über Websuche.
- Websuche: "Berghof Automation Berghof Automationstechnik patent Gehäuse Dichtung Verguss Google Patents Espacenet DEPATISnet": Google-Patents-Treffer zu Gehäuse/Vergussmasse (AT14902U1 "Elektronisches Gerätegehäuse mit Vergussmasse-Verschluss", DE3026371A1, DE10100421A1 u. a.) ohne erkennbaren Anmelder Berghof, daher nicht zugeordnet und nicht gezählt.
- Ergebnis: 0 gesicherte Treffer; Anmelder-Varianten (Berghof Automationstechnik GmbH, Berghof Automation GmbH, Berghof Group) nicht direkt abgefragt; nur eine Websuche. LÜCKE: Patentrecherche unvollständig (Regel F5).
10. Einstufung Tom: prüfenswert (Fertigung Mittel S, Verguss Mittel A, kein Niedrig)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "Berghof Automation GmbH", "Berghof Group", "Berghof": kein Treffer; Konzernabgleich Regel M ausgeführt)
13. Nachrecherche-Auftrag und Aktion (Vorschlag an Tina): (a) Fertigung der Steuerungen/Panels in Eningen mit V belegen: Katalog 2024 (PDF) bzw. Firmenseite "Produktion" und Stellenanzeigen (Elektronikfertiger, Montage) lesen. (b) Impressum: ist die Berghof Automation GmbH die fertigende Einheit (Abgrenzung Berghof Automationstechnik GmbH, Berghof Products + Instruments)? (c) Werden Panels optisch verklebt/Leiterplatten vergossen oder lackiert (Datenblatt IP-Klasse)? Aktion: nicht kontaktieren.
14. Quellen:
- https://www.chemie.de/firmen/18197/berghof-automationstechnik-gmbh.html (S, Suchsnippet): Berghof Automationstechnik GmbH, modulare und Safety-Steuerungen; Abruf 2026-10-15.
- https://automa.net/company/berghof-automation-gmbh (S): Berghof Automation GmbH, Arbachtalstraße 26, 72800 Eningen; Abruf 2026-10-15.
- https://www.it-in-germany.de/firma/Berghof+Automation+GmbH/5022451/50085/eng (S, Triage-Quelle): Prozesskette am Standort gebündelt (Suchzusammenfassung, Wortlaut nicht selbst gelesen); Abruf 2026-10-15.
- https://craft.co/berghof-group (S): „family-owned“ Berghof Group, gegründet 1966 (Suchzusammenfassung); Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep Berghof: kein Eintrag); Websuche "Berghof Automation Eningen Dosieranlage OR Vergussanlage OR Klebstoff OR Dichtung Nordson OR Scheugenpflug OR DOPAG OR Sonderhoff OR Henkel OR DELO Referenz" (keine Referenz zu Dosier-/Vergussanlagen oder Massen bei Berghof). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: teilweise belegt (S, Impressum nicht gelesen): Berghof Automation GmbH, Arbachtalstraße 26, 72800 Eningen (Verzeichnisse); Registerangaben nicht gefunden. Messeliste 72800 Eningen unter Achalm passt. Abweichung: Verzeichnisse führen auch "Berghof Automationstechnik GmbH" (frühere Firmierung/Adresse Harretstraße 1); Namenswechsel nicht belegt. Nicht verwechseln mit Berghof GmbH (yumda-Eintrag, andere Firma).

## 8. Bluhm Systeme GmbH
1. Firma: Bluhm Systeme GmbH (Messe: all about automation Düsseldorf 2026, Stand 720, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Elektronik, Netzteile), nachrangig LED/Sensorik in Kennzeichnungsgeräten
3. Gebiet: Rest Deutschland+Niederlande (Rheinbreitbach, Rheinland-Pfalz)
4. Sitz und Fertigungsort: Maarweg 33, 53619 Rheinbreitbach (Pressemitteilung, S). Laut Bionity-Profil "develop, design and produce" am Sitz (S); Gruppe BluhmWeber mit weiteren Produktions-/Vertriebsstandorten in Europa (GS1-Profil, S).
5. Website: https://www.bluhmsysteme.com
6. Was wird gebaut -> Bauteile: Kennzeichnungs- und Etikettiersysteme: Tintenstrahldrucker (Inkjet), Laserbeschrifter, Etikettierer, Thermotransfer-Direktdrucker, Sondermaschinen, eigene Etikettenproduktion (S). Typisch vergossen/verklebt/gedichtet (A): Druckkopf-/Ansteuerelektronik Mittel, Netzteile Mittel bis Hoch (Block A), Laserquelle/-elektronik Mittel, Steuerplatinen Mittel, Gehäusedichtung (IP-Schutz) Mittel.
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Sitz und Entwicklung/Produktion laut Profil in Rheinbreitbach, jedoch BluhmWeber-Gruppe mit mehreren Standorten (Konzernfall, V nötig); Stellenanzeigen Rheinbreitbach (Entwicklung Inkjet, Produktionsplanung/Auftragssteuerung, S) deuten auf Eigenfertigung, belegen aber Fertigungstiefe nicht. Triage-Hinweis "Stufe V offen" bestätigt.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A (Endprodukt-Regel Kennzeichnungsgeräte). Einzelbewertung: Netzteile Mittel (A), Druckkopf/Ansteuerelektronik Mittel (A), Laserbeschrifter-Elektronik Mittel (A), Steuerung/Panel Mittel (A), Etikettierer-Mechanik Niedrig (A). Hinweis: Wissensbasis Block C nennt Etiketten/Verpackung als niedrig, hier betrifft es aber Geräte mit Elektronik.
9. Patentrecherche (Pflicht): Datenbanken Google Patents, Espacenet, DEPATISnet; nur über Websuche.
- Websuche: "Bluhm Systeme GmbH Rheinbreitbach patent Anmelder Vergussmasse OR Dichtung OR Kleben Google Patents Espacenet DEPATISnet": keine Patentdatensätze; nur Firmenprofile (chemie.de, bionity, implisense, GS1).
- Ergebnis: 0 Treffer gefunden; Hinweis der Suche: Patente könnten unter Gruppen- oder Erfindernamen (BluhmWeber, Eckhard/Carsten Bluhm) laufen, nicht abgefragt. Nur eine Websuche. LÜCKE: Patentrecherche unvollständig (Regel F5).
10. Einstufung Tom: prüfenswert (Fertigung Mittel S, Verguss Mittel A, kein Niedrig)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "Bluhm Systeme GmbH", "BluhmWeber", "Bluhm Weber": kein Treffer). Siehe Kopfvermerk zum unverwandten Präfixtreffer "Weber".
13. Nachrecherche-Auftrag und Aktion (Vorschlag an Tina): (a) Fertigungsort der Geräte (Inkjet, Laser, Etikettierer) mit V belegen: Bluhm-Seite "Unternehmen/Produktion Rheinbreitbach", Stellenanzeigen (Montage, Elektronikfertigung). (b) Welche Einheit der BluhmWeber-Gruppe fertigt (Rheinbreitbach vs. andere Werke)? (c) Triage-Vermerk "Bluhm bei MOTEK zurückgestellt": Jey bestätigt, ob hier ein Vorlauf besteht (Memory nicht einsehbar, unverifiziert). Aktion: nicht kontaktieren.
14. Quellen:
- https://www.bionity.com/en/companies/1039147/bluhm-systeme-gmbh.html (S, Suchsnippet): „We develop, design and produce innovative labeling systems“; Abruf 2026-10-15.
- https://en.pine.gs1.de/member/6228952427d5990004e206d0 (S): Produktions- und Vertriebsstandorte in Deutschland, Österreich, Schweiz u. a., BluhmWeber Group (Suchzusammenfassung); Abruf 2026-10-15.
- https://implisense.com/en/companies/bluhm-systeme-gmbh-rheinbreitbach--DEZMK0S0PX32 (S): HRB 10343 Montabaur; Abruf 2026-10-15.
- https://www.bluhmsysteme.com/assets/Uploads/Documents/Bluhm-Weber/Press-Releases/202601-PM-aaa-Berlin.pdf (S, Pressemitteilung, nicht selbst gelesen): Adresse Maarweg 33, 53619 Rheinbreitbach; Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt (gegründet 1968 laut Suchzusammenfassung, S)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep Bluhm: kein Eintrag). Einzelsuche NICHT ausgeführt (Budget erschöpft). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: teilweise belegt (S, Impressum nicht gelesen): Bluhm Systeme GmbH, Maarweg 33, 53619 Rheinbreitbach, laut Aggregator HRB 10343 Amtsgericht Montabaur, Geschäftsführer u. a. Eckhard Bluhm und Carsten Bluhm (Pressemitteilung), Teil der BluhmWeber-Gruppe. Messeliste 53619 Rheinbreitbach passt. Keine Abweichung zur Vorgabe; Aggregator Implisense beschreibt die Firma abweichend als Handel mit Druckmaschinen (Widerspruch zu den Herstellerprofilen).

## 9. BWH Elektro-Vertriebs-GmbH
1. Firma: BWH Elektro-Vertriebs-GmbH (Messe: all about automation Düsseldorf 2026, Stand 218, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: unbekannt (Name deutet auf Elektro-Vertrieb)
3. Gebiet: Rest Deutschland+Niederlande (Wuppertal laut Vorgabe, nicht belegt)
4. Sitz und Fertigungsort: Wuppertal laut Messeliste (42329 Wuppertal), keine Quelle gefunden. Fertigungsort: unbekannt.
5. Website: unbekannt (nicht gefunden)
6. Was wird gebaut -> Bauteile: unbekannt. Websuche "BWH Elektro-Vertriebs-GmbH Wuppertal" liefert keine Seite zur Firma. Bauteile nicht ableitbar (?).
7. Fertigung DE/AT/NL: Niedrig, Stufe ?. Begründung: weder Produkt noch Standort belegt; der Name "Elektro-Vertriebs" deutet auf einen Vertrieb (A, nicht belegt). Keine Annahme zugunsten der Firma.
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe ?. Begründung: keine Produktangaben; Einzelbewertung nicht möglich (Elektro-Vertriebsprodukte unbekannt). Wert Niedrig bedeutet hier "nicht belegt", nicht "widerlegt".
9. Patentrecherche (Pflicht): Datenbanken Google Patents, Espacenet, DEPATISnet; nur über Websuche.
- Websuche: "BWH Elektro-Vertriebs GmbH Patent Anmelder DEPATISnet Wuppertal": keine Patentdatensätze; fremde Firmen (BFI Industrie-Elektronik Wuppertal HRA 14994, B.W. Vertrieb GmbH Kirchardt) sind andere Unternehmen und werden nicht vermischt.
- Ergebnis: 0 Treffer; Firma insgesamt nicht auffindbar, Anmelder-Zuordnung sinnlos ohne Identität. Nur eine Websuche. LÜCKE: Patentrecherche unvollständig (Regel F5).
10. Einstufung Tom: unwahrscheinlich (Fertigung und Verguss nicht belegt, Name deutet auf Vertrieb; Identität offen)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "BWH Elektro-Vertriebs-GmbH", "BWH": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag an Tina): Identität klären: Handelsregister (Wuppertal) und Messeprofil der aaa (Stand 218) lesen: Rechtsform, Adresse, Geschäftszweck; Website der Firma ermitteln (mögliche Schreibweise "BWH" evtl. Abkürzung, Hinweis auf B.W.H. oder BHW nicht belegt). Ist sie Hersteller oder reiner Vertrieb (E2)? Aktion: nicht kontaktieren, bis Identität belegt.
14. Quellen:
- Websuche "BWH Elektro-Vertriebs-GmbH Wuppertal" (2026-10-15): keine Treffer zur Firma; nächstliegende, aber andere Firmen: https://www.diedeutscheindustrie.de/firma/bfi%20industrie%20elektronik%20gmbh%20%20co.%20kg%20bfi%20industrie%20elektronik%20gmbh%20co%20kg/4016815/46350/eng („BFI Industrie-Elektronik GmbH & Co. KG“, Wuppertal, S); Abruf 2026-10-15.
- aaa_duesseldorf_2026.csv, Zeile 30: „BWH Elektro-Vertriebs-GmbH;218;42329;Wuppertal;Deutschland“ (Messeliste, Stufe S, Regel N5); Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep BWH: kein Eintrag). Einzelsuche NICHT ausgeführt (Firma nicht auffindbar, Budget erschöpft). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: NICHT belegt. Vorgabe: BWH Elektro-Vertriebs-GmbH, 42329 Wuppertal (Messeliste). Websuche fand keine Seite, kein Register, kein Impressum zu dieser Firma. Ampel höchstens Gelb (Tabellenzeile 2), Auftrag Identität.

## 10. Camozzi Automation GmbH
1. Firma: Camozzi Automation GmbH (Messe: all about automation Düsseldorf 2026, Stand 245, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Magnetventilspulen, Proportionalventile, Ventilinseln mit Elektronik)
3. Gebiet: Baden-Württemberg (Albershausen); Konzern außerhalb (Italien)
4. Sitz und Fertigungsort: Porschestraße 1, 73095 Albershausen (Verzeichnisse, S). Fertigung am Standort Albershausen: nicht belegt. Gruppe Camozzi (Brescia, IT) mit mehreren Produktionswerken (17 bis 25 laut unterschiedlichen Quellen, S).
5. Website: https://www.camozzi.de
6. Was wird gebaut -> Bauteile: Pneumatik, Magnetventile, Ventilinseln, Feldbus, Mikro-Dosierventile (K8MDC) (S, Produktseiten). Albershausen wird als spezialisiert auf Pneumatik, Steuerungstechnik und elektrische Automatisierung beschrieben (S), Produkt-zu-Werk-Zuordnung offen. Typisch vergossen/verklebt/gedichtet (A, Block A): Magnetventilspulen Hoch, Proportionalventile/Ventilinsel-Elektronik Mittel bis Hoch, Gehäusedichtungen Mittel.
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Triage "Vertriebs-/Servicetochter"; Konzern mit mehreren Werken (Stufe V erforderlich, fehlt); keine Quelle, dass in Albershausen gefertigt wird. Nicht zu verwechseln mit der österreichischen Camozzi Automation GmbH, Hall in Tirol (FN 275106v, KSV-Snippet): andere Einheit, AT-Fertigung nicht belegt.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (abgeleitet aus Produkttyp Magnetventilspulen/Magnetspulen, Wissensbasis Block A, Konzernprodukt). Einzelbewertung: Magnetventilspulen Hoch (A), Proportionalventile Hoch (A), Ventilinsel-/Feldbuselektronik Mittel (A), Gehäusedichtung Mittel (A), pneumatische Zylinder Niedrig (A). Bezieht sich auf die Produkte der Gruppe, nicht auf Albershausen.
9. Patentrecherche (Pflicht): Datenbanken Google Patents, Espacenet, DEPATISnet; nur über Websuche.
- Websuche: "Camozzi Spa patent solenoid valve coil potting OR overmolded OR encapsulated Google Patents Espacenet": Treffer ausschließlich Patente anderer Anmelder (US5538220, US11915866, US11994231, US5358215); kein Patent mit Anmelder Camozzi gefunden. Camozzi-Spulenkörper (Serie U7) laut Händlerseite mit "Encapsulating material PET" (S, Händlerseite rs-online) – Hinweis auf gekapselte Spule, keine Patentangabe.
- Ergebnis: 0 gesicherte Treffer; Anmelder-Varianten (Camozzi S.p.A., Camozzi Group S.p.A., Camozzi Automation S.p.A.) nicht direkt abgefragt; nur eine Websuche. LÜCKE: Patentrecherche unvollständig (Regel F5), Konzernanmelder nachprüfen.
10. Einstufung Tom: unwahrscheinlich (Fertigung DE Niedrig S: Vertriebs-/Servicetochter, Konzern; Produkttyp wäre Verguss Hoch A)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "Camozzi Automation GmbH", "Camozzi Group", "Camozzi": kein Treffer; Konzernabgleich Regel M ausgeführt)
13. Nachrecherche-Auftrag und Aktion (Vorschlag an Tina): (a) Gibt es ein Camozzi-Werk in Deutschland (Albershausen: Montage/Produktion von Ventilinseln, Steuerungen)? Camozzi-Standortseite, Impressum camozzi.de und Stellenanzeigen Albershausen (Montage, Produktion) lesen; Werke der Gruppe (Brescia, Italien) vs. Albershausen trennen. (b) Impressum/Register der Albershausener GmbH (Amtsgericht Stuttgart?). Ergibt sich nur Vertrieb/Service: "kein Fertiger" (E2). Aktion: nicht kontaktieren.
14. Quellen:
- https://www.allaboutautomation.de/en/?p=14975 (S, Messeprofil, Regel N5): Camozzi Automation GmbH, Albershausen; Abruf 2026-10-15.
- https://www.computer-automation.de/steuern-und-regeln/uwe-claus-ist-neuer-geschaeftsfuehrer.htm (S, Suchsnippet): Uwe Claus Geschäftsführer Camozzi Automation Albershausen ab 01.12.2018 (Datum veraltet); Abruf 2026-10-15.
- https://www.directindustry.com/soc/camozzi-automation-5625.html (S): „six production plants“ (Suchzusammenfassung, bezieht sich auf die Gruppe); Abruf 2026-10-15.
- https://www.ksv.at/en/business_search/detail/at-1472779-camozzi-automation-gmbh (S): Camozzi Automation GmbH, Hall in Tirol, FN 275106v (andere Einheit); Abruf 2026-10-15.
15. Größe/Umsatz: Gruppe laut Suchzusammenfassung 17 Produktionsstandorte, 2.600 Mitarbeiter (Artikel 2018, S, veraltet); für die GmbH unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep Camozzi: kein Eintrag); Websuche "Camozzi Albershausen OR Camozzi Group Dosieranlage OR Vergussmasse OR Klebstoff Nordson OR Scheugenpflug OR DOPAG OR Henkel OR DELO Referenz Magnetventil Fertigung" (nur Händler-/Produktseiten, kein Wettbewerberbezug). Messe-Signal: keine Wettbewerber auf der aaa. Hinweis: Camozzi verkauft selbst ein Mikro-Dosierventil (K8MDC) für Klebstoffe (S, bibus.com), kein Konflikt zu den Anlagen von Demak, aber Randsignal.
17. Identität: teilweise belegt (S, Impressum nicht gelesen): Camozzi Automation GmbH, Porschestraße 1, 73095 Albershausen (Verzeichnisse); Registerdaten nicht gefunden. Messeliste 73095 Albershausen passt. Abweichung/Gefahr der Verwechslung: Camozzi Automation GmbH, Löfflerweg 18, 6060 Hall in Tirol (FN 275106v) ist eine andere Gesellschaft; Konzern Camozzi Group S.p.A., Brescia.

## nicht aufgenommen (bereits bekannt / unklar)
Keine der 10 Firmen ist BEKANNT (Anzahl BEKANNT: 0), daher sind alle im Batch geführt. Vermerke:
- Bluhm Systeme GmbH / Marke "Weber Marking Systems": CRM-Rohtreffer "Weber GmbH & Co. KG [DE]" (bekannte_firmen_DE-AT-NL.txt Zeile 2549) und "Weber Elektronik GmbH [DE]" (Zeile 2548). Nur gleicher Wortstamm "Weber", keine belegte Verbindung zur BluhmWeber-Gruppe; nicht als Konzernbezug gewertet, Tina/Jey bei Bedarf prüfen.
- Benedict* (Messeliste Wülfrath) gegenüber gefundener Benedict GmbH Wien: kein CRM-Treffer, aber Identität unklar (Feld 17).

## Einschränkungen
- WebFetch nicht nutzbar: alle Abrufe (asyril.com, ateg.de, autec-gmbh.de, bahrmann.de, batmaschinenbau.de, allaboutautomation.de) scheiterten mit "getaddrinfo ENOTFOUND". Chrome-Werkzeuge (mcp__claude-in-chrome__*) in dieser Sitzung nicht verfügbar: Vermerk "Browser nicht verfügbar". Ein Umgehen über curl wurde nicht versucht (Sandbox-Regeln). Folge: Keine Impressen, Produktseiten oder Datenblätter selbst gelesen; ALLE Aussagen sind Stufe S, A oder ?, keine Stufe V. Es gibt keine Grün-fähigen Fertigungsbelege für Konzern-/Mehrwerksfälle.
- WebSearch-Budget (200 Aufrufe je Turn, geteilt mit anderen Agenten) erschöpft: Es konnten nur etwa 30 Abfragen laufen. NICHT ausgeführt: die Einzelsuche nach Wettbewerbereinsatz (Feld 16) für ATEG, Autec, Asyril, Bahrmann, BAT, Bluhm, BWH (dort nur Abgleich mit wettbewerber_referenzen.md und teilweise allgemeine Suche); die zweite Patentsuche je Firma; Impressums-/Registersuchen für BAT, Bluhm, Berghof, Asyril GmbH. Feld 16 ist daher bei diesen Firmen unvollständig (formal ausgefüllt, inhaltlich Lücke): Batch gilt in der Sache als UNVOLLSTÄNDIG, auch wenn batch_check.py die Formalien bestätigt.
- Patentrecherche (Feld 9): Google Patents, Espacenet und DEPATISnet konnten nicht direkt abgefragt werden (kein Browser, WebFetch ausgefallen); Abfragen liefen nur als Websuchen mit Datenbank-/Anmelder-Stichwörtern, die Suchmaschine fand keine Patente der Firmen. Das ist ein schwacher Negativbefund (kein Gegenbeweis); Rechtsstände wurden mangels Treffern nicht erhoben. Für alle 10 Firmen ist die Direktabfrage nachzuholen (Tom mit Browser oder Tina).
- Fremde Patent-Treffer ohne erkennbaren Anmelder-Bezug (Nockenschalter-Patente, Gehäuse-/Vergusspatente) wurden nicht den Firmen zugeordnet und nicht gezählt.
- Triage-Angaben (Mitarbeiterzahl Autec, "CPA-Gruppe" bei Asyril, Bluhm "bei MOTEK zurückgestellt laut Memory") sind unverifiziert übernommen; das Memory war nicht einsehbar.
- Aussteller-Beschreibungen der Messe liegen nur als Snippets vor (Stufe S, Regel N5). Halle ist in der Liste nicht angegeben; Feld 1 nennt nur die Standnummer.
- Größe, Umsatz, Mitarbeiter nur nebenbei erfasst (Feld 15), keine eigenen Suchaufrufe dafür. Keine Suche nach Ansprechpartnern oder Kontaktformularen (Regel K).
