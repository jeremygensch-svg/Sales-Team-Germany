# Tina Batch 07 – all about automation Düsseldorf 2026 (Prüfung von tom_batch_07.md)
Erstellt: 2026-10-15 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe: ausschließlich aaa_ergebnisse/tom_batch_07.md (10 Firmen).
**VERMERK: ohne Browser/Web-Abruf geprüft, vorläufig.** Chrome-Werkzeuge nicht verfügbar, WebFetch scheitert (DNS-Fehler, getestet an komaxgroup.com). Nutzbar war nur WebSearch (27 Abfragen, Ergebnis = Snippets/Zusammenfassungen, daher höchstens Stufe S). Keine V-Quelle selbst gelesen, "Zitat im Browser bestätigt" daher bei allen Firmen: nein.
Skripte: `python3 batch_check.py aaa_ergebnisse/tom_batch_07.md --tina` meldet nur "Feld 11: keine Ampel" (erwartet, Ampel ist Tinas Feld). `crm_abgleich.py` für jede Firma mit Konzern/Altname/Kürzel selbst ausgeführt (Ergebnis je Firma). Tabellenzeile = Zeilennummer der Ampel-Tabelle aus Regeldatei D.
Verifikationsdatum aller Einträge: 2026-10-15.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | KEYENCE Deutschland GmbH (116) | GELB | 5 | nein |
| 2 | Komax Kabelverarbeitungssysteme Deutschland GmbH (413) | GELB | 5 (Aspekt E1) | ja |
| 3 | Kübler Group - Fritz Kübler GmbH (426) | ROT | 1 (E5) | ja (Einheit im CRM bestätigen) |
| 4 | Lanfer Automation + Robotics GmbH (614) | GELB | 7 | ja |
| 5 | LASIT LASER DEUTSCHLAND GMBH (402) | GELB | 5 | nein |
| 6 | LinMot GmbH (310) | GELB | 5 | nein |
| 7 | Lovato Electric GmbH (802) | GELB | 5 | nein |
| 8 | Machine Creators GmbH & Co. KG (434) | GELB | 2 | ja |
| 9 | Magnescale Europe GmbH (621) | GELB | 5 | ja |
| 10 | MB connect line GmbH (615) | GELB | 3 | ja |

Bilanz: 0 Grün, 9 Gelb, 1 Rot (Kübler, E5, vorläufig bis Jey die Einheit bestätigt). Kein Grün, weil bei keiner Firma Fertigung in DE/AT/NL als V oder tragfähig nach Sitzregel belegt ist, ohne dass ein CRM-/Identitäts-/Konzernpunkt offen bleibt.

**Patent-Nachholung (Prüfpunkt 8, Regel F5): NICHT vollständig möglich.** Google Patents, Espacenet und DEPATISnet waren nicht direkt erreichbar. Ich habe je Firma höchstens eine indirekte WebSearch-Patentsuche ausgeführt (Kübler, Lovato, MB connect line, Magnescale, LinMot/NTI, LASIT/El.En./Lanfer, Keyence); für Komax und Machine Creators keine eigene. Ergebnis überall: kein Patent der Firma mit Verguss-Bezug im Snippet gefunden; das ist ausdrücklich KEIN Gegenbeweis und keine Pflichtsuche im Sinne von F5. Feld 9 bleibt für alle zehn Firmen UNVOLLSTÄNDIG. Das ändert keine der Ampeln (Patent hat keinen Einfluss auf die Tabelle), verhindert aber die Einstufung "verwendbar".

**Wettbewerbereinsatz (Feld 16):** Zweite Durchsicht von wettbewerber_referenzen.md (Zeilen 1 bis 378 gelesen; Treffer auf Keyence, Komax, Kübler, Lanfer, LASIT, LinMot, Lovato, Magnescale, MB connect line, Machine Creators nicht gesehen). Eigene Einzelsuchen nur für Komax. Toms "kein Hinweis gefunden (Stufe ?)" bleibt Stufe ?, nicht als Negativbeleg verwendbar. Komax hat laut Snippet Dosiergeräte von Giebler und Werner Wirth: der Treffer "Giebler" in kundendatenbank_export.txt Zeile 10 (Kunde Ulm Tamaschke/Burkhardt, "Giebler 2K-System mit WEVO 9251 FL") ist ein Kundenvermerk über ein Giebler-System, kein CRM-Eintrag von Komax und kein Konzernbezug.

---

## 1. KEYENCE Deutschland GmbH | Stand 116
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 5).** Fertigung in DE/AT/NL ist nicht belegt (Stufe S: Keyence gilt als Entwickler mit Auftragsfertigern, Wikipedia-Spiegel/Verzeichnisse), die deutsche GmbH ist laut Verzeichnissen Vertriebsgesellschaft. E2/E3 liegt nahe, ist aber nur mit S (Wikipedia, Verzeichnisse, Stellenanzeigen Vertrieb) belegt, nicht mit V: deshalb nicht Rot.
- Korrekturen an Toms Feldern: Feld 17 Registerdaten durch eigene Suche bestätigt (S): Siemensstraße 1, 63263 Neu-Isenburg, HRB 11973 Offenbach, Geschäftsführung Michio Sasaki und Shinji Furuta (BDI-Verzeichnis, S); die PLZ 62263 in einem Verzeichnis ist offenbar ein Tippfehler. Messeliste nennt PLZ 60549 (Frankfurt): Abweichung bleibt, Impressum nicht gelesen. Feld 7: Niedrig (S) bestätigt; Zusatz: Keyence-Produkte werden laut Snippet an "qualified contract manufacturing companies" gefertigt, Lager (nicht Werke) auch in Deutschland (Wikipedia, S). Feld 9: eigene indirekte Suche "Keyence Corporation patent potting/resin molded": kein Patent mit Keyence als Anmelder sichtbar; Fremdpatente aussortiert. Direkter Datenbankzugriff fehlt.
- Zitat im Browser bestätigt: nein (keine Quelle gelesen).
- Verguss (höchstes Bauteil): Hoch (A, Sensoren), aber ohne DE-Fertigung für die Ampel ohne Wirkung. CRM: neu (crm_abgleich.py "Keyence Deutschland", "Keyence Corporation": kein Treffer). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?).
- Nachrecherche-Auftrag (Gelb): Gibt es ein Keyence-Werk oder eine Montage in DE/AT/NL? Wo nachsehen: keyence.de Impressum und "Über uns/Standorte" im Browser, Keyence-Konzernseite zu Produktionsstandorten, Stellenanzeigen Neu-Isenburg (Montage/Produktion) 2025/2026. Bleibt die Frage mit "nein" belegt (V), ist Rot nach E2/E3 zu setzen.
- Nicht verwendbare Aussagen: "Auftragsfertiger"/Vertrieb (S, Wikipedia-Sekundärquelle); Verguss aller Sensoren (A); Mitarbeiter-/Umsatzzahlen (nicht geprüft). Stichprobe für Jey: nein.

## 2. Komax Kabelverarbeitungssysteme Deutschland GmbH | Stand 413
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 5; zugleich Aspekt E1).** Fertigung am Standort Nürnberg ist nicht belegt (Vertrieb/Service, ca. 25 Beschäftigte laut Verzeichnis, S; ein Verzeichnis führt den Standort als "manufacturer", S). Die Komax-Gruppe bietet nach der Gruppenseite (Österreich-Version, S) Dosier-, Misch- und Vergusssysteme (Giebler, Werner Wirth, Alpha 6, 2-K-DOS) an; ob die deutsche GmbH sie vertreibt, ist nicht belegt. Rot nach E1 setzt Stufe V und die Zuordnung zur deutschen Einheit voraus: fehlt.
- Korrekturen an Toms Feldern: Feld 17 bestätigt (S): Impressum-Snippet "Komax Deutschland GmbH", Willstätter Strasse 95, 90449 Nürnberg, Amtsgericht Nürnberg HRB 12581, Geschäftsführer Matthias Klaus; derselbe Sitz wie die Vorgabe, die Abweichung ist die Namensform (Messeliste: "Komax Kabelverarbeitungssysteme Deutschland GmbH"). Impressum nicht gelesen. Feld 4/7: Rolle des Standorts weiter offen; Konzern mit mehreren Werken, daher V nötig (Sitzregel greift nicht). Feld 9: keine eigene Suche möglich/ausgeführt, Toms Justia-Befund (kein Verguss-Patent) unverändert S.
- Zitat im Browser bestätigt: nein. Aus meiner Suche (S): Gruppenseite https://www.komaxgroup.com/en-at/expertise/mixing-technology-dosing-technology-and-dispensing-technology, Zusammenfassung: Geräte von Giebler und Werner Wirth, Alpha 6 und 2-K-DOS für Casting; Seite nicht gelesen.
- Verguss (höchstes Bauteil): Mittel (A, Antriebe/Sensorik/Steuerung der eigenen Maschinen). CRM: neu (crm_abgleich.py "Komax Kabelverarbeitungssysteme Deutschland GmbH", "Komax Deutschland", "Komax Holding", "Komax", "Schleuniger": kein Treffer; "Giebler" siehe oben, kein Bezug). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?).
- Nachrecherche-Auftrag (Gelb): (a) Vertreibt oder fertigt die Komax Deutschland GmbH Nürnberg Dosier-/Vergusssysteme (Giebler, Wirth, 2-K-DOS)? Wo nachsehen: komaxgroup.com/de Produktseite "Dichten, Kleben, Vergießen" im Browser lesen, Ansprechpartnerseite Nürnberg, Impressum. Ist es belegt, ist es Rot nach E1 mit Quelle. (b) Wird in Nürnberg montiert (Stellenanzeigen Nürnberg: Montage, Produktion)? Falls nein und kein Dosiergeschäft: Rot nach E2/E3 nur mit V. (c) Gehören Schleuniger (Haan) und Komax SLE (Grafenau) zur selben Einheit? Aktion: nicht ansprechen, bis (a) geklärt.
- Nicht verwendbare Aussagen: Dosiergeschäft der deutschen Einheit (S); Fertigung/Montage Nürnberg (?); "manufacturer" aus Verzeichnis (S); Gruppenwerke Haan/Grafenau (S, Triage); Mitarbeiterzahl (S). Stichprobe für Jey: ja (E1-Frage).

## 3. Kübler Group - Fritz Kübler GmbH | Stand 426 – BEKANNT
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: ROT (Tabellenzeile 1, harter Ausschluss E5).** Rot, weil: Firma im CRM. `crm_abgleich.py "Fritz Kübler GmbH"` meldet IDENTISCH mit bekannte_firmen_DE-AT-NL.txt Zeile 860 ("Fritz Kübler GmbH [DE]", ohne Ortsangabe); die Konzernbezeichnungen "Kübler Group"/"Kübler" treffen dieselbe Zeile. kundendatenbank_export.txt: kein Treffer (Grep auf "Kübler"/"kuebler"). Es ist die einzige bekannte Fritz Kübler GmbH, Sitz Schubertstraße 47, 78054 Villingen-Schwenningen (Verzeichnisse, S). Bestandskontakt pflegen, kein Neukunde.
- Hinweis zur Einschränkung: Das CRM nennt keinen Ort; "gleiche Einheit" ist daher nach Namen und Sitzregion anzunehmen, aber nicht per Ortsangabe belegt. Ergibt sich bei Jey ein anderer Ort, wäre es Gelb mit Auftrag "juristische Einheit manuell klären" (E5, Klarstellung). Deshalb Stichprobe für Jey: ja.
- Korrekturen an Toms Feldern: Feld 12 bestätigt (BEKANNT). Feld 7: Mittel (S) bestätigt; Zusatz aus eigener Suche: Gruppenseite nennt Produktionsstandorte "in Europa, Asien und den USA", eine ältere Pressemeldung nennt für 2020 "vier Produktionsstandorte in Deutschland, Indien und den USA" (S, widersprüchlich); Werkserweiterung Schwenningen undatiert (industrial-production.de, S; 2007 +2.500 m²). Keine aktuelle Produktions-/Montage-Stellenanzeige gefunden (nur Entwicklungsingenieure Elektronik, devjobs, S). Feld 8: Hoch (S) bestätigt: Sendix 3651/3671 und 3658/3678 mit "vollvergossener Elektronik" (computer-automation.de, Fachpresse, nicht Herstellerseite, S). Feld 9: eigene Suche "Kübler patent Vergussmasse/potting": kein Kübler-Patent mit Verguss gefunden; ein Treffer US 9622372 "Housing-side separating layer for the stress decoupling of potted electronics" nicht Kübler zuordenbar (Anmelder nicht erkennbar), nicht verwendet. Tom: EP0995974 und EP2867624 Rechtsstand weiter offen.
- Zitat im Browser bestätigt: nein.
- Verguss (höchstes Bauteil): Hoch (S, Drehgeber-Elektronik). Fertigung DE: Mittel (S). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?).
- Nachrecherche-Auftrag: keiner (Rot). Aktion: Jey bestätigt im CRM Ort/Datensatz von "Fritz Kübler GmbH"; bei Villingen-Schwenningen Bestandskunde.
- Nicht verwendbare Aussagen: Vergussaussage (S, Fachpresse); Fertigungsort Schwenningen (S); Mitarbeiterzahl >600 (S, Quellen widersprüchlich 480/600); Patentrechtsstand (nicht geprüft). Stichprobe für Jey: ja.

## 4. Lanfer Automation + Robotics GmbH | Stand 614
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 7).** Die Sitzregel (Zeile 4) lässt sich nicht sicher anwenden: Lanfer ist Teil der LB GmbH Bocholt (Gruppe), deren Struktur (mehrere Werke?) ungeklärt ist; zudem ist der Beleg für Fertigung nur Selbstdarstellung (Messeprofil, S: Schaltschrankbau als Kernkompetenz seit 1979, Serienfertigung). Verguss/Dichtung Mittel (A, Schaltschrank-Dichtung, zugekaufte Antriebe/Netzteile). Wäre die Gruppe ein Ein-Standort-Betrieb, wäre es Grün nach Zeile 4.
- Korrekturen an Toms Feldern: Feld 17 durch eigene Suche gestützt (S): Hoher Weg 13, 46325 Borken, HRB 20112 (Implisense); Messeprofil und StepStone bestätigen Name und Borken-Weseke. Eigene Website weiter nicht gefunden. Feld 5: "unbekannt" bleibt. Feld 9: Patentsuche LÜCKE bleibt; eine indirekte Suche "Lanfer Automation Robotics patent" blieb ohne Treffer (kein Gegenbeweis).
- Zitat im Browser bestätigt: nein.
- Verguss (höchstes Bauteil): Mittel (A). Fertigung DE: Mittel (A). CRM: neu (crm_abgleich.py "Lanfer Automation + Robotics GmbH", "Lanfer", "LB GmbH Bocholt": kein Treffer; Kürzel LB/LAR zu kurz, unzuverlässig). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?).
- Nachrecherche-Auftrag (Gelb): (a) Gehört Lanfer zu einer Gruppe mit weiteren Werken (LB GmbH Bocholt)? Wo nachsehen: Impressum der Lanfer-/LB-Website (Website zuerst ermitteln), Handelsregister Coesfeld HRB 20112, Gesellschafterliste. (b) Wird in Borken-Weseke selbst Schaltschrank gebaut (Karriereseite Elektroniker/Schaltschrankbauer, Stellenanzeige Arbeitsagentur 10000-1183410444-S war nicht lesbar)? (c) Patentsuche in Google Patents/Espacenet nachholen. Aktion: Beobachtung.
- Nicht verwendbare Aussagen: Verguss aller Bauteile (A); Schaltschrank-Dichtung (A); Mitarbeiterzahl >100 (S); Gruppenzugehörigkeit LB GmbH (S). Stichprobe für Jey: ja (kandidiert zu Grün bei Klärung der Gruppe).

## 5. LASIT LASER DEUTSCHLAND GMBH | Stand 402
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 5).** Fertigung in Immendingen ist nicht belegt; die Quellen beschreiben die deutsche GmbH als Vertriebs-/Servicegesellschaft eines italienischen Herstellers (Produktion Torre Annunziata bei Neapel, El.En.-Gruppe 70 %; DirectIndustry/findlight, S). Das genügt für E2/E3 nicht mit Stufe V, daher nicht Rot. Verguss Mittel (A).
- Korrekturen: Feld 7 Niedrig (S) bestätigt. Feld 17 weiter nur S (openPR Im Stockacker 7, 78194 Immendingen, "hundert Mitarbeiter"; Rechtsform nicht bestätigt). Zusatz: Eine Gruppenseite nennt Umsatz 2025 27 Mio. EUR (S, ohne Einfluss). Feld 9: eigene indirekte Suche "LASIT / El.En. patent potting": kein Treffer mit LASIT/El.En. als Anmelder; Direktzugriff fehlt, LÜCKE bleibt.
- Zitat im Browser bestätigt: nein.
- Verguss (höchstes Bauteil): Mittel (A, Netzteile, Steuerelektronik). CRM: neu (crm_abgleich.py "LASIT LASER DEUTSCHLAND GMBH", "LASIT", "El.En.": kein Treffer). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?).
- Nachrecherche-Auftrag (Gelb): Wird in Immendingen montiert oder nur vertrieben/gewartet? Wo nachsehen: lasit.com/Impressum der deutschen GmbH (Website erst bestätigen), openPR-Meldung vollständig, Stellenanzeigen Immendingen (Montage, Elektroniker, Service), Handelsregister (Freiburg/Villingen-Schwenningen) zur Rechtsform. Bei Beleg "nur Vertrieb/Service" (V): Rot nach E2.
- Nicht verwendbare Aussagen: Fertigung Immendingen (?); Verguss aller Bauteile (A); Rolle "Vertrieb" (S); Mitarbeiterzahl/Umsatz (S). Stichprobe für Jey: nein.

## 6. LinMot GmbH | Stand 310
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 5).** Die deutschen Standorte sind laut Firmenblog Vertrieb/Auftragsabwicklung/Reparaturservice (Essen, Büro Burgoberbach "sales office"), 20 Beschäftigte (S, Suchzusammenfassung); Fertigung beim Konzern NTI AG (CH). Das entspricht E2/E3 wahrscheinlich, ist aber nicht mit V belegt (Seite nicht gelesen); Reparatur mit Wicklungsarbeiten und Demo-Aufbau (Stellenanzeige) lässt Montage in Teilen offen.
- Korrekturen: Feld 7 Niedrig (S) bestätigt. Feld 9: eigene indirekte Suche "NTI AG LinMot patent stator potting": kein Patent mit NTI AG als Anmelder bestätigt; Treffer "Encapsulated motor with precision bearing registration" (US 5008572) und EP2390992A2 "Abgedichtetes Linearmotorsystem" sind nicht NTI zuordenbar (Anmelder im Snippet nicht erkennbar), nicht verwendet. LÜCKE bleibt. Feld 17 weiter S.
- Zitat im Browser bestätigt: nein.
- Verguss (höchstes Bauteil): Hoch (A, Linearmotor-Stator/Antriebselektronik; Produkttyp, Konzernprodukt). CRM: neu (crm_abgleich.py "LinMot GmbH", "NTI AG", "LinMot": kein Treffer). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?).
- Nachrecherche-Auftrag (Gelb): Werden in Essen oder Burgoberbach Antriebe montiert/vergossen oder nur Reparaturen, Demo-Aufbauten und Vertrieb betrieben? Wo nachsehen: linmot.com/blog/linear-linmot-gmbh/ vollständig im Browser, linmot.com Impressum, Handelsregister Essen, Stellenanzeigen "Montage/Produktion". Bei V-Beleg "nur Vertrieb/Service": Rot nach E2.
- Nicht verwendbare Aussagen: Verguss der Stator/Elektronik (A, Konzern); Reparatur-Vergussarbeiten (?); Mitarbeiterzahl (S). Stichprobe für Jey: nein.

## 7. Lovato Electric GmbH | Stand 802
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 5).** Fertigung in Waldbronn ist nicht belegt: Verzeichnisse und ein Lovato-Kontaktblatt nennen nur Adresse; Konzern Lovato Electric S.p.A. (Bergamo) mit Entwicklung/Fertigung in Italien ("designed, industrialized, tested and built by LOVATO Electric", S). Eine Montage-/Produktionsstelle in Waldbronn wurde nicht gefunden. Verguss Hoch (A, Schütze/Relais/Spulen/Netzteile) ist ohne DE-Fertigung für die Ampel ohne Wirkung.
- Korrekturen: Feld 17 jetzt durch eigene Suche gestützt (S): LOVATO ELECTRIC GMBH, Im Ermlisgrund 30, 76337 Waldbronn (Ortsteil Busenbach), Tel. 07243 76 69 37-0 (dasoertliche.de, Lovato-PDF https://download.lovatoelectric.com/PD034D04_24.pdf, S). Handelsregister/Impressum nicht gelesen. Feld 7: Niedrig/Stufe ? bleibt, Tom hatte nicht recherchiert; ich habe sie nur gesucht (keine Fertigungsindizien in DE). Feld 9: eigene indirekte Suche "Lovato Electric S.p.A. patent potting": kein Treffer mit Lovato als Anmelder; LÜCKE bleibt.
- Zitat im Browser bestätigt: nein.
- Verguss (höchstes Bauteil): Hoch (A). CRM: neu (crm_abgleich.py "Lovato Electric GmbH", "Lovato Electric S.p.A.", "Lovato": kein Treffer). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?).
- Nachrecherche-Auftrag (Gelb): Wird in Waldbronn montiert/gefertigt oder nur vertrieben (Lager/Vertrieb)? Wo nachsehen: lovatoelectric.com/de Impressum und Standortseite, Handelsregister Mannheim/Karlsruhe, Stellenanzeigen Waldbronn/Busenbach (Montage, Lager), Konzern-Standortliste. Bei V-Beleg "Vertriebsgesellschaft": Rot nach E2.
- Nicht verwendbare Aussagen: Fertigung Waldbronn (?); Verguss aller Bauteile (A); Familienkonzern (S, Triage). Stichprobe für Jey: nein.

## 8. Machine Creators GmbH & Co. KG | Stand 434
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Eine Firma "Machine Creators GmbH & Co. KG" in Meschede ist per WebSearch nicht auffindbar (Suche "Machine Creators GmbH & Co. KG Meschede": keine Treffer zur Firma). Nicht Rot: fehlender Beleg allein ist kein Rot-Grund.
- Korrekturen: Feld 17 bleibt NICHT belegt. Neu aus eigener Suche (S): Die Firma "Multimedial-Systeme" (Wildeshausener Straße 77, 59872 Meschede, Inhaber laut Stellenanzeige Sebastian Diers, "Sondermaschinenbau", multimedial-systeme.de) existiert; Quelle sind Stellenanzeigen auf karriere.ibb.com (S). Ob Machine Creators dieselbe Einheit, ein Markenname oder ein Messe-Eintrag mit falscher Schreibweise ist, ist unbelegt (nur gleicher Stand 434 und gleiche PLZ 59872 laut Messeliste). Gleichnamige Firmen nicht vermischt. Feld 3/4/7/8 unverändert (Niedrig, ?).
- Zitat im Browser bestätigt: nein (keine Quelle).
- Verguss: nicht bewertbar (kein Produkt belegt). CRM: neu (crm_abgleich.py "Machine Creators GmbH & Co. KG", "Machine Creators", "Multimedial-Systeme": kein Treffer). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Feld 9: LÜCKE (keine Patentsuche möglich ohne Identität).
- Nachrecherche-Auftrag (Gelb): Identität klären. Wo nachsehen: Ausstellerprofil auf duesseldorf.allaboutautomation.de (Stand 434), Handelsregister Arnsberg (Meschede) und Unternehmensregister nach "Machine Creators" und "Multimedial-Systeme", Impressum multimedial-systeme.de (Beziehung/Markenname?). Danach Produkte (Sondermaschinenbau: Montage am Sitz Meschede?) und Fertigung.
- Nicht verwendbare Aussagen: alle Aussagen zu Produkten, Fertigung und Verguss (?); Zusammenhang mit Multimedial-Systeme (?). Stichprobe für Jey: ja (Identität).

## 9. Magnescale Europe GmbH | Stand 621
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 5).** Widersprüchliche Sekundärangaben zur Rolle von Wernau: Die DMG-MORI-Standortseite beschreibt laut Suchzusammenfassung die Magnescale-Tochter im Anbau als "Hersteller hochpräziser magnetischer Messsysteme" (S), ein DirectIndustry-Profil nennt Wernau nur eine "sales company" (S). Konzern (DMG MORI/Magnescale Co., JP), daher V nötig; Fertigung in Wernau ist nicht belegt. Verguss Hoch (A, Messköpfe/Sensoren). Sollte die Fertigung in Wernau mit V belegt werden, wäre es Grün nach Zeile 4.
- Korrekturen an Toms Feldern: Feld 7 Mittel/S bestätigt, jetzt gestützt durch den zweiten (widersprüchlichen) Beleg. Feld 17: Adresse aus einem Katalog 2015 (Antoniusstrasse 14, 73249 Wernau, S; veraltet möglich), Tom nannte nur "Wernau"; Impressum nicht gelesen. Feld 9: eigene indirekte Suche "Magnescale patent potting": Anmelder früher "Sony Magnescale Inc" (z. B. US5016359, US4484391, US5635833 "protective resin tape", alle alt, kein Verguss); kein aktuelles Verguss-Patent mit Magnescale als Anmelder; US 11656107 "Encapsulated position sensor functional unit" nicht Magnescale zuordenbar. LÜCKE bleibt (Direktzugriff fehlt, Rechtsstand ungeprüft). Altname "Sony Magnescale" als Argument im Skript nachgetragen: crm_abgleich.py "Sony Manufacturing Systems": kein Treffer; "Sony Magnescale" selbst nicht gegen CRM geprüft (siehe Einschränkungen).
- Zitat im Browser bestätigt: nein. Quelle zum Nachlesen: https://en.dmgmori.com/company/locations/wernau (S, Seite nicht gelesen).
- Verguss (höchstes Bauteil): Hoch (A). CRM: neu (crm_abgleich.py "Magnescale Europe GmbH", "Magnescale", "DMG MORI", "Sony Manufacturing Systems": kein Treffer). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?).
- Nachrecherche-Auftrag (Gelb): Werden Magnescale-Messsysteme in Wernau hergestellt oder nur vertrieben? Wo nachsehen: DMG-MORI-Standortseite Wernau im Browser lesen (Wortlaut zum Anbau/Hersteller), Impressum magnescale.com/Europe, Handelsregister Esslingen/Stuttgart, Stellenanzeigen Wernau (Montage, Messtechnik-Fertigung). Zudem Konzernabgleich "Sony Magnescale"/"DMG MORI Seebach/Pfronten" nachholen.
- Nicht verwendbare Aussagen: Herstellung in Wernau (S, widersprüchlich); Verguss aller Bauteile (A); Konzernstruktur (S). Stichprobe für Jey: ja (aussichtsreichster Kandidat dieses Batches, Fertigungsfrage entscheidet).

## 10. MB connect line GmbH | Stand 615
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 3, CRM-Bezug unklar).** Fertigung in Deutschland: Gerätebauer mit eigenen Produkten (mbNET-Router) am Standort Dinkelsbühl, Hinweise "produced exclusively in Germany" in mbNET-Handbüchern 2017/2019 (S, Suchzusammenfassung, älter als sechs Monate) – nach Sitzregel Stufe A, Fertigung Hoch (A). Verguss/Dichtung Mittel (A). Das CRM führt ein Kürzel "MB [DE]" (bekannte_firmen_DE-AT-NL.txt Zeile 1563, ohne Ort); ob es MB connect line ist, ist offen: ohne diesen Punkt Grün nach Zeile 4. Daneben steht "MB Electronic AG [DE]" in Zeile 1564 (andere Firma, nicht Treffer).
- Korrekturen an Toms Feldern: Feld 17 durch eigene Suche gestützt (S): Winnettener Str. 6, 91550 Dinkelsbühl (it-in-germany.de-Verzeichnis, Handbücher); Impressum/Register nicht gelesen. Der Hinweis in einer Suchausgabe, die Firma sitze "in Maisach", stammt nicht aus einer Quelle und wird nicht verwendet. Feld 7: A bleibt, ergänzt um die Handbuch-Aussage (S). Feld 9: eigene indirekte Suche "MB connect line Patent Anmelder Gehäuse Vergussmasse": kein Patent der Firma gefunden (Fremdtreffer Grundfos EP2096740 u. a. aussortiert); LÜCKE bleibt.
- Zitat im Browser bestätigt: nein. Sinngemäß aus Suchzusammenfassung der Handbücher (S): "Our products are produced exclusively in Germany".
- Verguss (höchstes Bauteil): Mittel (A). CRM: unklar (crm_abgleich.py "MB connect line GmbH", "MB connectline", "MB connect line": kein Treffer; nur Kürzel "MB" IDENTISCH Zeile 1563). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?).
- Nachrecherche-Auftrag (Gelb): (a) Jey: Ist der CRM-Eintrag "MB" [DE] (bekannte_firmen_DE-AT-NL.txt Zeile 1563) die MB connect line GmbH Dinkelsbühl? Wo nachsehen: Kundendatenbank/CRM-Datensatz "MB" (Ort Dinkelsbühl? Ansprechpartner, Notizen). Bei ja: Rot nach E5. (b) Fertigung in Dinkelsbühl aktuell belegen (V): mbconnectline.com Impressum, Karriereseite, Stellenanzeigen Montage/Produktion 2025/2026. (c) Konzern/Mutter von MB connect line (Impressum, Handelsregister Ansbach). (d) Patentsuche nachholen. Aktion: nicht kontaktieren, bis (a) beantwortet.
- Nicht verwendbare Aussagen: "Made in Germany" (S, Handbuch/Ausstellertext, Messebeschreibungen nie V); Fertigungsort Dinkelsbühl (A); Verguss/Dichtung (A). Stichprobe für Jey: ja (CRM-Kürzel).

---

## Konsistenz und Auffälligkeiten
- Tom hat in vier Fällen (Lovato, Machine Creators, Magnescale, MB connect line) laut eigener Angabe keine Websuche ausgeführt; die dortigen Angaben stammten allein aus der Triage. Meine Kurzsuchen bestätigen Adressen (Lovato, MB connect line, Magnescale-Katalog), widerlegen keine Aussage und liefern bei Magnescale einen Widerspruch (Hersteller/Vertrieb).
- CRM-Kürzel: Der Abgleich mit Kürzel "MB" liefert für MB connect line einen Treffer ohne Ortsangabe; das CRM-Textexport hat keine Ortsspalte, daher ist ein Entscheid nur in der Kundendatenbank (xlsx) möglich.
- Die zwei Einstufungen "kein Fertiger" (Keyence, LinMot) und "Wettbewerber/Lieferant" (Komax) sind plausibel, aber nur mit S belegt: kein Rot, solange kein V vorliegt.
- Messe-Signal: unverändert keine Wettbewerber auf der aaa-Liste (Toms Grep); Komax ist über die Gruppe selbst Anbieter von Dosiergeräten.
- Vorschlag für fehlerlog_lehren.md (nicht eingetragen, Jey gibt frei): Bei Suchzusammenfassungen von WebSearch kann der Text Herkunftsangaben aus dem Modellwissen enthalten (Beispiel "MB connect line in Maisach"); solche Sätze ohne Quellen-URL gelten nicht als Beleg.

## Einschränkungen
- Browser nicht verfügbar; WebFetch scheitert mit DNS-Fehler (ENOTFOUND, geprüft an www.komaxgroup.com). Es wurden keine Seiten im Volltext gelesen; alle Aussagen sind Stufe S (Suchzusammenfassungen/Snippets) oder A; "Zitat im Browser bestätigt" überall nein. Die Ampeln sind daher vorläufig.
- WebSearch-Budget: 27 Abfragen verbraucht, verteilt auf alle zehn Firmen (Fertigung/Identität je Firma, Patent indirekt für acht Firmen). Keine eigene Websuche zu Wettbewerbereinsatz außer der Komax-Giebler-Suche.
- Patentrecherche (F5): Google Patents, Espacenet, DEPATISnet nicht erreichbar; nur indirekte Suchen. Feld 9 für alle zehn Firmen UNVOLLSTÄNDIG; Rechtsstand von Patenten nicht geprüft. Nachholung im Browser nötig, bevor ein Batch als vollständig und eine Firma als "verwendbar" gilt.
- Handelsregister/Unternehmensregister nicht abgerufen; Registerdaten (Keyence HRB 11973, Komax HRB 12581, Lanfer HRB 20112) stammen aus Verzeichnissen/Snippets (S).
- Altnamen/Konzerne nicht vollständig abgeglichen: "Sony Magnescale", "Magnescale Co.", "Komax SLE", "Giebler GmbH", "Werner Wirth" nicht als Skript-Argument geprüft (außer Giebler); CRM-Abgleich für "MB" liefert nur das Kürzel ohne Ort.
- Kundendatenbank (xlsx) nicht lesbar; kundendatenbank_export.txt: kein Treffer für die zehn Firmen (Ausnahme Giebler-Vermerk, kein Bezug), daher keine "Verifiziert am"-Prüfung nötig. Datenbankfelder nicht geändert, nichts verschickt, nichts committet.
- Größe/Umsatz und Kontakte nicht geprüft (Regeldatei D, K).
