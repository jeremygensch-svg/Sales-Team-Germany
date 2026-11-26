# Tina Batch 49 – electronica 2026 (Prüfung von tom_batch_49.md)
Erstellt: 2026-10-21 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe: ausschließlich electronica/ergebnisse/tom_batch_49.md (10 Firmen).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (21 Abfragen, Kurzfassungen/Snippets) und Bash zur Verfügung; WebFetch und Chrome nicht nutzbar. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün, nichts mailtauglich.
CRM: `python3 crm_abgleich.py` für alle Firmen samt Konzern-, Partner- und Schreibvarianten selbst wiederholt. Tabellenzeile = Zeilennummer der Ampel-Tabelle D. Verifikationsdatum aller Einträge: 2026-10-21.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | Walter Schneider GmbH (B3.429) | GELB | 6 | nein |
| 2 | Schneider & Gemsa GmbH (B2.278) | GELB | 5 | ja |
| 3 | SCHROEDER + BAUER Werkzeugbau Stanztechnik GmbH + Co. KG (B2.471) | GELB | 5 | nein |
| 4 | Schützinger GmbH (A4.526) | GELB | 5 | ja |
| 5 | Schukat electronic Vertriebs GmbH (C6.550) | GELB | 7 (Rot-Kandidat E2) | nein |
| 6 | Schulz-Electronic GmbH (A5.214) | GELB | 5 (Rot-Kandidat E2) | ja |
| 7 | Schweizer Electronic AG (A2.207) | GELB | 5 | ja |
| 8 | scia Systems GmbH (B1.909) | GELB | 3 | ja |
| 9 | SCREEN SPE Germany GmbH (B1.700) | GELB | 7 (Rot-Kandidat E2) | nein |
| 10 | SEGGER Microcontroller GmbH (C5.120) | GELB | 5 | nein |

Zahlen: Grün 0, Gelb 10, Rot 0.

Wichtigster Befund gegenüber Tom: **scia Systems** hat einen CRM-Konzernbezug, den Tom übersehen hat (Regel M): scia wurde 2013 "in partnership with VON ARDENNE GmbH" gegründet (S), und "Von Ardenne" / "VON ARDENNE GmbH" stehen im CRM (bekannte_firmen_DE-AT-NL.txt Zeilen 2516, 2517, beide [DE]). Toms Argument "VON ARDENNE nicht gesondert gesucht" war ein Anmelder-Hinweis, der CRM-Abgleich dieser Variante fehlte. Ebenso Zollner Elektronik AG (Partner von Schweizer) steht im CRM (Zeilen 2659 bis 2662); das ist ein Partner, kein belegter Konzern, aber Jey sollte es wissen.

Patente (F5): Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Eigene Zusatzsuchen per WebSearch (Anmelder + Stichwort) für Schützinger, Schweizer, SEGGER, Schulz-Electronic: keine Patentdatensätze der Firma mit Vergussbezug. Für die übrigen sechs Firmen keine eigene Wiederholung (Budget). Feld 9 ist bei ALLEN 10 Firmen ohne Direktabfrage der Datenbanken: nicht belastbar, kein Gegenbeweis; der Batch ist nach F5 UNVOLLSTÄNDIG, Nachholen im Browser nötig, bevor irgendein Grün final wird.

Wettbewerbereinsatz (F6): Toms Abgleich mit wettbewerber_referenzen.md (Teil 1 von mir bis Zeile 378 gelesen, Rest per Grep nicht auf diese Firmen geprüft) bleibt unwidersprochen; Schweizer/Zollner: Zollner steht dort nur als DELO-Testimonial (laut Tom), betrifft den Partner, nicht Schweizer. Kein Einfluss auf die Ampel.

---

## 1. Walter Schneider GmbH | Stand B3.429
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6).** Fertigung Remchingen Hoch (Sitzregel A; Stellenanzeige Presserei am Sitz, S), aber Kaltfließpressteile 2 bis 250 g aus Stahl sind massive Metallteile: alle plausiblen Bauteile Niedrig (A). Tom: unwahrscheinlich, bestätigt.
- Eigene Prüfung: Techpilot-Profil/Broschüre/Arbeitsagentur-Anzeige (S) bestätigen Remchingen, Gründung 1954, ca. 88 Beschäftigte, Geschäftsführung Siegle/Neumeyer. Keine Hinweise auf Montage, Dichtung oder Verklebung. Gleichnamige Firma Walter Schneider GmbH & Co. KG (Kreuztal/Siegen, Autohändler) ist eine andere Firma; Impressum der Remchinger Firma nicht gefunden.
- CRM: crm_abgleich.py "Walter Schneider GmbH", "Schneider Umformtechnik": nur Wortwurzel "Walter Kraus GmbH" (2534) und "Schneider Electric" (2111), andere Firmen. Neu. Zitat im Browser bestätigt: nein.
- Korrekturen an Toms Feldern: keine.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Enthalten Kundenbaugruppen mit Dichtungs-/Klebe-/Dosierschritten die Presseteile (z. B. Montage von Presse- plus Kunststoffteilen)? Wo nachsehen: schneider-umformen.de (Produkte, Leistungen, Impressum). Aktion: zurückstellen.
- Nicht verwendbare Aussagen: Fertigung Remchingen (S/A); Verguss Niedrig (A); Mitarbeiterzahl (S). Stichprobe für Jey: nein.

## 2. Schneider & Gemsa GmbH | Stand B2.278
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Auftragsfertiger mit Standorten in Iffezheim, Tschechien und Moldau/Rumänien (Techpilot-Profil: DE/CZ/RO; StepStone 2026: DE/CZ/Moldau, ca. 300 Mitarbeitende; S). Sitzregel greift nicht (Auftragsfertiger, Auslandswerke), Stufe V für den Fertigungsort fehlt. Verguss Hoch (A: Ladestationen, Kabelkonfektion mit Steckern), Pumpenelektronik/Baugruppen Mittel (A).
- Eigene Prüfung: Meine Suche bestätigt Gründung 1987, "industrial contract manufacturing", Kompetenzen Elektro-Ladestationen, Kabelbäume, Prüfkabelsätze, Motoranschlusskabel, elektromechanische Baugruppen (Techpilot, S). Eigene Website/Impressum nicht gefunden. In der Stellenanzeigen-Suche nur ein Controller-Posten, keine Produktions-/Vergussstelle. Kein harter Ausschluss (Auftragsfertiger mit Fertigung am Sitz ist plausibel, kein E2/E3 belegt).
- CRM: neu (nur Wortwurzel "Schneider Electric" 2111, andere Firma). Zitat im Browser bestätigt: nein.
- Korrekturen an Toms Feldern: keine. Hinweis: Auslandsstandorte widersprüchlich (Rumänien vs. Moldau), von Tom bereits genannt.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Werden Ladestationen und Kabelsätze in Iffezheim gefertigt, und wird dort vergossen/überspritzt/verklebt? Wo nachsehen: Firmenwebsite (Leistungen, Standorte, Produktzuordnung zu Werken), Impressum/Handelsregister Mannheim bzw. Baden-Baden, Stellenanzeigen Iffezheim (Montage, Vergießen, Elektronikfertigung). Aktion: erst nach Klärung weiter; bei Beleg Grün-Kandidat (Zeile 4).
- Nicht verwendbare Aussagen: Fertigung Iffezheim (S); Verguss aller Bauteile (A); Standorte Ausland (S, widersprüchlich); Mitarbeiterzahl (S). Stichprobe für Jey: ja (aussichtsreichste Firma im Batch, aber nur S/A).

## 3. SCHROEDER + BAUER Werkzeugbau Stanztechnik GmbH + Co. KG | Stand B2.471
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Stanzteil- und Werkzeughersteller mit Baugruppenmontage (Automotive-Elektrik/Elektronik), Pforzheimer Straße 37, 75245 Neulingen-Bauschlott (Ausbildungs-/Stellenanzeigen, S). Verguss Mittel (A, Baugruppen), Stanzbiegeteile/Werkzeuge Niedrig. Fertigung am Sitz plausibel, aber Holding-/Auftragsfertigerhinweis, daher Stufe V nötig.
- Eigene Prüfung: Meine Suche bestätigt "Stanz-Biegeteile und komplette Baugruppen" (S) und Ausbildung zum Stanz- und Umformmechaniker "Herstellung von Stanzbiegeteilen und Montage kompletter Baugruppen". Zugehörigkeit zur SUBA Holding ("fünf Standorte um Pforzheim", über 350 Mitarbeitende, S) NICHT belegt, die Stellenanzeigen nennen SUBA als Arbeitgeber; ein Patent-Analyseportal führt die Firma mit Sachsen-Anhalt als Sitz (Sekundärquelle, widerspricht den Anzeigen, vermutlich Datenfehler). Kein Hinweis auf Umspritzung/Kunststoff.
- CRM: crm_abgleich.py "SCHROEDER + BAUER ...", "Schroeder Bauer", "SUBA Holding": kein Treffer, neu. Zitat im Browser bestätigt: nein.
- Korrekturen an Toms Feldern: Feld 4: Holding-Zugehörigkeit ist nicht belegt, nur aus einer Stellenanzeige; Feld 17: Sitz-Widerspruch Patsnap (Sachsen-Anhalt) ergänzt.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Welche Baugruppen werden gefertigt, mit Umspritzung/Verklebung/Dichtung, und in welchem Werk? (b) Wie viele Werke hat SUBA, und in welchem Werk liegt die Baugruppenmontage? Wo nachsehen: schroeder-bauer.com (Leistungen, Baugruppen), suba-holding Seite, Impressum/Handelsregister Mosbach/Pforzheim, Stellenanzeige "Schroeder_Bauer_Stelle_0826" (wirtschaftskraft.de). Aktion: nicht kontaktieren, bis Baugruppeninhalt belegt ist.
- Nicht verwendbare Aussagen: Fertigung Neulingen (S); Baugruppen-Verguss (A); Holding-Zugehörigkeit (S); Größe unbekannt. Stichprobe für Jey: nein.

## 4. Schützinger GmbH | Stand A4.526
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Stuttgarter Familienunternehmen (gegr. 1951, ca. 3.000 Produkte, Eichwiesenring 6, 70567 Stuttgart laut Katalog, S). Fertigungsort offen: Händlerseiten nennen "Fertigungsprozesse in den Werken" (ISO 9001/13485), Farnell (laut Tom) "Fertigung durch spezialisierte Zulieferer". Verguss Hoch (A: Messleitungen mit Steckern/Überspritzung), Prüfspitzen und Steckverbinder Mittel (A).
- Eigene Prüfung: Meine Suchen (Fertigung Made in Germany; Stellenangebote Stuttgart; Patente) ergeben: keine Aussage zum Fertigungsort, keine Schützinger-Stellenanzeige für Produktion/Montage, kein Patent der Firma (einziger Patenttreffer EP0594937 gehört der anderen Stuttgarter Firma Contact GmbH). Medizintechnik-Steckverbinder (ISO 13485) stützen Verguss/Kleben, kleine Mengen zählen (Regel D). Kein Ausschluss belegt.
- CRM: neu (Schützinger / Schuetzinger / Schutzinger: kein Treffer). Zitat im Browser bestätigt: nein.
- Korrekturen an Toms Feldern: Feld 9 Zusatz: Anmelder-Schreibweisen Schützinger/Schuetzinger/Schutzinger in meiner Suche abgedeckt, ohne Treffer, weiter nicht belastbar. Adresse in Feld 4/17 ergänzt (Eichwiesenring 6, S).
- Nachrecherche-Auftrag (Gelb, Zeile 5): Wo werden Messleitungen, Prüfspitzen und Steckverbinder gefertigt/konfektioniert (Stuttgart eigenes Werk oder Zulieferer, Ort)? Wo nachsehen: Schützinger-Website (Über uns, Qualität "Werke"), Impressum, Produktdatenblätter ("Made in ..."), Stellenanzeigen Stuttgart (Montage/Konfektion/Spritzguss), ISO-Zertifikate (Standortangabe). Aktion: erst nach Fertigungsbeleg weiter.
- Nicht verwendbare Aussagen: Fertigung in Stuttgart (S/?); "Werke" ohne Ortsangabe (S); Verguss/Umspritzung (A); Zuliefererhinweis (S, Händlerseite, nicht gelesen). Stichprobe für Jey: ja.

## 5. Schukat electronic Vertriebs GmbH | Stand C6.550
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Distributor (Katalogdistributor und Franchise-Partner für u. a. Mean Well, Panasonic, Microchip, LiteOn; Großhandel, S), Hans-Georg-Schukat-Straße 2, 40789 Monheim, GF Yana Radzivil (Verzeichnis, S). E2 ist inhaltlich stark, aber nur Snippet, Zeile 1 verlangt Stufe V, daher Gelb statt Rot.
- Eigene Prüfung: Zwei Verzeichnisse und ein Branchenkompass nennen "wholesale and retail of electronic articles"; keine Eigenfertigung genannt. Impressum schukat.com nicht erreicht.
- CRM: neu (Schukat: kein Treffer). Zitat im Browser bestätigt: nein. Korrekturen an Toms Feldern: keine.
- Nachrecherche-Auftrag (Gelb, Zeile 7): E2 mit Stufe V belegen: Impressum/"Über uns" von schukat.com und Handelsregister (Unternehmensgegenstand "Großhandel") lesen. Bei Bestätigung Rot nach E2 mit Quelle. Aktion: nicht bearbeiten.
- Nicht verwendbare Aussagen: "Distributor ohne Fertigung" (S); Mitarbeiterzahl (S). Stichprobe für Jey: nein.

## 6. Schulz-Electronic GmbH | Stand A5.214
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Stromversorgungen: Vertriebspartner und autorisierter Servicestützpunkt zahlreicher Hersteller ("Quasihersteller"), Vertrieb der Regatron-Stromversorgungssparte, Marken TDK-Lambda und Delta Elektronika (S); daneben "maßgeschneiderte, programmierbare Stromversorgungen" und Entwicklung/Aufbau kompletter Prüfeinrichtungen (S). Eigenfertigung ungeklärt; Verguss Mittel (A, nur bei Eigenmontage).
- Eigene Prüfung: Dr.-Rudolf-Eberle-Straße 2, 76534 Baden-Baden/Steinbach, ca. 45 Mitarbeitende, 1975 (Verzeichnis, S). Die Azubianzeigen beschreiben Montage und Anschluss elektrischer Geräte (Geräteanpassung), aber keine Serienfertigung. Kein V-Beleg für E2 (Händler), daher nicht Rot. Meine Patent-Zusatzsuche: keine Treffer.
- CRM: neu. Zitat im Browser bestätigt: nein. Korrekturen an Toms Feldern: Tom führt "unwahrscheinlich" bei Fertigung Niedrig; nach Tabelle ist Fertigung S nicht Niedrig belegt, daher Zeile 5 mit Auftrag.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Baut Schulz-Electronic Geräte selbst (Montage/Anpassung/Verguss programmierbarer Netzteile, Prüfeinrichtungen) oder nur Vertrieb/Service? Wo nachsehen: schulz-electronic.de (Über uns, Leistungen, Eigenentwicklungen), Impressum, Stellenanzeigen (Montage/Fertigung Baden-Baden). Bei reinem Vertrieb Rot nach E2 mit Quelle. Aktion: zurückstellen.
- Nicht verwendbare Aussagen: Eigenfertigung (S/?); Verguss (A); Mitarbeiterzahl (S, evtl. veraltet). Stichprobe für Jey: ja (E2-Rot-Kandidat).

## 7. Schweizer Electronic AG | Stand A2.207
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Börsennotierte AG, Schramberg (Einsteinstraße 10), Leiterplatten und p² Pack Chip-Embedding; Auslandsfertigung (Jintan, China, mit Partner WUS) und viel Partnerware (2025: Eigenfertigung 55,9 Mio. EUR, Partnerprodukte 117,2 Mio. EUR, laut Tom, S). Fertigung Schramberg Mittel/S, Stufe V nötig. Verguss: Leiterplatten Niedrig (A, Block C), p² Pack Mittel bis Niedrig (Laminierung statt Verguss). Gesamt aktuell Niedrig bis Mittel, Zeile 6 käme erst nach belegter Fertigung.
- Eigene Prüfung: Meine Suche zu p² Pack bestätigt Schramberg und den Prozessablauf (Leadframe, Die-Attach, Embedding im PCB-Kern, Laminieren, Laserbohren; 2019-Präsentation, S) ohne Verguss. Zollner-Partnerschaft Juni 2024 (Design-in, Zandt) bestätigt (S). Patent-Zusatzsuche: kein Anmelder-Treffer der Firma mit Verguss; die von Tom genannte Embedding-Anmeldung 2007 ist Laminat-Einbettung (Rechtsstand weiter ungeprüft).
- CRM: Schweizer Electronic AG: neu. **Zollner Elektronik AG steht im CRM** (bekannte_firmen Zeile 2661; ferner 2659 "Zollner", 2660 "Zollner Electronik AG", 2662 "Zollner GmbH & Co. KG", alle [DE]); Zollner ist Partner, kein belegter Eigentümer oder Konzern von Schweizer (Zeile 3 daher nicht ausgelöst). Zitat im Browser bestätigt: nein.
- Korrekturen an Toms Feldern: Feld 12 Zusatz: Partner Zollner im CRM (Tom: nicht abgeglichen).
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Welche Produkte werden in Schramberg gefertigt, und enthält der p² Pack-Modulaufbau Verguss/Glob-Top/Dam&Fill? Wo nachsehen: Produktseite und Datenblatt p² Pack, Geschäftsbericht 2025 (Standort- und Segmentangaben), Impressum schweizer.ag. (b) Jey: Bedeutet der Zollner-Bezug im CRM etwas für die Ansprache (Partner, kein Konzern)? Aktion: zurückstellen.
- Nicht verwendbare Aussagen: Fertigung Schramberg (S); Verguss/Embedding-Aufbau (A); Umsatzaufteilung (S, Pressemeldung nicht gelesen); Patentstatus (ungeprüft). Stichprobe für Jey: ja.

## 8. scia Systems GmbH | Stand B1.909
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 3, CRM-Konzernbezug).** Hersteller von Ionenstrahl-/Plasma-Prozessanlagen, Chemnitz (HRB 27983 Amtsgericht Chemnitz, Stammkapital 200.401 EUR, S), gegründet 2013 "in partnership with VON ARDENNE GmbH", Dresden (S, SEMI-Profil). "VON ARDENNE" (Zeile 2516) und "VON ARDENNE GmbH" (2517) stehen im CRM. Die Beteiligungsquote ist nicht belegt; ob scia zur Gruppe gehört, ist offen (Regel M).
- Eigene Prüfung: Adresse in Quellen widersprüchlich: Annaberger Straße 240, 09125 Chemnitz (Verzeichnisse/Listen) gegen Clemens-Winkler-Str. 6c, 09116 (Messeliste); Mitarbeiterzahl 54 bis ca. 200 (S, widersprüchlich). Meine Suche: Eigenfertigung (Kernkomponenten, Systemdesign, Software, Service) laut Verzeichnis (S). Verguss Niedrig (A), unter Zeile 3 aber unerheblich.
- Korrekturen an Toms Feldern: Feld 12 von "neu" auf "CRM-Konzernbezug: VON ARDENNE (Zeilen 2516/2517), Einheit klären". Feld 17 ergänzt: Handelsregister HRB 27983 (S). Tom erwähnte VON ARDENNE nur als Patent-Anmelder-Variante. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 3): Jey: Ist die CRM-Einheit "VON ARDENNE GmbH" (Dresden) Gesellschafterin/Muttergesellschaft der scia Systems GmbH, und gilt der Bestandskontakt auch für scia? Wo nachsehen: CRM-Datensatz (Adresse, Ansprechpartner), Gesellschafterliste/Handelsregister Chemnitz HRB 27983 (Unternehmensregister), Impressum scia-systems.com. Hinweis: Auch bei Rot-Klärung (E5) wäre nur Konzernbezug mit Einheitenfrage betroffen; Verguss Niedrig spricht ohnehin gegen Priorität.
- Nicht verwendbare Aussagen: Beteiligung VON ARDENNE (nicht belegt); Sitzadresse (widersprüchlich); Verguss Niedrig (A); Mitarbeiterzahl (S). Stichprobe für Jey: ja (CRM-Konzernbezug, Tom hat ihn übersehen).

## 9. SCREEN SPE Germany GmbH | Stand B1.700
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Vertriebs-/Engineering-/Servicegesellschaft EMEA der SCREEN Semiconductor Solutions (Kyoto), Ismaning (Fraunhoferstraße 7), früher Dainippon Screen (Deutschland) GmbH, Düsseldorf (Japanischer Wertpapierbericht und North Data, S). Anlagen werden in Japan gebaut (laut Tom, S); E2 nicht mit Stufe V belegt, daher Gelb statt Rot.
- Eigene Prüfung: Gesellschaft von SCREEN Holdings bestätigt als Konzernunternehmen (S). Die Altnamen "Dainippon Screen" und "SCREEN Holdings" im CRM: kein Treffer (Rerun). Verguss Niedrig (A).
- CRM: neu. Zitat im Browser bestätigt: nein. Korrekturen an Toms Feldern: Feld 17 Zusatz: Vorgängername Dainippon Screen (Deutschland) GmbH (S).
- Nachrecherche-Auftrag (Gelb, Zeile 7): E2/E3 mit Stufe V belegen: Firmenseite screen-spe.com/eu/company und Impressum lesen (Vertrieb/Service, keine Fertigung in DE), Handelsregister München. Aktion: nicht bearbeiten.
- Nicht verwendbare Aussagen: "Vertriebs-/Servicegesellschaft" (S); Refurbishment Neufahrn (S); Mitarbeiterzahl (S). Stichprobe für Jey: nein.

## 10. SEGGER Microcontroller GmbH | Stand C5.120
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Software- und Debug-Tool-Hersteller, Ecolab-Allee 5, 40789 Monheim; Slogan "Designed and made in Germany" (SEGGER-Produktseite, S), Hardware-Fertigungsort und -umfang (J-Link, Flasher) nicht belegt. Verguss Niedrig (A, Kunststoffgehäuse-Elektronik).
- Eigene Prüfung: Wikipedia (Sekundärquelle, nur S): "developed, maintained and updated in Germany"; Presse: J-Link Ultra 2026 in neuem Kompaktgehäuse (S). Meine Patentsuche (Anmelder + Gehäuse/Vergussmasse): keine Patentdatensätze mit Vergussbezug. Rechtsform in Verzeichnissen teils "GmbH & Co. KG" (Abweichung).
- CRM: neu (SEGGER, SEGGER Microcontroller Systems: kein Treffer). Zitat im Browser bestätigt: nein.
- Korrekturen an Toms Feldern: keine; Tom: "E2 (Software) erwägen" ist nicht V-belegt, also nicht Rot.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Werden J-Link-/Flasher-Geräte in Monheim gefertigt oder bei einem Lohnfertiger, und gibt es Verguss/Verklebung der Elektronik? Wo nachsehen: segger.com/about (Production), Impressum (Rechtsform), Produktdatenblätter ("Made in"), Stellenanzeigen Monheim (Produktion, Montage). Aktion: nicht bearbeiten (Verguss voraussichtlich Niedrig).
- Nicht verwendbare Aussagen: Fertigung Monheim (S); "Designed and made in Germany" (S, Marketing); Wikipedia-Aussagen (S, Sekundärquelle). Stichprobe für Jey: nein.

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind durchgehend korrekt niedrig angesetzt (keine V vorgetäuscht). Seine Einstufungen bleiben nach Tabelle D alle Gelb, weil die Fertigungs-/Identitäts-/Konzernbelege (V) fehlen; kein Grün mangels V bei Auftragsfertiger/AG/Holding und weil Sitzregel nur A erlaubt, wo kein Auslands- oder Zulieferhinweis steht.
- Fehler bei Tom: scia/VON ARDENNE (Regel M) und Zollner (Partner Schweizer) nicht im CRM abgeglichen. Vorschlag Fehlerlog (Jey gibt frei, nicht eingetragen): "Gründungspartner und Kooperationspartner aus der Firmenbeschreibung mit crm_abgleich.py prüfen, nicht nur als Patent-Anmelder-Variante nennen."
- Rot ist bei keiner Firma gesetzt: Schukat, Schulz-Electronic und SCREEN sind E2-Kandidaten, aber ohne Stufe V.

## Einschränkungen
- Browser und WebFetch nicht verfügbar: kein Gegenlesen nach Abschnitt H, kein Impressum, kein Datenblatt gelesen; alle Aussagen Stufe S oder A. Keine "Zitat im Browser bestätigt: ja".
- WebSearch: 21 Abfragen (Identität/Fertigung aller zehn Firmen; Zusatzsuchen: scia/VON ARDENNE, Schützinger Patent und Stellen, Schneider & Gemsa Stellen, SUBA Holding, Schweizer/Zollner, Schweizer Patent, Schulz-Electronic Patent/Vertrieb, SEGGER Patent). Ergebnisse sind Kurzfassungen und Verzeichnisse.
- Patente: Google Patents, Espacenet, DEPATISnet nicht direkt abgefragt; F5 nicht erfüllt (alle 10). Für Walter Schneider, Schneider & Gemsa, Schroeder + Bauer, Schukat, scia, SCREEN keine eigene Wiederholung. Rechtsstand entfällt mangels Treffer, Schweizer-Anmeldung 2007 ungeprüft. Nachzuholen: SUBA, VON ARDENNE, SCREEN Holdings, SEGGER Microcontroller Systems, enge Suche (potting compound OR Vergussmasse).
- Wettbewerbereinsatz (F6): nur Listenabgleich (wettbewerber_referenzen.md bis Zeile 378 gelesen, Rest 253 Zeilen nicht); keine Einzelsuchen von mir.
- Handelsregister/Unternehmensregister nicht abgerufen. Kundendatenbank (Excel) nicht lesbar; kundendatenbank_export.txt über crm_abgleich.py geprüft, ohne Treffer für alle zehn.
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
