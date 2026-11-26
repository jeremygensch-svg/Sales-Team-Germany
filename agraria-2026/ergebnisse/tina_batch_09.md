# Tina Batch 09 - agraria 2026 (Prüfung von tom_batch_09.md)
Erstellt: 2026-11-25 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_09.md (Messe agraria Wels 25.-28.11.2026; Länder DE/AT/NL; Nr. 81 bis 90 der Messeliste, hier 1 bis 10).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser geprüft, vorläufig.** Es standen nur WebSearch (Snippets/Kurzfassungen) und Bash zur Verfügung; Chrome-Werkzeuge nicht genutzt (nicht verfügbar), WebFetch nicht eingesetzt. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein. Kein Grün ist mailtauglich (Stufe V fehlt).
Vollständigkeit von Toms Datei: 10 vollständige Firmenblöcke, jeweils mit den Feldern 1 bis 17 gefüllt, keine abgeschnittenen Felder. Einschränkung von Tom: keine V-Quelle; Patentfeld nur über WebSearch (Google Patents, Espacenet, DEPATISnet nicht direkt abgefragt); Konzernabgleich AGCO/Bauer Group von Tom nicht ausgeführt (von mir nachgeholt, s. u.). Nach Regel F5 ist Feld 9 daher bei allen Firmen nicht datenbankbelegt: Batch gilt als UNVOLLSTÄNDIG bei den Patenten, Nachholen im Browser nötig. `batch_check.py` nicht ausgeführt.
Skripte: `python3 crm_abgleich.py` für alle Firmen samt Kurz-, Alt-, Konzern- und Schreibvarianten selbst wiederholt (AMT Anlagen-Montagetechnik / AMT Agrar- und Schüttguttechnik; Landmaschinenbau Hubert Auer; AGCO, AGCO GmbH, Massey Ferguson; Röhren- und Pumpenwerk Bauer, Bauer Group, BSA GmbH, FAN Separator, Bauer Voitsberg; Hartmann Stallbauprofis, Hartmann Stalltechnik; Bayer AG, Bayer CropScience; Bayerwald Fenster und Haustüren). Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum aller Einträge: 2026-11-25.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | AMT Anlagen + Schüttguttechnik (Halle 23, Stand 255) | GELB | 2 | ja |
| 2 | APV Technische Produkte GmbH (Halle 22, Stand B60) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 3 | Auer Landmaschinenbau GmbH (Halle 22, Stand A30) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 4 | Austro Diesel GmbH (Freigelände, Stand 10) | GELB | 7 (Rot-Kandidat E2) | nein |
| 5 | Bacsak Christian (Freigelände, Stand 160) | GELB | 2 | nein |
| 6 | Bamberger - Event GmbH (Freigelände, Stand 1000) | GELB | 7 (Rot-Kandidat E2) | nein |
| 7 | Bauer GmbH, vermutl. Röhren- und Pumpenwerk Bauer (Halle 21, Stand C10) | GELB | 2 (Identität; danach Zeile 5, Konzern) | ja |
| 8 | Bauer Hoftechnik GmbH / Hartmann Stallbauprofis GmbH & Co KG (Halle 19, Stand 120) | GELB | 2 | ja |
| 9 | Bayer Austria GmbH (Halle 23, Stand 335) | GELB | 7 (Rot-Kandidat E2) | nein |
| 10 | Bayerwald GmbH (Halle 20, Stand 1260) | GELB | 2 | nein |

Zahlen: Grün 2 (beide schwach, nur Stufe A/S), Gelb 8, Rot 0. Kein Rot, weil für E2 überall die Stufe V fehlt (Regel E: Rot nur mit Quelle).

Jey-Entscheidungen angewandt: Verbände/Prüfdienstleister/Forschung: keine im Batch. CRM-Gleichnamigkeit: bei keiner Firma identischer oder sehr ähnlicher Kern-Name im CRM; die "Bauer"-Präfixtreffer (bekannte_firmen_DE-AT-NL.txt Zeilen 215 bis 217: Bauer & Böcker GmbH & Co. KG, BAUER Elektroanlagen Holding SE, Bauer Gear Motor GmbH, alle DE) haben andere Kern-Namen, Orte und Branchen; ich werte sie nicht als gleiche Einheit, Jey bitte bestätigen (Nr. 7, 8). Anlagenbauer bleiben drin: AMT baut nach den Quellen Rohrleitungs-/Anlagenbau und Trockner, keine Verguss-/Dosieranlagen (kein E1-Hinweis). Gegenprobe Konzernbezüge: AGCO/Massey Ferguson, BSA, FAN Separator, Bayer AG/CropScience, Hartmann: kein CRM-Treffer.

Patente (Prüfpunkt 8, F5): Google Patents, Espacenet und DEPATISnet nicht direkt abfragbar (kein Browser). Eigene Patent-WebSearch nur für Bauer (Nr. 7, 1 Abfrage); für die übrigen Firmen keine eigene Wiederholung, Toms Suchen werden weder übernommen noch widerlegt. "Keine Treffer" ist kein Gegenbeweis. Wettbewerbereinsatz (F6): Grep auf wettbewerber_referenzen.md mit amt, apv, auer, austro, bacsak, bamberger, bauer, hartmann, bayer, bayerwald, agco, massey: nur Namens-Fremdtreffer (Auer/Bauer in Fußnoten bzw. Firmen anderer Art, Fichter-Maschinen etc., keiner zu den geprüften Firmen); keine Einzelsuchen mit Wettbewerbernamen von mir. Messe-Signal: laut Tom keine Wettbewerber in der Ausstellerliste (von mir nicht wiederholt). Aussteller-Schreibweisen von mir nicht erneut gegen die CSV geprüft.

---

## 1. AMT Anlagen + Schüttguttechnik | Halle 23, Stand 255
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Zeile 1 greift nicht (kein CRM-Treffer, kein E-Beleg V); Zeile 2 trifft, weil die Zuordnung Messename "AMT Anlagen + Schüttguttechnik" zu "AMT Anlagen-Montagetechnik GmbH" (Kirchbach, FN 305255 f) nur Annahme ist. Meine Suche bestätigt das Unternehmen als Eintrag (evi.gv.at/f/305255f, WKO, KSV; S) und nennt als Geschäftszweck Rohrleitungsbau, Anlagenbau, Industriemontage (Wirtschaftsforum-Interview, S) plus zweiter Standort Greinbach (WKO, S). Trockner (Umlauf/Durchlauf/mobil) werden bei einem Landwirt.com-Händlerprofil unter derselben Adresse angeboten (S, Entitätszuordnung offen). Eigene Fertigung von Schaltschränken/Elektrik nicht gefunden. Verguss: Mittel (A, Steuerung/Sensorik/Brennersteuerung), Fertigung Kirchbach nicht belegt (Montageunternehmen, Teile ggf. zugekauft).
- CRM: kein Treffer (alle drei Schreibweisen), neu. E1: kein Hinweis auf Dosier-/Vergussanlagenbau.
- Korrekturen an Toms Feldern: Feld 4 ergänzt: zweiter Standort Greinbach (WKO, S), Fertigungsort daher zusätzlich offen; Feld 7 "Hoch (A)" nicht belastbar (Montage-/Rohrleitungsfokus, Fertigung eher Anlagenmontage vor Ort statt Serienfertigung); Toms "prüfenswert" bleibt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Ist die Messefirma = AMT Anlagen-Montagetechnik GmbH (Kirchbach/Greinbach)? Messeprofil agraria.at/aussteller (Browser), Impressum amt-agrar.com, Firmenbuch FN 305255 f. (b) Was wird gebaut und wo (Werk Kirchbach oder Greinbach; Schweißen, Schaltschrankbau; Trockner eigen oder Handel)? Stellenanzeigen und Produktseiten im Browser lesen. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Identität (A), Fertigung (S/A), Verguss aller Bauteile (A), Produkte Mühlen/Futtermischwagen (unbelegt). Stichprobe für Jey: ja (Identität und Produktrolle offen).

## 2. APV Technische Produkte GmbH | Halle 22, Stand B60
**ohne Browser geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Fertigung Stufe A nach Sitzregel, Verguss Mittel A).** Zeile 1 nicht (CRM neu, kein E), Zeile 2 nicht (Name in mehreren Verzeichnissen stimmig, Hötzelsdorf; Adresse Dallein 15/62 uneinheitlich, S), Zeile 3 nicht, Zeile 4 trifft: eigener Landtechnikhersteller mit Marke (Sämaschinen, Streuer, Walzen), erkennbarer Standort, kein Händler, kein Konzern, kein Auslagerungshinweis; Produkt mit "elektrisch gesteuerter Säwelle" (Prospekt-Snippet, S) und Terminal/Gebläsemotor/Sensorik: Verguss Mittel (A). Meine Stellensuche (APV Hötzelsdorf Montage) lieferte keinen APV-Treffer; kein Gegenbeleg, aber auch kein Fertigungsbeleg.
- CRM: kein Treffer, neu. Patent: keine eigene Wiederholung; Toms Ergebnis "kein Anmelderpatent, zwei Marken (Justia)" von mir nicht bestätigt.
- Korrekturen an Toms Feldern: keine inhaltlichen. Hinweis: "Peuerbach" in Toms Suchabfrage bleibt unbestätigt; Sitz Hötzelsdorf (S). Zitat im Browser bestätigt: nein.
- Nachrecherche (für Mailstufe nötig, kein Gelb): (a) Impressum apv.at: Rechtsform, Adresse (Dallein 15 oder 62), Firmenbuch. (b) Prospekt/Datenblatt PS-Serie: Elektronik, Motor, IP-Klasse; Karriereseite: Schlosser/Montage in Hötzelsdorf (Fertigung V). (c) Patente Google Patents/Espacenet (Anmelder-Varianten Ges.m.b.H./GmbH).
- Nicht verwendbare Aussagen: Fertigung Hötzelsdorf (A/S); alle Verguss-Bauteile (A); Patentfeld. Stichprobe für Jey: ja (Grün ohne V; Elektronikanteil unbelegt).

## 3. Auer Landmaschinenbau GmbH | Halle 22, Stand A30
**ohne Browser geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Fertigung Stufe A nach Sitzregel, Verguss Mittel A).** Landmaschinen-/Forsttechnikhersteller mit eigenem Namen, Sitz Hellmonsödt (WKO, S), "Manufactured by Auer Landmaschinenbau GmbH based in AUSTRIA" (S). Neu aus meiner Suche: Händlerbroschüre (agropool.ch, S): Hydraulikzylinder werden im Haus gefertigt, die Krane kommen aus Hellmonsödt, optionale Funksteuerung; Selbstdarstellung: baut seit 1922 Landmaschinen, Forstmaschinen seit 1998, 48 Mitarbeiter (agriculture-xprt/karriere.at, S; Gründungsjahr uneinheitlich 1922/1927). Das stützt Fertigung am Sitz (S, nicht V). Verguss Mittel (A): Funkfernsteuerung (laut Broschüre Option, Herkunft unbekannt, vermutlich zugekauft), Elektrohydraulik/Ventilspulen; Hauptprodukt mechanisch-hydraulisch. Kein Konzern, Importeur für Krane ab 2022: TECHNICA Agro + Kran GmbH (Vertrieb, nicht Fertigung).
- CRM: "Auer Landmaschinenbau", "Landmaschinenbau Hubert Auer": kein Treffer, neu. Gleichnamige Betriebe (Landmaschinen Franz Auer, Auer Josef) nicht vermischt; Patent AT406927B (Anmelder "Landmaschinenbau Hubert Auer K.") nicht zugeordnet, rein mechanisch, kein Signal.
- Korrekturen an Toms Feldern: Feld 4/7 durch Händlerbroschüre (S) gestützt, bleibt Hoch (A/S); Verguss bleibt Mittel (A), schwächer als Nr. 2 (Elektronikanteil gering). Zitat im Browser bestätigt: nein.
- Nachrecherche (kein Gelb): (a) Impressum und Karriereseite (Hellmonsödt: Schweißer, Monteur Elektrik) im Browser lesen; Auer-Website ermitteln. (b) Datenblatt Funksteuerung/Steuergerät: eigene Elektronik oder zugekauft, IP-Klasse. (c) Klären, ob GmbH und "Hubert Auer" dieselbe Gruppe sind.
- Nicht verwendbare Aussagen: Fertigung (S/A); Verguss (A); Patentzuordnung. Stichprobe für Jey: ja (Grün ohne V, Elektronikanteil gering).

## 4. Austro Diesel GmbH | Freigelände, Stand 10
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2).** Generalimporteur und Händler für Massey Ferguson (Landwirt.com-Händlerprofil, S; Eulerpool/Firmenbuchverzeichnis, FN 240246 d, S). Nach E2 Rot, aber nur mit Stufe V belegbar; meine Suche (Impressum/Produktion/Aufbauten) fand keine Fertigung und keinen Impressumstext. Konzern: AGCO/Massey Ferguson gegen CRM mit Skript nachgeholt: kein Treffer; Austro Diesel gehört nach den Quellen nicht zu AGCO (Importeur).
- Korrekturen: keine. Feld 12 ergänzt: Konzernabgleich jetzt ausgeführt (AGCO, AGCO GmbH, Massey Ferguson: neu). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Bestätigen, dass keine eigene Fertigung/Aufbauten bestehen. Impressum/"Über uns" austrodiesel.at im Browser lesen, Zitat als V sichern; bei Händler ohne Fertigung Rot nach E2 mit URL. Aktion: nicht weiter verfolgen.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 5. Bacsak Christian | Freigelände, Stand 160
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Kein Eintrag über Toms Suche; ich habe keine eigene Identitätssuche zu Bacsak wiederholt (offene Lücke, nicht ausgeführt). Name legt Einzelperson/Einzelunternehmen nahe (A), Messeliste nur "Sonstiges" (S). Fertigung und Verguss unbekannt; Rot nur bei V-Beleg (Freiberufler/Händler, E2/E3), sonst nicht.
- CRM: kein Treffer, neu (Bacsak Christian, Bacsak). Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer/was ist "Bacsak Christian"? Messeprofil agraria.at/aussteller (Browser), WKO-Firmen-A-Z, Firmenbuch; Schreibvarianten Bačsak/Bacsák. Danach: wird etwas hergestellt? Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (?). Stichprobe für Jey: nein (geringe Relevanz).

## 6. Bamberger - Event GmbH | Freigelände, Stand 1000
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2, Dienstleister).** Eintrag WKO (Oichten 27, Feldkirchen bei Mattighofen, S); Event/Veranstaltung nur aus Name abgeleitet (A), Geschäftszweck nicht gelesen. Keine eigene Wiederholung der Suche. Verguss Niedrig (A).
- CRM: "Bamberger Event", "Bamberger - Event GmbH": kein Treffer, neu. Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Geschäftszweck laut Firmenbuch/Gewerbeberechtigung (Eventservice oder Produktion/Herstellung von Ausstattung?), WKO-Eintrag im Browser lesen; bei Dienstleistung ohne Fertigung Rot nach E2 mit URL. Aktion: nicht weiter verfolgen.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 7. Bauer GmbH (vermutlich Röhren- und Pumpenwerk Bauer Ges.m.b.H., Voitsberg) | Halle 21, Stand C10
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2: Zuordnung des Messenamens "Bauer GmbH" zur Voitsberger Firma nicht belegt; danach Zeile 5: Konzern, Stufe V für Fertigung nötig).** Hätte die Zuordnung Bestand, wäre es der aussichtsreichste Kandidat des Batches: Maschinen-/Anlagenbauer, Beregnungsmaschinen mit Steuerung (Rainstar, eco ProRain), Pumpen, Separatoren.
- Eigene Prüfung (WebSearch, S): Firmenbuchverzeichnisse bestätigen "Röhren- und Pumpenwerk Bauer Gesellschaft m.b.H., Kowaldstraße 2, 8570 Voitsberg, FN 34294 h" (evi.gv.at, KSV); Bauer Group "develops and produces innovative wastewater and irrigation technology" (greentech.at, S); Messeprofil expoagro.german-pavilion.com führt "Röhren- und Pumpenwerk Bauer Gesellschaft m.b.H./FAN Separator GmbH" (nur Titel, S); Prospekt eco ProRain: Touchscreen-Bedienung, Verbrauchserfassung, Mobilsteuerung (S, Fertigungsort der Elektronik nicht genannt); Karriereseite karriere.at/f/bauer-röhren-u-pumpenwerk existiert (nicht gelesen). Konzern (FAN Separator, BSA): CRM kein Treffer (Skript, nachgeholt).
- Patente (eigene WebSearch, S): Anmelder "Röhren- und Pumpenwerk Rudolf Bauer AG, Voitsberg": EP0297084 / AT387305B "Steuerung zur Regelung der Rohreinzugsgeschwindigkeit einer Trommelberegnungsmaschine" (1988), AT368833B "Kontroll- und Steuervorrichtung zur Steuerung des Beregnungsablaufs" (1980), AT384346B "Korrektursteuerung für Berieselungssystem" (1985); AT389422B (Regner mit Funksteuerung) Anmelder nicht eindeutig; Rechtsstand: einzelne (z. B. AT365886B) laut Snippet erloschen, übrige nicht geprüft. Steuerungspatente belegen eigene Entwicklung von Steuerungen, bestehen aber nur als schwaches Zusatzsignal (alt, Rechtsstand offen), kein Verguss-Signal. Toms neuere Treffer (Separatoren 2022/2024, Aggregatoren) nicht wiederholt.
- CRM: CRM-Präfixtreffer Bauer & Böcker, BAUER Elektroanlagen Holding SE, Bauer Gear Motor GmbH (bekannte_firmen Zeilen 215 bis 217, alle DE): anderer Kern-Name und Ort; "Röhren- und Pumpenwerk Bauer": neu. Einheit und Konzernbezug (Bauer Group Voitsberg, BSA Bayern, FAN Separator) gegen CRM: keiner. Verguss Mittel (A: Bordcomputer/Steuerung, Sensorik, Funkmodule, Antriebe), mit Eigenentwicklung von Steuerungen (Patente S) eher am oberen Ende von Mittel.
- Korrekturen an Toms Feldern: Feld 12: Konzernabgleich nachgeholt (neu). Feld 9: zusätzlich Steuerungspatente 1980 bis 1988 (Anmelder Rudolf Bauer AG, Voitsberg) ergänzen. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2, danach 5): (a) Messeprofil agraria.at/aussteller Stand C10 Halle 21 im Browser: ist "Bauer GmbH" die Voitsberger Gruppe? Impressum bauer-at.com. (b) Welche Gesellschaft fertigt Beregnung/Steuerung, wo (Voitsberg, Töchter FAN Separator, BSA GmbH Bayern)? Karriereseite (Elektronik-/Steuerungsmontage, Vergießen), Datenblatt eco ProRain: IP-Klasse, Elektronik eigen oder zugekauft; V-Zitat. (c) Patente Google Patents/Espacenet/DEPATISnet (Anmelder-Varianten Rudolf Bauer AG / Ges.m.b.H.), Rechtsstand. (d) Jey: Bauer & Böcker u. a. als andere Firmen bestätigen. Aktion: nicht kontaktieren; bei Beleg Grün erwartbar.
- Nicht verwendbare Aussagen: Identität (A); Fertigung (S); Verguss aller Bauteile (A); Patente (Rechtsstand offen). Stichprobe für Jey: ja.

## 8. Bauer Hoftechnik GmbH / Hartmann Stallbauprofis GmbH & Co KG | Halle 19, Stand 120
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität: zwei Firmen in einem Messenamen, Hartmann nicht auffindbar).** Meine Suche bestätigt nur den KSV-Registereintrag Bauer Hoftechnik GmbH, Gewerbepark Süd 11, 5141 Moosdorf, FN 316784 i, 2008 gegründet, Domain bauerhoftechnik.at (S); keine Aussage, ob Hersteller oder Händler (mit dem Treffer Bauer-Stalltechnik anderer Händler nicht vermischt). Fertigung offen, Verguss Mittel (A: Tor-/Entmistungsantriebe, Tränkenheizung; bei Handel nicht zählbar). Sitzregel greift nicht (Händler-/Fertigerrolle unklar).
- CRM: Bauer Hoftechnik: nur Wortwurzel-Treffer (Zeilen 215 bis 217, andere Firmen); Hartmann Stallbauprofis, Hartmann Stalltechnik: kein Treffer, neu. Konzernbezug zur Bauer Group Voitsberg: nicht belegt (Skript Bauer Group: kein Treffer auf Voitsberg-Einheiten).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Messeprofil im Browser: welche der beiden Firmen stellt aus? (b) Bauer Hoftechnik: bauerhoftechnik.at, Impressum, Produktseiten, Stellenanzeigen Moosdorf: Fertigung oder Handel/Montage fremder Stalltechnik (bei Händler ohne Fertigung E2-Rot mit URL)? (c) Hartmann Stallbauprofis GmbH & Co KG: Sitz, Rechtsform, Fertigung (Firmenbuch, Messeprofil; Hartmann-Stallsysteme Bayern nicht vermischen). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle zu Fertigung, Produkt, Verguss (S/A/?). Stichprobe für Jey: ja (zwei Firmen, Rolle offen).

## 9. Bayer Austria GmbH | Halle 23, Stand 335
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2, Vertriebsgesellschaft eines Konzerns).** Tom: Vertrieb/Beratung Crop Science in Wien (Impressum-Snippet, S), Produktion der Gruppe in anderen Ländern (S). Ich habe die Quellen nicht erneut gesucht; Produkttyp Pflanzenschutzmittel: Verguss Niedrig (A, Produkt hat keine vergossenen Bauteile; Pflanzenschutzgeräte der Messeliste unbelegt). Nach E2/E3 Rot erwartbar, aber nur mit V.
- CRM: Bayer Austria, Bayer CropScience: kein Treffer; Bayer AG/Bayer: nur Präfix/Enthalten-Treffer Bayerische Motoren Werke (Zeile 222) und SGB-SMIT (2037), andere Firmen; kein Konzernbezug. Konzern Bayer AG mit mehreren Werken: für Fertigung Stufe V nötig.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Gibt es eine Produktion der Bayer Austria GmbH in Österreich? Standortseite bayer.com/de-at und Impressum im Browser lesen (V-Zitat); bei reiner Vertriebsgesellschaft Rot nach E2 mit URL. Aktion: nicht weiter verfolgen.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 10. Bayerwald GmbH | Halle 20, Stand 1260
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Meine Suche (Bayerwald GmbH Arbeitsbekleidung Österreich Aussteller agraria Wels) brachte keinen Treffer zur Firma; bestätigt Toms Befund "nicht auffindbar". Die Namensähnlichkeit zu "Bayerwald Fenster und Haustüren GmbH" (Neukirchen vorm Wald, Bayern) bleibt ungeklärt und ist nicht zugeordnet. Verguss Niedrig (A, Textil/Schutzbekleidung), Fertigung unbekannt.
- CRM: "Bayerwald GmbH", "Bayerwald Fenster und Haustüren": kein Treffer, neu. Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer ist die Bayerwald GmbH (Sitz, Rechtsform, Händler oder Hersteller)? Messeprofil agraria.at/aussteller im Browser (Adresse, Website), Firmenbuch/WKO. Falls Händler: Rot nach E2 mit URL. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/A/?). Stichprobe für Jey: nein.

---

## Einschränkungen
- Kein Browser: Chrome-Werkzeuge nicht verfügbar, WebFetch nicht genutzt; keine einzige Quelle selbst gelesen. Keine Stufe V im Batch, keine Aussage mailtauglich. Alle Ampeln vorläufig. Die zwei Grün (Nr. 2, 3) sind nach Sitzregel (Stufe A) begründet und müssen im Browser gegengelesen werden (Regel I).
- WebSearch: 9 Abfragen für diese Prüfung (Schwerpunkt Nr. 7 mit zwei Abfragen inkl. Patente, Nr. 3, 2, 1, 4, 8, 10 je eine); für Nr. 5, 6 und 9 keine eigene Websuche, nur CRM-Skript und Einordnung (Händler/Dienstleister/Vertrieb); Bacsak-Identitätssuche und Quellen zu Bayer Austria nicht wiederholt.
- Patente: Google Patents, Espacenet, DEPATISnet nicht direkt abgefragt; Rechtsstand fast durchweg offen; österreichisches Patentamt nicht abgefragt. Feld 9 gilt nach F5 bei allen zehn Firmen als nicht datenbankbelegt (Batch bei den Patenten unvollständig).
- Wettbewerbereinsatz (F6): nur Grep auf wettbewerber_referenzen.md, keine firmenspezifischen Einzelsuchen; "kein Hinweis" ist kein Gegenbeweis.
- Identität: Impressum und Firmenbuch bei keiner Firma selbst gelesen; offen bei Nr. 1, 5, 7, 8, 10.
- Nichts wurde verschickt, kein Datenbankfeld geändert; keine Kontaktsuche (Abschnitt K); kein git commit.
