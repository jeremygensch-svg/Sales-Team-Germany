# Tom Batch 46 – electronica 2026 (Export Stand 03.07.2026)
Erstellt: 2026-10-20 (Tom, Stufe 1, Version 2, Messemodus Regel N). Eingabe: electronica/batches_v2/pruef_46.md, 10 Firmen (Nr. 514, 515, 516, 517, 518, 519, 520, 522, 523, 526), keine doppelt gelisteten Firmen. Die Ersteinschätzung der Eingabe wurde nicht übernommen.
Alle Abrufdaten: 2026-10-20. Belegstufen: V = selbst gelesene Quelle, S = nur Suchsnippet/WebSearch-Kurzfassung (Seite nachlesen), A = aus Produkttyp abgeleitet, ? = angenommen. WebFetch und Chrome waren NICHT verfügbar: Es gibt in diesem Batch keine Stufe V. Alle URLs unten sind Suchtreffer (S), nicht gelesen.
Messe-Signal (Regel N2): Grep auf electronica/aussteller_namen.txt (2026-10-20) auf Wettbewerber aus Regel E1 und Materialhersteller: bdtronic GmbH (Z. 70), ELANTAS Europe GmbH (Z. 168), Momentive Performance Materials GmbH (Z. 415), RAMPF Advanced Polymers GmbH & Co. KG (Z. 502), RAMPF Production Systems GmbH & Co. KG (Z. 503), Nordson TEST&INSPECTION - Matrix Technologies GmbH (Z. 439, Prüftechnik, nur Randhinweis) stellen aus. Scheugenpflug, DOPAG, ViscoTec, Sonderhoff, Hilger u. Kern, Musashi, Henkel, DELO, Wacker, Sika: kein Treffer. Das Signal ändert keine Einstufung.
CRM-Abgleich: `python3 crm_abgleich.py` für jede Firma, dazu Konzern-/Alt-/Schwesternamen (Renu Electronics Pvt, RFMW, MRC Gigacomp, Richardson, Rikutec Germany, ROB Cemtrex, Cemtrex, Röchling SE, Roechling, Riken Keiki Co, ROKA). Ergebnis: kein Treffer außer PRÄFIX-Treffer "Richardson RFPD Germany GmbH [DE]" (bekannte_firmen_DE-AT-NL.txt Z. 1975), siehe Firma 2.

## 1. Renu Electronics GmbH
1. Firma: Renu Electronics GmbH (Messe: electronica 2026, Halle/Stand A1.645)
2. Segment / Demak-Geschäftsbereich: Optical Bonding (Touch-/HMI-Panels), Electrical Insulation (Industrie-PCs, Steuerelektronik), EMS-Baugruppen (Verguss auf Kundenwunsch)
3. Gebiet: Baden-Württemberg (Filderstadt)
4. Sitz und Fertigungsort: Filderstadt (Kurze Straße 29, 70794; Snippet S). Filderstadt wird als Kompetenzzentrum und Produktionsstandort beschrieben (S); die Gruppe fertigt auch in Indien (S, Zähler für Wasserzähler). Fertigende Einheit für die Produkte: Filderstadt laut Snippet, Produkt-zu-Werk-Zuordnung nicht belegt.
5. Website: https://www.renuelectronics.de (nicht gelesen; Adresse aus Messeprofilen abgeleitet, S)
6. Was wird gebaut -> Bauteile: HMI-Bediengeräte/Touch Panels und Industrie-PCs (ehemals Phoenix Contact HMI IPC Technology, davor SÜTRON electronic, gegründet 1968) sowie EMS: Entwicklung, SMT/THT-Fertigung, Box-Build, Test (S). Zertifikate ISO 9001, ISO 14001, IATF 16949, ISO 13485 (S). Typisch vergossen/verklebt/gedichtet (alles A): Touch/Display-Verklebung in HMI (A, Block B Optical Bonding), Gehäusedichtung IP65 (A, Block B), EMS-Baugruppen für Automotive/Medizin (A, Block B), Zähler-Elektronik aus dem Wasserzähler-Auftrag (A, Block A Energiezähler/Smart-Meter-Teile; Fertigungsort Indien laut Snippet).
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Sitz Filderstadt mit Produktionsstandort laut Snippets, aber Gruppe mit Werk in Indien (Konzern: Stufe V nötig, fehlt). Nachlesen: SPS-Ausstellerprofil und Renu-Standortseite.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: HMI-Touch/Display Mittel (A), HMI-Gehäuse/Dichtung Mittel (A), Industrie-PC-Elektronik Mittel (A), EMS-Baugruppen Automotive/Medizin Mittel (A, Medizintechnik-Regel: kleine Mengen zählen), Zähler-Elektronik Hoch (A, aber Fertigung Indien). Kein Beleg für Eigenverguss; ein Suchtreffer nennt weder Verguss noch Schutzlack.
9. Patentrecherche (Pflicht): Datenbanken Google Patents (über WebSearch-Operator site:patents.google.com, kein Browser) und Espacenet/DEPATISnet (nur über WebSearch-Suchbegriffe, Datenbank selbst nicht erreichbar).
- WebSearch: site:patents.google.com "Renu Electronics" OR "Sütron electronic" Vergussmasse OR potting OR Gehäuse: keine Treffer auf diesen Anmelder; nur allgemeine Vergussmassen-Patente anderer Anmelder (z. B. DE102020204941A1, AT14902U1, EP2695499; Anmelder in den Snippets nicht genannt, nicht zugeordnet).
- WebSearch: Sütron electronic Patent Espacenet OR DEPATISnet Bediengerät Gehäuse Dichtung Verguss: kein Treffer auf Sütron als Anmelder.
- Ergebnis: keine Treffer gefunden. Das ist kein Gegenbeweis; Anmelderfilter in Google Patents, Espacenet (pa=Sütron/Renu) und DEPATISnet nicht ausgeführt (siehe Einschränkungen). Phoenix Contact als Vorgänger-Anmelder nicht gesucht.
10. Einstufung Tom: prüfenswert (Fertigung Mittel S, Verguss Mittel A)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "Renu Electronics" und "Renu Electronics Pvt": kein Treffer; Vorgänger "Phoenix Contact" / "Sütron" nicht abgeglichen, siehe Einschränkungen)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Wird in Filderstadt gefertigt (HMI, EMS-Baugruppen) und was geht nach Indien? Impressum und Standortseite renuelectronics.de im Browser lesen, Stellenanzeigen Filderstadt (Fertigung, Montage, Vergießen). (b) Gehört Phoenix Contact (Vorgänger) zum CRM-Abgleich? Skript mit "Phoenix Contact" und "Sütron" laufen lassen. (c) Wird bei Renu vergossen/verklebt (Optical Bonding, Dichtung)? Aktion: Beobachtung, vorerst nicht kontaktieren.
14. Quellen:
- https://www.computer-automation.de/bedienen-und-beobachten/renu-uebernimmt-hmi-fertigung.htm, Suchsnippet (S): „Renu übernimmt HMI-Fertigung“ (Titel); Abruf 2026-10-20.
- https://sps.mesago.com/nuernberg/de/ausstellersuche.detail.html/renu-electronics-gmbh/mf_6_0052487661_4595611_10000128202501.html, Suchsnippet (S): Ausstellerprofil, Produktionsstandort Filderstadt laut Zusammenfassung; Abruf 2026-10-20.
- https://www.northdata.de/?id=6451262, Suchsnippet (S): „Sütron electronic GmbH“, Kurze Straße 29, Filderstadt, Gewinnabführung Phoenix Contact 2009; Abruf 2026-10-20.
15. Größe/Umsatz: unbekannt (Verzeichnis nennt 51 bis 100 Mitarbeitende, eine Quelle, S)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Renu/Sütron/Phoenix Contact); WebSearch "Renu Electronics Filderstadt Verguss OR Vergießen OR Schutzlack OR Dosieranlage Elektronikfertigung Stellenanzeige" (kein Anlagen- oder Materialname). Messe-Signal: bdtronic, ELANTAS, RAMPF, Momentive stellen auf der electronica aus.
17. Identität: teilweise belegt (S). Vorgabe: Renu Electronics GmbH, 70794 Filderstadt. North Data/Verzeichnisse: Kurze Straße 29, 70794 Filderstadt, frühere Firma Sütron electronic GmbH. Rechtsform, Register und Impressum nicht gelesen. Gleichnamige Renu Electronics Pvt Ltd (Indien, Konzernmutter) ist eine andere Einheit und wird nicht vermischt.

## 2. RFMW - MRC Gigacomp GmbH & Co. KG
1. Firma: RFMW - MRC Gigacomp GmbH & Co. KG (Messe: electronica 2026, Halle/Stand C5.561)
2. Segment / Demak-Geschäftsbereich: keiner (Distributor, kein Fertiger)
3. Gebiet: Bayern (Freising)
4. Sitz und Fertigungsort: Sitz Bahnhofstr. 1, 85354 Freising (S, CB Insights/EMV-Ausstellerprofil). Keine Fertigung belegt. Konzern: RFMW (San Jose, USA) übernahm MRC Gigacomp und MRC Components zum 01.04.2023 (S, Business Wire laut Suchzusammenfassung).
5. Website: https://www.rfmw.com/rfmw-germany/48 (Suchtreffer, nicht gelesen)
6. Was wird gebaut: nichts belegt. Vertrieb von HF-/Mikrowellen-Halbleitern, Bauelementen, Sensoren, Antennen und Leistungselektronik (S). Typisch vergossen/verklebt/gedichtet: keine eigenen Bauteile; Handelsware (A, Block C Handel ohne Eigenfertigung).
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Distributor mit Lager (S), keine Fertigung belegt.
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A (Block C: Handel/Distribution ohne Eigenfertigung). Einzelbewertung: HF-Halbleiter/Komponenten Niedrig (A, Handelsware), Schwestergesellschaft MRC Components (Magnetkerne, Vertrieb) Niedrig (A).
9. Patentrecherche (Pflicht): Datenbanken Google Patents (über WebSearch site:patents.google.com) und Espacenet/DEPATISnet (nicht erreichbar, nicht ausgeführt, E2-Kurzprüfung für Distributor).
- WebSearch: site:patents.google.com "RFMW" OR "MRC Gigacomp" potting OR encapsulation: keine Treffer auf diese Anmelder, nur allgemeine Potting-Patente anderer Anmelder.
- Ergebnis: keine Treffer gefunden (kein Gegenbeweis). Espacenet und DEPATISnet nicht ausgeführt, Grund: Distributor, WebSearch-Budget.
10. Einstufung Tom: kein Fertiger (Distributor, Quelle S)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "RFMW - MRC Gigacomp", "RFMW", "MRC Gigacomp": kein Treffer). Hinweis: Das Skript meldete beim Konzernbegriff "Richardson" den PRÄFIX-Treffer "Richardson RFPD Germany GmbH [DE]" (bekannte_firmen Z. 1975). Das ist ein anderer Distributor; nur zur Information, nicht dieselbe Einheit (Richardson wurde nicht als Konzern von RFMW belegt).
13. Nachrecherche-Auftrag und Aktion (Vorschlag): keiner nötig, falls Tina Rot (Zeile 1, E2) bestätigt. Bei Zweifel: Impressum der RFMW-Germany-Seite lesen (Eigenfertigung auszuschließen). Aktion: nicht aufnehmen.
14. Quellen:
- https://emv.mesago.com/koeln/de/ausstellersuche.detail.html/mrc-gigacomp-gmbh--co-kg.html, Suchsnippet (S): Anbieter von „RF and microwave semiconductors and components“ (sinngemäß, Zusammenfassung); Abruf 2026-10-20.
- https://www.businesswire.com/news/home/20230424005960/en, Suchsnippet (S): RFMW schließt Übernahme von MRC Gigacomp und MRC Components zum 1. April 2023 ab (sinngemäß); Abruf 2026-10-20.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag RFMW/MRC); keine weitere Websuche (Distributor ohne Fertigung, Budget). Messe-Signal: bdtronic, ELANTAS, RAMPF, Momentive auf der electronica.
17. Identität: teilweise belegt (S). Vorgabe "RFMW - MRC Gigacomp GmbH & Co. KG, 85354 Freising"; Suchtreffer führen MRC Gigacomp GmbH & Co. KG, Bahnhofstr. 1, Freising, Marke "MRC Gigacomp/RFMW". Register und Impressum nicht gelesen.

## 3. RG Elektrotechnologie GmbH
1. Firma: RG Elektrotechnologie GmbH (Messe: electronica 2026, Halle/Stand A1.502)
2. Segment / Demak-Geschäftsbereich: unklar; Electrical Insulation / EMS-Baugruppen, falls Fertigung bestätigt wird
3. Gebiet: Rest Deutschland+Niederlande (Quedlinburg, Sachsen-Anhalt, laut Verzeichnis OT Gernrode)
4. Sitz und Fertigungsort: Quedlinburg, OT Gernrode (S, Implisense-Profil, Straße nicht genannt). Fertigungsort nicht belegt.
5. Website: unbekannt (nicht gefunden)
6. Was wird gebaut: Laut Verzeichnis (S, Implisense, Bezahlseite, nur Snippet) Entwicklung elektrischer Technologien, Herstellung, Handel und Installation elektrischer und elektronischer Baugruppen. Konkrete Produkte nicht belegt. Eine eigene Website wurde nicht gefunden. Typisch vergossen/verklebt/gedichtet: unbekannt; falls EMS/Baugruppenfertigung: Baugruppen (A, Block B, Verguss auf Kundenwunsch).
7. Fertigung DE/AT/NL: Mittel, Stufe ?. Begründung: Gegenstand lautet "Herstellung", aber Produkt, Werk und Größe sind nicht belegt; Sitzregel A nur bei erkennbarem Geräte-/Industriebauer, hier nicht belegt.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe ?. Einzelbewertung: elektrische/elektronische Baugruppen Mittel (?, Typ unbekannt), Handel/Installation Niedrig (A). Reine Annahme aus dem Gegenstand der Gesellschaft, kein Produktbeleg.
9. Patentrecherche (Pflicht): Datenbanken Google Patents und Espacenet/DEPATISnet (beide nur indirekt über WebSearch erreichbar, keine Datenbankabfrage mit Anmelderfilter).
- WebSearch: patent "RG Elektrotechnologie" Quedlinburg: kein Treffer auf Patente dieses Anmelders; Treffer waren Jobseiten und andere Firmen.
- Google Patents mit Anmelderfilter und Espacenet pa="RG Elektrotechnologie" nicht ausgeführt (Browser fehlt).
- Ergebnis: keine Treffer gefunden (kein Gegenbeweis).
10. Einstufung Tom: prüfenswert (Fertigung Mittel ?, Verguss Mittel ?; Produkt unbekannt)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "RG Elektrotechnologie": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Welche Produkte fertigt die RG Elektrotechnologie GmbH in Gernrode (Messeprofil electronica, Firmenwebsite, Stellenanzeigen)? (b) Gehört sie zu einer Gruppe? (c) Impressum und Handelsregister (Stendal/Magdeburg, HRB laut Snippet 107964, nicht verifiziert) lesen. Aktion: Beobachtung bis Produkt geklärt.
14. Quellen:
- https://implisense.com/en/companies/rg-elektrotechnologie-gmbh-quedlinburg-ot-gernrode-DEVMPJUK2232, Suchsnippet (S): „RG Elektrotechnologie GmbH“ Quedlinburg OT Gernrode, Gegenstand Herstellung elektrischer Baugruppen (sinngemäß); Abruf 2026-10-20.
15. Größe/Umsatz: unbekannt (Snippet nennt Bilanzsumme ca. 6 Mio. EUR, 2022, eine Quelle S, nicht verwendbar)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag); WebSearch "RG Elektrotechnologie GmbH Quedlinburg Baugruppenfertigung Elektronik" und WebSearch "\"RG Elektrotechnologie\" GmbH" (keine Anlagen-/Materialnamen). Messe-Signal: bdtronic, ELANTAS, RAMPF, Momentive auf der electronica.
17. Identität: teilweise belegt (S). Vorgabe: RG Elektrotechnologie GmbH, 06485 Quedlinburg. Verzeichnis: Quedlinburg OT Gernrode (PLZ 06485 gehört zu Quedlinburg inkl. Gernrode, nicht geprüft). Gleichnamige/ähnliche Firmen (RGW Elektrotechnik GmbH Schwabach, RG GmbH, RG Technologies Polen) sind nicht dieselbe Firma und nicht vermischt. Impressum nicht gefunden.

## 4. RIGOL Technologies EU GmbH
1. Firma: RIGOL Technologies EU GmbH (Messe: electronica 2026, Halle/Stand A4.231)
2. Segment / Demak-Geschäftsbereich: keiner in DE (Vertriebs-/Serviceeinheit); Produkte (Messgeräte) wären Electrical Insulation, wenn sie hier gebaut würden
3. Gebiet: Bayern (Gilching), nur Vertrieb; Fertigung außerhalb (Suzhou, China)
4. Sitz und Fertigungsort: Sitz Friedrichshafener Str. 5, 82205 Gilching (S, RIGOL-Standortseite laut Suchzusammenfassung). Fertigung bei der Mutter in Suzhou, China (Campus 2014 eröffnet, SMT-Linien; S); später weitere Standorte Malaysia/China (S). Keine Fertigung in DE belegt.
5. Website: https://www.rigol.com (Suchtreffer, nicht gelesen)
6. Was wird gebaut: Die Mutter baut Oszilloskope, Funktionsgeneratoren, Spektrumanalysatoren, HF-Signalgeneratoren, Netzgeräte, Multimeter (S). In DE: Vertrieb und Service. Typisch vergossen: Netzteile/Stromversorgungen in Messgeräten (A, Block A), aber nicht in DE gefertigt.
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Fertigung der Mutter in China (Suzhou) laut Suchtreffern 2014; Gilching nur Europa-Niederlassung (seit 2011, S).
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A für das Produkt (Netzteile/Elektronik in Messgeräten); für die Einheit in Gilching ohne Bedeutung, da keine Fertigung. Einzelbewertung: Netzteil Mittel (A), Messgeräte-Elektronik Mittel (A), Gehäuse Niedrig (A).
9. Patentrecherche (Pflicht): Datenbanken Google Patents (über WebSearch site:patents.google.com) und Espacenet/DEPATISnet (nicht ausgeführt, Grund: keine Fertigung in DE, E2).
- WebSearch: site:patents.google.com Rigol Technologies potting OR encapsulation OR sealing: keine Treffer auf Rigol als Anmelder; nur allgemeine Potting-Patente anderer Anmelder.
- Ergebnis: keine Treffer gefunden (kein Gegenbeweis). Anmelder-Varianten Beijing/Suzhou RIGOL nicht gesucht.
10. Einstufung Tom: kein Fertiger (Vertriebsgesellschaft in DE; Fertigung China, Stufe S)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "RIGOL Technologies EU", "RIGOL Technologies": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): falls Tina nicht Rot (E3) setzt: Gibt es Fertigung/Endmontage in Gilching? Impressum RIGOL EU lesen. Aktion: nicht aufnehmen.
14. Quellen:
- https://www.rigol.com/de_DE/company/offices.html, Suchsnippet (S): „RIGOL EU, Friedrichshafener Str. 5, 82205 Gilching“ (sinngemäß); Abruf 2026-10-20.
- https://www.eenewseurope.com / https://microwavejournal.com/articles/22472-rigol-technologies-opens-a-new-manufacturing-and-engineering-campus-in-suzhou-china, Suchsnippet (S): Rigol eröffnet Fertigungs- und Entwicklungscampus in Suzhou (Titel); Abruf 2026-10-20.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag RIGOL); keine eigene Wettbewerbersuche (keine Fertigung in DE, Budget). Messe-Signal: bdtronic, ELANTAS, RAMPF, Momentive auf der electronica.
17. Identität: Abweichung. Vorgabe "RIGOL Technologies EU GmbH". RIGOL-Seiten nennen "RIGOL EU" und an anderer Stelle "RIGOL Technologies GmbH" (beide Friedrichshafener Str. 5, Gilching); ältere Adresse Carl-Benz-Str. 11 Gilching, Verzeichnis Puchheim wahrscheinlich veraltet (S). Genaue Firmierung/Register nicht gelesen.

## 5. RIKEN KEIKI
1. Firma: RIKEN KEIKI (Messe: electronica 2026, Halle/Stand C1.214)
2. Segment / Demak-Geschäftsbereich: keiner in DE (Vertrieb); Produkte (Gassensoren, Gaswarngeräte) wären Electrical Insulation / Sensorik, wenn hier gebaut
3. Gebiet: Rest Deutschland+Niederlande (Eschborn, Hessen), nur Niederlassung; Fertigung Japan (nicht eigens belegt)
4. Sitz und Fertigungsort: Riken Keiki GmbH, Mergenthalerallee 15-21, 65760 Eschborn, Tochter der Riken Keiki Co. Ltd (Japan), seit 2017 in Eschborn (S, Silicon Saxony). Keine Fertigung in Eschborn belegt.
5. Website: https://silicon-saxony.de/mitglieder/riken-keiki-gmbh/ (Mitgliederprofil, Suchtreffer; Firmenwebsite nicht gelesen)
6. Was wird gebaut: Tochter für Vertrieb/Service von Gasmessgeräten und Gaswarnanlagen (Planung, Wartung) in Europa außer UK (S). Die Mutter baut tragbare und stationäre Gasdetektoren, Gasanalysatoren, Sensoren (S). Typisch vergossen: Gassensoren und Warngeräte-Elektronik (A, Block A Sensoren/Ex-Schutz), aber Fertigungsort Mutter Japan.
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Eschborn ist laut Profil Tochter für Europa-Geschäft (Vertrieb, Planung, Wartung); Fertigung in DE nicht belegt.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A für das Produkt (Gassensoren, Ex-Schutz-Elektronik), aber nicht in DE/AT/NL gefertigt; für die Einheit in Eschborn bedeutungslos. Einzelbewertung: Gassensor-Elemente Hoch (A), Gaswarngeräte-Elektronik Hoch (A), Gehäuse Mittel (A).
9. Patentrecherche (Pflicht): Datenbanken Google Patents (über WebSearch site:patents.google.com) und Espacenet/DEPATISnet (nicht ausgeführt, E2/E3-Kurzprüfung).
- WebSearch: site:patents.google.com "Riken Keiki" potting OR resin OR sealing gas sensor: kein Treffer mit gesichertem Anmelder Riken Keiki; US7712349B2 "Gas sensor" (Harzpackage, Anmelder im Snippet nicht genannt, nicht zugeordnet).
- Ergebnis: keine gesicherten Treffer (kein Gegenbeweis). Japanische Anmelderschreibweise (理研計器) nicht gesucht.
10. Einstufung Tom: kein Fertiger (Vertriebs-/Servicetochter in DE, Fertigung Japan; Stufe S)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "RIKEN KEIKI", "Riken Keiki Co": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): falls nicht Rot (E3): Gibt es Montage/Fertigung in Eschborn? Impressum Riken Keiki GmbH lesen. Aktion: nicht aufnehmen.
14. Quellen:
- https://silicon-saxony.de/mitglieder/riken-keiki-gmbh/, Suchsnippet (S): „Tochtergesellschaft von Riken Keiki Co. Ltd“ (sinngemäß, deutsche Zusammenfassung); Abruf 2026-10-20.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag); keine eigene Wettbewerbersuche (keine Fertigung in DE, Budget). Messe-Signal: bdtronic, ELANTAS, RAMPF, Momentive auf der electronica.
17. Identität: Abweichung. Vorgabe "RIKEN KEIKI" (ohne Rechtsform), Sitz Eschborn 65760. Verzeichnis: "RIKEN KEIKI GmbH", Mergenthalerallee 15-21, 65760 Eschborn (S). Rechtsform und Register nicht gelesen.

## 6. RIKUTEC Germany GmbH & Co. KG
1. Firma: RIKUTEC Germany GmbH & Co. KG (Messe: electronica 2026, Halle/Stand: in der Eingabe "None", keine Halle/kein Stand angegeben)
2. Segment / Demak-Geschäftsbereich: keiner erkennbar (Kunststoff-Blasformen, Verpackung)
3. Gebiet: Rest Deutschland+Niederlande (Altenkirchen, Rheinland-Pfalz)
4. Sitz und Fertigungsort: Graf-Zeppelin-Str. 1-5, 57610 Altenkirchen (Westerwald) (S). Gruppe mit Produktion in Deutschland, Frankreich und Spanien (S, Berufsstart). Konzern, daher Stufe V für DE-Fertigung nötig.
5. Website: unbekannt (Suchtreffer: silicon-saxony.de/mitglieder/rikutec-germany-gmbh-co-kg/)
6. Was wird gebaut: Blasformteile aus Kunststoff, mehrschichtige HDPE-Fässer und IBC für hochreine Anwendungen (COEX-Akkumulatorkopf), technische Blasformteile; Maschinen- und Anlagenbau als Kernaktivität (S). Typisch vergossen/verklebt/gedichtet: Verpackung/Behälter (A, Block C), Steuerelektronik in Maschinen (A, Block B, nachrangig).
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Altenkirchen als Produktionsstandort laut Profil, aber Gruppe mit Werken in FR/ES.
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A. Einzelbewertung: Kunststoffbehälter/IBC Niedrig (A, Block C Verpackung), technische Blasformteile Niedrig (A), Maschinen-Steuerelektronik Mittel (A, nachrangig, nicht Fertigungsgegenstand).
9. Patentrecherche (Pflicht): Datenbanken Google Patents (über WebSearch site:patents.google.com) und Espacenet/DEPATISnet (nicht ausgeführt, Grund: Produkt Verpackung).
- WebSearch: site:patents.google.com Rikutec Richter Kunststofftechnik Blasformen Patent: kein Treffer auf RIKUTEC als Anmelder. Zufallsbefund (S): Zitierungstabelle nennt "Richter, Günter, 57610 Altenkirchen" als Anmelder DE8627708U1 "Palettenbehälter aus Kunststoff" (1986, Person, Gebrauchsmuster, kein Verguss, Rechtsstand nicht geprüft).
- Ergebnis: kein Patent mit Verguss gefunden.
10. Einstufung Tom: unwahrscheinlich (Verguss Niedrig A)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "RIKUTEC", "Rikutec Germany": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): keiner nötig. Falls Tina prüft: Fertigt RIKUTEC Elektronik/Steuerungen für Anlagen (Maschinenbau-Sparte)? Aktion: nicht aufnehmen.
14. Quellen:
- https://silicon-saxony.de/mitglieder/rikutec-germany-gmbh-co-kg/, Suchsnippet (S): Titel „RIKUTEC Germany GmbH & Co. KG“, Inhalt Blasformspezialist, mehrschichtige HDPE-Fässer und IBC (sinngemäß); Abruf 2026-10-20.
- https://berufsstart.de/unternehmen/rikutec/firmengeschichte.php, Suchsnippet (S): Gründung 1986 durch Günter Richter, Produktion in Deutschland, Frankreich, Spanien (sinngemäß); Abruf 2026-10-20.
15. Größe/Umsatz: "über 240 Mitarbeitende in fünf Ländern" (StepStone-Snippet, eine Quelle S, nicht verwendbar)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag); keine eigene Wettbewerbersuche (Produkt Verpackung, Budget). Messe-Signal: bdtronic, ELANTAS, RAMPF, Momentive auf der electronica.
17. Identität: teilweise belegt (S). Vorgabe RIKUTEC Germany GmbH & Co. KG, 57610 Altenkirchen; Suchtreffer bestätigen Adresse Graf-Zeppelin-Str. 1-5 und frühere Firmierung "RIKUTEC Richter Kunststofftechnik GmbH & Co. KG". Register/Impressum nicht gelesen. Die Messeeingabe enthält weder Halle noch Stand.

## 7. RM Components GmbH
1. Firma: RM Components GmbH (Messe: electronica 2026, Halle/Stand B6.135 / C6.530)
2. Segment / Demak-Geschäftsbereich: keiner (Großhändler)
3. Gebiet: Bayern (Schwabach)
4. Sitz und Fertigungsort: Schwabach (91126, Lager). Keine Fertigung belegt.
5. Website: unbekannt (nicht gelesen)
6. Was wird gebaut: nichts. Laut Pressemitteilung der Stadt Schwabach (2015) elektronischer Bauelemente-Großhändler und deutscher Distributor von Taiyo Yuden und Holystone; 16 Mitarbeitende, ca. 13 Mio. EUR Umsatz 2015 (S). Typisch vergossen/verklebt: nicht zutreffend, Handelsware (A, Block C). Die Ersteinschätzung "Transformatoren/Spulen" ist durch diese Quelle nicht gedeckt (Taiyo Yuden stellt Induktivitäten her; RM Components vertreibt sie nur).
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Großhändler laut Stadt-PM 2015 (alt, Lehre 17: aktuelle Quelle fehlt).
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A (Block C Handel ohne Eigenfertigung). Einzelbewertung: Induktivitäten/Bauelemente (Handelsware) Niedrig (A).
9. Patentrecherche (Pflicht): Datenbanken Google Patents (über WebSearch site:patents.google.com) und Espacenet/DEPATISnet (nicht ausgeführt, Distributor, E2).
- WebSearch: site:patents.google.com "RM Components" Schwabach OR "ROB Cemtrex" OR "ROB GmbH" Neulingen (kombinierte Suche mit Firma 8): kein Treffer auf RM Components als Anmelder.
- Ergebnis: keine Treffer gefunden (kein Gegenbeweis).
10. Einstufung Tom: kein Fertiger (Großhändler, Stufe S)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "RM Components": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): keiner nötig, falls Tina Rot (E2) bestätigt. Aktion: nicht aufnehmen.
14. Quellen:
- https://schwabach.de/images/referate/referat_3/downloads/Wirtschaftsfoerderung/Unternehmensbesuche/4_stadt-PM264_2015-10-15_Unternehmensbesuch_RM-Components.pdf, Suchsnippet (S): Titel „Unternehmensbesuch RM Components“, Inhalt Großhändler elektronischer Bauelemente, Taiyo Yuden und Holystone (sinngemäß); Abruf 2026-10-20.
15. Größe/Umsatz: 16 Mitarbeitende, ca. 13 Mio. EUR Umsatz (Stand 2015, eine Quelle S, veraltet)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag); keine eigene Wettbewerbersuche (Großhändler). Messe-Signal: bdtronic, ELANTAS, RAMPF, Momentive auf der electronica.
17. Identität: teilweise belegt (S). Vorgabe RM Components GmbH, 91126 Schwabach; Stadt-PM bestätigt Firma und Ort 2015. Rechtsform, Register nicht gelesen. Ein Suchtreffer "robotized rm systems GmbH" (Schwabach) ist eine andere Firma, nicht vermischt.

## 8. ROB GmbH
1. Firma: ROB GmbH (Messe: electronica 2026, Halle/Stand A1.123)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (EMS-Baugruppen, Kabelkonfektion), je nach Kunden E-Mobility Potting
3. Gebiet: Baden-Württemberg (Neulingen)
4. Sitz und Fertigungsort: Am Wolfsbaum 1, 75245 Neulingen (S, Cemtrex-Kontaktseite und Bloomberg-LEI-Eintrag HRB 724976 Amtsgericht Mannheim). Frühere ROB Group (Übernahme durch Cemtrex 2013, "ROB Cemtrex GmbH", Werk Rumänien 2013 laut Snippet). Aktuelle Konzernzugehörigkeit nicht belegt (S).
5. Website: unbekannt (nicht gelesen)
6. Was wird gebaut: Elektronikfertigung: Design, Entwicklung, Produktion, Montage, Logistik; "build-to-order" Module und Systeme; Kabelkonfektion (S, ensun/Evertiq/Cemtrex-Snippets). Stellenanzeigen nennen SMT-Linie, Leiterplattenbestückung, AOI (S). Typisch vergossen/verklebt/gedichtet: EMS-Baugruppen für Industrie/Automotive (A, Block B), Kabelkonfektion mit vergossenen Steckern (A, Block A, Kabelkonfektion nur als Leistung genannt).
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Neulingen als Produktionsstandort mit SMT-Linie laut Stellenanzeigen-Snippets; frühere Gruppe mit Werken in Rumänien und Cemtrex-Konzern, aktuell unklar (Konzern/mehrere Werke: Stufe V nötig).
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: EMS-Baugruppen Mittel (A), Kabelkonfektion Mittel (A), Box-Build-Systeme Mittel (A). Kein Beleg für Eigenverguss.
9. Patentrecherche (Pflicht): Datenbanken Google Patents (über WebSearch site:patents.google.com) und Espacenet/DEPATISnet (nicht ausgeführt).
- WebSearch: site:patents.google.com "RM Components" Schwabach OR "ROB Cemtrex" OR "ROB GmbH" Neulingen (kombinierte Suche mit Firma 7): keine Treffer auf ROB GmbH/ROB Cemtrex als Anmelder; nur unzusammenhängende Roboter-/Montage-Patente.
- Ergebnis: keine Treffer gefunden (kein Gegenbeweis). Anmelder-Varianten ROB Cemtrex, ROB Group, Cemtrex nur in dieser einen Suche enthalten.
10. Einstufung Tom: prüfenswert (Fertigung Mittel S, Verguss Mittel A)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "ROB GmbH", "ROB Cemtrex", "Cemtrex": kein Treffer; Hinweis: Kern-Name "rob" ist sehr kurz, Skript nur PRÄFIX/Kern, manuelles Grep "rob" nicht gesondert ausgeführt)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Gehört die ROB GmbH heute zu Cemtrex oder einem anderen Konzern? Impressum (Website) und Handelsregister Mannheim HRB 724976 lesen. (b) Was fertigt Neulingen aktuell (Branchen der Kunden, Automotive/Industrie), wird vergossen? Stellenanzeigen Neulingen im Browser lesen. (c) Konzern-CRM-Abgleich "Cemtrex" bleibt neu. Aktion: Beobachtung, nicht kontaktieren.
14. Quellen:
- https://lei.bloomberg.com/leis/view/529900CSEM9VFT6MQO24, Suchsnippet (S): „ROB GmbH“, Am Wolfsbaum 1, Neulingen, Amtsgericht Mannheim HRB 724976 (sinngemäß); Abruf 2026-10-20.
- https://cemtrex.com/contact/, Suchsnippet (S): „Am Wolfsbaum 1, 75245 Neulingen, Germany“; Abruf 2026-10-20.
- https://de.jobted.com/job/7b91782494fac1cf62ee5979408b5bbb, Suchsnippet (S): Stelle „Löter (m/w/d)“, SMT-Linie (nur Titel/Zusammenfassung, Firmenzuordnung nicht geprüft); Abruf 2026-10-20.
15. Größe/Umsatz: unbekannt (Quellen widersprüchlich: 51 bis 100 bzw. 201 Mitarbeitende, S)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag ROB/Cemtrex); WebSearch "ROB Cemtrex Neulingen Verguss OR Vergießen OR Kabelkonfektion OR Dosieranlage Nordson OR Scheugenpflug OR DOPAG" (kein Bezug zu ROB; Treffer nur allgemeine Scheugenpflug-Seiten). Messe-Signal: bdtronic, ELANTAS, RAMPF, Momentive auf der electronica.
17. Identität: teilweise belegt (S). Vorgabe ROB GmbH, 75245 Neulingen. Bloomberg-LEI: ROB GmbH, Am Wolfsbaum 1, Amtsgericht Mannheim HRB 724976, Status aktiv (S). Gleichnamige Firmen ausgeschlossen: ROB GmbH Schweiz (CHE-490.773.590, Suchtreffer onlineinfo.ch, andere Firma); ROB Cemtrex Automotive GmbH (HRB 725009, gleiche Adresse, laut Snippet gelöscht, Vorgängerfirma). Impressum nicht gelesen.

## 9. Röchling Industrial Lahnstein SE & Co. KG
1. Firma: Röchling Industrial Lahnstein SE & Co. KG (Messe: electronica 2026, Halle/Stand C1.860)
2. Segment / Demak-Geschäftsbereich: keiner erkennbar (Halbzeuge, Zerspanung); allenfalls Gasketing/Klebung als Kundenbearbeitung
3. Gebiet: Rest Deutschland+Niederlande (Lahnstein, Rheinland-Pfalz)
4. Sitz und Fertigungsort: Sustaplast-Straße 1, 56112 Lahnstein (S, Bayern-Innovativ-Profil), zweiter Standort Nentershausen. Fertigende Einheit: Lahnstein (Kompetenzzentrum für Hochleistungskunststoffe, S); Konzern Röchling SE & Co. KG mit weltweit vielen Werken.
5. Website: https://roechling.com/industrial/lahnstein (Suchtreffer, nicht gelesen)
6. Was wird gebaut: Halbzeuge und Fertigteile aus Hochleistungskunststoffen: extrudierte und kalandrierte Platten, Stäbe, Rohre, Profile, Folien, Pressplatten, CNC-gefertigte Teile nach Zeichnung; Marken SustaPEEK, Sustarin, Sustamid (S). Typisch vergossen/verklebt/gedichtet: Halbzeuge/Platten (A, Block C), zerspante Teile (A, Block C); Verklebung/Dichtung nur als Kundenanwendung der Teile, nicht als Röchling-Prozess belegt.
7. Fertigung DE/AT/NL: Hoch, Stufe S. Begründung: Mehrere Suchtreffer (Standortseite, DQS-Zertifikat mit Scope "development, manufacturing, machining", neue Halle 2019 mit 5 Mio. EUR) belegen Fertigung in Lahnstein; Konzern, daher V nötig, nicht erfüllt (keine Seite gelesen). Nachlesen: roechling.com/industrial/lahnstein.
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A. Einzelbewertung: Platten/Stäbe/Rohre Niedrig (A), Profile/Folien Niedrig (A), CNC-Fertigteile nach Zeichnung Niedrig bis Mittel (A, hängt vom Kundenteil ab, Produkt unbekannt).
9. Patentrecherche (Pflicht): Datenbanken Google Patents (über WebSearch site:patents.google.com) und Espacenet/DEPATISnet (über WebSearch-Suchbegriffe, Datenbank nicht abgefragt).
- WebSearch: site:patents.google.com Röchling Industrial Lahnstein Vergussmasse OR potting OR Verklebung OR Dichtung: keine Treffer auf Röchling als Anmelder; allgemeine Vergussmassen-Patente anderer Anmelder (z. B. EP4536730A1 laut Snippet 3M).
- WebSearch: Röchling Industrial Lahnstein Patent Anmelder Espacenet OR DEPATISnet Vergussmasse OR Dichtung OR Kleben: kein Patent gefunden; Treffer waren Firmenprofile (DQS, Silicon Saxony, FMB).
- Ergebnis: keine Treffer gefunden (kein Gegenbeweis). Anmelder-Varianten "Röchling Industrial SE" und Konzern "Röchling SE" nicht in einer Patentdatenbank abgefragt.
10. Einstufung Tom: unwahrscheinlich (Fertigung Hoch S, Verguss Niedrig A)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "Röchling Industrial Lahnstein", "Röchling SE", "Röchling", "Roechling": kein Treffer; Konzernabgleich Regel M durchgeführt)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Fertigt Lahnstein Teile für Elektronik/Halbleiter (Silicon Saxony/Bavarian Chips Alliance Mitglied, S) mit Klebung oder Dichtung? Produktseite und Sparten (Halbleiter-/Elektronikteile, Durostone-Isolierwerkstoffe) im Browser lesen. (b) Welcher Werkstoff/welche Sparte wird in Lahnstein gefertigt? Aktion: Beobachtung, geringe Priorität.
14. Quellen:
- https://roechling.com/industrial/lahnstein, Suchsnippet (S): Lahnstein als Kompetenzzentrum für Hochleistungskunststoffe, Extrusion, Kalandrieren, Heißpressen, CNC (sinngemäß); Abruf 2026-10-20.
- https://www.bayern-innovativ.de/en/competencies-bavarian-chips-alliance/roechling-industrial-lahnstein-se-und-co-kg/, Suchsnippet (S): Adresse „Sustaplast-Straße 1 (56112)“ und Standorte Lahnstein/Nentershausen (sinngemäß); Abruf 2026-10-20.
- https://www.dqsglobal.com/en/customer-database/roechling-industrial-lahnstein-se-co.-kg2, Suchsnippet (S): Scope Entwicklung, Fertigung, Zerspanung, Vertrieb technischer Kunststoffe (sinngemäß); Abruf 2026-10-20.
15. Größe/Umsatz: "über 370 Mitarbeitende" (Firmenseite laut Snippet) bzw. "über 300" (Stellenanzeigen); Quellen widersprüchlich, S, nicht verwendbar
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Röchling); WebSearch "Röchling Lahnstein Kleben OR Dosieranlage OR Klebstoff Henkel OR DELO OR Nordson OR Sonderhoff Halbzeuge" (kein Röchling-Bezug, nur allgemeine Dosiertechnik-Seiten). Messe-Signal: bdtronic, ELANTAS, RAMPF, Momentive auf der electronica.
17. Identität: teilweise belegt (S). Vorgabe Röchling Industrial Lahnstein SE & Co. KG, 56112 Lahnstein; DQS-Zertifikat und Bayern-Innovativ-Profil führen dieselbe Firmierung. Register/Impressum nicht gelesen. Andere Röchling-Einheiten (z. B. Röchling Industrial Weinfelden AG, Schweiz) sind nicht vermischt.

## 10. ROKA - Robert Karst GmbH & Co.KG Elektrotechnische Fabrik
1. Firma: ROKA - Robert Karst GmbH & Co.KG Elektrotechnische Fabrik (Messe: electronica 2026, Halle/Stand B2.331)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Kabelkonfektion, Steckvorrichtungen), nachrangig Gasketing/Klebung
3. Gebiet: Rest Deutschland+Niederlande (Berlin)
4. Sitz und Fertigungsort: Sitz laut Eingabe 12277 Berlin; Verzeichnis nennt Gneisenaustraße 27, 10961 Berlin (S, IT-in-Germany), gegründet 1901. Fertigungsort nicht belegt.
5. Website: roka-berlin.de (aus Verzeichnis, S; nicht gelesen)
6. Was wird gebaut: Verzeichnis (S): Kabelbefestigungsmaterial, Kabelschellen, Lautsprecherkabel, NF- und HF-Steckvorrichtungen, Koaxial-Steckverbinder, Antennenbuchsen und -stecker. Foreneintrag (S, sekundär): liefert hauptsächlich Industriekunden, Verpackungseinheit ca. 1000 Stück. Typisch vergossen/verklebt/gedichtet: Koaxial-/HF-Steckverbinder und Kabelkonfektion (A, Block A Kabelkonfektion/Stecker, Basis hoch, bei Standard-Koaxsteckern nur selten tatsächlich vergossen), Kabelschellen Niedrig (A).
7. Fertigung DE/AT/NL: Mittel, Stufe A (Sitzregel, "Elektrotechnische Fabrik" mit erkennbarem Standort); ob Berlin der Fertigungsort ist, ist nicht belegt (Stufe S/?, kein Werksbeleg). Direkte Fertigungsquelle fehlt.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Koaxial-/HF-Steckverbinder Mittel (A), Lautsprecher-/Antennenkabelkonfektion Mittel (A), Antennenbuchsen/-stecker Mittel (A), Kabelschellen/Befestigung Niedrig (A). Kein Beleg für Eigenverguss.
9. Patentrecherche (Pflicht): Datenbanken Google Patents (über WebSearch site:patents.google.com) und Espacenet/DEPATISnet (nicht ausgeführt, Grund: Budget/Browser fehlt).
- WebSearch: site:patents.google.com "Robert Karst" Berlin Steckverbinder OR connector OR Kabel: keine Treffer auf Robert Karst/ROKA als Anmelder; nur allgemeine deutsche Steckverbinder-Patente anderer Anmelder (z. B. DE4224673C2, DE3209734A1).
- Ergebnis: keine Treffer gefunden (kein Gegenbeweis). Anmelder-Varianten "Robert Karst GmbH & Co. KG", "ROKA" nur in dieser einen Suche.
10. Einstufung Tom: prüfenswert (Fertigung Mittel A, Verguss Mittel A)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu (crm_abgleich.py "ROKA Robert Karst", "ROKA": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Wo fertigt ROKA (Berlin, Eigenfertigung oder Zukauf aus Asien)? roka-berlin.de, Impressum und Stellenanzeigen im Browser lesen. (b) Sitz: Marienfelde (12277) oder Kreuzberg (10961)? (c) Werden Kabel/Stecker vergossen oder überspritzt (Overmolding)? Aktion: Beobachtung, nicht kontaktieren.
14. Quellen:
- https://www.it-in-germany.de/firma/Robert+Karst+GmbH+%26+Co.+KG+Elektrotechnische+Fabrik/5000735/51642/eng, Suchsnippet (S): „Robert Karst GmbH & Co. KG Elektrotechnische Fabrik“, Gneisenaustraße 27, Berlin, gegründet 1901 (sinngemäß); Abruf 2026-10-20.
- https://www.mikrocontroller.net/topic/492449, Suchsnippet (S, Forum, nur Zusatzsignal): ROKA liefert hauptsächlich Industriekunden (sinngemäß); Abruf 2026-10-20.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag ROKA/Karst); WebSearch "ROKA Robert Karst Elektrotechnische Fabrik Berlin Produkte Fertigung" und "roka-berlin.de ROKA ... Antennensteckverbinder Hersteller Berlin Produktion" (keine Anlagen-/Materialnamen). Messe-Signal: bdtronic, ELANTAS, RAMPF, Momentive auf der electronica.
17. Identität: Abweichung zur Vorgabe. Eingabe: 12277 Berlin; Verzeichnis (S): Gneisenaustraße 27, 10961 Berlin (möglicherweise alte Adresse oder anderer Standort). Firmierung "Robert Karst GmbH & Co. KG Elektrotechnische Fabrik" stimmt. Eine historische Anzeige von 1955 gehört laut Suchzusammenfassung zu einem anderen Unternehmen (Oskar Vierling, Ebermannstadt) und wird nicht vermischt. Impressum/Register nicht gelesen.

## nicht aufgenommen (bereits bekannt / unklar)
Keine Firma bekannt (BEKANNT) und keine als "unklar" nach B2 eingestuft. Hinweis: crm_abgleich.py meldete für den Konzernbegriff "Richardson" (Prüfung zu Firma 2, RFMW) den PRÄFIX-Treffer "Richardson RFPD Germany GmbH [DE]" (bekannte_firmen_DE-AT-NL.txt Z. 1975). Er wurde nicht als dieselbe Einheit gewertet, weil kein Beleg für eine Konzernbeziehung zwischen RFMW und Richardson vorliegt; Tina/Jey bei Bedarf bestätigen.

## Einschränkungen
- WebFetch und Chrome nicht verfügbar: Keine einzige Quelle wurde selbst gelesen. Alle Aussagen zu Produkt, Standort, Register, Größe sind Stufe S (WebSearch-Zusammenfassungen und Snippets) oder A/?. Es gibt in diesem Batch keine Stufe V und damit keine mailtaugliche Aussage; Zitate in Feld 14 sind sinngemäße Wiedergaben der Suchzusammenfassung, keine wörtlichen Seitenzitate. Tina muss die Quellen im Browser öffnen.
- Patentrecherche (F5) NICHT regelkonform: Google Patents und Espacenet/DEPATISnet konnten nur über WebSearch-Suchbegriffe (site:patents.google.com), nicht über Anmelderfilter oder Direktabfrage erreicht werden. Pro Firma wurde nur eine WebSearch-Patentsuche ausgeführt, für Renu und Röchling zwei. Espacenet und DEPATISnet wurden nirgends direkt abgefragt. Der batch_check.py-Test auf zwei genannte Datenbanken ist damit formal erfüllt, inhaltlich ist der Batch bei Feld 9 UNVOLLSTÄNDIG im Sinne von F5. "Keine Treffer" ist kein Gegenbeweis; die WebSearch-Treffer zeigten fast nur Patente anderer Anmelder. Patentstatus (erteilt/erloschen) konnte nirgends geprüft werden, da kein relevantes Patent einer der Firmen auftauchte.
- WebSearch-Budget (ca. 30 Abfragen): Wettbewerbersuche (F6) nur für Renu, RG, ROB, Röchling und ROKA eigens ausgeführt; für RFMW, RIGOL, RIKEN KEIKI, RIKUTEC und RM Components nur Abgleich mit wettbewerber_referenzen.md (keine Treffer), weil Distributor/Vertriebstochter/Verpackung. Die Datei wettbewerber_referenzen.md führt keine dieser zehn Firmen; "kein Hinweis" ist nie ein Gegenbeweis.
- CRM-Abgleich: Skript mit Firmen-, Konzern- und Altnamen ausgeführt. Nicht übergeben: Phoenix Contact und Sütron (Renu-Vorgänger), Taiyo Yuden (Lieferant RM Components). Für ROB (Kern-Name "rob" sehr kurz) wurde kein zusätzliches manuelles Grep ausgeführt.
- Identität: Keine Impressums-/Registerseite gelesen. Abweichungen zur Eingabe: ROKA (PLZ 12277 laut Messe, Verzeichnis 10961), RIGOL (Firmierung "RIGOL EU"/"RIGOL Technologies GmbH" statt "RIGOL Technologies EU GmbH"), RIKEN KEIKI (Eingabe ohne Rechtsform, Verzeichnis "RIKEN KEIKI GmbH"), RIKUTEC (Eingabe ohne Halle/Stand).
- Produkt-zu-Werk-Zuordnung ist bei Renu, ROB, Röchling und ROKA offen. Alle Verguss-Einstufungen beruhen auf Produkttyp (A) oder Annahme (?), nicht auf Belegen zu Eigenverguss.
- Keine Kontakte gesucht (Abschnitt K). Nicht committet.
