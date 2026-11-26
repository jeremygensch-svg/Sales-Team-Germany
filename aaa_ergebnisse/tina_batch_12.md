# Tina Batch 12 – all about automation Düsseldorf 2026 (Prüfung von tom_batch_12.md)
Erstellt: 2026-10-15 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe: ausschließlich aaa_ergebnisse/tom_batch_12.md (10 Firmen).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (22 Abfragen, Kurzfassungen/Snippets) und Bash zur Verfügung; WebFetch und Chrome nicht nutzbar. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün vergeben; nichts ist mailtauglich.
Skripte: `python3 batch_check.py aaa_ergebnisse/tom_batch_12.md` = VOLLSTÄNDIG (10 Blöcke; Toms Einschränkung zu Feld 9/16 bleibt, Skript prüft nur Felder). `python3 crm_abgleich.py` für alle Firmen samt Konzern-/Altnamen selbst wiederholt: neu bei allen außer TRsystems (siehe 8). Tabellenzeile = Zeilennummer der Ampel-Tabelle D (regeln_tom_tina.md).
Verifikationsdatum aller Einträge: 2026-10-15.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel (vorläufig) | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | Spectra GmbH & Co. KG (411) | GELB | 5 | nein |
| 2 | Stiwa AMS GmbH (423) | GELB | 5 | ja |
| 3 | Stiwa Automation* (423) | GELB | 5 | nein |
| 4 | SW Automatisierung GmbH (234) | GELB | 6 | nein |
| 5 | Tele Radio GmbH (119) | GELB | 5 | nein |
| 6 | Telemeter Electronic GmbH (440) | GELB | 5 (Rot-Kandidat E2) | ja |
| 7 | TIVAL Sensors GmbH (215) | GELB | 5 | ja |
| 8 | TRsystems GmbH (409) | GELB | 3 (Rot-Kandidat E5) | ja |
| 9 | Unitronics GmbH (612) | GELB | 2 (Rot-Kandidat E2/E3) | ja |
| 10 | Vision Center GmbH (238c) | GELB | 2 | ja |

Zahlen: Grün 0, Gelb 10, Rot 0. Kein Rot, weil kein harter Ausschluss mit Stufe V belegt ist (Zeile 1 verlangt V bzw. dieselbe Einheit im CRM bestätigt).

Patente (Prüfpunkt 8, F5): Google Patents, Espacenet und DEPATISnet waren nicht abfragbar. Eigene Zusatzsuche nur für Telemeter (kein Patent, nur Verzeichnisse). Feld 9 ist bei ALLEN 10 Firmen nicht belastbar; Batch nach F5 UNVOLLSTÄNDIG (Datenbankabfrage), Nachholen im Browser nötig, bevor irgendein Grün final wird. Wettbewerbereinsatz (F6): Listenabgleich bei Tom ohne Treffer; ich habe keine eigene Einzelsuche wiederholt (ohne Einfluss auf Ampel).

---

## 1. Spectra GmbH & Co. KG | Stand 411
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Mischform Hersteller/Händler; Fertigung in Reutlingen nur durch Verzeichnis gestützt (S). Verguss Mittel (A: Panel-PC-Display/Touch, IP65-Frontdichtung, Elektronik).
- Eigene Prüfung: it-in-germany (S): "Herstellung und Entwicklung von Industrie-PCs" und Handel mit IPC-Komponenten; EtherCAT-Profil (S) nennt "trading in components ... and development and production of industrial PC systems" im Imperfekt, kann veraltet sein. Adresse Mahdenstr. 3, 72768 Reutlingen konsistent (Wiley, Verzeichnis). Schwester Spectra (Schweiz) AG ist eine andere Gesellschaft. ICP Deutschland seit 14.07.2025 Teil von Spectra (S). Kein Hinweis auf Optical Bonding (Suche "PowerTwin verklebt/Optical Bonding": nichts; IP65-Front ohne Angabe der Bauweise). Sitzregel nicht sicher anwendbar (Händleranteil).
- Korrekturen an Toms Feldern: keine. CRM: neu (Spectra, ICP Deutschland). Identität (Feld 17) bleibt S, kein Impressum gelesen.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Werden die Spectra-Panel-PCs in Reutlingen montiert (eigene Fertigung) oder zugekauft/konfektioniert? Wo nachsehen: spectra.de Impressum/Über uns, Karriereseite (Montage/Test), Datenblatt PowerTwin ("Made in"), Stellenanzeigen. Zusatz: Ist die Front optisch verklebt/gedichtet (Datenblatt, IP65-Konstruktion)?
- Nicht verwendbare Aussagen: Fertigung Reutlingen (S); Verguss/Bonding aller Bauteile (A); "Produktion" aus EtherCAT-Profil (S, evtl. veraltet). Stichprobe Jey: nein.

## 2. Stiwa AMS GmbH | Stand 423
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Identität gegenüber Tom jetzt gestützt: Firmenbuch-Suchtreffer (S, evi.gv.at / firmenbuchgrundbuch.at) "STIWA AMS GmbH, FN 103503k, Salzburger Straße 52, 4800 Attnang-Puchheim", GmbH seit 21.06.1994; WKO nennt dieselbe Adresse, Domain ams-engineering.com. Zeile 2 daher nicht ausgelöst. Aber: Konzern mit mehreren Standorten (Stufe V nötig), und welche Einheit was fertigt, ist offen.
- Eigene Prüfung: Fertigung von Serienprodukten läuft laut stiwa.com (Snippet) in Gampern (STIWA Manufacturing: haptische Bedienelemente, adaptive Dämpfung, Smart Locking, Spritzguss, Stanzen, Komponentenmontage; Einseiter 11/2025 "mechatronische Baugruppen für Leistungselektronik/Hochvolt", S). Ob die AMS GmbH selbst fertigt oder Engineering betreibt, ist nicht belegt (Leistungen von ams-engineering.com nicht gefunden). In der Firmenbuch-Zusammenfassung steht ein Eintrag "Spaltung" März 2022 (Zuordnung zur AMS nicht geprüft). Hinweis: "AMS Research GmbH" unter gleicher Adresse nicht vermischen. Verguss Mittel (A: Elektronik-/Hochvolt-Baugruppen, Typ offen; Verguss/Kleben am Standort Gampern nicht belegt).
- Korrekturen an Toms Feldern: Feld 17 aktualisiert (Gesellschaft existiert: FN 103503k; Schwestern STIWA Automation GmbH FN 295396g, STIWA Holding GmbH FN 105266d, jeweils S). Feld 12: CRM neu bestätigt (Stiwa AMS, STIWA Group, Stiwa Holding).
- Nachrecherche-Auftrag (Gelb, Zeile 5): Welche Produkte fertigt/montiert die STIWA AMS GmbH selbst, und gehören sie zur Fertigung in Gampern/Attnang (STIWA Manufacturing Austria)? Enthalten sie vergossene/verklebte Teile (Sensor-, Leistungselektronik)? Wo nachsehen: Firmenbuchauszug FN 103503k (Gegenstand, Spaltung 2022), ams-engineering.com Impressum/Leistungen, stiwa.com/en/manufacturing und OnePager Electrification, Karriereseiten Gampern (Montage).
- Nicht verwendbare Aussagen: Fertigung/Einheit (S); Verguss (A); Umsatz 340 Mio. (S, eine Quelle); "18 Patente" (S, Aggregator). Stichprobe Jey: ja (Einheitenzuordnung im Konzern).

## 3. Stiwa Automation* | Stand 423
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, niedrige Priorität).** Gesellschaft belegt (S): STIWA Automation GmbH, FN 295396g, Attnang-Puchheim (WKO, Eulerpool). Fertigung dort Konzern mit mehreren Werken (Sitzregel greift nicht ohne V). Gebaut werden Montage- und Automationsanlagen (Anlagenbau); Verguss Niedrig (A), da Endprodukt Maschine.
- Eigene Prüfung: Referenzdatenblätter stiwa.com (S): Anlagen für DC/DC-Inverter (Plasma, Kleben, Pressen), Trennschalter (Dosieren), Injektionsnadeln (Kleber dosieren + UV-Härtung), Blutröhrchen (Sprühen/Dosieren). Das sind Prozessstationen in Kundenlinien, kein Beleg für ein eigenes Dosier-/Vergussanlagenprogramm: E1 nicht belegt, also nicht Rot. Der Auftrag von Tom (Wettbewerbsnähe) bleibt offen. Wettbewerbereinsatz: keine Wettbewerbernennung gefunden.
- Korrekturen an Toms Feldern: Feld 17 präzisiert (eigene Gesellschaft FN 295396g, nicht Duplikat von AMS); Sternchen aus der Liste bleibt unerklärt. Feld 7: Hoch (A) von Tom ist unter Konzernvorbehalt zu streng, ich setze Mittel (A, Sitzregel nicht anwendbar).
- Nachrecherche-Auftrag (Gelb, Zeile 5): Wird in Attnang-Puchheim gefertigt (Anlagenbau am Standort, V aus Impressum/Stellenanzeige) und bietet die Firma eigene Dosier-/Klebeanlagen als Produkt an (E1-Prüfung)? Wo nachsehen: stiwa.com/en/automation Produktseiten, Impressum, Stellenanzeigen Anlagenbau Attnang. Aktion: nur zusammen mit Nr. 2, sonst nicht priorisieren (Verguss Niedrig).
- Nicht verwendbare Aussagen: Fertigung Hoch (A); "keine vergossenen Teile" (A); Umsatz (S). Stichprobe Jey: nein.

## 4. SW Automatisierung GmbH | Stand 234
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6).** Identität gegenüber Tom jetzt gestützt: Firmenbuch (S): FN 196242t, SW Automatisierung GmbH, Holzerfeld 397, 5440 Golling an der Salzach, eingetragen 20.06.2000; Anschrift stimmt mit karriere.at überein. Maschinenbauer (WireTerminal) mit erkennbarem Standort: Fertigung Golling Mittel/Hoch (A, Sitzregel). Alle plausiblen Bauteile Niedrig (Crimp-/Schneidmechanik, zugekaufte Steuerung, Schaltschrankbau): Tom "unwahrscheinlich" bestätigt.
- Korrekturen: Feld 4/17: Golling bestätigt (S, Firmenbuch). CRM: neu. Kein Patent von mir geprüft.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Enthält ein Produkt (WireTerminal-Maschine, Schaltschrank-Elektronik) Dosier-, Dicht-, Klebe- oder Vergussschritte, oder wird Elektronik selbst gefertigt? Wo nachsehen: Produktseite sw-wireterminal.com/Datenblatt C3000, Stellenanzeigen Golling (karriere.at/f/sw-automatisierung). Aktion: niedrige Priorität.
- Nicht verwendbare Aussagen: Fertigung Golling (A/S); Verguss (A); "patented WireRails" (S, keine Nummer). Stichprobe Jey: nein.

## 5. Tele Radio GmbH | Stand 119
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Industrie-Funkfernsteuerungen, Verguss Mittel (A: Funk-/Empfängerelektronik, Gehäusedichtung). Fertigung Schierling nicht belegt; Gruppe (Tele Radio/Allgon AB, über 20 Töchter): Stufe V nötig.
- Eigene Prüfung: Hauptsitz Schierling, Flurweg 12 (2018, S); Presse 03/2026 aus Schierling (LogiMAT, S). Eigene Stellenanzeigen in Schierling sind nur Elektrokonstrukteur/Werkstudent im "Sonderanlagenbau" (tele-radio.com PDFs, S), keine Montage/Produktion. Selbstbeschreibung "develops, produces and markets" (S, Gruppe). Kein Hinweis auf deutsche Fertigung in Allgon-Quellen; Sonderanlagenbau in Schierling deutet auf Konstruktion/Konfektion. CRM: neu (Tele Radio, Allgon, Tele Radio AB).
- Korrekturen: keine; Feld 7 Mittel/S bestätigt.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Werden Handsender/Empfänger in Schierling montiert (V) oder nur in Schweden/Asien gefertigt? Wo nachsehen: tele-radio.com/de Impressum und Über uns, Allgon-Geschäftsbericht (Produktionsstandorte), Stellenanzeigen Produktion/Test Schierling, Sonderanlagenbau-Beschreibung.
- Nicht verwendbare Aussagen: Fertigung Schierling (S/?); Verguss (A); Konzernstruktur (S). Stichprobe Jey: nein.

## 6. Telemeter Electronic GmbH | Stand 440
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5; Rot-Kandidat E2).** Pressemeldung (S, deutscherpresseindex) beschreibt die Firma als "zertifiziertes Vertriebs- und Dienstleistungsunternehmen"; Baugruppen "aus eigener Entwicklung" sind für Serienbedarf möglich, es werden Entwicklungs- und Fertigungspartner genannt (Hinweis auf externe Fertigung). Ein Firmenprofil führt sie zusätzlich als Hersteller. E2 ist inhaltlich stark, aber nicht V, daher nicht Rot.
- Eigene Prüfung: Donauwörth, Joseph-Gänsler-Str. 10, Logistikzentrum, ca. 62 bis 70 Mitarbeiter (S, Verzeichnisse). Patentsuche (Websuche): nichts. CRM: neu.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Fertigt die Firma eigene Baugruppen in Donauwörth, oder ist sie reiner Vertrieb/Service mit externen Fertigungspartnern (dann Rot nach E2)? Wo nachsehen: telemeter.info Über uns/Impressum, Pressemeldung im Original, Stellenanzeigen (Produktion/Montage/Test), Handelsregister Augsburg (Gegenstand).
- Nicht verwendbare Aussagen: Eigenfertigung (S/?); Verguss HF-Module (A); Mitarbeiterzahl (S). Stichprobe Jey: ja (Rot-Kandidat).

## 7. TIVAL Sensors GmbH | Stand 215
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Verguss Hoch (A, Drucktransmitter/elektronische Druckschalter, Block A). Fertigung Wuppertal nicht belegt: ob Hersteller oder Anbieter zugekaufter Geräte, ist offen; Sitzregel deshalb nicht angewendet.
- Eigene Prüfung: Identität gestützt (S): Bloomberg-LEI nennt HRB 19302, Amtsgericht Wuppertal, aktiv, Eintrag 15.08.2005; Verzeichnis: Oberdörnen 74, 42283 Wuppertal, gegründet 2005 von Hartmut Linde. Messeprofil: "specialized in mechanical pressure switches and sensors for more than 20 years", ATEX/GL/VdS-Zulassungen, kundenspezifische Ausführungen (S); ein Hersteller-Hinweis (A), aber kein Fertigungsbeleg. Eigene Website nicht gefunden. Cylex-"closed" (Tom) nicht erneut gesehen; Aktualität offen. CRM: neu.
- Korrekturen an Toms Feldern: Feld 17: HRB 19302 Wuppertal (S) ergänzt. Einstufung "prüfenswert" bestätigt; wird Grün, sobald Sitzregel/Fertigung belegt.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Werden Druckschalter/Transmitter in Wuppertal montiert/kalibriert (Hersteller) oder zugekauft? Wo nachsehen: Website (tival-sensors.de/.com; Domain finden), Impressum, Zulassungsdokumente ATEX (Herstellername/Adresse auf Typenschild/Zertifikat), Handelsregister Wuppertal HRB 19302 (Gegenstand), Stellenanzeigen.
- Nicht verwendbare Aussagen: Fertigung Wuppertal (A/S); Verguss aller Bauteile (A); "Hersteller" (A). Stichprobe Jey: ja (hohes Potenzial, offener Fertigungsbeleg).

## 8. TRsystems GmbH | Stand 409 | BEKANNT-Vermerk
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 3, CRM-Konzernbezug; Rot-Kandidat E5).** crm_abgleich.py "TR-Electronic GmbH": IDENTISCH bekannte_firmen_DE-AT-NL.txt Zeile 2386 "TR-Electronic GmbH [DE]" und PRAEFIX Zeile 2385 "TR ELECTRONIC / TR SYSTEMS [DE]". "TRsystems" allein liefert wegen Leerzeichen im Kern-Namen keinen Direkttreffer; die CRM-Zeile 2385 nennt TR SYSTEMS aber ausdrücklich. TRsystems ist Tochter der TR-Electronic (Trossingen, S: TRgroup-Katalog, Bloomberg-LEI TR Electronic GmbH HRB 460344 Stuttgart, Eglishalde 6). Die CRM-Zeile hat keinen Ort, die Einheit ist daher nicht V-bestätigt: nicht Rot, sondern Jey bestätigt. Bei Bestätigung: Rot nach E5 (Bestandskontakt pflegen).
- Eigene Prüfung: Fertigung/Entwicklung "in Germany" laut TRgroup-Katalog (S), Industrie-PC-Hersteller laut EtherCAT-Profil (S); Fertigungsort TRsystems nicht belegt. kundendatenbank_export.txt: kein Treffer. Wegen CRM-Bezug keine weitere Fertigungsprüfung nötig.
- Korrekturen an Toms Feldern: Feld 12 bestätigt (BEKANNT/Konzernbezug); Zeilen 2385/2386 bestätigt. Pforzheim/Unidor weiter ungeklärt.
- Nachrecherche-Auftrag (Gelb, Zeile 3): Jey: Umfasst der CRM-Eintrag "TR ELECTRONIC / TR SYSTEMS" die TRsystems GmbH, Trossingen (Handelsregister Stuttgart; Adresse im CRM-Datensatz)? Wo nachsehen: CRM-Datensatz Zeile 2385 mit Adresse, Impressum trsystems.de. Aktion: nicht als Neukunde kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Trossingen (S); Verguss (A). Stichprobe Jey: ja.

## 9. Unitronics GmbH | Stand 612
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität; Rot-Kandidat E2/E3).** Eine "Unitronics GmbH" mit Register/Impressum in Esslingen ist nicht belegt: Indeed zeigt 7 Stellen in Esslingen (u. a. Regional Sales Manager, S), zwei Registerhinweise sind nicht zuordenbar (OpenRegister HRB B2609-213929, Zeppelinstraße 100 Esslingen: Name im Snippet nicht erkennbar, keine Zuordnung). Hersteller ist die Unitronics (1989) (R"G) Ltd., Israel. Die gleichnamig ähnliche UNITRONIC GmbH (Neuss, Elektro-Großhandel, Lagercrantz) ist eine andere Firma.
- Eigene Prüfung: Keine Quelle für Fertigung in DE/AT/NL; Esslinger Stellen sind Support/Vertrieb (S). Verguss Produkt Mittel (A, SPS), aber nicht am deutschen Standort. CRM: neu.
- Korrekturen: keine; Tom "kein Fertiger" vorläufig bestätigt, nicht Rot, weil E2/E3 nicht V belegt.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Existiert eine Unitronics GmbH in Esslingen (Handelsregister Stuttgart, Impressum unitronics.com/de)? (b) Falls ja: nur Vertrieb/Support (dann Rot nach E2/E3 mit Quelle) oder auch Montage/Konfektion? Wo nachsehen: Handelsregister Amtsgericht Stuttgart, Impressum deutsche Unitronics-Seite, Aussteller-Profil aaa Stand 612.
- Nicht verwendbare Aussagen: GmbH-Sitz Esslingen (S); Fertigung Israel (S); Verguss (A). Stichprobe Jey: ja (Rot-Kandidat).

## 10. Vision Center GmbH | Stand 238c
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Auch meine Zusatzsuchen (zwei Anfragen, mit Schwerte/58239/Bildverarbeitung) finden keine Vision Center GmbH in Schwerte. Gleichnamige Firmen anderen Ortes (Vision Center GmbH & Co. KG, Bonn; Vision Center Bayreuth GmbH, Zeiss-Optikfilialen, S) und Bildverarbeiter (Vision & Control Suhl, u. a.) sind andere Gesellschaften und werden nicht vermischt. Produkt, Website, Fertigung unbekannt (?). Weder Verguss noch Fertigung ableitbar.
- Korrekturen: keine. CRM: neu (generischer Name, Abgleich schwach).
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer ist die ausstellende "Vision Center GmbH" (Stand 238c, PLZ 58239 Schwerte): Produkt, Website, Handelsregister (Amtsgericht Hagen)? Wo nachsehen: aaa-Ausstellerseite Stand 238c (Einzelseite des Ausstellers), Handelsregister Hagen, Messekatalog. Aktion: nicht kontaktieren, bis Identität geklärt.
- Nicht verwendbare Aussagen: alles (kein Beleg außer Messeliste). Stichprobe Jey: ja.

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind durchgehend korrekt niedrig (keine vorgetäuschte V-Aussage). Zwei Identitätsfälle (Stiwa AMS, SW Automatisierung) haben sich durch Firmenbuch-Suchtreffer (S) entschärft, bleiben aber nicht V.
- Tom hat TRsystems korrekt als CRM-Bezug erkannt; Ampel-Zeile 3 statt Rot, bis Jey die Einheit bestätigt.
- Fehlerlog-Vorschlag (Jey gibt frei, nicht eingetragen): CRM-Kern-Name-Normalisierung trennt "TRsystems" und "TR SYSTEMS" nicht; Firmennamen immer auch mit Leerzeichen/Wortgrenzen-Variante an crm_abgleich.py übergeben.

## Klärungsbedarf Jey
TRsystems (CRM-Einheit 2385/2386), Unitronics (GmbH Esslingen, E2/E3), Vision Center (Identität), Telemeter (E2), TIVAL (Hersteller?), Stiwa AMS und Stiwa Automation (Einheiten im Konzern).

## Einschränkungen
- Browser und WebFetch nicht verfügbar: kein Gegenlesen nach Abschnitt H; kein Impressum, Datenblatt, Firmenbuchauszug oder Handelsregister selbst gelesen. Alle Aussagen Stufe S oder A. Keine "Zitat im Browser bestätigt: ja".
- WebSearch: 22 Abfragen (Spectra 3, Stiwa AMS 3, Stiwa Automation 1, SW Automatisierung 1, Tele Radio 3, Telemeter 2, TIVAL 3, TRsystems 2, Unitronics 2, Vision Center 2). Ergebnisse sind Kurzfassungen und Verzeichnisse. Die Suchkontingentgrenze (~30) wurde nicht ausgeschöpft.
- Patente (F5): Google Patents, Espacenet, DEPATISnet nicht abgefragt; Rechtsstände nicht prüfbar; Batch UNVOLLSTÄNDIG im Sinne F5. Wettbewerbereinsatz (F6): keine eigene Einzelsuche.
- Quellen sind Verzeichnisse (it-in-germany, Cylex, WKO, Firmenbuch-Aggregatoren, Bloomberg-LEI) und Messetexte: Stufe S. Messe-Beschreibungstexte nie V (Regel N5).
- kundendatenbank_export.txt ohne Treffer für alle zehn Firmen; keine "Verifiziert am"-Prüfung nötig. Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
