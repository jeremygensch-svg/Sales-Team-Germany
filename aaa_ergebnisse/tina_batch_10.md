# Tina Batch 10 – all about automation Düsseldorf 2026 (Prüfung von tom_batch_10.md)
Erstellt: 2026-10-15 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe: ausschließlich aaa_ergebnisse/tom_batch_10.md (10 Firmen).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Verfügbar waren nur WebSearch (27 von ca. 30 Abfragen, Standardmodus, nur Snippets/Kurzfassungen) und Bash. WebFetch und Chrome nicht nutzbar. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün vergeben, nichts ist mailtauglich.
Skripte: `python3 batch_check.py aaa_ergebnisse/tom_batch_10.md` = VOLLSTÄNDIG (10 Blöcke; das Skript prüft nur das Vorhandensein der Felder, Toms eigene Angabe "Feld 9 bei allen UNVOLLSTÄNDIG" bleibt bestehen). `python3 crm_abgleich.py` für alle Firmen samt Konzern-/Alt-/Partnernamen selbst wiederholt: Pilz, Pfannenberg (+Europe, Group, Manufacturing), Peakboard (+Theobald Software), Printec-DS (+PRINTEC DS Keyboard, DS Keyboard Technic, Camax DS), Klefinghaus, QuickMOVE, R+W, P+K, REFACTUM: kein Treffer (neu). red cable robots: kein Treffer; "KEBA" = IDENTISCH mit KEBA Group AG (bekannte_firmen_DE-AT-NL.txt Zeile 1273), aber nur Steuerungslieferant, kein Konzern (Regel M nicht ausgelöst, Tom-Einschätzung bestätigt).
Tabellenzeile = Zeilennummer der Ampel-Tabelle D. Verifikationsdatum aller Einträge: 2026-10-15.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel (vorläufig) | Tabellenzeile | Kurzgrund | Stichprobe Jey |
|---|---|---|---|---|---|
| 1 | P+K Maschinen- und Anlagenbau GmbH (700) | GELB | 2 | Identität/Sitz nur aus Messeliste, keine Website | ja |
| 2 | Peakboard GmbH (308) | GELB | 7 | Fertigung der Box unbekannt, E2 (Software) nicht V-belegt | nein |
| 3 | Pfannenberg* (435) | GELB | 2 | Vorgabe Wülfrath nicht belegt; Hamburg gefunden | ja |
| 4 | Pilz GmbH & Co. KG (725) | GELB (Grün-Kandidat) | 5 | Konzern/mehrere Werke, V für Ostfildern fehlt | ja |
| 5 | Pressluft Klefinghaus GmbH (415) | GELB | 5 | Händler-Mischform, Eigenfertigung nur Eigenangabe (S) | nein |
| 6 | Printec-DS HMI Solutions* (435) | GELB | 2 | Vorgabe Wülfrath nicht belegt; Steißlingen gefunden | ja |
| 7 | QuickMOVE GmbH (716) | GELB | 2 | Identität/Standort nicht belegt, Patent-/Böhrer-Hinweis | ja |
| 8 | R+W Antriebselemente GmbH (718) | GELB (Grün-Kandidat) | 5 | Gruppe mit Auslandstöchtern, V für Wörth fehlt | ja |
| 9 | red cable robots* (818) | GELB | 2 | Vorgabe Hoppstädten-Weiersbach nicht belegt; Duisburg gefunden | ja |
| 10 | REFACTUM GmbH (412) | GELB | 2 | Firma nicht auffindbar | ja |

Zahlen: Grün 0, Gelb 10, Rot 0.

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Ich habe nur für Pilz, Pfannenberg, R+W, QuickMOVE und P+K je eine zusätzliche Websuche ausgeführt. Feld 9 bleibt bei ALLEN 10 Firmen ohne Direktabfrage der Datenbanken: nicht belastbar, "keine Treffer" ist kein Gegenbeweis. Der Batch ist nach F5 UNVOLLSTÄNDIG; Nachholen im Browser nötig, bevor ein Grün final wird. Wettbewerbereinsatz (F6): Abgleich mit wettbewerber_referenzen.md per Grep (nur Festo KG, Zeile 465, als Referenzkunde eines Wettbewerbers; Klefinghaus ist Festo-Partner, Festo ist weder Konzern noch dieselbe Einheit, kein Bezug), keine Einzelsuche; ohne Einfluss auf die Ampel.

---

## 1. P+K Maschinen- und Anlagenbau GmbH | Stand 700
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Sondermaschinenbauer laut Messetext (Verguss Mittel, A, nur verbaute Antriebe/Sensorik/Steuerung). Für Zeile 4 (Sitzregel) fehlt die belegte Identität: Sitz Solingen steht nur in der Messeliste.
- Eigene Prüfung: Erneute Suche (Impressum, Patent/Gebrauchsmuster, Stellenanzeigen) fand nur das aaa-Ausstellerprofil (Sondermaschinen, Prüfmaschinen, Poka-Yoke-Systeme, Montage- und Schweißmaschinen, Kamera-/Robotersysteme; S). Keine Website, kein Impressum, keine Stellenanzeige, kein Patent. Kein Treffer in Solingen-Verzeichnissen. Das Muster "Sitz nur aus Messeliste" entspricht Lehre 1.
- Korrekturen an Toms Feldern: keine; Toms Stufen (A/S) sind korrekt niedrig. Feld 9 bleibt unvollständig.
- Zitat im Browser bestätigt: nein.
- **Nachrecherche-Auftrag (Gelb, Zeile 2):** Existiert die Firma mit Sitz Solingen, und wie lautet die Website/das Impressum? Wo nachsehen: aaa-Ausstellerprofil im Browser (Link zur Website), Handelsregister (Wuppertal), Impressum. Danach: Wird in Solingen gebaut, und welche Antriebe/Sensorik/Steuerungen stecken in den Maschinen (Produktseite, Referenzen)?
- Nicht verwendbare Aussagen: Sitz Solingen (A/S); Fertigung am Sitz (A); Verguss aller Bauteile (A). Stichprobe für Jey: ja (Identität).

## 2. Peakboard GmbH | Stand 308
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Software-Haus mit eigener Embedded-Box. Identität stimmt weitgehend (Stuttgart, Messeliste 70174), Fertigung der Hardware unbelegt (?), Verguss Niedrig (A). E2 (Software) ist nicht mit Stufe V belegt, daher nicht Rot (Zeile 1 verlangt V). Zeile 6 setzt belegte Fertigung voraus, deshalb Zeile 7.
- Eigene Prüfung: Suche zu Hersteller/Fertigung der Box ergab nur Produktseiten: Box ist "proprietäre Hardware", dezentral lauffähig, daneben BYOD-Option (S). Kein "Made in", kein Hersteller, kein Impressum im Ergebnis.
- Korrekturen: keine. Toms Einstufung "unwahrscheinlich, möglicher Ausschluss E2" bleibt plausibel, aber nicht belegt.
- Zitat im Browser bestätigt: nein.
- **Nachrecherche-Auftrag (Gelb, Zeile 7):** Wer fertigt die Peakboard Box und wo (Datenblatt, CE-Konformität, Hersteller-Adresse)? Wo nachsehen: peakboard.com/en/products und Datenblatt-PDF, Impressum, AGB (Hersteller/Garantiegeber). Ist es reiner Zukauf und Softwarevertrieb: Rot nach E2 mit Quelle.
- Nicht verwendbare Aussagen: Fertigungsort (?); Verguss der Box (A); Mitarbeiterzahl (S). Stichprobe für Jey: nein.

## 3. Pfannenberg* | Stand 435
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Die Vorgabe "Pfannenberg*, 42489 Wülfrath" ist nicht belegt. Gefunden: Pfannenberg Europe GmbH, Werner-Witt-Straße 1, 21035 Hamburg, laut Firmenseite "Pfannenberg locations" (S) und Firmenbuch-Eintrag (Österreich) HRB 119280 Amtsgericht Hamburg (S); eine weitere Gesellschaft Pfannenberg Group Holding GmbH (HRB 89112) an derselben Adresse (Bloomberg-LEI, S). Verguss Hoch (A, Signalgeber/LED-Signalleuchten), Fertigung nur Mittel/S.
- Eigene Prüfung: Suche "Pfannenberg Wülfrath": kein Treffer zu einem Standort oder einer Vertretung. Produktionsstandorte laut TRUMPF-Kundenbericht (undatiert, S): Deutschland, Italien, China, USA, ca. 470 Beschäftigte; ob Signaltechnik in Hamburg gefertigt wird, bleibt offen (RS-Online-Listings nennen als Ursprungsland je Produkt teils GB, teils DE, S: uneinheitlich, nicht auswertbar). Patente: Tom nennt Filterlüfter-Patente (Justia, S); mein Versuch zu Signalgeber-Patenten brachte nur Händlerlistings. Rechtsstand weiter ungeprüft. Gruppe mit mehreren Werken: Stufe V für Hamburg nötig.
- Korrekturen an Toms Feldern: Feld 17 ergänzt um zwei Gesellschaften in Hamburg (Europe GmbH und Group Holding); "Wülfrath" bleibt unbelegt. CRM: neu, auch für Europe/Group/Manufacturing (Tom bestätigt).
- Zitat im Browser bestätigt: nein.
- **Nachrecherche-Auftrag (Gelb, Zeile 2):** (1) Jey: Welche Einheit stellt in Düsseldorf aus (Pfannenberg Europe GmbH Hamburg oder eine Vertretung in Wülfrath) und warum teilt sich Stand 435 mit Printec-DS? Wo nachsehen: aaa-Ausstellerprofil, Impressum pfannenberg.com, Handelsregister Hamburg. (2) Nach Klärung: Wird die Signaltechnik (Signalleuchten, Signalgeber) in Hamburg gefertigt? Wo nachsehen: pfannenberg.com "locations", Stellenanzeigen Produktion/Montage Hamburg, Produktdatenblatt "Made in".
- Nicht verwendbare Aussagen: Wülfrath-Sitz; Fertigung Hamburg (S/?); Verguss Signalgeber (A); Beschäftigtenzahl (S, undatiert); Filterlüfter-Patente (S, Rechtsstand offen). Stichprobe für Jey: ja.

## 4. Pilz GmbH & Co. KG | Stand 725
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5), Grün-Kandidat.** Identität gut: Impressum-Snippets nennen Pilz GmbH & Co. KG, Felix-Wankel-Straße 2, 73760 Ostfildern, Amtsgericht Stuttgart HRA 210 893, Komplementärin Peter Pilz GmbH HRB 210 612 (S, pilz.com/imprint, mehrere Länderversionen konsistent). Verguss Hoch (A: Sicherheitsrelais, Sensoren, Antriebselektronik). Fertigung Ostfildern wahrscheinlich, aber: Gruppe mit mehreren Werken, daher Stufe V nötig (Tabelle: Zeile 4 nur mit V), und V fehlt.
- Eigene Prüfung: Pilz-Pressemitteilung 2022 (pilz.com/static/pilz/pressmessages, S): Investitionen von ca. 38 Mio. EUR bis 2025 in den Werken Ostfildern, Betschdorf (FR), Bad Ragaz (CH), Jintan (CN), u. a. für Erweiterung der SMD-Fertigung und Relaisproduktion. computer-automation.de (S): Peter Pilz Produktions- und Logistikzentrum Ostfildern, 6.900 m², dort werden Schaltgeräte, Steuerungen, Sensoren und Antriebstechnik hergestellt (Artikel undatiert/alt, Lehre 17). Stellenanzeigen: nur ein Embedded-Systems-Engineer-Eintrag (Aggregator), keine Montage-/Fertigungsanzeige gefunden. Patente: Websuche mit Vergussbegriffen liefert US 11470736, 10631421, 9622372, 12055558 u. a., aber die Snippets nennen keinen Anmelder; keine Zuordnung zu Pilz, nicht verwendet (Lehre 8, 15).
- Korrekturen an Toms Feldern: Feld 4/7 ergänzt um das vierte Werk Bad Ragaz (CH) und die Aussage zu SMD-/Relaisfertigung in Ostfildern (S). Feld 17 bestätigt, Register jetzt als S. Sonst keine.
- Zitat im Browser bestätigt: nein.
- **Nachrecherche-Auftrag (Gelb, Zeile 5):** Wird in Ostfildern gegenwärtig gefertigt (Elektronik/SMD, Relais, Sensoren), und welche Bauteile werden dort vergossen? Wo nachsehen: pilz.com Unternehmens-/Standortseite und Pressemitteilung 2022 im Browser lesen (V für Fertigung Ostfildern, Zitat <15 Wörter), Karriereportal Pilz (Produktion/Montage/Elektronikfertigung Ostfildern), Datenblatt PNOZ/PSEN (Produktionsort). Patente: Google Patents Anmelder "Pilz GmbH & Co. KG" mit "Vergussmasse OR potting compound" und Rechtsstand. Bei V: Grün (Zeile 4).
- Nicht verwendbare Aussagen: Fertigung Ostfildern (S); Produktionszentrum-Artikel (S, alt); Verguss aller Bauteile (A); Patente (nicht zuordenbar). Stichprobe für Jey: ja (Grün-Kandidat, Beleg nur S).

## 5. Pressluft Klefinghaus GmbH | Stand 415
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Identität belegt (S): Pressluft Klefinghaus GmbH, Kerkhagen 7, 58513 Lüdenscheid, Amtsgericht Iserlohn HRB 4474 (Bloomberg-LEI, aktiv). Mischform aus Händler (Festo-Partner) und Hersteller (Hubtüren, Steuerungstechnik seit 1978, ca. 40 Mitarbeiter, alles Eigenangabe/S); Sitzregel greift nicht (Händler-Mischform). Verguss Mittel (A).
- Eigene Prüfung: Eigenfertigung nur durch Eigenangabe "designs, produces and distributes Lift Gates" (S). Die einzigen Stellenanzeigen im Ergebnis betreffen Kältetechniker (Service), keine Montage/Schaltschrankbau. E2 nicht belegt, daher kein Rot.
- Korrekturen: keine. Toms "prüfenswert" ist plausibel.
- Zitat im Browser bestätigt: nein.
- **Nachrecherche-Auftrag (Gelb, Zeile 5):** Welcher Anteil ist Eigenfertigung in Lüdenscheid (Hubtüren, Steuerungs-/Schaltschrankbau), und welche Bauteile sind darin typisch vergossen/gedichtet? Wo nachsehen: klefinghaus.de Produktseiten Hubtüren und Steuerungstechnik, Steuerungstechnik-Broschüre 2024 (PDF, im Browser lesen), Karriereseite (Elektroniker/Montage), Impressum.
- Nicht verwendbare Aussagen: Eigenfertigung (S); Schaltschrankbau (nicht belegt); Verguss aller Bauteile (A); Gründungsjahr (widersprüchlich). Stichprobe für Jey: nein.

## 6. Printec-DS HMI Solutions* | Stand 435
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Die Vorgabe "Printec-DS HMI Solutions*, 42489 Wülfrath" ist nicht belegt. Gefunden (S, embedded-world.de, MECSPE, aaa-Profil): Printec-DS HMI Solutions GmbH, Zeppelinstraße 11, 78256 Steißlingen, früher PRINTEC DS Keyboard GmbH, Tel. +49 7738 802410, Website printecds.com. Fertigung Mittel (S, Hinweise auf Taiwan/China und Produktionspartner in Europa/Asien, daher V nötig), Verguss Mittel (A).
- Eigene Prüfung: Suche "Wülfrath" brachte nur eine andere Firma, Printec Solutions GmbH (Weselberg, laut Implisense Sitzverlegung); Zuordnung zu Wülfrath im Snippet nicht belegt. Nicht mit Printec-DS vermischen. "Selected production and development partners in Europe and Asia" (S) stützt Toms Auslagerungshinweis. Keine Stellenanzeigen gefunden (Menüpunkt "Jobangebote" nur erwähnt). Gemeinsamer Stand mit Pfannenberg: im Suchlauf nicht bestätigt.
- Korrekturen an Toms Feldern: Feld 17 bestätigt; ergänzt: Verwechslungsgefahr mit Printec Solutions GmbH. Feld 9: Vorgängernamen weiter nicht in Patentdatenbanken gesucht.
- Zitat im Browser bestätigt: nein.
- **Nachrecherche-Auftrag (Gelb, Zeile 2):** (1) Jey: Welche Einheit stellt aus (Steißlingen oder ein Wülfrath-Bezug) und warum Stand zusammen mit Pfannenberg? Wo nachsehen: aaa-Ausstellerprofil, Impressum printecds.com, Handelsregister Freiburg/Konstanz. (2) Danach: Werden Folientastaturen/Touch-Systeme in Steißlingen gefertigt, und gibt es Optical Bonding (Produktseiten, Katalog-Onepager auf mecspe.com im Browser lesen, Karriereseite)? Rolle von Camax DS srl klären.
- Nicht verwendbare Aussagen: Wülfrath-Sitz; Fertigung Steißlingen (S); Optical Bonding (A, unbelegt); Verguss/Klebung aller Bauteile (A). Stichprobe für Jey: ja.

## 7. QuickMOVE GmbH | Stand 716
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Weder Standort Köln noch eine Website/ein Impressum belegt. Meine Suchen (Impressum, HRB Köln) fanden nur unzusammenhängende Firmen (UK, BE, Kölner Immobilien-/Umzugsfirmen), keine QuickMOVE GmbH. Produkt (Fördersystem mit Zügen auf Aluprofil, dezentrale Zahnriemenantriebe; S, Messe/MOTEK-Texte) bestätigt; Verguss Mittel (A), Fertigung ? (Mittel).
- Eigene Prüfung / neuer Hinweis: Ein Fachartikel (MBO Oßwald, S) nennt "Böhrer's conveyor system Quick-Move" als international patentiert, Hersteller von Logistiksystemen für Apotheken. Ob QuickMOVE GmbH (Aussteller, MOTEK Halle 5 Stand 5204 laut Suchtreffer, S) mit der Firma Böhrer verbunden ist, ist unbelegt. Mögliche Konzern-/Eigentümerbeziehung, in der CRM-Abfrage nicht gesucht (Argument fehlte): `crm_abgleich.py "Böhrer"` ist nachzuholen. Patent daher möglicherweise unter Böhrer als Anmelder, nicht unter "QuickMOVE".
- Korrekturen an Toms Feldern: Feld 9/17 ergänzt um Böhrer-Hinweis. Toms Aussage, Köln komme nur aus der Messeliste, bestätigt.
- Zitat im Browser bestätigt: nein.
- **Nachrecherche-Auftrag (Gelb, Zeile 2):** Welche Gesellschaft ist QuickMOVE GmbH (Sitz, Register, Verhältnis zu Böhrer)? Wo nachsehen: Impressum quick-move.de (im Browser), MOTEK-Ausstellerprofil (motek-messe.de, Exhibitor 51170), Handelsregister Köln; CRM-Abgleich mit "Böhrer" nachholen. Danach: Wo werden Profile, Antriebe, Steuerungen gebaut oder montiert? Patente unter "Böhrer" und "Quick-Move" in Espacenet/DEPATISnet.
- Nicht verwendbare Aussagen: Sitz Köln (A/S); Fertigungsort (?); Eigenfertigung der Motoren (?); Verguss aller Bauteile (A); Patent-Zuordnung (nicht belegt). Stichprobe für Jey: ja.

## 8. R+W Antriebselemente GmbH | Stand 718
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5), Grün-Kandidat.** Identität weitgehend belegt (S): R+W Antriebselemente GmbH, Hattsteinstr. 4, 63939 Wörth am Main (Messeprofil, mit Tel. +49 9372 9864-0 und Mail info@rw-kupplungen.de). Abweichungen: PLZ 63929 bei einem Messelisting (vermutlich Tippfehler) und "Klingenberg" in einem Verzeichnis; kein Impressum/Register gefunden. Gruppe mit Auslandstöchtern: Stufe V für Wörth nötig, fehlt. Verguss Mittel (A, nur Sensormodul der "intelligenten Kupplung"; Balg-/Lamellenkupplungen mechanisch, Klemmverbindung laut Betriebsanleitung-Snippet).
- Eigene Prüfung: Stellenanzeigen (StepStone-Aggregator, S) für Wörth: Qualitätssicherung mit "Fertigungsprüfungen und Erststückfreigaben", Marketing, Verwaltung; keine Montage-/Elektronikanzeige. Das spricht für Produktion in Wörth, ist aber Aggregator-Snippet, kein V. "über 300 Mitarbeiter" (Stellenanzeige, S). Patente: keine Treffer in der Websuche, nur Fachpresse (SPS 2022 Sensorkupplung).
- Korrekturen: Feld 17 PLZ-Abweichung als wahrscheinlicher Tippfehler eingeordnet (S); keine inhaltliche Änderung an Toms Stufen.
- Zitat im Browser bestätigt: nein.
- **Nachrecherche-Auftrag (Gelb, Zeile 5):** Wird die Sensorkupplung (Elektronik) in Wörth gefertigt, und wie ist das Sensormodul geschützt (vergossen, verklebt)? Wo nachsehen: rw-kupplungen.de Impressum, Produktseite "Intelligente Kupplung" und Datenblatt (im Browser), Karriereseite/Stellenanzeigen Wörth (Montage, Elektronik), Standortseite. Bei V für Fertigung Wörth: Grün (Zeile 4, Verguss Mittel).
- Nicht verwendbare Aussagen: Fertigung Wörth (S); Verguss Sensormodul (A); Klemmverbindung statt Klebung (S); Mitarbeiterzahl (S, widersprüchlich). Stichprobe für Jey: ja (Grün-Kandidat).

## 9. red cable robots* | Stand 818
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Die Vorgabe "red cable robots*, 55768 Hoppstädten-Weiersbach" ist nicht belegt. Gefunden (S): Start-up und Uni-Ausgründung (Duisburg-Essen), gegründet 2023, ca. 5 Mitarbeiter, Gründer Roland Boumann, Robin Heidel, Tobias Burger, Patrik Lemmen (uni-due.de, high-tech.nrw, bouncewatch). Domain redcablerobots.com laut Verzeichnis (S, nicht geprüft). Kein Impressum/Register gefunden. Fertigung ?, Verguss Mittel (A, vermutlich Zukauf von Antrieben und KEBA-Steuerung).
- Eigene Prüfung: Suche nach Hoppstädten-Weiersbach/Birkenfeld und Fertigung/Winde: kein Treffer zu einer Produktion oder einem Standort dort. Vorab-Förderung (Hightech.NRW, Pre-Seed 360 kUSD, Aggregator) ohne Bezug zur Fertigung.
- Korrekturen: keine. CRM-Hinweis KEBA von Tom bestätigt (kein Konzernbezug).
- Zitat im Browser bestätigt: nein.
- **Nachrecherche-Auftrag (Gelb, Zeile 2):** (1) Jey/Browser: Sitz der red cable robots GmbH (Duisburg oder Hoppstädten-Weiersbach) laut Impressum redcablerobots.com und Handelsregister (Duisburg bzw. Bad Kreuznach/Idar-Oberstein). (2) Wo werden Winden und Plattform gebaut oder montiert (Eigenfertigung oder Lohnfertiger), und stammen die Antriebe aus Zukauf?
- Nicht verwendbare Aussagen: Sitz Hoppstädten-Weiersbach; Sitz Duisburg (S); Fertigungsort (?); Verguss (A); Mitarbeiterzahl (S, Sekundärquelle). Stichprobe für Jey: ja.

## 10. REFACTUM GmbH | Stand 412
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Auftrag Identität).** Weder Tom noch ich fanden die Firma außerhalb der Messeliste. Kein Beleg für einen harten Ausschluss; "kein Fertiger" (Tom) ist keine Rot-Begründung, da keine E-Bedingung mit Quelle vorliegt.
- Eigene Prüfung: Suchen "REFACTUM GmbH Kaiserslautern" und "refactum aaa Düsseldorf 2026 Aussteller Retrofit Stand 412": keine Treffer zur Firma (nur Uni Kaiserslautern, DFKI, csi u. a.). Weder Produkt noch Website bekannt.
- Korrekturen: Toms Feld 10 "kein Fertiger (vorläufig)" ist nicht belegt; besser: "unbekannt, Identität offen".
- Zitat im Browser bestätigt: nein.
- **Nachrecherche-Auftrag (Gelb, Zeile 2):** Existiert REFACTUM GmbH in Kaiserslautern und was bietet sie an? Wo nachsehen: aaa-Ausstellerprofil Stand 412 im Browser (Website-Link, Produkttext), Handelsregister Kaiserslautern, Schreibvarianten "Re-Factum", "Refactum". Danach Fertigung/Produkt bewerten.
- Nicht verwendbare Aussagen: alle (Sitz Kaiserslautern aus Messeliste, Produkt "Retrofit/Automation" nur Vermutung der Triage, ?). Stichprobe für Jey: ja.

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind überall korrekt niedrig angesetzt (keine V-Aussage vorgetäuscht). Er hat bei Pilz und R+W selbst auf "Grün bei V-Beleg" verwiesen; ich teile das, sie sind die beiden Grün-Kandidaten des Batches.
- Drei Sitz-Abweichungen aus der Messeliste (Pfannenberg*, Printec-DS*, red cable robots*, alle mit Sternchen): in allen drei Fällen existiert die Firma mit anderem Sitz (Hamburg, Steißlingen, Duisburg), der Wülfrath-/Hoppstädten-Eintrag ist nirgends belegt. Das stützt Lehre 1 (Listen mit falschen Sitzen). Hinweis, nicht Fakt: Das Sternchen scheint bei der Quelle eine Sonderkennzeichnung zu sein; Bedeutung nicht geklärt.
- Vorschlag Fehlerlog (Jey gibt frei, nicht eingetragen): (1) Bei Messelisten mit Sternchen-Einträgen Sitzangabe immer gegen Impressum prüfen. (2) Bei Produkten mit Markennamen im Patentkontext (Quick-Move/Böhrer) Anmelder- und Konzernnamen auch in den CRM-Abgleich geben (Lehre 13).

## Einschränkungen
- Browser und WebFetch nicht verfügbar: kein Gegenlesen nach Abschnitt H, kein Impressum, keine Datenblätter und keine Patentdatenbank gelesen; alle Aussagen Stufe S oder A. Es gibt keine einzige Aussage mit "Zitat im Browser bestätigt: ja".
- WebSearch: 27 Standardabfragen verbraucht (Pilz 4, Pfannenberg 5, Printec/Stand 3, R+W 3, Klefinghaus 2, QuickMOVE 3, red cable robots 2, REFACTUM 2, P+K 2, Peakboard 1). Ergebnisse sind Kurzfassungen, teils maschinell zusammengefasst; Zitate daraus sind nicht wörtlich verifiziert.
- Patente (F5): DEPATISnet, Espacenet, Google Patents nicht direkt abgefragt; Feld 9 bei allen 10 Firmen nicht belastbar. Anmelder-Varianten, Rechtsstand und Konzern-/Vorgängernamen (PRINTEC DS Keyboard, DS Keyboard Technic, Böhrer, Pfannenberg Europe) im Browser nachholen.
- Wettbewerbereinsatz (F6): nur Listenabgleich, keine Einzelsuchen; ohne Einfluss auf die Ampel.
- Handelsregister/Unternehmensregister nicht abgerufen, Registerangaben sind Suchsnippets (Pilz, Pfannenberg, Klefinghaus).
- Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K). Nichts verschickt, keine Datenbankfelder geändert, nichts committet.
