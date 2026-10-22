# electronica 2026 – Browser-Prüfliste für die Grün-Kandidaten

Stand 2026-10-22. Zweck: Die 46 Grün-Ampeln aus dem Tom/Tina-Lauf sind nur vorläufig (Sitzregel + Produkttyp, Stufe A/S). Diese Liste ist für einen Lauf mit Browser (Claude Code lokal mit Chrome-Erweiterung) gedacht.

## Startanweisung für den lokalen Claude

1. Lies `regeln_tom_tina.md` (Belegstufen V/A/S/?, Ampel-Tabelle D, Sitzregel, Bauteil-Regel, harte Ausschlüsse E1–E5, Pflicht F5 Patentrecherche, F6 Wettbewerbereinsatz), `efx_verguss_wissensbasis.md`, `wettbewerber_referenzen.md`.
2. Arbeite die Firmen unten ab, höchstens 10 pro Durchgang. Pro Firma im Browser: (a) Impressum/Standortseite öffnen und Sitz, Rechtsform, Handelsregisternummer notieren (V); (b) Fertigung am Sitz belegen: Produktionsbeschreibung, Stellenanzeigen mit Montage/Fertigung am Ort (V mit wörtlichem Kurzzitat); (c) Verguss/Klebung/Dichtung am Produkt belegen (Datenblatt, Produktseite, Gehäuse- oder Schutzart-Angabe); (d) Patentsuche in Google Patents, Espacenet und DEPATISnet nach Anmelder, Rechtsstand notieren; (e) Wettbewerbereinsatz (DELO, Henkel, Wacker, Elantas, Sonderhoff, Scheugenpflug, Nordson, Musashi usw. auf der Firmenseite oder in Referenzen); (f) Konzernzugehörigkeit prüfen (mehrere Werke? dann gilt die Sitzregel nicht).
3. Keine Kontaktsuche (Regel K). Nichts verschicken.
4. Ergebnis je Batch in `electronica/ergebnisse_browser/gruen_NN.md` im Tina-Format (Ampel neu: GRÜN bestätigt / GELB / ROT, Tabellenzeile D, Stufe der Belege, Zitate mit URL und Abrufdatum). Danach `python3 batch_check.py` und die Excel neu bauen lassen.
5. CRM vorher mit `python3 crm_abgleich.py "Firma" ["Konzern" …]` wiederholen; Treffer mit gleichem oder sehr ähnlichem Namen scheiden aus (Entscheidung Jey vom 22.10.).

## Entscheidungen von Jey (22.10.)

- Verbände, Prüfdienstleister und Forschungsorganisationen: raus.
- Firmen im CRM (gleicher oder sehr ähnlicher Name): raus.
- Anlagenbauer: raus, außer Verguss-/Dosieranlagen oder etwas, das Demak anbietet.

## Die 46 Grün-Kandidaten

| Nr | Firma | Stand | Gebiet | Demak | Tom/Tina-Batch |
|---|---|---|---|---|---|
| 1 | 2E mechatronic GmbH & Co. KG | B4.A03 | Baden-Württemberg | Verguss | 1 |
| 2 | Aaronia AG | A4.516 | Rest Deutschland+Niederlande | Verguss + Dichtung | 1 |
| 3 | Analog Microelectronics GmbH | Halle B4, Stand B4.201 | Rest Deutschland+Niederlande | Verguss | 4 |
| 4 | Bach Resistor Ceramics GmbH | B1.721 | Rest Deutschland+Niederlande | Verguss | 6 |
| 5 | Bungard Elektronik GmbH & Co.KG | A2.107 | Rest Deutschland+Niederlande | kein klarer Bereich | 8 |
| 6 | COLANDIS GmbH | B1.148 | Rest Deutschland+Niederlande | Dichtung + Verguss | 10 |
| 7 | ddm hopt+schuler GmbH & Co.KG | A3.418 | Baden-Württemberg | Verguss + Dichtung | 13 |
| 8 | DISPLAY VISIONS GmbH | B6.301 | Bayern | Verklebung + Verguss | 14 |
| 9 | E.E.P.D. GmbH | C5.306 | Bayern | Verguss + Verklebung + Dichtung | 15 |
| 10 | EPIGAP OSA Photonics GmbH | B5.400 | Rest Deutschland+Niederlande | Verguss + Verklebung | 17 |
| 11 | erfi Ernst Fischer GmbH + Co. KG | A4.343 | Baden-Württemberg | Verguss + Dichtung | 17 |
| 12 | ERS electronic GmbH | B1.356 | Bayern | Verguss + Verklebung + Dichtung | 18 |
| 13 | ESKA Erich Schweizer GmbH | B6.122 | Rest Deutschland+Niederlande | Verguss + Verklebung + Dichtung | 18 |
| 14 | exateq GmbH | B1.677 | Bayern | Verguss | 19 |
| 15 | FSM AG | Halle A1, Stand A1.525/3 | Baden-Württemberg | Verguss | 22 |
| 16 | Georg Schlegel GmbH & Co. KG | Halle A3, Stand 324 | Baden-Württemberg | Verguss + Dichtung | 48 |
| 17 | GfG Gesellschaft für Gerätebau mbH | C1.264 | Rest Deutschland+Niederlande | Verguss + Dichtung | 23 |
| 18 | HEIDEN power GmbH | A5.328 | Bayern | Verguss | 24 |
| 19 | Heinzinger electronic GmbH | A5.501 | Bayern | Verguss | 24 |
| 20 | HELMUT FISCHER GMBH INSTITUT FÜR ELEKTRONIK UND MESSTECHNIK | A4.648 | Baden-Württemberg | Verguss | 20 |
| 21 | iC-Haus GmbH | C5.420 | Rest Deutschland+Niederlande | Verguss + Verklebung | 26 |
| 22 | icotek GmbH & Co.KG | B3.409 | Baden-Württemberg | Dichtung | 26 |
| 23 | IL Metronic Sensortechnik GmbH | B4.318 | Rest Deutschland+Niederlande | Verguss + Dichtung | 26 |
| 24 | Isabellenhütte Heusler GmbH & Co. KG | B6.330 | Rest Deutschland+Niederlande | Verguss + Verklebung | 28 |
| 25 | JOWO - Systemtechnik AG | B2.112 | Rest Deutschland+Niederlande | Verguss + Dichtung | 29 |
| 26 | microtech GmbH electronic | A6.139 | Rest Deutschland+Niederlande | Verguss | 36 |
| 27 | OEC opto devices GmbH | B6.405 | Rest Deutschland+Niederlande | Verguss | 40 |
| 28 | OEG GmbH | C1.351 | Rest Deutschland+Niederlande | Verguss + Verklebung | 40 |
| 29 | OKW Odenwälder Kunststoffwerke Gehäusesysteme GmbH | B3.163 | Baden-Württemberg | Dichtung + Verklebung | 40 |
| 30 | Optris GmbH & Co. KG | A4.555 | Rest Deutschland+Niederlande | Verguss + Verklebung + Dichtung | 40 |
| 31 | PACE-Tec GmbH | C1.204 | Baden-Württemberg | Verguss + Dichtung | 41 |
| 32 | POLYTEC GmbH | B1.259 | Baden-Württemberg | Verguss + Verklebung | 43 |
| 33 | Ratioplast Electronics | B3.411 | Rest Deutschland+Niederlande | Verguss + Dichtung | 45 |
| 34 | REINHARDT System- und Messelectronic GmbH | A4.401 | Bayern | Verguss + Dichtung | 45 |
| 35 | ROLEC Gehäuse-Systeme GmbH | B3.250 | Rest Deutschland+Niederlande | Dichtung + Verklebung | 47 |
| 36 | SAW COMPONENTS Dresden GmbH | Halle C1, Stand 840 | Rest Deutschland+Niederlande | Verguss + Verklebung + Dichtung | 48 |
| 37 | Senso Tech GmbH | C1.233 | Rest Deutschland+Niederlande | Verguss | 50 |
| 38 | SIBA GmbH | A6.539 | Rest Deutschland+Niederlande | Verguss + Dichtung | 50 |
| 39 | SmarAct GmbH | C1.852 | Rest Deutschland+Niederlande | Verguss + Verklebung | 52 |
| 40 | Spitzenberger & Spies GmbH & Co. KG | A4.106 | Bayern | Verguss | 53 |
| 41 | SRT Resistor Technology GmbH | A6.300 | Bayern | kein klarer Bereich | 53 |
| 42 | Thyracont Vacuum Instruments GmbH | C1.848 | Bayern | Verguss | 56 |
| 43 | TIRA GmbH | A4.554 | Rest Deutschland+Niederlande | Verguss | 56 |
| 44 | TOELLNER Electronic Instrumente GmbH | A4.524 | Rest Deutschland+Niederlande | Verguss | 56 |
| 45 | VX Instruments GmbH | A4.317 | Bayern | Verguss | 60 |
| 46 | Winkler AG | C1.134 | Baden-Württemberg | Verguss | 60 |

## Details je Firma

### 1. 2E mechatronic GmbH & Co. KG (B4.A03)
- Gebiet/Ort: Baden-Württemberg –  | Quellen: `electronica/ergebnisse/tom_batch_01.md`, `tina_batch_01.md`
- Was wird gebaut (Tom): Kunststoff-Hybridtechnik, vor allem Sensorgehäuse in hohen Stückzahlen für die Automobilindustrie, vollautomatische Fertigung (S); MID-Technik mit drei Lasern und SMD-Bestückungslinie, MID-Produkte für Dental, LED-Lampen, Sonden (S) …
- Verguss laut Tom: Hoch, Stufe A. Einzelbewertung: Neigungssensor Hoch (A), Sensorgehäuse Automotive Mittel bis Hoch (A, Verklebung/Dichtung, Einlegeteile umspritzt), MID-LED-Lampen Hoch (A), Dental-/Medizin-MID Mittel …
- Offener Auftrag (Tina): Impressum/Standortseite 2e-mechatronic.de lesen (V für Sitz = Fertigungsort); Datenblatt Neigungssensor (Schutzart, Vergussmasse im Gehäuse?); Stellenanzeige Montage/Produktion Kirchheim; Patente Anmelder "2E mechatronic" in Google Patents/Espacenet/DEPATISnet.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 2. Aaronia AG (A4.516)
- Gebiet/Ort: Rest Deutschland+Niederlande – Strickscheid, Rheinland-Pfalz | Quellen: `electronica/ergebnisse/tom_batch_01.md`, `tina_batch_01.md`
- Was wird gebaut (Tom): Spektrumanalysatoren (SPECTRAN), Mess- und Richtantennen (IsoLOG 3D, HyperLOG), Drohnendetektion/-abwehr AARTOS, HF-Schirmmaterialien (S). Stellenanzeige (Snippet): Endmontage von Messsystemen und Drohnenabwehr, SMD-/THT-Platinen (S) …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: Drohnendetektions-Outdoorsysteme Mittel (A), Antennen mit Elektronik Mittel (A), Netzteile Mittel (A), Handgeräte Niedrig bis Mittel (A). Kein Beleg für Eigenverguss.
- Offener Auftrag (Tina): Impressum aaronia.com (V, Rechtsform, Sitz); welche Produkte (AARTOS-Outdoor, Antennen, Netzteile) werden in Strickscheid montiert und sind vergossen (Datenblätter, IP-Klasse, Stellenanzeige Montage); Patent-Datenbanken mit Anmelder "Aaronia".
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 3. Analog Microelectronics GmbH (Halle B4, Stand B4.201)
- Gebiet/Ort: Rest Deutschland+Niederlande – Mainz | Quellen: `electronica/ergebnisse/tom_batch_04.md`, `tina_batch_04.md`
- Was wird gebaut (Tom): Drucksensoren und analoge Signalaufbereitungs-ICs ("Frame ASICs") (S). Typisch vergossen/verklebt (A): Drucksensormodule (Block A), Sensorelektronik mit Gelschutz (A); ASIC-Chips selbst: Niedrig (A, Halbleiter, Fertigung extern).
- Verguss laut Tom: Hoch, Stufe A (abgeleitet aus Produkttyp Drucksensoren). Einzelbewertung: Drucksensormodule Hoch (A), Sensor-Baugruppen mit Gel/Klebung Mittel (A), ASIC-Chips Niedrig (A).
- Offener Auftrag (Tina): Impressum und Produktseiten analogmicro.de lesen (Montage Mainz, Konzernbezug zu AMSYS); Stellenanzeige im Original (join.com); Handelsregister Mainz. Falls Gruppe mit mehreren Werken oder Montage extern: zurück auf Gelb (Zeile 5).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 4. Bach Resistor Ceramics GmbH (B1.721)
- Gebiet/Ort: Rest Deutschland+Niederlande – Werneuchen, Brandenburg | Quellen: `electronica/ergebnisse/tom_batch_06.md`, `tina_batch_06.md`
- Was wird gebaut (Tom): keramische Heizelemente (Flachheizer, Glühzünder, Heizringe, Strahlungsheizer, Heizpatronen, Heizplatten, Chip-/Wafer-Heizer), nach eigener Beschreibung Plastifizieren, Walzen, Stanzen, Sintern, Bearbeiten, Montage (S). Typisch …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: Heizpatronen/Heizplatten (Anschlussverguss/Klebung) Mittel (A), Chip-/Wafer-Heizer Mittel (A), Vollkeramik-Heizer Niedrig (A), Keramikwiderstände Niedrig bis Mittel …
- Offener Auftrag (Tina): Datenblätter Heizpatrone/Heizplatte auf bachrc.de: Wie werden Anschlüsse isoliert/abgedichtet (Verguss, Kleber)? Impressum bachrc.de (Sitz = Fertigung, V). Patente im Browser: Anmelder "Bach Resistor Ceramics GmbH" in Espacenet/DEPATISnet.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 5. Bungard Elektronik GmbH & Co.KG (A2.107)
- Gebiet/Ort: Rest Deutschland+Niederlande – Windeck, Nordrhein-Westfalen | Quellen: `electronica/ergebnisse/tom_batch_08.md`, `tina_batch_08.md`
- Was wird gebaut (Tom): Maschinen (Ätz-, Laminier-, Bohr-/Fräsmaschinen, Durchkontaktierung), fotobeschichtetes Basismaterial und Verbrauchsmaterial für Leiterplatten-Kleinserien (S). Kunden: Hochschulen, Ingenieurbüros, Entwicklungsabteilungen (S). Typisch …
- Verguss laut Tom: Niedrig, Stufe A (Leiterplatten-Equipment und -Basismaterial, Block C; Maschinen-Steuerungen eher Mittel, aber Kleinserien-Labormaschinen). Einzelbewertung: fotobeschichtetes Basismaterial Niedrig …
- Offener Auftrag (Tina): Produktdatenblätter (Maschinensteuerungen, Pumpen, Netzteile: vergossen?), Impressum bungard.de (Fertigung Windeck, V), Stellenanzeige Montage Windeck. Aktion: niedrige Priorität.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 6. COLANDIS GmbH (B1.148)
- Gebiet/Ort: Rest Deutschland+Niederlande – Kahla, Thüringen | Quellen: `electronica/ergebnisse/tom_batch_10.md`, `tina_batch_10.md`
- Was wird gebaut (Tom): Reinraum-Komponenten und Systemlösungen: Fan-Filter-Module (FFM-S, FFM-C, FFM-E, FFM-LA, auch schwarz und mit Wärmetauscher und Regeleinheit), mobile Reinraumboxen, Mini-Environments, Reinraum-Miete, Beratung (S). Datenblatt …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: Filter-/Rahmendichtung (FIPFG-Typ) Mittel (A), Lüfter-/Regelelektronik Mittel (A), Wärmetauscher-Modul mit Regeleinheit Mittel (A), Aluminiumrahmen/Gehäuse Niedrig …
- Offener Auftrag (Tina): (a) Impressum/Standort colandis.com, Stellenanzeigen Montage Kahla (V für Fertigungsort); (b) Datenblatt FFM-C/-E: Dichtung (PU/Klebung), Lüfter-/Regelelektronik vergossen? Schutzart; (c) Patent-/Schutzrechtsnummern (DPMA/Espacenet/EUIPO, Rechtsstand).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 7. ddm hopt+schuler GmbH & Co.KG (A3.418)
- Gebiet/Ort: Baden-Württemberg – Rottweil | Quellen: `electronica/ergebnisse/tom_batch_13.md`, `tina_batch_13.md`
- Was wird gebaut (Tom): Komponenten und Systeme der Mensch-Maschine-Interaktion: Kartenleser (Kontakt/kontaktlos), Schalter, Encoder, Ticketing-Systeme (S). Typisch vergossen/verklebt/gedichtet: Encoder/Drehgeber (A, Block A "Drehgeber/Encoder", ob …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: Encoder Mittel (A, Typ offen, bei Industrie-Drehgeber Hoch), Kartenleser-Elektronik Mittel (A), Schalter Mittel (A), Ticketing-Terminals Mittel (A, Außeneinsatz).
- Offener Auftrag (Tina): hopt-schuler.com Impressum und Produktseiten im Browser lesen (Fertigung Rottweil V, IP-Klassen Kartenleser/Ticketing, Encoder-Typ), Stellenanzeige Montage im Original.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 8. DISPLAY VISIONS GmbH (B6.301)
- Gebiet/Ort: Bayern – Gilching | Quellen: `electronica/ergebnisse/tom_batch_14.md`, `tina_batch_14.md`
- Was wird gebaut (Tom): Industriedisplays von 7-Segment- bis Farb-Touch-Displays, Displays mit und ohne Touch, Optical Bonding, Touch-Lösungen und Assembly Services (S, lcd-module.com/Distributorseiten). Märkte: Medizintechnik, Automation, Industrie, Automotive …
- Verguss laut Tom: Hoch, Stufe S (Optical Bonding ausdrücklich als Leistung gelistet) mit A-Ableitung. Einzelbewertung: Optical-Bonding-Touch-Displays Hoch (S), Industrie-TFT-Module Mittel (A), LED-Hinterleuchtung …
- Offener Auftrag (Tina): Optical-Bonding-Seite und "Facts and Figures" auf lcd-module.com lesen (Bonding in Gilching? Reinraum, Klebstoff, Anlage); Impressum und Register (Rechtsform, HRB München); Karriereseite Gilching; Klebstoff-/Anlagenlieferant (Wettbewerbersignal).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 9. E.E.P.D. GmbH (C5.306)
- Gebiet/Ort: Bayern – Weichs | Quellen: `electronica/ergebnisse/tom_batch_15.md`, `tina_batch_15.md`
- Was wird gebaut (Tom): Industrie-Computer, Prozessorboards (PC/104-Plus), Module, Box-PCs, Panel-PCs, DIN-Schienen-Lösungen und kundenspezifische Systeme; "ISO 9001:2015 zertifiziert, in-house Design, Entwicklung, Serienfertigung und Test" (S …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: Prozessorboards/Module Mittel (A, Schutzlack), Panel-PC mit Display Mittel (A, Optical Bonding möglich), Box-PC-Gehäuse (Dichtung) Mittel (A), DIN-Schienen-Systeme …
- Offener Auftrag (Tina): Impressum/Gruppenstruktur (Trucomp, weitere Werke? Falls Mehrwerk, Fertigungsbeleg V nötig) auf eepd.de; Datenblatt Panel-PC (Schutzart, Display-Verklebung, Schutzlack); Stellenanzeige im Original lesen (gilt dann als V).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 10. EPIGAP OSA Photonics GmbH (B5.400)
- Gebiet/Ort: Rest Deutschland+Niederlande – Berlin-Köpenick | Quellen: `electronica/ergebnisse/tom_batch_17.md`, `tina_batch_17.md`
- Was wird gebaut (Tom): LED-Chips, SMD- und Through-Hole-LEDs sowie Photodioden von 200 nm (UV-C) bis 2300 nm (SWIR), Monolithic Displays, Serien in kleinen und mittleren Mengen (S). Das SWIR-LED-Produkt "OCI-460" kombiniert eine Silikonkuppel mit Keramikgehäuse …
- Verguss laut Tom: Mittel, Stufe A. Einzelbauteile: SMD-LED mit Silikonkuppel Mittel (S/A, Verkapselung im Package, vermutlich über Dosierung, nicht belegt), Through-Hole-LED Mittel (A), Photodioden-Chips Niedrig (A) …
- Offener Auftrag (Tina): Datenblätter/Produktseiten epigap-osa.de (Verkapselungsmaterial Silikon/Epoxid, Dosierung), Impressum und Register Berlin, Stellenanzeigen Berlin (Die-Bonding, Dosieren, Montage).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 11. erfi Ernst Fischer GmbH + Co. KG (A4.343)
- Gebiet/Ort: Baden-Württemberg – Freudenstadt | Quellen: `electronica/ergebnisse/tom_batch_17.md`, `tina_batch_17.md`
- Was wird gebaut (Tom): Technische Arbeitsplatzsysteme/Labormöbel, Mess- und Prüfgeräte, Prüfsysteme für elektrische Sicherheit und Funktion, didaktische Lehrsysteme, 19-Zoll-Einschubmodule wie Regelnetzgeräte, Stelltransformatoren und Messgeräte; eigene …
- Verguss laut Tom: Hoch, Stufe A. Begründung: Netzgeräte und Trafos sind laut Wissensbasis Block A "nahezu immer vergossen"; Einschätzung aus Produkttyp, kein direkter Beleg. Kein Gegenbeleg gefunden.
- Offener Auftrag (Tina): erfi.de Impressum/Register (Feld 17, V); Werksseite Freudenstadt (V Fertigungsort); Datenblatt Regelnetzgerät/Stelltransformator (Vergussangabe, IP-Klasse); Stellenanzeigen Wickeln/Vergießen/Montage.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 12. ERS electronic GmbH (B1.356)
- Gebiet/Ort: Bayern – Germering | Quellen: `electronica/ergebnisse/tom_batch_18.md`, `tina_batch_18.md`
- Was wird gebaut (Tom): Thermochucks (luftgekühlt -65 bis +550 °C und "High Power Dissipation" mit Flüssigkeits-Chillern) für Wafer-Prober sowie Debonding-/Warpage-Adjust-Tools für Fan-out-Wafer-Level-Packaging (S). Typisch vergossen/verklebt/gedichtet (alles A …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: Heizelemente/Temperatursensoren im Chuck Mittel (A, Heizelement ist Beispielprodukt der Endprodukt-Regel, Einbettung in Metallkörper statt Verguss offen) …
- Offener Auftrag (Tina): Impressum ers-gmbh.com (Gesellschaft, Adresse, V für Sitz); Datenblatt AC3/AirCool PRIME (Heizerbauart, Schutzart); Stellenanzeigen Germering (Montage/Produktion); Espacenet "ERS electronic" als Anmelder.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 13. ESKA Erich Schweizer GmbH (B6.122)
- Gebiet/Ort: Rest Deutschland+Niederlande – Kassel, Hessen | Quellen: `electronica/ergebnisse/tom_batch_18.md`, `tina_batch_18.md`
- Was wird gebaut (Tom): Feinsicherungen (Glas/Keramikrohr), SMD-Sicherungen, Thermosicherungen, PTC-Rückstellsicherungen, Automotive-Sicherungen, NH-Sicherungen, Sicherungshalter, Einpressbauteile (S). Typisch vergossen/verklebt/gedichtet: Thermosicherungen …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: Thermosicherung Mittel (A), Sicherungshalter Mittel (A), Glas-/Keramikrohr-Sicherung Mittel (A, Kappenverklebung/Verkittung), SMD-Sicherung Niedrig (A), PTC Mittel …
- Offener Auftrag (Tina): eska-fuses.de Impressum und Standortseite lesen (V Fertigung Kassel); Datenblatt Thermosicherung (Gehäuse/Verschluss: Epoxid, Keramik?); Stellenanzeigen Produktion Kassel.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 14. exateq GmbH (B1.677)
- Gebiet/Ort: Bayern – Neumarkt in der Oberpfalz | Quellen: `electronica/ergebnisse/tom_batch_19.md`, `tina_batch_19.md`
- Was wird gebaut (Tom): Batch-Nassprozessanlagen für Ätzen und Reinigen (Wet Benches), Chemie-Versorgungs- und Entsorgungssysteme, Carrier (S). Zielbranchen Solar, Elektronik, Energie, Life Science. Typisch vergossen/verklebt/gedichtet in solchen Anlagen: Steuer- …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: Füllstand-/Temperatursensoren (zugekauft) Mittel (A), Pumpen/Magnetventile Mittel (A), Schaltschrank-Steuerung Niedrig (A), Anlagenkörper Niedrig (A). Maschinenbau …
- Offener Auftrag (Tina): Impressum und Produktseiten der Firmenwebsite (Domain unbekannt) lesen: Fertigung Neumarkt (V), Steuerung/Sensorik Eigenbau oder Zukauf; Stellenanzeigen Neumarkt (Montage, Elektro).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 15. FSM AG (Halle A1, Stand A1.525/3)
- Gebiet/Ort: Baden-Württemberg –  | Quellen: `electronica/ergebnisse/tom_batch_22.md`, `tina_batch_22.md`
- Was wird gebaut (Tom): "intelligente Elektronik für mobile Energieversorgung, Messtechnik, Trafoschaltrelais" sowie EMS (E2MS) (S). Typisch vergossen/verklebt/gedichtet (A, aus Produkttyp): Trafoschaltrelais (Block A Relais/Trafo), Netzteile/Ladetechnik mobile …
- Verguss laut Tom: Hoch, Stufe A. Einzelbewertung: Trafoschaltrelais Hoch (A), Netzteile mobile Energieversorgung Hoch (A), Druckmessumformer Hoch (A), EMS-Baugruppen Mittel (A, Kunden aus Industrie). Kein Beleg für …
- Offener Auftrag (Tina): Impressum/Register (Freiburg) lesen; Stellenanzeige "Montagecenter" im Original (Standort); Datenblatt Trafoschaltrelais/Netzteil (Schutzart, vergossen?).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 16. Georg Schlegel GmbH & Co. KG (Halle A3, Stand 324)
- Gebiet/Ort: Baden-Württemberg – Dürmentingen | Quellen: `electronica/ergebnisse/tom_batch_48.md`, `tina_batch_48.md`
- Was wird gebaut (Tom): Schalter, Drucktaster, Not-Halt-Schalter, Kontaktgeber, Bedieneinheiten, Gehäuse, Klemmen, Endschalter, RFID-Systeme, Bus-Lösungen (S, Messeverzeichnis/Zeitung). Über 8.000 Produkte (S, Firmenangabe). Baureihen teils IP65 und IP67, andere …
- Verguss laut Tom: Hoch, Stufe A. Einzelbewertung: RFID-/Bus-Elektronikmodule Hoch (A, Block A RFID/Elektronik in rauer Umgebung), beleuchtete Taster mit LED Mittel (A), IP65-IP69K-Bedienelemente Mittel (A …
- Offener Auftrag (Tina): Fertigung vor Ort und Verguss/Klebung im Browser belegen; Impressum, Stellenanzeigen, Datenblätter lesen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 17. GfG Gesellschaft für Gerätebau mbH (C1.264)
- Gebiet/Ort: Rest Deutschland+Niederlande – Dortmund, NRW | Quellen: `electronica/ergebnisse/tom_batch_23.md`, `tina_batch_23.md`
- Was wird gebaut (Tom): Tragbare und stationäre Gasmessgeräte, Gassensoren, Mehrgasmessgeräte mit Mikroprozessor, Systemlösungen (Stufe S). Typisch vergossen/verklebt/gedichtet (Stufe A): Gassensoren und Sensormodule (Block A), Elektronikbaugruppen/Netzteile im …
- Verguss laut Tom: Hoch, Stufe A (Produkttyp: Gassensoren, Ex-Messgeräte nach Wissensbasis Block A). Einzelbewertung: Sensoren/Sensormodule Hoch (A); Mehrgas-Elektronik Mittel (A); Netzteil/Laderegler Hoch (A) …
- Offener Auftrag (Tina): Impressum/Standorte gfgsafety.com (Ein-Werk, Eigentümerstruktur, V), Stellenanzeige im Original (Montage Dortmund = V für Fertigungsort), Datenblatt Sensor/Transmitter (Verguss, Schutzart), Patente Espacenet/DEPATISnet Anmelder GfG.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 18. HEIDEN power GmbH (A5.328)
- Gebiet/Ort: Bayern – Pürgen | Quellen: `electronica/ergebnisse/tom_batch_24.md`, `tina_batch_24.md`
- Was wird gebaut (Tom): AC/DC-Netzteile in allen Leistungsklassen, Source-/Sink-Systeme, Ladegeräte, Bodenstromgeräte (Ground Power Units), elektronische Lasten, AC-Quellen, Frequenzumrichter, Leistungsanalysatoren, kundenspezifische Prüf- und Testsysteme (S) …
- Verguss laut Tom: Hoch, Stufe A (abgeleitet aus Produkttyp Netzteile/induktive Bauelemente). Bauteile: Transformatoren/Drosseln Hoch (A), DC/DC- und Netzteilmodule Hoch (A), Ladegeräte/Bodenstromsysteme Hoch (A) …
- Offener Auftrag (Tina): Impressum/Register beider HEIDEN-Gesellschaften, Datenblatt penFrame/DIN-Rail (Schutzart, "potted"), Stellenanzeige Montage Pürgen; Jey: Herkunft des Vermerks "bereits DEMAK-bekannt" (Kontakt außerhalb der Exportdateien?). Aktion: nicht kontaktieren, bis Vermerk geklärt.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 19. Heinzinger electronic GmbH (A5.501)
- Gebiet/Ort: Bayern – Rosenheim | Quellen: `electronica/ergebnisse/tom_batch_24.md`, `tina_batch_24.md`
- Was wird gebaut (Tom): Hochspannungs-Netzgeräte bis 300 kV, präzise Niederspannungs-Netzgeräte bis 10.000 A, programmierbare DC-Netzgeräte, Magnetnetzgeräte, Laborstromversorgungen, HV-Zubehör für Medizintechnik, Industrie, Forschung, Batterietest …
- Verguss laut Tom: Hoch, Stufe A (abgeleitet aus Produkttyp: Netzteile, Hochspannungstransformatoren/-module, induktive Bauelemente nach Block A). Bauteile: HV-Transformatoren/-Kaskaden Hoch (A; Gegenhypothese …
- Offener Auftrag (Tina): Impressum/Register Rosenheim (V Sitz), Datenblatt HV-Modul/Trafo (Isolation vergossen/Öl), Stellenanzeige Montage/Wickeln Rosenheim; Klärung, welche Einheit nach dem NI-Verkauf noch Automotive/Ladetest fertigt.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 20. HELMUT FISCHER GMBH INSTITUT FÜR ELEKTRONIK UND MESSTECHNIK (A4.648)
- Gebiet/Ort: Baden-Württemberg – Sindelfingen | Quellen: `electronica/ergebnisse/tom_batch_20.md`, `tina_batch_20.md`
- Was wird gebaut (Tom): Messgeräte für Schichtdicke, Materialanalyse (Röntgenfluoreszenz), Materialprüfung und Mikrohärte, von Handgeräten bis zu Inline-Systemen (S). Typisch vergossen/verklebt/gedichtet: Messsonden/Sensoren Hoch (A, Block A Sensoren; US5831430A …
- Verguss laut Tom: Hoch, Stufe A. Einzelbewertung siehe Feld 6. Kein Gegenbeleg gefunden.
- Offener Auftrag (Tina): (a) Standort-/Karriereseite helmut-fischer.com: Fertigung Sindelfingen und mögliche weitere Werke (V). (b) Werden Messsonden vergossen oder verklebt (Datenblatt/Stellenanzeige Sondenbau, Patentbeschreibung WO2012160132 "Herstellungsverfahren")? (c) Impressum/Gruppenname für Konzernabgleich Regel M.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 21. iC-Haus GmbH (C5.420)
- Gebiet/Ort: Rest Deutschland+Niederlande – Bodenheim, Rheinland-Pfalz | Quellen: `electronica/ergebnisse/tom_batch_26.md`, `tina_batch_26.md`
- Was wird gebaut (Tom): ASICs, optische und magnetische Encoder-ICs, Interpolatoren, Sensor-ICs sowie Mikrosysteme in Chip-on-Board-Technik und optoBGA/QFN-Gehäusen (S, magneticsmag.com). Typisch vergossen/verklebt (A): Chip-on-Board-Mikrosysteme und …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: COB-Mikrosysteme/Multichipmodule Mittel (A, Glob-Top, Block B), optoBGA-Sensorgehäuse Mittel (A), Standard-Kunststoff-ICs Niedrig (A, Mold). Hinweis …
- Offener Auftrag (Tina): Datenblatt/Fertigungsbeschreibung COB und optoBGA (Glob Top, Dam-and-Fill, Underfill), Stellenanzeige Reinraum-Montage, Impressum ichaus.de (Register).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 22. icotek GmbH & Co.KG (B3.409)
- Gebiet/Ort: Baden-Württemberg – Eschach | Quellen: `electronica/ergebnisse/tom_batch_26.md`, `tina_batch_26.md`
- Was wird gebaut (Tom): Kabeleinführungssysteme (teilbare Rahmen/Platten mit Tüllen), Kabelverschraubungen, EMV-Schirmanschlüsse, vorkonfigurierte Leitungen (S). Tüllen aus Elastomer, Korpus Polyamid, Tülle umspritzt (S), Schutzarten IP54 bis IP66. Typisch …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: Dichtungen/Tüllen (Gasketing) Mittel (A), vorkonfektionierte Leitungen mit Durchführungen Mittel (A), EMV-Schirmanschlüsse Niedrig (A), Spritzgussteile Niedrig (A …
- Offener Auftrag (Tina): Impressum/Register icotek.com (Rechtsform, Verhältnis zu Icotek Project GmbH & Co. KG); Datenblatt KEL-Serien (Dichtungsmaterial, geschäumt/gespritzt?); Stellenanzeige Konfektionierung im Original lesen (Verguss/Umspritzen der Leitungen?).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 23. IL Metronic Sensortechnik GmbH (B4.318)
- Gebiet/Ort: Rest Deutschland+Niederlande – Ilmenau-Unterpörlitz, Thüringen | Quellen: `electronica/ergebnisse/tom_batch_26.md`, `tina_batch_26.md`
- Was wird gebaut (Tom): Glasdurchführungen (Glas-Metall-Einschmelzungen, kundenspezifisch), UV-, Feuchte-, Temperatur- und Drucksensoren, Sensormodule, UV-Anzeige- und Referenzmessgeräte, vor allem UV-Desinfektion von Trink- und Prozesswasser (S). Typisch …
- Verguss laut Tom: Hoch, Stufe A (Produkttyp Sensoren/Sensormodule, kein direkter Beleg). Einzelbewertung: UV-/Drucksensoren Hoch (A), Sensormodule mit Elektronik Hoch (A), Anzeige-/Auswertegeräte Mittel (A) …
- Offener Auftrag (Tina): Pressemeldung PDF sensor-test.de im Browser lesen (V-Zitat "Fertigungstiefe"); Datenblätter UV-Sensor (Schutzart IP68? vergossen/verklebt, Dichtung Messfenster); Impressum il-metronic.de.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 24. Isabellenhütte Heusler GmbH & Co. KG (B6.330)
- Gebiet/Ort: Rest Deutschland+Niederlande – Dillenburg, Hessen | Quellen: `electronica/ergebnisse/tom_batch_28.md`, `tina_batch_28.md`
- Was wird gebaut (Tom): Widerstandslegierungen, Präzisions- und Strommesswiderstände/Shunts (FMx, BAL, ISA-WELD, ISA-PLAN; BAL für Batteriemanagement, -40 bis +170 °C, S), Stromsensor-Module auf Shunt-Basis (IVT-Serie, CAN-Schnittstelle, 16-Bit-ADC, Galvanik bis …
- Verguss laut Tom: Hoch, Stufe A (abgeleitet aus Produkttyp Strom-/Shunt-Sensormodul mit Elektronik, kein direkter Beleg). Einzelbewertung: IVT-Strommessmodule Hoch (A), BAL/Shunt für BMS mit Elektronik Mittel (A) …
- Offener Auftrag (Tina): Standortseite/Impressum und "about us" im Browser lesen (V für Dillenburg als Fertigungsort für Messmodule, Ausschluss weiterer Werke); IVT-MODular-/IVT-S-Datenblatt auf Gehäuse "vergossen/Potting" lesen; Karriereseite Dillenburg (Montage Elektronik); Patente DEPATISnet/Espacenet (Anmelder Isabellenhütte Heusler, Stichwort Vergussmasse/Verkapselung) mit Rechtsstand.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 25. JOWO - Systemtechnik AG (B2.112)
- Gebiet/Ort: Rest Deutschland+Niederlande – Delmenhorst, Niedersachsen | Quellen: `electronica/ergebnisse/tom_batch_29.md`, `tina_batch_29.md`
- Was wird gebaut (Tom): „Entwicklung, Herstellung, Planung und der Handel mit elektrischen und optischen Steckverbindern und Systemgeräten“ plus Verkabelung (S, Stellenanzeige). Produktprofil: VG- und MIL-Steckverbinder, Subsea-Steckverbinder, Raumfahrt …
- Verguss laut Tom: Hoch, Stufe A. Einzelbewertung: Subsea-/Offshore-Steckverbinder und Kabelkonfektion Hoch (A), ATEX/IECEx-Komponenten Hoch (A), LWL-Konfektion Mittel (A), Systemgeräte-Gehäuse Mittel (A). Kein …
- Offener Auftrag (Tina): jowosy.de Produktseiten und Impressum im Browser lesen (Sitz = Fertigungsort V, Rechtsform AG, welche Produkte in Delmenhorst gefertigt, ob Verguss/Überspritzung/Kleben); Stellenanzeige join.com im Original; Patentsuche Google Patents/Espacenet/DEPATISnet mit "JOWO" und Varianten.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 26. microtech GmbH electronic (A6.139)
- Gebiet/Ort: Rest Deutschland+Niederlande – Teltow, Brandenburg | Quellen: `electronica/ergebnisse/tom_batch_36.md`, `tina_batch_36.md`
- Was wird gebaut (Tom): Dünn- und Dickschicht-Chipwiderstände, SMD-Netzwerke, Platin-Chip-Temperatursensoren (Serie CPT) und Präzisionswiderstände, Kunden Medizintechnik, Automotive, Regelungstechnik (S, wts electronic Overview 06/2016). Typisch …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: Platin-Chip-Temperatursensoren Mittel (A), Chipwiderstände Niedrig (A), Netzwerke Niedrig (A). Das Maximum Mittel gilt nur, weil kundenspezifische Sensor-Varianten …
- Offener Auftrag (Tina): Datenblatt CPT/PTC und Linecard im Wortlaut (Passivierung, Glob-Top, vergossene Sensorvarianten mit Anschlussleitung); Impressum microtech-teltow.de (Sitz = Fertigungsort, V); Stellenanzeige Teltow im Original.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 27. OEC opto devices GmbH (B6.405)
- Gebiet/Ort: Rest Deutschland+Niederlande – Stocksee, Schleswig-Holstein | Quellen: `electronica/ergebnisse/tom_batch_40.md`, `tina_batch_40.md`
- Was wird gebaut (Tom): LED-Lichtquellen, individuell angepasste LED-Module und Panel-Leuchten, Display-Komponenten, Infrarot-LEDs; Lieferkette "von Rohmaterial bis Fertigprodukt" (S, LinkedIn-Profil). Typisch vergossen/verklebt: LED-Module (A, Block A, besonders …
- Verguss laut Tom: Hoch, Stufe A. Einzelbewertung: LED-Module Hoch (A), Signal-/Verkehrsanzeigen-Module Hoch (A), Panel-Leuchten Mittel (A), Display-/Backlight-Komponenten Mittel (A). Kein Direktbeleg für Eigenverguss.
- Offener Auftrag (Tina): optodevices.de Impressum/Produktseiten lesen (Fertigung am Sitz? SMT-Bestückung selbst?), Datenblätter (IP-Klasse, "vergossen"), Stellenanzeigen Stocksee.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 28. OEG GmbH (C1.351)
- Gebiet/Ort: Rest Deutschland+Niederlande – Frankfurt (Oder), Brandenburg | Quellen: `electronica/ergebnisse/tom_batch_40.md`, `tina_batch_40.md`
- Was wird gebaut (Tom): Mess- und Prüfgeräte für optische, physikalische und geometrische Parameter: MTF-Prüfstände, EFL-/Radius-Messsysteme, Autokollimatoren (elektronisch, IR), berührungslose Messgeräte für die Dosenindustrie (S, optics.org und IHK-Artikel) …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: Steuer-/Kameraelektronik Mittel (A, Einschätzung aus Produkttyp Prüf-/Messgerät), Optikfassungen/Linsen Mittel (A, Klebung), Gehäuse Niedrig (A), Netzteile …
- Offener Auftrag (Tina): Impressum oeggmbh.com und Handelsregister Frankfurt (Oder) HRB 4594 (Rechtsform, Name), Produktseite Kameramodule/Autokollimator (Gehäuse, Dichtung, Verklebung), Stellenanzeigen Montage.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 29. OKW Odenwälder Kunststoffwerke Gehäusesysteme GmbH (B3.163)
- Gebiet/Ort: Baden-Württemberg – Buchen/Odenwald | Quellen: `electronica/ergebnisse/tom_batch_40.md`, `tina_batch_40.md`
- Was wird gebaut (Tom): Standard-Kunststoffgehäuse für Elektronik (Mini-Data-Box, NET-BOX, Smart-Box IP65/IP66, EVOTEC, SLIM-CASE), Drehknöpfe, Zubehör (S). Fertigung "von Mustern bis Serie" mit Siebdruck, Tampondruck, Oberflächenveredelung, Montage und …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: leeres Kunststoffgehäuse Niedrig (A), Gehäusedichtung (Einlegedichtung, evtl. FIPFG) Mittel (A, Block B, FIPFG nicht belegt), Folientastatur/Frontfolie Mittel (A …
- Offener Auftrag (Tina): okw.com Produktseite C70/IN-BOX Datenblatt (Dichtungsverfahren: eingeschäumt = FIPFG? wo und von wem aufgebracht, Buchen?), Impressum/Gesellschafter (Konzern ja/nein), Karriereseite Buchen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 30. Optris GmbH & Co. KG (A4.555)
- Gebiet/Ort: Rest Deutschland+Niederlande – Berlin | Quellen: `electronica/ergebnisse/tom_batch_40.md`, `tina_batch_40.md`
- Was wird gebaut (Tom): stationäre Infrarot-Thermometer/Pyrometer (CT-, CTLaser-, CTi-Serien, über eine Million verkauft), Infrarot-Kameras, Handgeräte, Kalibrierquellen, Zubehör und Software (S). Outdoor-Schutzgehäuse IP66 für Kameras (S, SPS 2022). Typisch …
- Verguss laut Tom: Hoch, Stufe A. Einzelbewertung: Pyrometer-Sensorkopf Hoch (A, Block A Prozessensor im Feld), Kamera mit IP-Gehäuse Mittel (A), Schutzgehäuse IP66 Mittel (A), Elektronikbox/Schnittstelle Mittel (A) …
- Offener Auftrag (Tina): optris.com "About us"/Made in Germany und Impressum im Browser lesen (V, Zitat sichern), Datenblatt CT/CSmicro (Sensorkopf: vergossen? IP65/IP67), Stellenanzeige Produktion/Montage Berlin; Patente in Espacenet/DEPATISnet nachholen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 31. PACE-Tec GmbH (C1.204)
- Gebiet/Ort: Baden-Württemberg – Furtwangen | Quellen: `electronica/ergebnisse/tom_batch_41.md`, `tina_batch_41.md`
- Was wird gebaut (Tom): Nasschemische Prozessanlagen ("Nassbänke") für Halbleiter-, Elektronik-, High-Tech-, Medizintechnik- und Pharma-Kunden: manuell, teilautomatisch bis vollautomatisch, inkl. Medienversorgung und ATEX-Sicherheitstechnik; Anwendungen Ätzen …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: Heizelemente/Sensoren Mittel (A), Ultraschallgeber Mittel (A), Steuerschrank-Elektronik Niedrig (A), Behälter/Fluidik Niedrig (A). Wissensbasis Block C führt …
- Offener Auftrag (Tina): Impressum und Produktseite pace-tec.de lesen (Sitz = Fertigungsort, Rechtsform, Register Freiburg; V), Datenblatt Nassbank (verbaute Heizer/Sensoren/Ultraschallgeber, Schutzart), Stellenanzeige Montage/Elektrik Furtwangen; Patentabfrage (Google Patents/Espacenet/DEPATISnet) nachholen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 32. POLYTEC GmbH (B1.259)
- Gebiet/Ort: Baden-Württemberg – Waldbronn | Quellen: `electronica/ergebnisse/tom_batch_43.md`, `tina_batch_43.md`
- Was wird gebaut (Tom): Laser-Vibrometer (VibroFlex, VibroOne, UHF-120), Industrie-Vibrationssensor IVS-500 für akustische Qualitätsprüfung, Laser-Velocimeter LSV-1000 (alles S, Broschüre-Snippet, teils 2013 bis 2015 datiert). Typisch vergossen/verklebt/gedichtet …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: IVS-500 Industriesensor Mittel (A), Sensorkopf-Elektronik Mittel (A), Optik/Interferometer-Verklebung Mittel (A), Gehäuse Niedrig (A). Kein direkter Beleg, kein …
- Offener Auftrag (Tina): Impressum und Gesellschafterstruktur polytec.com lesen (keine Verbindung zu Bostik/Arkema, V); aktuelle Stellenanzeige Montage Waldbronn (V für Fertigungsort, alte Anzeige 2022); Datenblatt IVS-500 (IP-Klasse, Verguss) und Vibrometer-Datenblätter.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 33. Ratioplast Electronics (B3.411)
- Gebiet/Ort: Rest Deutschland+Niederlande – Lübbecke, NRW | Quellen: `electronica/ergebnisse/tom_batch_45.md`, `tina_batch_45.md`
- Was wird gebaut (Tom): Kundenspezifische Steckverbinder, Kunststoffteile und Werkzeuge für verschiedene Branchen; nahezu alle Fertigungsschritte im eigenen Haus (S, Wirtschaftsforum-Interview). 2016 Übernahme CS Components GmbH (S). Typisch …
- Verguss laut Tom: Mittel, Stufe A. Begründung: Steckverbinder/Konfektion mit möglichen überspritzten oder vergossenen Varianten; Beleg fehlt. Einzelbewertung: Steckverbinder mit Kabel/Leitung Mittel (A) …
- Offener Auftrag (Tina): Welche Steckverbinder/Konfektionen werden umspritzt oder vergossen? ratioplast.de Produktseiten, Datenblätter, Stellenanzeigen Lübbecke (Spritzguss/Montage); Impressum/Handelsregister (Rechtsform, Verhältnis zu Ratioplast-Optoelectronics, Standort CS Components).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 34. REINHARDT System- und Messelectronic GmbH (A4.401)
- Gebiet/Ort: Bayern – Dießen am Ammersee | Quellen: `electronica/ergebnisse/tom_batch_45.md`, `tina_batch_45.md`
- Was wird gebaut (Tom): Prüfsysteme (In-Circuit- und Funktionstest, Prüfadapter), Software-Module, SMD-Bauteilezähler, Kabeltestsysteme, Wetterstationen und Sensoren (Klima-, Niederschlags-, Windsensoren, beheizter Niederschlagsmesser) (S, Firmenprofile). Typisch …
- Verguss laut Tom: Hoch, Stufe A. Begründung: Sensoren im rauen Außeneinsatz (Temperatur, Feuchte, Niederschlag, Wind) gehören nach Wissensbasis Block A zu den fast immer vergossenen Bauteilen; Gegenbeleg gefunden …
- Offener Auftrag (Tina): Impressum/Standortseite reinhardt-testsystem.de (Fertigung am Sitz, V); Datenblatt MWS 55M und Sensoren (IP-Klasse, vergossene Elektronik/Sensorköpfe); Stellenanzeigen Dießen (Montage, Test).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 35. ROLEC Gehäuse-Systeme GmbH (B3.250)
- Gebiet/Ort: Rest Deutschland+Niederlande – Rinteln, Niedersachsen | Quellen: `electronica/ergebnisse/tom_batch_47.md`, `tina_batch_47.md`
- Was wird gebaut (Tom): Elektronik-Gehäuse aus Aluminium-Druckguss/Strangpressprofil, GFK-Polyester, ABS/PC mit CNC-Bearbeitung, Pulverbeschichtung, Lackierung, Frontplatten und Membrantastaturen; Schutzarten IP65 bis IP67 (S). Typisch gedichtet/verklebt (alles …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: Gehäusedichtung Mittel (A, Block B FIPFG), Frontplatten-/Tastaturverklebung Mittel (A, Block B Verklebung), Gehäusekörper Niedrig (A, Block C). Gegenbeleg nicht …
- Offener Auftrag (Tina): Impressum/Register Rinteln (Feld 17 V); Katalog/Datenblatt rolec.de (Dichtungsart, Frontplatten/Folientastaturen, IP-Klasse), Karriereseite (Montage/Kleben); Patentsuche Anmelder "ROLEC Gehäuse-Systeme" in Google Patents/DEPATISnet.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 36. SAW COMPONENTS Dresden GmbH (Halle C1, Stand 840)
- Gebiet/Ort: Rest Deutschland+Niederlande – Dresden, Sachsen | Quellen: `electronica/ergebnisse/tom_batch_48.md`, `tina_batch_48.md`
- Was wird gebaut (Tom): SAW-Filter und -Resonatoren (Serie), SAW-Sensoren, RFID-Tags, kundenspezifische Entwicklung und SAW-Wafer-Foundry (S, Silicon-Saxony-Profil). Branchen laut Profil: Automotive, Luftfahrt, Kommunikation, Medizin, Umwelt (S). Typisch …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: SAW-Sensoren Mittel (A), RFID-Tags Mittel (A, Gehäuse/Verkapselung je nach Ausführung), SAW-Filter/Resonatoren Niedrig (A, Keramik-/Metallgehäuse oder Kappe) …
- Offener Auftrag (Tina): Fertigung vor Ort und Verguss/Klebung im Browser belegen; Impressum, Stellenanzeigen, Datenblätter lesen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 37. Senso Tech GmbH (C1.233)
- Gebiet/Ort: Rest Deutschland+Niederlande – Magdeburg-Barleben, Sachsen-Anhalt | Quellen: `electronica/ergebnisse/tom_batch_50.md`, `tina_batch_50.md`
- Was wird gebaut (Tom): Inline-Messgeräte für Flüssigkeiten (LiquiSonic, Ultraschall-Schallgeschwindigkeit: Konzentration, Dichte), Sensor aus Edelstahl, optional beschichtet (Halar, PFA, Tantal), Ex-Version, neuer Ultraschallsensor für Halbleiter-Nassprozesse …
- Verguss laut Tom: Hoch, Stufe A (Produkttyp Prozess-/Füllstandssensoren, Ex-Ausführung, Block A). Einzelbewertung: Sensorkopf mit Wandlerelektronik Hoch (A), Ex-Sensor Hoch (A, Kapselung) …
- Offener Auftrag (Tina): (a) Aussteller-Detailseite C1.233 und Impressum sensotech.com lesen: Ist "Senso Tech GmbH" = SensoTech GmbH (Feld 17 V)? (b) Wird die Sensorelektronik in Barleben montiert und vergossen (Datenblatt LSM, Stellenanzeige Montage/Elektronik Barleben)? (c) Patente Anmelder "SensoTech GmbH" in Espacenet/DEPATISnet.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 38. SIBA GmbH (A6.539)
- Gebiet/Ort: Rest Deutschland+Niederlande – Lünen, NRW | Quellen: `electronica/ergebnisse/tom_batch_50.md`, `tina_batch_50.md`
- Was wird gebaut (Tom): Hoch- und Niederspannungssicherungen (HH, NH), Sicherungen für Leistungselektronik, Miniatursicherungen, Sicherungshalter und -einsätze (S). HH-Einsätze mit "reliable sealing against moisture, dust and corrosion" (S, Datenblatt HH) …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: HH-Sicherungseinsatz mit Abdichtung Mittel (A, Dichten/Verkleben der Endkappen), NH-Sicherungseinsatz Mittel (A), Sicherungen für Leistungselektronik …
- Offener Auftrag (Tina): Impressum/Standorte siba.de (Ein-Werk-Bestätigung, Rechtsform, V); HH-Information202002.pdf lesen (Zitat "dauerelastisch abgedichtet", Werk Lünen); aktuelle Stellenanzeige Montage Lünen; Patente Anmelder "SIBA" mit Füll-/Dichtbegriffen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 39. SmarAct GmbH (C1.852)
- Gebiet/Ort: Rest Deutschland+Niederlande – Oldenburg, Niedersachsen | Quellen: `electronica/ergebnisse/tom_batch_52.md`, `tina_batch_52.md`
- Was wird gebaut (Tom): piezobasierte Positionierer (Mikro-/Nanopositionierung, patentierte Piezoantriebe), Mess-/Sensorsysteme auf Basis von Laserinterferometern, Positionssensoren, parallele Kinematiken, miniaturisierte Roboter und Steuerungen (S). Typisch …
- Verguss laut Tom: Hoch, Stufe A (Positions-/Wegsensoren Block A, Piezoaktoren). Einzelbewertung: Piezoantriebe Hoch (A), Positionssensoren Hoch (A), Steuerelektronik Mittel (A), Interferometer/Optik Mittel (A) …
- Offener Auftrag (Tina): (a) Karriereseite smaract.com/stellenangebote und "Company" im Browser lesen, Zitat Montage Oldenburg (Fertigung V). (b) Datenblätter/Stellenanzeigen: Werden Piezoelemente, Sensoren oder Elektronik vergossen/verklebt? (c) Impressum: welche Gesellschaft fertigt (GmbH, Holding, Automation)? (d) Patente Google Patents/Espacenet, Anmelder SmarAct GmbH und SmarAct Holding GmbH.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 40. Spitzenberger & Spies GmbH & Co. KG (A4.106)
- Gebiet/Ort: Bayern – Viechtach | Quellen: `electronica/ergebnisse/tom_batch_53.md`, `tina_batch_53.md`
- Was wird gebaut (Tom): Wechselstromquellen und Netzsimulationssysteme für Labor und Prüfung (1,5 kHz bis 200 kHz, bis 270 V; 15 Hz bis 1500 Hz, bis 30 kVA), Störfestigkeitsprüfungen nach IEC/EN 61000-4-11 (S). Typisch vergossen/verklebt (A, Block A/E) …
- Verguss laut Tom: Hoch, Stufe A. Einzelbewertung: Leistungsverstärker/Leistungselektronik Hoch (A, Block A), Trafos/Drosseln Hoch (A, Block A), Steuerelektronik Mittel (A). Kein direkter Beleg für Verguss.
- Offener Auftrag (Tina): (a) Firmenwebsite/Impressum und Karriereseite im Browser lesen, Zitat zu Fertigung in Viechtach als V sichern. (b) Datenblätter der Leistungsverstärker/Netzsimulatoren auf Vergossenes (Trafos, Module) prüfen. (c) Patentsuche Espacenet/DEPATISnet Anmelder "Spitzenberger & Spies" und "Spitzenberger und Spies". (d) Wettbewerbereinsatz: Einzelsuche.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 41. SRT Resistor Technology GmbH (A6.300)
- Gebiet/Ort: Bayern – Cadolzburg | Quellen: `electronica/ergebnisse/tom_batch_53.md`, `tina_batch_53.md`
- Was wird gebaut (Tom): Dickschicht-Widerstände, Hochohm-Widerstände, Hochtemperaturwiderstände bis 300 °C, Hochspannungswiderstände bis 6 kV (SMD) bzw. 80 kV (bedrahtet), Leistungswiderstände (S). Typisch vergossen/verklebt/lackiert (A): Hochspannungswiderstände …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: Hochspannungswiderstände Mittel (A, Hochspannungs-Indikator, Umhüllung/Isolation), Leistungswiderstände Mittel (A), Dickschicht-Chip-Widerstände Niedrig (A) …
- Offener Auftrag (Tina): (a) Datenblätter der Hochspannungsreihen (z. B. HVR/GST/CDV, rhopointcomponents-PDFs oder srt-restech.de) im Browser lesen: Umhüllung Lack, Verguss, Formmasse oder Glas? (b) Fertigung Cadolzburg per Impressum/Standortseite als V. (c) Patente Espacenet/DEPATISnet (Anmelder SRT Resistor Technology, Siegert).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 42. Thyracont Vacuum Instruments GmbH (C1.848)
- Gebiet/Ort: Bayern – Passau | Quellen: `electronica/ergebnisse/tom_batch_56.md`, `tina_batch_56.md`
- Was wird gebaut (Tom): Vakuumsensoren (Piezo, Pirani, kapazitiv, Kaltkathode, Heißkathode), Vakuumschalter, Transmitter (Smartline, analog/RS485/Profinet/EtherCAT), Kompakt-Messgeräte, Anzeige- und Steuergeräte, Zubehör (S). Typisch vergossen/verklebt (A) …
- Verguss laut Tom: Hoch, Stufe A. Einzelbewertung: Transmitter/Drucksensoren Hoch (A, Produkttyp Block A), Sensorköpfe (Piezo, Kaltkathode) Hoch (A), Anzeige-/Steuergeräte Mittel (A), Zubehör Niedrig (A). Einschätzung …
- Offener Auftrag (Tina): (a) Fertigung Passau mit V belegen: Firmenwebsite thyracont-vacuum.com Unternehmens-/Karriereseite, Impressum, Produktionsfotos/Stellenanzeigen Montage. (b) Gehäuse/Elektronik der Transmitter (Smartline, VD800): Datenblatt auf Vergossen/Verklebt/Dichtung lesen. (c) Eigentümer/Konzern prüfen und gegen CRM abgleichen (Sitzregel-Voraussetzung). (d) Patente: Google Patents + Espacenet + DEPATISnet, Anmelder "Thyracont …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 43. TIRA GmbH (A4.554)
- Gebiet/Ort: Rest Deutschland+Niederlande – Schalkau, Thüringen | Quellen: `electronica/ergebnisse/tom_batch_56.md`, `tina_batch_56.md`
- Was wird gebaut (Tom): elektrodynamische Schwingprüfsysteme (Shaker von 9 N bis 300 kN, wassergekühlt), Modalerreger, Wuchtmaschinen, Materialprüfsysteme (S). Typisch vergossen/verklebt (A): Erreger- und Schwingspulen (Block A, Spulen) …
- Verguss laut Tom: Hoch, Stufe A. Einzelbewertung: Erreger-/Schwingspulen Hoch (A, Produkttyp Block A), Leistungsverstärker und Netzteile Mittel (A), Steuer-/Messelektronik Mittel (A), mechanische Teile Niedrig (A) …
- Offener Auftrag (Tina): (a) Stellenanzeige PDF (tira-gmbh.de/fileadmin/.../TIRA_Stellenanzeige_Mechatroniker_Industriemechaniker_01_2024.pdf) im Browser lesen, Zitat Montage Schalkau sichern (Fertigung V). (b) Datenblätter/Broschüre: Werden Erregerspulen und Leistungselektronik vergossen/imprägniert? (c) Patente Google Patents/Espacenet/DEPATISnet, Anmelder "TIRA GmbH".
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 44. TOELLNER Electronic Instrumente GmbH (A4.524)
- Gebiet/Ort: Rest Deutschland+Niederlande – Herdecke, Nordrhein-Westfalen | Quellen: `electronica/ergebnisse/tom_batch_56.md`, `tina_batch_56.md`
- Was wird gebaut (Tom): programmierbare DC-Netzgeräte, Labornetzgeräte (linear und Schaltnetzteil, 160 W bis 5200 W), elektronische Lasten, Breitband- und 4-Quadranten-Verstärker, Funktionsgeneratoren, Sonderausführungen (elektronischer Schalter …
- Verguss laut Tom: Hoch, Stufe A. Einzelbewertung: Isolationstransformator Hoch (A), Netzteile/Leistungsstufen Hoch (A, Block A), Verstärker Mittel (A), Funktionsgeneratoren (Elektronik) Niedrig bis Mittel (A), Gehäuse …
- Offener Auftrag (Tina): (a) Fertigung Herdecke mit V belegen: Firmenwebsite, Impressum, Stellenanzeigen Elektronikfertigung/Montage (Anzeige der Firma selbst nicht gefunden: Karriereseite im Browser lesen). (b) Datenblätter der Netzgeräte: Vollverguss, Trafo-Imprägnierung, Gehäuse. (c) Patente Google Patents/Espacenet/DEPATISnet, Schreibvarianten Toellner/Töllner.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 45. VX Instruments GmbH (A4.317)
- Gebiet/Ort: Bayern – Landshut | Quellen: `electronica/ergebnisse/tom_batch_60.md`, `tina_batch_60.md`
- Was wird gebaut (Tom): Mess- und Testsysteme für Leistungshalbleiter (SiC, GaN), Waveform-Digitizer, Generatoren, Source-Measure-Units in PXI/PXIe/VXI-Formaten. Typisch vergossen/verklebt (A): Hochspannungs-Prüfmodule, Netzteile, Trafos im 19-Zoll-Gerät …
- Verguss laut Tom: Mittel, Stufe A. Einzelbewertung: Hochvolt-/Leistungs-Prüfmodule Mittel (A), Netzteile/Trafos zugekauft Mittel (A, Endprodukt-Regel), Steckkarten (PCBA) Niedrig (A), 19-Zoll-Gehäuse Niedrig (A).
- Offener Auftrag (Tina): Impressum/Standortseite von vxinstruments.com lesen: nur Landshut oder auch Altdorf? Datenblatt zu Hochspannungs-SMU/Netzteilmodulen auf Verguss/Vergussmasse; Stellenanzeige Landshut Elektronikfertigung im Volltext. Patentsuche 2 mit Variante "VXI Instruments".
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

### 46. Winkler AG (C1.134)
- Gebiet/Ort: Baden-Württemberg – St. Leon-Rot | Quellen: `electronica/ergebnisse/tom_batch_60.md`, `tina_batch_60.md`
- Was wird gebaut (Tom): elektrische Heizsysteme: Behälterbeheizung, Heizhauben, Heizmatten und -manschetten, Heizschläuche, Silikonheizelemente, Temperaturregler, Ex-Schutz-Produkte (ATEX), komplette Plug-and-play-Heizlösungen mit Sensoren und Reglern (S) …
- Verguss laut Tom: Hoch, Stufe A. Einzelbewertung: Silikonheizelemente/Heizmatten Hoch (A, Endprodukt-Regel "Heizelement"), Ex-Schutz-Anschlüsse Hoch (A, Block A "Ex-Schutz"), Temperaturregler Mittel (A) …
- Offener Auftrag (Tina): Impressum winkler.org/winkler.eu im Browser lesen (Sitz, Fertigung St. Leon-Rot vs. Heidelberg); Datenblatt Silikonheizelemente/Ex-Anschlussdosen auf Verguss/Einbettung/Verklebung; Karriereseite Produktion/Montage. Patentsuche 2 (DEPATISnet, Anmelder "Winkler AG").
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz (V)  [ ] Verguss/Klebung/Dichtung am Produkt  [ ] Patente (Google/Espacenet/DEPATISnet)  [ ] Wettbewerbereinsatz  [ ] Konzern/mehrere Werke  [ ] CRM-Abgleich wiederholt

