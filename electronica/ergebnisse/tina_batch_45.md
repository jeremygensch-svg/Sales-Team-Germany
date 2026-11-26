# Tina Batch 45 – electronica 2026 (Prüfung von tom_batch_45.md)
Erstellt: 2026-10-21 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe: ausschließlich electronica/ergebnisse/tom_batch_45.md (10 Firmen, Nr. 502, 503, 504, 505, 508, 509, 510, 511, 512, 513).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (ca. 28 Abfragen, Snippets/Kurzfassungen) und Bash zur Verfügung; WebFetch und Chrome nicht nutzbar. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün ist mailtauglich. Harte Ausschlüsse E1 bis E4 verlangen nach Tabellenzeile 1 Stufe V; da keine V-Quelle gelesen werden konnte, ist keine Firma Rot, die Ausschluss-Kandidaten stehen als Gelb mit Auftrag "Ausschluss mit V belegen".
Skripte: `python3 crm_abgleich.py` für alle Firmen samt Konzern-, Alt- und Schwesternamen selbst wiederholt (Ergebnis je Firma unten). Tabellenzeile = Zeilennummer der Ampel-Tabelle D. Lehren 1 bis 17 aus fehlerlog_lehren.md beachtet.
Verifikationsdatum aller Einträge: 2026-10-21.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 502 | RAMPF Advanced Polymers GmbH & Co. KG (A5.324) | GELB (Rot-Kandidat E1) | 7 | nein |
| 503 | RAMPF Production Systems GmbH & Co. KG (A5.324) | GELB (Rot-Kandidat E1) | 7 | nein |
| 504 | RAPP Kunststofftechnik GmbH (B3.141) | GELB | 5 | nein |
| 505 | Ratioplast Electronics (B3.411) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 508 | REEL Reinheimer Elektronik GmbH (C2.616) | GELB | 5 | ja |
| 509 | REHAG ELEKTRONIK GmbH (C3.441) | GELB (Rot-Kandidat E2) | 7 | nein |
| 510 | REINHARDT System- und Messelectronic GmbH (A4.401) | GRÜN | 4 (Sitzregel) | ja |
| 511 | RENA Technologies GmbH (B1.312) | GELB | 5 | nein |
| 512 | Renesas Electronics (C5.479) | GELB (Rot-Kandidat E2) | 2 | ja |
| 513 | Rennsteig Werkzeuge GmbH (B2.228) | GELB | 5 | nein |

Zahlen: Grün 2, Gelb 8, Rot 0.

Patente (Prüfpunkt 8, Regel F5): DEPATISnet, Espacenet und Google Patents waren nicht direkt im Browser abfragbar. Ersatz: je Firma außer REHAG, Renesas, RENA und RAPP eine eigene site-gefilterte Websuche (patents.google.com, worldwide.espacenet.com, bei Reinhardt zusätzlich depatisnet.dpma.de): Ergebnisse siehe Firmenblöcke. Für REHAG, Renesas, RENA, RAPP keine eigene Wiederholung (Budget, Distributor/Vertrieb bzw. Verguss Niedrig). Rechtsstände nirgends belastbar geprüft (Ausnahme: Google-Status-Snippet bei US11114719B2). Feld 9 bleibt damit bei allen 10 Firmen ohne Direktabfrage: nicht belastbar, kein Gegenbeweis. Der Batch ist nach F5 UNVOLLSTÄNDIG im Sinne der Datenbankabfrage; Nachholen im Browser nötig, bevor ein Grün final wird. Wettbewerbereinsatz (F6): eigener Abgleich mit wettbewerber_referenzen.md (nur RAMPF dort als Materialhersteller geführt, Abschnitt 12); Einzelsuchen nur bei Reinhardt (MWS-Suche) und Ratioplast, sonst nicht wiederholt; ohne Einfluss auf die Ampel.

Messe-Signal (Regel N2) aus Toms Datei übernommen, nicht neu geprüft: bdtronic, ELANTAS, Momentive, Nordson Test&Inspection, beide RAMPF-Einheiten stellen aus; Zuordnung POLYTEC (Zeile 480) weiter offen. Ändert keine Ampel.

---

## 1. RAMPF Advanced Polymers GmbH & Co. KG | Stand A5.324 (Nr. 502)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB, Rot-Kandidat E1 (Tabellenzeile 7).** Materialhersteller für Elektrogießharze (Vergussmassen auf PU/Epoxid/Silikon): E1 trifft inhaltlich sehr wahrscheinlich zu, aber Tabellenzeile 1 verlangt Stufe V; ich habe nur Suchzusammenfassungen von rampf-group.com (S). Daher nicht Rot, bis die Seite gelesen ist.
- Eigene Prüfung: Websuche bestätigt Sitz Grafenberg, Pressemitteilung 2024 als "RAMPF Advanced Polymers GmbH & Co. KG", Portfolio "Dichtungssysteme, Elektrogießharze, Konstruktionsgießharze, Kantenvergusssysteme, Filtervergusssysteme und Klebstoffe", RAKU PUR als "zweikomponentige Polyurethan-Vergussmassen" (S, rampf-group.com-Pressemitteilungen und Broschüre Elektrogießharze, Zusammenfassung des Suchwerkzeugs). Ältere Meldungen 2020/21 nennen die Sparte noch "RAMPF Polymer Solutions" (Altname für die Patent- und CRM-Suche). Tom bestätigt.
- CRM: crm_abgleich.py "RAMPF Advanced Polymers", "RAMPF Holding", "RAMPF": kein Firmeneintrag; Treffer nur kundendatenbank_export.txt Zeile 15 (Opportunity Ungarn, RAMPF-Schaum/RAMPF 21-2056 als vom Kunden bemusterter Lieferant). Kein CRM-Kunde, Zeile 1 (E5) und 3 nicht ausgelöst. Hinweis für Vertrieb bleibt sinnvoll.
- Patente (Zusatzsuche enge Form): US11114719B2 "Electric cell potting compound and method of making", Anmelder RAMPF Advanced Polymers, Priorität 2019-02-15; Google-Status im Suchtext: aktiv, bis 2040 (ohne Gewähr, S); Familie US11594773B2, US11387511 (Batteriemodule, Schaum-Vergussmasse). CN110392945A auf der Seite mit Anmelder HB Fuller angezeigt: widersprüchlich, nicht gezählt. Ein weiteres Patent (flammhemmende PU-Zusammensetzung, Priorität 2023-07-26) nur im Snippet, Status ungeprüft. Espacenet/DEPATISnet nicht abfragbar.
- Korrekturen an Toms Feldern: Feld 9 Rechtsstand ergänzt (aktiv laut Google-Snippet); Feld 2/10 bestätigt.
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Ausschluss E1 mit Stufe V belegen. Frage: Stellt RAMPF Advanced Polymers in Grafenberg Vergussmassen/Klebstoffe als eigenes Produkt her? Wo nachsehen: rampf-group.com Produktseite "Elektrogießharze" bzw. Glossar "Potting Compounds", Impressum. Danach Rot nach Zeile 1 (E1). Aktion: kein Neukunde; Wettbewerbsbeobachtung am Stand A5.324.
- Nicht verwendbare Aussagen: Sitz-/Fertigungsort Grafenberg (S); Produktpalette (S, nur Zusammenfassung); Umsatz 219,3 Mio. EUR (S, eine Quelle); Rechtsstände der Patente (Google-Snippet). Stichprobe für Jey: nein.

## 2. RAMPF Production Systems GmbH & Co. KG | Stand A5.324 (Nr. 503)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB, Rot-Kandidat E1 (Tabellenzeile 7).** Anlagenhersteller für Misch-/Dosieranlagen für Dichten, Vergießen, Kleben: direkter Demak-Wettbewerber (E1), aber ohne Stufe V nicht Rot.
- Eigene Prüfung: Websuche bestätigt Zimmern ob Rottweil, "Misch- und Dosieranlagen für 1-, 2- und Mehrkomponenten-Reaktionskunststoffe für Dichten, Vergießen, Kleben", "mehr als 3.300 Anlagenlösungen", rund 220 Beschäftigte, mittelständisches Familienunternehmen (S, productronica-Broschüre 2025 und Pressemitteilungen Fakuma/Filtech 2024, Zusammenfassung). Produkte u. a. MC-EASY Multifunktionszelle. Nicht mit Advanced Polymers vermischt (Identität stimmt, S).
- CRM: crm_abgleich.py "RAMPF Production Systems", "RAMPF Holding": kein Firmeneintrag, nur Zeile 15 wie Block 1.
- Patente: Tom nennt EP4491267A1/WO2025012006A1 ohne Anmelder; ich habe keine Zuordnung gefunden, bleibt unbelegt. Eigene Zusatzsuche nicht wiederholt (Budget).
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): E1 mit V belegen (rampf-group.com Seite Production Systems, Impressum Zimmern ob Rottweil). Danach Rot. Aktion: als Wettbewerber führen, Referenzen für Feld 16 anderer Firmen auswerten.
- Nicht verwendbare Aussagen: Fertigungsort Zimmern (S); Zahlen 3.300/220 (S, Eigenangabe); Patentzuordnung EP4491267A1 (unbelegt). Stichprobe für Jey: nein.

## 3. RAPP Kunststofftechnik GmbH | Stand B3.141 (Nr. 504)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Spritzgießer (Teil der POLYRACK TECH-GROUP, Straubenhardt, Fertigung Spritzguss in Ettlingen): Mehrwerk-Gruppe, Sitzregel greift nicht, Fertigung nur S; zusätzlich Verguss Niedrig (A, reine Spritzgussteile), Zeile 6 käme erst nach Fertigungsbeleg.
- Eigene Prüfung: Websuche bestätigt Straubenhardt, gegründet 1993, 78 Beschäftigte 2023 (Implisense), "Kompaktspritzguss, Thermoplastischer Schaumguss, Mehrkomponententechnik", Werk Ettlingen (Blog 2015 und 2021, Alter beachten, Lehre 17). Kein Hinweis auf Baugruppenmontage oder Elektronikgehäuse. Tom: Ersteinschätzung "Steckverbinder" nicht bestätigt, stimme zu. Tom stuft "unwahrscheinlich"; bestätigt.
- CRM: crm_abgleich.py "RAPP Kunststofftechnik", "POLYRACK TECH-GROUP", "Polyrack": kein Treffer, neu. In Batch 43 stehen POLYRACK Electronic-Aufbausysteme (Zeile 5, Gelb) und die Holding (Zeile 7, Gelb): Bewertung gemeinsam mit Batch 43.
- Patente: eigene Wiederholung nicht ausgeführt; Toms Angabe (kein Anmelder RAPP) unbestätigt.
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Aktuelle Fertigung in Ettlingen/Straubenhardt belegen und prüfen, ob Montage-/Baugruppenschritte mit Kleben/Dichten/Vergießen stattfinden. Wo nachsehen: polyrack.com Seite "Plastics technology", Impressum RAPP, Stellenanzeigen Ettlingen. (b) Verhältnis zu Batch 43 (POLYRACK, gleicher Stand). Aktion: nicht priorisieren.
- Nicht verwendbare Aussagen: Fertigung Straubenhardt/Ettlingen (S, Blog 2015/2021); Verguss (A, Niedrig); Beschäftigtenzahl (S). Stichprobe für Jey: nein.

## 4. Ratioplast Electronics (H. Wiedemann GmbH) | Stand B3.411 (Nr. 505)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Sitzregel).** Hersteller kundenspezifischer Steckverbinder, Kunststoffteile und Werkzeuge mit "nahezu allen Fertigungsschritten im eigenen Haus" (S, Wirtschaftsforum) und erkennbarem Standort Lübbecke; Steckverbinder/Anschlussbaugruppen sind typisch überspritzt, vergossen oder verklebt (Mittel, A). Eigenverguss nicht belegt; Mehrwerk ist nicht ausgeschlossen (Niederlassung Bayern, Übernahme CS Components 2016).
- Eigene Prüfung: Websuche bestätigt "Ratioplast Electronics, H.Wiedemann GmbH", Jockweg 66, 32312 Lübbecke, gegründet 1966, Niederlassung in Bayern, 2016 Übernahme CS Components (S, wirtschaftsforum.de). Abgrenzung bestätigt: RATIOPLAST GmbH Schwabach und Sensor-Technik Wiedemann sind andere Firmen. Ratioplast-Optoelectronics GmbH (Jockweg 64/66, Lübbecke; Implisense: "Entwicklung und Fertigung elektronischer und mechanischer Produkte für Optoelektronik, Kommunikation, Energietechnik") ist wahrscheinlich Schwester oder Vorgängername, nicht belegt; Handelsregister nicht gefunden. Zeile 2 nicht ausgelöst, da Name und Sitz zur Vorgabe passen.
- CRM: crm_abgleich.py "Ratioplast Electronics", "Ratioplast Optoelectronics", "H. Wiedemann": kein Ratioplast-Treffer. Ähnlichkeit 0,88 nur zu Bihl+Wiedemann (bekannte_firmen Zeilen 256/257): andere Firma (Mannheim), kein Bezug; Zeile 3 nicht ausgelöst.
- Patente: Anmelder Ratioplast Optoelectronics GmbH: WO1998037446A1 / DE19706927C1 "Steckverbinder für Lichtwellenleiter" (1997), Folge DE19908231C2; kein Verguss als Gegenstand; Ratioplast-Electronics-Treffer: keine. Status nicht geprüft.
- Zitat im Browser bestätigt: nein.
- Nachrecherche (kein Gelb, für Mailstufe und endgültiges Grün nötig): Welche Steckverbinder/Konfektionen werden umspritzt oder vergossen? ratioplast.de Produktseiten, Datenblätter, Stellenanzeigen Lübbecke (Spritzguss/Montage); Impressum/Handelsregister (Rechtsform, Verhältnis zu Ratioplast-Optoelectronics, Standort CS Components).
- Nicht verwendbare Aussagen: Fertigung Lübbecke (A, gestützt durch S); Verguss/Überspritzung der Steckverbinder (A); "Eigenfertigung nahezu aller Schritte" (S, Interview); Rechtsform (S). Stichprobe für Jey: ja (schwaches Grün, Verguss nur aus Produkttyp).

## 5. REEL Reinheimer Elektronik GmbH | Stand C2.616 (Nr. 508)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Antennenhersteller (Fahrzeug-, Telematik-, Basisstationsantennen); Verguss plausibel bis wahrscheinlich, Fertigungsort aber nicht belegt und die Standortangabe (Hüttenberg gegen Wettenberg, LEI "lapsed") unklar; Sitzregel deshalb nicht sicher anwendbar (Lehre 4: Entwicklung ist keine Fertigung).
- Eigene Prüfung: Zwei Adressen bestätigt: Schmalheck 18, 35625 Hüttenberg (Datenblatt-PDF, dasoertliche) und Felsweg 6a, 35435 Wettenberg (it-in-germany.de); Website reinheimer-elektronik.de, kein Impressum erreicht. Händlerseite (mc-technologies.com) schreibt "entwickelt und produziert individuelle Antennensysteme seit 1994" (S, Händler, kein Beleg für den Ort). Datenblatt K70LFR (Stand 25.04.2022) nennt laut Suchzusammenfassung "vergossen" und wasserdicht IP 69K im verbauten Zustand, Option vergossene Kabeleinführung (S): das ist ein Direkthinweis auf Verguss (Verguss damit Hoch, Stufe S statt A; nicht V). Tom hatte Mittel (A). Kein Hinweis auf Auslandsfertigung gefunden, aber auch keiner auf Hessen.
- CRM: crm_abgleich.py "REEL Reinheimer Elektronik", "Reinheimer": kein Treffer, neu. Nicht verwechseln mit REEL GmbH Veitshöchheim (andere Firma, nicht im CRM geprüft).
- Patente: Anmelder REEL Reinheimer Elektronik, Wettenberg: EP0740361A1 "Flat antenna arrangement", DE29823087U1 (Breitband-Mehrbereichsantenne Fahrzeug), US7956814B2 / WO2007040748A1 (Antenne an Container, 2008 bzw. 2011 erteilt) laut Google-Snippets; kein Verguss als Gegenstand. Rechtsstand nicht geprüft.
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Wo werden die Antennen gefertigt (Hüttenberg/Wettenberg oder Ausland) und welche ist die aktuelle Anschrift? Wo nachsehen: reinheimer-elektronik.de Impressum/Unternehmensseite, Handelsregister Wetzlar HRB 7338, Stellenanzeigen, Datenblatt K70LFR im Original (Wortlaut "vergossen", Fertigungsvermerk). Danach Zeile 4 (Grün) bei Fertigung DE belegt. Aktion: nicht kontaktieren, bis Fertigungsort belegt ist.
- Nicht verwendbare Aussagen: Fertigung in Hessen (?/S); Verguss der Antennen (S, Datenblattzusammenfassung); "entwickelt und produziert" (S, Händler); Adresse (widersprüchlich). Stichprobe für Jey: ja (Standort und Fertigung ungeklärt, Verguss-Hinweis stark).

## 6. REHAG ELEKTRONIK GmbH | Stand C3.441 (Nr. 509)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB, Rot-Kandidat E2 (Tabellenzeile 7).** Hybrid-Distributor für aktive, passive, elektromechanische Bauelemente (Littelfuse, C&K, IXYS, Zilog, US Sensor), Services Taping, Programmieren, LED-Selektion (S, Luminovo-Partnerprofil, elektroniknet-Anbieterkompass); Rotenburg (Wümme) bestätigt. E2 ist inhaltlich naheliegend, aber nur S, daher nicht Rot (Zeile 1 braucht V).
- CRM: crm_abgleich.py "REHAG Elektronik": kein Treffer, neu. Patente: keine eigene Wiederholung (Distributor); Toms Angabe unbestätigt.
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Hat REHAG Eigenfertigung in DE/AT/NL oder nur Handel und Services (E2 mit V belegen)? Wo nachsehen: Firmenwebsite/Impressum, Unternehmensseite "Über uns" (Luminovo-Profil im Original lesen). Bei Bestätigung Rot (E2). Aktion: nicht aufnehmen.
- Nicht verwendbare Aussagen: Distributor ohne Fertigung (S); Gründung 1990 (S). Stichprobe für Jey: nein.

## 7. REINHARDT System- und Messelectronic GmbH | Stand A4.401 (Nr. 510)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN (Tabellenzeile 4, Fertigung Stufe A nach Sitzregel).** Eigenhersteller von Prüfsystemen und Wetterstationen/Klimasensoren in Dießen am Ammersee, ein Standort, kein Konzern, kein Händler, keine Auslagerungshinweise; Fachpresse: "entwickelt, produziert und vertreibt" (S). Klima-, Niederschlags- und Windsensoren im Außeneinsatz sowie Stationselektronik sind typisch vergossen oder verklebt (Hoch, A). Kein V-Beleg, daher Grün nur vorläufig.
- Eigene Prüfung: Websuche bestätigt Bergstr. 33, 86911 Dießen, Geschäftsführer Peter und Melanie Reinhardt, Handelsregister HRB 3350 Augsburg (Verzeichnis Die Deutsche Industrie, S), gegründet 1976, E-Mail info@reinhardt-testsystem.de; Wetterstation MWS 55M mit Burn-in und Klimakammer-Kalibrierung, Lüfter, optionaler Heizung (industrial-production.de, S). Kein Datenblatt mit IP-Klasse oder Verguss gefunden (Suche ohne Treffer, ausgeführt: "Wetterstation Sensor vergossen Fertigung", "MWS Schutzart IP Datenblatt"). Reinhardt GmbH Villingen-Schwenningen ist eine andere Firma und wurde nicht vermischt. Eine Stellenanzeige am Sitz fand ich nicht.
- Korrekturen an Toms Feldern: Feld 17 Registerangabe ergänzt (HRB 3350 Augsburg, S). Feld 10 "interessant" nicht bestätigt: beides nur A/S, nach Regel I nur mit Browser-Gegenlesen zu bestätigen; Einstufung vorläufig "prüfenswert-stark".
- CRM: crm_abgleich.py "REINHARDT System- und Messelectronic", "Reinhardt Testsystem": kein Treffer, neu.
- Patente: kein Patent mit Anmelder Reinhardt gefunden (Google Patents/Espacenet/DEPATISnet-Domainfilter); nur Produktnennung "MWS 5 W" in US20190064391A1 und US10539713B2 (Anmelder Dritte); DE10233149A1 nennt einen Erfinder "Reinhardt", Anmelder nicht ersichtlich, nicht zuordenbar. Acam-messelectronic-Treffer sind eine andere Firma. Keine Treffer ist kein Gegenbeweis.
- Zitat im Browser bestätigt: nein.
- Nachrecherche (kein Gelb, für Mailstufe nötig): Impressum/Standortseite reinhardt-testsystem.de (Fertigung am Sitz, V); Datenblatt MWS 55M und Sensoren (IP-Klasse, vergossene Elektronik/Sensorköpfe); Stellenanzeigen Dießen (Montage, Test).
- Nicht verwendbare Aussagen: Fertigung Dießen (A, gestützt durch S); Verguss aller Sensoren (A); "ca. 40 Beschäftigte" (S, evtl. veraltet); Register HRB 3350 (S). Stichprobe für Jey: ja (Grün ohne V-Beleg, Toms "interessant").

## 8. RENA Technologies GmbH | Stand B1.312 (Nr. 511)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Maschinenbauer für Nassprozessanlagen (Halbleiter, Solar, Medizintechnik). Konzern mit mehreren Werken: Sitzregel greift nicht. Korrektur zu Tom: laut Wirtschaftsforum-Interview auf rena.com (S) werden Anlagen "in Deutschland oder den USA assembliert, die Vorfertigung ist in Polen", "3 Fertigungsstandorte"; Gütenbach ist damit Montage- und Entwicklungsstandort, nicht die gesamte Fertigung. Verguss Niedrig (A, Prozessanlagen), Zeile 6 käme nach Fertigungsbeleg.
- Eigene Prüfung: Websuche bestätigt Hauptsitz Gütenbach, 1.100 installierte Maschinen, Tochter RENA Technologies North America (Albany, Oregon, früher MEI Wet Process Systems). Tom bestätigt "unwahrscheinlich".
- CRM: crm_abgleich.py "RENA Technologies", "RENA Sondermaschinenbau": kein Treffer, neu.
- Patente: keine eigene Wiederholung; Toms Angabe (nur Nassprozesspatente) unbestätigt.
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Welche Anlagen werden in Gütenbach montiert und enthalten Elektronik-/Sensorik-Baugruppen mit Verguss/Kleben/Dichten (zugekaufte Teile zählen)? Wo nachsehen: rena.com Interview-PDF "Interview-Wirtschaftsforum", Produktseiten, Stellenanzeigen Gütenbach Elektromontage. Aktion: nicht aufnehmen, außer Jey sieht Anlagen-Elektronik als Zielgruppe.
- Nicht verwendbare Aussagen: Fertigung Gütenbach (S, nur Montage); Verguss (A); Eigentümer Equistone (S); 560 Beschäftigte (S). Stichprobe für Jey: nein.

## 9. Renesas Electronics | Stand C5.479 (Nr. 512)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB, Rot-Kandidat E2 (Tabellenzeile 2, Identität).** Die ausstellende Gesellschaft ist nicht belegt: Renesas Electronics Europe GmbH (Arcadiastr. 10, 40472 Düsseldorf, HRB 3708 Amtsgericht Düsseldorf laut Companies-House-Eintrag, S; Vertriebsgesellschaft, 100 % Tochter von Renesas Electronics Corporation, Tokio, Bundesanzeiger-Zusammenfassung) gegen Renesas Electronics Germany GmbH (Dresden). Eine profibus.com-Seite nennt "Dinslaken" statt Düsseldorf (vermutlich Fehler, S).
- Konzern-Chip-Verkapselung (Mold/Underfill) ist Halbleiter-Backend und kein Demak-Anwendungsfall (A); Renesas-Patente (US5935314A, US6207296B1, US7268439B2) betreffen Epoxid-Formmasse und Underfill für Halbleiter, Anmelder Konzern. Rechtsstand nicht geprüft.
- CRM: crm_abgleich.py "Renesas Electronics", "Renesas Electronics Europe", "IDT", "Dialog Semiconductor": kein Treffer, neu.
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Welche Renesas-Gesellschaft stellt auf der electronica aus (Düsseldorf Vertrieb oder andere)? Ausstellerverzeichnis electronica und Renesas-Impressum lesen. (b) Wenn Düsseldorf: E2 (Vertriebsgesellschaft ohne Fertigung in DE/AT/NL) mit V belegen, dann Rot. Aktion: nicht aufnehmen.
- Nicht verwendbare Aussagen: Vertriebsgesellschaft (S); keine Fertigung der Einheit (S); Zuordnung der Patente zur Einheit (nein). Stichprobe für Jey: ja (Identität bestätigen).

## 10. Rennsteig Werkzeuge GmbH | Stand B2.228 (Nr. 513)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Handwerkzeug- und Crimpwerkzeughersteller, seit 1991 Tochter der KNIPEX-Werk C. Gustav Putsch KG, Wuppertal (Katalog, S): Tochterfirma, Stufe V nötig. Standortangaben uneinheitlich (Hauptsitz in Viernau, Fertigung in Altersbach, Anschrift Steinbach-Hallenberg). Verguss: Tom führt Mittel nur über Crimpmaschinen-Elektronik; meine Suche fand nur pneumatische Crimpmaschinen (CM 25, Datenblatt 2014, S) und keine Elektronik. Damit Verguss eher Niedrig (A); Tom selbst hält die Einstufung für schwach.
- CRM: crm_abgleich.py "Rennsteig Werkzeuge", "KNIPEX", "Knipex-Werk C. Gustav Putsch": kein Treffer, Konzern ebenfalls neu.
- Patente: Anmelder Rennsteig: EP2406040A1 (Rohrzange), DE102007019386B4 (Abmantelwerkzeug), US6176116B1, US6151950A (Crimpen): alles Mechanik; Zusatzsuche Verguss/Kleben/Dichtung ohne Rennsteig-Treffer. Rechtsstand nicht geprüft (teils alt).
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Fertigung belegen und Standort klären (Viernau/Altersbach/Steinbach-Hallenberg; Konzernzugehörigkeit Knipex, rennsteig.de Impressum/Unternehmensseite). (b) Baut Rennsteig Geräte mit Elektronik/Sensorik oder Isolierungen mit Verguss/Tauchen (rennsteig.de Katalog, Stellenanzeigen Elektronik/Montage)? Wird nichts gefunden, Verguss Niedrig und Gelb Zeile 6 bzw. nicht aufnehmen. Aktion: Beobachtung.
- Nicht verwendbare Aussagen: Produktion am Standort (S); Verguss der Crimpmaschinen (A, ohne Beleg); Beschäftigte/Umsatz (S, widersprüchlich 435/64 Mio. gegen 430/59,8 Mio.). Stichprobe für Jey: nein.

---

## Stichprobe für Jey (Klärungsbedarf)
- Reinhardt (Grün ohne V; Toms "interessant"), Ratioplast Electronics (schwaches Grün, Verguss nur Produkttyp, Verhältnis zu Ratioplast-Optoelectronics), REEL (Standort Hüttenberg/Wettenberg und Fertigungsort; Datenblatt mit "vergossen"), Renesas (welche Gesellschaft stellt aus).

## Einschränkungen
- Nur WebSearch (ca. 28 Abfragen), kein WebFetch, kein Chrome: keine Stufe-V-Aussage, keine Zitate im Seitentext geprüft, kein Impressum/Register direkt gelesen. Harte Ausschlüsse (RAMPF E1, REHAG E2, Renesas E2) konnten wegen fehlender V-Quelle nicht zu Rot führen (Tabellenzeile 1).
- Patentrecherche: Espacenet und DEPATISnet nicht direkt abfragbar; nur Google-Patents-Seiten über Domainfilter-Suche, Rechtsstände nur bei RAMPF (Google-Snippet). Für REHAG, Renesas, RENA, RAPP keine eigene Wiederholung. Feld 9 damit bei allen Firmen nicht belastbar; Batch nach F5 UNVOLLSTÄNDIG.
- Wettbewerbereinsatz (Feld 16): kein eigener Nachweis für Wettbewerberprodukte gefunden; keine belastbare Negativaussage.
- Alle Aussagen zu Fertigung, Produkt und Verguss sind Stufe S oder A; Quellen teils alt (RAPP/Polyrack Blog 2015 und 2021, Rennsteig Datenblatt 2014).
- Messe-Signal aus Toms Datei übernommen (aussteller_namen.txt nicht neu geprüft).
- Es wurde nichts verschickt und kein Datenbankfeld geändert.
