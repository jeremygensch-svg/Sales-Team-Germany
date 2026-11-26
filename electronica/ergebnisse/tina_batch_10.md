# Tina Batch 10 – electronica 2026 (Prüfung von tom_batch_10.md)
Erstellt: 2026-10-15 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe: ausschließlich electronica/ergebnisse/tom_batch_10.md (10 Firmen, Messemodus Regel N).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Nur WebSearch (27 Abfragen, Snippets/Kurzfassungen) und Bash standen zur Verfügung; WebFetch und Chrome nicht. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün ist mailtauglich.
CRM-Abgleich: `python3 crm_abgleich.py` für alle Firmen samt Konzern-/Alt-/Schwesternamen selbst wiederholt (Ergebnis je Firma unten). Tabellenzeile = Zeilennummer der Ampel-Tabelle D. Verifikationsdatum aller Einträge: 2026-10-15.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | Ce-Mat GmbH (C1.601) | GELB | 7 | nein |
| 2 | CEM Test Instruments GmbH (A4.568) | GELB | 5 | ja |
| 3 | Ceptronic GmbH (C3.440) | GELB | 7 | nein |
| 4 | CeramTec GmbH (C2.335) | GELB | 5 | ja |
| 5 | Chip Germany GmbH (C4.458) | GELB | 7 | nein |
| 6 | Chip 1 Exchange GmbH & Co. KG (C4.201) | GELB | 7 | nein |
| 7 | Chroma Germany GmbH (A4.624) | GELB | 5 | ja |
| 8 | CKD Europe B.V. (B1.476) | ROT | 1 | nein |
| 9 | coftech GmbH (B6.139) | GELB | 7 | ja |
| 10 | COLANDIS GmbH (B1.148) | GRÜN (vorläufig) | 4 (Sitzregel) | ja |

Zahlen: Grün 1, Gelb 8, Rot 1.

Patente (Prüfpunkt 8, Regel F5): Espacenet, DEPATISnet und Google Patents mit Anmelderfilter waren nicht abfragbar. Ich habe nur für CeramTec (Google-Patents-Treffer per Websuche, kein CeramTec-GmbH-Anmelder erkennbar; einziger Zufallstreffer "CeramTec AG" betrifft andere Themen), COLANDIS (Firma behauptet Patentschutz FFM-E/FFM-C, keine Nummern gefunden) und CKD (kein CKD-Anmelder unter den Treffern) eine eigene Suche wiederholt. Für die übrigen sieben Firmen keine Wiederholung. Feld 9 bleibt bei ALLEN 10 Firmen ohne Datenbank-Direktabfrage: nicht belastbar, kein Gegenbeweis. Batch nach F5 UNVOLLSTÄNDIG; Nachholen im Browser nötig, bevor das Grün (COLANDIS) final wird.
Wettbewerbereinsatz (F6): `wettbewerber_referenzen.md` per Grep über die ganze Datei (631 Zeilen) auf alle Firmen- und Konzernnamen (CeramTec, COLANDIS, coftech, Everbest/CEM, Chroma, Ceptronic, Chip, Ce-Mat, CKD): kein Treffer; eigene Einzelsuche nur CeramTec (kein Hinweis). Zusatzsignal, keine Wirkung auf die Ampel.
Messe-Signal (N2) per Grep auf electronica/aussteller_namen.txt bestätigt: bdtronic (Z. 70), ELANTAS Europe (168), RAMPF Advanced Polymers (502), RAMPF Production Systems (503), Nordson TEST&INSPECTION (439, Prüftechnik) stellen aus. Keine Wirkung auf die Ampel.

---

## 1. Ce-Mat GmbH | Stand C1.601
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Vertretung/Handel mit Halbleiter-Anlagenteilen (S, SEMI-Profil); E2 inhaltlich naheliegend, aber nur Stufe S, Zeile 1 verlangt V. Fertigung und Verguss Niedrig.
- Eigene Prüfung: Websuche bestätigt nur den indirekten Beleg Bachweg 2, Linsengericht (Companies-House-Officer-Eintrag, Beruf "Managing Director Ce-Mat", S); kein Impressum, keine Website, kein deutscher Registereintrag gefunden. CRM: crm_abgleich.py "Ce-Mat GmbH": zwei ENTHALTEN-Treffer (kundendatenbank_export.txt Z. 25 "thal-technologies", bekannte_firmen Z. 1643 "Momentive Performance Materials GmbH"), beides reine Teilstring-Treffer "performance materials"/"mat", keine Namensgleichheit: neu.
- Korrekturen an Toms Feldern: keine inhaltlichen. Feld 9 fehlt (Patentdatenbanken), Batch-Hinweis oben.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Hat Ce-Mat eigene Fertigung/Bearbeitung (Quarz-/Keramikteile) oder ist es reine Vertretung? Wo nachsehen: Impressum/Website (Domain unbekannt, über SEMI-Profil), Handelsregister Hanau (Gegenstand der Gesellschaft). Bei Bestätigung der Vertretung: Rot nach E2 mit Quelle. Aktion: nicht priorisieren.
- Nicht verwendbare Aussagen: Handels-/Vertretungsstatus (S); Sitz (S); Fertigung Niedrig (S); Verguss Niedrig (A). Stichprobe für Jey: nein. Zitat im Browser bestätigt: nein.

## 2. CEM Test Instruments GmbH | Stand A4.568
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Deutsche Zweigniederlassung der Shenzhen Everbest Machinery Industry (Marke CEM); Fertigung der Gruppe in Shenzhen (S), laut Implisense Unternehmensgegenstand "Vertrieb elektronischer Messgeräte" (S, Handel). Hinweise auf Auslandsfertigung und Vertrieb, aber kein V für E2/E3, daher nicht Rot. Verguss Mittel (A, Messgeräte-Elektronik, Gehäusedichtung).
- Eigene Prüfung: StepStone/Campusjäger: "in Deutschland ansässige Zweigniederlassung des führenden Herstellers" (S), Stellen nur Technischer Vertrieb; Globalsources-Profil: Shenzhen-Fabrik 24.000 m², über 1.000 Mitarbeitende, 32 Produktionslinien (S). Keine Montage-/Lagerstelle in Düsseldorf gefunden. CRM nachgeholt für Konzern: crm_abgleich.py "CEM Test Instruments GmbH", "Shenzhen Everbest", "Everbest": alle neu (Toms Lücke "Konzern nicht abgeglichen" geschlossen). Abgrenzung bestätigt: nicht CEM GmbH Kamp-Lintfort, nicht CEM S.p.A.
- Korrekturen: Feld 12/Konzernabgleich erledigt (neu); Feld 7 Stufe S bleibt. Feld 4 Fertigungsort (Shenzhen) durch Globalsources gestützt (S).
- Nachrecherche-Auftrag (Gelb, Zeile 5): Gibt es in Düsseldorf Montage, Konfektionierung oder Fertigung (Fertigungsbeleg) oder nur Vertrieb? Wo nachsehen: Impressum/Website der GmbH (Domain nicht bestätigt), Handelsregister Düsseldorf (Gegenstand: Vertrieb), Stellenanzeigen Lager/Montage. Bei V-Beleg "nur Vertrieb": Rot nach E2/E3 mit Quelle. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung nur in China (S); Handelsstatus (S); Verguss der Messgeräte (A); Mitarbeiterzahl (S, Gruppe). Stichprobe für Jey: ja (Rot-Kandidat E2/E3).

## 3. Ceptronic GmbH | Stand C3.440
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Beschaffungs-/Handelsmodell laut Verzeichnistext (S: "internationale Beschaffung von Bauelementen", Kooperation mit Distributoren in Asien); keine Fertigung gefunden, Verguss Niedrig. E2 plausibel, nicht V.
- Eigene Prüfung: Suche bestätigt Schondorfer Str. 2, 86926 Greifenberg, gegründet 2012 durch Vater und Sohn Dohrmann (S, supplychainconnect, Firmeneigentext). CRM: "Ceptronic GmbH": neu.
- Korrekturen: keine. Feld 9: Patente nicht gezielt gesucht.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Hat Ceptronic eigene Produkte/Konfektionierung (Gegenstand der Gesellschaft)? Wo nachsehen: Impressum/Website (nicht gefunden), Handelsregister München/Augsburg. Bei Bestätigung Rot nach E2. Aktion: nicht priorisieren.
- Nicht verwendbare Aussagen: Handelsmodell (S, Eigentext); Fertigung Niedrig (S); Verguss Niedrig (A). Stichprobe für Jey: nein.

## 4. CeramTec GmbH | Stand C2.335
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Konzern mit mehreren Werken (Sitzregel greift nicht, Stufe V nötig). Verguss Hoch (A: vollmontierte Ultraschall-/Piezosensoren, Medizin-Inline-Sensoren). Fertigung DE Stufe S, aber die Sensor-/Wandlermontage ist laut Konzernbroschüre den UK-Werken Ruabon und Southampton zugeordnet (S), Lauf a.d. Pegnitz der Piezokeramik (S).
- Eigene Prüfung / Korrektur an Tom: Tom schrieb "ein Standort in Deutschland (Plochingen)". Meine Suche: Broschüre "Messtechnik Sensoren" nennt sechs Standorte, Plochingen = "Headquarter, Production and R&D", Marktredwitz = Substrate/Drucksensorkomponenten, Lauf a.d. Pegnitz = Piezokeramik/Silikat-/Aluminiumoxidkeramik (Bayern), Ruabon/Southampton (UK) = Piezoprodukte und Wandler-/Sensorbaugruppen (S). Pressetext "vertikale Integration bis zur Sensormontage" nennt keinen Ort. Ob Ultraschall-Durchflusssensoren in DE montiert und vergossen werden, ist offen und möglicherweise UK. Stellen: Marktredwitz "Montage von Baugruppen" (Industriemechaniker, S), Lauf Manufacturing Engineering/QS, Plochingen nur Verwaltungsrollen. Ein Gegenbeleg zur Sensorlinie senkt die Firma nicht (Bauteil-Regel); Medizin-/Messtechnikmodule bleiben möglich.
- Patente: breite Google-Patents-Suche (Websuche): ähnliche Sensor-Vergusspatente (EP3814726B1 Ultraschallsensor mit Vergussmasse u. a.) ohne erkennbaren CeramTec-Anmelder; "CeramTec AG" taucht als Altfirma mit anderen Themen auf (Anmelder-Variante zu prüfen). Kein Verguss-Patent von CeramTec belegt. Wettbewerber: kein Hinweis (zwei Suchen). CRM: crm_abgleich.py "CeramTec GmbH", "CeramTec Group", "CeramTec-ETEC": neu.
- Nachrecherche-Auftrag (Gelb, Zeile 5): An welchem deutschen Werk (Plochingen, Lauf, Marktredwitz, Lohmar/ETEC) werden Ultraschall-/Piezosensor-Baugruppen montiert und vergossen/verklebt, oder ausschließlich in Ruabon/Southampton? Wo nachsehen: Broschüre "Messtechnik Sensoren" und Datenblätter Durchflusssensor (Fertigungsort, Schutzart), Standortseiten ceramtec-group.com, Stellenanzeigen Montage/Sensoren je Werk, Patentdatenbanken (Anmelder CeramTec GmbH/AG, Stichwörter Verguss/Klebstoff). Aktion: vorerst Beobachtung; Gebiet ggf. Bayern statt Baden-Württemberg.
- Nicht verwendbare Aussagen: Plochingen als Sensorfertigung (S, widerlegt/offen); Sensorverguss (A); Umsatz/Mitarbeiter (Wikipedia, S, veraltet). Stichprobe für Jey: ja (größte Restunsicherheit, Konzern).

## 5. Chip Germany GmbH | Stand C4.458
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Distributor von Halbleitern/Bauelementen (S, zwei Verzeichnisse), keine Fertigung gefunden, Verguss Niedrig. E2 plausibel, nicht V.
- Eigene Prüfung: Suche bestätigt Kennedystraße 56-58, 63477 Maintal und Website en.chip-germany.com (S); kein Impressum/Register gefunden. CRM: "Chip Germany GmbH": Kern-Name "chip", neu (Name generisch, schwacher Abgleich).
- Korrekturen: keine. Feld 9 nicht gezielt.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Hat Chip Germany eigene Fertigung (Lohnbestückung, Konfektionierung)? Wo nachsehen: Impressum en.chip-germany.com, Handelsregister Hanau. Bei Bestätigung Rot nach E2. Aktion: nicht weiter verfolgen.
- Nicht verwendbare Aussagen: Distributorstatus (S); keine Fertigung (S/?). Stichprobe für Jey: nein.

## 6. Chip 1 Exchange GmbH & Co. KG | Stand C4.201
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Distributor von Auslauf-/Langläuferbauteilen (S: Wikipedia, supplychainconnect); keine Fertigung gefunden, Verguss Niedrig. E2 plausibel, nicht V.
- Eigene Prüfung: LEI-Eintrag bestätigt Amtsgericht Offenbach HRA 40510 und zwei Neu-Isenburger Adressen (Dornhofstraße 65, Martin-Behaim-Straße 10); ein Ranking nennt Fort Worth (Texas) als Hauptsitz (andere Einheit/US-Muttergesellschaft, ungeklärt). CRM: "Chip 1 Exchange", "Chip One Exchange": neu.
- Korrekturen: Feld 17 Zusatz: zwei Adressen laut LEI; Fort-Worth-Angabe als Identitätsfrage Konzern/US-Einheit (S).
- Nachrecherche-Auftrag (Gelb, Zeile 7): Gehört die Neu-Isenburger KG zu einem US-Konzern und gibt es eigene Fertigung (Test/Programmierung zählt nicht)? Wo nachsehen: Impressum chip1.com, Handelsregister Offenbach. Bei Bestätigung Rot nach E2. Aktion: nicht weiter verfolgen.
- Nicht verwendbare Aussagen: Distributorstatus (S); Sekundärquelle Wikipedia (S). Stichprobe für Jey: nein.

## 7. Chroma Germany GmbH | Stand A4.624
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Tochter von Chroma ATE Inc. (Taiwan, Konzern, Hinweis auf Auslandsfertigung). Augsburg: Vertrieb/Service, Stellenanzeige "Service Engineer Test Systems" nennt "in-house system checks, preparation, basic assembly, verification" (S), also etwas Vorbereitung/Montage vor Ort, keine Fertigung belegt. Chroma ATE Europe B.V. (Ede, Morsestraat 32, 1.625 m²) von GlobalSpec als "Manufacturer" klassifiziert (S, Verzeichniseinstufung), Fertigung in Ede nicht belegt. Verguss Mittel (A, Netzteile/Leistungselektronik).
- Korrekturen an Toms Feld 4/7: Augsburg nicht nur "Vertrieb", sondern auch Service mit Grundmontage (S); Ede ist offen (NL zählt zur Zielregion). Konzernabgleich: crm_abgleich.py "Chroma Germany GmbH", "Chroma ATE Europe", "Chroma ATE": neu. Patente nicht wiederholt.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Werden in Ede (NL) oder Augsburg Geräte (Stromversorgungen, Testsysteme) montiert/gefertigt? Wo nachsehen: Impressum Chroma Germany und Chroma ATE Europe (chromaate.com/eu), Handelsregister (KvK Ede), Stellenanzeigen Ede (Production/Assembly), Standortseite. Aktion: nicht kontaktieren; falls Ede fertigt, eigene Prüfung der Einheit Chroma ATE Europe B.V.
- Nicht verwendbare Aussagen: Vertriebsstandort Augsburg als alleinige Funktion (S); Fertigung nur Taiwan (?, nicht belegt); Ede-Fertigung (S/?). Stichprobe für Jey: ja.

## 8. CKD Europe B.V. | Stand B1.476 | BEKANNT
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT (Tabellenzeile 1, E5).** Rot, weil: dieselbe Einheit steht im CRM, bekannte_firmen_DE-AT-NL.txt Zeile 415 "CKD Europe BV Germany Office [DE]" (Bestandskontakt pflegen, kein Neukunde). Zusätzlich Fertigung der Gruppe in Japan/Malaysia (S, Zeile 4 wäre ohnehin Gelb, E3 nicht V).
- Eigene Prüfung: crm_abgleich.py "CKD Europe B.V.": PRAEFIX auf Z. 415, "CKD Corporation": neu (Konzern nicht im CRM). Silicon-Saxony-Mitgliedseintrag "CKD Europe B.V. Germany Office", Heisenbergbogen 2, 85609 (S) stützt Einheitengleichheit (Aschheim); die Sitz-Gesellschaft der B.V. in NL ist unbelegt. Patente: eine Suche (CKD, Spulenverguss): kein CKD-Anmelder unter den Treffern.
- Korrekturen: keine. Einzige Restfrage für Jey: ist der CRM-Eintrag "Germany Office" dieselbe Einheit wie die ausstellende B.V.? Dann bleibt Rot; sonst Gelb (Zeile 3) "Einheit klären".
- Nachrecherche-Auftrag: keiner (Rot). Aktion: Bestandskontakt pflegen.
- Nicht verwendbare Aussagen: Produktion Japan/Malaysia (S); Sitz B.V. (unbelegt). Stichprobe für Jey: nein.

## 9. coftech GmbH | Stand B6.139
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Tom fand kein Produkt. Mit weiteren Suchen: Cylex-Verzeichniseintrag (Eigentext, S): "international ausgerichtetes Handelshaus und professionelles Serviceunternehmen" für elektronische Bauelemente (Quarze, SAW-Filter, Duplexer, Keramikfilter, Antennen), Rohstoffe und Metalle (Ferrolegierungen). Das trägt E2 stark, ist aber nur S. Fertigung Niedrig (S), Verguss Niedrig (A).
- Eigene Prüfung: LEI-Eintrag bestätigt Coftech GmbH, Heinrich-Held-Str. 33, 45133 Essen, Amtsgericht Essen HRB 14382 (S); unter derselben Adresse führt ein Verzeichnis die Arnold Jäger Holding GmbH (Kunststoffe), nicht mit coftech vermischen. Keine eigene Website gefunden. CRM: "coftech GmbH": neu.
- Korrekturen an Toms Feldern: Feld 6/8: Produkt/Geschäftsfeld nun mit Stufe S belegt (Handelshaus Bauelemente/Rohstoffe); Feld 2 "nicht bestimmbar" -> keiner (Handel). Tom-Hinweis "Halle B6 = Displays" nicht verwenden.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Hat coftech eigene Fertigung oder Produkte (Gegenstand der Gesellschaft)? Wo nachsehen: Handelsregister Essen HRB 14382, Impressum/Website (nicht gefunden), Ausstellerprofil exhibitors.electronica.de (Halle B6.139). Bei Bestätigung "nur Handel": Rot nach E2 mit Quelle. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Handelshaus (S, Eigentext Cylex); Zugehörigkeit zu Display-Segment (Hallenhinweis, kein Beleg); Fertigung (S/?). Stichprobe für Jey: ja (Rot-Kandidat E2, nur Bestätigung).

## 10. COLANDIS GmbH | Stand B1.148
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN, vorläufig (Tabellenzeile 4, Sitzregel).** Eigenhersteller von Fan-Filter-Modulen mit einem erkennbaren Standort Kahla (eigene Produkte, kein Händler, kein Konzernhinweis, keine Auslagerungshinweise). Firmenpräsentation (S): "550 m² Produktionsfläche ISO 7, Reinräume ISO 5/ISO 1, alle Teile gereinigt, unter Reinraumbedingungen montiert und getestet"; 10.000. FFM 2019 (S). Verguss Mittel (A: Lüfter-/Regelelektronik, Filterrahmen-Dichtung/-Verklebung, Wärmetauschermodul mit Regeleinheit); kein Eigenverguss belegt. Grün nur A/S, nicht mailtauglich.
- Eigene Prüfung: Schreibweise der Straße: Fraunhofer-Snippet (Tom) "Im Carnisch 34", Firmenprofil und Seiten "Im Camisch 34", 07768 Kahla; vermutlich OCR-/Schreibfehler, im Impressum lesen (Feld 17). Implisense: Handelsregister Jena (laut Profil, S). Firma nennt "patentierte" FFM-E/FFM-C-Module, keine Nummern (DPMA/Espacenet offen). Wettbewerber: kein Hinweis (Listenabgleich, DOPAG-Filterfall Tecnofil ohne Bezug). CRM: "COLANDIS GmbH": neu.
- Korrekturen an Toms Feldern: Feld 7 Stufe A (Sitzregel) bestätigt; Zusatz: Produktionsfläche mit Montage am Sitz ist S-Beleg (Firmenpräsentation, undatiert) und stützt die Sitzregel. Feld 10 "prüfenswert" bleibt (Verguss Mittel).
- Nachrecherche (für Mailstufe, kein Gelb): (a) Impressum/Standort colandis.com, Stellenanzeigen Montage Kahla (V für Fertigungsort); (b) Datenblatt FFM-C/-E: Dichtung (PU/Klebung), Lüfter-/Regelelektronik vergossen? Schutzart; (c) Patent-/Schutzrechtsnummern (DPMA/Espacenet/EUIPO, Rechtsstand).
- Nicht verwendbare Aussagen: Fertigung/Montage Kahla (A/S, undatierte Präsentation); Verguss aller Bauteile (A); "patentiert" (S, Eigenaussage); Mitarbeiterzahl >30 (S, alt). Stichprobe für Jey: ja (Grün ohne V-Beleg).

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind durchweg korrekt als S/A gesetzt, keine V vorgetäuscht. Tom-Einstufungen "kein Fertiger" bei Ce-Mat, CEM, Ceptronic, Chip, Chip 1, Chroma, CKD sind plausibel, aber nur bei CKD durch einen Beleg (CRM) hart; die übrigen bleiben Gelb mit Auftrag.
- Korrigiert gegenüber Tom: CeramTec (mehrere deutsche Werke, Sensormontage vermutlich UK), coftech (Produkt/Handelshaus gefunden), Chroma (Augsburg mit Service-Grundmontage; Ede offen), CEM (Konzern-CRM-Abgleich nachgeholt), COLANDIS (Straßenschreibung).
- Vorschlag Fehlerlog (Jey gibt frei, nicht eingetragen): Verzeichnis-Straßennamen aus Snippets (OCR) gegen Herstellerseite gegenlesen; bei Konzernen mit Werken in DE und UK die montierende Einheit je Produktlinie bestimmen (CeramTec).

## Einschränkungen
- Browser und WebFetch nicht verfügbar: kein Impressum, kein Datenblatt, keine Quelle gelesen; alle Aussagen Stufe S oder A. Kein "Zitat im Browser bestätigt: ja".
- WebSearch: 27 Abfragen (Identität/Fertigung je Firma, Patent-Zusatzsuchen CeramTec/COLANDIS/CKD, Wettbewerber CeramTec, Konzern Everbest/Chroma). Ergebnisse sind Kurzfassungen und Verzeichniseinträge.
- Patente F5: Pflichtsuche in Espacenet/DEPATISnet/Google Patents (Anmelderfilter) bei keiner Firma erfüllt; Batch UNVOLLSTÄNDIG. Anmelder-Varianten offen: CeramTec AG/ETEC/Morgan, CKD Kabushiki Kaisha/シーケーディ, Chroma ATE Inc., Shenzhen Everbest, COLANDIS (DPMA).
- Wettbewerbereinsatz F6: Listenabgleich vollständig (ganze Datei), Einzelsuche nur CeramTec.
- Handelsregister/Unternehmensregister nicht abgerufen. Kundendatenbank (Excel) nicht lesbar; kundendatenbank_export.txt ohne Treffer außer dem Ce-Mat-Teilstring.
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
