# Tom Batch 01 – agraria 2026 (Messe Wels 25.-28.11.2026)
Erstellt: 2026-11-24 (Tom, Stufe 1, Version 2, Messemodus Regel N). Eingabe: agraria-2026/batches_v2/pruef_01.md, 10 Firmen. Die Ersteinschätzung der Eingabe (CRM-Hinweis, Produkte der Messeliste) wurde nicht übernommen; Produkte der Messeliste sind Stufe S.
Abrufdatum aller Quellen: 2026-11-24. Belegstufen: V = selbst gelesen, S = nur Suchsnippet/Kurzfassung (Seite nachlesen), A = aus Produkttyp abgeleitet, ? = angenommen.
WICHTIG zu den Stufen: WebFetch und Chrome waren NICHT verfügbar, nur WebSearch. Es gibt in diesem Batch KEINE Stufe-V-Aussage. Alle Quellen sind WebSearch-Ergebnistexte (Stufe S), die wörtlichen Kurzzitate in Feld 14 stammen aus diesen Ergebnistexten und nicht aus selbst gelesenen Seiten; nicht mailtauglich. Keine einzige Impressum-/Registerseite wurde gelesen.
Patentrecherche: Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Je Firma wurden mindestens zwei WebSearch-Abfragen ausgeführt (site:patents.google.com bzw. Anmelder plus Stichwörter, Abfrage mit Espacenet/DEPATISnet-Bezug); diese indexieren die Datenbanken nur teilweise. "Keine Treffer" bedeutet "in WebSearch nicht gefunden" und ist KEIN Datenbankergebnis. Rechtsstand wurde nirgends geprüft.
Messe-Signal (Regel N2): Grep auf agraria-2026/agraria_2026_aussteller_DE-AT-NL.csv (333 Zeilen, 2026-11-24) nach Wettbewerbern/Materialherstellern aus Regel E1 (bdtronic, Elantas, RAMPF, Scheugenpflug, DOPAG, ViscoTec, Sonderhoff, Hilger u. Kern, Musashi, Nordson, Henkel, DELO, Wacker, Sika, GONANO, Marco, EPOXONIC, WEVO, Panacol, Lohmann, OTTO-CHEMIE, Hexion): kein Treffer. Kein Messe-Signal.
CRM-Abgleich: `python3 crm_abgleich.py` für jede Firma, zusätzlich mit Kurzform, Konzern- und Schreibvarianten (Lehre 13). Ergebnisse je Firma in Feld 12.
Entscheidungen von Jey berücksichtigt: Verbände/Prüfdienstleister/Forschung raus (keine im Batch); Firmen im CRM mit gleichem/sehr ähnlichem Namen raus (keine: einziger Wortwurzel-Treffer ADLER Elektrotechnik Leipzig ist eine andere Firma); Anlagenbauer bleiben drin (autarkize), keiner baut Verguss-/Dosieranlagen (E1).

## 1. Adler Arbeitsmaschinen GmbH
1. Firma: Adler Arbeitsmaschinen GmbH (Messe agraria 2026, Halle 20, Stand B10)
2. Segment / Demak-Geschäftsbereich: Kommunal-/Landtechnik (Anbau-Kehrmaschinen, Schneeräumgeräte, Streuer, Bohrgeräte). Kein klarer Demak-Bereich; Randfall Electrical Insulation (Steuerelektronik/Beleuchtung der Anbaugeräte), nur über Endprodukt-Regel.
3. Gebiet: Rest Deutschland+Niederlande (Nordwalde, Nordrhein-Westfalen; S)
4. Sitz und Fertigungsort: An den Bahngleisen 28, 48356 Nordwalde (S, Verzeichnisangabe). Rechtsform laut Verzeichnis GmbH & Co. KG (Messeliste: GmbH). Fertigungsort Nordwalde nicht belegt (nur "Made in Germany" und Herstellerprofil, S); fertigende Einheit vermutlich Nordwalde (A, Sitzregel).
5. Website: nicht ermittelt (Messeprofil: https://galabau-messe.com/en/exhibitors/adler-arbeitsmaschinen-gmbh-co-kg-2301434)
6. Was wird gebaut: Anbau-Kehrmaschinen (z. B. ADLER K 750), Anbau-Schneeräumgeräte, Streuer, Bohrgeräte (S, Verzeichnis). Typisch vergossen/verklebt/gedichtet: Steuer-/Bedienelektronik der Streuer, Arbeitsbeleuchtung (LED), Magnetventile/Hydraulikelektrik, Kabelkonfektion (A, Endprodukt-Regel; zugekaufte Teile zählen). Nichts davon belegt.
7. Fertigung DE/AT/NL: Hoch, Stufe A. Begründung: Sitzregel (Gerätebauer mit erkennbarem Standort, eigene Produkte, "Manufacturer", "Made in Germany" laut Verzeichnis/Messeprofil, S); kein Konzern, keine Hinweise auf Auslagerung. Stufe V nicht erreicht.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Streuer-Steuergerät Mittel (A), LED-Arbeitsscheinwerfer Mittel (A), Magnetventile/Hydraulik Mittel (A), Rahmen/Kehrwalze/Räumschild Niedrig (A). Elektronikanteil nicht belegt, Einschätzung aus Produkttyp.
9. Patentrecherche (Pflicht, mind. 2 Suchen): Google Patents über WebSearch: Abfrage `site:patents.google.com "Adler Arbeitsmaschinen" Anmelder`: keine Patente dieses Anmelders gefunden (nur historische Fremdpatente, z. B. DE242533C, andere Anmelder). Espacenet/DEPATISnet über WebSearch: Abfrage "Adler Arbeitsmaschinen Nordwalde Fertigung Produktion" ohne Patent-/Gebrauchsmustertreffer. Weder Google Patents noch Espacenet noch DEPATISnet direkt abgefragt, Rechtsstand n. a., Anmelder-Variante "ADLER Arbeitsmaschinen GmbH & Co. KG" nur über WebSearch. Ergebnis: 0 Treffer (WebSearch).
10. Einstufung Tom: prüfenswert (Fertigung Hoch, Verguss Mittel)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu. `crm_abgleich.py "Adler Arbeitsmaschinen GmbH"` und mit "ADLER Arbeitsmaschinen GmbH & Co. KG": nur Wortwurzel-Treffer bekannte_firmen_DE-AT-NL.txt:44 "ADLER Elektrotechnik Leipzig GmbH [DE]". Anderer Kern-Name (Arbeitsmaschinen vs. Elektrotechnik Leipzig), anderes Geschäft; Hinweis der Eingabe "ähnlicher Name" geprüft: keine gleiche Einheit, kein Konzernbezug belegt (Konzernzugehörigkeit nicht geprüft). Tina bitte bestätigen.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Impressum/Handelsregister: Rechtsform GmbH oder GmbH & Co. KG, Sitz Nordwalde, kein Bezug zu ADLER Elektrotechnik Leipzig. (b) Produktseiten/Datenblätter Streuer und Kehrmaschinen: Steuerelektronik, Beleuchtung, IP-Klasse; Fertigung Nordwalde (Stellenanzeigen Montage/Schweißer). Aktion: nicht kontaktieren.
14. Quellen:
- https://galabau-messe.com/en/exhibitors/adler-arbeitsmaschinen-gmbh-co-kg-2301434 (S, Messeprofil, nach Regel N5 nie V): "Made in Germany" (Ergebnistext); Abruf 2026-11-24.
- https://www.agriculture-xprt.com/companies/adler-arbeitsmaschinen-gmbh-co-kg-53280 (S, Verzeichnis): "ADLER Arbeitsmaschinen GmbH & Co. KG", Adresse "An den Bahngleisen 28"; Abruf 2026-11-24.
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep "adler": kein Eintrag für diese Firma); Websuche "Amazone OR BvL OR Bergmann Landtechnik Scheugenpflug OR Nordson OR Sonderhoff OR DOPAG OR Henkel Referenz Dosieranlage Verguss" (kein Treffer zu Adler); Websuche "Adler Arbeitsmaschinen Nordwalde Fertigung Produktion" (keine Wettbewerber). Messe-Signal: keiner.
17. Identität: Name weicht ab: Messeliste "Adler Arbeitsmaschinen GmbH", Verzeichnisse "ADLER Arbeitsmaschinen GmbH & Co. KG", Nordwalde (S). Impressum/Register nicht gelesen. Die Firmen "Adler" in Autohaus-/Kompressor-Treffern sind andere Firmen und wurden nicht vermischt.

## 2. AGRARMONITOR
1. Firma: AGRARMONITOR (Messe agraria 2026, Halle 17, Stand 190)
2. Segment / Demak-Geschäftsbereich: kein Demak-Bereich; Software/Beratung für Lohnunternehmer und Ackerbaubetriebe (Dokumentation, GPS-Tracking, Rechnungsstellung).
3. Gebiet: Rest Deutschland+Niederlande (Kalletal, Nordrhein-Westfalen; S, Partnerverzeichnis)
4. Sitz und Fertigungsort: Betreiberin laut Verzeichnissen betriko GmbH, Kohlbeet 2, 32689 Kalletal (S, Wolters-Kluwer-Partnerseite). AGRARMONITOR ist ein Produktname. Kein Fertigungsort (Software).
5. Website: https://www.agrarmonitor.de (aus Suchergebnis; nicht gelesen)
6. Was wird gebaut: Software zur Betriebs-/Auftragsdokumentation mit GPS-Tracking (S). Bauteile typisch vergossen: keine (reine Software; "GPS Geräte, Tracking" der Messeliste könnten zugekaufte Tracker sein, A/?, ohne Eigenfertigung belegt).
7. Fertigung DE/AT/NL: Niedrig, Stufe A. Begründung: Software-/Beratungsanbieter, keine Hardwarefertigung belegt.
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A. Einzelbewertung: Software Niedrig (A), zugekaufte GPS-Tracker Niedrig (?), nicht selbst gefertigt.
9. Patentrecherche (Pflicht, mind. 2 Suchen): Google Patents/Espacenet/DEPATISnet nicht direkt abfragbar, Ausführung über WebSearch. Abfrage 1 (Espacenet-Bezug): "betriko GmbH Kalletal Patent Anmelder espacenet": kein Patent von betriko GmbH gefunden (nur unbeteiligte Patentblatt-Auszüge des DPMA, Anmelder anderer Firmen; Implisense-Profil: Branche IT, Software und Maschinenentwicklung). Abfrage 2 (Firma/Produkt): "AGRARMONITOR Software Agrarmonitoring Impressum": keine Patentbezüge. Anmelder-Varianten "Betriko", "betriko GmbH", "AGRARMONITOR" nur über WebSearch; Rechtsstand n. a. Ergebnis: 0 Treffer (WebSearch).
10. Einstufung Tom: kein Fertiger (Software)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu. `crm_abgleich.py "AGRARMONITOR" "betriko GmbH"`: kein Treffer.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Impressum agrarmonitor.de lesen (betriko GmbH, Sitz, Register); Tina prüft Ausschluss E2 (Software/Beratung). Aktion: nicht weiter verfolgen.
14. Quellen:
- https://www.wolterskluwer.com/de-de/solutions/addison-komplettloesung-steuerberater/agrarmonitor (S, Partnerseite): "Partner: Betriko GmbH", "Kohlbeet 2, 32689 Kalletal" (Ergebnistext); Abruf 2026-11-24.
- https://omr.com/de/reviews/product/agrarmonitor (S, Verzeichnis): Produkt "AGRARMONITOR" (Software); Abruf 2026-11-24.
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep "agrarmonitor": kein Eintrag); Websuche "AGRARMONITOR Software Agrarmonitoring Impressum" (keine Wettbewerber). Messe-Signal: keiner.
17. Identität: AGRARMONITOR ist laut Verzeichnissen ein Produkt der betriko GmbH, Kalletal (S). Rechtsform/Register/Impressum nicht gelesen; Abweichung zur Vorgabe: Vorgabename ist die Marke, nicht die Gesellschaft.

## 3. AGRIBOX GmbH
1. Firma: AGRIBOX GmbH (Messe agraria 2026, Halle 24, Stand 40)
2. Segment / Demak-Geschäftsbereich: kein Demak-Bereich erkennbar; laut Messeliste (S) Klauenpflegezubehör, Tierhygiene, Arbeitsschutz/Schutzbekleidung, Futtermittelzusätze, Reinigungsbedarf, Einstreu.
3. Gebiet: nicht ermittelt (Sitz nicht gefunden; Land laut Messeliste DE)
4. Sitz und Fertigungsort: nicht ermittelt. Zwei Suchen fanden keine Firma "AGRIBOX GmbH". Die Treffer "AGRIBOX" sind Produktnamen (Kälberboxen) des italienischen Herstellers AGRITECH S.R.L., ohne Bezug zur Aussteller-GmbH belegt.
5. Website: nicht ermittelt
6. Was wird gebaut: nicht belegt. Messeliste (S): Verbrauchs-/Hygieneprodukte, Bekleidung, Futtermittelzusätze, daher wahrscheinlich Handel/Vertrieb (?). Typisch vergossen: keine (A, Block C: Handel/Verbrauchsgüter).
7. Fertigung DE/AT/NL: Niedrig, Stufe ?. Begründung: keine Firma auffindbar; Produktspektrum (Hygiene, Bekleidung, Futtermittel) ohne Elektronik; Fertigung nicht belegt.
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A. Einzelbewertung: Klauenpflegezubehör Niedrig (A), Hygieneprodukte Niedrig (A), Bekleidung Niedrig (A), Futtermittel Niedrig (A).
9. Patentrecherche (Pflicht, mind. 2 Suchen): Google Patents über WebSearch: `site:patents.google.com "Agribox GmbH" OR "AGRIBOX" Anmelder Klauenpflege`: kein Patent mit Agribox als Anmelder gefunden (nur Klauenpflege-Vorrichtungen aus Familie DE2209989 von 1972, Anmelder im Snippet nicht genannt, zeitlich und inhaltlich keine Zuordnung). Espacenet/DEPATISnet-Bezug: Abfragen "AGRIBOX GmbH Klauenpflege Tierhygiene Sitz Impressum" und "AGRIBOX Klauenpflege Produkte Hersteller Agribox GmbH Standort": keine Firma und keine Patente gefunden. Datenbanken nicht direkt abgefragt, Rechtsstand n. a., Anmelder-Identität offen. Ergebnis: 0 Treffer (WebSearch).
10. Einstufung Tom: unwahrscheinlich (Verguss Niedrig; Identität offen)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu. `crm_abgleich.py "AGRIBOX GmbH" "Agribox"`: kein Treffer.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Identität klären: Handelsregister/Impressum der "AGRIBOX GmbH" (Sitz, Gesellschaftszweck), Messeprofil agraria lesen. Ist es Händler (E2) oder Hersteller von Klauenpflege-/Hygieneprodukten (Chemie, kein Verguss)? Aktion: nicht kontaktieren.
14. Quellen:
- https://www.agriexpo.online/de/produkte-hersteller/agritech-individuelle-huette-1416-2092.html (S, Verzeichnis): "AGRIBOX 1" als Produktname von AGRITECH (Ergebnistext, Zuordnung zur Aussteller-GmbH nicht belegt); Abruf 2026-11-24.
- Messeliste agraria-2026/batches_v2/pruef_01.md (S): "Klauenpflegezubehör; Tierhygiene; Arbeitsbekleidung"; Abruf 2026-11-24.
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep "agribox": kein Eintrag); Websuchen zur Firma (keine Wettbewerber). Messe-Signal: keiner.
17. Identität: NICHT belegt. Firma "AGRIBOX GmbH" nicht auffindbar; Namensverwechslung mit dem Produktnamen AGRIBOX (AGRITECH S.R.L., Italien) möglich, nicht vermischt. Rechtsform, Adresse, Register unbekannt. Tabellenzeile 2 (Gelb, Auftrag Identität) möglich.

## 4. AMAZONEN-Werke H. Dreyer SE & Co. KG
1. Firma: AMAZONEN-Werke H. Dreyer SE & Co. KG (Messe agraria 2026, Halle 22, Stand B20)
2. Segment / Demak-Geschäftsbereich: Landtechnik (Sä-, Bodenbearbeitungs-, Düngerstreuer- und Pflanzenschutztechnik, Kommunaltechnik, Smart/Precision Farming); Demak-Bereich Electrical Insulation/Sensorik nur über Endprodukt-Regel.
3. Gebiet: Rest Deutschland+Niederlande (Hasbergen, Niedersachsen; S)
4. Sitz und Fertigungsort: Am Amazonenwerk 9-13, Hasbergen (Impressum-Snippet, Handelsregister Osnabrück; S). Konzern mit mehreren Werken: Hasbergen-Gaste (Stammwerk, Anbauschleuderstreuer laut Standortseite), Hude/Altmoorhausen (Sä- und Bodenbearbeitungstechnik), Leipzig, Forbach (Frankreich), Ungarn (S). Fertigende Einheit für Elektronik/Sensorik nicht belegt (Stellenanzeigen Elektronik-Entwicklung und -Qualität in Hasbergen-Gaste, S).
5. Website: https://amazone.net
6. Was wird gebaut: Feld-/Gebläsespritzen, Düngerstreuer, Sämaschinen, Grubber, Kommunalgeräte, Precision-Farming-Systeme (Messeliste und Konzernseite, S). Typisch vergossen/verklebt/gedichtet: ISOBUS-Bordcomputer/Steuergeräte, Sensoren (Verteilsensoren, Wägezellen, Temperatur/Feuchte laut Presseseite AmaSense), Elektro-Stellantriebe, Magnetventile, LED-Arbeitsbeleuchtung, Kabelbäume (A, Endprodukt-Regel; Elektronik-Entwicklung am Sitz laut Stellenanzeigen S).
7. Fertigung DE/AT/NL: Hoch, Stufe S. Begründung: Stammwerk Hasbergen laut Konzernseite; es ist aber ein Konzern mit mehreren Werken (auch Frankreich, Ungarn), daher wäre V mit Zuordnung Produkt-zu-Werk nötig (fehlt); welches Werk Elektronik fertigt, ist offen.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A. Einzelbewertung: ISOBUS-Steuergerät/Terminal Hoch (A, Block B/A, IP-Klasse im Außeneinsatz), Sensorik Hoch (A, Block A), Stellantriebe/Elektromotoren Mittel (A), LED-Beleuchtung Mittel (A), Stahlbau/Pflug-/Säschare Niedrig (A). Kein direkter Verguss-Beleg.
9. Patentrecherche (Pflicht, mind. 2 Suchen): Google Patents über WebSearch: `site:patents.google.com Amazonen-Werke H. Dreyer Vergussmasse OR potting OR encapsulation OR Dichtung`: kein Amazone-Patent mit Verguss gefunden. Zweite Abfrage Espacenet/DEPATISnet-Bezug: "Amazonen-Werke Patent espacenet Anmelder AMAZONEN WERKE DREYER H Sensor Gehäuse vergossen": Treffer DE102013103060A1 "Vorrichtung zum Ermitteln von zumindest einem Verteilungsparameter" (Amazonen-Werke H. Dreyer GmbH & Co. KG, 2014-10-16, Google Patents, Rechtsstand nicht geprüft) und EP2520148 "sensor arrangement" (Zuordnung zu Amazone im Snippet nur als verwandte Anmeldung, Rechtsstand nicht geprüft); beide Sensorik/Streutechnik, kein Verguss im Snippet. Weitere Abfrage "Amazone Schwenkantrieb Elektronik ISOBUS ... Stellenanzeige" ohne Patentbezug. Ergebnis: 2 Sensor-Patente, kein Verguss-Patent in WebSearch gefunden. Datenbanken nicht direkt abgefragt; Anmelder-Varianten (Amazonen-Werke H. Dreyer SE & Co. KG, GmbH & Co. KG) nicht vollständig.
10. Einstufung Tom: interessant (Fertigung Hoch UND Verguss Hoch; Stufen S bzw. A, vorläufig)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu. `crm_abgleich.py "AMAZONEN-Werke H. Dreyer SE & Co. KG" "AMAZONE" "AMAZONEN-WERKE"`: kein Treffer, kein Konzernbezug.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Welches Werk fertigt Bordcomputer/Sensorik (Hasbergen-Gaste?)? Standortseiten amazone.net/…/gruppe-standorte und Stellenanzeigen (Elektronik-Montage) lesen. (b) Datenblätter ISOBUS-Terminal/Sensor: IP-Klasse, Verguss/Dichtung. (c) Patente Anmelder "Amazonen-Werke H. Dreyer" mit Stichwort Verguss/Dichtung in Google Patents/Espacenet/DEPATISnet direkt, Rechtsstand. Aktion: nicht kontaktieren.
14. Quellen:
- https://amazone.net/nl-be/impressum-962892 (S, Snippet): "Am Amazonenwerk 9-13" Hasbergen, Handelsregister Osnabrück; Abruf 2026-11-24.
- https://amazone.net/en/company/company-history/portrait (S, Snippet): Hasbergen-Gaste als Stammwerk, Werke Hude, Forbach, Leipzig; Abruf 2026-11-24.
- https://amazone.net/en/career/locations-and-contacts (S, Snippet): Hasbergen-Gaste, "mounted spreaders" (Anbauschleuderstreuer); Abruf 2026-11-24.
- https://patents.google.com/patent/EP2520148C0/de (S, Snippet): Titel "sensor arrangement" (Zuordnung zu Amazone nicht gesichert); Abruf 2026-11-24.
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep "amazone": kein Eintrag); Websuche "Amazone OR BvL OR Bergmann Landtechnik Scheugenpflug OR Nordson OR Sonderhoff OR DOPAG OR Henkel Referenz Dosieranlage Verguss" (nur Amazone-Anleitungen, kein Wettbewerber-Bezug); Websuche zur Elektronikfertigung (keine Anlagen-/Materialnamen). Messe-Signal: keiner.
17. Identität: Name passt zur Vorgabe (AMAZONEN-Werke H. Dreyer SE & Co. KG laut Messeliste; Impressum-Snippet nennt Hasbergen, Handelsregister Osnabrück; Rechtsform SE & Co. KG selbst nicht gelesen, Impressum-Seite nicht gelesen). Stellenanzeigen nennen teils "Amazonen Werke GmbH"/"AMAZONEN-WERKE H. DREYER SE & CO. KG" (Varianten). Konzern: Amazone-Gruppe.

## 5. autarkize GmbH
1. Firma: autarkize GmbH (Messe agraria 2026, Halle 17, Stand 200)
2. Segment / Demak-Geschäftsbereich: Anlagenbau Pyrolyse/Biomasse-Konversion (modulare Container-Anlagen für Gas und Pflanzenkohle); Demak-Bereich nur über Endprodukt-Regel (Steuer-/Sensorelektronik der Anlage).
3. Gebiet: Bayern (Pfronten, Allgäu; S)
4. Sitz und Fertigungsort: Bürgermeister-Haff-Straße 8, Pfronten (CB Insights, S); ein Verzeichnis nennt abweichend An der Säge 3, 87640 Biessenhofen (S). Gründung 2022, Start-up (Seed 2024). Fertigungsort der Container-Anlagen nicht belegt (Eigenfertigung oder Zulieferer/Montage offen).
5. Website: nicht ermittelt (Hinweis: Domain autarkize.com laut Suchergebnis; nicht gelesen)
6. Was wird gebaut: modulare Pyrolyse-Anlagen in Schiffscontainern bis 2,5 MW, Output erneuerbares Gas und zertifizierte Pflanzenkohle (S). Typisch vergossen/verklebt/gedichtet: Mess-/Regelungselektronik, Temperatur-/Drucksensoren, Schaltschrank-/Steuerungselektronik, Gasmesstechnik (A, Endprodukt-Regel; zugekaufte Teile zählen). Nichts belegt.
7. Fertigung DE/AT/NL: Mittel, Stufe A. Begründung: Anlagenbauer mit Sitz in Bayern (Sitzregel greift nur bedingt: Start-up, Fertigungsort/Montage der Anlagen nicht belegt, Auslagerung offen). Mittel statt Hoch.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Sensorik (Temperatur/Druck/Gas) Mittel (A), Steuer-/Schaltschrankelektronik Mittel (A), Reaktor/Container Niedrig (A). Einschätzung aus Produkttyp.
9. Patentrecherche (Pflicht, mind. 2 Suchen): Google Patents/Espacenet über WebSearch: Abfrage "autarkize Pyrolyse Anlage Fertigung Pfronten Patent Anmelder": kein Patent mit autarkize als Anmelder gefunden (Fremdtreffer AT520769A1 und EP0007620 gehören anderen Anmeldern). Zweite Abfrage "autarkize GmbH Biogas Impressum Sitz" ohne Patentbezug. Direkte Abfrage in Google Patents, Espacenet, DEPATISnet nicht möglich; Rechtsstand n. a. Ergebnis: 0 Treffer (WebSearch). Empfohlen: DPMAregister/DEPATISnet Anmelder "autarkize".
10. Einstufung Tom: prüfenswert (Fertigung Mittel, Verguss Mittel)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu. `crm_abgleich.py "autarkize GmbH" "autarkize"`: kein Treffer.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Impressum/Handelsregister: Sitz Pfronten oder Biessenhofen. (b) Wo werden die Container-Anlagen gefertigt/montiert (eigene Werkstatt, Partner, Stellenanzeigen)? (c) Steuerungs-/Sensorik: eigene Elektronik oder Zukauf? Aktion: nicht kontaktieren.
14. Quellen:
- https://www.cbinsights.com/company/autarkize (S, Snippet): Hauptsitz "Bürgermeister-Haff-Straße 8", Pfronten (Ergebnistext); Abruf 2026-11-24.
- https://www.htgf.de/portfolio/htgffamily/autarkize/ (S, Snippet): Pfronten, Pyrolyse-Technologie (Ergebnistext); Abruf 2026-11-24.
- https://water-equipment-registry.pages.dev/manufacturer/autarkize-gmbh/ (S, Verzeichnis): Adresse "An der Säge 3, 87640 Biessenhofen"; Abruf 2026-11-24.
15. Größe/Umsatz: Seed-Finanzierung 2,3 Mio. EUR (Oktober 2024, S); Mitarbeiterzahl unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep "autarkize": kein Eintrag); Websuchen "autarkize GmbH Biogas Impressum Sitz" und "autarkize Pyrolyse Anlage Fertigung" (keine Wettbewerber). Messe-Signal: keiner.
17. Identität: Name passt (autarkize GmbH, Pfronten, Allgäu; S). Abweichung: zwei Adressangaben (Pfronten vs. Biessenhofen), Impressum/Register nicht gelesen.

## 6. BB-Umwelttechnik GmbH
1. Firma: BB-Umwelttechnik GmbH (Messe agraria 2026, Halle 19, Stand 170)
2. Segment / Demak-Geschäftsbereich: Landtechnik/Grünlandtechnik (Doppelmesser-Mähwerke, Schwader, Messerschleifmaschinen); kein klarer Demak-Bereich.
3. Gebiet: nicht ermittelt (Sitz nicht gefunden; Land laut Messeliste DE)
4. Sitz und Fertigungsort: nicht ermittelt. Verzeichnisse nennen "BB-Umwelttechnik GmbH, By Max Bannaski" (Inhaber laut Fachartikel Max Bannaski, S); Messerbalken werden laut Fachartikel zugekauft (Hersteller ESM, Ennepetal, S). Ob BB selbst fertigt und wo, ist nicht belegt.
5. Website: nicht ermittelt
6. Was wird gebaut: Doppelmesser-/Schmetterlings-Mähwerke (z. B. Seco Duplex), Kammschwader (Clementer), Messerschleifmaschinen (S, Händler-/Verzeichnisseiten). Typisch vergossen/verklebt/gedichtet: überwiegend mechanisch-hydraulisch; allenfalls Beleuchtung und Hydraulik-Magnetventile (A, Einschätzung aus Produkttyp); nichts belegt.
7. Fertigung DE/AT/NL: Niedrig, Stufe ?. Begründung: Sitz und Eigenfertigung nicht belegt, Hinweis auf Zukauf zentraler Komponenten; möglicherweise Montage/Vertrieb. Nur Verzeichnis-/Händlerlage.
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A. Einzelbewertung: Mähwerk/Schwader mechanisch Niedrig (A), Hydraulik-Magnetventile/Beleuchtung Niedrig bis Mittel (A, Einschätzung, daher höchstens Niedrig ausgewiesen, nicht belegt), Schleifmaschinen Niedrig (A).
9. Patentrecherche (Pflicht, mind. 2 Suchen): Abfrage 1 (Google-Patents-/Gebrauchsmuster-Bezug): "BB-Umwelttechnik Bannaski Patent Mähwerk Gebrauchsmuster Anmelder": kein Patent/Gebrauchsmuster von BB-Umwelttechnik oder Bannaski gefunden. Abfrage 2 (Espacenet/DEPATISnet-Bezug, Firmensitz): ""BB Umwelttechnik" Max Bannaski Hersteller Ort ...": keine Patentdaten. Google Patents, Espacenet, DEPATISnet nicht direkt abgefragt; Rechtsstand n. a. Ergebnis: 0 Treffer (WebSearch).
10. Einstufung Tom: unwahrscheinlich (Fertigung Niedrig, Verguss Niedrig)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu. `crm_abgleich.py "BB-Umwelttechnik GmbH" "BB Umwelttechnik"`: kein Treffer.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Impressum/Handelsregister: Sitz, Rechtsform, Fertigungsort (eigene Fertigung oder Montage/Zukauf?). Herstellerseite bb-umwelttechnik lesen. Aktion: nicht kontaktieren.
14. Quellen:
- https://www.environmental-expert.com/companies/bb-umwelttechnik-gmbh-by-max-bannaski-155851/products (S, Verzeichnis): "BB-Umwelttechnik GmbH, By Max Bannaski" (Ergebnistext); Abruf 2026-11-24.
- https://www.lfulg.sachsen.de/download/Nachlese_KAM_Doppelmesser-Maehwerk.pdf (S, Snippet): Max Bannaski "Inhaber von BB Umwelttechnik", Messerbalken von ESM, Ennepetal (Ergebnistext); Abruf 2026-11-24.
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep "BB-Umwelt": kein Eintrag); Websuchen zur Firma (keine Wettbewerber). Messe-Signal: keiner.
17. Identität: nicht belegt: Rechtsform GmbH laut Messeliste und Verzeichnis; Adresse, Register, Impressum unbekannt. Andere Firmen "BBB Umwelttechnik GmbH" (Gelsenkirchen), "BB Engineering" nicht vermischt.

## 7. Bergmann Ludwig GmbH
1. Firma: Bergmann Ludwig GmbH (Messe agraria 2026, Halle 20, Stand C50)
2. Segment / Demak-Geschäftsbereich: Landtechnik (Ladewagen, Überladewagen, Miststreuer, Transportfahrzeuge); Demak-Bereich nur über Endprodukt-Regel.
3. Gebiet: Rest Deutschland+Niederlande (Goldenstedt, Niedersachsen; S)
4. Sitz und Fertigungsort: Ludwig Bergmann GmbH, Hauptstraße 64-66, 49424 Goldenstedt (Implisense/Handelsregister HRB 112411 laut Snippet, S). Hersteller seit 1896, Ladewagen seit 60 Jahren (S). Weitere Werke nicht gefunden. Fertigende Einheit: Goldenstedt (A, Sitzregel).
5. Website: nicht ermittelt (Herstellerprofil: https://www.agriculture-xprt.com/companies/ludwig-bergmann-gmbh-51062)
6. Was wird gebaut: Ladewagen (REPEX-Baureihe, ISOBUS-Bedienung serienmäßig), Überladewagen, Miststreuer (z. B. M 2120 SW E) (S). Typisch vergossen/verklebt/gedichtet: ISOBUS-Steuergerät/Bedienterminal, Sensoren (Füllstand, Wiegetechnik), Elektro-/Hydraulik-Magnetventile, Beleuchtung, Kabelbäume (A, Endprodukt-Regel; ISOBUS-Bedienung S).
7. Fertigung DE/AT/NL: Hoch, Stufe A. Begründung: Sitzregel (Landmaschinenhersteller mit erkennbarem Standort, eigene Produkte, kein Konzern; "Manufacturer" laut Verzeichnis S). V nicht erreicht. Hinweis: zusätzliche Gesellschaft "Ludwig Bergman International Sales GmbH" (Vertrieb, gleiche Anschrift).
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: ISOBUS-Steuergerät Mittel (A), Sensorik/Wiegetechnik Mittel (A), Magnetventile Mittel (A), Beleuchtung Mittel (A), Rahmen/Aufbau Niedrig (A). Elektronik zugekauft vermutet; nichts belegt.
9. Patentrecherche (Pflicht, mind. 2 Suchen): Google Patents über WebSearch: `site:patents.google.com "Ludwig Bergmann GmbH" Patent Ladewagen`: keine Bergmann-Patente gefunden (nur Fremdpatente AT/CH, z. B. Pöttinger AT500198B1). Espacenet/DEPATISnet-Bezug: "Ludwig Bergmann GmbH Goldenstedt Patent Anmelder espacenet EP": kein EP-Anmelder gefunden (nur Markeneinträge, z. B. Madrid-Marke BERGMANN XPERT, Handelsregisterdaten). Direktabfrage der Datenbanken nicht möglich, Rechtsstand n. a. Ergebnis: 0 Treffer (WebSearch).
10. Einstufung Tom: prüfenswert (Fertigung Hoch, Verguss Mittel)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu. `crm_abgleich.py "Bergmann Ludwig GmbH" "Ludwig Bergmann GmbH" "Bergmann"`: nur Wortwurzel-Treffer "Ludwig Leuchten GmbH & Co. KG" (bekannte_firmen_DE-AT-NL.txt:1481), andere Firma, kein Bezug.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Impressum Ludwig Bergmann GmbH lesen (Sitz Goldenstedt, Fertigung); Datenblatt REPEX/ISOBUS-Terminal: Elektronik Eigenbau oder Zukauf, IP-Klasse; Stellenanzeigen Elektrik/Montage Goldenstedt. Aktion: nicht kontaktieren.
14. Quellen:
- https://implisense.com/en/companies/ludwig-bergmann-gmbh-goldenstedt-DEX5S47D6761 (S, Snippet): "Hauptstraße 64-66" Goldenstedt, HRB 112411 (Ergebnistext); Abruf 2026-11-24.
- https://farmersjournal.ie/bergmann-celebrates-60-years-of-manufacturing-forage-wagons-792930 (S, Snippet): "60 years of manufacturing forage wagons"; Abruf 2026-11-24.
- https://www.agriculture-xprt.com/companies/ludwig-bergmann-gmbh-51062 (S, Verzeichnis): "medium-sized, family run business"; Abruf 2026-11-24.
15. Größe/Umsatz: unbekannt ("mittelständisch, Familienunternehmen", S).
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep "bergmann": kein Eintrag); Websuche "Amazone OR BvL OR Bergmann Landtechnik Scheugenpflug OR Nordson OR Sonderhoff OR DOPAG OR Henkel Referenz Dosieranlage Verguss" (kein Treffer zu Bergmann). Messe-Signal: keiner.
17. Identität: Messename "Bergmann Ludwig GmbH" = umgekehrte Schreibweise von "Ludwig Bergmann GmbH", Goldenstedt (S). Impressum/Register nicht gelesen. Händler (Neyer, Deschberger) in Treffern nicht vermischt.

## 8. BRIXIES Schäfer Brand Distribution GmbH
1. Firma: BRIXIES Schäfer Brand Distribution GmbH (Messe agraria 2026, Halle 20, Stand 1130)
2. Segment / Demak-Geschäftsbereich: Spielwaren (Klemmbausteine aus ABS); kein Demak-Bereich. Messeliste: "Sonstiges".
3. Gebiet: Rest Deutschland+Niederlande (Daufenbach, Rheinland-Pfalz; S, Adresse der Schwesterfirma Schäfer Toy Company GmbH)
4. Sitz und Fertigungsort: Sitz der Brand Distribution GmbH nicht belegt; Schäfer Toy Company GmbH, Industriestraße 28, 56307 Daufenbach (Messekatalog Zoomark, S). Fertigungsort der Bausteine nicht belegt (ein Fertigungsland wurde nicht gefunden).
5. Website: https://brixies.de (aus Suchergebnis; nicht gelesen)
6. Was wird gebaut: Marke/Vertrieb von Klemmbausteinen aus ABS; laut Messekatalog konzentriert sich die Firma auf Design und Vertrieb der Serie Brixies Plus (S). Typisch vergossen: keine (A, Block C: Handel/Distribution ohne belegte Eigenfertigung).
7. Fertigung DE/AT/NL: Niedrig, Stufe ?. Begründung: Distribution/Markeninhaber, Eigenfertigung nicht belegt, Fertigungsland nicht gefunden (Spielzeugproduktion typischerweise Asien, nur als Branchenkontext, nicht belegt).
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A. Einzelbewertung: ABS-Steine Niedrig (A), Verpackung Niedrig (A). Elektronikanteile (z. B. Lichtsets) nicht belegt.
9. Patentrecherche (Pflicht, mind. 2 Suchen): Espacenet/DEPATISnet-Bezug (DPMAregister) über WebSearch: `"Schäfer Toy Company" OR "Brand Distribution GmbH" Brixies Patent Gebrauchsmuster Geschmacksmuster Anmelder Daufenbach`: keine Patent-, Gebrauchsmuster- oder Designanmeldung von Schäfer Toy Company oder Schäfer Brand Distribution gefunden (nur unbeteiligte Patentblatt-/Designblatt-Auszüge). Google-Patents-Bezug: Abfrage "Schäfer Toy Company Brixies Daufenbach Produktion ... Hersteller" ohne Patentbezug. Google Patents, Espacenet, DEPATISnet nicht direkt abgefragt; Rechtsstand n. a. Ergebnis: 0 Treffer (WebSearch).
10. Einstufung Tom: kein Fertiger (Marke/Distribution)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu. `crm_abgleich.py "BRIXIES Schäfer Brand Distribution GmbH" "Schäfer Toy Company" "Schäfer"`: nur Wortwurzel-/Präfix-Treffer "Schäfer Elektronik GmbH" (bekannte_firmen_DE-AT-NL.txt:2091), "Neuschäfer Elektronik", "Schaeffler"; andere Firmen, kein Bezug erkennbar (Elektronik vs. Spielwaren). Tina bitte bestätigen.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Impressum brixies.de lesen (Sitz Schäfer Brand Distribution GmbH, Gesellschafter/Schwesterfirma Schäfer Toy Company GmbH); wird in Daufenbach gefertigt oder nur vertrieben? Aktion: nicht weiter verfolgen (E2, Distribution).
14. Quellen:
- https://www.zoomark.it/en/2025-exhibitors-catalogue/exhibitor-detail/6135.html?id=9674 (S, Messekatalog, nach Regel N5 nie V): "Schaefer Toy Company GmbH", "Industriestraße 28, 56307 Daufenbach" (Ergebnistext); Abruf 2026-11-24.
- https://brixies.de/en/pages/business (S, Snippet): Betreiber "Schäfer Brand Distribution GmbH" (Ergebnistext); Abruf 2026-11-24.
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep "brixies"/"schäfer toy": kein Eintrag); Websuchen zur Firma (keine Wettbewerber). Messe-Signal: keiner.
17. Identität: Abweichung: Messeliste "BRIXIES Schäfer Brand Distribution GmbH", Suchtreffer "Schäfer Brand Distribution GmbH" (Betreiber brixies.de) und "Schäfer Toy Company GmbH" (Daufenbach). Beziehung der beiden Gesellschaften und Sitz der Brand Distribution nicht belegt; Register/Impressum nicht gelesen. Gelb (Identität) möglich.

## 9. BvL van Lengerich
1. Firma: BvL van Lengerich (Messe agraria 2026, Halle 19, Stand 130)
2. Segment / Demak-Geschäftsbereich: Landtechnik/Fütterungstechnik (Futtermischwagen, Entnahmetechnik, Biogastechnik, Farmmanagement); Demak-Bereich nur über Endprodukt-Regel (Wiege-/Steuerungselektronik, Elektroantriebe).
3. Gebiet: Rest Deutschland+Niederlande (Emsbüren, Niedersachsen; S)
4. Sitz und Fertigungsort: Bernard van Lengerich Maschinenfabrik GmbH & Co. KG, Grenzstraße 16, 48488 Emsbüren (Agritechnica-Ausstellerverzeichnis/Firmenverzeichnis, S). Gruppe mit mehreren Geschäftsbereichen (laut Wikipedia-Benutzerentwurf: Landtechnik, Oberflächentechnik, Elektrotechnik; Sekundärquelle, nur S). Fertigende Einheit/Produkt-Werk-Zuordnung nicht belegt.
5. Website: nicht ermittelt (Verzeichnis: https://www.agriexpo.online/de/soc/bernard-van-lengerich-maschinenfabrik-gmbh-co-kg-168522.html)
6. Was wird gebaut: Futtermischwagen (V-MIX, selbstfahrend), Silageentnahmetechnik, Einstreutechnik, Biogastechnik (Rührwerke/Fütterung), digitale Produkte (S, Pressemeldungen topagrar). Typisch vergossen/verklebt/gedichtet: Wiegesysteme (Wägezellen/Sensoren), Steuerungs- und Bedienelektronik, Elektro- und Hydraulikantriebe, Beleuchtung, Kabelbäume (A, Endprodukt-Regel). Ein Geschäftsbereich "Elektrotechnik" der Gruppe (S, Sekundärquelle) erhöht die Plausibilität, ist aber nicht belegt.
7. Fertigung DE/AT/NL: Hoch, Stufe S. Begründung: Maschinenbauer mit Sitz Emsbüren (seit 1860, S); Gruppe mit mehreren Geschäftsbereichen, daher wäre Stufe V (Werk-Zuordnung) nötig, fehlt. Keine Hinweise auf Auslandsfertigung gefunden.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A. Einzelbewertung: Wiege-/Sensorsystem Hoch (A, Block A Sensoren), Steuerungs-/Bedienelektronik Hoch (A, Block B Industrie-Steuerung im rauen Außeneinsatz, IP-Klasse), Elektroantriebe Mittel (A), Beleuchtung Mittel (A), Mischbehälter/Schnecken Niedrig (A). Kein direkter Beleg.
9. Patentrecherche (Pflicht, mind. 2 Suchen): Google Patents über WebSearch: `site:patents.google.com "Bernard van Lengerich Maschinenfabrik" Patent`: keine Einzeltreffer auf Google Patents; Aggregator goodip.io listet Anmelder "LENGERICH MASCHF" mit ca. 44 Anmeldungen seit 1972 (Silageentnahme, Schneid-/Misch-/Verteilgeräte; Rechtsstand nicht geprüft). Espacenet/DEPATISnet-Bezug: "Lengerich Maschinenfabrik Patent Vergussmasse OR Elektronik OR Dichtung DEPATISnet Anmelder BvL": keine Patente zu Verguss/Elektronik/Dichtung, nur Fremdpatente anderer Anmelder. Direktabfrage nicht möglich; Anmelder-Varianten (Bernard van Lengerich Maschinenfabrik GmbH & Co. KG, "Lengerich Maschf") nur über WebSearch. Ergebnis: ca. 44 Anmeldungen (Aggregator, S), kein Verguss-Treffer.
10. Einstufung Tom: interessant (Fertigung Hoch UND Verguss Hoch; Stufen S bzw. A, vorläufig)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu. `crm_abgleich.py "BvL van Lengerich" "Bernard van Lengerich Maschinenfabrik" "BvL"`: kein Treffer, kein Konzernbezug.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Impressum und Standortseite: Werke der BvL-Gruppe, wird in Emsbüren gefertigt? (b) Geschäftsbereich "Elektrotechnik" prüfen (eigene Schaltschrank-/Elektronikfertigung? ggf. vergossene Baugruppen). (c) Datenblätter Wiegesystem/Steuerung (IP-Klasse). (d) Patentabfrage direkt in Google Patents/Espacenet/DEPATISnet mit Rechtsstand. Aktion: nicht kontaktieren.
14. Quellen:
- https://digital.agritechnica.com/newfront/exhibitor/bvl---bernard-van-lengerich-maschinenfabrik-gmbh--co-kg-4ab5caa7 (S, Snippet): Titel "Grenzstr. 16"; Abruf 2026-11-24.
- https://www.agriexpo.online/de/soc/bernard-van-lengerich-maschinenfabrik-gmbh-co-kg-168522.html (S, Verzeichnis): "Bernard van Lengerich Maschinenfabrik GmbH & Co. KG"; Abruf 2026-11-24.
- https://de.wikipedia.org/wiki/Benutzer:Jost_Si/Bernard_van_Lengerich (S, Sekundärquelle, Benutzerentwurf, nie V): Geschäftsbereiche Landtechnik, Oberflächentechnik, Elektrotechnik (Ergebnistext); Abruf 2026-11-24.
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep "BvL"/"van Lengerich": kein Eintrag; der Treffer "Bischof+Klein (Lengerich)" ist eine andere Firma in anderem Ort); Websuche "Amazone OR BvL OR Bergmann Landtechnik Scheugenpflug OR Nordson ... Referenz Dosieranlage Verguss" (BvL nur Landtechnik/Reinigung, keine Dosier-Referenz). Messe-Signal: keiner.
17. Identität: Messename "BvL van Lengerich" = Kurzform von "Bernard van Lengerich Maschinenfabrik GmbH & Co. KG", Emsbüren (S). Register/Impressum nicht gelesen. Verwechslungsgefahr "Bischof+Klein, Lengerich" (andere Firma, nicht vermischt).

## 10. Colostrum BioTec GmbH
1. Firma: Colostrum BioTec GmbH (Messe agraria 2026, Halle 19, Stand 30)
2. Segment / Demak-Geschäftsbereich: Lebensmittel/Nahrungsergänzung (Kolostrum-Produkte, Milchprodukte); kein Demak-Bereich. Messeliste nennt auch Melktechnik/Tränken, nicht belegt (S, Ausstellerliste).
3. Gebiet: Bayern (Königsbrunn bei Augsburg; S)
4. Sitz und Fertigungsort: Richthofenstraße 21 1/2, 86343 Königsbrunn, HRB 30013 Amtsgericht Augsburg (Firmenprofil/North Data, S). Produktion am Standort Königsbrunn laut eigenem Ausstellerprofil (S). Hinweis: Verpackungsangabe eines Serums nennt CPI Colostrum Products International GmbH, Simbach am Inn als Hersteller (Lohnhersteller oder Vertrieb, ungeklärt, S).
5. Website: nicht ermittelt (Verzeichnis: https://www.ingredientsnetwork.com/colostrum-biotec-gmbh-comp307418.html)
6. Was wird gebaut: Kolostrum-Pulver und -Flüssigprodukte, Nahrungsergänzungsmittel, Kosmetik-Seren (S). Typisch vergossen/verklebt/gedichtet: keine (A, Lebensmittelproduktion).
7. Fertigung DE/AT/NL: Hoch, Stufe S. Begründung: Produktion in Königsbrunn laut Ausstellerprofil, nur Snippet (Ausstellerprofil nie V, Regel N5); für Verguss-Bewertung ohne Bedeutung.
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A. Einzelbewertung: Kolostrum-Produkte Niedrig (A), Abfüllverpackung Niedrig (A), eventuelle Melktechnik laut Messeliste Niedrig (?, nicht belegt, vermutlich Zusatzstoffe/Tränken).
9. Patentrecherche (Pflicht, mind. 2 Suchen): Abfrage 1 (Google Patents/Espacenet-Bezug): "Colostrum BioTec Patent Anmelder Kolostrum Verfahren espacenet": kein Patent mit Colostrum BioTec als Anmelder gefunden (Fremdtreffer: Biotest Pharma EP0338229/EP0652013, Meggle AT358376B, EP0918464 mit unbekanntem Anmelder; keine gleichnamige Firma). Abfrage 2 "Colostrum BioTec GmbH Sitz Impressum Kolostrum Produktion" (Firma; Markeneinträge, keine Patente). Datenbanken Google Patents, Espacenet, DEPATISnet nicht direkt abgefragt; Rechtsstand n. a. Ergebnis: 0 Treffer (WebSearch); keine Verguss-Relevanz.
10. Einstufung Tom: unwahrscheinlich (Verguss Niedrig)
11. Ampel: (leer, vergibt Tina)
12. CRM-Status: neu. `crm_abgleich.py "Colostrum BioTec GmbH" "Colostrum"`: kein Treffer.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Optional Impressum lesen; Messeprofil klären, ob Melk-/Tränketechnik gefertigt wird (sonst Lebensmittelhersteller, kein Verguss). Aktion: nicht weiter verfolgen, Entscheidung Tina.
14. Quellen:
- https://implisense.com/en/companies/colostrum-biotec-gmbh-koenigsbrunn-DE4FTLPJ3211 (S, Firmenprofil): Königsbrunn, "Richthofenstraße 21 1/2", HRB 30013 (Ergebnistext); Abruf 2026-11-24.
- https://www.ingredientsnetwork.com/colostrum-biotec-gmbh-comp307418.html (S, Ausstellerprofil, nie V): "we produce colostrum and colostrum based food and nutritional supplements" (Ergebnistext); Abruf 2026-11-24.
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (Grep "colostrum": kein Eintrag); Websuche zur Firma und Patentabfrage (keine Wettbewerber). Messe-Signal: keiner.
17. Identität: Name passt (Colostrum BioTec GmbH, Königsbrunn, HRB 30013 AG Augsburg laut Verzeichnis, S). Impressum nicht gelesen. Ähnliche Firma "Colostrum Technologies GmbH" (Bayern-International-Verzeichnis) nicht vermischt; ebenso CPI Colostrum Products International GmbH (Simbach).

## nicht aufgenommen (bereits bekannt / unklar)
Keine Firma ist BEKANNT, alle zehn erscheinen im Batch. Wortwurzel-Treffer des Skripts, alle als andere Firma bewertet (Tina bitte bestätigen):
- Adler Arbeitsmaschinen GmbH (Nordwalde): CRM-Schreibweise "ADLER Elektrotechnik Leipzig GmbH" (bekannte_firmen_DE-AT-NL.txt:44), anderer Kern-Name und anderes Geschäft, kein Ausschluss nach Jeys Regel "gleicher/sehr ähnlicher Name".
- Bergmann Ludwig GmbH (Goldenstedt): CRM "Ludwig Leuchten GmbH & Co. KG" (Zeile 1481), andere Firma.
- BRIXIES Schäfer Brand Distribution GmbH: CRM "Schäfer Elektronik GmbH" (Zeile 2091) und "Neuschäfer Elektronik GmbH" (Zeile 1702), "Schaeffler" (Zeilen 2073/2075), andere Firmen.

## Einschränkungen
- WebFetch und Chrome nicht verfügbar. Keine einzige Seite wurde selbst gelesen: alle Aussagen sind Stufe S, A oder ?. Keine V-Quelle, keine Aussage mailtauglich. Kurzzitate in Feld 14 stammen aus WebSearch-Ergebnistexten (teils Zusammenfassungen), nicht aus gelesenen Seiten; Tina muss sie im Browser prüfen.
- WebSearch-Limit: rund 30 Abfragen für 10 Firmen. Patentfelder beruhen ausschließlich auf WebSearch (Google-Patents-Snippets); Google Patents, Espacenet und DEPATISnet wurden nicht direkt abgefragt, Rechtsstand nirgends geprüft. Für AGRIBOX ist der Anmelder nicht identifiziert, für AGRARMONITOR/betriko und BRIXIES wurde je eine Abfrage mit Anmeldernamen ausgeführt; Direktabfragen der Datenbanken sind von Tina nachzuholen.
- Wettbewerbersuche (Feld 16): Grep auf wettbewerber_referenzen.md und eine kombinierte Websuche für die Landtechnikhersteller; je Firma höchstens eine zusätzliche Websuche. "Kein Hinweis" ist kein Gegenbeweis.
- Identität: Impressum und Handelsregister bei keiner Firma gelesen. Offen: AGRIBOX GmbH (Firma nicht auffindbar), BB-Umwelttechnik GmbH (Sitz unbekannt), BRIXIES (Beziehung Brand Distribution zu Schäfer Toy Company), autarkize (zwei Adressen), Adler (GmbH vs. GmbH & Co. KG).
- Gebiet: für AGRIBOX GmbH und BB-Umwelttechnik GmbH nicht ermittelbar (keine Sitzangabe gefunden); nicht erfunden.
- Keine Kontakt- oder Ansprechpartnersuche (Abschnitt K).
