# Tina Batch 44 – electronica 2026 (Prüfung von tom_batch_44.md)
Erstellt: 2026-10-20 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe: ausschließlich electronica/ergebnisse/tom_batch_44.md (10 Firmen).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (23 Abfragen, Kurzfassungen/Snippets) und Bash zur Verfügung; WebFetch und Chrome nicht nutzbar. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün ist mailtauglich.
Skripte: `python3 batch_check.py electronica/ergebnisse/tom_batch_44.md` = VOLLSTÄNDIG (10 Blöcke; erkennt nur Felder, nicht die fehlende Datenbankabfrage F5). `python3 crm_abgleich.py` für alle Firmen (auch PTW SpinTec) selbst wiederholt: überall "kein Treffer, neu". Tabellenzeile = Zeilennummer der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum aller Einträge: 2026-10-20.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | PROVERTHA Cables Connectors & Solutions GmbH (B3.100) | GELB | 5 | ja |
| 2 | PTW Asia Pte Ltd (B1.120) | GELB | 2 | nein |
| 3 | Puerstinger High Purity Systems GmbH (B1.761) | GELB | 2 | nein |
| 4 | Pure Gas Engineering GmbH (C2.135) | GELB | 7 | nein |
| 5 | PVA TePla AG (C1.301) | GELB | 5 | ja |
| 6 | Q-Lab (C3.358) | GELB | 2 | ja |
| 7 | Qnity (B3.340) | GELB | 2 | ja |
| 8 | QUASYS GmbH (B1.164) | GELB | 2 | ja |
| 9 | R&A ELECTRONICS GmbH (C2.425) | GELB | 2 | ja |
| 10 | Ramgraber Semiconductor Equipment GmbH (B1.171) | GRÜN (schwach) | 4 (Sitzregel) | ja |

Zahlen: Grün 1, Gelb 9, Rot 0. Kein Rot, weil E1 bis E3 nirgends mit Stufe V belegt ist (Tabellenzeile 1 verlangt V). Rot-Kandidaten bei Bestätigung: R&A (E2), QUASYS (E2), Q-Lab (E3/E2), PTW Asia (E3), Qnity (E1), Puerstinger/Pure Gas (E2).
Messe-Signal (Regel N, aus Toms Grep, nicht von mir wiederholt): bdtronic, RAMPF (beide Gesellschaften), ELANTAS stellen aus; ändert keine Ampel.
Patente (F5): Google Patents, Espacenet, DEPATISnet nicht abfragbar. Batch bleibt nach F5 UNVOLLSTÄNDIG; Websuche-Wiederholungen bei Provertha, PVA TePla, Ramgraber unten. Wettbewerbereinsatz (F6): wettbewerber_referenzen.md von mir nur Zeilen 1 bis 378 gelesen (Rest per Grep nicht erneut geprüft, Tom meldet ganze Datei ohne Eintrag); keine Einzelsuche ergab einen Hinweis.

---

## 1. PROVERTHA Cables Connectors & Solutions GmbH | B3.100
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, mit Hinweis auf Fertigung im Ausland).** Pforzheim ist laut Suchergebnissen Headquarter mit Distribution, Entwicklung, Versand; die Kabel- und Steckerfertigung liegt laut Firmenmeldung (UL-Hinweis) in Ungarn (Sárvár, Beled, Kapuvár). Verguss Hoch (A, umspritzte Sensorstecker, Kabelkonfektion), aber Fertigungsbeleg DE fehlt und es gibt einen Auslandshinweis; Stufe V nötig. E3 nicht Rot, da nur Stufe S.
- Eigene Prüfung: WebSearch bestätigt "over 850 people ... in the head office in Pforzheim and in the three manufacturing facilities ... Hungary" (provertha.de/en/?p=26609, S); UL-Notiz "production of our cable products takes place in our plants in Hungary" (provertha.de/?p=2178, S); Katalog "Fertigung in Ungarn, Customer Service in Deutschland" (S). Keine Quelle für Montage in Pforzheim; Stellenanzeigensuche ohne Provertha-Treffer (nur Randstad-Treffer anderer Kunden). Eigentümer: Familie Szalay, 100 % privat (S), kein Konzern im CRM-Sinn. Patente: Website nennt patentierte M12-Press-Fit-Steckverbinder, Flexlock, Quick-Lock, Wire-Clip (S); Patsnap nennt 30 Patente (Drittangabe, nicht geprüft); keine Nummern, kein Rechtsstand, kein Verguss-Bezug erkennbar.
- Korrekturen an Toms Feldern: Feld 7 "Mittel" ist zu hoch angesetzt; mit Auslandshinweis eher Niedrig bis Mittel (S). Feld 9: Patentzahl/Produktpatente ergänzt (Tom: "kein Patent, nur teilweise patentiert"). Feld 10 "prüfenswert" bleibt höchstens vorläufig. Feld 17 Namensreihenfolge (Connectors, Cables & Solutions) bestätigt, keine Identitätsabweichung.
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Werden Steckverbinder oder Kabelkonfektion in Pforzheim gefertigt/montiert, oder ist Pforzheim nur Entwicklung/Vertrieb? Wo nachsehen: Standortseite provertha.de/en/company (Funktionen je Standort), Impressum, Stellenanzeigen am Sitz (Montage/Fertigung), Produktseite Sonderstecker (?p=25219) auf "Made in"/Werk. Zusätzlich: Werden die umspritzten Stecker harzvergossen oder nur thermoplastisch umspritzt (Datenblatt)? Aktion: Beobachtung, vor Klärung nicht priorisieren.
- Nicht verwendbare Aussagen: Fertigung Pforzheim (nicht belegt, Hinweis auf Ungarn); Verguss aller Bauteile (A); Umspritzen = Verguss (A, falsch möglich); Mitarbeiterzahl (S, widersprüchlich 500/850); Patentzahl 30 (S, Drittquelle). Stichprobe für Jey: ja (Toms Einstufung "prüfenswert" stützt sich auf unbelegte Fertigung).

## 2. PTW Asia Pte Ltd | B1.120
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Die Exportliste führt Land Deutschland, gefunden ist eine Singapurer Gesellschaft (Refurbishing/Service für Halbleiter-Nassprozessanlagen, SEMI-Verzeichnis, S). Verbindung zur PTW SpinTec GmbH (Villach, Österreich, OEM Single-Wafer-Nassätzen, SEMI-Eintrag, S) ist laut Suche plausibel (Gruppe mit Centres of Excellence in Österreich, Singapur, Philippinen, Taiwan, S), Eigentum aber nicht belegt. Verguss Niedrig (A, Service/Ersatzteile).
- Eigene Prüfung: crm_abgleich "PTW Asia", "PTW SpinTec", "PTW": neu. E3/E2 (Service, Sitz Singapur) nicht Stufe V belegt, daher nicht Rot. Die Firma, die in AT fertigt (PTW SpinTec GmbH), ist eine andere Einheit und nicht bewertet.
- Korrekturen: keine inhaltlichen; Feld 12 bestätigt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer stellt in B1.120 aus (PTW Asia Singapur oder PTW SpinTec Villach)? Gehört PTW Asia zu PTW SpinTec? Wo nachsehen: electronica-Ausstellerseite B1.120, SEMI-Eintrag PTW SpinTec GmbH, ACRA/Handelsregister Villach. Wenn PTW SpinTec die fertigende Einheit ist, getrennt als eigene Firma prüfen (Nassprozessanlagen: Heizungen, Sensorik, Steuerung, Verguss Mittel A möglich). Aktion: nicht priorisieren, bis Einheit geklärt.
- Nicht verwendbare Aussagen: Sitz/Fertigung (S); Gründung Österreich 2007 (S, Jobportal); Mitarbeiterzahl 55 (S). Stichprobe für Jey: nein.

## 3. Puerstinger High Purity Systems GmbH | B1.761
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Meine Suche fand keine Firmenseite, kein Impressum und keinen Treffer außer dem einen Verzeichnis (Tom) bzw. nur ähnlich benannte andere Firmen (High Purity Systems US, INTEGA, SEMPA; nicht vermischt). Firma damit nicht belegt auffindbar; Tätigkeit nur aus einem Verzeichnis (S). Fertigung/Verguss Niedrig (A/S).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Existiert die Gesellschaft in Burghausen mit welcher Tätigkeit (Anlagenbau vs. Rohrleitungsbau), und gibt es Eigenfertigung (Gasschränke, Steuerungen)? Wo nachsehen: Handelsregister Traunstein/Unternehmensregister, electronica-Ausstellerprofil B1.761, Website über Impressum. Bei Dienstleister ohne Eigenprodukte: Rot nach E2 mit Quelle. Aktion: nicht weiter verfolgen.
- Nicht verwendbare Aussagen: Sitz, Tätigkeit, Fertigung (S/?). Stichprobe für Jey: nein.

## 4. Pure Gas Engineering GmbH | C2.135
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Nur der SEMI-Eintrag (Dresden, Hertha-Lindner-Straße, Mitglied seit 19.05.2026; "complete gas engineering solutions", Wartungsservice, S) wurde wiedergefunden. Engineering/Service, vermutlich E2 (Beratung/Design), aber nicht mit V belegt; Zeile 1 verlangt V, Zeile 6 setzt belegte Fertigung voraus, daher Zeile 7.
- Korrekturen: keine. Tom schlug "keine Nachrecherche" vor; Gelb verlangt einen Auftrag, siehe unten. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Hat die Firma eigene Produkte/Fertigung (Gasschränke, Panels) oder ist sie reiner Engineering-/Servicedienstleister (E2)? Wo nachsehen: Impressum/Website (nicht gefunden, über SEMI-Eintrag oder electronica-Ausstellerseite C2.135), Handelsregister Dresden. Aktion: nicht weiter verfolgen, bei Bestätigung Rot E2.
- Nicht verwendbare Aussagen: alle Tätigkeitsangaben (S, ein Verzeichnis). Stichprobe für Jey: nein.

## 5. PVA TePla AG | C1.301
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Identität stimmt (Im Westpark 10-12, 35435 Wettenberg, S). Konzern mit mehreren Werken (vier Standorte in Deutschland, Werk Marano Vicentino/Italien für Prozesskammern, S), daher Stufe V für Fertigung nötig. Belegt (S): Wettenberg "central administration and largest production site"; Stellenanzeige "Meister Produktion Elektromontage" der PVA Metrology & Plasma Solutions GmbH in Wettenberg; Ausbau von Produktions- und Logistikhalle am Hauptsitz. Verguss Mittel (A, Generatoren/Heizelemente/Sensorik/Steuerelektronik der Anlagen), ohne Beleg, welche Baugruppe in Wettenberg entsteht; Eigenfertigung von Generatoren/Heizelementen laut meiner Suche nicht belegt.
- Eigene Prüfung: Patente (Websuche): keine Verguss-/Encapsulation-Patente gefunden; Aggregator nennt 12 Patente, Themen Halbleiter/Kristallzucht (S, Drittquelle). Anmelder-Varianten (Tochter-GmbHs) mit Datenbankabfrage offen. PVA (pva.net, US-Dosieranlagenhersteller) ist eine andere Firma, nicht vermischt. CRM Konzern/Töchter: neu.
- Korrekturen: Feld 4 ergänzt: Standort Wettenberg ca. 340 Beschäftigte (Stellenanzeige, S); Italien-Werk mit Kernkomponenten Prozesskammern (nicht in Toms Feld). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Welche Anlagen/Baugruppen werden in Wettenberg tatsächlich montiert (Elektromontage der PVA Metrology & Plasma Solutions GmbH: Steuerschränke, Generatoren, Sensorik?) und enthalten sie vergossene/verklebte Teile? Wo nachsehen: Stellenanzeige Elektromontage im Original, pvatepla.com Standortseite und Produktseiten Plasma-/Metrologie-Systeme, Datenblätter Ultraschall-Transducer, Patente der Töchter in Espacenet/DEPATISnet. Aktion: Beobachtung.
- Nicht verwendbare Aussagen: Fertigung Wettenberg (S, Konzern); Verguss aller Bauteile (A); Patentzahl 12 (S). Stichprobe für Jey: ja (börsennotierter Konzern, viele Werke).

## 6. Q-Lab | C3.358
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Liste: Oberhaching. Gefunden: Q-Lab Corporation (Westlake, Ohio; Pressemeldung 2017: QUV-Geräte "manufactured exclusively" in Westlake, S) und Q-Lab Deutschland GmbH (Saarbrücken: Vertrieb, Reparatur, Kalibrierung, Prüflabor, S). Ein Standort Oberhaching ist nicht belegt, ebenso kein Munich-Büro; Q-Lab Deutschland begann 2008 in Düsseldorf (S). Fertigung DE/AT/NL damit Niedrig (S); E3 nicht V-belegt (Quelle 2017, Stufe S), daher nicht Rot.
- Korrekturen: Feld 3/4 ergänzt: Fertigungsaussage "exklusiv Westlake" aus 2017 (S), nach Lehre 17 zu alt für ein Rot. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Welche Q-Lab-Gesellschaft stellt in C3.358 aus, und gibt es einen Sitz Oberhaching? Wo nachsehen: electronica-Ausstellerseite C3.358, Impressum q-lab.com/de-de, Handelsregister Saarbrücken (Q-Lab Deutschland GmbH). Fertigungsort aktuell auf q-lab.com/company (Facilities) lesen; bei aktueller Quelle V "Produktion nur Ohio": Rot E3. Aktion: nicht weiter verfolgen.
- Nicht verwendbare Aussagen: Sitz Oberhaching (nicht belegt); Fertigung ausschließlich Westlake (S, 2017); Verguss Mittel (A, für DE ohne Bedeutung). Stichprobe für Jey: ja (Rot-Kandidat E3, nur Bestätigung nötig).

## 7. Qnity | B3.340
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Qnity Electronics, Inc. (Wilmington, Delaware; Ausgründung der DuPont-Elektroniksparte, November 2025, S) mit Laird-Marke Qnity Laird. Eine Rosenheimer Gesellschaft oder Qnity GmbH wurde nicht gefunden; europäische Fertigung Laird s.r.o. in Liberec (Tschechien, S), laut Wikipedia nur 2 Werke in EMEA (S). Hersteller 2K-dosierbarer Gap Filler (Tflex CR910/CR550, Datenblätter S): Materialhersteller im Demak-Umfeld, E1 im Sinne "Klebstoffe/Dichtstoffe/Vergussmassen" plausibel, aber Zuordnung nicht V-belegt, daher nicht Rot. Aufgrund Zeile 2 Gelb.
- Eigene Prüfung: crm_abgleich "Qnity", "Laird", "DuPont": neu (DuPont war Argument, kein Treffer). Fertigung DE/AT/NL: kein Beleg.
- Korrekturen: Feld 8 von Tom ("Niedrig, Lieferantenrolle") bleibt; Feld 4 Ergänzung Laird s.r.o. Liberec (S). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Welche Gesellschaft stellt in B3.340 aus (Rosenheim)? Gibt es eine deutsche Qnity/Laird-Einheit mit Fertigung? Wo nachsehen: electronica-Ausstellerseite B3.340 mit Impressum, qnityelectronics.com Standortliste, Handelsregister Traunstein. Entscheidung E1 durch Jey/Tina nach Produktseite (Wärmeleit-Gap-Filler als Dichtstoff/Vergussmasse-Äquivalent?). Aktion: nicht als Kunde ansprechen.
- Nicht verwendbare Aussagen: Sitz Rosenheim (nicht belegt); Beschäftigtenzahl 10.000 (S); Herkunft Laird-Pads (S, Händlerkatalog). Stichprobe für Jey: ja (E1-Einordnung).

## 8. QUASYS GmbH | B1.164
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Meine Suche bestätigt: keine QUASYS GmbH in Eichstetten auffindbar; gefunden nur Quasys AG, Hünenberg (CH), "kleines, international tätiges Handelsunternehmen" (Messeverzeichnis, S) für Feeder, Test-Sockets, Bonding-Tools, Verpackungsequipment. Handelsfirma, vermutlich E2, aber nicht V.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Gibt es eine QUASYS GmbH in 79356 Eichstetten, und wie steht sie zur Quasys AG (Hünenberg)? Wo nachsehen: electronica-Ausstellerseite B1.164, Handelsregister Freiburg, Impressum quasys.ch. Bei Bestätigung Handelsfirma: Rot E2 mit Quelle. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Existenz/Sitz der GmbH; "Handelsunternehmen" (S). Stichprobe für Jey: ja (Identität).

## 9. R&A ELECTRONICS GmbH | C2.425
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität).** Meine Suche fand keine Frankfurter GmbH; gefunden nur R&A Electronics, Shenzhen (Sourcing, randa.hk, Datanyze, S, gegründet 2015, ca. 150 Beschäftigte). Distributor/Broker, E2 inhaltlich stark, aber Zuordnung der Frankfurter Firma zu Shenzhen nicht belegt, daher kein Rot.
- Korrekturen: keine. Feld 12: "RA Electronics"-Ähnlichkeiten (0,89 bis 0,90) bestätigt als kein Treffer. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Existiert R&A ELECTRONICS GmbH in 60325 Frankfurt und was tut sie (Handel vs. eigene Fertigung)? Wo nachsehen: electronica-Ausstellerseite C2.425, Handelsregister Frankfurt, Impressum randa.hk. Bei Händler/Broker: Rot E2 mit Quelle. Aktion: nicht weiter verfolgen.
- Nicht verwendbare Aussagen: Sitz; Tätigkeit (S); Zuordnung zu Shenzhen (?). Stichprobe für Jey: ja (Rot-Kandidat E2).

## 10. Ramgraber Semiconductor Equipment GmbH | B1.171
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Sitzregel).** Eigenhersteller kundenspezifischer nasschemischer Anlagen (Nass-/Ätzanlagen, Galvanik, Ultraschallreinigung, Spin-Rinse-Dryer) mit Sitz Pappelstraße 2, Hofolding/Brunnthal (Bayern) und Zweigstandort Wutach (BW, beide DE). Gegründet 1972 (Anfangs Schaltschränke, Galvanik- und Ultraschallgeräte, S), Geschäftsführer Holger Koch, keine Konzernmutter in den Suchergebnissen (S), ca. 47 Beschäftigte (S, möglicherweise veraltet). Gerätebauer mit erkennbarem Standort, kein Händler, kein Auslagerungshinweis: Sitzregel Stufe A. Verguss Mittel (A: Füllstand-/Temperatursensoren, Heizungen, Steuerelektronik der Anlagen); Eigenverguss nicht belegt, zugekaufte Teile zählen.
- Eigene Prüfung: Identität: "Ramgraber Semiconductor Equipment GmbH" (SEMI) und "Ramgraber GmbH" (Bayern International, openregister-Treffer ohne Zuordnung) unter derselben Adresse, S. Montage-Stellenanzeige am Sitz nicht gefunden. Patente (Websuche): keine Anmeldertreffer; die Wet-Bench-Patente (US11961745, US11854841, US11482430) tragen laut Snippet keinen Anmelder Ramgraber (nicht zugeordnet, aussortiert). Datenbankabfrage offen. CRM: neu. Wettbewerbereinsatz: kein Hinweis (S/?).
- Korrekturen: Feld 4 ergänzt: Zweigstandort Wutach, historisch Schaltschrank/Galvanik. Feld 7 "Hoch A" bestätigt (nur Sitzregel, nicht V). Feld 10 "prüfenswert" ist nach Regel D konsistent mit Grün (Fertigung Hoch A + Verguss Mittel A wäre prüfenswert; Zeile 4 ergibt Grün). Zitat im Browser bestätigt: nein.
- Nachrecherche (empfohlen, kein Gelb): Impressum/Register Ramgraber (Rechtsform, Gesellschaftsname, Sitz = Fertigung, V), Stellenanzeige Montage/Elektrik Hofolding, Datenblatt Wet-Bench/Spin-Rinser-Dryer (Heizungen, Sensorik, Dichtungen), Patente Anmelder "Ramgraber" in Espacenet/DEPATISnet. Aktion: Beobachtung; Messebesuch B1.171 vorbereiten.
- Nicht verwendbare Aussagen: Fertigung Hofolding (A/S); Verguss aller Bauteile (A); 47 Beschäftigte/Umsatz unter 5 Mio. EUR (S, Verzeichnis); Gesellschaftsname (S). Stichprobe für Jey: ja (einziges Grün ohne V-Beleg).

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind überall korrekt als S/A geführt. Seine Einstufungen "kein Fertiger" bleiben vorläufig; kein Rot ohne V-Beleg.
- Abweichungen von Tom: Provertha Fertigung eher Niedrig (Hinweis auf Ungarn); PVA TePla Gelb statt Beobachtung; Pure Gas Engineering hat nach Gelb-Regel Auftrag; Ramgraber Grün (nach Zeile 4 mit Sitzregel).
- Vorschlag Fehlerlog (Jey gibt frei, nicht eingetragen): Bei Messelisten-Gesellschaften mit abweichendem Sitz (Q-Lab, Qnity, QUASYS, R&A, PTW Asia) vor Bewertung die ausstellende Gesellschaft über die Ausstellerseite klären; Auslandsfertigungs-Hinweise in Firmenmeldungen (Provertha UL-Notiz) schon in Tom-Lauf prüfen.

## Einschränkungen
- Browser und WebFetch nicht verfügbar: kein Gegenlesen nach Abschnitt H, kein Impressum, Register oder Datenblatt gelesen; alle Aussagen Stufe S oder A. Keine "Zitat im Browser bestätigt: ja".
- WebSearch: 23 Abfragen (Priorität: Provertha 4, PVA TePla 3, Ramgraber 4, Q-Lab 3, Qnity 3, QUASYS 1, R&A 1, PTW 1, Puerstinger 1, Pure Gas 1; Patent-Zusatzsuchen für Provertha, PVA TePla, Ramgraber). Ergebnisse sind Kurzfassungen; Aussagen zu Websites sind Suchzusammenfassungen.
- Patente (F5): Google Patents, Espacenet, DEPATISnet nicht abgefragt; Pflichtsuche nicht erfüllt, "kein Treffer" schwach. Anmelder-Varianten (PVA Metrology & Plasma Solutions, PVA Industrial Vacuum Systems, PTW SpinTec, Laird Technologies, Q-Panel) nicht per Datenbank gesucht; Rechtsstand der Laird-TIM-Patente (US9515004, US9260645) ungeprüft.
- Wettbewerbereinsatz (F6): wettbewerber_referenzen.md nur bis Zeile 378 von 631 gelesen; Toms Grep (Messe-Signal) nicht wiederholt; Einzelsuche nur bei Provertha, PVA TePla, Ramgraber (ohne Treffer).
- Handelsregister/Unternehmensregister nicht abgerufen. CRM-Abgleich per Skript wiederholt; Kundendatenbank-Aktualität nicht relevant (keine Treffer).
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
