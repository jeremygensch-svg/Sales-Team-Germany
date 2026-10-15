# Tina Batch 21 – electronica 2026 (Prüfung von tom_batch_21.md)
Erstellt: 2026-10-15 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q, Messemodus N). Eingabe: ausschließlich electronica/ergebnisse/tom_batch_21.md (10 Firmen, Listen-Nr. 222 bis 231).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Nur WebSearch (12 Abfragen, Snippets/Kurzfassungen) und Bash standen zur Verfügung; WebFetch und Chrome nicht nutzbar. Es gibt in diesem Batch KEINE Stufe-V-Aussage aus der Websuche; "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Einzige gelesene Primärquelle ist die CRM-Textdatei (Rot Nr. 3).
Skripte: `python3 batch_check.py` = VOLLSTÄNDIG (10 Blöcke, formal). `python3 crm_abgleich.py` für alle Firmen, Instituts- und Verbandsnamen selbst wiederholt. Tabellenzeile = Zeilennummer der Ampel-Tabelle D. Verifikationsdatum aller Einträge: 2026-10-15.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | Flextem GmbH (B4.361) | GELB | 2 | ja |
| 2 | Forschungsvereinigung Räumliche Elektronische Baugruppen 3-D MID e.V. (B3.400) | GELB | 7 | ja |
| 3 | Fraunhofer-Gesellschaft zur Förderung der angewandten Forschung e.V. (C5.241) | ROT | 1 (E5) | nein |
| 4 | Fraunhofer ENAS (C5.241) | GELB | 3 | nein |
| 5 | Fraunhofer IIS Institut für Integrierte Schaltungen IIS (C5.241) | GELB | 3 | nein |
| 6 | Fraunhofer-Institut für Keramische Technologien und Systeme IKTS (C5.241) | GELB | 3 | nein |
| 7 | Fraunhofer-Institut für Mikroelektronische Schaltungen und Systeme IMS (C3.300) | GELB | 3 | nein |
| 8 | Fraunhofer-Institut für Physikalische Messtechnik IPM (C1.908) | GELB | 3 | nein |
| 9 | Fraunhofer IZM (C5.241) | GELB | 3 | ja |
| 10 | FrelTec GmbH (A6.100) | GELB | 5 | ja |

Zahlen: Grün 0, Gelb 9, Rot 1.

Patente (Prüfpunkt 8, F5): Google Patents, Espacenet, DEPATISnet waren nicht direkt abfragbar. Eigene Zusatzsuchen nur per WebSearch: IZM (Anmelder Fraunhofer, Vergussmasse): einziger Zufallstreffer DE102020204941A1 (Vergussmasse-Verfahren, Anmelder im Snippet nicht erkennbar, Rechtsstand ungeprüft, nicht zuordenbar); übrige Fraunhofer-Treffer (publica) betreffen Löt-/Flip-Chip-Themen, nicht Verguss. Flextem, FrelTec, 3-D MID: keine Patentdaten gefunden. Feld 9 ist damit bei ALLEN 10 Firmen nicht belastbar; der Batch ist nach F5 UNVOLLSTÄNDIG (Datenbankabfrage im Browser nachholen). Keine Ampel hängt davon ab (kein Grün).

Wettbewerbereinsatz (F6) / Messe-Signal: Messe-Signal von mir gegengeprüft (aussteller_namen.txt Z. 70 bdtronic, 168 ELANTAS, 439 Nordson Test&Inspection/Matrix, 502/503 RAMPF; Scheugenpflug, DOPAG, ViscoTec, Sonderhoff, Henkel, DELO, Wacker nicht gefunden): bestätigt, ohne Einfluss auf die Ampel. Hinweis IZM/Nordson siehe Nr. 9.

---

## 1. Flextem GmbH | B4.361
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).**
- Begründung: Vorgabe "Flextem GmbH, 67240 Bobenheim-Roxheim" ist weder durch Website noch Registereintrag belegt. Meine drei Suchen (Firma+Ort, Firma+Sensorik/electronica, Firma+Handelsregister Ludwigshafen) liefern keine Firma dieses Namens; nur Fremdtreffer (Flextime GmbH AT, Flextron AG CH, Flex GmbH CH, Flexoptix) – nicht vermischt. Produkt, Fertigung und Verguss damit unbekannt (Stufe ?). Kein E-Ausschluss belegt, also nicht Rot.
- Toms Felder: bestätigt. Einstufung "prüfenswert" ist nur Namens-Screening; nach den Regeln nicht tragfähig, bleibt vorläufig. Feld 7/8 "Mittel" beruht auf ? und ist nicht verwendbar. CRM: crm_abgleich.py "Flextem GmbH": kein Treffer, neu. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Gibt es die Flextem GmbH, wo (Sitz laut Messeliste 67240 Bobenheim-Roxheim, Namensvariante prüfen) und was stellt sie her? Wo nachsehen: electronica-Ausstellerprofil (Halle B4, Stand 361) im Browser, Handelsregister (handelsregister.de, Amtsgericht Ludwigshafen), Impressum der dort verlinkten Website, Google-Suche "Flextem" mit Schreibvarianten (Flex-Tem, FlexTem). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Segment Sensorik (?); Fertigung Mittel (?); Verguss Mittel (?); Sitz (nur Messeliste, S). Stichprobe für Jey: ja (Identität).

## 2. Forschungsvereinigung Räumliche Elektronische Baugruppen 3-D MID e.V. | B3.400
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).**
- Begründung: Verein zur Förderung der MID-Technologie mit Mitgliedern aus Industrie und Forschung; keine eigene Fertigung belegt (A/S). E2 nennt wörtlich Hochschulen, Software, Beratung, Händler; ein Forschungsverband steht nicht ausdrücklich dort. Daher kein Rot ohne Entscheidung von Jey. Kein CRM-Bezug. Hinweis Mitglieder: Fertiger von MID-Bauteilen als Kandidaten, aber nicht Gegenstand dieser Zeile.
- Eigene Prüfung: Suche bestätigt Sitz Nürnberg, Fürther Str. 246b, 90429 Nürnberg, Website 3dmid.de (zwei unabhängige Quellen: Bayern Innovativ, Hanser-Buch; beide S); Erlangen (Egerlandstr. 7-9) stammt aus älterem Bayern-International-Eintrag, vermutlich veraltet. Mitgliederzahl widersprüchlich (84 bis über 100). Damit Identität weitgehend belegt (Zeile 2 nicht ausgelöst). CRM: crm_abgleich.py mit Kurz- und Vollname: kein Treffer, neu.
- Korrekturen an Toms Feldern: Feld 5 Website ergänzen: 3dmid.de (S); Feld 4: Nürnberg, Erlangen-Angabe veraltet. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Jey-Entscheidung: Gilt ein reiner Forschungsverband ohne Fertigung als harter Ausschluss (E2-Analogie)? Falls ja Rot mit Quelle 3dmid.de (Impressum/Satzung: Verein, keine Fertigung). Wo nachsehen: 3dmid.de Impressum und "Über uns", Vereinsregister Nürnberg. Aktion: nicht aufnehmen; Mitgliederliste optional als Kandidatenquelle.
- Nicht verwendbare Aussagen: Keine Fertigung (A/S); Mitgliederzahl (S, widersprüchlich); Patent EP0784418A2 (kein Anmeldernachweis). Stichprobe für Jey: ja (Regelfrage E2 für Verbände).

## 3. Fraunhofer-Gesellschaft zur Förderung der angewandten Forschung e.V. | C5.241
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT (Tabellenzeile 1, Ausschluss E5: dieselbe Einheit im CRM).**
- Rot, weil: Firma steht mit identischem Kern-Namen im CRM: bekannte_firmen_DE-AT-NL.txt Zeile 830 "Fraunhofer Gesellschaft [DE]" (crm_abgleich.py "Fraunhofer-Gesellschaft": IDENTISCH, von mir selbst wiederholt, Datei gelesen). Zusätzlich Sitz München (Hansastraße 27c, 80686) und Vereinsform laut Suche (Bayerischer Landtag, Lobbyregister, S) gleiche Einheit wie Messeliste. Bestandskontakt, kein Neukunde. Zusätzlich ohne Fertigung (Forschungsorganisation).
- Korrekturen an Toms Feldern: keine; Feld 12 bestätigt (bekannt, Zeile 830). Institutezahl 75/76 je nach Quelle (nicht relevant). Zitat im Browser bestätigt: nein (CRM-Datei direkt gelesen).
- Nachrecherche-Auftrag: keiner (Rot). Aktion: nicht neu aufnehmen.
- Nicht verwendbare Aussagen: Patente DE102017202956A1 (Titel/Verguss-Bezug ungelesen, S), publica-Eintrag "glass-solder potting" (Anmelder unbestätigt, S). Stichprobe für Jey: nein.

## 4. Fraunhofer ENAS | C5.241
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 3, CRM-Konzernbezug).**
- Begründung: Institut selbst nicht im CRM, aber Fraunhofer Gesellschaft (Zeile 830) und Institute IFAM, IFAM Dresden, IISB, IWU, LBF (Z. 831 bis 837) stehen im CRM; Einheit unklar (Regel M). Unabhängig davon: Forschung, Prototypen, Fertigung Niedrig (S), Verguss Niedrig (A); Dünnschicht-Verkapselung ist keine Vergussmasse.
- Eigene Prüfung: crm_abgleich.py "Fraunhofer ENAS" und "Fraunhofer-Gesellschaft": nur Wortwurzel-Treffer, wie Tom. Keine ENAS-eigene Quelle im Web gelesen. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 3): Ist Fraunhofer ENAS (Chemnitz) als Einheit der im CRM geführten Fraunhofer Gesellschaft zu behandeln, und gilt für Fraunhofer-Institute allgemein dieselbe Behandlung wie für die Gesellschaft (Rot E5 oder separat)? Entscheidung Jey anhand CRM-Datensätzen Zeile 830 bis 837 (Ansprechpartner/Status). Aktion: nicht neu aufnehmen.
- Nicht verwendbare Aussagen: Alles zu Fertigung/Verguss (A/S); Website enas.fraunhofer.de (S). Stichprobe für Jey: nein (Sammelentscheidung mit Nr. 9).

## 5. Fraunhofer IIS Institut für Integrierte Schaltungen IIS | C5.241
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 3).**
- Begründung: wie Nr. 4. IIS selbst nicht im CRM; Präfix-Nähe zu "Fraunhofer IISB" (Z. 833, anderes Institut, ebenfalls Erlangen) und Gesellschaft Z. 830. Forschung (IC-Design, Sensorik), Serienfertigung nicht belegt (S), Verguss Niedrig (A).
- Eigene Prüfung: crm_abgleich.py "Fraunhofer IIS": Präfix IISB, Wortwurzel; Einheit klären. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 3): Siehe Nr. 4; zusätzlich: Ist IIS identisch mit dem CRM-Eintrag "Fraunhofer IISB" (nein nach Namen: IISB = Integrierte Systeme und Bauelementetechnologie, IIS = Integrierte Schaltungen; im CRM gegenprüfen)? Aktion: nicht neu aufnehmen.
- Nicht verwendbare Aussagen: Fertigung/Verguss (A/S); "concept to serial production" (Selbstbeschreibung, S). Stichprobe für Jey: nein.

## 6. Fraunhofer-Institut für Keramische Technologien und Systeme IKTS | C5.241
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 3).**
- Begründung: wie Nr. 4; IKTS selbst nicht im CRM. Eigene Suche bestätigt Abteilung Hybride Mikrosysteme (Dickschicht, Systemintegration/AVT, Dispensing/Jetting als Auftragsverfahren, Pilotmaßstab laut Stellenanzeige; S), aber keine Vergussmassen-Quelle. Fertigung Niedrig (S, Pilot), Verguss Niedrig (A).
- Korrekturen an Toms Feldern: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 3): Siehe Nr. 4. Aktion: nicht neu aufnehmen.
- Nicht verwendbare Aussagen: Verguss Hybridbaugruppen (A); Standort Hermsdorf (S). Stichprobe für Jey: nein.

## 7. Fraunhofer-Institut für Mikroelektronische Schaltungen und Systeme IMS | C3.300
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 3).**
- Begründung: wie Nr. 4; IMS (Duisburg) nicht im CRM. CMOS-Chips, Packaging über Partner (S), Fertigung Niedrig, Verguss Niedrig (S; Chip-Scale-Package mit Lötrahmen statt Verguss). Keine eigene Zusatzsuche zu IMS (Budget).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 3): Siehe Nr. 4. Aktion: nicht neu aufnehmen.
- Nicht verwendbare Aussagen: Fertigung Duisburg (S); Kunststoff-Packaging über Partner (S); allgemeine Sensor-Packaging-Patente (nicht zuordenbar). Stichprobe für Jey: nein.

## 8. Fraunhofer-Institut für Physikalische Messtechnik IPM | C1.908
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 3).**
- Begründung: wie Nr. 4; IPM (Freiburg) nicht im CRM. Prototypen von Mess-/Sensorsystemen, Fertigung Niedrig (S), Verguss Niedrig (A; Gas-/H2-Sensoren Mittel nur als Prototypen, A). Keine eigene Zusatzsuche zu IPM (Budget). Halle/Stand C1.908 abweichend von den übrigen Instituten, laut Liste.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 3): Siehe Nr. 4. Aktion: nicht neu aufnehmen.
- Nicht verwendbare Aussagen: Fertigung/Verguss (A/S); Sensoren Mittel (A). Stichprobe für Jey: nein.

## 9. Fraunhofer IZM | C5.241
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 3).**
- Begründung: IZM (Berlin) nicht im CRM, Konzernbezug Fraunhofer (Z. 830 ff.) wie Nr. 4. Eigene Suche bestätigt Toms Befund: IZM-Themenbroschüre Power (2025) nennt Potting weich/hart als Verfahren für Leistungselektronik (S), CIPS-2022-Paper zu Verkapselung (S). Das ist Forschung/Prototypen, keine Serienfertigung: Fertigung Niedrig (S), Verguss Mittel (S), kein Serienbeleg.
- Wettbewerbereinsatz (F6), von mir bestätigt: Nordson ASYMTEK Axiom X-1020 (Underfill/Glob-Top, DispenseJet DJ-9000) und Century C-341 im Berliner Applied Research Center laut Pressemeldung (Stufe S; Snippets evertiq / siliconsemiconductor / circuitsassembly, undatiert); 2019 ASYMTEK in der IZM Future Packaging Line (SMTconnect), 2025 Vantage-System im IZM Hybrid Live Lab (productronica-Ankündigung, S). Kein Ampeleinfluss.
- Korrekturen: Feld 16 ergänzt um die Termine 2019/2025 (S). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 3): Siehe Nr. 4. Zusatz: Ist IZM als Technologie-/Testpartner (Potting Lab) separat zu führen und nicht als Neukunde? Entscheidung Jey. Aktion: nicht neu aufnehmen.
- Nicht verwendbare Aussagen: Verguss Mittel (S, Forschungsprozess); Patente DE102008027558, DE19542883 (Rechtsstand ungeprüft, Verguss-Bezug schwach); DE102020204941A1 (Anmelder unbekannt). Stichprobe für Jey: ja (Forschungsthema Verguss, Partnerfrage).

## 10. FrelTec GmbH | A6.100
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).**
- Begründung: Fertigung in Starnberg ist nur Stufe S: Branchenverzeichnis (Implisense, WZ C27.90 "Manufacture of other electrical equipment") nennt "Entwicklung, Herstellung, Import/Export und Vertrieb"; Sortiment umfasst Passivbauteile (Widerstände, Kondensatoren, Dioden) und Steckverbinder, also Händlerprofil möglich. Sitzregel greift nicht sicher (Eigenprodukte nicht belegt). E2 nicht V-belegt, daher nicht Rot. Verguss Mittel (A, nur falls Steckverbinder/Kabelkonfektion selbst gefertigt).
- Identität (Prüfung): Name, Mathildenstraße 10a, 82319 Starnberg, HRB 169250 München, GF Michael Frömsdorf, Telefon 08151 3684898, Domain freltec.com stimmen in zwei Quellen überein (Implisense, Branchenbuch muenchen.de; beide Aggregatoren, S); Impressum der Firma nicht gelesen. Zeile 2 daher nicht ausgelöst. Website freltec.com damit als Angabe der Aggregatoren (S) verwendbar, nicht Toms "Vermutung". Eigene Suche nach Messeprofil/Produktseite erfolglos.
- Korrekturen an Toms Feldern: Feld 5 und 17 ergänzt (siehe oben). Einstufung "unwahrscheinlich" bleibt vorläufig. CRM: crm_abgleich.py "FrelTec GmbH": kein Treffer, neu. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Stellt FrelTec in Starnberg Steckverbinder/Kabel/Baugruppen selbst her (oder lässt sie fertigen) oder handelt sie nur (E2)? Wo nachsehen: freltec.com (Impressum, Produktseiten, "Über uns", Fertigung/Qualität), electronica-Ausstellerprofil Halle A6 Stand 100, Stellenanzeigen (Montage, Konfektion). Bei belegter reiner Handelstätigkeit Rot nach E2 mit Quelle. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Starnberg (S); "Herstellung" (Aggregator-Text, S); Verguss Steckverbinder (A); Größe "mittelgroß" (S). Stichprobe für Jey: ja (Fertiger oder Händler).

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind korrekt niedrig (keine V-Aussage vorgetäuscht). Er überließ die Entscheidung über Forschungseinrichtungen mit "E2, Tina entscheidet". Mein Ergebnis: E2 nennt Hochschulen, nicht Forschungsinstitute/Verbände; daher nur Fraunhofer-Gesellschaft Rot (E5 über CRM, harter Beleg), Institute Gelb nach Regel M, Verband Gelb. Jey sollte die Regelfrage "Forschungsinstitute/Verbände = E2?" einmal entscheiden; damit erledigen sich Nr. 2 bis 9 gemeinsam.
- Prüfpunkt 4 (Grün-Kandidaten/"interessant"): Tom führt keine Firma als "interessant" und ich keine als Grün; daher kein Browser-Gegenlesen verpflichtend, bleibt für Flextem (Identität) trotzdem nötig.
- Vorschlag Fehlerlog (Jey gibt frei, nicht eingetragen): (1) Messelisten mit Forschungsinstituten: Regel klären, ob Fraunhofer-Institute wie die Gesellschaft (E5) oder einzeln zu behandeln sind. (2) Namens-Screening-Hinweise der Eingabe ("Sensorik") nicht als Einstufungsgrundlage verwenden (Flextem).

## Einschränkungen
- Browser und WebFetch nicht verfügbar: kein Gegenlesen nach Abschnitt H, keine Impressen/Datenblätter/Register gelesen; alle Web-Aussagen Stufe S oder A. Keine "Zitat im Browser bestätigt: ja".
- WebSearch: 12 Abfragen verbraucht (Flextem 3, FrelTec 3, 3-D MID 1, Fraunhofer-Gesellschaft 1, IZM Verguss/Patent/Nordson 3, IKTS 1). Für ENAS, IIS, IMS, IPM keine eigene Websuche, nur Toms Quellen und CRM-Abgleich (Ampel hängt hier nicht an Websuche, sondern an Zeile 3).
- Patente: Pflichtsuche F5 (Google Patents, Espacenet, DEPATISnet) nicht erfüllt, alle 10 Firmen. Rechtsstand aller Patente ungeprüft. Anmelder-Zuordnung einzelner Fraunhofer-Institute ungeprüft.
- Wettbewerbereinsatz (F6): Abgleich mit wettbewerber_referenzen.md nur in den gelesenen Teilen (Zeilen 1 bis 378 von 631); Treffer für die zehn Firmen dort nicht gesehen, Rest nicht geprüft. Einzige Hinweis: Nordson am IZM (S).
- Handelsregister/Unternehmensregister nicht abgerufen. kundendatenbank_export.txt: kein Treffer zu Fraunhofer/Flextem/FrelTec, daher keine "Verifiziert am"-Prüfung nötig.
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
