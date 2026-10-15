# all about automation Düsseldorf 2026 – Ergebnis Tom v2 + Tina v2 (Stand 2026-10-15)

235 Aussteller laut Liste. 41 davon stehen bereits im CRM (`aaa_nicht_aufgenommen.md`), 54 wurden in der Triage aussortiert (Händler, Software, Beratung, Verbände, Fertigung nur außerhalb DE/AT/NL; `aaa_ergebnisse/triage_0X.md`). **127 Firmen wurden von Tom und Tina geprüft: 25 GRÜN, 100 GELB, 2 ROT.** Vollständige Tabelle mit allen 127: `aaa_liste_ergebnis.csv` (Excel, Semikolon-getrennt).

## Wichtig zur Belastbarkeit (bitte vor Weitergabe lesen)

- **Alle Ampeln sind vorläufig.** In dieser Cloud-Umgebung standen weder Browser (Chrome) noch WebFetch noch Patentdatenbanken zur Verfügung; es gab nur Websuche-Treffer (je Agent ca. 20–30 Abfragen). Es gibt daher **keine einzige Aussage der Belegstufe V** (selbst gelesene Quelle). Kein GRÜN ist mailtauglich.
- **GRÜN heißt hier nur:** Sitzregel (Industrie-/Gerätebauer mit erkennbarem Standort in DE/AT/NL) plus ein Produkttyp, der typisch Vergossenes/Verklebtes enthält. Nicht belegt ist, dass die Firma tatsächlich selbst fertigt oder vergießt.
- **Pflicht-Patentrecherche (F5) ist bei allen Firmen offen** (Google Patents, Espacenet, DEPATISnet waren nicht erreichbar). "Keine Treffer" ist kein Befund.
- **Wettbewerbereinsatz (F6)** wurde meist nur gegen `wettbewerber_referenzen.md` und mit 1 Suche geprüft.
- **Gelb ist hier der Normalfall:** Nach den v2-Regeln führt fehlender Beleg zu Gelb mit Nachrecherche-Auftrag, nicht zu Rot. Die Aufträge stehen in der CSV.
- **Empfehlung:** Die Nachrecherche (Schleife P) und die Patentsuche mit Browser nachholen, in einer Umgebung mit Chrome (z. B. lokal bei dir).

## GRÜN (25, vorläufig, alle zur Stichprobe durch Jey)

| Firma (Stand) | Gebiet | Segment | CRM | Zeile |
|---|---|---|---|---|
| ACD Elektronik GmbH (511) | Baden-Württemberg (Achstetten); Gruppe hat weitere … | Optical Bonding (Touch-/HMI-Displays an Handhelds und Safety-Panels), … | neu (Grep "ACD", "acd " in beiden Dateien: kein Treffer; … | 4 |
| ACI Laser GmbH (206) | Rest Deutschland+Niederlande (Grammetal OT Nohra, Thüringen) | Electrical Insulation (Steuer-/Treiberelektronik, Netzteile der Lasersysteme), … | neu (Grep "aci laser", "aci ": kein Treffer in beiden … | 4 |
| AIRTEC Pneumatic GmbH (220) | Baden-Württemberg (Fertigung im Technologiezentrum … | Electrical Insulation (Magnetspulen der Ventile, Ventil-Terminals mit … | neu (Grep "airtec": kein Treffer in beiden Dateien). … | 4 |
| AIXONTEC GmbH (111) | Rest Deutschland+Niederlande (Aachen, NRW) | Electrical Insulation (Kabelkonfektion, überspritzte/vergossene Steckverbinder, … | neu (Grep "aixontec", "aix": kein Treffer; Schwestermarke … | 4 (Sitzregel) |
| Armbruster Engineering GmbH & Co. KG (620) | Rest Deutschland+Niederlande (Bremen); weitere Standorte … | kein klarer Bereich (digitale Montageassistenz, Systemintegration); Randfall … | neu (Grep "armbruster": kein Treffer in beiden Dateien) | 4 |
| BAT Maschinenbau GmbH (418) | Rest Deutschland+Niederlande (Meinerzhagen, NRW) | Electrical Insulation / E-Mobility Potting (Endprodukt: … | neu (crm_abgleich.py "BAT Maschinenbau GmbH": kein Treffer) | 4 (Sitzregel) |
| CETA Testsysteme GmbH (230) | Rest Deutschland+Niederlande (Hilden, NRW) | Electrical Insulation (Drucksensoren, Messelektronik, Netzteile in … | neu (crm_abgleich.py "CETA Testsysteme": kein Treffer) | 4 (Sitzregel) |
| CONTA-CLIP Verbindungstechnik GmbH (224) | Rest Deutschland+Niederlande (Hövelhof, NRW) | Electrical Insulation (Klemmen/Anschlusstechnik für Leistungselektronik, … | neu (crm_abgleich.py "CONTA-CLIP Verbindungstechnik": kein … | 4 (Sitzregel) |
| Dreisbach & Jungmann GmbH & Co. KG (826) | Rest Deutschland+Niederlande (Lüdenscheid, NRW) | Electrical Insulation (Heizelemente, Sensorik, Steuerelektronik in Öfen) | neu (crm_abgleich.py "Dreisbach & Jungmann": kein Treffer) | 4 (Sitzregel) |
| EXTRA Computer GmbH (242) | Baden-Württemberg (Giengen an der Brenz) | Optical Bonding (Panel-PC-Displays, Touch), FIPFG/Gasketing (Gehäuse Rugged … | neu. crm_abgleich.py mit "EXTRA Computer GmbH", "exone", … | 4 (Sitzregel) |
| FIBRO Rundtische GmbH (134) | Baden-Württemberg (Weinsberg) | Electrical Insulation (Encoder/Auswertemodul S.E.M., Antriebselektronik), … | neu. crm_abgleich.py mit "FIBRO Rundtische GmbH", "FIBRO", … | 4 (Sitzregel) |
| Georg Schlegel GmbH & Co. KG (120) | Baden-Württemberg (Dürmentingen); Schwesterwerk Leipzig … | LED Encapsulation (LED-Leuchttaster/Leuchtmelder), Electrical Insulation … | neu. crm_abgleich.py mit "Georg Schlegel GmbH & Co. KG", … | 4 (Sitzregel) |
| GMK Electronic Design GmbH (203) | Bayern (Wernberg-Köblitz, Oberpfalz) | Optical Bonding (Touch-Keyboards mit Glasfront), FIPFG/Gasketing … | neu. crm_abgleich.py mit "GMK Electronic Design GmbH", … | 4 (Sitzregel) |
| GRIP GmbH Handhabungstechnik (238a) | Rest Deutschland+Niederlande (Dortmund, NRW) | Electrical Insulation (elektrische Greifer, Sensorik, Kontaktmodule), … | neu. crm_abgleich.py "GRIP GmbH Handhabungstechnik" und … | 4 (Sitzregel) |
| H. Zander GmbH / Hermann Zander GmbH & Co. KG (217) | Rest Deutschland+Niederlande (Aachen, NRW) | Electrical Insulation (Sicherheitsrelais, Netzteile, Schaltgeräte, Sensorik), … | neu. crm_abgleich.py mit "H. Zander GmbH", "Hermann Zander … | 4 (Sitzregel) |
| INperfektion GmbH (717) | prüfenswert | Rest Deutschland+Niederlande (Wegberg, NRW) | Electrical Insulation (Elektronikbaugruppen, Steuerungen), nachrangig … | neu (crm_abgleich.py "INperfektion GmbH", "item": kein … | 4 (Sitzregel) |
| Janitza electronics GmbH (114) | interessant | Rest Deutschland+Niederlande (Lahnau, Hessen) | Electrical Insulation (Stromwandler, Messgeräte, Netzteile, … | neu (crm_abgleich.py "Janitza Electronics GmbH": kein … | 4 (Sitzregel) |
| measX GmbH & Co. KG (610) | Rest Deutschland+Niederlande (Mönchengladbach/Aachen) | Electrical Insulation (Mess-/Prüfelektronik, Schaltschränke), nachrangig | neu. crm_abgleich.py "measX": kein Treffer in … | 4 (Sitzregel) |
| MKC Michels & Kleberhoff Computer GmbH (711) | Rest Deutschland+Niederlande (Wuppertal, NRW) | Electrical Insulation (Elektronikbaugruppen, Controller, I/O-Module), … | neu. crm_abgleich.py "MKC Michels & Kleberhoff Computer": … | 4 (Sitzregel) |
| Müller Maschinentechnik GmbH (534) | Rest Deutschland+Niederlande (Düren, NRW) | Electrical Insulation (Ventil-/Steuerungselektronik in Handhabungsanlagen), … | neu (Hinweis). crm_abgleich.py "Müller Maschinentechnik … | 4 (Sitzregel) |
| Optris GmbH & Co. KG (123) | Rest Deutschland+Niederlande (Berlin) | Electrical Insulation (Temperatursensoren/Pyrometer, Messelektronik), … | neu (crm_abgleich.py "Optris GmbH & Co. KG": kein Treffer … | 4 (Sitzregel) |
| Robco GmbH (131) | Bayern (München) | Electrical Insulation / E-Mobility-nah (Gelenkmodule mit Motor, Elektronik, … | neu (crm_abgleich.py "Robco": kein Treffer, 2026-10-15) | 4 (Sitzregel) |
| SABO Elektronik GmbH (444) | Rest Deutschland+Niederlande (Schwerte, NRW) | Electrical Insulation (Steuerplatinen, Netzteile), Optical Bonding … | neu (crm_abgleich.py "SABO Elektronik": kein Treffer, … | 4 (Sitzregel) |
| SK LASER GmbH (100) | Rest Deutschland+Niederlande (Wiesbaden, Hessen) | Electrical Insulation (Laserquelle, Steuerelektronik, Netzteil), nachrangig … | neu (crm_abgleich.py "SK LASER": kein Treffer, 2026-10-15) | 4 (Sitzregel) |
| W. Gessmann GmbH (Stand 806) | interessant | Baden-Württemberg (Leingarten) | Electrical Insulation (Joystick-Sensorik, Steuerelektronik), nachrangig … | neu (crm_abgleich.py "W. Gessmann GmbH": kein Treffer; Grep … | 4 (Sitzregel) |

## ROT (2)

- **aiXbrain GmbH (316)**: neu (Grep "aixbrain": kein Treffer). Beteiligung QSC AG 25,1 Prozent seit 2019 (Suchsnippet qbeyond.de, S): Grep "qsc", "q.beyond": kein Treffer.
- **Kübler Group - Fritz Kübler GmbH (426)**: BEKANNT (CRM-Schreibweise "Fritz Kübler GmbH [DE]", bekannte_firmen_DE-AT-NL.txt Zeile 860). crm_abgleich.py "Fritz Kübler" meldet IDENTISCH; kundendatenbank_export.txt kein Treffer. Gleiche juristische Einheit sehr …

## GELB (100): Auswahl mit Rot-Kandidaten (E2/E3, nur mit V-Quelle bestätigbar)

- MEDI Kabel GmbH (132): GELB (Rot-Kandidat E2)
- NACHI EUROPE GmbH (222): GELB (Rot-Kandidat E2/E3)
- OnRobot GmbH (534): GELB (Rot-Kandidat E2/E3)
- Wagner GmbH (435) | kein Fertiger: GELB (Rot-Kandidat E2)
- Yaskawa Europe GmbH – Drives Motion Controls Division (630) | unwahrscheinlich: GELB (Rot-Kandidat E3)

Alle 100 Gelb-Firmen mit Sitz, Gebiet, CRM-Status und konkretem Nachrecherche-Auftrag: `aaa_liste_ergebnis.csv`.

## Fälle für Jey (CRM-Konzernbezug / Identität)

ABB STOTZ-KONTAKT (ABB AG im CRM), Kübler (Fritz Kübler GmbH, Rot), TRsystems (TR ELECTRONIC im CRM), ESCHA (TSL-ESCHA), Metz Connect (metz GmbH), Norgren (IMI), RK Rose+Krieger (Phoenix Mecano), Ruhrbotics (HAHN), WEG Germany (KATT), Kaiser (Kaiser Elektroplanung), Benedict (Wülfrath oder Wien), Pfannenberg/Printec-DS/red cable robots (Sitz laut Liste nicht belegt), MERECS, REFACTUM, Vision Center und Machine Creators (nicht auffindbar).

## Dateien
- `aaa_ergebnisse/tom_batch_01–13.md`, `tina_batch_01–13.md`: Detailblöcke je Firma (Felder 1–17, Quellen, Patente, Wettbewerber)
- `aaa_batches_v2/pruef_01–12.md`: Eingabe der Prüf-Batches
