# Übergabe: WoTS 2026 – Lead-Recherche (Tom/Tina), Stand 2026-10-05

Diese Datei reicht, um die Arbeit in einer neuen Claude-Session (Claude Code, claude.ai oder GitHub-Umgebung) nahtlos fortzusetzen. Alle Zwischenergebnisse liegen als Dateien im Projektordner (Index unten).

## 1. Auftrag (Jey)
Aussteller der Messe WoTS 2026 (https://fhi.nl/en/wots/exposanten/) durch Stufe 1 (recherche-mitarbeiter, "Tom") und Stufe 2 (recherche-pruefer, "Tina") laufen lassen. Vorgaben:
- Tiefgreifende Fragen wie üblich: Produktbeschreibungen/Datenblätter/Karriereseiten der Firmenwebsite lesen.
- **AKTUALISIERT 2026-10-05 (verbindlich, ersetzt die ursprüngliche Zwei-Quellen-Vorgabe):** Eine zweite Quelle zur Fertigung ist NICHT nötig. Geprüft wird nur: was wird in DE/AT/NL hergestellt und woraus besteht es. Steckt im Produkt etwas, das in der Regel vergossen wird (z. B. Sensor ~99 %), ist die Firma GRÜN – auch ohne Eigenverguss-Beleg. Neubewertung aller Leads: `wots_ergebnisse/NEUBEWERTUNG_gruen_regel.md` (20 GRÜN, nach Jeys Bestätigung vom 2026-10-06 zusätzlich 5 GRÜN = BINDER, Amixon, Brooks Steißlingen, Eppendorf, Hettich – auch zugekaufte verbaute vergossene Bauteile zählen, weil die Firmen selbst mit dem Vergießen anfangen könnten; plus 9 GRÜN-Grenzfälle, siehe Neubewertungsdatei). Hinweis: Die Statuszeilen unten ("kein Lead GRÜN") stammen aus der alten Regel und sind durch die Neubewertung überholt.
- (alt) Doppelte Prüfung lokale Fertigung NL/DE/AT: mindestens zwei UNABHÄNGIGE Quellen – gilt nicht mehr.
- **Patente** zu Verguss/Verkapselung/Verpotten (Google Patents, Espacenet, DEPATISnet), Anmelder = Firma/Konzern.
- **Endprodukt-Regel:** Auch wenn die Firma nicht schreibt, dass sie selbst vergießt – steckt im fertigen Produkt ein vergossenes Bauteil, ist der Lead sofort interessant (siehe `efx_verguss_wissensbasis.md`, Abschnitt E). Immer trennen: "Endprodukt enthält vergossenes Teil" vs. "Firma vergießt selbst".
- Fakten-Regel: Unbelegtes als Einschätzung kennzeichnen; kein GRÜN ohne zwei unabhängige Fertigungsquellen UND direkten Verguss-/Bonding-Beleg.
- Arbeitsweise: **batchweise, einer nach dem anderen** (Nutzungslimit!). Nicht 14 Agenten parallel.

## 2. Wichtige Fakten
- **Messe:** WoTS 2026 war **22.–25.09.2026, Jaarbeurs Utrecht** (Hallen 7–11), nicht Eindhoven (Primärquelle fhi.nl/en/wots). Messe ist vorbei -> in Mails nur rückblickender Bezug ("Sie waren auf der WoTS 2026 vertreten"), keine Stand-Einladung.
- **Websuche-Limit:** Subagenten hatten ein Limit von 200 WebSearch-Aufrufen/Session (`CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`) und später ein Session-Limit (Reset 15:30). Folge: Patentrecherche bei Tom meist nur oberflächlich (Google Patents), Tina-Läufe 01/02/06/08/10/11 ohne Web. "Keine Treffer" ≠ Gegenbeweis.
- **Aussteller:** 440 gesamt (130 Electronics, 144 Industry, 164 Laboratory, 2 Mischwelten). Vorauswahl: 119 Firmen in 14 Batches (`wots_batches/batch_01..14.md`); aussortiert: Distributoren, Software/Beratung, Studententeams, Prüfgeräte/PCB-Händler, reine Labor-Verbrauchsmaterial-Firmen.
- **Zielregion:** Fertigung in DE/AT/NL. Zielgruppe: Demak-Geschäftsbereiche (E-Mobility Potting, Electrical Insulation, LED Encapsulation, Optical Bonding, FIPFG/Gasketing, Kromex/Doming) – siehe Memory `demak-produktportfolio`.
- **CRM-Abgleich:** `bekannte_firmen_DE-AT-NL.txt`, `bekannte_kontakte_DE-AT-NL.txt`, `kundendatenbank_export.txt`. Regel: Kern-Name nach Normalisierung identisch -> BEKANNT; gleicher Kern, anderes Land (z. B. Benelux-Tochter eines DE-Konzerns) -> "unklar/konzernbekannt", nicht als neu aufnehmen, Einheit vor Kontakt manuell klären.
- **ACHTUNG Datenschutz bei GitHub:** CRM-Dateien (`bekannte_*.txt`, `kundendatenbank_export.txt`, `*.xlsx`, `email-entwuerfe/`) enthalten Kunden-/Personendaten -> NICHT in ein öffentliches Repo. Nur in ein privates Repo oder gar nicht hochladen.

## 3. Workflow der Kette
0. (optional) LinkedIn-Vorstufen 0a/0b · 1 recherche-mitarbeiter (Tom) · 2 recherche-pruefer (Tina) · 3 email-autor · 4 email-pruefer · 5 finale-qualitaetskontrolle (verschickt nie selbst; Freigabe durch Jey). Agent-Definitionen: `.claude/agents/*.md` (für Fortsetzung in anderer Umgebung diesen Ordner mitnehmen). Messe-Modus von Stufe 1 steht in `01-recherche-mitarbeiter.md` ("MESSE-MODUS"), Wissensbasis in `efx_verguss_wissensbasis.md`.

## 4. Stand der Ergebnisse (Dateien in `wots_ergebnisse/`)
| Batch | Tom (Stufe 1) | Tina (Stufe 2) |
|---|---|---|
| 01 | tom_batch_01.md | in `tina_batches_01-02-06-08-10-11_ohne_web.md` (ohne Web) |
| 02 | tom_batch_02.md | dito |
| 03 | tom_batch_03.md | tina_batch_03.md (mit Web) |
| 04 | tom_batch_04.md | tina_batch_04.md (mit Web) |
| 05 | tom_batch_05.md | tina_batch_05.md (mit Web) |
| 06 | tom_batch_06.md | in Sammeldatei (ohne Web) |
| 07 | tom_batch_07.md | tina_batch_07.md (mit Web) |
| 08 | tom_batch_08.md | in Sammeldatei (ohne Web) |
| 09 | tom_batch_09.md | tina_batch_09.md (mit Web, fertig) |
| 10 | tom_batch_10.md | in Sammeldatei (ohne Web) |
| 11 | tom_batch_11.md | in Sammeldatei (ohne Web) |
| 12 | tom_batch_12.md | tina_batch_12.md (mit Web, fertig) |
| 13 | tom_batch_13.md | nicht nötig (fast nur bekannte Konzerne) |
| 14 | tom_batch_14.md | nicht nötig (beide bekannt) |

## 5. Lead-Übersicht (Stand: Tom + Tina, kein einziger GRÜN)
**Mit direktem Verguss-/Bonding-Beleg (Tom/Tina laut Quellenzitat; Fertigung noch nicht zweifach unabhängig belegt) – höchste Nachprüf-Priorität:**
- A1 Electronics (Almelo) – Potting/Conformal Coating; GELB. Metis Group (Gimv) gemeinsam mit AME (CRM bekannt) und Variass -> Ansprache abstimmen.
- ETI / ARA Industries (Aalten) – Imprägnierung/Potting/Vakuumverguss auf eti.nl; GELB, Lead = ETI.
- Axtron (Maarsbergen) – "Coating, potting, encapsulation" auf axtron.nl/diensten; GELB.
- Bestronics (Veldhoven) – "Potting and conformal coating" auf /productie/; GELB.
- Hortec Electronics (Oldenzaal) – "ingegoten (potting)" auf hortec.nl/manufacturing-services (Tina bestätigt); GELB.
- Dytos (Zoetermeer) – Optical Bonding "entirely in our production facility in the Netherlands" (Tina bestätigt); GELB (Bereich Optical Bonding).
- SCHURTER Electronics B.V. (Hardenberg) – Optical Bonding/LOCA im Reinraum; "Kunde interessant" (Tina 09 steht aus).
- TFT-solutions (Barendrecht) – Optical Bonding der Z-Serie; Ort des Bondings offen; GELB.

**Produkttyp-Ableitung (Verguss nur Einschätzung), GELB:** Sentech (Nieuwkuijk, Fertigung 3 Quellen), SIGMATEK (Lamprechtshausen AT, Fertigung belegt einfach; neu aus Batch 07), Bronkhorst, Klay Instruments, CS Instruments (Lead = Tannheim BW), KNF Neuberger (Freiburg-Munzingen, Fertigung 2 Quellen belegt), Insyte, Intemo, KITT, Makso, AE Sensors, Althen, Demcon, Hetronic (nur Gesprächsaufhänger), Wefabricate, Variass, Conta-Clip, HELU (nur Konzern DE), AVT, AEMICS, Amixon, Brooks Automation Steißlingen, Thermo-Electra, Norgren, METZ CONNECT (CRM "metz GmbH" klären), Sommer Benelux (Lead eher Partner Freiberg), VACUUBRAND/JULABO/Analytik Jena/Eppendorf/BINDER/Hettich (Batch 12, Tina fehlt).

**BEKANNT / Konzern im CRM (nicht neu ansprechen):** ISE Magnetics, AME, VDL TBP/Rena (Leads-Tab unbearbeitet -> Entscheidung Jey), Bernstein, Mach Technology, ifm, Turck, Endress+Hauser (Verguss patentbelegt US11375633), KROHNE, HIWIN, Bihl+Wiedemann, EUCHNER, SAMSON, Schmersal, WAGO, Weidmüller, WERMA, HABIA/HEW-KABEL (Habia Cable gehört seit 14.10.2022 zu HEW-KABEL Holding), Freudenberg, Bürkert, JUMO, Festo, Danfoss, AUMA, Bender, Phoenix Mecano, Betronic (Zwaag = ex Expice B.V., im CRM Z. 755).

**ROT / kein Lead:** Distributoren, Design-Häuser, Software, Wettbewerber (DATRON), u. a. Kendrion 3T, Inscope, Intronics, Isatronick, Koetje, Productronics, Maas CPS, Rioniz, Logic, Novatrace, Romex, Binder Nederland (Vertrieb), Ideetron (Eigenprodukt-Claim falsch: RFI Engineering), Frontfolies, EEMC, Formit, InduCompWare, Tele Radio Benelux, Rotero, Roxtec, Led techno, LECO, Husk, Gascontrol, HellermannTyton, HIMA, Georg Fischer, AWH, amber Tech, Subtecto, Tricas, Vention, VI Tech, Tooltronics, Comdes, BMF, Brunelco, Contecto, Baulds (letztere beide zurück an Stufe 1).

## 6. Offene Aufgaben (in dieser Reihenfolge, EIN Batch nach dem anderen)
1. (erledigt) Tina Batch 09 -> `tina_batch_09.md`. Neu daraus: Buschjost GmbH (Bad Oeynhausen, IMI/Norgren) als Neu-Lead; Norgren B.V. und Sommer Benelux ROT/zurück an Stufe 1; METZ-Patent zählt NICHT als Verguss-Beleg; CRM "metz GmbH" und "IMI" im CRM prüfen.
2. (erledigt) Tina Batch 12 -> `tina_batch_12.md`: 6 GELB (VACUUBRAND, JULABO [Lead JULABO GmbH Seelbach], Analytik Jena [E+H-Konzernbezug], Eppendorf, BINDER, Hettich), 3 ROT; kein Eigenverguss belegt.
3a. (Portion 1 erledigt, siehe `wots_ergebnisse/web_nachpruefung_portion_1.md`): Axtron Potting in-house BELEGT (axtron.nl/diensten/specials/, Browser gelesen); A1 Potting via Gimv belegt + Metis-Gruppe mit AME; ETI Verguss NICHT belegt (Standardtrafos IP00) -> abgewertet. WICHTIG: WebFetch-Zusammenfassungen liefern falsche Negativbefunde -> Unterseiten im Browser gegenlesen.
3. Web-Nachprüfung der restlichen Top-Leads (Bestronics, TFT-solutions, Bronkhorst, CS Instruments, KNF, SIGMATEK, Sentech, Dytos, Hortec, SCHURTER; alle noch offen), je 3–4 Firmen pro Lauf, mit zwei unabhängigen Fertigungsquellen (KvK/Handelsregister/Stellenanzeige/Presse) + Patentabfrage (Espacenet/DEPATISnet mit Anmelderfilter) + Datenblatt/IP: A1, ETI, Axtron, Bestronics, TFT-solutions, Bronkhorst, CS Instruments, KNF, SIGMATEK (Firmenbuch, P-DIAS-Datenblatt), Sentech, Dytos, Hortec, SCHURTER.
4. Jey-Entscheidungen: (a) Messebezug nur rückblickend ja/nein; (b) Benelux-Töchter bekannter Konzerne (AUMA, Bender, Bürkert, JUMO, Festo, Danfoss, Phoenix Mecano, HABIA, Freudenberg) bekannt = ja/nein; (c) VDL Rena (Leads-Tab, unbearbeitet) in die Kette?; (d) Metis-Gruppe (A1/AME/Variass) gemeinsam ansprechen?
5. Danach Stufe 3 (email-autor) NUR für freigegebene GRÜN/GELB-Firmen; je Firma die Liste "nicht verwendbar" aus den Tina-Berichten beachten (z. B. keine MA-/Umsatzzahlen, keine Verguss-Behauptung ohne Beleg, keine nicht verifizierten Ansprechpartner).

## 7. Prompt zum Weitermachen (in neue Claude-Session einfügen)
> Lies `UEBERGABE_WoTS_2026.md` und die Dateien in `wots_ergebnisse/`. Setze die WoTS-2026-Recherche fort: arbeite die offenen Aufgaben aus Abschnitt 6 strikt batchweise ab (immer nur ein Agent-Lauf gleichzeitig), speichere jedes Ergebnis sofort als Datei in `wots_ergebnisse/`, halte dich an Fakten-Regel, Zwei-Quellen-Regel für Fertigung NL/DE/AT, Patent-Check und Endprodukt-Regel. Messe war 22.–25.09.2026 in Utrecht (vorbei). Verschicke nichts; Freigaben macht Jey.

## 7b. Hauptergebnis (Stand 2026-10-06)
**`WoTS_2026_Aussteller.xlsx`** = die fertige Messeliste im gewohnten Format (alle 440 Aussteller mit Ampel GRÜN/GELB/ROT; 44 GRÜN davon 23 neu + 21 CRM-bekannt, 20 GELB, 376 ROT; Blätter: Aussteller, Laufliste GRÜN+GELB nach Halle/Stand, Zusatz-Leads ohne Stand [SIGMATEK, Buschjost, CS Instruments GmbH, JULABO GmbH, Binder, Sommer GmbH], Legende & Regeln). Stufe 3 (E-Mails) ist von Jey NICHT gewünscht – nur die Liste.

## 7c. NEUER AUFTRAG Drohnen + Humanoide (Stand 2026-10-06)
Auftrag/Regeln: `AUFTRAG_Drohnen_Humanoide.md`. Ergebnisse in `drohnen_humanoide/`: Batch 1 Drohnen-OEMs (`tom_batch_1_drohnen_oems.md`), Batch 2 Humanoide-OEMs (`tom_batch_2_humanoide_oems.md`), Batch 3 Zulieferer Drohnen (`tom_batch_3_zulieferer_drohnen.md`) – alle Stufe 1, Tina-Prüfung steht aus. **Batch 4 (Zulieferer Humanoide) NICHT gestartet** (Start im Auto-Mode blockiert) – Prompt-Vorlage: gleiche Struktur wie Batch 3, Quellen humanoids.fyi/GitHub-Atlas (Zulieferer: Infineon, SKF, Ewellix, Bosch Sensortec, Maxon, Harmonic Drive, Rollvis, Schaeffler), Kategorien Aktuatoren/Motoren/Wicklungen, Getriebe, Sensorik (Kraft-/Momentsensoren, Encoder), Servo-/Leistungselektronik/EMS, Akku/BMS, Hände/Greifer/Kabel, Kühlung/Dichtungen; Ziel 20-30 Firmen nach Gebiet BW/Bayern/Rest DE (AT/NL getrennt). Danach: Tina je Batch (einzeln), dann Excel (Ampel + 3 Gebiete, Format wie `WoTS_2026_Aussteller.xlsx`). Offene Annahme: "3 Vertriebsgebiete" = BW / Bayern / Rest Deutschland.

## 8. Dateiindex
- `WoTS_2026_Aussteller.csv` – alle 440 Aussteller (Stand, Adresse, Branche, Website, CRM-Treffer)
- `wots_batches/batch_01..14.md` – Eingabe je Batch · `wots_ergebnisse/` – Tom/Tina-Ergebnisse
- `efx_verguss_wissensbasis.md` – Verguss-Wissensbasis (A–E) · `.claude/agents/` – Agent-Definitionen
- CRM (nicht öffentlich teilen): `bekannte_firmen_DE-AT-NL.txt`, `bekannte_kontakte_DE-AT-NL.txt`, `kundendatenbank_export.txt`, `Demak_Kunden_Datenbank.xlsx`
