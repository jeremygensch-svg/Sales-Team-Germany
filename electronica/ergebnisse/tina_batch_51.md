# Tina Batch 51 - electronica 2026 (Prüfung von tom_batch_51.md)
Erstellt: 2026-10-21 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe: ausschließlich electronica/ergebnisse/tom_batch_51.md (10 Firmen, Tom-Nr. 569 bis 578).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (15 Abfragen, Kurzfassungen/Snippets) und Bash zur Verfügung; WebFetch und Chrome nicht nutzbar. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün vergeben, nichts ist mailtauglich.
Skripte: `python3 crm_abgleich.py` für alle Firmen samt Konzern-/Altnamen selbst wiederholt (Ergebnis je Firma unten). Tabellenzeile = Zeilennummer der Ampel-Tabelle D (regeln_tom_tina.md).
Verifikationsdatum aller Einträge: 2026-10-21.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | SIEGERT WAFER GmbH (C1.717) | GELB | 2 (Identität/Adresse) | ja |
| 2 | SI Electronics GmbH (C5.339) | GELB | 7 (Rot-Kandidat E2, nicht V) | nein |
| 3 | Siemens Industrial Software GmbH (B5.338) | GELB | 2 (Name abweichend), zusätzlich 3 (CRM-Konzern Siemens AG) | ja |
| 4 | SIIX Europe GmbH (A1.619) | GELB | 2 (Firma nicht auffindbar) | ja |
| 5 | SilcoTek GmbH (C2.236) | GELB | 7 (Rot-Kandidat E2, nicht V) | nein |
| 6 | Silex Technology Europe GmbH (C2.505) | GELB | 5 | ja |
| 7 | Silicon Saxony e. V. (B1.221) | GELB | 7 (Rot-Kandidat E2 analog, nicht V) | nein |
| 8 | Silicon Saxony Management GmbH (B1.521) | GELB | 7 (Register fehlt, Rot-Kandidat) | ja |
| 9 | SIMONA AG (B1.862) | GELB | 5 | nein |
| 10 | Singulus Technologies AG (B1.458) | GELB | 5 | ja |

Zahlen: Grün 0, Gelb 10, Rot 0. Toms Einstufung "prüfenswert" (Singulus) wird nicht zu Grün, weil mehrere Standorte (Stufe V nötig) und nur Snippets.

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet und DEPATISnet nicht direkt abfragbar. Eigene Patent-Websuchen: Singulus (1), SIMONA (1), SIIX (1), Siegert Wafer/Silex/SilcoTek (1 gemeinsame); für SI Electronics, Siemens, Silicon Saxony (beide) keine eigene Wiederholung (Suchbudget; Verband/Händler/Software). Ergebnis: kein Treffer mit Vergussbezug und passendem Anmelder; Rechtsstand nicht geprüft. Feld 9 ist damit bei ALLEN 10 Firmen ohne Datenbankabfrage: nach F5 UNVOLLSTÄNDIG, Nachholen im Browser nötig. "Keine Treffer" ist kein Gegenbeweis.
Wettbewerbereinsatz (F6): Grep auf wettbewerber_referenzen.md für Siegert, SI Electronics, Siemens, SIIX, Silco, Silex, Silicon Saxony, SIMONA, Singulus: einziger Treffer "Siemens AG A&D MC" (DELO-Liste, V dort; andere Einheit als die Software-GmbH). Zusätzlich eigene Einzelsuchen mit Wettbewerbernamen für Singulus und SIIX: kein Hinweis gefunden (nur Nordson-Händlermeldungen Slowakei/Ungarn ohne SIIX-Bezug). Messe-Signal von Tom übernommen, nicht nachgeprüft, ohne Einfluss auf die Ampel.

---

## 1. SIEGERT WAFER GmbH | C1.717
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität/Adresse).** Zwei Adressen in Aachen (SEMI: Gewerbepark Brand 82, 52078; Lieferantendatenblätter: Charlottenburger Allee 7, 52068; S). Neu gegenüber Tom: dieselben Datenblätter nennen HRB 17499 und USt-ID, Geschäftsführer Marcus Siegert und Michael Kinch (S), die Firma existiert also, welche Adresse aktuell gilt, ist offen. Fertigung: SEMI-Profil nennt "own production facility" für SOI-Wafer, Ort offen (S). Verguss Niedrig (A, Wafer/Substrate; Polieren, Dicing sind keine Vergussbauteile).
- Eigene Prüfung: crm_abgleich.py "SIEGERT WAFER GmbH": kein Treffer, neu. Verwechslung ausgeschlossen mit SIEGERT electronic GmbH (Cadolzburg) und Peter Siegert (Patente). Patent: eine gemeinsame Websuche, keine Siegert-Wafer-Anmeldungen (Datenbank offen).
- Korrekturen an Toms Feldern: Feld 17 Zusatz HRB 17499 (S, Datenblatt, Registergericht nicht genannt). Feld 5 weiter ohne Website. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (1) Welche Adresse ist die aktuelle Firmenanschrift, und wo steht das Werk? Handelsregister (HRB 17499, Amtsgericht Aachen), Impressum der Firmenwebsite. (2) Falls Fertigung in Aachen belegt: Welche Bauteile (nur Wafer, dann Verguss Niedrig, Zeile 6)? Aktion: nicht priorisieren.
- Nicht verwendbare Aussagen: Eigenwerk-Standort (S); Adresse (widersprüchlich); Verguss (A). Stichprobe für Jey: ja (Identität).

## 2. SI Electronics GmbH | C5.339
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Selbstbeschreibung "procurement, logistics and quality assurance of electronic components" (S, Stellenanzeigen) spricht für Beschaffung/Prüfung ohne Fertigung, Ausschluss E2 ist inhaltlich stark, aber nicht Stufe V und daher nicht Rot. Meine Registersuche (Handelsregister, Geschäftsgegenstand) fand nichts; Geschäftsgegenstand offen.
- Eigene Prüfung: crm_abgleich.py "SI Electronics GmbH" / "SI Group": nur Fehlalarme Cms Electronics [AT] und IMM electronics GmbH [DE] (je 0,90), SI Group kein Treffer; neu. Patent: keine eigene Wiederholung.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Hat die GmbH Montage, Konfektion oder Baugruppenfertigung in Mannheim? Wo nachsehen: Impressum und Leistungsseite der SI Group, Handelsregister Mannheim (Gegenstand des Unternehmens), Stellenanzeigen Mannheim (Produktion/Montage). Bei V-Beleg "Händler/Prüfdienst ohne Fertigung": Rot nach E2 mit URL. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: "kein Fertigungsbetrieb" (S); Mitarbeiterzahl (S, Aggregator); Rechtsform (Anzeigentext). Stichprobe für Jey: nein.

## 3. Siemens Industrial Software GmbH | B5.338
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, zusätzlich Zeile 3).** Zeile 2: Der Name der Vorgabe "Siemens Industrial Software GmbH" ist nicht belegt. Meine Suche fand "Siemens Industry Software GmbH" in Zürich und Linz (andere Länder, LEI/Verzeichnis, S), eine "Siemens Industry Software GmbH & Co. KG" (Wikipedia, 2013, S) und Siemens-Arbeitsort Nürnberg; ein Registereintrag der Nürnberger GmbH fehlt. Zeile 3: Siemens AG steht im CRM (bekannte_firmen Z2178 bis 2180), Einheit unklar (Regel M). Inhaltlich Software, also Rot-Kandidat E2, aber nicht V.
- Eigene Prüfung: crm_abgleich.py "Siemens Industrial Software GmbH", "Siemens Industry Software", "Siemens Digital Industries Software", "Siemens AG": Präfix Siemens (Z2178), Siemens AG (Z2179), SIEMENS AG (Z2180) und weitere Siemens-Wortwurzeltreffer (Energy, Healthineers, Bad Neustadt); dieselbe Einheit nicht im CRM, daher kein E5-Rot. wettbewerber_referenzen.md: nur "Siemens AG A&D MC" (andere Einheit).
- Korrekturen: Feld 17: Rechtseinheit und exakter Name offen (Industry statt Industrial; Nürnberg, Linz, Zürich nicht vermischen). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeilen 2/3): (1) Jey: Wie heißt die Aussteller-Einheit auf B5.338 exakt (Aussteller-Detailseite exhibitors.electronica.de), und ist sie mit CRM "Siemens AG" (Z2178 bis 2180) als Bestandskonzern abgedeckt? (2) Handelsregister Nürnberg: Firmierung, Gegenstand (Software). Bei V-Beleg Software ohne Hardwarefertigung: Rot nach E2. Aktion: nicht kontaktieren, Konzern-Siemens-Kontakt im CRM pflegen.
- Nicht verwendbare Aussagen: alle Fertigungs-/Produktaussagen (S/A); Rechtsform. Stichprobe für Jey: ja (Name, CRM-Einheit).

## 4. SIIX Europe GmbH | A1.619
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Firma nicht auffindbar).** Meine Suche "SIIX Europe GmbH Willich" lieferte keine Seite zu dieser Firma; Willich-Treffer gehören zu silex, ROHM, Varex, LACROIX. Bestätigt Toms Negativbefund (kein Beleg, kein Gegenbeweis). Konzern SIIX (Japan): europäische Produktion Slowakei, Ungarn geplant (evertiq, S, 2017er Meldungen, Stand offen). Verguss Mittel (A, EMS-Baugruppen Automotive/Industrie; reine SMT niedrig); Fertigung in DE/AT/NL nicht belegt (Niedrig, S).
- Eigene Prüfung: crm_abgleich.py "SIIX Europe GmbH", "SIIX Corporation": kein Treffer, neu. Patent: eine eigene Suche, kein SIIX-Anmelder (nur fremde Vergusspatente). Wettbewerber: eine Einzelsuche (SIIX Slowakei/Ungarn mit Nordson, DOPAG, Scheugenpflug, Henkel): kein SIIX-Bezug.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (1) Existiert eine SIIX-Gesellschaft in DE (Aussteller-Detailseite A1.619, Handelsregister, siix.com Standortliste) und wo sitzt sie? (2) Hat sie Fertigung/Montage in DE/AT/NL (sonst Rot nach E3/E2 mit V)? Aktion: Identität vor Weiterarbeit klären.
- Nicht verwendbare Aussagen: alle zu Willich (?); Konzernfertigung Slowakei (S, alt); Verguss (A). Stichprobe für Jey: ja.

## 5. SilcoTek GmbH | C2.236
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Europäische Vertriebs-/Supportgesellschaft der SilcoTek Corp., gegründet 2009 in Oberursel, heute Hessenring 83, 61348 Bad Homburg (Verzeichnisse, S; frühere Adresse Schaberweg 23 erklärt den Adresswiderspruch). Lieferung beschichteter Lagerware aus Deutschland (chemie.de, S), Beschichtung selbst in Bellefonte, USA (S). Verguss Niedrig (A, Oberflächenbeschichtung). E2/E3 stark, nicht V.
- Eigene Prüfung: crm_abgleich.py "SilcoTek GmbH", "SilcoTek Corporation": kein Treffer, neu. Patent: gemeinsame Suche, keine Verguss-Anmeldungen. Im Silicon-Saxony-Mitgliederverzeichnis geführt (S, ohne Relevanz für die Ampel).
- Korrekturen: Adresse aktualisiert (siehe oben). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Beschichtet die GmbH in Deutschland (Lohnbeschichtung) oder nur Vertrieb? Impressum silcotekgmbh.de, Handelsregister Bad Homburg (Gegenstand). Bei V "nur Vertrieb": Rot nach E2. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Vertriebsrolle (S); Fertigung USA (S); Verguss (A). Stichprobe für Jey: nein.

## 6. Silex Technology Europe GmbH | C2.505
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Willich, Hanns-Martin-Schleyer-Str. 3, Tochter seit 2000 der silex technology Inc., Kyoto; dort Hauptsitz und Fertigung (silextechnology.com Kontaktseite, pressebox, S). Meine Suche fand keine Fertigung in Willich; Europa-Gesellschaft vermutlich Vertrieb/Support (?). Verguss Mittel (A, WLAN-Module/Device Server im Gehäuse). Identität stimmt (mehrere Verzeichnisse, S).
- Eigene Prüfung: crm_abgleich.py "Silex Technology Europe GmbH", "silex technology Inc": kein Treffer, neu. Patent: gemeinsame Suche, nichts zu silex. Keine Verwechslung mit LACROIX, ROHM (ebenfalls Willich) und Silex Microsystems (Schweden).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Hat die GmbH Entwicklung, Montage oder Fertigung in Willich? Impressum/Über-uns silextechnology.com/de, Stellenanzeigen Willich (Hardware/Produktion), Handelsregister Krefeld. Bei V "nur Vertrieb": Rot nach E2. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Japan (S); Vertriebsrolle Willich (?); Verguss (A). Stichprobe für Jey: ja.

## 7. Silicon Saxony e. V. | B1.221
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Branchenverband (Cluster, rund 600 Mitglieder laut Wikipedia/Eigenseite, S), M.-v.-Ardenne-Ring 20 F, 01099 Dresden. Keine Produkte, Verguss Niedrig (A). Ein Verband steht nicht wörtlich in E2; Rot nur per Analogie und nur mit V, daher Gelb mit Entscheidungsauftrag.
- Eigene Prüfung: crm_abgleich.py "Silicon Saxony e.V.": kein Treffer, neu. Patent: keine Wiederholung (Verband). Mitglieder (u. a. SIMONA, SilcoTek) nicht abgeglichen.
- Korrekturen: Mitgliederzahl uneinheitlich (550/600/650), ohne Belang. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Jey entscheidet, ob ein Verband ohne Produkte analog E2 als Rot gilt (Regelfrage); Belegseite: silicon-saxony.de "Über uns"/Satzung (V für "keine Fertigung"). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Mitgliederzahl (S); Verbandsstatus (S). Stichprobe für Jey: nein.

## 8. Silicon Saxony Management GmbH | B1.521
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7, Identität teilweise).** Korrektur zu Tom: Die Team-Seite silicon-saxony.de/ueber-uns/team führt "Silicon Saxony Management GmbH" neben den Verbandsmitarbeitern (S), und eine Jubiläumsbroschüre nennt deren Gründung (S). Existenz damit gestützt, Register/Handelsregister weiter nicht gelesen. Management-/Dienstleistungsgesellschaft des Netzwerks, keine Produkte; Verguss Niedrig (A).
- Eigene Prüfung: crm_abgleich.py "Silicon Saxony Management GmbH": kein Treffer, neu. Patent: keine Wiederholung.
- Korrekturen: Feld 17 von "nicht belegt" auf "teilweise belegt (S, Team-Seite)". Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Handelsregister Dresden (Firmierung, Gegenstand) und Impressum silicon-saxony.de lesen; bei V "Verbandsmanagement ohne Fertigung": Entscheidung wie Nr. 7. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Rolle und Adresse (S/?). Stichprobe für Jey: ja (Identität, gemeinsam mit Nr. 7 entscheiden).

## 9. SIMONA AG | B1.862
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Konzern mit mehreren Werken: zwei Werke Kirn (Halbzeuge) und Ringsheim, Baden-Württemberg (Rohre, Formteile, Fertigteile), dazu ausländische Werke (Geschäftsbericht 2018 und Folgequellen, S, veraltet); Stufe V nötig und nicht erreicht. Korrektur zu Tom: Fertigteile entstehen laut Snippet in Ringsheim, nicht Kirn; 2024 Hinweis auf kundenindividuelle Sonderformteile in eigenen Kunststoffwerkstätten (S). Verguss Niedrig (A, Platten, Rohre, Formteile; Elektronikgehäuse nicht belegt).
- Eigene Prüfung: crm_abgleich.py "SIMONA AG": kein Treffer, neu. Patent: eine Suche, keine SIMONA-Treffer zu Verguss/Dichtung/Klebung (Datenbank offen). Silicon-Saxony-Mitgliederverzeichnis führt SIMONA im Bereich Mikro-/Nanoelektronik (S).
- Korrekturen: Feld 3/4: Ringsheim (BW) als Fertigteil-Werk ergänzen. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Werden in Ringsheim oder Kirn Fertigteile für Elektronik/Halbleiter (Gehäuse, Tanks) mit Klebung, Dichtung oder Verguss gefertigt? simona.de Produktseite "Fertigteile", Datenblatt, Geschäftsbericht 2024 (hauptversammlung.de PDF) im Browser lesen. Sonst Verguss Niedrig bestätigen (Zeile 6). Aktion: Beobachtung, kein Kontakt.
- Nicht verwendbare Aussagen: Werkszuordnung (S, 2018); Fertigung DE (S); Verguss (A). Stichprobe für Jey: nein.

## 10. Singulus Technologies AG | B1.458
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Fertigungsbeleg nur Snippet).** Maschinenbauer, Sitz Kahl am Main; Stellenanzeigen Sonderanlagenbau-Mechaniker (Montage, Stücklisten-Prüfung), Inbetriebnehmer und Mechatronik-Ausbildung in Kahl (stellenmarkt.de, S); 2022 Konzentration der Produktion in Kahl (Singulus-Meldung, S). Sitzregel greift nicht sicher: weitere Standorte (Fürstenfeldbruck, Puchheim, China), und eine Stellenanzeige zählt als V nur, wenn ich sie gelesen habe (nur Snippet). Verguss Mittel (A, Steuerungen, Antriebe, Sensorik der Anlagen; Anlagen selbst nicht vergossen, Spannungsfeld Block C).
- Eigene Prüfung: crm_abgleich.py "Singulus Technologies AG": kein Treffer, neu. Patent: eine Suche (Justia-Liste, PitchBook: Themen Vakuum-Schleuse, Beschichtungsquellen, Dichtung von Anlagenkomponenten, kein Verguss; US12283491 "singulated encapsulated components" Anmelder nicht Singulus bestätigt). Wettbewerber: eine Einzelsuche (Nordson, Henkel, DELO, Scheugenpflug): kein Hinweis.
- Korrekturen: Toms "prüfenswert" ist nach Regel D (mehrere Standorte, nur S) nicht Grün; Feld 4 ergänzt um Puchheim (Elektrokonstruktion, S). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (1) Fertigung/Montage in Kahl mit V belegen: Stellenanzeige Sonderanlagenbau Kahl öffnen und lesen, Standortseite singulus.com. (2) Werden dort Schaltschränke/Steuerungen selbst montiert, und werden Teile geklebt, gedichtet oder vergossen? Stellenanzeigen Elektromontage Kahl. Bei V für (1) und Mittel/Hoch für Verguss: Grün (Zeile 4) erwartbar, geringe bis mittlere Priorität (Maschinenbau). Aktion: Beobachtung.
- Nicht verwendbare Aussagen: Fertigung Kahl (S); Verguss (A); Mitarbeiterzahl (S); Verlagerung 2022 (S, alt). Stichprobe für Jey: ja.

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind durchgehend niedrig und ehrlich angesetzt (keine vorgetäuschte V-Aussage). Zwei Korrekturen an Toms Befunden: Silicon Saxony Management GmbH ist auf der Team-Seite des Verbands belegt (S); Siegert Wafer hat eine HRB-Nr. in Lieferantendokumenten (S); SIMONA hat das Fertigteil-Werk in Ringsheim.
- Keine harten Ausschlüsse mit V belegt, daher kein Rot, obwohl vier bis fünf Firmen (SI Electronics, SilcoTek, Silicon Saxony beide, ggf. Siemens Software, Silex) Rot-Kandidaten nach E2 sind. Eine Browser-Runde (Impressum/Handelsregister) würde diese Gelb voraussichtlich in Rot überführen.
- Vorschlag Fehlerlog (Jey gibt frei, nicht eingetragen): (1) Messelisten-Namen mit abweichender Rechtseinheit (Siemens "Industrial" statt "Industry") früh gegen Aussteller-Detailseite prüfen. (2) Verbände/Cluster in Regel E2 ausdrücklich aufnehmen oder ausdrücklich ausnehmen.

## Einschränkungen
- Browser nicht verfügbar, WebFetch nicht verfügbar: kein Gegenlesen nach Abschnitt H, kein Impressum, keine Stellenanzeige, kein Datenblatt gelesen; alle Aussagen Stufe S oder A. Kein Grün, nichts mailtauglich.
- WebSearch: 15 Abfragen (Identität/Impressum für 9 Firmen, Patente 4, Wettbewerber 2). Ergebnisse sind Suchmaschinen-Kurzfassungen; Zitate nicht wörtlich geprüft.
- Patente: Pflichtsuche F5 nicht erfüllt (Google Patents, Espacenet, DEPATISnet nicht direkt abgefragt; für SI Electronics, Siemens, Silicon Saxony e. V./Management keine eigene Suche). Anmeldervarianten, Konzernfirmen (SIIX Corporation Japan, silex technology Inc., SilcoTek Corp.) und Rechtsstand offen. Der Batch ist nach F5 UNVOLLSTÄNDIG.
- Wettbewerbereinsatz (F6): Listenabgleich plus Einzelsuchen nur für Singulus und SIIX. Messe-Signal (aussteller_namen.txt) von Tom übernommen, nicht nachgeprüft (Eingabe auf Toms Datei beschränkt).
- Handelsregister/Unternehmensregister nicht abgerufen; HRB 17499 stammt aus Lieferantendatenblättern (S). Kundendatenbank (Excel) nicht lesbar; kundendatenbank_export.txt ohne Treffer für alle zehn Firmen. CRM-Hinweise Siemens (Z2178 bis 2180) per Skript, nicht inhaltlich geklärt.
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
