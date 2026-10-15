# Tina Batch 02 – all about automation Düsseldorf 2026 (Prüfung von tom_batch_02.md)
Erstellt: 2026-10-15 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe: ausschließlich aaa_ergebnisse/tom_batch_02.md (10 Firmen), eigene Nachrecherche.
**Vermerk für den ganzen Batch: ohne Browser/Web-Abruf geprüft, vorläufig.** Chrome-Werkzeuge nicht verfügbar, WebFetch scheitert mit "getaddrinfo ENOTFOUND" (getestet an benedict.at), curl auf Espacenet, Google Patents, DEPATISnet und batmaschinenbau.de ohne Verbindung (000). Es lief nur WebSearch (20 Abfragen, Zusammenfassungen und Snippets). Keine Quelle wurde im Wortlaut selbst geöffnet: Kein "Zitat im Browser bestätigt" möglich (überall "nein, nicht prüfbar"), keine Aussage wird von mir auf Stufe V gehoben.
Skripte: `batch_check.py --tina`: einzige Lücke bei allen 10 Blöcken ist Feld 11 (Ampel, Tinas Feld); sonst formal vollständig. `crm_abgleich.py` für alle 10 Firmen samt Konzern, Schwester, Marke selbst ausgeführt (siehe je Firma). Verifikationsdatum aller Einträge: 2026-10-15.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel (vorläufig) | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | Asyril GmbH (524) | GELB | 5 | ja |
| 2 | ATEG Automation GmbH (123) | GELB | 5 | nein |
| 3 | Autec Sondermaschinenbau GmbH (226) | GELB | 5 (Aspekt Zeile 2 offen) | ja |
| 4 | Bahrmann GmbH (239) | GELB | 5 | nein |
| 5 | BAT Maschinenbau GmbH (418) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 6 | Benedict* (435) | GELB | 2 | ja |
| 7 | Berghof Automation GmbH (223) | GELB | 5 | nein |
| 8 | Bluhm Systeme GmbH (720) | GELB | 5 | ja |
| 9 | BWH Elektro-Vertriebs-GmbH (218) | GELB | 2 | nein |
| 10 | Camozzi Automation GmbH (245) | GELB | 5 | nein |

Summe: Grün 1, Gelb 9, Rot 0. Kein Rot, weil kein harter Ausschluss E1 bis E4 mit Stufe V belegt werden konnte (Asyril E3, ATEG und Bahrmann E2 sowie BWH E2 sind nur Verdacht aus Snippets).

Patentprüfung (Regel F5), gilt für alle 10: NICHT vollständig nachholbar. Espacenet, DEPATISnet und Google Patents waren für mich nicht erreichbar (siehe oben). Ersatz: pro Firma eine bis zwei Websuchen mit Anmeldernamen und Verguss-Stichwörtern (nur Camozzi, Benedict, Bluhm, Berghof neu; für Asyril, ATEG, Autec, Bahrmann, BAT keine eigene Patentsuche, nur Toms Websuchen übernommen). Ergebnis: kein Patent der Firmen gefunden. Das ist ein schwacher Negativbefund und kein Gegenbeweis; Rechtsstände nicht erhoben. Einzige Auffälligkeit: Benedict, siehe dort (AT187967B, "Elektro Werkstaetten Benedikt", andere Schreibweise, nicht zugeordnet). Laut Regel F5 gilt der Batch damit als UNVOLLSTÄNDIG im Feld 9; die Ampeln stehen unter diesem Vorbehalt und sind "vorläufig". Direktabfragen sind mit Browser nachzuholen.
Wettbewerbereinsatz (Feld 16, Regel F6): wettbewerber_referenzen.md enthält keinen der 10 Namen (Asyril, ATEG, Autec, Bahrmann, BAT, Benedict, Berghof, Bluhm, BWH, Camozzi; Tom per Grep, ich nicht erneut). Einzelsuchen konnte ich aus dem Budget nur teilweise wiederholen (Camozzi, Berghof, Benedict, Bluhm jeweils im Rahmen der Fertigungssuche, ohne Hinweis). Bei Asyril, ATEG, Autec, Bahrmann, BAT, BWH bleibt Feld 16 inhaltlich leer ("kein Hinweis gefunden", Stufe ?, ohne Wettbewerber-Einzelsuche). Hat keinen Einfluss auf die Ampel.

---

## 1. Asyril GmbH | Stand 524 (Halle nicht angegeben)
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 5, Fertigungsbeleg fehlt).** Asyril GmbH Offenburg existiert als deutsche Gesellschaft (Technikzentrum und Showroom seit Oktober 2023, Max-Planck-Straße 1, Leitung Alexander Roller; S, Suchzusammenfassung von asyril.com/news/strengthened-presence-in-germany). Montage oder Produktion der Asycube in Offenburg ist nicht belegt; Fachpresse nennt Asyril einen Schweizer Hersteller ("Switzerland-based manufacturer", industrial-production.de, S). Bei belegter Fertigung in Offenburg wäre es mit Verguss Mittel (A) Grün; ein Konzern-/Tochterfall verlangt Stufe V (Sitzregel nicht anwendbar).
- Korrekturen an Toms Feldern: Feld 10 "kein Fertiger" ist als Einstufung zu hart. Harter Ausschluss E3 (Fertigung ausschließlich außerhalb DE/AT/NL) ist plausibel, aber nur Stufe S, daher nicht Rot. Feld 17 bleibt teilweise belegt: Identität der Asyril GmbH durch die Firmen-News gestützt (S), Register/Impressum nicht gelesen. Feld 9: Patentlage nicht verändert (Tom: kein Verguss-Patent; Direktabfrage fehlt, auch bei mir).
- CRM: neu (crm_abgleich.py "Asyril GmbH", "Asyril SA", "CPA": kein Treffer). Verguss (höchstes Bauteil): Mittel (A, Antriebselektronik der Vibrationsplattform, Steuerung).
- Zitat im Browser bestätigt: nein (nicht prüfbar).
- Nachrecherche-Auftrag (Gelb): Wird die Asycube (Antrieb, Elektronik) in Offenburg montiert oder nur in Villaz-St-Pierre (CH)? Wo nachsehen: Impressum und Karriereseite der Asyril GmbH (asyril.com), Stellenanzeigen Offenburg (Montage/Produktion/Elektronik), Datenblatt Asycube (Herkunftsangabe "Made in Switzerland"?). Wenn nur Vertrieb, Service und Tests in Offenburg: ROT nach E3/E2 mit Quelle. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen (A/S/?): Fertigung in Offenburg (nicht belegt); Verguss aller Bauteile (A); "develops, produces and markets" (S, bezieht sich auf die Schweizer SA); Zugehörigkeit zur CPA-Gruppe (Triage, unverifiziert); Registerdaten (S).
- Stichprobe für Jey: ja (E3-Entscheidung; ein Beleg zur Fertigung genügt, um Rot oder Grün zu setzen).

## 2. ATEG Automation GmbH | Stand 123
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 5).** Eigenfertigung in Remscheid ist unbelegt; das Messeprofil beschreibt die Firma als 1995 gegründete Vertriebsgesellschaft für Automatisierungskomponenten mit herstellerübergreifender Beratung (S, Suchzusammenfassung des aaa-Profils, Düsseldorf 2024). Das spricht stark für E2 (Händler/Vertrieb), ist aber nur S und nicht Rot. Verzeichniseintrag nennt zugleich Terminals, Folientastaturen, Gateways, ohne "Hersteller".
- Korrekturen: Feld 10 "unwahrscheinlich" bestätigt; Feld 9 unverändert (keine Direktabfrage). Feld 17: Intzestraße 50, 42859 Remscheid, Geschäftsführer Stefan Glaubitz (Verzeichnis, S); Register HRB 11800 Wuppertal (Toms Angabe, nur Verzeichnis, S).
- CRM: neu (crm_abgleich.py "ATEG Automation GmbH": kein Treffer). Verguss (höchstes Bauteil): Mittel (A, nur bei Eigenfertigung von HMI-Elektronik/Folientastaturen).
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): Hat ATEG eine eigene Produktlinie (Eigenmarke, "Made in Germany", Montage) oder nur Handel? Wo nachsehen: ateg.de Produktseiten und Impressum, Stellenanzeigen Remscheid (Montage/Fertigung). Nur Handel: ROT nach E2 mit Quelle. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Eigenfertigung (?), Verguss/Verklebung (A), Verzeichnisdaten (S). Stichprobe für Jey: nein.

## 3. Autec Sondermaschinenbau GmbH | Stand 226
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 5; zugleich offener Aspekt Zeile 2).** Sondermaschinenbauer am Sitz Amberg (Montage-/Prüfautomaten für Automotive, Elektro, Medizintechnik), aber Teil der "AUTEC Gruppe" (Stellenanzeigen und Messeprofil: inhabergeführte, mittelständische Gruppe mit Hauptsitz Amberg; S). Bei Konzern/Gruppe verlangt die Sitzregel Stufe V, die fehlt; deshalb nicht Zeile 4, obwohl Verguss Mittel (A, verbaute Antriebe, Sensorik, Steuerungen).
- Korrekturen: Feld 17: Toms Registerwiderspruch (Oskar-von-Miller-Straße 7 aus einem OpenRegister-Snippet unter verkürztem Namen "Sondermaschinenbau GmbH") fand ich nirgends bestätigt; ProvenExpert, Bayern International, eBay-Profil und aaa-Profil nennen einheitlich An den Franzosenäckern 11, 92224 Amberg (S). Ein Register- oder Impressumeintrag ist nicht gelesen (Registernummer unbekannt), die Identität bleibt daher nur teilweise belegt. Der Widerspruch ist damit eher eine unzuverlässige Registerquelle als eine zweite Firma, aber nicht geklärt. Feld 9: Patente unverändert (Tom: keine; Direktabfrage fehlt).
- CRM: neu (crm_abgleich.py "Autec Sondermaschinenbau GmbH", "AUTEC Gruppe": kein Treffer). Verguss (höchstes Bauteil): Mittel (A).
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): (a) Welche Einheiten umfasst die AUTEC Gruppe und ist die Autec Sondermaschinenbau GmbH die Gesellschaft, die in Amberg baut? Wo nachsehen: Impressum der Firmenseite, Handelsregister Amberg (Adresse, HRB). (b) Montage-/Elektrikerstellen am Sitz Amberg als Beleg für den Fertigungsort (StepStone-Anzeigen nennen die GmbH bereits, S; Original lesen). Danach Grün (Zeile 4), wenn Fertigungsort V.
- Nicht verwendbare Aussagen: Fertigungsort (A/S), Mitarbeiterzahl 40 (S, Triage), Verguss aller Bauteile (A), Registeradresse Oskar-von-Miller-Straße (S, widersprüchlich). Stichprobe für Jey: ja (wahrscheinlicher Grün-Kandidat nach V-Beleg, Identitätswiderspruch klären).

## 4. Bahrmann GmbH | Stand 239
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 5).** "System provider" für Messtechnik mit Vertriebspartnern METRIX (USA), Ono Sokki (Japan), Dr. E. Horn (DE); die Messeprofile sagen nichts zu Eigenfertigung (S, zwei aaa-Profile, 1980 gegründet). Händlercharakter nicht ausgeschlossen, aber auch nicht belegt: kein Rot.
- Korrekturen: Feld 7 Niedrig/S bestätigt. Feld 9: Patentsuche bei Tom nur eine Websuche; meine Zusatzsuche zur Eigenfertigung ergab keine Patente und keinen Fertigungshinweis. Feld 17 teilweise belegt (Verzeichnis, S).
- CRM: neu (crm_abgleich.py "Bahrmann GmbH": kein Treffer). Verguss: Mittel (A, bedingt; Sensoren/Ex-Schutz-Geräte stammen von Partnern).
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): Entwickelt oder baut Bahrmann eigene Systeme (Auswertegeräte, Ex-Schutz-Gehäuse, Schaltschränke) in Gärtringen? Wo nachsehen: bahrmann.de Produktseiten und Impressum, Stellenanzeigen (Montage, Elektronik), Messeprofil aaa vollständig. Nur Vertrieb: ROT nach E2.
- Nicht verwendbare Aussagen: Eigene Produkte (?), Verguss der Partnersensoren (A, fremde Ware), Verzeichnisdaten (S). Stichprobe für Jey: nein.

## 5. BAT Maschinenbau GmbH | Stand 418
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GRÜN, schwach (Tabellenzeile 4).** Sondermaschinenbauer mit eigenen Produkten (Zuführtechnik, Schrauben-/Mutternzuführung, Montageautomaten, Bildverarbeitung) am Sitz Meinerzhagen, gegründet 1999, kein Konzern erkennbar, kein Hinweis auf Auslagerung: Sitzregel erfüllt (Fertigung Hoch, A). Eine Fachpresse-Notiz nennt "mehr als 500 Automationssysteme projektiert, gebaut, produziert und montiert" (industrial-production.de, S). Verguss Mittel (A, Endprodukt-Regel: verbaute Antriebe, Sensorik, Steuerungselektronik).
- Korrekturen: keine an Toms Werten (Fertigung Hoch A, Verguss Mittel A bestätigt). Feld 9 unvollständig (Tom nur eine Websuche, ich keine Direktabfrage): Grün steht unter Patent-Vorbehalt.
- CRM: neu (crm_abgleich.py "BAT Maschinenbau GmbH": kein Treffer). Zitat im Browser bestätigt: nein (Impressum nicht lesbar). Eigene Stellensuche (Meinerzhagen, Elektriker/Monteur): keine Anzeige von BAT gefunden, kein Gegenbeleg.
- Nicht verwendbare Aussagen: Fertigungsort Meinerzhagen (A/S, Sitzregel), Verguss aller Bauteile (A), Registerdaten (nicht belegt), Gründungsjahr (S). Nachrecherche (empfohlen, kein Gelb): Impressum/Register (Amtsgericht, HRB), Stellenanzeigen Elektrik/Montage, ob Steuerungen im Haus aufgebaut werden.
- Stichprobe für Jey: ja (Grün stützt sich nur auf Sitzregel A plus Produkttyp A; Patent- und Impressumsprüfung fehlen).

## 6. Benedict* | Stand 435 (Messeliste: 42489 Wülfrath)
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 2, Identität).** Alle gefundenen Quellen verorten Benedict in Wien (BENEDICT GmbH, Lieblgasse 7, 1220 Wien, Firmenbuch 67832d, Eintragung 1993, Stammkapital 220.000 EUR, Geschäftsführer Alexander Benedict; evi.gv.at und advantageaustria.org, S). Keine Quelle verbindet Benedict mit Wülfrath. Der Messename "Benedict*" mit Sternchen ist unaufgelöst. Aus meiner Suche: Die aaa-Seiten anderer Messeorte führen "Benedict GmbH" und "Benedict GmbH*" (Friedrichshafen, Wels, Berlin; S): das Sternchen taucht dort ebenfalls auf und deutet auf ein Messe-Kennzeichen, nicht auf eine zweite Firma. Das ist nur ein Hinweis, kein Beleg.
Wäre die Einheit Wien bestätigt, ergäbe sich Grün (Zeile 4): Fertigung Wien Hoch (A nach Sitzregel, ergänzt um S "headquarters and production lines located in Vienna"), Verguss Hoch (A, Schützspulen/Magnetsysteme).
- Korrekturen: Feld 17 Abweichung bestätigt. Die PLZ 42489 Wülfrath der Messeliste ist nicht aufgelöst. Feld 3 (Gebiet) steht bei Wien = Österreich, aber unter Vorbehalt. Feld 9: Google-Patents-Treffer AT187967B (Schützanker-Lagerung) nennt als Anmelder "Elektro Werkstaetten Benedikt" (andere Schreibweise, nicht zugeordnet, nicht gezählt); AT510941 (Magnetvorrichtung) ohne erkennbaren Anmelder, nicht zugeordnet. Kein Verguss-Patent von Benedict gefunden.
- CRM: neu (crm_abgleich.py "Benedict GmbH", "Benedict": kein Treffer). Zitat im Browser bestätigt: nein. Wicklerei/eigene Spulenfertigung: in keiner Quelle genannt (S/offen).
- Nachrecherche-Auftrag (Gelb): (a) Ist der Aussteller "Benedict*" in 42489 Wülfrath die BENEDICT GmbH Wien (Messe-Sitz der Vertretung?) oder eine deutsche Vertriebsgesellschaft? Wo nachsehen: aaa-Ausstellerprofil mit Stand 435 (Adresse und Kontaktbereich), Impressum benedict.at, Standortseite (Vertretung Deutschland). (b) Fertigung Wien mit V: Firmenseite "Über uns/Produktion", Stellenanzeigen Wien. Aktion: nicht kontaktieren, bis die Einheit von Jey bestätigt ist.
- Nicht verwendbare Aussagen: Fertigung Wien (A, ergänzend S), Verguss Hoch (A), Zuordnung zu Wülfrath (keine), Mitarbeiterzahl 51 bis 200 (theorg, S). Stichprobe für Jey: ja (stärkster Grün-Kandidat des Batches, hängt nur an der Identität).

## 7. Berghof Automation GmbH | Stand 223
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 5).** Steuerungen, Industrie-PCs, Bedienpanels, I/O-Systeme und Prüftechnik mit Sitz Eningen. Berghof ist eine Firmengruppe mit weiteren Einheiten (Berghof Fluoroplastic Technology, Membrane Technology, Products + Instruments, Umweltengineering, Gigahertz-Optik; S) und die Berghof Automation hat laut Fachpresse die Standorte Mühlhausen und Eningen ("bleiben bestehen", industrial-production.de, S). Damit Gruppe/Mehrwerk: Stufe V für Eningen als Fertigungsort nötig, vorhanden ist nur S (Katalog-Zusammenfassung). Verguss Mittel (A: Steuerungselektronik, Panels, Netzteile).
- Korrekturen: Tom wies auf den Konzernabgleich hin; ich ergänze das zweite Werk (Mühlhausen), dem Tom keine Aussage zuordnet. Feld 17: Namensvarianten Berghof Automation GmbH / Berghof Automationstechnik GmbH (Adresse Arbachtalstraße 26 und Harretstraße 1) bleiben ungeklärt, möglicherweise Umzug oder Umfirmierung (S). Feld 9: Patente unverändert, keine Zuordnung (Anmelder Berghof nicht gefunden, Direktabfrage fehlt).
- CRM: neu (crm_abgleich.py "Berghof Automation GmbH", "Berghof Group", "Berghof Automationstechnik": kein Treffer; Konzernabgleich M ausgeführt). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): Werden die Steuerungen und Panels in Eningen oder in Mühlhausen gefertigt? Wo nachsehen: Berghof-Automation-Katalog 2024 (PDF) und Seite "Produktion/Unternehmen", Impressum, Stellenanzeigen (Elektronikfertigung/Montage Eningen). Nach V-Beleg Grün (Zeile 4).
- Nicht verwendbare Aussagen: Fertigungsort Eningen (S), Verguss/Lack/Optical Bonding (A), Registerdaten (nicht belegt). Stichprobe für Jey: nein.

## 8. Bluhm Systeme GmbH | Stand 720
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 5).** Hersteller von Kennzeichnungssystemen (Inkjet, Laser, Etikettierer, Thermotransfer) mit Zentrale Rheinbreitbach und Teil der BluhmWeber-Gruppe mit vielen Standorten (Produktions- und Vertriebsstandorte u. a. in Österreich, Schweiz, Frankreich, Niederlande, Italien, Polen; S). Meine Suche liefert Hinweise auf Produktion am Sitz (Fachmesse-Interview 2022: alle Systeme "in Rheinbreitbach" produziert, von Inkjet bis Laser und RFID; eigene Etikettenproduktion am Hauptsitz; Entwicklung Markoprint-Inkjet mit Team in Lübeck; alles S, nicht selbst gelesen). Gruppenfall verlangt Stufe V; Zitat nicht im Wortlaut gelesen. Verguss Mittel (A: Netzteile, Druckkopf-/Steuerelektronik; Block C nennt Etiketten Niedrig, die Geräte aber nicht).
- Korrekturen: Feld 7 Mittel/S bestätigt, Tendenz nach oben, sobald eine V-Quelle gelesen ist. Zur Weber-Rohtreffer-Frage (Toms Kopfvermerk): crm_abgleich.py mit "Weber Marking Systems" findet nur "Weber Elektronik GmbH [DE]" (bekannte_firmen_DE-AT-NL.txt Zeile 2548, Wortwurzel) und "Weber GmbH & Co. KG [DE]" (Zeile 2549, Präfix), beide ohne Ortsangabe in der Textliste. Die Marke Weber Marking Systems gehört zur BluhmWeber-Gruppe (weber-marking.com, Standortseite, S). Eine Identität der CRM-Einträge mit der Marke ist nicht belegt, aber nicht ausgeschlossen: Regel M verlangt bei Konzernbezug Gelb, daher steht diese Prüfung im Auftrag. Feld 17: Implisense nennt Handel mit Druckmaschinen, die Herstellerprofile (Bionity, Pressetexte) dagegen "develop, design and produce"; der Widerspruch ist eine Aggregator-Einordnung. Feld 9: eine Websuche ohne Treffer, Gruppennamen und Erfinder (Bluhm) nicht abgefragt.
- CRM: neu (crm_abgleich.py "Bluhm Systeme GmbH", "BluhmWeber": kein Treffer; "Weber Marking Systems": zwei Rohtreffer, siehe oben). Triage-Hinweis "bei MOTEK zurückgestellt laut Memory": im Repo steht dazu nur dieser Vermerk in triage_01.md und aaa_batches_v2/pruef_01.md, keine Quelle; unverifiziert. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): (a) Fertigung der Geräte in Rheinbreitbach mit V belegen: Bluhm-Seite "Unternehmen/Produktion", Stellenanzeigen Montage/Elektronikfertigung (StepStone Rheinbreitbach). (b) Zählen "Weber GmbH & Co. KG" und "Weber Elektronik GmbH" im CRM zu BluhmWeber (Ort der CRM-Datensätze, Jey)? (c) Ob ein MOTEK-Vorlauf besteht (Jey). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Rheinbreitbach (S), Verguss aller Bauteile (A), Gründungsjahr 1968 (S), Mitarbeiter-/Umsatzangaben (nicht geprüft). Stichprobe für Jey: ja (CRM-Wurzel "Weber", MOTEK-Vermerk).

## 9. BWH Elektro-Vertriebs-GmbH | Stand 218
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Eigene Suche "BWH Elektro-Vertriebs" Wuppertal: keine Seite, kein Register, kein Impressum, kein Verzeichniseintrag (wie bei Tom). Die einzige Quelle ist die Messeliste (aaa_duesseldorf_2026.csv, Zeile 30: Stand 218, 42329 Wuppertal). Der Name deutet auf Vertrieb (E2), das reicht ohne Beleg nicht für Rot.
- Korrekturen: keine; Felder 4 bis 8 bleiben "unbekannt/Stufe ?". Feld 8 "Niedrig" bedeutet "nicht belegt", nicht "widerlegt" (Toms Kennzeichnung korrekt, bei Tabellenzeile 6 nicht anzuwenden). Feld 9 nur eine Websuche, ohne Identität sinnlos.
- CRM: neu (crm_abgleich.py "BWH Elektro-Vertriebs-GmbH", "BWH": kein Treffer). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): Welche Firma steht hinter "BWH Elektro-Vertriebs-GmbH" (Rechtsform, Adresse, Geschäftszweck, Website)? Wo nachsehen: aaa-Ausstellerprofil Stand 218, Handelsregister Wuppertal (gemeinsames Registerportal), Unternehmensregister. Ist sie reiner Vertrieb: ROT nach E2 mit Quelle.
- Nicht verwendbare Aussagen: alle Produkt-, Fertigungs- und Verguss-Aussagen (?). Stichprobe für Jey: nein (Messeprofil/Register reichen).

## 10. Camozzi Automation GmbH | Stand 245
*ohne Browser/Web-Abruf geprüft, vorläufig*
**Ampel: GELB (Tabellenzeile 5).** Deutsche Niederlassung der Camozzi Group (Brescia) in Albershausen, vor rund 38 Jahren als Niederlassung mit Schwerpunkt Verbindungstechnik für Fluidtechnik gegründet, 55 Mitarbeiter, spezialisiert auf Pneumatik, Steuerungstechnik, elektrische Automatisierung (Wirtschaftsforum-Interview, S). Keine Quelle für Montage oder Produktion am Standort; Fertigungsangaben beziehen sich auf die Gruppe (17 bis 25 Werke, widersprüchlich, 2018). Gruppen-/Tochterfall: Sitzregel nicht anwendbar, Stufe V nötig. Verguss Hoch (A, Magnetventilspulen der Gruppe), gilt aber für Konzernprodukte, nicht für Albershausen.
- Korrekturen: Feld 7 Niedrig/S ist vertretbar, aber "Vertriebs-/Servicetochter" ist ebenfalls nur Triage/S; deshalb Gelb (Zeile 5) statt harter Ausschluss. Feld 17: Verwechslung mit der österreichischen Camozzi Automation GmbH (Hall in Tirol, FN 275106v) ausgeschlossen: andere Einheit. Feld 9: eine Websuche ohne Anmelder-Treffer; meine zwei Zusatzsuchen (Spule, Anmelder Camozzi) ergaben ebenfalls nur Händlerseiten. Camozzi-Spulen U7 mit "Encapsulating material PET" laut Händlerseite (S): nur Hinweis auf gekapselte Spule, kein Patent.
- CRM: neu (crm_abgleich.py "Camozzi Automation GmbH", "Camozzi Group", "Camozzi": kein Treffer; Konzernabgleich M ausgeführt). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): Gibt es Montage oder Fertigung (z. B. Ventilinseln, Steuerungen, Konfektion) in Albershausen? Wo nachsehen: camozzi.de Impressum und Standortseite, Stellenanzeigen Albershausen (Montage/Produktion/Logistik), Gruppen-Werkliste (camozzi.com). Nur Vertrieb/Service: ROT nach E2 mit Quelle (Zeile 1).
- Nicht verwendbare Aussagen: Fertigung Albershausen (?), Verguss/Spulen am Standort (A, Gruppenprodukt), Mitarbeiterzahl Gruppe (S, 2018), Geschäftsführer-Datum 2018 (veraltet). Stichprobe für Jey: nein.

---

## Konsistenz und Auffälligkeiten
- Tom hat in allen 10 Blöcken sauber auf die Quellenlage hingewiesen; Stufen S/A korrekt. Keine einzige V-Aussage, daher keine Herabstufung nötig. Tom vergab keine Ampel (Feld 11 leer, wie vorgesehen).
- Auffällig: Fünf von zehn Firmen stehen nur wegen fehlendem Stufe-V-Beleg bei Konzern/Gruppe (Berghof, Bluhm, Camozzi, Asyril, Autec) auf Gelb. Wären die Fertigungsbelege per Browser lesbar, wären Berghof, Bluhm und Autec wahrscheinliche Grün-Kandidaten.
- Messe-Signal: kein Wettbewerber (E1) in der aaa-Ausstellerliste (laut Tom per Grep; "Panasonic Industry Europe" nur wegen "Ottobrunn" ein Fehltreffer).
- Neuer Fehlertyp zur Aufnahme in fehlerlog_lehren.md (nicht eingetragen, Jey gibt frei): Registerabfragen unter verkürztem Firmennamen (Autec: "Sondermaschinenbau GmbH") liefern fremde Treffer und dürfen keinen Identitätswiderspruch begründen, solange die volle Firma nicht gelesen ist.

## Klärungsbedarf Jey (Zusammenfassung)
1. Benedict*: Ist der Aussteller in Wülfrath die BENEDICT GmbH Wien (Lieblgasse 7)? Dann Grün.
2. Bluhm Systeme: Gehören "Weber GmbH & Co. KG" (Zeile 2549) und "Weber Elektronik GmbH" (Zeile 2548) im CRM zur BluhmWeber-Gruppe (Ort der CRM-Datensätze)? Besteht ein MOTEK-Vorlauf?
3. Autec: AUTEC Gruppe, Gesellschaft und Adresse (Franzosenäckern 11 oder Oskar-von-Miller-Straße 7) bestätigen.
4. Asyril: E3-Entscheidung nach Fertigungsbeleg (Offenburg nur Technikzentrum?).
5. BWH Elektro-Vertriebs-GmbH: Identität; ob Aufwand lohnt (vermutlich Vertrieb).

## Einschränkungen
- Browser (Chrome) nicht verfügbar; WebFetch nicht nutzbar (DNS-Fehler); curl-Test auf Espacenet, DEPATISnet, Google Patents und batmaschinenbau.de ohne Verbindung, kein Umgehungsversuch. Alle Aussagen von mir beruhen auf WebSearch-Zusammenfassungen (20 Abfragen, 0 Seiten im Wortlaut gelesen). Keine Quelle wurde im Browser gegengelesen, keine Grün-Kandidatin (BAT) nach Regel O/I vollständig geprüft: Ampel Grün ist vorläufig.
- Pflicht-Patentrecherche (F5) nicht erfüllt: weder Google Patents noch Espacenet noch DEPATISnet direkt abgefragt; Feld 9 für alle 10 Firmen Websuche-Niveau, Rechtsstände nicht erhoben. Der Batch ist in Feld 9 UNVOLLSTÄNDIG.
- Feld 16 (Wettbewerbereinsatz): Einzelsuchen mit Wettbewerbernamen nur für Camozzi, Berghof, Benedict, Bluhm (Tom) bzw. gar nicht (Asyril, ATEG, Autec, Bahrmann, BAT, BWH).
- Handelsregister/Unternehmensregister nicht abgerufen (Impressen und Registernummern nur aus Verzeichnissen/Snippets, Stufe S).
- Datenbankfelder nicht geändert, nichts verschickt, nichts committet. Kundendatenbank (xlsx) nicht lesbar; kundendatenbank_export.txt ohne Treffer für alle 10 Firmen, daher keine "Verifiziert am"-Prüfung. Größe/Umsatz und Kontakte nicht geprüft (Regeldatei D, K).
