# Tina Batch 19 - agraria 2026, Wels (Prüfung von tom_batch_19.md)
Erstellt: 2026-11-25 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_19.md (10 Messezeilen, Messe-Nr. 181 bis 190; Nr. 187/188 "Lagerhaus" sind Doppelzeilen und werden gebündelt, daher 9 Prüfeinheiten).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser geprüft, vorläufig.** Es standen nur WebSearch (5 Abfragen, Kurzfassungen/Snippets) und Bash zur Verfügung; WebFetch scheiterte (kwb.net und kubota.com nicht auflösbar, Hosts nicht freigegeben), Chrome nicht vorhanden. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein. Kein Grün ist mailtauglich.
Skript: `python3 crm_abgleich.py` für alle Firmen samt Konzern-/Alt-/Schwesternamen selbst wiederholt (Kubota, Kubota Baumaschinen/Corporation/Europe, Esch-Technik; Kuhn, Kuhn Group, Bucher, Bucher Industries; KWB, Kraft und Wärme aus Biomasse, PDP Holding, Porsche; KWS Saat; Kärcher, Alfred Kärcher; L&L-Varianten; Lagerhaus, RWA, Raiffeisen Lagerhaus; Verbandsnamen). Ergebnis deckt sich mit Tom. Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum aller Einträge: 2026-11-25.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | KUBOTA (H21 B30) | GELB | 2 | ja |
| 2 | KUHN CENTER AUSTRIA GmbH (H20 A30) | GELB (Rot-Kandidat E2) | 3 | ja |
| 3 | KWB Energiesysteme GmbH (H17 240) | GRÜN (schwach, vorläufig) | 4 (Sitzregel) | ja |
| 4 | KWS Austria Saat GmbH (H23 315) | GELB (Rot-Kandidat, Jey-Entscheidung nötig) | 7 | nein |
| 5 | Kärcher Store Plotka OG (H20 1230) | GELB (Rot-Kandidat E2) | 3 | nein |
| 6 | L&L-Lenksysteme GmbH (H17 50) | GELB (Rot-Kandidat E2) | 7 | nein |
| 7+8 | Lagerhaus (Nr. 187/188 gebündelt, H20 F30) | GELB (Rot-Kandidat E2) | 2 | nein |
| 9 | Landesverband der Schafzucht und Schafhaltung OÖ (H24 135) | ROT (Jey-Entscheidung Verband) | 1 (E2 analog, Jey) | nein |
| 10 | Landesverband für Leistungsprüfung und Qualitätssicherung in OÖ, LfL OÖ (H24 10) | ROT (Jey-Entscheidung Prüfdienstleister/Verband) | 1 (E2 analog, Jey) | nein |

Zahlen: Grün 1 (schwach), Gelb 6 Einheiten (7 Messezeilen), Rot 2. Der Batch ist dünn wegen der Ausstellerstruktur (Händler/Verbände/Saatgut), nicht wegen mangelnder Recherche. Einziger echter Kandidat: KWB.

Hinweis zu Rot: Die Tabellenzeile 1 verlangt Stufe V. Für Nr. 9 und 10 stützt sich Rot auf Jeys ausdrückliche Entscheidung (Verbände/Prüfdienstleister raus) und die Messelistenkategorie "Vereine, Verbände" (S). Für die Händler (Nr. 2, 5, 6, 7+8) fehlt der V-Beleg für "Händler ohne Fertigung" (nur Snippets), daher Gelb mit Rot-Kandidat; ein Blick ins Impressum/Firmenbuch im Browser genügt zum Rot nach E2.

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Eigene Patent-Websuche nur für KWB (1 Abfrage) und Kubota (1 Abfrage); für die übrigen Firmen keine eigene Wiederholung, Toms Suchen werden weder übernommen noch widerlegt. Feld 9 ist damit bei ALLEN Firmen ohne Datenbankabfrage: nach F5 UNVOLLSTÄNDIG, Nachholen im Browser nötig (Toms Batch ist laut seiner Einschränkung ebenfalls so unvollständig). "Keine Treffer" ist kein Gegenbeweis. Wettbewerbereinsatz (F6): Grep auf wettbewerber_referenzen.md mit Kubota, Kuhn, Bucher, KWB, Kärcher, Lagerhaus: kein Treffer; keine eigenen Einzelsuchen mit Wettbewerbernamen. Messe-Signal (E1-Wettbewerber unter den Ausstellern): von Tom übernommen (kein Treffer), nicht neu geprüft.

---

## 1. KUBOTA | Halle 21 Stand B30 (Messe-Nr. 181)
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Die Messezeile nennt keine Rechtsform; in Frage kommen Kubota Baumaschinen GmbH (Zweibrücken, DE), Esch-Technik GesmbH (St. Veit/Glan, AT, Generalvertretung laut Tom, S) oder Kubota Europe. Meine Suche zur Zuordnung (agraria/Kubota/Esch) brachte keinen Treffer, die Messeliste ist von mir nicht bestätigt (Tom-Angabe, S). CRM: crm_abgleich.py für "KUBOTA", "Kubota Baumaschinen", "Kubota Corporation", "Kubota Europe", "Esch-Technik": kein Treffer, neu.
- Eigene Prüfung Fertigung: Eine Websuche liefert Pressehinweise, dass Kubota Baumaschinen GmbH in Zweibrücken Minibagger und Radlader für Europa produziert (Gründung 1988, Produktion seit 1989; Snippets von kbm.kubota-eu.com, internationalrentalnews.com, rheinpfalz.de; S). Laut Kubota-Mitteilung vom Dezember 2024 (Snippet, S) übernimmt KBM Teile des früheren Tadano-Demag-Geländes in Zweibrücken, Produktion von Minibaggern und Radladern soll ab Mitte 2026 schrittweise anlaufen. Das stützt Toms Fertigungsangabe für die Einheit Kubota Baumaschinen, nicht für die in Wels ausstellende Einheit. Aktuelle Stellenanzeigen für Montage: nicht gefunden (Suche zeigte nur die Personal-Kontaktseite).
- Eigene Prüfung Patente (Kubota Corporation, potting/encapsulation/sealing, Websuche mit Google-Patents-Ausrichtung): keine Kubota-Treffer, nur fremde Anmelder; kein Gegenbeweis, Google Patents/Espacenet mit Anmelder "Kubota" nachholen.
- Bewertung Zeilen: Zeile 1 nicht (kein E-Beleg V), Zeile 2 trifft (Identität der Messeeinheit offen). Gelände Zweibrücken: Fertigung Mittel (S), Verguss Hoch (A, Steuergeräte, Sensoren, Magnetspulen), nur für die Einheit Zweibrücken, nicht für Importeur.
- Korrekturen an Toms Feldern: Feld 7 bleibt Mittel (S); Feld 3 "Österreich" ist nach Messeland, nicht nach belegter Einheit; Feld 10 "prüfenswert" akzeptiert. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Welche Gesellschaft stellt in Halle 21 B30 aus? Messeprofil agraria.at/aussteller, Impressum der Kubota-Seite im Browser lesen. (b) Ist es Esch-Technik (Importeur, Rot nach E2 bei V) oder Kubota Baumaschinen GmbH (Zweibrücken, dann Fertigung mit V belegen, Elektronik/Steuergeräte Eigenmontage?). (c) Patentsuche Espacenet/Google Patents mit pa=Kubota und potting/encapsulation. Aktion: nicht kontaktieren, bis Einheit geklärt.
- Nicht verwendbare Aussagen: Fertigung Zweibrücken (S), Zuordnung der Messeeinheit (?), Verguss (A), Esch-Technik-Rolle (S). Stichprobe für Jey: ja (Identität).

## 2. KUHN CENTER AUSTRIA GmbH | Halle 20 Stand A30 (Messe-Nr. 182)
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 3, CRM-Konzernbezug; Rot-Kandidat E2 Händler).** crm_abgleich.py: "KUHN CENTER AUSTRIA", "Kuhn", "Kuhn Group": kein Treffer; "Bucher Industries"/"Bucher": Bucher Hydraulics GmbH (Z. 362) und Bucher Municipal GmbH (Z. 363), beide [DE], dazu "Jetter / Bucher Automation AG" (Z. 1217/1218, anderer Konzern, kein Bezug). Kuhn Group ist laut Tom Division der Bucher Industries (S, nicht von mir geprüft). Damit Zeile 3 (Konzern/Schwester im CRM, Einheit unklar). Die CRM-Einheiten (Hydraulik, Kommunalfahrzeuge) sind nicht dieselbe wie ein österreichischer Kuhn-Händler, keine Zeile 1. "Kuhn Reaktionsharz Technik GmbH" ist eine andere Firma, kein Bezug (Jey: gleicher Name rein = raus gilt nur bei gleicher/sehr ähnlicher Einheit, trifft hier nicht).
- Eigene Prüfung: keine eigene Websuche (Händler, nach Vorgabe reicht CRM + Einordnung). Tom: Handelsgesellschaft/Kompetenzzentrum, Fertigung der Maschinen im Konzern außerhalb (S). Fertigung Niedrig, Verguss Niedrig auf Gesellschaftsebene.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 3): (a) Jey bestätigt: Zählt Bucher Hydraulics/Bucher Municipal als Konzernbezug zur Kuhn Group (Bucher Industries)? (b) Impressum/Firmenbuch FN 357450m im Browser lesen: reiner Handel/Service ohne Fertigung (dann Rot nach E2 mit URL). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Händlerstatus (S), Konzernzugehörigkeit (S), Verguss (A). Stichprobe für Jey: ja (Konzernbezug).

## 3. KWB Energiesysteme GmbH | Halle 17 Stand 240 (Messe-Nr. 183)
**ohne Browser geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Fertigung Stufe S/A nach Sitzregel, Verguss Hoch A).** Eigener Industrie-/Gerätebauer (Biomasse-Heizkessel, Regelung Comfort 4) mit erkennbarem Hauptstandort St. Margarethen an der Raab (Steiermark); Töchter laut Tom nur Vertrieb. Sitzregel erfüllt, solange kein Konzern mit mehreren Werken und keine Auslagerung: das ist nicht V-belegt. Kein harter Ausschluss, CRM-Abgleich negativ (siehe unten).
- Eigene Prüfung: crm_abgleich.py "KWB Energiesysteme", "KWB", "Kraft und Wärme aus Biomasse", "PDP Holding": kein Treffer, neu. Der Eigentümer Peter Daniell Porsche (PDP Holding, laut Tom S) ist eine Familienholding; "Porsche"/"Porsche AG"/"Dr. Ing. h.c. F. Porsche AG" im CRM (Z. 553-555, 1862-1864) ist ein anderer Konzern, kein Konzernbezug im Sinn Regel M; Jey zur Kenntnis. Websuche Standort/Produktion: Snippets bestätigen Namenswechsel 2022 von "KWB - Kraft und Wärme aus Biomasse GmbH" zu KWB Energiesysteme GmbH; KWB-Seite nennt Kernkompetenz Entwicklung von Pellet-, Hackgut- und Scheitholzheizungen und "viele KWB-Erfindungen und Patente" (siebenkammerige Zellenradschleuse, cleanEfficiency 2.0, Kriechbrenner; Snippet von kwb.net, S). Jobsuche: nur Service-, Software-, Einkaufs- und Dispositionsstellen am Standort gefunden, keine Produktions-/Elektronikmontagestelle (Stellenseite im Browser prüfen; kein Gegenbeweis). Produktion am Standort aus meiner Suche nicht erneut belegt, nur Toms Snippets (S).
- Eigene Prüfung Patente: Websuche mit Google-Patents-Ausrichtung und Anmeldervarianten (KWB Energiesysteme, KWB Kraft und Wärme aus Biomasse): keine Patentdatensätze, nur kwb.net-Seiten; aber KWB selbst nennt Patente, sie betreffen Mechanik/Verbrennung (Zellenradschleuse, Brenner), nicht Verguss. Kein Verguss-Patent belegt; Direktsuche Espacenet pa="KWB" mit Altname nachholen.
- Bauteile (Bauteil-Regel): Regelelektronik Comfort 4 Hoch (A), Sensorik Heißbereich Hoch (A), Zündelement/Heizpatrone Hoch (A), Antriebsmotoren Hoch (A), Türdichtungen Mittel (A), Kessel/Schnecken Niedrig (A). Maximum Hoch (A).
- Korrekturen an Toms Feldern: Mitarbeiterzahl widersprüchlich (400 Gruppe vs. 226 Standort, S) als offen belassen; Feld 7 "Hoch S" ist nach Sitzregel tragend, nicht V. Toms "interessant" nach Regel I nur mit Browser-Gegenlesen bestätigbar. Zitat im Browser bestätigt: nein.
- Nachrecherche (für Mailstufe, kein Gelb): (a) kwb.net Impressum/Standort im Browser: Produktion der Kessel in St. Margarethen mit V und Zitat belegen. (b) kwb.at Karriere: Elektronik-/Schaltschrankmontage oder Zukauf der Regelung Comfort 4? (c) Datenblatt Pelletheizung: IP-Klasse, Elektronik. (d) Patente Espacenet/Google Patents direkt. (e) Wettbewerbereinsatz in Stellenanzeigen/Anwenderseiten. Aktion: nicht kontaktieren (Regel K), Jey-Stichprobe.
- Nicht verwendbare Aussagen: Fertigung St. Margarethen (S, nur durch Sitzregel A getragen), Mitarbeiterzahl (S), Verguss (A), Eigentümer (S). Stichprobe für Jey: ja.

## 4. KWS Austria Saat GmbH | Halle 23 Stand 315 (Messe-Nr. 184)
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7, Rot-Kandidat: branchenfremd).** Saatgut-Zucht/-Vertrieb (Messekategorie "Samen, Saatgut", S). Es gibt keinen Fertigungsbetrieb für Geräte/Elektronik; ein Ausschluss E1 bis E4 ist nicht ausdrücklich einschlägig (kein Händler im Sinn E2, kein Verband), daher nicht Rot, sondern Jey-Entscheidung. crm_abgleich.py "KWS Austria Saat", "KWS Saat", "KWS": kein Treffer, neu. "KWS Schwimmbadanlagen GmbH" (Z. 1363) ist laut Tom eine andere Firma; Jey: gleicher/sehr ähnlicher Name raus gilt hier nicht, da kein ähnlicher Firmenname (nur Kürzel). Keine eigene Websuche (Branche offensichtlich).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Jey entscheidet, ob Saatgut/Pflanzenzüchtung generell als Ausschluss gilt (Vorschlag: neue Ausschlussklasse "Agrarprodukte ohne Geräte"); sonst keine weitere Recherche. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 5. Kärcher Store Plotka OG | Halle 20 Stand 1230 (Messe-Nr. 185)
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 3, CRM-Konzernbezug; Rot-Kandidat E2 Händler).** crm_abgleich.py: "Kärcher Store Plotka": kein Treffer; "Kärcher"/"Alfred Kärcher": Alfred Kaercher Vertriebs-GmbH (Z. 75) und Alfred Kärcher Vertriebs-GmbH (Z. 76), beide [DE]. Das ist die deutsche Vertriebsgesellschaft des Herstellers, die Messeeinheit (OG, Wels, Franchise-Fachhandel laut Tom, S) ist eine andere Rechtseinheit; die Namensähnlichkeit ist Konzern-/Markenbezug, daher Zeile 3, nicht Zeile 1. Tom nennt zudem DE 102024132901 A1 (Alfred Kärcher SE & Co. KG, Energiespeicher in Vergussmaterial, Offenlegung, S): Hinweis auf Eigenverguss beim Hersteller, nicht bei der Händlerin; von mir nicht nachgeprüft.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 3): Impressum/Firmenbuch des Stores im Browser lesen: selbständige Händlerin (OG, Wels), keine Fertigung? Dann Rot nach E2 mit URL; Jey bestätigt, dass der CRM-Bezug nur den Hersteller-Vertrieb betrifft und keine Neukunden-Chance auf Konzernebene (Alfred Kärcher SE & Co. KG, Winnenden) ergibt. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Händlerstatus (S), Konzernpatent (S). Stichprobe für Jey: nein.

## 6. L&L-Lenksysteme GmbH | Halle 17 Stand 50 (Messe-Nr. 186)
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7, Rot-Kandidat E2 Händler/Installateur).** Einbau und Vertrieb von FJDynamics-Lenksystemen (Tom, S). crm_abgleich.py "L&L-Lenksysteme", "L&L Lenksysteme", "LL Lenksysteme": kein Treffer, neu. Identität nur teilweise belegt (Rechtsform/Adresse nicht gelesen). Keine eigene Websuche.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Impressum ll-lenksysteme.at im Browser: Rechtsform, Adresse, Firmenbuch; Eigenbau/Konfektion (Kabelbäume, Bedienteile) oder reiner Handel/Einbau? Bei reinem Handel Rot nach E2 mit URL. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 7+8. Lagerhaus (Messe-Nr. 187 und 188, Doppelzeile) | Halle 20 Stand F30
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt; Rot-Kandidat E2).** "Lagerhaus" ist eine Verbundmarke vieler selbständiger Genossenschaften (Zentrale RWA, Korneuburg, laut Tom, S); die ausstellende Einheit ist nicht benannt. crm_abgleich.py "Lagerhaus", "RWA Raiffeisen Ware Austria", "Raiffeisen Lagerhaus": kein Treffer, neu. Beide Messezeilen (Nr. 187 ohne Produktangabe, Nr. 188 Landtechnikhandel) werden als eine Einheit bewertet. Keine eigene Websuche.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Messeprofil agraria.at/aussteller (Halle 20 F30): welche Genossenschaft stellt aus? Dann Firmenbuch; reiner Handel mit Werkstatt belegt, dann Rot nach E2 mit URL. Eigenmarken HEVI/IMPOS (Tom, S): Herstellung nur prüfen, wenn Jey es wünscht. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 9. Landesverband der Schafzucht und Schafhaltung OÖ | Halle 24 Stand 135 (Messe-Nr. 189)
**ohne Browser geprüft, vorläufig. Ampel: ROT (Jey-Entscheidung: Verbände raus; E2-analog; Tabellenzeile 1).** Bedingung: Verband/Organisation der Schafzucht, kein Fertiger. Quelle: Messeliste agraria.at/aussteller, Kategorie "Vereine, Verbände, ARGE, Organisationen" (S, von Tom übernommen, nicht von mir gelesen). Identität (Rechtsform/ZVR) nicht belegt, aber für den Ausschluss unerheblich. crm_abgleich.py: kein Treffer.
- Korrekturen: keine. Nachrecherche: keiner. Zitat im Browser bestätigt: nein.
- Nicht verwendbare Aussagen: Verbandsstatus (S). Stichprobe für Jey: nein.

## 10. Landesverband für Leistungsprüfung und Qualitätssicherung in Oberösterreich (LfL OÖ) | Halle 24 Stand 10 (Messe-Nr. 190)
**ohne Browser geprüft, vorläufig. Ampel: ROT (Jey-Entscheidung: Verbände/Prüfdienstleister raus; Tabellenzeile 1).** Bedingung: Prüf- und Qualitätssicherungsdienstleister für Milch/Fleisch (Snippet readkong, laut Tom: "Dienstleistungsunternehmen in der Qualitätssicherung von Milch und Fleisch", S). crm_abgleich.py "…Qualitätssicherung in Oberösterreich", "LfL OÖ": kein Treffer. LfL Bayern ist eine andere Einrichtung und wurde nicht vermischt.
- Korrekturen: keine. Nachrecherche: keiner. Zitat im Browser bestätigt: nein.
- Nicht verwendbare Aussagen: Dienstleisterstatus (S). Stichprobe für Jey: nein.

---

## Empfehlungen für Jey
1. KWB ist der einzige Kandidat: im Browser V-Beleg für Fertigung St. Margarethen und Elektronikmontage holen, Patente direkt prüfen, dann Grün bestätigen.
2. Kubota: ausstellende Einheit klären; falls Esch-Technik, Rot (Importeur); falls Kubota Baumaschinen Zweibrücken, eigener Fertigungsprüfauftrag (ggf. Gelb-Schleife).
3. Händler (Kuhn Center Austria, Kärcher Store Plotka, L&L, Lagerhaus): Rot-Bestätigung per Impressum/Firmenbuch in einem Browserlauf.
4. Regelvorschlag: neue Ausschlussklasse "Agrarprodukt/Saatgut ohne Gerätefertigung" (Nr. 4).

## Nicht aufgenommen / CRM-Konzernbezüge (zur Kenntnis)
- KUHN CENTER AUSTRIA: Bucher Hydraulics GmbH (Z. 362), Bucher Municipal GmbH (Z. 363) im CRM, Konzernbezug zu Bucher Industries (laut Tom).
- Kärcher Store Plotka OG: Alfred Kärcher Vertriebs-GmbH (Z. 75/76) im CRM.
- Zufallsnamen ohne Bezug: Kuhn Reaktionsharz Technik GmbH (Z. 1354), KWS Schwimmbadanlagen GmbH (Z. 1363). Keine Firma ist als gleiche Einheit im CRM (kein Rot nach E5).

## Einschränkungen
- Kein Browser; WebFetch für kwb.net und kubota.com nicht möglich (Hosts nicht erreichbar; müssten in den Netzwerkeinstellungen der Sitzung freigegeben werden). Nur 5 WebSearch-Abfragen: KWB Produktion/Stellen, KWB Patente, Kubota Zweibrücken, Kubota/Esch agraria, Kubota Patente. Keine Stufe V.
- Patentdatenbanken (Google Patents, Espacenet, DEPATISnet) nicht direkt abgefragt: Feld 9 bei allen Firmen UNVOLLSTÄNDIG nach F5; für Händler/Verbände/Saatgut/Software nach Vorgabe nur CRM + Einordnung.
- Messeliste agraria.at (Halle/Stand, Kategorien) von mir nicht selbst gelesen; Angaben von Tom übernommen. Das Suchergebnis zu Halle 21/Esch-Technik lieferte keine Bestätigung.
- Wettbewerbereinsatz (F6) nur per Grep auf wettbewerber_referenzen.md, keine Einzelsuchen.
- Keine Kontaktsuche (Regel K). Es wurde nichts verschickt und kein Datenbankfeld geändert.
