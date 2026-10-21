# Tina Batch 62 - electronica 2026 (Prüfung von tom_batch_62.md)
Erstellt: 2026-10-21 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich electronica/ergebnisse/tom_batch_62.md (10 Firmen, Nr. 698 bis 707 der Messeliste, hier Nr. 1 bis 10).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (11 Abfragen, Kurzfassungen/Snippets) und Bash zur Verfügung; WebFetch/Chrome nicht vorhanden. Es gibt in diesem Batch KEINE Stufe-V-Aussage. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Nichts davon ist mailtauglich.
Skripte: `python3 crm_abgleich.py` für alle Firmen samt Alt-/Konzern-/Schwesternamen selbst wiederholt. Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum: 2026-10-21.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | X-FAB (C3.121) | GELB | 5 | nein |
| 2 | Yamaichi Electronics Deutschland GmbH (A3.321) | ROT (vorläufig, E5) | 1 | ja |
| 3 | Yokogawa Deutschland GmbH Test&Measurement (A4.117) | GELB | 5 | ja |
| 4 | Carl Zeiss Microscopy (B1.618) | GELB | 3 | ja |
| 5 | Carl Zeiss Digital Innovation GmbH (B1.740) | GELB (Rot-Kandidat E2) | 3 | nein |
| 6 | Zentel EMEA (C4.119) | GELB | 2 | ja |
| 7 | Zerode Kühlkörper (B3.334) | GELB | 2 | ja |
| 8 | ZETTLER GROUP (A3.419) | GELB (Rot-Kandidat E2/E3) | 5 | nein |
| 9 | ZILLKON Zillgitt GmbH Kontaktfedern (B3.263) | GELB | 6 | nein |
| 10 | Zillner electronics GmbH (C3.358) | GELB (Rot-Kandidat E2) | 5 | nein |

Zahlen: Grün 0, Gelb 9, Rot 1 (vorläufig).

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Eigene Patent-Websuchen (Anmelder plus Stichwort) nur für Yamaichi, Carl Zeiss Microscopy, ZETTLER und X-FAB (je 1 Abfrage, zusätzlich zu Toms Abfragen, die ich weder übernehme noch widerlege). Für Yokogawa, Zeiss Digital, Zentel, Zerode, ZILLKON, Zillner keine eigene Patentsuche: Feld 9 ist nach F5 bei Zentel, Zerode, ZILLKON, Zillner (Tom: keine Abfrage) und bei allen übrigen ohne Datenbankabfrage UNVOLLSTÄNDIG. Der Batch ist insgesamt UNVOLLSTÄNDIG (auch Tom hat es gemeldet). "Keine Treffer" ist kein Gegenbeweis. Wettbewerbereinsatz (F6): Grep auf wettbewerber_referenzen.md mit X-FAB, Yamaichi, Yokogawa, Zeiss, Zentel, Zerode, Zettler, Zillkon, Zillgitt, Zillner, Powerchip: kein Treffer; keine Einzelsuchen mit Wettbewerbernamen von mir. Messe-Signal (bdtronic, ELANTAS, RAMPF stellen aus) von Tom übernommen, ohne Einfluss. Aussteller-Schreibweisen aller zehn Firmen per Grep in electronica/aussteller_namen.txt bestätigt (Zeilen 699, 701, 702 u. a.).

---

## 1. X-FAB | C3.121
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Fertigungsbeleg fehlt).** Zeile 1 nein (kein E-Beleg), 2 nein, 3 nein: crm_abgleich.py "X-FAB", "X-FAB Silicon Foundries", "X-FAB MEMS Foundry": kein Treffer, neu. Zeile 4 scheitert, weil Verguss Niedrig (Wafer/MEMS-Chip, A) und die Fertigung bei einem Konzern mit mehreren Werken nur Stufe S hat (Sitzregel greift nicht). Zeile 5 trifft.
- Eigene Prüfung: Patentabfrage (Anmelder "X-FAB Semiconductor Foundries" OR "X-FAB MEMS Foundry" plus encapsulation/potting/adhesive): kein Treffer mit X-FAB als Anmelder, nur fremde Sensor-Packaging-Patente (z. B. EP2722660B1, US7563652B2, Anmelder nicht erkennbar, nicht zugeordnet). Das bestätigt Toms "0 zuordenbar", ist aber kein Datenbankergebnis.
- Korrekturen an Toms Feldern: keine. Tom-Einstufung "unwahrscheinlich" nachvollziehbar. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Welche Gesellschaft fertigt in Erfurt (Impressum, Handelsregister Jena/Erfurt, xfab.com Standortseite lesen)? (b) Gibt es am Standort Packaging-/Gehäuseschritte mit Verguss oder Kleben (Produktseite MEMS, Stellenanzeigen Erfurt)? Niedrige Priorität, vermutlich kein Ziel. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Erfurt (S); Verguss Niedrig (A); Konzernstruktur (S). Stichprobe für Jey: nein.

## 2. Yamaichi Electronics Deutschland GmbH | A3.321
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT, vorläufig (Tabellenzeile 1, E5: Firma im CRM).** crm_abgleich.py "Yamaichi Electronics Deutschland", "Yamaichi Electronics", "Yamaichi": bekannte_firmen_DE-AT-NL.txt Zeile 2634 "Yamaichi [DE]" (IDENTISCH für "Yamaichi", PRAEFIX für die längeren Namen); kundendatenbank_export.txt kein Treffer. Nach B2 ist das eine eindeutige Kurzform mit gleicher Wortwurzel (Kern-Name 'yamaichi', Länder-Kennung DE, die einzige deutsche Yamaichi-Gesellschaft ist die Aschheimer GmbH), also BEKANNT; Rot nach E5 wegen Bestandskontakt, nicht Neukunde.
- Eigene Prüfung: Suche bestätigt Adresse Bahnhofstraße 20, 85609 Aschheim (Dornach) (elektroniknet-Anbieterkompass, yamaichi.de/contact-us/germany; S) und Fertigung von Steckverbindern und Kabelkonfektion in Frankfurt (Oder) seit 2006 (Broschüre, S, 2018 bis 2020). Handelsregister nicht gefunden. Patente: Abfrage Google Patents-Stil (Anmelder Yamaichi Electronics Deutschland plus sealing/overmold/encapsulation): kein Yamaichi-Patent zu Verguss/Überspritzung; ipqwery listet 22 Datensätze, davon 16 Patente, ein flat connector 2025 (Nr. und Rechtsstand nicht ausgelesen). Nur Pressemeldung zum überspritzten Knickschutz (Y-Circ P, S). Entscheidend ist hier das CRM, nicht die Produktlage; ohne den CRM-Treffer wäre sie Gelb (Zeile 5, Konzern, Fertigung S) mit Verguss Hoch (A).
- Korrekturen an Toms Feldern: Feld 12 "bekannt" bestätigt; Toms Ausgabe ließ die Ampel offen (Gelb-Auftrag a), ich entscheide Rot, weil die einzige deutsche Gesellschaft gleichen Kern-Namens betroffen ist. Zitat im Browser bestätigt: nein.
- Nachrecherche (Bestätigung, kein Gelb): Jey bestätigt, dass CRM "Yamaichi" die Aschheimer GmbH meint (nicht nur Japan-/Gruppen-Kontakt). Steht die CRM-Zeile für eine andere Einheit (z. B. Yamaichi Electronics Co.), wird die Ampel Gelb, Zeile 3, Auftrag "Einheit klären". Aktion: Bestandskontakt pflegen, nicht neu ansprechen.
- Nicht verwendbare Aussagen: Fertigung Frankfurt (Oder) (S, Quellen 2018 bis 2020); Verguss Hoch (A); Patente. Stichprobe für Jey: ja (CRM-Einheit).

## 3. Yokogawa Deutschland GmbH Test&Measurement | A4.117
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Fertigungsbeleg fehlt/widersprüchlich).** crm_abgleich.py "Yokogawa Deutschland", "Yokogawa Electric", "Yokogawa Test&Measurement", "Yokogawa-nbn", "nbn Elektronik", "Rota Yokogawa", "Yokogawa": kein Treffer (nur ähnlich 0.90 "Eben Elektronik GmbH" für "nbn Elektronik", erkennbar andere Firma). Damit sind Toms offene Alt-/Schwesternamen nachgeholt: neu. Konzern mit mehreren Werken, Sitzregel greift nicht.
- Eigene Prüfung: Suche bestätigt (S) Meilhaus-Pressemeldung 2018 "Messtechnik aus eigener Produktion" am Standort Herrsching und die Karrierezeile "Entwicklung | Produktion | Direktvertrieb" (daa-technikum, Fassungen 2021 und 2026), aber auch die Stellenanzeige 2026 für einen Servicetechniker im "Vertriebs- und Servicecenter" Herrsching (Reparatur und Kalibrierung); keine Montage-/Produktionsstelle gefunden. Der Widerspruch bleibt, welche Geräte (falls überhaupt) in Herrsching gebaut werden. Eigene Patentsuche: keine (Budget); Tom fand 0 zuordenbare. Rota Yokogawa (Wehr) wäre eine andere Einheit und ist nicht Teil der Vorgabe.
- Korrekturen: Feld 12 (Altnamen) nachgeholt, kein Treffer. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Welche Produkte fertigt Herrsching heute selbst (nicht nur Vertrieb/Service/Kalibrierung)? Yokogawa-Seite Test&Measurement "Über uns"/Standort Herrsching, Impressum und aktuelle Stellenanzeigen Produktion/Montage im Browser lesen. Bei nur Service/Vertrieb: Rot nach E2 mit URL. Dazu Patentsuche (Anmelder Yokogawa Electric Corp., Rota Yokogawa, Stichwort Vergussmasse/Dichtung) in Google Patents/Espacenet. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Herrsching (S, 2018); Verguss Mittel (A). Stichprobe für Jey: ja (Rot oder Gelb offen).

## 4. Carl Zeiss Microscopy | B1.618
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 3, CRM-Konzernbezug; zugleich Zeile 2 Identität offen).** crm_abgleich.py "Carl Zeiss Microscopy", "Carl Zeiss AG", "Carl Zeiss", "ZEISS GROUP": IDENTISCH Zeile 383 "Carl Zeiss AG" [DE], PRAEFIX Zeile 384 "Carl Zeiss Jena GmbH" [DE], IDENTISCH Zeile 2645 "ZEISS GROUP" [DE]; kundendatenbank_export.txt kein Treffer. Konzernbezug bestätigt, Einheit unklar. Die erste zutreffende Tabellenzeile ist 2 (Identität: Vorgabe ohne Rechtsform, Oberkochen vs. Jena), die Wirkung ist gleich (Gelb); ich führe Zeile 3 als tragend, Zeile 2 als Zusatzauftrag.
- Eigene Prüfung: Suche zur Fertigung bestätigt nur Historie (Jena, Oberkochen) und eine Jenaer Stellenanzeige für "ZEISS Research Microscopy Solutions" (S); welche Mikroskope wo gebaut werden, bleibt offen (Tom-Aussage Fertigung Mittel S korrekt). Patente: Abfrage (Anmelder "Carl Zeiss Microscopy GmbH" plus encapsulation/potting/adhesive/sealing): kein Patent dieses Anmelders gefunden; Treffer fremde Vergusspatente (z. B. US9622372, US12055558, Anmelder nicht erkennbar, nicht zugeordnet). Damit ist Toms Befund gestützt, Rechtsstand nicht geprüft. Verguss Hoch (A) für LED-Beleuchtung/Netzteile bleibt Produkttyp-Ableitung, Medizin-/Labortechnik-Regel spricht für Verguss.
- Korrekturen an Toms Feldern: keine. Tom-Einstufung "prüfenswert" bestätigt, nicht höher (Fertigung S). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 3): (a) Jey/Tina: Welche Einheit meint CRM "Carl Zeiss AG"/"Carl Zeiss Jena GmbH"/"ZEISS GROUP", und ist die Carl Zeiss Microscopy GmbH (Jena) bzw. Carl Zeiss Microscopy Deutschland GmbH (Oberkochen) dieselbe Einheit oder eine Schwester (Impressum, Handelsregister Jena und Aalen, CRM-Datensatz)? (b) Welche Mikroskope fertigt Oberkochen/Jena, mit Beleg V (Standortseite zeiss.com/microscopy, Stellenanzeigen Montage)? (c) Patentsuche Google Patents/Espacenet nachholen (Anmelder Carl Zeiss Microscopy GmbH, Carl Zeiss AG, Carl Zeiss Jena). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung (S); alle Bauteil-Verguss-Bewertungen (A); Konzernstruktur (S). Stichprobe für Jey: ja (CRM-Einheit, Konzernfall).

## 5. Carl Zeiss Digital Innovation GmbH | B1.740
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 3, CRM-Konzernbezug; Rot-Kandidat E2).** crm_abgleich.py "Carl Zeiss Digital Innovation", "Carl Zeiss AG", "Saxonia Systems": PRAEFIX Zeile 383 "Carl Zeiss AG", Zeile 384 "Carl Zeiss Jena GmbH"; "Saxonia Systems" kein Treffer. Zeile 1 verlangt E2 mit Stufe V; Tom hat Software/Beratung nur als S (Pressemeldung 2020, Impressum-Treffer). Vor Zeile 4 oder E2-Rot steht also Zeile 3.
- Eigene Prüfung: keine eigene Suche (Budget, offensichtlich Softwareeinheit); Toms Angaben nicht widerlegt, aber nicht gelesen.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 3): Impressum/Leistungsseite zeiss.com/digital-innovation im Browser lesen, Zitat "Software/Beratung, keine Hardwarefertigung" als V sichern (E2), danach Rot mit URL; zugleich klären, ob CRM "Carl Zeiss AG" diese Einheit mitmeint (Jey). Aktion: nicht weiter verfolgen.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 6. Zentel EMEA | C4.119
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** crm_abgleich.py "Zentel EMEA", "Zentel", "Zentel Electronics", "Powerchip": kein Treffer, neu (Powerchip-Konzernabgleich nachgeholt).
- Eigene Prüfung: Suche "Zentel EMEA GmbH Schöngeising Impressum Handelsregister" fand keinen Eintrag zur Firma (nur fremde OpenRegister-Seiten, aussortiert). Die Gesellschaft in Schöngeising ist damit weiter unbelegt. Fabless-Modell nur aus Toms S-Quelle. Keine Patentsuche (nicht ausgeführt, Feld 9 offen).
- Korrekturen: Tom-Einstufung "kein Fertiger" ist ohne V kein Rot (E2 verlangt Stufe V). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Existiert "Zentel EMEA" als Gesellschaft in 82296 Schöngeising (Messeprofil exhibitors.electronica.de lesen, Handelsregister München, Impressum der Zentel-Europe-Website)? Fertigt sie dort oder nur Vertrieb? Bei Vertrieb ohne Fertigung: Rot nach E2/E3 mit URL. Patentsuche nachholen (Anmelder Zentel Electronics Corp., Stichwort encapsulation). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/A/?). Stichprobe für Jey: ja (Firma nicht identifizierbar).

## 7. Zerode Kühlkörper | B3.334
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** crm_abgleich.py "Zerode Kühlkörper", "Zerode": kein Treffer, neu.
- Eigene Prüfung: Suche "Zerode Kühlkörper Stuttgart electronica 2026 Aussteller" ergibt keinen Hinweis auf die Firma (das Ausstellerverzeichnis wurde nicht durchsucht; die Aussteller-Namensdatei electronica/aussteller_namen.txt führt den Eintrag, Quelle S). Firma bleibt damit, wie bei Tom, nicht auffindbar; Schreibvariante oder Marke möglich. Keine Patentsuche.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Aussteller-Detailseite exhibitors.electronica.de (Name, Adresse 70565 Stuttgart, Website, Produktgruppen) im Browser lesen; Handelsregister Stuttgart und Schreibvarianten (Zerode, Z-Erode, Zerode GmbH) prüfen. Danach Fertigung und Wärmeleitverklebung klären. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (?). Stichprobe für Jey: ja (Firma nicht identifizierbar).

## 8. ZETTLER GROUP | A3.419
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Fertigung in DE/AT/NL nicht belegt; Rot-Kandidat E2/E3).** crm_abgleich.py "ZETTLER GROUP", "Zettler Electronics", "American Zettler", "Zettler": kein Treffer, neu. E2/E3 sind nur Stufe S (Ausstellerprofil, nach Regel N5 nie V), daher nicht Rot.
- Eigene Prüfung: Suche bestätigt (S) Junkersstraße 3, Puchheim, Vertrieb über Distributoren in EMEA, Fertigungsstätten in Asien; keine Produktions- oder Montagestelle in Puchheim gefunden (Stellentreffer nur American Zettler in den USA). Patente: Abfrage (Anmelder Zettler Electronics GmbH / American Zettler plus relay potting): kein Treffer mit Zettler als Anmelder; Treffer EP0118841A3 zitiert ein Zettler-Patent von 1977 (DE2732517, Relaisabdichtung), also historisches Signal für Relais-Verguss, kein aktueller Beleg (Rechtsstand abgelaufen zu vermuten, nicht geprüft). Verguss Hoch (A) bleibt Produkttyp (Relais, Trafos).
- Korrekturen an Toms Feldern: Feld 9 ergänzt um das zitierte Zettler-Altpatent DE2732517 (S, über EP0118841A3). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Gibt es Montage, Konfektion oder Ladesystem-Fertigung in Puchheim oder anderswo in DE/AT/NL (Impressum, Standortseite zettler-group.com, Stellenanzeigen Puchheim im Browser lesen)? Bei reinem Vertrieb: Rot nach E2 mit URL. Patentsuche Google Patents/Espacenet nachholen (Anmelder ZETTLER Electronics GmbH, Zettler Group). Aktion: nicht kontaktieren, solange keine Fertigung belegt.
- Nicht verwendbare Aussagen: Fertigung Asien (S); Relais-/Trafo-Verguss (A); Altpatent (S). Stichprobe für Jey: nein.

## 9. ZILLKON Zillgitt GmbH Kontaktfedern | B3.263
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6, Fertigung belegt, Verguss Niedrig).** crm_abgleich.py "ZILLKON Zillgitt", "Zillkon", "Zillgitt": kein Treffer, neu. Zeile 4 scheitert am Verguss: Kontaktfeder (Metall-Stanz-Biegeteil) Niedrig (A). Fertigung am Sitz: Eigenhersteller mit erkennbarem Standort (Sitzregel, Stufe A; Stanz-/Biege-Einrichter-Anzeige nur S), kein Konzern, daher Fertigung belegt im Sinne von Zeile 6.
- Eigene Prüfung: Suche bestätigt die StepStone-Beschreibung (S): "Hersteller von Kontaktfedern aus Metallen im Dünnblech-Bereich", Einsatz HF-, Medizin-, Lasertechnik, Wachstum durch E-Mobilität; Stanz-Biegeartikel nach Zeichnung. Keine Firmenwebsite, kein Hinweis auf Umspritzung oder Baugruppen. Keine Patentsuche (Feld 9 offen, Tom ebenfalls).
- Korrekturen: Tom-Feld 7 (Hoch, S) und Sitzregel zusammengeführt: Fertigung Hoch, Stufe A (Sitzregel) mit S-Stütze. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Firmenwebsite/Impressum (Domain über Messeprofil) lesen: nur Metallteile, oder auch Baugruppen mit Kunststoff-Umspritzung, Einlegeteile in Steckverbinder, Verguss? Patente nachholen (Anmelder ZILLKON Zillgitt GmbH, Stichwort Kontaktfeder, Umspritzung). Niedrige Priorität. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung (A/S); Verguss Niedrig (A). Stichprobe für Jey: nein.

## 10. Zillner electronics GmbH | C3.358
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5; Rot-Kandidat E2 Händler).** crm_abgleich.py "Zillner electronics", "Zillner": kein Treffer, neu. E2 ist nur Stufe S (Verzeichnis implisense, Handelsregister-Zusammenfassung), daher nicht Rot.
- Eigene Prüfung: keine eigene Suche (Budget); Toms Register-Snippet (HRB 311086 München, Gründung Februar 2026, "Handel und Vertrieb von elektronischen Bauteilen") nicht widerlegt, nicht gelesen. Keine Patentsuche.
- Korrekturen: Tom-Feld 13 verbindlich ergänzt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Handelsregistereintrag HRB 311086 (handelsregister.de/unternehmensregister.de) und Impressum im Browser lesen; Zitat "Handel und Vertrieb ..." als V sichern, dann Rot nach E2 mit URL. Aktion: nicht weiter verfolgen.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind durchgehend ehrlich niedrig angesetzt; keine V-Aussage vorgetäuscht. Seine Einstufungen "kein Fertiger" (Zentel, Zettler, Zillner, Zeiss Digital) sind ohne V keine Rot-Gründe; deshalb Gelb mit Auftrag, jeweils mit "dann Rot nach E2/E3".
- Einzige Ampel-Änderung gegenüber Tom: Yamaichi von offen auf Rot (E5), vorläufig und von Jey zu bestätigen (Einheit).
- Zwei Zeiss-Einheiten (Microscopy, Digital Innovation) hängen am selben CRM-Konzernbezug; eine Entscheidung von Jey zur CRM-Einheit klärt beide.
- Yokogawa: Widerspruch zwischen "eigene Produktion" (2018) und Vertriebs-/Servicecenter (2026) bleibt offen; Tom hat dies korrekt als Widerspruch geführt.
- Kein Grün in diesem Batch; die aussichtsreichsten Kandidaten für eine spätere Aufwertung sind Carl Zeiss Microscopy (bei klarer Einheit und belegtem Werk, Verguss Hoch A) und ggf. Yokogawa (bei belegter Herrschinger Fertigung).
- Vorschlag Fehlerlog (Jey gibt frei, nicht eingetragen): Bei Konzernen mit mehreren Gesellschaften (Zeiss) und Kurzform im CRM (Yamaichi) vor der Recherche die CRM-Einheit mit Jey klären, um doppelte Arbeit zu vermeiden.

## Einschränkungen
- WebFetch und Chrome nicht verfügbar: kein Gegenlesen nach Abschnitt H, keine Impressen, Datenblätter, Karriereseiten oder Register gelesen; alle Aussagen Stufe S, A oder ?. Keine "Zitat im Browser bestätigt: ja", kein Grün, nichts mailtauglich.
- WebSearch: 11 Abfragen (Yamaichi 2, Carl Zeiss Microscopy 2, Yokogawa 1, ZETTLER 2, X-FAB 1, Zerode 1, Zentel 1, ZILLKON 1). Ohne eigene Suche: Zeiss Digital Innovation, Zillner; ohne eigene Patentsuche: Yokogawa, Zeiss Digital, Zentel, Zerode, ZILLKON, Zillner.
- Patente: Pflichtsuche F5 (Google Patents, Espacenet, DEPATISnet) für keine Firma erfüllt; Rechtsstand nirgends geprüft; Batch UNVOLLSTÄNDIG, bevor eine Ampel final wird.
- Wettbewerbereinsatz (F6): nur Listenabgleich und Toms Angaben; "kein Hinweis" ist kein Gegenbeweis.
- Identität: Impressum und Handelsregister bei keiner Firma gelesen. Offene Abweichungen: Zentel EMEA, Zerode, Zeiss Microscopy (Rechtsform/Sitz), Yokogawa (Ratingen vs. Herrsching), ZETTLER (Gruppenname), X-FAB (fertigende Gesellschaft).
- Veraltete Quellen: Yamaichi (2018 bis 2020), Yokogawa Meilhaus (2018), Zeiss Digital (2020).
- Kundendatenbank (xlsx) nicht lesbar; Abgleich per Skript auf Textexporte. Nichts verschickt, keine Datenbankfelder geändert, kein git commit. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
