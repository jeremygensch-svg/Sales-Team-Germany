# Tina Batch 26 - agraria 2026 (Prüfung von tom_batch_26.md)
Erstellt: 2026-11-26 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_26.md (10 Einträge, Nr. 251 bis 260; Nr. 257 und 258 sind zwei Abteilungen derselben RWA AG). Eine ältere Datei tina_batch_26.md existierte nicht (der abgebrochene Lauf hat nichts hinterlassen); diese Datei ist die vollständige Neufassung. Nummerierung im Block `## N.` ist die laufende Nummer 1 bis 10 wie bei Tom; die Messe-Nr. steht in Klammern.
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (Snippets/Kurzfassungen, 10 eigene Abfragen) und Bash zur Verfügung; kein Browser, kein WebFetch. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün, nichts mailtauglich.
Skripte: `python3 crm_abgleich.py` für alle Firmen samt Konzern-/Alt-/Schwesternamen selbst wiederholt (RZO, RMIG, RM Hutter, Hutter Lochbleche, Reiter Lochbleche, Roto Tech, Rotschne, RT Engineering / RT Engineering Anlagentechnik, Reiter, Reiter Respiro, Rubner, RWA, Raiffeisen, Raiffeisen Ware Austria, Saatbau, samo, Samo Maschinenbau): einziger Treffer AEHNLICH 0.90 für "RT Engineering" gegen bekannte_firmen_DE-AT-NL.txt:2384 "TQN ENGINEERING [DE]" (manuell: Ähnlichkeitseffekt des Wortes Engineering, kein Namensbezug). Zusätzlich Grep auf die Aussteller-CSV: alle Schreibweisen bestätigt; die CSV führt zu RMIG als Produktprofil auch "Saatgut-, -beet, -druckwalzen, -reinigung; Trocknungsanlagen" (Messeliste, S).
Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum aller Einträge: 2026-11-26.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | Rinderzuchtverband und Erzeugergemeinschaft OÖ (RZO) (Halle 24 / Stand 10; Nr. 251) | ROT (Entscheidung Jey: Verbände raus) | 1/E-Katalog nicht anwendbar, Jey-Vorgabe | nein |
| 2 | RMIG Lochbleche GmbH (Halle 23 / Stand 490; Nr. 252) | GELB (niedrige Priorität) | 7 | nein |
| 3 | ROTO-TECH GmbH (Halle 18 / Stand 240; Nr. 253) | GELB | 2 | ja |
| 4 | Rotschne Josef KG (Halle 20 / Stand F70; Nr. 254) | ROT (E2 Händler, nur Stufe S) | 1 (vorläufig) | nein |
| 5 | RT Engineering GmbH (Freigelände / Stand 60; Nr. 255) | GELB | 2 | ja |
| 6 | Rubner Holzbau GmbH (Halle 23 / Stand 310; Nr. 256) | GELB (niedrige Priorität) | 7 | nein |
| 7 | RWA Raiffeisen Ware Austria AG, Abt. Landw. Fachbedarf (Halle 20 / Stand F30; Nr. 257) | ROT (E2 Händler/Großhandel, nur Stufe S) | 1 (vorläufig) | nein |
| 8 | RWA Raiffeisen Ware Austria AG, Abt. Ersatzteile/Werkstätten/Reifen (Halle 20 / Stand F30; Nr. 258) | ROT (E2 Händler/Großhandel, nur Stufe S) | 1 (vorläufig) | nein |
| 9 | SAATBAU LINZ eGen (Halle 21 / Stand 1330; Nr. 259) | ROT (Entscheidung Jey: Saatgut raus) | Jey-Vorgabe | nein |
| 10 | samo (Halle 22 / Stand C50; Nr. 260) | GELB (Grün-Kandidat nach Klärung) | 2 | ja |

Zahlen: Grün 0, Gelb 5, Rot 5 (davon 2 nach Entscheidung Jey, 3 als E2-Händler/Großhändler vorläufig auf Stufe S).
Hinweis zu Rot: Nach Regel E ist Rot nur bei belegtem (V) hartem Ausschluss zulässig. Hier wird Rot aus zwei Gründen vergeben: (a) Jey hat Verbände/Saatgut ausdrücklich ausgeschlossen (Nr. 1, 9); (b) bei Händlern/Großhändlern (Nr. 4, 7, 8) liegt E2 nur auf Stufe S vor (Händlerprofil, Verzeichnisse), Impressum/Firmenseite nicht gelesen: Rot daher vorläufig und im Browser zu bestätigen. Jey kann diese Zeilen ohne Aufwand abnicken.

Wichtigstes Ergebnis meiner Prüfung: Die Identitätsfrage bei Nr. 5 ist durch meine Suche weitgehend geklärt (RT Engineering GmbH, Hofkirchen an der Trattnach, FN 408221a, Geschäftsführer Thomas Reiter, Website reiter-respiro.com, Stellenportal "REITER (RT Engineering GmbH)", Reiter-Respiro-Katalog mit Pickup/Schwad-Technik; alle S). Das ist Kandidat B von Tom, nicht der Anlagentechnik-Kandidat aus Walding. Dadurch ist Nr. 5 ein deutlich konkreterer Kandidat (Landtechnik-Hersteller mit Eigenmarke), bleibt aber ohne V-Beleg Gelb. Bei Nr. 10 hat meine Suche den Firmenbuchsitz korrigiert: samo Maschinenbau GmbH, FN 178601z, Sternstraße 21, 4901 **Ottnang am Hausruck** (Toms Ortsangabe Thomasroith stammt vom Händlerprofil auf landwirt.com).

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Eigene Patent-Websuchen nur für Nr. 10 samo (2 Abfragen) und Nr. 5 RT Engineering (1 Abfrage, Anlagentechnik-Walding-Variante; Hofkirchen/Reiter nicht auf Patente durchsucht). Für alle übrigen Firmen habe ich keine eigene Patentsuche wiederholt. Die vier bei Tom fehlenden Patentsuchen (Nr. 251, 254, 257, 258 = Tina-Nr. 1, 4, 7, 8) sind weiterhin NICHT nachgeholt; die zweite Datenbank bei Nr. 255 (Tina-Nr. 5) ebenfalls nicht für den Hofkirchen-Kandidaten. Der Batch ist damit nach F5 UNVOLLSTÄNDIG, bis diese Suchen (Google Patents, Espacenet, DEPATISnet mit Anmelder und Stichwort Verguss/potting/Dichtung/Klebung) im Browser nachgeholt sind. Für die vier betroffenen Einheiten (Verband, Händler, Großhandel) ändert ein Patentfund die Ampel voraussichtlich nicht (Rot nach Jey-Entscheidung bzw. E2), für Nr. 5 ist die Lücke relevant. "Keine Treffer" ist kein Gegenbeweis; Rechtsstand nirgends geprüft.
Wettbewerbereinsatz (F6): Grep auf wettbewerber_referenzen.md mit RZO, Rinderzucht, RMIG, Roto-Tech, Rotschne, RT Engineering, Reiter, Respiro, Rubner, RWA, Raiffeisen, Saatbau, samo: kein Treffer. Keine Einzelsuchen mit Wettbewerbernamen von mir. Messe-Signal (E1-Namen auf der Ausstellerliste, Toms Grep): kein Wettbewerber unter den Ausstellern, ohne Einfluss auf die Ampel.
Nachrecherche-Schleife (Regel P): Gelb bei Nr. 2, 3, 5, 6, 10 mit Auftrag; Nr. 5 und Nr. 10 haben Priorität (einzige Maschinenbauer).

---

## 1. Rinderzuchtverband und Erzeugergemeinschaft OÖ (RZO) | Halle 24, Stand 10 (Nr. 251)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT (Entscheidung Jey: Verbände raus; kein Katalog-Ausschluss E1 bis E4 mit V belegt).** Zucht-/Besamungsverband, keine Fertigung, kein Bauteil (A). Messeliste: "Vereine, Verbände, ARGE, Organisationen; Genetik; Besamung; Rinderzucht" (S, Regel N5). CRM: "RZO", "Rinderzuchtverband und Erzeugergemeinschaft OÖ": kein Treffer, neu.
- Eigene Prüfung: nur CRM-Skript, Aussteller-CSV und Toms Angaben; keine eigene Websuche (Suchbudget, Verband ohne Fertigung).
- Korrekturen an Toms Feldern: keine. Feld 9 (Patentsuche) bleibt bei Tom ungeprüft, hier ebenfalls nicht nachgeholt (siehe Übersicht). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: keiner (Rot). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Segment Verband (S aus Messeliste und LK-OÖ-Snippet); keine Fertigung (A). Stichprobe für Jey: nein. Verifikation: 2026-11-26.

## 2. RMIG Lochbleche GmbH | Halle 23, Stand 490 (Nr. 252)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7, niedrige Priorität).** Zeile 1 greift nicht (kein E-Beleg V; Jey-Entscheidung "Anlagenbauer bleiben drin" betrifft sie nicht, Metall-Halbzeug ist kein Anlagenbau), Zeile 2 nicht (Name, Sitz, FN 89601t stimmen, S), Zeile 3 nicht (CRM-Abgleich auch mit RMIG, RM Hutter, Hutter Lochbleche, Reiter Lochbleche: kein Treffer; Konzern RMIG A/S nicht im CRM), Zeile 4 nicht (Konzerneinheit mit mehreren Werken: Sitzregel nicht anwendbar, Fertigung Leobersdorf nicht belegt), Zeile 5 formal, Verguss Niedrig (Lochbleche, Siebe, A); daher Zeile 7. Realistisch kein Ziel, nur formal offen.
- Eigene Prüfung: keine eigene Websuche (Suchbudget). Toms Angaben stützen sich auf Firmenbuch-/Katalogsnippets (S).
- Korrekturen an Toms Feldern: Feld 2: laut Aussteller-CSV führt RMIG auch "Saatgut-, -beet, -druckwalzen, -reinigung; Trocknungsanlagen" (Produktprofil Landtechnik-Zubehör); ändert die Einordnung Halbzeug/Siebe nicht. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Wird in Leobersdorf gefertigt oder nur vertrieben (rmig.com Standortseite/Impressum), und liefert RMIG Baugruppen mit Elektronik/Dichtung/Verklebung (Trocknungsanlagen-Zubehör)? Wo: rmig.com Standorte, Produktseiten, Stellenanzeigen Leobersdorf. Bei reinem Lochblech: Verguss Niedrig, nicht weiterverfolgen. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Leobersdorf (S), Konzernzugehörigkeit (S), Verguss Niedrig (A), Mitarbeiter (?). Stichprobe für Jey: nein. Verifikation: 2026-11-26.

## 3. ROTO-TECH GmbH | Halle 18, Stand 240 (Nr. 253)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Eigene Suche "Roto-Tech GmbH Österreich Obstpresse Kipper Kellerei Hersteller": kein Treffer zu einer Firma ROTO-TECH GmbH (nur Fremdfirmen wie Armbruster/ROTOVIB, Kerbl, Brandt; nicht vermischt). CRM: "ROTO-TECH GmbH", "Roto Tech": kein Treffer, neu. Sammelprofil (Obstverarbeitung, Kläranlagen, Regenwassernutzung, Kipper, Kellerei) deutet auf Händler/Allrounder; ohne V kein Rot nach E2.
- Korrekturen an Toms Feldern: Feld 7: Toms "Mittel, Stufe ?" ist ohne Beleg nicht belastbar; ich setze Fertigung "unbekannt". Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer ist ROTO-TECH GmbH, wo ansässig, Hersteller oder Händler? Wo: Firmenbuch/WKO-Firmen A-Z, Messeprofil agraria.at Halle 18 Stand 240, Impressum der Firmenseite. Bei Händler ohne Fertigung: Rot nach E2 mit URL. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/?). Stichprobe für Jey: ja (Firma nicht identifizierbar). Verifikation: 2026-11-26.

## 4. Rotschne Josef KG | Halle 20, Stand F70 (Nr. 254)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT, vorläufig (Tabellenzeile 1, E2: Händler ohne Fertigung; nur Stufe S).** Landtechnikhandel (Krone, Seko, Elho, Amazone), Autohaus, Zweirad; Freistadt, FN 19011 h (S, landwirt.com, KSV). Keine eigene Fertigung belegt, keine eigenen Bauteile (A). CRM: "Rotschne Josef KG", "Rotschne": kein Treffer, neu.
- Eigene Prüfung: keine eigene Websuche; Toms Angaben nicht widerlegt.
- Korrekturen: keine. Der E2-Beleg ist Stufe S; Bestätigung über Firmenseite/Impressum im Browser nötig, bevor Rot endgültig ist. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: keiner (Rot). Offen: Patentsuche der Vollständigkeit halber.
- Nicht verwendbare Aussagen: Händlerstatus (S), keine Fertigung (A). Stichprobe für Jey: nein. Verifikation: 2026-11-26.

## 5. RT Engineering GmbH | Freigelände, Stand 60 (Nr. 255)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht V-belegt; Grün-Kandidat nach Klärung).** Zeile 1 greift nicht, Zeile 2 trifft (Messeprofil nicht gelesen, Zuordnung nur über Namensgleichheit und Snippets). Zeile 3 nicht: der Skript-Treffer TQN ENGINEERING (0.90) ist manuell geprüft ein Ähnlichkeitseffekt (Kern-Namen rt vs tqn, DE statt AT); CRM "RT Engineering", "RT Engineering Anlagentechnik", "Reiter", "Reiter Respiro": kein weiterer Treffer. Jey kann die Nicht-Zuordnung zu TQN bestätigen.
- Eigene Prüfung (3 Suchen): (1) Firmenbuchsnippets: RT Engineering GmbH, FN 408221a, Sitz Eben 5a, 4716 Hofkirchen an der Trattnach; Statistik-Austria-Eintrag (Eben 5, Geschäftsführer Dipl.-Ing. Thomas Reiter, Website reiter-respiro.com); Stellenportal "REITER (RT Engineering GmbH)" (S). (2) Reiter-Innovative-Technology-Katalog "The heart of technology" (agriexpo, S): Respiro R3/R9 mit Pickup und "uniform swath" (Schwad-Technik), Katalogadresse Straßfeld 46, Schlüßlberg (älter, S). Das passt zur Messelistenangabe "Schwader, Schwadermäher". Die Walding-Gesellschaft (RT Engineering Anlagentechnik GmbH, FN 227400m, "Engineering und Vertrieb von Anlagen", Geschäftsführer Peter Koll) ist eine andere Einheit und nach heutigem Stand NICHT der Aussteller; nicht vermischen. (3) Patent-Websuche (Anmelder RT Engineering Anlagentechnik Walding): keine Treffer mit diesem Anmelder; für die Hofkirchen-Gesellschaft und "Reiter Innovative Technology" als Anmelder-Variante KEINE Patentsuche gemacht (offen).
- Verguss (Bauteil-Regel, alle A): Hubwerks-/Maschinensteuerung Mittel, Sensorik Mittel, Hydraulik-Magnetventile Mittel, Rahmen/Zinken/Pickup Niedrig; Maximum Mittel. Fertigung am Sitz Hofkirchen/Umgebung bei Landmaschinenhersteller mit Eigenmarke: Sitzregel (Zeile 4) wäre bei bestätigter Identität anwendbar, sofern kein Konzern/Auslagerungshinweis (Katalog nennt Reiter Innovative Technology, Schlüßlberg: Einheitenbezug unklar). Bei Bestätigung: Grün (Zeile 4), Verguss nur Mittel A.
- Korrekturen an Toms Feldern: Feld 4/17: Kandidat B (Hofkirchen, FN 408221a) ist durch Marke Reiter Respiro und Stellenportal klar der wahrscheinlichere; Kandidat A (Walding) ist auszuschließen, sobald das Messeprofil gelesen ist. Feld 12: kein CRM-Bezug. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Messeprofil agraria Freigelände Stand 60 und Website reiter-respiro.com (Impressum: Firma, Adresse, FN) lesen: ist der Aussteller die RT Engineering GmbH, Hofkirchen? (b) Gehören Reiter Innovative Technology (Schlüßlberg) und RT Engineering GmbH zusammen, wo wird montiert (Impressum, Stellenanzeigen Montage)? (c) Welche Elektronik ist verbaut (Hubwerkssteuerung, Sensoren, Ventile, eigen oder zugekauft)? (d) Patentsuche Google Patents, Espacenet, DEPATISnet mit Anmelder RT Engineering GmbH, Reiter Innovative Technology, Thomas Reiter nachholen. Aktion: nicht kontaktieren, hohe Priorität.
- Nicht verwendbare Aussagen: Identität Hofkirchen (S), Produkte (S), Fertigungsort (A/S), Verguss (A), Konzernbezug (?). Stichprobe für Jey: ja. Verifikation: 2026-11-26.

## 6. Rubner Holzbau GmbH | Halle 23, Stand 310 (Nr. 256)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7, niedrige Priorität).** Holz-/Stallbau (Brettschichtholz, Elemente), Ober-Grafendorf, FN 84010w, Konzern Rubner Gruppe (Kiens) mit mehreren Werken (S). CRM: "Rubner Holzbau GmbH", "Rubner", "Rubner Gruppe": kein Treffer, kein Konzernbezug (Regel M ohne Befund). Fertigung Ober-Grafendorf nur S, Konzern verlangt V; Verguss Niedrig (Strukturverklebung Brettschichtholz ist kein Demak-Fall, A). Zeile 6/7: Gelb. Realistisch kein Ziel.
- Eigene Prüfung: keine eigene Websuche (Suchbudget). Toms Angaben nicht widerlegt.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Gibt es in der Stallbau-Sparte Produkte mit Elektronik/Dichtung/Dosierung (z. B. Stallfenster, Lüftung) und wird in Ober-Grafendorf gefertigt? Wo: rubner.com Standort- und Produktseiten. Ohne solche Produkte nicht weiterverfolgen. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Produktionsstandorte (S), Konzernstruktur (S), Verguss (A). Stichprobe für Jey: nein. Verifikation: 2026-11-26.

## 7. RWA Raiffeisen Ware Austria AG, Abt. Landw. Fachbedarf | Halle 20, Stand F30 (Nr. 257)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT, vorläufig (Tabellenzeile 1, E2: Großhändler ohne Fertigung; nur Stufe S).** Agrar-Großhandel Korneuburg, FN 159839h (S). Keine Fertigung belegt, keine eigenen Bauteile (A). CRM: "RWA Raiffeisen Ware Austria AG", "Raiffeisen Ware Austria", "RWA", "Raiffeisen": kein Treffer; Konzernabgleich (Raiffeisen) ohne Treffer. Gleiche Gesellschaft wie Nr. 8 (zwei Abteilungen, eine Rechtseinheit, nicht doppelt zählen).
- Korrekturen: keine. E2-Beleg nur S; Firmenseite/Impressum im Browser bestätigen. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: keiner (Rot). Offen: Patentsuche der Vollständigkeit halber.
- Nicht verwendbare Aussagen: Händlerstatus (S), keine Fertigung (A). Stichprobe für Jey: nein. Verifikation: 2026-11-26.

## 8. RWA Raiffeisen Ware Austria AG, Abt. Ersatzteile/Werkstätten/Reifen | Halle 20, Stand F30 (Nr. 258)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT, vorläufig (Tabellenzeile 1, E2: Großhändler ohne Fertigung; nur Stufe S).** Wie Nr. 7 (gleiche Gesellschaft, Abteilung Ersatzteile/Werkstattausrüstung/Reifen, Messeliste S). CRM: kein Treffer, kein Konzernbezug.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: keiner (Rot). Offen: Patentsuche der Vollständigkeit halber.
- Nicht verwendbare Aussagen: Händlerstatus (S), keine Fertigung (A). Stichprobe für Jey: nein. Verifikation: 2026-11-26.

## 9. SAATBAU LINZ eGen | Halle 21, Stand 1330 (Nr. 259)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT (Entscheidung Jey: Saatgut raus; kein Katalog-Ausschluss E1 bis E4 mit V belegt).** Saatgutzüchtung/-produktion/-vertrieb, Leonding, FN 76126a (S). Kein Gerätebau, Verguss Niedrig (A; Beizung/Pillierung ist Beschichtung). CRM: "SAATBAU LINZ eGen", "Saatbau": kein Treffer, neu. Die Aussteller-CSV führt außerdem "NÖ. Saatbaugenossenschaft" (anderer Aussteller, nicht im Batch, kein Zusammenhang belegt).
- Korrekturen: Toms Feld 7 "Mittel, Stufe A" ist nach Sitzregel nicht tragfähig (kein Industrie-/Gerätebauer); ohne Einfluss auf Rot (Jey-Vorgabe). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: keiner (Rot). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Segment/Produkt (S), Mitarbeiterzahl (?). Stichprobe für Jey: nein. Verifikation: 2026-11-26.

## 10. samo | Halle 22, Stand C50 (Nr. 260)
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht V-belegt; Grün-Kandidat nach Klärung).** Zeile 1 greift nicht (E2 bei Händlerprofil auf landwirt.com nur Hinweis, kein Beleg; die Seite führt auch Hersteller als "dealer"), Zeile 2 trifft: Messename "samo" ohne Rechtsform; Zuordnung zu samo Maschinenbau GmbH nur über Namensgleichheit (S). CRM: "samo", "Samo Maschinenbau": kein Treffer, neu.
- Eigene Prüfung (4 Suchen): (1) Firmenbuch-Snippet evi.gv.at/f/178601z (S): samo Maschinenbau GmbH, FN 178601z, Sternstraße 21, 4901 **Ottnang am Hausruck**, Geschäftsgegenstand allgemeiner Maschinenbau, Geschäftsführer Paul Wiesmayr und Gerald Brunnthaller (bestellt 29.05.2026). Thomasroith als Ortsteil von Ottnang: nicht belegt, nur wahrscheinlich (gleiche PLZ 4901 und gleiche Straße im landwirt.com-Profil). (2) Produkt-/Fertigungssuche: nur landwirt.com-Händlerprofil und Gebrauchtinserate (Thor 520 Grubber, Variochop 7R70, 6-reihige Sämaschine); kein Beleg zu Eigenfertigung, kein Hersteller-Impressum. (3) Stellenanzeigen-Suche (Schweißer/Monteur, Ottnang): keine Anzeige von samo gefunden (kein Gegenbeleg). (4) Patent-Websuche: je eine Abfrage im Google-Patents-Stil (Samo Maschinenbau GmbH, Sämaschine, Anmelder) und im Espacenet/DPMA-Stil (Anmelder, Sternstraße 21): kein Patent mit Anmelder samo Maschinenbau; Fremdtreffer SAMA Maschinenbau (Weißenstadt, andere Firma, nicht zugeordnet). Datenbanken nicht direkt abfragbar; DEPATISnet/Espacenet-Direktabfrage und Rechtsstand offen.
- Verguss (Bauteil-Regel, alle A): Sämaschinen-Antriebs-/Dosiersteuerung Mittel, Sensorik Mittel, Kabelbaum/Stecker Mittel, Rahmen/Zinken/Scharen Niedrig; Maximum Mittel. Das Inserat nennt "mechanical kinematics" bei der Sämaschine, Elektronik nicht belegt; hydraulisch laut Inserat.
- Bei bestätigter Identität und eigenen Produkten wäre Zeile 4 (Sitzregel, Stufe A, Verguss Mittel A) anwendbar, aber nur schwach; der landwirt.com-Händlerstatus ("dealer") und fehlende Fertigungsbelege sprechen für genaues Hinsehen, ob samo selbst baut oder Marken vertreibt.
- Korrekturen an Toms Feldern: Feld 3/4/17: Firmenbuchsitz ist Ottnang am Hausruck (FN 178601z), nicht Thomasroith; Feld 17: Firmenbuch-Name "samo Maschinenbau GmbH" ist wörtlich der Messename, damit Identität wahrscheinlich, aber nur S. Feld 7: Toms "Hoch, Stufe A" bleibt ohne V-Beleg nicht verwendbar. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Messeprofil agraria Halle 22 Stand C50 und Firmenseite/Impressum lesen: Aussteller = samo Maschinenbau GmbH, Ottnang am Hausruck? (b) Baut samo Thor-Grubber und Sämaschinen selbst in Ottnang (Firmenseite, Produktseiten, Stellenanzeigen, Impressum) oder Vertrieb fremder Maschinen? (c) Welche Elektronik (Sämaschinen-Steuerung, ISOBUS, Sensoren) ist verbaut, eigen oder zugekauft? (d) Patentsuche Google Patents, Espacenet, DEPATISnet mit Anmelder samo Maschinenbau GmbH im Browser. Aktion: nicht kontaktieren, hohe Priorität.
- Nicht verwendbare Aussagen: Identität (S), Fertigung am Sitz (A), Produkte (S), Verguss (A), Händlerstatus (S). Stichprobe für Jey: ja. Verifikation: 2026-11-26.

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind durchgehend korrekt niedrig angesetzt; keine V-Aussage vorgetäuscht. Einstufung "prüfenswert" für Nr. 255/260 bleibt vorläufig; keine Firma ist für Grün belegbar (Regel I: ohne Browser-Gegenlesen nicht bestätigbar).
- Widerspruch zu Tom: Sitz samo = Ottnang am Hausruck (Firmenbuch), nicht Thomasroith. Identitätsklärung bei RT Engineering: Hofkirchen (Reiter Respiro) wahrscheinlicher als Walding.
- Rot-Vergabe (Nr. 1, 4, 7, 8, 9) beruht auf Jey-Entscheidungen bzw. E2 auf Stufe S; streng nach Regel E wäre bei Nr. 4, 7, 8 Rot erst nach V-Beleg zulässig.
- Nr. 257 und 258 sind dieselbe Rechtseinheit; für die Kundenstatistik als eine Firma zählen.
- Vorschlag Fehlerlog (Jey gibt frei, nicht eingetragen): Bei Landtechnik-Ausstellern ohne Rechtsform (samo) und bei gleichnamigen Gesellschaften (RT Engineering) zuerst Firmenbuch-Treffer mit Marken-/Geschäftsführernamen abgleichen; Händlerprofile auf landwirt.com nennen auch Hersteller "dealer".

## Einschränkungen
- Browser und WebFetch nicht verfügbar: kein Gegenlesen nach Abschnitt H, keine Impressen, Firmenbuchauszüge, Datenblätter oder Karriereseiten gelesen; alle Aussagen Stufe S, A oder ?. Keine "Zitat im Browser bestätigt: ja", kein Grün, nichts mailtauglich.
- WebSearch: 10 eigene Abfragen: samo 5 (Produktion/Fertigung, Patent/Anmelder, Eigenentwicklung/Firmenbuch, Stellenanzeigen, Patentabfrage im Google-Patents-Stil); RT Engineering 4 (Schwader/Hersteller, Patent/Walding, Hofkirchen/Firmenbuch, Reiter Respiro); ROTO-TECH 1. Keine eigene Websuche für Nr. 1, 2, 4, 6, 7, 8, 9 (Verband/Händler/Großhandel/Saatgut, Jey-Entscheidungen; RMIG und Rubner nur Toms Angaben, nicht widerlegt).
- Patente: Pflichtsuche F5 (Google Patents, Espacenet, DEPATISnet) nicht erfüllt; Batch UNVOLLSTÄNDIG. Fehlend: Toms vier Lücken (Nr. 251, 254, 257, 258), zweite Datenbank bei RT Engineering GmbH Hofkirchen, direkte Datenbankabfrage für alle Firmen, Anmeldervarianten (Reiter Innovative Technology, RMIG A/S, Rubner Gruppe, Samo-Schreibvarianten). Rechtsstand nirgends geprüft.
- Wettbewerbereinsatz (F6): nur Listenabgleich und Toms Angaben; "kein Hinweis" ist kein Gegenbeweis.
- Kundendatenbank (Excel) nicht lesbar; CRM-Abgleich per Skript auf die Textexporte; keine "Verifiziert am"-Prüfung nötig (kein Treffer).
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
