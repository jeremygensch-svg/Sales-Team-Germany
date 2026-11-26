# Tina Batch 46 – electronica 2026 (Prüfung von tom_batch_46.md)
Erstellt: 2026-10-20 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q, Messemodus Regel N). Eingabe: ausschließlich electronica/ergebnisse/tom_batch_46.md (10 Firmen).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (23 Abfragen, Snippets/Kurzfassungen) und Bash zur Verfügung; WebFetch und Chrome nicht nutzbar. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Ergebnis ist mailtauglich. Rot ist nirgends vergeben, weil Tabellenzeile 1 Stufe V verlangt und keine Quelle gelesen werden konnte.
Verifikationsdatum aller Einträge: 2026-10-20. Tabellenzeile = Zeilennummer der Ampel-Tabelle D.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | Renu Electronics GmbH (A1.645) | GELB | 5 | ja |
| 2 | RFMW - MRC Gigacomp GmbH & Co. KG (C5.561) | GELB (Rot-Kandidat E2) | 7 | nein |
| 3 | RG Elektrotechnologie GmbH (A1.502) | GELB | 5 | ja |
| 4 | RIGOL Technologies EU GmbH (A4.231) | GELB (Rot-Kandidat E2/E3) | 7 | nein |
| 5 | RIKEN KEIKI (C1.214) | GELB (Rot-Kandidat E2/E3) | 7 | nein |
| 6 | RIKUTEC Germany GmbH & Co. KG (kein Stand angegeben) | GELB | 6 | nein |
| 7 | RM Components GmbH (B6.135 / C6.530) | GELB (Rot-Kandidat E2) | 7 | ja |
| 8 | ROB GmbH (A1.123) | GELB | 5 | ja |
| 9 | Röchling Industrial Lahnstein SE & Co. KG (C1.860) | GELB | 6 | nein |
| 10 | ROKA - Robert Karst GmbH & Co.KG Elektrotechnische Fabrik (B2.331) | GELB | 2 | ja |

Zahlen: Grün 0, Gelb 10, Rot 0.

Skripte: `python3 crm_abgleich.py` für alle Firmen samt Konzern-, Alt- und Schwesternamen selbst wiederholt (zusätzlich: Phoenix Contact, Sütron electronic, Finvest, ROB Electronic, MAFELEC, TTI, Exponential Technology Group, Kautex, Taiyo Yuden, Richter Kunststofftechnik). Ergebnis: kein Treffer auf dieselbe Einheit; Treffer nur Phoenix Contact (Renu-Vorgänger, siehe Firma 1), Richardson RFPD (Firma 2) und sinnlose Wortwurzel-Treffer "Robert Bosch" bei "Robert Karst" (Firma 10, nicht relevant). Wettbewerberliste (wettbewerber_referenzen.md): Grep auf alle zehn Namen im gelesenen Teil ohne Treffer.

Patente (Prüfpunkt 8, Regel F5): Datenbanken (Google Patents, Espacenet, DEPATISnet) nicht direkt abfragbar. Eigene Wiederholung nur für Renu (Anmeldervarianten Sütron, Phoenix Contact HMI-IPC, Renu): keine Treffer. Für die übrigen neun Firmen keine eigene Patentsuche (Budget). Feld 9 bleibt bei ALLEN 10 Firmen nach F5 nicht belegbar; der Batch ist bei Feld 9 und 16 UNVOLLSTÄNDIG im Sinne der Datenbankabfrage, Nachholen im Browser nötig, bevor irgendein Grün final wird. "Keine Treffer" ist nie ein Gegenbeweis.

Messe-Signal (Regel N2) von Tom übernommen, nicht nachgeprüft: bdtronic, ELANTAS, RAMPF, Momentive stellen aus; ändert keine Ampel.

---

## 1. Renu Electronics GmbH | Halle/Stand A1.645
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Filderstadt ist als Produktionsstandort beschrieben, aber nur Stufe S; die Firma gehört zur Renu Group (Indien, Konzern: Stufe V nötig, Sitzregel greift nicht). Verguss Mittel (A: HMI/Touch-Verklebung, Dichtung, EMS-Baugruppen).
- Eigene Prüfung: Identität bestätigt (S): Renu Electronics GmbH, ehemals Phoenix Contact HMI-IPC Technology GmbH, davor SÜTRON electronic GmbH; Verkauf an Renu Electronics (Pune, Indien) Ende 2021, "Teil der Renu Group seit 2022". Phoenix Contact kündigte 2021 an, die Fertigung in Filderstadt laufe "unverändert" weiter (S, computer-automation.de; Quelle von 2021, keine aktuelle Aussage, Lehre 17). Renu-Seite (S): SMT/THT-Fertigung, Box-Build, Test in Filderstadt; Zählerfertigung in Indien. Keine aktuelle Stellenanzeige Renu Filderstadt gefunden.
- CRM: "Renu Electronics", "Renu Electronics Pvt", "Sütron" neu. Neu gegenüber Tom: "Phoenix Contact" steht im CRM (bekannte_firmen Z. 1812, 1814, 1815; E-Mobility GmbH Z. 1813). Phoenix Contact ist laut Quellenlage nicht mehr Eigentümer (Verkauf 2021, S), also nicht Zeile 3. Einheit/aktuelle Beziehung trotzdem von Jey bestätigen lassen.
- Korrekturen an Toms Feldern: Feld 12 "neu" ergänzen um Hinweis "Vorgänger Phoenix Contact im CRM". Feld 9: eigene Suche (Sütron/Phoenix Contact HMI-IPC/Renu): keine Treffer, nicht belastbar. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Werden die HMI-Geräte und EMS-Baugruppen heute noch in Filderstadt gefertigt/montiert (aktueller Beleg 2025/2026)? Wo nachsehen: Impressum und Standortseite renuelectronics.de, Stellenanzeigen Filderstadt (Fertigung, SMT, Montage), SPS-Ausstellerprofil; Produkt-zu-Werk-Zuordnung (HMI Filderstadt, Zähler Indien). Zusätzlich: Wird bei Renu vergossen/verklebt (Optical Bonding, Schutzlack)? Und: Besteht noch eine Geschäftsbeziehung zum CRM-Kontakt Phoenix Contact (Jey)?
- Nicht verwendbare Aussagen: Fertigung Filderstadt (S, 2021); Verguss aller Bauteile (A); Zählerfertigung Indien (S); 51 bis 100 Mitarbeitende (S); Rechtsform/Register (nicht gelesen). Stichprobe für Jey: ja.

## 2. RFMW - MRC Gigacomp GmbH & Co. KG | Halle/Stand C5.561
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB, Rot-Kandidat E2 (Tabellenzeile 7).** Distributor (HF/Mikrowellen-Bauelemente) mit Lager in Freising; keine Fertigung gefunden. Rot nach E2 verlangt Stufe V, hier nur S. Verguss Niedrig (Handelsware, A).
- Eigene Prüfung (S): MRC Gigacomp/MRC Components vertreten und vertreiben Hersteller von HF-/Mikrowellen-Komponenten in DACH und Benelux; 2023 von RFMW übernommen; RFMW gehört seit 2018 zu TTI Inc. / Exponential Technology Group (S, Business Wire, deutsche Fassung). Konzernnamen TTI und Exponential Technology Group im CRM: kein Treffer. "Richardson RFPD" ist ein anderer Distributor, kein Konzernbeleg, nicht Zeile 3.
- Korrekturen an Toms Feldern: Feld 4 Zusatz Konzern TTI/XTG (S). Feld 9/16 weiter nur Kurzprüfung. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Hat die Freisinger Gesellschaft Eigenfertigung oder eigene Produkte? Wo nachsehen: Impressum rfmw.com/rfmw-germany bzw. mrc-gigacomp.de, Handelsregister (Gegenstand der Gesellschaft). Bei Bestätigung Rot nach E2 mit Quelle.
- Nicht verwendbare Aussagen: "Distributor ohne Fertigung" (S, nicht V); Konzern TTI/XTG (S); Verguss Niedrig (A). Stichprobe für Jey: nein (nur Bestätigung E2).

## 3. RG Elektrotechnologie GmbH | Halle/Stand A1.502
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Produkt und Werk nicht belegt, keine Website gefunden; Sitzregel greift nicht (kein erkennbarer Geräte-/Industriebauer).
- Eigene Prüfung (S, Implisense): HRB 107964, Quedlinburg OT Gernrode. Gegenstand laut Verzeichnis ist breiter als bei Tom: "Entwicklung, Herstellung, Vertrieb, Reparatur von Maschinen und Ausrüstungen, insbesondere Elektronik-Produktionsmaschinen und Fertigungsausrüstung, Zubehör und Engineering", daneben elektrische/elektronische Baugruppen (Installation), Mess-/Regeltechnik, Breitband-/Verkabelung. Das könnte Maschinenbau für die Elektronikfertigung bedeuten (dann Fertigung ggf. Hoch, aber Verguss und mögliche Nähe zu Wettbewerbern in E1 offen). Nicht von Tom genannt. Nicht V. Eigene Suchen fanden keine Website und kein Messeprofil.
- Korrekturen an Toms Feldern: Feld 6 und 8 (Verguss Mittel "?") nicht verwendbar; Gegenstand "Elektronik-Produktionsmaschinen" ergänzen. Feld 17 bleibt teilweise belegt. CRM neu. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Was stellt die RG Elektrotechnologie GmbH in Gernrode her (Baugruppen für Kunden, Maschinen für die Elektronikfertigung, Dosier-/Vergussanlagen = E1)? Wo nachsehen: electronica-Ausstellerprofil (Halle A1, Stand 502), Impressum/Website, Handelsregister Stendal (HRB 107964, Gegenstand im Wortlaut), Stellenanzeigen Gernrode.
- Nicht verwendbare Aussagen: Fertigung Gernrode (?); Verguss Mittel (?); Bilanzsumme (S). Stichprobe für Jey: ja (Produkt völlig offen).

## 4. RIGOL Technologies EU GmbH | Halle/Stand A4.231
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB, Rot-Kandidat E2/E3 (Tabellenzeile 7).** Europa-Vertriebs-/Serviceeinheit in Gilching, Fertigung der Mutter in China (S). Rot braucht V.
- Eigene Prüfung (S): Mehrere RIGOL-Impressen führen "RIGOL Technologies EU GmbH", Gilching, Geschäftsführer Yue Wang; Registerangaben widersprüchlich (HRB-Nummer unterschiedlich geschrieben), Adresse Friedrichshafener Str. 5 gegen Carl-Benz-Str. 11 (beide Gilching). Die Identität ist damit besser belegt als bei Tom (Name stimmt zur Vorgabe), bleibt aber S. Keine Fertigung in Gilching gefunden.
- Korrekturen an Toms Feldern: Feld 17 aktualisieren (Name "RIGOL Technologies EU GmbH" im Impressum bestätigt, S; zwei Adressen). Zitat im Browser bestätigt: nein. CRM neu.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Gibt es Endmontage, Kalibrierung mit Fertigungscharakter oder Eigenprodukte in Gilching? Wo nachsehen: Impressum rigol.com/europe/legal/Imprint.html und eu.rigol.com, Handelsregister München (Gegenstand), Stellenanzeigen Gilching. Bei Bestätigung Rot nach E2/E3 mit Quelle.
- Nicht verwendbare Aussagen: Fertigung nur in China (S); Verguss der Messgeräte (A); Registernummer (widersprüchlich). Stichprobe für Jey: nein.

## 5. RIKEN KEIKI | Halle/Stand C1.214
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB, Rot-Kandidat E2/E3 (Tabellenzeile 7).** Tochter Riken Keiki GmbH Eschborn (seit 2017, zuständig für Europa ohne UK, S) für Vertrieb/Service; Fertigung nicht in DE belegt.
- Eigene Prüfung (S): Silicon-Saxony-Profil bestätigt Mergenthalerallee 15-21, 65760 Eschborn, Tochter von Riken Keiki Co. Ltd. Kein Register-/Impressumtreffer. Weder Lager noch Montage in Eschborn belegt. Produkt (Gassensoren, Ex-Schutz) hätte hohen Verguss, aber nicht in DE/AT/NL gefertigt (S).
- Korrekturen an Toms Feldern: keine inhaltlichen. Feld 17: Rechtsform "GmbH" nur Verzeichnis (S). CRM: "Riken Keiki GmbH", "Riken Keiki Co" neu. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Gibt es Montage, Konfektionierung oder Fertigung in Eschborn? Wo nachsehen: Impressum rikenkeikigmbh.com (Domain laut Verzeichnis), Handelsregister Frankfurt/Amtsgericht (Gegenstand), Stellenanzeigen Eschborn. Bei Bestätigung Rot nach E2/E3 mit Quelle.
- Nicht verwendbare Aussagen: Fertigung Japan (S); Verguss Hoch für Produkt (A, ohne Bedeutung für Eschborn). Stichprobe für Jey: nein.

## 6. RIKUTEC Germany GmbH & Co. KG | kein Stand angegeben
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6).** Fertigung Altenkirchen plausibel (S), aber Gruppe mit Werken in DE/FR/ES (Konzern: V nötig); Verguss für Behälter/Blasformteile Niedrig, nur Maschinen-Steuerelektronik Mittel (A, nachrangig).
- Eigene Prüfung (S): Blasformspezialist und Blasformmaschinen-Bauer (Maschinenbau als Basis), Produktion in Deutschland, Frankreich, Spanien; die Haushalts-Behälterfertigung wird laut Fachpresse von Altenkirchen nach Drulingen (FR) und Lantarón (ES) verlagert (S, Datum nicht bestätigt). Kooperation Kautex Maschinenbau für internationalen Vertrieb von Rikutec-Maschinen (S, Kautex nicht im CRM). Als Maschinenbauer wären die Anlagen (Steuerung, Schaltschrank) ein möglicher Verguss-Bezug, nicht belegt.
- Korrekturen an Toms Feldern: Feld 7 Zusatz: Verlagerung Haushaltsproduktion ins Ausland (S) schwächt Fertigung Altenkirchen für Behälter. Feld 1: Messeprofil ohne Halle/Stand (Eingabe fehlerhaft, an Jey melden). CRM neu. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Welche Produkte entstehen in Altenkirchen (Maschinen, Großbehälter) und enthalten diese dosierte/verklebte/vergossene Bauteile (Steuerungen, Heizelemente, Sensorik, Wärmespeicher mit Elektronik)? Wo nachsehen: Produkt- und Standortseite rikutec.com, Sparte "Thermal Storage/Energietechnik", Stellenanzeigen Altenkirchen.
- Nicht verwendbare Aussagen: Fertigung Altenkirchen (S); Verguss (A); Mitarbeiterzahlen (S). Stichprobe für Jey: nein.

## 7. RM Components GmbH | Halle/Stand B6.135 / C6.530
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB, Rot-Kandidat E2 (Tabellenzeile 7).** Großhändler für SMD-Bauelemente (Taiyo Yuden, Holystone) mit Lager Schwabach; einzige Quelle ist die Stadt-PM von 2015 (Lehre 17).
- Eigene Prüfung (S): Stadt Schwabach 2015 bestätigt Distribution; elektroniknet-Anbieterkompass nennt O'Brien-Str. 5, 91126 Schwabach (Straße neu gegenüber Tom, aktuelles Datum nicht erkennbar). Keine Eigenprodukte gefunden. Ersteinschätzung "Transformatoren/Spulen" bleibt zu Recht verworfen (Handelsware). Taiyo Yuden im CRM: neu.
- Korrekturen an Toms Feldern: Feld 4 Straße ergänzen (S). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Hat sich das Geschäftsmodell seit 2015 geändert (Eigenprodukte, Fertigung)? Wo nachsehen: aktuelle Firmenwebsite/Impressum, Handelsregister Fürth (Gegenstand), electronica-Ausstellerprofil. Bei Bestätigung Rot nach E2 mit aktueller Quelle.
- Nicht verwendbare Aussagen: "Großhändler" (S, 2015); Umsatz/Mitarbeiter (S, veraltet). Stichprobe für Jey: ja (nur alte Quelle).

## 8. ROB GmbH | Halle/Stand A1.123
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** EMS-Fertiger mit SMT-Linie in Neulingen laut Stellenanzeigen-Snippets (S); Fertigung Stufe S, Sitzregel nicht anwendbar (Auftragsfertiger, Stufe V nötig). Verguss Mittel (A).
- Korrektur an Tom (wichtig): Cemtrex ist nicht der aktuelle Konzern. Cemtrex hat ROB Cemtrex laut eigener Pressemeldung am 22.08.2019 verkauft (ca. 250 Mitarbeitende, DE und Rumänien; Kaufpreis 6,37 Mio. EUR, S); ein Fachmedium nennt die Finvest GmbH (Beteiligungsgruppe) als Käufer (eine Quelle, S, nicht bestätigt). Der aktuelle Eigentümer ist damit unbelegt. "Finvest" und "Cemtrex" im CRM: kein Treffer. Identität sonst bestätigt (S): ROB GmbH, Am Wolfsbaum 1, 75245 Neulingen, Amtsgericht Mannheim HRB 724976. Stellenanzeigen (SMT-Einrichter, Löter/AOI) nennen ROB GmbH Neulingen (S, undatiert). Rumänisches Werk der Vorgängergruppe: Hinweis auf Fertigung im Ausland, ob noch zur ROB GmbH gehörig, unbekannt.
- Korrekturen an Toms Feldern: Feld 4/12/17: Konzernzugehörigkeit "Cemtrex" streichen bzw. als Altzustand (bis 2019) kennzeichnen. Feld 9: eigene Suche nicht wiederholt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Wird bei ROB GmbH in Neulingen aktuell bestückt/montiert (Beleg V: Impressum, Standortseite, datierte Stellenanzeige)? (b) Wer ist heute Eigentümer (Finvest?) und gibt es einen Konzern mit CRM-Bezug? Handelsregister Mannheim HRB 724976, Impressum. (c) Welche Branchen/Produkte (Automotive, Medizin, Industrie) und wird vergossen/Schutzlack aufgetragen? Stellenanzeigen im Original.
- Nicht verwendbare Aussagen: Fertigung Neulingen (S); Verguss (A); Konzern Cemtrex (veraltet); Käufer Finvest (S, eine Quelle); Mitarbeiterzahl (widersprüchlich). Stichprobe für Jey: ja.

## 9. Röchling Industrial Lahnstein SE & Co. KG | Halle/Stand C1.860
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6).** Fertigung Lahnstein Hoch (S, Stellenanzeigen "Produktion Profilextrusion"; Konzern: V fehlt); Verguss Niedrig bis Mittel: Halbzeuge (Platten, Stäbe, Rohre, Profile) und zerspante Teile, kein Vergussprodukt. Kein E1: Röchling ist weder Anlagen- noch Vergussmassenhersteller (Durostone sind Faserverbund-Platten/Profile aus Epoxid-/Polyesterharz, also Isolierwerkstoffe, kein Wettbewerbsprodukt zu Demak-Harzen).
- Eigene Prüfung (S): Jobportal Röchling nennt in Lahnstein Produktionsmitarbeiter Profilextrusion und eine Stelle "Industriemanager Halbleiterindustrie"; Stellenanzeigen beschreiben Platten/Rundstäbe/Profile aus Thermoplasten und Zerspanung nach Zeichnung. Kein Hinweis auf Kleben, Dichten oder Elektronikbaugruppen in Lahnstein. Durostone (Elektroisolation für Trafos, Schaltanlagen) gehört nach Quelle zu Röchling Industrial allgemein, nicht dem Werk Lahnstein zugeordnet. CRM: "Röchling Industrial", "Röchling SE", "Roechling" neu.
- Korrekturen an Toms Feldern: Feld 8 bestätigt Niedrig; Zusatz: Kunden-Fertigteile für Halbleiter/Elektronik möglich, aber unbelegt. Feld 9: Tom führte zwei Suchen aus; nicht wiederholt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Fertigt Lahnstein Teile, in denen verklebt, gedichtet oder vergossen wird (Halbleiter-/Elektronikteile, Verbundteile mit Verklebung)? Wo nachsehen: roechling.com/industrial/lahnstein (Sparten, Branchen Halbleiter/Elektronik), Datenblatt-Programm Lahnstein, Stellenanzeige "Industriemanager Halbleiter". Aktion: geringe Priorität.
- Nicht verwendbare Aussagen: Fertigung Lahnstein (S, Konzern); Verguss (A); Mitarbeiterzahl (S, widersprüchlich). Stichprobe für Jey: nein.

## 10. ROKA - Robert Karst GmbH & Co.KG Elektrotechnische Fabrik | Halle/Stand B2.331
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Sitz widersprüchlich).** Die Messeangabe 12277 Berlin (Marienfelde) widerspricht der Verzeichnisadresse Gneisenaustraße 27, 10961 Berlin (S, Verzeichnis, gegründet 1901). Ohne geklärten Standort ist die Sitzregel (Stufe A) nicht sauber anwendbar; ohne den Widerspruch wäre Zeile 4 denkbar (Elektrotechnische Fabrik, kein Konzern/Händler), aber Verguss nur Mittel: Standard-Koaxsteckverbinder werden selten vergossen.
- Eigene Prüfung (S): Zweite Suche bestätigt dieselbe Firmierung, roka-berlin.de, Produkte (Kabelschellen, NF-/HF-Steckvorrichtungen, Koaxialstecker; Forum nennt Einpressstecker und Gehäuse), nur Industriekunden. Kein Hinweis auf den Fertigungsort (kein "Made in", kein Impressum, keine Stellenanzeige), also auch kein Beleg gegen Zukauf aus Asien. CRM: neu (Wortwurzel-Treffer "Robert Bosch" irrelevant).
- Korrekturen an Toms Feldern: Feld 7: "Mittel Stufe A (Sitzregel)" zu vorsichtig angesetzt; wegen Standortwiderspruch nicht als Sitzregel verwenden. Feld 17 Abweichung bleibt (zwei PLZ). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Welcher Standort ist der Sitz/Fertigungsort (Marienfelde 12277 oder Kreuzberg 10961)? Impressum roka-berlin.de, Handelsregister Berlin-Charlottenburg, electronica-Ausstellerprofil. (b) Wird in Berlin gefertigt oder zugekauft; werden Kabel/Stecker vergossen oder überspritzt? Produktseite, Datenblätter, Stellenanzeigen Berlin.
- Nicht verwendbare Aussagen: Fertigung Berlin (A/?); Verguss Steckverbinder (A); Forumsaussage zu Industriekunden (S, sekundär). Stichprobe für Jey: ja.

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind überall korrekt niedrig angesetzt (keine V-Aussage vorgetäuscht). Er hat keine Firma als "interessant" geführt; die Einstufungen "prüfenswert" (Renu, RG, ROB, ROKA) bleiben vorläufig.
- Gegenüber Tom neu: Phoenix Contact im CRM (Renu-Vorgänger); Cemtrex-Verkauf 2019 (ROB); Gegenstand "Elektronik-Produktionsmaschinen" bei RG; Verlagerung der Rikutec-Behälterfertigung ins Ausland; Konzern TTI/XTG bei RFMW.
- Die vier Distributor-/Vertriebsfälle (RFMW, RM, RIGOL, Riken Keiki) sind Rot-Kandidaten, aber ohne gelesene Quelle nicht Rot (Zeile 1 verlangt V). Schnell erledigt, sobald je ein Impressum/Register im Browser gelesen ist (Phase P, Tom Runde 1).
- Vorschlag Fehlerlog (Jey gibt frei, nicht eingetragen): (1) Konzernangaben aus Gründerjahren prüfen: Cemtrex als Konzern von ROB war seit 2019 veraltet (Datum der Konzernquelle). (2) Beim CRM-Abgleich frühere Eigentümer (Phoenix Contact bei Renu) mitgeben und melden, auch wenn sie nicht mehr Konzern sind.

## Einschränkungen
- Browser nicht verfügbar, WebFetch nicht verfügbar: kein Gegenlesen nach Abschnitt H, kein Impressum, kein Register, kein Datenblatt gelesen; alle Aussagen Stufe S oder A. Keine "Zitat im Browser bestätigt: ja", kein Grün möglich, kein Rot möglich.
- WebSearch: 23 Abfragen (Identität/Fertigung zu Renu 3, ROB 4, RG 2, ROKA 2, Röchling 2, RIGOL, Riken Keiki 2, RIKUTEC, RFMW, RM Components, Patent Renu/Sütron 2, Cemtrex-Verkauf 2). Ergebnisse sind Kurzfassungen und Verzeichnisse; Treffer wie "Finvest als Käufer" sind eine Einzelquelle.
- Patente: nur eine eigene Wiederholung (Renu); Google Patents/Espacenet/DEPATISnet nicht direkt abgefragt; F5 für alle zehn Firmen nicht erfüllt. Rechtsstand entfällt mangels Treffer.
- Wettbewerbereinsatz (F6): nur Abgleich mit wettbewerber_referenzen.md (gelesen bis Zeile 378 von 631; Rest nicht gelesen, Grep zeigte keine Treffer im gelesenen Teil), keine Einzelsuche. "Kein Hinweis" ist nie ein Gegenbeweis.
- Handelsregister/Unternehmensregister nicht abgerufen. Kundendatenbank_export.txt ohne Treffer für alle Firmen (keine "Verifiziert am"-Prüfung nötig).
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
