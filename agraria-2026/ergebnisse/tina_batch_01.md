# Tina Batch 01 - agraria 2026 (Prüfung von tom_batch_01.md)
Erstellt: 2026-11-24 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_01.md (10 Firmen, Nr. 1 bis 10, Messe Wels 25.-28.11.2026, Länder DE/AT/NL).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Seitenabruf geprüft, vorläufig.** Verfügbar waren nur WebSearch (Snippets/Kurzfassungen) und Bash. WebFetch scheiterte (amazone.net und www.bvl-group.de nicht auflösbar: Host liegt außerhalb der erlaubten Netzdomains der Sitzung), Chrome nicht vorhanden. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün ist mailtauglich.
Skripte: `python3 crm_abgleich.py` für alle Firmen samt Kurz-, Konzern-, Alt- und Schwesternamen selbst wiederholt (Amazone/Dreyer, Betriko, Agritech, Bannaski, Schäfer Toy Company, Schäfer Brand Distribution, BvL/van Lengerich, CPI Colostrum Products u. a.). Ergebnis deckt sich mit Tom: alle 10 neu; nur Wortwurzel-Treffer (ADLER Elektrotechnik Leipzig GmbH Z. 44, HADLER GmbH Z. 955, Ludwig Leuchten GmbH & Co. KG Z. 1481, Schäfer Elektronik GmbH Z. 2091), alle andere Firma/andere Branche, keine Namensgleichheit im Sinn von Jeys Regel "gleicher/sehr ähnlicher Name raus". Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum aller Einträge: 2026-11-24.
Jey-Entscheidungen angewendet: Verbände/Prüfdienstleister/Forschung: keine im Batch. CRM-Namensgleiche: keine. Anlagenbauer bleiben drin (autarkize); E1 (baut selbst Verguss-/Dosieranlagen) trifft keine Firma, soweit erkennbar (kein V, nur Snippets).

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | Adler Arbeitsmaschinen GmbH (Halle 20, B10) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 2 | AGRARMONITOR (Halle 17, 190) | GELB | 7 (Rot-Kandidat E2) | nein |
| 3 | AGRIBOX GmbH (Halle 24, 40) | GELB | 2 | ja |
| 4 | AMAZONEN-Werke H. Dreyer SE & Co. KG (Halle 22, B20) | GELB | 5 | ja |
| 5 | autarkize GmbH (Halle 17, 200) | GELB | 5 | ja |
| 6 | BB-Umwelttechnik GmbH (Halle 19, 170) | GELB | 2 | nein |
| 7 | Bergmann Ludwig GmbH (Halle 20, C50) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 8 | BRIXIES Schäfer Brand Distribution GmbH (Halle 20, 1130) | GELB | 2 (Rot-Kandidat E2) | nein |
| 9 | BvL van Lengerich (Halle 19, 130) | GELB | 5 | ja |
| 10 | Colostrum BioTec GmbH (Halle 19, 30) | GELB | 6 | nein |

Zahlen: Grün 2 (beide schwach, ohne V), Gelb 8, Rot 0. Kein Rot, weil kein harter Ausschluss mit Stufe V belegt ist (E2-Kandidaten: AGRARMONITOR, BRIXIES; Identitätsfälle: AGRIBOX, BB-Umwelttechnik).

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Eigene Patent-Websuche nur für AMAZONE (1 Abfrage, Ergebnis siehe Nr. 4). Für die übrigen 9 Firmen keine eigene Patentsuche wiederholt; Toms Suchen (WebSearch, keine Datenbank, Rechtsstand nie geprüft) werden weder übernommen noch widerlegt. Feld 9 ist damit bei ALLEN 10 Firmen ohne Datenbankabfrage: nach F5 UNVOLLSTÄNDIG, Nachholen im Browser nötig. Besonders nötig für Nr. 1, 4, 7, 9 (Grün/Grün-nah). "Keine Treffer" ist kein Gegenbeweis.
Wettbewerbereinsatz (F6): Grep auf wettbewerber_referenzen.md (Adler, agrarmonitor, betriko, agribox, amazon, autarkize, bb-umwelt, bannaski, bergmann, brixies, schäfer toy, lengerich, bvl, colostrum, Landtechnik-Hersteller): einziger Treffer "Bischof+Klein (Lengerich)", andere Firma, anderer Ort (kein BvL-Bezug). Keine Einzelsuchen mit Wettbewerbernamen von mir. Messe-Signal: Tom meldet keinen Wettbewerber unter den Ausstellern; von mir nicht wiederholt (CSV nicht neu gegreppt).

---

## 1. Adler Arbeitsmaschinen GmbH | Halle 20, Stand B10
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Fertigung Stufe A nach Sitzregel, Verguss Mittel A).** Zeile 1 nein (kein E-Beleg), 2 nein (Identität bis auf Rechtsform GmbH/GmbH & Co. KG stimmig), 3 nein (kein Konzernbezug; ADLER Elektrotechnik Leipzig GmbH ist andere Firma), 4 trifft. Gerätebauer mit erkennbarem Standort Nordwalde, eigene Produkte, kein Konzern, keine Auslagerungshinweise.
- Eigene Prüfung: crm_abgleich.py "Adler Arbeitsmaschinen GmbH", "ADLER Arbeitsmaschinen GmbH & Co. KG", "Adler": nur ADLER Elektrotechnik Leipzig (Z. 44) und HADLER (Z. 955), andere Firmen. Neue Stütze für Fertigung: WebSearch-Snippet einer StepStone-Stellenanzeige "Mitarbeiter (m/w/d) Produktion Bohrgeräte" bei ADLER Arbeitsmaschinen GmbH & Co. KG, Nordwalde, Landmaschinen-/Produktion und Service der Bohrgeräte (S, undatiert; als Snippet nicht V). Kein Wettbewerbereinsatz gefunden.
- Verguss: Mittel (A, Endprodukt-Regel): Streuer-Steuergerät, LED-Arbeitsscheinwerfer, Magnetventile. Elektronikanteil NICHT belegt; die Stellenanzeige nennt Bohrgeräte, Produktbreite (Kehrmaschinen, Streuer) von mir nicht bestätigt.
- Korrekturen an Toms Feldern: Feld 17: Rechtsform GmbH & Co. KG durch zwei Verzeichnisse und Stellenanzeige gestützt (S), Messeliste "GmbH" abweichend. Feld 7: Fertigung bleibt Hoch (A), leicht gestützt. Zitat im Browser bestätigt: nein.
- Patente: nur Toms WebSearch (0 Treffer), Datenbanken offen.
- Nachrecherche (kein Gelb, für Mailstufe nötig): (a) Impressum und Handelsregister (Rechtsform, Sitz Nordwalde). (b) Produktseiten/Datenblätter Streuer: Steuerelektronik, Beleuchtung, IP-Klasse (Verguss A auf V heben). (c) Stellenanzeige Produktion Bohrgeräte im Browser lesen (Fertigung V). (d) Patente/Gebrauchsmuster Google Patents/DEPATISnet mit Anmelder-Varianten.
- Nicht verwendbare Aussagen: Fertigung Nordwalde (A/S); Verguss aller Bauteile (A); Produktspektrum (S). Stichprobe für Jey: ja (Grün ohne V, Verguss nur abgeleitet).

## 2. AGRARMONITOR | Halle 17, Stand 190
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2 Software/Beratung).** Produkt der betriko GmbH (Kalletal), Software für Lohnunternehmer (S). Keine Fertigung, Verguss Niedrig (A). Zeile 1 verlangt Stufe V für E2, nur Snippets vorhanden, daher nicht Rot. CRM: AGRARMONITOR, betriko GmbH, Betriko: kein Treffer, neu.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Impressum agrarmonitor.de im Browser lesen (Gesellschaft betriko GmbH, Sitz, Register, Geschäftszweck); wörtliches Zitat zu Software/Beratung als V sichern, dann Rot nach E2 mit URL. Zusätzlich klären, ob die in der Messeliste genannten "GPS Geräte" selbst gefertigt werden (dann Fertigungsfrage neu). Aktion: nicht weiter verfolgen bis geklärt.
- Nicht verwendbare Aussagen: alle (S/A/?). Stichprobe für Jey: nein.

## 3. AGRIBOX GmbH | Halle 24, Stand 40
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Meine Suche "AGRIBOX GmbH Klauenpflege Handelsregister Sitz Geschäftsführer" findet keine Firma AGRIBOX GmbH (nur DPMA-Markenregister-Treffer ohne erkennbare Zuordnung, Genossenschaft Klauenpfleger eG Sachsen, Kerbl-Produktseiten; nicht zugeordnet, nicht vermischt). Gleicher Befund wie Tom. Produktname AGRIBOX gehört bei Tom zu AGRITECH S.R.L. (Italien), Bezug zum Aussteller unbelegt. Verguss Niedrig (A: Hygiene/Bekleidung/Futtermittel/Zubehör); wahrscheinlich Handel (E2), aber ohne V nicht Rot. CRM: AGRIBOX GmbH, Agribox, Agritech: kein Treffer, neu.
- Korrekturen: Gebiet "nicht ermittelt" bestätigt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer ist AGRIBOX GmbH? Messeprofil agraria (Aussteller-Detailseite, Adresse, Website), DPMAregister-Markenabfrage "AGRIBOX" (Inhaber), Handelsregister (handelsregister.de/northdata). Bei Händler ohne Fertigung: Rot nach E2 mit URL. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/A/?). Stichprobe für Jey: ja (Firma nicht identifizierbar).

## 4. AMAZONEN-Werke H. Dreyer SE & Co. KG | Halle 22, Stand B20
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Fertigungsbeleg für die Elektronik fehlt).** Konzern mit mehreren Werken (Hasbergen-Gaste, Hude, Leipzig, Forbach FR, Ungarn; S): nach Sitzregel ist Stufe V mit Produkt-Werk-Zuordnung nötig, fehlt; Sitzregel greift nicht. Verguss Hoch (A: ISOBUS-Terminal/Steuergerät, Sensorik, Endprodukt-Regel). Hinweis: Toms "interessant" ist ohne V/Browser nach Regel I nicht bestätigt; bei V-Beleg Fertigung Hasbergen wäre Zeile 4 Grün sicher (Kandidat mit der höchsten Grün-Aussicht des Batches).
- Eigene Prüfung: crm_abgleich.py "AMAZONEN-Werke H. Dreyer SE & Co. KG", "Amazone", "Amazonen Werke", "Dreyer": kein Treffer, neu, kein Konzernbezug. WebSearch Elektronikfertigung: kein Beleg, wo AMATRON-Terminals gefertigt werden. Neu: Firmenhistorie-Snippet nennt Zusammenarbeit mit Müller Elektronik seit 1985 (Heinrich Müller / Dr. Scheufler); ob Terminals/Elektronik in Hasbergen oder bei diesem Partner gebaut werden, ist offen (S). Das ist ein Auslagerungsrisiko für die Elektronik, nicht für die Landtechnik. Impressum-/Standortseite amazone.net per WebFetch nicht erreichbar (Host nicht erlaubt).
- Patente (eigene Suche, 1 Abfrage Amazonen-Werke + potting/Vergussmasse/Verguss/Gehäuse/Sensor): kein Amazone-Patent zu Verguss. Bestätigt: DE102013103060A1 "Vorrichtung zum Ermitteln von zumindest einem Verteilungsparameter" (Amazonen-Werke H. Dreyer GmbH & Co. KG, 2013 angemeldet, 2014-10-16 offengelegt; Google Patents, nur als zitierter Stand der Technik gesehen; Rechtsstand NICHT geprüft). EP2520148 "sensor arrangement": Zuordnung zu Amazone weiter nicht gesichert. Treffer zu "Dreyer" und Verguss (Endress+Hauser EP0766073/US6051783, Erfinder Volker Dreyer) sind Fremd- bzw. Personentreffer und wurden aussortiert. Datenbanken direkt: offen. Wettbewerbereinsatz: kein Hinweis (Grep, keine Einzelsuche).
- Korrekturen an Toms Feldern: Feld 4: Elektronik-Fertigungsort offen, Müller-Elektronik-Kooperation als offener Punkt ergänzt. Feld 9: DE102013103060A1 Anmeldedatum 2013 (Google-Patents-Snippet), Rechtsstand weiter offen. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Wo werden Bordcomputer/Terminals (AMATRON/AMAPAD), Sensoren und Steuergeräte gefertigt oder montiert: Hasbergen-Gaste oder bei Partner/Ausland? Wo: Seite "40 Jahre AMATRON" und Standortseiten amazone.net im Browser, Stellenanzeigen Elektronikmontage/Fertigung Hasbergen. (b) Impressum: Rechtsform SE & Co. KG und fertigende Einheit. (c) Datenblätter ISOBUS-Terminal/Sensor (IP-Klasse, Verguss/Dichtung). (d) Patente Google Patents/Espacenet/DEPATISnet mit Rechtsstand, Anmelder-Varianten (SE & Co. KG, GmbH & Co. KG). Aktion: nicht kontaktieren; hohe Priorität.
- Nicht verwendbare Aussagen: Fertigung Hasbergen für Elektronik (S); Verguss aller Bauteile (A); Patentstatus; Werkliste (S). Stichprobe für Jey: ja (Toms Interessant ohne V; Konzern).

## 5. autarkize GmbH | Halle 17, Stand 200
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Start-up (Gründung 2022, Seed 2,3 Mio. EUR Oktober 2024; Quellen renewable-carbon.eu, chemie.de, htgf, S), modulare Pyrolyse-Container-Anlagen bis 2,5 MW (S). Sitzregel nur bedingt anwendbar: Fertigungsort/Montage der Container nicht belegt, Auslagerung offen, Adresse widersprüchlich (Pfronten Bürgermeister-Haff-Straße 8 vs. Biessenhofen An der Säge 3). E1: kein Hinweis, dass autarkize Verguss-/Dosieranlagen baut. Verguss Mittel (A: Mess-/Regelungs-/Gasmesselektronik, Schaltschrank; zugekaufte Teile zählen). CRM: autarkize GmbH, autarkize: kein Treffer, neu.
- Eigene Prüfung: eine WebSearch (Fertigung/Werkstatt/Impressum): keine Aussage zu Fertigungsort; Adresskonflikt bleibt (kein Impressum erreichbar).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Impressum autarkize.com und Handelsregister: Sitz Pfronten oder Biessenhofen. (b) Wird die Anlage in Eigenwerkstatt in Deutschland gebaut/montiert oder durch Partner? Stellenanzeigen, Pressemeldungen, Chemiecluster-Bayern-Artikel "Hot Seat Michel Konder" im Browser lesen. (c) Steuerungs-/Sensorik: Zukauf oder Eigenbau? (d) DPMAregister/DEPATISnet Anmelder "autarkize". Aktion: nicht kontaktieren; mittlere Priorität.
- Nicht verwendbare Aussagen: Fertigung (A); Verguss (A); beide Adressen (S). Stichprobe für Jey: ja (Fertigungsort und Adresse offen).

## 6. BB-Umwelttechnik GmbH | Halle 19, Stand 170
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität/Sitz nicht belegt).** Meine Suche bestätigt: Verzeichnisse nennen "BB-Umwelttechnik GmbH, By Max Bannaski", Doppelmesser-Mähwerke Seco Duplex bis 9 m; Messerbalken werden laut Fachartikel (2020) von ESM Ennepetal zugekauft (S). Kein Sitz gefunden. Neu: eine Broschüre von 2023 nennt www.bbumwelttechnik.com (Impressum nicht geöffnet). Verguss Niedrig (A; überwiegend mechanisch-hydraulisch); Fertigung Niedrig (?). Nach Tabelle ohne Identität nicht bewertbar. CRM: BB-Umwelttechnik GmbH, BB Umwelttechnik, Bannaski: kein Treffer, neu.
- Korrekturen: Feld 5 Website-Vorschlag bbumwelttechnik.com (aus Broschüren-Snippet, nicht gelesen). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Impressum bbumwelttechnik.com lesen: Sitz, Rechtsform, Register; fertigt BB selbst (Montage der Mähwerke) oder Handel/Vertrieb zugekaufter Technik? Bei reinem Handel Rot E2 mit URL; bei Fertigung ohne Elektronik bleibt Verguss Niedrig (Zeile 6, kein Ziel). Aktion: niedrige Priorität.
- Nicht verwendbare Aussagen: alle (S/A/?). Stichprobe für Jey: nein.

## 7. Bergmann Ludwig GmbH | Halle 20, Stand C50
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Fertigung Stufe A nach Sitzregel, Verguss Mittel A).** Landmaschinenhersteller (Ladewagen, Überladewagen, Miststreuer) in Goldenstedt, eigene Produkte, kein Konzern erkennbar, keine Auslagerungshinweise. Schwäche: Elektronik (ISOBUS) vermutlich zugekauft, aber nach Endprodukt-Regel zählen verbaute Zukaufteile.
- Eigene Prüfung: crm_abgleich.py "Bergmann Ludwig GmbH", "Ludwig Bergmann GmbH", "Bergmann": nur Ludwig Leuchten GmbH & Co. KG (Z. 1481), andere Firma; neu. Stellensuche Goldenstedt (Elektriker/Montage/Ladewagen): keine Anzeige der Firma gefunden (Negativbefund, kein Gegenbeleg). Weitere Gesellschaft "Ludwig Bergman International Sales GmbH" (Vertrieb, gleiche Anschrift laut Tom): fertigende Einheit bleibt Ludwig Bergmann GmbH.
- Korrekturen an Toms Feldern: Feld 17 bestätigt (umgekehrte Namensschreibweise). Fertigung weiter nur A. Zitat im Browser bestätigt: nein.
- Nachrecherche (kein Gelb, für Mailstufe nötig): (a) Impressum und Handelsregister Ludwig Bergmann GmbH (HRB 112411 laut Tom-Snippet, Gericht nicht belegt), Website ermitteln. (b) Karriereseite/Stellenanzeigen Elektrik/Montage Goldenstedt (Fertigung V). (c) Datenblatt REPEX/ISOBUS-Terminal, Wiegetechnik: IP-Klasse, Eigenbau oder Zukauf (Verguss A auf V). (d) Patente/Gebrauchsmuster Google Patents/DEPATISnet.
- Nicht verwendbare Aussagen: Fertigung Goldenstedt (A/S); Verguss (A); Patent 0 Treffer (nur WebSearch). Stichprobe für Jey: ja (Grün ohne V; Elektronik evtl. Zukauf).

## 8. BRIXIES Schäfer Brand Distribution GmbH | Halle 20, Stand 1130
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität/Beziehung der Gesellschaften offen; Rot-Kandidat E2).** Marke/Distribution von ABS-Klemmbausteinen; Schwesterfirma Schäfer Toy Company GmbH (Daufenbach, S). Eigenfertigung nicht belegt, Verguss Niedrig (A). Ohne V kein Rot. CRM: BRIXIES Schäfer Brand Distribution GmbH, Schäfer Toy Company, Brixies, Schäfer Brand Distribution: nur Wortwurzel Schäfer Elektronik GmbH (Z. 2091), andere Firma, neu. Keine eigene Websuche (Suchbudget).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Impressum brixies.de lesen: Sitz der Schäfer Brand Distribution GmbH, Verhältnis zur Schäfer Toy Company GmbH, Hersteller/Fertigungsland der Bausteine. Bei Vertrieb ohne Fertigung in DE/AT/NL: Rot nach E2/E3 mit URL. Aktion: nicht weiter verfolgen bis geklärt.
- Nicht verwendbare Aussagen: alle (S/A/?). Stichprobe für Jey: nein.

## 9. BvL van Lengerich | Halle 19, Stand 130
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Gruppe mit mehreren Geschäftsbereichen: Stufe V nötig).** Bernard van Lengerich Maschinenfabrik GmbH & Co. KG, Emsbüren. Neu aus meiner Suche (S, Kurzfassung): Familiengruppe mit drei Geschäftsbereichen (Landtechnik, Oberflächentechnik, Elektrotechnik), "alle drei Unternehmen am Standort Emsbüren", dritte Produktionshalle, Ausbau seit 2016; Quelle bvl-group.de/Verzeichnisse, Snippet. Das mildert das Mehrwerk-Risiko (ein Standort), ersetzt aber nicht V. Der Elektrotechnik-Bereich ist nur als Existenz bestätigt, nicht nach Inhalt (Schaltschrank/Elektronik/Verguss offen). Verguss Hoch (A: Wiege-/Sensorsystem, Steuerung/Bedienelektronik, Endprodukt-Regel). Nach V-Beleg Emsbüren Grün erwartbar (zweitaussichtsreichste Firma).
- Eigene Prüfung: crm_abgleich.py "BvL van Lengerich", "Bernard van Lengerich Maschinenfabrik", "BvL", "van Lengerich": kein Treffer, neu, kein Konzernbezug. bvl-group.de per WebFetch nicht erreichbar (Host nicht erlaubt). Wikipedia-Benutzerentwurf bleibt Sekundärquelle (S). Verwechslung "Bischof+Klein (Lengerich)" (DOPAG-Referenz in wettbewerber_referenzen.md Z. 164) ist eine andere Firma in Lengerich bei Osnabrück, nicht vermischt.
- Patente: nur Toms Aggregator-Angabe (ca. 44 Anmeldungen "LENGERICH MASCHF", Silage/Misch/Verteil, S); keine eigene Datenbankabfrage; Rechtsstand und Verguss-Bezug offen.
- Korrekturen an Toms Feldern: Feld 4: Standort Emsbüren für alle drei Bereiche durch Kurzfassung gestützt (S). Toms "interessant" ohne V nicht bestätigt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Standortseite/Impressum bvl-group.de im Browser: Wird in Emsbüren gefertigt (V, wörtliches Zitat)? Welche Gesellschaft fertigt Futtermischwagen und Elektronik? (b) Was macht der Bereich "Elektrotechnik" (Schaltschrank, Steuerungen, Elektronikmontage mit Verguss)? Stellenanzeigen Elektronik/Elektrotechnik Emsbüren. (c) Datenblätter Wiege-/Steuerungssystem (IP-Klasse). (d) Patente Google Patents/Espacenet/DEPATISnet, Anmelder "Bernard van Lengerich Maschinenfabrik" und "Lengerich Maschf", mit Rechtsstand und Stichworten Verguss/Dichtung. Aktion: nicht kontaktieren; hohe Priorität.
- Nicht verwendbare Aussagen: Fertigung Emsbüren (S); Elektrotechnik-Bereich (S, Sekundärquelle); Verguss (A); Patentzahl (S). Stichprobe für Jey: ja (Toms Interessant ohne V; Gruppe).

## 10. Colostrum BioTec GmbH | Halle 19, Stand 30
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6; Verguss Niedrig für alle Bauteile, Fertigung nur S).** Lebensmittel-/Nahrungsergänzungshersteller (Kolostrum), Königsbrunn (S). Alle plausiblen Bauteile Niedrig (A); Messelistenhinweis auf Melk-/Tränketechnik ungeklärt (?). Kein harter Ausschluss belegt, daher nicht Rot (Rot nur nach E; eine reine Niedrig-Einstufung ist laut Tabelle Gelb). CRM: Colostrum BioTec GmbH, Colostrum, CPI Colostrum Products: kein Treffer, neu. Keine eigene Websuche (Suchbudget); Toms Angaben nicht widerlegt.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Messeprofil agraria lesen: Welche Produkte genau (nur Kolostrum/Lebensmittel oder auch Melk-/Tränketechnik mit Elektronik)? Produktseiten/Impressum im Browser. Bei reinem Lebensmittelhersteller: Verguss Niedrig bestätigt, kein Ziel. Aktion: nicht weiter verfolgen, niedrige Priorität.
- Nicht verwendbare Aussagen: Fertigung Königsbrunn (S, Ausstellerprofil); Verguss (A). Stichprobe für Jey: nein.

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind durchgehend korrekt niedrig angesetzt; keine V-Aussage vorgetäuscht. Seine Einstufungen "interessant" (Amazone, BvL) sind nach Regel I ohne Quellen-Gegenlesen im Browser nicht bestätigt; beide bleiben Gelb, weil beide Konzern/Gruppe mit mehreren Geschäftsbereichen sind und die Sitzregel dafür V verlangt. Adler und Bergmann (Einzelstandort-Hersteller) laufen über die Sitzregel in Grün (schwach).
- Rangfolge für die Nachrecherche (Aussicht auf Grün): 1. Amazone, 2. BvL, dann Adler und Bergmann (Verguss auf V heben), danach autarkize.
- Mögliche Rot-Kandidaten bei V-Beleg: AGRARMONITOR (E2), BRIXIES (E2/E3), AGRIBOX (E2 oder Identität), BB-Umwelttechnik (E2 oder Verguss Niedrig).
- Vorschlag Fehlerlog (Jey gibt frei, nicht eingetragen): Bei Landtechnik-Konzernen mit Zulieferer-Elektronik (Amazone/Müller Elektronik) Herkunft der Elektronik getrennt von der Maschine prüfen.

## Einschränkungen
- Browser und WebFetch nicht nutzbar (WebFetch: amazone.net und www.bvl-group.de nicht auflösbar, Hosts liegen außerhalb der erlaubten Netzdomains; Freigabe in den Netzwerkeinstellungen der Sitzung nötig, sonst kein Gegenlesen nach Abschnitt H). Keine Impressen, Datenblätter oder Karriereseiten gelesen; alle Aussagen Stufe S, A oder ?. Keine "Zitat im Browser bestätigt: ja", kein Grün mailtauglich.
- WebSearch: 10 Abfragen (Amazone Elektronikfertigung und Patent, BvL Elektrotechnik, Bergmann Stellen, autarkize Fertigung, Adler Stellen, BB-Umwelttechnik Sitz, AGRIBOX Register). NICHT eigens gesucht: AGRARMONITOR/betriko, BRIXIES/Schäfer, Colostrum BioTec (Suchbudget; Toms Angaben nicht widerlegt, nur CRM-Abgleich selbst wiederholt).
- Patente: Pflichtsuche F5 (Google Patents, Espacenet, DEPATISnet) für alle 10 Firmen nicht erfüllt; Batch UNVOLLSTÄNDIG, bevor ein Grün final wird. Rechtsstand nirgends geprüft; Anmeldervarianten zurückgestellt.
- Wettbewerbereinsatz (F6): nur Listenabgleich und Toms Angaben; "kein Hinweis" ist kein Gegenbeweis. Messe-Signal aus Toms Grep übernommen, nicht wiederholt.
- Handelsregister/Impressum bei keiner Firma gelesen; Identität nur über Snippets. Kundendatenbank (Excel) nicht lesbar; CRM-Abgleich per Skript auf Textexporte (Treffer nur Wortwurzeln).
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
