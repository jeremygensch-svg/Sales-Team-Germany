# Tina Batch 10 - agraria 2026 (Prüfung von tom_batch_10.md)
Erstellt: 2026-11-25 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_10.md (10 Firmen, Nr. 1 bis 10 des Batches, in Toms Datei Messe-Nr. 91 bis 100; Messe Agrarmesse Wels 2026, Länder DE/AT/NL).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Seitenabruf geprüft, vorläufig.** Es standen nur WebSearch (5 Abfragen, Kurzfassungen/Snippets) und Bash zur Verfügung; Chrome nicht vorhanden, WebFetch nicht eingesetzt (Tom meldete die Hosts als nicht erreichbar). Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün ist mailtauglich.
Skripte: `python3 crm_abgleich.py` für alle 10 Firmen samt Konzern-, Alt-, Schwester- und Markennamen selbst wiederholt (Details je Firma). Ergebnis: kein Firmen-/Konzerntreffer im CRM; einziger Beinahe-Treffer "Bräuer" ~ "BREUER GmbH & Co. KG [DE]" (bekannte_firmen_DE-AT-NL.txt Zeile 333, Ähnlichkeit 0,92), anderer Name, anderes Land, kein Treffer. Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum aller Einträge: 2026-11-25.
Entscheidungen von Jey angewandt: Verbände/Beratung/Prüfdienstleister/Forschung raus (Nr. 2, 5); CRM-Treffer mit gleichem/sehr ähnlichem Namen raus (keiner); Anlagenbauer bleiben drin, außer sie bauen selbst Verguss-/Dosieranlagen (E1): keine der zehn Firmen baut Dosier-/Vergussanlagen.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | BERTI Mulchgeräte (H19, Stand 70) | GELB | 2 (Rot-Kandidat E3) | ja |
| 2 | Bio Austria OÖ (H20, Stand 1100) | ROT | 1 (E2, Jey-Vorgabe Verbände) | nein |
| 3 | Blickwinkel digital service (H17, Stand 90) | GELB | 7 (Rot-Kandidat E2) | nein |
| 4 | Bobcat Vario Welt (H20, Stand B10) | GELB | 7 (Rot-Kandidat E2/E3) | nein |
| 5 | Boden.Wasser.Schutz.Beratung (H21, Stand 1300) | ROT | 1 (E2 Beratung, Jey-Vorgabe) | nein |
| 6 | Boehlerit (H20, Stand 1150) | GELB | 5 | nein |
| 7 | Bohnenkamp Austria GesmbH (H18, Stand 30) | GELB | 7 (Rot-Kandidat E2) | nein |
| 8 | Brantner Fahrzeugbau (H22, Stand A10) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 9 | Bräuer Stalltechnik GmbH (H23, Stand 370) | GELB | 7 | ja |
| 10 | CA Catering Foodtruck Frau Knolle (Freigelände, Stand 180) | GELB | 2 (Streichkandidat, kein Fertiger) | nein |

Zahlen: Grün 1 (schwach, vorläufig), Gelb 7, Rot 2.

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Eigene Patent-Websuche nur für Brantner (1 Abfrage, kein Anmelder-Treffer); für die übrigen Firmen keine eigene Wiederholung, Toms Suchen werden weder übernommen noch widerlegt. Feld 9 ist damit bei allen 10 Firmen ohne Datenbankabfrage: nach F5 UNVOLLSTÄNDIG, Nachholen im Browser nötig, besonders für Brantner (Grün). "Keine Treffer" ist kein Gegenbeweis. Wettbewerbereinsatz (F6): Grep auf wettbewerber_referenzen.md mit berti, bobcat, brantner, boehlerit, bohnenkamp, bräuer/braeuer, blickwinkel, svea, joz: kein Treffer; keine Einzelsuchen mit Wettbewerbernamen von mir.

---

## 1. BERTI Mulchgeräte | Halle 19, Stand 70
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt; Rot-Kandidat E3).** Zeile 1 greift nicht, da E3 (Fertigung nur außerhalb DE/AT/NL) nicht mit V belegt ist. Hersteller BERTI Macchine Agricole, Caldiero (Italien), "Made in Italy" nur S; ob der Aussteller eine österreichische Vertriebsfirma ist, bleibt offen. Meine Suche: nur Händlerinserate in Österreich (landwirt.com: Deschberger Landtechnik, Land und Technik u. a.), kein offizieller Importeur gefunden. Verguss Niedrig (A).
- CRM: crm_abgleich.py "BERTI Mulchgeräte", "Berti", "BERTI Macchine Agricole": kein Treffer, neu.
- Korrekturen an Toms Feldern: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer ist die ausstellende Rechtsperson (Hersteller BERTI Macchine Agricole S.p.A. oder österreichischer Importeur/Händler) und wo wird gefertigt? Ausstellerverzeichnis der agraria (Detailseite Halle 19, Stand 70) und Impressum lesen. Bei Italien-Werk/Händler: Rot nach E3/E2 mit Beleg V. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Italien (S), Sitz, Verguss Niedrig (A), Patentfeld. Stichprobe für Jey: ja (Identität).

## 2. Bio Austria OÖ | Halle 20, Stand 1100
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT (Tabellenzeile 1, E2 plus Jey-Entscheidung "Verbände raus").** Rot, weil: Interessenverband/Verein ohne Produktion (E2; Quelle Toms Snippet "BIO AUSTRIA OÖ, Auf der Gugl 3, 4021 Linz", https://www.bio-austria.at/app/uploads/2026/07/bioinfo-ooe-03-2026.pdf, nur S) und Vorgabe Jey. Eigener Beleg V fehlt; die Rot-Entscheidung stützt sich auf die Jey-Vorgabe.
- CRM: "Bio Austria", "Bio Austria OÖ": kein Treffer, neu (irrelevant, da raus).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: keiner (Rot). Aktion: nicht aufnehmen.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 3. Blickwinkel digital service | Halle 17, Stand 90
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2).** Händler/Nachrüster für Lenksysteme (SVEA) in Kirchdorf am Inn laut Händlerprofil (S). Rot nach E2 verlangt Beleg (V), fehlt; eigene Suche nicht ausgeführt. Elektronik (Lenksystem) wird beim Hersteller SVEA vergossen, nicht bei der Firma (A). Verguss für die Firma Niedrig.
- CRM: "Blickwinkel digital service", "Blickwinkel": kein Treffer, neu.
- Korrekturen: Schreibung im Eintrag "servcie" ist Messelisten-Tippfehler (Tom vermerkt). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Montiert oder fertigt die Firma Lenksystem-Baugruppen selbst (Kabelbäume, Konfektion) oder ist sie reiner Händler? lenksystem.pro, Impressum und Händlerprofil auf landwirt.com im Browser lesen. Reiner Händler: Rot nach E2. Aktion: niedrige Priorität, nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 4. Bobcat Vario Welt | Halle 20, Stand B10
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2/E3).** VarioWelt ist laut topagrar-Snippet eine Einkaufsgenossenschaft in Oberösterreich (Vertrieb), Hersteller Bobcat fertigt in Tschechien u. a. (S). Beleg V für E2/E3 fehlt, daher nicht Rot. Konzernabgleich: "Bobcat", "Doosan Bobcat", "VarioWelt": kein CRM-Treffer.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Betreibt VarioWelt eigene Fertigung/Aufbauten in AT oder ist sie reine Handelsgenossenschaft? Firmenbuch/Impressum VarioWelt und Händlerprofil lesen. Bei reinem Handel: Rot (E2). Aktion: niedrige Priorität.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 5. Boden.Wasser.Schutz.Beratung | Halle 21, Stand 1300
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT (Tabellenzeile 1, E2 Beratung plus Jey-Entscheidung).** Rot, weil: Beratungsdienst im Umfeld der Landwirtschaftskammer OÖ/Land OÖ ohne Produktion (E2; Quelle https://www.land-oberoesterreich.gv.at/216273.htm, nur S) und Vorgabe Jey (Beratung/Verbände/Forschung raus).
- CRM: "Boden.Wasser.Schutz.Beratung", "Landwirtschaftskammer Oberösterreich": kein Treffer.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: keiner. Aktion: nicht aufnehmen.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 6. Boehlerit | Halle 20, Stand 1150
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Hartmetall-Werkzeuge, Weltsitz und Produktion Kapfenberg (S, WKO-Interview; meine Suche bestätigt Kapfenberg, ca. 800 Mitarbeiter weltweit, ca. 500 Kapfenberg, S). Gruppe mit weiteren Standorten (DE, Türkei laut Tom): Sitzregel greift nicht, V nötig, fehlt. Verguss Niedrig (A): Wendeschneidplatten werden gesintert/gelötet/beschichtet; meine Suche fand keinen Hinweis auf Sensorik, Klebung oder Verguss. Zeile 6 und 5 treffen zusammen; höhere Zeilennummer wird nicht gewählt, Zeile 5 zuerst. Verwechslungsgefahr mit voestalpine Böhler Edelstahl (anderer Konzern, nicht vermischt); CRM "Boehlerit", "Böhler": kein Treffer.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (1) Fertigungsbeleg V für Kapfenberg (Firmenseite/Impressum). (2) Gibt es Produkte mit Elektronik/Sensorik oder Klebung (z. B. Werkzeughalter mit Sensor, Kleben von Hartmetall in Stahlkörper)? Produktkatalog lesen. Ohne solche Produkte: Verguss Niedrig, kein Ziel. Aktion: niedrige Priorität.
- Nicht verwendbare Aussagen: Fertigung (S), Verguss (A), Patentfeld (nur Snippets). Stichprobe für Jey: nein.

## 7. Bohnenkamp Austria GesmbH | Halle 18, Stand 30
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2).** Reifen-/Räder-Großhandel, Tochter der Bohnenkamp AG, Osnabrück (S). Sitz und Fertigung nicht ermittelt, keine Fertigung belegt. Konzernabgleich Regel M: "Bohnenkamp", "HR Agrartechnik": kein CRM-Treffer, also kein Konzernbezug. Elektronik der Reifendruckregelanlagen kommt vom Zulieferer HR Agrartechnik (A, nicht Firma).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Sitz der Bohnenkamp Austria GesmbH (Firmenbuch) und ob Montage/Fertigung betrieben wird (Radmontage, Konfektion Reifendruckanlagen). Firmenbuch und bohnenkamp.de Standortseite lesen. Reiner Handel: Rot (E2). Aktion: niedrige Priorität.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 8. Brantner Fahrzeugbau | Halle 22, Stand A10
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN (schwach), Tabellenzeile 4 (Sitzregel: Fertigung Stufe A/S, Verguss Mittel Stufe A).** Zeilen 1 bis 3 greifen nicht: kein E-Beleg, Identität stimmig (Hans Brantner & Sohn Fahrzeugbaugesellschaft m.b.H., FN 63473v, KR Hans Brantner-Straße 8, 2136 Laa an der Thaya, nach Firmenbuchverzeichnis-Snippet, S), kein CRM-Konzernbezug. Eigene Suche: eine Landespressemeldung NÖ von 2010 nennt laut Snippet Produktion "zu 100 Prozent" in Laa an der Thaya (S, https://www.noe.gv.at/noe/pressAnnouncement/getPdf/63118); Stellenangebot "Entwicklungsingenieur Mechatronik" (htlkrems.ac.at, S) deutet auf hydraulik-mechatronische Entwicklung am Sitz. Industriefahrzeug-Bauer mit eigenem Produkt, ein erkennbarer Standort, keine Auslagerungshinweise: Sitzregel erfüllt (Hallenbau-GmbH ist eigene Gesellschaft mit anderer Adresse, nicht die fertigende Einheit). Verguss Mittel (A): LED-Beleuchtung/Kabelbaum, Sensorik/Waage und Steuerungen, Hydraulikdichtungen; Stahlmulde Niedrig. Das ist eine Ableitung ohne Beleg verbauter Elektronik, daher nur schwaches Grün; Bauteil-Regel angewandt (Maximum zählt). Patent: eine eigene Patent-Websuche ("Hans Brantner Sohn Fahrzeugbaugesellschaft patents.google.com"): kein Anmelder-Treffer; Hinweis "patented by Brantner" (Selbstreinigungskante) ohne Nummer (S). Datenbankabfrage fehlt.
- CRM: "Brantner Fahrzeugbau", "Brantner", "Hans Brantner & Sohn": kein Treffer, neu. Hinweis zur Verwechslung: Brantner-Gruppen (z. B. Umwelt/Entsorgung, Hallenbau) sind andere Einheiten, nicht abgeglichen mit dem CRM-Bestand außer über Name "Brantner": kein Treffer.
- Korrekturen an Toms Feldern: keine inhaltlich; Fertigung Hoch bleibt Stufe S (Land NÖ Pressemeldung hinzugefügt, ebenfalls S). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (zur Absicherung, damit das Grün final werden kann): (1) Welche Elektronik/Beleuchtung/Sensorik ist in Brantner-Anhängern verbaut und wird sie in Laa montiert (Kabelbäume)? Produktseiten (hb-brantner.at / brantner-fahrzeugbau.at), Datenblätter, Stellenanzeigen Laa im Browser lesen. (2) Fertigung Laa: Impressum/Firmenseite im Browser, Zitat festhalten (V). (3) Patentsuche F5 in Google Patents, Espacenet, DEPATISnet nachholen (Anmelder "Hans Brantner & Sohn", "Brantner").
- Nicht verwendbare Aussagen: Fertigung Laa (S), Verguss (A), Patentfeld, Produktumfang. Stichprobe für Jey: ja (einziges Grün, rein abgeleitet).

## 9. Bräuer Stalltechnik GmbH | Halle 23, Stand 370
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Eigene Suche bestätigt Wachtberg 74, 4441 Behamberg (Advantage Austria, WKO) und Eigenfertigung (Blechbearbeitung, Laserschneiden, Schweißroboter, techpilot; Advantage Austria: "Produktion und Vertrieb" von Stallungen; weiterer Standort im Bezirk Amstetten laut techpilot, alles S). Fertigung in AT also plausibel (Sitzregel am ehesten erfüllt, aber zwei Standorte/Bundesland uneinheitlich). Das Problem ist der Verguss: Stahlbau, Boxen, Gitter sind Niedrig; Mittel nur über zugekaufte Antriebe/Steuerungen (A), der Entmistungsroboter Barn-E stammt von JOZ (NL) und wird nur vertrieben. Für Zeile 4 reicht das ohne Produktbeleg nicht. CRM: "Bräuer", "Bräuer Stalltechnik", "JOZ": kein Firmentreffer; BREUER GmbH & Co. KG [DE] (0,92) ist anderer Name/anderes Land, nicht bekannt.
- Korrekturen an Toms Feldern: Bundesland: PLZ 4441 liegt in Oberösterreich, WKO-Eintrag nennt Niederösterreich; Gebiet Österreich unverändert. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Baut Bräuer selbst Anlagen mit Elektrik/Elektronik (Futter-/Fördertechnik, Steuerschränke, Tränken) oder nur Stahlbau, und an welchem Standort (Behamberg/Amstetten)? Firmenwebsite, Impressum, Produktkatalog und Stellenanzeigen im Browser lesen. Nur Stahlbau: Verguss Niedrig, kein Ziel. Aktion: mittlere Priorität, nicht kontaktieren.
- Nicht verwendbare Aussagen: Verguss (A), Eigenanteil, Bundesland, Patentfeld. Stichprobe für Jey: ja (Produktumfang offen).

## 10. CA Catering Foodtruck Frau Knolle | Freigelände, Stand 180
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt; Streichkandidat).** Gastronomie/Catering laut Messeliste ("Sonstiges"), Firma ist nicht auffindbar (Toms Suchen ohne Treffer; eigene Suche nicht ausgeführt). Ein Cateringbetrieb ist kein Fertiger; ein Rot nach E2/E3 ist mangels Quelle nicht belegbar, daher nur Gelb. CRM: "CA Catering Foodtruck Frau Knolle", "Frau Knolle": kein Treffer.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Identität und Tätigkeit der Ausstellerfirma (Name, Sitz, Rechtsform) im Ausstellerverzeichnis der agraria, Detailseite Freigelände Stand 180, prüfen. Bestätigt sich Catering: Rot (kein Fertiger, keine Fertigung). Aktion: Streichempfehlung, keine weitere Recherche nötig, wenn Jey zustimmt.
- Nicht verwendbare Aussagen: alle (A). Stichprobe für Jey: nein.

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind durchgehend korrekt niedrig angesetzt (keine V-Aussage vorgetäuscht). Toms Einschätzungen "kein Fertiger"/"unwahrscheinlich" bei Nr. 1, 3, 4, 7 sind ohne V-Beleg nicht Rot; ich setze Gelb mit Auftrag (Regel D: fehlender Beleg allein ist nie Rot).
- Rot nur bei Nr. 2 und 5, gestützt auf die Jey-Entscheidung (Verbände/Beratung raus), nicht auf einen von mir gelesenen V-Beleg.
- Brantner ist der einzige Kandidat mit Fertigung in Österreich und plausibler Elektronik; Grün stützt sich auf Sitzregel und Produkttyp (A), nicht auf Belege.
- Vorschlag Fehlerlog (Jey gibt frei, nicht eingetragen): Bei Messelisten mit Händler-/Verbands-/Gastro-Ausstellern vor der Recherche Ausstellerkategorie (Messeprofil) prüfen, um Suchaufwand und Gelb-Aufträge zu sparen.

## Einschränkungen
- Browser (Chrome) nicht verfügbar, WebFetch nicht eingesetzt: kein Gegenlesen nach Abschnitt H, keine Impressen, Datenblätter oder Karriereseiten gelesen; alle Aussagen Stufe S, A oder ?. Kein "Zitat im Browser bestätigt: ja", kein Grün mailtauglich. Stufe V (Regel O) nicht möglich.
- WebSearch: 5 Abfragen (Brantner Produktion, Brantner Patent, Bräuer Produktion, BERTI Importeur, Boehlerit Produkte). NICHT durchgeführt: eigene Suchen zu Bio Austria OÖ, Blickwinkel, Bobcat Vario Welt, Boden.Wasser.Schutz.Beratung, Bohnenkamp Austria, CA Catering (nur CRM und Einordnung, Sitzungslimit/Priorisierung); keine eigene Patentsuche für Nr. 1 bis 7, 9, 10; keine eigenen Wettbewerbersuchen (nur Listenabgleich).
- Patente: Pflichtsuche F5 (Google Patents, Espacenet, DEPATISnet) für alle 10 Firmen nicht erfüllt; Batch UNVOLLSTÄNDIG, bevor ein Grün final wird. Rechtsstand nirgends geprüft. Anmeldervarianten (Boehlerit-Gruppe, Bobcat/Doosan, Bohnenkamp AG) nicht gesucht.
- Wettbewerbereinsatz (F6): nur Listenabgleich und Toms Angaben; "kein Hinweis" ist kein Gegenbeweis. Messe-Signal (E1-Wettbewerber auf der agraria) nicht geprüft; keine der zehn Firmen ist selbst E1.
- Offen: Identität BERTI (Hersteller vs. österreichischer Importeur), Sitz Bohnenkamp Austria, Bundesland Bräuer (OÖ/NÖ), Identität Frau Knolle. Firmenbuch/Impressum nirgends gelesen.
- Kundendatenbank (Excel) nicht lesbar; CRM-Abgleich per Skript auf Textexporte. Keine "Verifiziert am"-Prüfung nötig (keine CRM-Treffer).
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
