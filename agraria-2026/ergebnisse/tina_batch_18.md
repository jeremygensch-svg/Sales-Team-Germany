# Tina Batch 18 - agraria 2026 (Prüfung von tom_batch_18.md)
Erstellt: 2026-11-25 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_18.md (10 Firmen, Nr. 1 bis 10 des Batches; Tom nummeriert in der Eingabe 171 bis 180, hier Nr. 1 bis 10 in Toms Reihenfolge).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser geprüft, vorläufig.** Es standen WebSearch (10 Abfragen, Kurzfassungen der Suchmaschine) und Bash zur Verfügung. Kein Browser (Chrome) verfügbar; WebFetch habe ich nicht eingesetzt, da Tom für dieselben Firmenhosts "Host nicht auflösbar" meldet. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün ist mailtauglich.
Skripte: `python3 crm_abgleich.py` für alle Firmen samt Konzern-/Alt-/Schwester-/Schreibvarianten selbst wiederholt (Deere, Lagerhaus, RWA, Albert Kerbl, Königswieser Gerätetechnik, Kipkop, Krampe Fahrzeugbau, Krusta Wasserfilterbau, Jenz Maschinenbau u. a.): alle zehn neu. Einzige Skript-Hinweise sind Wortwurzel-Zufälle (Alber GmbH und Albert & Hummel GmbH bei "Albert Kerbl"; Nutz Maschinenbau GmbH bei "Jenz Maschinenbau"), ohne Bezug. Zusätzlich Grep auf Firmen-/Konzernnamen in bekannte_firmen_DE-AT-NL.txt und kundendatenbank_export.txt: kein Treffer. Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum aller Einträge: 2026-11-25.
Jey-Entscheidungen angewendet: Verbände, Prüfdienstleister und Forschung raus (in diesem Batch keine Firma betroffen); Firmen im CRM mit gleichem/sehr ähnlichem Namen raus (keine); Anlagenbauer bleiben drin, außer sie bauen selbst Verguss-/Dosieranlagen (E1): Krusta ist Wasserfilter-Anlagenbauer, kein Verguss-/Dosieranlagenbauer, E1 trifft nicht.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | JENZ (Halle 18, Stand 430) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 2 | JOHN DEERE - Lagerhaus Technik-Center GmbH (Halle 20, Stand F10) | GELB | 5 (Rot-Kandidat E2) | nein |
| 3 | Kerbl Austria Handels GmbH (Halle 23, Stand 280) | GELB | 5 (Rot-Kandidat E2) | nein |
| 4 | KGD Königswieser (Halle 18, Stand 10) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 5 | KIP KOP GmbH (Halle 18, Stand 330) | GELB | 2 | ja |
| 6 | Kneidinger 1880 GmbH (Halle 18, Stand 200) | GELB | 5 (Rot-Kandidat E2) | nein |
| 7 | Kostbar Markt (Halle 20, Stand 1180) | GELB | 2 (Rot-Kandidat E2) | nein |
| 8 | kraftholz neuhofer gmbh (Halle 18, Stand 50) | GELB | 5 (Rot-Kandidat E2) | nein |
| 9 | Krampe (Halle 20, Stand F100) | GELB | 2 | ja |
| 10 | Krusta Wassertechnik (Halle 23, Stand 320) | GELB | 2 | ja |

Zahlen: Grün 2 (beide schwach, nur Stufe A/S), Gelb 8, Rot 0. Kein Rot, weil jede E2-Einordnung (Händler/Dienstleister) nur auf Stufe S/A beruht; Rot braucht V mit URL.

Messe-Signal (Regel N2) von Tom übernommen und nicht eigenständig neu gegriffen: kein Wettbewerber unter den Ausstellern; ändert nichts an der Ampel.

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Eigene Patent-Websuche für die vier aussichtsreichsten Firmen (Jenz, Königswieser, Krampe; Krusta nur Fertigungs-/Identitätssuche, Patentbezug über Anmeldername nicht gesondert gefahren). Für Nr. 2, 3, 5, 6, 7, 8 keine eigene Patentsuche (Händler/Plattform/Dienstleister, nicht identifizierte Firma): Toms Suchen dort weder übernommen noch widerlegt. "Keine Treffer" ist kein Gegenbeweis. Batch deshalb nach F5 UNVOLLSTÄNDIG, bevor ein Grün final wird; Nachholen im Browser (Google Patents, DEPATISnet) nötig.
Wettbewerbereinsatz (F6): Grep auf wettbewerber_referenzen.md mit Jenz, Deere, Lagerhaus, Kerbl, Königswieser, Kip, Kneidinger, Kostbar, kraftholz, Krampe, Krusta: kein Treffer; keine Einzelsuchen mit Wettbewerbernamen von mir.

Korrekturen an Tom, kompakt:
- Nr. 1 JENZ: Tom fand kein Jenz-Patent. Meine Suche: Anmeldung "Mobiler Trommelhacker mit Fahrerhaus" DE102023130471A1 (Veröffentlichung 2025-05-08) und EP4549023A2, Anmelder Jenz GmbH laut Suchmaschinenzusammenfassung (S); Familie mit DE102013100254A1 und DE102015106209A1 (Anmelder dort nicht bestätigt). Kein Verguss-Bezug erkennbar.
- Nr. 9 Krampe: Tom fand keine Patente. North-Data-Profil (S): 8 Schutzrechtsanmeldungen (1 Patent, 7 Gebrauchsmuster, u. a. "Hydraulisch schwenkbarer Unterfahrschutz"), Patenterteilung Schubboden-Kippsattel laut Firmennews (S). Kein Verguss-Bezug.
- Nr. 4 Königswieser: Website ermittelt (koenigswieser.com); Tom hatte keine. Winden laut Hersteller-Website "in Vorchdorf entwickelt und endgefertigt" (S, Zusammenfassung). Funkfernbedienung bei SA-Modellen laut Website nur Zubehör, nicht ab Werk montiert (S).
- Nr. 10 Krusta: Rechtsform nicht "Ges.mbH", sondern "Krusta Wasserfilter GmbH"/"Krusta Wasserfilterbau GmbH" (Kompass/wlw, S); Österreich ist laut Krusta-Seiten nur "Vertretung Österreich" in Wels (S).

---

## 1. JENZ | Halle 18 Stand 430
**ohne Browser geprüft, vorläufig. Ampel: GRÜN (schwach), Tabellenzeile 4 (Sitzregel).** Zeilen 1 bis 3 greifen nicht: kein E-Beleg V, Identität stimmig (JENZ GmbH Maschinen- und Fahrzeugbau, Wegholmer Str. 14, 32469 Petershagen, Amtsgericht Bad Oeynhausen HRB 5064 laut North Data und Hersteller-Seite, S; Messeliste führt "AT", Sitz ist DE, Abweichung benannt), kein CRM-Bezug. Eigene Holzhacker/Zerkleinerer, ein Standort, kein Händler: Sitzregel Stufe A; "produces ... at its site in Petershagen" (jenz.de/About, S). Verguss Mittel (A: Maschinensteuerung "easy2", Touchscreen-Kabine, Joysticks, Sensorik, Magnetventile der Hydraulik, Kabelbaum). Konzernzugehörigkeit nicht ausdrücklich geprüft (North-Data-Netzwerk nicht gelesen).
- Eigene Prüfung: CRM neu. Patent: eigene Suche, Treffer Jenz (siehe Korrekturen oben), Rechtsstand offen, Verguss nicht belegt. Wettbewerber: kein Treffer.
- Korrekturen an Toms Feldern: Feld 9 (kein Jenz-Patent) ergänzt; Feld 4 Sitz bestätigt (S), Feld 7 bleibt Hoch (A); Verguss Mittel (A) bestätigt. Zitat im Browser bestätigt: nein.
- Nachrecherche (für Mailstufe nötig, kein Gelb): (a) jenz.de Impressum und "About JENZ" im Browser lesen: Fertigung Petershagen mit V; (b) Steuerung/Elektronik Eigenbau oder zugekauft (Stellenanzeigen Elektriker/Elektronik); (c) Messeprofil agraria Halle 18 Stand 430 lesen: Aussteller läuft unter AT (Vertriebspartner?). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Petershagen (A/S); Verguss Mittel (A); Elektronikumfang (?); Patentzuordnung (S). Stichprobe für Jey: ja (Grün nur auf A, Verguss unbelegt).

## 2. JOHN DEERE - Lagerhaus Technik-Center GmbH | Halle 20 Stand F10
**ohne Browser geprüft, vorläufig. Ampel: GELB, Tabellenzeile 5 (Rot-Kandidat E2).** Landtechnikhändler/Service (Korneuburg, John-Deere-Vertrieb Österreich; Toms Quellen, S). Keine Fertigung belegt; Sitzregel gilt nicht (Händler). Verguss Niedrig (A, Fremdprodukte). CRM: "Deere", "Lagerhaus", "RWA", "John Deere Lagerhaus Technik-Center": kein Treffer, neu; Konzernbezug (Regel M) nicht im CRM. Keine eigene Websuche (Händler: CRM plus Einordnung genügt).
- Korrekturen: keine. Rechtsform (GmbH oder GmbH & Co KG) weiter offen. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Betreibt die Gesellschaft über Handel und Werkstatt hinaus eigene Fertigung/Montage in AT? Firmenbuch FN 148552 i (justiz.gv.at/evi.gv.at) und rwa.at-Beschreibung im Browser lesen; bei reiner Handels-/Servicegesellschaft: Rot nach E2 mit URL. Aktion: nicht kontaktieren. Deere-Werke wären ein eigener Konzernauftrag (nicht dieser Eintrag).
- Nicht verwendbare Aussagen: alle zu Fertigung (S) und Verguss (A). Stichprobe für Jey: nein.

## 3. Kerbl Austria Handels GmbH | Halle 23 Stand 280
**ohne Browser geprüft, vorläufig. Ampel: GELB, Tabellenzeile 5 (Rot-Kandidat E2).** Vertriebsgesellschaft (Poggersdorf; "key sales hub", S laut Tom). Keine Fertigung in AT belegt; Name "Handels GmbH" stützt E2, aber ohne V kein Rot. Fertigung in Buchbach (Bayern) gehört zur Mutter Albert Kerbl GmbH, nicht zu dieser Einheit; nicht vermischt. Verguss Niedrig (A; beheizte Tränken nur Annahme). CRM: "Kerbl", "Albert Kerbl": kein Treffer, kein Konzernbezug. Keine eigene Websuche.
- Korrekturen: keine. Patent-Aggregator-Angabe (14 Anmeldungen) betrifft die Mutter, nicht diese Einheit. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Hat Kerbl Austria Handels GmbH Fertigung/Montage/Konfektion in Poggersdorf? Firmenbuch FN 33382 t und kerbl.com/Standortseite Österreich im Browser lesen; bei reinem Vertrieb Rot nach E2 mit URL. Mutter Albert Kerbl GmbH (Buchbach) wäre ein eigener Auftrag. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 4. KGD Königswieser | Halle 18 Stand 10
**ohne Browser geprüft, vorläufig. Ampel: GRÜN (schwach), Tabellenzeile 4 (Sitzregel).** Identität: Messename ist Produktkürzel; Firma ist Königswieser Gerätetechnik GmbH, Einsiedlinger Straße 51, 4655 Vorchdorf, mit Website koenigswieser.com (Suchtreffer: Herold, Landwirt.com, Hersteller-Website und Betriebsanleitungen, S). Das Identitätsrisiko aus Toms Feld 17 ist damit bis auf Impressum-Gegenlesen ausgeräumt; Zeile 2 greift nicht. Eigene Forstseilwinden, Gründung 1972, ein Standort, kein Händler, kein Konzernhinweis: Sitzregel Stufe A, gestützt durch "in Vorchdorf entwickelt und endgefertigt" (Zusammenfassung der Hersteller-Website, S). Verguss Hoch (A): Magnetspulen/Ventilelektrik der elektrohydraulischen Winden (KGD SA/EH); Funksteuerung nur Zubehör, nicht ab Werk (S), daher dort Niedrig bis Mittel; Bauteil-Regel: Maximum zählt, Grün bleibt.
- Eigene Prüfung: CRM "KGD Königswieser", "Königswieser Gerätetechnik": neu. Patent: eine eigene Suche (Königswieser Patent/Gebrauchsmuster Seilwinde): keine Treffer, kein Gegenbeweis; Anmelder-Varianten und IPC A66D nicht gefahren. Wettbewerber: kein Treffer.
- Korrekturen an Toms Feldern: Feld 5 (Website) ergänzt: koenigswieser.com; Feld 6/8: Funkfernbedienung bei SA-Modellen laut Website Zubehör (nicht ab Werk), Magnetspulen als Hoch-Bauteil bleiben (A). Toms "interessant" nicht über A hinaus bestätigt. Zitat im Browser bestätigt: nein.
- Nachrecherche (für Mailstufe nötig, kein Gelb): (a) koenigswieser.com Impressum und Unternehmensseite im Browser lesen: Fertigung Vorchdorf mit V (Zitat); (b) Datenblatt/Betriebsanleitung Baureihe SA: Magnetventile/Spulen, Schutzart, Elektrik; (c) Gesellschaft von "Konrad Forsttechnik"/Gleichnamigen abgrenzen. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Vorchdorf (A/S); Verguss Hoch (A); Eigenbau der Elektrik (?). Stichprobe für Jey: ja (Grün nur A, Tom "interessant").

## 5. KIP KOP GmbH | Halle 18 Stand 330
**ohne Browser geprüft, vorläufig. Ampel: GELB, Tabellenzeile 2 (Identität nicht belegt).** Messeliste: "Arbeitsbühnen; Anhänger". Meine eigene Suche (Kipkop Arbeitsbühne Anhänger Hersteller Österreich) findet keine Firma dieses Namens (nur Dorn Lift, Sky Go, Palfinger, Teupen u. a., nicht vermischt); zusammen mit Toms zwei Suchen drei erfolglose Abfragen. Sitz, Hersteller oder Händler, Fertigung offen. CRM: "KIP KOP", "Kipkop": kein Treffer, neu.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer ist KIP KOP GmbH? Messeprofil agraria.at (Halle 18 Stand 330: Adresse, Website, Produktgruppen) im Browser, Firmenbuch (evi.gv.at/justiz.gv.at) und WKO-Firmen-A-Z nach "KIP KOP", "Kipkop", "Kip-Kop". Danach Hersteller/Händler klären. Aktion: nicht weiter verfolgen, bis Identität geklärt.
- Nicht verwendbare Aussagen: alle (?). Stichprobe für Jey: ja (Firma nicht identifizierbar).

## 6. Kneidinger 1880 GmbH | Halle 18 Stand 200
**ohne Browser geprüft, vorläufig. Ampel: GELB, Tabellenzeile 5 (Rot-Kandidat E2).** Landtechnik-/Forsthändler mit Werkstatt (Altenfelden, Zwettl, Putzleinsdorf); Hammerschmiede-Historie nur Geschichte. Keine Fertigung belegt, Sitzregel gilt nicht (Händler). Verguss Niedrig (A). CRM: "Kneidinger", "Kneidinger 1880": kein Treffer, neu. Keine eigene Websuche.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Gibt es eigene Fertigung/Metallbau/Aufbauten in Altenfelden? kneidinger.at (Leistungen, Stellenanzeigen) im Browser lesen; bei reinem Handel/Service Rot nach E2 mit URL. Niedrige Priorität. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 7. Kostbar Markt | Halle 20 Stand 1180
**ohne Browser geprüft, vorläufig. Ampel: GELB, Tabellenzeile 2 (Rot-Kandidat E2).** Online-Plattform zur Lebensmittelrettung/Direktvermarktung, laut Ministeriumsseite vom BMLUK beauftragt (S laut Tom). Betreiber, Rechtsform und Sitz nicht ermittelt, daher Identität nicht belegt; Fertigung nicht zu erwarten, Verguss Niedrig (A, Block C). Zählt inhaltlich zu Dienstleistung/Plattform (E2) und liegt nahe an Jeys Entscheidung "Verbände/Dienstleister raus", aber ohne V kein Rot. CRM: "Kostbar Markt": kein Treffer. Keine eigene Websuche.
- Korrekturen: Toms Auftrag "keine Vertiefung" ist bei Gelb ungültig; ersetzt durch den Auftrag unten. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer betreibt Kostbar Markt? Impressum kostbarmarkt.at und BMLUK-Seite im Browser lesen; bei Behörden-/Vereinsplattform ohne Produktion Rot nach E2 mit URL (Vorschlag: Rot-Bestätigung durch Jey). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 8. kraftholz neuhofer gmbh | Halle 18 Stand 50
**ohne Browser geprüft, vorläufig. Ampel: GELB, Tabellenzeile 5 (Rot-Kandidat E2).** Forstdienstleister/Holzlogistik/Baumpflege mit Forstgerätehandel (Händlerlisting, S). Keine Fertigung belegt. Name und Firmenbuchnummer (FN 368396 i) passen; zwei Adressen (Zell am Moos laut KSV, Neukirchen an der Vöckla laut Maschinensucher) nur als Auffälligkeit, nicht als Identitätsbruch. Verguss Niedrig (A). CRM: "kraftholz", "kraftholz neuhofer": kein Treffer, neu. Keine eigene Websuche.
- Korrekturen: Toms Auftrag "keine Vertiefung, außer ..." ist als Gelb ungültig; ersetzt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Baut die Firma eigene Maschinen/Geräte oder nur Dienstleistung und Handel? Firmenbuch FN 368396 i und Website/Händlerprofil im Browser lesen; bei reinem Dienstleister/Händler Rot nach E2 mit URL. Niedrige Priorität. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 9. Krampe | Halle 20 Stand F100
**ohne Browser geprüft, vorläufig. Ampel: GELB, Tabellenzeile 2 (Identität nicht belegt).** Messeliste führt AT; Hersteller Krampe Fahrzeugbau GmbH, Zusestraße 4, 48653 Coesfeld, HRB 1815 AG Coesfeld (Impressum-/North-Data-Treffer, S). Meine Suche zum Österreich-Vertrieb: keine offizielle Importgesellschaft gefunden; Krampe wird in AT über unabhängige Händler und Lagerhaus-Technik-Center verkauft (Landwirt.com/Autoline-Listings, S). Ob der Aussteller in Wels der Hersteller oder ein Händler ist, bleibt ungeklärt. Auch für den Hersteller wäre Grün nicht ohne V möglich: mehrere Werke (Flamschen, Lette), Sitzregel verlangt dann V. Hersteller-Daten: ca. 280 Mitarbeiter, über 1.200 Fahrzeuge/Jahr; Stellenanzeigen Endmontage mit Einbau und Prüfung elektrischer Baugruppen und Steuerungen (Aggregator, S). Verguss Mittel (A: LED-Beleuchtung, Kabelbaum/Stecker, Magnetventile, ggf. Wiegesensorik).
- Eigene Prüfung: CRM "Krampe", "Krampe Fahrzeugbau": neu. Patent: eigene Suche, North-Data-Profil (S) mit 8 Anmeldungen (siehe Korrekturen); Anmelder-/Rechtsstand offen, kein Verguss-Bezug. Wettbewerber: kein Treffer.
- Korrekturen an Toms Feldern: Feld 9 (keine Patente) widerlegt für den Hersteller; Feld 7 bleibt Hoch (S), gilt nur für den Hersteller. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Wer ist der Aussteller in Halle 20 Stand F100: Hersteller Coesfeld oder österreichischer Händler/Lagerhaus-Partner? Messeprofil agraria.at im Browser lesen. (b) Wenn Hersteller: krampe.de (Impressum, Karriere "Endmontage"/Elektrik) lesen, Fertigung Coesfeld mit V belegen, Verguss-Bauteile (Beleuchtung, Steuerungen) und Zukauf klären; dann Grün erwartbar. Wenn Händler: Rot nach E2 mit URL für den Aussteller, Hersteller separat führen. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung (S); Verguss Mittel (A); Anzahl Mitarbeiter (S, zwei Zahlen 250/280); Patente (S). Stichprobe für Jey: ja (Aussteller-Rolle offen).

## 10. Krusta Wassertechnik | Halle 23 Stand 320
**ohne Browser geprüft, vorläufig. Ampel: GELB, Tabellenzeile 2 (Identität nicht belegt).** Hersteller der Filteranlagen ist Krusta Wasserfilter(bau) GmbH, Stadtlohn (DE), laut Suchmaschinenzusammenfassung Produktion in Eigenregie am Standort Stadtlohn (S; Adressangaben widersprüchlich: Südstraße 16/17, Borsigstraße 37 "Büro und Fertigung", Lager Ottostraße 10). Österreich: krusta.at nennt "Vertretung Österreich" in Wels (Peter Hofer, Impressum: handelt im Auftrag der Krusta Wasserfilter GmbH; S): Der Aussteller "Krusta Wassertechnik (AT)" ist daher vermutlich die Vertretung, nicht der Hersteller; nicht belegt. Wasserfilter-Anlagenbau ist kein E1 (keine Verguss-/Dosieranlagen). Verguss Mittel (A: Steuerventile/Steuerköpfe mit Elektronik, Dosierpumpen, Schaltschrank; Elektriker im Haus, S). CRM "Krusta", "Krusta Wasserfilterbau": neu.
- Korrekturen an Toms Feldern: Feld 4/17: Rechtsform GmbH statt "Ges.mbH"; Adressvarianten; Österreich-Vertretung Wels als wahrscheinlicher Aussteller. Feld 9: keine eigene Patentsuche zu Krusta über Anmeldername (nur Fertigungs-/Identitätssuchen). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Wer steht hinter dem Messestand (Hersteller Stadtlohn oder Vertretung Wels)? Messeprofil agraria.at, Impressum krusta.at und krusta-wasserfilter.de im Browser lesen; Handelsregister Coesfeld/Stadtlohn für die GmbH. (b) Wenn Hersteller: Fertigung Stadtlohn mit V (Über-uns-Seite, Stellenanzeigen) und welche Steuer-/Dosierelektronik verbaut wird. Ist der Aussteller nur die Vertretung: Rot nach E2 für diese Einheit mit URL, Hersteller Stadtlohn als eigener Eintrag führen. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Stadtlohn (S); Verguss Mittel (A); Adresse; Aussteller-Rolle (?). Stichprobe für Jey: ja (Identität/Rolle).

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind durchgehend korrekt niedrig angesetzt (keine V-Aussage vorgetäuscht). Seine Einstufungen "prüfenswert" (Jenz, Krampe, Krusta) und "interessant" (Königswieser) sind ohne Browser-Gegenlesen nicht über A/S hinaus zu bestätigen; Grün daher nur schwach.
- Muster dieses Batches: Die Messeliste nennt "AT", der Hersteller sitzt aber in DE (Jenz, Krampe, Krusta). Bei Jenz ist die Zuordnung eindeutig (Marke = Hersteller), bei Krampe und Krusta ist der Aussteller wahrscheinlich Händler/Vertretung. Vorschlag Fehlerlog (Jey gibt frei, nicht eingetragen): Bei Messelisten mit Land AT und Herstellern mit deutschem Sitz früh das Messeprofil lesen, bevor die Ampel vergeben wird.
- Zwei Tom-Aufträge ("keine Vertiefung" bei Kostbar Markt und kraftholz neuhofer, "nur falls Jey will" bei Kneidinger) machten Gelb ungültig; von mir durch konkrete Aufträge ersetzt (Rot-Kandidaten E2).
- Jey-Entscheidungen: keine Firma des Batches ist Verband, Prüfdienstleister oder Forschung; keine im CRM mit gleichem/ähnlichem Namen. Kostbar Markt kommt einer Plattform/Dienstleister-Aussortierung am nächsten (E2).

## Einschränkungen
- Kein Browser und kein WebFetch-Einsatz: kein Gegenlesen nach Abschnitt H, keine Impressen, Datenblätter, Register oder Karriereseiten gelesen. Alle Aussagen Stufe S, A oder ?; keine "Zitat im Browser bestätigt: ja"; kein Grün mailtauglich.
- WebSearch: 10 Abfragen. Königswieser 2 (Produktion/Elektronik, Patent), Krampe 3 (Patent, Österreich-Vertrieb, Stellenanzeigen), Jenz 2 (Patent/Steuerung, Trommelhacker-Anmeldung), Krusta 2 (Österreich/Hersteller, Fertigung/Steuerung), KIP KOP 1. Keine eigene Websuche für Nr. 2, 3, 6, 7, 8 (Händler/Plattform/Dienstleister: nur CRM und Einordnung).
- Patente: Pflichtsuche F5 (Google Patents, Espacenet, DEPATISnet) nicht direkt abgefragt; nur Suchmaschinen-Zusammenfassungen. Rechtsstand nirgends geprüft; Anmelderzuordnung bei Jenz (DE102023130471A1/EP4549023A2) und Krampe (North Data) nur S. Für Krusta, KIP KOP und die Händler keine eigene Patentsuche. Batch UNVOLLSTÄNDIG nach F5.
- Wettbewerbereinsatz (F6): nur Listenabgleich (Grep) und Toms Angaben; "kein Hinweis" ist kein Gegenbeweis. Messe-Signal von Tom übernommen.
- Sperrliste und Tab "Partner & Lieferanten" (E4) nicht eigenständig abgeglichen. Kundendatenbank (Excel) nicht lesbar; CRM-Abgleich per Skript und Grep auf die Textexporte. Keine "Verifiziert am"-Prüfung nötig (alle neu).
- Messeprofile auf agraria.at nicht gelesen; Gebiet bei Nr. 5, 7 beruht auf der Messeliste.
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
