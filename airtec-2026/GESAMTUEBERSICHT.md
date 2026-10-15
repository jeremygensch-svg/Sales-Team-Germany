# AIRTEC / DefenceTec / Counter-UAS 2026 (Augsburg) – Gesamtübersicht Tom (Stufe 1) + Tina (Stufe 2)

Stand: 2026-10-08. 108 Aussteller laut Liste vom 08.10.2026 in 9 Batches. Ergebnis: **0 GRÜN, 22 GELB, 86 ROT.**
Quelldateien: `batches/`, `tom/tom_batch_XX.md`, `tina/tina_batch_XX.md`. Tabelle zum Weitergeben: `liste_gelb.csv`.

## Gemeinsame Grenzen (gelten für ALLE Einstufungen)
- **Kein GRÜN:** Bei keiner Firma ist Verguss am Standort belegt; alle Verguss-Werte sind Ableitungen aus dem Produkttyp. Nach der Faktenregel höchstens GELB.
- **CRM-Abgleich nicht erfolgt:** `bekannte_firmen_DE-AT-NL.txt` und `kundendatenbank_export.txt` liegen nicht im Repo. **Vor jeder Ansprache manuell abgleichen** (Jey).
- **Patente:** nicht recherchiert (nur vereinzelt, keine Treffer). Kein Gegenbeweis.
- **Prüftiefe:** Nur WebSearch-Snippets, WebFetch/Registerabrufe nicht möglich; teils Rate-Limit. Eigenangaben von Firmen zählen als eine Quelle.
- Mitarbeiter-/Umsatzzahlen sind überwiegend nur einfach belegt: nicht verwenden.

## GELB – weiter an Stufe 3 mit Auflagen (Reihenfolge = grobe Priorität)
| Firma | Stand | Bereich | Sitz | Fertigung | Verguss (abgeleitet) | Demak-Bereich | Auflage / nicht verwenden |
|---|---|---|---|---|---|---|---|
| **Turck Beierfeld GmbH** (beste Prio) | R2300 | DefenceTec | Grünhain-Beierfeld, Sachsen | 95 % | 75–85 %; Potting/Overmolding belegt auf Ebene duotec (IVAM), Standort Beierfeld nicht | Electrical Insulation | Nicht "vergießt in Beierfeld" sagen; Mitarbeiterzahl nicht verwenden |
| **CUONICS GmbH** | P1400 | DefenceTec | Straubing, Bayern | 90 % (Eigenangabe EN 9100, Serienfertigung) | 80–90 % (Avionik) | Electrical Insulation | Potting nicht belegt; Mitarbeiterzahl nicht verwenden |
| **Becker Avionics GmbH** | N3800 | AIRTEC | Baden-Württemberg (Rheinmünster / Baden-Baden / Ettlingen widersprüchlich) | 80 % | 85 % (Avionik-Baugruppen) | Electrical Insulation | Sitz und juristische Einheit (Becker Flugfunkwerk?) vor Kontakt klären |
| **ARGUS INTERCEPTION GmbH** | P4100 | Counter-UAS | Rotenburg (Wümme), Niedersachsen | 75 % (Eigenfertigung nicht direkt belegt) | 60–70 % | Electrical Insulation / E-Mobility Potting (nur bei Bestätigung) | Produkt A1-Falke belegt; Akku-/Verguss-Bedarf nicht verwenden |
| **Compact Dynamics GmbH** | N2400 | AIRTEC | Starnberg, Bayern (Schaeffler-Tochter) | 70 % (Prototypen/Kleinserie) | 70–85 % (Statorverguss, nicht belegt) | E-Mobility Potting / Electrical Insulation | Konzern Schaeffler: Zuständigkeit klären |
| **eMoSys GmbH** | N2200 | AIRTEC | Starnberg, Bayern (100 % MTU) | 90 % (Entwicklung + Kleinserie) | unbelegt | E-Mobility Potting / Electrical Insulation | Nicht "vergießt Statoren" sagen; MTU-Einkauf evtl. zentral |
| **Variosystems Germany GmbH** | P2000 | DefenceTec | Geseke, NRW | 85 % | 50–60 %; belegt ist Parylene-Beschichtung, **kein Potting** | Electrical Insulation (nur falls Potting) | Tom-Wert "Verguss 90 %" nicht haltbar |
| **Würth Elektronik GmbH & Co. KG** | N3600 | AIRTEC | Waldenburg, Baden-Württemberg | 80 % (nicht eigenständig belegt) | 60–90 % unbelegt | Electrical Insulation / E-Mobility Potting | Juristische Einheit (KG vs. eiSos) klären; Großkonzern, Werk-/Technikebene nötig |
| **pikatron GmbH** | P3200 | DefenceTec | Usingen, Hessen | 70 % | 60–70 % (Trafos/Induktivitäten) | Electrical Insulation | Mitarbeiterzahl/Gründungsjahr widersprüchlich |
| **Rosenberger Hochfrequenztechnik GmbH & Co. KG** | R2200 | DefenceTec | Fridolfing, Bayern | 80 % | 50–85 % (Steckverbinder) | Electrical Insulation | Großkonzern; Verguss nicht als Fakt |
| **RIEGL Research & Defense GmbH** | P2100 | DefenceTec | Horn, Niederösterreich (AT) | 90 % (Gruppe) | 60–75 % | Electrical Insulation | Rechtliche Einheit (R&D GmbH vs. RIEGL Laser Measurement Systems) klären |
| **HARTING Deutschland GmbH & Co. KG** | R1000 | DefenceTec | Espelkamp, NRW (Rest DE) | ca. 80 % | ca. 50 % | Electrical Insulation (Vermutung) | Kein Defence-Bezug belegt; CRM-Abgleich besonders wichtig |
| **V4Smart GmbH & Co. KG** | R1100 | DefenceTec | Ellwangen (BW) + Nördlingen (Bayern) | 90 % | 40–60 % | E-Mobility Potting (nur Hypothese) | Zellverguss nicht verwenden; Porsche-Tochter |
| **Leonardo Germany GmbH** | N1100 | DefenceTec | Neuss, NRW (Konzern Italien) | 50 % | 60–70 % | Electrical Insulation (vermutet) | Nur über Leonardo Germany ansprechen; Beschaffungsstruktur klären; kein Massen-Email |
| **Skyeton Germany GmbH** | P1500 | DefenceTec | Sitz unbekannt (Mutter Ukraine) | ca. 10 % DE; Fertigung in DE nur geplant | ca. 60 % | Electrical Insulation / E-Mobility Potting (Vermutung) | "Fertigt in Deutschland" nicht verwenden |
| **KE-TEC GmbH** | P2600 | DefenceTec | Betzigau / Kempten, Bayern | 60 % | 30–40 % | Electrical Insulation (nur vermutet) | Identität mit Aussteller nicht verifiziert |
| **Gantner Instruments Test & Measurement GmbH** | N3000 | AIRTEC | Lauf a.d. Pegnitz, Bayern | ca. 40 % | ca. 50 % | Electrical Insulation (nur bei Eigenfertigung) | Nicht mit Schruns (AT) verwechseln |
| **THYRA GmbH** | P4200 | Counter-UAS | Darmstadt, Hessen | 40–60 % | 40 % | Electrical Insulation (hypothetisch) | Serienfertigung in DE nicht belegt (MoU betrifft Kolibri i10) |
| **CustomCells GmbH** | P1100 | DefenceTec | Itzehoe, Schleswig-Holstein | 60 % | 40 % | E-Mobility Potting (nur Pack-Ebene) | Insolvenz 2025, Tübinger Werk nicht wieder eröffnet; Eigentümer klären |
| **nVent SCHROFF** | R2100 | DefenceTec | Straubenhardt, Baden-Württemberg | 90 % | 30–45 % | FIPFG/Gasketing (nur Hypothese) | Kein FIPFG-/Vergussbeleg; niedrige Prio |
| **Effegi Elettronica S.r.l.** | N4300 | AIRTEC | Vigone (Turin), Italien | 5 % DE/AT/NL | ca. 50 % | Electrical Insulation | Außerhalb Zielmarkt; Umsatzangaben widersprüchlich |
| **HYBtronics Microsystems, S.A.** | N1000 | DefenceTec | Vitoria-Gasteiz, Spanien | 5 % DE/AT/NL | ca. 50 % | nur bei DACH-Bezug | Niedrige Prio; Produkte nicht belegt |

## ROT (86): kein Fertiger / unwahrscheinlich / nicht verifizierbar
- **Behörden, Hochschulen, Forschung, Verbände, Beratung, Verlag, Wirtschaftsförderung (kein Fertiger):** BAAINBw, InnoZBw, NSPA, DLR, Fraunhofer AVIATION & SPACE, TUM, TH Augsburg, THWS IDIS, NAAMCE, Composites United, Mobility goes Additive, Hyogo/NIRO, IRON Cluster, Ukraine Pavilion, ADSH, Augsburg Innovationspark, Regio Augsburg Wirtschaft, Wirtschaftsförderung Augsburg, VFS/H2 Advisors, Mittler Report Verlag, Hofstetter Schurack & Partner, UMS Consulting, Oannes Consulting, CR Consult, EXPERT-Security, SGS, TechnoLab, MicroGenesis, Gamma Technologies, Airbus Protect, NoMoreMines, Marple, Mark3D.
- **Unwahrscheinlich (Zerspanung, Werkzeug, Composites, Maschinenbau, Material):** Lindauer Dornier, Nippon Graphite Fiber, OXEON/TeXtreme, Dieffenbacher, Connova, CTC, CONNECTEC JAPAN, GRADEL, GROB-WERKE, Gubesch, HQW Precision, Hufschmied, Rees, KOWE CNC, LANGZAUNER, Knoepfel, IWE, JOT Automation, Parmaco, Persico, Porsche Werkzeugbau, Roth Industries, ThermHex, Thermwood, BIONTEC, BICONEX, Buchner, CMMC, Zeisberg Carbon, Drake Plastics, Formlabs, EOS, F. Zimmermann, Haltermann Carless, FFT (Wettbewerber/Lieferant), RED Aircraft (Flugmotoren, Adenau), Rheinmetall Aviation Services, Collier Aerospace.
- **Von Tina herabgestuft:** Battenberg Robotic (Prüf-/Messroboter), diondo (zugekaufte Röntgenquellen), CONDOR/GERMAN DRONES (Zuordnung/Counter-UAS-Bezug nicht belegt), PCB Piezotronics, pk components, ISP SYSTEM, INOYAD.
- **Nicht identifizierbar / nicht verifizierbar (bei Interesse manuell prüfen):** Harald Böhl GmbH (N4100), Sander Elektrische Anlagen (M1000), Tech Lab Co. (M4100), Fuji Design (M4300), Zuri.com SE (N2000), Wimedes (N3550), BIEGLO (P1000), DDTS (P4300), Marple.

## Nächste Schritte
1. CRM-Dateien bereitstellen und alle 22 GELB abgleichen.
2. Verguss am Standort belegen: Datenblätter, Stellenanzeigen, Patente (Espacenet/DEPATISnet mit Anmelderfilter) – Top-5: Turck Beierfeld, CUONICS, Becker Avionics, Compact Dynamics, Würth Elektronik.
3. Juristische Einheit/Sitz klären bei Becker, Würth, RIEGL, Leonardo, Gantner, CustomCells.
4. Danach Stufe 3 (Email-Autor) nur für freigegebene Firmen.
