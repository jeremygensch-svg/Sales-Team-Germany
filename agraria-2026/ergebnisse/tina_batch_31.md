# Tina Batch 31 - agraria 2026, Wels (Prüfung von tom_batch_31.md)
Erstellt: 2026-11-26 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_31.md (10 Firmen, Nr. 301 bis 310 bei Tom; hier 1 bis 10 in Toms Reihenfolge).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (3 Abfragen, Snippets/Kurzfassungen) und Bash zur Verfügung; WebFetch und Chrome nicht genutzt. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün, nichts mailtauglich.
Skripte: `python3 crm_abgleich.py` für alle Firmen samt Konzern-/Alt-/Schwesternamen selbst wiederholt (Urban, Urban Landtechnik, Vakutec, Vakutec Gülletechnik, Valibiotics, Ventura, Vereinigung Lohnunternehmer Österreich, Vitan, VLV, Vogelsang Austria / Vogelsang GmbH & Co. KG / Vogelsang, Voran Maschinen / Voran, Vredestein Tyres / Apollo Vredestein / Apollo Tyres / Apollo). Ergebnis deckt sich mit Tom: nur Vogelsang hat Treffer. Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum aller Einträge: 2026-11-26.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | Urban GmbH & Co. KG (H23 / 225) | GELB | 2 (Identität; Messeliste AT, Sitz Hude/DE) | ja |
| 2 | Vakutec (H20 / C40) | GELB | 2 (Kurzname ohne Rechtsform; danach evtl. 4) | ja |
| 3 | Valibiotics GmbH (H23 / 470) | ROT (Jey-Entscheidung Biotech/Saatgut) | außerhalb Tabelle D (sonst 6/7) | nein |
| 4 | Ventura (H24 / 110) | GELB | 2 (nicht identifizierbar) | ja |
| 5 | Vereinigung Lohnunternehmer Österreich, VLÖ (H20 / B20) | ROT (Jey-Entscheidung Verbände) | außerhalb Tabelle D (E2-nah) | nein |
| 6 | Vitan GmbH (H23 / 325) | GELB (Empfehlung Ausschluss) | 6 | nein |
| 7 | VLV - Verband landw. Veredelungsproduzenten (H23 / 380) | ROT (Jey-Entscheidung Verbände) | außerhalb Tabelle D (E2-nah) | nein |
| 8 | Vogelsang Austria GmbH (H18 / 190) | ROT (Jey-Entscheidung CRM-Name) | formal 3, per Jey-Vorgabe raus | nein |
| 9 | Voran Maschinen GmbH (H22 / C20) | GELB | 5 | ja |
| 10 | Vredestein Tyres (H18 / 300) | GELB (Rot-Kandidat E3) | 2 (Identität/Land), Verguss Niedrig | nein |

Zahlen: Grün 0, Gelb 6, Rot 4 (alle 4 Rot beruhen auf Entscheidungen von Jey, nicht auf Tabelle-E-Belegen).
Hinweis zu Rot: Nach Tabelle D ist Rot nur bei E1 bis E5 mit Stufe V möglich. Die vier Rot-Fälle (3, 5, 7, 8) folgen ausdrücklich der Vorgabe von Jey (Verbände, Biotech/Saatgut, ähnlicher Name im CRM raus). Sie sind keine Aussage "Beleg erbracht"; Jey kann sie umstoßen.

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet, DEPATISnet nicht direkt abfragbar. Eigene Websuche je 1 Abfrage nur für Urban, Vakutec (Impressum/Produktion, kein Patentbezug) und Voran; keine eigene Patentsuche für Valibiotics, Ventura, VLÖ, Vitan, VLV, Vogelsang, Vredestein. Feld 9 ist damit bei allen 10 Firmen ohne Datenbankabfrage nach F5 UNVOLLSTÄNDIG (auch Toms Batch). Nachholen im Browser nötig, bei Urban, Vakutec, Voran Pflicht vor Mailstufe. "Keine Treffer" ist kein Gegenbeweis. Wettbewerbereinsatz (F6): Grep auf wettbewerber_referenzen.md mit urban, vakutec, voran, vogelsang, ventura, vredestein, apollo, vitan, valibio: kein Treffer; keine Einzelsuchen mit Wettbewerbernamen. Messe-Signal: laut Tom kein E1-Wettbewerber unter den DE/AT/NL-Ausstellern (von mir nicht wiederholt), ohne Einfluss auf Ampel.
Aussteller-Namen gegen agraria_2026_aussteller_DE-AT-NL.csv: siehe Abschnitt Einschränkungen.

---

## 1. Urban GmbH & Co. KG | Halle 23, Stand 225
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität/Land abweichend; danach vermutlich Zeile 4).** Gebiet: Rest Deutschland+Niederlande (Hude/Wüsting, Niedersachsen), Messeliste führt AT. Nach Regel O ist bei Abweichung zur Vorgabe höchstens Gelb, bis Jey die Firma bestätigt. Gerätebauer mit erkennbarem Standort (Sitzregel A erfüllbar), Verguss Hoch (A: Magnetventile, Pumpenantriebe, Sensorik, Steuerelektronik im Stallklima, UV-C-Lampenmodule; Endprodukt-Regel). Kein CRM-Treffer, neu.
- Eigene Prüfung (S): Meine Suche bestätigt Auf der Striepe 9, 27798 Hude, Gründung 1984 in Wüsting, "develops, manufactures and markets its products" dort; Geschäftsführer Helmut Urban und Joshua Hirneiß (Pressemitteilung EuroTier 2024, Snippet). Eigenentwicklung computergesteuerter Kälbertränkeautomaten, Produktlinie Alma Pro. Rechtsform "GmbH & Co. KG" passt zur Messeliste und spricht gegen eine Verwechslung mit der österreichischen Urban GmbH (Maria Anzbach), ist aber kein Beleg. Die Messeliste-Länderangabe AT ist vermutlich Eintragungsfehler (Vermutung, ?).
- Patent: 1 eigene Abfrage (Urban Hude Wüsting Patent Tränkeautomat): kein Patent der Firma; nur fremde Tränkeautomat-Patente (Forster, Engen, 1980er; Suevia). Bestätigt Toms schwachen Negativbefund, aber ohne Datenbankabfrage und ohne Anmelder-Varianten (Helmut Urban, "Urban Tierzucht" u. a.). F5 offen.
- Korrekturen an Toms Feldern: Feld 4: Wort "Fertigung" stützt sich nur auf Snippet-Eigenaussage (S); Toms Einstufung "interessant" nicht bestätigt (nur S/A, Regel I verlangt Browser-Gegenlesen). Feld 17: Messeliste-Land bleibt Abweichung. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Ist die Messefirma die Urban GmbH & Co. KG, Hude (HRB 3252 AG Oldenburg) und nicht die AT-Urban GmbH? Wo: Ausstellerprofil agraria.at (Adresse, Website), Impressum urbanonline.de, Handelsregister. (b) Fertigung in Wüsting mit V belegen (Über-uns-Seite oder Stellenanzeige Montage/Elektronik). (c) Patent-/Gebrauchsmustersuche Espacenet/DEPATISnet mit Anmelder-Varianten inkl. "Helmut Urban". (d) Welche Bauteile werden vergossen/verklebt (Datenblatt Alma Pro). Aktion: nicht kontaktieren; bei Bestätigung Grün erwartbar, hohe Priorität.
- Nicht verwendbare Aussagen: Fertigung Wüsting (S/A); Verguss aller Bauteile (A); Mitarbeiterzahl (S); Patentnegativbefund; Länderzuordnung. Stichprobe für Jey: ja.

## 2. Vakutec | Halle 20, Stand C40
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität; nach Klärung Zeile 4 möglich, Verguss aber unsicher).** Messeliste nennt nur "Vakutec". Gefunden: Vakutec Gülletechnik GmbH, Pernsteinerstraße 14, 4542 Nußbach (landwirt.com-Händlerseite, S). Meine Suche bringt neu: Website vakutec.at (Händlerinserat, S) und Eigenbeschreibung "Mit unserem Firmensitz mitten in Österreich produzieren wir kundennah Gülletechnik" (S, Quelle ein Inserat/Snippet, nicht gelesen); Inserate nennen "Österreichischen Hersteller". Das stützt Sitzregel A (Gerätebauer, ein Standort), ist aber nicht V. Verguss: Vakuumfass ist überwiegend Mechanik/Hydraulik; Hoch/Mittel hängt allein von verbauter Sensorik/Elektrohydraulik/Bedienterminal ab (A, nicht belegt), daher nur Mittel (A, schwach). CRM: kein Treffer, neu.
- Patent: meine Suche brachte keine Patentabfrage (nur Impressums-/Produktsuche). Toms 1 Abfrage ohne Treffer bleibt; F5 offen.
- Korrekturen: Feld 5 (Website) ergänzt: vakutec.at (S). Feld 4: Eigenproduktion als Eigenaussage in Snippet (S), nicht nur Händlerinserat. Tom "prüfenswert" passt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Ist die Messefirma "Vakutec" = Vakutec Gülletechnik GmbH, Nußbach (Firmenbuch, Impressum vakutec.at, Ausstellerprofil agraria.at)? (b) Fertigung Nußbach mit V (Über-uns-Seite "produzieren wir kundennah", Stellenanzeige Montage/Schweißer). (c) Welche Elektrik/Elektronik ist verbaut (Füllstandsensor, Magnetventile, Bedienterminal; Datenblatt VA-Serie)? Ohne verbaute Elektronik Verguss eher Niedrig, dann Zeile 6. (d) Patente Espacenet/DEPATISnet nachholen. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Nußbach (S/A); Verguss (A); Identität Kurzname. Stichprobe für Jey: ja.

## 3. Valibiotics GmbH | Halle 23, Stand 470
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT, aber nur als Entscheidung von Jey (Biotech/Saatgutbehandlung raus), nicht als Tabelle-E-Beleg.** Biostimulanzien für Boden/Blatt und Saatgutbehandlung (S), kein Demak-Bereich, Verguss Niedrig (A). Nach reiner Tabelle D wäre es Zeile 6/7 Gelb. CRM: kein Treffer, neu. Keine eigene Websuche (Biotech, Aufwand nach Priorität nicht gerechtfertigt).
- Korrekturen: keine. Patente WO2021037314 / EP4021186 / US 18/031,793 von Tom nicht nachgeprüft; ohne Verguss-Bezug, irrelevant für die Ampel. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: nicht nötig (Rot). Falls Jey die Entscheidung zurücknimmt: Produkte/Verpackungsabfüllung klären.
- Nicht verwendbare Aussagen: Fertigung Traiskirchen (S); Verguss (A). Stichprobe für Jey: nein.

## 4. Ventura | Halle 24, Stand 110
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Firma nicht identifizierbar).** Nur Messelisten-Kurzname und Beschreibung "Milchwirtschaft, -abfüllgeräte, -kühlanlagen" (S). Toms drei Suchen ohne Treffer; von mir nicht wiederholt (Rest-Suchbudget auf Urban/Vakutec/Voran gelegt). Hersteller oder Händler offen, daher kein E2-Rot. CRM: kein Treffer, neu. Mögliche Verwechslung mit anderen Ventura-Firmen ausgeschlossen, da nichts zugeordnet.
- Korrekturen: Toms Einstufung "unwahrscheinlich" nicht belegt (Identität offen); Verguss Mittel (A) nur unter Herstellervorbehalt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer ist "Ventura" (Rechtsform, Sitz, Website)? Wo: Ausstellerprofil agraria.at (Browser), Firmenbuch, WKO-Firmen A-Z, Suchbegriffe "Ventura Milchkühlung/Milchtank/Abfüllanlage Österreich". Danach Hersteller/Händler klären; Händler ohne Fertigung = Rot nach E2 mit URL. Aktion: nicht kontaktieren; bei Nichtauffinden Frage an Jey ("braucht Mensch").
- Nicht verwendbare Aussagen: alle (S/A/?). Stichprobe für Jey: ja.

## 5. Vereinigung Lohnunternehmer Österreich (VLÖ) | Halle 20, Stand B20
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT, Entscheidung von Jey (Verbände raus); inhaltlich E2-nah (Organisation ohne Fertigung), aber nicht mit V belegt.** Messeliste: "Vereine, Verbände, ARGE, Organisationen; Beratung/Information" (S). CRM: kein Treffer, neu. Keine eigene Websuche (Verband).
- Korrekturen: keine. Feld 9 bei Tom formal unvollständig, für Verband ohne Belang. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: nicht nötig.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 6. Vitan GmbH | Halle 23, Stand 325
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6, Fertigung S, Verguss Niedrig); Empfehlung: Ausschluss.** Spezialfutter/Mineralleckstein, Grödig (FN 52712v, S): kein Demak-Bereich, Verguss Niedrig (A). Futter ist nicht ausdrücklich in Jeys Ausschlussliste (Verbände/Prüfdienstleister/Forschung/Saatgut/Medien), daher nach Tabelle Gelb statt Rot. CRM: kein Treffer, neu. Keine eigene Websuche.
- Korrekturen: Feld 7 "Hoch (S)" für Fertigung ist für die Ampel irrelevant. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Jey bestätigt, dass Futtermittelhersteller ausgeschlossen werden; andernfalls prüfen, ob Messelisten-Zusatzprodukte (Schädlingsbekämpfung, Geräte) Bauteile mit Verguss enthalten (Ausstellerprofil agraria.at). Aktion: nicht kontaktieren, keine weitere Recherche ohne Jeys Freigabe.
- Nicht verwendbare Aussagen: Fertigung Grödig (S); Verguss (A). Stichprobe für Jey: nein.

## 7. VLV - Verband landwirtschaftlicher Veredelungsproduzenten | Halle 23, Stand 380
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT, Entscheidung von Jey (Verbände raus); E2-nah, nicht mit V belegt.** Nur Messelisteneintrag "Beratung/Information" (S), Sitz und Rechtsform unbekannt. CRM: kein Treffer, neu.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: nicht nötig.
- Nicht verwendbare Aussagen: alle (S/?). Stichprobe für Jey: nein.

## 8. Vogelsang Austria GmbH | Halle 18, Stand 190
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT, Entscheidung von Jey (Firma mit sehr ähnlichem Namen im CRM); formal nach Tabelle D und Regel M wäre es Zeile 3 (Gelb, Einheit klären).** crm_abgleich.py bestätigt: "Vogelsang GmbH & Co. KG" IDENTISCH mit bekannte_firmen_DE-AT-NL.txt Zeile 2505 [DE] (Konzern, Essen/Oldenburg); "Vogelsang Austria GmbH" PRAEFIX auf dieselbe Zeile; "Vogelsang Elektromotoren GmbH" (Zeile 2504) Wortwurzel, vermutlich andere Firma, nicht geklärt. Die AT-Einheit (Pyhra, FN 399349d, Gründung 2013 "to better support the Austrian customers locally", S) ist laut Tom Vertriebs-/Servicegesellschaft; das wäre zusätzlich E2-nah, aber nicht V. BEKANNT über Konzern.
- Korrekturen: Toms Vermerk "BEKANNT" bestätigt, Rot-Grund ist Jeys Namensregel, nicht E5 (andere juristische Einheit). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag: nicht nötig. Falls Jey die AT-Einheit separat will: Firmenbuchauszug Pyhra, Konzernstruktur (Gesellschafter, Fertigung Konzern Deutschland), Klärung zu "Vogelsang Elektromotoren" im CRM.
- Nicht verwendbare Aussagen: Vertriebsrolle (S), Verguss Mittel (A), Konzernfertigung DE (?). Stichprobe für Jey: nein.

## 9. Voran Maschinen GmbH | Halle 22, Stand C20
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Fertigungsbeleg fehlt; Sitzregel nicht sicher anwendbar).** Gebiet Österreich (Pichl bei Wels). Mein Gegencheck: Advantage Austria (Snippet) bestätigt Inn 7, 4632 Pichl bei Wels und Leistungsspektrum "Maschinenbau, Anlagenbau, Lohnfertigung, Fassadenbau"; TechPilot-Profil beschreibt die Firma als Lohnfertiger in Blech- und Schweißtechnik (S). Dieser Auftragsfertiger-Hinweis (Sitzregel: bei Auftragsfertigern Stufe V nötig) und die Spanne Anlagenbau/Fassade machen Stufe A für die Eigenprodukt-Fertigung unsicher; Fertigung Pichl selbst ist plausibel (160 Mitarbeiter, S). E1: kein Bau von Dosier-/Vergussanlagen gefunden (Obstmühlen, Pressen, Silos, Anlagen), Anlagenbauer bleibt nach Jey drin. Verguss Mittel (A: zugekaufte Motoren, Näherungssensoren, Steuerschrank; Endprodukt-Regel). CRM: "Voran Maschinen", "Voran": kein Treffer, neu.
- Patent: 1 eigene Abfrage (voran Maschinen Pichl Patent Gebrauchsmuster): keine Anmeldung der Firma, nur Händler-/Verzeichnisseiten und Behördenseiten; Negativbefund ohne Datenbank, F5 offen.
- Korrekturen an Toms Feldern: Feld 7 von Tom "Hoch S" (Sitzregel) ist nur bei Eigenproduktgerätebauer tragfähig; Hinweis Lohnfertiger neu. Toms Aussage "Pettenbach nicht genannt, keine Sitzabweichung" nicht nachprüfbar. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Fertigt voran in Pichl eigene Maschinen (Mühlen, Pressen) und welcher Anteil ist Lohnfertigung (voran.at "Über uns"/Produktion, Impressum, Stellenanzeigen Schlosser/Elektriker/Montage Pichl) mit V belegen. (b) Welche Elektrik/Sensorik/Schaltschränke werden verbaut oder selbst gebaut (Datenblätter RM/WALC/WAR). (c) Patente Espacenet/DEPATISnet. (d) Wirklich keine Dosier-/Vergussanlagen im Programm (E1) per Produktkatalog. Aktion: nicht kontaktieren; bei Beleg Grün erwartbar, mittlere Priorität.
- Nicht verwendbare Aussagen: Fertigung Pichl (S); Mitarbeiterzahl (S); Verguss (A); Patentnegativbefund. Stichprobe für Jey: ja (Lohnfertiger vs. Gerätebauer).

## 10. Vredestein Tyres | Halle 18, Stand 300
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität/Land; Rot-Kandidat E3 und Verguss Niedrig).** Messeliste AT, Tom findet Apollo Vredestein B.V., Enschede (NL), Konzern Apollo Tyres (Indien); Werk Enschede laut Eurofound-Meldung Schließung "around the summer of 2026", Verlagerung nach Ungarn/Indien (S, Stand nicht geprüft). Reifen = Verguss Niedrig (A). Rot nach E3 würde V für die Fertigung außerhalb DE/AT/NL erfordern; nicht vorhanden. CRM: "Vredestein Tyres", "Apollo Vredestein", "Apollo Tyres", "Apollo": kein Treffer, neu; kein Konzernbezug. Keine eigene Websuche.
- Korrekturen: keine; Toms Aktion "nicht weiterverfolgen" fachlich nachvollziehbar. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Welche Einheit stellt auf der agraria aus (Ausstellerprofil agraria.at, Adresse)? (b) Wurde Enschede geschlossen (aktuelle Quelle 2026)? Bei V-Beleg Fertigung nur außerhalb DE/AT/NL: Rot nach E3 mit URL; Verguss ohnehin Niedrig. Aktion: nicht kontaktieren; geringe Priorität, Jey kann direkt ausschließen.
- Nicht verwendbare Aussagen: Werkschließung/Verlagerung (S); Verguss (A). Stichprobe für Jey: nein.

---

## Einschränkungen
- Nur WebSearch (3 Abfragen: Urban Patent, Vakutec Impressum/Produktion, Voran Patent) und Bash/Python; WebFetch und Chrome nicht genutzt, keine Seite selbst gelesen. Alle Aussagen aus Snippets (S); Browser nicht verfügbar, daher keine Stufe V und keine Zitatbestätigung.
- Nicht durchgeführte Suchen (offen): Patent-/Anmeldersuche in Google Patents, Espacenet, DEPATISnet bei ALLEN 10 Firmen (inkl. Anmelder-Varianten Helmut Urban, Vogelsang-Konzern, Apollo Tyres); Rechtsstand nirgends geprüft. Keine Websuche zu Valibiotics, Ventura, VLÖ, Vitan, VLV, Vogelsang, Vredestein (CRM + Einordnung nach Auftrag). Keine Einzelsuchen zu Wettbewerbereinsatz (nur Grep auf wettbewerber_referenzen.md).
- Der Aussteller-Namensabgleich gegen agraria-2026/agraria_2026_aussteller_DE-AT-NL.csv wurde in diesem Lauf nicht neu ausgeführt; Namen stammen aus Toms Datei.
- Identität: Urban, Vakutec, Ventura, Vredestein offen (siehe Aufträge). Firmenbuchdaten aus Aggregatoren und Snippets.
- Alle Ampeln vorläufig. Rot bei 3, 5, 7, 8 folgt Entscheidungen von Jey, nicht Tabelle E. Es wird nichts verschickt und kein CRM-Feld geändert. Keine Kontaktsuche (Regel K).
- Priorität für Nachrecherche im Browser: Urban (Identität, Fertigung, Patente), Voran (Lohnfertiger-Frage), Vakutec (Elektrik verbaut?), dann Ventura.
