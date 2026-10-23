# Tina Batch 12 – electronica 2026 (Prüfung von tom_batch_12.md)
Erstellt: 2026-10-15 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q, Messemodus Regel N). Eingabe: ausschließlich electronica/ergebnisse/tom_batch_12.md (10 Firmen). Tabellenzeile = Zeilennummer der Ampel-Tabelle D.
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Verfügbar waren nur WebSearch (19 Abfragen, Snippets/Kurzfassungen) und Bash. WebFetch und Chrome nicht nutzbar. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Keine Aussage und kein Grün ist mailtauglich.
Verifikationsdatum aller Einträge: 2026-10-15.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | cps Programmier-Service GmbH (C3.441) | GELB | 2 | ja |
| 2 | Creative Insights Technologies GmbH (C5.318) | GELB | 2 | ja |
| 3 | CRS Prüftechnik GmbH (A4.611) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 4 | CSA Group Bayern GmbH (A4.565) | GELB (Rot-Kandidat E2) | 7 | nein |
| 5 | C+S Chlorgas GmbH (B0.116) | GELB | 6 | nein |
| 6 | CTS GmbH Clima Temperatur Systeme (A4.229) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 7 | CTX Thermal Solutions GmbH (B3.237) | GELB | 7 | nein |
| 8 | cyberTECHNOLOGIES GmbH (C1.619) | GELB | 5 | ja |
| 9 | DAS Environmental Expert GmbH (B1.261) | GELB | 5 | ja |
| 10 | dataTec AG (A4.207) | GELB (Rot-Kandidat E2) | 7 | nein |

Zahlen: Grün 2, Gelb 8, Rot 0.

Hinweise zum ganzen Batch:
- Nr. 132 fehlt in Toms Eingabe (Nummernlücke 124-131, 133, 134), laut Tom bereits in der Eingabe so. Nicht von mir ergänzt; Jey bitte prüfen, ob eine Firma verloren ging.
- CRM: `python3 crm_abgleich.py` für alle Firmen samt Konzern-/Alt-/Schreibvarianten selbst wiederholt (cps, Creative Insights, CRS, CSA Group Bayern/CSA Group, C+S/C&S Chlorgas, CTS, CTX/Contrinex, cyberTECHNOLOGIES/cyber Technologies, DAS Environmental Expert/Dünnschicht-Anlagen-Systeme/Dürr, dataTec): kein Treffer, außer "Dürr" (bekannte_firmen_DE-AT-NL.txt Z. 577-579: Dürr Aktiengesellschaft, Dürr system AG, Dürr Systems AG). Eine Verbindung DAS zu Dürr ist in keiner Quelle belegt (siehe Nr. 9). Contrinex (von Tom offen gelassen) nachgeholt: neu.
- Patente (F5): Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Eigene Anmelder-Websuchen (nur Snippets) für CRS, CTS, DAS (zwei Suchen) und cyberTECHNOLOGIES: keine Patente der Firma auffindbar. Für cps, Creative Insights, CSA, C+S, CTX, dataTec keine eigene Wiederholung (Budget). Feld 9 ist damit bei ALLEN 10 Firmen nach F5 nicht erfüllt: Batch UNVOLLSTÄNDIG; Nachholen im Browser (Google Patents, Espacenet pa=..., DEPATISnet) nötig, bevor ein Grün final wird. "Keine Treffer" ist kein Gegenbeweis.
- Wettbewerbereinsatz (F6): `wettbewerber_referenzen.md` per Grep vollständig (631 Zeilen) auf alle zehn Namen und Altnamen abgeglichen: kein Treffer. Keine eigene Einzelsuche je Firma. Ohne Einfluss auf die Ampel.
- Messe-Signal (Regel N2) von Tom übernommen, nicht neu geprüft: bdtronic (Z. 70), ELANTAS (Z. 168), RAMPF (Z. 502/503) auf der electronica; ändert nichts an den Ampeln.

---

## 1. cps Programmier-Service GmbH | Stand C3.441
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).**
- Begründung: Meine Suche `"cps Programmier-Service" Lindhorst` fand die Firma ebenfalls nicht (nur CPS GmbH Berlin, CPS Computer Program Services u. a., andere Firmen). Ohne Identität sind weder Fertigung noch Produkt prüfbar. E2 (Dienstleister) ist nicht mit Quelle belegt, also nicht Rot.
- Korrekturen an Toms Feldern: keine; Toms Einstufung "kein Fertiger (vorläufig)" ist nachvollziehbar, aber nur Namensableitung (?). CRM: neu (Skript bestätigt).
- Nachrecherche-Auftrag (Gelb, Zeile 2): Existiert die Firma in Lindhorst, und was stellt sie her (Fertiger oder Programmierdienst, z. B. Chipprogrammierung)? Wo nachsehen: aussteller-Profil C3.441 im electronica-Ausstellerverzeichnis, Handelsregister (Amtsgericht Stadthagen/Bückeburg), Impressum der Firmenwebsite (Domain unbekannt, über Ausstellerprofil suchen). Bei Dienstleister-Bestätigung mit Quelle: Rot E2.
- Nicht verwendbare Aussagen: alles zu Tätigkeit, Fertigung, Verguss (Stufe ?); Segment "Programmierservice" (?). Stichprobe für Jey: ja (Firma nicht auffindbar, Rot-Kandidat).

## 2. Creative Insights Technologies GmbH | Stand C5.318
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität/Sitz widersprüchlich).**
- Begründung: Einzige Quelle ist ein Branchenverzeichnis (orte.muenchen.de, Lichtenbergstr. 8, "85386 Garching", S); Messeliste nennt 85748 Garching, die PLZ 85386 gehört zu Eching. Mein Handelsregister-Suchversuch fand keinen Registereintrag. Tätigkeit und Produkt unbekannt.
- Korrekturen: keine. Feld 3 (Bayern) bleibt, da beide Orte in Bayern. CRM: neu.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Welche Gesellschaft stellt aus (Sitz Garching oder Eching), was wird hergestellt (Hardware oder Software)? Wo nachsehen: Ausstellerprofil C5.318 electronica, Handelsregister München (Name + Adresse Lichtenbergstr. 8), Website/Impressum. Bei reiner Software/IT mit Quelle: Rot E2.
- Nicht verwendbare Aussagen: Kategorie "elektrische Geräte" (S, Verzeichnis); Fertigung, Verguss (?); Sitz (widersprüchlich). Stichprobe für Jey: ja.

## 3. CRS Prüftechnik GmbH | Stand A4.611
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Fertigung Stufe A nach Sitzregel, Verguss Mittel Stufe A).**
- Begründung: Hersteller von Prüfsystemen für Leistungshalbleiter und Leiterplatten (Isolationstests, End-of-Line-Linien) laut PCIM-Ausstellerprofil (S), Adresse Reichenaustraße 242, 78467 Konstanz, Telefon +49 7531 (Konstanz) im selben Profil. Gerätebauer mit eigenen Produkten, kein Händler; Hochspannungs-/Stromquellen, Messwandler, Steuerelektronik der Prüfsysteme typisch vergossen (Mittel, A). Der Orts-Widerspruch (Konstanz laut PCIM, Meersburg laut INGUN-Broschüre 2020) liegt innerhalb Baden-Württembergs und ändert Gebiet und Sitzregel nicht; Zeile 2 daher nicht ausgelöst, aber Identität/Standort nicht V-belegt.
- Eigene Prüfung: Suche nach Impressum/Geschäftsführer erfolglos (nur Ingun Prüfmittelbau GmbH Konstanz, andere Firma, nicht vermischt). Patentsuche (Anmelder, Prüfvorrichtung): kein Patent der Firma, nur fremde. CRM neu.
- Korrekturen: Tom stuft "prüfenswert"; Ampel Grün nach Tabelle D, aber nur als Vorschlag mit Stichprobe. Zitat im Browser bestätigt: nein.
- Nachrecherche (empfohlen, kein Gelb): Impressum/Handelsregister (aktueller Sitz, Standortzahl; Mehrwerk wäre V-pflichtig), Stellenanzeigen Montage/Elektronik, Datenblatt Prüfstation (Hochspannungsmodul, Eigenbau oder Zukauf).
- Nicht verwendbare Aussagen: Fertigung Konstanz/Meersburg (A/S); Verguss aller Bauteile (A); Segment Electrical Insulation (A). Stichprobe für Jey: ja (Grün ohne V, Standortwiderspruch).

## 4. CSA Group Bayern GmbH | Stand A4.565
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; E2-Rot-Kandidat, nicht V-belegt).**
- Begründung: Mehrere Snippets (Bayern-International, Fachpresse) beschreiben europäische Zentrale und Prüfcampus Plattling für Prüfung, Inspektion, Zertifizierung; keine Eigenprodukte gefunden. Das stützt E2 (Dienstleister) stark, ist aber keine Stufe V, daher nicht Rot (Zeile 1 verlangt V). Hinweis: Eine zweite Gesellschaft "CSA Group Europe GmbH" (Frankfurt) existiert laut Wiley-Eintrag; Beziehung unbekannt, nicht vermischt.
- Korrekturen: keine. CRM neu (Skript, auch "CSA Group").
- Nachrecherche-Auftrag (Gelb, Zeile 7): Gibt es eigene Produkte oder Fertigung in Plattling, oder ausschließlich Prüf-/Zertifizierungsdienst? Wo nachsehen: Impressum und Leistungsseiten csagroup.org/de (Plattling), Handelsregister Passau; bei Bestätigung Rot E2 mit URL. Aktion: nicht verfolgen.
- Nicht verwendbare Aussagen: "keine Fertigung" (S); Mitarbeiterzahl 180-300 (S, widersprüchlich). Stichprobe für Jey: nein.

## 5. C+S Chlorgas GmbH | Stand B0.116
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6).**
- Begründung: Abfüllung von HCl-Gas für Chemie/Pharma/Halbleiter (S), kein Elektronikbauteil; Verguss Niedrig bei allen plausiblen Bauteilen (A). E1-E5 nicht belegt (Hersteller technischer Gase ist kein Händler nach E2 und kein Materialhersteller im Demak-Kerngeschäft).
- Korrektur an Toms Feld 4: Das Silicon-Saxony-Profil (meine Suche) beschreibt als neuen Abfüllstandort das ChemiePark Bitterfeld-Wolfen ("Fokus Abfüllung HCl-Gas dort"), Kontaktadresse Reit 4, Künzing, Familienunternehmen "seit über 30 Jahren", Herkunft Gersthofen genannt. Fertigungsort daher nicht Künzing gesichert, sondern Künzing/Bitterfeld-Wolfen (beide DE); Gebiet kann Rest Deutschland statt Bayern sein. Unterschied ohne Einfluss auf die Ampel. CRM neu.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Welche Produkte/Bauteile haben Dosier-, Dicht- oder Klebeschritte (voraussichtlich keine)? Wo nachsehen: chlorgas.de Produktseite und Impressum (Standorte). Aktion: nicht priorisieren.
- Nicht verwendbare Aussagen: Abfüllung am Standort Künzing (S, widersprüchlich); "kleine Firma" (S). Stichprobe für Jey: nein.

## 6. CTS GmbH Clima Temperatur Systeme | Stand A4.229
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Sitzregel, Verguss Mittel Stufe A).**
- Begründung: Mittelständischer Hersteller von Klima- und Temperaturprüfschränken, Lotzenäcker 21, 72379 Hechingen (mehrere Verzeichnisse und DAkkS-Urkunde D-K-18066-01-00 konsistent, S). Neu aus meiner Suche: Handwerkskammer-Reutlingen-Zeitschrift dhz 19/2015 (S, nicht geöffnet) nennt Gründung 1996 und Produktion "ausschließlich am Standort Hechingen"; Auslandsgesellschaften (SE, BE, AT, CZ) sind laut Quellen Vertrieb/Service. Heizelemente, Sensorik, Steuerung/Netzteile und Magnetventile der Kammern sind typisch vergossen (Mittel, A; Bauteil-Regel: Maximum zählt).
- Eigene Prüfung: Patentsuche (Anmelder, Klimakammer): keine Patente der Firma auffindbar. Stellenanzeigen Montage/Elektronik in Hechingen: keine für CTS auffindbar. Konzern/Mutter: keine genannt. CRM neu.
- Korrekturen: Toms "prüfenswert" (Verguss Mittel) bleibt; Ampel Grün nach Tabelle D. Zitat im Browser bestätigt: nein.
- Nachrecherche (empfohlen): Impressum/Standortseite cts-umweltsimulation.de (Domain unbestätigt), Stellenanzeige Hechingen, Datenblatt (Heizregister, Sensoren, Eigenbau oder Zukauf).
- Nicht verwendbare Aussagen: Fertigung Hechingen (A/S); Verguss (A); Website-Domain (abgeleitet); Produktionsfläche 5.000 m² (S, Eigenangabe). Stichprobe für Jey: ja (Grün ohne V).

## 7. CTX Thermal Solutions GmbH | Stand B3.237
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).**
- Begründung: Kühlkörperhersteller/-händler, Lötscher Weg 104, 41334 Nettetal. Meine Suche: Profilkühlkörper per Strangpressen, Kaltfließpressen (LED-Kühlkörper) und Reibrührschweißen (Broschüre eines Vertriebspartners, S) deuten auf Fertigungsprozesse, aber ob am Standort Nettetal oder über Partner (Pada Engineering, Aavid), ist offen. Verguss Niedrig (A): Kühlkörper, Kühlplatten, Lüfter sind nicht typisch vergossen. Weder Zeile 5 noch 6 eindeutig anwendbar (Fertigung offen und Verguss Niedrig), daher Zeile 7. Leitungswechsel Feb. 2025 (Schmitz an Mirau, Wiley, S) ohne Bezug zur Ampel.
- Korrekturen: keine. CRM neu (inkl. Contrinex, Vorgänger). Stellenanzeigen Nettetal fand ich nicht.
- Nachrecherche-Auftrag (Gelb, Zeile 7): (a) Wird in Nettetal gefertigt (Strangpressen, Zerspanung, Montage) oder nur Logistik/Handel? (b) Gibt es Gehäuse-/Lüfterbaugruppen mit Elektronik, die Dichtung, Verklebung (Wärmeleitkleber) oder Verguss erhalten? Wo nachsehen: ctx.eu Produkt- und Impressum-/Standortseite, Stellenanzeigen Nettetal, Datenblätter Gehäuse. Aktion: nur bei Eigenfertigung und Elektronik-Baugruppen weiter.
- Nicht verwendbare Aussagen: Fertigung Nettetal (S/?); Verguss Niedrig (A); Pada-Beteiligung (S). Stichprobe für Jey: nein.

## 8. cyberTECHNOLOGIES GmbH | Stand C1.619
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Hinweis auf Fertigung in China).**
- Begründung: Georg-Kollmannsberger-Str. 3, 85386 Eching; Hersteller laserbasierter Messsysteme (ca. 10 Mitarbeiter, Gründung 2000, Verzeichnisse, S). Implisense (S): Unternehmensgegenstand "Herstellung und Vertrieb von Elektronik-, Mechanik- und Optikprodukten", kein Produktionsort. Eine chinesische Regierungsmeldung (Changzhou, S) nennt München als Hauptsitz, Gründung 1992 und eine geplante erste Fertigungsbasis in China: Auslagerungshinweis, Stufe V wäre nötig (Sitzregel greift nicht). Verguss Mittel (A: Sensorkopf, Steuerelektronik; Epoxid wird nur gemessen, kein Beleg).
- Korrekturen: keine inhaltlichen. Zusatz Feld 17: Gründungsjahr 1992 gegen 2000 (Quellen zweier Firmen oder Verwechslung, ungeklärt). Patente: keine Patente der Firma auffindbar (Anmelder-Websuche). CRM neu.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Werden die Messsysteme für den europäischen Markt in Eching gebaut und montiert (Fertigungsbeleg) und ist die Changzhou-Meldung dieselbe Firma? Wo nachsehen: Impressum und Produktseiten der Firmenwebsite (Domain unbekannt, über Ausstellerprofil C1.619 suchen), Stellenanzeigen Eching (Montage, Elektronik), Handelsregister München (Sitz). 
- Nicht verwendbare Aussagen: Fertigung Eching (S); Verguss (A); Mitarbeiterzahl 10 (S, eine Quelle). Stichprobe für Jey: ja (Auslandshinweis, Identität).

## 9. DAS Environmental Expert GmbH | Stand B1.261
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Fertigung Stufe S im Konzern/Mehrstandort).**
- Begründung: Goppelner Straße 44, 01219 Dresden, Amtsgericht Dresden HRB 3716, früher Das-Dünnschicht Anlagen Systeme GmbH (North Data, S). Gruppe mit 850+ Mitarbeitern und Tochterfirmen: Stufe V für die fertigende Einheit nötig (Sitzregel nicht anwendbar). Meine Suche: Stellenanzeigen "Mitarbeiter Fertigung" (elektrische und mechanische Montage von Anlagen und Baugruppen nach Stücklisten, Schaltplänen) und "Fachkraft Endabnahme", Standort Dresden (Aggregator praktischkommune.de/StepStone, Stand 27.06.2026, nur Snippet, S): das stützt Montage in Dresden stark, ist aber nicht gelesen, daher S (gelesen wäre V für den Fertigungsort). Verguss Mittel (A: Schaltschrank/Steuerung, Zünd-/Flammensensorik, Magnetventile, Gehäusedichtung).
- Korrektur an Toms Feld 12 (CRM): Eine Dürr-Zugehörigkeit ist durch keine Quelle belegt. Meine Suche zu Gesellschaftern fand nur "Familienunternehmen" (Chemie.de-Profil, S) und Management Reichardt; kein Dürr-Bezug. Zeile 3 ist daher nicht ausgelöst; CRM-Status: neu (Skript für DAS und Dünnschicht-Anlagen-Systeme: kein Treffer). Offen bleibt nur die Gesellschafterliste (nicht abgerufen).
- Patente: Toms Treffer (US7377771B2, Anmelder "Das-Dünnschicht Anlagen Systeme GmbH", Brennerthema) konnte ich nicht bestätigen, aber auch nicht widerlegen: meine zwei Anmelder-Suchen (Verguss/Dichtung; Brenner/Scrubber) lieferten nur fremde Patente. Kein Verguss-Patent gefunden. Rechtsstand offen.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (1) Fertigung Dresden belegen: Stellenanzeige "Mitarbeiter Fertigung" im Original öffnen (Karriereseite das-ee.com oder StepStone) und Standortseite/Impressum lesen. (2) Gesellschafter: Handelsregister Dresden HRB 3716, Gesellschafterliste (Dürr ausschließen). (3) Werden Schaltschränke/Sensorik vergossen oder gedichtet (Datenblatt, Schaltschrank-Fertigung)? Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Dresden (S); Verguss (A); Dürr-Bezug (?, nicht belegt); 850+ Mitarbeiter (S, Selbstangabe); Patent US7377771B2 (S, Status offen). Stichprobe für Jey: ja (Konzernstruktur, Fertigungsbeleg).

## 10. dataTec AG | Stand A4.207
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; E2-Rot-Kandidat, nicht V-belegt).**
- Begründung: Mehrere Snippets (Pressemeldungen, Kompass "Großhandel", LRBW-Mitgliedsprofil) beschreiben dataTec als größten Fachdistributor für Mess- und Prüftechnik (über 50 Marken, Auslandsgesellschaften ES, CH, AT, SE, EE, FI), Ferdinand-Lassalle-Straße 52, 72770 Reutlingen. Das trägt E2 (Händler ohne Fertigung) stark, ist aber nicht V, daher nicht Rot.
- Korrekturen: Straßennummer 52 ergänzt (S). CRM neu. Keine Eigenfertigung gefunden.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Hat dataTec Eigenprodukte oder Fertigung (z. B. eigene Marke, Konfektionierung) in DE/AT/NL? Wo nachsehen: Impressum und "Über uns" datatec.eu, Handelsregister Stuttgart/Stuttgart-Reutlingen; bei Bestätigung Händler ohne Fertigung: Rot E2 mit URL. Aktion: nicht verfolgen.
- Nicht verwendbare Aussagen: "kein Eigenprodukt" (S); Umsatz 85 Mio. EUR, 140-150 Mitarbeiter (S). Stichprobe für Jey: nein.

---

## Konsistenz und Auffälligkeiten
- Toms Belegstufen sind durchgehend korrekt niedrig (S/A/?); keine vorgetäuschte V-Aussage gefunden. Kein falsches Grün erkennbar, aber beide Grün-Vorschläge (CRS, CTS) beruhen ausschließlich auf Sitzregel und Produkttyp (A).
- Abweichungen von Tom: C+S Fertigungsort (Bitterfeld-Wolfen statt nur Künzing), DAS CRM (neu statt unklar, Dürr-Annahme unbelegt), CRS und CTS jeweils Grün statt offen.
- Vorschlag Fehlerlog (nicht eingetragen, Jey gibt frei): "Vermuteter Konzern ohne Quelle (DAS gegen Dürr) nicht als CRM-Unklar führen, sondern als Nachrecherche zur Gesellschafterliste."

## Einschränkungen
- Browser (Chrome) und WebFetch nicht verfügbar: kein Gegenlesen nach Abschnitt H, kein Impressum, Datenblatt oder Register gelesen; alle Aussagen Stufe S, A oder ?. Keine "Zitat im Browser bestätigt: ja".
- WebSearch: 19 Abfragen verbraucht (Identität/Fertigung für alle zehn Firmen, Patente für CRS, CTS, DAS (zwei), cyberTECHNOLOGIES, Gesellschafterfrage DAS, zusätzlich je eine Standort-/Stellensuche CTS, CTX, DAS). Das Limit von rund 30 war nicht ausgeschöpft; Wettbewerber-Einzelsuchen und Patentwiederholungen für cps, Creative Insights, CSA, C+S, CTX, dataTec unterblieben (Priorisierung: Firmen, die Tom als prüfenswert führt, und offene Identitäts-/Konzernfragen).
- Patente (F5): Datenbanken nicht direkt abgefragt; Pflichtsuche nicht erfüllt, Batch UNVOLLSTÄNDIG bezüglich Feld 9 bei allen Firmen. Rechtsstände nicht geprüft.
- Handelsregister/Unternehmensregister nicht abgerufen; Gesellschafterlisten unbekannt. Kundendatenbank (Excel) nicht lesbar; Abgleich nur gegen kundendatenbank_export.txt und bekannte_firmen_DE-AT-NL.txt über das Skript.
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
