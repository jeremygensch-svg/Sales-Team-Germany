# AIRTEC / DefenceTec / Counter-UAS 2026 – Tina (Stufe 2) Prüfung Batch 02 – Stand 2026-10-08

Geprüft: airtec-2026/tom/tom_batch_02.md gegen airtec-2026/batches/batch_02.md. Messe AIRTEC Augsburg laut Suchtreffern (messen.de) 20.–22.10.2026; noch bevorstehend.

## Grenzen / Lücken (bitte lesen)
- CRM-Dateien (bekannte_firmen_DE-AT-NL.txt, kundendatenbank_export.txt) fehlen im Repo -> Schritt 0 nicht durchführbar. Abgleich (inkl. "Verifiziert am") MANUELL NACHZUHOLEN vor Stufe 3. Kein CRM-Status behauptet.
- Nur WebSearch-Ergebnistexte ausgewertet; Verzeichnis-/Jobanzeigenquellen sind schwach.
- Verguss-% durchgehend aus Produkttyp abgeleitet (Wissensbasis fehlt) = nicht belegt -> keine Grün-Vergabe.
- Patente nicht recherchiert (Lücke, kein Gegenbeweis). Zwei-Quellen-Pflicht für Größenangaben nirgends erfüllt -> Größen nicht verwenden.

## Ergebnis

| Firma (Stand) | Ampel | Sitz / Gebiet (Tina) | Fertigung % | Verguss % | Demak-Bereich | Belegt / nicht verwenden |
|---|---|---|---|---|---|---|
| CUONICS GmbH (P1400, DefenceTec) | GELB | Äußere Passauer Str. 137, 94315 Straubing (Enforcetac + ProvenExpert, zwei Quellen); Bayern | 90 % – "EN 9100:2018, in-house 21G serial production" (Enforcetac, Eigenangabe), Siemens-Fallstudie bestätigt Entwicklung sicherheitskritischer Systeme (Flight Control, I/O) für Flächenflugzeuge/Hubschrauber/Drohnen; Serienstückzahl unbekannt | 80–90 % abgeleitet (Avionik-Baugruppen), Potting nicht belegt | Electrical Insulation | Belegt (Eigenangabe/Verzeichnis): Gründung 2015, Gf. Philipp Lemberger (Dealroom), DO-254/DO-178C. NICHT verwenden: Verguss/Potting, Mitarbeiterzahl ~50, Zertifizierungsumfang als unabhängig bestätigt. Kontaktperson (Gf.) laut Dealroom, Email/Telefon offen. |
| Compact Dynamics GmbH (N2400, AIRTEC) | GELB | Starnberg (Bayern); Schaeffler-Tochter (100 % seit 12/2017, electrive) -> Konzernkontext, Zuständigkeit vor Kontakt klären | 70 % – Entwicklung plus Prototypen/Kleinserie (Stellenanzeige, Schaeffler-Pressemitteilung "small volume production and motor sport"); Serienfertigung nicht belegt | 70–85 % abgeleitet (Stator/Wicklungsverguss), nicht belegt | E-Mobility Potting / Electrical Insulation | Belegt: Entwickler hochdynamischer E-Antriebe (Luftfahrt, Motorsport, Automotive), Standort. NICHT verwenden: Verguss, Mitarbeiterzahl (~95 Stellenanzeige vs. 80 Bayern-Datenbank – widersprüchlich), "90 % Fertigung". |
| CustomCells GmbH (P1100, DefenceTec) | GELB (niedrige Prio) | Itzehoe (Schleswig-Holstein, Rest DE). Korrektur: Tübingen laut electrive/battery-news NICHT wieder eröffnet; Tom nennt Serienlinie Tübingen als aktiv. | 60 % – Insolvenz 05/2025, Übernahmevereinbarung 02.07.2025 (Family-Office-Konsortium um ABACON/SALVIA); F&E und laufende Produktion in Itzehoe weiter vorgesehen; Stand 2026 nicht belegt | 40 % abgeleitet (Zellbau selbst wenig Verguss; Pack-Ebene unbelegt) | E-Mobility Potting (nur bei Pack-Fertigung) | Belegt: Insolvenz/Übernahme (chemie.de, electrive, battery-news). NICHT verwenden: Tübinger Werk, aktuelle Produktionsmengen, Mitarbeiterzahl. Juristische Einheit (neue Eigentümer/Gesellschaft) vor Kontakt manuell klären; Aussage zur Firmenlage 2026 offen. |
| diondo GmbH (P1200, DefenceTec) | ROT | Hattingen (NRW, Rest DE) | 85 % – CT-/Röntgensysteme "develops, manufactures" (Quelle: Suchtext) | 30 % abgeleitet; Hinweis, dass Röntgenquellen von Dritten stammen ("component-supplier-neutral", NDT-2024-Abstract) -> Tom 50 % nicht gehalten | – (Electrical Insulation nur bei Nachweis HV-Eigenfertigung) | Nachbesserung: Eigenfertigung von HV-Quelle/Detektormodulen klären. Größe uneinheitlich (35 PitchBook, 20+ village.ai, 10-49 Leichtbauatlas) -> nicht verwenden. |
| CONDOR / GERMAN DRONES (P4400, Counter-UAS) | ROT | Essen (NRW); CONDOR Multicopter & Drones GmbH, Gruppe CONDOR; 1-10 MA/gegr. 2019 (Verzeichnis) | nicht belegt (Gesellschaftszweck nennt Entwicklung/Herstellung, aber Hardware/Zubehör/Training als Angebot) | nicht belegt, Tom 60 % -> <=20 % | – | Zuordnung zum Aussteller weiterhin nicht verifiziert; Counter-UAS-Bezug nicht belegt. Nachbesserung: Ausstellerprofil manuell prüfen. |
| Composites United e.V. (M2140) | ROT | Berlin | 0 % | 0 % | – | Verband; kein Fertiger. Kurzbestätigung. |
| CONNECTEC JAPAN (M4200) | ROT | Myoko (Japan), außerhalb Gebiet | <=5 % | 80 % ohne DE-Fertigung | – | Außerhalb DE/AT/NL. |
| Connova AG (M2210) | ROT | Villmergen (CH); Werk Sachsen unsicher | 60 % laut Tom unbelegt | Klebstoff 40 % / Elektronik 15 % | – | Faserverbund, Fit gering. |
| CR Consult (N5500) | ROT | nicht verifiziert | unbekannt | <5 % | – | Auch Tinas Suche: kein Treffer, Ausstellereintrag nicht auffindbar. Nachbesserung: Ausstellerliste manuell. |
| CTC GmbH (M2170) | ROT | Stade (Niedersachsen) | 95 % | 30 % | – | CFK-Prozesse, kein Elektronikverguss. |
| DDTS – Drone Defense Test Systems (P4300) | ROT | nicht verifiziert | unbekannt | unbekannt | – | Tinas Suche: keine Treffer. Nachbesserung: Identität manuell klären. |
| Dieffenbacher GmbH (M2160) | ROT | Eppingen (Baden-Württemberg) | 95 % | 15 % | – | Anlagenbauer; Größenangaben (1.700 MA, >400 Mio. EUR) nicht verwendbar. |

## Kritik an Tom
- Compact Dynamics: Fertigung 90 % übertrieben, Quellen sprechen von Prototypen/Kleinserie; Verguss 85 % reine Ableitung.
- CustomCells: Tübinger Serienlinie nach Insolvenz laut Quellen geschlossen; Status der Gesellschaft 2026 offen.
- diondo: "prüfenswert" ohne Nachweis eigener Hochspannungs-/Quellenfertigung; Hinweis auf Fremdquellen.
- CUONICS: Einstufung "Kunde interessant" plausibel (Avionik-Eigenfertigung, 21G), Verguss aber nur Ableitung -> Gelb statt Grün.

## Weiter an Stufe 3
CUONICS (GELB), Compact Dynamics (GELB), CustomCells (GELB, niedrige Prio). Auflagen: CRM-Abgleich vor Kontakt manuell (Jey); Verguss- und Größenaussagen nicht verwenden; Compact Dynamics: Schaeffler-Konzernkontext beachten; CustomCells: juristische Einheit klären. Nicht weiter: alle ROT. Verifiziert am 2026-10-08 (nur teilweise, siehe Grenzen).

## Quellen
- https://www.enforcetac.com/en/exhibitors/cuonics-gmbh-2524769
- https://www.provenexpert.com/cuonics-gmbh-straubing/
- https://app.dealroom.co/companies/cuonics
- https://resources.sw.siemens.com/zh-TW/case-study-cuonics
- https://www.electrive.net/2017/12/13/schaeffler-uebernimmt-compact-dynamics-komplett/
- https://www.industrial-production.de/antriebstechnik/e-mobilitaet-schaeffler-kauft-compact-dynamics.htm
- https://www.bayern-international.de/en/company-database/company-details/compact-dynamics-gmbh-1303
- https://www.electrive.net/2025/07/03/aufkauf-insolventer-zellspezialist-customcells-findet-investor/
- https://battery-news.de/en/2025/07/04/insolvent-customcells-finds-buyer-for-core-business/
- https://www.chemie.de/news/1186624/customcells-sichert-zukunft-mit-neuen-investoren.html
- https://www.ihk.de/bochum/hauptnavigation/wirtschaft-im-revier/deep-dive-diondo-7040770
- https://pitchbook.com/profiles/company/317915-11
- https://www.bindt.org/events-and-awards/ndt-2024/abstract-2c5/
- https://implisense.com/en/companies/condor-multicopter-drones-gmbh-essen-DEMHH5W0AB82
- https://lidarmag.com/2018/03/06/drone-volt-deployed-in-germany-thanks-to-a-powerful-partnership/
- https://www.messen.de/de/7716/augsburg/airtec/info
