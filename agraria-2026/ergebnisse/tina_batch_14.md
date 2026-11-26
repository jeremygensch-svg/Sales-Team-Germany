# Tina Batch 14 - agraria 2026 (Prüfung von tom_batch_14.md)
Erstellt: 2026-11-25 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_14.md (10 Firmen, Nr. 131 bis 140, Messe agraria Wels 2026, Länder DE/AT/NL; laut Messeliste alle AT). Halle/Stand stehen unverändert aus Toms Datei. Toms Blöcke 1 bis 10 entsprechen den Nr. 131 bis 140.
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (6 Abfragen, Kurzfassungen/Snippets) und Bash zur Verfügung; Chrome nicht verfügbar, WebFetch nicht genutzt. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün vergeben, nichts mailtauglich.
Vollständigkeit von Toms Batch: batch_check.py meldet VOLLSTÄNDIG (10 Blöcke, alle Felder, Feld 11 absichtlich leer). Abbruch-Vermerk: Toms Datei endet mit vollständigem Abschnitt "Einschränkungen"; es fehlt kein Block. Inhaltlich unvollständig bleiben: Feld 9 (keine direkte Datenbankabfrage, nur WebSearch), Feld 16 (keine Wettbewerber-Referenzseiten), Feld 17 (Impressum/Firmenbuch bei keiner Firma gelesen).
Skripte: `python3 crm_abgleich.py` für alle zehn Firmen samt Konzern-/Alt-/Schwester-/Schreibvarianten selbst wiederholt (Fröling/Froeling, Fuhrmann, Fallmann, Garant, Raiffeisen Ware Austria, RWA, GEA, GEA Group, GEA Farm Technologies, Westfalia, Genetic, Genezis, Genol, OMV, Gesing): überall "kein Treffer -> neu". Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum aller Einträge: 2026-11-25.
Entscheidungen von Jey, angewandt: Verbände/Prüfdienstleister/Forschung raus; Firmen im CRM mit gleichem/sehr ähnlichem Namen raus (im Batch keiner, alle kein Treffer); Anlagenbauer bleiben drin, außer sie bauen selbst Verguss-/Dosieranlagen (E1; im Batch kein E1-Fall erkennbar). Ein harter Ausschluss ergibt nur mit Stufe V Rot (Zeile 1); da keine V-Quelle vorliegt, steht bei offensichtlichen Ausschlüssen GELB mit Zusatz "Rot-Kandidat E2/E3" (wie in tina_batch_12) und der Empfehlung, nach Jeys Entscheidung auszusortieren.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 131 | Freie Bauern OÖ (Halle 20, Stand 1240) | GELB (Rot-Kandidat E2, Verband) | 2 | nein |
| 132 | Fröling Heizkessel- und Behälterbau GmbH (Halle 17, Stand 250) | GELB | 5 | ja |
| 133 | Fuhrmann Fahrzeuge GmbH (Halle 21, Stand C40) | GELB | 5 | ja |
| 134 | Futtermittel Fallmann GmbH (Halle 24, Stand 50) | GELB | 2 | nein |
| 135 | Garant Tiernahrung (Halle 23, Stand 100) | GELB | 6 | nein |
| 136 | GEA Austria GmbH (Halle 23, Stand 150) | GELB (Rot-Kandidat E2) | 5 | ja |
| 137 | Genetic Austria GmbH (Halle 24, Stand 10) | GELB (Rot-Kandidat E2) | 7 | nein |
| 138 | Genezis Trade Austria (Halle 17, Stand 100) | GELB (Rot-Kandidat E2/E3) | 7 | nein |
| 139 | Genol GesmbH (Halle 20, Stand F30) | GELB (Rot-Kandidat E2) | 7 | nein |
| 140 | Gesing Tierzucht Österreich GmbH (Halle 23, Stand 60) | GELB | 2 | nein |

Zahlen: Grün 0, Gelb 10 (davon 6 Rot-Kandidaten bzw. Aussortier-Empfehlung, 2 echte Prüffälle Fröling und Fuhrmann, 1 Konzern-Landesgesellschaft GEA), Rot 0.

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Eigene Patent-Suche nur für Fröling (1 WebSearch, Treffer siehe Block 132); für die übrigen neun Firmen keine eigene Wiederholung, Toms Suchen werden weder übernommen noch widerlegt. Feld 9 ist damit nach F5 UNVOLLSTÄNDIG, Nachholen im Browser nötig; das gilt vorrangig für Fröling und Fuhrmann. "Keine Treffer" ist kein Gegenbeweis. Wettbewerbereinsatz (F6): Grep auf wettbewerber_referenzen.md mit Fröling, Fuhrmann, Fallmann, Garant, GEA, Genezis, Genol, Gesing, Genetic, Freie Bauern: kein Treffer; keine Einzelsuchen mit Wettbewerbernamen von mir. Messe-Signal: laut Tom kein E1-Wettbewerber unter den zehn Firmen; für die gesamte Messeliste nicht geprüft.
Nicht durchgeführt (offen benannt): Browser-Gegenlesen aller Quellen (Regel H/I/O), Impressum-/Firmenbuchlesen, Patentdatenbanken, Wettbewerber-Referenzseiten, eigene Standort-/Produktseiten von Fröling und Fuhrmann.

---

## 131. Freie Bauern OÖ | Halle 20, Stand 1240
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2; Rot-Kandidat E2).** Politische Bauernvertretung/Wahlgruppe (Tom, S; Messelisten-Kategorie "Vereine, Verbände, ARGE, Organisationen"). Jeys Entscheidung "Verbände raus" greift inhaltlich, die Quelle ist aber nur ein Zeitungssnippet (S), Identität (Rechtsform, Sitz, Register) nicht belegt. CRM: kein Treffer, neu. Tabellenzeile 1 verlangt Stufe V, daher Gelb; Empfehlung: aussortieren.
- Korrekturen an Toms Feldern: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Vereinsregister/ZVR-Abfrage und Website der Gruppe: Ist es ein Verein/Verband ohne Fertigung? Nur nötig, falls Jey nicht allein nach Messelisten-Kategorie aussortieren will. Aktion: aussortieren (Verband), nicht kontaktieren.
- Nicht verwendbare Aussagen: Sitz, Rechtsform, Gleichsetzung mit Freiheitlicher Bauernschaft (S/?). Stichprobe für Jey: nein.

## 132. Fröling Heizkessel- und Behälterbau GmbH | Halle 17, Stand 250
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Fertigungsbeleg V fehlt).** Zeile 1 greift nicht (kein E belegt, kein CRM-Treffer, auch nicht auf "Fröling"/"Froeling"), Zeile 2/3 nicht, Zeile 4 nicht erfüllt: Fröling hat laut Tom mehrere Werke (Grieskirchen, Stritzing, Marzahna/DE), die Sitzregel gilt dann nicht, Stufe V für die Fertigung ist nötig und fehlt (nur S). Verguss Hoch (A) nach Bauteil-Regel (Sensoren, zugekaufte EC-Gebläsemotoren mit Elektronik, Steuerplatinen, Zündelemente); das ist nur abgeleitet. Toms "interessant" ist daher nicht bestätigt (nach Regel I nur mit Browser-Gegenlesen).
- Eigene Prüfung: WebSearch bestätigt über Jobportale (jobs.at/karriere.at, S), dass Fröling in Grieskirchen eine Entwicklungsabteilung hat (Stellen "Konstrukteur Entwicklungsabteilung", "Embedded Software Entwickler C/C++ Schwerpunkt UI" in Grieskirchen) und dass das Unternehmen laut Suchzusammenfassung "in eigenen Werken in Österreich und Deutschland" fertigt (S). Eine Stelle zu Elektromontage/Steuerungsbau wurde nicht gefunden (kein Gegenbeleg). Patent (1 WebSearch, Espacenet-Publikationsserver): nur EP 0 060 338 "Brennstoffbefeuerter Heizkessel", Anmeldung 30.10.1981, Anmelder "Froling GmbH & Co. Kessel-Apparatebau" (Zuordnung zur heutigen GmbH ungeklärt, Rechtsstand vermutlich erloschen, nicht geprüft); kein Treffer zu Verguss/Dichtung/Sensor in dieser Abfrage. Toms Patent EP3495045B1 (Brennwertkessel, Rechtsstand "Granted And Under Opposition") nicht nachgeprüft (S aus Aggregator).
- Korrekturen an Toms Feldern: Feld 4: Welches Werk Regelungen/Kessel fertigt, bleibt offen; "Fertigung Hoch, S" nur als "Hoch (S), V fehlt" führen. Feld 9: Patente nur Kesseltechnik, kein Verguss-Bezug; Zuordnung Altpatent zur heutigen Firma ungeklärt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Fertigungsbeleg V: froeling.com Standortseiten/Impressum und Stellenanzeigen (Elektromontage, Steuerungsbau, Vergießen/Kleben) im Browser lesen; welches Werk fertigt Regelungen und Kessel in AT? (b) Verguss konkret: Datenblatt/Produktseite Regelung (Touch-Display), Saugzug-/Gebläsemotor, Lambdasonde, Temperaturfühler, IP-Klassen. (c) Patentsuche Google Patents/Espacenet/DEPATISnet mit Anmelder "Fröling Heizkessel- und Behälterbau" inkl. Variante "Froling" und Stichwörtern Verguss/Dichtung/Sensor/Regelung. (d) Wettbewerbereinsatz: Referenzseiten von Nordson/Scheugenpflug/Sonderhoff/DOPAG nach "Fröling" durchsuchen. Aktion: nicht kontaktieren, bis (a) belegt. Hinweis: aussichtsreichste Firma des Batches.
- Nicht verwendbare Aussagen: Fertigung AT/DE (S); Werkszuordnung (?); Verguss aller Bauteile (A); Patent EP3495045B1 und Rechtsstand (S); Mitarbeiterzahl (S). Stichprobe für Jey: ja (beste Firma des Batches, Grün/Gelb hängt nur an V für Fertigung).

## 133. Fuhrmann Fahrzeuge GmbH | Halle 21, Stand C40
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Fertigungsbeleg V fehlt).** Kein CRM-Treffer (auch "Fuhrmann" allein nicht). Fertigung Steinebrunn nur S (Prospekt 2014, Händlerangaben); Zweitstandort Valtice/Feldsberg (Tschechien) fertigt Radladerschaufeln, also Hinweis auf Auslagerung ins Ausland, damit Sitzregel nicht anwendbar und Stufe V nötig. Verguss Mittel (A): zugekaufte LED-Leuchten, Magnetventile, ABS/EBS, Kabelbaum; Elektrik ist beim Kipper Nebenbaugruppe. Zeile 6 nicht anwendbar (Verguss nicht Niedrig).
- Eigene Prüfung: Eine WebSearch (Stellenangebote Steinebrunn/Kipper/Elektrik) ergab keinen Treffer zur Firma in Steinebrunn; der einzige Treffer "Fuhrmann Nutzfahrzeuge Service GmbH" (Erharting, DE) ist eine andere Firma (Servicebetrieb) und darf nicht vermischt werden. Kein Beleg, kein Gegenbeleg. Eigene Patentsuche nicht durchgeführt.
- Korrekturen an Toms Feldern: keine inhaltlichen; Feld 17: Verwechslungsgefahr zusätzlich mit Fuhrmann Nutzfahrzeuge Service GmbH (Erharting). Website weiter nicht ermittelt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Website der Firma ermitteln und lesen (Standort-/Produktseite, Impressum, Firmenbuch Ges.m.b.H. Steinebrunn): Wo werden Kipper gebaut, wo die Radladerschaufeln? (b) Welche Elektrik wird verbaut/konfektioniert (Stellenanzeigen Elektriker/Montage, Kabelbaum selbst?), Datenblatt Beleuchtung/ABS. (c) Patentsuche im Browser (Anmelder "Fuhrmann Fahrzeuge" bzw. "Fuhrmann Ges.m.b.H."). Aktion: nicht kontaktieren, bis (a) belegt.
- Nicht verwendbare Aussagen: Fertigung Steinebrunn und "100 % Österreich" (S); Adresse (Prospekt 2014, alt); Verguss (A). Stichprobe für Jey: ja (Fertigungsort und Elektrikanteil offen).

## 134. Futtermittel Fallmann GmbH | Halle 24, Stand 50
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt; Aussortier-Empfehlung).** Entgegen Toms "in Suchergebnissen nicht auffindbar" findet meine WebSearch einen Katalog "www.futtermittel-fallmann.com - Ihr Spezialist für Wiederkäuer, Sommer 2021" (Readkong, S): Mineralfutter, Boli, Eutergesundheitsprodukte, Online-Shop, Geschäftsführung Birgit Fallmann (Telefonvorwahl 0676, Österreich vermutet, nicht belegt). Damit ist die Firma auffindbar, aber Sitz, Rechtsform, Register und ob Hersteller oder Händler bleiben offen. Produkt ist Stoffprodukt (Futter, Boli); alle plausiblen Bauteile Verguss Niedrig (A). CRM: kein Treffer, neu.
- Korrekturen an Toms Feldern: Feld 4/5/17: Website futtermittel-fallmann.com (S) und Geschäftsführung (S) ergänzen; "nicht auffindbar" gestrichen. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Impressum von futtermittel-fallmann.com im Browser lesen: Rechtsform, Sitz, Firmenbuch, Hersteller oder Händler. Aktion: aussortieren (Futtermittel, kein vergossenes Produkt), sofern das Impressum keinen Maschinen-/Gerätebau zeigt.
- Nicht verwendbare Aussagen: Sitz, Fertigung, Hersteller-Status (S/?); Verguss Niedrig (A). Stichprobe für Jey: nein.

## 135. Garant Tiernahrung | Halle 23, Stand 100
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6, Fertigung S, Verguss Niedrig in allen Bauteilen; Aussortier-Empfehlung).** Mischfutterhersteller (Garant-Tiernahrung GmbH, Pöchlarn, Konzern RWA Raiffeisen Ware Austria; Tom, S). Mehrere Werke und Konzern: Fertigung bräuchte Stufe V, ist aber für die Ampel unerheblich, da Futtermittel keine vergossenen/verklebten/gedichteten Bauteile enthält (A). Kein harter Ausschluss E1 bis E4 belegt, daher nicht Rot. CRM: kein Treffer, auch nicht auf Garant, RWA, Raiffeisen Ware Austria.
- Korrekturen an Toms Feldern: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Nur falls Jey nicht allein nach Branche aussortiert: Produkte/Bauteile prüfen (Garant Produktseite, Impressum garant.co.at); erwartet bleibt Verguss Niedrig. Aktion: nicht weiterverfolgen, Jey bestätigt das Aussortieren.
- Nicht verwendbare Aussagen: Fertigung Aschach/Pöchlarn/Graz (S); Mitarbeiterzahl (S, 2014); Verguss Niedrig (A). Stichprobe für Jey: nein.

## 136. GEA Austria GmbH | Halle 23, Stand 150
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5; Rot-Kandidat E2 als Vertriebs-/Servicegesellschaft).** Konzernabgleich (Regel M): GEA, GEA Group, GEA Farm Technologies, Westfalia: kein CRM-Treffer, also kein Zeile-3-Fall. Verguss für das Konzernprodukt Hoch (A; Melksteuerung, Durchflussmesser, Pulsatoren), aber für diese Einheit ist Fertigung in AT nicht belegt (Zeile 5).
- Eigene Prüfung: WebSearch fand den Firmenbuchauszug (evi.gv.at/f/128711g, S): GEA Austria GmbH, Breitwies 1, 5303 Thalgau, FN 128711 g, Gesellschafter GEA Farm Technologies GmbH und GEA Mechanical Equipment GmbH, vertretungsbefugt Mag. Klaus Laimer, eingetragen seit 07.12.1994. Geschäftszweig im Auszug nicht sichtbar. Das klärt die Identität teilweise: Rechtsträger ist laut Register Thalgau; Toms Wiener "GEA CEE GmbH" ist damit eine andere Einheit und nicht gleichzusetzen. Fertigung in Thalgau weiter ungeklärt.
- Korrekturen an Toms Feldern: Feld 4/17: Sitz Thalgau (Register-Snippet S) statt "Wien bzw. Thalgau"; Gesellschafter ergänzen. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Fertigt GEA Austria in Thalgau (Stellenanzeigen Montage/Produktion Thalgau, gea.com/de/austria, Firmenbuchauszug mit Geschäftszweig im Browser)? (b) Ist die Einheit nur Vertrieb/Service (dann E2, Rot)? (c) Falls Fertigung der Melktechnik bei GEA Farm Technologies (Bönen, DE): als eigene Firma erst nach Jeys Freigabe prüfen, sie stellt nicht auf der Messeliste aus. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung (?), Verguss des Konzernprodukts (A), Konzernpatente (S), Rechtsträger Wien (S). Stichprobe für Jey: ja (Einheitenfrage Konzern).

## 137. Genetic Austria GmbH | Halle 24, Stand 10
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2).** Gemeinschaftsunternehmen der Besamungsstationen, Export von Rindersamen/Embryonen/Zuchttieren (Advantage-Austria-Profil, S; meine Suche bestätigt "Zusammenschluss der österreichischen Rinderbesamungsstationen", Hohenzell/Innkreis, S). Keine Fertigung technischer Produkte, verbandsnah/Vertriebsgesellschaft: Jeys Entscheidung "Verbände raus" und E2 treffen inhaltlich zu, nur S-Beleg. CRM: kein Treffer. Nicht mit genetiX Austria GmbH verwechseln.
- Korrekturen an Toms Feldern: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Nur zur Absicherung: Firmenbuch/Impressum der Gesellschaft, Geschäftszweck (kein Gerätebau). Aktion: aussortieren.
- Nicht verwendbare Aussagen: Gemeinschaftsunternehmen-Status, kein Fertiger (S/A). Stichprobe für Jey: nein.

## 138. Genezis Trade Austria | Halle 17, Stand 100
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2/E3).** Düngemittelhandel Wien (WKO-Firmen-A-Z, S); Hersteller Nitrogénművek Zrt. in Ungarn (S). Händler ohne Fertigung in DE/AT/NL, Produkt Dünger ohne Verguss (A). Schwester Genezis Trade Germany (München) laut Katalog: kein CRM-Treffer. Nur S, daher kein Rot.
- Korrekturen an Toms Feldern: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Impressum/Firmenbuch Genezis Trade Austria GmbH lesen: reiner Handel? Aktion: aussortieren (Händler).
- Nicht verwendbare Aussagen: Hersteller Ungarn, kein eigener Betrieb (S). Stichprobe für Jey: nein.

## 139. Genol GesmbH | Halle 20, Stand F30
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2).** Schmierstoff-Vertriebsmarke (Korneuburg, Gesellschafter RWA und OMV Downstream laut Firmenbuch-Snippet, S); Herstellung nicht belegt. CRM: Genol, RWA, OMV, Raiffeisen Ware Austria: kein Treffer (kein Zeile-3-Fall). Schmierstoffe sind kein Verguss-/Klebstoff-Kerngeschäft; ob Fette/Dichtmassen im Sortiment sind (Nähe zu E1 Materialhersteller), nicht geprüft.
- Korrekturen an Toms Feldern: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Produktseite/Impressum: Stellt Genol selbst her oder vertreibt es nur; führt das Sortiment Dichtmassen/Klebstoffe (dann E1)? Aktion: aussortieren, sofern nur Schmierstoffvertrieb.
- Nicht verwendbare Aussagen: Fertigung, Gesellschafter (S/?). Stichprobe für Jey: nein.

## 140. Gesing Tierzucht Österreich GmbH | Halle 23, Stand 60
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Meine WebSearch bestätigt Toms Befund: kein Treffer zu "Gesing Tierzucht Österreich GmbH" (nächste: PIG Austria GmbH, Rinderzucht Austria, geneticAUSTRIA, andere Firmen, nicht gleichzusetzen). Messelisten-Beschreibung: Genetik/Besamung/Schweinezucht, also kein technischer Fertiger (S/A). CRM: Gesing kein Treffer.
- Korrekturen an Toms Feldern: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Firmenbuch/WKO-Abfrage "Gesing" (Firmenname, Sitz, Geschäftszweck; ggf. Schreibweise "Gesing Tierzucht GmbH" bzw. Mutter in Deutschland). Aktion: aussortieren (Tierzucht), außer die Identität zeigt Gerätebau.
- Nicht verwendbare Aussagen: alle zu Sitz, Produkt, Identität (S/?). Stichprobe für Jey: nein.

## Einschränkungen
- Kein Browser, kein WebFetch: Stufe V gibt es in diesem Batch nicht; alle Ampeln vorläufig; kein Grün vergeben. Kein Zitat von Tom im Browser gegengelesen.
- Websuche: 6 Abfragen (Fröling Produktion, Fröling Patent, Fuhrmann Produktion, GEA Austria Firmenbuch, Fallmann, Gesing). Ergebnisse sind Kurzfassungen; Aussagen daraus sind Stufe S.
- Patente (F5): Google Patents/Espacenet/DEPATISnet nicht direkt abfragbar; eigene Suche nur zu Fröling, nicht zu den übrigen neun Firmen. Feld 9 bleibt nach F5 unvollständig, Nachholen im Browser für Fröling und Fuhrmann zuerst.
- Wettbewerbereinsatz (F6): nur Grep auf wettbewerber_referenzen.md, keine Einzelsuche. Kein Einfluss auf die Ampel.
- Identität (Feld 17): Impressum/Firmenbuch bei keiner Firma im Original gelesen; GEA Austria (Thalgau, FN 128711 g) und Fallmann (futtermittel-fallmann.com) nur über Snippets teilgeklärt.
- Nichts verschickt, kein Datenbankfeld geändert.
