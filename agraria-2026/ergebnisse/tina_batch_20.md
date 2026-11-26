# Tina Batch 20 - agraria 2026 (Prüfung von tom_batch_20.md)
Erstellt: 2026-11-25 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_20.md (10 Firmen, Nr. 1 bis 10 des Batches; Tom-Nummern 191 bis 200 der Eingabeliste).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (9 Abfragen, Kurzfassungen/Snippets) und Bash zur Verfügung; WebFetch und Chrome nicht nutzbar. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün ist mailtauglich.
Skripte: `python3 crm_abgleich.py` für alle 10 Firmen sowie Konzern-/Alt-/Schwesternamen selbst wiederholt (Borealis, Grupa Azoty, Agrofert, Lely Industries, Lely Holding, Lely Deutschland, Lely West, Mayrhofer, Lema, Lasco, Landrichinger, Ley, Eidenhammer, Landwirtschaftskammer, Landjugend, Agrarmedien, Landwirt): überall "kein Treffer -> neu". Damit schließt der CRM-Abgleich auch die von Tom offen gelassenen Namen (Agrofert, Lely Holding, Mayrhofer). Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum aller Einträge: 2026-11-25.
Jey-Entscheidungen angewandt: Verbände/Prüfdienstleister/Forschung raus; CRM-Namensgleiche raus (hier keine); Anlagenbauer bleiben drin, außer sie bauen selbst Verguss-/Dosieranlagen (E1).

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | Landesverband für Ziegenzucht und -Haltung OÖ (H24/130) | ROT (Jey-Entscheidung Verband) | 1 (E2) | nein |
| 2 | Landjugend Oberösterreich (H21/1340) | ROT (Jey-Entscheidung Verband) | 1 (E2) | nein |
| 3 | Landtechnik Eidenhammer GmbH (H22/A40) | GELB | 7 (Rot-Kandidat E2, Händler) | nein |
| 4 | Landwirt Agrarmedien GmbH (H20/1140) | GELB | 7 (Rot-Kandidat E2, Verlag) | nein |
| 5 | Landwirtschaftskammer Oberösterreich Rinderberatung (H24/10) | ROT (Jey-Entscheidung Verband/Beratung) | 1 (E2) | nein |
| 6 | LASCO Heutechnik GmbH (H23/290) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 7 | LAT Nitrogen Austria GmbH (H23/115) | GELB | 6 (Verguss Niedrig; Identität offen) | nein |
| 8 | LELY (H23/140) | GELB | 2 (Identität; zusätzlich Zeile-5-Thema) | ja |
| 9 | LEMA (H19/55) | GELB | 2 (Identität; Rot-Kandidat E2 möglich) | ja |
| 10 | LEY Maschinen GmbH (H19/110) | GRÜN (schwach) | 4 (Sitzregel) | ja |

Zahlen: Grün 2 (beide schwach), Gelb 5, Rot 3.
Hinweis zu Rot 1, 2, 5: Rot stützt sich auf die Jey-Entscheidung "Verbände raus" und den Firmennamen (Verband bzw. Körperschaft); die Quelle ist nur die Messeliste (Stufe S). Nach Tabelle D Zeile 1 wäre für E2 sonst V nötig. Die Jey-Entscheidung ersetzt hier die Einzelbelegung; vorläufig, bitte bestätigen.

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet und DEPATISnet nicht direkt abfragbar. Eigene Patent-WebSearch nur für LASCO (2 Abfragen, Treffer s. u.) und Lely (1 Abfrage, kein Lely-Treffer). Für die übrigen Firmen keine eigene Wiederholung (Verbände/Verlag/Händler: nicht sinnvoll bzw. aus Sitzungslimit nicht nachgeholt; LAT, LEMA, LEY nicht eigens gesucht, Toms Suchen weder übernommen noch widerlegt). Feld 9 ist damit bei ALLEN 10 Firmen ohne Datenbankabfrage: nach F5 UNVOLLSTÄNDIG, Nachholen im Browser nötig. "Keine Treffer" ist kein Gegenbeweis. Wettbewerbereinsatz (F6): Grep auf wettbewerber_referenzen.md mit den Wörtern Lely, Lasco, Lema, Ley, Eidenhammer, LAT Nitrogen, Borealis, Agrofert, Mayrhofer: kein Treffer; keine Einzelsuchen mit Wettbewerbernamen von mir. Messe-Signal (N2): Grep der Gesamtliste agraria_2026_aussteller_DE-AT-NL.csv auf E1-Namen (Scheugenpflug, DOPAG, ViscoTec, RAMPF, bdtronic, Nordson, Sonderhoff, ELANTAS, Henkel, DELO, Wacker, Sika, Panacol, OTTO-CHEMIE, Musashi, Hilger): 0 Treffer. Damit ist Toms offener Punkt N2 erledigt, ohne Einfluss auf die Ampel.

---

## 1. Landesverband für Ziegenzucht und -Haltung OÖ | Halle 24, Stand 130
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT (Tabellenzeile 1, E2 nach Jey-Entscheidung "Verbände raus").** Zuchtverband, keine Fertigung; Messeliste: Produktgruppen Hofmanagement/Vereine, Verbände (S). CRM: crm_abgleich.py "Landesverband für Ziegenzucht und Haltung OÖ": kein Treffer, neu.
- Rot, weil: Verband/Interessenvertretung ohne Fertigung; Quelle nur Messeliste https://agraria.at/aussteller (S) und Name; Jey-Entscheidung ersetzt Einzelbeleg.
- Korrekturen an Toms Feldern: keine. Feld 9 (Patent) bei Verband bedeutungslos. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: keiner (Rot). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Sitz OÖ (A), alle Produktangaben (S). Stichprobe für Jey: nein.

## 2. Landjugend Oberösterreich | Halle 21, Stand 1340
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT (Tabellenzeile 1, E2 nach Jey-Entscheidung).** Jugendorganisation/Verband, keine Fertigung (Messeliste S). CRM: "Landjugend Oberösterreich", "Landjugend": kein Treffer, neu.
- Rot, weil: Verein/Verband ohne Fertigung (https://agraria.at/aussteller, S; Jey-Entscheidung).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: keiner. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (A/S). Stichprobe für Jey: nein.

## 3. Landtechnik Eidenhammer GmbH | Halle 22, Stand A40
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2 Händler).** Landtechnikhändler (Premium Gold Händler laut Landwirt.com-Profil, S), Filialen Marchtrenk und St. Veit im Pongau, Handelsware Hoflader/Landmaschinen anderer Marken (Eurotrac, Toyo, Thaler, Schieder). Keine Eigenfertigung gefunden, aber ohne Impressum/Firmenseite nicht V; E2 braucht V, daher nicht Rot. CRM: "Landtechnik Eidenhammer", "Eidenhammer": kein Treffer, neu. Verguss Niedrig (A, Handelsware).
- Korrekturen: Toms "kein Fertiger" ist plausibel, aber Stufe S; Ampel daher Gelb statt Rot. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Bestätigen, dass Eidenhammer nur Händler/Werkstatt ist und keine Anbaugeräte/Aufbauten fertigt. Wo: Firmenwebsite/Impressum, Firmenbuch (Burgkirchen), Messeprofil agraria. Bei Beleg: Rot nach E2 mit URL. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Händlerstatus (S), Standort (S). Stichprobe für Jey: nein.

## 4. Landwirt Agrarmedien GmbH | Halle 20, Stand 1140
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2 Verlag/Medien).** Verlag/Portal (Messeliste: Verlage, Zeitschriften, Fachbücher, S); keine technischen Produkte. Verlag fällt nicht wörtlich unter die Jey-Entscheidung (Verbände/Prüfdienstleister/Forschung), nur unter E2 sinngemäß; Beleg nur Messeliste (S). Zuordnung zur Portalmarke landwirt.com nicht belegt (Tom, bestätigt). CRM: "Landwirt Agrarmedien", "Agrarmedien", "Landwirt": kein Treffer, neu.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Impressum landwirt.com/Firmenbuch lesen: Ist die GmbH reiner Verlag/Medienhaus ohne Produktion technischer Waren (Merchandise nur Zukauf)? Bei Beleg Rot nach E2 mit URL; Jey kann alternativ Verlage pauschal als "raus" bestätigen. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (A/S). Stichprobe für Jey: nein.

## 5. Landwirtschaftskammer Oberösterreich Rinderberatung | Halle 24, Stand 10
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT (Tabellenzeile 1, E2 nach Jey-Entscheidung).** Interessenvertretung/Beratung (Körperschaft öffentlichen Rechts, A), keine Fertigung. CRM: "Landwirtschaftskammer Oberösterreich Rinderberatung", "Landwirtschaftskammer": kein Treffer, neu.
- Rot, weil: Verband/Beratung (E2, Jey-Entscheidung; Messeliste https://agraria.at/aussteller, S).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: keiner. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (A/S). Stichprobe für Jey: nein.

## 6. LASCO Heutechnik GmbH | Halle 23, Stand 290
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Fertigung Stufe A nach Sitzregel).** Hersteller von Heukränen, Trocknungsanlagen, Steuerungen mit erkennbarem Standort Pöndorf (Neubau/Erweiterung laut Land OÖ, S), eigene Produkte, kein Händler, kein Konzern mit mehreren Werken, kein Auslagerungshinweis. Neu aus meiner Suche: karriere.at-Firmenseite Pöndorf nennt für LASCO Heutechnik die Tags Schweißer und Montage (S, nur Tags, undatiert, nicht V); stützt Fertigung am Sitz. Verguss Mittel (A: Funk-/Kransteuerung, Trocknungssteuerung, Feuchte-/Temperatursensorik, Motoren/Windenantriebe). CRM: "LASCO Heutechnik", "LASCO", "Lasco", "Landrichinger": kein Treffer, neu.
- Eigene Prüfung Patente (WebSearch, keine Datenbankabfrage): GoodIP-Profil "LASCO Heutechnik GmbH" nennt 33 Patentanmeldungen, meist EPA, DE, HU (S, Drittseite); EP2390606 "Hay drying system" (Anmelder LASCO Heutechnik GmbH, Lochen, Erfinder Johann Landrichinger, Priorität 28.05.2010 DE 202010007362 U, EPO GPI, S): Luftumwälzung/Schläuche, kein Verguss-Bezug; Rechtsstand nicht ermittelt. Das widerspricht Toms "keine Patente gefunden": er hat keine gefunden, es gibt aber mindestens eine Anmeldung (Anmelder-Name abweichend: Sitz Lochen). Verguss-relevante Patente nicht gefunden (Suche nicht ausgeschöpft). Heukran-Linie laut Landwirt.com-Meldung 2012 aus "Maraton Heukran" hervorgegangen (S): Vorgängername für Patent- und CRM-Suche merken (CRM "Maraton" nicht geprüft).
- Korrekturen an Toms Feldern: Feld 9 (Patente existieren, 33 laut GoodIP, S); Feld 4 Hinweis Lochen/Pöndorf bleibt; Rest bestätigt. Zitat im Browser bestätigt: nein.
- Nachrecherche (für Mailstufe nötig, kein Gelb): (a) lasco.at, Produktseiten Heukran-/Trocknungssteuerung, Datenblätter im Browser lesen: Wird Steuerelektronik selbst gefertigt/vergossen? (b) Impressum und Stellenanzeigen Pöndorf als V für Fertigung (Zitat Schweißer/Montage). (c) Google Patents/Espacenet/DEPATISnet, Anmelder LASCO Heutechnik GmbH, Landrichinger, Maraton, mit Stichwort Verguss/Dichtung; Rechtsstand je Patent. (d) CRM "Maraton" nachprüfen.
- Nicht verwendbare Aussagen: Fertigung Pöndorf (A/S), Verguss aller Bauteile (A), ca. 60 Beschäftigte (S), Patentzahl (S). Stichprobe für Jey: ja (Grün ohne V; Verguss nur abgeleitet; Elektronik evtl. zugekauft).

## 7. LAT Nitrogen Austria GmbH | Halle 23, Stand 115
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6, Fertigung belegt (S), Verguss Niedrig bei allen Bauteilen; zusätzlich Identität offen).** Düngemittel-/Stickstoffchemie, Werk Linz (S); keine Elektronik- oder Geräteprodukte, daher keine typisch vergossenen Bauteile (A). Zwei Gesellschaften (LAT Nitrogen Linz GmbH Werk, LAT Nitrogen Austria GmbH): welche stellt aus, ungeklärt. Nicht E1 (kein Klebstoff-/Vergussmassenhersteller belegt), daher nicht Rot. CRM: "LAT Nitrogen Austria", "LAT Nitrogen", "Borealis", "Grupa Azoty", "Agrofert": kein Treffer, neu (Agrofert-Abgleich von mir nachgeholt).
- Korrekturen: keine. Zitat im Browser bestätigt: nein. Eigene Patentsuche nicht wiederholt.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Welche LAT-Gesellschaft steht auf der Messe (Firmenbuch FN 257746 p)? Gibt es Produkte/Anlagenteile mit Dichtung/Verguss (z. B. Abfüll-/Verpackungsanlagen, Eigenbau)? Wo: Firmenbuch, lat-nitrogen.com. Erwartung: uninteressant, niedrige Priorität. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Linz (S); Mitarbeiterzahl (S); Produktionsstand nach Teileinstellung 2024 (S). Stichprobe für Jey: nein.

## 8. LELY | Halle 23, Stand 140
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt; Zeile 5 würde ebenfalls Gelb ergeben).** Messeliste nennt nur "LELY"; tatsächliche Firma vermutlich Lely Industries N.V., Maassluis (NL, S), in AT Vertriebsgesellschaft. Konzern mit mehreren Werken: Sitzregel gilt nicht, Stufe V nötig. Meine Suchen: Lely-Eigenseiten (Careers/Campus, S) bestätigen Maassluis als Produktionshaus (Campus-Erweiterung eröffnet 30.06.2022, Produktionskapazität verdoppelt; Elektronik-Ingenieursstellen); Agriland nennt 16 Montageschritte, 160 Personen in der Produktion, 80 Roboter pro Woche (S). Widerspruch: ein niederländischer Artikel (mtsprout.nl, undatiert, abgeschnitten) sagt, der Astronaut werde derzeit in Rotterdam entwickelt und produziert, mit geplanter Rückkehr nach Maassluis (S, einzelne Quelle, nicht bestätigt). Für Fertigung in NL spricht beides (NL), doch Standort je Produkt/Elektronik ungeklärt. Verguss Hoch (A: Sensoren, Antriebe, Steuerelektronik im Stall). Eigene Aussage "Elektronik in Maassluis gefertigt": nicht belegt. CRM: "LELY", "Lely Industries", "Lely Holding", "Lely Deutschland", "Lely West": kein Treffer, neu. Lely-Patent-Suche (Anmelder "Lely Patent N.V." plus potting/encapsulation/sealing): kein Lely-Treffer, nur Fremdanmelder, keine Datenbankabfrage; Patentstatus offen.
- Korrekturen an Toms Feldern: Feld 4 um Rotterdam-Hinweis ergänzen (Stufe S, ungeklärt); Feld 9 weiter UNVOLLSTÄNDIG (direkte Anmelderabfrage fehlt). Toms "interessant" nicht bestätigt (nur S/A, Regel I verlangt Browser-Gegenlesen). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2/5): (a) Welche Einheit stellt aus: Lely Industries N.V. oder AT-Gesellschaft (Impressum lely.com, Firmenbuch AT, Messeprofil)? (b) Fertigung Elektronik/Sensorik in Maassluis (V): lely.com/careers/production-logistics und production-supply-chain, Stellenanzeigen "Electronics" im Browser lesen; Rotterdam-Hinweis klären. (c) Google Patents/Espacenet, Anmelder "Lely Patent N.V.", "Lely Industries N.V.", "Lely Holding", Stichwort potting/sealing. Wenn Fertigung NL belegt: Grün erwartbar (Zeile 4). Aktion: nicht kontaktieren, bis Einheit geklärt.
- Nicht verwendbare Aussagen: Fertigung Maassluis (S), Konzernangaben/Mitarbeiterzahl (S), Verguss aller Bauteile (A), Patentstatus. Stichprobe für Jey: ja (Identität und Konzern).

## 9. LEMA | Halle 19, Stand 55
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt; Rot-Kandidat E2/Handel).** Messeliste nennt nur "LEMA"; Zuordnung zu LEMA Mayrhofer GmbH, Siegfried-Marcus-Straße 3, 4070 Eferding (Herold, S) ist Annahme. Meine Suche: karriere.at-Profil führt die Branche als "Handel", 1957 gegründet, 11 bis 30 Mitarbeiter (S); mehrere Händlerinserate (Landwirt.com) für "Lema"-Hochdruckreiniger Red Power/Hot; kein Treffer zu Werk, Produktion oder Impressum. Wahrscheinlich Marke bzw. Importeur/Vertrieb, Eigenfertigung unbelegt (Hersteller der Geräte unbekannt). Nicht Rot, da kein V. Verguss Mittel (A, Reiniger: Pumpenmotor, Brennersteuerung). CRM: "LEMA", "LEMA Mayrhofer", "Mayrhofer", "Lema": kein Treffer, neu (Mayrhofer-Abgleich nachgeholt).
- Korrekturen an Toms Feldern: Feld 7 "Fertigung Mittel (S)" ist zu hoch gegriffen; Branchenhinweis "Handel" spricht gegen Hersteller, daher Fertigung eher unbelegt/offen. Feld 17 bleibt Annahme. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Ist Aussteller "LEMA" = LEMA Mayrhofer GmbH? Messeprofil agraria.at, Impressum, Firmenbuch Eferding. (b) Fertigt Mayrhofer in Eferding (Montage Hochdruckreiniger) oder importiert/vertreibt es Fremdfabrikate? Impressum, Produktseiten, Stellenanzeigen im Browser. Bei Vertrieb ohne Fertigung: Rot nach E2/E3 mit URL. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Sitz Eferding (S), Fertigung (S/?), Verguss (A), Größe (S). Stichprobe für Jey: ja (Firma nicht identifiziert).

## 10. LEY Maschinen GmbH | Halle 19, Stand 110
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Fertigung Stufe A nach Sitzregel).** Maschinen-/Anlagenbauer mit einem erkennbaren Standort Lengau (Ley Maschinen Gesellschaft m.b.H., Gewerbestraße 12 A; Verzeichnis der Metalltechnischen Industrie, Mitgliedsfirmen, S): Getreidemühlen, Mahl- und Mischanlagen, Förderschnecken, laut Verzeichnis auch "Computer und Wägetechnik" (S); eigene Marke "Ley" in Landwirt.com-Inseraten (S). Kein Händler-, Konzern- oder Auslagerungshinweis. Anlagenbauer von Mühlen/Mischanlagen, keine Dosier-/Vergussanlagen: E1 nicht einschlägig, bleibt drin (Jey). Verguss Mittel (A: Steuerung/Schaltschrank, Motoren, Füllstands-/Näherungssensoren). Meine Suche nach Eigenfertigung des Schaltschranks/der Steuerung: kein Beleg (kein Gegenbeleg). CRM: "LEY Maschinen", "Ley": kein Treffer, neu. Identität: Messe- und Verzeichnisname stimmen überein (m.b.H. = GmbH).
- Korrekturen an Toms Feldern: Feld 7 "Mittel (S)" besser "Hoch (A, Sitzregel)"; Feld 8 bestätigt (Mittel A). Eigene Patentsuche nicht wiederholt. Zitat im Browser bestätigt: nein.
- Nachrecherche (für Mailstufe nötig, kein Gelb): (a) ley-getreidetechnik.at, Impressum, Stellenanzeigen Lengau im Browser lesen: Fertigung/Montage am Sitz (V). (b) Baut Ley die Steuerung selbst oder Zukauf (Datenblatt/Produktseite)? (c) Firmenbuch Lengau (Identität, Eigentümer/Konzern). (d) Patente, Anmelder Ley Maschinen, Verguss/Dichtung.
- Nicht verwendbare Aussagen: Fertigung Lengau (A/S), Verguss (A), Produktpalette (S). Stichprobe für Jey: ja (Grün ohne V; Verguss nur abgeleitet).

---

## Einschränkungen
- Kein WebFetch, kein Browser: keine Stufe-V-Aussage, keine Firmenwebsite, kein Impressum, kein Firmenbuch gelesen; Zitate in Toms Feld 14 nicht gegengelesen. Beide Grün-Kandidaten (Nr. 6, 10) sind nur nach Sitzregel (Stufe A) Grün und unbestätigt.
- WebSearch: 9 Abfragen (LASCO 3, Lely 3, LEMA 1, LEY 1, plus GoodIP/EPO-Detail zu EP2390606); Ergebnisse sind Kurzfassungen. Nicht durchgeführt: eigene Patent-/Wettbewerbersuche für LAT, LEMA, LEY, Eidenhammer und alle Verbände/Verlag; keine Datenbankabfrage (Google Patents, Espacenet, DEPATISnet) für irgendeine Firma, daher Feld 9 überall unvollständig und der Batch nach Regel F5 UNVOLLSTÄNDIG.
- Patent-Rechtsstand (z. B. EP2390606 LASCO) nicht ermittelt; GoodIP-Zahl "33 Anmeldungen" ist Drittangabe (S).
- Konzernabgleich für LAT (Agrofert, Borealis) und Lely (Holding) im CRM erledigt (kein Treffer); "Maraton" (Vorgängername LASCO-Heukran) nicht gesucht.
- Es wurde nichts verschickt und kein CRM-Feld geändert; kein git commit.
