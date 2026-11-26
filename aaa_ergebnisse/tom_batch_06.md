# Tom Batch 06 – all about automation Düsseldorf 2026 (Messemodus, Regel N)
Erstellt: 2026-10-15 (Tom, Stufe 1, Version 2, getrennter Agent, nur Tom-Rolle). Eingabe: aaa_batches_v2/pruef_05.md, 10 Firmen. Halle ist in der Liste nicht angegeben, Feld 1 trägt Stand aus dem Input. Stand/Sitz-Hinweise der Triage waren unverifiziert und wurden geprüft.
Abrufdatum aller Quellen: 2026-10-15. Belegstufen: V = Seite selbst gelesen, S = nur Suchsnippet/Kurzfassung (Seite nachlesen), A = aus Produkttyp abgeleitet, ? = angenommen.
WICHTIG zur Stufe: In diesem Lauf waren weder Chrome-Werkzeuge noch WebFetch nutzbar (WebFetch: "getaddrinfo ENOTFOUND" für alle Firmen- und Patentseiten). Browser nicht verfügbar. Es gibt daher KEINE Stufe-V-Aussage in diesem Batch; alle Quellen sind Suchsnippets (S). Messe-Beschreibungstexte sind nach Regel N5 ebenfalls S.
Patentrecherche: Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar, nur über WebSearch-Anfragen (site:patents.google.com, Stichwort worldwide.espacenet.com / DEPATISnet). Die Ergebnisse sind Suchmaschinenantworten, keine Datenbankabfrage mit Anmelderfilter. Siehe Einschränkungen: Batch ist bei Feld 9 nur eingeschränkt belastbar.
Messe-Signal (Regel N2): Grep auf aaa_duesseldorf_2026.csv nach Scheugenpflug, DOPAG, Nordson, ViscoTec, bdtronic, RAMPF, Sonderhoff, Hilger, Musashi, Henkel, DELO, ELANTAS, Wacker, Sika, GONANO, Marco, Panacol, Lohmann, OTTO, EPOXONIC, WEVO, Hexion, Loctite, Dymax, Graco, Atlas Copco: kein Wettbewerber unter den Ausstellern (einziger Textfund "otto" in "Ottobrunn" bei Panasonic Industry Europe, Falschtreffer). Gilt für alle 10 Firmen.
CRM-Abgleich: crm_abgleich.py für jede Firma mit Konzern-/Schwesternamen ausgeführt (2026-10-15). Ergebnis: 0 BEKANNT; 1 Präfix-Treffer (Kaiser).

## 1. igus GmbH
1. Firma: igus GmbH (Messe: all about automation Düsseldorf 2026, Stand 603, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (konfektionierte, überspritzte/vergossene Leitungen, Schrittmotoren, Sensorik), nachrangig Gasketing
3. Gebiet: Rest Deutschland+Niederlande (Köln, NRW)
4. Sitz und Fertigungsort: Köln (Stammsitz mit Spritzguss- und Leitungsfertigung, S). Fertigende Einheit: igus-Werk Köln; Rechtsform laut Quellen schwankend igus GmbH / igus SE & Co. KG (siehe Feld 17). Weltweiter Konzern mit weiteren Werken.
5. Website: https://www.igus.de
6. Was wird gebaut -> Bauteile: Energieketten, chainflex-Leitungen, Gleitlager (Spritzguss), Linearachsen, eigenes kleines Schrittmotorenprogramm (NEMA 17/23, optional Encoder/Bremse), Roboter (robolink), intelligente Sensorik (S, industrial-production.de-Snippet, computer-automation.de-Snippet). Typisch vergossen/verklebt/gedichtet (alle A): Leitungen mit überspritzten/vergossenen Steckern (A, Block A Kabelkonfektion; igus-Produktmeldung "Continuous-Flex Cables ... with Over-Molded Connectors", S, igus Inc.), Schrittmotoren mit Encoder/Elektronik (A, Block A), Sensorik (A, Block A). Welches Produkt in welchem Werk entsteht, ist NICHT belegt.
7. Fertigung DE/AT/NL: Hoch, Stufe S. Begründung: Snippet computer-automation.de: "857 Spritzgussmaschinen" in Köln und der überwiegende Teil der Fertigung weiter in Deutschland; Konzern, daher V nötig (Quelle nicht im Browser gelesen). Motor-/Elektronikfertigung in Köln NICHT belegt (Suche ergab keinen Ort für die Schrittmotoren).
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (abgeleitet aus Produkttyp konfektionierte Leitungen mit überspritzten Steckern, Motoren mit Elektronik). Einzelbewertung: Leitungskonfektion/überspritzte Stecker Hoch (A), Schrittmotoren mit Encoder Hoch (A), Sensorik Hoch (A), Roboter-Elektronik Mittel (A), Energieketten/Gleitlager Niedrig (A). Überspritzen im Thermoplast ist nicht zwingend Harzverguss.
9. Patentrecherche (Pflicht):
- Google Patents (per WebSearch "site:patents.google.com igus GmbH potting OR Vergussmasse OR overmolded cable"): keine Treffer mit Anmelder igus; nur Fremdpatente (z. B. EP2087492B1 Overmolded wire bundle, Anmelder im Snippet nicht genannt, nicht zugeordnet; AT235579B Vergussmasse Wicklungen, Fremdanmelder, nicht igus).
- Google Patents (per WebSearch "igus patent potting compound cable connector igus GmbH assignee"): nur Fremdanmelder (Eaton/Cooper US10014613B2, US8395044B2), kein igus-Treffer. US12463368 "Electrical connection for an actuator unit": Anmelder im Snippet unbekannt, nicht zugeordnet.
- Espacenet / DEPATISnet (per WebSearch "espacenet igus GmbH applicant potting OR Vergussmasse"; "igus Patent Anmelder igus GmbH Vergussmasse Espacenet DEPATISnet"): keine Datenbankseite erreichbar; ein Patsnap-Profil nennt 2.146 igus-Patente insgesamt (Sekundärquelle, S, Gründungsjahr dort falsch). Keine Verguss-Zuordnung.
- Ergebnis: Große Patentfamilie vorhanden (Sekundärquelle), aber kein Patent mit Verguss/Dichtung als Kern gefunden; Rechtsstand nicht geprüft; direkter Anmelderfilter (Google Patents, Espacenet, DEPATISnet) nicht ausgeführt. Mit enger Suche (potting compound OR Vergussmasse) zu wiederholen, sobald Browser verfügbar.
10. Einstufung Tom: interessant (Fertigung Hoch S, Verguss Hoch A), mit Vorbehalt Identität (Feld 17) und Werkszuordnung
11. Ampel: 
12. CRM-Status: neu (crm_abgleich.py "igus GmbH", "igus SE & Co. KG": kein Treffer in bekannte_firmen und kundendatenbank_export)
13. Nachrecherche-Auftrag und Aktion (Vorschlag an Tina): (a) Wo werden Schrittmotoren, Encoder/Elektronik und konfektionierte Leitungen mit Steckern gefertigt (Köln?) und wird dort vergossen? Produktseite Schrittmotoren, Stellenanzeigen Köln (Leitungskonfektion/Montage) im Browser lesen. (b) Impressum igus.de: igus GmbH oder igus SE & Co. KG, Register. (c) Aktuelle V-Quelle für Köln-Fertigung beschaffen. Aktion: noch nicht kontaktieren.
14. Quellen:
- https://www.computer-automation.de/e-mechanik-und-interfaces/igus-investiert-in-automatisierung-und-lokale-produktion-124-4-mio--euro-fuer-lieferketten-und-internationale-standorte-909918.htm (S, Suchsnippet): "857 Spritzgussmaschinen" in Köln; Abruf 2026-10-15.
- https://www.industrial-production.de/maschinenelemente---linearaktuator-mit-motor.htm (S, Suchsnippet, Pfad laut Suchtreffer .../antriebstechnik/maschinenelemente---linearaktuator-mit-motor.htm): eigenes Motorenprogramm NEMA 17/23; Abruf 2026-10-15.
- https://www.automation.com/en-us/products/product21/igus-continuous-flex-cables-available-with-over-mo (S, Snippet, igus Inc. 2006): Leitungen mit "Over-Molded Connectors"; Abruf 2026-10-15.
- https://discovery.patsnap.com/company/igus/ (S, Snippet): 2.146 Patente (Sekundärquelle); Abruf 2026-10-15.
15. Größe/Umsatz: rund 4.600 Mitarbeitende weltweit (Stellenportal-Snippet, S); Umsatz Milliardenbereich laut computer-automation.de-Titel "igus Umsatzmilliarde gehalten" (S); sonst unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag igus); Websuche "igus Dosieranlage OR Vergussanlage OR Klebstoff Nordson OR Scheugenpflug OR DOPAG OR ViscoTec OR Henkel Fertigung Köln" (nur allgemeine Treffer ohne Wettbewerberbezug). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: TEILWEISE. Vorgabe "igus GmbH" (Köln); Triage nennt "igus SE & Co. KG". Snippet US-Markenregister: Inhaber "igus GmbH, Köln" bzw. Feld "IGUS SE & CO. KG" (S). Impressum nicht gelesen, Register nicht belegt. Abweichung Rechtsform benannt; gleichnamige Auslandsgesellschaften (igus Inc. USA) nicht vermischt. Tina: Zeile 2 prüfen.

## 2. ima-tec GmbH
1. Firma: ima-tec GmbH (Messe: all about automation Düsseldorf 2026, Stand 140, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: kein Kerngeschäft (Maschinenbauer); Sekundär: Electrical Insulation (verbaute Steuerungs-/Schaltschrankelektronik), eventuell Klebe-/Dosierstationen in Montageanlagen
3. Gebiet: Bayern (Kürnach bei Würzburg)
4. Sitz und Fertigungsort: Wachtelberg 10 a, 97273 Kürnach (Implisense-Snippet, S); Fertigungsort = Sitz laut Eigenbeschreibung Sondermaschinenbau (S). Seit 2017 Tochter der SAR Group (Österreich).
5. Website: https://www.ima-tec-gmbh.com
6. Was wird gebaut -> Bauteile: Sondermaschinen: Montage-, Prüf- und Handhabungssysteme, Automatisierungslösungen, Montage- und Prüffunktionen (S, Messeprofil/Verzeichnisse); Schaltschrankbau laut Triage. Typisch vergossen/verklebt/gedichtet: in den Maschinen verbaute Sensorik, Netzteile, Antriebe (A, Block A, Endprodukt-Regel, zugekaufte Teile zählen); Klebe-/Dosierstationen in Kundenanlagen möglich (?, nicht belegt, keine Referenz gefunden). Das Unternehmen selbst vergießt vermutlich nicht.
7. Fertigung DE/AT/NL: Hoch, Stufe A (Sitzregel: Maschinenbauer mit erkennbarem Standort Kürnach, eigene Produkte). Vorbehalt: Konzernzugehörigkeit SAR Group (S); Hinweise auf Auslagerung nicht gefunden.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: verbaute Sensoren/Netzteile (zugekauft) Mittel (A), Steuerungselektronik/Schaltschrank Mittel (A), Klebe-/Dosiermodul in Kundenanlagen Mittel (?), Mechanik/Handling Niedrig (A). Einordnung Integrator (E1 "Integratoren von Dosier-/Dispensing-Anlagen"): kein Beleg, dass ima-tec Dosieranlagen als Produkt anbietet; zu prüfen.
9. Patentrecherche (Pflicht):
- Google Patents (per WebSearch "site:patents.google.com ima-tec OR imatec Kürnach Anmelder"): kein Treffer zu Kürnach. Nur Imatec – Innovative Machine Technology S.à r.l. (Luxemburg, z. B. US11660772 helical tube winding): andere Firma, aussortiert.
- Espacenet / DEPATISnet (per WebSearch "ima-tec Kürnach Patent Montageanlage Kleben Dosieren"): keine Patente der Kürnacher Firma gefunden; Datenbanken nicht direkt abgefragt.
- Ergebnis: keine Patente gefunden; kein Gegenbeweis. Anmelder-Varianten (SAR Group, "ima-tec") nur über Websuche geprüft.
10. Einstufung Tom: prüfenswert (Fertigung Hoch A, Verguss Mittel A); E1-Prüfung Integrator offen
11. Ampel: 
12. CRM-Status: neu (crm_abgleich.py "ima-tec GmbH", "SAR Group": kein Treffer); Konzernbezug SAR: kein Treffer
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Bietet ima-tec Klebe-/Dosier-/Vergussstationen als Anlagenprodukt an (dann E1 Integrator) oder baut es nur Montage-/Prüfanlagen? Produkt- und Referenzseiten auf ima-tec-gmbh.com im Browser lesen. (b) Impressum/Handelsregister Würzburg HRB 9371 gegenlesen. (c) Welche eigenen Elektronik-/Schaltschrankbaugruppen entstehen in Kürnach? Aktion: keine Ansprache vor Klärung (a).
14. Quellen:
- https://app.implisense.com/en/companies/ima-tec-gmbh-kuernach--DEKTP2DFTS28 (S, Snippet): Wachtelberg 10 a, 97273 Kürnach, HRB 9371 Würzburg, Gegenstand "Entwicklung, Herstellung und Vertrieb von Montagesystemen"; Abruf 2026-10-15.
- https://www.heilbronn.allaboutautomation.de/en/?p=425202 (S, Messeprofil, Regel N5): "part of the SAR Group since 2017", über 95 Mitarbeiter; Abruf 2026-10-15.
- https://www.northdata.de/?id=8135546 (S, Snippet): Sitz Kürnach (Hinweis älteren Datums); Abruf 2026-10-15.
15. Größe/Umsatz: Triage 97 MA (Implisense-Snippet), Messeprofil "über 95 Mitarbeiter" (zwei S-Quellen, widersprechen sich nicht); Umsatz unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag ima-tec); Websuche "ima-tec Kürnach Montageanlage Dosiersystem Referenz Nordson OR ViscoTec OR DOPAG OR Scheugenpflug OR Henkel" (keine Treffer mit ima-tec-Bezug); Websuche "ima-tec Kürnach Patent Montageanlage Kleben Dosieren". Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: TEILWEISE belegt (S). ima-tec GmbH, Wachtelberg 10 a, 97273 Kürnach, Amtsgericht Würzburg HRB 9371 (Implisense-Snippet); Impressum nicht gelesen. Gleichnamige IMA-TEC GmbH in Homburg/Saar (Würzburger Str. 3-5, automa.net, Demontage/Elektrotechnik) und IMA Automation Amberg sind andere Firmen, nicht vermischt. Keine Abweichung zur Liste.

## 3. IMPADY
1. Firma: IMPADY (Messe: all about automation Düsseldorf 2026, Stand 818, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: keiner (laut Startbase Consulting/B2B-Plattform)
3. Gebiet: außerhalb/unklar (Sitz Darmstadt laut Startbase = Rest Deutschland+Niederlande; Vorgabe Hoppstädten-Weiersbach nicht belegt)
4. Sitz und Fertigungsort: Sitz laut Startbase: Darmstadt (S, unclaimed Profil). Vorgabe-Sitz Hoppstädten-Weiersbach (Rheinland-Pfalz): keine Quelle gefunden, die IMPADY dort nennt. Fertigungsort: nicht belegt.
5. Website: unbekannt (in der Liste nicht angegeben, nicht gefunden)
6. Was wird gebaut -> Bauteile: nicht belegt. Startbase: "IMPADY GmbH", Consulting, Seed Stage, Platform B2B, gegründet 2025, 1 bis 10 Beschäftigte (S, unverifiziert). Kein Produkt, kein Bauteil bekannt (?).
7. Fertigung DE/AT/NL: Niedrig, Stufe ?. Begründung: keine Fertigungsangabe; Profil zeigt Beratung/Plattform.
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A (Produkttyp Beratung/Plattform, Wissensbasis Block C). Keine Bauteile bekannt.
9. Patentrecherche (Pflicht):
- Google Patents (per WebSearch, Anfrage zusammen mit INSEVIS/INperfektion/JAM/IXON "Patent Anmelder Gebrauchsmuster Vergussmasse"; zusätzlich Name IMPADY in Identitätssuche): keine Treffer zu IMPADY.
- Espacenet / DEPATISnet (per WebSearch, gleiche Anfrage): keine Treffer; Datenbanken nicht direkt abgefragt.
- Ergebnis: keine Patente gefunden; Firma sehr jung (2025) und nicht eindeutig identifiziert; kein Gegenbeweis.
10. Einstufung Tom: kein Fertiger (vorläufig; Beratung/Plattform, möglicher Ausschluss E2, Tina entscheidet; Identität ungeklärt)
11. Ampel: 
12. CRM-Status: neu (crm_abgleich.py "IMPADY": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Identität klären: Gibt es eine IMPADY GmbH (Darmstadt) mit Handelsregistereintrag, und ist die Messefirma in Hoppstädten-Weiersbach identisch? Handelsregister (Darmstadt), Messe-Ausstellerprofil auf allaboutautomation.de im Browser lesen, Website finden. Aktion: nicht kontaktieren.
14. Quellen:
- https://www.startbase.com/organization/impady/ (S, Snippet): "Consulting ... Seed Stage ... Platform B2B ... 2025 ... Darmstadt"; Abruf 2026-10-15.
- WebSearch "IMPADY Hoppstädten-Weiersbach Darmstadt Firma": kein Treffer, der IMPADY mit Hoppstädten-Weiersbach verbindet; Abruf 2026-10-15.
15. Größe/Umsatz: 1 bis 10 Beschäftigte (Startbase, unclaimed, S); Umsatz unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag IMPADY); Websuche zu IMPADY (nur Startbase-Profil, keine Fertigung, daher keine Wettbewerber-Suche sinnvoll). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: NICHT belegt. Vorgabe: IMPADY, Hoppstädten-Weiersbach. Gefunden: "IMPADY GmbH", Darmstadt (Startbase, S, nicht verifiziert). Kein Impressum, kein Register gefunden. Sitz-Widerspruch Darmstadt/Hoppstädten-Weiersbach bleibt. Ampel höchstens Gelb (Tabellenzeile 2).

## 4. INperfektion GmbH
1. Firma: INperfektion GmbH (Messe: all about automation Düsseldorf 2026, Stand 717, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Elektronikbaugruppen, Steuerungen), nachrangig Gasketing/Sealing (Schaltschrank-/Schutzeinhausungen)
3. Gebiet: Rest Deutschland+Niederlande (Wegberg, NRW)
4. Sitz und Fertigungsort: Friedrich-List-Allee 18, 41844 Wegberg (Presseindex-Snippet, S). Fertigende Einheit: INperfektion GmbH am Sitz (Eigenangabe Elektronikfertigung/Schaltschrankbau, S).
5. Website: https://www.inperfektion.de
6. Was wird gebaut -> Bauteile: Full-Service-Anbieter für Automatisierung: "Hard-/Softwareentwicklung, Elektronikfertigung, Elektroanlagenkonstruktion, Schaltschrankbau" (S, Presseindex-Snippet); Messeprofil: schlüsselfertige Roboterzellen und Automatisierungssysteme, Koksofen-Servicemaschinen, Ersatzteile (S); item-Plus-Partner seit 2021 für Profil-Schutzeinhausungen/Schutzzäune (S, Messeprofil Straubing). Typisch vergossen/verklebt/gedichtet: Elektronikbaugruppen der eigenen Elektronikfertigung (A, Block B, Schutzlack/Teilverguss, Einschätzung aus Produkttyp), Schaltschränke/Steuerungen mit Netzteilen, Relais, Sensoren (A, Endprodukt-Regel, zugekaufte Teile), Profil-Schutzeinhausungen (Niedrig, A). Eigenverguss nicht belegt.
7. Fertigung DE/AT/NL: Hoch, Stufe A (Sitzregel: Geräte-/Anlagenbauer mit erkennbarem Standort Wegberg, eigene Leistungen, kein Hinweis auf Auslagerung). Stützend S: Eigenangabe "Elektronikfertigung ... Schaltschrankbau" (Presseindex).
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Elektronikbaugruppen Mittel (A), Schaltschrank/Steuerungen mit zugekauften Netzteilen/Sensoren Mittel (A), Roboterzellen/Koksofenmaschinen Niedrig (A), Schutzeinhausungen Niedrig (A).
9. Patentrecherche (Pflicht):
- Google Patents (per WebSearch, Anfrage gemeinsam mit INSEVIS/JAM/IXON "Patent Anmelder Gebrauchsmuster Vergussmasse" sowie "INperfektion GmbH Wegberg ... Schutzlack Verguss Impressum"): keine Treffer zu INperfektion.
- Espacenet / DEPATISnet (per WebSearch, gleiche Anfragen): keine Treffer; Datenbanken nicht direkt abgefragt.
- Ergebnis: keine Patente gefunden; kein Gegenbeweis.
10. Einstufung Tom: prüfenswert (Fertigung Hoch A, Verguss Mittel A)
11. Ampel: 
12. CRM-Status: neu (crm_abgleich.py "INperfektion GmbH", "item": kein Treffer). item-Konzernbezug (item Industrietechnik): kein Treffer.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Werden in Wegberg Elektronikbaugruppen selbst gefertigt (SMD/THT, Schutzlack, Verguss) oder nur Schaltschrank/Verdrahtung? Website Leistungen, Karriereseite, Stellenanzeigen Wegberg im Browser lesen. (b) Fertigt INperfektion Produkte in Serie oder Einzelanlagen (Koksofenmaschinen)? Aktion: Beobachtung.
14. Quellen:
- https://www.deutscherpresseindex.de/?p=406309 (S, Snippet): "Hard-/Softwareentwicklung, Elektronikfertigung, Elektroanlagenkonstruktion, Schaltschrankbau"; Friedrich-List-Allee 18, 41844 Wegberg; Abruf 2026-10-15.
- https://www.duesseldorf.allaboutautomation.de/en/exhibitors/inperfektion-gmbh-223375/ (S, Messeprofil, Regel N5): Roboterzellen, Koksofen-Servicemaschinen; Abruf 2026-10-15.
- https://straubing.allaboutautomation.de/en/?p=447915 (S, Messeprofil 2024): item-Plus-Partner seit 2021; Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag INperfektion); Websuche "INperfektion GmbH Wegberg Elektronikfertigung Schutzlack Verguss Impressum" (Treffer nur Turck-Verguss-Anleitung und Scheugenpflug-Seite ohne INperfektion-Bezug); Websuche "INperfektion Wegberg item Plus Partner ...". Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: TEILWEISE belegt (S). INperfektion GmbH, Friedrich-List-Allee 18, 41844 Wegberg, Geschäftsführer Carsten Finke (Presseindex-Snippet). Register nicht gefunden, Impressum nicht gelesen. Keine Abweichung zur Liste. Tätigkeitsprofil weicht von Triage ab (Triage: Profil-Schutzeinhausungen; Quellen: Automatisierung, Roboterzellen, Elektronikfertigung).

## 5. INSEVIS GmbH
1. Firma: INSEVIS GmbH (Messe: all about automation Düsseldorf 2026, Stand 615, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Steuerelektronik, Gateways), Gasketing/Sealing (HMI-Frontdichtung), Optical Bonding (HMI-Panels, Touch-Displays)
3. Gebiet: Bayern (Erlangen)
4. Sitz und Fertigungsort: Erlangen. Anschrift der Holding laut LEI-Snippet: INSEVIS Holding GmbH, Am Weichselgarten 7, 91058 Erlangen (HRB 20784 Fürth). Fertigungsort der Geräte: NICHT belegt (nur Werbeaussage "made in Germany").
5. Website: https://www.insevis.com
6. Was wird gebaut -> Bauteile: S7-kompatible SPS, S7-HMI-Panels, S7-Panel-SPS, IIoT-Gateways (VPN, OPC UA, MQTT); Eigenwerbung "made in Germany" (S, Messeprofile). Typisch verklebt/gedichtet/vergossen: HMI-Panels mit Touch-Display (Optical Bonding, A, Block B), Front-/Gehäusedichtung (A, Block B), Steuer- und Gateway-Elektronik (A, Block B), Netzteil-Module (A, Block A, falls verbaut). Ob eigene Fertigung oder EMS, ist unbelegt.
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Sitz Erlangen, Eigenangabe "made in Germany" (Messeprofil, Regel N5: S); Fertigungsort und fertigende Gesellschaft nicht belegt (GmbH, Vertriebs GmbH, Holding).
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: HMI-Panels (Display/Touch) Mittel (A), Steuerelektronik/SPS Mittel (A), Gateways Niedrig bis Mittel (A), Gehäusedichtung Mittel (A).
9. Patentrecherche (Pflicht):
- Google Patents (per WebSearch, gemeinsame Anfrage mit INperfektion/JAM/IXON "Patent Anmelder Gebrauchsmuster Vergussmasse"): keine Treffer zu INSEVIS.
- Espacenet / DEPATISnet (per WebSearch, gleiche Anfrage): keine Treffer; Datenbanken nicht direkt abgefragt. Anmelder-Varianten (INSEVIS Holding, INSEVIS Vertriebs GmbH) nicht gesondert durchsucht.
- Ergebnis: keine Patente gefunden; kein Gegenbeweis.
10. Einstufung Tom: prüfenswert (Fertigung Mittel S, Verguss Mittel A)
11. Ampel: 
12. CRM-Status: neu (crm_abgleich.py "INSEVIS GmbH", "INSEVIS Vertriebs GmbH": kein Treffer); Holding/Schwester im CRM: nein
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Welche Gesellschaft fertigt (INSEVIS GmbH, INSEVIS Vertriebs GmbH oder Holding) und wo (Erlangen oder EMS)? Impressum insevis.com, Handelsregister Fürth, Stellenanzeigen Erlangen (Montage/Produktion) im Browser lesen. (b) Werden Panels mit Frontdichtung/Verklebung im Haus montiert? Aktion: Beobachtung.
14. Quellen:
- https://www.berlin.allaboutautomation.de/en/exhibitors/insevis-gmbh-204670/ (S, Messeprofil, Regel N5): "Erlangen-based S7 system provider"; "made in Germany"; Abruf 2026-10-15.
- https://www.friedrichshafen.allaboutautomation.de/en/products/s7-plcs-s7-panels-s7-panel-plcs-s7-gateways-130091/ (S, Snippet): S7-SPS, S7-Panels, S7-Gateways; Abruf 2026-10-15.
- https://lei.bloomberg.com/leis/view/9845006FECET6D59EC41 (S, Snippet): INSEVIS Holding GmbH, Am Weichselgarten 7, 91058 Erlangen, Fürth HRB 20784; Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag INSEVIS); Websuche "INSEVIS Erlangen HMI Panels Gateways entwickelt gefertigt Erlangen Produktion" (nur Messeprofile). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: NICHT eindeutig (S). Vorgabe "INSEVIS GmbH" ; Triage nennt zusätzlich "INSEVIS Vertriebs GmbH" (Messeprofil 204670); LEI-Snippet zeigt "INSEVIS Holding GmbH" (Erlangen, HRB 20784). Welche Gesellschaft Aussteller und Fertiger ist, ist nicht belegt; Impressum nicht gelesen. Ampel höchstens Gelb (Tabellenzeile 2).

## 6. IXON B.V.
1. Firma: IXON B.V. (Messe: all about automation Düsseldorf 2026, Stand 438, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (nachrangig; Router-Elektronik mit Schutzlack/Teilverguss)
3. Gebiet: Rest Deutschland+Niederlande (Niederlande)
4. Sitz und Fertigungsort: Zuster Bloemstraat 20, 5835 DW Beugen, Niederlande (Händlerverzeichnis-Snippet, S). Triage nennt Overloon; Overloon in keiner Suchquelle belegt. Fertigungsort der Hardware: NICHT belegt.
5. Website: https://www.ixon.cloud
6. Was wird gebaut -> Bauteile: IXrouter3 (Varianten IX2400, IX2405, IX2410, IX2415; Ethernet, 4G, Wi-Fi), Metallgehäuse für Schaltschrank/DIN-Schiene, Schutzart laut zwei Händlerseiten IP20 (S); IXON Cloud (Software). Typisch vergossen/verklebt (A): Router-Elektronik hinter Metallgehäuse Niedrig (A, IP20 spricht gegen Verguss; Schutzlack möglich), keine weiteren Bauteile bekannt.
7. Fertigung DE/AT/NL: Niedrig, Stufe ?. Begründung: Hardware-Hersteller laut Händlern nur "Origin Netherlands"; Fertigungsort (eigen oder EMS, Asien) unbelegt. IXON positioniert sich primär als Cloud-/IIoT-Anbieter.
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A. Einzelbewertung: Router-Leiterplatte Niedrig (A), Metallgehäuse Niedrig (A), Netzteil extern Niedrig (A), Software keine Teile. Kein Gegenbeleg, aber IP20-Geräte für den Schaltschrank werden typisch nicht vergossen.
9. Patentrecherche (Pflicht):
- Google Patents (per WebSearch, gemeinsame Anfrage mit INSEVIS/INperfektion/JAM "Patent Anmelder Gebrauchsmuster Vergussmasse"): keine Treffer zu IXON B.V.
- Espacenet / DEPATISnet (per WebSearch, gleiche Anfrage): keine Treffer; Datenbanken nicht direkt abgefragt. Gleichnamige Firmen (IXON-Marken anderer Hersteller) nicht ausgewertet.
- Ergebnis: keine Patente gefunden; kein Gegenbeweis.
10. Einstufung Tom: unwahrscheinlich (Fertigung Niedrig ?, Verguss Niedrig A)
11. Ampel: 
12. CRM-Status: neu (crm_abgleich.py "IXON B.V.": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Wo wird der IXrouter gefertigt (Beugen/Overloon oder EMS-Partner im Ausland)? Impressum, Konformitätserklärung, Stellenanzeigen im Browser lesen. (b) Sitz klären: Beugen oder Overloon (KvK-Auszug). Aktion: nicht priorisieren.
14. Quellen:
- https://www.ixon.cloud/ixrouter (S, Snippet): "Next generation connectivity hardware for industrial machines"; Abruf 2026-10-15.
- https://adjditec.com/en/products/ix2410-ixon (S, Händler): Zuster Bloemstraat 20, Beugen; Abruf 2026-10-15.
- https://iepsol.com/product/ixrouter3-iot-remote-access-gateway/ (S, Händler): Metallgehäuse, IP20; Abruf 2026-10-15.
- https://www.allaboutautomation.de/en/?p=386250 (S, Triage-Quelle, nicht erneut abgerufen).
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag IXON); Websuche "IXON IXrouter hardware manufactured Overloon Netherlands production KvK" und "IXON B.V. Beugen IXrouter Gehäuse ... EMS Partner" (keine Wettbewerber-Treffer). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: TEILWEISE (S). IXON B.V., Zuster Bloemstraat 20, 5835 DW Beugen (Händlerseite). Triage nennt Overloon: kein Beleg gefunden; KvK-Auszug und Impressum nicht gelesen. Abweichung Beugen/Overloon benannt. Gleichnamige Firmen nicht vermischt.

## 7. JAM automation GmbH
1. Firma: JAM automation GmbH (Messe: all about automation Düsseldorf 2026, Stand 118, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: kein direkter Bereich; Sekundär: Electrical Insulation (verbaute Steuerungselektronik), Dosier-/Klebezellen als Anlagenbauer (E1 prüfen)
3. Gebiet: Rest Deutschland+Niederlande (Radevormwald, NRW)
4. Sitz und Fertigungsort: Albert-Einstein-Str. 6, 42477 Radevormwald (Messeverzeichnis-Snippet, S). Fertigung = Sitz (Sondermaschinenbau, S). Triage-Vorgabe "Köln" ist nicht belegt.
5. Website: unbekannt (in der Liste nicht angegeben, nicht gefunden; Messeprofil https://www.duesseldorf.allaboutautomation.de/en/exhibitors/jam-automation-gmbh-223493)
6. Was wird gebaut -> Bauteile: robotergestützte Sondermaschinen, Montage- und Prüfsysteme, "Werkzeugmaschinen-Montage mit Robotern"; ein Messetext nennt Cobot Melfa Assista für präzise Flüssigkeitsapplikation ("injections of liquids", S). Typisch vergossen/verklebt/gedichtet: verbaute Sensorik, Netzteile, Steuerelektronik in den Anlagen (A, Endprodukt-Regel, zugekauft); Dosier-/Klebezelle als Teil der Maschine (?, nicht belegt). JAM vergießt selbst vermutlich nicht.
7. Fertigung DE/AT/NL: Hoch, Stufe A (Sitzregel: Sondermaschinenbauer mit erkennbarem Standort, ca. 30 Mitarbeitende, keine Hinweise auf Auslagerung).
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: verbaute Sensorik/Netzteile Mittel (A), Steuerungselektronik Mittel (A), Cobot-Dosierzelle Mittel (?), Mechanik/Handling Niedrig (A). E1-Vorbehalt: Wenn JAM Dosieranlagen als Integrator verkauft, gilt Ausschluss E1 (Integratoren von Dosier-/Dispensing-Anlagen); Beleg dafür fehlt, Tina entscheidet.
9. Patentrecherche (Pflicht):
- Google Patents (per WebSearch, gemeinsame Anfrage mit INSEVIS/INperfektion/IXON "Patent Anmelder Gebrauchsmuster Vergussmasse"): keine Treffer zu JAM automation.
- Espacenet / DEPATISnet (per WebSearch, gleiche Anfrage und "JAM automation Radevormwald Cobot Flüssigkeitsdosierung ..."): keine Treffer; Datenbanken nicht direkt abgefragt.
- Ergebnis: keine Patente gefunden; kein Gegenbeweis.
10. Einstufung Tom: prüfenswert (Fertigung Hoch A, Verguss Mittel A), mit Vorbehalt E1 (Integrator)
11. Ampel: 
12. CRM-Status: neu (crm_abgleich.py "JAM automation GmbH": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Bietet JAM Dosier-/Klebe-/Vergusszellen als Produkt oder Kundenlösung (E1 Integrator)? Messeprofil und Website-Referenzen im Browser lesen. (b) Sitz klären: Radevormwald (Quellen) statt Köln (Vorgabe); Impressum und Handelsregister (Wuppertal) prüfen. Aktion: keine Ansprache vor Klärung (a).
14. Quellen:
- https://www.duesseldorf.allaboutautomation.de/en/exhibitors/jam-automation-gmbh-223493 (S, Messeprofil, Regel N5): "about 30" Mitarbeitende, robotergestützte Sondermaschinen, Prüf-/Montagesysteme; Abruf 2026-10-15.
- https://implisense.com/en/companies/jam-automation-gmbh-radevormwald-DE7D3BDIH932 (S, Snippet): Radevormwald, kleine Firma, Prokurist Jörg Demtröder; Abruf 2026-10-15.
- https://www.berlin.allaboutautomation.de/en/exhibitors/jam-automation-gmbh-202198/ (S, Messeprofil): Albert-Einstein-Str. 6, 42477 Radevormwald; Abruf 2026-10-15.
15. Größe/Umsatz: ca. 30 Mitarbeitende (Messeprofil, S); Bilanzsumme ca. 1 Mio. EUR (Implisense-Snippet, S); sonst unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag JAM); Websuche "JAM automation Radevormwald Cobot Flüssigkeitsdosierung Dosierzelle Klebstoff Nordson OR ViscoTec OR DOPAG OR Scheugenpflug" (kein JAM-Bezug zu einem Wettbewerber). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: TEILWEISE (S). JAM automation GmbH (Sondermaschinenbau), Albert-Einstein-Str. 6, 42477 Radevormwald; Register/Impressum nicht gelesen. Abweichung zur Triage-Vorgabe: Sitz Radevormwald, nicht Köln. Nicht vermischen mit JAM-Tech GmbH (Eibiswald, AT) und JAMI GmbH (Siegen).

## 8. Janitza electronics GmbH
1. Firma: Janitza electronics GmbH (Messe: all about automation Düsseldorf 2026, Stand 114, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Stromwandler, Messgeräte, Netzteile, Blindleistungsregler), nachrangig E-Mobility/Energie (Messtechnik für Netze)
3. Gebiet: Rest Deutschland+Niederlande (Lahnau, Hessen)
4. Sitz und Fertigungsort: Vor dem Polstück 6, 35633 Lahnau (Messe-Frankfurt-Verzeichnis, S). Entwicklung und Fertigung am Standort Lahnau laut Interview (S). Neubauprojekt mit zusätzlicher Produktionsfläche (industrial-production.de, S).
5. Website: https://www.janitza.com
6. Was wird gebaut -> Bauteile: Messgeräte, Netzanalysatoren (Power Quality), Stromwandler (Aufsteck-/Rogowski-, IP57-Spulen laut Händler-/Handbuch-Snippet), Blindleistungsregler, Energiedaten-Management (S). Typisch vergossen/verklebt/gedichtet (alle A): Stromwandler und Rogowski-Spulen (A, Block A Spulen/Wandler), Messelektronik und Netzteile (A, Block A/B), Geräte mit Frontdichtung (A, Block B), Kommunikations-Gateways (A, Block B). Konkreter Verguss nicht belegt.
7. Fertigung DE/AT/NL: Hoch, Stufe A (Sitzregel: Gerätebauer mit erkennbarem Standort, eigene Produkte, mittelständisch, keine Hinweise auf Auslagerung). Stützend S: Wirtschaftsforum "entwickelt und gefertigt" am Standort Lahnau; Stellenanzeige "Bestücker (THT)" Lahnau (Indeed-Snippet).
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Stromwandler, Messelektronik, Netzteile; Produkttyp Block A). Einzelbewertung: Stromwandler/Rogowski-Spulen Hoch (A), Netzteile Hoch (A), Messelektronik Mittel (A), Gehäuse/Frontdichtung Mittel (A), Gateways Mittel (A). Kein Gegenbeleg.
9. Patentrecherche (Pflicht):
- Google Patents (per WebSearch "site:patents.google.com Janitza electronics GmbH Gehäuse Vergussmasse OR potting OR Stromwandler"): kein Patent mit Anmelder Janitza gefunden; nur Fremdpatente zu vergossenen Wandlern (z. B. CH656249A5, DE3048285A1), keine Janitza-Zuordnung.
- Espacenet / DEPATISnet (per WebSearch "espacenet Janitza electronics applicant patent Lahnau EP"): kein Espacenet-Datensatz auffindbar; Datenbanken nicht direkt abgefragt.
- Ergebnis: keine Patente gefunden; kein Gegenbeweis. Anmelder-Varianten (Janitza, Eugen Janitza GmbH, Janitza Deutschland GmbH) nur über Websuche.
10. Einstufung Tom: interessant (Fertigung Hoch A, Verguss Hoch A)
11. Ampel: 
12. CRM-Status: neu (crm_abgleich.py "Janitza Electronics GmbH": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Werden in Lahnau Stromwandler/Rogowski-Spulen und Netzteile gefertigt und vergossen? Produktdatenblätter (Schutzart, Vergussmasse), Stellenanzeigen Lahnau (Fertigung, Montage) im Browser lesen. (b) Impressum der fertigenden Gesellschaft: Janitza electronics GmbH (Amtsgericht Wetzlar HRB 928) oder Janitza Deutschland GmbH (HRB 8716). (c) Aktuelle V-Quelle für die Fertigung in Lahnau (Karriereseite, Pressemeldung 2025). Aktion: Kandidat für Priorität nach Gegenlesen.
14. Quellen:
- https://www.wirtschaftsforum.de/portraits/janitza-electronics-gmbh/wie-moderne-messtechnik-die-energiewende-befoerdert (S, Snippet): Produkte "entwickelt und gefertigt" am Standort Lahnau; Abruf 2026-10-15.
- https://www.industrial-production.de/wirtschaft---unternehmen/energietechnik-janitza-electronics-knackt-die-500-mitarbeiter-marke.htm (S, Snippet): Neubauprojekt mit Produktionsfläche; Abruf 2026-10-15.
- https://light-building.messefrankfurt.com/frankfurt/en/exhibitor-search.detail.html/janitza-electronics-gmbh.html (S, Snippet): Vor dem Polstück 6, 35633 Lahnau; Abruf 2026-10-15.
- https://www.firminform.de/unternehmen/Janitza-electronics-GmbH-Lahnau-Waldgirmes (S, Snippet): Amtsgericht Wetzlar HRB 928; Abruf 2026-10-15.
- https://de.indeed.com/Janitza-Jobs (S, Snippet): Stelle "Bestücker (m/w/d)" Lahnau; Abruf 2026-10-15.
15. Größe/Umsatz: über 500 Beschäftigte (industrial-production.de-Titel "knackt die 500 Mitarbeiter-Marke", S; Karriereportale widersprüchlich 101-500 bzw. 501-1000); Umsatz unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Janitza); Websuche "Janitza Stromwandler Vergussmasse OR vergossen OR Epoxid Datenblatt Lahnau Fertigung Wandler" (nur allgemeine Vergussmassen-Seiten, kein Hersteller-Bezug); Websuche "Janitza electronics Lahnau Stellenanzeige Produktion ... Vergießen". Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: TEILWEISE belegt (S). Janitza electronics GmbH, Vor dem Polstück 6, 35633 Lahnau (Waldgirmes), Amtsgericht Wetzlar HRB 928 (firminform-Snippet); Impressum nicht gelesen. Keine Abweichung zur Liste. Getrennt führen: Janitza Deutschland GmbH (Lahnau, HRB 8716, Vertriebsgesellschaft, S).

## 9. Kaiser GmbH & Co. KG
1. Firma: Kaiser GmbH & Co. KG (Messe: all about automation Düsseldorf 2026, Stand 115, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Gasketing/Sealing (luftdichte Dosen, Dichtmanschetten, Dichtungseinsätze), nachrangig Electrical Insulation (Elektronik-Dosen, Brandschutz)
3. Gebiet: Rest Deutschland+Niederlande (Schalksmühle, NRW)
4. Sitz und Fertigungsort: Ramsloh 4, 58579 Schalksmühle (Messe-Frankfurt-Snippet, S). Fertigung am Sitz: Stellenanzeige Schalksmühle sucht Einrichter für Spritzgießmaschinen (Arburg, Engel; StepStone-Snippet, S). Weitere Standorte (4 europäische laut Triage) und Töchter AGRO (CH), HELIA (BE), ATTEMA (NL); Fertigungsrolle der Töchter nicht geprüft.
5. Website: https://www.kaiser-elektro.de
6. Was wird gebaut -> Bauteile: Geräte-, Verbindungs-, Hohlwand- und Betonbaudosen, luftdichte Dosen, Feuchtraumtechnik, Brandschutzsysteme, Kabelverschraubungen, Electronic-Dose (S, Händler- und Messeseiten, Flyer Feuchtraumtechnik 2024). Typisch verklebt/gedichtet/vergossen: Dichtungseinsätze/Dichtmanschetten (A, Gasketing), luftdichte Dosen mit Dichtlippen/Kragen (A, Block B), Brandschutz-Elemente (A). Das Produkt wird vor allem mechanisch/spritzgegossen; Verguss/Verklebung durch Kunden bei der Montage (Kleberkragen laut Flyer, S) ist keine eigene Fertigung.
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Konzern/Gruppe mit mehreren Standorten (V nötig); Spritzguss in Schalksmühle nur über Stellenanzeigen-Snippet (S). Produkt-zu-Werk-Zuordnung offen.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Dichtungseinsätze/Dichtmanschetten Mittel (A, Dichtung, Dosier- oder Schaumdichtung), luftdichte Dosen Mittel (A), Electronic-Dose Niedrig (A), Standard-Installationsdosen Niedrig (A), Brandschutz-Systeme Niedrig (A).
9. Patentrecherche (Pflicht):
- Google Patents (per WebSearch "site:patents.google.com Kaiser GmbH & Co KG Schalksmühle Dichtung OR Klebung OR Einbaudose"): Anmelder Kaiser GmbH & Co KG: DE2926078A1 "Unterputzdose für den Betonbau" (1979, Anmeldung, Status alt, Rechtsstand nicht geprüft), DE2526890A1 "Elektrische Einbaudose" (1975), DE4403238C1 "Variables Installationssystem für Decken und Wände", DE19825115A1 "Elektrische Einbaudose für den Betonbau". Kein Verguss-/Klebe-Kern.
- Espacenet / DEPATISnet (per WebSearch "Kaiser GmbH & Co KG Schalksmühle Patent ..."): keine Datenbankseite erreichbar; nicht direkt abgefragt. Rechtsstand (erloschen/aktiv) nicht geprüft; alte Patente vermutlich erloschen (Einschätzung, ?).
- Ergebnis: Patente vorhanden (Installationsdosen), keines mit Verguss/Dichtung/Klebung als Kern gefunden; schwaches Signal.
10. Einstufung Tom: prüfenswert (Fertigung Mittel S, Verguss Mittel A)
11. Ampel: 
12. CRM-Status: unklar. crm_abgleich.py "Kaiser GmbH & Co. KG": Präfix-Treffer bekannte_firmen_DE-AT-NL.txt Zeile 1247 "Kaiser Elektroplanung GmbH [DE]" (laut Triage andere Firma: Planungsbüro); Töchter AGRO, ATTEMA: kein Treffer; "HELIA": Präfix-Treffer Zeile 1008 "Heliatek GmbH [DE]" (anderer Name, kein Bezug). Jey bestätigt, dass Kaiser Elektroplanung nicht dieselbe Einheit ist.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) CRM-Zeile "Kaiser Elektroplanung GmbH": Ort und Tätigkeit prüfen, andere Firma bestätigen. (b) Werden die luftdichten Dosen/Dichtungseinsätze in Schalksmühle gefertigt und wie wird gedichtet (Schaumdichtung, Dosierung)? Produktdatenblatt luftdichte Dosen 1040-01, Stellenanzeigen Schalksmühle im Browser lesen. (c) Impressum/Register Amtsgericht Iserlohn HRA 3479 gegenlesen. Aktion: erst nach (a) ansprechen.
14. Quellen:
- https://light-building.messefrankfurt.com/frankfurt/de/ausstellersuche.detail.html/kaiser-gmbh--co-kg.html (S, Snippet): "Kaiser GmbH & Co. KG, Ramsloh 4, 58579 Schalksmühle"; Abruf 2026-10-15.
- https://www.stepstone.de/cmp/de/kaiser-gmbh-%26-co-kg-5055393/jobs (S, Snippet): Einrichter Spritzgießmaschinen (Arburg, Engel); Abruf 2026-10-15.
- https://assets.kaiser-elektro.de/media/18/18916/KAISER_Flyer_Feuchtraumtechnik_2024_DE_web.pdf (S, Snippet): Dichtschicht/Kragen wird an die Wand geklebt; Abruf 2026-10-15.
- https://patents.google.com/patent/DE2926078A1/cg-RX-API-DMAC10.html (S, Snippet): Anmelder Kaiser GmbH & Co KG, "Unterputzdose für den Betonbau"; Abruf 2026-10-15.
- bekannte_firmen_DE-AT-NL.txt Zeile 1247: "Kaiser Elektroplanung GmbH [DE]"; Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Kaiser; Treffer "TU Kaiserslautern" Falschtreffer); Websuche "Kaiser Schalksmühle Elektro Dosen Fertigung Spritzguss Dichtung Dosieranlage OR Klebstoff Sonderhoff OR Henkel OR Nordson" (kein Wettbewerberbezug). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: TEILWEISE belegt (S). KAISER GmbH & Co. KG, Ramsloh 4, 58579 Schalksmühle; persönlich haftende KAISER Verwaltungs GmbH (AG Iserlohn HRB 3972), KG: AG Iserlohn HRA 3479 (Sekundärdokument-Snippet), Geschäftsführer Burkard Kaiser, Steffen Oellers; Impressum nicht gelesen. Keine Abweichung zur Liste. Gleichnamige CRM-Firma Kaiser Elektroplanung GmbH ist nach Triage eine andere Firma, nicht vermischt; weitere Namensvettern (KAISER+KRAFT, Kaiser Werkzeug) nicht mit dieser Firma gleichzusetzen.

## 10. Kalitec Verbindungstechnik GmbH
1. Firma: Kalitec Verbindungstechnik GmbH (Messe: all about automation Düsseldorf 2026, Stand 143, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: keiner im Kern (Handel); allenfalls Electrical Insulation, falls Kabelkonfektion überspritzt/vergossen
3. Gebiet: Rest Deutschland+Niederlande (Solingen, NRW)
4. Sitz und Fertigungsort: Lindgesfeld 8h, 42653 Solingen (Telefonbuch-Snippet, S). Fertigungsort: nicht belegt; Eigenfertigung nicht belegt.
5. Website: https://www.kabelschuhe-shop.de
6. Was wird gebaut -> Bauteile: Online-Industriegroßhandel (seit 2006) für Kabelschuhe, Steckverbinder, Leitungen, Werkzeuge; Kabelkonfektion "nach Maß" im Angebot (S, Messeprofile). Implisense-Snippet: "technischer Industriehandel für elektronische und elektromechanische Bauteile", Schwerpunkt Kabelschuhe, Steckverbinder, konfektionierte Kabel (S). Typisch vergossen/überspritzt: konfektionierte Leitungen, falls Eigenfertigung (A, Block A, aber nicht belegt); Handelsware (Kabelschuhe, Steckverbinder) wird nicht von Kalitec vergossen.
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Selbstbeschreibung und Branchenprofil sind Großhandel/Shop; Konfektion könnte im Haus sein, ist aber nicht belegt (Triage ebenso).
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe A (Händler ohne belegte Eigenfertigung, Wissensbasis Block C). Einzelbewertung: Konfektionierte Leitungen Mittel nur falls Eigenfertigung (?), Kabelschuhe/Steckverbinder (Handelsware) Niedrig (A), Werkzeuge Niedrig (A). Höchstes belegbares Bauteil: Niedrig.
9. Patentrecherche (Pflicht):
- Google Patents (per WebSearch "Kalitec Verbindungstechnik Patent OR Gebrauchsmuster Kabelschuh Solingen"): keine Treffer mit Anmelder Kalitec; nur Fremdpatente zu Kabelschuhen (z. B. Bosch-Altpatent, kein Kalitec-Bezug).
- Espacenet / DEPATISnet (per WebSearch, gleiche Anfrage mit Stichwort DEPATISnet): keine Treffer; Datenbanken nicht direkt abgefragt.
- Ergebnis: keine Patente oder Gebrauchsmuster gefunden; kein Gegenbeweis.
10. Einstufung Tom: kein Fertiger (Händler, Eigenfertigung unbelegt, möglicher Ausschluss E2; Tina entscheidet)
11. Ampel: 
12. CRM-Status: neu (crm_abgleich.py "Kalitec Verbindungstechnik GmbH": kein Treffer)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Fertigt Kalitec Leitungen/Konfektion selbst in Solingen (Werkstatt, Stellenanzeigen "Kabelkonfektion", Impressum/Unternehmensseite)? Wenn nein: Händler (E2), nicht weiter verfolgen. Aktion: nicht priorisieren.
14. Quellen:
- https://www.duesseldorf.allaboutautomation.de/en/exhibitors/kalitec-verbindungstechnik-gmbh-221274/ (S, Messeprofil, Regel N5): „Online-Industriegroßhandel“ seit 2006, Kabelkonfektion nach Maß; Abruf 2026-10-15.
- https://implisense.com/en/companies/kalitec-verbindungstechnik-gmbh-solingen-DEQ3N39IY129 (S, Snippet): „technischer Industriehandel“ mit elektronischen und elektromechanischen Bauteilen; Abruf 2026-10-15.
- https://adresse.dastelefonbuch.de/Solingen/2-Solartechnik-Kalitec-Verbindungstechnik-GmbH-Solingen-Lindgesfeld.html (S, Snippet): Lindgesfeld 8h, 42653 Solingen; Abruf 2026-10-15.
15. Größe/Umsatz: Bilanzsumme ca. 2 Mio. EUR (Implisense-Snippet, S); Mitarbeiterzahl unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Kalitec); Websuche "Kalitec Verbindungstechnik GmbH Solingen Impressum Kabelkonfektion Eigenfertigung" (Händlerprofil, keine Fertigung, daher keine weitere Wettbewerber-Suche sinnvoll). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: TEILWEISE (S). Kalitec Verbindungstechnik GmbH, Lindgesfeld 8h, 42653 Solingen-Gräfrath (Telefonbuch-/Implisense-Snippet); Triage "Solingen" damit gestützt. Impressum, Register und Geschäftsführer nicht gefunden. Keine Abweichung.

## nicht aufgenommen (bereits bekannt / unklar)
- Keine Firma BEKANNT (crm_abgleich.py für alle 10 Firmen und Konzern-/Schwesternamen: igus SE & Co. KG, SAR Group, item, INSEVIS Vertriebs GmbH, AGRO, HELIA, ATTEMA).
- Unklar: Kaiser GmbH & Co. KG (gefunden: "Kaiser GmbH & Co. KG", Schalksmühle) gegenüber CRM-Schreibweise "Kaiser Elektroplanung GmbH [DE]" (bekannte_firmen Zeile 1247); steht in diesem Batch trotzdem als eigener Block (Messe-Vollständigkeit), CRM-Status unklar, Jey bestätigt die Einheit. Falschtreffer: "HELIA" ~ "Heliatek GmbH" (Zeile 1008), anderer Name.

## Einschränkungen
- Browser nicht verfügbar (keine Chrome-Werkzeuge in diesem Lauf). WebFetch war nicht nutzbar (getaddrinfo ENOTFOUND für patents.google.com, inperfektion.de, ima-tec-gmbh.com, insevis.com, ixon.cloud, janitza.com). Dadurch keine Stufe-V-Aussage; Impressen und Datenblätter wurden nicht gelesen; alle tragenden Aussagen sind S oder A. Tina muss insbesondere igus, Janitza (interessant) sowie ima-tec, JAM, INSEVIS, Kaiser im Browser gegenlesen.
- Patentrecherche (Feld 9): Google Patents, Espacenet und DEPATISnet konnten nicht direkt mit Anmelderfilter abgefragt werden; es wurden jeweils zwei bis drei WebSearch-Anfragen je Firma ausgeführt (Google-Patents-Suchbegriffe sowie Espacenet-/DEPATISnet-Suchbegriffe). Diese Suchen belegen Patent-Treffer nur über Suchmaschinen-Snippets; ein "keine Treffer" ist daher schwächer als in früheren Batches und kein Gegenbeweis. Rechtsstand für Kaiser-Patente nicht geprüft. Die eigentlichen Datenbanksuchen (Anmelderfilter plus enge Suche potting compound OR Vergussmasse, Konzern-/Schwester-Varianten) fehlen und sind nachzuholen; Batch gilt hinsichtlich Feld 9 als nur eingeschränkt belastbar.
- Websuche-Limit: je Firma nur wenige Anfragen; Größe/Umsatz nicht gezielt gesucht.
- Nicht verifizierte Triage-Hinweise: Sitz IMPADY (Darmstadt/Hoppstädten-Weiersbach) bleibt offen; Sitz IXON (Beugen/Overloon) offen; JAM-Sitz Radevormwald nur über Messeprofil/Verzeichnis (S).
- Kontaktsuche gemäß Regel K nicht durchgeführt; keine Ansprechpartner notiert (Zufallsfunde: Geschäftsführer-Namen aus Verzeichnissen nur in Feld 17, ohne Kontaktdaten).
