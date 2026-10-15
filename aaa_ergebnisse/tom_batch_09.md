# Tom Batch 09 – all about automation Düsseldorf 2026 (aaa, Messemodus Regel N)
Erstellt: 2026-10-15 (Tom, Stufe 1, Version 2, getrennter Agent, keine Ampel). Eingabe: aaa_batches_v2/pruef_08.md, 10 Firmen. Halle ist in der Liste nicht angegeben, Feld 1 trägt nur die Standnummer.
Alle Abrufdaten: 2026-10-15. Umgebung: WebFetch und Chrome NICHT verfügbar. Alle Aussagen stammen aus WebSearch-Zusammenfassungen und Snippets, daher durchgehend Stufe S (nicht V). Stufe A = aus Produkttyp abgeleitet. Stufe ? = angenommen. Keine einzige Aussage in diesem Batch ist Stufe V; Quellenzitate in Feld 14 sind Ausschnitte aus Suchergebnissen (S). Triage-Angaben (Stand, Sitz, Produkttyp) sind unverifiziert und wurden nur dort übernommen, wo die Suche sie stützte.
Budget: 30 WebSearch-Abfragen, je Firma 3 (Produkt/Fertigungsort, Patent, Wettbewerber).
Messe-Signal (Regel N2): Keine Wettbewerber aus Regel E1 (Scheugenpflug, DOPAG, Nordson, ViscoTec, bdtronic, RAMPF, Sonderhoff, Hilger u. Kern, Musashi, Marco, GONANO, Henkel, DELO, ELANTAS, Wacker, Sika, Atlas Copco, Graco u. a.) in aaa_duesseldorf_2026.csv (Grep 2026-10-15; einziger Zufallstreffer "Ottobrunn" bei Panasonic, kein Wettbewerber).
Patent-Hinweis (gilt für alle Firmen, Feld 9): Die Patentdatenbanken selbst (Google Patents, Espacenet, DEPATISnet) konnten ohne Browser NICHT direkt mit Anmelderfilter abgefragt werden. Je Firma lief eine WebSearch mit Anmelder und Verguss-/Dichtungsbegriffen, die Treffer aus Google Patents, EPO und Justia liefern kann. Das ist schwächer als die Pflichtsuche nach F5 (zwei Datenbanken im Browser). Regel F5 ist damit nur formal und schwach erfüllt, der Batch ist bei Feld 9 nachzuholen (siehe Einschränkungen).

## 1. Möller GmbH
1. Firma: Möller GmbH (Messe: all about automation Düsseldorf 2026, Stand 221, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: kein klarer Bereich erkennbar (Produkt unbekannt)
3. Gebiet: Rest Deutschland+Niederlande (Diepholz, Niedersachsen, laut Messeliste PLZ 49356)
4. Sitz und Fertigungsort: Im Fange 1, 49356 Diepholz (Verzeichniseintrag, S). Fertigungsort nicht belegt.
5. Website: unbekannt
6. Was wird gebaut: nicht belegt. Verzeichnis ordnet die Adresse unter "Elektrogeräte und -bedarf" ein, vermutlich Handel (S, Triage bestätigt durch Suche nicht). Keine Bauteile ableitbar (? ).
7. Fertigung DE/AT/NL: Niedrig, Stufe ?. Begründung: weder Produkt noch Fertigung gefunden; Verzeichniskategorie deutet auf Handel.
8. Verguss/Bonding (höchstes Bauteil): Niedrig, Stufe ?. Keine Bauteile bekannt; Einzelbewertung nicht möglich. Abgrenzung: Möller Group GmbH & Co. KG (Bielefeld, Kunststoff/Gummi/Metall) und Möller GmbH & Co. KG (Meschede, Bodensysteme) sind andere Firmen und nicht vermischt.
9. Patentrecherche (Pflicht): Websuche mit Abfragerichtung Google Patents / Espacenet / DEPATISnet (Datenbanken nicht direkt abgefragt, siehe Patent-Hinweis): Anmelder "Möller GmbH" Diepholz + Vergussmasse OR potting OR Dichtung: keine Treffer mit Möller-Anmelder aus Diepholz; nur Altpatente anderer Anmelder (z. B. DE19517735B4 Dichtflächenverbindung, andere Firma). Zweite Suche (Google Patents / Espacenet / DEPATISnet, Anmelder-Feld) fehlt.
10. Einstufung Tom: unwahrscheinlich (vorläufig; Fertigung Niedrig ?, möglicher Ausschluss E2 Händler, Tina entscheidet)
11. Ampel:
12. CRM-Status: unklar. crm_abgleich.py "Möller GmbH" "Möller-Preussler": PRAEFIX-Treffer bekannte_firmen_DE-AT-NL.txt Zeile 1642 "Möller-Preussler Transformatoren GmbH [DE]" (Kern-Name "moeller preussler" vs. "moeller"). Kein Ortsabgleich möglich; Triage nennt Namensähnlichkeit, wahrscheinlich andere Firma. kundendatenbank_export.txt: kein Treffer.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Identität: Was ist die Möller GmbH, Im Fange 1, Diepholz (eigene Website, Impressum, Handelsregister Walsrode/Diepholz)? (b) Ist sie mit Möller-Preussler Transformatoren GmbH verbunden (Ort dieser CRM-Firma prüfen)? (c) Produkte und Fertigung. Aktion: nicht kontaktieren, bis Identität geklärt.
14. Quellen:
- https://www.dasoertliche.de/Themen/Elektro/Diepholz.html (S, Suchsnippet): „Möller GmbH“ unter Elektro Diepholz, Im Fange 1; Abruf 2026-10-15.
- bekannte_firmen_DE-AT-NL.txt Zeile 1642 (CRM): „Möller-Preussler Transformatoren GmbH [DE]“; Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Möller); Websuche "Möller GmbH Diepholz Elektro Nordson OR Scheugenpflug OR DOPAG OR Henkel Referenz" (nur Bodo Möller Chemie, Offenbach, Henkel-Distributor, andere Firma). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: NICHT belegt. Vorgabe "Möller GmbH, Diepholz". Nur Verzeichnisadresse (S), keine Website, kein Impressum, kein Register. Gleichnamige Firmen (Möller Group Bielefeld, Möller Meschede, Bodo Möller Chemie Offenbach) nicht vermischt. Ampel höchstens Gelb (Tabellenzeile 2).

## 2. Müller Maschinentechnik GmbH
1. Firma: Müller Maschinentechnik GmbH (Messe: all about automation Düsseldorf 2026, Stand 534, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Ventil-/Steuerungselektronik in Handhabungsanlagen), nachrangig Gasketing/Sealing (Pneumatik)
3. Gebiet: Rest Deutschland+Niederlande (Düren, NRW)
4. Sitz und Fertigungsort: Felix-Wankel-Straße 11, 52351 Düren (Stellenanzeige, S); zweiter Standort seit 2019 Distelrather Straße, Düren (Firmenprofil, S). Messeliste: PLZ 52321 (Abweichung zur PLZ der Stellenanzeige 52351, siehe Feld 17).
5. Website: mueller-maschinentechnik.de (unbestätigt, nicht geöffnet)
6. Was wird gebaut: "Baugruppen und Anlagen zur Automatisierung von Montage- und Handhabungsprozessen" (S), Handhabungssysteme (z. B. Fahrachse mit 6-Achs-Roboter für Walzwerk), Greifersysteme, Pneumatik- und Ventiltechnik (S). Typisch vergossen/verklebt/gedichtet (alles Stufe A): Magnetventilspulen und Ventilelektronik in Pneumatik (A, Block A), Steuerungs-/Sensorik-Einbauten (A, Block B), Greifer/Mechanik nicht. Ob selbst vergossen wird, ist nicht belegt (zugekaufte Teile zählen nach Endprodukt-Regel).
7. Fertigung DE/AT/NL: Hoch, Stufe A (Sitzregel: Maschinenbauer mit zwei Standorten beide in Düren, eigene Anlagen, keine Hinweise auf Auslagerung). Stützend S: Profil "entwickelt und fertigt maßgeschneiderte Baugruppen und Anlagen", über 50 Mitarbeiter, Stellenanzeige Mechatroniker Düren.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Magnetventile/Ventilspulen Mittel (A, zugekauft/verbaut), Steuerungs- und Sensorikbauteile Mittel (A), Roboterzelle/Handling-Mechanik Niedrig (A), Greifer Niedrig (A), Pneumatikdichtungen Niedrig (A). Kein Beleg für Eigenverguss.
9. Patentrecherche (Pflicht): Websuche mit Abfragerichtung Google Patents / Espacenet / DEPATISnet (Datenbanken nicht direkt abgefragt): Anmelder "Müller Maschinentechnik" Düren + Greifer OR Ventil OR Dichtung: keine Treffer mit diesem Anmelder; Zufallstreffer anderer Anmelder (z. B. DE2654494B2 Greifer für einen Manipulator, EP4067709C0 Membranventil) nicht zugeordnet. Zweite, datenbankdirekte Suche fehlt. Ein Treffer "Langhubgreifer GRR" ist ein Gemeinschaftsprodukt mit PHD, kein Patent.
10. Einstufung Tom: prüfenswert (Fertigung Hoch A, Verguss Mittel A)
11. Ampel:
12. CRM-Status: neu (Hinweis). crm_abgleich.py "Müller Maschinentechnik GmbH" "Müller Industrie-Elektronik": Kern-Name "mueller maschinentechnik" ohne identischen Treffer; nur GLEICHE WORTWURZEL (bekannte_firmen Zeilen 1673 "mueller-ie", 1674 "Müller Industrie-Elektronik GmbH", 1675/1676 Müller Werbemittel). Laut Triage erkennbar anderes Unternehmen; Ort der CRM-Firmen im Export nicht angegeben, deshalb Ortsabgleich nicht möglich. kundendatenbank_export.txt: kein Treffer.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Welche Ventile/Elektronik werden in Düren selbst montiert oder gefertigt, und wird dort vergossen oder geklebt (Produktseiten, Stellenanzeigen Düren, Fotos)? (b) Impressum und Register (Amtsgericht Düren), PLZ 52321 vs. 52351. (c) Gehört "Müller Industrie-Elektronik" im CRM zu einem anderen Ort? Aktion: Beobachtung.
14. Quellen:
- https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1206114850-S (S, Suchzusammenfassung): „System- und Komponentenlieferant auf dem Gebiet Handhabungstechnik, Pneumatik und Ventiltechnik“; Abruf 2026-10-15.
- https://www.industrial-production.de/firma/mueller-maschinentechnik-gmbh.htm (S, Suchzusammenfassung): „Seit 2019 gibt es einen zweiten Standort“ (Distelrather Straße, sinngemäß); Abruf 2026-10-15.
- bekannte_firmen_DE-AT-NL.txt Zeilen 1673 bis 1676 (CRM, nur Wortwurzel); Abruf 2026-10-15.
15. Größe/Umsatz: "über 50 Mitarbeiter", gegründet 2000 (Firmenangabe, S); Umsatz unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Müller Maschinentechnik); Websuche "Müller Maschinentechnik Düren Dosieranlage OR Klebstoff OR Nordson OR Scheugenpflug OR Henkel OR DOPAG" (nur andere Firmen, kein Bezug). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: teilweise belegt (S). Name, Ort Düren, Gründung 2000 passen zur Vorgabe. Adresse laut Stellenanzeige 52351 Düren, Messeliste 52321 (Abweichung der PLZ, Impressum nicht gelesen). Rechtsform GmbH und Register nicht belegt. Nicht verwechseln mit Müller Werkzeugmaschinen Robotik & Handelshaus e.K. und Müller Martini.

## 3. Mütron Müller GmbH & Co. KG
1. Firma: Mütron Müller GmbH & Co. KG (Messe: all about automation Düsseldorf 2026, Stand 305, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Kabelkonfektion mit Hotmelt-Umspritzung, Baugruppen), nachrangig Gasketing
3. Gebiet: Rest Deutschland+Niederlande (Achim, Niedersachsen, laut Messeliste PLZ 28832; Sitz in Quellen nicht bestätigt)
4. Sitz und Fertigungsort: Achim laut Messeliste; in den Suchergebnissen nicht bestätigt (S). Fertigungsort nicht belegt.
5. Website: muetron.de (unbestätigt, nicht geöffnet)
6. Was wird gebaut: Messeprofil (aaa 2024/2025, S): Vertrieb elektromechanischer Komponenten, daneben Herstellung von Kabelsystemen und Geräteaufbau. Branchenverzeichnis (S): "kundenspezifische Elektronikbaugruppen und Kabelbäume", Kabelkonfektion mit Crimpen, Löten und Hotmelt-Umspritzung für Medizintechnik, Kran- und Lkw-Technik. Messeprodukt "Hotmelt overmolding of wires and connectors" (berlin.allaboutautomation.de, Titel im Snippet, S). Typisch vergossen/verklebt: umspritzte Kabel/Stecker Hoch (A, Block A; Hotmelt-Niederdruckumspritzung ist Umspritzen, nicht zwingend Harzverguss), Baugruppen/Geräteaufbau Mittel (A, Block B).
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Eigenfertigung (Kabelsysteme, Geräteaufbau) nur aus Messeprofil und Verzeichnis (S); Standort nicht bestätigt; Distributor mit Eigenfertigung, daher V nötig (Sitzregel greift nicht).
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Produkttyp konfektionierte, umspritzte Kabel/Stecker, Block A; Messeprodukt "Hotmelt overmolding" S). Einzelbewertung: Hotmelt-umspritzte Kabel/Stecker Hoch (A), Kabelbäume ohne Umspritzung Mittel (A), Elektronikbaugruppen Mittel (A), Distributionsware (zugekauft, nicht gebaut) Niedrig (A).
9. Patentrecherche (Pflicht): Websuche mit Abfragerichtung Google Patents / Espacenet / DEPATISnet (Datenbanken nicht direkt abgefragt): Anmelder "Mütron Müller" Achim + Kabel Umspritzung OR Vergussmasse: keine Treffer mit diesem Anmelder; nur allgemeine Kabel-Verguss-Patente anderer Anmelder (z. B. AT233643B Kabelgarnitur, DE3035183A1 Muffenkörper, nicht zugeordnet). Zweite, datenbankdirekte Suche (Anmelderfilter) fehlt.
10. Einstufung Tom: prüfenswert (Fertigung Mittel S, Verguss Hoch A); Vorbehalt: Distributor (E2), nur wenn Eigenfertigung am Standort belegt wird
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "Mütron Müller GmbH & Co. KG" "Muetron": kein Treffer in beiden Dateien)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Sitz: Ist Achim der Sitz und die Fertigung (Impressum muetron.de, Handelsregister Walsrode/Achim)? (b) Wird die Hotmelt-Umspritzung in Eigenfertigung gemacht (Produktseite "Hotmelt overmolding of wires and connectors", Stellenanzeigen, Maschinen)? (c) Umfang der Eigenfertigung gegenüber Handel. Aktion: nicht kontaktieren, bis (b) geklärt.
14. Quellen:
- https://www.duesseldorf.allaboutautomation.de/en/?p=351944 (S, Suchzusammenfassung Messeprofil): „vertreibt hauptsächlich elektromechanische Komponenten und fertigt Kabelsysteme“ (sinngemäß, Quelle gibt Englisch); Abruf 2026-10-15.
- https://bouncewatch.com/company/mutron-mueller (S, Verzeichnis): „Hotmelt“ in der Kabelkonfektion, gegründet 1961, ca. 16 Mitarbeiter (sinngemäß); Abruf 2026-10-15.
- https://www.berlin.allaboutautomation.de/en/products/hotmelt-overmolding-of-wires-and-connectors-306375/ (S, Titel im Snippet): „Hotmelt overmolding of wires and connectors“; Abruf 2026-10-15.
15. Größe/Umsatz: ca. 16 Mitarbeiter (Aggregator, S, möglicherweise veraltet); Umsatz unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Mütron); Websuche "Mütron Müller Achim Heißkleber Hotmelt Maschine Nordson OR Henkel Technomelt OR Loctite OR Scheugenpflug" (keine Treffer zu Mütron). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: NICHT belegt. Vorgabe "Mütron Müller GmbH & Co. KG, Achim". Name stimmt mit Messeprofilen überein (S), Sitz Achim in keiner gelesenen Quelle bestätigt, kein Impressum, kein Register. Ampel höchstens Gelb (Tabellenzeile 2).

## 4. NACHI EUROPE GmbH
1. Firma: NACHI EUROPE GmbH (Messe: all about automation Düsseldorf 2026, Stand 222, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Servomotoren/Antriebe der Roboter), nachrangig Gasketing (Dichtapplikation durch Roboter ist Anwendung, nicht Produkt)
3. Gebiet: Rest Deutschland+Niederlande (Krefeld, NRW)
4. Sitz und Fertigungsort: Bischofstraße 99, 47809 Krefeld (Verzeichnis, S); Krefeld = europäische Zentrale und Logistikzentrum, Vertrieb/Service (S). Werke der Gruppe in Tschechien (Katalog, S). Fertigung in Krefeld nicht belegt.
5. Website: nachi.de (unbestätigt, nicht geöffnet)
6. Was wird gebaut: Industrieroboter, Hydraulik- und Werkzeugkomponenten der Nachi-Fujikoshi Corp. (Japan); Krefeld laut Katalog "logistics center … hub for European distribution" (S). Typisch vergossen (Stufe A, Produkttyp): Servomotoren/Antriebe und Robotersteuerungen (A, Block A), Hydraulikventile mit Magnetspulen (A, Block A). Welche Einheit wo fertigt, ist nicht belegt (nur Produkttyp der Gruppe).
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Krefeld wird als Vertrieb, Service und Logistikzentrum beschrieben; Europa-Werk in Tschechien genannt (Hinweis auf Fertigung im Ausland); keine Fertigungsangabe für Krefeld. Konzern/Marke: V nötig, nicht vorhanden.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Servomotoren/Antriebe der Gruppe, Block A). Einzelbewertung: Servomotoren Hoch (A), Hydraulikmagnetventile Hoch (A), Robotersteuerung Mittel (A), Mechanik/Getriebe Niedrig (A).
9. Patentrecherche (Pflicht): Websuche mit Abfragerichtung Google Patents / Espacenet / DEPATISnet (Datenbanken nicht direkt abgefragt): Anmelder "Nachi Europe" OR "Nachi-Fujikoshi" + encapsulation OR potting OR sealing OR servo motor: kein Treffer mit Nachi als belegtem Anmelder. Treffer ohne belegten Nachi-Anmelder: US 10116184 und US 10069371 "Robot having isolated stator and encoder" (Anmelder im Snippet nicht genannt), EP4211368A4 "A seal structure for protecting a motor of a robot" (laut Snippet ABB, nicht Nachi). Nachi-Katalog "robot sealing" betrifft Dichtraupen-Applikation, kein Patent. Zweite, datenbankdirekte Suche (Anmelder "Nachi-Fujikoshi", Gruppe) fehlt; Rechtsstand nicht geprüft.
10. Einstufung Tom: unwahrscheinlich (Fertigung Niedrig S; Vertriebs-/Servicegesellschaft, möglicher Ausschluss E2/E3, Tina entscheidet)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "NACHI EUROPE GmbH" "Nachi" "Nachi-Fujikoshi Corp" "Nachi-Fujikoshi": kein Treffer; Konzernabgleich Regel M ausgeführt)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Gibt es in Krefeld Montage, Fertigung oder Reparatur/Umbau von Antrieben (Stellenanzeigen Krefeld, nachi.de Standortseite, Impressum)? Wenn nur Vertrieb/Service/Logistik: Einstufung "kein Fertiger". Aktion: nicht weiter verfolgen, bis ein Fertigungsbeleg vorliegt.
14. Quellen:
- https://pdf.directindustry.com/pdf/nachi-europe/company-profile/18417-9249.html (S, Suchzusammenfassung): „logistics center in Krefeld“ als Drehscheibe für den europäischen Vertrieb, Fabrik in Tschechien (sinngemäß); Abruf 2026-10-15.
- https://www.industrial-production.de/zulieferer/nachi-verstaerkt-fokus-auf-den-europaeischen-markt.htm (S, Suchzusammenfassung): „über 70“ Techniker, Ingenieure, Kaufleute und Vertriebsmitarbeiter (sinngemäß); Abruf 2026-10-15.
15. Größe/Umsatz: über 70 bis 80 Mitarbeiter (Artikel 2017 und Stellenanzeige, S; Verzeichnisse widersprüchlich: 77 bis 500+); Umsatz unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Nachi); Websuche "Nachi Robotics Sealing Dispensing robot Nordson OR Graco OR Scheugenpflug OR DOPAG Partner Europe Krefeld" (keine Partnerschaft belegt; Yaskawa-Seite zu Dosierrobotern ohne Nachi-Bezug). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: teilweise belegt (S). Name, Krefeld, Bischofstraße 99 passen (Verzeichnis, Stepstone-Profil). Ein Snippet nennt zusätzlich eine UK-Adresse (Birmingham) für "Nachi Europe", vermutlich andere Einheit. Impressum und Register (Amtsgericht Krefeld) nicht gelesen.

## 5. Niederrhein Automation GmbH
1. Firma: Niederrhein Automation GmbH (Messe: all about automation Düsseldorf 2026, Stand 602, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Gasketing/Sealing (Schaltschrankbau), nachrangig Electrical Insulation (Steuerungs- und Antriebstechnik)
3. Gebiet: Rest Deutschland+Niederlande (Wegberg, NRW, laut Messeliste PLZ 41844; Sitz laut Triage nicht bestätigt)
4. Sitz und Fertigungsort: Wegberg laut Messeliste; die Suche fand keine Firmenseite, kein Impressum, keine Adresse (S). Fertigungsort nicht belegt.
5. Website: unbekannt (keine gefunden)
6. Was wird gebaut: laut Triage Systemintegrator/Anlagenbau: Steuerungstechnik, Schaltschrankbau, Robotik, Bildverarbeitung, Sondermaschinen (Messeprofil, S, nicht erneut gelesen). Typisch vergossen/verklebt/gedichtet (Stufe A): Schaltschrank-Dichtungen und Gehäuse (A, Block B FIPFG), Steuerungs- und Antriebskomponenten (zugekauft, A, Block B), Sondermaschinen-Mechanik Niedrig.
7. Fertigung DE/AT/NL: Mittel, Stufe ?. Begründung: Integrator/Schaltschrankbau am Sitz plausibel, aber Standort, Firma und Eigenfertigung in keiner Quelle belegt; Sitzregel nicht anwendbar (Identität offen).
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Schaltschrankdichtung/Gehäuse Mittel (A), Steuerungs-/Antriebselektronik verbaut Mittel (A), Bildverarbeitungs-/Sensorikkomponenten Mittel (A), Sondermaschinen-Mechanik Niedrig (A).
9. Patentrecherche (Pflicht): Websuche mit Abfragerichtung Google Patents / Espacenet / DEPATISnet (Datenbanken nicht direkt abgefragt): Anmelder "Niederrhein Automation" Wegberg + Patent OR Gebrauchsmuster: keine Treffer; nur Wegberger Anmelder anderer Firmen (z. B. Carl Walther, W. Schlafhorst, Aisin Seiki laut patentleaderboard-Snippet). Zweite, datenbankdirekte Suche fehlt.
10. Einstufung Tom: prüfenswert (schwach: Fertigung Mittel ?, Verguss Mittel A); Vorbehalt Identität und Integrator-Eigenschaft (möglicher Ausschluss E2)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "Niederrhein Automation GmbH": kein Treffer in beiden Dateien). Partner MABRI.VISION laut Triage nicht abgeglichen (nicht Konzern).
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Identität: Gibt es eine Firmenseite/Impressum und einen Handelsregistereintrag "Niederrhein Automation GmbH" in Wegberg? (b) Wird in Wegberg ein Schaltschrank oder eine Maschine selbst gebaut (Stellenanzeigen Elektroniker/Monteur Wegberg)? Aktion: nicht kontaktieren.
14. Quellen:
- https://www.duesseldorf.allaboutautomation.de/en/exhibitors/niederrhein-automation-gmbh-223378/ (S, Triage-Quelle, nicht neu abgerufen); Abruf nicht erfolgt, übernommen aus pruef_08.md.
- WebSearch 2026-10-15 "Niederrhein Automation GmbH Wegberg Steuerungstechnik Schaltschrankbau Impressum": „keine Impressum- oder Webseite für Niederrhein Automation GmbH gefunden“ (sinngemäß, Suchergebnis ohne Firmenseite, S); Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag); Websuche "Niederrhein Automation Wegberg Sondermaschinen Kleben Dosieren Nordson OR Scheugenpflug OR DOPAG OR ViscoTec OR Henkel" (keine Treffer zur Firma). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: NICHT belegt. Vorgabe "Niederrhein Automation GmbH, Wegberg". Nur Messeliste und Messeprofil (S); keine Website, kein Impressum, kein Register gefunden. Ampel höchstens Gelb (Tabellenzeile 2).

## 6. NIES electronic gmbh
1. Firma: NIES electronic gmbh (Messe: all about automation Düsseldorf 2026, Stand 410, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Kabelkonfektion, Stecker), nachrangig keine
3. Gebiet: Rest Deutschland+Niederlande (Frankfurt am Main, Hessen)
4. Sitz und Fertigungsort: Edisonstraße 7, 60388 Frankfurt (Stellenanzeige, Datenschutzhinweis, S). Kabelkonfektion laut Stellenanzeige in der Abteilung am Standort (S).
5. Website: https://nies-electronic.de
6. Was wird gebaut: Familienunternehmen (3. Generation, seit 1932), "Distributor, Kabelkonfektionär und Berater" (Imagebroschüre, Snippet S). Konfektionierte Kabel und Kabelbäume nach Zeichnung/Stückliste: Löten, Crimpen mit halbautomatischen Maschinen (Stellenanzeige 2026, S). Steckverbinder von Neutrik, Amphenol u. a. werden vertrieben (S). Umspritzen/Vergießen ist in den gefundenen Quellen NICHT erwähnt. Typisch vergossen/verklebt: konfektionierte Kabel mit Steckern Mittel (A, Block A nur bei vergossenen/umspritzten Steckern; hier Löten/Crimpen belegt), zugekaufte Stecker mit Spritzguss/Dichtung Mittel (A).
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Kabelkonfektion in Frankfurt laut Stellenanzeige 2026 (S, Snippet; ein Produktionsjob am Sitz wäre V, wenn im Browser gelesen). Hauptgeschäft Distribution, daher keine Sitzregel.
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: konfektionierte Kabel/Stecker Mittel (A), Kabelbäume ohne Umspritzung Niedrig (A), Distributionsware (zugekauft) Niedrig (A). Triage "Mittel" bestätigt, Verguss selbst nicht belegt.
9. Patentrecherche (Pflicht): Websuche mit Abfragerichtung Google Patents / Espacenet / DEPATISnet (Datenbanken nicht direkt abgefragt): Anmelder "NIES electronic" Frankfurt + Kabel: keine Treffer mit diesem Anmelder; Zufallstreffer EPO-Beschwerdekammerentscheidungen und Kabelpatente anderer Anmelder (AEG Kabel, Kabelmetal, Kaiser Kabel). Zweite, datenbankdirekte Suche fehlt.
10. Einstufung Tom: prüfenswert (Fertigung Mittel S, Verguss Mittel A); Vorbehalt: Distributor (E2), Eigenfertigung nur Kabelkonfektion
11. Ampel:
12. CRM-Status: neu mit Hinweis. crm_abgleich.py "NIES electronic gmbh": nur AEHNLICH 0.90 zu "CiS Electronic GmbH [DE]" (bekannte_firmen Zeile 413); Kern-Name verschieden ("nies electronic" vs. "cis electronic"), laut Triage erkennbar andere Firma. kundendatenbank_export.txt: kein Treffer.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Werden in Frankfurt Kabel umspritzt, vergossen oder Steckergehäuse verklebt (Imagebroschüre, Stellenanzeige im Volltext, Leistungsseite "Kabelkonfektion")? Wenn nur Löten/Crimpen: Einstufung "unwahrscheinlich". Aktion: Beobachtung.
14. Quellen:
- https://nies-electronic.de/pdfs/Stellenanzeige-Mitarbeiter-Konfektion.pdf (S, Suchzusammenfassung): „Edisonstraße 7, 60388 Frankfurt“ und Konfektion mit Löten und halbautomatischen Crimpmaschinen (sinngemäß); Abruf 2026-10-15.
- https://nies-electronic.de/pdfs/imagebroschuere-web.pdf (S, Snippet): „individually tailored cable assemblies“ (Suchzusammenfassung, Distributor, Kabelkonfektionär); Abruf 2026-10-15.
- https://www.northdata.de/391200DA1IN61I0OW582 (S, Snippet): Amtsgericht Frankfurt am Main HRB 19249; Abruf 2026-10-15.
15. Größe/Umsatz: 40 bis 49 Mitarbeiter (zwei Stellenanzeigen widersprüchlich, S); Umsatz unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag NIES); Websuche "NIES electronic Frankfurt Kabelkonfektion Spritzguss OR Vergießen OR Heißkleber Neutrik Amphenol Henkel OR Nordson" (kein Bezug zu Henkel oder Nordson). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: teilweise belegt (S). Name, Frankfurt, Edisonstraße 7 (PLZ 60388 wie Messeliste) passen; Register laut North-Data-Snippet Amtsgericht Frankfurt HRB 19249. Impressum nicht gelesen. Keine Abweichung zur Vorgabe.

## 7. Norgren GmbH
1. Firma: Norgren GmbH (Messe: all about automation Düsseldorf 2026, Stand 303, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Magnetventilspulen, Ventilelektronik), nachrangig Gasketing/Sealing
3. Gebiet: Rest Deutschland+Niederlande (Alpen, NRW laut Messeliste PLZ 46519); ein Verzeichnis nennt Fellbach (Baden-Württemberg)
4. Sitz und Fertigungsort: Alpen, Bruckstraße 93 (RS-Online-Herstellerangabe, S); ein Branchenverzeichnis nennt Stuttgarter Str. 120, Fellbach (S). Fertigung in beiden nicht belegt. Eine RS-Produktseite (Norgren V61 Magnetventil) nennt Herkunftsland CZ (S), also mindestens teilweise Fertigung in Tschechien.
5. Website: norgren.com (nicht geöffnet)
6. Was wird gebaut: Pneumatik: Aktuatoren, Druckluftaufbereitung, Ventilinseln, Steuerventile, Druckschalter, Magnetventile (24 V DC, IP65, laut Triage); Fluidik-Komponenten für Medizin/Analytik (Verzeichnis, S). Typisch vergossen/verklebt (A, Block A): Magnetventilspulen (Spulenlisting: "copper coil winding with epoxy or thermoplastic encapsulation", Produktlisting S), Ventilinsel-Elektronik, Druckschalter. Welches Produkt in Alpen entsteht, ist nicht belegt.
7. Fertigung DE/AT/NL: Mittel, Stufe S. Begründung: Marke/Konzern (IMI plc, Division IMI Precision Engineering) mit mehreren Werken, V nötig und nicht vorhanden; Hinweis auf Fertigung im Ausland (CZ) für das Magnetventil V61; Alpen als Sitz/Standort der GmbH, Fertigungsrolle offen. Bleibt Mittel, nicht Niedrig, weil nicht widerlegt.
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Magnetventilspulen, Block A; Spulenlisting S). Einzelbewertung: Magnetventilspulen Hoch (A), Ventilinsel-/Druckschalter-Elektronik Mittel (A), Zylinder/Dichtungen Niedrig (A), Druckluftaufbereitung Niedrig (A).
9. Patentrecherche (Pflicht): Websuche mit Abfragerichtung Google Patents / Espacenet / DEPATISnet (Datenbanken nicht direkt abgefragt): Anmelder "Norgren GmbH" Alpen + solenoid valve coil potting/encapsulated: kein Treffer mit Norgren GmbH. Treffer der US-Einheit Norgren, Inc. (Justia/Google, Anmelderliste): Familie "Fluid Resistant Solenoid and Related Method", Anmeldung 2015-09-01 (Spule, Kern, Tauchanker im Gehäuse; Verguss im Snippet nicht erwähnt; Rechtsstand nicht geprüft, https://patents.justia.com/assignee/norgren-inc). Nicht Norgren: US6012700A "Overmolded solenoid valve" (Snap-Tite), EP0847064A1 (Anmelder im Snippet nicht genannt). Zweite, datenbankdirekte Suche (Konzern IMI, Vorgänger Herion) fehlt.
10. Einstufung Tom: prüfenswert (Fertigung Mittel S, Verguss Hoch A); Vorbehalt Konzern-/Einheitenfrage
11. Ampel:
12. CRM-Status: unklar, CRM-Konzernbezug möglich. crm_abgleich.py "Norgren GmbH" "IMI Precision Engineering" "IMI plc": Norgren und IMI plc/IMI Precision Engineering kein Treffer; aber Abgleich auf Kern-Name "imi" ergab IDENTISCH bekannte_firmen_DE-AT-NL.txt Zeile 1127 "IMI [DE]". Ob dieser CRM-Eintrag zum Konzern IMI plc gehört oder eine andere Firma ist, ist offen (Regel M). kundendatenbank_export.txt: kein Treffer.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Ist "IMI" im CRM (Zeile 1127) dieselbe Einheit wie IMI plc / Norgren (Jey bestätigt)? (b) Wird in Alpen oder Fellbach gefertigt oder nur vertrieben (Impressum, Standortseite IMI Precision Engineering, Stellenanzeigen Alpen Montage/Fertigung)? (c) Welche Einheit (Sparte) fertigt Magnetventile und Spulen, wo? Aktion: nicht kontaktieren, bis (a) geklärt.
14. Quellen:
- https://de.rs-online.com/web/p/pneumatik-regelventile-magnetvorgesteuert/2180148 (S, Snippet): Norgren, Adresse „Bruckstraße 93“ Alpen; Abruf 2026-10-15.
- https://ch.rs-online.com/web/p/pneumatik-regelventile-magnetvorgesteuert/2180338 (S, Suchzusammenfassung): Herkunftsland „CZ“ für Norgren V61; Abruf 2026-10-15.
- https://www.chemie.de/firmen/21456/norgren-gmbh.html (S): „Stuttgarter Str. 120“, Fellbach, Unternehmen der britischen IMI-Gruppe (sinngemäß); Abruf 2026-10-15.
- https://piprocessinstrumentation.com/instrumentation/flow-measurement/article/15562016/norgren-announces-name-change-as-part-of-global-imi-transition (S): „IMI Precision Engineering“, Norgren wird IMI Norgren; Abruf 2026-10-15.
- bekannte_firmen_DE-AT-NL.txt Zeile 1127 (CRM): „IMI [DE]“; Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt (Konzerntochter)
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Norgren/IMI); Websuche "Norgren IMI Precision Engineering coil assembly dispensing potting Nordson OR Scheugenpflug OR DOPAG OR Henkel Loctite case study" (keine Fallstudie). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: ABWEICHUNG. Vorgabe "Norgren GmbH, Alpen". Sitzangaben widersprüchlich: Alpen (RS Online) und Fellbach (chemie.de). Marke heute "IMI Norgren" / Division IMI Precision Engineering (IMI plc). Impressum und Register nicht gelesen. Ampel höchstens Gelb (Tabellenzeilen 2 und 3).

## 8. OnRobot GmbH
1. Firma: OnRobot GmbH (Messe: all about automation Düsseldorf 2026, Stand 534, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Antriebe und Sensorik der Greifer), nachrangig Gasketing
3. Gebiet: Rest Deutschland+Niederlande (Soest, NRW laut Messeliste PLZ 59494)
4. Sitz und Fertigungsort: Soest = Büro (DACH/Benelux) (Verzeichnis, S). Hauptsitz OnRobot A/S, Teglværksvej 47H, Odense, Dänemark (S). Fertigungsort der Greifer in keiner Quelle genannt.
5. Website: onrobot.com (nicht geöffnet)
6. Was wird gebaut (Gruppe): elektrische Greifer, Kraft-Momenten-Sensoren, Vakuumgreifer, Gecko-Greifer, Werkzeugwechsler (S). Typisch vergossen/verklebt (A, Block A/B): Greiferantriebe mit Elektronik, Sensorik (A), Gecko-Pads (Fibrillen-Haftstruktur, kein Klebstoff, A). Ob in Soest etwas gebaut wird, ist nicht belegt.
7. Fertigung DE/AT/NL: Niedrig, Stufe S. Begründung: Soest wird nur als Büro geführt, Fertigung nicht belegt; Gruppe in Dänemark; Mehrheitsübernahme März 2026 laut Verzeichnis (S, ohne Bezug zum Fertigungsort).
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Greiferantriebe/Sensorik der Gruppe, Block A). Einzelbewertung: Kraft-Momenten-Sensoren Hoch (A), Greifermotoren mit Elektronik Hoch (A), Vakuumpumpe/Ventile Mittel (A), Gecko-Pad Niedrig (A), Werkzeugwechsler-Mechanik Niedrig (A).
9. Patentrecherche (Pflicht): Websuche mit Abfragerichtung Google Patents / Espacenet / DEPATISnet (Datenbanken nicht direkt abgefragt): Anmelder OnRobot A/S + gripper potting OR encapsulation OR sealing OR adhesive: kein belegter Treffer mit Verguss-Bezug. Treffer im Ergebnis ohne gesicherte Anmelderzuordnung zu OnRobot: CA3150722 / WO2021048000 (Elektroadhäsion mit Staubschutz, C09J 7/00), WO2021245136 (Magnetgreifer mit einstellbaren Zuständen), Dosierwerkzeug für Pastenbaumaterial (andere Anmelder vermutet, nicht belegt). Rechtsstand nicht geprüft. Zweite, datenbankdirekte Suche fehlt.
10. Einstufung Tom: unwahrscheinlich (Fertigung Niedrig S; Vertriebs-/Büro-Tochter, möglicher Ausschluss E2, Tina entscheidet)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "OnRobot GmbH": kein Treffer in beiden Dateien; Konzern "OnRobot A/S" nicht separat im Skript übergeben, siehe Einschränkungen)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): Wo werden OnRobot-Greifer gefertigt (Odense, Auftragsfertiger, Ungarn/Asien)? Wird in Soest montiert (Stellenanzeigen Soest, Impressum)? Wenn nur Vertrieb: "kein Fertiger" für DE. Aktion: nicht weiter verfolgen.
14. Quellen:
- https://automa.net/company/onrobot-dach-benelux (S, Suchzusammenfassung): „Soest“ unter den Niederlassungen von OnRobot; Abruf 2026-10-15.
- https://chemanager-online.com/en/node/367881 (S, Suchzusammenfassung): OnRobot A/S, Teglværksvej 47H, Odense; Abruf 2026-10-15.
- https://www.industrial-production.de/firma/onrobot-a-s.htm (S, Triage-Quelle, Suchzusammenfassung): Hersteller OnRobot A/S Odense; Abruf 2026-10-15.
15. Größe/Umsatz: unbekannt
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag OnRobot); Websuche "OnRobot gripper manufacturing Odense dispensing Nordson OR Scheugenpflug OR DOPAG OR Henkel OR DELO adhesive production" (kein Bezug). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: teilweise belegt (S). OnRobot GmbH als DACH-/Benelux-Büro in Soest in Verzeichnissen genannt; Rechtsform, Adresse, Register nicht belegt (kein Impressum gelesen). Hersteller ist OnRobot A/S, Odense.

## 9. Optonic GmbH
1. Firma: Optonic GmbH (Messe: all about automation Düsseldorf 2026, Stand 237, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Optical Bonding / Klebung (Kamera- und Sensorgehäuse), nachrangig Electrical Insulation (Kameraelektronik)
3. Gebiet: Baden-Württemberg (Freiburg im Breisgau)
4. Sitz und Fertigungsort: Freiburg im Breisgau (Verzeichnis, S); Profil: "alle unsere Lösungen am Standort Freiburg entwickelt und hergestellt" (Firmenprofil, Suchzusammenfassung, S).
5. Website: optonic.de (unbestätigt, nicht geöffnet)
6. Was wird gebaut: 2D/3D-Kamerasysteme, Stereo-3D-Kameras (Ensenso-Linie), Steuerungs- und schlüsselfertige Vision-Systeme, Software MIKADO (S). Hervorgegangen aus isys vision und Ensenso GmbH (S). Typisch vergossen/verklebt (A, Block B): Kameramodule (Objektiv-/Sensorklebung, Active Alignment), Kameraelektronik in Industriegehäusen, Beleuchtungsmodule. Ob Optonic selbst klebt oder vergießt, ist nicht belegt. Hinweis: Der Ensenso-N40/N45-Hersteller laut Suchergebnis ist IDS (Faserverbundgehäuse); das Verhältnis Optonic zu IDS ist unbelegt.
7. Fertigung DE/AT/NL: Hoch, Stufe A (Sitzregel: Hersteller mit eigenen Produkten und erkennbarem Standort Freiburg, keine Hinweise auf Auslagerung). Stützend S: Profil "entwickelt und hergestellt in Freiburg"; Stellenanzeigen Reparatur-/Servicetechniker für 3D-Industriekameras in Freiburg (Snippet).
8. Verguss/Bonding (höchstes Bauteil): Mittel, Stufe A. Einzelbewertung: Kameramodule (Optik, Klebung) Mittel (A), Kameraelektronik/Gehäuse Mittel (A), Steuerungs-/Robotersteuerung (zugekauft) Niedrig (A), Software keine Teile.
9. Patentrecherche (Pflicht): Websuche mit Abfragerichtung Google Patents / Espacenet / DEPATISnet (Datenbanken nicht direkt abgefragt): Anmelder Optonic OR "isys vision" OR "Ensenso GmbH" + camera housing potting OR sealing OR adhesive: keine Treffer mit diesen Anmeldern; nur Kameragehäuse-Patente anderer Anmelder (z. B. US4113137, US6038087, EP0446875B1, nicht zugeordnet). Zweite, datenbankdirekte Suche (Vorgängerfirmen isys vision, Ensenso, ggf. IDS) fehlt.
10. Einstufung Tom: prüfenswert (Fertigung Hoch A, Verguss Mittel A)
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "Optonic GmbH" "isys vision" "Ensenso": kein Treffer in beiden Dateien)
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Impressum/Register Optonic GmbH Freiburg lesen, Verhältnis zu IDS Imaging Development Systems (Ensenso) klären. (b) Werden Kameras in Freiburg montiert, werden Objektive verklebt oder Gehäuse gedichtet/vergossen (Produktseite Ensenso/Optonic, Datenblatt IP-Klasse, Stellenanzeigen Montage)? Aktion: Beobachtung.
14. Quellen:
- https://bouncewatch.com/company/optonic-gmbh (S, Suchzusammenfassung): „alle unsere Lösungen am Standort Freiburg entwickelt und hergestellt“ (laut Zusammenfassung, Profiltext); Abruf 2026-10-15.
- https://de.indeed.com/cmp/Optonic/jobs (S, Snippet): Stellenanzeigen Servicetechniker 3D-Industriekameras Freiburg (sinngemäß); Abruf 2026-10-15.
- https://www.duesseldorf.allaboutautomation.de/en/?p=366180 (S, Messeprofil): „leading provider of 2D and 3D image processing and control solutions“ (Suchzusammenfassung); Abruf 2026-10-15.
15. Größe/Umsatz: widersprüchlich (21 bis 100 Mitarbeiter, Verzeichnisse, S); Umsatz unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Optonic/isys/Ensenso); Websuche "Optonic Freiburg Stereo-3D Kamera Ensenso Gehäuse Fertigung Klebstoff DELO OR Henkel OR Nordson OR Scheugenpflug" (kein Bezug). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: teilweise belegt (S). Name, Freiburg im Breisgau, Geschäftsfeld passen; die Gründungsangabe widerspricht sich (1990 vs. 2020, Verzeichnisse). Impressum, Rechtsform und Register nicht gelesen. Abweichung zur Triage "hervorgegangen aus isys vision und Ensenso GmbH": im Suchergebnis bestätigt (S).

## 10. Optris GmbH & Co. KG
1. Firma: Optris GmbH & Co. KG (Messe: all about automation Düsseldorf 2026, Stand 123, Halle nicht angegeben)
2. Segment / Demak-Geschäftsbereich: Electrical Insulation (Temperatursensoren/Pyrometer, Messelektronik), nachrangig Gasketing und Optical Bonding (Gehäuse mit Optik/Fenster)
3. Gebiet: Rest Deutschland+Niederlande (Berlin)
4. Sitz und Fertigungsort: Ferdinand-Buisson-Str. 14, 13127 Berlin (Verzeichnisse, Messeliste, S). Entwicklung und "90 % der Produktion" am Berliner Hauptsitz (Eigenangabe laut Suchergebnis, S); Ausweitung in Berlin laut Pressemeldung "Optris expands in Berlin" (Titel im Snippet, S).
5. Website: https://optris.com
6. Was wird gebaut: stationäre Infrarot-Industriethermometer (Pyrometer), tragbare Infrarot-Thermometer, Infrarot-Wärmebildkameras, Kalibrierquellen, Software (S). Typisch vergossen/verklebt/gedichtet (A, Block A): Temperatursensoren/Pyrometer (Sensoren im Feldeinsatz), Messelektronik in Schutzgehäusen, Kameras mit Schutzgehäuse IP66 (Outdoor-Schutzgehäuse laut Snippet SPS 2022, S); IP65-Angabe zu Thermometern nicht im Snippet bestätigt (nur Verzeichnis-Titel "Optris IP65 thermometers", S). Ob Eigenverguss, ist nicht belegt.
7. Fertigung DE/AT/NL: Hoch, Stufe A (Sitzregel: Gerätebauer mit eigenen Produkten und erkennbarem Standort, keine Auslagerungshinweise). Stützend S: Eigenangabe, der überwiegende Teil der Produktion (neun Zehntel) und die Entwicklung in Berlin, ISO 9001:2015 (Suchzusammenfassung).
8. Verguss/Bonding (höchstes Bauteil): Hoch, Stufe A (Sensoren/Pyrometer im Feldeinsatz, Block A). Einzelbewertung: Pyrometer/Temperatursensoren Hoch (A), Messelektronik im Schutzgehäuse Hoch (A), IR-Kameras mit Gehäuse und Fenster Mittel (A), Software keine Teile. Der restliche Produktionsanteil (laut Eigenangabe) ist nicht näher benannt.
9. Patentrecherche (Pflicht): Websuche mit Abfragerichtung Google Patents / Espacenet / DEPATISnet (Datenbanken nicht direkt abgefragt): Anmelder Optris + infrared sensor housing potting OR encapsulation OR sealing OR vergossen: keine Patente mit Anmelder Optris in den Treffern. Zufallstreffer anderer Anmelder (US11415437 Sensor, US12055558 Gehäuse-Vergießen, EP0779503A2 Infrarotsensor, nicht zugeordnet). Zweite, datenbankdirekte Suche (Anmelder "Optris GmbH", Schreibvarianten) fehlt.
10. Einstufung Tom: interessant (Fertigung Hoch A, Verguss Hoch A); Vorbehalt: nur Stufe A und S, keine V-Quelle
11. Ampel:
12. CRM-Status: neu (crm_abgleich.py "Optris GmbH & Co. KG": kein Treffer in beiden Dateien). Mutter/Konzern laut Suche nicht genannt; Konzernabgleich daher ohne weiteren Namen.
13. Nachrecherche-Auftrag und Aktion (Vorschlag): (a) Impressum und Handelsregister (Optris GmbH vs. Optris GmbH & Co. KG, Amtsgericht Charlottenburg). (b) Datenblätter Pyrometer/Kameras: Schutzart, Hinweise auf vergossene Elektronik. (c) Stellenanzeigen Berlin Produktion/Montage zur Fertigung am Standort als V. (d) Patentsuche in Google Patents/Espacenet nachholen. Aktion: Kandidat für Gegenlesen im Browser.
14. Quellen:
- https://www.photonics.com/c19152/Optris_GmbH (S, Suchzusammenfassung): „Ferdinand-Buisson-Str. 14, 13127 Berlin“ und „all product development and 90% of production executed at our headquarters in Berlin“; Abruf 2026-10-15.
- https://optris.com/en/?p=25981 (S, Snippet): „Non-Contact Temperature Measuring – Made in Germany“ (Seitentitel); Abruf 2026-10-15.
- https://ias.german-pavilion.com/en/sites/exhibitors/99553 (S, Messeprofil, Snippet): Eintrag Optris GmbH; Abruf 2026-10-15.
- https://www.directindustry.com/product-manufacturer/optris-ip65-thermometer-219993-136688.html (S, Titel im Snippet): „Optris IP65 thermometers“; Abruf 2026-10-15.
15. Größe/Umsatz: über 100 Mitarbeiter, gegründet 2003 (Firmenangabe laut Suchzusammenfassung, S); Umsatz unbekannt.
16. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Suchen: wettbewerber_referenzen.md (kein Eintrag Optris); Websuche "Optris Berlin Infrarotkamera Produktion Klebstoff OR Vergussmasse OR Dosieranlage Henkel OR DELO OR Nordson OR Scheugenpflug" (kein Bezug). Messe-Signal: keine Wettbewerber auf der aaa.
17. Identität: teilweise belegt (S). Verzeichnisse und Messelisten führen sowohl "Optris GmbH" (Photonics, Laser Focus World, Industrial Production, Messen) als auch "Optris GmbH & Co. KG" (Formnext, automa.net); Triage nennt die Namensvariante. Adresse Berlin stimmt überein. Rechtsform und Register nicht belegt (Impressum nicht gelesen).

## nicht aufgenommen (bereits bekannt / unklar)
Keine der 10 Firmen ist eindeutig BEKANNT (0). Alle 10 stehen im Batch. Vermerke zu CRM-Treffern:
- Möller GmbH (Liste, Diepholz) gegenüber CRM "Möller-Preussler Transformatoren GmbH [DE]" (bekannte_firmen_DE-AT-NL.txt Zeile 1642): Präfix-Treffer, andere Schreibweise, Ort der CRM-Firma nicht ersichtlich. Status unklar, Einheit manuell klären.
- Norgren GmbH (Liste, Alpen): kein Treffer unter dem Firmennamen. Konzernabgleich: Kern-Name "imi" identisch mit CRM-Zeile 1127 "IMI [DE]"; ob IMI plc gemeint ist, offen. Status unklar (CRM-Konzernbezug), Entscheidung bei Tina/Jey.
- Müller Maschinentechnik GmbH: nur Wortwurzel "mueller" im CRM (Zeilen 1673 bis 1676, andere Firmen). Als neu geführt, mit Hinweis.
- NIES electronic gmbh: Ähnlichkeit 0.90 zu "CiS Electronic GmbH" (Zeile 413), Kern-Name verschieden. Als neu geführt.

## Einschränkungen
- Werkzeuge: WebFetch und Chrome waren nicht verfügbar. Es wurden ausschließlich WebSearch-Zusammenfassungen und Snippets ausgewertet. Damit ist KEINE Aussage in diesem Batch Stufe V; alle Fertigungs- und Produktangaben sind S oder A. Kein Impressum, keine Produktseite, kein Datenblatt wurde gelesen. Zitate in Feld 14 sind Ausschnitte oder sinngemäße Wiedergaben aus Suchzusammenfassungen (als "sinngemäß" markiert), nicht aus den Seiten selbst. Alle Zitate sind im Browser gegenzulesen (H).
- Patentrecherche (Feld 9) NUR SCHWACH und unvollständig gegenüber F5: pro Firma genau EINE WebSearch mit Anmelder und Stichwörtern; Google Patents, Espacenet und DEPATISnet wurden NICHT direkt abgefragt (kein Browser, kein Anmelderfilter, kein Rechtsstand). Keine zweite Suche, keine engen Zusatzsuchen, Vorgänger-/Schwesterfirmen und Konzerne (Nachi-Fujikoshi, IMI, OnRobot A/S, Optonic-Vorgänger, Optris-Schreibvarianten) nur in den Suchtexten mitgesucht. Die Aussagen "keine Treffer" sind daher kein Gegenbeweis. Der Batch gilt nach Regel N4 bei Feld 9 als UNVOLLSTÄNDIG, die datenbankdirekte Suche muss nachgeholt werden (bei interessant/prüfenswert Firmen zuerst: Optris, Norgren, Mütron, Optonic, Müller Maschinentechnik).
- Wettbewerbereinsatz (Feld 16): je Firma eine WebSearch plus Abgleich mit wettbewerber_referenzen.md (kein Eintrag für eine der 10 Firmen, Grep 2026-10-15) und Messeliste. Referenzseiten der Wettbewerber, Fachpresse, Stellenanzeigen nicht gezielt durchsucht. "Kein Hinweis" ist Stufe ? und kein Gegenbeweis.
- Produkt und Fertigungsort: je Firma eine Suche. Triage-Angaben (Sitz, Produkttyp) sind nur dort bestätigt, wo die Suche sie stützte. Nicht bestätigt: Sitz Achim (Mütron), Sitz Wegberg und Existenz einer Firmenseite (Niederrhein Automation), Sitz Alpen vs. Fellbach (Norgren), Fertigung Soest (OnRobot), Fertigung Krefeld (Nachi), Fertigung Diepholz und Produkt (Möller). Die Websites der Triage (muetron.de, mueller-maschinentechnik.de, nachi.de, optonic.de) wurden nicht geöffnet.
- Identität (Feld 17): kein einziges Impressum und kein Registerauszug gelesen. Bei Möller, Mütron, Niederrhein Automation und Norgren ist die Identität nicht belegt (Tabellenzeile 2).
- Python lief (crm_abgleich.py ausgeführt). Konzernnamen wurden nur teilweise übergeben: Norgren (IMI plc, IMI Precision Engineering), Nachi (Nachi, Nachi-Fujikoshi), Optonic (isys vision, Ensenso), Mütron (Muetron), Müller (Müller Industrie-Elektronik), Möller (Möller-Preussler), Nies nicht, OnRobot und Optris ohne weiteren Konzernnamen (OnRobot A/S wurde nicht separat übergeben). CRM-Dateien enthalten keine Ortsangaben, daher kein Ortsabgleich.
- Größe/Umsatz nur nebenbei erfasst (Feld 15), Mitarbeiterzahlen widersprüchlich. Keine Suche nach Ansprechpartnern oder Kontaktformularen (Regel K).
- Halle ist in der Liste nicht angegeben; Feld 1 nennt nur die Standnummer. Aussteller-Beschreibungstexte der Messe wären Stufe S (N5).
