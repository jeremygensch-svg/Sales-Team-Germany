# Tina Batch 15 - agraria 2026, Wels (Prüfung von tom_batch_15.md)
Erstellt: 2026-11-25 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_15.md (10 Firmen, Nr. 141 bis 150 der Messeliste; hier Nr. 1 bis 10 des Batches). Länder der Messe: DE/AT/NL; alle zehn Firmen sind AT.
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Verfügbar waren nur WebSearch (6 Abfragen, Snippets/Kurzfassungen) und Bash. WebFetch wurde nicht eingesetzt, Chrome nicht verfügbar. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Keine Ampel ist mailtauglich, auch kein Grün.
Skripte: `python3 crm_abgleich.py` für alle Firmen samt Alt-/Konzern-/Schreibvarianten selbst wiederholt (Ergebnis: alle zehn neu; einzige Wortwurzel-Zufallstreffer "Josef Barthelme", "Wilhelm Gronbach/Schröder" ohne Bezug). Zusätzlich Grep auf gruber/gielesb/guntam/glinss/grube/granit/fricke in beiden CRM-Dateien: kein Treffer. Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum aller Einträge: 2026-11-25.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | Gielesberger Kran- und Trocknungstechnik GmbH (Halle 19, Stand 100) | GELB | 2 | ja |
| 2 | GKT - Green Kool Technology (Halle 23, Stand 230) | GELB | 2 | ja |
| 3 | Glinßner GmbH (Halle 18, Stand 230) | GELB | 6 | nein |
| 4 | Granit Quality parts (Halle 18, Stand 380) | GELB | 2 (Rot-Kandidat E2) | nein |
| 5 | Grube Forst GmbH (Halle 18, Stand 160) | GELB | 7 (Rot-Kandidat E2) | nein |
| 6 | Gruber GmbH (Halle 20, Stand A15) | GELB | 2 (Rot-Kandidat E2) | nein |
| 7 | Gruber Maschinen GmbH (Halle 20, Stand C30) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 8 | Gruber Otto GmbH (Halle 20, Stand B10) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 9 | Grundbichler Josef (Halle 18, Stand 60) | GELB | 7 (Rot-Kandidat E2) | nein |
| 10 | Guntamatic Heiztechnik GmbH (Halle 17, Stand 130) | GRÜN (schwach) | 4 (Sitzregel) | ja |

Zahlen: Grün 3 (alle schwach: nur Stufe S/A, Verguss nur aus Produkttyp), Gelb 7, Rot 0. Kein Rot, weil jeder Rot-Grund (E2 Händler) ohne Stufe V nicht belegbar ist (Tabellenzeile 1 verlangt Stufe V).

**Vollständigkeit von Toms Batch (Tom-Lauf wurde abgebrochen):** Die zehn Firmenblöcke sind vollständig (Felder 1 bis 17, Feld 11 leer wie vorgesehen). UNVOLLSTÄNDIG ist der Schlussabschnitt "Einschränkungen": er endet mit dem Verweis "Aussteller-Namensabgleich mit Regel-E1-Wettbewerbern: siehe unten", darunter steht nichts. Der Messe-Signal-Abgleich (Regel N2) fehlt damit in Toms Datei. Ich habe ihn nachgeholt: Grep der Wettbewerber-/Materialhersteller-Namen aus Regel E1 (Scheugenpflug, DOPAG, ViscoTec, RAMPF, bdtronic, Hilger u. Kern, Sonderhoff, Nordson, Musashi, ELANTAS, DELO, Henkel, Wacker, Sika, OTTO-CHEMIE, Panacol, Lohmann, Hexion, Marco, GONANO, EPOXONIC, WEVO) in agraria-2026/agraria_2026_aussteller_DE-AT-NL.csv: kein Treffer, es stellt kein E1-Wettbewerber auf der agraria aus. Ob Toms Abbruch weitere Inhalte (z. B. Gesamtfazit) gekostet hat, ist aus der Datei nicht erkennbar.

**Patente (Prüfpunkt 8, Regel F5):** Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar (kein Browser). Eigene Patent-Websuche nur für Guntamatic (1 Abfrage, Anmelder + Stichwort: kein Patent des Anmelders, einziger Treffer DE1579901C3 ist ein fremdes Altpatent ohne Guntamatic-Bezug). Für alle übrigen Firmen keine eigene Wiederholung; Toms WebSearch-Suchen werden weder übernommen noch widerlegt. Feld 9 ist damit bei ALLEN 10 Firmen ohne Datenbankabfrage: nach F5 UNVOLLSTÄNDIG, die beiden Datenbanksuchen (Google Patents + Espacenet/DEPATISnet) sind im Browser nachzuholen, bevor irgendein Grün als verwendbar gilt. Priorisierung: Guntamatic, Gruber Maschinen, Otto Gruber (Anmelder-Varianten "Otto Gruber Ges M B H Maschbau", "Maschb Otto Gruber"; Toms Treffer AT1167U3 und CH476450A mechanisch, nicht verguss-relevant, Rechtsstand fehlt).
**Wettbewerbereinsatz (F6):** Grep auf wettbewerber_referenzen.md mit allen Firmen-, Konzern- und Variantennamen sowie Hainzl, Fronius: kein Treffer (nur unverwandte Zeilen "Truma" und ein anonymer Heizungsanwender). Keine Einzelsuchen mit Wettbewerbernamen von mir. Kein Messe-Signal (siehe oben). Ohne Einfluss auf die Ampel.
**Entscheidungen Jey eingehalten:** Verbände/Prüfdienstleister/Forschung: keine im Batch. CRM mit gleichem/sehr ähnlichem Namen: keine (Thomas Gruber KG der Messeliste ist nicht Teil des Batches). Anlagenbauer: Gruber Maschinen und Guntamatic bleiben drin; keiner der zehn baut Verguss-/Dosieranlagen (E1 trifft nicht zu).

---

## 1. Gielesberger Kran- und Trocknungstechnik GmbH | Halle 19, Stand 100
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Zeile 1 greift nicht (kein E-Beleg), Zeile 2 trifft: Tom fand nur einen WKO-Eintrag einer Einzelperson (Manfred Gielesberger); mein Suchlauf "Gielesberger Vorchdorf Heukran Heutrocknung Steuerung Funkfernsteuerung Firma Website" fand weder eine Firma noch eine Website in Vorchdorf (nur Wettbewerber HSR Lengau, LASCO Lochen, Heutrocknung SR Straßwalchen). Rechtsform GmbH, Firmenbuch und Produkte der Firma sind damit nicht belegt. Ohne Identität kein Grün, auch wenn Verguss Mittel (A) und Fertigung Mittel (S/A) plausibel wären.
- CRM: crm_abgleich.py "Gielesberger Kran- und Trocknungstechnik GmbH" und "Gielesberger": kein Treffer, neu.
- Korrekturen an Toms Feldern: Feld 17 bestätigt (Identität offen); Feld 4 Sitz Vorchdorf bleibt S, nicht durch mich bestätigt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Gibt es die Gielesberger Kran- und Trocknungstechnik GmbH (Firmenbuch, Impressum), mit welcher Adresse, und was fertigt sie dort (Kran, Trocknungsanlage) mit welcher Steuerung? Wo: Firmenbuchauszug (firmenbuchgrundbuch.at / evi.gv.at), Messeprofil agraria Halle 19 Stand 100 und Eigenseite im Browser. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Sitz Vorchdorf (S), Produkte (S, Messetext), Fertigung (S/A), Verguss Mittel (A), Patent "keine Treffer" (nur Websuche). Stichprobe für Jey: ja (Firma nicht auffindbar).

## 2. GKT - Green Kool Technology | Halle 23, Stand 230
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Tom fand die Firma nicht (zwei Abfragen); die gefundene GKT GmbH Gloggnitz (ex GIG Karasek, Prozesstechnik) wird zu Recht nicht gleichgesetzt. Ich habe keine eigene Suche wiederholt (Suchbudget für aussichtsreichere Firmen priorisiert); Toms Negativbefund ist aus WebSearch und damit kein Beleg für "nicht vorhanden". Fertigung nur "?" , Verguss Mittel (A, Produkttyp Kühlanlage: Steuerung, Sensoren).
- CRM: "GKT - Green Kool Technology", "Green Kool", "GKT GmbH", "GIG Karasek": kein Treffer, neu.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer ist GKT - Green Kool Technology (Rechtsform, Sitz, Firmenbuch)? Gibt es einen Bezug zur GKT GmbH Gloggnitz? Fertigt die Firma selbst in AT und mit welcher Steuerung? Wo: Messeprofil agraria Halle 23 Stand 230 im Browser, Firmenbuch, Websuche "Green Kool Technology" mit Domain-Varianten. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alles außer dem Messeeintrag (S/A/?). Stichprobe für Jey: ja (Firma nicht auffindbar).

## 3. Glinßner GmbH | Halle 18, Stand 230
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6, Fertigung belegt-plausibel, Verguss Niedrig bei allen Bauteilen).** Schlosserei/Maschinenbau (Kippschaufeln "Kipptus", Holzrückezangen, Holzspalter), Sitz Pabneukirchen, Fertigung am Sitz (A nach Sitzregel, S laut WKO-Snippet). Alle Bauteile Niedrig (A): Stahlschweißbau, zugekaufte Hydraulikzylinder, einfache Schalter. Tabelle: Fertigung ok, Verguss Niedrig = Zeile 6, nicht Rot (Mangel an Beleg ist nie Rot). Identität "Glinßner GmbH" = "Josef Glinßner GmbH" wahrscheinlich, nicht belegt.
- CRM: "Glinßner GmbH", "Josef Glinßner GmbH", "Glinssner": kein Treffer, neu.
- Korrekturen: keine; Toms Einstufung "unwahrscheinlich" folge ich. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 6, niedrige Priorität): Gibt es elektrische/elektronische Baugruppen (Steuerung, Sensorik, Beleuchtung, Funkfernsteuerung) in den Produkten (Holzspalter, Holzrückezange, Kippschaufel)? Wo: Produktseiten/Prospekte (Messe Tulln Broschüre Unikipptus_2024.pdf), Eigenseite, Firmenbuch für Rechtsform. Aktion: nicht kontaktieren, nur falls Jey Landtechnik-Mechanikbauer nachprüfen will.
- Nicht verwendbare Aussagen: Fertigung Pabneukirchen (S/A), Verguss Niedrig (A), Mitarbeiterzahl (S). Stichprobe für Jey: nein.

## 4. Granit Quality parts | Halle 18, Stand 380
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Rot-Kandidat E2).** Granit Parts ist eine Handelsmarke der Wilhelm Fricke SE, Heeslingen (Großhandel Ersatzteile Landtechnik/Hydraulik, S). Wer in Wels ausstellt, ist nicht belegt (Identität offen, Zeile 2). Inhaltlich sehr wahrscheinlich E2 (Händler ohne Fertigung), aber ein Rot braucht Stufe V und die Identität des Ausstellers; beides fehlt. Fertigung Niedrig (S), Verguss Niedrig (A, Handelsware).
- CRM: "Granit Quality parts", "Wilhelm Fricke", "Granit Parts": kein Treffer (nur Wortwurzel-Zufälle "Wilhelm Gronbach/Schröder"), neu.
- Korrekturen: Toms Einstufung "kein Fertiger" bleibt als Hinweis; Ampel von Tom (leer) hier Gelb statt Rot, weil E2 ohne V nicht belegt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Welche juristische Person stellt unter "Granit Quality parts" aus (österreichischer Händler oder Fricke SE)? Wo: Messeprofil agraria Halle 18 Stand 380, Impressum von ersatzteilwelt.at/Granit-Partnershop. Bei Händler ohne Fertigung (V durch Impressum/Händlerseite): Rot nach E2. Aktion: nicht aufnehmen.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 5. Grube Forst GmbH | Halle 18, Stand 160
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7, Rot-Kandidat E2).** Identität stimmig (GRUBE-FORST GmbH, Gmundner Straße 25, 4663 Laakirchen, FN 107834 f, S; Firmenbuchzweck "Ausrüstungen für Wald, Landschaft, Natur und Umwelt"). Händler/Ausrüster (Schutzbekleidung, Forstgeräte als Handelsware), keine Fertigung belegt. E2 ist sehr wahrscheinlich, aber nur S, daher nicht Rot. Fertigung Niedrig (S), Verguss Niedrig (A).
- CRM: "Grube Forst GmbH", "Grube KG Forstgerätestelle", "Grube": kein Treffer, neu.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Fertigt Grube Forst eigene Produkte in Laakirchen oder ist es reiner Handel? Wo: Eigenseite/Impressum, Firmenbuch (Gewerbewortlaut), Herold. Bei reinem Handel (V): Rot nach E2. Aktion: nicht aufnehmen.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 6. Gruber GmbH | Halle 20, Stand A15
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt; Rot-Kandidat E2).** Messeprodukte Notstromaggregate und Mäher; häufiger Name. Beste Übereinstimmung: Gruber GmbH / Team Gruber, 4652 Steinerkirchen a. d. Traun (Fachhändler laut Snippets, S), aber nicht bestätigt. Händler ohne belegte Fertigung (Niedrig), Verguss Niedrig (A).
- CRM: "Gruber GmbH" (Kern-Name "gruber"), "Team Gruber": kein Treffer in beiden CRM-Dateien, neu. Wegen des Kern-Namens trotzdem Identitätsrisiko bei Gleichnamigen.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Welche Gruber GmbH stellt in Halle 20 Stand A15 aus (Ort, Firmenbuch), und fertigt sie selbst? Wo: Messeprofil agraria, Impressum von teamgruber/Honda-Händlerseite. Händler: Rot nach E2 (V nötig). Aktion: nicht aufnehmen.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 7. Gruber Maschinen GmbH | Halle 20, Stand C30
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN (schwach), Tabellenzeile 4 (Sitzregel).** Zeile 1 und 2 greifen nicht (kein E-Beleg, Name/Sitz stimmig: Kirchdorf 6, 4673 Gaspoltshofen), Zeile 3 nicht (CRM neu). Getreidetechnik-Hersteller (Silos, Mühlen, Mahl-/Mischanlagen) mit einem Standort, "Traditionsbetrieb seit mehr als 100 Jahren". Meine Suche (jobs.at/karriere.at-Snippets, S): Familienunternehmen mit ca. 80 Mitarbeitern, offene Stellen in Gaspoltshofen unter anderem Montage von Maschinen im Bereich Getreidetechnik (Förderer, Reinigungsmaschinen) und Ersatzteillager: stützt Fertigung/Montage am Sitz, bleibt S (nicht gelesen). Sitzregel (Stufe A) ist damit erfüllt. Verguss Mittel (A): Steuerungs-/Antriebselektronik der Mühlen, Füllstands-/Temperatursensoren Silo; Elektrotechnik-/Schaltschrank-Stellen bei Gruber habe ich nicht gefunden, die Eigenfertigung der Elektrik ist offen. Das Grün stützt sich damit auf Produkttyp (Maschinen mit Steuerung), nicht auf einen Beleg.
- CRM: "Gruber Maschinen GmbH": kein Treffer, neu. Nicht zu verwechseln mit Maschinenbau Otto Gruber GmbH und Gruber GmbH (Steinerkirchen).
- Korrekturen an Toms Feldern: keine inhaltlich; Feld 7 durch Stellenanzeigen-Snippet ergänzt (80 Mitarbeiter, Montage-Stelle, S). Zitat im Browser bestätigt: nein.
- Nachrecherche (kein Gelb, aber vor Mailverwendung nötig): getreidetechnik.com (Referenzen, Karriere, Impressum) im Browser lesen: Sensorik/Steuerung im Produkt, Schaltschrankbau am Sitz; Patentsuche Google Patents + Espacenet nachholen.
- Nicht verwendbare Aussagen: Sitz/Fertigung (S/A), Mitarbeiterzahl (S), Verguss Mittel (A), "keine Patente" (nur Websuche). Stichprobe für Jey: ja (Grün nur auf Produkttyp, schwach).

## 8. Gruber Otto GmbH | Halle 20, Stand B10
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN (schwach), Tabellenzeile 4 (Sitzregel).** Gemeint ist sehr wahrscheinlich Maschinenbau Otto Gruber GmbH, Harham 53, 5760 Saalfelden (Namensreihenfolge/Zusatz abweichend; Patent-Anmelder "Otto Gruber Ges M B H Maschbau" passt, Register nicht gelesen). Eigene Suche (Wirtschaftsforum-Snippets, S): entwickelt und fertigt Ladewagen/Miststreuer für alpine Regionen, 40 Mitarbeiter am Standort Saalfelden, ca. 5 Mio. EUR Umsatz (Größe optional); keine Hinweise auf Konzern oder Auslagerung. Sitzregel erfüllt. Verguss Mittel (A) mit Tendenz nach oben: neues Bremssystem mit ABS/EBS/EWS (elektronisches Bremssystem, Stabilisierung) laut topagrar-Snippet (eine Quelle, S) und Ladeautomatik-Sensoren am Ladewagen (Prospekt-Snippet, S). Ob Steuergerät/Sensoren selbst gebaut oder zugekauft werden, ist offen (Bauteil-Regel: zugekauft zählt trotzdem).
- CRM: "Gruber Otto GmbH", "Maschinenbau Otto Gruber", "Otto Gruber": kein Treffer, neu.
- Korrekturen an Toms Feldern: Feld 6/8 ergänzt um ABS/EBS-Steuerung und Sensorik der Ladeautomatik (S) statt nur "Bremssteuerung"; Feld 17 weiter offen (Firmenbuch evi.gv.at/f/71274s tauchte in der Suche auf, nicht gelesen, Zuordnung unbestätigt). Zitat im Browser bestätigt: nein.
- Nachrecherche (vor Mailverwendung): (a) Impressum/Firmenbuch: "Gruber Otto GmbH" = Maschinenbau Otto Gruber GmbH? (b) Produktseite Bremssystem/Ladeautomatik: Elektronik Eigenbau oder Zukauf, welche Hersteller? (c) Patentsuche Google Patents/Espacenet nachholen (Toms Treffer AT1167U3, CH476450A nur Mechanik, Rechtsstand CH476450A laut Snippet "ceased").
- Nicht verwendbare Aussagen: Sitz/Fertigung (S/A), Mitarbeiter/Umsatz (S, eine Quelle), Verguss Mittel (A), Bremssystem (S, eine Quelle). Stichprobe für Jey: ja (Identität und Grün auf Produkttyp).

## 9. Grundbichler Josef | Halle 18, Stand 60
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7, Rot-Kandidat E2).** Landmaschinenhändler ("Since 22 years Dealer", Kellau 35, 5431 Kuchl, landwirt.com-Händlerverzeichnis, S), keine Fertigung belegt, Handelsware Motormäher/-sägen. E2 sehr wahrscheinlich, aber nur S, daher nicht Rot. Fertigung Niedrig (S), Verguss Niedrig (A).
- CRM: "Grundbichler Josef", "Grundbichler": kein Treffer, neu.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Reiner Handel/Werkstatt oder eigene Fertigung? Wo: Händlerverzeichnis landwirt.com lesen, Gewerbeauskunft/Firmen-A-Z (WKO). Bei Handel (V): Rot nach E2. Aktion: nicht aufnehmen.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 10. Guntamatic Heiztechnik GmbH | Halle 17, Stand 130
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN (schwach), Tabellenzeile 4 (Sitzregel).** Identität stimmig: GUNTAMATIC Heiztechnik GmbH, Bruck 7, 4722 Peuerbach, FN 96219z, ca. 250 Mitarbeiter, "develops and produces biomass heating systems" (evi.gv.at- und Heinze-Snippets, S; Lambrechten der Vorgabe nicht belegt). Fertigung Peuerbach: Fronius-Anwenderbericht-Snippet "Processing, parts production, and assembly are almost entirely completed in-house" (S); Industrie-/Gerätebauer, ein Standort, eigene Produkte, kein Konzernhinweis: Sitzregel (Stufe A) erfüllt. Verguss Hoch (A, Bauteil-Regel, höchstes Bauteil): Temperatur-/Lambda-/Füllstandssensoren, EC-Lüfter-/Saugzugmotoren mit Elektronik, Steuerplatinen, Zünd-/Heizelemente. Die Steuerelektronik (ca. 10.000 Baugruppen/Jahr) liefert laut Hainzl-Referenzseite (Snippet, S) der EMS-Dienstleister HAINZL, Linz (AT); das ändert nach Bauteil-Regel die Ampel nicht, ist aber für die Ansprache wichtig (Verguss der Platinen eventuell bei Hainzl). Kein Hinweis auf Verguss/Dichtung in der Suche (kein Gegenbeleg). Patent: 1 eigene Suche, kein Patent von Guntamatic gefunden (Google-Patents/Espacenet nicht abgefragt).
- CRM: "Guntamatic Heiztechnik GmbH", "Guntamatic", "Hainzl": kein Treffer, neu. Wettbewerbereinsatz: kein Eintrag in wettbewerber_referenzen.md.
- Korrekturen an Toms Feldern: keine inhaltlichen; Mitarbeiterzahl 250 durch zweite Snippet-Quelle (Heinze/evi) gestützt, aber beides S. Zitat im Browser bestätigt: nein.
- Nachrecherche (vor Mailverwendung, Grün-Kandidat): (a) Impressum und Produktseiten guntamatic.com im Browser lesen (Zitat zur Fertigung in Peuerbach, Steuerungen BIOSMART/BIOCOM); (b) Fronius-Referenz öffnen und Zitat gegenlesen; (c) Stellenanzeigen Peuerbach (Elektromontage/Elektronik); (d) Patentsuche Google Patents + Espacenet/DEPATISnet, Schreibweise GUNTAMATIC/Guntamatic Heiztechnik; (e) wer vergießt/bestückt die Steuerplatinen (Hainzl-Seite lesen).
- Nicht verwendbare Aussagen: Fertigung in Peuerbach (S, Fronius-Zusammenfassung), Mitarbeiterzahl (S), Verguss Hoch (A), Elektronik bei Hainzl (S), "keine Patente" (nur Websuche). Stichprobe für Jey: ja (Grün-Kandidatin, Toms "interessant", ohne eine V-Quelle).

---

## nicht aufgenommen (bereits bekannt / unklar)
- Bereits im CRM: keine Firma des Batches (crm_abgleich.py für alle zehn plus Varianten: neu).
- Nicht weiterverfolgen, falls Jey die Händler-Einordnung bestätigt (Rot-Kandidaten E2, Beleg V fehlt): Granit Quality parts (Nr. 4), Grube Forst GmbH (Nr. 5), Gruber GmbH (Nr. 6), Grundbichler Josef (Nr. 9).
- Identität unklar: Gielesberger Kran- und Trocknungstechnik GmbH (Nr. 1), GKT - Green Kool Technology (Nr. 2), Granit Quality parts (Nr. 4), Gruber GmbH (Nr. 6).

## Einschränkungen
- Nur WebSearch (6 Abfragen, Snippets/Kurzfassungen) und Bash; kein Browser, WebFetch nicht genutzt. Keine Stufe V, keine Quelle im Volltext gelesen, kein Zitat gegengelesen. Alle Ampeln vorläufig; die drei Grün sind schwach (nur S/A).
- Patentdatenbanken (Google Patents, Espacenet, DEPATISnet) nicht abgefragt; Feld 9 bei allen Firmen nach F5 unvollständig, Nachholen im Browser nötig. Eigene Patent-Websuche nur für Guntamatic.
- Nicht durchgeführte eigene Suchen (offen): GKT/Green Kool (keine Wiederholung), Glinßner, Granit/Fricke, Grube Forst, Gruber GmbH, Grundbichler (nur CRM + Einordnung nach Toms Quellen, wie vom Auftrag für Händler/kleine Mechanikbauer vorgesehen); Wettbewerbereinsatz-Einzelsuchen mit Wettbewerbernamen für alle Firmen.
- Aussteller-Beschreibungen der Messe sind Stufe S (Regel N5); agraria.at nicht gegengelesen.
- Toms Lauf war abgebrochen: Schlussabschnitt "Einschränkungen" endet ohne den angekündigten E1-Abgleich; von mir nachgeholt (kein Treffer in der Ausstellerliste).
- Es wurde nichts verschickt und kein Datenbankfeld geändert; kein git commit.
