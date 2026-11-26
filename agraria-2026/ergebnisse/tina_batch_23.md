# Tina Batch 23 - agraria 2026, Wels (Prüfung von tom_batch_23.md)
Erstellt: 2026-11-25 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_23.md (10 Firmen, Nr. 221 bis 230 der Messeliste, hier als Nr. 1 bis 10 geführt).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser geprüft, vorläufig.** Es standen WebSearch (4 Abfragen, nur Snippets/Kurzfassungen), Bash/Python und Grep zur Verfügung; kein Browser, WebFetch nicht genutzt. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein. Kein Ergebnis ist mailtauglich.
Skripte: `python3 crm_abgleich.py` für alle Firmen samt Konzern-/Alt-/Schreibvarianten selbst wiederholt (Moser-Glaser, Moser Solar, Motorex AG, Motorex-Bucher, Nero Mulcher, Niederl, novutrack, Saatbau, Niederösterreichische Saatbaugenossenschaft). Einziger Treffer: Moser (Zeile 1647). "Niederl" liefert nur Wortfragment-Zufallstreffer (Niederlande, Niederlassung), kein Firmenbezug. Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum: 2026-11-25.
Entscheidungen von Jey angewendet: Verbände/Prüfdienstleister/Forschung raus (im Batch keine solche Firma); Firmen im CRM mit gleichem/sehr ähnlichem Namen raus (Moser); Anlagenbauer bleiben drin, außer sie bauen selbst Verguss-/Dosieranlagen (E1; im Batch keiner, Grep Messeliste auf E1-Namen ohne Treffer laut Tom, von mir nicht wiederholt).

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | monica.farm (H23 / 220) | GELB | 2 | ja |
| 2 | Moser GmbH (H23 / 430) | ROT (Jey-Regel ähnlicher CRM-Name) | 1 (nach Jey-Entscheidung, Einheit nicht belegt) | ja |
| 3 | MOTOREX GmbH (H18 / 250) | GELB (Rot-Kandidat E2) | 7 | nein |
| 4 | Multikraft Produktions- und Handels GmbH (H23 / 330) | GELB | 6 | nein |
| 5 | NERO (H21 / C50) | GELB | 2 | ja |
| 6 | Niederl GmbH Stalltechnik (H23 / 410) | GELB | 2 | ja |
| 7 | novu.track GmbH (H22 / 1140) | GELB | 2 | ja |
| 8 | Nufarm GmbH & Co KG (H23 / 450) | GELB | 6 (Konzern, Fertigung nur S) | nein |
| 9 | NÖ. Saatbaugenossenschaft (H23 / 460) | GELB | 6 | nein |
| 10 | Obereder GmbH (H19 / 180) | GELB (Rot-Kandidat E2) | 7 | nein |

Zahlen: Grün 0, Gelb 8, Rot 1 (Moser, per Jey-Entscheidung), plus Gelb-Rot-Kandidaten Nr. 3 und 10. Keine Grün-Kandidatin; die beiden aussichtsreichsten (NERO, novu.track) scheitern an der Identität.

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet und DEPATISnet nicht direkt abfragbar. Eigene Patent-Websuche nur für novu.track (1 Abfrage, kein Patentbezug gefunden, Rechtsstand nicht prüfbar) und NERO (Herstellersuche; ohne Herstellernamen keine Anmeldersuche möglich). Für die übrigen acht Firmen keine eigene Patentsuche (Händler/Agrochemie/Genossenschaft, ohne Einfluss auf die Ampel); Toms Suchen werden weder übernommen noch widerlegt. Feld 9 ist damit bei ALLEN 10 Firmen ohne Datenbankabfrage: nach F5 UNVOLLSTÄNDIG, im Browser (Google Patents, Espacenet, DEPATISnet, Rechtsstand) nachholen, vorrangig für novu.track und NERO nach Klärung des Herstellers. "Keine Treffer" ist kein Gegenbeweis. Toms Patentsuche (je 1 WebSearch) ist ausdrücklich unvollständig und wird von mir nicht als erfüllt gewertet.
Wettbewerbereinsatz (F6): Grep auf wettbewerber_referenzen.md mit allen Firmen- und Konzernnamen (nero, novu, moser, motorex, multikraft, niederl, nufarm, obereder, saatbau, monica): kein Treffer (einziger Treffer "Niederlassung" im Graco-Eintrag, Zufall). Keine Einzelsuchen mit Wettbewerbernamen von mir (Sitzungslimit/Priorität).

---

## 1. monica.farm | Halle 23, Stand 220
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** CRM: crm_abgleich.py "monica.farm": kein Treffer, neu. Firma weder bei Tom noch bei mir identifizierbar (keine eigene Websuche; Toms zwei Suchen ohne Fund, Domain-Abruf scheiterte). Produktbeschreibung nur aus Messeliste (S, nach Regel N5 nie V): Agrarmonitoring/Software, Kamerasysteme. Software-/Plattformanbieter wäre E2, aber ohne V kein Rot.
- Korrekturen an Toms Feldern: keine; Toms Einstufung "kein Fertiger" bleibt vorläufig. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer ist monica.farm (Rechtsform, Sitz, Firmenbuch/Impressum)? Baut sie eigene Kamera-/Sensorhardware und wo? Wo: Website monica.farm im Browser (Impressum, Produktseite), Firmenbuch/evi.gv.at, Messeprofil agraria. Bei reiner Software/Plattform: Rot nach E2 mit URL. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle zu Sitz, Produkt, Fertigung, Verguss (?/S/A). Stichprobe für Jey: ja (Firma nicht identifizierbar). Verifikation: 2026-11-25.

## 2. Moser GmbH | Halle 23, Stand 430
**ohne Browser geprüft, vorläufig. Ampel: ROT nach Jey-Entscheidung (Firmen mit sehr ähnlichem CRM-Namen raus), Tabellenzeile 1 sinngemäß (E5).** Eigener Skriptlauf: "Moser GmbH" = Kern-Name "moser", PRAEFIX-Treffer bekannte_firmen_DE-AT-NL.txt:1647 "Moser-Glaser AG [DE]"; "Moser-Glaser" IDENTISCH mit derselben Zeile. Hinweis zur Ehrlichkeit: Dass Messefirma (Kandidat Moser Solar GmbH, Ried im Traunkreis, AT) und CRM-Einheit Moser-Glaser AG dieselbe juristische Einheit sind, ist NICHT belegt; Rot beruht allein auf Jeys Namensregel, nicht auf einem V-Beleg. Unabhängig davon wäre sie ohnehin kaum Grün: Installateur/Errichter von PV-Anlagen (S), Fertigung nicht belegt, E2 (Händler/Installateur) wahrscheinlich; Identität (mehrere Moser-Firmen) offen.
- Korrekturen an Toms Feldern: Toms Behandlung (nicht aufnehmen) bestätigt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: keiner (raus). Nur falls Jey die Namensregel für diesen Fall aufhebt: Welche Moser GmbH stellt in Halle 23 aus, Firmenbuch/Impressum, Verhältnis zu Moser-Glaser AG.
- Nicht verwendbare Aussagen: Fertigung (S); Verguss Mittel (A, zugekauft); Identität. Stichprobe für Jey: ja (Rot ohne V-Beleg der Einheit). Verifikation: 2026-11-25.

## 3. MOTOREX GmbH | Halle 18, Stand 250
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2).** Vertriebsgesellschaft (MOTOREX (A) GmbH, Hallein) des Schweizer Herstellers MOTOREX AG (Langenthal); Produktion außerhalb DE/AT/NL (S, Tom). Schmierstoffe: Verguss Niedrig (A). E2/E3 plausibel, aber nur Stufe S, daher kein Rot. CRM: "MOTOREX GmbH", "Motorex AG", "Motorex-Bucher": kein Treffer, neu (Konzern ebenfalls nicht im CRM).
- Korrekturen an Toms Feldern: Toms Feld 13 "keiner nötig" ist bei Gelb ungültig, Auftrag ergänzt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Hat MOTOREX GmbH Hallein eigene Produktion/Abfüllung/Montage (z. B. Schmiergeräte)? Wo: Impressum und Karriereseite motorex.com/at, Firmenbuch evi.gv.at/f/411735v im Browser. Ohne Fertigungsbeleg: Rot E2 mit URL. Aktion: nicht kontaktieren, geringe Priorität.
- Nicht verwendbare Aussagen: Vertrieb ohne Fertigung (S); Verguss Niedrig (A); Konzerngröße (S). Stichprobe für Jey: nein. Verifikation: 2026-11-25.

## 4. Multikraft Produktions- und Handels GmbH | Halle 23, Stand 330
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6, Fertigung wahrscheinlich, Verguss Niedrig).** Hersteller fermentierter Bodenhilfsstoffe/EM in Pichl bei Wels (Sitzregel A, Quellen S). Alle Bauteile/Produkte (Flüssigprodukte, Verpackung) Niedrig (A); kein Bezug zu den sechs Demak-Bereichen erkennbar. Kein harter Ausschluss, daher nicht Rot. CRM: "Multikraft": kein Treffer, neu.
- Korrekturen: keine; Toms "unwahrscheinlich" bestätigt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Gibt es Produkte/Bauteile mit Verguss-, Klebe- oder Dichtungsbedarf (z. B. Dosier-/Ausbringgeräte, eigene Abfüll- oder Verpackungslinie mit Klebe-/Dichtschritten)? Wo: Produktseiten multikraft.com im Browser. Erwartung: bleibt Gelb/uninteressant. Aktion: nicht kontaktieren, niedrigste Priorität.
- Nicht verwendbare Aussagen: Fertigung am Sitz (S/A); Verguss Niedrig (A). Stichprobe für Jey: nein. Verifikation: 2026-11-25.

## 5. NERO | Halle 21, Stand C50
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Eigene Prüfung (2 WebSearch: Hersteller/Impressum; Hersteller/Importeur): ausschließlich Händlerinserate auf landwirt.com (u. a. Gailer GmbH Kötschach-Mauthen, KOL-Technik bei Graz, Landtechnik Karl Scheuch NÖ, Der Kern der Landtechnik e.U. Unterweißenbach). Das Portal führt die Marke teils als "Sonstige", nennt keinen Hersteller. Kein Hersteller, Importeur, Sitz oder Impressum gefunden; ein Hinweis auf österreichische Fertigung fehlt völlig. Produkte (Schlegel-/Böschungsmulcher, Holzhacker) enthalten typisch vergossene Teile nur in der Hydraulik-/Elektrik-Peripherie (Magnetventilspulen, Kabelbäume, A, Mittel). Landtechnik-Anbaugeräte aus Stahlbau: Verguss Mittel bleibt schwach. CRM: "NERO", "Nero Mulcher": kein Treffer, aber ohne Herstellername nicht abgleichbar. Patente: ohne Hersteller keine Anmeldersuche möglich (Feld 9 offen). Möglich ist, dass NERO eine Handelsmarke eines Herstellers außerhalb DE/AT/NL ist; nicht belegt, kein Rot.
- Korrekturen an Toms Feldern: Feld 7 "Mittel ?" bleibt, Toms "prüfenswert" nicht bestätigt (Stufe ?/S/A, nach Regel I nur mit Browser). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2), Priorität hoch: Wer stellt NERO-Mulcher her (Firma, Rechtsform, Sitz, Werk, Importeur für Österreich)? Wo: Messeprofil agraria Halle 21 C50 und Ausstellerseite, Standbetreuung vor Ort, Herstellerseite über Händler-Datenblatt-PDF (z. B. static.landwirt.com/5974/6933265/lw6933265_de.pdf, Gailer-Inserate), Typenschild-Fotos der Inserate, Impressum der Herstellerseite. Danach CRM-Abgleich mit dem Herstellernamen, Fertigungsort (V) und Patentsuche (Google Patents/Espacenet/DEPATISnet) wiederholen. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle zu Hersteller, Sitz, Fertigung (?), Verguss (A). Stichprobe für Jey: ja. Verifikation: 2026-11-25.

## 6. Niederl GmbH Stalltechnik | Halle 23, Stand 410
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Keine eigene Websuche; Toms einziger Treffer ist NIEDERL d.o.o. (Rogasovci, Slowenien) als Partnerkontakt eines Herstellers (S, Wasserbauer-Seite): Abweichung zum Messenamen "GmbH", Zuordnung offen. Händler/Partner wahrscheinlich (E2 bzw. E3 bei Fertigung nur in Slowenien), aber ohne V kein Rot. Bei "Niederl" liefert das Skript nur Wortfragmente, CRM neu.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Existiert eine Niederl GmbH in Österreich (Firmenbuch, evi.gv.at), identisch mit NIEDERL d.o.o. (SI)? Fertigt oder montiert sie selbst Stalltechnik? Wo: Impressum auf stalltechnikshop.at im Browser, Firmenbuch, Messeprofil agraria. Bei Handel/Fertigung nur SI: Rot E2/E3 mit URL. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle zu Sitz, Fertigung (S), Verguss (A, zugekaufte Elektronik). Stichprobe für Jey: ja. Verifikation: 2026-11-25.

## 7. novu.track GmbH | Halle 22, Stand 1140
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität teilweise, Sitz widersprüchlich).** Eigene Prüfung (2 WebSearch): Firmenbuch-Spiegelseite firmenbuchgrundbuch.at führt "novu.track GmbH, FN 311087g", Adresse Grünhüblgasse 1, 8750 Judenburg (S); KSV1870 führt unter "novutrack gmbh" die Adresse Bundesstraße 34, 8740 Zeltweg, Gründung 2008 (S). Widerspruch Judenburg/Zeltweg; Statistik Austria (FSK-Liste) nennt Geschäftsführer Gerhard Hartleb mit Website novutrack.at (S); eine EOC GmbH (Judenburg) hat novu.track als Gesellschafter (S). Firma ist also real und in der Steiermark (Gebiet: Österreich), das ist ein Fortschritt gegenüber Tom (Sitz offen). Produkt/Fertigung weiterhin ohne Beleg: nur FFG-Projektbeschreibung Monitoring/Alarmierung Lebend-Tiertransport mit Sensoren und Datenlogger (S, Zuordnung zur Firma nicht belegt). Produkttyp (Sensor-/Loggermodule, rauer Einsatz): Verguss Mittel (A, Hoch möglich bei Eigenbau). Fertigung DE/AT/NL: Stufe ? (Entwickler/Integrator; Eigenfertigung oder EMS unbekannt); Sitzregel nicht anwendbar (Hardware-Eigenbau ungeklärt). Patente: eigene Suche (1 WebSearch "Zeltweg Judenburg Elektronik Entwicklung Produktion Patent"): keine Patentbezüge, keine Produktionshinweise; Google Patents/Espacenet/DEPATISnet nicht abgefragt, Feld 9 offen. CRM: "novu.track", "novu track", "novutrack": kein Treffer, neu. Wettbewerbereinsatz: kein Hinweis (nur Grep).
- Korrekturen an Toms Feldern: Feld 4/17 ergänzt (Sitz Judenburg laut Firmenbuch-Spiegel, KSV Zeltweg, widersprüchlich; FN 311087g, Website novutrack.at, alles S). Toms "prüfenswert" bleibt vorläufig. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2; Priorität hoch): (a) Welche Adresse ist der aktuelle Sitz (Judenburg oder Zeltweg), Rechtsform und Impressum? Wo: novutrack.at Impressum im Browser, offizieller Firmenbuchauszug FN 311087g. (b) Wird die Tracking-Hardware (Sensoren, Logger, GPS-Tracker) selbst gebaut/montiert und wo? Wo: Produktseiten novutrack.at, Datenblätter, Stellenanzeigen (Montage/Elektronikfertigung), Pressemeldungen. (c) Patente: Google Patents, Espacenet, DEPATISnet mit Anmelder "novu.track GmbH", "novutrack", Gerhard Hartleb als Erfinder, Stichwörter Verguss/Sensor/Gehäuse, Rechtsstand. Bei belegter Eigenfertigung in AT mit Sensor-/Logger-Hardware: Grün erwartbar (Zeile 4). Aktion: nicht kontaktieren bis geklärt.
- Nicht verwendbare Aussagen: Sitz (S, widersprüchlich); Produkt und Fertigung (S/?); Verguss (A). Stichprobe für Jey: ja. Verifikation: 2026-11-25.

## 8. Nufarm GmbH & Co KG | Halle 23, Stand 450
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6; Fertigung nur S, Konzern).** Agrochemie-Werk Linz (Chemiepark), Konzern Nufarm Limited: Stufe V für den Fertigungsort nötig, fehlt. Verguss Niedrig (A) für alle Produkte (Wirkstoffe, Formulierungen, Gebinde). Kein harter Ausschluss (kein Händler: Werk laut Snippets), kein Wettbewerber im Demak-Kerngeschäft. CRM: "Nufarm": kein Treffer, Konzern auch nicht im CRM (kein Konzernbezug). Keine eigene Patentsuche.
- Korrekturen: keine. Toms "unwahrscheinlich" bestätigt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Gibt es Verguss/Klebe/Dichtungsbedarf (z. B. Abfüll-/Verschlusstechnik, Dosieranlagen im Werk)? Erwartung: nein. Wo: Produktseiten nufarm.com/at, Standortseite im Browser. Aktion: nicht kontaktieren, niedrigste Priorität; Rot erst, wenn Jey einen Branchenausschluss einführt.
- Nicht verwendbare Aussagen: Fertigung Linz (S); Größe/Umsatz (S, undatiert); Verguss Niedrig (A). Stichprobe für Jey: nein. Verifikation: 2026-11-25.

## 9. NÖ. Saatbaugenossenschaft | Halle 23, Stand 460
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6).** Saatgut-/Pflanzkartoffelgenossenschaft (Meires/Windigsteig, S). Fertigung/Aufbereitung in AT mittel (S), Verguss Niedrig (A, Saatgut, Verpackung). Kein harter Ausschluss. CRM: "Saatbau", "Niederösterreichische Saatbaugenossenschaft": kein Treffer, neu. Saatbau Linz (andere Genossenschaft) nicht gleichgesetzt.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Betreibt die Genossenschaft eigene Aufbereitungs-/Verpackungs-/Beizanlagen mit Dosier-/Klebe-/Dichtschritten? Erwartung: nein. Wo: Standortseite (Website nicht ermittelt; Messeprofil), Firmenbuch evi.gv.at/f/50827x. Aktion: nicht kontaktieren, niedrigste Priorität.
- Nicht verwendbare Aussagen: Fertigungsort (S), Verguss Niedrig (A). Stichprobe für Jey: nein. Verifikation: 2026-11-25.

## 10. Obereder GmbH | Halle 19, Stand 180
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2).** Händler für Stretchfolien, Rundballennetze, Garne, Schmiergeräte (S, landwirt.com); keine Fertigung belegt, Produkte Niedrig (A). E2 wahrscheinlich, aber nur Snippet, daher kein Rot. CRM: "Obereder": kein Treffer, neu. Identität nur teilweise (Sigharting, Rechtsform aus Messeliste).
- Korrekturen an Toms Feldern: Toms Feld 13 "keiner nötig" bei Gelb ungültig, Auftrag ergänzt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Bestätigt Impressum/Firmenseite reinen Handel (Rot E2) oder gibt es Konfektion/Fertigung (z. B. Netz-/Folienkonfektion) in Sigharting? Wo: Website der Obereder GmbH (nicht ermittelt; Messeprofil, Firmenbuch). Aktion: nicht kontaktieren; bei bestätigtem Handel Rot.
- Nicht verwendbare Aussagen: Händlerstatus und Sitz (S); Verguss Niedrig (A). Stichprobe für Jey: nein. Verifikation: 2026-11-25.

## nicht aufgenommen (bereits bekannt / unklar)
- Moser GmbH (Nr. 2 oben): CRM-Schreibweise "Moser-Glaser AG [DE]" (bekannte_firmen_DE-AT-NL.txt:1647), gefundene Schreibweise "Moser GmbH"/"Moser Solar GmbH" (Ried im Traunkreis, AT). Ähnlicher Name, nach Jey-Entscheidung raus; Einheitengleichheit nicht belegt.
- Keine Verbände/Prüfdienstleister/Forschungseinrichtungen und keine Dosier-/Vergussanlagenbauer (E1) unter den zehn Firmen.

## Einschränkungen
- Nur WebSearch (4 Abfragen, Schwerpunkt NERO und novu.track), Snippets/Kurzfassungen; kein Browser, WebFetch nicht eingesetzt. Keine V-Aussage, keine Zitate gegen Originalseiten geprüft. Alle Ampeln vorläufig, kein Ergebnis mailtauglich.
- Patentrecherche (F5) für ALLE zehn Firmen unvollständig: weder Google Patents noch Espacenet noch DEPATISnet abgefragt, kein Rechtsstand. Eigene Patent-Websuche nur für novu.track und teilweise NERO (Hersteller unbekannt). Nachzuholen im Browser, vorrangig novu.track und NERO.
- Wettbewerbereinsatz (F6): nur Grep auf wettbewerber_referenzen.md, keine Einzelsuchen; Messe-Signal (E1-Wettbewerber auf der Messe) nur von Tom übernommen, nicht wiederholt.
- Nicht auffindbar/offen: monica.farm, NERO (Hersteller), Niederl GmbH Stalltechnik (nur Slowenien d.o.o.), novu.track (Sitz Judenburg vs. Zeltweg), Moser (Einheit).
- Stufe-S-Belege aus Verzeichnissen (WKO, evi.gv.at, KSV, firmenbuchgrundbuch.at, landwirt.com, chemie.de) sind Sekundärquellen und höchstens S.
- Es wurde nichts verschickt und kein CRM-Feld geändert; kein git commit.
