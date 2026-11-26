# electronica 2026 - Browser-Prüfung Grün-Kandidaten, Durchgang 05 (Nr. 41 bis 46)

Stand 2026-10-22, Tina (Stufe 2, v2), Chrome get_page_text, nur lesend, eigener Tab. CRM-Abgleich (ein Skriptaufruf mit allen 6 Firmen plus Kurz-/Alt-/Schreibvarianten SRT, Thyracont, Toellner, Töllner, Winkler): 6 von 6 Firmen "kein Treffer -> neu"; zusätzlich Grep über wettbewerber_referenzen.md, kundendatenbank_export.txt und bekannte_firmen_DE-AT-NL.txt (alle sechs Namen): keine Treffer.
Regel 22.10.: Verbände/Prüfdienstleister/Forschung und CRM-Firmen scheiden aus, Anlagenbauer bleiben drin (Ausscheiden nur bei eigenen Verguss-/Dosieranlagen, E1 mit URL und Zitat). Keine der sechs Firmen baut oder vertreibt Dosier-/Vergussanlagen oder Vergussmassen/Klebstoffe: kein E1.
Patentwerkzeuge: Google Patents (patents.google.com/?assignee=...) und Espacenet (worldwide.espacenet.com, pa=..., Legacy-Ansicht); DEPATISnet nicht abgefragt (Sparmodus, zwei Datenbanken). Die Espacenet-Ansicht meldete bei Testsuche pa=srt AND txt=resistor Fremdtreffer (SRT INC), die Suche funktioniert also grundsätzlich; Rechtsstand je Treffer nur dort genannt, wo Treffer vorhanden.
Datenblatt-PDFs (SRT, rhopoint) waren im Browser und per WebFetch nicht als Text lesbar: Verguss durchgängig Stufe A.

---

## 41. SRT Resistor Technology GmbH (A6.300)
- Ampel neu: GELB. Tabellenzeile D: 7 (Fertigung Cadolzburg V belegt, aber Verguss am Produkt nur Niedrig bis Mittel (A) und ohne Datenblattbeleg; Z.4 verlangt Mittel/Hoch, Z.6 verlangt alle Bauteile Niedrig, beides nicht belegbar).
- Identität (V, 22.10.2026): https://srt-restech.de/impressum/ - "SRT Resistor Technology GmbH", "Am Farrnbach 10, 90556 Cadolzburg", "Handelsregister: HRB 1918, Registergericht: Fürth/Bayern". Stimmt mit Vorgabe (Cadolzburg) überein. Hinweis: Datenschutzerklärung nennt Ostlandstraße 31 (Altadresse, in Verzeichnissen ebenfalls). Zitat im Browser bestätigt: ja.
- Fertigung (V, 22.10.2026): https://srt-restech.de/unternehmen/ - "Entwicklung und Produktion spezieller Widerstände und Sonderprodukte"; "Schwerpunkt der Produktion liegt derzeit im Bereich der Hochohmwiderstände in Dickschichttechnik"; "Produktion am Standort Deutschland". Zitate im Browser bestätigt: ja. Einschränkung: Präzisions-/Leistungswiderstände und Keramik-Chipkondensatoren sind "Ergänzung zu unserer Eigenfertigung" von "namhaften Herstellern" (Handelsware); Joint Venture DoubleCircle in Bengbu/China seit 2005 (Fertigung dort nicht beschrieben). Eigenfertigung der Hochohm-/Hochspannungswiderstände in Cadolzburg damit plausibel, die Zuordnung Hochspannungsreihen (HVR/HVM/HVT/RIT/GST) zum Werk Cadolzburg nicht wörtlich belegt.
- Verguss/Klebung/Dichtung: Hochspannungswiderstände bis 80 kV (bedrahtet) und 6 kV (SMD) Mittel (A; Umhüllung/Isolation Lack/Epoxid/Silikon typisch, Aufbau nicht gelesen), Hochspannungsteiler HVT Mittel (A), Dickschicht-Chipwiderstände Niedrig (A), "klebbare Chipwiderstände für die Automobilelektronik" (S, Eigenschaft: Montage per Leitkleber beim Kunden, kein Vergussprozess des Herstellers). Maximum = Niedrig bis Mittel (A), schwach. Datenblätter HVR/HVM/HVT/RIT/GST (PDFs auf srt-restech.de/produkte/) nicht textlesbar.
- Patente: Google Patents (assignee "SRT Resistor Technology", 22.10.): keine Treffer. Espacenet (pa="srt resistor"; zweite Suche pa=srt AND txt=resistor, 22.10.): 0 Treffer bzw. nur Fremdtreffer (SRT INC, TV-Technik, aussortiert). Vorgängerfirma Siegert GmbH (MBO 1996) nicht gesucht. Kein Signal (kein Gegenbeweis).
- Wettbewerbereinsatz: kein Hinweis gefunden (Grep wettbewerber_referenzen.md; keine Einzelsuche, Sparmodus).
- Konzern/Werke: eigenständig ("ein eigenständiges Unternehmen"), ein Sitz Cadolzburg, JV in China. Kein CRM-Bezug.
- CRM-Status: neu.
- Offener Auftrag (Gelb): Wie sind die Hochspannungswiderstände (HVR, HVM, HVT, RIT, GST) umhüllt: Lack, Epoxid-/Silikon-Verguss, Glas, Formmasse? Datenblätter auf https://srt-restech.de/produkte/ (Links zu PDFs unter /pdf/datenblaetter/bedrahtete-widerstaende/) per Download durch Jey oder Text-Extraktion lesen. Wird Verguss/Vergussumhüllung (Epoxid/Silikon) belegt: GRÜN Z.4; sind es reine Lack-/Glasumhüllungen: Gelb Z.6 mit Frage an Jey, ob Bauelementehersteller ohne Vergussschritt Zielgruppe sind.
- Nicht verwendbare Aussagen: Verguss/Umhüllung der Hochspannungswiderstände (A); Zuordnung HV-Reihen zum Werk Cadolzburg (A).
- Stichprobe für Jey: ja (Bauelementehersteller, Verguss-Hebel unklar).

## 42. Thyracont Vacuum Instruments GmbH (C1.848)
- Ampel neu: GRÜN bestätigt (V Eigenproduktion, Sitzregel anwendbar). Tabellenzeile D: 4. Verguss nur A, daher schwächer belegt.
- Identität (V, 22.10.2026): https://thyracont-vacuum.com/impressum/ - "Thyracont Vacuum Instruments GmbH, Max-Emanuel-Straße 10, 94036 Passau", "Registergericht: Amtsgericht Passau, Registernummer: HRB 4409"; Geschäftsführer Plöchinger, Salzberger. Stimmt mit Vorgabe überein. Zitat im Browser bestätigt: ja.
- Fertigung (V, 22.10.2026): https://thyracont-vacuum.com/ - "Thyracont entwickelt und produziert innovative Vakuummessgeräte." und "Seit 1970. Made in Germany." Zitate im Browser bestätigt: ja. Ein Standort Passau erkennbar (Gründung 1970 durch Plöchinger, Garage im Bayerischen Wald; physicsworld/gasworld S). Keine Hinweise auf Konzern, weitere Werke oder Auslagerung.
- Verguss/Klebung/Dichtung: Vakuumtransmitter (Smartline, Analogline, USB, Mini-Transmitter) mit Elektronik im Metallgehäuse Hoch (A, Block A Transmitter/Drucksensoren; Datenblatt VCR-SL laut Suchtreffer S: "Schutzart bis IP54", Edelstahl-Messzelle metallgedichtet), passive Sensorköpfe (Piezo, Pirani, Kaltkathode) Mittel (A), Kompakt-Messgeräte VD800 mit Silikon-Schutzhülle Mittel (A), Zubehör Niedrig. Maximum = Hoch/Mittel (A), kein Direktbeleg für Vergussmasse (Suche ergab nichts, kein Gegenbeweis).
- Patente: Google Patents (assignee "Thyracont", 22.10.): keine Treffer. Espacenet (pa=thyracont, 22.10.): 0 Treffer. Kein Signal (kein Gegenbeweis).
- Wettbewerbereinsatz: kein Hinweis gefunden (Grep wettbewerber_referenzen.md).
- Konzern/Werke: Websuche (22.10.) ergab keine Eigentümer-/Konzernangabe; Familiengründung, Geschäftsführung Plöchinger/Salzberger. Kein CRM-Bezug.
- CRM-Status: neu.
- Offener Auftrag: keiner für die Ampel. Zur Mailtauglichkeit: Smartline-/Mini-Transmitter-Datenblatt im Original (Schutzart, vergossene Elektronik) und Stellenanzeige Montage Passau.
- Nicht verwendbare Aussagen: Verguss der Transmitter-Elektronik (A); IP54-Angabe (S, Suchtreffer).
- Stichprobe für Jey: nein.

## 43. TIRA GmbH (A4.554)
- Ampel neu: GRÜN bestätigt (V Entwicklung/Fertigung/Montage am Sitz Schalkau, Verguss Hoch A). Tabellenzeile D: 4.
- Identität (V, 22.10.2026): https://www.tira-gmbh.de/sonstige/impressum/ - "TIRA GMBH, Eisfelder Straße 23/25, 96528 Schalkau", "Handelsregister: HRB 302424, Registergericht: Jena". Stimmt mit Vorgabe überein (Schalkau, Thüringen). Zitat im Browser bestätigt: ja.
- Fertigung (V, 22.10.2026): https://www.tira-gmbh.de/karriere/stellenmarkt/monteur-fuer-elektrodynamische-pruefanlagen/ - "Die TIRA GmbH mit Firmensitz in Schalkau" und "Mehr als 130 hoch qualifizierte Mitarbeiter entwickeln und fertigen modernste Anlagentechnik"; Aufgabe "Montage und Inbetriebnahme der Shaker und Prüfanlagen" nach Werksabnahme. Ergänzend https://www.tira-gmbh.de/tira-gmbh/unternehmen/ - "Ausbau des eigenen mechanischen Fertigungszentrums". Zitate im Browser bestätigt: ja. Stellenanzeige ohne Datum (Zitat aktuell, Seite trägt Copyright 2026). Die Seite spricht von "TIRA Gruppe" und "TIRA Standorte" (Gruppenstruktur nicht erläutert); Fertigung am Sitz Schalkau ist unabhängig davon V belegt.
- Verguss/Klebung/Dichtung: Erreger-/Schwingspulen der elektrodynamischen Shaker (Block A Spulen) Hoch (A), Leistungsverstärker/Netzteile Mittel (A), Steuer-/Messelektronik Mittel (A), Mechanik Niedrig (A). Maximum = Hoch (A). Datenblätter zu Verguss/Imprägnierung der Spulen nicht gelesen (nur Suchtreffer-Titel).
- Anlagenbauer-Prüfung (Regel 22.10.): Prüf- und Auswuchtanlagen, keine Dosier-/Vergussanlagen, kein E1.
- Patente: Google Patents (assignee "TIRA GmbH", 22.10.): keine Treffer. Espacenet (pa="tira gmbh"; pa=tira AND txt=exciter, 22.10.): 0 Treffer. Kein Signal (kein Gegenbeweis; Anmelder-Variante "TIRA Schwingtechnik/TIRA Gruppe" nicht gesucht).
- Wettbewerbereinsatz: kein Hinweis gefunden (Grep wettbewerber_referenzen.md).
- Konzern/Werke: "TIRA Gruppe" erwähnt, Sitz Schalkau; weitere Werke nicht belegt. Kein CRM-Bezug.
- CRM-Status: neu.
- Offener Auftrag: keiner für die Ampel. Zur Mailtauglichkeit: Verguss/Imprägnierung der Erregerspulen (Broschüre/Datenblatt, Stellenanzeige Elektroniker) und Klärung, was "TIRA Gruppe" umfasst.
- Nicht verwendbare Aussagen: Verguss Schwingspulen/Verstärker (A).
- Stichprobe für Jey: nein.

## 44. TOELLNER Electronic Instrumente GmbH (A4.524)
- Ampel neu: GELB. Tabellenzeile D: 2 (Identität nicht über Impressum/Register belegt: toellner.de zeigt am 22.10.2026 "Technische Wartungsarbeiten", kein Impressum lesbar). Kein Widerspruch zur Vorgabe, Firma ist über Messeprofil auffindbar; nach Impressum-Beleg voraussichtlich GRÜN Z.4.
- Identität: Messeprofil (S, 22.10.2026) https://www.embedded-world.de/en/exhibitors/toellner-electronic-instrumente-gmbh-2610992 - "Gahlenfeldstraße 31, 58313 Herdecke". Zitat im Browser bestätigt: ja (Adresse). Impressum/HRB nicht erreichbar (https://www.toellner.de/ und /impressum: Wartungsseite); Websuche fand keinen Registereintrag (openregister-Treffer gehört zu anderer Herdecker Firma, aussortiert). Rechtsform GmbH nur aus Firmenname/Messeprofil.
- Fertigung (S/A): Messeprofil - "has been successfully developing and producing highly dynamic DC power supplies" (S, Aussteller-Beschreibung, nie V). Sitzregel (Gerätebauer, eigener Standort Herdecke, keine Konzern-/Auslagerungshinweise gefunden) würde Stufe A genügen lassen. Ältere Messeprofile (S): seit 1972, Export 42 Länder. Stellenanzeige der Firma nicht gefunden.
- Verguss/Klebung/Dichtung: programmierbare DC-Netzgeräte/Labornetzgeräte (160 W bis 5200 W), Netzteile/Leistungsstufen, Isolations-/Netztransformatoren Hoch (A, Block A Netzteile/Trafos), 4-Quadranten-Verstärker Mittel (A), Funktionsgeneratoren Niedrig bis Mittel (A). Maximum = Hoch (A). Datenblatt nicht gelesen.
- Patente: Google Patents (assignee "Toellner", 22.10.): 1 Treffer US9611743B2 "Radially compressible and expandable rotor for a pump ..." (Anmelder Thomas Toellner / ECP Entwicklungsgesellschaft, Medizinpumpe, erteilt 2017-04-04): andere Person/Firma, aussortiert. Espacenet (pa="toellner electronic", 22.10.): 0 Treffer. Kein Signal. Schreibvariante Töllner nicht gesondert gesucht.
- Wettbewerbereinsatz: kein Hinweis gefunden (Grep wettbewerber_referenzen.md).
- Konzern/Werke: kein Konzernhinweis gefunden. Kein CRM-Bezug.
- CRM-Status: neu (Toellner, Töllner, TOELLNER Electronic Instrumente: kein Treffer).
- Offener Auftrag (Gelb): Impressum und Handelsregister (Rechtsform, HRB, Registergericht) der TOELLNER Electronic Instrumente GmbH belegen: toellner.de/impressum erneut aufrufen, sobald die Wartungsseite weg ist; alternativ Handelsregister-Auszug (handelsregister.de). Gleichzeitig Fertigung Herdecke mit V belegen (Firmen-Unternehmensseite oder Stellenanzeige Elektronikmontage). Sind Sitz und Fertigung bestätigt: GRÜN Z.4.
- Nicht verwendbare Aussagen: Fertigung in Herdecke (S, Messetext); Rechtsform und Register (?); Verguss der Netzgeräte (A).
- Stichprobe für Jey: nein (Auftrag klar, reine Beleglücke wegen Wartungsseite).

## 45. VX Instruments GmbH (A4.317)
- Ampel neu: GRÜN (schwach). Tabellenzeile D: 4 (Sitzregel: Gerätebauer, ein Standort Landshut, keine Auslagerungshinweise; Verguss Mittel A). Fertigungsaussage der Firma lautet nur "engineered in Germany" (Lehre 4), Eigenfertigung kommt aus Jobbörsen-Snippets (S). Daher Stichprobe.
- Identität (V, 22.10.2026): https://vxinstruments.com/imprint/ - "VX Instruments GmbH, Roedersteinstraße 10, 84034 Landshut", "Registering court: Amtsgericht Landshut, Registration number: HRB 4785"; vertreten durch Christian Degenhart. WEEE-Reg.-Nr. DE 53704080. Stimmt mit Vorgabe überein (nur Landshut, kein Altdorf-Standort im Impressum). Zitat im Browser bestätigt: ja.
- Fertigung (A/S): https://vxinstruments.com/about-vxi/ - "100% engineered in Germany" und "From the initial idea to series production" (Entwicklung in Deutschland, Fertigungsort Landshut nicht wörtlich); Tochter nur "VX Instruments Asia Pte. Ltd." (Singapur, Vertrieb/Support). Jobbörse (S, Websuche StepStone/Glassdoor): "Made in Germany" aus neuerem Technologiestandort Landshut und Aufbau von Teststationen für "eigene Elektronikfertigung" (Anzeigen ohne Datum). Zitate zur Entwicklung im Browser bestätigt: ja. Keine Stellenanzeige Montage im Volltext gelesen (Karriereseite zeigt im Text keine Stellen).
- Verguss/Klebung/Dichtung: Hochvolt-/Leistungs-Prüfmodule (SMU, Generatoren) Mittel (A), zugekaufte Netzteile/Trafos im Gerät Mittel (A, Endprodukt-Regel), Steckkarten (PCBA) Niedrig (A), 19-Zoll-Gehäuse Niedrig (A). Maximum = Mittel (A), schwach (Messtechnik-Einzelstücke, kleine Serien: laut Medizintechnik-Regel zählen kleine Mengen).
- Patente: Google Patents (assignee "VX Instruments", 22.10.): keine Treffer. Espacenet (pa="vx instruments", 22.10.): 0 Treffer. Variante "VXI Instruments"/"Degenhart" nicht gesondert gesucht. Kein Signal.
- Wettbewerbereinsatz: kein Hinweis gefunden (Grep wettbewerber_referenzen.md).
- Konzern/Werke: familiengeführt ("family-owned company"), Singapur-Tochter Vertrieb. Kein CRM-Bezug.
- CRM-Status: neu.
- Offener Auftrag: keiner für die Ampel. Zur Mailtauglichkeit: Original-Stellenanzeige Elektronik-/Produktionsmitarbeiter Landshut (V Fertigungsort) und Datenblatt Hochvolt-SMU auf Vergussmasse.
- Nicht verwendbare Aussagen: Fertigung in Landshut (S/A); Verguss der Prüfmodule (A).
- Stichprobe für Jey: ja (Fertigungsort nur A/S, Verguss Mittel nur aus Produkttyp).

## 46. Winkler AG (C1.134)
- Ampel neu: GELB. Tabellenzeile D: 7 (mehrere Werke: Heidelberg, Walldorf und Tunesien; Sitzregel nicht anwendbar; Fertigung DE ist V belegt, aber welches Produkt in welchem Werk entsteht, ist offen, Serien in Tunesien).
- Identität (V, 22.10.2026): https://winkler.org/impressum/ - "Winkler AG, Sitz: Heidelberg", "Opelstr. 1-3, 68789 St. Leon-Rot", "Handelsregister: HRB 732577, Registergericht: Mannheim". Stimmt mit Vorgabe (St. Leon-Rot) überein; Sitz laut Register Heidelberg, Betriebsadresse St. Leon-Rot (Abweichung von Verzeichnissen, die Englerstraße 24 Heidelberg nennen). Nicht verwechseln mit Winkler-Federn (Stuttgart, winkler.de). Zitat im Browser bestätigt: ja.
- Fertigung (V, 22.10.2026): https://winkler.org/ueber-uns/ - "Mit drei Produktionsstandorten ist Winkler hervorragend aufgestellt" ; "Mitarbeiter in Heidelberg und Walldorf sind hierbei spezialisiert auf große oder sehr komplexe Einzelproduktfertigungen" ; "Mit unserem Produktionsstandort in Tunesien sind wir seit 2014 auch bestens aufgestellt, um hohe Stückzahlen" (Zitate gekürzt). Zitate im Browser bestätigt: ja. Fertigung in DE damit V belegt (Einzelstücke, komplexe Heizlösungen), Serien/hohe Stückzahlen aber in Tunesien; ob Silikonheizelemente und Ex-Anschlüsse in Heidelberg/Walldorf oder Tunesien entstehen, nicht belegt. St. Leon-Rot selbst wird nicht als Produktionsstandort genannt (Heidelberg/Walldorf; Betriebsadresse liegt neben Walldorf).
- Verguss/Klebung/Dichtung: https://winkler.org/produkte/silikonheizelemente/ - "Auf Metall- und Maschinenteile vulkanisiert" und "Selbstklebend" (Silikonheizelemente, Schutzklasse II): Heizelement = Beispielprodukt der Endprodukt-Regel Hoch (A, Verklebung/Einbettung belegt als Eigenschaft V, Verfahren offen); Heizschläuche/Heizmatten mit Anschlussbereich Hoch (A); Ex-Schutz-Anschlüsse (ATEX, Block A Ex-Schutz) Hoch (A); Temperaturregler Mittel (A). Maximum = Hoch (A). Zitate im Browser bestätigt: ja.
- Anlagenbauer-Prüfung: Beheizungslösungen, keine Dosier-/Vergussanlagen, kein E1.
- Patente: Google Patents (assignee "Winkler AG", 22.10.): 1 Treffer DE102015223346A1 "Hose line, a sleeve and a method for producing a hose line" (Anmelder Edmund Stegmüller Winkler GmbH, anderes Unternehmen, Anmeldung 2015, veröffentlicht 2017-06-01; gleichnamige Firma aussortiert, Zuordnung zu Winkler AG nicht belegt). Espacenet (pa="winkler ag" AND txt=heating, 22.10.): 0 Treffer. Kein Signal. Schwäche: Namensgleichheit Winkler, breite Suche nicht eng nach potting gefahren.
- Wettbewerbereinsatz: kein Hinweis gefunden (Grep wettbewerber_referenzen.md).
- Konzern/Werke: eigenständige AG (Vorstand Ernst, Medek, Zenner; Aufsichtsrat Schild), Kooperationen mit Neybo GmbH (Vertrieb Labor/Fass) und Semimed Thermal (UK). Kein CRM-Bezug.
- CRM-Status: neu (Winkler, Winkler AG: kein Treffer).
- Offener Auftrag (Gelb): In welchem Werk (Heidelberg, Walldorf oder Tunesien) werden Silikonheizelemente, Heizschläuche/-matten und Ex-Anschlussdosen gefertigt/vergossen? Quellen: winkler.org Unterseiten "Standorte"/"Produktion" und Karriereseite (Stellenanzeigen Produktion/Montage Heidelberg/Walldorf, Vulkanisieren/Vergießen), Produktseite EX-Produkte https://winkler.org/produkte/atex-produkte/ (Anschlussbereich vergossen?), Datenblatt Silikonheizelement. Wird Fertigung der Silikonheizelemente oder Ex-Produkte in DE belegt: GRÜN Z.4; ausschließlich Tunesien: Rot E3 nur bei V-Beleg für alle relevanten Produkte (unwahrscheinlich, da DE-Standorte V).
- Nicht verwendbare Aussagen: Produkt-Werk-Zuordnung (?); Verguss/Verklebungsverfahren der Heizelemente und Ex-Anschlüsse (A).
- Stichprobe für Jey: ja (Serienfertigung in Tunesien; Demak-Relevanz hängt am deutschen Anteil).

---

## Zusammenfassung Durchgang 05
| Nr | Firma | Ampel neu | Zeile D | Kernbegründung | Auftrag |
|---|---|---|---|---|---|
| 41 | SRT Resistor Technology GmbH | GELB | 7 | Produktion Cadolzburg V, Hochspannungswiderstände Verguss nur Niedrig-Mittel (A), Datenblatt nicht lesbar | HV-Datenblätter: Umhüllung Lack/Glas/Epoxid-Verguss? |
| 42 | Thyracont Vacuum Instruments GmbH | GRÜN | 4 | "entwickelt und produziert" Passau V, Transmitter/Sensoren Hoch A | keiner |
| 43 | TIRA GmbH | GRÜN | 4 | Stellenanzeige "entwickeln und fertigen" Schalkau V, Erregerspulen Hoch A | keiner |
| 44 | TOELLNER Electronic Instrumente GmbH | GELB | 2 | Impressum/HRB nicht lesbar (Website Wartung), Fertigung nur Messeprofil S | Impressum/HRB und Fertigung Herdecke belegen |
| 45 | VX Instruments GmbH | GRÜN (schwach) | 4 | Impressum V Landshut, Sitzregel, Fertigung nur "engineered in Germany" + Jobbörse S, Verguss Mittel A | keiner (Stichprobe) |
| 46 | Winkler AG | GELB | 7 | Heidelberg/Walldorf V, aber Serien in Tunesien, Produkt-Werk-Zuordnung offen | Produkt-Werk-Zuordnung Silikonheizelemente/Ex-Produkte |

Ausscheider: keine (kein CRM-Treffer, kein Verband/Prüfdienst/Forschung, kein Verguss-/Dosieranlagen- oder Materialhersteller, kein Rot-Fall).

## Einschränkungen
- toellner.de war am 22.10.2026 nur als Wartungsseite erreichbar: Impressum, Register und Fertigungsaussagen der Firma fehlen; nur Messeprofil (S) und Verzeichnisse.
- Datenblatt-PDFs (SRT, rhopoint, Nürnbergmesse) per Browser und WebFetch nicht textlesbar; Verguss bei allen sechs Firmen Stufe A, kein Datenblatt im Original gelesen. Die Suchzusammenfassung zu Thyracont VCR-SL (IP54) ist Stufe S.
- DEPATISnet nicht abgefragt; Patente über Google Patents + Espacenet (Legacy-Ansicht, "0 results" bei fünf Firmen: SRT, Thyracont, TIRA, TOELLNER, VX Instruments; ein Fremdtreffer bei Winkler, einer bei TOELLNER). Rechtsstand nur für die zwei Fremdtreffer erhoben (beide nicht der Firma zugehörig). Eine Absicherung durch DEPATISnet ist für Firmen mit "0 Treffer" noch offen.
- Keine Wettbewerber-Einzelsuche (Sparmodus), nur Grep auf wettbewerber_referenzen.md (kein Treffer für alle sechs Firmen).
- Browser: Navigationsklicks auf verdeckte Menüeinträge (Thyracont, Winkler) lösten keine Seite aus, Unterseiten wurden per URL aufgerufen; VX-Karriereseite lieferte im Text keine Stellenanzeigen. Ein Parallel-Agent nutzt dasselbe Chrome (fremde Tabs nicht angefasst).
