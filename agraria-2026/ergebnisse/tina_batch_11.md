# Tina Batch 11 - agraria 2026 (Prüfung von tom_batch_11.md)
Erstellt: 2026-11-25 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_11.md (Messe agraria Wels 25.-28.11.2026, Länder DE/AT/NL, 10 Firmen, Nr. 101 bis 110).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (5 Abfragen, Snippets/Kurzfassungen) und Bash zur Verfügung; WebFetch und Chrome nicht genutzt/nutzbar. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein. Kein Grün, nichts mailtauglich.
Skripte: `python3 crm_abgleich.py` für alle 10 Firmen samt Konzern-/Marken-/Alt-/Schwesternamen selbst wiederholt (CLA Tech, CLAAS, CLAAS Austria, ClimaBarn, FabricAir, FabricAir Austria, CNH Industrial (Österreich), CNH, Case IH, New Holland, Steyr Traktoren, cooks catering, Country, Hõbekala, DeLaval, Tetra Laval, DeLaval Österreich, Deschberger (Karl/Landtechnik), DEUTZ-FAHR, Deutz, SDF, SDF Group, SAME Deutz-Fahr, Deutz-Fahr Land). Einziger Treffer: Nr. 110 (Deutz AG / DEUTZ AG, bekannte_firmen_DE-AT-NL.txt Zeilen 509/510). Der Steyr-Fehltreffer (BMW) aus Toms Lauf tritt bei "Steyr Traktoren" nicht auf. Wettbewerberabgleich: Grep auf wettbewerber_referenzen.md nach CLAAS, CNH, Case IH, Steyr, New Holland, DeLaval, Deutz, SDF, Same, FabricAir, ClimaBarn, Country, Deschberger, CLA Tech: kein Treffer. Messe-Signal (Wettbewerber unter den DE/AT/NL-Ausstellern): von Tom übernommen, keiner; ohne Einfluss auf die Ampel. Verifikationsdatum aller Einträge: 2026-11-25. Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md).

Jey-Entscheidungen angewandt: Verbände/Prüfdienstleister/Forschung raus (keine im Batch); CRM-Namensähnlichkeit raus (Nr. 110, Einordnung siehe dort); Anlagenbauer bleiben drin, außer sie bauen selbst Verguss-/Dosieranlagen (E1): keine Firma betroffen. Händler/Vertriebsgesellschaften: Rot-Kandidat E2, aber mangels Stufe V nur Gelb.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 101 | CLA Tech Maschinen- und Fertigungstechnik GmbH (Halle 18, Stand 530) | GELB | 7 | nein |
| 102 | CLAAS Regional Center Central Europe GmbH (Freigelände, Stand 30) | GELB | 7 (Rot-Kandidat E2) | nein |
| 103 | ClimaBarn (Halle 18, Stand 460) | GELB | 2 (Rot-Kandidat E3) | nein |
| 104 | CNH Industrial Österreich GmbH (Halle 20, Stand A10) | GELB (aussichtsreichste Firma) | 5 | ja |
| 105 | cooks catering GmbH (Freigelände, Stand 40) | GELB | 2 (Rot-Kandidat E2) | nein |
| 106 | Country OÜ (Halle 20, Stand B10) | GELB | 2 (Rot-Kandidat E3) | nein |
| 107 | DeLaval (Halle 23, Stand 160) | GELB | 2 | ja |
| 108 | Deschberger Karl GesmbH & Co KG (Halle 19, Stand 240) | GELB | 7 (Rot-Kandidat E2) | nein |
| 109 | Deschberger Landtechnik GmbH (Freigelände, Stand 10) | GELB | 7 (Rot-Kandidat E2) | nein |
| 110 | DEUTZ-FAHR (Halle 21, Stand C30) | GELB | 3 (nach Jey-Entscheidung raus, Bestätigung nötig) | ja |

Zahlen: Grün 0, Gelb 10, Rot 0. Kein Grün, weil bei Konzernen (CNH, DEUTZ-FAHR, DeLaval) Stufe V für die Fertigung fehlt und ohne Browser nicht beschaffbar war; Rot nirgends, weil jeder Ausschluss (E2/E3) nur mit Stufe S belegt ist.

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Eigene Patent-Websuche nur für CNH (1 Abfrage, nur generische USPTO-Treffer ohne Anmelderzuordnung, kein CNH-Patent bestätigt). Für die übrigen 9 Firmen keine eigene Wiederholung; Toms WebSearch-Suchen werden weder übernommen noch widerlegt. Feld 9 ist damit bei ALLEN 10 Firmen ohne Datenbankabfrage: nach F5 UNVOLLSTÄNDIG, Nachholen im Browser nötig (Priorität: Nr. 107 US11864528B2 Rechtsstand und Vergussbezug, Nr. 104, Nr. 110). Kein Rechtsstand irgendwo geprüft. Wettbewerbereinsatz (F6): nur Listenabgleich; keine Einzelsuchen mit Wettbewerbernamen von mir.

---

## 101. CLA Tech Maschinen- und Fertigungstechnik GmbH | Halle 18, Stand 530
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Zeile 1-3 greifen nicht (kein E-Beleg, Identität nur S aber stimmig, CRM neu). Zeile 4 nicht, da das Produkt (Hühnerstall, Stahl/Stalleinrichtung) kein typisch vergossenes Bauteil zeigt; Zeile 6 nicht, da Fertigung nur nach Sitzregel (A) und Produkte unbelegt. Anlagenbauer bleibt drin (Jey), E1 nicht belegt. Verguss Niedrig bis Mittel (A, nur falls Steuerung/Türautomatik verbaut).
- Eigene Prüfung: CRM neu (Skript, drei Schreibweisen). Eigene Suche "CLA Tech ... Guntersdorf Hühnerstall Produkte": kein einziger Treffer zur Firma, Toms Befund (WKO-Snippet) nicht bestätigt, aber auch nicht widerlegt.
- Korrekturen an Toms Feldern: Feld 8 ist uneinheitlich (Gesamt Niedrig, Einzelbauteil Türautomatik Mittel); nach Bauteil-Regel ist das Maximum Mittel (A, unbelegt). Feld 10 "unwahrscheinlich" daher nicht gedeckt, besser "prüfenswert (offen)". Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Was baut CLA Tech (Stalleinrichtung, Stahlbau, Zulieferteile) und verbaut sie Elektronik/Steuerungen? Wo: Impressum/Produktseite cla-tech.at im Browser lesen (Domain war für Tom nicht auflösbar), Firmenbuch evi.gv.at. Bei reinem Stahlbau ohne Elektronik: Verguss Niedrig, kein Ziel. Aktion: nicht kontaktieren, niedrige Priorität.
- Nicht verwendbare Aussagen: alle (S/A): Sitz, Fertigung, Produkt, Verguss. Stichprobe für Jey: nein.

## 102. CLAAS Regional Center Central Europe GmbH | Freigelände, Stand 30
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7, Rot-Kandidat E2).** Vertriebsgesellschaft (Spillern, FN 474371f, nur S) ohne eigene Fertigung: E2 wahrscheinlich, aber ohne Stufe V nach Zeile 1 nicht Rot. CRM: weder Gesellschaft noch Konzern CLAAS, CLAAS Austria im CRM (Skript), also neu.
- Eigene Prüfung: Skript bestätigt Toms Abgleich. Konzernwerke (Harsewinkel, Paderborn, Bad Saulgau) sind andere Einheiten; Verguss dort Hoch (A), für diese Gesellschaft nicht anwendbar.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Bestätigen, dass die Gesellschaft reine Vertriebs-/Rentalgesellschaft ist (Firmenbuch-Unternehmensgegenstand, Impressum claas.com/AT). Bei Bestätigung Rot E2. Optional an Jey: Sollen die CLAAS-Werke (Selbstfahrende Erntemaschinen GmbH, Harsewinkel u. a.) separat als Kandidaten geprüft werden? Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle zu Fertigung/Verguss (S/A). Stichprobe für Jey: nein.

## 103. ClimaBarn | Halle 18, Stand 460
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Rot-Kandidat E3).** Aussteller ist eine Marke (FabricAir A/S, Dänemark), keine Rechtseinheit; ausstellende Einheit unklar, Identität nicht belegt. Fertigung in DE/AT/NL nicht belegt, Produktionsort offen; in AT nur FabricAir Austria GmbH (Vertrieb, S). Verguss Mittel (A, zugekaufte EC-Ventilatoren/Steuerung). CRM: ClimaBarn, FabricAir, FabricAir Austria kein Treffer, neu.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer stellt aus (FabricAir Austria GmbH oder anderer Träger) und wo wird ClimaBarn produziert? Impressum climabarn.de und fabricair.com im Browser lesen, Messe-Detailseite agraria.at. Bei Produktion außerhalb DE/AT/NL: Rot E3. Aktion: nicht kontaktieren, niedrige Priorität.
- Nicht verwendbare Aussagen: Herkunft/Produktion, Verguss (S/A). Stichprobe für Jey: nein.

## 104. CNH Industrial Österreich GmbH | Halle 20, Stand A10
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Fertigungsbeleg V fehlt).** Konzern mit mehreren Werken, Sitzregel gilt nicht, Stufe V nötig; Fertigung St. Valentin nur S (mehrere Snippets: WKO-Portrait, trend.at, CNH-Presse "St. Valentin plant breaks 10,000 tractors barrier"). Verguss Hoch (A: Steuergeräte, Sensoren, LED-Scheinwerfer; Terminals/Optical Bonding Mittel). Wäre bei V-Beleg Grün (Zeile 4). CRM: CNH Industrial (Österreich), CNH, Case IH, New Holland, Steyr Traktoren: kein Treffer, Konzern nicht im CRM (Regel M kein Konzernbezug).
- Eigene Prüfung: Suche zu Stellenanzeigen St. Valentin zeigt Test-/Software-/Field-Service-/Elektrotechnik-Stellen (karriere.at, jobs.at, devjobs.at; nur Snippets, S), aber keine Montageanzeige. Das stützt den Standort als Entwicklungs-/Teststandort, ersetzt aber keinen Produktionsbeleg. Eigene Patentsuche (1 Abfrage): nur generische USPTO-Potting-Treffer ohne CNH-Anmelder; kein CNH-Patent bestätigt (kein Gegenbeweis).
- Korrekturen an Toms Feldern: Feld 15 widersprüchlich (860/599 Mitarbeiter), nicht verwenden. Feld 10 "interessant" nach Regel I ohne Browser-Gegenlesen nicht bestätigbar. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (1) Fertigungsbeleg V: Wird in St. Valentin montiert (Traktorenwerk Steyr/Case IH)? Pressemeldung media.cnh.com und Standortseite im Browser lesen, wörtliches Zitat sichern. (2) Welche Elektronik (Kabelbäume, Terminals, Steuergeräte) wird im Werk montiert/zugekauft? Karriereseite careers.cnh.com, Produktionsstellen St. Valentin. (3) Patente CNH im Browser (Google Patents/Espacenet/DEPATISnet, Anmelder CNH Industrial Italia/America/Belgium, Rechtsstand). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung St. Valentin (S), Verguss (A), Größe. Stichprobe für Jey: ja (aussichtsreichste Firma, V-Beleg fehlt).

## 105. cooks catering GmbH | Freigelände, Stand 40
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Rot-Kandidat E2).** Firma mit diesem Namen nicht auffindbar (Identität nicht belegt, nur Messelisteneintrag), Catering-Dienstleister ohne Produkt. CRM neu (Skript, "cooks catering", "Cooks"). Verguss Niedrig (A).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Existiert die Firma (Firmenbuch evi.gv.at, Messe-Detailseite agraria.at) und ist sie tatsächlich nur Gastronom? Bei Bestätigung Rot E2 (Dienstleister). Vorschlag: Jey kann das ohne Recherche streichen. Aktion: nicht aufnehmen.
- Nicht verwendbare Aussagen: alle. Stichprobe für Jey: nein.

## 106. Country OÜ | Halle 20, Stand B10
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Rot-Kandidat E3).** Messeliste führt AT, Register (inforegister.ee, S) zeigt OÜ Country, Estland (Reg.-Nr. 12565983): Identität widersprüchlich. Fertigung vermutlich Estland (E3), nicht V. Verguss Niedrig (A). CRM neu (Skript).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Ist der Messeaussteller die estnische OÜ Country, und liegt die Fertigung in Estland? country.ee Kontakt/Impressum im Browser lesen, Messe-Detailseite. Bei Bestätigung Rot E3. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigungsort, Umsatz 6,42 Mio. (S). Stichprobe für Jey: nein.

## 107. DeLaval | Halle 23, Stand 160
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2: ausstellende Einheit nicht belegt; zugleich wäre Zeile 5 offen).** Verguss Hoch (A; Patent US11864528B2 DeLaval Holding AB, CPC H05K5/064, nur Snippet-Signal, Rechtsstand ungeprüft). CRM neu (DeLaval, Tetra Laval, DeLaval Österreich).
- Eigene Prüfung: Suche zu Standorten: Konzernproduktion Tumba (SE); DeLaval GmbH Deutschland in Glinde (Sitz), Gallin = weltweites Logistikzentrum (kein Werk), DeLaval GesmbH Österreich in Eugendorf (Händlerbetreuung, kein Werk) (alle S). Hoogezand (NL) nicht bestätigt, Toms Beispiel damit ungedeckt. Kein Fertigungsstandort in DE/AT/NL gefunden; ausstellende Einheit am wahrscheinlichsten die Vertriebsgesellschaft Eugendorf (nicht belegt).
- Korrekturen an Toms Feldern: Feld 7 "Mittel" überschätzt; ohne Werk-Beleg in DE/AT/NL eher Niedrig bis offen. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Welche Einheit stellt in Wels aus (DeLaval GesmbH Österreich, Eugendorf?) und fertigt sie? Messe-Detailseite, Firmenbuch. (b) Gibt es ein DeLaval-Werk in DE/AT/NL? delaval.com Standortseite "DeLaval Worldwide", Stellenanzeigen Produktion. (c) US11864528B2 im Browser, Rechtsstand und Vergussbezug. Ohne Werk in DE/AT/NL: Rot E3 bzw. E2 für die Vertriebsgesellschaft. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung, Verguss, Patentbezug (S/A). Stichprobe für Jey: ja.

## 108. Deschberger Karl GesmbH & Co KG | Halle 19, Stand 240
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7, Rot-Kandidat E2).** Landtechnikhändler (landwirt.com-Händlerprofil, S) ohne belegte Fertigung. CRM neu (Skript). Verguss Niedrig (A).
- Korrekturen: keine. Namensabweichung (Messe ohne "Landtechnik") unkritisch, Verhältnis zu Nr. 109 offen. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Hat die Firma Eigenfertigung (z. B. Silo-/Förderanlagenbau)? Firmenbuch und Firmenwebsite/Impressum im Browser; Klärung Gruppe mit Nr. 109. Sonst Rot E2. Aktion: nicht aufnehmen.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 109. Deschberger Landtechnik GmbH | Freigelände, Stand 10
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7, Rot-Kandidat E2).** Händler, Sitz Senftenbach nur aus einer Anzeige (S), Identität schwach. CRM neu (Skript).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Firmenbuch (Rechtsform, Sitz, Gegenstand) und Impressum deschberger-landtechnik.at im Browser lesen; Eigenfertigung ja/nein; Beziehung zu Nr. 108. Sonst Rot E2. Aktion: nicht aufnehmen.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 110. DEUTZ-FAHR | Halle 21, Stand C30
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 3, nach Jey-Entscheidung "CRM-Name ähnlich = raus" nicht aufnehmen).** Skript: Präfix-Treffer Deutz AG / DEUTZ AG (Zeilen 509/510); SDF, SDF Group, SAME Deutz-Fahr kein Treffer. Deutz AG (Köln, Motoren) und DEUTZ-FAHR (SDF Group, Italien; Werk DEUTZ-FAHR Land, Lauingen) sind nach Suchlage verschiedene Unternehmen, E5 (dieselbe Einheit) daher nicht belegt, also kein Rot. Ich folge der Entscheidung von Jey (raus), führe aber Gelb, weil Rot formal nicht begründbar ist. Wäre ohne CRM-Bezug: Fertigung Lauingen S (Traktoren 6/7/9-Serie, Eröffnung 2017, mehrere Snippets; Konzern, daher V nötig) und Verguss Hoch (A) = Zeile 5 Gelb.
- Eigene Prüfung: Suche bestätigt Werk Lauingen (profi.co.uk, deutz-fahr.com Pressemeldung 2017 und Product Range 2025; nur Snippets, S); Impressum nicht gefunden. Ausstellende Einheit in Wels weiter ungeklärt.
- Korrekturen: Feld 12 "unklar" korrekt, Feld 3 (Bayern) nur für Lauingen, nicht für Messeeinheit. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 3, an Jey): Soll SDF/DEUTZ-FAHR Land (Lauingen) trotz Namensähnlichkeit zu Deutz AG als eigener Kunde geführt werden? Falls ja: Impressum DEUTZ-FAHR Land GmbH und Werkseite im Browser lesen (Fertigungsbeleg V), Handelsregister, ausstellende Einheit klären. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Lauingen (S), Verguss (A). Stichprobe für Jey: ja (Entscheidung).

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind durchgehend korrekt niedrig angesetzt; keine V-Aussage vorgetäuscht. Seine Einstufungen "interessant" (Nr. 104, 110) sind ohne Browser-Gegenlesen nicht bestätigbar.
- Tom hat Feld 11 (Ampel) leer gelassen, wie vorgesehen; von mir gefüllt.
- Drei der Gelb sind faktisch Rot-Kandidaten Händler/Dienstleister (102, 105, 108, 109) und zwei Ausland (103, 106); Rot erst nach V-Beleg (ein Impressum/Firmenbuchblick).
- Nr. 107: Toms Hoogezand-Beispiel ist durch meine Suche nicht gedeckt; Fertigung Feld 7 "Mittel" zu optimistisch.
- Vorschlag Fehlerlog (nicht eingetragen): Messeaussteller mit Marken-/Konzernnamen (DeLaval, DEUTZ-FAHR, ClimaBarn) früh auf ausstellende Rechtseinheit prüfen.

## Einschränkungen
- Browser und WebFetch nicht verfügbar: kein Gegenlesen nach Abschnitt H, keine Impressen, Datenblätter oder Karriereseiten gelesen; alle Aussagen Stufe S, A oder ?.
- WebSearch: 5 Abfragen (CNH Stellen/Werk, DEUTZ-FAHR Lauingen, DeLaval Standorte, CNH Patent, CLA Tech). NICHT durchgeführt: eigene Suchen für Nr. 102, 103, 105, 106, 108, 109 (nur CRM und Einordnung, wie beauftragt für Händler/Dienstleister; bei 103 und 106 ist der Ausland-Befund nur Toms Snippet-Stand), keine eigene Patentsuche außer CNH.
- Patente: Pflichtsuche F5 (Google Patents, Espacenet, DEPATISnet) für alle 10 Firmen nicht erfüllt; Batch UNVOLLSTÄNDIG. Rechtsstand nirgends geprüft. Anmeldervarianten (CNH Industrial Italia/America, DeLaval Holding AB, SDF S.p.A.) zurückgestellt.
- Wettbewerbereinsatz (F6): nur Listenabgleich und Toms Angaben; "kein Hinweis" ist kein Gegenbeweis.
- Handelsregister/Firmenbuch nicht abgerufen. Kundendatenbank (Excel) nicht lesbar; CRM-Abgleich per Skript auf Textexporte. Keine "Verifiziert am"-Prüfung nötig (kein Treffer außer Nr. 110).
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
