# Tom Batch 58 – electronica 2026 (Export-Stand 03.07.2026)
Erstellt: 2026-10-21 (Tom, Stufe 1, Version 2, Messemodus Regel N). Eingabe: electronica/batches_v2/pruef_58.md, 10 Firmen (Nr. 649 bis 659, Nr. 653 fehlt in der Eingabe). Die Ersteinschätzung der Eingabe wurde nicht übernommen.
Abrufdatum aller Quellen: 2026-10-21. Belegstufen: V = selbst gelesen, S = nur Suchtext/Kurzfassung (Seite nachlesen), A = aus Produkttyp abgeleitet, ? = angenommen.
WICHTIG zu den Stufen: WebFetch war NICHT nutzbar (DNS-Fehler, curl über Proxy 403), Chrome-Werkzeuge standen nicht zur Verfügung. Es gibt in diesem Batch KEINE Stufe-V-Aussage. Alle Quellenangaben stammen aus WebSearch-Ergebnistexten (Stufe S, Zitate sind Wortlaut aus diesen Ergebnistexten, nicht von der Originalseite gelesen) und sind nicht mailtauglich.
BATCH UNVOLLSTÄNDIG (Feld 9): Das WebSearch-Budget der Session (200 Aufrufe je Turn, von allen Agenten geteilt) war aufgebraucht, bevor die Patentrecherche begann. Für KEINE der zehn Firmen wurde eine Patentsuche (Google Patents, Espacenet, DEPATISnet) ausgeführt. Feld 9 benennt das ehrlich als fehlend. Die Suche muss nachgeholt werden (Nachfolgelauf mit neuem Budget oder erhöhtem CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION). Ein bestandener batch_check.py darf hier nicht als vollständige Patentrecherche gelesen werden.
Ebenfalls fehlend wegen des Budgets: gezielte Wettbewerber-Einzelsuche (Feld 16); dort gilt nur der Abgleich mit wettbewerber_referenzen.md (Grep, keine Treffer für alle zehn Firmen und die genannten Konzerne).
Messe-Signal (Regel N2): Grep auf electronica/aussteller_namen.txt (2026-10-21) findet Wettbewerber/Materialhersteller nach Regel E1 unter den Ausstellern: bdtronic GmbH, ELANTAS Europe GmbH, RAMPF Advanced Polymers GmbH & Co. KG, RAMPF Production Systems GmbH & Co. KG; zusätzlich Nordson TEST&INSPECTION - Matrix Technologies GmbH (Prüftechnik) und Momentive Performance Materials GmbH (Silikone). Der Hinweis ändert nichts an der Ampel und ist keiner der zehn Firmen zugeordnet.

## 1. TT Electronics
1. Firma: TT Electronics (Messe electronica 2026, Halle/Stand C3.124); rechtliche Einheit laut Registertreffern: TT Electronics GmbH
2. Segment / Demak-Geschäftsbereich: Konzern mit Sensorik, Magnetics (Induktivitäten), Widerständen; Electrical Insulation / E-Mobility Potting wären nur bei Fertigung in DE/AT/NL relevant. Landshut selbst: Vertrieb (S).
3. Gebiet: Bayern (Landshut)
4. Sitz und Fertigungsort: Sitz TT Electronics GmbH, Ergoldinger Str. 2b, 84030 Landshut, Amtsgericht Landshut HRB 10931 (S, Ergebnistext Creditreform/North Data). Der Ergebnistext nennt als Geschäftsgegenstand "wholesale of electronic components". Konzern TT Electronics plc, London. Konzern-Fertigung laut Mouser-Profil in UK, Nordamerika, Schweden, Asien, Deutschland nicht genannt (S). Ein Dresdner Sensorwerk ist nur aus einer Börsenmeldung von 2006 bekannt (S, veraltet, Lehre 17). Fertigende Einheit in DE/AT/NL: nicht belegt.
5. Website: nicht gelesen. Verzeichnisprofil: https://exhibitors.electronica.de/exhibitor-portal/2024/list-of-exhibitors/exhibitordetails/tt-electronics/?elb=807.1100.4910.1.111
6. Was wird gebaut: Konzernsortiment passive Bauteile (magnetische und elektrokeramische Produkte, Widerstände, SMD-Induktivitäten) und Sensoren (S, Ergebnistexte electronica-Profil und Lieferantenprofil). Typisch vergossen/verklebt (A, Block A): Induktivitäten/Spulen und Sensoren sind Produkttypen, die praktisch immer vergossen werden. Wo das in DE/AT/NL geschieht, ist nicht belegt.
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Landshut als Großhandel/Vertrieb beschrieben, Konzern ohne belegtes Werk in DE/AT/NL (Konzern mit mehreren Werken, V nötig, fehlt). Offen, nicht widerlegt.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (nur Produkttyp, nicht der Standort). Einzelbewertung: Magnetics/Induktivitäten Hoch (A), Sensoren Hoch (A), Widerstände Niedrig (A). Die Bewertung gilt für den Konzern, nicht für Landshut.
9. Patentrecherche (Pflicht): NICHT AUSGEFÜHRT. Google Patents: nicht gesucht (WebSearch-Budget erschöpft). Espacenet: nicht gesucht. DEPATISnet: nicht gesucht. Anmelder-Varianten für den Nachlauf: TT Electronics plc, TT Electronics GmbH, TT Electronics Integrated Manufacturing Services, Optek Technology, BI Technologies, Welwyn Components, Stichwörter Verguss/potting/encapsulation. Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: unwahrscheinlich (Fertigung DE/AT/NL Niedrig, Stufe S; Konzern-Verguss Hoch nur Stufe A)
11. Ampel:
12. CRM-Status: unklar, CRM-Konzernbezug möglich. crm_abgleich.py "TT Electronics" "TT Group" "Transducers Tomorrow" "BI Technologies" "Optek" "Welwyn": Optek IDENTISCH mit bekannte_firmen_DE-AT-NL.txt Zeile 1761 "OPTEK" [DE]; laut Ergebnistext gehört Optek Technology (Plano, Texas) zum TT-Konzern, ob die CRM-Einheit dieselbe ist, ist offen. Weitere Treffer "TT Electronics" nur Ähnlichkeit 0.89 bis 0.90 zu rtg electronics GmbH, TDK Electronics AG, TR-Electronic GmbH (andere Firmen, kein Bezug). Regel M: Gelb-Auftrag "ist OPTEK im CRM die TT-Tochter?" an Tina.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Welche Einheit steht als OPTEK [DE] im CRM (kundendatenbank/CRM-Eintrag lesen) und gehört sie zum TT-Konzern? (b) Fertigt TT Electronics in DE/AT/NL (Standortliste ttelectronics.com, Impressum der GmbH Landshut, Stellenanzeigen)? (c) Patentsuche nachholen. Aktion: nicht kontaktieren.
14. Quellen:
- https://firmeneintrag.creditreform.de/84030/8350030785/TT_ELECTRONICS_GMBH (S, Ergebnistext): "TT Electronics GmbH, Landshut"; Abruf 2026-10-21.
- https://www.northdata.com/TT+Electronics+GmbH,+Landshut/HRB+10931 (S, Ergebnistext): "District Court of Landshut HRB 10931"; Abruf 2026-10-21.
- https://www.mouser.com/manufacturer/tt-electronics/ (S, Ergebnistext): "design and manufacturing facilities in the UK, North America, Sweden"; Abruf 2026-10-21.
15. Größe/Umsatz: Konzern 2025 Umsatz 481,4 Mio. GBP (S, Ergebnistext Börsenzusammenfassung, eine Quelle); Landshut unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep auf TT Electronics, Optek, Landshut: kein Eintrag); Web-Einzelsuche nicht ausgeführt (Budget). Messe-Signal: ELANTAS, RAMPF, bdtronic auf der electronica, ohne Bezug.
17. Identität: Name "TT Electronics" passt zu TT Electronics GmbH, Ergoldinger Str. 2b, 84030 Landshut (PLZ passt zur Messeliste), HRB 10931 Amtsgericht Landshut (S). Impressum nicht gelesen. Ältere Anschriften Werne und Freising laut Ergebnistext. Gleichnamig: Konzernmutter TT Electronics plc (London), andere Rechtsform.

## 2. TTI Inc.
1. Firma: TTI  Inc. (Messe electronica 2026, Halle/Stand C3.578)
2. Segment / Demak-Geschäftsbereich: keiner; Bauteil-Distributor
3. Gebiet: Bayern (Maisach-Gernlinden)
4. Sitz und Fertigungsort: Europa-Zentrale Ganghoferstr. 34, 82216 Maisach-Gernlinden (S, Pressemeldungen 2013 bis 2015); Logistikerweiterung laut Fachmeldung April 2026 (S). Fertigung: keine, Lager/Logistik.
5. Website: nicht gelesen (Verzeichnis: https://www.ttieurope.com/)
6. Was wird gebaut: nichts; "specialist distributor of passive, connector, electromechanical, discrete, power and sensor components" (S). Gehört zu Berkshire Hathaway. Typisch vergossene Teile: keine eigenen (A, Block C Handel ohne Fertigung).
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Distributor mit Logistikzentrum, keine Fertigung beschrieben.
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A. Einzelbewertung: gehandelte Bauteile Niedrig (A, kein Eigenverguss), Logistik Niedrig (A).
9. Patentrecherche (Pflicht): NICHT AUSGEFÜHRT. Google Patents: nicht gesucht (WebSearch-Budget erschöpft). Espacenet: nicht gesucht. DEPATISnet: nicht gesucht. Anmelder-Varianten für den Nachlauf: TTI Inc., TTI Europe, TTI Electronics. Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: kein Fertiger (Distributor; möglicher Ausschluss E2, Tina entscheidet)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "TTI Inc" "TTI" "Berkshire Hathaway": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Keine inhaltliche Nachrecherche nötig, falls Tina E2 mit Impressum bestätigt (ttieurope.com Impressum lesen). Patentsuche nachholen. Aktion: nicht weiter verfolgen.
14. Quellen:
- https://www.ttieurope.com/content/dam/Press-Releases/Europe/PDF/TTI_wins_Honeywell_DOTY_2013.pdf (S, Ergebnistext): "Ganghoferstr. 34, 82216 Maisach-Gernlinden"; Abruf 2026-10-21.
- https://logistik-online.ch/tag/tti-inc/ (S, Ergebnistext, Stand 14.04.2026): "expanding its European headquarters in Maisach-Gernlinden"; Abruf 2026-10-21.
15. Größe/Umsatz: ca. 8.800 Mitarbeiter weltweit (S, eine Quelle, Logistikmeldung April 2026); Umsatz unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep TTI, Berkshire: kein Eintrag); Web-Einzelsuche nicht ausgeführt (Budget, Distributor ohne Fertigung). Messe-Signal: ELANTAS, RAMPF, bdtronic auf der electronica, ohne Bezug.
17. Identität: Messename "TTI  Inc." (US-Muttergesellschaft, Fort Worth) vs. deutsche Niederlassung in Maisach-Gernlinden; die Rechtsform der deutschen Einheit (Niederlassung oder GmbH) ist nicht belegt. Adresse Maisach-Gernlinden passt zur Messeliste (PLZ 82216). Register/Impressum nicht gelesen.

## 3. TTL Network GmbH
1. Firma: TTL Network GmbH (Messe electronica 2026, Halle/Stand B3.418)
2. Segment / Demak-Geschäftsbereich: Kabel und Schnittstellenkabel; Randfall Electrical Insulation (Kabelkonfektion), nur wenn in DE/AT/NL gefertigt
3. Gebiet: Rest Deutschland+Niederlande (Halle/Westf., NRW)
4. Sitz und Fertigungsort: Sitz Weststraße 87, 33790 Halle (Westf.) (S, Ergebnistext); Messe-Frankfurt-Eintrag nennt Neulehenstraße 8c, 33790 Halle (Westf.) (Abweichung, S). Fertigung laut Ergebnistext: "certified production facilities are in Asia and Eastern Europe"; Engineering, Kundenservice, Projektmanagement in Halle (S). Fertigende Einheit außerhalb DE/AT/NL.
5. Website: nicht gelesen (Verzeichnis: https://ttl-network.de/en/)
6. Was wird gebaut: kundenspezifische Spezialkabel und Standard-Schnittstellenkabel (Linien TTL Lab, TTL Live, TTL Lan, TTL Link); Branchen Automation, Automotive, Medizintechnik, Maschinenbau, Telekommunikation (S). Typisch vergossen/überspritzt (A, Block A): Kabelkonfektion mit überspritzten oder vergossenen Steckern, aber nach Quelle im Ausland gefertigt.
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Ergebnistext nennt Produktion in Asien und Osteuropa (Hinweis auf Fertigung im Ausland, harter Ausschluss E3 möglich, V nötig); in Halle nur Engineering und Projektmanagement.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Produkttyp). Einzelbewertung: konfektionierte Kabel mit Steckern Hoch (A), Spezialkabel Mittel (A). Gilt nur, wenn die Fertigung doch in DE/AT/NL läge.
9. Patentrecherche (Pflicht): NICHT AUSGEFÜHRT. Google Patents: nicht gesucht (WebSearch-Budget erschöpft). Espacenet: nicht gesucht. DEPATISnet: nicht gesucht. Anmelder-Variante für den Nachlauf: TTL Network GmbH, Stichwörter Kabel/Stecker/Verguss/overmolding. Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: unwahrscheinlich (Fertigung DE/AT/NL Niedrig, Stufe S; mögliche Montage in Halle nicht belegt)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "TTL Network" "TTL": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Wird in Halle (Westf.) etwas montiert, konfektioniert oder vergossen? Firmenseite "Über uns"/Produktion, Broschüre (ttl-network.de/wp-content/uploads/2025/02/TTLNetwork_Brochure_ENG.pdf) und Stellenanzeigen lesen. (b) Adressabweichung Weststraße 87 / Neulehenstraße 8c im Impressum klären. (c) Patentsuche nachholen. Aktion: nicht kontaktieren.
14. Quellen:
- https://ttl-network.de/en/?p=23160 (S, Ergebnistext): "certified production facilities are in Asia and Eastern Europe"; Abruf 2026-10-21.
- https://www.wirtschaftsforum.de/ttl-network-gmbh (S, Sekundärquelle): "Weststraße 87, 33790 Halle"; Abruf 2026-10-21.
- https://pls.messefrankfurt.com/frankfurt/de/ausstellersuche.detail.html/ttl-network-gmbh.html (S, Ausstellerprofil, nach Regel N5 nie V): "Neulehenstraße 8c33790 Halle (Westf.)Deutschland"; Abruf 2026-10-21.
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep TTL: kein Eintrag); Web-Einzelsuche nicht ausgeführt (Budget). Messe-Signal: ELANTAS, RAMPF, bdtronic auf der electronica, ohne Bezug.
17. Identität: Name, Ort und PLZ 33790 passen zur Messeliste (S). Straßenabweichung zwischen Messeprofil (Neulehenstraße 8c) und Firmenverzeichnissen (Weststraße 87). Familienunternehmen, gegründet 2001 laut Ergebnistext. Rechtsform GmbH, Register/Impressum nicht gelesen.

## 4. TÜV SÜD Product Service GmbH
1. Firma: TÜV SÜD Product Service GmbH (Messe electronica 2026, Halle/Stand C1.540)
2. Segment / Demak-Geschäftsbereich: keiner; Prüf- und Zertifizierungsdienstleister
3. Gebiet: Bayern (München)
4. Sitz und Fertigungsort: Ridlerstraße 65, 80339 München, Amtsgericht München HRB 85742 (S, Ergebnistext Impressum). Fertigung: keine, Dienstleistung.
5. Website: nicht gelesen (Verzeichnis: https://www.tuvsud.com/de-de/ueber-uns/unsere-gesellschaften/product-service)
6. Was wird gebaut: nichts; Produktprüfung und Zertifizierung, Benannte Stelle ("Notified Body"), NRTL, CB-Scheme (S). Typisch vergossene Teile: keine (A, Block C Dienstleistung).
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Prüfdienstleister ohne Produktfertigung.
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A. Einzelbewertung: Prüfleistung Niedrig (A); geprüfte Kundenprodukte sind nicht Produkte der Firma.
9. Patentrecherche (Pflicht): NICHT AUSGEFÜHRT. Google Patents: nicht gesucht (WebSearch-Budget erschöpft). Espacenet: nicht gesucht. DEPATISnet: nicht gesucht. Anmelder-Varianten für den Nachlauf: TÜV SÜD Product Service GmbH, TÜV SÜD AG. Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: kein Fertiger (Prüfdienstleister; Ausschluss E2 Dienstleister, Tina entscheidet)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "TÜV SÜD Product Service" "TÜV SÜD" "TUV SUD": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Keine inhaltliche Nachrecherche nötig; Impressum im Browser bestätigen (E2). Patentsuche nachholen. Aktion: nicht weiter verfolgen.
14. Quellen:
- https://www.tuvsud.com/de-de/ueber-uns/unsere-gesellschaften/product-service/impressum (S, Ergebnistext): "Ridlerstraße 65, 80339 München"; Abruf 2026-10-21.
- https://www.tuvsud.com/de-de/ueber-uns/unsere-gesellschaften/product-service (S, Ergebnistext): "Notified Body für alle relevanten EU-Richtlinien"; Abruf 2026-10-21.
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep TÜV: kein Eintrag); Web-Einzelsuche nicht ausgeführt (Dienstleister ohne Fertigung, Budget). Messe-Signal: ELANTAS, RAMPF, bdtronic auf der electronica, ohne Bezug.
17. Identität: Name, Rechtsform GmbH und Sitz München passen zur Messeliste (PLZ 80339), Register HRB 85742 laut Impressum-Ergebnistext (S, Seite nicht gelesen). Gleichnamige Gruppengesellschaften (TÜV SÜD AG) nicht vermischt.

## 5. UL International Germany GmbH
1. Firma: UL International Germany GmbH (Messe electronica 2026, Halle/Stand C2.643)
2. Segment / Demak-Geschäftsbereich: keiner; Prüf- und Zertifizierungsdienstleister (Ersteinschätzung "Software / IT-Dienstleistung" nicht bestätigt)
3. Gebiet: Rest Deutschland+Niederlande (Neu-Isenburg, Hessen)
4. Sitz und Fertigungsort: Neu-Isenburg bei Frankfurt (S, Ergebnistext); Prüflabore in Neu-Isenburg (EV-Ladeinfrastruktur, EMV-Neubau ab Baustart April 2026) und Rosenheim (Brandprüfung) (S). Straße und Register nicht ermittelt. Fertigung: keine.
5. Website: nicht gelesen (Verzeichnis: https://www.ul.com/de/news/werkzeuge-dakks-erweiterung-und-gs-akkreditierung)
6. Was wird gebaut: nichts; Produktsicherheits-Prüfung, Zertifizierung (GS, ENEC, CB), EMV/Funk, Ladeinfrastruktur-Tests, Brandprüfungen (S). Typisch vergossene Teile: keine (A, Block C Dienstleistung).
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Prüfdienstleister, Labore statt Produktion.
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A. Einzelbewertung: Prüfleistung Niedrig (A).
9. Patentrecherche (Pflicht): NICHT AUSGEFÜHRT. Google Patents: nicht gesucht (WebSearch-Budget erschöpft). Espacenet: nicht gesucht. DEPATISnet: nicht gesucht. Anmelder-Varianten für den Nachlauf: UL International Germany GmbH, UL LLC, Underwriters Laboratories, UL Solutions. Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: kein Fertiger (Prüfdienstleister; Ausschluss E2 Dienstleister, Tina entscheidet)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "UL International Germany" "UL Solutions" "Underwriters Laboratories" "UL": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Impressum (Straße, Register) lesen und E2 bestätigen. Patentsuche nachholen. Aktion: nicht weiter verfolgen.
14. Quellen:
- https://www.ul.com/de/news/werkzeuge-dakks-erweiterung-und-gs-akkreditierung (S, Ergebnistext): "DAkkS" und "GS" Akkreditierung, Bezug Neu-Isenburg; Abruf 2026-10-21.
- https://www.ul.com/de/news/ul-solutions-beginnt-mit-dem-bau-eines-neuen-labors-fuer-elektromagnetische-und-drahtlose (S, Ergebnistext): "neuen Labors für elektromagnetische und drahtlose"; Abruf 2026-10-21.
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep UL Solutions: kein Eintrag); Web-Einzelsuche nicht ausgeführt (Dienstleister ohne Fertigung, Budget). Messe-Signal: ELANTAS, RAMPF, bdtronic auf der electronica, ohne Bezug.
17. Identität: Name UL International Germany GmbH, Neu-Isenburg (PLZ 63263 laut Messeliste) passt zur Meldung "UL International Germany GmbH is UL's German subsidiary in Neu-Isenburg" (S, Ergebnistext). Straße, Rechtsform-Beleg und Register nicht gelesen.

## 6. ULVAC GmbH
1. Firma: ULVAC GmbH (Messe electronica 2026, Halle/Stand B1.606)
2. Segment / Demak-Geschäftsbereich: keiner; Vakuumtechnik (Anlagenbau), Vertriebs-/Service-Tochter
3. Gebiet: Bayern (Kirchheim b. München)
4. Sitz und Fertigungsort: Klausnerring 4, 85551 Kirchheim bei München (S, Chillventa-Ausstellerprofil und ULVAC-Gruppenverzeichnis). Verzeichnisse beschreiben die Einheit hauptsächlich als Vertriebs-, Service- und Support-Tochter von ULVAC Japan (Chigasaki); der Geschäftsführer nennt laut Interview Pläne für lokale Produktionsstandorte (S). Fertigung in DE: nicht belegt.
5. Website: nicht gelesen (Verzeichnis: https://www.wirtschaftsforum.de/ulvac-gmbh)
6. Was wird gebaut: Vakuumpumpen, Vakuum- und Beschichtungsanlagen der Gruppe, in Kirchheim Vertrieb/Service (S). Typisch vergossen/verklebt (A, Block C): Maschinenbau/Anlagen; Steuerelektronik der Anlagen enthält zugekaufte vergossene Teile, aber der Anlagenbau selbst ist kein typischer Vergussfall.
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: als Vertriebs-/Servicegesellschaft beschrieben; geplante Produktion nur Ankündigung (Interview, Datum nicht ermittelt).
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A. Einzelbewertung: Vakuumanlagen Niedrig (A), Steuerelektronik der Anlagen Mittel (A, Endprodukt-Regel, aber nicht am Standort gefertigt belegt). Höchstes Bauteil Mittel nur bei Fertigung am Standort, die nicht belegt ist.
9. Patentrecherche (Pflicht): NICHT AUSGEFÜHRT. Google Patents: nicht gesucht (WebSearch-Budget erschöpft). Espacenet: nicht gesucht. DEPATISnet: nicht gesucht. Anmelder-Varianten für den Nachlauf: ULVAC GmbH, ULVAC Inc., ULVAC Technologies, Stichwörter Vakuum, Verguss, potting. Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: unwahrscheinlich (Fertigung DE Niedrig S, Verguss Niedrig A; Konzern ULVAC Inc. Maschinenbauer)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "ULVAC" "ULVAC Technologies": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Wird in Kirchheim montiert oder gefertigt? Firmenseite ulvac.de und Impressum lesen. (b) Datum der Produktionspläne klären (Wirtschaftsforum-Interview). (c) Patentsuche nachholen. Aktion: nicht kontaktieren.
14. Quellen:
- https://www.chillventa.de/en/exhibitors/ulvac-gmbh-2555840 (S, Ergebnistext, Ausstellerprofil nach N5 nie V): "Klausnerring 4, 85551 Kirchheim bei München"; Abruf 2026-10-21.
- https://www.wirtschaftsforum.de/ulvac-gmbh/innovation-im-vakuum (S, Sekundärquelle): "local production sites as well as research and development centres"; Abruf 2026-10-21.
15. Größe/Umsatz: unbekannt (Verzeichnisangaben zu Mitarbeitern und Gründungsjahr widersprüchlich).
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep ULVAC: kein Eintrag); Web-Einzelsuche nicht ausgeführt (Budget). Messe-Signal: ELANTAS, RAMPF, bdtronic auf der electronica, ohne Bezug.
17. Identität: Name ULVAC GmbH, Kirchheim b. München (PLZ 85551 passt zur Messeliste), Geschäftsführer laut Bayern International: Christopher C. Goebel (S). Register/Impressum nicht gelesen. Muttergesellschaft ULVAC Inc., Chigasaki (Japan), andere Einheit.

## 7. Unisolution GmbH
1. Firma: Unisolution GmbH (Messe electronica 2026, Halle/Stand C4.300)
2. Segment / Demak-Geschäftsbereich: nicht ermittelt (Tätigkeit nicht belegt)
3. Gebiet: Bayern (Hohenbrunn)
4. Sitz und Fertigungsort: Lise-Meitner-Str. 1, 85662 Hohenbrunn (S, Ergebnistext des Firmen-Impressums); Amtsgericht München HRB 250352; Sitzverlegung von Brunnthal nach Hohenbrunn laut Gesellschafterbeschluss vom 25.01.2022 (S, Registerbekanntmachung im Ergebnistext). Fertigungsort nicht belegt.
5. Website: unisolution-gmbh.de (Impressums-Link aus Ergebnistext, Seite nicht gelesen): https://unisolution-gmbh.de/en/imprint/
6. Was wird gebaut: nicht ermittelt. Die Suchergebnisse enthielten nur Register- und Verzeichnisdaten (GmbH, Stammkapital 25.000 EUR, ein Geschäftsführer, Mike Sigrist, Gründung 2019), keine Produkt- oder Tätigkeitsangabe. Typisch vergossene Teile: keine ableitbar (?).
7. Fertigung DE/AT/NL: Niedrig, Stufe ?. Begründung: weder Produkt noch Fertigung belegt; Niedrig heißt hier "nicht belegt", nicht "widerlegt".
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe ?. Keine Bauteile bekannt.
9. Patentrecherche (Pflicht): NICHT AUSGEFÜHRT. Google Patents: nicht gesucht (WebSearch-Budget erschöpft). Espacenet: nicht gesucht. DEPATISnet: nicht gesucht. Anmelder für den Nachlauf: Unisolution GmbH (gleichnamige Firmen aussortieren, z. B. Unified Solution GmbH Wiesbaden, UNISERV GmbH, die in den Suchtreffern als Namensähnliche auftauchten und nicht dieselbe Firma sind). Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: kein Fertiger (vorläufig, Tätigkeit nicht belegt, daher keine belastbare Einstufung; Tina entscheidet)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "Unisolution" "Uni Solution": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Was tut Unisolution GmbH (Startseite und Impressum unisolution-gmbh.de im Browser lesen, Messeprofil electronica Produktgruppe)? Fertigung vorhanden? Aktion: nicht kontaktieren, bis Tätigkeit geklärt.
14. Quellen:
- https://unisolution-gmbh.de/en/imprint/ (S, Ergebnistext): "Lise-Meitner-Str. 1 85662 Hohenbrunn"; Abruf 2026-10-21.
- https://www.online-handelsregister.de/handelsregisterauszug/by/Muenchen/HRB/250352/Unisolution-GmbH (S, Ergebnistext): "Hohenbrunn (HRB 250352)"; Abruf 2026-10-21.
- https://www.northdata.com/Unisolution+GmbH,+Hohenbrunn/Amtsgericht+M%C3%BCnchen+HRB+250352 (S, Ergebnistext): "Unisolution GmbH, Hohenbrunn, Germany"; Abruf 2026-10-21.
15. Größe/Umsatz: Stammkapital 25.000 EUR (S, Implisense-Ergebnistext, eine Quelle); Mitarbeiter und Umsatz unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep Unisolution: kein Eintrag); keine Tätigkeit ermittelt, daher keine gezielte Wettbewerbersuche möglich. Messe-Signal: ELANTAS, RAMPF, bdtronic auf der electronica, ohne Bezug.
17. Identität: Name, Rechtsform GmbH, Adresse Hohenbrunn (PLZ 85662 passt zur Messeliste) und Register HRB 250352 Amtsgericht München stimmen in mehreren Verzeichnisquellen überein (S, Impressum nicht gelesen). Gründungsdatum widersprüchlich (17., 18., 25. Juli 2019). Gleichnamig-ähnliche Firmen (Unified Solution GmbH Wiesbaden, UNISERV GmbH Pforzheim) sind andere Firmen und nicht vermischt.

## 8. UniTemp GmbH
1. Firma: UniTemp GmbH (Messe electronica 2026, Halle/Stand B1.156)
2. Segment / Demak-Geschäftsbereich: Thermoprozess-Anlagenbauer (Löt- und Temperaturanlagen); Randfall Electrical Insulation über Heizelemente und Elektronik der Geräte. Kein klarer Demak-Bereich (Ersteinschätzung "nicht eindeutig" ersetzt).
3. Gebiet: Bayern (Pfaffenhofen a. d. Ilm)
4. Sitz und Fertigungsort: Luitpoldstraße 6, 85276 Pfaffenhofen (S, Bayern-International-Datenbank, Ergebnistext). Hersteller mit einem Standort, gegründet 2000, ca. 18 Mitarbeiter (S). Fertigung am Sitz nicht gelesen, aber Sitzregel (kleiner Gerätebauer, eigene Produkte, ein Standort, keine Hinweise auf Auslagerung).
5. Website: nicht ermittelt (Verzeichnis: https://bayern-international.de/en/company-database/company-details/unitemp-gmbh-7764)
6. Was wird gebaut: Rapid-Thermal-Annealing-Anlagen, Reflow-Lötöfen, Präzisions-Heizplatten, vor allem für Labore und Kleinserien (S). Typisch vergossen/verklebt/gedichtet (A, Endprodukt-Regel): Heizelemente der Heizplatten, Temperatursensoren/Thermoelemente, Netzteile und Steuerelektronik der Anlagen; Vakuum-Prozesskammern mit Dichtungen. Nicht belegt, Ableitung aus dem Endprodukt.
7. Fertigung DE/AT/NL: Hoch, Stufe A (Sitzregel). Begründung: Gerätebauer mit erkennbarem Standort Pfaffenhofen, Verzeichnis führt ihn als Hersteller (S); eine V-Quelle (Firmenseite, Stellenanzeige) fehlt.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Heizelemente der Heizplatten Mittel (A), Sensorik/Thermoelemente Mittel (A), Steuerelektronik/Netzteile Mittel (A), Ofengehäuse/Kammer Niedrig (A). Löt-/Temperaturanlagen sind nach Block C kein typischer Vergussfall, daher nicht Hoch.
9. Patentrecherche (Pflicht): NICHT AUSGEFÜHRT. Google Patents: nicht gesucht (WebSearch-Budget erschöpft). Espacenet: nicht gesucht. DEPATISnet: nicht gesucht. Anmelder-Variante für den Nachlauf: UniTemp GmbH (Pfaffenhofen), Stichwörter rapid thermal annealing, Heizplatte, Verguss, potting. Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: prüfenswert (Fertigung Hoch A, Verguss Mittel A)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "UniTemp" "Uni Temp" "Unitemp": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Fertigung in Pfaffenhofen mit V-Quelle belegen (Firmenseite, Impressum, Stellenanzeigen). (b) Aufbau der Heizplatten/Öfen: Heizpatronen oder Heizfolien vergossen oder verklebt, Elektronik (Datenblätter lesen). (c) Patentsuche nachholen. Aktion: nicht kontaktieren.
14. Quellen:
- https://bayern-international.de/en/company-database/company-details/unitemp-gmbh-7764 (S, Ergebnistext): "Luitpoldstraße 6" in 85276 Pfaffenhofen, "rapid thermal annealing systems"; Abruf 2026-10-21.
15. Größe/Umsatz: ca. 18 Mitarbeiter, Umsatz unter 5 Mio. EUR (Verzeichnis, eine Quelle, S).
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep UniTemp: kein Eintrag); Web-Einzelsuche nicht ausgeführt (Budget). Messe-Signal: ELANTAS, RAMPF, bdtronic auf der electronica, ohne Bezug.
17. Identität: Name, Rechtsform GmbH und Ort Pfaffenhofen (PLZ 85276 passt zur Messeliste) stimmen mit dem Verzeichnis überein (S). Register/Impressum nicht gelesen. Namensgleiche Produktlinie "UniTemp" Temperatursensoren von wenglor ist ein Produktname einer anderen Firma und wurde nicht mit UniTemp GmbH vermischt.

## 9. UNI-TREND Technology EU GmbH
1. Firma: UNI-TREND Technology EU GmbH (Messe electronica 2026, Halle/Stand A4.361)
2. Segment / Demak-Geschäftsbereich: Messgeräte-Marke UNI-T (Multimeter, Oszilloskope u. ä.); kein klarer Demak-Bereich. Europäische Tochter eines chinesischen Herstellers.
3. Gebiet: Bayern (Augsburg)
4. Sitz und Fertigungsort: Steinerne Furt 62, 86167 Augsburg laut UNI-T-Filialseite (S, Ergebnistext); älterer Katalog 2023 nennt Affinger Str. 12, 86167 Augsburg (S). Die Filialseite führt die Einheit neben den Gesellschaften in China, Hongkong und USA (S). Fertigung in DE nicht belegt, Hersteller in China.
5. Website: nicht gelesen (Verzeichnis: https://instruments.uni-trend.com/branch)
6. Was wird gebaut: Elektronische Messgeräte der Marke UNI-T (S, Ergebnistexte, Produkte nicht im Detail gelesen). Typisch vergossen/verklebt (A, Endprodukt-Regel): Netzteile, Platinen, Sensoren in Messgeräten. Standort Augsburg: Vertriebs-/Europa-Gesellschaft (Annahme ?, nicht belegt).
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: EU-Tochter eines Herstellers mit Fertigung in China (Hinweis auf Fertigung im Ausland, V nötig); in Augsburg keine Produktion beschrieben.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Messgeräte-Elektronik Mittel (A, Endprodukt-Regel), Gehäuse/Zubehör Niedrig (A). Gilt nur, falls in DE/AT/NL gefertigt.
9. Patentrecherche (Pflicht): NICHT AUSGEFÜHRT. Google Patents: nicht gesucht (WebSearch-Budget erschöpft). Espacenet: nicht gesucht. DEPATISnet: nicht gesucht. Anmelder-Varianten für den Nachlauf: UNI-TREND Technology EU GmbH, Uni-Trend Technology (China) Co., Ltd., Uni-Trend Technology (Dongguan), Stichwörter Verguss/potting. Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: unwahrscheinlich (Fertigung DE/AT/NL Niedrig, Stufe S; Vertriebsgesellschaft vermutet, Tätigkeit nicht belegt)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "UNI-TREND Technology EU" "UNI-T" "Uni-Trend" "Uni Trend": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Impressum und Handelsregister (Augsburg) lesen: Tätigkeit der EU-GmbH (Vertrieb, Service, Montage?). (b) Wo werden UNI-T-Geräte gefertigt (Herstellerseite, Impressum)? (c) Patentsuche nachholen. Aktion: nicht kontaktieren.
14. Quellen:
- https://instruments.uni-trend.com/branch (S, Ergebnistext): "Steinerne Furt 62, 86167 Augsburg"; Abruf 2026-10-21.
- https://www.mecspe.com/portale/it/uni-trend-technology-eu-gmbh (S, Ausstellerprofil MECSPE, nach N5 nie V): "Uni-Trend Technology EU GmbH"; Abruf 2026-10-21.
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep UNI-T, Uni-Trend: kein Eintrag); Web-Einzelsuche nicht ausgeführt (Budget). Messe-Signal: ELANTAS, RAMPF, bdtronic auf der electronica, ohne Bezug.
17. Identität: Name passt zur Vorgabe, Ort Augsburg und PLZ 86167 passen zur Messeliste (S). Adressabweichung Steinerne Furt 62 (aktuell) / Affinger Str. 12 (älterer Katalog); ein MECSPE-Profil nennt zusätzlich München (widersprüchlich). Openregister-Suche lieferte keinen eindeutigen Treffer. Rechtsform GmbH, Register/Impressum nicht gelesen.

## 10. uwe electronic GmbH
1. Firma: uwe electronic GmbH (Messe electronica 2026, Halle/Stand A4.607)
2. Segment / Demak-Geschäftsbereich: nicht ermittelt (Ersteinschätzung "Steckverbinder / Kontakttechnik" nicht bestätigt)
3. Gebiet: Bayern (Unterhaching)
4. Sitz und Fertigungsort: Telefonbuch-Eintrag "uwe electronic Vertriebs GmbH", Inselkammerstr. 10, 82008 Unterhaching (S, Ergebnistext). Fertigungsort nicht belegt.
5. Website: nicht ermittelt
6. Was wird gebaut: nicht ermittelt. Die Suchergebnisse enthielten keine Produkt- oder Tätigkeitsangabe. Der Firmenname im Telefonbuch enthält "Vertriebs", das deutet auf Vertrieb hin (Annahme ?, nicht Fakt). Typisch vergossene Teile: keine ableitbar (?).
7. Fertigung DE/AT/NL: Niedrig, Stufe ?. Begründung: Tätigkeit nicht belegt; Niedrig heißt "nicht belegt", nicht "widerlegt".
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe ?. Keine Bauteile bekannt.
9. Patentrecherche (Pflicht): NICHT AUSGEFÜHRT. Google Patents: nicht gesucht (WebSearch-Budget erschöpft). Espacenet: nicht gesucht. DEPATISnet: nicht gesucht. Anmelder-Varianten für den Nachlauf: uwe electronic GmbH, uwe electronic Vertriebs GmbH. Batch für diese Firma UNVOLLSTÄNDIG.
10. Einstufung Tom: kein Fertiger (vorläufig, Tätigkeit nicht belegt; möglicher Ausschluss E2 Händler/Vertrieb, Tina entscheidet)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "uwe electronic" "uwe": kein Treffer; Ähnlichkeit 0.90 zu "RAWE Electronic GmbH" Zeile 1948 ist eine andere Firma, kein Bezug)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Identität und Tätigkeit klären: Ist "uwe electronic GmbH" dieselbe Firma wie "uwe electronic Vertriebs GmbH", Inselkammerstr. 10? Impressum/Startseite im Browser lesen, Handelsregister München, Messeprofil electronica (Produktgruppe). Fertigung in Unterhaching? Aktion: nicht weiter verfolgen, bis Identität und Tätigkeit geklärt sind.
14. Quellen:
- https://adresse.dastelefonbuch.de/Unterhaching/1-Elektronik-uwe-electronic-Vertriebs-GmbH-Unterhaching-Inselkammerstr.html (S, Ergebnistext): "uwe electronic Vertriebs GmbH" Inselkammerstr. 10, 82008 Unterhaching; Abruf 2026-10-21.
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep uwe: kein Eintrag); keine Firmenseite auffindbar, daher keine gezielte Wettbewerbersuche möglich. Messe-Signal: ELANTAS, RAMPF, bdtronic auf der electronica, ohne Bezug.
17. Identität: NICHT belegt. Nur ein Telefonbucheintrag unter dem Namen "uwe electronic Vertriebs GmbH" (andere Namensform als die Messeliste "uwe electronic GmbH"), PLZ 82008 passt zur Messeliste. Weder Impressum noch Register gefunden. Tina: Tabellenzeile 2 prüfen.

## nicht aufgenommen (bereits bekannt / unklar)
- TT Electronics: Konzernbezug unklar. CRM-Schreibweise "OPTEK" [DE] (bekannte_firmen_DE-AT-NL.txt Zeile 1761), gefundene Schreibweise "Optek Technology" (Tochter von TT Electronics laut Ergebnistext). Firma bleibt im Batch, Gelb-Auftrag in Feld 12/13.
- Keine der anderen neun Firmen ist im CRM (Skript: kein Treffer oder nur Ähnlichkeit zu fremden Firmen, siehe Feld 12).

## Einschränkungen
- WebFetch nicht nutzbar (DNS-Fehler), Direktzugriff per curl gesperrt (Proxy 403), Chrome-Werkzeuge nicht verfügbar: keine Stufe V, kein Browser-Gegenlesen.
- WebSearch-Budget (200 Aufrufe je Turn, geteilt) erschöpft nach den Identitäts- und Produktsuchen: Patentrecherche (Feld 9) für alle zehn Firmen NICHT ausgeführt, Wettbewerber-Einzelsuchen (Feld 16) NICHT ausgeführt. Batch UNVOLLSTÄNDIG, Nachlauf nötig, bevor er an Tina geht.
- Zitate in Feld 14 sind Wortlaut aus WebSearch-Ergebnistexten (teils zusammenfassend formuliert), nicht von der Originalseite; Tina muss sie vor Verwendung im Browser prüfen.
- Offene Identitäten: Unisolution (Tätigkeit unbekannt), uwe electronic (Namensform abweichend, Tätigkeit unbekannt), TTI Inc. (Rechtsform der deutschen Einheit), UNI-TREND (Adressabweichung).
