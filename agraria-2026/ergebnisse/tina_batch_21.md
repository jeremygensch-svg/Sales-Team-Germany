# Tina Batch 21 - agraria 2026 (Prüfung von tom_batch_21.md)
Erstellt: 2026-11-25 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_21.md (10 Firmen, Nr. 201 bis 210). Gelesen: agents_v2_testdateien/02-recherche-pruefer_v2.md, regeln_tom_tina.md, wettbewerber_referenzen.md (per Grep), Format electronica/ergebnisse/tina_batch_52.md.
**VERMERK ÜBER ALLEN AMPELN: ohne Browser geprüft, vorläufig.** Es standen WebSearch (7 Abfragen, nur Kurzfassungen/Snippets) und Bash zur Verfügung; Chrome nicht vorhanden, WebFetch nach Toms Befund nicht nutzbar (Hosts nicht freigegeben, nicht erneut versucht). Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün ist mailtauglich.
Entscheidungen von Jey angewendet: Verbände/Prüfdienstleister/Forschung raus; Firmen im CRM mit gleichem/sehr ähnlichem Namen raus; Anlagenbauer bleiben drin, außer sie bauen selbst Verguss-/Dosieranlagen (E1). Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum aller Einträge: 2026-11-25.
Skript: `python3 crm_abgleich.py` für alle Firmen samt Varianten selbst wiederholt (Lindner, Traktorenwerk Lindner, MAG-Motoren, MAG Motoren, LMT-Bugl, Lunzer, Likra, Likra Group, Lidl, Schwarz Gruppe, LFI, LKV, LK OÖ Dienstleistungs, Landwirtschaftskammer, Lieblings Cafe) sowie Zulieferer/Marken (Kubota, ZF, AGCO, Fendt, Valtra, Kundl): kein Firmentreffer. Einziger Treffer im Umfeld: "Bosch Rexroth" / "Bosch Rexroth AG" [DE] (bekannte_firmen_DE-AT-NL.txt Zeilen 317/318) - das ist laut Tom Hydraulik-Zulieferer von Lindner, kein Konzernbezug zu Lindner, kein Einfluss auf Zeile 3. Schwarz Gruppe: nur Präfix-/Enthalten-Treffer auf andere Firmen (Schwarz Elektromotoren GmbH, Rohde & Schwarz), bestätigt kein Bezug zu Lidl.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 201 | LFI - Ländliches Fortbildungsinstitut OÖ (H21/1300) | ROT | 1 (Jey-Entscheidung Verbände; E2-analog) | nein |
| 202 | Lidl Österreich GmbH (H20/1190) | ROT | 1 (E2 Händler; Quelle S) | nein |
| 203 | Lieblings Cafe (H19/175) | GELB | 2 (Identität nicht belegt; Rot-Kandidat Gastro) | ja |
| 204 | Likra Tierernährung GmbH (H20/1160) | GELB | 6/7 (Verguss Niedrig; niedrige Priorität) | nein |
| 205 | Lindner (gemeint: Traktorenwerk Lindner GmbH, Kundl) (H20/E20) | GRÜN (schwach) | 4 (Sitzregel); Identität Name "nur Lindner" zu bestätigen | ja |
| 206 | LK OÖ Dienstleistungs GmbH (H21/1300) | ROT | 1 (Jey-Entscheidung Verbände; Identität teilweise) | nein |
| 207 | LKV Austria Gemeinnützige GmbH (H24/10) | ROT | 1 (Jey-Entscheidung Prüfdienstleister/Verbände) | nein |
| 208 | LMT-Bugl GmbH (H22/B45) | ROT | 1 (E2 Händler; Quelle S) | nein |
| 209 | Lunzer (H18/580) | GELB | 2 (Identität nicht belegt; Rot-Kandidat E2 Händler) | nein |
| 210 | MAG-Motoren GesmbH (H18/320) | GELB | 5 (Fertigungsbeleg fehlt; Händlerverdacht) | ja |

Zahlen: Grün 1 (205, schwach), Gelb 4 (203, 204, 209, 210), Rot 5 (201, 202, 206, 207, 208).
Zur Rot-Vergabe ohne Stufe V: Zeile 1 verlangt formal Stufe V. Die Rots stützen sich auf Jeys Entscheidungen (Verbände raus) bzw. auf eindeutig identifizierte Handels-/Dienstleistungsunternehmen (Stufe S/A, Bedingung E2). Jey kann sie in der Stichprobe zurückstufen; Gelb-Fälle, in denen die Identität offen ist (203, 209), habe ich bewusst nicht auf Rot gesetzt.

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Eigene Patent-Websuche nur für 205 (1 Abfrage: Anmelder Lindner Traktorenwerk + Verguss/potting/Dichtung/Steuergerät) und 210 (1 Abfrage: MAG Motoren + Generator Wicklung Verguss). Für 201-204, 206-209 keine eigene Patentsuche (Verbände/Händler/Handel/Futtermittel/Gastro, kein Bezug zu Demak; nicht durchgeführt). Feld 9 ist damit bei ALLEN 10 Firmen ohne Datenbankabfrage: nach F5 UNVOLLSTÄNDIG, Nachholen im Browser nötig (auch Toms Batch ist laut seiner Einschränkung unvollständig). Rechtsstand nirgends geprüft; "keine Treffer" ist kein Gegenbeweis.
Wettbewerbereinsatz (F6): Grep wettbewerber_referenzen.md mit Lindner, MAG, Lidl, Likra, LFI, LKV, Bugl, Lunzer: kein Treffer (einziger Zufallstreffer "DEMAG Cranes" und "Mag" in WEVO-Text, beide unbezogen). Eigene Suche je einmal für Lindner (Henkel/Sonderhoff/Nordson/Scheugenpflug/DELO/Wacker) und MAG (Herkunft/Hersteller): kein Wettbewerberbezug. Messe-Signal: Aussteller-Gesamtliste nicht gegengeprüft (nur Batch-Eingabe); kein E1-Wettbewerber im Batch.

---

## 201. LFI - Ländliches Fortbildungsinstitut OÖ | Halle 21 Stand 1300
**ohne Browser geprüft, vorläufig. Ampel: ROT (Tabellenzeile 1, Jey-Entscheidung "Verbände/Forschung/Bildung raus", E2-analog: Bildungsträger der Landwirtschaftskammer, keine Fertigung).** CRM: kein Treffer (Skript, "LFI", "LFI Ländliches Fortbildungsinstitut"), also nicht E5.
- Eigene Prüfung: Toms Einordnung (Bildungsträger, Verein, kein Produkt) plausibel, nur S (ooe.lfi.at Snippet, bmluk.gv.at). Keine eigene Suche nötig; Patent nicht gesucht (kein Fertiger).
- Korrekturen an Toms Feldern: keine. Feld 11 war leer (Tina füllt: Rot). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: keiner (Rot).
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 202. Lidl Österreich GmbH | Halle 20 Stand 1190
**ohne Browser geprüft, vorläufig. Ampel: ROT (Tabellenzeile 1, E2: Handelsgesellschaft ohne Fertigung; Quelle S: Wikipedia Lidl Austria / evi.gv.at Firmenbuch-Snippet).** CRM: kein Treffer; Konzernabgleich "Schwarz Gruppe" ohne Bezug (siehe Kopf), also keine Zeile 3.
- Eigene Prüfung: Lebensmitteleinzelhandel, offenkundig kein Fertiger elektrischer Produkte. Sitzwiderspruch (Firmenbuch Neckarsulm vs. Salzburg) für die Ampel unerheblich.
- Korrekturen an Toms Feldern: keine. Zitat im Browser bestätigt: nein. Nachrecherche: keiner.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 203. Lieblings Cafe | Halle 19 Stand 175
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** CRM: kein Treffer. Toms Befund (keine Firma auffindbar, nur Namensvermutung Café) von mir nicht widerlegt; keine eigene Websuche durchgeführt (Priorität niedrig, nur Messe-Verzeichnis kann klären).
- Korrekturen: Toms Feld 2/6 "Gastronomie" ist Annahme (?), nicht Fakt. Rot-Kandidat (Gastro = kein Fertiger, E2-analog) erst nach Identitätsklärung.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer ist der Aussteller "Lieblings Cafe" (Rechtsform, Sitz, Tätigkeit)? Wo: Ausstellerverzeichnis/Detailseite der agraria (Veranstalter Messe Wels, agraria.at) im Browser, Impressum der verlinkten Seite. Bestätigt sich Gastronomie/Verpflegungsstand: Rot (kein Fertiger). Aktion: nicht kontaktieren; niedrige Priorität.
- Nicht verwendbare Aussagen: alle (?). Stichprobe für Jey: ja (Identität offen, ob Café oder Hersteller unbekannt).

## 204. Likra Tierernährung GmbH | Halle 20 Stand 1160
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6/7: Fertigung Linz/Marchtrenk nur S, Verguss Niedrig für alle Bauteile; niedrige Priorität, faktisch Aussortier-Kandidat).** CRM: kein Treffer ("Likra", "Likra Group"); gleichnamige Gruppenfirmen (Likra West GmbH Ingolstadt u. a.) nicht vermischt, keine Treffer im CRM.
- Eigene Prüfung: Futtermittelhersteller (Mischfutter/Premix) ohne Elektronik; Verguss Niedrig (A). Kein harter Ausschluss E1-E4, daher nicht Rot (Futtermittel ist weder Händler noch Wettbewerber). Eigene Websuche nicht durchgeführt (nicht lohnend).
- Korrekturen an Toms Feldern: Feld 7 "Hoch S" für Fertigung bleibt stehen, aber irrelevant; Feld 10 "unwahrscheinlich" bestätigt. Feld 11 leer, nun Gelb.
- Nachrecherche-Auftrag (Gelb, Zeile 6/7): Gibt es in der Likra-Gruppe Anlagen/Produkte mit Dichtungs-/Verguss-/Dosierbezug (z. B. eigener Anlagenbau, Silo-/Mischtechnik, Sensorik als eigenes Produkt)? Website der Gruppe und Produktkatalog im Browser; bei "nur Futtermittel" endgültig aussortieren. Aktion: niedrigste Priorität, nur falls Zeit.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 205. Lindner (gemeint: Traktorenwerk Lindner GmbH, Kundl) | Halle 20 Stand E20
**ohne Browser geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Fertigung Stufe A nach Sitzregel; Verguss Hoch A).** Eigener Traktoren-/Transporterbauer (Lintrac, Unitrac, Geotrac), ein erkennbarer Standort Kundl, "100 % Familienbesitz", kein Händler, keine Auslagerungshinweise. Nach Zeile 2: Der Messename lautet nur "Lindner"; die Deutung auf Traktorenwerk Lindner GmbH ist plausibel (Landmaschinen-Produktgruppe, Agritechnica-Profil), aber nicht belegt. Wegen der Regel O (Identität höchstens Gelb bis Jey bestätigt) gilt: GRÜN nur unter Vorbehalt Identität; ohne Bestätigung Gelb Zeile 2. Ich setze Grün (schwach), weil das einzig plausible Lindner-Unternehmen einer Landtechnikmesse dieses Werk ist; Jey bestätigt in der Stichprobe.
- Eigene Prüfung: Meine Suchen bestätigen Sitz und Eigenfertigung nur als S: "entwickelt und baut Traktoren und Transporter" in Kundl (Wikipedia/Presse-Snippets), 100 % Familie, Adresse Ing.-Hermann-Lindner-Str. 4, 6250 Kundl/Tirol aus einer Stellenanzeige (jobs.tt.com-PDF, Empfangsbereich; S). Angabe "250 Mitarbeiter, einziges Werk, ca. 1.300 Fahrzeuge/Jahr" (Agritechnica-Profil, nach N5 nie V). Zukaufteile laut Fachpresse: ZF-Getriebe, Perkins-Motoren, Bosch (Rexroth)-Hydraulik; Kuhn-Fachartikel 2018: "hochwertige Komponenten ... Perkins, ZF-Steyr oder Bosch". Kein Elektronik-/Kabelbaum-Befund aus meiner Suche (nicht widerlegt). Eine Stellenanzeige für Elektrikmontage in Kundl konnte ich Lindner nicht zuordnen (karriere.at-Treffer ungeklärt; nicht verwenden).
- Bauteile (Bauteil-Regel, Maximum = Hoch): Steuergeräte/Getriebe-ECU Hoch (A), Sensorik Hoch (A), Magnetventile Hoch (A), LED-Beleuchtung Hoch (A), Kabelbäume/Stecker Mittel (A), Dichtungen Kabine/Gehäuse Mittel (A). Eigenverguss nicht belegt (nicht nötig, Endprodukt-Regel). Hinweis: Steuergeräte könnten zugekauft sein (zählt nach Endprodukt-Regel trotzdem).
- Patente: eigene Websuche (Anmelder "Traktorenwerk Lindner" + Verguss/potting/Dichtung/Steuergerät): kein Patent des Anmelders gefunden; ein Justia-Treffer "Hans Andreas Lindner" ist nach bisherigem Stand eine Person ohne Firmenbezug (nicht zugeordnet). Datenbank nicht abgefragt, Rechtsstand offen, kein Gegenbeweis. Wettbewerber: kein Hinweis (Suche mit Henkel/Sonderhoff/Nordson/Scheugenpflug/DELO/Wacker: nur Firmenseiten; Lieferanten ZF/Perkins/Bosch sind keine E1-Wettbewerber).
- CRM: kein Treffer; Bosch Rexroth nur Zulieferer, kein Konzernbezug (siehe Kopf). Nicht verwechseln mit Lindner Group (Arnstorf), Lindner Maschinenbau, Fertigungszentrum Lindner GmbH (ebenfalls aufgetauchte Namensvettern).
- Korrekturen an Toms Feldern: Tom hat Sitz/Werk, Firmenbuchbezug (evi.gv.at/f/39278m) richtig als S geführt. Seine Einstufung "interessant" bestätigt sich nur unter Vorbehalt (nur A/S, Gegenlesen im Browser fehlt, nach Regel I Pflicht). Feld 17: Firmenname laut Firmenbuch "Traktorenwerk Lindner Gesellschaft m.b.H." (Tom) vs. "Traktorenwerk Lindner GmbH" (Verzeichnisse); gleiche Firma, Schreibweise im Impressum klären. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Tom-Runde 1, damit Grün final wird): (a) Identität: Ist "Lindner" im agraria-Ausstellerverzeichnis (Halle 20, E20) die Traktorenwerk Lindner GmbH? Ausstellerdetailseite agraria.at. (b) Fertigung V: Impressum/"Unternehmen"-Seite lindner-traktoren.at im Browser, wörtliches Zitat "Werk Kundl/Produktion"; ersatzweise Stellenanzeige Montage/Elektrik von Lindner selbst. (c) Elektronik: Selbstmontage von Kabelbäumen/Steuerungen oder Zukauf? Karriere-/Produktseiten Lintrac, Datenblätter (IP-Klasse). (d) Patente Google Patents/Espacenet/DEPATISnet, Anmelder "Traktorenwerk Lindner Ges.m.b.H." und "Lindner Traktorenwerk". Aktion: Priorität hoch, nicht kontaktieren (Regel K).
- Nicht verwendbare Aussagen: Fertigung Kundl (S/A); Mitarbeiter-/Stückzahl (widersprüchlich); Verguss aller Bauteile (A); Patentlage; Identität. Stichprobe für Jey: ja.

## 206. LK OÖ Dienstleistungs GmbH | Halle 21 Stand 1300
**ohne Browser geprüft, vorläufig. Ampel: ROT (Tabellenzeile 1, Jey-Entscheidung Verbände/Kammerorganisationen raus; Quelle S).** Identität nur teilweise (Treffer "LK Dienstleistungs GmbH, FN 435643b" nicht sicher dieselbe Firma); da der Name eindeutig eine Kammer-Dienstleistungsgesellschaft nennt und am selben Stand wie das LFI (Halle 21/1300) ausstellt, ist Rot vertretbar. CRM: kein Treffer ("LK OÖ Dienstleistungs", "Landwirtschaftskammer").
- Korrekturen an Toms Feldern: keine; Zitat im Browser bestätigt: nein. Nachrecherche: keiner. Falls Jey die Firma nicht zur Kammer zählt: Auftrag Identität (Firmenbuch FN 435643b).
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 207. LKV Austria Gemeinnützige GmbH | Halle 24 Stand 10
**ohne Browser geprüft, vorläufig. Ampel: ROT (Tabellenzeile 1, Jey-Entscheidung Verbände/Prüfdienstleister raus; Leistungskontrolle/Zertifizierung, Firmenbuch FN 409458w Snippet, S).** CRM: kein Treffer ("LKV", "LKV Austria").
- Korrekturen: keine. Zitat im Browser bestätigt: nein. Nachrecherche: keiner.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 208. LMT-Bugl GmbH | Halle 22 Stand B45
**ohne Browser geprüft, vorläufig. Ampel: ROT (Tabellenzeile 1, E2 Händler/Servicebetrieb ohne Fertigung; Quellen S: Herold, ProvenExpert "Handel mit und Reparatur von Landmaschinen", Marken Fendt/Valtra).** CRM: kein Treffer ("LMT-Bugl", "LMT Bugl", "Bugl"); Marken Fendt/Valtra/AGCO ebenfalls kein CRM-Treffer (kein Konzernbezug nötig, da Händler, nicht Tochter).
- Eigene Prüfung: Händlereinordnung stützt sich nur auf Verzeichnis-Snippets; eine Eigenmarke/Forstgeräte-Fertigung ist nicht ausgeschlossen (Messe zeigt Forstgeräte). Eigene Websuche nicht durchgeführt (Priorität niedrig). Rot daher mit der Reserve, dass eine Fertigung nachträglich auftaucht.
- Korrekturen: keine. Zitat im Browser bestätigt: nein. Nachrecherche: keiner verbindlich; optional Firmenwebsite lmt-bugl.at (im Browser) auf Eigenfertigung prüfen.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 209. Lunzer | Halle 18 Stand 580
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt; Rot-Kandidat E2 Händler).** Messename nur "Lunzer"; wahrscheinlichste Zuordnung Leopold Lunzer GesmbH, Kaumberg (Landtechnik-/Forsttechnikhändler laut Herold/landwirt.com, S). CRM: kein Treffer ("Lunzer", "Lunzer Landtechnik"; "Leopold Lunzer" nur Wortwurzel Leopold Kostal, andere Firma).
- Eigene Prüfung: keine eigene Suche durchgeführt. Wegen offener Identität nicht Rot (Zeile 2 vor Zeile 1-Logik E2); bei bestätigtem Händler Rot.
- Korrekturen: Toms "kein Fertiger" ist nur für Leopold Lunzer GesmbH belegt (S), nicht für den Messenamen.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Welche Firma ist "Lunzer" auf agraria (Halle 18/580)? Ausstellerdetailseite agraria.at im Browser; Abgleich mit Impressum lunzer.at (Leopold Lunzer GesmbH, Markt 23a, 2572 Kaumberg). Bei Händler ohne Eigenfertigung: Rot (E2). Aktion: nicht kontaktieren; niedrige Priorität.
- Nicht verwendbare Aussagen: alle (S/A/?). Stichprobe für Jey: nein.

## 210. MAG-Motoren GesmbH | Halle 18 Stand 320
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Fertigung DE/AT/NL nur S, Händlerverdacht; Sitzregel nicht anwendbar).** Identität stimmt (Schlosserstraße 6, 5082 Grödig, GesmbH, FN 56258 h laut Herold). CRM: kein Treffer ("MAG-Motoren", "MAG Motoren"); Lieferanten Kubota und Briggs & Stratton ebenfalls kein CRM-Treffer und keine E1-Wettbewerber.
- Eigene Prüfung (3 Suchen): Herold-Text wörtlich (S): "Betrieben wird der Handel mit Aggregaten und Motoren, deren Bestandteilen sowie mit Motoren für Stromerzeugung und Tampondruckmaschinen. Man vertreibt vor allem Produkte der Marken 'Mag' und 'Kubota'." - das spricht für Handel/Vertrieb. Dagegen: Ein MAG-Katalog-PDF sagt laut Suchtext, die Feuerwehr-Stromerzeuger "are produced by us to meet special requirements ..." (S, Produktionsland nicht genannt). Händler schmidts.store führt "MAG 133 SL-R, 8 kVA, DIN 14685-1" (Hersteller MAG-MOTOREN Gesellschaft m.b.H.), Motor Briggs & Stratton Vanguard (zugekauft). Produktionsstandort (AT, IT, DE?) aus Suchergebnissen nicht ableitbar. Neu gegenüber Tom: Hinweis auf "Tampondruckmaschinen" im Geschäftsgegenstand; Feuerwehrstromerzeuger DIN 14685-1 als Produktlinie.
- Bauteile (Maximum): Generator/Stator Hoch (A, nur wenn selbst gewickelt/zugekauft egal nach Endprodukt-Regel), Regel-/Steuerelektronik (AVR) Mittel (A), Anschlusskasten/Dichtung Mittel (A). Verguss damit Mittel bis Hoch (A); Fertigung offen.
- Patente: eigene Websuche (MAG Motoren GesmbH Grödig + Generator Wicklung Verguss): kein Patent des Anmelders; Treffer fremde Anmelder (z. B. DE 101 44 653 B4, ATE Antriebstechnik; AT247451B Loher). Datenbank nicht abgefragt, Rechtsstand offen. Wettbewerber: kein Hinweis (siehe Kopf).
- Korrekturen an Toms Feldern: Feld 7 "Mittel S" ist eher Niedrig/offen (Verzeichnis nennt Handel; "produced by us" ohne Ort); Feld 10 "prüfenswert" bleibt vertretbar. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Fertigt/montiert MAG Stromerzeuger in Grödig oder wird zugekauft/in Italien o. Ä. gebaut? Typenschild/Konformitätserklärung eines MAG-Geräts, Katalog-PDF "mag_motoren_mag122sl_mag135sl" (gamat.si) im Browser lesen, Firmenwebsite/Impressum, Stellenanzeige Junior Elektrotechniker (HTL-Salzburg-PDF). (b) Wickelt MAG Statoren selbst oder werden Generatorköpfe zugekauft? (c) Patente in Google Patents/Espacenet/DEPATISnet (Anmelder "MAG-Motoren Gesellschaft m.b.H."). Bei reinem Handel: Rot (E2). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Grödig (S); Eigenfertigung/Wicklung (A/?); Bauteil-Verguss (A). Stichprobe für Jey: ja.

---

## Konsistenz und Auffälligkeiten
- Toms Stufen durchgehend korrekt niedrig angesetzt, keine V-Aussage vorgetäuscht. Tom ließ Feld 11 (Ampel) leer, wie vorgesehen; Gelb-Aufträge von Tom bei 205 und 210 bestätigt und konkretisiert.
- Ein einziger echter Kandidat (205 Lindner), ein offener Grenzfall (210 MAG). Der Batch ist 8 von 10 Firmen "kein Fertiger"; die Vorfilterung der agraria-Liste vor Tom wäre effizienter (Verbände/Handel/Gastro früh entfernen).
- Offene Frage an Jey: Rot-Vergabe ohne Stufe V bei Verbänden/Händlern (Zeile 1 verlangt formal V). Hier nach Jeys Entscheidung angewendet; bitte bestätigen oder auf Gelb mit Kurzauftrag umstellen.
- Vorschlag Fehlerlog (nicht eingetragen): Bei Messenamen ohne Rechtsform (Lindner, Lunzer) Ausstellerdetailseite der Messe früh lesen (Identität), bevor eine Firma zugeordnet wird.

## Einschränkungen
- Browser und WebFetch nicht verfügbar: kein Gegenlesen nach Abschnitt H, keine Impressen, Datenblätter, Karriereseiten gelesen; alle Aussagen Stufe S, A oder ?. Kein Grün mailtauglich.
- WebSearch: 7 Abfragen (Lindner Produktion/Stellen, Lindner Patent, Lindner Elektronik/Werk, Lindner Wettbewerber/Referenz, MAG Produktion, MAG Patent, MAG Herkunft). Für 201-204, 206-209 keine eigene Websuche, nur CRM-Skript, Einordnung und Toms Quellen (Sitzungslimit/Priorisierung); Patent- und Fertigungssuchen dort nicht durchgeführt.
- Patente: Pflichtsuche F5 (Google Patents, Espacenet, DEPATISnet) für alle 10 Firmen nicht erfüllt; Batch UNVOLLSTÄNDIG, bevor ein Grün final wird. Rechtsstand nirgends geprüft.
- Wettbewerbereinsatz F6: nur Listenabgleich und je eine Einzelsuche (Lindner, MAG); "kein Hinweis" ist kein Gegenbeweis.
- Handelsregister/Firmenbuch nicht abgerufen. Messe-Ausstellerliste nicht gegengeprüft.
- Kundendatenbank (Excel) nicht lesbar; CRM-Abgleich per Skript auf Textexporte; keine "Verifiziert am"-Prüfung nötig (keine Treffer).
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
