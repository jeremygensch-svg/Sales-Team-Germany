# Tom Batch 07 – all about automation Düsseldorf 2026 (Messemodus, Regel N)
Erstellt: 2026-10-15 (Tom, Stufe 1, Version 2, getrennter Agent, keine Ampel). Eingabe: aaa_batches_v2/pruef_06.md, 10 Firmen. Halle ist in der Liste nicht angegeben, Feld 1 trägt Standnummer. Stand/Sitz-Hinweise der Triage sind unverifiziert.
Abrufdatum aller Quellen: 2026-10-15. Belegstufen: V = selbst gelesen, S = Suchsnippet/WebFetch-Kurzfassung/Triage-Angabe (Seite nachlesen), A = aus Produkttyp abgeleitet, ? = angenommen.
WICHTIG zur Methodik: In diesem Lauf war nur WebSearch nutzbar (Snippet-Ergebnisse, daher alle Quellen höchstens Stufe S, nie V). WebFetch scheiterte bei jeder Domain mit DNS-Fehler (getaddrinfo ENOTFOUND, u. a. patents.google.com, worldwide.espacenet.com, kuebler.com, komaxgroup.com). Chrome-Werkzeuge (mcp__claude-in-chrome__*) standen nicht zur Verfügung: Browser nicht verfügbar. Das WebSearch-Limit (200 Aufrufe je Turn, geteilt) war nach den ersten Firmen erschöpft; für Lovato, Machine Creators, Magnescale und MB connect line konnte keine eigene Websuche mehr laufen (siehe Einschränkungen).
Messe-Signal (Regel N2): Grep auf aaa_duesseldorf_2026.csv nach Scheugenpflug, DOPAG, ViscoTec, Nordson, bdtronic, RAMPF, Sonderhoff, Hilger, Musashi, Henkel, DELO, Elantas, Wacker, Sika, Marco, GONANO, Atlas Copco, Graco, Panacol, Lohmann, OTTO-CHEMIE, EPOXONIC, WEVO, Hexion, Loctite, Dymax, dosier, dispens: kein Treffer. Komax (Firma 2 dieses Batches) ist selbst Anbieter von Dosieranlagen (siehe dort).
CRM-Abgleich: crm_abgleich.py mit Firma, Konzern, Altnamen und Kürzeln ausgeführt (Lehre 13); Ergebnisse je Firma in Feld 12.

## 1. KEYENCE Deutschland GmbH
1. Firma: KEYENCE Deutschland GmbH (Messe: all about automation Düsseldorf 2026, Stand 116, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Sensoren, Messsysteme), nur falls in DE gefertigt
3. Gebiet: Rest Deutschland+Niederlande (Neu-Isenburg, Hessen)
4. Sitz und Fertigungsort: Sitz laut Verzeichnissen Siemensstraße 1, 63263 Neu-Isenburg (S, Verzeichnis). Fertigung in DE/AT/NL nicht belegt; Konzern KEYENCE Corp., Osaka.
5. Website: https://www.keyence.de (laut Triage; Seite nicht gelesen)
6. Was wird gebaut: Sensoren, Messsysteme, Laser-Markierer, Bildverarbeitung (S, Verzeichnisprofile). Typisch vergossen: Sensoren Hoch (A, Block A), Bildverarbeitungs-/Steuerelektronik Mittel (A). Hersteller ist Mutter in Japan, die deutsche GmbH ist Vertrieb (S).
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Suchergebnisse (Wikipedia-Spiegel, Firmenprofil) beschreiben Keyence als Entwickler ohne eigene Fertigung (Auftragsfertiger); GlobalData nennt Fertigungs- und Lagerstandorte in Asien, Europa, Amerika ohne Ort. Stellenanzeigen Neu-Isenburg: nur Vertrieb/Produktmanagement (S), keine Montage. Konzernfall, V fehlt.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Sensoren, Block A). Einzelbewertung: Sensoren Hoch (A), Laser-Markierer Mittel (A), Vision-Kameras/Controller Mittel (A). Nutzen für Demak nur, wenn Fertigung DE belegt würde.
9. Patentrecherche (Pflicht, mind. 2 Suchen): Google Patents (nur indirekt per WebSearch "Keyence Corporation patent potting OR encapsulation OR Vergussmasse sensor housing"), DEPATISnet (nur indirekt per WebSearch "DEPATISnet Keyence Anmelder Vergussmasse OR Verguss"). Direkter Datenbankzugriff (Google Patents, Espacenet, DEPATISnet) war nicht möglich (WebFetch DNS-Fehler, Browser nicht verfügbar). Treffer: 0 mit Keyence als Anmelder in den Ergebnislisten; Fremd-Patente anderer Anmelder aussortiert. "Keine Treffer" ist hier nur ein Suchlücken-Befund, kein Gegenbeweis. Enge Nachsuche (Anmelder "Keyence Corp" / キーエンス) in Google Patents und Espacenet offen.
10. Einstufung Tom: kein Fertiger (Vertriebsgesellschaft, Fertigung bei Mutter/Auftragsfertigern, Stufe S; harter Ausschluss E2/E3 möglich, Tina entscheidet)
11. Ampel:
12. CRM-Status: neu. crm_abgleich.py "KEYENCE Deutschland GmbH" "KEYENCE Corporation": kein Treffer in bekannte_firmen_DE-AT-NL.txt und kundendatenbank_export.txt.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Gibt es ein Keyence-Werk in DE/AT/NL? Keyence.de Impressum/Standortseite und Handelsregister Offenbach HRB 11973 lesen; Patentsuche mit Anmelder "Keyence Corp" direkt in Google Patents und Espacenet nachholen. Aktion: keine, solange Fertigung DE unbelegt.
14. Quellen: https://www.bayern-innovativ.de/en/profiles/keyence/ (S): Snippet nennt „Siemensstraße 1, 63263 Neu-Isenburg“; https://en.wikipedia.org/wiki/Keyence (S, Sekundärquelle): Snippet „manufactured at qualified contract manufacturing companies“; https://daa-technikum.de/fileadmin/user_upload/Keyence-GmbH2-04-10-2024.pdf (S): Stelle „Junior Produktmanager“ in Neu-Isenburg; Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt (nicht gesucht)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Keyence); keine eigene Websuche zu Wettbewerber-Anlagen ausgeführt (Suchlimit, Firma ohne DE-Fertigung nachrangig). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: Name passt (Keyence Deutschland GmbH, Verzeichnisse S). Abweichung zur Vorgabe: Liste nennt PLZ 60549 Frankfurt (Messeliste), Verzeichnisse nennen 63263 Neu-Isenburg; Register laut Verzeichnis Offenbach HRB 11973 (S, nicht gegengelesen). Impressum nicht gelesen.

## 2. Komax Kabelverarbeitungssysteme Deutschland GmbH
1. Firma: Komax Kabelverarbeitungssysteme Deutschland GmbH (Messe: all about automation Düsseldorf 2026, Stand 413, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Kabelverarbeitungs-Maschinenbau; Berührung mit Demak-Kerngeschäft (Dosieren/Vergießen) als Anbieter, nicht als Anwender
3. Gebiet: Bayern (Nürnberg)
4. Sitz und Fertigungsort: Willstätter Strasse 95, 90449 Nürnberg (S, Impressum-Snippet). Rolle des Standorts: Vertrieb/Service, ca. 25 Beschäftigte (Bayern International, S). Gruppenwerke: Komax SLE Grafenau, Schleuniger Haan (laut Triage), Schließungen Wiedensahl, Jettingen, Sömmerda (Presse 2024, S).
5. Website: https://www.komaxgroup.com
6. Was wird gebaut: Maschinen zur Kabelverarbeitung (Crimp-to-Crimp, Konfektion). Zusätzlich bietet die Komax-Gruppe Mischen/Dosieren/Vergießen/Kleben an: Geräte von Giebler und Werner Wirth, Dosierzelle Alpha 6, Mischer 2-K-DOS Touch für 2K-Vergussmassen und Klebstoffe auf PU-, Epoxid-, Silikonbasis (S, komaxgroup.com/en-at/expertise/...). In den eigenen Maschinen verbaut: Antriebe, Sensorik, Steuerung (A, Mittel).
7. Fertigung DE/AT/NL: Niedrig, Stufe S für den Standort Nürnberg (nur Vertrieb/Service belegt); Konzern mit mehreren Werken, V nötig. Geschäftsbericht 2020 nennt Fertigung "an deutschen Standorten" ohne Nürnberg (S).
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Antriebe/Servo Mittel (A), Sensorik Mittel (A), Schaltschrank/Steuerung Mittel (A). Nutzen als Anwender fraglich.
9. Patentrecherche (Pflicht, mind. 2 Suchen): Google Patents (indirekt, WebSearch "Komax Patent Anmelder potting OR Vergussmasse OR Verguss ... patents.google.com"), Justia-Anmelderliste "Patents Assigned to Komax AG" als Ersatz für Espacenet/DEPATISnet (beide nicht direkt erreichbar). Ergebnis: Komax-AG-Patente betreffen Benetzung von Kabelenden (US7685964, angemeldet 2004, erteilt 2010), Montage von Steckergehäusen, Kabeltransport; kein Verguss-Patent. Treffer mit Eaton/anderen Anmeldern ("Cable assembly with protector", US8395044) sind fremd und aussortiert. Rechtsstand nicht geprüft. Espacenet/DEPATISnet: Lücke.
10. Einstufung Tom: Wettbewerber/Lieferant (Komax-Gruppe bietet Dosier-/Vergusssysteme an, E1, Stufe S; Zuordnung zur deutschen Vertriebsgesellschaft offen, Tina entscheidet)
11. Ampel:
12. CRM-Status: neu. crm_abgleich.py mit "Komax Kabelverarbeitungssysteme Deutschland GmbH", "Komax", "Komax AG", "Schleuniger": kein Treffer.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Vertreibt Komax Deutschland die Dosiergeräte (Giebler, Werner Wirth, 2-K-DOS, Alpha 6) in DACH? Komax-Seite "Sealing, bonding, and casting systems" und Produktlinie lesen. (b) Wird in Nürnberg montiert? (c) Gehören Schleuniger (Haan) und Komax SLE zum selben Unternehmen? Aktion: nicht als Neukunde ansprechen, bis (a) geklärt.
14. Quellen: https://www.komaxgroup.com/en-at/expertise/mixing-technology-dosing-technology-and-dispensing-technology (S): „2-K-DOS Touch mixer and proportioner quickly and precisely mixes and dispenses“; https://www.komaxgroup.com/de/imprint (S): Komax Deutschland GmbH, „Willstätter Strasse 95, 90449 Nürnberg“, „Amtsgericht Nürnberg, HRB 12581“; https://www.bayern-international.de/en/company-database/company-details/komax-deutschland-gmbh-20003 (S): Hersteller mit ca. 25 Beschäftigten; https://patents.justia.com/assignee/komax-ag (S); Abruf 2026-10-15.
15. Größe/Umsatz: Standort ca. 25 Beschäftigte (Verzeichnis, S); Konzern unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?); Komax ist selbst Anbieter. Suchen: wettbewerber_referenzen.md (kein Eintrag Komax); Websuche "Komax Kabelverarbeitung Kunde Nordson OR Scheugenpflug OR DOPAG OR Henkel OR Loctite Klebstoff Dosieren Referenz" (kein Kundenbezug). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: Abweichung. Vorgabe: "Komax Kabelverarbeitungssysteme Deutschland GmbH". Impressum-Snippet nennt "Komax Deutschland GmbH", HRB 12581 Nürnberg, Geschäftsführer Matthias Klaus (S); Verzeichnis führt den Langnamen. Konzern Komax Holding AG, Dierikon (CH). Impressum nicht im Volltext gelesen.

## 3. Kübler Group - Fritz Kübler GmbH
1. Firma: Kübler Group - Fritz Kübler GmbH (Messe: all about automation Düsseldorf 2026, Stand 426, Halle nicht angegeben) - BEKANNT
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Drehgeber, Sensorik, Zähler)
3. Gebiet: Baden-Württemberg (Villingen-Schwenningen)
4. Sitz und Fertigungsort: Schubertstraße 47, 78054 Villingen-Schwenningen (S, Betriebsanleitung). Gruppe mit Produktionsstandorten in Europa, Asien, USA (Pune, Charlotte laut Triage). Welche Produkte in Schwenningen entstehen: nicht belegt.
5. Website: https://www.kuebler.com (Domain in Suchergebnissen bestätigt, S)
6. Was wird gebaut: Inkremental-/Absolutdrehgeber, Sendix, Safety-Encoder, Zähler, Neigungssensoren, Schleifringe (S). Sendix 3651/3671 und 24-mm-Reihen mit "vollvergossener Elektronik" und IP69k (S, Fachpresse computer-automation.de). Typisch vergossen: Drehgeber-Elektronik Hoch (S/A), Magnetsensoren Hoch (A), Zähler Mittel (A).
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Konzern mit mehreren Werken (V nötig, fehlt); Werkserweiterung Schwenningen (industrial-production.de, undatiert, S) und Fachartikel mit "vier Produktionsstandorten" (S, widersprüchlich: Deutschland/Indien/USA vs. Europa/Asien/USA). Produkt-zu-Werk offen.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe S für Sendix (Fachpresse: vollvergossene Elektronik) und A aus Produkttyp (Drehgeber, Block A). Einzelbewertung: Drehgeber-Elektronik Hoch (S), Magnetgeber Hoch (A), Safety-Encoder Hoch (A), Zähler Mittel (A).
9. Patentrecherche (Pflicht, mind. 2 Suchen): Google Patents (indirekt, WebSearch "site:patents.google.com Fritz Kübler GmbH Drehgeber Vergussmasse" und "Kübler Drehgeber Patent potting encapsulation"), Espacenet (indirekt, WebSearch "Fritz Kübler GmbH Patent Drehgeber Gehäuse vergossen Verguss EP Espacenet"); direkter Zugriff Google Patents/Espacenet/DEPATISnet nicht möglich. Treffer: EP0995974 "Drehgeber" (Patentinhaber Fritz Kübler GmbH, Einspruch Heidenhain, EPO-Beschwerde T 1703/13 vom 2018-02-21; Gegenstand kein Verguss erkennbar; Rechtsstand nicht geprüft) und EP2867624 "multichannel rotary angle encoder" (Kübler, Beschwerde T 0614/19 vom 2022-09-29 gegen Widerruf; Rechtsstand offen, kein Verguss erkennbar). Kein Patent mit Vergussmasse/Verkapselung als Gegenstand gefunden. Zusatz: Sendix-Produkte mit "Sensor Protect"-Technik (vollvergossene Elektronik plus mechanische Baugruppe) laut Fachpresse (S), kein Patentbeleg. Enge Suche in DEPATISnet offen.
10. Einstufung Tom: prüfenswert (Fertigung Mittel S, Verguss Hoch S; durch CRM-Eintrag Rot-Kandidat E5, siehe Feld 12)
11. Ampel:
12. CRM-Status: BEKANNT (CRM-Schreibweise "Fritz Kübler GmbH [DE]", bekannte_firmen_DE-AT-NL.txt Zeile 860). crm_abgleich.py "Fritz Kübler" meldet IDENTISCH; kundendatenbank_export.txt kein Treffer. Gleiche juristische Einheit sehr wahrscheinlich (Name identisch, Sitz Villingen-Schwenningen); Ort im CRM nicht angegeben.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Bestandskontakt pflegen, kein Neukunde. Zu klären: Steht im CRM dieselbe Einheit (Ort VS)? Aktion: Jey bestätigt Einheit.
14. Quellen: https://www.computer-automation.de/sensoren/drehgeber-fuer-einsatz-in-nutzfahrzeugen.htm (S): Sendix 3651/3671 mit „vollvergossene Elektronik“; https://www.computer-automation.de/sensoren/in-24-mm-baugroesse.htm (S): „Sensor Protect“ mit vollvergossener Elektronik; https://legacy.epo.org/boards-of-appeal/decisions/pdf/t131703du1.pdf (S): Patent EP 0995974, Patentinhaber Fritz Kübler GmbH; https://www.industrial-production.de/wirtschaft---unternehmen/fritz-kuebler--werkserweiterung-schafft-platz-fuer-innovationen.htm (S): Erweiterungsbau Schwenningen; bekannte_firmen_DE-AT-NL.txt Zeile 860 „Fritz Kübler GmbH“; Abruf 2026-10-15.
15. Größe/Umsatz: mehr als 600 Beschäftigte (Unternehmensseite laut Suchsnippet, eine Quelle, S); Umsatz unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Kübler); keine eigene Websuche zu Wettbewerber-Anlagen ausgeführt (Suchlimit). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: Name passt (Fritz Kübler GmbH, Kübler Group), Adresse Schubertstraße 47, Villingen-Schwenningen (S, Betriebsanleitung); PLZ uneinheitlich (78054 gegen 78045 in einem Verzeichnis); Impressum kuebler.com nicht gelesen, Register nicht belegt. Vorgabe-Domain "kuebler.com unbestätigt": Domain in Suchergebnissen als Hersteller-Seite vorhanden (S).

## 4. Lanfer Automation + Robotics GmbH
1. Firma: Lanfer Automation + Robotics GmbH (Messe: all about automation Düsseldorf 2026, Stand 614, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Gasketing/Sealing (Schaltschrankbau), Electrical Insulation (Steuerungsbau); Systemintegrator
3. Gebiet: Rest Deutschland+Niederlande (Borken-Weseke, NRW)
4. Sitz und Fertigungsort: Hoher Weg 13, 46325 Borken (Register-Aggregator, S). Teil der LB GmbH, Bocholt (S). Schaltschrankbau/Anlagenbau am Sitz laut Eigenprofil (S).
5. Website: unbekannt (nicht gefunden; Messeprofil https://www.duesseldorf.allaboutautomation.de/en/exhibitors/lanfer-automation-robotics-gmbh-238600/ existiert, S)
6. Was wird gebaut: Pick/Pack/Palettier-Zellen, Maschinenbeladung, Intralogistik, Steuerungs- und Schaltschrankbau (S, Messeprofil/Karriereportal: "über 100 Mitarbeitende"). Typisch vergossen/verklebt/gedichtet: Schaltschränke (Dichtung, FIPFG) Mittel (A), zugekaufte Antriebe/Servos/Netzteile Mittel (A), Sensorik in Robotikzellen Mittel (A).
7. Fertigung DE/AT/NL: Mittel, Stufe A. Begründung: Sitzregel (Integrator mit erkennbarem Standort), aber Gruppenzugehörigkeit LB GmbH und kein Montage-Beleg: Stellenportal zeigt nur eine Vertriebsleiter-Stelle (S), keine Montageanzeige.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Schaltschrank-Dichtung Mittel (A), Antriebe Mittel (A), Steuerungselektronik zugekauft Mittel (A), Robotik-Greifer/Mechanik Niedrig (A).
9. Patentrecherche (Pflicht, mind. 2 Suchen): LÜCKE. Google Patents, Espacenet und DEPATISnet nicht abgefragt: WebSearch-Limit erschöpft, direkter Datenbankzugriff nicht möglich (WebFetch DNS-Fehler, Browser nicht verfügbar). Anmelder-Varianten für die Nachholung: "Lanfer Automation + Robotics", "LAR GmbH", "Lanfer Automation", "LB GmbH". Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: prüfenswert (Fertigung Mittel A, Verguss Mittel A)
11. Ampel:
12. CRM-Status: neu. crm_abgleich.py mit "Lanfer Automation + Robotics GmbH", "LB GmbH", "LAR GmbH": kein Treffer (Kürzel LB/LAR sind für den Abgleich sehr kurz, Treffer unzuverlässig).
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Wird der Schaltschrankbau in Borken-Weseke selbst gefertigt (Website, Karriereseite Elektroniker/Schaltschrankbauer)? (b) Eigene Website und Impressum ermitteln. (c) Patentsuche nachholen. (d) Gruppe LB GmbH Bocholt: weitere Einheiten? Aktion: Beobachtung.
14. Quellen: https://implisense.com/en/companies/lanfer-automation-robotics-gmbh-borken-DEP04EEC3A04 (S): „Lanfer Automation + Robotics GmbH“, HRB 20112 Borken, Amtsgericht Coesfeld (Snippet); https://www.stepstone.de/cmp/de/lanfer-automation-%2b-robotics-gmbh-171794/jobs (S): eine Stelle „Vertriebsleiter“; https://www.duesseldorf.allaboutautomation.de/en/exhibitors/lanfer-automation-robotics-gmbh-238600/ (S, Messeprofil: nie V); Abruf 2026-10-15.
15. Größe/Umsatz: über 100 Beschäftigte (Implisense/Messeprofil, S); Umsatz unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Lanfer); Websuche "Lanfer Automation Robotics Borken Schaltschrankbau Fertigung Stellenanzeige Montage" (keine Anlagen-/Materialnamen). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: Name stimmt (S). Handelsregister HRB 20112 (früher LAR GmbH, Verschmelzung mit Lanfer Automation Beteiligungs GmbH Dezember 2021, Umfirmierung 2022-01-10; Aggregator, S). Teil der LB GmbH Bocholt. Impressum der Firma nicht gelesen. Keine Abweichung zur Vorgabe.

## 5. LASIT LASER DEUTSCHLAND GMBH
1. Firma: LASIT LASER DEUTSCHLAND GMBH (Messe: all about automation Düsseldorf 2026, Stand 402, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Laser-/Steuerelektronik, Netzteile in Lasermarkieranlagen)
3. Gebiet: Baden-Württemberg (Immendingen)
4. Sitz und Fertigungsort: Im Stockacker 7, 78194 Immendingen (openPR, S). Produktion der Muttergesellschaft LASIT S.p.A. in Italien (Torre Annunziata/Vico Equense, Triage/openPR, S). Fertigung in Immendingen nicht belegt.
5. Website: unbekannt (lasit.com laut Triage unbestätigt)
6. Was wird gebaut: Lasermarkier- und Beschriftungssysteme (Triage, S). Typisch vergossen: Laserquelle/Netzteile Mittel (A), Steuerelektronik Mittel (A), Kabel/Stecker Mittel (A).
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Tochter eines italienischen Herstellers, openPR beschreibt "Expansion nach Deutschland" mit rund 100 Mitarbeitenden, nennt aber keine Produktion in Immendingen (Snippet abgeschnitten). Konzern: V nötig, fehlt.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Netzteile Mittel (A), Steuerelektronik Mittel (A), Laserquelle Niedrig (A, optisch-mechanisch), Gehäuse/Dichtung Niedrig (A).
9. Patentrecherche (Pflicht, mind. 2 Suchen): LÜCKE. Google Patents, Espacenet und DEPATISnet nicht abgefragt: WebSearch-Limit erschöpft, direkter Datenbankzugriff nicht möglich. Anmelder-Varianten für die Nachholung: "LASIT S.p.A.", "Lasit Laser Deutschland", El.En. S.p.A. (Konzern). Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: unwahrscheinlich (Fertigung Niedrig S; vorläufig, Patentsuche offen)
11. Ampel:
12. CRM-Status: neu. crm_abgleich.py mit "LASIT LASER DEUTSCHLAND GMBH", "LASIT", "El.En.": kein Treffer.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Wird in Immendingen montiert oder nur vertrieben/serviciert? Eigene Website/Impressum, Stellenanzeigen Immendingen (Montage, Elektroniker), openPR-Pressemeldung vollständig lesen. Patentsuche LASIT/El.En. nachholen. Aktion: Beobachtung.
14. Quellen: https://www.openpr.de/pressemitteilungen/lasit-0225428/ (S): „LASIT ist ein Unternehmen mit hundert Mitarbeitern“ und Adresse Im Stockacker 7, 78194 Immendingen; Abruf 2026-10-15.
15. Größe/Umsatz: ca. 100 Mitarbeitende (openPR, Pressemeldung der Firma, S); Umsatz unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag LASIT/El.En.); keine eigene Websuche zu Wettbewerber-Anlagen ausgeführt (Suchlimit). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: Name und Adresse nach openPR (S) passend; Impressum und Register nicht gelesen, Rechtsform in der Quelle nicht bestätigt. Mutter LASIT S.p.A. (IT), El.En.-Gruppe (Triage, S).

## 6. LinMot GmbH
1. Firma: LinMot GmbH (Messe: all about automation Düsseldorf 2026, Stand 310, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Linearmotoren, Servoantriebe), nur falls gefertigt
3. Gebiet: Rest Deutschland+Niederlande (Sitz Essen); Büro Burgoberbach in Bayern
4. Sitz und Fertigungsort: Sitz Essen, Büro Burgoberbach seit 2024; Mutter NTI AG, Spreitenbach (CH), produziert laut Triage in CH und SK. Das Unternehmen beschreibt Burgoberbach als Vertriebsbüro, nicht als Produktionsstandort (S).
5. Website: https://linmot.com
6. Was wird gebaut: Linearmotoren und Servoantriebe (Hersteller NTI AG). In Deutschland laut Blog: Engineering, Auftragsabwicklung, Buchhaltung, Reparaturservice, Aufbau von Demo-Modellen und Validierungstests (S). Typisch vergossen: Statorwicklungen/Linearmotoren Hoch (A, Block A), Antriebselektronik Hoch (A). Eigenfertigung in DE nicht belegt.
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Eigene Beschreibung nennt Vertrieb, Auftragsabwicklung, Reparatur; 20 Beschäftigte in Deutschland; Produktion bei der Mutter in der Schweiz/Slowakei (Triage, S).
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Linearmotor-Stator, Block A). Einzelbewertung: Motorwicklung Hoch (A), Servoantrieb-Elektronik Hoch (A), Reparaturen in Essen/Burgoberbach Mittel (?), Demo-Aufbauten Niedrig (A).
9. Patentrecherche (Pflicht, mind. 2 Suchen): LÜCKE. Google Patents, Espacenet und DEPATISnet nicht abgefragt: WebSearch-Limit erschöpft, direkter Datenbankzugriff nicht möglich. Anmelder-Varianten für die Nachholung: "NTI AG", "LinMot", "Linmot USA". Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: kein Fertiger (Vertriebs-/Service-Tochter, Stufe S; harter Ausschluss E2/E3 nicht endgültig belegt, Tina entscheidet)
11. Ampel:
12. CRM-Status: neu. crm_abgleich.py mit "LinMot GmbH", "NTI AG": kein Treffer.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Werden in Essen/Burgoberbach Reparaturen mit Wicklungs-/Motorarbeiten (Vergießen) durchgeführt oder Antriebe montiert? Blog-Seite linmot.com/blog/linear-linmot-gmbh/ vollständig lesen; Impressum; Patentsuche nachholen. Aktion: Beobachtung.
14. Quellen: https://linmot.com/blog/linear-linmot-gmbh/ (S): Burgoberbach als „sales office“, Aufgaben Auftragsabwicklung, Reparaturservice; https://www.stepstone.de/jobs/in-burgoberbach (S): Stelle technischer Innendienst, Aufbau von Demo-Modellen; Abruf 2026-10-15.
15. Größe/Umsatz: 20 Beschäftigte in Deutschland (Eigenaussage laut Snippet, eine Quelle, S)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag LinMot/NTI); keine eigene Websuche zu Wettbewerber-Anlagen ausgeführt (Suchlimit). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: Name stimmt mit Quelle überein (LinMot GmbH, Sitz Essen, S). Impressum und Handelsregister nicht gelesen. Abweichung zur Vorgabe: keine; Triage-Angabe "Büro Burgoberbach" bestätigt (S).

## 7. Lovato Electric GmbH
1. Firma: Lovato Electric GmbH (Messe: all about automation Düsseldorf 2026, Stand 802, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Schütze, Relais, Spulen, Netzteile)
3. Gebiet: Baden-Württemberg (Waldbronn, laut Triage)
4. Sitz und Fertigungsort: Im Ermlisgrund 30, Waldbronn (Triage, PDF-Quelle nicht gelesen, S). Konzernsitz Bergamo (IT). Fertigung Waldbronn: nicht belegt, Vertriebsniederlassung vermutet (Triage).
5. Website: https://www.lovatoelectric.com (laut Triage)
6. Was wird gebaut: Schütze, Relais, Motorschutz, Steuerungen, Niederspannungs-Schaltgeräte (Triage, S). Typisch vergossen: Spulen/Relais/Schütze Hoch (A, Block A), Netzteile Hoch (A), Steuerungen Mittel (A). Aussage gilt für das Konzernprodukt, nicht für Waldbronn.
7. Fertigung DE/AT/NL: Niedrig, Stufe ? (nicht recherchiert). Begründung: Tochter, Triage vermutet Vertrieb; kein Beleg für Montage in Waldbronn; Konzern, V nötig.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Schütze/Relais/Spulen, Block A). Einzelbewertung: Spulen Hoch (A), Relais Hoch (A), Netzteile Hoch (A), Steuerungen Mittel (A).
9. Patentrecherche (Pflicht, mind. 2 Suchen): LÜCKE. Google Patents, Espacenet und DEPATISnet nicht abgefragt: WebSearch-Limit erschöpft, direkter Datenbankzugriff nicht möglich. Anmelder-Varianten für die Nachholung: "Lovato Electric S.p.A.", "Lovato Electric". Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: unwahrscheinlich (vorläufig: Fertigung DE Niedrig, Stufe ?; nicht recherchiert, Nachrecherche erforderlich)
11. Ampel:
12. CRM-Status: neu. crm_abgleich.py mit "Lovato Electric GmbH", "Lovato Electric S.p.A.": kein Treffer.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Wird in Waldbronn gefertigt/montiert oder nur vertrieben? Impressum lovatoelectric.com/de, Handelsregister Mannheim/Karlsruhe, Stellenanzeigen Waldbronn. Patente Lovato Electric S.p.A. nachholen. Aktion: Beobachtung.
14. Quellen: Triage-Angabe aus pruef_06.md, selbst nicht abgerufen: https://download.lovatoelectric.com/PD034D04_24.pdf (S): Triage nennt „Waldbronn, Im Ermlisgrund 30“; Zitat aus der Triage übernommen; Abruf 2026-10-15 (nur Triage-Datei gelesen).
15. Größe/Umsatz: unbekannt (Familienkonzern laut Triage)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Lovato); keine Websuche ausgeführt (Suchlimit). Messe-Signal: keine Wettbewerber auf der aaa. Lücke.
17. Identität: nicht belegt. Name/Adresse nur aus Triage (S); Impressum und Register nicht gelesen. Konzern Lovato Electric S.p.A. (IT) laut Triage.

## 8. Machine Creators GmbH & Co. KG
1. Firma: Machine Creators GmbH & Co. KG (Messe: all about automation Düsseldorf 2026, Stand 434, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: unbekannt
3. Gebiet: Rest Deutschland+Niederlande (Meschede laut Messeliste, Stufe ?)
4. Sitz und Fertigungsort: Meschede, PLZ 59872 laut Messeliste (aaa_duesseldorf_2026.csv); Fertigungsort unbekannt.
5. Website: unbekannt
6. Was wird gebaut: unbekannt. Nur Vorgabe: gleicher Stand 434 und gleiche PLZ 59872 wie "Multimedial-Systeme" (Meschede, Triage nennt Wildshausener Str. 77); Verbindung nicht belegt (?). Keine Bauteil-Aussage möglich.
7. Fertigung DE/AT/NL: Niedrig, Stufe ? (Firma nicht auffindbar, keine Produkte bekannt)
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe ? (keine Information; Produkttyp unbekannt, daher kein A)
9. Patentrecherche (Pflicht, mind. 2 Suchen): LÜCKE. Google Patents, Espacenet und DEPATISnet nicht abgefragt: WebSearch-Limit erschöpft, direkter Datenbankzugriff nicht möglich. Anmelder-Variante für die Nachholung: "Machine Creators". Triage meldet: Firma per Websuche nicht auffindbar. Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: unwahrscheinlich (vorläufig: Identität und Produkte unbekannt, nicht auffindbar laut Triage, Stufe ?)
11. Ampel:
12. CRM-Status: neu. crm_abgleich.py mit "Machine Creators GmbH & Co. KG", "Multimedial-Systeme": kein Treffer.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Identität klären (Handelsregister Arnsberg/Meschede, Messeprofil auf allaboutautomation.de, Bezug zu Multimedial-Systeme). Danach Produkte und Fertigung. Aktion: Jey bestätigt Identität.
14. Quellen: aaa_duesseldorf_2026.csv Zeile „Machine Creators GmbH & Co. KG;434;59872;Meschede;Deutschland“; Triage aaa_batches_v2/pruef_06.md (S, Firma nicht auffindbar); Abruf 2026-10-15. Keine gelesene Webquelle; Ausstellerverzeichnis zum Nachlesen: https://www.duesseldorf.allaboutautomation.de/en/exhibitors/ (nicht abgerufen).
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag); keine Websuche ausgeführt (Suchlimit, Firma nicht identifiziert). Lücke. Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: NICHT belegt. Rechtsform, Adresse, Register unbekannt; Firma laut Triage per Websuche nicht auffindbar; Bezug zu Multimedial-Systeme (gleicher Stand 434, gleiche PLZ) nicht belegt. Gleichnamige Firmen nicht vermischt.

## 9. Magnescale Europe GmbH
1. Firma: Magnescale Europe GmbH (Messe: all about automation Düsseldorf 2026, Stand 621, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Wegmesssensorik, Längenmesssysteme)
3. Gebiet: Baden-Württemberg (Wernau)
4. Sitz und Fertigungsort: Wernau (Triage, laut DMG-MORI-Standortseite, S). Ob dort gefertigt oder nur vertrieben wird: nicht eindeutig (Triage).
5. Website: https://www.magnescale.com (laut Triage unbestätigt)
6. Was wird gebaut: Magnetische und Laser-Längenmesssysteme, Sensoren (Triage, S). Typisch vergossen: Wegmesssensoren/Messköpfe Hoch (A, Block A), Auswerteelektronik Mittel (A). Fertigungsort nicht belegt.
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Triage-Hinweis, DMG-MORI-Seite nenne einen Messsystem-Hersteller am Standort Wernau, "nicht eindeutig"; Konzern Magnescale Co. (JP) / DMG MORI, V nötig, fehlt. Seite nicht von mir gelesen.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Wegmesssensorik, Block A). Einzelbewertung: Messköpfe/Sensoren Hoch (A), Auswerteelektronik Mittel (A), Linear-Maßstäbe Niedrig (A).
9. Patentrecherche (Pflicht, mind. 2 Suchen): LÜCKE. Google Patents, Espacenet und DEPATISnet nicht abgefragt: WebSearch-Limit erschöpft, direkter Datenbankzugriff nicht möglich. Anmelder-Varianten für die Nachholung: "Magnescale Co.", "Sony Manufacturing Systems" (Vorgängerfirma, nicht belegt), "DMG MORI". Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: prüfenswert (Fertigung Mittel S, Verguss Hoch A; vorläufig, nicht selbst recherchiert)
11. Ampel:
12. CRM-Status: neu. crm_abgleich.py mit "Magnescale Europe GmbH", "Magnescale", "DMG MORI": kein Treffer.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Fertigt Magnescale Europe in Wernau (Stellenanzeigen Montage, DMG-MORI-Standortseite im Browser lesen)? Impressum und Handelsregister (Stuttgart/Esslingen). Aktion: Beobachtung.
14. Quellen: Triage-Angabe aus pruef_06.md, selbst nicht abgerufen: https://en.dmgmori.com/company/locations/wernau (S): Triage zitiert „Hersteller magnetischer Messsysteme am Standort, nicht eindeutig“; Abruf 2026-10-15 (nur Triage-Datei gelesen).
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Magnescale/DMG MORI); keine Websuche ausgeführt (Suchlimit). Lücke. Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: nicht belegt. Name/Ort nur aus Messeliste und Triage (S); Impressum und Register nicht gelesen. Konzernbezug DMG MORI/Magnescale Co. laut Triage.

## 10. MB connect line GmbH
1. Firma: MB connect line GmbH (Messe: all about automation Düsseldorf 2026, Stand 615, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation / Gasketing (IIoT-Router, Gateways in Industriegehäusen)
3. Gebiet: Bayern (Dinkelsbühl)
4. Sitz und Fertigungsort: Winnettener Str. 6, 91550 Dinkelsbühl (Triage, Quelle Messe-Ausstellerseite, S). Fertigung am Sitz laut Eigenangabe "developed and manufactured in Germany" (Ausstellertext, S).
5. Website: https://www.mbconnectline.com (laut Triage)
6. Was wird gebaut: Fernwartungs-Router mbNET, IIoT-Gateways (Triage, S). Typisch vergossen/verklebt/gedichtet: Elektronikbaugruppen/Netzteile in Gehäusen Mittel (A, Block B), Gehäusedichtung/Gehäuseverklebung Mittel (A), Industrierouter-Leiterplatten mit Schutzlack Mittel (A). Kein Beleg für Verguss.
7. Fertigung DE/AT/NL: Hoch, Stufe A. Begründung: Sitzregel (Gerätebauer mit eigenen Produkten, erkennbarer Standort Dinkelsbühl, keine Hinweise auf Auslagerung). Eigenangabe "manufactured in Germany" stammt aus einem Aussteller-Beschreibungstext (Stufe S, Regel N5), kein V. Konzernbezug nicht geprüft.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Netzteil/Elektronikbaugruppe Mittel (A), Gehäuse/Dichtung Mittel (A), Antennen/Stecker Niedrig (A).
9. Patentrecherche (Pflicht, mind. 2 Suchen): LÜCKE. Google Patents, Espacenet und DEPATISnet nicht abgefragt: WebSearch-Limit erschöpft, direkter Datenbankzugriff nicht möglich. Anmelder-Varianten für die Nachholung: "MB connect line", "MB connectline". Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: prüfenswert (Fertigung Hoch A, Verguss Mittel A; vorläufig, nicht selbst recherchiert)
11. Ampel:
12. CRM-Status: unklar. crm_abgleich.py "MB connect line GmbH" und "MB connectline": kein Treffer. Nur das Kürzel "MB" liefert IDENTISCH (bekannte_firmen_DE-AT-NL.txt Zeile 1563, "MB [DE]", ohne Ort). Kürzel kann dieselbe Firma sein (Lehre 13), Zuordnung nicht möglich. Konzern/Mutter von MB connect line nicht geprüft.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Ist CRM-Eintrag "MB" [DE] (Zeile 1563) MB connect line? Jey prüft in der Kundendatenbank (Ort Dinkelsbühl?). (b) Wird in Dinkelsbühl gefertigt (Impressum, Stellenanzeigen Montage/Produktion)? (c) Gehört MB connect line zu einem Konzern? (d) Patentsuche nachholen. Aktion: nicht kontaktieren, bis (a) geklärt.
14. Quellen: Triage-Angabe aus pruef_06.md, selbst nicht abgerufen: https://gitex.german-pavilion.com/en/sites/exhibitors/126386 (S, Ausstellertext): Triage zitiert „developed and manufactured in Germany“, Adresse Winnettener Str. 6, Dinkelsbühl; bekannte_firmen_DE-AT-NL.txt Zeile 1563 „MB“; Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag MB connect line); keine Websuche ausgeführt (Suchlimit). Lücke. Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: nicht belegt. Name/Adresse nur aus Triage (Ausstellerseite, S); Impressum und Register nicht gelesen. Abweichung: CRM-Kürzel "MB" ohne Ortsangabe, Zuordnung offen.

## nicht aufgenommen (bereits bekannt / unklar)
- BEKANNT: Kübler Group - Fritz Kübler GmbH (Messe-Schreibweise) = CRM "Fritz Kübler GmbH [DE]" (bekannte_firmen_DE-AT-NL.txt Zeile 860). Block oben mit Vermerk BEKANNT geführt, damit die Liste vollständig bleibt.
- unklar: MB connect line GmbH gegen CRM "MB" [DE] (Zeile 1563), Kürzel ohne Ort (siehe Feld 12 Firma 10).
- Keine weiteren Treffer in bekannte_firmen_DE-AT-NL.txt oder kundendatenbank_export.txt.

## Einschränkungen
- Browser nicht verfügbar: Chrome-Werkzeuge (mcp__claude-in-chrome__*) standen in diesem Lauf nicht zur Verfügung; kein Gegenlesen (Abschnitt H). Daher keine Aussage mit Stufe V.
- WebFetch: jede Abfrage scheiterte mit DNS-Fehler (ENOTFOUND), darunter patents.google.com, worldwide.espacenet.com, kuebler.com, komaxgroup.com. Keine Seite wurde im Volltext gelesen; alle Quellen sind Suchsnippets (Stufe S) oder Triage-Angaben.
- WebSearch-Limit (200 Aufrufe je Turn, geteilt) erschöpft nach den Recherchen zu Keyence, Komax, Kübler, Lanfer, LASIT, LinMot. Für Lovato Electric, Machine Creators, Magnescale Europe und MB connect line wurde keine einzige Websuche ausgeführt; ihre Angaben stammen allein aus der Triage (pruef_06.md), dem CRM-Abgleich und Produkttyp (Stufe A).
- Patentrecherche (F5): Weder Google Patents noch Espacenet noch DEPATISnet waren direkt erreichbar. Keyence, Komax und Kübler wurden nur indirekt per WebSearch geprüft; Lanfer, LASIT, LinMot, Lovato, Machine Creators, Magnescale und MB connect line wurden gar nicht gesucht. Feld 9 ist für diese sieben Firmen eine LÜCKE (Batch UNVOLLSTÄNDIG), nicht "keine Treffer".
- Wettbewerbereinsatz (F6): Nur Abgleich mit wettbewerber_referenzen.md (kein Eintrag zu einer der 10 Firmen) und für Komax, Lanfer je eine Websuche; für die übrigen Firmen keine Einzelsuche.
- Identität (Feld 17): Bei keiner Firma wurde ein Impressum im Volltext gelesen; Abweichungen: Keyence (PLZ Neu-Isenburg gegen Frankfurt), Komax (Name im Impressum "Komax Deutschland GmbH"), Machine Creators (nicht auffindbar).
- Komax: Einstufung Wettbewerber/Lieferant beruht auf einem Suchsnippet der Gruppenseite (Stufe S); ob die deutsche Vertriebsgesellschaft die Dosiergeräte anbietet, ist offen.
- Keine Kontaktsuche (Regel K) ausgeführt.
