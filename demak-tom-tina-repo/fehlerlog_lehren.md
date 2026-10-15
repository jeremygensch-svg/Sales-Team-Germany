# Fehlerlog und Lehren für Tom und Tina (Stand 2026-10-14)

Jede Korrektur von Jey wird hier als Fall ergänzt (Firma | Fehler | Ursache | neue Regel). Tom und Tina lesen den Abschnitt "Lehren" in Schritt 0.

## Lehren (verbindlich, aus den Kalibrierläufen 2026-10-12 bis 14)
1. **Identität zuerst.** Listen aus Gemini oder anderen KI-Quellen haben bei der Hälfte der Firmen Sitz oder Namen falsch (Pironex Rostock statt Darmstadt, Schildknecht Murr statt Mannheim, Steinel Herzebrock statt Herne, Kredig Obernburg/Mainhausen statt Darmstadt, Proservia Eschborn, Jäger zwei Firmen vermischt). Name, Rechtsform, Adresse und Register oder Impressum prüfen (Feld 17).
2. **Konzernabgleich.** Bei Tochter- und Markenfirmen den Konzern gegen das CRM prüfen (Reijnen Sealing: Member of TTS Group, TTS GROUP steht im CRM). Das Skript crm_abgleich.py mit Firmen- und Konzernnamen aufrufen.
3. **Sekundärquellen sind keine Belege.** Wikipedia, Wirtschaftsforum-Kurzfassungen und WebFetch-Kurzfassungen sind höchstens Stufe S. Steinel: Wikipedia nannte Leipzig als Fertigung, die Standortseite zeigt aber nur Kunststoff in Leipzig, Elektronik und Verguss in Rumänien/Moldau.
4. **"In Deutschland entwickelt" ist keine Fertigung** (OASE). "Production facilities in Germany, Brazil, USA and China" belegt Nürtingen nicht (Heller).
5. **Gesellschaft ist nicht Werk.** Die Scherdel GmbH in Marktredwitz ist Zentrale; gefertigt wird in Wiesau. Bei Gruppen immer die fertigende Einheit nennen.
6. **Ein Gegenbeleg zu einem Bauteil stuft die Firma nicht herab** (Dentsply Sirona: Röntgenstrahler ölisoliert, aber Steuerelektronik, Sensorik, Mikromotoren). Verguss nach höchstem Bauteil bewerten.
7. **Kleine Dosiermengen zählen** (Medizintechnik).
8. **Patente nie auslassen.** Mindestens zwei Datenbanken; große Trefferlisten zusätzlich mit enger Suche (potting compound OR Vergussmasse) (Scherdel-Patent wurde in der breiten Suche übersehen). Anmelder prüfen (gleichnamige Firmen, Personen als Anmelder).
9. **Negativbefunde sind kein Beweis.** "Kein Treffer" und "kein Hinweis" immer mit den ausgeführten Suchen.
10. **Tom und Tina nie im selben Agenten** als Prüfung (Unabhängigkeit).
11. **Prozentwerte täuschen Genauigkeit vor** (Fertigung 65 % auf 90 % zwischen zwei Läufen bei gleichem Beleg): Skala Hoch/Mittel/Niedrig mit Belegstufe.
12. **Website-Regeln:** Google Patents lädt im Browser verzögert (Screenshot vor dem Auslesen, Ergebnisliste per DOM/Screenshot); Espacenet-Direkt-URL mit pa=... funktioniert; nordson.com und reijnensealing.com können Textlesen verweigern; Captcha/Bot-Prüfung nie lösen.

13. **Altmarken und Abkürzungen beim CRM-Abgleich mitgeben.** crm_abgleich.py findet nur, was als Argument übergeben wird: immer Firmenname, Konzern, frühere Namen und Abkürzungen (HBK = früher HBM = Hottinger Baldwin Messtechnik). Gleiche Kürzel im CRM können dieselbe Firma sein.
14. **Patentstatus ist Pflicht.** "Erteilt" reicht nicht: Withdrawn, Expired oder Fee Related nennen (HBK DE10350724B4 erloschen; Caterpillar EP2993361A1 und Roche EP2151680A1 zurückgezogen). Zurückgezogene oder erloschene Patente sind nur ein schwaches Zusatzsignal, kein Verguss-Beleg.
15. **Patentsuche mit korrekter Anmelder-Schreibweise.** "Deere" + "potting compound" statt voller Firmenname; bei Mitanmeldern den Hauptanmelder nennen (Roche AG statt Roche Diagnostics).
16. **Impressum der fertigenden Einheit lesen.** Die Domain gehört oft einer anderen Gesellschaft (roche.de = Roche Deutschland Holding; deere.de = John Deere Walldorf International GmbH).
17. **Ein Beleg von 2022 ist keine aktuelle Fertigung.** Aktuelle Quelle (2025/2026) nötig, sonst Stufe S oder Nachrecherche (Heidelberger Druck Wallbox).

## Fälle
| Datum | Firma | Fehler | Ursache | neue Regel |
|---|---|---|---|---|
| 2026-10-12 | Reijnen Sealing | Tom meldete "kein CRM-Treffer", TTS GROUP steht im CRM | Konzern nicht abgeglichen | Regel M, crm_abgleich.py |
| 2026-10-12 | Dentsply Sirona | Tina stufte Firma auf Gelb wegen eines ölisolierten Bauteils | Ein Bauteil statt Gesamtprodukt bewertet | Bauteil-Regel (D), Jey 2026-10-14 |
| 2026-10-12 | Steinel | Leipzig als Fertigung von Elektronik angenommen | Wikipedia als Quelle | Sekundärquellen nur Stufe S |
| 2026-10-12 | Scherdel | Patent mit Epoxid-Vergussmasse in breiter Suche übersehen | Trefferliste zu groß | enge Zusatzsuche (F5) |
| 2026-10-14 | HBK (Darmstadt) | Tom: "CRM neu", dabei steht "HBM" (Altmarke) im CRM | Altname nicht als Argument übergeben | Lehre 13, Skriptaufruf mit Altnamen |
| 2026-10-14 | HBK / Caterpillar / Roche | Patente als "erteilt/Verguss V" gemeldet, tatsächlich erloschen oder zurückgezogen | Rechtsstand nicht geprüft | Lehre 14, Patentstatus Pflicht |
| 2026-10-14 | Deere | Patentsuche mit falscher Anmelder-Schreibweise ohne Treffer, Impressum der falschen Gesellschaft | Suchbegriff und Domain-Inhaber nicht geprüft | Lehren 15, 16 |
