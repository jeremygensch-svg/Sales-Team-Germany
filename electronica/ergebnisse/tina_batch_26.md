# Tina Batch 26 – electronica 2026 (Prüfung von tom_batch_26.md)
Erstellt: 2026-10-15 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe: ausschließlich electronica/ergebnisse/tom_batch_26.md (10 Firmen, Nr. 281, 282, 284, 285, 286, 287, 289, 290, 291, 293).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Verfügbar waren nur WebSearch (29 Abfragen, Kurzfassungen/Snippets), Bash und Dateizugriff; WebFetch und Chrome nicht nutzbar. Es gibt in diesem Batch KEINE Stufe-V-Aussage (weder bei Tom noch bei mir). "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün ist mailtauglich.
Skripte: `python3 crm_abgleich.py` für alle Firmen samt Konzern-, Alt-, Schwester- und Investorennamen selbst wiederholt. Tabellenzeile = Zeile der Ampel-Tabelle D. Verifikationsdatum aller Einträge: 2026-10-15.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 281 | Peter HUBER Kältemaschinenbau SE (C2.229) | GELB | 3 | ja |
| 282 | Hürner Luft- und Umwelttechnik GmbH (C2.253) | GELB | 5 | nein |
| 284 | IBH Ingenieurbüro Harm Elektrotechnik GmbH (B2.328) | GELB | 7 | nein |
| 285 | iC-Haus GmbH (C5.420) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 286 | icotek GmbH & Co.KG (B3.409) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 287 | ICT Suedwerk GmbH (B3.149) | GELB | 7 | ja |
| 289 | Ikegami Electronics (Europe) GmbH (B5.261) | GELB | 7 | nein |
| 290 | IK Elektronik GmbH (A1.525/14) | GELB | 5 | nein |
| 291 | IL Metronic Sensortechnik GmbH (B4.318) | GRÜN | 4 (Sitzregel) | ja |
| 293 | IMO Oberflächentechnik GmbH (B2.425) | GELB | 6 | nein |

Zahlen: Grün 3, Gelb 7, Rot 0.

**Patente (Prüfpunkt 8, Regel F5):** Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Ich habe für Huber, Hürner, icotek, IL Metronic und iC-Haus je eine eigene Anmelder-Websuche gemacht (Ergebnisse je Firma unten); für die übrigen fünf keine eigene Wiederholung (Budget; Händler/Dienstleister). Feld 9 ist bei ALLEN 10 Firmen ohne Datenbankabfrage: nicht belastbar, kein Gegenbeweis. Batch nach F5 UNVOLLSTÄNDIG; Nachholen im Browser nötig, bevor ein Grün final wird.
**Wettbewerbereinsatz (F6):** Ich habe wettbewerber_referenzen.md vollständig per Grep auf alle zehn Firmennamen (und Hürner, HLU, Metronic, Ikegami, IMO, Huber) geprüft: kein Treffer. Einzelsuchen nur teilweise wiederholt; "kein Hinweis" ist kein Gegenbeweis. Ohne Einfluss auf die Ampel.
**Messe-Signal (Regel N2) von mir bestätigt:** aussteller_namen.txt enthält bdtronic, ELANTAS Europe, Momentive, Nordson TEST&INSPECTION (Prüftechnik), RAMPF Advanced Polymers und RAMPF Production Systems; sonst keine Wettbewerber aus Regel E1. Hinweis, ohne Einfluss.

---

## 281 Peter HUBER Kältemaschinenbau SE | Halle/Stand C2.229
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 3, Schwester im CRM).** Eigener Gerätebauer in Offenburg (ein Standort, Sitzregel A), Verguss Hoch (A: Heizelemente, Sensoren, Pumpenmotoren). Ohne CRM-Bezug wäre es Grün (Zeile 4). Aber: Die Huber-Familie/Peter Huber Kältemaschinenbau SE hat J. Schneider Elektrotechnik (Offenburg, 420 Beschäftigte) zum 01.01.2024 übernommen, "bleibt eigenständig, Schwesterfirma" (Huber-Newsroom und Wirtschaft im Südwesten laut Suchergebnis, S). Diese Firma steht im CRM: `crm_abgleich.py "J. Schneider Elektrotechnik"` = IDENTISCH, bekannte_firmen_DE-AT-NL.txt Zeile 1208 (ohne Ort). Tom hat den Schwesterbezug nicht gefunden (Lehre 2, Regel M).
- Eigene Prüfung: Adresse Werner-von-Siemens-Str. 1, 77656 Offenburg (S, mehrere Quellen); über 350 Beschäftigte am Standort; 4.500-m²-Produktionshalle (S); Stellenanzeige Montagemitarbeiter Kältetechnik, Offenburg, Start 30.07.2026: Löten/Hartlöten von Baugruppen, Einbau, Inbetriebnahme, Funktionsprüfung (S, Make-it-in-Germany) – stützt Montage am Sitz, kein Bezug zu Elektronik-Verguss. Namensvarianten AG/SE/GmbH in Quellen; SE aktuell.
- Patent (eigene Websuche "Peter Huber Kältemaschinenbau Patent Temperiervorrichtung Anmelder"): keine Datensätze. Nicht belastbar.
- Korrekturen an Toms Feldern: Feld 12 "neu" ist falsch bzw. zu ergänzen: CRM-Konzernbezug über Schwester J. Schneider Elektrotechnik. Feld 10 "interessant" nicht bestätigt (nur A/S; Regel I verlangt Gegenlesen). Huber Automotive AG (Z. 1084) ist weiter eine andere Firma, kein Bezug erkennbar (Tom-Bitte erledigt).
- Zitat im Browser bestätigt: nein.
- **Nachrecherche-Auftrag (Gelb, Zeile 3):** (1) An Jey: Ist die CRM-Zeile "J. Schneider Elektrotechnik" (Z. 1208, Offenburg?) die Offenburger Schwester der Huber SE? Wenn ja: Konzernbezug zu einem Bestandskunden, Vorgehen mit Jey/Vertrieb abstimmen (kein Neukunde im Sinne E5 für die Huber SE selbst, da andere Einheit, aber Konzernpflege). Wo nachsehen: CRM-Datensatz (Ort, Ansprechpartner, Verifiziert-Datum), Handelsregister Freiburg, Huber-Newsroom "Expansion of the Huber Group". (2) Fertigung/Vergussstellen in Offenburg belegen (Datenblätter Schutzart, Heizer-/Elektronikfertigung, Impressum).
- Nicht verwendbare Aussagen: Fertigung Offenburg (A/S); Verguss aller Bauteile (A); Schwesterverhältnis (S, Suchergebnis, Quelle Huber-Newsroom nachlesen); Mitarbeiterzahl (S). Stichprobe für Jey: ja.

## 282 Hürner Luft- und Umwelttechnik GmbH | C2.253
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Fertigung in Mücke-Atzenhain nur als Firmenaussage im Snippet (S), und die Firma ist keine Einzelwerk-Firma: weitere Standorte Ransbach-Baumbach (Kunststoffapparate), Schwalbach, Töchter China/Singapur/Malaysia; seit August 2024 75 % bei der Beteiligungsgesellschaft VTC (München, nach Suchergebnis fünf Gruppenfirmen), Clama Holding behält Anteil. Nach Sitzregel (Konzern/mehrere Werke) ist Stufe V nötig, daher Zeile 5. Verguss Mittel (A) bleibt wie bei Tom.
- Eigene Prüfung: Adresse Ernst-Hürner-Straße, 35325 Mücke-Atzenhain (S, Verzeichnis); Website laut Suchergebnis hlu.eu (Tom nennt hlu.de, "nicht verifiziert": zu korrigieren). Stellenanzeigen Mücke-Atzenhain nur für Lüftungsmonteur/Inbetriebnahme/MSR (Anlagenmontage vor Ort beim Kunden), keine Elektronik- oder Produktionsstelle gefunden (S). 2025 Übernahme VSS Umwelttechnik (Abgaswäsche) laut Aggregator (S, nicht gesichert).
- CRM: `crm_abgleich.py "Hürner Luft- und Umwelttechnik GmbH", "Hürner", "Hürner-Funken", "HLU", "VTC", "VTC Verwaltungs", "Hürner Schweisstechnik"`: alle neu (Tom-Auftrag Altname/Investor erledigt). Patent (eigene Suche mit Hürner-Funken): keine Anmeldertreffer (nur Altpatente anderer, z. B. AT67431B Funkenlöscher, nicht zuordenbar).
- Korrekturen an Toms Feldern: Feld 5 hlu.eu statt hlu.de; Feld 7 "Hoch" auf Mittel (S) bzw. Zeile 5 (V nötig wegen Konzern/mehrere Werke). Zitat im Browser bestätigt: nein.
- **Nachrecherche-Auftrag (Gelb, Zeile 5):** (a) Wird die Elektrik (Motoren, Steuerung, Frequenzumrichter) in Mücke-Atzenhain gefertigt/montiert oder zugekauft, und was passiert in Ransbach-Baumbach? Wo nachsehen: hlu.eu Impressum und Standortseiten, Datenblätter Ventilatoren/Antriebe, Stellenanzeigen Produktion/Elektromontage, Broschüre HLU 01/2021 (Zitat "fertigen wir nahezu alle Ventilatoren ... in unserem Werk" im Original prüfen). (b) Welche Dichtungen/Klebungen kommen in den Kunststoffapparaten zum Einsatz (Produktseiten).
- Nicht verwendbare Aussagen: Fertigung Mücke-Atzenhain (S); Verguss/Antriebe (A); Mitarbeiterzahl (S, uneinheitlich); Domain (?). Stichprobe für Jey: nein.

## 284 IBH Ingenieurbüro Harm Elektrotechnik GmbH | B2.328
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2).** Mehrere Verzeichnisse (S) bestätigen: "Ingenieurbüro, Schwerpunkt Beratung und Vertrieb", gelistet als Elektrogroßhändler/Fachplanung, ca. 40 Beschäftigte, ISO 9001 und EN 9100, Geschäftsführer Christian Harm (D&B, S); keine Eigenfertigung gefunden. Das trägt E2 stark, ist aber nicht Stufe V (Zeile 1 verlangt V), daher Gelb statt Rot.
- Eigene Prüfung: Adresse Gutenbergring 35, 22848 Norderstedt bestätigt (S); Name auch als "IBH Elektrotechnik GmbH". Handelsregister-Gegenstand nicht abrufbar. CRM: `crm_abgleich.py` "IBH Ingenieurbüro Harm Elektrotechnik GmbH", "IBH Elektrotechnik": neu. Patent: keine eigene Wiederholung (Händler). Zitat im Browser bestätigt: nein.
- Korrekturen: keine. Toms Einstufung "kein Fertiger" ist plausibel, nur S.
- **Nachrecherche-Auftrag (Gelb, Zeile 7):** Hat IBH eigene Fertigung/Produkte oder nur Beratung/Vertrieb? Wo nachsehen: Impressum und Über-uns ibh-elektrotechnik.de, Handelsregister (Unternehmensgegenstand, Amtsgericht Kiel/Norderstedt), Stellenanzeigen (Montage/Fertigung). Bei Bestätigung Rot nach E2 mit URL. Aktion: nicht priorisieren.
- Nicht verwendbare Aussagen: "kein Fertiger/Händler" (S, noch nicht E2-belegt); Mitarbeiterzahl (S). Stichprobe für Jey: nein.

## 285 iC-Haus GmbH | C5.420
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Sitzregel).** Halbleiter-/Mikrosystemhersteller mit einem Standort Bodenheim, eigene Produkte (ASICs, Encoder-ICs); Wafer extern, aber Montage (Standardgehäuse, Chip-on-Board/Flex, Flip-Chip, optoBGA), Test und Reinraum am Sitz (mehrere Verzeichnisse und Fachpresse, S). Verguss Mittel (A: COB-Mikrosysteme/Multichipmodule werden typischerweise per Glob-Top gekapselt; Dosieren kleiner Mengen zählt). Kein Konzern erkennbar.
- Eigene Prüfung: Adresse Am Kümmerling 18, 55294 Bodenheim jetzt in Suchergebnis bestätigt (Tom: "Vorwissen, ?"). Reinraum für Chipbearbeitung und Montage 2006 (S, 40-Jahre-Artikel). Glob Top ausdrücklich NICHT in den Quellen genannt. Stellenanzeigen: nur ein Werkstudent-Inserat 2021 (Produktion/Montage, S), also Montage am Sitz, mehr nicht.
- Patent (eigene Suche): keine iC-Haus-Anmeldertreffer; auch US6876090B2 (Expired) ist nicht iC-Haus zuzuordnen. CRM: "iC-Haus GmbH", "iC Haus": neu. Zitat im Browser bestätigt: nein.
- Korrekturen: keine inhaltlichen; Feld 4 Adresse jetzt S statt "?". Feld 10 "prüfenswert" bestätigt.
- Nachrecherche (empfohlen, nicht Gelb): Datenblatt/Fertigungsbeschreibung COB und optoBGA (Glob Top, Dam-and-Fill, Underfill), Stellenanzeige Reinraum-Montage, Impressum ichaus.de (Register).
- Nicht verwendbare Aussagen: Verguss/Glob Top (A); Fertigung Bodenheim (S); Reinraum-Montagelinie (S); Mitarbeiterzahl (S). Stichprobe für Jey: ja (Grün stützt sich auf Sitzregel und Produkttyp, beides A; Halbleiter-Verguss ist Grenzfall zum Demak-Kerngeschäft).

## 286 icotek GmbH & Co.KG | B3.409
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Sitzregel).** Eigener Hersteller in Eschach (BW), Ausland nur Vertrieb. Neu gegenüber Tom: SPS-2025-Ausstellerprofil sagt "Produkte werden ausschließlich in Deutschland hergestellt" (S, Suchergebnis); RS-Components-Listing führt Ursprungsland DE (S). Stellenanzeigen auf icotek.com (Eschach): Konfektionierung/Montage elektronischer Baugruppen, Industriemechaniker/Mechatroniker mit Kabelkonfektion (Original-PDFs, im Suchergebnis zitiert, S; "produzieren wir unsere Produkte ... in über 60 Länder"). Verguss Mittel (A): Elastomer-Tüllen/Dichtplatten, Umspritzen, konfektionierte Leitungen. Spritzguss/Umspritzen selbst ist kein Demak-Verguss; die Grün-Begründung beruht auf Dichtungen/Gasketing und Leitungskonfektion (A) und ist die schwächste im Batch.
- Eigene Prüfung Patente: Treffer bei Google Patents mit Anmelder "Icotek Project GmbH & Co. KG" (DE102020208235A1, DE102021201300B3, DE102021126007A1 "Kabeldurchführung"; Status nicht geprüft, Zuordnung nur Snippet, S); Titel zeigen kein Vergussthema. Neue Anmeldervariante/Schwesterfirma "Icotek Project GmbH & Co. KG": `crm_abgleich.py` = neu. Adresse Eschach bestätigt (Messe Frankfurt, elektro.net, S); Moosbach-Eintrag bleibt ungeklärt. CRM: "icotek GmbH & Co.KG", "icotek": neu. Zitat im Browser bestätigt: nein.
- Korrekturen: Feld 9 ergänzt (Icotek-Project-Patente, s. o.); Feld 7 Stufe bleibt A/S, Fertigungsbelege stärker. Feld 17: Rechtsform "icotek GmbH & Co. KG" vs. "icotek GmbH" in Quellen uneinheitlich.
- Nachrecherche (empfohlen): Impressum/Register icotek.com (Rechtsform, Verhältnis zu Icotek Project GmbH & Co. KG); Datenblatt KEL-Serien (Dichtungsmaterial, geschäumt/gespritzt?); Stellenanzeige Konfektionierung im Original lesen (Verguss/Umspritzen der Leitungen?).
- Nicht verwendbare Aussagen: Fertigung "ausschließlich in Deutschland" (S, Messeprofil, nach Regel N5 nie V); Verguss/Dichtungen (A); Patentzuordnung (S). Stichprobe für Jey: ja.

## 287 ICT Suedwerk GmbH | B3.149
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Die Identität ist jetzt greifbar: Bajuwarenring 12 a, 82041 Oberhaching, gegründet 2017, Geschäftsführer Wolfgang Reitberger-Kunze (Bayern International als "Hersteller und Dienstleister", Implisense, Messekatalog electronica, alles S). Produkt: Wärmeleitfolien, Silikonfolien, Gap-Filler, Wärmeleitkeramik, Silikon-Kappen/-Schläuche für Leistungselektronik, Serien- und Lohnfertigung am Standort (S). Das widerspricht der Listen-Ersteinschätzung "Stromversorgung" und Toms Hypothese Netzteile. Damit ist die Firma eher Zulieferer von Wärmemanagementmaterial: sie baut keine vergossenen Endprodukte, sondern liefert Material, das neben/anstelle von Vergussmasse eingesetzt wird (Gap-Filler, Silikon). Ob das E1 (Materialhersteller im Demak-Kerngeschäft) trifft, ist nicht V-belegt und fachlich Grenzfall (Wärmeleitfolien sind kein Verguss-/Klebstoff-Hersteller im Sinne der Beispiele). Daher Gelb.
- Eigene Prüfung: CRM "ICT Suedwerk GmbH", "ICT Südwerk": neu. Patent: keine eigene Wiederholung. Katalog-PDFs (exhibitors.electronica.de) im Suchergebnis genannt, nicht gelesen. Zitat im Browser bestätigt: nein.
- Korrekturen an Toms Feldern: Feld 2 "unbekannt" -> Wärmemanagement-Materialien; Feld 6 (Produkt) und Feld 5 (Website ict-suedwerk.de laut Suchergebnis, nicht gelesen); Feld 17 Identität jetzt teilbelegt (Registerauszug fehlt, Verwechslung mit ICT North America ausgeschlossen); Feld 7 und 8 von "Mittel ?" auf Verguss Niedrig/Mittel (Material, nicht Endprodukt) zu ändern.
- **Nachrecherche-Auftrag (Gelb, Zeile 7):** (1) Ist ICT Suedwerk Hersteller (Produktion in Oberhaching) oder Konverter/Händler von Zukaufmaterial, und stellt sie Gap-Filler/Dosiermaterial her (dann E1 prüfen) oder nur Folien/Stanzteile? Wo nachsehen: electronica-Katalog (PDF), Website ict-suedwerk.de Impressum und Produktseiten, Handelsregister München. (2) Setzt sie Dosieranlagen ein (Gap-Filler-Dosierung)? Dann Partner/Wettbewerbs-Umfeld statt Kunde. Aktion: Jey entscheidet, ob Material-Zulieferer überhaupt Zielgruppe sind.
- Nicht verwendbare Aussagen: Produktliste (S); Fertigung Oberhaching (S); Gründungsjahr, Gesellschafter (S); Verguss (A/?). Stichprobe für Jey: ja (Zielgruppen-Entscheidung).

## 289 Ikegami Electronics (Europe) GmbH | B5.261
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2).** Mehrere Quellen (gophotonics, sportsvideo.org, IABM, UK Companies House für die Zweigstelle Sunbury; alle S): "sales and service organisation for Europe and Africa", gegründet 1970, Zweigstellen UK/Dänemark, Händler in weiteren Ländern; Produktion beim japanischen Konzern. Eine Montage/Fertigung in Neuss ist nicht belegt, aber nicht V-ausgeschlossen (Zeile 1 verlangt V).
- Eigene Prüfung: Adresse Ikegamistraße 1, 41460 Neuss (S). Handelsregister-Gegenstand nicht abrufbar. CRM: "Ikegami Electronics (Europe) GmbH", "Ikegami Tsushinki", "Ikegami": neu. Patent: keine Wiederholung (Konzernanmelder Japan, GmbH nicht Anmelder). Zitat im Browser bestätigt: nein.
- Korrekturen: keine.
- **Nachrecherche-Auftrag (Gelb, Zeile 7):** Gibt es Montage, Reparatur mit Teilefertigung oder Konfektionierung in Neuss, oder reiner Vertrieb/Service (E2)? Wo nachsehen: Handelsregister Neuss (Unternehmensgegenstand), Impressum ikegami.de, Stellenanzeigen Neuss (Service/Montage). Bei Bestätigung Rot nach E2 mit URL. Aktion: nicht priorisieren.
- Nicht verwendbare Aussagen: "Vertriebsgesellschaft" (S, noch nicht E2-belegt); Fertigung Japan (S); Verguss/Bonding der Produkte (A, nur Konzern). Stichprobe für Jey: nein.

## 290 IK Elektronik GmbH | A1.525/14
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Eigene Produktion in Muldenhammer OT Hammerbrücke (über 1.200 m², ISO 9001, IPC-A-610, rund 60 Beschäftigte, zwei Standorte inkl. Dresden; pressebox, silicon-saxony, S). Die Firma bezeichnet sich aber als Entwickler und "EMS-Dienstleister"; für Auftragsfertiger verlangt die Sitzregel Stufe V, Tom hat Hoch auf Sitzregel gestützt. Verguss Mittel (A) wegen Funksensoren/Antennen in Schutzgehäusen, aber weder Verguss noch Gehäuse-IP in den Quellen belegt (eigene Suche ohne Treffer).
- Eigene Prüfung: Register HRB 22126 Chemnitz, USt-ID DE814407549, Geschäftsführer Jan-Erik Kunze (Verzeichnis it-in-germany, S, nicht aus Impressum). Adresse bestätigt. CRM: `crm_abgleich.py "IK Elektronik GmbH", "IK Elektronik"`: nur Ähnlichkeitstreffer anderer Firmen (CHK, EKM, SK, TWK, WIR; Z. 407, 408, 630, 2206, 2433, 2599) und Enthalten-Treffer Benning, ZwoTec: keine Einheit, neu. Patent: keine eigene Wiederholung. Zitat im Browser bestätigt: nein.
- Korrekturen an Toms Feldern: Feld 7 "Hoch" -> Fertigung am Sitz plausibel, aber EMS/Auftragsfertiger braucht V (Zeile 5). Feld 17 um Register HRB 22126 Chemnitz ergänzen (S).
- **Nachrecherche-Auftrag (Gelb, Zeile 5):** (a) Fertigungsbeleg V: Impressum und Produktions-/EMS-Seite ik-elektronik.de, Stellenanzeige Produktion/Bestückung Hammerbrücke. (b) Werden Funksensoren, Antennen oder EMS-Baugruppen vergossen oder verklebt (Datenblatt Schutzart, Broschüre "Verguss auf Kundenwunsch" im Original lesen) und welche EMS-Kundenbranchen? Aktion: Beobachtung.
- Nicht verwendbare Aussagen: Fertigung Hammerbrücke (S); 1.200 m² (S); Verguss (A); Mitarbeiterzahl (S, uneinheitlich). Stichprobe für Jey: nein.

## 291 IL Metronic Sensortechnik GmbH | B4.318
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GRÜN (Tabellenzeile 4, Sitzregel).** Eigener Hersteller mit einem Standort (Mittelstraße 33, 98693 Ilmenau-Unterpörlitz), Gründung 1992, familiengeführt (Geschäftsführer Christian und Andreas Hansch), kein Konzernhinweis; Glasschmelz-Bandofen und Nickel-/Goldgalvanik im Haus, Pressemeldung Sensor+Test 2026 und Produktmeldung 01/2026 "hohe Fertigungstiefe", rund 90 Beschäftigte (alle S, mehrere unabhängige Verzeichnisse und Messeseiten). Verguss Hoch (A: UV-/Feuchte-/Temperatur-/Drucksensoren und Sensormodule mit Elektronik für Wassereinsatz). Eigenverguss nicht belegt (eigene Suche: "keine Hinweise auf Vergießen").
- Eigene Prüfung: Stellenanzeigen Unterpörlitz: nur Haustechnik/Hausmeister gefunden (S), keine Produktions-Stelle. Patent (eigene Suche mit Hansch/Gehäuse/Verguss): keine Datensätze. Domain nach Suchergebnis il-metronic.com und il-metronic.de (beide genannt, nicht gelesen). CRM: "IL Metronic Sensortechnik GmbH", "IL Metronik", "Metronic": neu. Zitat im Browser bestätigt: nein.
- Korrekturen: Feld 5 Domain unklar (.com/.de). Sonst keine. Feld 10 "interessant" nicht abschließend bestätigt (nur A/S).
- Nachrecherche (empfohlen, für Mailstufe): Pressemeldung PDF sensor-test.de im Browser lesen (V-Zitat "Fertigungstiefe"); Datenblätter UV-Sensor (Schutzart IP68? vergossen/verklebt, Dichtung Messfenster); Impressum il-metronic.de.
- Nicht verwendbare Aussagen: Fertigung Unterpörlitz (S); Verguss Sensoren (A); "Glasschmelzofen/Galvanik" (S, Verzeichnis); Mitarbeiterzahl 50 gegen 90 (S, widersprüchlich). Stichprobe für Jey: ja (Grün ohne V-Beleg, Interessant-Kandidat).

## 293 IMO Oberflächentechnik GmbH | B2.425
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6).** Fertigung belegt (Lohngalvanik am Sitz Königsbach-Stein, über 30 Bandanlagen, rund 430 bis 500 Beschäftigte, ISO 9001/14001/IATF 16949; IMO-Dokumente und Fachpresse, S), aber alle plausiblen Bauteile Niedrig (beschichtete Kontakte/Stanzteile, Galvanikprozess). Kein E2-Beleg (Lohnfertiger in DE), kein Rot. Tom: unwahrscheinlich, bestätigt.
- Eigene Prüfung: Adresse Remchinger Straße 5, 75203 Königsbach-Stein, Familienunternehmen seit 1973, Geschäftsführer Bernd Müller (Pressemeldung 2021, S). CRM: "IMO Oberflächentechnik GmbH", "IMO Ingo Müller Oberflächentechnik": neu. Patent: keine eigene Wiederholung. Zitat im Browser bestätigt: nein.
- Korrekturen: keine.
- **Nachrecherche-Auftrag (Gelb, Zeile 6):** Welche Produkte/Bauteile enthalten Dosier-, Klebe-, Dicht- oder Vergussschritte (z. B. Umspritzen/Maskieren selektiv, Kundenbaugruppen, eigene Montage)? Wo nachsehen: Leistungsportfolio imo-gmbh.com, Technisches Merkblatt Galvanik 04.2024, Reportage Galvanotechnik 12/2023. Aktion: nicht priorisieren.
- Nicht verwendbare Aussagen: Verguss Niedrig (A); Fertigung Sitz (S); Kundennamen Bosch/Continental usw. (S, Werbeaussage). Stichprobe für Jey: nein.

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind überall ehrlich auf S/A gesetzt; es wurde keine V-Aussage vorgetäuscht. Seine Einstufungen "interessant" (Huber, IL Metronic) sind mangels Gegenlesen (Regel I) nur vorläufig.
- Wesentlicher Fund: Huber hat im CRM eine Schwesterfirma (J. Schneider Elektrotechnik, Z. 1208). Tom meldete "neu". Ursache: Konzern-/Schwesterbezug nicht recherchiert. Vorschlag Fehlerlog (Jey gibt frei, nicht eingetragen): Bei Familien-/Inhabergeführten Mittelständlern per Websuche "Übernahme/Schwesterfirma" prüfen und Schwestern gegen das CRM abgleichen.
- ICT Suedwerk: Listen-Ersteinschätzung "Stromversorgung" war falsch (tatsächlich Wärmemanagement-Material); Zielgruppen-Frage für Material-Zulieferer an Jey.
- Hürner: Domain war falsch (hlu.eu statt hlu.de), Gruppen-/Mehrwerk-Bezug über VTC wurde von Tom nur als Investor vermerkt, aber nicht in die Sitzregel einbezogen.
- IK Elektronik: EMS ist Auftragsfertigung, daher Sitzregel nicht ausreichend.

## Einschränkungen
- Browser und WebFetch nicht verfügbar: kein Gegenlesen nach Abschnitt H, keine Impressen, Datenblätter, Kataloge oder Handelsregister gelesen; alle Aussagen Stufe S oder A. Kein "Zitat im Browser bestätigt: ja", kein Grün mailtauglich.
- WebSearch: 29 Abfragen verbraucht (Identität/Fertigung je Firma, Stellenanzeigen für Huber, Hürner, icotek, iC-Haus, IL Metronic; Patent-Websuchen für Huber, Hürner, icotek, IL Metronic, iC-Haus; Konzern/Schwester für Huber, Hürner, ICT Suedwerk, Ikegami, IBH, IMO, IK Elektronik). Keine eigene Patentsuche für IBH, ICT Suedwerk, Ikegami, IK Elektronik, IMO.
- Patente: Pflichtsuche F5 (Google Patents, Espacenet, DEPATISnet) für alle 10 Firmen nicht erfüllt. Offene Anmeldervarianten: "Peter Huber Kältemaschinenbau AG/SE", "Hürner-Funken", "Icotek Project GmbH & Co. KG" (Rechtsstand der drei DE-Anmeldungen prüfen), "IL Metronik", "IMO Ingo Müller Oberflächentechnik", "Ikegami Tsushinki".
- Wettbewerbereinsatz (F6): Datei wettbewerber_referenzen.md komplett per Grep geprüft (kein Treffer), Einzelsuchen nicht wiederholt.
- Kundendatenbank_export.txt: kein Treffer für Huber, Schneider, icotek (Grep); daher keine "Verifiziert am"-Prüfung. Die CRM-Zeile "J. Schneider Elektrotechnik" steht nur in bekannte_firmen_DE-AT-NL.txt (ohne Ort/Datum).
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
