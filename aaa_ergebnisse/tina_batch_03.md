# Tina Batch 03 – all about automation Düsseldorf 2026 (Prüfung von tom_batch_03.md)
Erstellt: 2026-10-15 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe: ausschließlich aaa_ergebnisse/tom_batch_03.md (10 Firmen).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (20 Abfragen, Snippets/Kurzfassungen) und Bash zur Verfügung; WebFetch und Chrome nicht nutzbar. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist daher überall: nein (nicht möglich). Kein Grün ist mailtauglich.
Skripte: `python3 batch_check.py` = VOLLSTÄNDIG (10 Blöcke; Toms Einschränkung: Patente/Wettbewerber nur über Websuche, Skript erkennt nur die Felder). `python3 crm_abgleich.py` für alle Firmen samt Konzern-, Alt- und Schwesternamen selbst wiederholt (Ergebnis je Firma unten). Tabellenzeile = Zeilennummer der Ampel-Tabelle D.
Verifikationsdatum aller Einträge: 2026-10-15.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel (vorläufig) | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | CETA Testsysteme GmbH (230) | GRÜN | 4 (Sitzregel) | ja |
| 2 | CONTA-CLIP Verbindungstechnik GmbH (224) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 3 | DFS Montageautomation GmbH (414) | GELB | 6 | nein |
| 4 | Dreisbach & Jungmann GmbH & Co. KG (826) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 5 | DSP Systeme GmbH (147) | GELB | 5 | nein |
| 6 | Dussmann Industrial Automation GmbH (513) | GELB | 2 | ja |
| 7 | EFCO Electronics GmbH (211) | GELB | 5 | nein |
| 8 | embedded data GmbH (420) | GELB | 2 | ja |
| 9 | ESCHA GmbH & Co. KG (209) | GELB | 3 | ja |
| 10 | Europascal GmbH (122) | GELB | 7 | ja (Rot-Kandidat E2) |

Zahlen: Grün 3, Gelb 7, Rot 0.

Patente (Prüfpunkt 8, Regel F5): DEPATISnet, Espacenet und Google Patents waren nicht direkt abfragbar. Ich habe je Firma (CETA, CONTA-CLIP, ESCHA, Dreisbach & Jungmann) eine zusätzliche Anmelder-Websuche ausgeführt: keine Patentdatensätze. Für DFS, DSP, Dussmann, EFCO, embedded data, Europascal keine eigene Wiederholung (Budget). Feld 9 bleibt damit bei ALLEN 10 Firmen ohne Direktabfrage der Datenbanken: nicht belastbar, kein Gegenbeweis. Der Batch ist nach F5 UNVOLLSTÄNDIG im Sinne der Datenbankabfrage; Nachholen im Browser nötig, bevor ein Grün final wird. Zugleich Wettbewerbereinsatz (F6): nur für CETA, CONTA-CLIP von Tom gezielt gesucht, bei den übrigen schwach ("kein Hinweis gefunden", ohne Einfluss auf Ampel).

---

## 1. CETA Testsysteme GmbH | Stand 230
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN (Tabellenzeile 4, Fertigung Stufe A nach Sitzregel).** Eigenhersteller von Lecktest-/Durchflussprüfgeräten mit einem Standort in Hilden, kein Konzern, kein Händler; Sensoren, Netzteil und Messelektronik sind typisch vergossen (Hoch, A). Kein Beleg Stufe V, daher Grün nur vorläufig.
- Eigene Prüfung: Websuche bestätigt Adresse Marie-Curie-Straße 35-37, 40721 Hilden und aus Nürnbergmesse-Katalog/Broschüre (S): "Made in Germany" sind Eigenentwicklungen, wichtige Komponenten und Kalibriernormale "in eigener Regie hergestellt"; FACHPACK-Profil nennt "German manufacturer" (S); DAkkS-Kalibrierlabor (S). Das stützt die Sitzregel (Gerätebauer, Hilden), ist aber nur Snippet. Branchen laut Broschüre: Automotive, Medizintechnik, E-Mobility (S).
- Korrekturen an Toms Feldern: keine inhaltlichen. Feld 10 "interessant" nicht bestätigt, weil nur A/S (nach Regel I nur mit Browser-Gegenlesen zu bestätigen); Feld 9: eigene Patentsuche ohne Treffer, weiter nicht belastbar. CRM: crm_abgleich.py "CETA Testsysteme GmbH": kein Treffer, neu.
- Zitat im Browser bestätigt: nein (Browser nicht verfügbar).
- Nachrecherche (kein Gelb, für Mailstufe nötig): Impressum/Register Hilden lesen (Feld 17 V), Stellenanzeige Montage/Elektronik Hilden, Datenblatt cetatest x25 (verbaute Sensoren/Netzteile, Schutzart).
- Nicht verwendbare Aussagen: Fertigung Hilden (A/S); Verguss aller Bauteile (A); "Schlüsselkomponenten im eigenen Haus" (S, Messekatalog); Rechtsform GmbH (S). Stichprobe für Jey: ja (Grün ohne V-Beleg).

## 2. CONTA-CLIP Verbindungstechnik GmbH | Stand 224
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Sitzregel).** Familiengeführter Hersteller mit eigenem Kunststoff-Spritzguss in Hövelhof (Stellenanzeige "Leitung Kunststoff-Spritzguss" laut Suchergebnis, S); Verguss Mittel (A: Hochvolt-/Trafoklemmen, Elektronik-/Leiterplattenklemmen, Gehäuse mit Dichtung "CONTA-BOX"). Eigenverguss nicht belegt.
- Eigene Prüfung: Websuche bestätigt Hövelhof, gegründet 1978, Linien CONTA-CONNECT/-ELECTRONICS/-CON, Gehäuse in Kunststoff/Aluminium (S, DirectIndustry, Katalog-PDF). StepStone-Anzeige "Leitung Spritzgussteam", Betriebsort Hövelhof, Arbeitgeber CONTA-CLIP (S). Ob es weitere Werke gibt (Mehrwerk-Konzern wäre V-pflichtig), ist nicht ausgeschlossen: Tom nennt "mittelständisch, familiengeführt" nur als S.
- Korrekturen: keine. Patent-Zusatzsuche: keine Datensätze (Zufallstreffer AT14902U1 nicht zuzuordnen). CRM: neu.
- Zitat im Browser bestätigt: nein.
- Nachrecherche (empfohlen): Impressum und Standorte conta-clip.com (Ein-Werk-Bestätigung, V); Case Study "Sinus Leistungselektronik" (PDF) und Datenblatt Trafoklemmen lesen (Hinweis auf Verguss/Dichtung); Stellenanzeige im Original.
- Nicht verwendbare Aussagen: Verguss aller Bauteile (A); Spritzguss am Sitz (S); Familienunternehmen/Einwerk (S); Case-Study-Inhalt (nicht gelesen). Stichprobe für Jey: ja (schwächstes Grün: Reihenklemmen selbst kaum vergossen).

## 3. DFS Montageautomation GmbH | Stand 414
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6).** Fertigung Lorsch Hoch (A, Sitzregel), aber alle plausiblen Bauteile Niedrig (Montage-/Fördersysteme aus Standardprofilen, Zukauf-Steuerungen; Wissensbasis Block C). Tom: unwahrscheinlich, bestätigt.
- Identität: Name "DFS Montageautomation GmbH, Industriestr. 6, 64653 Lorsch" in drei unabhängigen Snippets konsistent (aaa-Ausstellerprofil, Implisense, dasoertliche); die Stellenanzeige nennt "DFS Maschinenbau GmbH" (Namensvariante), Register/Impressum nicht gelesen. Ich werte das nicht als Widerspruch (Zeile 2 nicht ausgelöst), aber offen. Kein E2-Beleg (Anlagenbauer, kein Händler).
- Korrekturen: keine. CRM: crm_abgleich.py "DFS Montageautomation GmbH", "DFS Maschinenbau": neu. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Welche Produkte/Bauteile enthalten Dosier-, Klebe-, Dicht- oder Vergussschritte (Referenzprojekte, Kundenanlagen mit Dosierstationen, eigene Schaltschrank-/Elektronikfertigung)? Wo nachsehen: Website der Firma (laut Tom unbestätigte Domain dfs-automation.com; Impressum lesen und zugleich "Maschinenbau/Montageautomation" klären), Referenzen, Stellenanzeigen Elektromonteur. Aktion: nicht priorisieren (Partner-/Integrator-Potenzial).
- Nicht verwendbare Aussagen: Verguss alle Bauteile (A); Fertigung Lorsch (A/S); Domain (unbestätigt). Stichprobe für Jey: nein.

## 4. Dreisbach & Jungmann GmbH & Co. KG | Stand 826
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Sitzregel).** Sondermaschinen-/Ofenbauer mit einem erkennbaren Standort Lüdenscheid (eigene Produkte, kein Händler, kein Konzernhinweis); Heizelemente, Sensorik und Steuer-/Leistungselektronik der Öfen sind typisch vergossen (Mittel, A, auch zugekaufte Teile zählen).
- Eigene Prüfung: Websuche bestätigt Am Drostenstück 31-33, 58507 Lüdenscheid und Tätigkeit "Sondermaschinen, Industrieofenbau/Wärmebehandlung, Automationsanlagen von Zuführung bis Montage/Prüfung" (S, onlinestreet.de). Keine Patente (eigene Zusatzsuche, kein Treffer). Eine Stellenanzeige für Montage wurde nicht gefunden (Suche brachte nur Haushaltsgeräte-Treffer).
- Korrekturen: keine. CRM: crm_abgleich.py "Dreisbach & Jungmann GmbH & Co. KG": neu. Zitat im Browser bestätigt: nein.
- Nachrecherche (empfohlen): Impressum/Standort dreisbach-jungmann.de (V für Sitz = Fertigungsort), Datenblatt Durchlaufofen RFO: Heizelement-Bauart (Heizpatronen/Keramik, Vergussstellen) und Steuerung (Schaltschrank, Fremdlieferant?).
- Nicht verwendbare Aussagen: Verguss aller Bauteile (A); Fertigung Lüdenscheid (S/A); "seit über 30 Jahren" (S, Verzeichnis); Fachartikel RFO (Teaser, Abo-Wand). Stichprobe für Jey: ja (Grün stützt sich auf Sitzregel und Produkttyp, beides A).

## 5. DSP Systeme GmbH | Stand 147
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Fertigung in Düsseldorf nicht belegt (S: Mischform Entwicklungsdienstleister, eigene Module/Modems, Vertrieb von Partnerprodukten); Sitzregel greift nicht sicher. Verguss Mittel (A, OFDM-Modem-Module).
- Eigene Prüfung: Suchergebnis bestätigt Vohwinkelallee 8, 40229 Düsseldorf; Selbstbeschreibung (Verzeichnis, S): "Engineering Services, Hardware und Algorithmen", Lieferung "bestückter und getesteter Baugruppen", ISO 9001:2015, eigene Produkte DSP-Module und OFDM-Modems. "Bestückte und getestete Baugruppen" deuten auf Fertigung oder Fremdbestückung, unentschieden. Name "AR Bayer DSP Systeme GmbH" erscheint beim Analog-Devices-Partnerprofil unter derselben Adresse, daher nur Namensvariante (S). E2 (Design-Haus) nicht belegt, also nicht Rot.
- Korrekturen: keine. CRM: crm_abgleich.py "DSP Systeme GmbH", "AR Bayer DSP Systeme": neu. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Werden die DSP-Module/Modems in Düsseldorf gefertigt/bestückt oder extern (Fertigungsbeleg)? Wo nachsehen: Impressum und Produktseite dsp-sys.de (Datenblatt cOSMo/Socket-Modem: "Made in", Schutzlack/Verguss), Handelsregister Düsseldorf (Identität AR Bayer DSP Systeme GmbH), Stellenanzeigen (Bestücker, Test, Montage).
- Nicht verwendbare Aussagen: Eigenfertigung (S/?); Verguss der Modems (A); Patent des OFDM-Verfahrens (S, Nummer unbekannt, kein Verguss). Stichprobe für Jey: nein.

## 6. Dussmann Industrial Automation GmbH | Stand 513
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Die Vorgabe "Dussmann Industrial Automation GmbH" ist nicht belegt; alle Messeprofile (mehrere aaa-Standorte, S) nennen "Dussmann Elektrotechnik und Automation GmbH", Standorte Göppingen und Essen, "seit 2025 Teil der Dussmann Technical Solutions Division" (Stellenanzeige, S). Dazu: Konzern mit Schaltanlagen-/Schaltschrankbau als Projektgeschäft, Verguss Niedrig (A).
- Eigene Prüfung: Suche nach Impressum ohne Treffer; weiter ohne Register. Messeprofile nennen Schaltschrankbau als Kernkompetenz (S), Fertigungsfläche/Produktion nicht belegt. Konzernabgleich (Regel M) jetzt nachgeholt: crm_abgleich.py "Dussmann Industrial Automation", "Dussmann Elektrotechnik und Automation", "Dussmann Group", "Dussmann Service Deutschland", "Dussmann Technical Solutions": überall kein Treffer, Konzern-CRM-Bezug entfällt (Zeile 3 nicht ausgelöst).
- Korrekturen an Toms Feldern: Feld 12/Konzernabgleich erledigt (neu); Feld 9 Zweitsuche weiterhin offen. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Existiert eine "Dussmann Industrial Automation GmbH" oder ist die ausstellende Gesellschaft ausschließlich die Dussmann Elektrotechnik und Automation GmbH (Sitz Göppingen, PLZ 73037)? Impressum auf dussmann.com/Technical-Solutions-Seite und Handelsregister (Amtsgericht Ulm bzw. Stuttgart) lesen. (b) Ist Schaltschrankbau eigene Werkstattfertigung oder Montage beim Kunden? Falls Dienstleister/Projektmontage ohne eigene Produkte, ist E2 zu prüfen. Aktion: nicht priorisieren.
- Nicht verwendbare Aussagen: Identität der Vorgabe (nicht belegt); Fertigung Göppingen/Essen (S); Verguss (A, Zukaufteile). Stichprobe für Jey: ja (Identität bestätigen).

## 7. EFCO Electronics GmbH | Stand 211
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5; mit Hinweis auf Fertigung im Ausland).** Tochter von EFCO (Everfine Industrial/EFCO Technology, Taipeh). In Deggendorf laut Fachpresse (S) nur "design-in support on site" und Kleinserie kundenspezifischer Computer; Auslieferung "aus der Zentrale in Taiwan". Meine Suche bestätigt: EFCO-Headquarters Taipeh mit "high level assembly production center" (S), keine Quelle für Montage in Deggendorf. Konzern: Stufe V nötig, fehlt. Verguss Mittel (A).
- Eigene Prüfung: crm_abgleich.py "EFCO Electronics GmbH", "EFCO Technology", "EFCO", "Everfine Industrial" (EtherCAT-Mitgliedsname): alle neu. E3 (Fertigung ausschließlich außerhalb DE/AT/NL) ist nicht V-belegt, also nicht Rot.
- Korrekturen: Feld 17 Zusatz: EtherCAT-Eintrag führt den Konzern als "Everfine Industrial (EFCO)" (S). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Werden Geräte in Deggendorf montiert/konfiguriert (Fertigungsbeleg) oder nur aus Taiwan geliefert? Wo nachsehen: Impressum efcotec.de, Stellenanzeigen "Mitarbeiter Montage/Test" der EFCO Electronics GmbH (StepStone-Firmenseite), Produktseiten ("Made in"), ggf. direkte Frage an die Firma. Sonst nach Beleg E3 Rot.
- Nicht verwendbare Aussagen: Fertigung Deggendorf (S/?); Verguss/Display-Bonding (A); "ca. 150 Mitarbeiter" (S, Zuordnung unklar). Stichprobe für Jey: nein.

## 8. embedded data GmbH | Stand 420
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Zwei Standortangaben: Bad Neuenahr-Ahrweiler (automa.net, Messeliste PLZ 53474) gegen Armsheim, HRB 52664 Mainz (Implisense, BuiltWith). Meine Suche bestätigt Armsheim/HRB 52664 und findet keine Quelle für Bad Neuenahr-Ahrweiler; der BuiltWith-Kontakt zeigt eine saarländische Vorwahl (+49 6831), also ein dritter Hinweis ohne Klärung. Produkt nach Profil Industrial-IoT-Software ("david"), Hardware nicht belegt.
- Eigene Prüfung: kein Impressum gefunden. E2 (Software) ist nicht mit Stufe V belegt, daher nicht Rot. Fertigung Niedrig, Verguss Niedrig (alle Bauteile, A/?): Zeile 6 käme erst nach geklärter Identität.
- Korrekturen: Toms Einstufung "kein Fertiger" bleibt vorläufig. CRM: crm_abgleich.py "embedded data GmbH": neu (generischer Name, Abgleich schwach). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Welche Gesellschaft stellt aus (Sitz Bad Neuenahr-Ahrweiler oder Armsheim; gleichnamige Firmen nicht vermischen)? Impressum embedded-data.de, Handelsregister Mainz/Koblenz (HRB 52664), aaa-Ausstellerprofil lesen. (b) Gibt es eigene Hardware (Gateway) und wo gefertigt? Wenn nur Software: Rot nach E2 mit Quelle. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Sitz (widersprüchlich); Produktbeschreibung "david" (S); Hardware (?). Stichprobe für Jey: ja.

## 9. ESCHA GmbH & Co. KG | Stand 209
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 3, CRM-Konzernbezug).** crm_abgleich.py "ESCHA": ENTHALTEN "TSL-ESCHA GmbH" (bekannte_firmen_DE-AT-NL.txt Zeilen 2420 bis 2422, alle [DE], ohne Ort). Jey muss bestätigen, ob die Einheit dieselbe ist. Sonst wäre Fertigung Halver Mittel (S: Gruppe mit "Produktion auf drei Kontinenten") und Verguss Hoch (S/A: umspritzte Stecker/Leitungen), also ohne CRM-Bezug erst nach Fertigungsbeleg (Zeile 5).
- Eigene Prüfung zur Einheit: Suchergebnisse beschreiben TSL-ESCHA GmbH als eigenständig (gegründet 1986, Oststraße 7, 58553 Halver, Türtaster/LED-Signalgeräte, 2021 von Turck duotec Holding an MAFELEC TEAM verkauft, ca. 17 Mio. EUR Umsatz, S); die ausstellende ESCHA hat Elberfelder Straße 32, 58553 Halver, Familienunternehmen, Konzernumsatz über 102 Mio. EUR 2022 (S). Beide gleicher Ort, anderer Straßenname, anderer Eigentümer laut Quellenlage: mit großer Wahrscheinlichkeit zwei Gesellschaften, aber nicht V belegt. Historisch lieferte ESCHA laut chinesischem Firmenprofil (PDF, S) ab 1983 Kunststoffgehäuse/Steckverbinder an "Werner Turck GmbH"; CRM führt "Werner Turck GmbH & Co. KG" (Zeile 2571), "Hans Turck GmbH & Co. KG" (973), "Turck Beierfeld/mechatec" (2428 bis 2431). Ein weiterer Konzernbezug ESCHA zu Turck-CRM ist damit nicht ausgeschlossen (Kunden-/Lieferantenverhältnis, kein Eigentum belegt). Zusätzlich MAFELEC im CRM: kein Treffer.
- Korrekturen an Toms Feldern: Feld 12 bestätigt (unklar). Zusatz: Turck-Bezug über Werner Turck (Zeile 2571) von Tom nicht genannt. Feld 17: Tom nennt PLZ-Abweichung Liste 58542 gegen 58553 Verzeichnisse (Halver); eigene Suche bestätigt 58553. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 3): (1) Jey: Ist die CRM-Zeile "TSL-ESCHA GmbH" (Oststraße 7, Halver) dieselbe Einheit wie die ESCHA GmbH & Co. KG (Elberfelder Straße 32)? Und gehört "Werner Turck GmbH & Co. KG" zum Bestandskontakt der Turck-Gruppe oder ist sie eine eigenständige Firma? Wo nachsehen: CRM-Datensätze (Adresse), Handelsregister Iserlohn beider Gesellschaften, Impressum escha.net/en/impressum-englisch. (2) Fertigung Halver belegen (Impressum, Stellenanzeige Produktion/Montage Halver, Standortseite) und ob Überspritzen/Verguss in Halver passiert (Datenblatt, Karriereseite). Aktion: nicht kontaktieren, bis (1) geklärt ist.
- Nicht verwendbare Aussagen: Fertigung in Halver (S); Verguss (S/A, "Überspritzen" ist Spritzguss, nicht Vergießen); Konzernumsatz (S, eine Quelle); Turck-Historie (S, Quelle ausländisches PDF). Stichprobe für Jey: ja.

## 10. Europascal GmbH | Stand 122
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Händler/Kalibrierdienstleister: mehrere Snippets (S) nennen "Vertrieb, Kalibrierungen und herstellerunabhängige Reparaturen", Authorized Fluke Calibration Service Center, DAkkS-Labor, Additel-Geräte als Vertriebsprodukt. Das trägt E2 inhaltlich stark, ist aber nicht Stufe V. Rot nur bei belegtem Ausschluss (Zeile 1 verlangt V), daher Gelb.
- Eigene Prüfung: Adresse laut DAkkS-Akkreditierungsurkunde D-K-15055-01-02 (S): An der Wiesenhecke 10, 63456 Hanau (deckt sich mit PLZ der Messeliste). Keine Eigenprodukte, keine Fertigung gefunden. Verguss Niedrig (A, Zukauf-Messgeräte). CRM: crm_abgleich.py "Europascal GmbH": neu. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Gibt es eigene Produkte oder Fertigung in Hanau (Händler/Dienstleister mit E2 belegen)? Wo nachsehen: Impressum und Produktseite von Europascal (Domain laut Tom unbekannt; über DAkkS-Urkunde/aaa-Ausstellerprofil auffindbar), Stellenanzeigen (Kalibrierer, Service), Additel-Händlerverzeichnis. Bei Bestätigung Rot nach E2 mit Quelle.
- Nicht verwendbare Aussagen: "kein Fertiger" (S, noch nicht E2-belegt); Mitarbeiterzahl 11 bis 50 (S). Stichprobe für Jey: ja (Rot-Kandidat, nur Bestätigung nötig).

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind überall korrekt niedrig angesetzt (keine V-Aussage vorgetäuscht). Er stufte CETA als "interessant" (Fertigung Hoch A + Verguss Hoch A) ein; nach Regel I wäre dafür Browser-Gegenlesen nötig, daher von mir nur "Grün vorläufig".
- Tom nannte Konzernabgleich Dussmann als offen; nachgeholt, ohne Treffer. Der Abgleich der EFCO-Konzernnamen (Everfine) und von MAFELEC/Werner Turck ist ergänzt.
- Vorschlag Fehlerlog (Jey gibt frei, nicht eingetragen): (1) Bei Namensgleichheit am selben Ort (ESCHA gegen TSL-ESCHA) zusätzlich Eigentümer- und Lieferantenbeziehungen (Turck) abgleichen. (2) Messelisten-Gesellschaftsnamen (Dussmann Industrial Automation) gegen Impressum prüfen, sie existieren teils nicht.

## Einschränkungen
- Browser nicht verfügbar, WebFetch nicht verfügbar: kein Gegenlesen nach Abschnitt H, kein Impressum und kein Datenblatt gelesen; alle Aussagen Stufe S oder A. Keine "Zitat im Browser bestätigt: ja".
- WebSearch: 20 Abfragen verbraucht (Identität/Fertigung bei Dussmann, ESCHA, CETA, CONTA-CLIP, Dreisbach, EFCO, embedded data, DFS, DSP, Europascal; je vier Patent-Zusatzsuchen CETA, CONTA-CLIP, ESCHA, Dreisbach; Turck-Historie). Ergebnisse sind Kurzfassungen und Verzeichnisse.
- Patente: DEPATISnet, Espacenet, Google Patents nicht direkt abgefragt; Pflichtsuche F5 nicht erfüllt (alle 10 Firmen). Zurückgestellt: Anmeldervarianten (u. a. "CETA Testsysteme", "CONTA-CLIP", "ESCHA Bauelemente", "Dreisbach+Jungmann", "DSP Systeme/AR Bayer", "EFCO Technology/Everfine"), Rechtsstand entfällt mangels Treffer.
- Wettbewerbereinsatz (F6): für acht Firmen nur Listenabgleich (wettbewerber_referenzen.md, Teil 1 gelesen bis Zeile 378; Nordson-/Sonderhoff-/DELO-Kundenlisten ohne Treffer in den von mir gelesenen Teilen, Rest per Grep nicht auf ESCHA etc. geprüft) und keine Einzelsuche. Tom meldet DELO-Liste ohne ESCHA; nicht von mir wiederholt.
- Handelsregister/Unternehmensregister nicht abgerufen. Kundendatenbank (Excel) nicht lesbar; kundendatenbank_export.txt ohne Treffer für alle zehn Firmen (Turck, Halver, ESCHA geprüft), daher keine "Verifiziert am"-Prüfung nötig.
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
