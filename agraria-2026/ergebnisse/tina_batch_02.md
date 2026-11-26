# Tina Batch 02 - agraria 2026 (Prüfung von tom_batch_02.md)
Erstellt: 2026-11-24 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_02.md (10 Firmen, Nr. 11 bis 20, Agrarmesse Wels 2026, Länder DE/AT/NL).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser geprüft, vorläufig.** Es standen nur WebSearch (6 eigene Abfragen, Kurzfassungen/Snippets) und Bash zur Verfügung; WebFetch wurde nicht genutzt, Chrome nicht vorhanden. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün ist mailtauglich. Verifikationsdatum aller Einträge: 2026-11-24.
Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Jey-Entscheidungen angewandt: Verbände/Prüfdienstleister/Forschung raus; CRM-Namensgleichheit raus (trifft keine Firma, siehe unten); Anlagenbauer bleiben außer Verguss-/Dosieranlagenbauer (E1). Rot nur bei E-Beleg mit Stufe V; da keine V-Quelle existiert, ist Rot in diesem Lauf nirgends möglich. Firmen, die ich für ausschlusswürdig halte, sind "Gelb, Rot-Kandidat" mit Empfehlung an Jey.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 11 | Dr. Knopf & Oswald GmbH (H24, St. 160) | GELB | 7 | nein |
| 12 | Eder GmbH Feedstar (H19, St. 130) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 13 | Eurogenetik ENIV (H24, St. 10) | GELB (Rot-Kandidat) | 2 | nein |
| 14 | farmsaat AG (H17, St. 180) | GELB (Rot-Kandidat, Saatgut) | 7 | nein |
| 15 | Fliegl Agrartechnik GmbH (H20, St. B10) | GELB | 5 | ja |
| 16 | geo-konzept GmbH (H17, St. 150) | GELB (Rot-Kandidat E2) | 7 | nein |
| 17 | Geringhoff (H19, St. 80) | GELB | 2 | ja |
| 18 | hairtex e.K. (H20, St. 1210) | GELB (Rot-Kandidat, Textil) | 7 | nein |
| 19 | Hardi GmbH (H22, St. C30) | GELB (Rot-Kandidat E2/E3) | 7 | ja |
| 20 | Huber Gülletechnik Georg Huber GmbH & Co. KG (H18, St. 80) | GELB | 5 | ja |

Zahlen: Grün 1 (schwach), Gelb 9, Rot 0.

**Empfehlung an Jey (Streichliste, nur Empfehlung, keine Ampel-Änderung):** 13, 14, 16, 18 und 19 sind nach Jeys Entscheidungen (Dienstleister/Software/Vertrieb, Textil, Saatgut) vermutlich auszusortieren; formal bleibt Gelb, weil kein V-Beleg für E2/E3 vorliegt. 11 (Stalltechnik, Verguss Niedrig) ist ein schwacher Kandidat.

**CRM (Prüfpunkt 5, Regel B2/M):** `python3 crm_abgleich.py` für alle Firmen samt Schreib-, Alt-, Konzern- und Schwestervarianten selbst wiederholt (u. a. Knopf Oswald, Eder Landtechnik, Rinderzucht Tirol, Fliegl Fahrzeugbau/Gruppe, geokonzept, Carl Geringhoff/Vertriebsgesellschaft, Hardi International, Exel Industries, Georg Huber, Huber Automotive): kein Treffer, außer Wortwurzel "Huber" -> bekannte_firmen_DE-AT-NL.txt Zeile 1084 "Huber Automotive AG [DE]" (Kern-Name verschieden, siehe Nr. 20). Keine Firma bekannt, kein CRM-Konzernbezug nach Regel M. Das Ergebnis stimmt mit Toms CRM-Angaben überein. Die Datei kundendatenbank_export.txt wird vom Skript mit durchsucht; "Verifiziert am"-Prüfung entfällt (keine Treffer).

**Messe-Signal:** Tom meldet per Grep auf agraria_2026_aussteller_DE-AT-NL.csv keine E1-Wettbewerber/Materialhersteller in der Liste; von mir nicht erneut geprüft, übernommen.

**Patente (Prüfpunkt 8, Regel F5):** Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Eigene Patent-Websuchen nur für Fliegl (potting/Vergussmasse), Eder (Feedstar), Geringhoff; für die übrigen sieben Firmen keine eigene Wiederholung, Toms Suchen weder übernommen noch widerlegt. Feld 9 ist damit bei ALLEN 10 Firmen ohne Datenbankabfrage: nach F5 UNVOLLSTÄNDIG; Nachholen im Browser (Google Patents, Espacenet, DEPATISnet, Rechtsstand) nötig. Auch Toms Batch ist laut seiner Einschränkung unvollständig. "Keine Treffer" ist kein Gegenbeweis. **Wettbewerbereinsatz (F6):** Grep auf wettbewerber_referenzen.md für alle zehn Firmen und Konzernnamen: kein Treffer (die Datei nennt keine dieser Firmen; die Grep-Treffer betrafen nur Fremdtexte). Keine Einzelsuchen mit Wettbewerbernamen von mir.

---

## 11. Dr. Knopf & Oswald GmbH | Halle 24, Stand 160
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Zeile 1 nicht (kein E-Beleg V), 2 nicht (Name/Sitz Aßling stimmen laut S), 3 nicht (CRM neu), 4 nicht (Fertigung nur S, Sitzregel nicht tragend: Hersteller-Status laut AgriExpo-Eigentext, Verguss nur Niedrig), 5/6 nicht, daher 7. Alle belegbaren Bauteile (Schlauchbelüftung, Kälberhütten) sind Niedrig (A); ein Verguss-Bauteil wäre nur eine unbelegte Klimasteuerung (?).
- Eigene Prüfung: CRM neu (Skript). Keine eigene Websuche (Priorität auf aussichtsreichere Firmen). Toms Angaben nicht widerlegt.
- Korrekturen an Toms Feldern: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Enthalten CAT3000 oder die Kälberställe eine eigene Elektronik (Lüftungsklappenantrieb, Klimasteuerung, Sensoren), und wird in Aßling gefertigt? Wo: Produktseiten/Datenblatt CAT3000 und Impressum (Website erst über AgriExpo-Profil ermitteln), im Browser. Wird nichts Elektronisches gefunden: Vorschlag an Jey, zu streichen. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Aßling (S), Verguss Niedrig (A), Bauteilliste (A/?), Größe. Stichprobe für Jey: nein.

## 12. Eder GmbH Feedstar | Halle 19, Stand 130
**ohne Browser geprüft, vorläufig. Ampel: GRÜN, schwach (Tabellenzeile 4, Sitzregel).** Zeile 1 nicht (Eder Landtechnik GmbH ist ein Händler, aber nicht dieselbe Einheit belegt), 2 nicht (Name Eder GmbH, Marke Feedstar, Tuntenhausen stimmen über Bayern International, Markenregister und Eder-Produkttext überein), 3 nicht (CRM neu). Zeile 4: Maschinenbauer mit erkennbarem Standort, eigene Produkte, Fertigung "Made in Tuntenhausen" (S, eigene Suche bestätigt Toms Zitat: System in den Werkstätten in Tuntenhausen gefertigt, Fahrzeugbau-Sparte mit eigener Teilefertigung mit Trumpf-Laser/Kantbank, S); Verguss Mittel (A: Steuerung/Funkmodul, Motor mit Steuerung, Sensoren; Eigenverguss oder Zukauf offen, zählt nach Endprodukt-Regel).
- Eigene Prüfung: WebSearch "Eder GmbH Tuntenhausen Feedstar Patent Futterband Steuerung Fertigung": kein Patent mit Nummer; Marke FEEDSTAR (Serial 79306411, 18.01.2021, Justia) ist keine Patentangabe; Steuerung/Funk/App und Elektromotor (Mischwagen mit Hybridantrieb) im Produkt bestätigt (S, Herstellerbroschüre). Eurotier-Eintrag nach N5 nie V.
- Korrekturen an Toms Feldern: Feld 9: "patentiert" laut Eurotier/Neyer ohne Nummer weiter ungeklärt; Feld 7 kann auf "Hoch (S, Sitzregel)" bleiben. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (zur Absicherung des schwachen Grüns, vor einer Ansprache zwingend): (a) Impressum/Handelsregister: Ist die Eder GmbH die baugleiche Einheit wie die Eder Landtechnik GmbH (Adresse Moorweg 5), welche Gesellschaft fertigt? (b) Wird die Steuer-/Funkelektronik selbst bestückt/vergossen oder zugekauft (Karriereseite, Stellenanzeigen Elektronik-Montage)? (c) Patentnummer des Feedstar suchen (Google Patents, Anmelder Eder GmbH, Eder Landtechnik GmbH; DPMA-Register). Alles im Browser.
- Nicht verwendbare Aussagen: alle (A/S): Fertigung Tuntenhausen, Verguss, Patent "patentiert". Stichprobe für Jey: ja (einzige Grün-Kandidatin, nur S/A belegt).

## 13. Eurogenetik ENIV | Halle 24, Stand 10
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität; Rot-Kandidat nach Jeys Entscheidung "Dienstleister raus").** Firma "ENIV" nicht auffindbar, Land laut Messeliste DE, Hinweise auf Tirol (AT). Tierzucht/Besamung: kein Fertiger, Fertigung und Verguss Niedrig (A). Rot (E2) ist ohne V nicht zulässig.
- Eigene Prüfung: CRM-Skript (Eurogenetik, Rinderzucht Tirol): neu. Keine eigene Websuche (kein Fertiger).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer ist "Eurogenetik ENIV" (Name, Rechtsform, Sitz)? Messeprofil agraria und Impressum lesen. Bestätigt sich Tierzucht/Besamung, an Jey: streichen (Entscheidung Dienstleister/Verband). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Identität, Zuordnung Rinderzucht Tirol (S), Branche. Stichprobe für Jey: nein.

## 14. farmsaat AG | Halle 17, Stand 180
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat: Saatgutzüchter, kein Fertiger).** Identität stimmig (Everswinkel, HRB 11044 Münster, S). Saatgut: Fertigung und Verguss Niedrig (A), kein Vergussprodukt erkennbar. Kein E-Beleg V; Rot nicht zulässig.
- Eigene Prüfung: CRM-Skript: neu. Keine eigene Websuche.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Frage an Jey statt Recherche: Messekategorie "Siliermittel/Silierwagen" auf dem Messeprofil prüfen; wird nur Saatgut/Siliermittel (kein Gerät) angeboten, Streichung durch Jey. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle zum Produkt (A/S). Stichprobe für Jey: nein.

## 15. Fliegl Agrartechnik GmbH | Halle 20, Stand B10
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Fertigungsbeleg V fehlt bei Gruppe mit mehreren Werken).** Zeile 1 nicht (Fliegl Dosiertechnik ist Biogas-Feststoffdosierung, kein Verguss-/Dosieranlagenbau im Sinne E1; nach Produktseite zu bestätigen), 2 nicht, 3 nicht (CRM neu, auch Konzernname), 4 nicht (Konzern/Mehrwerk, Sitzregel greift nicht, V fehlt), 5 trifft. Verguss Hoch (A): ISOBUS/CAN-Steuergeräte, Leuchten, Magnetventile, Wägezellen, Kabelsätze; nach Endprodukt-Regel tragend.
- Eigene Prüfung: zwei WebSearch-Abfragen. (1) Patent/Vergussmasse: kein Fliegl-Patent zu Verguss gefunden; CB Insights nennt 4 Patente ohne Titel (S); bekannt ist die "patentierte Abschiebetechnik" (kein Verguss). (2) Stellen/Montage: Stellenanzeigen Fliegl Agrartechnik Mühldorf für Elektroniker (Automatisierung/Industrieelektrik), Mechatroniker, Industriemechaniker, Schaltschrankbau-Hinweis (S, StepStone/Arbeitsagentur); Azubibroschüre 2025 nennt in Mühldorf vier Montagelinien für Kipper, Dosiertechnik/Biogas, Gülle- und Transporttechnik (S). Eine Elektroniker-Stelle am Sitz ist ein Indiz für Elektronik-/Montagetätigkeit am Standort, aber der Snippet nennt keine Fertigung konkreter Produkte (nicht V). Toms Arbeitsagentur-Stelle "ISOBUS, CAN, EMC, ECUs": Arbeitgeber weiter unbestätigt.
- Korrekturen an Toms Feldern: Feld 4/7 durch Stellenanzeigen etwas gestützt, bleibt S. Feld 9: Anmelder-Varianten Fliegl Fahrzeugbau/Fliegl Agrartechnik in keiner Datenbank geprüft. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Standortseite Mühldorf und Karriereseite im Browser lesen: Wortlaut zur Montage der Gülle-/Kippersysteme und der Elektronik (V mit Zitat). Eine konkrete Stellenanzeige "Elektroniker/Mechatroniker, Fliegl Agrartechnik GmbH, Mühldorf" mit Tätigkeit Verdrahtung/Montage Steuerungen speichern. (b) Werden ISOBUS-Steuergeräte, Leuchten, Sensorik selbst montiert/vergossen oder zugekauft? (c) Patente: Google Patents/Espacenet/DEPATISnet, Anmelder "Fliegl Agrartechnik", "Fliegl Fahrzeugbau", "Josef Fliegl", Stichwörter potting/Vergussmasse/Dichtung. Aussichtsreichste Firma im Batch nach Eder. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Mühldorf (S), Verguss (A), Patentzahl (S), Stellenanzeige (Arbeitgeber unbestätigt). Stichprobe für Jey: ja.

## 16. geo-konzept GmbH | Halle 17, Stand 150
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2 Software/Beratung/Vertrieb).** Nur S-Quellen (Topcon-Vertriebspartner, Software, Drohnendienstleistung, Beratung); Rot erfordert V, daher Gelb. Eigene Hardwarefertigung nicht belegt, Fertigung/Verguss Niedrig.
- Eigene Prüfung: CRM-Skript (geo-konzept, geokonzept): neu. Keine eigene Websuche.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Website geo-konzept.de lesen: eigene Hardware/Werkstatt oder reiner Vertrieb/Software? Bei Bestätigung E2 (V): Rot. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 17. Geringhoff | Halle 19, Stand 80
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität; danach Zeile 5).** Zwei Gesellschaften/Adressen: Carl Geringhoff Vertriebsgesellschaft mbH & Co. KG (Porschestr. 8, Ahlen, Messe) und Carl Geringhoff GmbH & Co. KG (Nordstrasse 54, Ahlen, Patentanmelder); fertigende Einheit nicht zugeordnet. Konzern mit mehreren Werken (Ahlen, zweites deutsches Werk, USA): Sitzregel greift nicht, V fehlt. Verguss Mittel (A: Sensorik/Abstandsregelung, Magnetventile, Kabelsätze).
- Eigene Prüfung: WebSearch Patent Geringhoff: bestätigt EP0131853 (Carl Geringhoff GmbH & Co KG, Ahlen, 1983 angemeldet, Maisernte-Vorsatz mit Klappteilen), DE102019127508A1 (2019, Schneidwerk, Anmelder Carl Geringhoff GmbH & Co. KG, Titel gekürzt), DE2823743C2 (Haspel/Schneidtisch-Höhenverstellung, Geringhoff als Zitat) (alle S, Google-Patents-/EPO-Snippet, Rechtsstand nicht geprüft); ipqwery: ca. 107 Datensätze/93 Patente (S). Kein Treffer zu Verguss/Dichtung/Klebung; keine Quelle zu Elektronik/Sensorik in Ahlen. Aktuelle Anmeldungen (2019) zeigen aktive Entwicklung, nicht Verguss.
- Korrekturen an Toms Feldern: Feld 9 um DE102019127508A1 (2019, S) ergänzt; sonst bestätigt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Impressum/Handelsregister geringhoff.com: Welche Gesellschaft fertigt in Ahlen, wo liegt das zweite deutsche Werk? (b) Enthalten die Vorsätze Sensorik/Elektronik (Produktseite/Datenblatt, z. B. Abstandsregelung)? (c) Patent-Datenbanken im Browser, Anmelder beide Gesellschaften, Stichworte potting/Dichtung/Sensor. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Ahlen (S), Verguss (A), Patentliste (S). Stichprobe für Jey: ja (Identität, Werkzuordnung).

## 18. hairtex e.K. | Halle 20, Stand 1210
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat: Textil/Arbeitsbekleidung, kein Vergussprodukt).** Alle Bauteile Niedrig (A). Kein E-Beleg V; Rot nicht zulässig.
- Eigene Prüfung: CRM-Skript: neu. Keine eigene Websuche.
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Frage an Jey: Textil ohne Vergussbezug streichen? Falls Prüfung gewünscht: Produktsortiment auf hairtex-Seite lesen (gibt es beheizte/elektronische Produkte?). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (A/S). Stichprobe für Jey: nein.

## 19. Hardi GmbH | Halle 22, Stand C30
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2/E3: Vertriebsgesellschaft, Fertigung in DK/FR laut Fachpresse S).** Rot nicht zulässig, weil nur S. Verguss Hoch auf Produktebene (A: Spritzcomputer, Magnetventile), aber ohne Fertigung DE/AT/NL.
- Eigene Prüfung: WebSearch "HARDI GmbH Wedemark Impressum ...": keine Seite der HARDI GmbH gefunden, Wedemark-Adresse (Tom: Händlerportal landwirt.com, S) damit nicht bestätigt; die Suche ist ergebnislos (kein Gegenbeleg). Konzern HARDI International A/S / Exel Industries: kein CRM-Treffer.
- Korrekturen an Toms Feldern: Feld 4/17: Adresse Wedemark nur aus einer Händlerportalquelle, Eigenprüfung unbestätigt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): hardi.com/de Impressum im Browser lesen: Sitz und Rolle der HARDI GmbH; Gibt es Montage/Fertigung in DE/AT/NL (Jobs, Standortseite)? Bestätigt sich "nur Vertrieb, Werke DK/FR" mit V-Zitat: Rot (E2/E3). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: ja (Rot-Kandidat, Adresse ungeklärt).

## 20. Huber Gülletechnik Georg Huber GmbH & Co. KG | Halle 18, Stand 80
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Fertigungsbeleg fehlt).** Telefonbuch führt "Landmaschinenhandel"; Eigenfertigung nicht belegt (Händler vs. Hersteller offen, bei Händler: E2). Sitzregel greift nicht, Herstellerstatus unbelegt. Verguss Mittel (A: Motor, Schaltkasten).
- Eigene Prüfung: CRM-Skript: Wortwurzel-Treffer nur "Huber Automotive AG" (bekannte_firmen Zeile 1084, Kern-Name verschieden): keine Namensgleichheit im Sinne der Jey-Entscheidung, kein Konzernbezug belegt, bleibt zur Bestätigung markiert. WebSearch "Georg Huber GmbH Tittmoning ... Eigenfertigung": nur Telefonbuch/Sellwerk/Topagrar bestätigt (Landmaschinenhandel, Produkt Güllepumpe DGP/ES-ZS, Standort Tittmoning); keine Quelle zur Eigenfertigung; Treffer zu Huber SE (Berching) und GEA sind andere Firmen, nicht vermischt.
- Korrekturen an Toms Feldern: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 5): georg-huber.de Impressum/Produktseiten im Browser lesen: Fertigt Huber Pumpen/Rührwerke in Tittmoning oder handelt/baut nur um? Wer liefert Motor und Schaltkasten? Gehört die Firma zu Huber Automotive AG (nur Namensbezug, unwahrscheinlich)? Aktion: nicht kontaktieren; bei reinem Handel an Jey (E2).
- Nicht verwendbare Aussagen: Fertigung Tittmoning (S), Verguss (A). Stichprobe für Jey: ja.

---

## nicht aufgenommen (bereits bekannt / unklar)
Keine Firma bekannt (Skript, Regel B2/M). Wortwurzel-Treffer "Huber Automotive AG" [DE] (Zeile 1084) zu Nr. 20: verschiedene Kern-Namen, nicht ausgeschlossen, zur Bestätigung durch Jey markiert.

## Einschränkungen
- Nur WebSearch (6 eigene Abfragen) und Bash verfügbar; kein Browser, kein Seitenlesen. Es gibt keine Stufe-V-Aussage. Alle Ampeln vorläufig; Nr. 12 ist nur ein schwaches Grün (Sitzregel, A/S).
- Eigene Websuche nur für Eder, Fliegl (2 Abfragen), Geringhoff, Huber, Hardi, priorisiert nach Aussicht. Für Nr. 11, 13, 14, 16, 18 keine eigene Websuche (Kurzprüfung: Skript und Toms Befund; Sitzungslimit/Priorität). Google Patents, Espacenet, DEPATISnet nie direkt abgefragt: Feld 9 bei allen zehn Firmen nach F5 unvollständig, ohne Rechtsstand.
- Wettbewerbereinsatz (Feld 16): nur Grep auf wettbewerber_referenzen.md, keine Einzelsuchen.
- Identität: kein Impressum/Handelsregister gelesen. Offene Fälle: Nr. 12 (Eder GmbH vs. Eder Landtechnik GmbH), 13 (Firma nicht identifiziert), 17 (zwei Gesellschaften), 19 (Adresse), 20 (Händler/Hersteller).
- Die Suche zu Hardi lieferte nur irrelevante Treffer; ihr Ergebnis ist kein Beleg für oder gegen die Wedemark-Adresse.
- Keine Kontakt-/Ansprechpartnersuche (Abschnitt K). Es wurde nichts verschickt, kein CRM-Feld geändert, kein git commit.
