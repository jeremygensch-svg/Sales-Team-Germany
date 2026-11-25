# Tina Batch 08 - agraria 2026 Wels (Prüfung von tom_batch_08.md)
Erstellt: 2026-11-24 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_08.md (10 Firmen, Eingabe-Nr. 71 bis 80; hier Blöcke 1 bis 10 wie bei Tom). Länder DE/AT/NL.
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Seitenabruf geprüft, vorläufig.** Es standen nur WebSearch (4 eigene Abfragen, Snippets/Kurzfassungen), Bash und das CRM-Skript zur Verfügung; ein Browser fehlt, WebFetch wurde nicht eingesetzt. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Nichts ist mailtauglich.
Entscheidungen von Jey angewandt: Verbände/Prüfdienstleister/Forschung raus; Firmen im CRM mit gleichem/sehr ähnlichem Namen raus; Anlagenbauer bleiben drin, außer sie bauen selbst Verguss-/Dosieranlagen (E1). Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum: 2026-11-24.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | AGRAR-HANDEL Edlinger GmbH (H23/440) | GELB (Rot-Kandidat E2) | 7 | nein |
| 2 | AgrarCommander GesmbH (H20/F30) | GELB (Rot-Kandidat E2 Software) | 7 | nein |
| 3 | AgrATool GmbH (H18/130) | GELB (Rot-Kandidat E2 Händler) | 7 | ja |
| 4 | AgriFlow (H20/1125) | GELB | 2 | ja |
| 5 | AGROTEL (H24/80) | GELB | 2 | ja |
| 6 | Agrovio Alp GmbH (H22/1120) | GELB | 2 | ja |
| 7 | AKRA Karner Düngerproduktion (H23/270) | GELB | 6 | nein |
| 8 | All You Can Miet GmbH (H22/B30) | GELB (Rot-Kandidat E2) | 7 | nein |
| 9 | AMA Marketing Gmbh (H21/1360) | ROT (Jey-Entscheidung Verband/Organisation, E2) | 1 | nein |
| 10 | Amselgruber Landtechnik GmbH (H22/C40) | GELB (Rot-Kandidat E2 Händler) | 7 | nein |

Zahlen: Grün 0, Gelb 9, Rot 1. Keine Grün-Kandidatin im Batch.

CRM: `python3 crm_abgleich.py` für alle zehn Firmen samt Kurz-/Konzern-/Schwesternamen selbst wiederholt (Edlinger; Agrar Commander, Raiffeisen; Agratool; Agri Flow; Agrotel Handelsgesellschaft, Agrotel GmbH; Agrovio; Karner, AKRA; AllYouCanMiet; Agrarmarkt Austria; Amselgruber): überall "kein Treffer, neu". Toms CRM-Angaben bestätigt. Kein Konzern-/Altnamenbezug (Regel M) gefunden; die Konzernprüfung beschränkt sich auf die genannten Namen.
Wettbewerberabgleich (F6): Grep auf wettbewerber_referenzen.md nach Edlinger, AgrarCommander, AgrATool, AgriFlow, AGROTEL, Agrovio, Karner/AKRA, All You Can Miet, AMA, Amselgruber: kein Treffer. Eigene Wettbewerber-Einzelsuche nur für AGROTEL (siehe dort), sonst nicht gefahren (Händler/Software/Dünger). Messe-Signal von Tom übernommen (kein Wettbewerber-Aussteller), ohne Einfluss.
Patente (F5): Google Patents, Espacenet, DEPATISnet nicht direkt abfragbar (kein Browser). Eigene Patent-WebSearch nur für AGROTEL (1 Abfrage, bestätigt EP1031277, erloschen, ohne Vergussbezug). Für die übrigen neun Firmen keine eigene Patentsuche von mir; Toms Suchen (je zwei WebSearch-Abfragen, 0 Treffer) werden weder bestätigt noch widerlegt. Feld 9 ist damit bei allen Firmen ohne Datenbankabfrage: nach F5 UNVOLLSTÄNDIG, im Browser nachholen (bei den Rot-Kandidaten/Rot nachrangig, bei AGROTEL, AKRA, Amselgruber, AgrATool nur falls Eigenfertigung bestätigt wird).
Nicht durchgeführt (offen benannt): alle Seitenabrufe (Impressum, Firmenbuch, Websites), Patentdatenbanken, enge Suche potting compound/Vergussmasse, Stellenanzeigen-Suche, Größe/Umsatz, Kontaktsuche (Regel K).

---

## 1. AGRAR-HANDEL Edlinger GmbH | Halle 23 Stand 440
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2).** Handelsunternehmen mit Futtermitteln/Zusätzen, Sitz Nußbach OÖ. Zeile 1 greift nicht, weil der E2-Beleg (Händler ohne Fertigung) nur Stufe S ist (WKO-Snippet, Messeliste). CRM: neu (Skript bestätigt). Verguss Niedrig (A), Fertigung Niedrig (A).
- Korrekturen an Toms Feldern: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Ist die Firma reiner Händler (dann Rot nach E2 mit URL) oder betreibt sie Mischfutter-/Fertigungsanlagen? Wo: Firmenwebsite/Impressum, WKO-Eintrag https://firmen.wko.at/agrar-handel-edlinger-gmbh/ im Browser lesen. Aktion: nicht kontaktieren; bei Händlerbeleg Rot.
- Nicht verwendbare Aussagen: alle zu Fertigung, Produkt, Verguss (A/S). Stichprobe für Jey: nein. Verifikation: 2026-11-24.

## 2. AgrarCommander GesmbH | Halle 20 Stand F30
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2 Software).** Farmmanagement-Software, Korneuburg; Beleg nur Verzeichnissnippets (S), daher kein V-Rot. Rechtsform GesmbH/GmbH uneinheitlich (Tom Feld 17), Konzern Raiffeisen: CRM kein Treffer. Verguss Niedrig (A).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Bietet die Firma Hardware (Sensoren, Terminals) an oder ausschließlich Software? Wo: agrarcommander.at, Impressum/Firmenbuch Korneuburg im Browser. Bei reiner Software Rot nach E2. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein. Verifikation: 2026-11-24.

## 3. AgrATool GmbH | Halle 18 Stand 130
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2 Händler).** Registerzweck "Handel mit landwirtschaftlichen Maschinen" (S, Snippet), Dimbach OÖ. Messeliste nennt Tore, Antriebe, Stalltechnik, Gülletechnik. Meine Websuche (Eigenmarke/Hersteller Dimbach) fand keinen Bezug zu AgrATool: weder Eigenfertigung noch Gegenbeleg. Verguss Niedrig (A); Zukauf-Tor-Antriebe zählen ohne Fertigung nicht (Tom, nachvollziehbar).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Hat AgrATool eine Eigenfertigung (Eigenmarke Tore/Antriebe/Stalltechnik)? Wo: agratool.at (KSV nennt "agrartool.at": Schreibweise klären), Impressum, Produktseiten, Stellenanzeigen Dimbach. Bei reinem Handel Rot (E2). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung/Produkt/Verguss (S/A). Stichprobe für Jey: ja (Website-Schreibweise unklar, Eigenmarke möglich). Verifikation: 2026-11-24.

## 4. AgriFlow | Halle 20 Stand 1125
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Toms Suchen und die Messeliste ergeben keine auffindbare Firma; Rechtsform, Sitz, Land unbekannt. Ich habe keine eigene Identitätssuche gefahren (offen). Fertigung/Verguss Niedrig (?), Produkt laut Messeliste Software/Smart Farming (S). Kein E-Beleg, daher nicht Rot. CRM: neu.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer ist AgriFlow (Rechtsform, Sitz, Land, Tätigkeit)? Wo: Messeprofil agraria.at (Aussteller AgriFlow, Adresse/Website), Firmenbuch/Impressum. Prüfen, ob Hardware (Sensorik, Durchflussmessung) angeboten wird; bei reiner Software Rot (E2). Aktion: nicht weiter verfolgen bis geklärt.
- Nicht verwendbare Aussagen: alle (?). Stichprobe für Jey: ja (Firma nicht identifizierbar). Verifikation: 2026-11-24.

## 5. AGROTEL | Halle 24 Stand 80
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität: zwei gleichnamige Einheiten DE/AT; Zeile 4 wäre bei Klärung nicht automatisch erfüllt).** Meine Websuchen bestätigen Toms Befund: AGROTEL GmbH, Hartham 9, Neuhaus am Inn; AgriExpo-Profil (S): "developed, planned and manufactured in our own factory"; eigene Montageteams; ISO 9001/14001 (S). Daneben AGROTEL Handelsgesellschaft m.b.H., Enzenkirchen (AT). Messeliste führt Land AT, ausstellende Einheit unklar. Produkte laut meiner Suche: Hallen, Windschutz, Textiltore, Biogaskomponenten; Tore mit Antrieben/Steuerungen oder Eigenelektronik ließen sich NICHT bestätigen (Toms Elektronik-Annahme bleibt A auf Zukaufteilen). Bauteile: Torantriebe/Steuerung (Zukauf) Mittel (A), Planen/Gasspeicher (Schweißen/Kleben ungeklärt) Niedrig, Stahlbau Niedrig. Gesamt Verguss Mittel (A), schwach; bei Eigenfertigung nur der Hallen/Tore wäre Zeile 6 (Verguss Niedrig) möglich. E1 geprüft: kein Dosier-/Vergussanlagenbau erkennbar, Firma bleibt drin.
- Patent (eigene Suche): Luxemburger Patentregister: EP1031277 "Hygiene device", Anmelder AGROTEL GmbH, Neuhaus/Inn, angemeldet 2000, Status erloschen (Ablauf 2020-02-24 laut Register, S); kein Vergussbezug, nur schwaches Signal. Broschüre bewirbt Cosyhome Calf Village als "patent protected" (Nummer unbekannt). Datenbanken nicht abgefragt.
- Wettbewerbereinsatz: eigene Websuche nur über Antrieb/Steuerung; keine Hinweise auf Wettbewerber-Produkte. Kein Beleg für "kein Einsatz".
- Korrekturen an Toms Feldern: Feld 3/4: Messeliste AT, Fertigung DE belegt nur S; Feld 8 Mittel nur über Zukaufteile (A), von mir als schwach gewertet. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Welche Einheit stellt aus: AGROTEL GmbH (Neuhaus am Inn) oder AGROTEL Handelsgesellschaft m.b.H. (Enzenkirchen)? Messeprofil agraria.at, Impressum agrotel.eu, Handelsregister Passau/Firmenbuch Linz. (b) Fertigung Neuhaus am Inn mit V belegen (Firmenseite/Stellenanzeige, Zitat). (c) Werden Torantriebe/Steuerungen selbst gebaut oder zugekauft; Planen/Gasspeicher geschweißt oder geklebt? Wo: Produktseiten Tore/Biogas, Gesamtprospekt (https://www.ecomondo.com/restricted-assets/digital-profiles/01_ATTACHMENTS/RIC25/AGROTEL-Gesamtprospekt-EN-Kurzdruck-68d3f8e4a4eab.pdf.pdf). (d) Patente DEPATISnet/Espacenet mit Anmelder AGROTEL GmbH vollständig. Aktion: nach Klärung entscheiden; vorerst nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Neuhaus (S); Verguss Mittel (A); Zuordnung der ausstellenden Einheit (?). Stichprobe für Jey: ja (Identität, Verguss nur über Zukauf). Verifikation: 2026-11-24.

## 6. Agrovio Alp GmbH | Halle 22 Stand 1120
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Nur WKO-Verzeichniseintrag (Wien-Innenstadt); Tätigkeit (Dünger, In-Furrow-Nachrüstsätze, Düngeplanung) lässt Händler/Beratung vermuten, aber ohne V kein Rot. Eigene Suche habe ich nicht wiederholt (offen). Verguss Niedrig (A: Düngemittel, mechanische Sätze). CRM: neu.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer ist Agrovio Alp GmbH (Firmenbuch, Impressum, Website), wer fertigt die IN-FURROW-Nachrüstsätze, und gibt es Elektronik (Dosiersteuerung, Sensorik) darin? Wo: Firmenbuch Wien, Messeprofil agraria.at, Produktseite Hersteller des Systems. Bei Handels-/Beratungsfirma ohne Fertigung Rot (E2). Aktion: nicht kontaktieren bis geklärt.
- Nicht verwendbare Aussagen: alle zu Fertigung/Produkt (S/A/?). Stichprobe für Jey: ja (Identität und Hersteller offen). Verifikation: 2026-11-24.

## 7. AKRA Karner Düngerproduktion | Halle 23 Stand 270
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6, Fertigung wahrscheinlich DE/AT/NL, Verguss Niedrig).** Düngemittelhersteller (Neulengbach NÖ, Karner Düngerproduktion GmbH, Marke AKRA; S). Düngemittel ist Chemie, aber kein Vergussmassen-/Klebstoffhersteller, daher kein E1. Alle Bauteile Niedrig (A: Dünger, Gebinde, Granulier-/Mischanlagen), keine plausible Vergusskomponente. Zeile 6 verlangt belegte Fertigung; sie ist nur S, daher Zeile 6/7 mit Auftrag. Tom stuft "unwahrscheinlich"; ich stimme zu, setze aber Gelb statt Rot, weil kein harter Ausschluss vorliegt. CRM: neu (Karner, AKRA geprüft).
- Korrekturen: Tom Feld 7 "Hoch (S)" für Fertigung ist nach Sitzregel nur A/S; kein Einfluss auf die Ampel. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Werden neben Dünger Geräte/Elektronik (Dosier- oder Ausbringtechnik, Messsensorik) gebaut oder verkauft? Wo: duenger-akra.at Produktseiten und Impressum im Browser. Ohne Elektronikprodukt Priorität niedrig. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Neulengbach (S); Verguss Niedrig (A). Stichprobe für Jey: nein. Verifikation: 2026-11-24.

## 8. All You Can Miet GmbH | Halle 22 Stand B30
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2).** Vermietung/Handel von Baumaschinen (Fremdhersteller Kramer, Manitou), Seyring NÖ; Beleg nur Händlerprofil-Snippet (S). Keine Eigenfertigung belegt, aber auch kein V für E2. Eigene Websuche nicht gefahren (offen). CRM: neu.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Betreibt die Firma Eigenbau/Umbau von Maschinen? Wo: Firmenbuch NÖ, Messeprofil agraria.at, landwirt.com-Händlerprofil im Browser. Bei Vermietung/Handel Rot (E2) mit URL. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein. Verifikation: 2026-11-24.

## 9. AMA Marketing Gmbh | Halle 21 Stand 1360
**ohne Browser geprüft, vorläufig. Ampel: ROT (Tabellenzeile 1, harter Ausschluss E2 plus Jey-Entscheidung "Verbände/Organisationen raus").** Rot, weil: Marketing- und Lizenzgesellschaft (AMA-Gütesiegel, Alleingesellschafterin Agrarmarkt Austria), keine Produkte, keine Fertigung (Quellen laut Tom: https://www.rechnungshof.gv.at/rh/home/home/Agrarmarkt_Austria_Marketing_GesmbH , https://www.wko.at/ktn/handel/agrarhandel/ama-guetesiegel-richtlinie-agrarhandelundmuehlen20240405-bes.pdf; beide nur S, von mir nicht gegengelesen). Das Rot stützt sich auf Jeys ausdrückliche Entscheidung; der Quellenbeleg ist nur Stufe S, die Einordnung als Organisation ist aber eindeutig. CRM: neu (auch Agrarmarkt Austria: kein Treffer).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: keiner (Rot). Optional: ama.at Impressum zur Bestätigung der Rolle.
- Nicht verwendbare Aussagen: Quellenzitate (S). Stichprobe für Jey: nein. Verifikation: 2026-11-24.

## 10. Amselgruber Landtechnik GmbH | Halle 22 Stand C40
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2 Händler).** Landmaschinenhandel (Registerzweck, S). Meine Websuche bestätigt Händlerprofil auf landwirt.com (Premium Plus Händler) und Verkauf von Dominator-Anbaugeräten unter dem Händlerschriftzug; ob Dominator Eigen- oder Fremdmarke ist, ungeklärt (ein Inserat nennt Fremdhersteller Otte). Keine Eigenfertigung belegt, kein Gegenbeleg. Verguss Niedrig (A). CRM: neu.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Wer stellt die Marke "Dominator" her, und hat Amselgruber eigene Fertigung (Umbauten, Anbaugeräte)? Wo: amselgruber.at Impressum/"Über uns", Dominator-Herstellerseite, Firmenbuch FN 420393 a. Bei reinem Handel Rot (E2). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle zu Fertigung/Produkt (S/A). Stichprobe für Jey: nein. Verifikation: 2026-11-24.

---

## nicht aufgenommen (bereits bekannt / unklar)
Kein CRM-Treffer bei allen zehn Firmen (Skript von mir wiederholt). Unklar (Identität): Nr. 4 AgriFlow, Nr. 5 AGROTEL (zwei Einheiten DE/AT), Nr. 6 Agrovio Alp. Ausgeschieden nach Jey-Entscheidung: Nr. 9 AMA Marketing (Organisation). Rot-Kandidaten bei Beleg V: Nr. 1, 2, 3, 8, 10 (Händler/Software/Vermieter).

## Einschränkungen
- Nur WebSearch (vier eigene Abfragen, Snippets) verfügbar, kein Browser: keine Stufe V, keine Zitatbestätigung, alle Ampeln vorläufig. Sitzungslimit: Suchen auf AGROTEL (2), Amselgruber (1), AgrATool (1) konzentriert; AgriFlow, Agrovio, AKRA, Edlinger, AgrarCommander, All You Can Miet, AMA nicht selbst nachgesucht.
- Patentdatenbanken nicht abgefragt; Feld 9 bei allen Firmen nach F5 unvollständig (siehe Gesamtübersicht). Keine Fertigungs- oder Stellenanzeigensuche außer AGROTEL.
- Größe/Umsatz nicht gesucht; keine Kontaktsuche (Regel K). Es wurde nichts in die Datenbank geschrieben, kein git commit.
