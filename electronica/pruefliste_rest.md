# electronica 2026 – Browser-Prüfliste für die restlichen Zielfirmen

Stand 2026-10-23. 207 Firmen aus der Außendienst-Excel (Prio A/B/C), die noch nicht im Browser geprüft sind (Spalte Prüfstand = vorläufig). Reihenfolge: Prio A (Grün-Kandidaten, vor allem Anlagenbauer), dann B, dann C, je Gebiet.

## Startanweisung für den lokalen Claude (Chrome-Erweiterung aktiv)

Vorgehen und Regeln wie in `electronica/pruefliste_gruen.md` (Startanweisung dort lesen) und `electronica/ergebnisse_browser/gruen_01.md` als Formatvorlage.
- Entscheidungen von Jey: Verbände/Prüfdienstleister/Forschung raus. Firmen im CRM (gleicher oder sehr ähnlicher Name) raus. **Anlagenbauer bleiben drin**; raus nur, wenn die Firma selbst Verguss-/Dosieranlagen baut oder vertreibt (E1, mit URL und Zitat).
- Pro Firma im Browser: Impressum/Handelsregister (Sitz), Fertigung am Sitz, Verguss/Klebung/Dichtung am Produkt, Patente (Google Patents + Espacenet), Wettbewerber-Referenzen, Konzern/mehrere Werke, CRM-Abgleich (`python3 crm_abgleich.py`).
- Pro Durchgang höchstens 10 Firmen in dieser Reihenfolge. Ergebnis: `electronica/ergebnisse_browser/rest_NN.md`, Format wie `gruen_NN.md`: Überschrift `## N. Firma (Stand)`, danach Zeile `- Ampel neu: GRÜN|GELB|ROT … Tabellenzeile D: Z` und bei Gelb `- OFFENER AUFTRAG …`.
- Nach jedem Durchgang: committen, pushen. Die Excel baut sich per `python3 tools/electronica/build_el.py` neu (liest gruen_*.md und rest_*.md automatisch; Ampel, Prio und Spalte Prüfstand werden übernommen). Dann `python3 tools/electronica/make_pruefliste_rest.py` für die verbleibende Liste.
- Keine Kontaktsuche (Regel K), nichts verschicken.

## Firmen

| Nr | Prio | Firma | Stand | Gebiet |
|---|---|---|---|---|
| 1 | A | CRS Prüftechnik GmbH | A4.611 | Baden-Württemberg (Stefan) |
| 2 | A | CTS GmbH Clima Temperatur Systeme | A4.229 | Baden-Württemberg (Stefan) |
| 3 | A | Diener electronic GmbH & Co. KG Plasma Surface Technology | B2.412 | Baden-Württemberg (Stefan) |
| 4 | A | E+H Metrology GmbH | B1.772 | Baden-Württemberg (Stefan) |
| 5 | A | FIXTEST Prüfmittelbau GmbH | A4.301 | Baden-Württemberg (Stefan) |
| 6 | A | Intego GmbH | C1.814 | Bayern (Dietmar) |
| 7 | A | Ramgraber Semiconductor Equipment GmbH | B1.171 | Bayern (Dietmar) |
| 8 | A | UniTemp GmbH | B1.156 | Bayern (Dietmar) |
| 9 | A | Walter Lemmen GmbH | A2.327 | Bayern (Dietmar) |
| 10 | A | Werner Lieb GmbH | B1.279 | Bayern (Dietmar) |
| 11 | A | GÖPEL electronic GmbH | A4.251 | Rest DE / NL (Manuel) |
| 12 | A | MK Versuchsanlagen GmbH & Co. KG | B1.822 | Rest DE / NL (Manuel) |
| 13 | A | SENTECH Instruments GmbH | B1.900 | Rest DE / NL (Manuel) |
| 14 | A | Viscom SE | A4.443 | Rest DE / NL (Manuel) |
| 15 | A | Vistec Electron Beam GmbH | B1.679 | Rest DE / NL (Manuel) |
| 16 | B | Advanced Energy Industries GmbH | C3.320 | Baden-Württemberg (Stefan) |
| 17 | B | AP&S International GmbH | B1.656 | Baden-Württemberg (Stefan) |
| 18 | B | Axon' Kabel GmbH | B3.516 | Baden-Württemberg (Stefan) |
| 19 | B | CeramTec GmbH | C2.335 | Baden-Württemberg (Stefan) |
| 20 | B | DEWETRON Deutschland GmbH | A4.547 | Baden-Württemberg (Stefan) |
| 21 | B | Ersa GmbH & Co. KG | A2.115 | Baden-Württemberg (Stefan) |
| 22 | B | FEINMETALL GmbH | A4.606 | Baden-Württemberg (Stefan) |
| 23 | B | GEMÜ Gebr. Müller Apparatebau GmbH & Co. KG | B1.718 | Baden-Württemberg (Stefan) |
| 24 | B | Inovan GmbH & Co. KG | B2.566 | Baden-Württemberg (Stefan) |
| 25 | B | Jauch Quartz GmbH | B6.201 | Baden-Württemberg (Stefan) |
| 26 | B | Keysight Technologies Deutschland GmbH | A4.506 | Baden-Württemberg (Stefan) |
| 27 | B | KRAMSKI GmbH | B2.452 | Baden-Württemberg (Stefan) |
| 28 | B | LAUDA DR. R. WOBSER GmbH & Co. KG | C2.147 | Baden-Württemberg (Stefan) |
| 29 | B | LCD Mikroelektronik GmbH | B6.431 | Baden-Württemberg (Stefan) |
| 30 | B | Leicht+Müller Syscotec GmbH | B2.261 | Baden-Württemberg (Stefan) |
| 31 | B | LXinstruments GmbH | A4.300 | Baden-Württemberg (Stefan) |
| 32 | B | Mattson International GmbH | B1.521 | Baden-Württemberg (Stefan) |
| 33 | B | MCD Elektronik GmbH | A4.232 | Baden-Württemberg (Stefan) |
| 34 | B | METZ CONNECT GmbH | A3.320 | Baden-Württemberg (Stefan) |
| 35 | B | nVent SCHROFF | B3.343 | Baden-Württemberg (Stefan) |
| 36 | B | Obducat Europe GmbH | B1.357 | Baden-Württemberg (Stefan) |
| 37 | B | POLYRACK Electronic-Aufbausysteme GmbH | B3.141 | Baden-Württemberg (Stefan) |
| 38 | B | POLYRACK TECH-GROUP Holding GmbH & Co. KG | B3.141 | Baden-Württemberg (Stefan) |
| 39 | B | Promicron AG | C1.269 | Baden-Württemberg (Stefan) |
| 40 | B | PROVERTHA Cables Connectors & Solutions GmbH | B3.100 | Baden-Württemberg (Stefan) |
| 41 | B | RAPP Kunststofftechnik GmbH | B3.141 | Baden-Württemberg (Stefan) |
| 42 | B | RENA Technologies GmbH | B1.312 | Baden-Württemberg (Stefan) |
| 43 | B | Renu Electronics GmbH | A1.645 | Baden-Württemberg (Stefan) |
| 44 | B | ROB GmbH | A1.123 | Baden-Württemberg (Stefan) |
| 45 | B | Schaffroth GmbH | B2.181 | Baden-Württemberg (Stefan) |
| 46 | B | SCHROEDER + BAUER Werkzeugbau Stanztechnik GmbH + Co. KG | B2.471 | Baden-Württemberg (Stefan) |
| 47 | B | Schweizer Electronic AG | A2.207 | Baden-Württemberg (Stefan) |
| 48 | B | Schützinger GmbH | A4.526 | Baden-Württemberg (Stefan) |
| 49 | B | SEPA EUROPE GmbH | B3.344 | Baden-Württemberg (Stefan) |
| 50 | B | Telegärtner Karl Gärtner GmbH | B3.311 | Baden-Württemberg (Stefan) |
| 51 | B | Trelleborg Sealing Solutions Germany GmbH | C1.329 | Baden-Württemberg (Stefan) |
| 52 | B | Tria Technologies GmbH | B5.103 | Baden-Württemberg (Stefan) |
| 53 | B | ACCRETECH (Europe) GmbH | B1.401 | Bayern (Dietmar) |
| 54 | B | ACTRON AG | C2.519 | Bayern (Dietmar) |
| 55 | B | Alps Alpine Europe GmbH | B4.311 | Bayern (Dietmar) |
| 56 | B | Assdev GmbH | A1.525/16 | Bayern (Dietmar) |
| 57 | B | BvR electronic GmbH | A1.525/19 | Bayern (Dietmar) |
| 58 | B | Bühler Alzenau GmbH | B1.836 | Bayern (Dietmar) |
| 59 | B | Camtek Germany GmbH | B1.510 | Bayern (Dietmar) |
| 60 | B | Chroma Germany GmbH | A4.624 | Bayern (Dietmar) |
| 61 | B | cyberTECHNOLOGIES GmbH | C1.619 | Bayern (Dietmar) |
| 62 | B | DELTEC GROUP GmbH | A1.407 | Bayern (Dietmar) |
| 63 | B | DISCO HI-TEC EUROPE GmbH | B1.201 | Bayern (Dietmar) |
| 64 | B | esmo AG | C1.241 | Bayern (Dietmar) |
| 65 | B | FrelTec GmbH | A6.100 | Bayern (Dietmar) |
| 66 | B | Hermos AG | B1.279 | Bayern (Dietmar) |
| 67 | B | INOVA Semiconductors GmbH | C5.259 | Bayern (Dietmar) |
| 68 | B | Kerafol Keramische Folien GmbH & Co. KG | C3.452 | Bayern (Dietmar) |
| 69 | B | KISCO (Deutschland) GmbH | C2.160 | Bayern (Dietmar) |
| 70 | B | Koh Young Europe GmbH | C2.329 | Bayern (Dietmar) |
| 71 | B | Kurtz Ersa Semicon GmbH | A2.115 | Bayern (Dietmar) |
| 72 | B | LEONHARD KURZ Stiftung & Co. KG | B4.301 | Bayern (Dietmar) |
| 73 | B | MEDi Kabel GmbH | B2.507 | Bayern (Dietmar) |
| 74 | B | mentec GmbH | B3.261 | Bayern (Dietmar) |
| 75 | B | MTC Micro Tech Components GmbH | B3.244 | Bayern (Dietmar) |
| 76 | B | Novomotec GmbH | B4.102 | Bayern (Dietmar) |
| 77 | B | PIC Proximity Instrumentation Controls Kontaktbauelemente GmbH | B4.319 | Bayern (Dietmar) |
| 78 | B | Plasma Parylene Systems GmbH | A2.649 | Bayern (Dietmar) |
| 79 | B | Rosenberger Group | B2.356 | Bayern (Dietmar) |
| 80 | B | Schmid-Multitech GmbH | B3.554 | Bayern (Dietmar) |
| 81 | B | Singulus Technologies AG | B1.458 | Bayern (Dietmar) |
| 82 | B | SKP Technik GmbH | A1.525/13 | Bayern (Dietmar) |
| 83 | B | SM Selbstklebetechnik GmbH & Co.KG | A1.644 | Bayern (Dietmar) |
| 84 | B | SUSS MicroTec Solutions GmbH & Co. KG | B1.600 | Bayern (Dietmar) |
| 85 | B | THORA Elektronik GmbH | B3.232 | Bayern (Dietmar) |
| 86 | B | W. L. Gore & Associates GmbH | B1.179 | Bayern (Dietmar) |
| 87 | B | Acculogic GmbH | A4.467 | Rest DE / NL (Manuel) |
| 88 | B | AEMtec GmbH | A2.319 | Rest DE / NL (Manuel) |
| 89 | B | AMSYS GmbH & Co. KG | B4.201 | Rest DE / NL (Manuel) |
| 90 | B | apra-norm Elektromechanik GmbH | B3.363 | Rest DE / NL (Manuel) |
| 91 | B | apra-plast Kunststoffgehäuse-Systeme GmbH | B3.363 | Rest DE / NL (Manuel) |
| 92 | B | Arias GmbH | B1.446 | Rest DE / NL (Manuel) |
| 93 | B | ASPINA GmbH | B4.310 | Rest DE / NL (Manuel) |
| 94 | B | ASSMANN WSW components GmbH | B2.238 | Rest DE / NL (Manuel) |
| 95 | B | ATV Systems GmbH | C1.423 | Rest DE / NL (Manuel) |
| 96 | B | Brooks Instrument GmbH | B1.766 | Rest DE / NL (Manuel) |
| 97 | B | btv technologies GmbH | B5.481 | Rest DE / NL (Manuel) |
| 98 | B | Cathedy GmbH | A5.200 | Rest DE / NL (Manuel) |
| 99 | B | CEFEG GmbH Federn- und Verbindungstechnik Chemnitz | B2.428 | Rest DE / NL (Manuel) |
| 100 | B | CEM Test Instruments GmbH | A4.568 | Rest DE / NL (Manuel) |
| 101 | B | Condair GmbH | C3.575 | Rest DE / NL (Manuel) |
| 102 | B | Coronex Electronic GmbH | A1.643 | Rest DE / NL (Manuel) |
| 103 | B | DAS Environmental Expert GmbH | B1.261 | Rest DE / NL (Manuel) |
| 104 | B | DBK EMS GmbH & Co. KG | A1.525/11 | Rest DE / NL (Manuel) |
| 105 | B | Dehner Elektronik GmbH | A5.220 | Rest DE / NL (Manuel) |
| 106 | B | DISPLAY Elektronik GmbH | B6.402 | Rest DE / NL (Manuel) |
| 107 | B | Drews Electronic GmbH | A1.525/9 | Rest DE / NL (Manuel) |
| 108 | B | ELEKTRISOLA Dr. Gerd Schildbach GmbH & Co. KG | A5.240 | Rest DE / NL (Manuel) |
| 109 | B | Elektrosil GmbH | B3.460 | Rest DE / NL (Manuel) |
| 110 | B | ELEMENT 3-5 GmbH | C1.323 | Rest DE / NL (Manuel) |
| 111 | B | EMI-tec Elektronische Materialien GmbH | B3.257 | Rest DE / NL (Manuel) |
| 112 | B | Ernst & Engbring GmbH | B2.211 | Rest DE / NL (Manuel) |
| 113 | B | Excelitas Technologies | B4.302 | Rest DE / NL (Manuel) |
| 114 | B | Finetech GmbH & Co. KG | C1.836 | Rest DE / NL (Manuel) |
| 115 | B | Gaptec Electronic GmbH & Co. KG | A5.103 | Rest DE / NL (Manuel) |
| 116 | B | Glenair GmbH | A3.125 | Rest DE / NL (Manuel) |
| 117 | B | Group Intellect Power Technology Europe GmbH | A5.418 | Rest DE / NL (Manuel) |
| 118 | B | Hürner Luft- und Umwelttechnik GmbH | C2.253 | Rest DE / NL (Manuel) |
| 119 | B | IK Elektronik GmbH | A1.525/14 | Rest DE / NL (Manuel) |
| 120 | B | Ikegami Electronics (Europe) GmbH | B5.261 | Rest DE / NL (Manuel) |
| 121 | B | IMST GmbH | C5.164 | Rest DE / NL (Manuel) |
| 122 | B | INFICON | B1.730 | Rest DE / NL (Manuel) |
| 123 | B | Intermas-Elcom GmbH | B3.342 | Rest DE / NL (Manuel) |
| 124 | B | Jintian Copper (Germany) GmbH | B2.147 | Rest DE / NL (Manuel) |
| 125 | B | Kelington Engineering (Germany) GmbH | C1.105 | Rest DE / NL (Manuel) |
| 126 | B | Kikusui Electronics Europe GmbH | A4.159 | Rest DE / NL (Manuel) |
| 127 | B | Kingbright Electronic Europe GmbH | C6.479 | Rest DE / NL (Manuel) |
| 128 | B | Kokusai Semiconductor Europe GmbH | C1.219 | Rest DE / NL (Manuel) |
| 129 | B | Kurt J. Lesker Company GmbH | B1.316 | Rest DE / NL (Manuel) |
| 130 | B | Linux Automation GmbH | C5.178 | Rest DE / NL (Manuel) |
| 131 | B | LPKF Laser & Electronics SE | A2.219 | Rest DE / NL (Manuel) |
| 132 | B | M-O-T Mikro- und Oberflächentechnik GmbH | C1.271 | Rest DE / NL (Manuel) |
| 133 | B | Magic Power Technology GmbH | A5.401 | Rest DE / NL (Manuel) |
| 134 | B | MC Technologies GmbH | C2.616 | Rest DE / NL (Manuel) |
| 135 | B | MCRT GmbH | C1.856 | Rest DE / NL (Manuel) |
| 136 | B | Metrel GmbH | A4.570 | Rest DE / NL (Manuel) |
| 137 | B | micronex GmbH | A1.525/18 | Rest DE / NL (Manuel) |
| 138 | B | MUEGGE GmbH | C2.108 | Rest DE / NL (Manuel) |
| 139 | B | N&H Technology GmbH | B3.361 | Rest DE / NL (Manuel) |
| 140 | B | NanoFocus AG | C1.553 | Rest DE / NL (Manuel) |
| 141 | B | Neosid Pemetzrieder GmbH & Co. KG | A6.500 | Rest DE / NL (Manuel) |
| 142 | B | Nikon Metrology GmbH | B1.117 | Rest DE / NL (Manuel) |
| 143 | B | NOFFZ Technologies GmbH | A4.418 | Rest DE / NL (Manuel) |
| 144 | B | PeakTech Prüf- und Messtechnik GmbH | A4.529 | Rest DE / NL (Manuel) |
| 145 | B | PMK Mess- und Kommunikationstechnik GmbH | A4.439 | Rest DE / NL (Manuel) |
| 146 | B | Precitec Optronik GmbH | C1.432 | Rest DE / NL (Manuel) |
| 147 | B | PVA TePla AG | C1.301 | Rest DE / NL (Manuel) |
| 148 | B | REEL Reinheimer Elektronik GmbH | C2.616 | Rest DE / NL (Manuel) |
| 149 | B | Rorze Engineering GmbH | B1.238 | Rest DE / NL (Manuel) |
| 150 | B | RRC power solutions | A5.218 | Rest DE / NL (Manuel) |
| 151 | B | Scanfil Electronics GmbH | A1.214 | Rest DE / NL (Manuel) |
| 152 | B | Sensitec GmbH | B4.119 | Rest DE / NL (Manuel) |
| 153 | B | Silex Technology Europe GmbH | C2.505 | Rest DE / NL (Manuel) |
| 154 | B | SIMONA AG | B1.862 | Rest DE / NL (Manuel) |
| 155 | B | SK-tronic GmbH | A1.525/24 | Rest DE / NL (Manuel) |
| 156 | B | SOLARC Innovative Solarprodukte GmbH | A5.332 | Rest DE / NL (Manuel) |
| 157 | B | TechniSat Digital GmbH | A1.435 | Rest DE / NL (Manuel) |
| 158 | B | TSI GmbH | B0.722 | Rest DE / NL (Manuel) |
| 159 | B | W+P PRODUCTS GmbH | B2.404 | Rest DE / NL (Manuel) |
| 160 | B | Werner Wirth GmbH | B2.504 | Rest DE / NL (Manuel) |
| 161 | C | Display LC Deutschland GmbH | B6.404 | Baden-Württemberg (Stefan) |
| 162 | C | elbe electronic GmbH | A1.525/6 | Baden-Württemberg (Stefan) |
| 163 | C | EMCA elektromechanische Bauteile GmbH | A3.118 | Baden-Württemberg (Stefan) |
| 164 | C | ET System electronic GmbH | A5.230 | Baden-Württemberg (Stefan) |
| 165 | C | Everlight Electronics Europe GmbH | C5.261 | Baden-Württemberg (Stefan) |
| 166 | C | hera Laborsysteme GmbH | A4.425 | Baden-Württemberg (Stefan) |
| 167 | C | Karl Enghofer GmbH & Co. KG | B2.411 | Baden-Württemberg (Stefan) |
| 168 | C | LAB14 GmbH | B1.234 | Baden-Württemberg (Stefan) |
| 169 | C | Peter HUBER Kältemaschinenbau SE | C2.229 | Baden-Württemberg (Stefan) |
| 170 | C | Schulz-Electronic GmbH | A5.214 | Baden-Württemberg (Stefan) |
| 171 | C | Shantou Goworld Display Germany GmbH | B6.421 | Baden-Württemberg (Stefan) |
| 172 | C | TRS-STAR GmbH | C4.400 | Baden-Württemberg (Stefan) |
| 173 | C | Advantech Europe B.V. | C5.302 | Bayern (Dietmar) |
| 174 | C | ai-energy GmbH | A6.620 | Bayern (Dietmar) |
| 175 | C | Aprotech GmbH | C2.352 | Bayern (Dietmar) |
| 176 | C | ATEcare Service GmbH & Co.KG | A4.346 | Bayern (Dietmar) |
| 177 | C | AUMOVIO SE | B4.A04 | Bayern (Dietmar) |
| 178 | C | BDT Bavaria Digital Technik GmbH | A1.602 | Bayern (Dietmar) |
| 179 | C | GES High Voltage GmbH | B3.320 | Bayern (Dietmar) |
| 180 | C | JDI Europe GmbH | B6.441 | Bayern (Dietmar) |
| 181 | C | Keenfinity GmbH | A1.126 | Bayern (Dietmar) |
| 182 | C | Kurtz Ersa Smart Production GmbH | A4.461 | Bayern (Dietmar) |
| 183 | C | LEDtronix - a division of LEDoptix GmbH | A1.525/23 | Bayern (Dietmar) |
| 184 | C | MAIR Elektronik GmbH | A1.431 | Bayern (Dietmar) |
| 185 | C | Puerstinger High Purity Systems GmbH | B1.761 | Bayern (Dietmar) |
| 186 | C | Schlemmer | B2.124 | Bayern (Dietmar) |
| 187 | C | SCREEN SPE Germany GmbH | B1.700 | Bayern (Dietmar) |
| 188 | C | SUYIN GmbH | B2.101 | Bayern (Dietmar) |
| 189 | C | ULVAC GmbH | B1.606 | Bayern (Dietmar) |
| 190 | C | Veeco GmbH | B1.341 | Bayern (Dietmar) |
| 191 | C | AES motomation GmbH | B1.672 | Rest DE / NL (Manuel) |
| 192 | C | AMETEK Programmable Power | A4.478 | Rest DE / NL (Manuel) |
| 193 | C | Brandenburgische Kondensatoren Technologie GmbH | nicht angegeben | Rest DE / NL (Manuel) |
| 194 | C | DETAKTA Isolier- und Messtechnik GmbH & Co. KG | B3.357 | Rest DE / NL (Manuel) |
| 195 | C | Faeth GmbH / Fäth GmbH | B1.265 | Rest DE / NL (Manuel) |
| 196 | C | FEIN Elektronik GmbH | A1.637 | Rest DE / NL (Manuel) |
| 197 | C | KITEC microelectronic technologie GmbH | B1.358 | Rest DE / NL (Manuel) |
| 198 | C | Lutronic GmbH | B2.207 | Rest DE / NL (Manuel) |
| 199 | C | Minimax Fire Solutions International GmbH | C2.112 | Rest DE / NL (Manuel) |
| 200 | C | MS Power GmbH | C2.673 | Rest DE / NL (Manuel) |
| 201 | C | ROKA - Robert Karst GmbH & Co.KG Elektrotechnische Fabrik | B2.331 | Rest DE / NL (Manuel) |
| 202 | C | Samwha Europe GmbH | A6.527 | Rest DE / NL (Manuel) |
| 203 | C | scia Systems GmbH | B1.909 | Rest DE / NL (Manuel) |
| 204 | C | SEI Interconnect Products (Europe) Ltd. | B3.519 | Rest DE / NL (Manuel) |
| 205 | C | SIIX Europe GmbH | A1.619 | Rest DE / NL (Manuel) |
| 206 | C | Song Chuan Precision Europe GmbH | A3.141 | Rest DE / NL (Manuel) |
| 207 | C | PTW Asia Pte Ltd | B1.120 | außerhalb |

## Details je Firma

### 1. CRS Prüftechnik GmbH (A4.611) – Prio A
- Gebiet/Ort: Baden-Württemberg (Stefan) – 78467 Konstanz/Bodensee | Quellen: `electronica/ergebnisse/tom_batch_12.md`, `tina_batch_12.md`
- Was wird gebaut: Prüftechnik für die Elektronikindustrie: Isolationsprüfung, statische und dynamische Tests für Leistungshalbleiter, Montagevorrichtungen, Dichtheits- und optische Tests …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Impressum/Handelsregister (aktueller Sitz, Standortzahl; Mehrwerk wäre V-pflichtig), Stellenanzeigen Montage/Elektronik, Datenblatt Prüfstation (Hochspannungsmodul, Eigenbau oder Zukauf).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 2. CTS GmbH Clima Temperatur Systeme (A4.229) – Prio A
- Gebiet/Ort: Baden-Württemberg (Stefan) – 72379 Hechingen | Quellen: `electronica/ergebnisse/tom_batch_12.md`, `tina_batch_12.md`
- Was wird gebaut: Umweltsimulationsanlagen: Temperatur- und Klimaprüfschränke, Temperaturschockschränke, Pharma-Klimakammern;
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Impressum/Standortseite cts-umweltsimulation.de (Domain unbestätigt), Stellenanzeige Hechingen, Datenblatt (Heizregister, Sensoren, Eigenbau oder Zukauf).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 3. Diener electronic GmbH & Co. KG Plasma Surface Technology (B2.412) – Prio A
- Gebiet/Ort: Baden-Württemberg (Stefan) – 72224 Ebhausen | Quellen: `electronica/ergebnisse/tom_batch_14.md`, `tina_batch_14.md`
- Was wird gebaut: Niederdruck- und Atmosphärendruck-Plasmaanlagen, Plasma-HF-Generatoren, Vakuumkammern, Vakuumsysteme, Parylene-Beschichtungsanlagen ;
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Werden HF-Generatoren und Steuerelektronik in Ebhausen entwickelt/gefertigt und vergossen? Produktseiten und Datenblätter plasma.com, Karriereseite (Elektronikfertigung) lesen. Impressum: Rechtsform, Register (HRA-Nummer aus eBay-Profil unbestätigt), Abgrenzung zur Vertriebs-KG.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 4. E+H Metrology GmbH (B1.772) – Prio A
- Gebiet/Ort: Baden-Württemberg (Stefan) – 76185 Karlsruhe | Quellen: `electronica/ergebnisse/tom_batch_15.md`, `tina_batch_15.md`
- Was wird gebaut: Messgeräte und automatisierte Mess-/Handlingsysteme für die Halbleiterindustrie (Wafer-Dicke, Ebenheit/Warp, Widerstand, Dotierungstyp;
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): Impressum und Handelsregister Karlsruhe (Gesellschafter, Eichhorn + Hausmann statt Endress+Hauser bestätigen); Datenblatt MX 20x und Stellenanzeige im Original (Sensor-Klebung/Verguss).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 5. FIXTEST Prüfmittelbau GmbH (A4.301) – Prio A
- Gebiet/Ort: Baden-Württemberg (Stefan) – 78234 Engen, Landkreis Konstanz | Quellen: `electronica/ergebnisse/tom_batch_20.md`, `tina_batch_20.md`
- Was wird gebaut: Federkontaktstifte/Prüfstifte (über 8000 Standardartikel), kundenspezifische Federkontakte, Batterie-Kontaktstifte, Hochstrom-Kontaktstifte.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): (a) Impressum fixtest.de (Rechtsform/Name, Standort Engen, V). (b) Datenblätter Kontaktstecker/Mikroschalter/Batteriekontakte: Gehäuse, IP-Klasse, Dichtung/Verguss. (c) Volltext der beiden Patente und Rechtsstand (DPMAregister).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 6. Intego GmbH (C1.814) – Prio A
- Gebiet/Ort: Bayern (Dietmar) – 91058 Erlangen | Quellen: `electronica/ergebnisse/tom_batch_27.md`, `tina_batch_27.md`
- Was wird gebaut: kundenspezifische kamerabasierte Mess- und Prüfsysteme (IR/UV, Lock-in-Thermografie, 3D-Messung, Software "Inspector") für Halbleiter, Solar, Medizintechnik, Batterie …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Anzeige Mechatroniker im Original lesen (V für Fertigungsort), Impressum Intego GmbH Erlangen (HRB Fürth), Produktseiten: welche Beleuchtung/Optik wird selbst gebaut und verklebt oder vergossen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 7. Ramgraber Semiconductor Equipment GmbH (B1.171) – Prio A
- Gebiet/Ort: Bayern (Dietmar) – 85649 Brunnthal-Hofolding | Quellen: `electronica/ergebnisse/tom_batch_44.md`, `tina_batch_44.md`
- Was wird gebaut: Nassprozess-Anlagen für Halbleiter und Solar: manuelle und automatische Reinigungs- und Ätzanlagen, Anlagen für stromloses Nickel-Bumping, Galvanikanlagen …
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Impressum/Register Ramgraber (Rechtsform, Gesellschaftsname, Sitz = Fertigung, V), Stellenanzeige Montage/Elektrik Hofolding, Datenblatt Wet-Bench/Spin-Rinser-Dryer (Heizungen, Sensorik, Dichtungen), Patente Anmelder "Ramgraber" in Espacenet/DEPATISnet. Aktion: Beobachtung; Messebesuch B1.171 vorbereiten.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 8. UniTemp GmbH (B1.156) – Prio A
- Gebiet/Ort: Bayern (Dietmar) – 85276 Pfaffenhofen a. d. Ilm | Quellen: `electronica/ergebnisse/tom_batch_58.md`, `tina_batch_58.md`
- Was wird gebaut: Rapid-Thermal-Annealing-Anlagen, Reflow-Lötöfen, Präzisions-Heizplatten, vor allem für Labore und Kleinserien.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): (a) Fertigung in Pfaffenhofen mit V belegen (Firmenseite unitemp.de, Impressum, Stellenanzeigen); Straße klären. (b) Datenblätter HP-220 und Reflow-Ofen: Heizpatronen/Heizfolien vergossen oder verklebt, Elektronik-Netzteil, Sensorik? Ohne Beleg bleibt Verguss nur A. (c) Patente Google Patents/Espacenet/DEPATISnet (Anmelder UniTemp GmbH; Stichwörter Heizplatte, Verguss, potting, Lötofen). (d) …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 9. Walter Lemmen GmbH (A2.327) – Prio A
- Gebiet/Ort: Bayern (Dietmar) – 97892 Kreuzwertheim, Unterfranken | Quellen: `electronica/ergebnisse/tom_batch_33.md`, `tina_batch_33.md`
- Was wird gebaut: Anlagen für Leiterplatten- und Oberflächentechnik (chemische Prozessanlagen, Galvanik, Belichtungsgeräte für Leiterplatten) aus Kunststoffen wie PVC, PP, PE, PVDF.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Fertigung vor Ort und Verguss/Klebung belegen; Impressum, Stellenanzeigen, Datenblätter lesen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 10. Werner Lieb GmbH (B1.279) – Prio A
- Gebiet/Ort: Bayern (Dietmar) – 96472 Rödental, Oberfranken | Quellen: `electronica/ergebnisse/tom_batch_60.md`, `tina_batch_60.md`
- Was wird gebaut: Automatisierungslösungen für Halbleiter und Leistungselektronik: EFEM (Equipment Front End Modules), Load Ports, Substrat-Handlingkomponenten, Lader- und Tray-Systeme.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Stellenanzeige (arbeitsagentur.de, Jobdetail 10000-1204428208-S) im Browser lesen = V für Montage; Datenblatt/Produktseite EFEM auf Elektronik- und Sensorbaugruppen, Impressum werner-lieb.de.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 11. GÖPEL electronic GmbH (A4.251) – Prio A
- Gebiet/Ort: Rest DE / NL (Manuel) – 07745 Jena, Thüringen | Quellen: `electronica/ergebnisse/tom_batch_23.md`, `tina_batch_23.md`
- Was wird gebaut: Elektrische und optische Prüf-/Inspektionssysteme für Baugruppen (Embedded JTAG Solutions/Boundary Scan, AOI/AXI/SPI Inspection Solutions), Automotive-Prüfsysteme (z.
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): Impressum/Standorte goepel.com (Jena als Fertigungsort, Tochtergesellschaften), Stellenanzeigen Montage/Produktion, Datenblatt eines Interface-/Kameramoduls (Schutzart, Verguss/Klebung).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 12. MK Versuchsanlagen GmbH & Co. KG (B1.822) – Prio A
- Gebiet/Ort: Rest DE / NL (Manuel) – 35325 Mücke-Merlau, Hessen | Quellen: `electronica/ergebnisse/tom_batch_37.md`, `tina_batch_37.md`
- Was wird gebaut: Handschuhprüfgeräte (Glovetester GTD3, GITS 4, SimpleX, automatisch/drahtlos) für Isolatoren und RABS der Pharmaindustrie, Handschuhports, Reinraum-/Laborsysteme …
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Impressum/Register (V für Sitz = Fertigungsort), Datenblatt GTD3 (Bauteile, Platine/Sensor, Vergussmasse?), Stellenanzeige Elektronik-Montage Mücke im Original.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 13. SENTECH Instruments GmbH (B1.900) – Prio A
- Gebiet/Ort: Rest DE / NL (Manuel) – 12489 Berlin-Adlershof | Quellen: `electronica/ergebnisse/tom_batch_50.md`, `tina_batch_50.md`
- Was wird gebaut: Plasmaprozessanlagen (Ätzen, Abscheiden, ALD) und Dünnschicht-Messtechnik (Ellipsometer, Reflektometer).
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Produktdatenblatt Plasmaanlage (Netzteil/Generator selbst gebaut oder zugekauft; Schutzlack/Verguss), Impressum und aktuelle Karriereseite (Elektronikfertigung); Patente Anmelder "SENTECH" mit Rechtsstand. Aktion: geringe Priorität.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 14. Viscom SE (A4.443) – Prio A
- Gebiet/Ort: Rest DE / NL (Manuel) – 30455 Niedersachsen, Hannover | Quellen: `electronica/ergebnisse/tom_batch_59.md`, `tina_batch_59.md`
- Was wird gebaut: automatische Inspektionssysteme für Lotpaste, Optik (AOI), Röntgen (AXI), Schutzlack, Batterie, Bonds und Software.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): (a) Karriereseite viscom.com und Stellenanzeigen Produktion Hannover im Browser lesen (Fertigung V, Zitat). (b) Impressum Viscom SE (Rechtsform, Adresse, Register). (c) Welche Baugruppen werden in Hannover vergossen/verklebt (Röntgenmodule, Kameramodule, Netzteile)? Produktseite, Stellenanzeigen. (d) Patentsuchen Anmelder Viscom AG/Viscom SE in Google Patents/Espacenet/DEPATISnet (Rechtsstand …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 15. Vistec Electron Beam GmbH (B1.679) – Prio A
- Gebiet/Ort: Rest DE / NL (Manuel) – 07743 Jena, Thüringen | Quellen: `electronica/ergebnisse/tom_batch_60.md`, `tina_batch_60.md`
- Was wird gebaut: Variable-Shaped-Beam-Elektronenstrahl-Belichtungsanlagen (z.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Eigentümer/Handelsregister Jena und Impressum lesen; Datenblatt SB3050-2 oder Stellenanzeigen Jena auf Hochspannungsverguss/Kleben prüfen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 16. Advanced Energy Industries GmbH (C3.320) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 72555 Metzingen | Quellen: `electronica/ergebnisse/tom_batch_01.md`, `tina_batch_01.md`
- Was wird gebaut: Konzern: Präzisions-Stromversorgungen für Plasmaprozesse (Halbleiter, Dünnschicht), Industrie/Medizin, Datacenter, Telekom.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Welche Gesellschaft stellt aus (Metzingen oder Raunheim/LumaSense), und was wird in Raunheim gefertigt (Produkte, Vergussschritte)? Wo nachsehen: Standortseite advancedenergy.com/about, Impressum der Advanced Energy Industries GmbH und der LumaSense Technologies GmbH (Handelsregister Darmstadt/Offenbach), Stellenanzeigen Raunheim (Montage, Produktion), Produktseiten LumaSense. Konzernzuordnung …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 17. AP&S International GmbH (B1.656) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 78166 Donaueschingen-Aasen | Quellen: `electronica/ergebnisse/tom_batch_04.md`, `tina_batch_04.md`
- Was wird gebaut: manuelle, halb- und vollautomatische Nassprozessanlagen (Reinigen, Ätzen, Trocknen) und Chemikalienversorgung für Halbleiter, MEMS, Optoelektronik bis 300 mm Wafer.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): In welchem Werk (Donaueschingen-Aasen oder Dresden) werden die Nassprozessanlagen gebaut und montiert? Wo nachsehen: Impressum und Standortseite ap-s.de, Silicon-Saxony-Artikel zum Dresden-Standort, Stellenanzeigen Montage/Elektromontage. Meles-Gruppe als Konzern gegen CRM (erledigt, kein Treffer) und Meles-Portfolio ansehen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 18. Axon' Kabel GmbH (B3.516) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 71229 Leonberg | Quellen: `electronica/ergebnisse/tom_batch_06.md`, `tina_batch_06.md`
- Was wird gebaut: Entwicklung und Fertigung von Leitern, Kabeln, konfektionierten Kabelbäumen, Steckverbindern und integrierten Systemen für Luftfahrt, Automotive u.
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Wird in Leonberg gefertigt/konfektioniert (Fertigungsbeleg V) oder nur entwickelt und vertrieben? Wo nachsehen: Impressum/Standortseite axon-cable.com, aktuelle Stellenanzeigen Leonberg (Montage/Konfektion), Messe-Pressemitteilung (PDF) im Browser. Aktion: Beobachtung.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 19. CeramTec GmbH (C2.335) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 73207 Plochingen | Quellen: `electronica/ergebnisse/tom_batch_10.md`, `tina_batch_10.md`
- Was wird gebaut: Technische Keramik;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): An welchem deutschen Werk (Plochingen, Lauf, Marktredwitz, Lohmar/ETEC) werden Ultraschall-/Piezosensor-Baugruppen montiert und vergossen/verklebt, oder ausschließlich in Ruabon/Southampton? Wo nachsehen: Broschüre "Messtechnik Sensoren" und Datenblätter Durchflusssensor (Fertigungsort, Schutzart), Standortseiten ceramtec-group.com, Stellenanzeigen Montage/Sensoren je Werk, Patentdatenbanken …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 20. DEWETRON Deutschland GmbH (A4.547) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 73650 Winterbach, Messefirma, Vertrieb | Quellen: `electronica/ergebnisse/tom_batch_13.md`, `tina_batch_13.md`
- Was wird gebaut: Mess- und Datenerfassungssysteme für Test & Messung, modulare Messtechnik.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): (a) Fertigt die DEWETRON (Österreich, Ges.m.b.H. Grambach) selbst in Grambach (Fertigungsbeleg V: Firmenseite "Made in Austria", Stellenanzeigen Fertigung/Montage Grambach)? (b) Welche Module enthalten Vergossenes/Verklebtes/Gedichtetes (Datenblätter, IP-Klassen, Stromsensoren)? (c) Ist die Messefirma Winterbach nur Vertrieb (dann nur Ansprache über die österreichische Einheit, Jey entscheidet …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 21. Ersa GmbH & Co. KG (A2.115) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 97877 Wertheim | Quellen: `electronica/ergebnisse/tom_batch_17.md`, `tina_batch_17.md`
- Was wird gebaut: Lötanlagen (Reflow, Welle, Selektiv), Schablonendrucker, Lötstationen, Entlötstationen, Lötkolben, Lötspitzen, Rework- und Inspektionssysteme ;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Welche Einheit fertigt Lötstationen/Lötkolben (Wertheim?) und werden Heizelemente/Stationselektronik verklebt oder vergossen? Wo nachsehen: Impressum kurtzersa.com/imprint, Ersa-Soldering-Tools-Katalog 2025 (PDF) und Produktseiten, Stellenanzeigen Wertheim (Montage Handlöttechnik), Handelsregister Mannheim (HRB 570023 gegen HRA 713121). Aktion: Beobachtung.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 22. FEINMETALL GmbH (A4.606) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 71083 Herrenberg | Quellen: `electronica/ergebnisse/tom_batch_19.md`, `tina_batch_19.md`
- Was wird gebaut: Federkontaktstifte (ICT/FCT, Fine-Pitch, Hochstrom, Kabelbaum), Prüfadapter, Wafer-Probe-Cards, Kontaktiersysteme für Leiterplatten, Kabelbäume, Steckverbinder.
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): Welche Produkte (Probe Cards, Kontaktstifte) werden in Herrenberg gefertigt und montiert, und gehört Feinmetall zu einer Gruppe? Wo nachsehen: Impressum und Standortseite feinmetall.com (Herrenberg, Produktions-/Montagehinweis), Karriereseite (Stelle "Montagemitarbeiter": Aufgaben Kleben/Vergießen/Montage Probe Cards, ein gelesenes Stellenangebot am Sitz zählt als V), Datenblatt Cantilever Probe …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 23. GEMÜ Gebr. Müller Apparatebau GmbH & Co. KG (B1.718) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 74635 Kupferzell/Ingelfingen | Quellen: `electronica/ergebnisse/tom_batch_22.md`, `tina_batch_22.md`
- Was wird gebaut: Ventile, Mess- und Regelsysteme für Flüssigkeiten, Dämpfe und Gase ;
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Werden Stellungsregler, Rückmelder, Sensorik oder Antriebselektronik in Ingelfingen oder Kupferzell gefertigt/bestückt, und wird dort vergossen, beschichtet oder geklebt? Wo nachsehen: gemu-group.com Standortseiten Deutschland (Produktionsstandort Criesbach, Kupferzell), Stellenanzeigen "Elektronikmontage/SMT" im Original, Datenblatt Stellungsregler (Schutzart, Gehäuse), Impressum (Sitz …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 24. Inovan GmbH & Co. KG (B2.566) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 75217 Birkenfeld bei Pforzheim, Enzkreis | Quellen: `electronica/ergebnisse/tom_batch_27.md`, `tina_batch_27.md`
- Was wird gebaut: Band- und Stanzgitter-Kontaktelemente, Mikrostanzteile, Schnappscheiben (Snap Domes), bondfähige Oberflächen, galvanisch veredelte Bänder ;
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Fertigungsbeleg: Stehen alle drei Werke in Birkenfeld (Standortseiten im Browser lesen, Impressum, Register), und gehört Inovan zu einer Gruppe? Zugleich: Werden Baugruppen (Sensor, Steckverbinder, Hybridteile) montiert und verklebt/vergossen oder nur Stanzteile geliefert? Wo nachsehen: inovan.de Kontakttechnik-/Kunststofftechnik-Seiten, Stellenanzeigen Montage. Aktion: keine Kontaktaufnahme vor …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 25. Jauch Quartz GmbH (B6.201) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 78056 Villingen-Schwenningen | Quellen: `electronica/ergebnisse/tom_batch_28.md`, `tina_batch_28.md`
- Was wird gebaut: frequenzgebende Bauteile (Quarze, Oszillatoren, MEMS-Oszillatoren), Lithium-Ionen-/Lithium-Polymer-Batterien, kundenspezifische Batteriepacks mit BMS (Faktenblatt …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Stellenanzeige "Produktionsmitarbeiter Batterie-Assemblierung" (jauch.com-PDF) im Original lesen (Arbeitsort VS; Tätigkeiten Verguss/Kleben?) und Standortseite jauch.com: Werden Batteriepacks/BMS in Villingen-Schwenningen montiert und vergossen/verklebt, oder in Asien? Faktenblatt electronica (PDF) lesen. Patente DEPATISnet/Espacenet nachholen. Aktion: Messegespräch möglich, Fragen nur über das …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 26. Keysight Technologies Deutschland GmbH (A4.506) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 71034 Böblingen | Quellen: `electronica/ergebnisse/tom_batch_30.md`, `tina_batch_30.md`
- Was wird gebaut: Mess- und Prüftechnik für Digital/Photonik/Netzwerk, Automotive-Energy-Solutions-Sparte mit Sitz in Böblingen.
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): (a) Welche Produkte werden in Böblingen gefertigt (Fertigungsbeleg V für die fertigende Einheit)? Wo nachsehen: jobs.keysight.com Standort Böblingen, Impressum keysight.com/de, Produktseiten Photonik-Testsysteme "Made in Germany". (b) Enthalten Fertigungs-Stellenanzeigen (Photonic Alignment and Packaging, Optoelektronik-Baugruppen) Kleben/Dispensing/Underfill/Verguss? Anzeigen im Original lesen …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 27. KRAMSKI GmbH (B2.452) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 75179 Pforzheim | Quellen: `electronica/ergebnisse/tom_batch_31.md`, `tina_batch_31.md`
- Was wird gebaut: Stanz- und Hybridteile (Metall-Kunststoff-Verbund), Werkzeug- und Formenbau, Präzisionsstanzteile, Press-Fit-Pins, Steckverbinder- und Kontaktteile, Schalterteile;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Wird in Pforzheim gefertigt (V) und welche Baugruppen/Produkte werden dort verklebt, gedichtet, vergossen (Hybrid-Teile mit Dichtfunktion, Sensor-/Leistungselektronik-Baugruppen)? Wo nachsehen: kramski.com (Standorte, Produktseiten "Hybrid parts", "Assembly"), Karriereseite Pforzheim (Montage), Datenblätter. Aktion: Beobachtung.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 28. LAUDA DR. R. WOBSER GmbH & Co. KG (C2.147) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 97922 Lauda-Königshofen | Quellen: `electronica/ergebnisse/tom_batch_32.md`, `tina_batch_32.md`
- Was wird gebaut: Temperiergeräte (Thermostate, Umwälzthermostate, Kälte- und Heizsysteme, Prozessthermostate für Technikum und Produktion seit 1964), Messgeräte (Tensiometer, Filmwaage …
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Werden Thermostate/Heizsysteme in Lauda-Königshofen gefertigt oder montiert (V)? Wo nachsehen: Impressum und Standortseite lauda.de, Karriereseite (Montage/Elektronikfertigung), Pressemeldungen zur Produktionshalle. (2) Werden Heizelemente, Temperaturfühler oder Elektronik selbst vergossen oder zugekauft (Datenblatt Schutzart, Stellenanzeigen "Vergießen/Kleben")? Aktion: erster Kandidat für …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 29. LCD Mikroelektronik GmbH (B6.431) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 76275 Ettlingen | Quellen: `electronica/ergebnisse/tom_batch_32.md`, `tina_batch_32.md`
- Was wird gebaut: Display- und Bediengeräte "mainly based on LCDs", kundenspezifische Displays, TFT, monochrome Displays, e-Paper, Touchscreens, vom Konzept bis zur Serienfertigung, vor …
- Demak-Bereich: Verklebung + Verguss + Dichtung
- Offener Auftrag (Tina): Werden Displays/Touch in Ettlingen montiert oder gebondet (Fertigungsbeleg), oder reiner Entwickler mit Zukauf? Wo nachsehen: Impressum und Über-uns lcd-mikroelektronik.de, Produktseiten (Optical Bonding, Cleanroom), Stellenanzeigen Ettlingen, Handelsregister Mar-Mosbach (Zweck). Bei reinem Design-Haus: E2 mit Quelle.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 30. Leicht+Müller Syscotec GmbH (B2.261) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 75196 Remchingen | Quellen: `electronica/ergebnisse/tom_batch_33.md`, `tina_batch_33.md`
- Was wird gebaut: Hybridbaugruppen aus Kunststoff und Metall (Spritzguss mit Stanzteilen), Sondermaschinenbau für die eigene Produktion, Kontaktpins/Stanzkontakte.
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Stellenanzeige "Anlagenführer Baugruppenfertigung" Remchingen im Volltext lesen (Produktionsjob am Sitz = V für Fertigungsort). (2) Welche Baugruppen enthalten Verguss, Abdichten oder Verkleben (Datenblatt/Produktseite Sensorbaugruppen, Steckerbaugruppen)? Wo: leicht-mueller.de Produkte/Karriere, Impressum (Register), Broschüre-PDF. Danach voraussichtlich Grün.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 31. LXinstruments GmbH (A4.300) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 71154 Nufringen | Quellen: `electronica/ergebnisse/tom_batch_34.md`, `tina_batch_34.md`
- Was wird gebaut: Mess- und Prüftechnik: Netzsimulatoren, Hochspannungs-Prüfhauben (HVE900, LX-HVE600EC, "safe up to 10 kV"), Funktionstestsysteme für Baugruppen, SCOE/EGSE für Satelliten …
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Werden Prüfsysteme (Netzsimulator, Prüfhaube) in Nufringen gebaut und montiert, oder nur entwickelt und extern gefertigt bzw. an einem anderen Gruppenstandort? Wo nachsehen: Produktseiten und Datenblätter lxinstruments.com ("Made in"), Impressum (welche Gesellschaft Nufringen vs. Amstetten stellt aus), Stellenanzeigen Montage/Fertigung Nufringen (Karriereseite, Arbeitsagentur), Pressemeldung …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 32. Mattson International GmbH (B1.521) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 89160 Dornstadt bei Ulm | Quellen: `electronica/ergebnisse/tom_batch_35.md`, `tina_batch_35.md`
- Was wird gebaut: "Plasma- und thermische Schnellverarbeitungsanlagen für die Halbleiterindustrie" (Rapid Thermal Processing, Trockenätzen;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): (a) Ist Mattson International GmbH nur Vertriebs-/Service-Gesellschaft, und werden Anlagen in Dornstadt von der Thermal Products GmbH gefertigt? Wo nachsehen: Impressum und Handelsregister Ulm beider Gesellschaften, Standortseite mattson.com. (b) Fertigungsbeleg (Montage/Produktion Dornstadt) per Stellenanzeige oder Standortseite. Falls International nur Vertrieb/Service: E2 für die ausstellende …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 33. MCD Elektronik GmbH (A4.232) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 75217 Birkenfeld bei Pforzheim | Quellen: `electronica/ergebnisse/tom_batch_35.md`, `tina_batch_35.md`
- Was wird gebaut: "Mess- und Prüftechnik" bzw.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Werden die Prüfsysteme in Birkenfeld montiert oder in Ungarn/China? Wo nachsehen: Impressum und Standortseite der Firma, Stellenanzeigen Montage/Elektronik Birkenfeld, Brochure 2026 (exhibitors.electronica.de) ganz lesen. Nahe an Grün, falls Birkenfeld per V als Fertigung bestätigt.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 34. METZ CONNECT GmbH (A3.320) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 78176 Blumberg | Quellen: `electronica/ergebnisse/tom_batch_36.md`, `tina_batch_36.md`
- Was wird gebaut: Anschlusstechnik: Klemmen, Leiterplattensteckverbinder, Board-to-Board, Patchfelder, Wanddosen, Relais und Koppelmodule.
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Welche Produkte (Relaismodule, Elektronikbaugruppen, Kabelkonfektion) werden an welchem Blumberger Werk gefertigt und wird dort vergossen, geklebt oder gedichtet? Wo nachsehen: metz-connect.com Unternehmens-/Standortseiten (Werk-Produkt-Zuordnung, V), Datenblätter Relaismodule/Rundsteckverbinder (IP-Klasse, Vollverguss), Karriereseite Elektronikfertigung/Konfektionierung im Original, Impressum …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 35. nVent SCHROFF (B3.343) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 75334 Straubenhardt | Quellen: `electronica/ergebnisse/tom_batch_39.md`, `tina_batch_39.md`
- Was wird gebaut: Gehäuse, Schränke, Subracks, Backplanes, Stromversorgungen, vormontierte Chassis für Telekommunikation, Rechenzentren und Verkehrstechnik.
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Welche Produkte (Netzteile, Elektronik, Gehäuse) werden in Straubenhardt aktuell gefertigt und wo wird gedichtet (FIPFG) oder vergossen? Wo: schroff.nvent.com Produkt-/Datenblattseiten (Made-in), nVent-Standortseite, Karriereseite/Stellenanzeigen mit Datum 2025/2026, Impressum (Firmierung), Handelsregister Mannheim/Mosbach. Bei V-Beleg Fertigung Straubenhardt: Grün.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 36. Obducat Europe GmbH (B1.357) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 78315 Radolfzell | Quellen: `electronica/ergebnisse/tom_batch_40.md`, `tina_batch_40.md`
- Was wird gebaut: Nasschemie-/Lithografie-Anlagen (QUICKSTEP, MICROCLUSTER Coater/Developer, Nassprozess-Systeme;
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Werden die Nassprozess-Systeme tatsächlich in Radolfzell gebaut oder nur dort vertrieben/serviciert (Konzern-Hauptwerk Lund)? Wo nachsehen: obducat.com (Standorte, Radolfzell-Seite), Impressum/Handelsregister Amtsgericht Freiburg, Stellenanzeigen Radolfzell (Montage). Aktion: nicht priorisieren (Verguss Niedrig).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 37. POLYRACK Electronic-Aufbausysteme GmbH (B3.141) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 75334 Straubenhardt | Quellen: `electronica/ergebnisse/tom_batch_43.md`, `tina_batch_43.md`
- Was wird gebaut: 19-Zoll-Gehäuse, Frontplatten, Steckbaugruppen, Subracks, Systemtechnik, Gehäuseserien (FrameTEC, EmbedTEC, CasTEC, Verotec Case), VME/CompactPCI-Aufbausysteme …
- Demak-Bereich: Dichtung + Verguss
- Offener Auftrag (Tina): Wird das Produkt (Gehäuse, Subracks, Baugruppen) in Straubenhardt gefertigt/montiert (Fertigungsbeleg V)? Wo nachsehen: Indeed-Stellenanzeige "Facharbeiter Montage unserer Systeme" im Original (Montagejob am Sitz gilt als V), Impressum und Standortseite polyrack.com. (2) Welche Baugruppen enthalten Dichtungen (FIPFG/Schaum), Verklebung oder Verguss (Elektronikfertigung der Gruppe, Datenblätter …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 38. POLYRACK TECH-GROUP Holding GmbH & Co. KG (B3.141) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 75334 Straubenhardt | Quellen: `electronica/ergebnisse/tom_batch_43.md`, `tina_batch_43.md`
- Was wird gebaut: Dachgesellschaft der POLYRACK TECH-GROUP;
- Demak-Bereich: Dichtung + Verguss
- Offener Auftrag (Tina): Soll die Holding als eigene Zeile geführt werden oder mit Nr. 478 zusammengelegt werden? Wo nachsehen: Impressum polyrack.com, Handelsregister Mannheim/Mosbach (Zuständigkeit). Empfehlung: zusammenlegen, Bewertung läuft über Nr. 478. Aktion: nicht gesondert bearbeiten.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 39. Promicron AG (C1.269) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 74366 Kirchheim am Neckar | Quellen: `electronica/ergebnisse/tom_batch_43.md`, `tina_batch_43.md`
- Was wird gebaut: familiengeführter Hersteller halb-/vollautomatischer Mikroskop- und AOI-Inspektionssysteme (Promis 300, DM8000, Promis A) für Wafer-Inspektion, Defect Review, optische …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Baut Promicron die Inspektionssysteme/Mikroskope selbst in Kirchheim (Fertigungsbeleg) oder handelt/refurbisht sie überwiegend (E2)? Wo nachsehen: Website promicron.de (Domain ungeprüft), Impressum, Handelsregister (Stuttgart/Heilbronn), Produktseiten Promis/DM8000 (verbaute Antriebe, Kameras, Beleuchtung; Verguss/Klebung). Aktion: Beobachtung.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 40. PROVERTHA Cables Connectors & Solutions GmbH (B3.100) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 75180 Pforzheim | Quellen: `electronica/ergebnisse/tom_batch_44.md`, `tina_batch_44.md`
- Was wird gebaut: Steckverbinder (D-Sub, M12/M8, Hauben, Vollmetallhauben), Kabelkonfektion und Kabelbäume nach Kundenwunsch, umspritzte Sonderstecker für die Automobilindustrie (z.
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Werden Steckverbinder oder Kabelkonfektion in Pforzheim gefertigt/montiert, oder ist Pforzheim nur Entwicklung/Vertrieb? Wo nachsehen: Standortseite provertha.de/en/company (Funktionen je Standort), Impressum, Stellenanzeigen am Sitz (Montage/Fertigung), Produktseite Sonderstecker (?p=25219) auf "Made in"/Werk. Zusätzlich: Werden die umspritzten Stecker harzvergossen oder nur thermoplastisch …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 41. RAPP Kunststofftechnik GmbH (B3.141) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 75334 Straubenhardt, Werk Ettlingen | Quellen: `electronica/ergebnisse/tom_batch_45.md`, `tina_batch_45.md`
- Was wird gebaut: Spritzgießer: Entwicklung, Prototyping und Werkzeugbau für thermoplastische Teile;
- Demak-Bereich: Dichtung
- Offener Auftrag (Tina): (a) Aktuelle Fertigung in Ettlingen/Straubenhardt belegen und prüfen, ob Montage-/Baugruppenschritte mit Kleben/Dichten/Vergießen stattfinden. Wo nachsehen: polyrack.com Seite "Plastics technology", Impressum RAPP, Stellenanzeigen Ettlingen. (b) Verhältnis zu Batch 43 (POLYRACK, gleicher Stand). Aktion: nicht priorisieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 42. RENA Technologies GmbH (B1.312) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 78148 Gütenbach | Quellen: `electronica/ergebnisse/tom_batch_45.md`, `tina_batch_45.md`
- Was wird gebaut: Nasschemische Prozessanlagen (Reinigen, Ätzen, Texturieren, Beschichten, Galvanik, Trocknen) für Halbleiter, Solar, Glas, additive Fertigung, Medizintechnik;
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Welche Anlagen werden in Gütenbach montiert und enthalten Elektronik-/Sensorik-Baugruppen mit Verguss/Kleben/Dichten (zugekaufte Teile zählen)? Wo nachsehen: rena.com Interview-PDF "Interview-Wirtschaftsforum", Produktseiten, Stellenanzeigen Gütenbach Elektromontage. Aktion: nicht aufnehmen, außer Jey sieht Anlagen-Elektronik als Zielgruppe.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 43. Renu Electronics GmbH (A1.645) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 70794 Filderstadt | Quellen: `electronica/ergebnisse/tom_batch_46.md`, `tina_batch_46.md`
- Was wird gebaut: HMI-Bediengeräte/Touch Panels und Industrie-PCs (ehemals Phoenix Contact HMI IPC Technology, davor SÜTRON electronic, gegründet 1968) sowie EMS: Entwicklung …
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): Werden die HMI-Geräte und EMS-Baugruppen heute noch in Filderstadt gefertigt/montiert (aktueller Beleg 2025/2026)? Wo nachsehen: Impressum und Standortseite renuelectronics.de, Stellenanzeigen Filderstadt (Fertigung, SMT, Montage), SPS-Ausstellerprofil; Produkt-zu-Werk-Zuordnung (HMI Filderstadt, Zähler Indien). Zusätzlich: Wird bei Renu vergossen/verklebt (Optical Bonding, Schutzlack)? Und …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 44. ROB GmbH (A1.123) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 75245 Neulingen | Quellen: `electronica/ergebnisse/tom_batch_46.md`, `tina_batch_46.md`
- Was wird gebaut: Elektronikfertigung: Design, Entwicklung, Produktion, Montage, Logistik;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): (a) Wird bei ROB GmbH in Neulingen aktuell bestückt/montiert (Beleg V: Impressum, Standortseite, datierte Stellenanzeige)? (b) Wer ist heute Eigentümer (Finvest?) und gibt es einen Konzern mit CRM-Bezug? Handelsregister Mannheim HRB 724976, Impressum. (c) Welche Branchen/Produkte (Automotive, Medizin, Industrie) und wird vergossen/Schutzlack aufgetragen? Stellenanzeigen im Original.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 45. Schaffroth GmbH (B2.181) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 73666 Baltmannsweiler, laut Liste | Quellen: `electronica/ergebnisse/tom_batch_48.md`, `tina_batch_48.md`
- Was wird gebaut: Laut Implisense-Profil Handel, Herstellung und Verarbeitung von Elektrokabeln, Elektroleitungen und Elektrozubehörteilen, kleines Unternehmen, Bilanzsumme ca.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Eigene Website/Impressum der Schaffroth GmbH, 73666 Baltmannsweiler finden (Messeprofil electronica-Ausstellerportal, Handelsregister Stuttgart/Esslingen): Konfektioniert die Firma Leitungen selbst, werden Stecker vergossen oder überspritzt, oder reiner Kabelhandel (dann E2)?
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 46. SCHROEDER + BAUER Werkzeugbau Stanztechnik GmbH + Co. KG (B2.471) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 75245 Neulingen-Bauschlott | Quellen: `electronica/ergebnisse/tom_batch_49.md`, `tina_batch_49.md`
- Was wird gebaut: Präzisions-Stanzwerkzeuge, Stanz-Biegeteile und komplette Baugruppen für Automotive-Elektrik, Elektronik und Telekommunikation, enge Toleranzen.
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): (a) Welche Baugruppen werden gefertigt, mit Umspritzung/Verklebung/Dichtung, und in welchem Werk? (b) Wie viele Werke hat SUBA, und in welchem Werk liegt die Baugruppenmontage? Wo nachsehen: schroeder-bauer.com (Leistungen, Baugruppen), suba-holding Seite, Impressum/Handelsregister Mosbach/Pforzheim, Stellenanzeige "Schroeder_Bauer_Stelle_0826" (wirtschaftskraft.de). Aktion: nicht kontaktieren …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 47. Schweizer Electronic AG (A2.207) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 78713 Schramberg | Quellen: `electronica/ergebnisse/tom_batch_49.md`, `tina_batch_49.md`
- Was wird gebaut: Leiterplatten (Automotive, Industrie, Hochfrequenz) und Chip-Embedding p² Pack (SiC-Chips in der Leiterplatte, Power-Embedding, Partnerschaft mit Zollner seit Juni 2024) …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): (a) Welche Produkte werden in Schramberg gefertigt, und enthält der p² Pack-Modulaufbau Verguss/Glob-Top/Dam&Fill? Wo nachsehen: Produktseite und Datenblatt p² Pack, Geschäftsbericht 2025 (Standort- und Segmentangaben), Impressum schweizer.ag. (b) Jey: Bedeutet der Zollner-Bezug im CRM etwas für die Ansprache (Partner, kein Konzern)? Aktion: zurückstellen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 48. Schützinger GmbH (A4.526) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 70567 Stuttgart | Quellen: `electronica/ergebnisse/tom_batch_49.md`, `tina_batch_49.md`
- Was wird gebaut: Messleitungen, Prüfspitzen und Tastköpfe, Bananenstecker und -buchsen, Laborklemmen, Halter;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Wo werden Messleitungen, Prüfspitzen und Steckverbinder gefertigt/konfektioniert (Stuttgart eigenes Werk oder Zulieferer, Ort)? Wo nachsehen: Schützinger-Website (Über uns, Qualität "Werke"), Impressum, Produktdatenblätter ("Made in ..."), Stellenanzeigen Stuttgart (Montage/Konfektion/Spritzguss), ISO-Zertifikate (Standortangabe). Aktion: erst nach Fertigungsbeleg weiter.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 49. SEPA EUROPE GmbH (B3.344) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 79427 Eschbach im Breisgau, Gewerbepark Breisgau | Quellen: `electronica/ergebnisse/tom_batch_50.md`, `tina_batch_50.md`
- Was wird gebaut: kleine DC-Lüfter (Axial, Radial) und Chipkühler, kundenspezifische Lösungen ;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Werden Lüfter in Eschbach gefertigt/montiert oder nur entwickelt, konfektioniert und vertrieben, und gehört SEPA EUROPE zu einer (asiatischen) Gruppe? Wo nachsehen: Impressum und "Über uns" sepa-europe.com, Handelsregister Freiburg HRB 6056, Stellenanzeigen Eschbach (Montage, Wickelei, Konfektion), Datenblatt "Made in"-Angabe. Aktion: Fertigungsbeleg beschaffen, nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 50. Telegärtner Karl Gärtner GmbH (B3.311) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 71144 Steinenbronn | Quellen: `electronica/ergebnisse/tom_batch_56.md`, `tina_batch_56.md`
- Was wird gebaut: Steckverbinder (HF-Koax, RJ45, M12-Rundsteckverbinder, DIN-41622, 4.3-10 auch für Glasfaser), Netzwerkkomponenten, Spritzguss, Industrial Electronics, Kabelkonfektion.
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Welches deutsche Werk (Steinenbronn, Klingenberg) fertigt Kabelkonfektion bzw. Industriesteckverbinder mit Verguss/Überspritzung, und gibt es eine V-Quelle? Wo: telegaertner.com Standort-/Produktionsseiten und Industrial-Cabling-Seiten, Impressum, Stellenanzeigen Steinenbronn/Klingenberg im Browser; Patente Google Patents/DEPATISnet mit Anmelder "Telegärtner Karl Gärtner GmbH" und Schreibvariante …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 51. Trelleborg Sealing Solutions Germany GmbH (C1.329) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 70565 Stuttgart | Quellen: `electronica/ergebnisse/tom_batch_57.md`, `tina_batch_57.md`
- Was wird gebaut: polymerbasierte Präzisionsdichtungen und Dichtungssysteme (O-Ringe, Hydraulik-/Pneumatikdichtungen, Wellendichtungen, LSR-Teile, Silikonschläuche, Luftfahrtdichtungen);
- Demak-Bereich: Dichtung
- Offener Auftrag (Tina): (a) Welche Trelleborg-Einheit fertigt in DE/AT/NL, und gehört das zur Stuttgarter Gesellschaft? Wo: Standortseite trelleborg.com/seals (Germany, Locations), Impressum der Gesellschaft. (b) Bietet Trelleborg FIPG/CIPG, Dichtstoffe oder Klebungen (Gummi-Metall) an (dann Wettbewerbs-/Bonding-Bezug, E1 prüfen)? Produktseiten im Browser. (c) Patentsuche in Google Patents/Espacenet/DEPATISnet mit …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 52. Tria Technologies GmbH (B5.103) – Prio B
- Gebiet/Ort: Baden-Württemberg (Stefan) – 76297 Stutensee | Quellen: `electronica/ergebnisse/tom_batch_57.md`, `tina_batch_57.md`
- Was wird gebaut: Embedded-Compute-Module (COM-HPC, COM Express, Qseven, SMARC, OSM) und komplette Systeme einschließlich Design- und Fertigungsdienstleistung für Industrie-OEMs.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): (a) Fertigung Stutensee/Eschbach mit V belegen: Stellenanzeige im Volltext (Browser), Standortseite tria-technologies.com, Impressum. (b) Werden Wärmeleit-Materialien dosiert, Boards lackiert, Underfill/Verguss eingesetzt (Datenblätter rugged Systeme, Stellenanzeigen "Dispensen", "Vergussprozess")? (c) Patentsuche nachholen (Tria, Avnet Embedded, MSC Technologies). Aktion: bei V-Beleg Fertigung …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 53. ACCRETECH (Europe) GmbH (B1.401) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 81241 Landsberger Str. 396, 81241 München | Quellen: `electronica/ergebnisse/tom_batch_01.md`, `tina_batch_01.md`
- Was wird gebaut: Wafer-Prober, Grinder, Dicer, CMP, industrielle Messtechnik (Rauheit, Kontur, Form), Batterie-Testtechnik.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Gibt es eine Montage oder Fertigung in München oder Dresden (Impressum, Standortseite accretech.eu, Stellenanzeigen)? Wenn nein, mit Quelle Rot nach E2/E3 (Vertriebsgesellschaft, Fertigung nur außerhalb DE/AT/NL). Aktion: keine Priorität.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 54. ACTRON AG (C2.519) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 85435 Erding | Quellen: `electronica/ergebnisse/tom_batch_01.md`, `tina_batch_01.md`
- Was wird gebaut: laut Registerprofil Großhandel mit elektronischen Bauteilen (WZ G46.52);
- Demak-Bereich: Verklebung
- Offener Auftrag (Tina): Betreibt ACTRON in Erding/Leipzig/Schwalmtal eigene Display-Montage mit Optical Bonding (Reinraum, Klebeanlage)? Wo nachsehen: actron.de (Leistungen "Optical Bonding", Impressum), Stellenanzeigen (Bonding-/Montagetechniker), Steliau-Seite (Partnerfertiger). Bei reinem Handel/Design-in ohne Fertigung: Rot nach E2 mit Quelle.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 55. Alps Alpine Europe GmbH (B4.311) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 85716 Unterschleißheim | Quellen: `electronica/ergebnisse/tom_batch_03.md`, `tina_batch_03.md`
- Was wird gebaut: Konzern: "Hersteller elektronischer und elektromechanischer Komponenten" (Geschäftsfelder Mobile/Home, Automotive, Energy, Healthcare, Industrial, IoT;
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): Gibt es heute eine Fertigung oder Montage von Alps Alpine in DE/AT/NL? Wo nachsehen: Standortliste alpsalpine.com (Global Network, Europa), Impressum/Handelsregister München (HRB255899), Pressemeldung zur Dortmund-Schließung (Vollartikel), Karriereseite Europa. Bei Beleg "keine Fertigung in DE/AT/NL" Rot nach E3 mit Quelle.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 56. Assdev GmbH (A1.525/16) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 91301 Forchheim | Quellen: `electronica/ergebnisse/tom_batch_05.md`, `tina_batch_05.md`
- Was wird gebaut: EMS: Flachbaugruppen und Geräte, Muster bis Serie, SMD, THT, AOI, ICT, Funktionstest, Dampfphasenlöten.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Fertigung Forchheim als V (Stellenanzeige "SMT-Maschinenführer" oder "Löter/Montierer" auf stepstone.de/arbeitsagentur.de im Original lesen; Impressum assdev.de) und Verguss/Schutzlack tatsächlich vorhanden (Leistungsseite assdev.de, embedded-world-Profil, Karriereseite)? Bei V für Fertigung und Verguss Mittel (A) ergibt sich Grün nach Zeile 4. Zusätzlich Jey: Gruppenstruktur (ASSDEV GmbH als …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 57. BvR electronic GmbH (A1.525/19) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 85551 Kirchheim bei München | Quellen: `electronica/ergebnisse/tom_batch_08.md`, `tina_batch_08.md`
- Was wird gebaut: Elektronikdienstleistungen (Beratung, Entwicklung, Konstruktion, Logistik, Fertigung, Montage, Test, Service) und LED-Lichtsysteme mit "own concept and production …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): (a) Fertigt BvR in Kirchheim selbst (SMT/Montage), und werden LED-Module oder Baugruppen vergossen? Wo nachsehen: Firmenwebsite (Domain bisher unbekannt), Impressum, Stellenanzeige "Bestücker/in" im Original, Produktseiten LED-Lichtsysteme (IP-Klasse, Treiber vergossen). (b) Bestätigung von Name, Rechtsform und Register (Handelsregister München). Aktion: Messegespräch möglich, Fragen über das …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 58. Bühler Alzenau GmbH (B1.836) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 63755 Alzenau, Unterfranken | Quellen: `electronica/ergebnisse/tom_batch_08.md`, `tina_batch_08.md`
- Was wird gebaut: Dünnschicht-Vakuumbeschichtungsanlagen (Optik, Ophthalmik, Metallisierung, Verpackung, flexible Elektronik, Glas), ca.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): (a) Fertigt Alzenau selbst Steuerungs-/Schaltschrank-/Elektronikbaugruppen oder kauft es sie zu (Frage nach vergossenen Bauteilen)? Wo nachsehen: Standortseite Bühler Alzenau, Stellenanzeigen Montage/Elektrik Alzenau. (b) Kurz bestätigen, dass Bühler Motor und Bühler Technologies keine Konzernschwestern sind (Handelsregister/Konzernseite). Aktion: Priorität niedrig (Maschinenbau).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 59. Camtek Germany GmbH (B1.510) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 85551 Kirchheim b. München laut Liste | Quellen: `electronica/ergebnisse/tom_batch_09.md`, `tina_batch_09.md`
- Was wird gebaut: Metrologie- und Inspektionsanlagen für Halbleiter (Advanced Packaging, Memory, CMOS-Sensoren, MEMS), Konzern Camtek Ltd.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Ist die Kirchheimer Einheit reine Vertriebs-/Serviceniederlassung (dann Rot nach E2/E3 mit Quelle) oder gibt es Montage/Fertigung (FRT Bergisch Gladbach getrennt bewerten)? Wo nachsehen: camtek.com Standortseite/Impressum, Handelsregister München (Camtek Germany GmbH), Stellenanzeigen Kirchheim.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 60. Chroma Germany GmbH (A4.624) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 86165 Augsburg | Quellen: `electronica/ergebnisse/tom_batch_10.md`, `tina_batch_10.md`
- Was wird gebaut: Präzisions-Messgeräte, automatische Testsysteme, programmierbare DC-Stromversorgungen (62000P), Batterie-/Netz-Simulatoren, MES.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Werden in Ede (NL) oder Augsburg Geräte (Stromversorgungen, Testsysteme) montiert/gefertigt? Wo nachsehen: Impressum Chroma Germany und Chroma ATE Europe (chromaate.com/eu), Handelsregister (KvK Ede), Stellenanzeigen Ede (Production/Assembly), Standortseite. Aktion: nicht kontaktieren; falls Ede fertigt, eigene Prüfung der Einheit Chroma ATE Europe B.V.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 61. cyberTECHNOLOGIES GmbH (C1.619) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 85386 Eching bei München | Quellen: `electronica/ergebnisse/tom_batch_12.md`, `tina_batch_12.md`
- Was wird gebaut: hochauflösende laserbasierte, berührungslose 3D-Oberflächenmesssysteme (Ebenheit, Dickschicht, Koplanarität;
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): Werden die Messsysteme für den europäischen Markt in Eching gebaut und montiert (Fertigungsbeleg) und ist die Changzhou-Meldung dieselbe Firma? Wo nachsehen: Impressum und Produktseiten der Firmenwebsite (Domain unbekannt, über Ausstellerprofil C1.619 suchen), Stellenanzeigen Eching (Montage, Elektronik), Handelsregister München (Sitz).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 62. DELTEC GROUP GmbH (A1.407) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 93437 Furth im Wald | Quellen: `electronica/ergebnisse/tom_batch_13.md`, `tina_batch_13.md`
- Was wird gebaut: EMS/High Performance Electronics Manufacturing;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Wird die Elektronik in Furth im Wald gefertigt (Stufe V), und werden dort Baugruppen vergossen, dosiert oder lackiert? Wo nachsehen: Website der DELTEC Group (Impressum, Standort-/Produktionsseite, Maschinenpark), Stellenanzeigen auf der Karriereseite mit Arbeitgebername DELTEC (Vergießer, Dosieren, Selektivlackieren), Pressemeldung der Übernahme Tunesien im Original (Rolle Furth). Wahrscheinlich …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 63. DISCO HI-TEC EUROPE GmbH (B1.201) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 85551 Kirchheim bei München | Quellen: `electronica/ergebnisse/tom_batch_14.md`, `tina_batch_14.md`
- Was wird gebaut: Dicing-Sägen, Grinder, Polierer (Hersteller Konzern, Japan);
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Werden in Kirchheim Maschinen/Baugruppen montiert oder nur Service/Wafer-Lohnbearbeitung durchgeführt? Wo nachsehen: Impressum/Standortseite disco.co.jp bzw. dicing-grinding.com, Karriereseite Kirchheim. Bei ausschließlich Service/Vertrieb: Rot E2 mit Quelle. Aktion: niedrige Priorität.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 64. esmo AG (C1.241) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 83022 Rosenheim | Quellen: `electronica/ergebnisse/tom_batch_18.md`, `tina_batch_18.md`
- Was wird gebaut: Maschinen für Halbleiter-Test (esmo semicon: Handling-/Testsysteme) und Sondermaschinenbau/Automatisierung (esmo automation), Schaltschrankbau und Verdrahtung.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Welche Gesellschaft fertigt in Rosenheim, und werden dort Baugruppen/Maschinen montiert (Fertigungsbeleg V)? Enthalten die Maschinen Verguss-/Klebe-/Dichtschritte (eigene Elektronik, Sensorik)? Wo nachsehen: Impressum esmo-group.com, Stellenanzeige Montage Maschinenbau im Original (Karriereseite), Standortseite Rosenheim.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 65. FrelTec GmbH (A6.100) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 82319 Starnberg | Quellen: `electronica/ergebnisse/tom_batch_21.md`, `tina_batch_21.md`
- Was wird gebaut: laut Branchenverzeichnis "Entwicklung, Herstellung, Import/Export und Vertrieb elektromechanischer und elektronischer Bauteile" mit Steckverbindern und Passivbauteilen …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Stellt FrelTec in Starnberg Steckverbinder/Kabel/Baugruppen selbst her (oder lässt sie fertigen) oder handelt sie nur (E2)? Wo nachsehen: freltec.com (Impressum, Produktseiten, "Über uns", Fertigung/Qualität), electronica-Ausstellerprofil Halle A6 Stand 100, Stellenanzeigen (Montage, Konfektion). Bei belegter reiner Handelstätigkeit Rot nach E2 mit Quelle. Aktion: nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 66. Hermos AG (B1.279) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 95490 Mistelgau | Quellen: `electronica/ergebnisse/tom_batch_25.md`, `tina_batch_25.md`
- Was wird gebaut: RFID-Reader (LFM Loadport Reader, HFM-6X, HFS-SL, E84) für Halbleiterfabriken, Software-/Track-and-Trace-Plattformen, Schaltanlagen und Schaltschränke.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Stellenanzeige im Browser lesen (Zitat, Datum, Ort Mistelgau), Impressum hermos.com (fertigende Einheit Hermos AG gegen HERMOS Schaltanlagen GmbH), Datenblatt LFM/HFM (Schutzart, "Verguss/potted"), Schaltanlagenbau Mistelgau/Bad Lobenstein (Dichtungen, Netzteile).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 67. INOVA Semiconductors GmbH (C5.259) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 81379 München | Quellen: `electronica/ergebnisse/tom_batch_27.md`, `tina_batch_27.md`
- Was wird gebaut: Halbleiter für Gigabit-Datenkommunikation (APIX3), ISELED-LED-Treiber/Controller (INLC10AQ), ILaS-Kabeltransceiver.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Wo werden Chips und Module von INOVA gefertigt/gebaut, und gibt es Eigenfertigung in DE (Evaluation-Boards, Tests)? Wo nachsehen: Firmenseite inova-semiconductors.de (Unternehmen/Legal Notice), Presseseite "Fertigung bei Foundry". Bei V-Beleg ausschließlich Ausland: Rot nach E3 mit Quelle. Aktion: nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 68. Kerafol Keramische Folien GmbH & Co. KG (C3.452) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 92676 Eschenbach i. d. OPf. | Quellen: `electronica/ergebnisse/tom_batch_30.md`, `tina_batch_30.md`
- Was wird gebaut: Keramikfolien nach eigenem Verfahren auf kontinuierlichen Linien , Produktbereiche Thermal Management, Ceramic Tapes & Substrates, Filterkeramik, SOFC.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Ist Kerafol Hersteller und Anbieter von Vergussmassen/Gap-Fillern (E1) und ist das das Kerngeschäft oder ein Nebenprodukt neben Keramik? Wo nachsehen: kerafol.com Produktseiten Keratherm GFL/KP und Datenblätter, Firmenprofil. (2) Anmelder und Rechtsstand der Koppe-Patente (Justia/Google Patents, Espacenet, DEPATISnet; Anmelder-Varianten "Kerafol Keramische Folien", "Kerafol"). (3) Impressum …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 69. KISCO (Deutschland) GmbH (C2.160) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 85748 Garching bei München | Quellen: `electronica/ergebnisse/tom_batch_30.md`, `tina_batch_30.md`
- Was wird gebaut: Gruppe: Kunstharze, Chemieprodukte, Elektronikmaterialien, Verpackungsmaterialien, diX-Parylene-Beschichtung ;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): (a) Gegenstand der GmbH (Impressum kisco-net.com bzw. Handelsregister München) und Name der Mutter bestätigen. (b) Gibt es Fertigung/Beschichtungsservice (SCS Europa) in Deutschland? (c) Ist der Konzern als Materialhersteller E1 einzustufen oder nur Handelshaus (E2)? Bei Bestätigung Rot mit Quelle. Aktion: nicht kontaktieren, bis (a) geklärt.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 70. Koh Young Europe GmbH (C2.329) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 63755 Alzenau | Quellen: `electronica/ergebnisse/tom_batch_31.md`, `tina_batch_31.md`
- Was wird gebaut: 3D-Inspektionssysteme SPI/AOI (True3D) für SMT-Linien.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Gibt es Montage/Fertigung in Alzenau (sonst Rot nach E3/E2)? Wo nachsehen: Impressum kohyoung.com/ge, Karriereseite Alzenau (Montage/Produktion), Handelsregister Aschaffenburg. Aktion: nicht priorisieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 71. Kurtz Ersa Semicon GmbH (A2.115) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 99880 Vaterstetten bei München | Quellen: `electronica/ergebnisse/tom_batch_32.md`, `tina_batch_32.md`
- Was wird gebaut: Vakuumlötsysteme für Halbleiter und Mikroelektronik, Serienanlage SRO i-LINE mit Infrarotheizung.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Werden die Vakuumlötanlagen in Vaterstetten gebaut (Fertigungsbeleg) und enthalten sie vergossene/geklebte/gedichtete Baugruppen (Heizmodule, Steuerung)? Wo nachsehen: Impressum Kurtz Ersa Semicon, Produktseite SRO i-LINE (Datenblatt), Handelsregister München (ATV Technologie), Stellenanzeigen Montage. Aktion: zurückstellen (Anlagenbau, Verguss Niedrig).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 72. LEONHARD KURZ Stiftung & Co. KG (B4.301) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 90763 Fürth | Quellen: `electronica/ergebnisse/tom_batch_32.md`, `tina_batch_32.md`
- Was wird gebaut: Heißprägefolien, Kaltprägefolien, Dekor- und Funktionsschichten auf Trägerfolien, IMD-Systeme ;
- Demak-Bereich: Verklebung + Verguss
- Offener Auftrag (Tina): In welchem Werk werden Touch-Sensor-Folien/FFB-Produkte gefertigt (Fürth oder anderes Werk), und wird dabei geklebt/dosiert? Wo nachsehen: kurz-world.com Standortseite und FFB-Produktseite, Pressekit 07/2024 (PDF), Stellenanzeigen Fürth (Montage/Kleben). Zusatzfrage: Ist "Kurz Industrie-Elektronik GmbH" (CRM Zeile 1361) eine andere Firma?
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 73. MEDi Kabel GmbH (B2.507) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 84478 Waldkraiburg | Quellen: `electronica/ergebnisse/tom_batch_35.md`, `tina_batch_35.md`
- Was wird gebaut: Verzeichnisprofil: Händler (Distributor) mit F&E-Anteil;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Hat Medi Kabel eigene Konfektion/Fertigung in Waldkraiburg (Stecker anspritzen/vergießen) oder ist es reiner Händler (dann Rot E2 mit Quelle)? Wo nachsehen: medikabel.de Impressum und Leistungsseiten, Stellenanzeigen "Konfektion/Fertigung", Katalog.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 74. mentec GmbH (B3.261) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 83362 Surberg | Quellen: `electronica/ergebnisse/tom_batch_36.md`, `tina_batch_36.md`
- Was wird gebaut: Kunststoffgehäuse "von der Einzelanfertigung bis zur Serie", Folien- und Silikontastaturen, Touch-Displays, Acrylglas-Teile.
- Demak-Bereich: Verklebung + Dichtung
- Offener Auftrag (Tina): Welche Teile (Touch-Displays, Folientastaturen, Gehäuse) werden in Surberg bzw. Eisenberg gefertigt/verklebt, und werden Displays mit Flüssigklebstoff gebondet oder nur Folien laminiert? Wo nachsehen: Website/Impressum der mentec GmbH (Rechtsform, HRB, Sitz Neuried), Standortseiten Surberg und Eisenberg, Broschüre (Nürnberg-Messe-PDF) im Wortlaut, Stellenanzeigen Surberg/Eisenberg im Original.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 75. MTC Micro Tech Components GmbH (B3.244) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 89407 Dillingen an der Donau | Quellen: `electronica/ergebnisse/tom_batch_37.md`, `tina_batch_37.md`
- Was wird gebaut: Hersteller und Distributor von EMV-Lösungen (Stoff-/Folie-über-Schaum-Dichtungen, leitfähige Schäume, Elastomere, Abschirmfenster, Federkontakte) und Wärmemanagement …
- Demak-Bereich: Dichtung + Verguss
- Offener Auftrag (Tina): (a) Was wird in Dillingen gefertigt (Stanzen, Kaschieren, Mischen/Dosieren) und was in Südkorea? (b) Stellt MTC Gap Filler/Dichtungsmaterial selbst her (dann E1) oder konfektioniert es Fremdmaterial? (c) Werden Dichtungen vor Ort dosiert/geschäumt (FIPFG)? Wo nachsehen: mtc.de Impressum, Unternehmens-/Produktseiten und Datenblatt TCTP, Stellenanzeigen Dillingen im Original, discoverIE-Seite zu …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 76. Novomotec GmbH (B4.102) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 85521 Hohenbrunn-Riemerling | Quellen: `electronica/ergebnisse/tom_batch_39.md`, `tina_batch_39.md`
- Was wird gebaut: Kompakte EC-Innenläufer-, EC-Außenläufer- und EC-Flachmotoren (1 W bis 1 kW), Frameless-Kits, Radialgebläse, DC-Bürstenmotoren;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Montiert/wickelt/vergießt Novomotec Motoren in Hohenbrunn oder werden sie als Fertigprodukte zugekauft (Herkunft)? Wo: novomotec.de Impressum, Datenblätter (Herstellerangabe "Made in"), Stellenanzeige im Original, Addtech-Meldung/Jahresbericht (Beschreibung "Hersteller" oder "Händler"), Handelsregister München (Unternehmensgegenstand). Bei Zukauf: Rot nach E2 mit Quelle.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 77. PIC Proximity Instrumentation Controls Kontaktbauelemente GmbH (B4.319) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 90530 Wendelstein | Quellen: `electronica/ergebnisse/tom_batch_42.md`, `tina_batch_42.md`
- Was wird gebaut: Reedschalter, SMD-Reedschalter, Reedsensoren, Füllstandssensoren, Magnete, kundenspezifische Sensoren mit Stecker/Kabel und Leiterplattenbaugruppen.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Werden in Wendelstein Sensoren montiert/vergossen oder alles in China/Türkei? Wo nachsehen: Katalog PIC_2024_DE_FINAL.pdf (Standortangaben je Produktlinie), Impressum/Standortseite pic-gmbh.com, Stellenanzeigen Fertigung Wendelstein, Historie-Seite. Bei Bestätigung rein ausländischer Fertigung: Rot nach E3 mit Quelle.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 78. Plasma Parylene Systems GmbH (A2.649) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 83026 Rosenheim | Quellen: `electronica/ergebnisse/tom_batch_42.md`, `tina_batch_42.md`
- Was wird gebaut: Plasmareinigung, -aktivierung, -ätzen und Plasmapolymerisation;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Ist die Firma Anlagenbauer, Lohnbeschichter oder beides, und gibt es Produkte mit Dosier-/Dicht-/Klebeschritten (z. B. Plasma-Aktivierung vor Kleben/Verguss als Prozessschritt für Demak-Kunden)? Wo nachsehen: Impressum und Produktseiten plasmaparylene.de, Handelsregister Traunstein HRB 18565. Aktion: keine, solange Rolle ungeklärt.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 79. Rosenberger Group (B2.356) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 83413 Fridolfing | Quellen: `electronica/ergebnisse/tom_batch_47.md`, `tina_batch_47.md`
- Was wird gebaut: HF-Koaxialsteckverbinder, HF-Messtechnik, HF-Steckverbinder-Systeme für Automobil-Elektronik, Medizintechnik und Industrieelektronik, Fiberoptik, Kabel-Assemblies.
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Welche Produkte (Automotive-HSD/Kabel-Assemblies, Steckverbinder) werden in Fridolfing gefertigt und gibt es dort Vergießen, Kleben oder Dosieren? Wo nachsehen: Impressum rosenberger.com (fertigende Gesellschaft), Standortseite "Headquarters Germany", Produktseiten Automotive/HSD (Made in), Stellenanzeigen mit Dosieren/Kleben/Verguss auf webtools.rosenberger.com; EP4097799 im Volltext lesen …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 80. Schmid-Multitech GmbH (B3.554) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 93105 Tegernheim bei Regensburg | Quellen: `electronica/ergebnisse/tom_batch_48.md`, `tina_batch_48.md`
- Was wird gebaut: Laut Stellenanzeigen (StepStone, S) "seit 1989 ein Hersteller passiver elektronischer Bauteile" mit Schwerpunkten AC/DC- und DC/DC-Spannungswandler, EMV-Ferrite und …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Fertigt Schmid-Multitech selbst in Tegernheim (Website/Impressum, Produktseiten mit Herkunftsangabe "Made in ...", Datenblätter der Wandler, Stellenanzeigen Produktion/Wickeln/Vergießen auf Karriereseite) oder Handel mit Partnerprodukten? Messeprofil electronica-Ausstellerportal ergänzend. Ergebnis entscheidet zwischen Grün (Eigenfertigung) und Rot (E2).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 81. Singulus Technologies AG (B1.458) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 63796 Kahl am Main, Unterfranken | Quellen: `electronica/ergebnisse/tom_batch_51.md`, `tina_batch_51.md`
- Was wird gebaut: Vakuumbeschichtungs- und nasschemische Produktionsanlagen (MEDLINE, SILEX III Solar-Fertigungssystem), Sonderanlagenbau.
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): Fertigung/Montage in Kahl mit V belegen: Stellenanzeige Sonderanlagenbau Kahl öffnen und lesen, Standortseite singulus.com. (2) Werden dort Schaltschränke/Steuerungen selbst montiert, und werden Teile geklebt, gedichtet oder vergossen? Stellenanzeigen Elektromontage Kahl. Bei V für (1) und Mittel/Hoch für Verguss: Grün (Zeile 4) erwartbar, geringe bis mittlere Priorität (Maschinenbau). Aktion …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 82. SKP Technik GmbH (A1.525/13) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 91077 Neunkirchen a. Brand | Quellen: `electronica/ergebnisse/tom_batch_52.md`, `tina_batch_52.md`
- Was wird gebaut: die Kategorie "Hersteller" mit Schwerpunkten "Kabel und isolierte Drähte", "technische Dienstleistungen für Elektrotechnik und Elektronik" und …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Was fertigt SKP Technik und wo? Firmenwebsite (nicht ermittelt; Domain über Messeprofil exhibitors.electronica.de suchen), Impressum, Stellenanzeigen Neunkirchen im Browser lesen. Aktion: nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 83. SM Selbstklebetechnik GmbH & Co.KG (A1.644) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 82275 Emmering bei Fürstenfeldbruck | Quellen: `electronica/ergebnisse/tom_batch_52.md`, `tina_batch_52.md`
- Was wird gebaut: kundenspezifische Lösungen aus Folien und Klebebändern: Etiketten/Kennzeichnung, Stanzteile, Dichtungen, Isolierungen, leitfähige Verbindungen;
- Demak-Bereich: Dichtung + Verguss + Verklebung
- Offener Auftrag (Tina): (a) Fertigt SM in Emmering selbst, mit welchen Prozessen (Stanzen, Laminieren, Dosieren)? (b) Eigene Klebstoffe oder fremde Tapes (E1)? (c) Eigentümer/Konzern. Wo: Firmenseite (Domain über Messeprofil), Impressum, Stellenanzeigen im Browser. Aktion: nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 84. SUSS MicroTec Solutions GmbH & Co. KG (B1.600) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 85748 Garching bei München | Quellen: `electronica/ergebnisse/tom_batch_54.md`, `tina_batch_54.md`
- Was wird gebaut: Lithographiesysteme (Mask Aligner, Coater, Developer) und Bondersysteme für MEMS, Verbindungshalbleiter und 3D-Integration.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): career.suss.com Job 407/29 im Browser öffnen, wörtliches Zitat zur Montage in Garching sichern (Fertigung V); Impressum/Register: welche Gesellschaft fertigt in Garching? (2) Welche Elektronikbaugruppen werden verbaut oder selbst gebaut und wo wird geklebt, gedichtet, dosiert? Produktseiten Bonder/Coater, DELO-Referenzseite lesen (Anwendung, Einheit). Aktion: nicht kontaktieren; hohe Priorität …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 85. THORA Elektronik GmbH (B3.232) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 91555 Feuchtwangen | Quellen: `electronica/ergebnisse/tom_batch_56.md`, `tina_batch_56.md`
- Was wird gebaut: Das Verzeichnis nennt EMV-Schirmprodukte (Abschirmbänder, leitfähige Gewebe, Garne, Elastomerdichtungen, Abschirmgehäuse und -bleche, EMV-Kabelverschraubungen) …
- Demak-Bereich: Dichtung
- Offener Auftrag (Tina): Konfektioniert/fertigt THORA selbst (Stanzen, Schneiden, Dichtungs-/Gewebekonfektion, mechanische Teile) oder handelt sie nur? Wo: Firmenwebsite (Domain nicht ermittelt, über Messeprofil exhibitors.electronica.de suchen), Impressum, Stellenanzeigen Feuchtwangen im Browser. Bei reinem Handel (V): Rot nach E2.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 86. W. L. Gore & Associates GmbH (B1.179) – Prio B
- Gebiet/Ort: Bayern (Dietmar) – 85640 Putzbrunn | Quellen: `electronica/ergebnisse/tom_batch_23.md`, `tina_batch_23.md`
- Was wird gebaut: PTFE/ePTFE-Membranen, Filter, Dichtungen, Fasern (Profil);
- Demak-Bereich: Verguss + Dichtung + Verklebung
- Offener Auftrag (Tina): Welche Werke (Putzbrunn, Pleinfeld, Feldkirchen) fertigen die auf der electronica gezeigten Elektronikprodukte (Kabelbaugruppen, Vents, Dichtungen)? Wo nachsehen: gore.de/standorte, Pressemitteilung Landkreis Weißenburg-Gunzenhausen zu Pleinfeld (Nr. 2026/126), Karriereseite Pleinfeld (Kabel-/Baugruppenfertigung, Kleben/Vergießen), Produktseite Gore Elektronik (Made in).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 87. Acculogic GmbH (A4.467) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 22453 Hamburg | Quellen: `electronica/ergebnisse/tom_batch_01.md`, `tina_batch_01.md`
- Was wird gebaut: Flying-Probe-Tester (Scorpion), In-Line-MDA, Prüfsoftware X-matic.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Wo werden Scorpion-/Acculogic-Systeme gebaut (Hamburg, Markham/Kanada)? Wo nachsehen: Impressum Acculogic GmbH, inTEST-10-K (Standortliste/Properties), Stellenanzeigen Hamburg (Montage/Test). Aktion: nachrangig.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 88. AEMtec GmbH (A2.319) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 12489 Berlin-Adlershof | Quellen: `electronica/ergebnisse/tom_batch_02.md`, `tina_batch_02.md`
- Was wird gebaut: Entwicklung, Industrialisierung und Fertigung von mikro- und optoelektronischen Modulen bis zu Systemen;
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): (a) Fertigung Berlin als V belegen und zuordnen, dass Underfill/Encapsulation/Kleben im Werk Berlin (nicht Dresden/Boston) läuft: aemtec.com Leistungsseiten und Impressum, adlershof.de-Meldung zum Neubau, Stellenanzeige Berlin Reinraum/Produktion. (b) Wird selbst vergossen/dispensiert und mit welchen Anlagen/Materialien (Wettbewerbereinsatz)? Wo: Technologie-/Leistungsseiten, Datenblätter …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 89. AMSYS GmbH & Co. KG (B4.201) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 55124 Mainz | Quellen: `electronica/ergebnisse/tom_batch_04.md`, `tina_batch_04.md`
- Was wird gebaut: Drucksensoren (Messzellen, SMD-Sensoren, Transmitter, 5 mbar bis 600 bar), Feuchte-, Temperatur- und Neigungssensoren.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Werden die AMSYS-Transmitter und Sensormodule in Mainz montiert/gelgeschützt oder von Partnern (TE/MEAS, Analog Microelectronics) bezogen? Wo nachsehen: Impressum und "About us" amsys.info, Datenblatt ms761.pdf ("Made in"), Stellenanzeigen AMSYS (Montage/Prüfung). Händleranteil klären (bei reinem Handel Rot nach E2).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 90. apra-norm Elektromechanik GmbH (B3.363) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 54552 Mehren, Rheinland-Pfalz | Quellen: `electronica/ergebnisse/tom_batch_04.md`, `tina_batch_04.md`
- Was wird gebaut: 19-Zoll-Netzwerk- und Industrie-Schaltschränke, Wand- und Tischgehäuse, Elektronik-Aufbausysteme, Steckeinheiten, Hutschienengehäuse, Display- und Kunststoffgehäuse;
- Demak-Bereich: Dichtung + Verguss
- Offener Auftrag (Tina): (a) In welchem Werk werden die Elektromechanik-Baugruppen (Vormontage, Verkabelung) gefertigt, Mehren/Meuspath oder anderswo (Impressum apra.de, Standortseite)? (b) Gibt es Gehäuse mit Deckeldichtung (IP-Klasse) oder verklebte/vergossene Baugruppen? Produktkatalog/Datenblätter apra.de lesen. Aktion: erst nach Beleg ansprechen, nur über Endprodukt.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 91. apra-plast Kunststoffgehäuse-Systeme GmbH (B3.363) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 54550 Daun, Rheinland-Pfalz | Quellen: `electronica/ergebnisse/tom_batch_04.md`, `tina_batch_04.md`
- Was wird gebaut: individuelle Kunststoffgehäuse vom Prototyp über Kleinserien bis mehrere tausend Stück, auch ohne Werkzeugkosten.
- Demak-Bereich: Dichtung
- Offener Auftrag (Tina): Werden die Gehäuse in Daun gefertigt (Spritzguss/Fräsen)? Und liefert apra-plast Gehäuse mit eingelegter/aufgeschäumter Dichtung (IP65/IP67) oder verklebten Teilen? Wo nachsehen: Impressum und Katalog apra.de, Datenblatt "Gehäuse IP", Stellenanzeigen Daun (Konstrukteur, Produktion). Aktion: gemeinsam mit Nr. 41.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 92. Arias GmbH (B1.446) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 58239 Schwerte, Nordrhein-Westfalen | Quellen: `electronica/ergebnisse/tom_batch_04.md`, `tina_batch_04.md`
- Was wird gebaut: Nassprozessanlagen (Wet Benches) für Labore und Fabs, Digestorien, Laminar-Flow-Einheiten, Chemikalienversorgung, Reinstwasseranlagen;
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Gehört arias zur JDT Group, und werden die Anlagen in Schwerte gefertigt? Wo nachsehen: Impressum arias.de bzw. arias.jdt-group.de, JDT-Standortseite, Handelsregister Hamm/Iserlohn (Schwerte), Pressemeldung zur Übernahme; danach Baugruppen (Heizung, Sensorik, Steuerung) mit Dichtung/Verklebung/Verguss. Patentsuche mit Anmeldervariante nachholen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 93. ASPINA GmbH (B4.310) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 65760 Eschborn, Hessen | Quellen: `electronica/ergebnisse/tom_batch_05.md`, `tina_batch_05.md`
- Was wird gebaut: Kundenspezifische Antriebslösungen: bürstenlose DC-Motoren, Schrittmotoren, Gebläse, Roboterkomponenten, Flüssigkeitspumpen für Medizin, Automotive, HVAC, Automation …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Werden in Eschborn Motoren/Baugruppen montiert, konfektioniert oder vergossen (Fertigungsbeleg), oder reiner Vertrieb/Service? Wo nachsehen: Impressum eu.aspina-group.com, Handelsregister Frankfurt (Unternehmensgegenstand ASPINA GmbH/Shinano Kenshi Europe GmbH), Stellenanzeigen Eschborn (Montage, Test, Service). Bei Bestätigung reinen Vertriebs: Rot nach E2/E3 mit Quelle.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 94. ASSMANN WSW components GmbH (B2.238) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 58513 Lüdenscheid, NRW | Quellen: `electronica/ergebnisse/tom_batch_05.md`, `tina_batch_05.md`
- Was wird gebaut: Computer- und Netzwerkstecker, IC-Sockel, Stiftleisten/Jumper, Klemmen, Kühlkörper/Strangpressprofile, Netzkabel, Modular-/USB-Kabelkonfektion, Audio-/Video-Kabel.
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Wird in Lüdenscheid (Zentrale) konfektioniert/montiert oder ist die Fertigung ausschließlich in Osteuropa/Asien (dann Rot nach E3 mit Quelle)? Wo nachsehen: Impressum und Standortseite assmann-wsw.com (assmann-wsw.com/en/current/ im Browser lesen), Stellenanzeigen Lüdenscheid (Konfektion, Produktion), Handelsregister Iserlohn (Unternehmensgegenstand), Rolle der ASSMANN Electronic GmbH.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 95. ATV Systems GmbH (C1.423) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 01189 Dresden | Quellen: `electronica/ergebnisse/tom_batch_06.md`, `tina_batch_06.md`
- Was wird gebaut: Automatisierung, kundenspezifische Software, digitale Prozessautomatisierung, hochpräzise Positioniersysteme, Mess- und Prüfdienstleistungen ;
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Hat ATV Systems eigene Produkte/Fertigung (Positioniersysteme) oder nur Integration/Vertrieb? Bei Nur-Vertrieb/Dienstleistung Rot nach E2 mit Quelle. Wo nachsehen: Impressum und Produktseiten atv-systems.de, Stellenanzeigen Dresden. Aktion: keine.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 96. Brooks Instrument GmbH (B1.766) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 01109 Dresden, Sachsen | Quellen: `electronica/ergebnisse/tom_batch_08.md`, `tina_batch_08.md`
- Was wird gebaut: Massendurchflussregler und -messer.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Gibt es Fertigung oder Montage von Durchflussreglern in den Niederlanden (Veenendaal/Ede) oder in Dresden? Wo nachsehen: Brooks-Seite "About us"/Standorte (brooksinstrument.com/en/about-us), Impressum Brooks Instrument GmbH und Brooks Instrument BV, Stellenanzeigen Montage/Produktion NL. Wenn nur Service/Vertrieb: Rot nach E2/E3 mit Quelle.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 97. btv technologies GmbH (B5.481) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 59423 Unna, Nordrhein-Westfalen | Quellen: `electronica/ergebnisse/tom_batch_08.md`, `tina_batch_08.md`
- Was wird gebaut: Dienstleistungen rund um elektronische Bauteile: Komponentenmanagement, Logistik, Programmierung, Test, Montage, Langzeitlagerung.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Montiert btv in Unna selbst Baugruppen/Endprodukte, und gehören Vergießen, Kleben oder Dosieren zum Leistungsumfang? Wo nachsehen: Firmenwebsite/Impressum, DQS-Zertifikatsumfang (Referenz 257791), Stellenanzeige Montage Unna im Original. Ist der Umfang nur Programmieren/Test/Gurten/Logistik: Rot nach E2 mit Quelle.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 98. Cathedy GmbH (A5.200) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 22848 Norderstedt, Schleswig-Holstein | Quellen: `electronica/ergebnisse/tom_batch_09.md`, `tina_batch_09.md`
- Was wird gebaut: externe AC/DC-Netzteile, Wandstecker- und Tischnetzteile 5 bis 76 V, bis 330 W, für Büroelektronik, Set-Top-Boxen, Netzwerk, POS.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Wird in Norderstedt gefertigt/montiert/vergossen oder nur importiert (Fertigung in Shenzhen)? Wo nachsehen: Firmenimpressum/Website (Domain suchen, Shop-Impressum auf ebay.de im Browser lesen), Handelsregister (Registergericht, Gegenstand der Gesellschaft), Stellenanzeigen Norderstedt, Produktetikett "Made in". Bei Bestätigung der Importrolle Rot nach E3/E2.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 99. CEFEG GmbH Federn- und Verbindungstechnik Chemnitz (B2.428) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 09116 Chemnitz, Sachsen | Quellen: `electronica/ergebnisse/tom_batch_09.md`, `tina_batch_09.md`
- Was wird gebaut: Federn aus Draht und Band (Druck-, Zug-, Schenkel-, Flachfedern), Stanzbiegeteile, Biegeteile aus Draht, Baugruppen (Schweißen, Nieten, Clinchen, Laserschweißen) für …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Welche Baugruppen (Elektronik/Sensor/Medizintechnik, Steckverbinder-Kontakte) fertigt CEFEG, und enthalten sie Kleb-, Dicht-, Umspritz- oder Vergussschritte (auch zugekaufte, verbaute Teile)? Wo nachsehen: cefeg.de Produktseite "Baugruppen", Kundenbranchen, Stellenanzeigen Montage/Baugruppenfertigung Chemnitz, Impressum (Sitz = Fertigungsort, V).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 100. CEM Test Instruments GmbH (A4.568) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 40547 Düsseldorf | Quellen: `electronica/ergebnisse/tom_batch_10.md`, `tina_batch_10.md`
- Was wird gebaut: Messeprofil: "30-year electronics manufacturer" für Prüfgeräte Energie/Medizin;
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Gibt es in Düsseldorf Montage, Konfektionierung oder Fertigung (Fertigungsbeleg) oder nur Vertrieb? Wo nachsehen: Impressum/Website der GmbH (Domain nicht bestätigt), Handelsregister Düsseldorf (Gegenstand: Vertrieb), Stellenanzeigen Lager/Montage. Bei V-Beleg "nur Vertrieb": Rot nach E2/E3 mit Quelle. Aktion: nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 101. Condair GmbH (C3.575) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 22848 Norderstedt, Schleswig-Holstein | Quellen: `electronica/ergebnisse/tom_batch_11.md`, `tina_batch_11.md`
- Was wird gebaut: Luftbefeuchtung und Verdunstungskühlung: Elektroden-Dampfbefeuchter (Condair EL, RS, RM, GS), Direkt-Raumbefeuchtung, Wasseraufbereitung.
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Fertigt die Condair Operations GmbH in Norderstedt Dampfbefeuchter (Condair EL/RS/RM) inkl. Steuerung/Heizelementen? Wo nachsehen: https://www.condairgroup.com/company-information/condair-operations-germany und Standortbroschüre lesen (V mit Zitat); Stellenanzeige "Mitarbeitender in der Produktion" im Original lesen; Produktdatenblatt RS "Made in/Hersteller". (2) Impressum condair.de: Welche …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 102. Coronex Electronic GmbH (A1.643) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 40880 Ratingen, Nordrhein-Westfalen | Quellen: `electronica/ergebnisse/tom_batch_11.md`, `tina_batch_11.md`
- Was wird gebaut: EMS: Beschaffung, Bestückung von Leiterplatten, komplexe Baugruppen und Fertiggeräte (Box Build), Kabel/Kabelbäume, Prototyping, Test, ATEX-Zulassung.
- Demak-Bereich: Verguss + Verklebung + Dichtung
- Offener Auftrag (Tina): Fertigt Coronex heute in Ratingen (aktuelle Quelle 2025/26: coronex.de Leistungen/Maschinenpark, Stellenanzeige Bestückung/Montage)? (2) Werden Verguss, Schutzlack, Dosieren oder Kleben angeboten oder genannt (Leistungsseite, ATEX-Seite, Kundenreferenzen)? (3) Impressum/Register Ratingen (Identität). Patent: Google Patents Anmelder "Coronex" in Browser. Bei (1) mit V und Verguss A Mittel: Grün …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 103. DAS Environmental Expert GmbH (B1.261) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 01219 Dresden, Sachsen | Quellen: `electronica/ergebnisse/tom_batch_12.md`, `tina_batch_12.md`
- Was wird gebaut: Point-of-Use-Abgasreinigungs- und Abwasseranlagen für die Halbleiterindustrie (Brenner-Wäscher-Systeme wie ESCAPE, Gaswäscher, Trockenbrenner, Partikelabscheider) …
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Fertigung Dresden belegen: Stellenanzeige "Mitarbeiter Fertigung" im Original öffnen (Karriereseite das-ee.com oder StepStone) und Standortseite/Impressum lesen. (2) Gesellschafter: Handelsregister Dresden HRB 3716, Gesellschafterliste (Dürr ausschließen). (3) Werden Schaltschränke/Sensorik vergossen oder gedichtet (Datenblatt, Schaltschrank-Fertigung)? Aktion: nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 104. DBK EMS GmbH & Co. KG (A1.525/11) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 76761 Rülzheim, Rheinland-Pfalz | Quellen: `electronica/ergebnisse/tom_batch_13.md`, `tina_batch_13.md`
- Was wird gebaut: EMS-Anbieter für Leiterplattenbestückung, Baugruppenmontage und Systembau.
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): Wird in Rülzheim durch DBK EMS vergossen, verklebt, gedichtet oder lackiert, und gibt es einen Fertigungsbeleg in Stufe V? Wo nachsehen: Website der DBK Group (EMS-Seite, Impressum DBK EMS GmbH & Co. KG), Stellenanzeigen im Original (StepStone/Karriereseite) mit Stichwörtern Verguss/Dosieren/Selektivbeschichten, Maschinenpark-Seite. Aktion: Beobachtung, nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 105. Dehner Elektronik GmbH (A5.220) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 65375 Oestrich-Winkel, Hessen | Quellen: `electronica/ergebnisse/tom_batch_13.md`, `tina_batch_13.md`
- Was wird gebaut: Netzteile, Steckernetzteile, LED-Netzteile und LED-Treiber, laut Verzeichnis Fokus auf Vertrieb und Beschaffung.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Montiert, vergießt oder entwickelt Dehner Elektronik Netzteile in Oestrich-Winkel selbst, oder wird ausschließlich importiert (E2)? Wo nachsehen: Firmenwebsite/Impressum (Domain unbestätigt), Handelsregister Wiesbaden (Unternehmensgegenstand), Herstellerangabe in weiteren Datenblättern/Typenschildern (Made in), Stellenanzeigen Montage/Prüffeld. Bei Importeur bestätigt: Rot nach E2. Aktion: nicht …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 106. DISPLAY Elektronik GmbH (B6.402) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 63667 Nidda, Hessen | Quellen: `electronica/ergebnisse/tom_batch_14.md`, `tina_batch_14.md`
- Was wird gebaut: Display-Lieferant seit 1984, beschreibt sich als Hersteller;
- Demak-Bereich: Verklebung + Dichtung
- Offener Auftrag (Tina): Montiert/fertigt DISPLAY Elektronik in Nidda selbst (Tastaturen, Module, Bonding) oder lässt extern fertigen/handelt? Wo nachsehen: Website display-elektronik.de (Impressum, "Über uns", Produktion), Karriereseite Nidda, Datenblätter "Made in". Bei reinem Handel: Rot E2 mit Quelle. Aktion: nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 107. Drews Electronic GmbH (A1.525/9) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 47475 Kamp-Lintfort, Nordrhein-Westfalen | Quellen: `electronica/ergebnisse/tom_batch_15.md`, `tina_batch_15.md`
- Was wird gebaut: Elektronikfertigung (EMS): "Bestückung von Leiterplatten", Fertigung elektronischer Baugruppen, Materialbeschaffung und technische Prüfung, "vom Prototyp bis zur …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): (a) Wird in Kamp-Lintfort selbst gefertigt (Fertigungsbeleg V: Impressum, Standortseite, Stellenanzeige Produktion im Original)? (b) Welche Kundenbranchen, bietet Drews Schutzlack/Verguss/Dosieren an? Wo nachsehen: Firmenwebsite (Domain über Handelsregister/Impressum ermitteln), Leistungsseite, StepStone-Firmenprofil. Aktion: niedrig priorisieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 108. ELEKTRISOLA Dr. Gerd Schildbach GmbH & Co. KG (A5.240) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 51580 Reichshof-Eckenhagen, NRW | Quellen: `electronica/ergebnisse/tom_batch_16.md`, `tina_batch_16.md`
- Was wird gebaut: Kupferlackdraht, Backlackdraht (Selfbonding), voll isolierter Draht und Hochfrequenzlitze.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Liefert Elektrisola Spulen, Wickelgüter oder konfektionierte Litzen (Verguss/Verklebung bei Elektrisola selbst, z. B. Backlackdraht-Wicklungen, Isolierung von Litzenenden)? Welche Produkte entstehen im Werk Eckenhagen? Wo nachsehen: elektrisola.com Produkt- und Standortseiten, Impressum, Patent Google Patents mit Anmelder "Elektrisola" und "Dr. Gerd Schildbach". Aktion: vorerst nicht ansprechen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 109. Elektrosil GmbH (B3.460) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 22761 Hamburg | Quellen: `electronica/ergebnisse/tom_batch_16.md`, `tina_batch_16.md`
- Was wird gebaut: Das Verzeichnis nennt als Produktkategorien LIN-Bussysteme, Kleinmotoren, Thermomanagement für Brennstoffzellen, Steckverbinder, Softwareentwicklung, Simulation …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Werden Baugruppen/Kleinmotoren in Hamburg gefertigt oder an Dritte vergeben (Fertigungsbeleg)? Wo nachsehen: elektrosil.com (Produkte, "Über uns", Impressum), embedded-world-Ausstellerprofil im Original, Stellenanzeigen Hamburg (Montage/Prüffeld), Handelsregister Hamburg (Unternehmensgegenstand). Aktion: nach Klärung ansprechen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 110. ELEMENT 3-5 GmbH (C1.323) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 52499 Baesweiler bei Aachen | Quellen: `electronica/ergebnisse/tom_batch_16.md`, `tina_batch_16.md`
- Was wird gebaut: Epitaxie- und Plasmasysteme sowie Ionen-/Plasmaquellen für Chiphersteller, AlN-Beschichtungsanlage.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Enthalten die Anlagen oder Plasma-/Ionenquellen vergossene, verklebte oder gedichtete Baugruppen aus eigener Fertigung (Hochspannungsversorgung, Sensorik, Vakuumdurchführungen)? Wo nachsehen: Produktseiten element3-5.com, Datenblätter, Stellenanzeigen (Montage/Elektronik Baesweiler). Aktion: nicht priorisieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 111. EMI-tec Elektronische Materialien GmbH (B3.257) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 12277 Berlin | Quellen: `electronica/ergebnisse/tom_batch_17.md`, `tina_batch_17.md`
- Was wird gebaut: Vertriebsseite dacpol.eu : "EMI-tec Form-in-Place Gaskets" mit Micro-Sil-Compound, Dichtungsbreiten 0,3 bis 1,8 mm, entwickelt für Luftfahrt, Automotive, Telekom.
- Demak-Bereich: Dichtung
- Offener Auftrag (Tina): (a) Verkauft EMI-tec Dichtungsmassen/Compounds (Materialhersteller, dann Rot nach E1) oder fertigt es Dichtungen auf Kundenteilen (FIPFG-Anwender)? (b) Ist die Firma in Berlin (PLZ 12277) ansässig und fertigt dort? Wo nachsehen: Website der Firma (Domain unbekannt, über Dacpol/Datenblatt-Impressum ermitteln), Impressum, Handelsregister Berlin-Charlottenburg, Produktseiten "Form-in-Place Gaskets" …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 112. Ernst & Engbring GmbH (B2.211) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 45739 Oer-Erkenschwick, NRW | Quellen: `electronica/ergebnisse/tom_batch_15.md`, `tina_batch_15.md`
- Was wird gebaut: Entwicklung und Produktion von Spezialleitungen und Kabeln für Kommunikation, Signal, Daten, Medizin, Robotik, Mess-/Regeltechnik;
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): (a) Welche Werke fertigen (Oer-Erkenschwick, Brandenburg/Forst, Ukraine, China) und wo werden die Kabel mit angespritzten Steckern konfektioniert? Wo nachsehen: eue-kabel.de (Standorte, Impressum), Elektronikpraxis-Artikel 2007, Stellenanzeigen. (b) Harzverguss (PU/Epoxid) oder thermoplastisches Überspritzen? Wo nachsehen: Produkt-/Konfektionsseiten, Datenblätter. Aktion: Messegespräch …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 113. Excelitas Technologies (B4.302) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 65199 laut Liste Wiesbaden, Hessen | Quellen: `electronica/ergebnisse/tom_batch_19.md`, `tina_batch_19.md`
- Was wird gebaut: Thermopile- und pyroelektrische Sensoren, Hochleistungssensoren, gepulste Laser (LiDAR/3D), Fotodioden für Rauchmelder, Photon-Counting-Module, industrielle Blitzlampen.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): (a) Werden Sensoren/Fotodioden/Detektoren von der Excelitas Technologies GmbH & Co. KG in Wiesbaden gefertigt oder nur entwickelt und vertrieben (Fertigung dann in Manila u. a.)? Wo nachsehen: Impressum und Standortseite excelitas.com/location/wiesbaden-germany im Browser, jobs.excelitas.com mit Filter Wiesbaden (Produktion/Montage), Datenblätter IR-Sensoren (Herkunftsangabe). (b) Gibt es …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 114. Finetech GmbH & Co. KG (C1.836) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 12681 Berlin-Marzahn | Quellen: `electronica/ergebnisse/tom_batch_20.md`, `tina_batch_20.md`
- Was wird gebaut: Hochpräzisions-Die-Bonder und Flip-Chip-Bonder (FINEPLACER, FiNEXT), SMD-Rework-Systeme.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): (a) Was wird in Berlin-Marzahn gefertigt/montiert (Maschinenbau, Elektronikfertigung)? Standort-/Karriereseite finetech.de, Impressum, Stellenanzeigen "Montage/Produktion" (V nötig wegen Konzern). (b) Setzt Finetech eigene Klebstoffe/Vergussmassen oder Dosierwerkzeuge ein, und ist MARTIN/Finetech Wettbewerber im Dosiergeschäft (E1)? Impressum und Produktseiten FINEPLACER/MARTIN. (c) Entscheidung …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 115. Gaptec Electronic GmbH & Co. KG (A5.103) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 63225 Langen, Hessen | Quellen: `electronica/ergebnisse/tom_batch_22.md`, `tina_batch_22.md`
- Was wird gebaut: isolierte und nicht isolierte Wandler AC-DC, DC-DC, POL, LED-Treiber, 0,1 bis ca.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Findet in Langen Fertigung, Montage oder Verguss statt, oder ausschließlich in Taiwan/China (E3 mit V belegen)? Wo nachsehen: gaptec-electronic.com ("Über uns", Impressum), Datenblatt "Made in", Stellenanzeigen Langen (Fertigung, Qualität). Bei Bestätigung Rot nach E3 mit URL.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 116. Glenair GmbH (A3.125) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 61348 Bad Homburg, Hessen | Quellen: `electronica/ergebnisse/tom_batch_23.md`, `tina_batch_23.md`
- Was wird gebaut: Mil-Spec-Rundsteckverbinder, Rechtecksteckverbinder, Backshells, Kabelkonfektion.
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Welche Produkte werden in Salem (und evtl. Bad Homburg) gefertigt, und ist die ausstellende Gesellschaft die fertigende Einheit? Wo nachsehen: Karriereseite Glenair GmbH (Stellen Kabelmontage/Produktion Salem), Impressum glenair.de, Handelsregister; Verguss-Hinweise in Stellenanzeigen (Vergießen, Potting, Kleben).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 117. Group Intellect Power Technology Europe GmbH (A5.418) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 48155 Münster, NRW | Quellen: `electronica/ergebnisse/tom_batch_23.md`, `tina_batch_23.md`
- Was wird gebaut: Ladegeräte, Adapter, Schaltnetzteile von 1 bis 3000 Watt, Transformatoren, OEM/ODM-Fertigung.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Gibt es in Münster Montage/Fertigung oder nur Vertrieb/Entwicklung? Wo nachsehen: Handelsregister Münster (Unternehmensgegenstand), Impressum der Konzernseite, Stellenanzeigen (Montage/Produktion Münster), Messeprofil electronica. Bei Vertrieb ohne Fertigung Rot nach E2/E3 mit Quelle.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 118. Hürner Luft- und Umwelttechnik GmbH (C2.253) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 35325 Mücke-Atzenhain, Hessen | Quellen: `electronica/ergebnisse/tom_batch_26.md`, `tina_batch_26.md`
- Was wird gebaut: Kunststoff-Ventilatoren (Gehäuse PE, Laufrad PP), Zu- und Abluftanlagen, Abluftwäscher, Behälter, Kunststoff-Wärmetauscher, Schalldämpfer.
- Demak-Bereich: Dichtung + Verguss
- Offener Auftrag (Tina): (a) Wird die Elektrik (Motoren, Steuerung, Frequenzumrichter) in Mücke-Atzenhain gefertigt/montiert oder zugekauft, und was passiert in Ransbach-Baumbach? Wo nachsehen: hlu.eu Impressum und Standortseiten, Datenblätter Ventilatoren/Antriebe, Stellenanzeigen Produktion/Elektromontage, Broschüre HLU 01/2021 (Zitat "fertigen wir nahezu alle Ventilatoren ... in unserem Werk" im Original prüfen). (b) …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 119. IK Elektronik GmbH (A1.525/14) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 08262 Muldenhammer OT Hammerbrücke, Sachsen; Zweigstelle Dresden | Quellen: `electronica/ergebnisse/tom_batch_26.md`, `tina_batch_26.md`
- Was wird gebaut: Antennen, Funkmodule, Funksensoren, Funksysteme und HF-Baugruppen als Entwicklung und EMS (SMT-/THT-Bestückung, Montage, Geräteprüfung;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): (a) Fertigungsbeleg V: Impressum und Produktions-/EMS-Seite ik-elektronik.de, Stellenanzeige Produktion/Bestückung Hammerbrücke. (b) Werden Funksensoren, Antennen oder EMS-Baugruppen vergossen oder verklebt (Datenblatt Schutzart, Broschüre "Verguss auf Kundenwunsch" im Original lesen) und welche EMS-Kundenbranchen? Aktion: Beobachtung.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 120. Ikegami Electronics (Europe) GmbH (B5.261) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 41460 Neuss, NRW | Quellen: `electronica/ergebnisse/tom_batch_26.md`, `tina_batch_26.md`
- Was wird gebaut: nichts belegt.
- Demak-Bereich: Verklebung
- Offener Auftrag (Tina): Gibt es Montage, Reparatur mit Teilefertigung oder Konfektionierung in Neuss, oder reiner Vertrieb/Service (E2)? Wo nachsehen: Handelsregister Neuss (Unternehmensgegenstand), Impressum ikegami.de, Stellenanzeigen Neuss (Service/Montage). Bei Bestätigung Rot nach E2 mit URL. Aktion: nicht priorisieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 121. IMST GmbH (C5.164) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 47475 Kamp-Lintfort, NRW | Quellen: `electronica/ergebnisse/tom_batch_27.md`, `tina_batch_27.md`
- Was wird gebaut: Entwicklung von Hochfrequenzschaltungen, Funkmodulen, Antennen, Radarlösungen;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Fertigt IMST Module selbst in Kamp-Lintfort (Montage/Serie) oder über EMS? Wo nachsehen: Karriere- und Produktseiten imst.de (Stellenanzeigen Montage/Fertigung, Datenblatt iM891A: "Made in"), Impressum/Handelsregister Kamp-Lintfort. Bei reinem Design-Haus: Rot nach E2 mit Quelle. Aktion: keine.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 122. INFICON (B1.730) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 50968 Köln, NRW | Quellen: `electronica/ergebnisse/tom_batch_27.md`, `tina_batch_27.md`
- Was wird gebaut: Lecksuchgeräte (Helium-/Wasserstoff-Schnüffler XL3000flex, Sentrac mit Sensistor-Sensor), Vakuum-Messtechnik, Sensortechnologien.
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Welche Produkte werden in Köln montiert (Lecksucher, DFT-Linie), und enthalten sie vergossene/verklebte Baugruppen (Sensor, Elektronik) aus eigener oder zugekaufter Fertigung? Wo nachsehen: Standortseite Köln und Karriereseite inficon.com (Stellenanzeige im Original), Impressum INFICON GmbH, Datenblatt XL3000flex/Contura (Schutzart, Sensor). Aktion: keine Kontaktaufnahme vor Klärung.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 123. Intermas-Elcom GmbH (B3.342) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 64293 Darmstadt, Hessen | Quellen: `electronica/ergebnisse/tom_batch_27.md`, `tina_batch_27.md`
- Was wird gebaut: Elektronikschränke (19-Zoll), Gehäuse, Baugruppenträger, Einschubkassetten, Netzwerkschränke.
- Demak-Bereich: Dichtung + Verguss
- Offener Auftrag (Tina): (a) Wird in Darmstadt gefertigt oder zugekauft (Fertigungsbeleg)? (b) Gehört die Firma zu einer Gruppe (Regel M)? (c) Werden Gehäuse mit Dichtungen (aufgeschäumt/dosiert) geliefert? Wo nachsehen: Impressum und Standortseite intermas-el.com, Handelsregister Darmstadt, Katalog/Datenblätter Gehäuse (Dichtung, EMV), Stellenanzeigen Darmstadt. Aktion: keine Kontaktaufnahme vor (a) und (b).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 124. Jintian Copper (Germany) GmbH (B2.147) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 60325 Frankfurt am Main | Quellen: `electronica/ergebnisse/tom_batch_29.md`, `tina_batch_29.md`
- Was wird gebaut: Konzern: Kupferrohre, -stangen, -bänder, Lackdraht (enameled wire), NdFeB-Dauermagnete u.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Gibt es Fertigung oder Montage in DE/AT/NL (Frankfurter Gesellschaft: Handel oder Produktion)? Wo nachsehen: Impressum/Handelsregister Frankfurt, en.jtcopper.com/about und /company-profile (Standortliste "production bases"), electronica-Ausstellerprofil B2.147. Ohne Produktion in DE/AT/NL: Rot E3/E2 mit Quelle.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 125. Kelington Engineering (Germany) GmbH (C1.105) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 01067 Dresden, Sachsen | Quellen: `electronica/ergebnisse/tom_batch_30.md`, `tina_batch_30.md`
- Was wird gebaut: "Design, Installation, Test und Inbetriebnahme" von Ultrahochreinheits-Gas- und Chemikalienverteilungen sowie Lieferung von Gasschränken, Gaspanels, Ventilmanifolds.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Fertigt die GmbH (Gaspanels, Schränke) in Dresden oder installiert sie nur beim Kunden? Wo nachsehen: Impressum/Standortseite der Gesellschaft (Domain unbekannt, über Silicon-Saxony-Profil), Handelsregister Dresden (Gegenstand), Stellenanzeigen Dresden (Montage/Werkstatt). Aktion: nicht priorisieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 126. Kikusui Electronics Europe GmbH (A4.159) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 40472 Düsseldorf | Quellen: `electronica/ergebnisse/tom_batch_30.md`, `tina_batch_30.md`
- Was wird gebaut: Gruppe: DC-/AC-Netzgeräte, elektronische Lasten, Hipot-/Isolationsprüfgeräte.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Montiert/fertigt die GmbH in Düsseldorf oder nur Vertrieb/Service? Wo nachsehen: Impressum der europäischen Kikusui-Seite (Gegenstand), Handelsregister Düsseldorf, Stellenanzeigen. Bei reinem Vertrieb Rot nach E2 mit Quelle. Aktion: nicht priorisieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 127. Kingbright Electronic Europe GmbH (C6.479) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 47661 Issum, Nordrhein-Westfalen | Quellen: `electronica/ergebnisse/tom_batch_30.md`, `tina_batch_30.md`
- Was wird gebaut: Kingbright-Produkte sind LED-Bauteile (THT- und SMD-LEDs, S).
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Impressum/Handelsregister der Gesellschaft (Gegenstand Vertrieb?) lesen; gibt es Montage/Konfektion in Issum? Bei reinem Vertrieb Rot nach E2 mit Quelle. Aktion: nicht priorisieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 128. Kokusai Semiconductor Europe GmbH (C1.219) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 40699 Erkrath, NRW; Liste schreibt "Ekrath" … | Quellen: `electronica/ergebnisse/tom_batch_31.md`, `tina_batch_31.md`
- Was wird gebaut: Thermische Batch-Prozessanlagen (Vertron, Quixace), Metrologie- und Veraschungslösungen;
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Wird in Erkrath gefertigt/montiert (Beleg), und enthalten die Anlagen dort Dosier-/Klebe-/Vergussschritte? Wo nachsehen: Impressum kokusai-se.com, Stellenanzeigen Erkrath, Handelsregister Wuppertal. Aktion: nicht priorisieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 129. Kurt J. Lesker Company GmbH (B1.316) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 01259 Dresden, Sachsen | Quellen: `electronica/ergebnisse/tom_batch_32.md`, `tina_batch_32.md`
- Was wird gebaut: Einkammer-Beschichtungssysteme und Cluster-Tools mit Robotertransfer für Produktion und Forschung.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Fertigt oder montiert die Dresdner GmbH Systeme selbst, oder ist sie reine Vertriebs-/Servicegesellschaft (dann E2/E3 mit Quelle, Rot)? Wo nachsehen: Impressum und Standortseite lesker.com (deutsche Seite), Handelsregister Dresden, Stellenanzeigen Dresden (Montage/Test).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 130. Linux Automation GmbH (C5.178) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 31137 Hildesheim, Niedersachsen | Quellen: `electronica/ergebnisse/tom_batch_33.md`, `tina_batch_33.md`
- Was wird gebaut: Hardware für Embedded-Linux-Test und Entwicklung: LXA TAC (Test Automation Controller mit Stromversorgungsschaltung bis 48 V / 5 A, UART, CAN, USB), Sensor- und …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Wo wird die LXA-TAC-Hardware gefertigt (Hildesheim, Lohnfertiger, Ausland)? Wo: Produktseite/Datenblatt/Shop linux-automation.com ("Made in"), Pengutronix-Blog zur Produktion, Stellenanzeigen Fertigung/Test in Hildesheim.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 131. LPKF Laser & Electronics SE (A2.219) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 30827 Garbsen, Niedersachsen | Quellen: `electronica/ergebnisse/tom_batch_33.md`, `tina_batch_33.md`
- Was wird gebaut: Lasersysteme für Leiterplatten-Prototyping und Depaneling, IC-Packaging, Schablonen, Laser Direct Structuring (LDS), Kunststoffschweißen, Solar- und Batteriefertigung.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Welche Systeme werden aktuell in Garbsen gebaut/montiert (nicht nur Zentrale)? Wo: Standortseite lpkf.com, Geschäftsbericht 2025 (Segment/Standortliste), Stellenanzeigen Montage/Elektronik Garbsen. Anlagenbauer (Block C): Zielgruppe mit Jey klären.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 132. M-O-T Mikro- und Oberflächentechnik GmbH (C1.271) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 66128 Saarbrücken, Saarland | Quellen: `electronica/ergebnisse/tom_batch_37.md`, `tina_batch_37.md`
- Was wird gebaut: laut Silicon-Saxony-Profil "complete design build manufacturer" für Nassprozessanlagen (Wet Benches, Komponenten, Systemintegration, Umwelt-Nassprozesslösung) für …
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Wo und von welcher Gesellschaft werden die Anlagen gebaut (Saarbrücken: M-O-T oder WOLL), und enthalten sie Dosier-, Kleb-, Dicht- oder Vergussschritte (Elektronik, Sensorik)? Wo nachsehen: mot-semicon.com Impressum/Produkte, Handelsregister Saarbrücken. Aktion: Beobachtung, geringe Priorität.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 133. Magic Power Technology GmbH (A5.401) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 66994 Dahn, Rheinland-Pfalz | Quellen: `electronica/ergebnisse/tom_batch_34.md`, `tina_batch_34.md`
- Was wird gebaut: "develops and manufactures standard and customized power supplies from 5W - >1000W up to CF class in mostly fanless mode" ;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Werden die Netzteile in Dahn gefertigt/montiert, oder entwickelt und in Taiwan/China gefertigt? Wo nachsehen: mgpower.de Impressum und "Über uns", Datenblätter ("Made in"), Stellenanzeigen Dahn (Karriereseite, Arbeitsagentur), Handelsregister Zweibrücken HRB 30781 (Gesellschafter). Zusätzlich: Sind Medizin-/OEM-Netzteile vollvergossen (Datenblatt)? Aktion: Beobachtung.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 134. MC Technologies GmbH (C2.616) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 30179 Hannover, Niedersachsen | Quellen: `electronica/ergebnisse/tom_batch_35.md`, `tina_batch_35.md`
- Was wird gebaut: "Industrie-Router, M2M-Terminals, Hutschienen-PCs sowie Gateways" für industrielle Mobilfunk-Datenübertragung ;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Werden Konfektion (Kabel mit vergossenen/überspritzten Steckern, Solar-Stringkabel mit Vergussmasse) und Router in Hannover gefertigt? Wo nachsehen: mc-technologies.com Seiten "Custom cable assembly and development" und "Cable assembly with specialized partners" lesen, Impressum/Register (HRB 57312), Stellenanzeigen Kabelkonfektion Hannover.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 135. MCRT GmbH (C1.856) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 35452 Heuchelheim bei Gießen, Hessen | Quellen: `electronica/ergebnisse/tom_batch_35.md`, `tina_batch_35.md`
- Was wird gebaut: "customer specific cleanroom solutions" (Reinraum-Anlagen, Mini-Environments für die Halbleiterindustrie;
- Demak-Bereich: Dichtung + Verguss
- Offener Auftrag (Tina): Wird in Heuchelheim heute noch gefertigt (Filter-Fan-Units), und gibt es Dichtungs-/Klebeschritte? Wo nachsehen: mcrt.de Produktseiten und Impressum, Karriereseite (Montage), aktuelle Standortangabe Amelicor-Seite.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 136. Metrel GmbH (A4.570) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 46539 Dinslaken, NRW | Quellen: `electronica/ergebnisse/tom_batch_36.md`, `tina_batch_36.md`
- Was wird gebaut: Mess- und Prüfgeräte für elektrische Installationen , gefertigt in Slowenien.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Ist Metrel GmbH Dinslaken ausschließlich Vertriebs-/Servicegesellschaft ohne Montage (E2) und wird alles in Horjul gefertigt (E3)? Wo nachsehen: https://metrel.si/en/content/about-en/company-structure.html im Wortlaut lesen, Impressum metrel.de, Stellenanzeigen Dinslaken (Montage/Fertigung?). Bei Bestätigung: Rot nach E2/E3 mit Zitat.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 137. micronex GmbH (A1.525/18) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 31832 Springe, Niedersachsen, laut Messeliste | Quellen: `electronica/ergebnisse/tom_batch_36.md`, `tina_batch_36.md`
- Was wird gebaut: EMS-Dienstleistungen: elektronische und mechatronische Baugruppen, Projektmanagement, Werkzeugbau, Materiallogistik, After-Sales.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Wo fertigt micronex (Springe?) und für welche Branchen (Automotive/Industrie), wird vergossen/Selektivlöten/Dispensing angeboten? Wo nachsehen: micronex.de (Impressum, Leistungen/Fertigung, Referenzen), Handelsregister Hannover HRB 101041, Stellenanzeigen. Zusätzlich Konzernabgleich, falls Teil einer Gruppe.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 138. MUEGGE GmbH (C2.108) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 64385 Reichelsheim im Odenwald, Hessen | Quellen: `electronica/ergebnisse/tom_batch_38.md`, `tina_batch_38.md`
- Was wird gebaut: "leading manufacturer of industrial microwave components, systems, and plasma sources" ;
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Werden die Generatoren/Netzteile in Reichelsheim gefertigt und montiert (Fertigungsbeleg V), und ist das die fertigende Einheit neben den Schwestergesellschaften? Wo nachsehen: Impressum muegge.de, Standortseite/Karriereseite (Montage, Elektronikfertigung), Unternehmensregister Darmstadt HRB 70541 (aktueller Status, Firmierung), Datenblatt Generator (Netzteil/Trafo, Vergussangabe). Zugleich …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 139. N&H Technology GmbH (B3.361) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 47877 Willich, NRW | Quellen: `electronica/ergebnisse/tom_batch_38.md`, `tina_batch_38.md`
- Was wird gebaut: "developing and manufacturing custom HMI components, molded parts and electromechanical assemblies" seit 2001 ;
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Welche Produkte werden in Willich montiert/gespritzt/vergossen, welche stammen aus Asien (Fertigungsbeleg V für Willich)? Wo nachsehen: Impressum und Standortseite nh-technology.de, Fachartikel "25 Jahre N&H" (nh-technology.de/en/25-jahre-nh-technology), Karriereseite (Montage, Produktion), Katalog 2025. Wenn nur Asien: Rot nach E3 mit Quelle.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 140. NanoFocus AG (C1.553) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 46049 Oberhausen, NRW | Quellen: `electronica/ergebnisse/tom_batch_38.md`, `tina_batch_38.md`
- Was wird gebaut: optische und taktile Messsysteme und Software für technische Oberflächen: µsurf (konfokales Multi-Pinhole-3D-System), µscan (optisches Scanning-Profilometer), µsprint …
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): Werden die Sensoren (µsurf/µscan) weiterhin in Oberhausen gefertigt oder in andere Mahr-Werke (Göttingen/Esslingen) verlagert, und wo ist der Vergussschritt? Wo nachsehen: Impressum nanofocus.com/.de, Standortseite Mahr-Gruppe, Pressemeldung zur Integration, Karriereseite (Montage, Produktion), Datenblatt µsurf (Schutzart, Sensorkopf). Patente: Google Patents/Espacenet mit Anmelder "NanoFocus AG" …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 141. Neosid Pemetzrieder GmbH & Co. KG (A6.500) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 58553 Halver, NRW | Quellen: `electronica/ergebnisse/tom_batch_38.md`, `tina_batch_38.md`
- Was wird gebaut: spritzgegossene Weichferrit-Komponenten, induktive Bauelemente und kundenspezifische Sensorspulen sowie miniaturisierte HF-RFID-Transponder (NeoTAG, 13,56 MHz) für …
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): (a) Wird Neosid-Ware (Spulen/Induktivitäten/Transponder) in Halver gefertigt, oder teils bei NEOTECH in Polen/anderen Werken (Fertigungsbeleg V)? (b) Werden Spulen und Transponder vergossen, verklebt oder in Gehäuse gedichtet (Hoch bleibt A bis zum Beleg)? Wo nachsehen: Impressum und Standortseite neosid.de, Datenblätter (z. B. P 0724 NeoTAG), Karriereseite (Produktion, Vergießen, Montage) …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 142. Nikon Metrology GmbH (B1.117) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 40472 Düsseldorf laut Eingabe | Quellen: `electronica/ergebnisse/tom_batch_39.md`, `tina_batch_39.md`
- Was wird gebaut: Koordinatenmessgeräte, optische CMM, 3D-Laserscanner, Röntgen-/CT-Systeme, Messmikroskope, Large-Volume-Metrology.
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): Montiert oder fertigt die Düsseldorfer GmbH selbst Messgeräte, oder ist sie reine Vertriebs-/Servicegesellschaft (dann E2)? Wo: Impressum industry.nikon.com/de-de, Stellenanzeigen Düsseldorf (Montage/Produktion), Handelsregister Düsseldorf. Aktion: nicht priorisieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 143. NOFFZ Technologies GmbH (A4.418) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 47918 Tönisvorst, NRW | Quellen: `electronica/ergebnisse/tom_batch_39.md`, `tina_batch_39.md`
- Was wird gebaut: Automatische Testsysteme (ATE, ICT/FCT, AOI), Universal Tester Platform (UTP), Radar-Testsystem UTP 5065, Bildverarbeitung für LED-/Display-Inspektion und …
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): Werden die Testsysteme/Kleinserien-Baugruppen in Tönisvorst montiert und dort Bauteile vergossen, verklebt oder gedichtet? Wo: Stellenanzeige im Original (arbeitsagentur.de Detail 10000-1202733172-S) und Karriereseite noffz.com lesen; Impressum (Adresse Vorster Straße 238 oder Tempelsweg 24a, Register); Standortseite (welches Werk fertigt was). Bei V-Beleg Tönisvorst und Elektronikmontage: Grün.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 144. PeakTech Prüf- und Messtechnik GmbH (A4.529) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 22926 Ahrensburg, Schleswig-Holstein | Quellen: `electronica/ergebnisse/tom_batch_41.md`, `tina_batch_41.md`
- Was wird gebaut: Elektronische Mess- und Prüfgeräte (Multimeter, Oszilloskope, Netzgeräte/Stromversorgungen, Generatoren, Umweltmesstechnik) unter der Marke PeakTech;
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Werden PeakTech-Geräte in Ahrensburg montiert/geprüft (Endmontage, Kalibrierung) oder nur entwickelt und aus Taiwan/China zugekauft? Wo nachsehen: Zertifikat im Original (TÜV NORD Online-Datenbank, Geltungsbereich und Standorte), Firmenbroschüre 2024 und peaktech.de/Information/Quality-management (im Browser lesen), "Made in"/Herkunft auf Datenblättern oder Typenschildern, Stellenanzeigen …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 145. PMK Mess- und Kommunikationstechnik GmbH (A4.439) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 65812 Hessen: Bad Soden, Sulzbach, Groß-Umstadt | Quellen: `electronica/ergebnisse/tom_batch_42.md`, `tina_batch_42.md`
- Was wird gebaut: aktive und passive Tastköpfe, Hochspannungstastköpfe, Stromtastköpfe und Stromwandler, Kalibriergeneratoren, Hochspannungsgeräte, Netzteile, Zubehör.
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): (a) Wird in Sulzbach/Groß-Umstadt gefertigt (V-Beleg)? Impressum und Standortseite pmk.de, Stellenanzeigen Produktion/Montage Sulzbach, SAHA-Profil im Browser. (b) Stromwandler/Hochspannungstastköpfe vergossen? Datenblätter Current Transformers/BumbleBee lesen. Aktion: nach Fertigungsbeleg Ansprache möglich.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 146. Precitec Optronik GmbH (C1.432) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 63263 Neu-Isenburg, Hessen | Quellen: `electronica/ergebnisse/tom_batch_43.md`, `tina_batch_43.md`
- Was wird gebaut: Chromatisch-konfokale und interferometrische Sensoren (CHRocodile-Reihe: Punkt-, Linien-, Multipoint-Sensoren, Flächenscan, Zeilenkamera), CHRocodile C "Optoelektronik …
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): Werden die CHRocodile-Sensoren in Neu-Isenburg montiert (Fertigungsbeleg V)? Wo nachsehen: Stellenanzeige "Optik- und Gerätemontage Hightech-Sensoren" und "Production Engineer" im Original (Karriereseite precitec.com, StepStone), Impressum Precitec Optronik GmbH; zugleich Datenblatt CHRocodile C (Schutzart, Vergussmasse/Klebung). Aktion: Beobachtung.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 147. PVA TePla AG (C1.301) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 35435 Wettenberg, Hessen | Quellen: `electronica/ergebnisse/tom_batch_44.md`, `tina_batch_44.md`
- Was wird gebaut: Segment Semiconductor Systems: Kristallzuchtanlagen, Metrologie (Ultraschallmikroskope) und Plasmasysteme zur Waferreinigung;
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): Welche Anlagen/Baugruppen werden in Wettenberg tatsächlich montiert (Elektromontage der PVA Metrology & Plasma Solutions GmbH: Steuerschränke, Generatoren, Sensorik?) und enthalten sie vergossene/verklebte Teile? Wo nachsehen: Stellenanzeige Elektromontage im Original, pvatepla.com Standortseite und Produktseiten Plasma-/Metrologie-Systeme, Datenblätter Ultraschall-Transducer, Patente der Töchter …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 148. REEL Reinheimer Elektronik GmbH (C2.616) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 35625 Hüttenberg/Wettenberg, Hessen | Quellen: `electronica/ergebnisse/tom_batch_45.md`, `tina_batch_45.md`
- Was wird gebaut: Antennen: Planarantennen für GSM/GPS, Fahrzeugantennen, Basisstationsantennen, kombinierte Mobilfunk-/Telematikantennen für Autos.
- Demak-Bereich: Verguss + Verklebung + Dichtung
- Offener Auftrag (Tina): Wo werden die Antennen gefertigt (Hüttenberg/Wettenberg oder Ausland) und welche ist die aktuelle Anschrift? Wo nachsehen: reinheimer-elektronik.de Impressum/Unternehmensseite, Handelsregister Wetzlar HRB 7338, Stellenanzeigen, Datenblatt K70LFR im Original (Wortlaut "vergossen", Fertigungsvermerk). Danach Zeile 4 (Grün) bei Fertigung DE belegt. Aktion: nicht kontaktieren, bis Fertigungsort …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 149. Rorze Engineering GmbH (B1.238) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 01159 Dresden, Sachsen | Quellen: `electronica/ergebnisse/tom_batch_47.md`, `tina_batch_47.md`
- Was wird gebaut: Wafer-Handling-Roboter und Automatisierungssysteme für den Wafer-Transfer (Mutter: Reinraumroboter, Load Ports, EFEM;
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Montiert oder fertigt die Rorze Engineering GmbH in Dresden Roboter/Komponenten, oder nur Vertrieb/Service? Wo nachsehen: Impressum und Karriereseite der Firma (Rorze-Konzernseite, Standort Dresden), Handelsregister Dresden HRB 38768, Stellenanzeigen Montage/Test Dresden. Aktion: ohne Fertigungsbeleg nicht weiter verfolgen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 150. RRC power solutions (A5.218) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 66424 Homburg/Saar | Quellen: `electronica/ergebnisse/tom_batch_47.md`, `tina_batch_47.md`
- Was wird gebaut: Smart Battery Packs, Ladegeräte, Stromversorgungen, Power-Management-Module, DC-Kfz-Adapter, Kabel;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Werden Battery Packs/Ladegeräte in Homburg montiert/gefertigt, oder bei Partnern in Asien/USA? Und: Wird dort vergossen (Pack-Elektronik, Ladegeräte)? Wo nachsehen: rrc-ps.com Über uns/Produktion, Impressum (Gesellschafter/Konzern), Stellenanzeigen Homburg (Produktion, Montage, Test), Datenblätter (Herkunftsangabe), Handelsregister Saarbrücken. Aktion: erst nach Fertigungsbeleg weiter.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 151. Scanfil Electronics GmbH (A1.214) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 99848 Wutha-Farnroda, Thüringen | Quellen: `electronica/ergebnisse/tom_batch_48.md`, `tina_batch_48.md`
- Was wird gebaut: EMS-Dienstleistungen: Leiterplattenbestückung, Chip-on-Board, mechanische Montage, Systemintegration, Entwicklung, Prototyping, Prüfmittelentwicklung, Reparatur.
- Demak-Bereich: Verguss + Verklebung + Dichtung
- Offener Auftrag (Tina): (a) Vergießen, Dosieren, Kleben oder Schutzlack im Werk Wutha-Farnroda? Scanfil.com Standortseite/Capabilities, Stellenanzeigen (Karriereseite, StepStone) im Wortlaut lesen; (b) V-Beleg für Fertigung in Wutha-Farnroda (Standortseite oder Pressemeldung im Wortlaut, Abrufdatum); (c) Frische: Meldungen nach 2022 zum Werk prüfen. Sind (a) und (b) mit V belegt, ist Zeile 4 erreichbar.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 152. Sensitec GmbH (B4.119) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 35578 Wetzlar, Hessen; zweiter Standort Mainz | Quellen: `electronica/ergebnisse/tom_batch_50.md`, `tina_batch_50.md`
- Was wird gebaut: magnetoresistive Sensoren (AMR, GMR, TMR) als Sensorchips (blank oder im SMD-Gehäuse), Platinen oder "completely packaged sensor solutions", magnetisierte Maßstäbe und …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Wird Sensorsystem-Montage/Packaging (Vergießen, Kleben) in Wetzlar oder Mainz durchgeführt, und bleibt die Fertigung unter Sinomags dort? Wo nachsehen: Sensitec_Sinomags_Folder_DE_web.pdf und Imagefolder im Browser lesen (Stufe V mit Zitat), Impressum sensitec.com, Stellenanzeigen Wetzlar/Mainz (Montage von Baugruppen und Sensoren), Datenblatt "packaged sensor solutions". Zusatz: Google …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 153. Silex Technology Europe GmbH (C2.505) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 47877 Willich, NRW | Quellen: `electronica/ergebnisse/tom_batch_51.md`, `tina_batch_51.md`
- Was wird gebaut: Drahtlos-LAN-Module, System-on-Modules (Qualcomm, NXP i.MX9), Access Points, Device Server, Print Server.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Hat die GmbH Entwicklung, Montage oder Fertigung in Willich? Impressum/Über-uns silextechnology.com/de, Stellenanzeigen Willich (Hardware/Produktion), Handelsregister Krefeld. Bei V "nur Vertrieb": Rot nach E2. Aktion: nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 154. SIMONA AG (B1.862) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 55606 Kirn, Rheinland-Pfalz | Quellen: `electronica/ergebnisse/tom_batch_51.md`, `tina_batch_51.md`
- Was wird gebaut: thermoplastische Kunststoff-Halbzeuge (Platten, Stäbe), Rohre, Formteile, Profile;
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Werden in Ringsheim oder Kirn Fertigteile für Elektronik/Halbleiter (Gehäuse, Tanks) mit Klebung, Dichtung oder Verguss gefertigt? simona.de Produktseite "Fertigteile", Datenblatt, Geschäftsbericht 2024 (hauptversammlung.de PDF) im Browser lesen. Sonst Verguss Niedrig bestätigen (Zeile 6). Aktion: Beobachtung, kein Kontakt.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 155. SK-tronic GmbH (A1.525/24) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 99441 Magdala, Thüringen | Quellen: `electronica/ergebnisse/tom_batch_52.md`, `tina_batch_52.md`
- Was wird gebaut: Leiterplattenbestückung (SMD und THT, Muster bis Serie) bis zu Gerätesystemen, Elektronikfertigung/EMS, ISO 9001 seit 2001.
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): Fertigung Magdala mit V belegen (Firmenseite, Stellenanzeigen) und Kundenbranchen/Verfahren (Vergießen, Schutzlack, Kleben) klären. Aktion: bei Beleg Grün erwartbar, mittlere Priorität.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 156. SOLARC Innovative Solarprodukte GmbH (A5.332) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 10999 Berlin | Quellen: `electronica/ergebnisse/tom_batch_52.md`, `tina_batch_52.md`
- Was wird gebaut: Entwicklung und Vertrieb von Photovoltaik-Kleingeräten (Solarmixer SoLait, Universalladegeräte scotty und e.GO!, Messgerät MacSolar), OEM-Solarstromversorgungen und …
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Ist SOLARC 2026 aktiv und fertigt in Berlin (Handelsregister/Unternehmensregister, solarc.de Impressum, aktuelle Messeprofile electronica/Intersolar, Stellenanzeigen)? Wie werden Module eingebettet und Elektronik vergossen? Aktion: nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 157. TechniSat Digital GmbH (A1.435) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 54550 Daun, Rheinland-Pfalz | Quellen: `electronica/ergebnisse/tom_batch_55.md`, `tina_batch_55.md`
- Was wird gebaut: Fernseher, Digitalradios (DAB+), Satelliten-/Kabel-Receiver, Wallboxen (TECHNIVOLT), Zubehör.
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): Wallbox TECHNIVOLT: In welchem Werk wird montiert (Daun)? technisat.de/de/impressum und Produktseite/Datenblatt TECHNIVOLT im Browser lesen (Zitat "hergestellt in" oder Stellenanzeige Montage/Fertigung Daun, Karriereseite). Bei V-Beleg Daun: Grün (Zeile 4). Außerdem: Patente Google Patents/Espacenet/DEPATISnet (TechniSat Digital, TechniSat Teledigital, TechniVolt). Aktion: nicht kontaktieren …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 158. TSI GmbH (B0.722) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 52068 Aachen, Nordrhein-Westfalen | Quellen: `electronica/ergebnisse/tom_batch_57.md`, `tina_batch_57.md`
- Was wird gebaut: Präzisionsmessgeräte für Luftströmung, Partikel und Umweltparameter (Konzernbeschreibung, S);
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Wird in Aachen montiert oder gefertigt (nicht nur Service)? Wo: tsi.com/company und Impressum der deutschen Seite im Browser, Stellenanzeigen Aachen (Produktion/Montage). Ohne Fertigungsbeleg: kein Ziel (Verguss Hoch gilt nur für die Konzernprodukte). Patentsuche (TSI Incorporated, TSI GmbH). Aktion: niedrige Priorität.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 159. W+P PRODUCTS GmbH (B2.404) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 32257 Bünde, Nordrhein-Westfalen | Quellen: `electronica/ergebnisse/tom_batch_61.md`, `tina_batch_61.md`
- Was wird gebaut: Leiterplatten-Steckverbinder (Stiftleisten, Buchsenleisten, D-Sub, IC-Fassungen, Modular Jacks, LED- und Power-Steckverbinder), über 20.000 Varianten.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Welche Produkte werden in Bünde montiert/gespritzt (wppro.com Standort-/Historienseite, Katalog "Made in Germany"-Angaben, Karriereseite Produktion Bünde im Browser lesen)? Gibt es vergossene/abgedichtete Varianten (IP-Datenblätter)? Aktion: bei V-Beleg Bünde und Verguss Mittel: Grün prüfen; nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 160. Werner Wirth GmbH (B2.504) – Prio B
- Gebiet/Ort: Rest DE / NL (Manuel) – 22525 Hamburg | Quellen: `electronica/ergebnisse/tom_batch_60.md`, `tina_batch_60.md`
- Was wird gebaut: exklusiver Zierick-Partner in DACH seit 2008 (US-Hersteller, Mt.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Fertigt/montiert Werner Wirth in Hamburg (Hellgrundweg 111) selbst oder nur Handel/Lager? Firmenseite, Impressum, Stellenanzeigen Hamburg lesen. (2) Selka Süßbrich Belgern: Impressum und Leistungsseite im Browser lesen = V für Fertigung in DE. (3) Welche Konfektionsprodukte sind überspritzt/vergossen/abgedichtet (Datenblatt)? (4) Patentsuche 1 und 2 sauber mit Anmelder "Werner Wirth GmbH" und …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 161. Display LC Deutschland GmbH (B6.404) – Prio C
- Gebiet/Ort: Baden-Württemberg (Stefan) – 68163 Mannheim | Quellen: `electronica/ergebnisse/tom_batch_14.md`, `tina_batch_14.md`
- Was wird gebaut: kundenspezifische Displaylösungen seit 1989, passive Displays bis TFT, AMOLED, PMOLED, e-Paper.
- Demak-Bereich: Verklebung
- Offener Auftrag (Tina): (a) Welche Gesellschaft stellt aus: Display LC AG (Mannheim, Schweizer Mutter?), Display LC Deutschland GmbH oder Display LC Europe AG? Wo nachsehen: Impressum displaylc.com, Handelsregister Mannheim, Ausstellerprofil electronica B6.404. (b) Fertigung/Optical Bonding vorhanden oder Handel? Bei Vertriebsgesellschaft ohne Fertigung: Rot E2. Aktion: nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 162. elbe electronic GmbH (A1.525/6) – Prio C
- Gebiet/Ort: Baden-Württemberg (Stefan) – 76275 Ettlingen; Schwesterstandort Gaggenau | Quellen: `electronica/ergebnisse/tom_batch_16.md`, `tina_batch_16.md`
- Was wird gebaut: Elektronik-Baugruppen und Produkte als EMS inkl.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Jey: Ist die CRM-Zeile "electronic concept GmbH" (bekannte_firmen, Z. 637) die Gaggenauer Gesellschaft, die jetzt zur elbe Gruppe gehört? Wo nachsehen: CRM-Datensatz (Ort), Handelsregister Mannheim/Stuttgart, Impressum elbe-Gruppe. (2) Fertigt elbe in Ettlingen selbst; bietet sie Verguss/Schutzlack? Impressum, Website, Stellenanzeige mit Firmennamen lesen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 163. EMCA elektromechanische Bauteile GmbH (A3.118) – Prio C
- Gebiet/Ort: Baden-Württemberg (Stefan) – 74193 Schwaigern laut Liste; Verzeichnis nennt Leingarten, beide … | Quellen: `electronica/ergebnisse/tom_batch_16.md`, `tina_batch_16.md`
- Was wird gebaut: Verzeichnis ordnet unter "elektronische Bauteile und Schaltungen" ein ;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Welcher Sitz stimmt (Schwaigern oder Leingarten) und was stellt EMCA her? Wo nachsehen: Handelsregister Stuttgart (Heilbronn-Bezirk), Impressum auf der Firmenwebsite (Domain über electronica-Ausstellerprofil), Produktkatalog; danach Fertigung und Verguss (Spulen/Relais/Magnete) prüfen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 164. ET System electronic GmbH (A5.230) – Prio C
- Gebiet/Ort: Baden-Württemberg (Stefan) – 68804 Altlußheim | Quellen: `electronica/ergebnisse/tom_batch_18.md`, `tina_batch_18.md`
- Was wird gebaut: programmierbare Laborstromversorgungen (DC-Serien LAB/S, LAB/SL, LAB/SLR, LAB/HPL 5 bis 10 kW bis 600 V/500 A), bidirektionale AC-Quellen (30 bis 500 kVA) und …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Jey: Ist CRM-Zeile 737 "ETS" (und 2036 "S.E. System Electronic") dieselbe Einheit wie ET System electronic GmbH, Altlußheim? Wo nachsehen: CRM-Datensatz (Ort, Ansprechpartner, Historie). (2) Gehört ET System zu einer Gruppe ("Sub-Division of a leading power supply manufacturer")? Impressum et-system.de, Handelsregister Mannheim, Katalogseite etesters.com lesen. (3) Werden Geräte in Altlußheim …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 165. Everlight Electronics Europe GmbH (C5.261) – Prio C
- Gebiet/Ort: Baden-Württemberg (Stefan) – 76187 Karlsruhe, Vertriebsbüro | Quellen: `electronica/ergebnisse/tom_batch_19.md`, `tina_batch_19.md`
- Was wird gebaut: Hochleistungs-LEDs, SMD-LEDs, Lampen, LED-Lichtmodule, Anzeigen, Optokoppler, Infrarotbauteile.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Hat die Everlight Electronics Europe GmbH eine eigene Fertigung/Montage in DE (nein = Rot E2/E3 mit Quelle)? Wo nachsehen: Impressum der Karlsruher GmbH (everlight-led.de bzw. everlight.com), Handelsregister Mannheim, Werksliste en.everlight.com/about. Aktion: nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 166. hera Laborsysteme GmbH (A4.425) – Prio C
- Gebiet/Ort: Baden-Württemberg (Stefan) – 74572 Blaufelden | Quellen: `electronica/ergebnisse/tom_batch_25.md`, `tina_batch_25.md`
- Was wird gebaut: Elektro-Labortische, Elektro-Ausbildungstische und Elektro-Montagetische (Bench-Rack-System LS2000, Ausbildungssysteme für Elektroberufe seit 2006, Netzwerkgeräte-Serie …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Ist die CRM-Zeile "Hera GmbH & Co. KG" (Zeile 1032) dieselbe Einheit wie hera Laborsysteme (Blaufelden)? Wo nachsehen: CRM-Datensatz (Adresse/Ort), Handelsregister (Ulm HRB 690397 gegen Enger), Impressum hera.de. Danach: Werden in Blaufelden eigene Elektronikmodule/Netzteile gefertigt oder vergossen (Datenblatt IMOD, Karriereseite)?
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 167. Karl Enghofer GmbH & Co. KG (B2.411) – Prio C
- Gebiet/Ort: Baden-Württemberg (Stefan) – 75217 Birkenfeld, Enzkreis | Quellen: `electronica/ergebnisse/tom_batch_29.md`, `tina_batch_29.md`
- Was wird gebaut: Branchenbucheintrag "Metallwarenfabrik".
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Welche Firma ist die Karl Enghofer GmbH & Co. KG (Website, Impressum, Handelsregister Mannheim/Pforzheim), was fertigt sie (Stanz-/Kontaktteile, Baugruppen, Umspritzung)? Wo nachsehen: Messeprofil B2.411, Handelsregister, Gelbe-Seiten-Eintrag mit Website-Link, Stellenanzeigen. Anschließend Fertigungs- und Vergussfrage nach Zeile 4/5/6.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 168. LAB14 GmbH (B1.234) – Prio C
- Gebiet/Ort: Baden-Württemberg (Stefan) – 69124 Heidelberg | Quellen: `electronica/ergebnisse/tom_batch_32.md`, `tina_batch_32.md`
- Was wird gebaut: Die Gruppe wird als "high-tech companies specializing in nanofabrication, microfabrication and surface analysis" beschrieben.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Welche Gesellschaft stellt aus und wo sitzt sie (Heidelberg oder Essen)? Wo nachsehen: Impressum lab14.com, Handelsregister, electronica-Ausstellerprofil B1.234 (stellt eine Tochter aus, z. B. Notion Systems?). Danach: Fertigung und Verguss der ausstellenden Tochter einzeln bewerten (Sitzregel). Aktion: zurückstellen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 169. Peter HUBER Kältemaschinenbau SE (C2.229) – Prio C
- Gebiet/Ort: Baden-Württemberg (Stefan) – 77656 Offenburg | Quellen: `electronica/ergebnisse/tom_batch_26.md`, `tina_batch_26.md`
- Was wird gebaut: Umwälzthermostate, Kältemaschinen/Chiller und dynamische Temperiersysteme.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): An Jey: Ist die CRM-Zeile "J. Schneider Elektrotechnik" (Z. 1208, Offenburg?) die Offenburger Schwester der Huber SE? Wenn ja: Konzernbezug zu einem Bestandskunden, Vorgehen mit Jey/Vertrieb abstimmen (kein Neukunde im Sinne E5 für die Huber SE selbst, da andere Einheit, aber Konzernpflege). Wo nachsehen: CRM-Datensatz (Ort, Ansprechpartner, Verifiziert-Datum), Handelsregister Freiburg …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 170. Schulz-Electronic GmbH (A5.214) – Prio C
- Gebiet/Ort: Baden-Württemberg (Stefan) – 76534 Baden-Baden/Steinbach | Quellen: `electronica/ergebnisse/tom_batch_49.md`, `tina_batch_49.md`
- Was wird gebaut: Anbieter professioneller Stromversorgungen: AC/DC, DC/DC, elektronische Lasten, Bordnetz-Simulation, Laserdiodentreiber, Hochspannung, Wechselrichter.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Baut Schulz-Electronic Geräte selbst (Montage/Anpassung/Verguss programmierbarer Netzteile, Prüfeinrichtungen) oder nur Vertrieb/Service? Wo nachsehen: schulz-electronic.de (Über uns, Leistungen, Eigenentwicklungen), Impressum, Stellenanzeigen (Montage/Fertigung Baden-Baden). Bei reinem Vertrieb Rot nach E2 mit Quelle. Aktion: zurückstellen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 171. Shantou Goworld Display Germany GmbH (B6.421) – Prio C
- Gebiet/Ort: Baden-Württemberg (Stefan) – 73265 Dettingen unter Teck | Quellen: `electronica/ergebnisse/tom_batch_50.md`, `tina_batch_50.md`
- Was wird gebaut: kundenspezifische LCD-, TFT- und Touch-Module für Industrie, Automotive, Haushalt, "developing, selling and delivering" ;
- Demak-Bereich: Verklebung
- Offener Auftrag (Tina): Hat die GmbH in Dettingen eigene Montage/Optical-Bonding-Fertigung oder nur Vertrieb/Entwicklung/Lager? Wo nachsehen: Impressum und "Über uns" goworld-lcd.de (Zitat für Vertriebsrolle = V für E2/E3), Handelsregister (Gegenstand des Unternehmens), Stellenanzeigen Dettingen. Bei V-Beleg Rot nach E2/E3 mit URL. Aktion: nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 172. TRS-STAR GmbH (C4.400) – Prio C
- Gebiet/Ort: Baden-Württemberg (Stefan) – 76297 Stutensee | Quellen: `electronica/ergebnisse/tom_batch_57.md`, `tina_batch_57.md`
- Was wird gebaut: überwiegend Distribution von Halbleitern (Schwerpunkte FPGAs und Leistungsbauteile), dazu Displays und Industrie-PCs, die nach Kundenvorgabe in Stutensee montiert und …
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): (a) Identität: Impressum und Handelsregister der TRS-STAR GmbH (Stutensee, Amtsgericht Mannheim bzw. Karlsruhe prüfen), Firmenwebsite (Domain nicht ermittelt). Zugehörigkeit zu MSC Group/Avnet-Umfeld? (b) Wer betreibt die Leuchtenlinie in Frankenthal (gleiche Gesellschaft?), werden Leuchten selbst gefertigt und vergossen (IP-Klasse in Datenblättern t.exterieur)? (c) Werden Displays optisch …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 173. Advantech Europe B.V. (C5.302) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 82110 Germering, laut Messeliste | Quellen: `electronica/ergebnisse/tom_batch_01.md`, `tina_batch_01.md`
- Was wird gebaut: Industrie-PCs, ruggedized Fahrzeugterminals (DLT-V-Serie, IP65, vibrations- und stoßfest, Heizung, Weitbereichs-Netzteil), Tablets.
- Demak-Bereich: Verguss + Verklebung
- Offener Auftrag (Tina): Welche Gesellschaft stellt aus (B.V. Eindhoven oder Service-IoT GmbH Germering), und fertigt die Service-IoT GmbH in Germering heute Fahrzeugterminals (aktuelle Quelle 2025/26)? Wo nachsehen: Impressum advantech.com/de-de bzw. Service-IoT-Seite, Handelsregister München (Service-IoT GmbH), Stellenanzeigen Germering (Montage, Test), Produktseite "Made in Germany". Dann Fertigungsbeleg V und Einheit …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 174. ai-energy GmbH (A6.620) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 91126 Rednitzhembach | Quellen: `electronica/ergebnisse/tom_batch_02.md`, `tina_batch_02.md`
- Was wird gebaut: Elektrifizierung des Antriebsstrangs, Leistungselektronik, Produktgruppen elektrischer Antriebsstrang, passive und aktive Komponenten.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Jey: Ist die CRM-Zeile "alfatec GmbH & Co. KG" (Zeile 72) bzw. "alfatec" (Zeile 71) dieselbe Gruppe/Anschrift wie ai-energy (Meckenloher Str. 11)? Und welche Rolle hat Hitachi/Eigene Harze (Bestandskontakt)? Wo: CRM-Datensatz (Adresse, Verifiziert am), Handelsregister Nürnberg HRB 36744 (Gesellschafter), Impressum der ai-energy-Website. (2) Wo und von wem werden die ai-energy-Produkte gefertigt …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 175. Aprotech GmbH (C2.352) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 97753 Karlstadt-Karlburg | Quellen: `electronica/ergebnisse/tom_batch_04.md`, `tina_batch_04.md`
- Was wird gebaut: Anlagen zur Kristallzucht für Halbleitermaterialien, Wafer-Prüf- und Messsysteme, Wafer-Handling und Automation;
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Ist die Ausstellerin "Aprotech GmbH" die aprotec GmbH (Karlstadt)? Wo nachsehen: electronica-Ausstellerprofil (Website/Adresse), Impressum aprotec-gmbh.de, Handelsregister Würzburg. Danach Fertigung Karlstadt (Impressum, Stellenanzeigen Montage) und verbaute Komponenten prüfen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 176. ATEcare Service GmbH & Co.KG (A4.346) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 85232 Bergkirchen laut Messeliste; Aichach laut anderen Quellen | Quellen: `electronica/ergebnisse/tom_batch_05.md`, `tina_batch_05.md`
- Was wird gebaut: Automatische Testsysteme (ATE), optische und Röntgen-Inspektionssysteme, Service/Kalibrierung/Schulung/Software-Updates;
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Welcher Sitz ist maßgeblich (Bergkirchen oder Aichach, Rechtsform GmbH & Co. KG) und gibt es Eigenprodukte/Fertigung? Wo nachsehen: Impressum der Firmenseite (Domain nicht ermittelt; über Ausstellerprofil electronica suchen), Handelsregister Augsburg/München (Unternehmensgegenstand), Stellenanzeigen. Bei reinem Vertrieb/Service: Rot nach E2 mit Quelle.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 177. AUMOVIO SE (B4.A04) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 60488 Regensburg | Quellen: `electronica/ergebnisse/tom_batch_06.md`, `tina_batch_06.md`
- Was wird gebaut: Sensorlösungen, Displays, Brems- und Komfortsysteme, Software.
- Demak-Bereich: Verguss + Verklebung + Dichtung
- Offener Auftrag (Tina): Jey: Ist AUMOVIO Germany GmbH Rechtsnachfolgerin/umfirmierte Einheit der CRM-Zeile "Continental Automotive Technologies GmbH" bzw. steht "Continental" (Zeile 442) für dieselbe Gruppe? Wo nachsehen: Handelsregister/Unternehmensregister (Amtsgericht), CRM-Datensatz, Impressum aumovio.com. (2) Welche Produkte werden in Regensburg/Babenhausen gefertigt und vergossen? Stellenanzeigen, Standortseite …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 178. BDT Bavaria Digital Technik GmbH (A1.602) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 87459 Pfronten | Quellen: `electronica/ergebnisse/tom_batch_07.md`, `tina_batch_07.md`
- Was wird gebaut: EMS;
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Jey: Gehört BDT Pfronten heute noch zur AdCapital AG, und ist der CRM-Bestandskontakt (Erich Jaeger, EW HOF, FRAKO oder TALLER) für Pfronten ohne Bedeutung (eigene Gesellschaft, anderer Ansprechpartner)? Wo nachsehen: CRM-Datensätze, AdCapital-Geschäftsbericht 2024/2025 (Beteiligungsliste, adcapital.de Investor Relations), Handelsregister Kempten, Impressum bdt-online.de. (2) Wird in Pfronten …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 179. GES High Voltage GmbH (B3.320) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 85399 Hallbergmoos | Quellen: `electronica/ergebnisse/tom_batch_23.md`, `tina_batch_23.md`
- Was wird gebaut: Hochspannungs-Steckverbinder (Einzelpin, Mehrpin, modular), z.
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): (a) Welche Gesellschaft stellt aus: GES High Voltage GmbH (Register, Sitz) oder GES Electronic & Service GmbH (HRB 70513)? Wo nachsehen: Impressum ges-electronic.de bzw. GES-High-Voltage-Domain, Handelsregister München, Messeprofil electronica. (b) Danach Fertigung am Sitz (Impressum, Stellenanzeigen Montage/Test) und Gießharz im Kabelanschluss (Datenblatt Series 100). Aktion: erst Identität …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 180. JDI Europe GmbH (B6.441) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 80339 München | Quellen: `electronica/ergebnisse/tom_batch_28.md`, `tina_batch_28.md`
- Was wird gebaut: Die Mutter ist Displayhersteller (LCD/Touch/Automotive), die GmbH vermutlich Vertrieb/Europa-Büro (A/?).
- Demak-Bereich: Verklebung
- Offener Auftrag (Tina): Ist JDI Europe GmbH ausschließlich Vertrieb (E2 mit V)? Wo nachsehen: EDINET-Wertpapierbericht (Segment/Beschreibung "Sales of display"), Handelsregister München, Impressum j-display.com (Europe). Bei Bestätigung Rot nach E2 mit Quelle. Aktion: keine.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 181. Keenfinity GmbH (A1.126) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 81737 München; EMS-Werk Straubing | Quellen: `electronica/ergebnisse/tom_batch_29.md`, `tina_batch_29.md`
- Was wird gebaut: 2025 aus Bosch ausgegliederte Sicherheits- und Kommunikationsgruppe (Triton), Geschäfte Intrusion & Access, Video, Audio, EMS.
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Jey: Steht im CRM die Bosch-Einheit "Bosch Security Systems/Building Technologies" (Grasbrunn/Straubing) oder nur andere Bosch-Gesellschaften (Robert Bosch GmbH, Rexroth, Power Tools)? Wo nachsehen: CRM-Datensätze der Zeilen 313 bis 318 und 1993 bis 2002 (Ort, Ansprechpartner). Ist Keenfinity damit Neukunde (nach Ausgliederung eigene Einheit) oder Bestandskontakt? (2) Was fertigt Straubing …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 182. Kurtz Ersa Smart Production GmbH (A4.461) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 99880 Vaterstetten bei München | Quellen: `electronica/ergebnisse/tom_batch_32.md`, `tina_batch_32.md`
- Was wird gebaut: Vakuumlötsysteme für Halbleiter und Mikroelektronik, Serienanlage SRO i-LINE mit Infrarotheizung.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Werden die Vakuumlötanlagen in Vaterstetten gebaut (Fertigungsbeleg) und enthalten sie vergossene/geklebte/gedichtete Baugruppen (Heizmodule, Steuerung)? Wo nachsehen: Impressum Kurtz Ersa Semicon, Produktseite SRO i-LINE (Datenblatt), Handelsregister München (ATV Technologie), Stellenanzeigen Montage. Aktion: zurückstellen (Anlagenbau, Verguss Niedrig).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 183. LEDtronix - a division of LEDoptix GmbH (A1.525/23) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 83620 Feldkirchen-Westerham | Quellen: `electronica/ergebnisse/tom_batch_32.md`, `tina_batch_32.md`
- Was wird gebaut: "LEDtronix" als Name ist nicht auffindbar.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Was ist "LEDtronix", gehört es zur LEDoptix GmbH, und wo sitzt die Gesellschaft? Fertigt sie LED-Module/Leuchten selbst? Wo nachsehen: Impressum ledoptix.de, Handelsregister München, electronica-Ausstellerprofil A1.525/23, Produkt- und Stellenseiten. Bei reinem Vertrieb/Installation: Rot nach E2 mit Quelle.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 184. MAIR Elektronik GmbH (A1.431) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 85445 Schwaig bei München; Verzeichnis nennt auch Oberding, 85445 | Quellen: `electronica/ergebnisse/tom_batch_34.md`, `tina_batch_34.md`
- Was wird gebaut: EMS: "development, procurement, THT, SMT in the clean room, analytics by AOI, X-Ray, grinding laboratory, rework, logistics";
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): (a) Jey: Ist MAIR Elektronik GmbH im CRM als Teil von RAWE Electronic GmbH (Zeile 1948) oder Demmel AG (Zeile 501) bereits betreut? Wo nachsehen: CRM-Datensätze (Ort Weiler, Kontakte), Handelsregister Schwaig/München (Gesellschafter). (b) Wird in Schwaig vergossen oder lackiert? Wo nachsehen: Leistungsseite und Impressum der MAIR-Website (Domain unbestätigt, Kandidat mair-elektronik.de) …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 185. Puerstinger High Purity Systems GmbH (B1.761) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 84489 Burghausen | Quellen: `electronica/ergebnisse/tom_batch_44.md`, `tina_batch_44.md`
- Was wird gebaut: nicht belegt.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Existiert die Gesellschaft in Burghausen mit welcher Tätigkeit (Anlagenbau vs. Rohrleitungsbau), und gibt es Eigenfertigung (Gasschränke, Steuerungen)? Wo nachsehen: Handelsregister Traunstein/Unternehmensregister, electronica-Ausstellerprofil B1.761, Website über Impressum. Bei Dienstleister ohne Eigenprodukte: Rot nach E2 mit Quelle. Aktion: nicht weiter verfolgen.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 186. Schlemmer (B2.124) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 85551 Raum München | Quellen: `electronica/ergebnisse/tom_batch_48.md`, `tina_batch_48.md`
- Was wird gebaut: Kabelmanagement- und Kabelschutzsysteme für Automotive: Kabelverschraubungen, Wellrohre, Schutzschläuche, mechatronische Steckverbindungen, Luft- und Flüssigkeitssysteme …
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): (a) Welche juristische Einheit stellt aus (Schlemmer GmbH Aschheim, Schlemmer-Gruppe, Delfingen-Gesellschaft) und gibt es einen Standort in Kirchheim/Heimstetten? Impressum schlemmer.com, Messeprofil, Handelsregister München. (b) Wird in Aschheim produziert oder nur Technical Center/Verwaltung; welche Produkte (Mechatronic Solutions, Steckverbinder) in welchem deutschen Werk? (c) Stand der …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 187. SCREEN SPE Germany GmbH (B1.700) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 85737 Ismaning | Quellen: `electronica/ergebnisse/tom_batch_49.md`, `tina_batch_49.md`
- Was wird gebaut: nichts in DE/AT/NL belegt;
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): E2/E3 mit Stufe V belegen: Firmenseite screen-spe.com/eu/company und Impressum lesen (Vertrieb/Service, keine Fertigung in DE), Handelsregister München. Aktion: nicht bearbeiten.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 188. SUYIN GmbH (B2.101) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 84347 Pfarrkirchen | Quellen: `electronica/ergebnisse/tom_batch_54.md`, `tina_batch_54.md`
- Was wird gebaut: Steckverbinder für E-Mobility, Industrie und Medizintechnik: Batterie-Steckverbinder (Feder- und Messerkontakt) ab Lager und kundenspezifische Entwicklung.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Gibt es in Pfarrkirchen Montage, Konfektion oder Musterfertigung (Löten, Kleben, Vergießen)? Impressum und Karriereseite suyin.com, Stellenanzeigen im Browser; bei reiner Zentrale ohne Fertigung Rot nach E3 mit URL. Aktion: niedrige Priorität, nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 189. ULVAC GmbH (B1.606) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 85551 Kirchheim b. München | Quellen: `electronica/ergebnisse/tom_batch_58.md`, `tina_batch_58.md`
- Was wird gebaut: Vakuumpumpen, Vakuum- und Beschichtungsanlagen der Gruppe, in Kirchheim Vertrieb/Service.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): ulvac.de Impressum und "Über uns" im Browser lesen: Vertriebs-/Servicegesellschaft ohne Fertigung (V) -> Rot nach E2; sonst Montage/Fertigung in Kirchheim klären. Patente nachholen (Anmelder ULVAC GmbH, ULVAC Inc.). Aktion: nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 190. Veeco GmbH (B1.341) – Prio C
- Gebiet/Ort: Bayern (Dietmar) – 85609 Aschheim | Quellen: `electronica/ergebnisse/tom_batch_59.md`, `tina_batch_59.md`
- Was wird gebaut: Dünnschicht-Prozessanlagen für Halbleiter, LED, Leistungselektronik, MEMS.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Handelsregister (Amtsgericht München) und Impressum der Veeco-Seite: korrekter Firmenname, Adresse Aschheim, Tätigkeit (Vertrieb/Service oder Montage)? Stellenanzeigen Aschheim im Browser. Bei Vertrieb/Service V: Rot nach E2/E3. Aktion: nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 191. AES motomation GmbH (B1.672) – Prio C
- Gebiet/Ort: Rest DE / NL (Manuel) – 41564 Kaarst bzw. Meerbusch, NRW | Quellen: `electronica/ergebnisse/tom_batch_02.md`, `tina_batch_02.md`
- Was wird gebaut: Handling-Equipment für Wafer/Panel: Load Ports, Roboter, Pre-Aligner, EFEM/iFEM-Komplettsysteme, Auto-Teaching.
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): (a) Welche Adresse ist der Sitz der GmbH (Kaarst oder Meerbusch; Handelsregister Neuss/Düsseldorf, Impressum motomation.com)? (b) Montiert die GmbH Load Ports/EFEM selbst oder liefert sie nur Fremdprodukte (Händler/Integrator → Rot nach E2 mit Quelle)? Wo: motomation.com Impressum und Produktseiten, Stellenanzeigen "Montage/Fertigung". Aktion: nicht priorisieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 192. AMETEK Programmable Power (A4.478) – Prio C
- Gebiet/Ort: Rest DE / NL (Manuel) – 40670 Meerbusch laut Liste | Quellen: `electronica/ergebnisse/tom_batch_04.md`, `tina_batch_04.md`
- Was wird gebaut: programmierbare DC-Netzteile 30 W bis 150 kW und AC-Quellen 800 VA bis 480 kVA, Marken Sorensen, Elgar, California Instruments.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Welche Einheit stellt aus (AMETEK Germany GmbH, Meerbusch, oder die US-Division) und gibt es Fertigung/Montage von Netzteilen in DE/AT/NL (z. B. Powervar-Standort)? Wo nachsehen: Impressum ametek.de / Messeprofil im electronica-Portal; Standortliste ametek.com; Handelsregister Neuss. Aktion: keine Ansprache.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 193. Brandenburgische Kondensatoren Technologie GmbH (nicht angegeben) – Prio C
- Gebiet/Ort: Rest DE / NL (Manuel) – 17291 Prenzlau, Brandenburg | Quellen: `electronica/ergebnisse/tom_batch_08.md`, `tina_batch_08.md`
- Was wird gebaut: Entstörkondensatoren und Filter ("EMI anti-interference capacitors and filters", Händlerseite, S);
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): (a) Existiert die "Brandenburgische Kondensatoren Technologie GmbH" als eigene Gesellschaft, oder ist die ausstellende Firma die "Brandenburgische Kondensatoren GmbH"? Wo nachsehen: Impressum bkprenzlau.de (Domain nur aus Datenblatt, S), Handelsregister (Registergericht Neuruppin/Prenzlau), Ausstellerprofil auf electronica.de (Halle/Stand fehlt). (b) Wird aktuell in Prenzlau gefertigt und wie …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 194. DETAKTA Isolier- und Messtechnik GmbH & Co. KG (B3.357) – Prio C
- Gebiet/Ort: Rest DE / NL (Manuel) – 22851 Norderstedt, Schleswig-Holstein | Quellen: `electronica/ergebnisse/tom_batch_13.md`, `tina_batch_13.md`
- Was wird gebaut: Verzeichnis beschreibt DETAKTA als Spezialisten für den Handel mit innovativen Isolierstoffen für industrielle Anwendungen.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Existiert die Firma mit Sitz Norderstedt, und ist sie Händler (E2) oder Hersteller von Isolierstoffen/Messtechnik? Wo nachsehen: Handelsregister (Amtsgericht Kiel bzw. Norderstedt), Impressum auf der echten Firmenwebsite (Domain über electronica-Ausstellerprofil ermitteln), Produktkatalog. Bei Händler bestätigt: Rot nach E2 mit Quelle. Aktion: nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 195. Faeth GmbH / Fäth GmbH (B1.265) – Prio C
- Gebiet/Ort: Rest DE / NL (Manuel) – Klipphausen, Sachsen | Quellen: `electronica/ergebnisse/tom_batch_19.md`, `tina_batch_19.md`
- Was wird gebaut: Gasversorgungs- und Chemieversorgungssysteme, Wassertechnik, Tanks mit Tankauskleidung, Elektro-, Mess- und Regelungstechnik, OEM-Lohnfertigung, HighQ-Recyclinganlagen.
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): Jey: Ist die Bürkert GmbH & Co. KG im CRM (Zeile 366) Bestandskontakt der Bürkert-Gruppe, und gilt die Fäth GmbH als Schwester/Beteiligung (Rot E5 nur bei derselben Einheit; sonst Neukontakt nach Jeys Entscheidung)? Wo nachsehen: CRM-Datensatz Bürkert (Ort Ingelfingen?), Bürkert-Pressemitteilung "Bürkert and Fäth join forces", Handelsregister Dresden (Fäth GmbH) und Aschaffenburg (FäthGroup …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 196. FEIN Elektronik GmbH (A1.637) – Prio C
- Gebiet/Ort: Rest DE / NL (Manuel) – 61381 Friedrichsdorf, Hessen | Quellen: `electronica/ergebnisse/tom_batch_19.md`, `tina_batch_19.md`
- Was wird gebaut: Profile: "specialized distributor of electronic components" (EtherCAT-Profil, S) mit Analog-ICs, Leistungshalbleitern, Quarzen, Optoelektronik, Mikrocontrollern …
- Demak-Bereich: Verklebung + Verguss
- Offener Auftrag (Tina): Wird in Friedrichsdorf Elektronik bestückt oder werden Displays angepasst/verklebt, oder nur beschafft/extern gefertigt (dann Rot E2 mit V-Quelle)? Wo nachsehen: Impressum und Standortseite fein-elektronik.de, Stellenanzeigen (Bestückung/Montage), Ausstellerprofil electronica. Zusätzlich: Namen der vier Gruppeneinheiten für Konzernabgleich.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 197. KITEC microelectronic technologie GmbH (B1.358) – Prio C
- Gebiet/Ort: Rest DE / NL (Manuel) – 23569 Lübeck laut Messeliste | Quellen: `electronica/ergebnisse/tom_batch_30.md`, `tina_batch_30.md`
- Was wird gebaut: Laut SEMI-Profil Lieferung von "Wafer-Handling, Messtechnik und Verbrauchsmaterial": Batch-Wafer-Transfersysteme, Wafer-Loader, FOUP-Stocker, berührungslose …
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): (a) Sitz der ausstellenden Gesellschaft (Erding oder Lübeck; ggf. Zweigniederlassung)? Wo nachsehen: Impressum kitec.de, Handelsregister Erding/Landshut bzw. Lübeck, Mesago-/electronica-Ausstellerprofil. (b) Hersteller oder Vertretung? Bei Vertretung Rot nach E2 mit Quelle. Aktion: Jey bestätigt Firma, bevor weiterrecherchiert wird.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 198. Lutronic GmbH (B2.207) – Prio C
- Gebiet/Ort: Rest DE / NL (Manuel) – 58579 Schalksmühle | Quellen: `electronica/ergebnisse/tom_batch_34.md`, `tina_batch_34.md`
- Was wird gebaut: Schwestergesellschaft der Lumberg Group;
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): (a) Gehört die Lutronic GmbH rechtlich zur Gruppe Lumberg Holding (CRM Zeile 1483), oder ist sie eine Schwester unter gleichem Eigentümer; welche Anschrift gilt (Im Gewerbepark 2 oder Hälverstr. 94)? Wo nachsehen: Impressum lutronic.biz, Handelsregister Iserlohn, CRM-Adresse. (b) Wird in Schalksmühle irgendetwas gefertigt oder konfektioniert, oder ausschließlich vertrieben (Rot E3 bei V-Beleg)? …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 199. Minimax Fire Solutions International GmbH (C2.112) – Prio C
- Gebiet/Ort: Rest DE / NL (Manuel) – 23840 Bad Oldesloe, Schleswig-Holstein | Quellen: `electronica/ergebnisse/tom_batch_37.md`, `tina_batch_37.md`
- Was wird gebaut: Brandschutz: Brandmelder und Brandmeldezentralen, Löschsysteme (Gruppe, S).
- Demak-Bereich: Verguss + Dichtung
- Offener Auftrag (Tina): (a) Welche Gesellschaft stellt aus und fertigt: Minimax Fire Solutions International GmbH (Reinfeld?) oder Minimax GmbH & Co. KG (Bad Oldesloe)? Impressum minimax.com/de, Handelsregister Lübeck/Bad Oldesloe lesen. (b) Wird Melder-/Zentralenelektronik in Bad Oldesloe gebaut und dort vergossen/lackiert (aktuelle Stellenanzeige im Original, Standortseite)? Aktion: Beobachtung.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 200. MS Power GmbH (C2.673) – Prio C
- Gebiet/Ort: Rest DE / NL (Manuel) – 65760 Eschborn, Hessen | Quellen: `electronica/ergebnisse/tom_batch_37.md`, `tina_batch_37.md`
- Was wird gebaut: Selbstbeschreibung im Messeprofil : Leistungshalbleiter und Systeme: bipolare Halbleiter-Chips, Stud-/Schraub-Dioden und -Thyristoren, Kapselbauelemente, Module, auf …
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Wird in Eschborn oder anderswo in DE/AT/NL gefertigt (Montage Power-Stacks/Module) oder ausschließlich in China (dann Rot nach E3 mit Quelle)? Wo nachsehen: mspowergroup.com (Standorte, Impressum), Richardson-Pressemeldung im Original, Handelsregister Frankfurt/Königstein (Gesellschafter), Stellenanzeigen Eschborn (Montage/Prüffeld).
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 201. ROKA - Robert Karst GmbH & Co.KG Elektrotechnische Fabrik (B2.331) – Prio C
- Gebiet/Ort: Rest DE / NL (Manuel) – 12277 Berlin | Quellen: `electronica/ergebnisse/tom_batch_46.md`, `tina_batch_46.md`
- Was wird gebaut: Verzeichnis : Kabelbefestigungsmaterial, Kabelschellen, Lautsprecherkabel, NF- und HF-Steckvorrichtungen, Koaxial-Steckverbinder, Antennenbuchsen und -stecker.
- Demak-Bereich: Verguss + Verklebung + Dichtung
- Offener Auftrag (Tina): (a) Welcher Standort ist der Sitz/Fertigungsort (Marienfelde 12277 oder Kreuzberg 10961)? Impressum roka-berlin.de, Handelsregister Berlin-Charlottenburg, electronica-Ausstellerprofil. (b) Wird in Berlin gefertigt oder zugekauft; werden Kabel/Stecker vergossen oder überspritzt? Produktseite, Datenblätter, Stellenanzeigen Berlin.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 202. Samwha Europe GmbH (A6.527) – Prio C
- Gebiet/Ort: Rest DE / NL (Manuel) – 60528 Frankfurt am Main, laut Liste | Quellen: `electronica/ergebnisse/tom_batch_48.md`, `tina_batch_48.md`
- Was wird gebaut: Die Suche fand keine Seite der Samwha Europe GmbH.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Gibt es eine Samwha Europe GmbH in 60528 Frankfurt, und fertigt oder konfektioniert sie selbst? Impressum auf samwha.com / Europa-Seite, Handelsregister Frankfurt (Unternehmensregister) lesen. Ergebnis Vertrieb ohne Fertigung (Stufe V) = Rot nach E2.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 203. scia Systems GmbH (B1.909) – Prio C
- Gebiet/Ort: Rest DE / NL (Manuel) – 09116 Chemnitz, Sachsen | Quellen: `electronica/ergebnisse/tom_batch_49.md`, `tina_batch_49.md`
- Was wird gebaut: Ionenstrahl- und Plasma-Prozessanlagen (Ätzen, Trimmen, Beschichten;
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Jey: Ist die CRM-Einheit "VON ARDENNE GmbH" (Dresden) Gesellschafterin/Muttergesellschaft der scia Systems GmbH, und gilt der Bestandskontakt auch für scia? Wo nachsehen: CRM-Datensatz (Adresse, Ansprechpartner), Gesellschafterliste/Handelsregister Chemnitz HRB 27983 (Unternehmensregister), Impressum scia-systems.com. Hinweis: Auch bei Rot-Klärung (E5) wäre nur Konzernbezug mit Einheitenfrage …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 204. SEI Interconnect Products (Europe) Ltd. (B3.519) – Prio C
- Gebiet/Ort: Rest DE / NL (Manuel) – 22844 Norderstedt, Schleswig-Holstein | Quellen: `electronica/ergebnisse/tom_batch_50.md`, `tina_batch_50.md`
- Was wird gebaut: Wire and Cable für Automotive, Kabelkonfektion für Medizin, Flexible Flat Cable für Consumer/Automotive.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Jey: Welche Gesellschaft steht hinter CRM-Zeilen "Sumitomo"/"SUMITOMO" (2273/2274)? Gehört sie zur Sumitomo-Electric-Gruppe? Wo nachsehen: CRM-Datensätze (Ort/Ansprechpartner), Sumitomo-Gruppenübersicht. (2) Hat Norderstedt eigene Konfektion/Fertigung? Impressum, Stellenanzeigen, Sumitomo-Seite lesen; sonst Rot nach E2/E3 mit Quelle. Aktion: nicht kontaktieren, bis (1) geklärt ist.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 205. SIIX Europe GmbH (A1.619) – Prio C
- Gebiet/Ort: Rest DE / NL (Manuel) – 47877 Willich, NRW | Quellen: `electronica/ergebnisse/tom_batch_51.md`, `tina_batch_51.md`
- Was wird gebaut: EMS-Dienstleister (Konzern SIIX Corporation, Japan);
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): Existiert eine SIIX-Gesellschaft in DE (Aussteller-Detailseite A1.619, Handelsregister, siix.com Standortliste) und wo sitzt sie? (2) Hat sie Fertigung/Montage in DE/AT/NL (sonst Rot nach E3/E2 mit V)? Aktion: Identität vor Weiterarbeit klären.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 206. Song Chuan Precision Europe GmbH (A3.141) – Prio C
- Gebiet/Ort: Rest DE / NL (Manuel) – 65558 Isselbach-Ruppenrod, Rheinland-Pfalz, laut Messeliste | Quellen: `electronica/ergebnisse/tom_batch_52.md`, `tina_batch_52.md`
- Was wird gebaut: Gruppe entwickelt und fertigt elektromechanische Relais (Automotive, General Purpose, Industrial, Zubehör), Hochstrom-/Hochvolt-Relais für Solar und E-Mobility.
- Demak-Bereich: Verguss
- Offener Auftrag (Tina): (a) Ist "Song Chuan Precision Europe GmbH" = "Song Chuan Europe GmbH"? Impressum, Handelsregister (Amtsgericht Montabaur/Limburg), Messeprofil. (b) Montage/Fertigung in Isselbach? Stellenanzeigen. Bei V-Beleg Vertrieb ohne Fertigung: Rot nach E2/E3 mit URL. Aktion: nicht kontaktieren.
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

### 207. PTW Asia Pte Ltd (B1.120) – Prio C
- Gebiet/Ort: außerhalb – Singapur | Quellen: `electronica/ergebnisse/tom_batch_44.md`, `tina_batch_44.md`
- Was wird gebaut: Aufarbeitung (Refurbishing) von Halbleiter-Anlagen, Ersatzteile, Vor-Ort-Service und Improvement-Kits für Anlagen von LAM (früher SEZ), AMAT (früher Semitool), Screen …
- Demak-Bereich: kein klarer Bereich
- Offener Auftrag (Tina): Wer stellt in B1.120 aus (PTW Asia Singapur oder PTW SpinTec Villach)? Gehört PTW Asia zu PTW SpinTec? Wo nachsehen: electronica-Ausstellerseite B1.120, SEMI-Eintrag PTW SpinTec GmbH, ACRA/Handelsregister Villach. Wenn PTW SpinTec die fertigende Einheit ist, getrennt als eigene Firma prüfen (Nassprozessanlagen: Heizungen, Sensorik, Steuerung, Verguss Mittel A möglich). Aktion: nicht priorisieren …
- Zu prüfen: [ ] Impressum/Sitz  [ ] Fertigung am Sitz  [ ] Verguss/Klebung/Dichtung  [ ] Patente  [ ] Wettbewerbereinsatz  [ ] Konzern/Werke  [ ] CRM wiederholt  [ ] E1 (eigene Verguss-/Dosieranlagen?)

