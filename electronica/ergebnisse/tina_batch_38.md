# Tina Batch 38 – electronica 2026 (Prüfung von tom_batch_38.md)
Erstellt: 2026-10-15 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe: ausschließlich electronica/ergebnisse/tom_batch_38.md (10 Firmen, Nr. 422 bis 427 und 429 bis 432).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** WebFetch und Chrome nicht verfügbar; nur WebSearch (19 Abfragen mit Ergebnis, die 20. scheiterte am Sitzungslimit) und Bash. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün vergeben. Tabellenzeile = Zeilennummer der Ampel-Tabelle D. Verifikationsdatum aller Einträge: 2026-10-15.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 422 | MUEGGE GmbH (C2.108) | GELB | 5 | ja |
| 423 | Multek Technology Germany GmbH (A2.177) | GELB | 2 | nein |
| 424 | MultiOceans GmbH (B3.121) | GELB | 2 | ja |
| 425 | municom Vertriebs GmbH (B6.231) | GELB | 2 | nein (Rot-Kandidat E2) |
| 426 | NanoFocus AG (C1.553) | GELB | 5 | ja |
| 427 | Nanya Technology Europe GmbH (B5.500) | GELB | 7 | nein (Rot-Kandidat E2) |
| 429 | NCAB Group Germany GmbH (A2.243) | GELB | 7 | nein (Rot-Kandidat E2/E3) |
| 430 | Neosid Pemetzrieder GmbH & Co. KG (A6.500) | GELB | 5 | ja |
| 431 | Neumonda GmbH (C5.361) | GELB | 7 | nein (Rot-Kandidat E2) |
| 432 | N&H Technology GmbH (B3.361) | GELB | 5 | ja |

Zahlen: Grün 0, Gelb 10, Rot 0.

CRM-Abgleich: `python3 crm_abgleich.py` für alle Firmen samt Konzern-, Alt- und Schwesternamen selbst wiederholt (Muegge/Muegge Gerling/Muegge Group; Multek/Flex/Multilayer Technology; MultiOceans; municom Vertriebs/municom GmbH; NanoFocus/Carl Mahr Holding/Mahr; Nanya; NCAB/NCAB Group/B&B Leiterplattenservice; Neosid/Pemetzrieder; Neumonda/Neumonda Technology/Intelligent Memory; N&H/N+H/NH Technology): alle neu, kein Konzernbezug (Regel M). Einziger Hinweis: "Intelligent Memory" gleiche Wortwurzel mit "Intelligent Machines Gmbh" / "InTELLIGENT MASCHINEN GMBH" (bekannte_firmen_DE-AT-NL.txt Zeilen 1166/1167), andere Firma, Tom korrekt. Toms CRM-Feld 12 bestätigt bei allen zehn.

Patente (Prüfpunkt 8, F5): Google Patents, Espacenet, DEPATISnet nicht direkt abfragbar. Eigene Patent-Websuchen nur für Neosid und Muegge (beide ohne Treffer mit Verguss/Dichten/Kleben und ohne Anmelderzuordnung), die geplante Statusprüfung zu NanoFocus US11029143B2 scheiterte am Limit. Feld 9 bleibt bei ALLEN zehn Firmen ohne Datenbankabfrage: nicht belastbar, kein Gegenbeweis. Der Batch ist nach F5 UNVOLLSTÄNDIG; Nachholen im Browser nötig, bevor irgendein Grün final wird (vor allem Neosid, Muegge, NanoFocus). Wettbewerbereinsatz (F6): Tom hat wettbewerber_referenzen.md abgeglichen (0 Treffer); ich habe nur Teil 1 (Zeilen 1 bis 378) gelesen, Zeilen 379 bis 631 nicht, daher Toms Abgleich nicht vollständig gegengeprüft. Kein Einfluss auf die Ampel.

---

## 422. MUEGGE GmbH | Stand C2.108
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Gerätebauer mit erkennbarem Sitz Reichelsheim und Verguss Hoch (A: HV-Netzteile, Trafos, Leistungsmodule), aber Sitzregel nicht sicher: Mehrere Standorte/Eigentümerwechsel (Meyer Burger zu HQ Equita 2020, Verdane Oktober 2023, laut Dealroom, S), US-Tochter Modesto; Fertigung der Generatoren in Reichelsheim nur S.
- Eigene Prüfung: Handelsregister Darmstadt HRB 70541 (North Data und Die Deutsche Industrie, S) mit früheren Namen Roth & Rau Muegge GmbH, Muegge-electronic GmbH; Adresse Hochstr. 4-6, 64385 Reichelsheim bestätigt. North Data zeigt "Muegge GmbH" mit Kreuz, aber Stellenanzeigen 2025/2026 (Stepstone, S) nennen aktiv "Muegge GmbH, Reichelsheim" mit "developing and manufacturing ... microwave and plasma technology". Identität damit plausibel (Zeile 2 nicht ausgelöst), Registerstatus offen. Keine Stellenanzeige für Montage/Elektronikfertigung gefunden.
- Patent (eigene Websuche): kein Patent mit Muegge als Anmelder zu Verguss gefunden; nur Produktseiten (everythingrf). Datenbanken nicht abgefragt.
- Korrekturen an Toms Feldern: Feld 4/17: Eigentümerlage (Verdane, Finanzinvestor) und HRB 70541 ergänzen; Kreuz bei North Data vermutlich Vorgängerfirma-Eintrag, nicht belegt. CRM: neu.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Werden die Generatoren/Netzteile in Reichelsheim gefertigt und montiert (Fertigungsbeleg V), und ist das die fertigende Einheit neben den Schwestergesellschaften? Wo nachsehen: Impressum muegge.de, Standortseite/Karriereseite (Montage, Elektronikfertigung), Unternehmensregister Darmstadt HRB 70541 (aktueller Status, Firmierung), Datenblatt Generator (Netzteil/Trafo, Vergussangabe). Zugleich Patente in Google Patents/Espacenet/DEPATISnet mit Anmeldervarianten (Muegge GmbH, Muegge electronic, Roth & Rau Muegge) nachholen.
- Nicht verwendbare Aussagen: Fertigung Reichelsheim (S); Verguss aller Bauteile (A); Mitarbeiterzahl (widersprüchlich, S); Eigentümerwechsel (S, Dealroom). Stichprobe für Jey: ja.

## 423. Multek Technology Germany GmbH | Stand A2.177
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Meine Suche bestätigt: kein Eintrag "Multek Technology Germany GmbH" in Frankfurt; nur Böblingen (Evertiq, Schließung gemeldet, älterer Artikel) und ein Hinweis auf "Multi Circuit Boards Ltd." in Brunnthal (electronics.org-Verzeichnis, andere Firma, nicht zuordnen). Leiterplattenhersteller: Verguss Niedrig (A, Block C), Fertigung DE Niedrig (S). Inhaltlich "unwahrscheinlich" wie Tom, aber Zeile 2 geht vor.
- Korrekturen: keine. CRM: neu. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Existiert die Gesellschaft in Frankfurt (Name, Rechtsform, Register) und ist sie Vertriebsbüro oder Fertigung? Wo nachsehen: Ausstellerprofil auf electronica.de (Halle A2, Stand 177), Handelsregister Frankfurt, Impressum multek.com. Wenn nur Vertrieb/Leiterplatten ohne Fertigung DE: E2/E3 mit Quelle prüfen, dann Rot. Aktion: nicht priorisieren.
- Nicht verwendbare Aussagen: Identität (nicht belegt); Konzernzugehörigkeit zu Flex (S); alle Fertigungs-/Verguss-Einstufungen (S/A). Stichprobe für Jey: nein.

## 424. MultiOceans GmbH | Stand B3.121
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Zwei weitere Suchen ("MultiOceans GmbH Köln", "MultiOceans electronica Aussteller") bestätigen Toms Befund: keine Firma dieses Namens in Köln auffindbar (nur MULTI-Transporte GmbH, Frechen, nicht verwenden; Multi Germany GmbH, Gießen, Immobilien, nicht zuordnen). "Nicht auffindbar" ist kein Beleg für Nichtexistenz; Rot ist ausgeschlossen. Toms "unwahrscheinlich" ist ein Platzhalter, kein Befund.
- Korrekturen: keine. CRM: neu. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Welche Firma steht hinter Stand B3.121 (Schreibweise, Produkt, Sitz 50859 Köln)? Wo nachsehen: Ausstellerverzeichnis electronica.de (Browser), Handelsregister Köln, Messekatalog/Hallenplan. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (Sitz Köln aus Messeliste; Fertigung/Verguss ?). Stichprobe für Jey: ja (Existenz der Firma).

## 425. municom Vertriebs GmbH | Stand B6.231
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Gefunden wird nur "municom GmbH", Fuchsgrube 4, 83278 Traunstein, HR-Nr. 11648, Gründung 1977, Geschäftsführer Thomas Wende (it-in-germany, bayern-international, dastelefonbuch, S); eine "municom Vertriebs GmbH" ist nicht belegt. Beschreibung: "distribution of prefabricated high-frequency parts and optical transfer technology", Verzeichnis führt zugleich "Distributor und Hersteller" (S). E2 inhaltlich stark, aber nicht V; Rot nur mit Quelle, daher Gelb.
- Korrekturen: Feld 17 bestätigt (Abweichung Vertriebs GmbH). Feld 10 "kein Fertiger" bleibt vorläufig (Verzeichnis nennt auch "Hersteller"). CRM: neu.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Ist die ausstellende Gesellschaft die municom GmbH (HRB 11648 Traunstein) oder eine eigene municom Vertriebs GmbH? (b) Fertigt municom Module/Gehäuse selbst oder nur Handel (Beleg für E2)? Wo nachsehen: Impressum municom.de, Handelsregister Traunstein, Produktseiten/Stellenanzeigen. Bei bestätigtem Handel ohne Fertigung: Rot nach E2 mit Quelle.
- Nicht verwendbare Aussagen: Distributor-Status (S); Mitarbeiterzahl 31 (S, Datum unbekannt); Gehäuse im Angebot (S). Stichprobe für Jey: nein.

## 426. NanoFocus AG | Stand C1.553
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Messgerätebauer in Oberhausen (Sitz Max-Planck-Ring 48, 46049, durch Factsheet 2020 und weitere Quellen konsistent, S), Verguss Mittel (A, Sensorköpfe, Elektronik, LED). Sitzregel greift nicht sicher: Konzern. Neu gegenüber Tom: Carl Mahr Holding hat nach Squeeze-out (Eintragung 22.12.2025, Anteil von ca. 59 % auf ca. 96,9 %) die Minderheitsaktionäre abgefunden und integriert NanoFocus vollständig in die Mahr-Gruppe (Unternehmeredition, S). Toms 50,1 % (Stand 2020) ist überholt. Eine 2018er Research-Note (S) sagt, Mahr habe weltweit exklusive Rechte an NanoFocus-Standardprodukten (µsurf, µscan); wo gefertigt wird, ist nicht belegt.
- Eigene Prüfung: Indeed-Eintrag nennt Stellen Elektronikentwickler und Anwendungstechniker in Oberhausen, Servicetechniker in Ettlingen (S); keine Montage-/Fertigungsstelle gefunden. Konzernabgleich Mahr: kein CRM-Treffer.
- Korrekturen an Toms Feldern: Feld 4/17 Eigentümerlage aktualisieren (Squeeze-out 2025). Patent-Rechtsstand US11029143B2 nicht geprüft (Limit). CRM: neu.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Werden die Sensoren (µsurf/µscan) weiterhin in Oberhausen gefertigt oder in andere Mahr-Werke (Göttingen/Esslingen) verlagert, und wo ist der Vergussschritt? Wo nachsehen: Impressum nanofocus.com/.de, Standortseite Mahr-Gruppe, Pressemeldung zur Integration, Karriereseite (Montage, Produktion), Datenblatt µsurf (Schutzart, Sensorkopf). Patente: Google Patents/Espacenet mit Anmelder "NanoFocus AG" nachholen, Rechtsstand von US11029143B2 und Familie EP3504507 prüfen.
- Nicht verwendbare Aussagen: Fertigung Oberhausen (S); Verguss aller Bauteile (A); Mitarbeiterzahl ca. 75 (S, alt); Patentstatus (S). Stichprobe für Jey: ja (Konzernintegration).

## 427. Nanya Technology Europe GmbH | Stand B5.500
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Identität bestätigt (Pempelforter Straße 50, 40211 Düsseldorf, HRB 44547 Amtsgericht Düsseldorf, Bloomberg-LEI und Telefonbuchverzeichnis, S). Vertriebsbüro der taiwanischen Nanya Technology Corp, keine Fertigung in DE belegt; E2/E3 sehr wahrscheinlich, aber ohne Impressum/Quelle nicht V, daher nicht Rot.
- Korrekturen: keine. Kein Impressum der GmbH gefunden. CRM: neu. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Reine Vertriebsgesellschaft? Wo nachsehen: Impressum/Standortseite nanya.com (Europa), Handelsregister Düsseldorf HRB 44547 (Gegenstand: Vertrieb). Bei Bestätigung Rot nach E2/E3 mit Quelle.
- Nicht verwendbare Aussagen: "Vertriebsbüro" (S); Fertigung der Mutter in Taiwan (S). Stichprobe für Jey: nein.

## 429. NCAB Group Germany GmbH | Stand A2.243
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Beschaffungs-/Vertriebsmodell: Sitz Elsenheimer Straße 7, 80687 München (Wirtschaftsforum, S). Wirtschaftsforum (S) beschreibt NCAB dennoch teils als "Hersteller": Partnerfabriken in China, ca. 100 eigene QS-Mitarbeiter und "eigene Maschinen vor Ort" (Zitat des CEO, S). Die B&B-Leiterplattenproduktion in Mittweida wurde laut NCAB 2022 geschlossen (Inderes/NCAB, S). Für die Münchner GmbH keine Fertigung in DE/AT/NL belegt. Verguss Niedrig (A, Leiterplatten).
- Korrekturen an Toms Feldern: Feld 6/7 ergänzen, dass NCAB sich teils als Hersteller darstellt (Fertigung ausschließlich China, partnerbasiert); ändert die Einordnung E3/E2 nicht, zeigt aber, dass "Händler" nicht V-belegt ist. Fünf Standorte in DACH laut Wirtschaftsforum (S): Funktion unbekannt. CRM: neu.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Fertigt oder bestückt NCAB Group Germany selbst in DE/AT/NL (Standorte Pforzheim, München, weitere)? Wo nachsehen: Impressum ncabgroup.com/de, Standortseite, Handelsregister München. Bei Bestätigung reinen Handels: Rot nach E2/E3 mit Quelle.
- Nicht verwendbare Aussagen: Sourcing ohne eigene Fertigung (S); Mitarbeiterzahl B&B (S). Stichprobe für Jey: nein.

## 430. Neosid Pemetzrieder GmbH & Co. KG | Stand A6.500
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Toms Einstufung "interessant" ist nicht bestätigt (nur S/A, Regel I verlangt Browser-Gegenlesen). Hersteller mit erkennbarem Sitz Halver (Langenscheid 26-30, 58553; Stepstone-Snippet: "entwickeln und produzieren rund 80 ... Beschäftigte ... Ferrite, Induktivitäten und RFID-Transponder", Metoree-Adresse, S) und Verguss Hoch (A: Spulen, Sensorspulen, Transponder). Die Sitzregel greift nicht sicher: Meine Suche (Firmenhistorie, S) nennt eine Tochter NEOTECH in Polen (1998, Mehrheitsbeteiligung) sowie Neosid Ltd. (UK) als Namensverwandte; Mehrwerk-/Gruppenhinweis ist V-pflichtig. Transponder laut wiot-group "100% in Germany (Halver)" (S, Tom).
- Eigene Prüfung: Stellenanzeige (Stepstone) gefunden: Anwendungstechniker Mess-/Prüftechnik (langjähriger Mitarbeiter geht in Ruhestand), keine Produktions-/Vergussanzeige. Suche nach Vergussbezug ("Vergussmasse", "Gießharz", "IP68 epoxy"): kein Neosid-Treffer, der Begriff Verguss erscheint nirgends; das ist kein Gegenbeweis. Patentsuche (Anmelder Neosid, Verguss): kein Treffer mit Neosid-Anmelder; Datenbanken nicht abgefragt. Gründungsjahr uneinheitlich (1923/1933 in Quellen, S), ohne Einfluss.
- Korrekturen an Toms Feldern: Feld 4 ergänzen um Tochter NEOTECH (Polen) und Frage nach Produktionsaufteilung Halver/Polen; Feld 17 Gründungsjahr unsicher. CRM: neu.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Wird Neosid-Ware (Spulen/Induktivitäten/Transponder) in Halver gefertigt, oder teils bei NEOTECH in Polen/anderen Werken (Fertigungsbeleg V)? (b) Werden Spulen und Transponder vergossen, verklebt oder in Gehäuse gedichtet (Hoch bleibt A bis zum Beleg)? Wo nachsehen: Impressum und Standortseite neosid.de, Datenblätter (z. B. P 0724 NeoTAG), Karriereseite (Produktion, Vergießen, Montage), Handelsregister Iserlohn/Hagen (Gesellschafter). Patente: Google Patents/Espacenet/DEPATISnet mit Anmelder "Neosid Pemetzrieder" nachholen. Aktion: Browser-Gegenlesen vor Kontakt.
- Nicht verwendbare Aussagen: Fertigung Halver (S, Sitzregel nur A); Verguss aller Bauteile (A); Mitarbeiterzahl 80 (S); "patentierte Gehäusegeometrien" (S, keine Nummern). Stichprobe für Jey: ja (Toms einziger "interessant").

## 431. Neumonda GmbH | Stand C5.361
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Bestätigt: Basler Straße 5, 61352 Bad Homburg (embedded-world, aubi-plus, S); Gruppe aus Memphis Electronic (Distribution), Intelligent Memory (fabless DRAM/NAND) und Neumonda Technology (IP und Tester Rhinoe, Octopus, Raptor); Quellen von 2023 und älter (S). Eine Quelle nennt Oberursel als Sitz der Holding (Evertiq/eeNews, S). Keine Fertigung belegt, Verguss Niedrig (A). E2 nicht V.
- Korrekturen: Feld 4/17 ergänzen: Evertiq-Quelle nennt für die Holding Oberursel, Ausstellerseite Bad Homburg, aubi-plus nennt "Neumonda Holding" in Bad Homburg (S): Entität unterscheiden (Holding, Distribution, Technology). CRM: neu (Fehlalarm Intelligent Machines bestätigt).
- Nachrecherche-Auftrag (Gelb, Zeile 7): Werden die Neumonda-Tester (Neumonda Technology) selbst gebaut/montiert, und in DE? Wo nachsehen: Impressum neumonda.com, Produktseite Rhinoe/Octopus, Karriereseite. Bei Bestätigung reiner Distribution/fabless: Rot nach E2/E3 mit Quelle.
- Nicht verwendbare Aussagen: fabless-Status (S, 2023); Sitz (S, widersprüchlich Oberursel/Bad Homburg). Stichprobe für Jey: nein.

## 432. N&H Technology GmbH | Stand B3.361
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Willich (Gießerallee 21, 47877; eigenes Gebäude im Gewerbepark Stahlwerk Becker, Gründung 12.12.2000, S) mit Entwicklung, Prüflabor, Baugruppenmontage als Leistung; Produktion überwiegend im Partnernetzwerk Asien und Tochter Shanghai, Mehrheitsbeteiligung FoShan SNT (2023) (Katalog, S). Fertigung in Willich weder belegt noch widerlegt; Hinweis auf Auslandsfertigung, daher Sitzregel gesperrt. Verguss Mittel (A/S). Nicht Rot, da E3 "ausschließlich" nicht V-belegt ("Montage und Baugruppenfertigung" im Verzeichnis, Prüf- und Testlabor am Standort Willich).
- Korrekturen: Feld 15: aktuelle Mitarbeiterzahl 51, davon 13 Ingenieure (laut 2025-Unternehmensdokument im Suchtreffer, S); Tom nennt 42 (2022). CRM: neu.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Welche Produkte werden in Willich montiert/gespritzt/vergossen, welche stammen aus Asien (Fertigungsbeleg V für Willich)? Wo nachsehen: Impressum und Standortseite nh-technology.de, Fachartikel "25 Jahre N&H" (nh-technology.de/en/25-jahre-nh-technology), Karriereseite (Montage, Produktion), Katalog 2025. Wenn nur Asien: Rot nach E3 mit Quelle.
- Nicht verwendbare Aussagen: Montage Willich (S/?); IP68-Angabe (S); Verguss aller Bauteile (A); Mitarbeiterzahl (S). Stichprobe für Jey: ja (Grenzfall Fertigung Willich/Asien).

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind überall ehrlich niedrig (S/A, keine V vorgetäuscht). Seine Einstufung "interessant" bei Neosid halte ich nach Regel I für nicht bestätigt (Gelb 5, Tochter Polen).
- Nur zwei Quellenlücken von Tom, die meine Suche ergänzt hat: NanoFocus-Eigentümerlage (Squeeze-out 2025) und Neosid-Tochter NEOTECH. Beide ändern die Sitzregel-Anwendung.
- Vorschlag Fehlerlog (Jey gibt frei, nicht eingetragen): (1) Bei Eigentümerangaben aus Factsheets (NanoFocus 50,1 % von 2020) immer auf aktuelle Meldungen prüfen (Lehre 17). (2) Bei Herstellern mit ausländischer Tochter (Neosid, NEOTECH Polen) Sitzregel nur nach Werkprüfung.

## Einschränkungen
- Browser und WebFetch nicht verfügbar: kein Gegenlesen nach H, keine Impressen, Datenblätter oder Register gelesen; alle Aussagen Stufe S oder A. Keine "Zitat im Browser bestätigt: ja"; daher kein Grün möglich.
- WebSearch: 19 Abfragen mit Ergebnis, eine (NanoFocus-Patentstatus) am Sitzungslimit gescheitert. Schwerpunkt: Neosid (4), Muegge (3), NanoFocus (2), Multek (1), MultiOceans (2), municom (1), N&H (1), Nanya (1), NCAB (1), Neumonda (1), Neosid-Eigentümer (1).
- Patente: Datenbanken nicht abgefragt (Google Patents, Espacenet, DEPATISnet); Pflichtsuche F5 nicht erfüllt, Batch UNVOLLSTÄNDIG; Rechtsstände nur aus Toms Aggregator-Snippets (Justia, PitchBook) und nicht verwendbar.
- Wettbewerbereinsatz (F6): wettbewerber_referenzen.md nur bis Zeile 378 von 631 gelesen; Toms Grep (0 Treffer) nicht vollständig wiederholt.
- Handelsregister/Unternehmensregister nicht abgerufen; Kundendatenbank (Excel) nicht lesbar, kundendatenbank_export.txt ohne Treffer für alle zehn Firmen, keine "Verifiziert am"-Prüfung nötig.
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
