# Tina Batch 06 – all about automation Düsseldorf 2026 (Prüfung von tom_batch_06.md)
Erstellt: 2026-10-15 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe: ausschließlich aaa_ergebnisse/tom_batch_06.md (10 Firmen).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Chrome-Werkzeuge und WebFetch standen nicht zur Verfügung. Nur WebSearch (21 Abfragen, Snippets/Zusammenfassungen). Es gibt in diesem Batch daher keine Stufe-V-Aussage von mir; "Zitat im Browser bestätigt" ist überall: nein. Patentdatenbanken (Google Patents, Espacenet, DEPATISnet) wurden von mir nicht direkt abgefragt.
Skripte: `batch_check.py ... --tina` meldet nur "Feld 11: keine Ampel" für alle 10 Blöcke (erwartet, Ampel ist Tinas Feld); sonst keine Beanstandung. `crm_abgleich.py` für jede Firma samt Konzern/Schwester selbst wiederholt (Ergebnis je Firma unten). Tabellenzeile = Zeilennummer aus Regeldatei D.
Verifikationsdatum aller Einträge: 2026-10-15. Kein Datenbankfeld geändert, nichts verschickt.

## Gesamtübersicht
| Nr | Firma (Stand) | Toms Einstufung | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|---|
| 1 | igus GmbH (603) | interessant | GELB | 5 | ja |
| 2 | ima-tec GmbH (140) | prüfenswert | GELB | 5 (Aspekt E1 offen) | nein |
| 3 | IMPADY (818) | kein Fertiger | GELB | 2 | ja |
| 4 | INperfektion GmbH (717) | prüfenswert | GRÜN (schwach, vorläufig) | 4 (Sitzregel) | ja |
| 5 | INSEVIS GmbH (615) | prüfenswert | GELB | 2 | ja |
| 6 | IXON B.V. (438) | unwahrscheinlich | GELB | 7 (Aspekt Zeile 2) | nein |
| 7 | JAM automation GmbH (118) | prüfenswert | GELB | 2 (Aspekt E1 offen) | ja |
| 8 | Janitza electronics GmbH (114) | interessant | GRÜN (vorläufig) | 4 (Sitzregel) | ja |
| 9 | Kaiser GmbH & Co. KG (115) | prüfenswert | GELB | 3 (Aspekt Zeile 5) | ja |
| 10 | Kalitec Verbindungstechnik GmbH (143) | kein Fertiger | GELB | 7 (Aspekt E2 nicht belegt) | nein |

Bilanz: 2 Grün, 8 Gelb, 0 Rot. Kein Rot, weil kein harter Ausschluss E1 bis E5 mit Stufe V belegt ist (Kalitec/IMPADY/ima-tec/JAM bleiben Verdachtsfälle).
CRM (selbst wiederholt): kein BEKANNT. Einziger Treffer: Kaiser, Präfix auf bekannte_firmen_DE-AT-NL.txt Zeile 1247 "Kaiser Elektroplanung GmbH [DE]" (auch bei "Kaiser Elektro" und "KAISER Verwaltungs GmbH" Wortwurzel). kundendatenbank_export.txt: keine Treffer, daher keine "Verifiziert am"-Prüfung nötig. Messe-Signal: laut Tom (Grep aaa_duesseldorf_2026.csv) keine Wettbewerber; von mir nicht wiederholt.

Patente (Prüfpunkt 8, nur eingeschränkt): Eigene WebSearch-Abfragen (Janitza "Patent Anmelder Vergussmasse", igus "Anmelder Vergussmasse/potting") fanden keine Patente mit Anmelder Janitza oder igus; die Treffer (DE1241908B Janitza-Zuordnung nicht erkennbar; EP2398644A1 und EP0587003A1 igus-Zuordnung nicht erkennbar) sind keinem Anmelder zugeordnet und nicht verwendbar. Das ist keine Datenbankabfrage mit Anmelderfilter, Feld 9 bleibt wie bei Tom nur eingeschränkt belastbar. Nachzuholen im Browser für alle 10: Google Patents/Espacenet/DEPATISnet, Anmelder-Varianten (igus GmbH/igus SE & Co. KG; Janitza electronics/Eugen Janitza GmbH; SAR Group) und enge Suche (potting compound OR Vergussmasse). Rechtsstand der Kaiser-Altpatente (1975 bis ca. 1998) nicht geprüft.

---

## 1. igus GmbH | Stand 603
**Ampel: GELB (Tabellenzeile 5).** Ohne Browser/Web-Abruf geprüft, vorläufig. Mehrwerks-Konzern, daher wäre Stufe V für die Fertigung nötig (Sitzregel greift nicht); belegt ist nur Köln als Sitz und Kunststoff-Spritzguss (S). Ob Schrittmotoren, Encoder-Elektronik und Leitungskonfektion mit Steckern in Köln entstehen, ist offen. Verguss Hoch (A) wäre gegeben, deshalb Gelb statt Grün nur wegen der Fertigungsbeleg-Lücke.
- Korrekturen an Toms Feldern: Feld 7 bleibt Hoch, aber nur S (Tom korrekt gekennzeichnet). Eigene Suche bestätigt: igus-Campus Köln "produziert, testet und forscht" (Suchzusammenfassung, S), 857 Spritzgussmaschinen Köln (computer-automation.de, S); Motorenfertigungsort weiter nicht belegt. Feld 17: Adressverzeichnis nennt "igus GmbH, Spicher Straße 1a, 51147 Köln"; Stellenanzeigen führen "igus SE & Co. KG" (S). Rechtsform bleibt offen, Sitz Köln einheitlich, deshalb kein Identitäts-Gelb (Zeile 2), aber Auftrag Impressum. Feld 9: eigene Suche ohne igus-zugeordneten Verguss-Patentfund (Tom ebenso); Patsnap-Zahl 2.146 ist Sekundärquelle (S, nicht verwendbar). Aussage "Leitungen mit überspritzten Steckern": Produktseite igus.ca nennt Stecker "IP66/67 ... before the injection molding" (S); das ist Überspritzen im Thermoplast, nicht zwingend Harzverguss (Tom korrekt vorsichtig).
- CRM: neu (crm_abgleich.py "igus GmbH", "igus SE & Co. KG": kein Treffer). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?; wettbewerber_referenzen.md ohne igus, Tom-Suchen).
- Zitat im Browser bestätigt: nein (Browser nicht verfügbar).
- Nachrecherche-Auftrag (Gelb): (a) Werden Schrittmotoren (NEMA 17/23), Encoder-/Sensorelektronik und konfektionierte Leitungen/Stecker in Köln (oder Rest DE) gefertigt und wo ist die Vergussstufe? Wo nachsehen: igus.de Produktseite Schrittmotoren/Datenblatt (Herkunftsland, "Made in"), igus-Karriereseite Köln (Montage Elektronik/Konfektion 2025/2026), Pressemeldungen zur Kölner Produktion. (b) Impressum igus.de: igus GmbH oder igus SE & Co. KG, Registerauszug (Amtsgericht Köln). (c) Aktuelle V-Quelle (2025/2026) für Fertigung am Kölner Werk. Aktion: noch nicht kontaktieren.
- Nicht verwendbare Aussagen: Fertigung Hoch (S); Verguss alle Bauteile (A); Motorenfertigung Köln (?); Patsnap-Patentzahl (S); Mitarbeiter/Umsatz (S, ohne Ampel-Einfluss); Produkt-zu-Werk-Zuordnung (offen). Stichprobe für Jey: ja (Toms "interessant", aber nur S).

## 2. ima-tec GmbH | Stand 140
**Ampel: GELB (Tabellenzeile 5; E1 offen).** Ohne Browser/Web-Abruf geprüft, vorläufig. Tochter der SAR Group (seit 2017): Sitzregel nach Regeldatei D greift bei Konzern/Mehrwerk nicht, Stufe V für die Fertigung fehlt. Eigene Suche: Kürnach bei Würzburg, "über 95 Mitarbeiter", Sondermaschinenbau/Montage (Messeprofil und Stellenanzeige, S); keine Hinweise auf Kleben/Dosieren als Produkt.
- Korrekturen: Feld 7 Hoch/A ist nach Sitzregel wegen SAR-Konzernbezug zu hoch gegriffen, zu führen als Mittel/S bis Fertigungsbeleg V. Feld 17: Verwechslung mit IMA-TEC GmbH Homburg/Saar (automa.net, Demontage/Elektrotechnik) ausgeschlossen, nicht vermischen. Verguss Mittel (A, verbaute Zukaufteile; Endprodukt-Regel) bleibt Toms Wert.
- CRM: neu (crm_abgleich.py "ima-tec GmbH", "SAR Group": kein Treffer). Konzernbezug SAR im CRM: nein. Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?).
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): (a) Wird in Kürnach selbst montiert/gefertigt (Stellenanzeige "Montage Sondermaschinen" Kürnach gilt als V für den Fertigungsort) und ist ima-tec die fertigende Einheit innerhalb der SAR Group? Wo: ima-tec-gmbh.com Karriere/Kompetenzseite, SAR-Group-Seite (Standorte). (b) E1-Frage: Bietet ima-tec Dosier-/Kleb-/Vergussstationen als Anlagenprodukt an (Integrator)? Produkt-/Referenzseiten lesen. (c) Impressum/HRB 9371 Würzburg gegenlesen. Aktion: keine Ansprache vor Klärung (b).
- Nicht verwendbare Aussagen: Fertigung Kürnach (A/S); Verguss/Klebstationen in Kundenanlagen (?); Mitarbeiterzahl (S). Stichprobe für Jey: nein.

## 3. IMPADY | Stand 818
**Ampel: GELB (Tabellenzeile 2).** Ohne Browser/Web-Abruf geprüft, vorläufig. Identität nicht belegt: einziger Fund ist ein unbeanspruchtes Startbase-Profil "IMPADY GmbH, Darmstadt, Consulting, Seed Stage, Platform B2B, 2025" (S); die Vorgabe Hoppstädten-Weiersbach wird von keiner Quelle gestützt (eigene Suche "IMPADY GmbH Hoppstädten-Weiersbach" bestätigt: kein Treffer). Harter Ausschluss E2 (Beratung/Plattform) wahrscheinlich, aber nicht mit Stufe V belegt, daher nicht Rot.
- Korrekturen: Toms Einstufung "kein Fertiger (vorläufig)" ist nachvollziehbar, aber nur S. Website unbekannt.
- CRM: neu (crm_abgleich.py "IMPADY": kein Treffer). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): Gibt es eine IMPADY GmbH mit Handelsregistereintrag, und ist die Messefirma (Hoppstädten-Weiersbach) damit identisch? Wo nachsehen: Ausstellerprofil auf allaboutautomation.de (Düsseldorf, Stand 818) im Browser, Handelsregister/Unternehmensregister (Darmstadt und Amtsgericht Bad Kreuznach/Idar-Oberstein-Umfeld), Website per Domain-Suche. Wenn Beratung/Plattform ohne Hardware: Rot nach E2 mit Quelle. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (Fertigung ?, Verguss A, Startbase S, Mitarbeiterzahl S). Stichprobe für Jey: ja (Identität nur Jey/Messeliste klärbar).

## 4. INperfektion GmbH | Stand 717
**Ampel: GRÜN, schwach (Tabellenzeile 4, Sitzregel).** Ohne Browser/Web-Abruf geprüft, vorläufig. Anlagen-/Automatisierungsbauer mit erkennbarem Standort Wegberg, eigene Leistungen (Elektronikfertigung, Schaltschrankbau laut Eigenangabe, S), kein Konzernhinweis und kein Auslagerungshinweis gefunden; Verguss Mittel (A: Elektronikbaugruppen, Schaltschrank-/Steuerungskomponenten mit Netzteilen/Relais/Sensoren, Endprodukt-Regel).
- Korrekturen: keine an Toms Werten (Fertigung Hoch A, Verguss Mittel A bestätigt). Eigene Suche zum Impressum blieb erfolglos (kein INperfektion-Impressum, keine Registerdaten; ein Wegberger Registerfund ist nicht zuordenbar und nicht verwendet), Feld 17 bleibt TEILWEISE (S). Hinweis: item-Plus-Partner (Profilsysteme) deutet auf Handelsanteil; Einzel-/Sonderanlagen (Koksofen-Servicemaschinen) statt Serie. Das Tätigkeitsprofil weicht von der Triage ab (Automatisierer statt reiner Schutzeinhausungen).
- CRM: neu (crm_abgleich.py "INperfektion GmbH", "item": kein Treffer). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Zitat im Browser bestätigt: nein.
- Nachrecherche (kein Gelb, für Mail-Stufe nötig): Werden Elektronikbaugruppen in Wegberg selbst bestückt/vergossen oder nur Schaltschränke verdrahtet? Website inperfektion.de Leistungen, Impressum, Stellenanzeigen Wegberg (Montage/Elektronik) im Browser lesen; Handelsregister Mönchengladbach.
- Nicht verwendbare Aussagen: Fertigung Wegberg (A, gestützt S); Eigenverguss (unbelegt); Verguss alle Bauteile (A); Impressum/Geschäftsführer (S). Stichprobe für Jey: ja (Grün stützt sich auf Sitzregel A + Eigenangabe, Identität nur S; bei negativem Befund Richtung Zeile 5/6 kippen).

## 5. INSEVIS GmbH | Stand 615
**Ampel: GELB (Tabellenzeile 2).** Ohne Browser/Web-Abruf geprüft, vorläufig. Identität nicht eindeutig: Messeprofile führen "INSEVIS GmbH" und "INSEVIS Vertriebs GmbH" (SPS Nürnberg-Verzeichnis nennt "INSEVIS Vertriebs GmbH"), LEI-Record zeigt "INSEVIS Holding GmbH, Am Weichselgarten 7, Erlangen, HRB 20784 Fürth" (S). Welche Gesellschaft ausstellt und fertigt, ist offen. Fertigung nur Werbeaussage "made in Germany" (S, Messetext nach Regel N5). Verguss Mittel (A).
- Korrekturen: Feld 7 Mittel/S bestätigt. Eigene Suche brachte nur Messe- und Verzeichnisseiten; neu: Panel-SPS-Beschreibung "IP65-dichte Metallfront" (Messetext, S), unterstützt Dichtung/Bonding Mittel (A), kein Beleg für Fertigungsort.
- CRM: neu (crm_abgleich.py "INSEVIS GmbH", "INSEVIS Holding GmbH", "INSEVIS Vertriebs GmbH": kein Treffer). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): (a) Welche Gesellschaft ist Hersteller und Aussteller (INSEVIS GmbH, Vertriebs GmbH, Holding)? Wo: insevis.com Impressum, Handelsregister Fürth (HRB 20784 und die der GmbH/Vertriebs GmbH), Ausstellerprofil 204670 gegenlesen. (b) Wo werden S7-Panels/SPS/Gateways gebaut (Erlangen oder EMS im Ausland)? Wo: Stellenanzeigen Erlangen (Montage/Produktion), Produktdatenblätter (Herkunftsland), Konformitätserklärung. Aktion: Beobachtung.
- Nicht verwendbare Aussagen: "made in Germany" (S, Eigenwerbung); Fertigungsort (S/?); Gesellschaftszuordnung (nicht belegt); Verguss (A). Stichprobe für Jey: ja.

## 6. IXON B.V. | Stand 438
**Ampel: GELB (Tabellenzeile 7; Aspekt Identität/Zeile 2 wegen Beugen/Overloon).** Ohne Browser/Web-Abruf geprüft, vorläufig. Fertigungsort der Hardware nicht belegt (Fertigung in DE/AT/NL: weder Beleg noch Gegenbeleg; Sitz NL: Beugen, Zuster Bloemstraat 20, S), Verguss Niedrig (A: IP20-Router im Metallgehäuse für Schaltschrank; Händlerseiten, S). Zeile 6 passt nicht, weil Fertigung nicht belegt ist; Rot nicht möglich, weil keine E-Bedingung belegt ist.
- Korrekturen: Sitz Beugen durch eigene Suche gestützt (Verzeichnis und fhi.nl-Ausstellerseite, S); Overloon aus der Triage ist nur über ein Verzeichnis mit AT-Automation B.V. und eine Nachricht erwähnt, kein Beleg als IXON-Sitz. Hardware "selbst entworfen" (S), Fertigungsort offen. Toms "unwahrscheinlich" ist nachvollziehbar.
- CRM: neu (crm_abgleich.py "IXON B.V.": kein Treffer). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, niedrige Priorität): Wo wird der IXrouter gefertigt (Beugen/NL oder EMS Asien) und wie ist die Schutzart/Bauweise (vergossen oder nur Schutzlack)? Wo: Datenblatt/Konformitätserklärung IXrouter3 auf ixon.cloud, KvK-Auszug (Sitz Beugen/Overloon), Stellenanzeigen. Aktion: nicht priorisieren.
- Nicht verwendbare Aussagen: Fertigungsort (?); IP20 (S, Händler); Verguss Niedrig (A). Stichprobe für Jey: nein.

## 7. JAM automation GmbH | Stand 118
**Ampel: GELB (Tabellenzeile 2; Aspekt E1).** Ohne Browser/Web-Abruf geprüft, vorläufig. Sitz-Abweichung zur Triage-Vorgabe: Quellen nennen übereinstimmend Radevormwald (Albert-Einstein-Str. 6, 42477; Messeprofile Düsseldorf/Berlin/Wetzlar, Implisense, Verzeichnisse, alle S), nicht Köln. Nach Regel O ist bis zur Bestätigung durch Jey höchstens Gelb möglich. Ohne diese Abweichung wäre es Grün (Zeile 4): Sondermaschinenbauer, ca. 30 Mitarbeitende, Sitzregel A; Verguss Mittel (A, verbaute Zukaufteile).
- Korrekturen: Fertigung Hoch/A bestätigt, Sitz Radevormwald bestätigt (S, nicht Köln). Namensvettern JAM Software GmbH (Trier), JAMI GmbH (Siegen), JAM-Tech (AT) ausgeschlossen. E1-Frage unverändert offen: Messetext nennt "Cobot ... präzise Injektion von Flüssigkeiten" (S), keine Aussage zu Dosier-/Vergussanlagen als Produkt; Website nicht gefunden.
- CRM: neu (crm_abgleich.py "JAM automation GmbH": kein Treffer). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): (a) Identität: Impressum/Handelsregister (Wuppertal) von JAM automation GmbH, Radevormwald, und ob es ein "Köln" gibt (Quelle der Vorgabe bei Jey erfragen). (b) E1: Verkauft JAM Dosier-/Klebe-/Vergusszellen als Produkt? Messeprofil 223493 vollständig und Website/Referenzen im Browser lesen. Aktion: keine Ansprache vor Klärung (b).
- Nicht verwendbare Aussagen: Fertigung (A/S); Dosierzelle (?); Verguss (A); Bilanzsumme/Mitarbeiter (S). Stichprobe für Jey: ja (Sitz-Vorgabe Köln/Radevormwald).

## 8. Janitza electronics GmbH | Stand 114
**Ampel: GRÜN (Tabellenzeile 4, Sitzregel), vorläufig.** Ohne Browser/Web-Abruf geprüft, vorläufig. Gerätebauer mit eigenen Produkten und erkennbarem Standort Lahnau (mittelständisch, Inhaber Markus Janitza), Fertigung am Sitz durch zwei unabhängige Fundstellen gestützt (Wirtschaftsforum-Interview: "entwickelt und gefertigt" am Standort Lahnau; computer-automation.de-Kurzportrait: "entwickelt und fertigt die gesamte Produktpalette ... in Deutschland am Standort Lahnau", beide S). Hinweise auf Auslagerung ins Ausland: keine gefunden. Verguss Hoch (A): Stromwandler/Rogowski-Spulen, Netzteile, Messelektronik (Bauteil-Regel, Maximum); ein Gegenbeleg liegt nicht vor.
- Korrekturen: keine an Toms Werten; ergänzt: Neubau Produktionsstätte (30 Mio. EUR, 10.000 m², Fertigstellung laut Firmenpräsentation 2. Quartal 2026, S) und IHK Lahn-Dill "40 Jahre Janitza" (S) stützen den Standort; Stellenanzeigen Lahnau (Bestücker THT, Endmontage, Indeed, S, Datum nicht erkennbar). Eine Stellenanzeige am Sitz gilt erst nach Lesen im Browser als V. Eigene Datenblatt-Suche (Rogowski-Spulen 15.03.609/610, Händlerdaten: 1 kV CAT III, -40 bis +80 °C, Genauigkeitsklasse 0,5) liefert keine Aussage zur Vergussart: Verguss bleibt A. Feld 17: Janitza electronics GmbH, Lahnau, HRB 928 Wetzlar (S); Janitza Deutschland GmbH (HRB 8716) separat, Eugen Janitza GmbH nur als historische Mutter genannt (S), Impressum nicht gelesen.
- CRM: neu (crm_abgleich.py "Janitza electronics GmbH", "Janitza Deutschland GmbH": kein Treffer). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Zitat im Browser bestätigt: nein.
- Nachrecherche (kein Gelb, für Mail-Stufe nötig): (a) Aktuelle V-Quelle für Fertigung/Montage in Lahnau (Karriereseite Janitza, Stellenanzeige Fertigung, Pressemeldung Neubau 2025/2026) im Browser. (b) Impressum der fertigenden Gesellschaft (electronics GmbH vs Deutschland GmbH). (c) Datenblatt Stromwandler/Netzteil: Vergussmasse oder Schutzart (IP57) zur Aufwertung von A auf V. (d) Patentsuche mit Anmelder "Janitza" und Varianten in Google Patents/Espacenet/DEPATISnet nachholen.
- Nicht verwendbare Aussagen: alle Fertigungs- und Verguss-Aussagen sind S oder A (keine Stufe V); "IP57-Spulen" (Händler/Handbuch-Snippet, S); Mitarbeiterzahl (S, widersprüchlich); Produkt-zu-Werk-Zuordnung (Stromwandler in Lahnau): offen. Stichprobe für Jey: ja (Grün ohne einen einzigen Browser-Beleg; Toms "interessant").

## 9. Kaiser GmbH & Co. KG | Stand 115
**Ampel: GELB (Tabellenzeile 3; Aspekt Zeile 5).** Ohne Browser/Web-Abruf geprüft, vorläufig. CRM unklar: Präfix-Treffer "Kaiser Elektroplanung GmbH [DE]" (bekannte_firmen_DE-AT-NL.txt Zeile 1247, ohne Ortsangabe) bei crm_abgleich.py für "Kaiser GmbH & Co. KG", "KAISER Verwaltungs GmbH" und "Kaiser Elektro"; ob es dieselbe Einheit ist, entscheidet Jey. Zusätzlich Gruppe mit mehreren Standorten (AGRO CH, HELIA BE, Attema NL, Gorinchem; Fertigungsrolle der Töchter unbekannt, eigene Suche S), daher wäre für die Fertigung Stufe V nötig; vorhanden nur Stellenanzeigen-Snippets (Spritzguss-Einrichter Arburg/Engel, eigener Werkzeugbau Schalksmühle, S). Verguss Mittel (A: Dichtungseinsätze, luftdichte Dosen).
- Korrekturen an Toms Feldern: Feld 12: Toms "unklar" bestätigt. Toms Formulierung "Jey bestätigt, dass Kaiser Elektroplanung nicht dieselbe Einheit ist" ist eine Behauptung ohne Beleg im Batch; als offene Entscheidung behandeln, nicht als erledigt. Feld 4: Mitarbeiterzahl "über 600" und "family-owned" aus Verzeichnissen (S, ohne Ampel-Einfluss). Kein Beleg für Eigenfertigung von Dichtungen/Verklebung; Kleberkragen wird laut Flyer von Kunden verarbeitet. Bauteil-Regel: höchstes Bauteil Mittel (A), kein Hoch. Feld 9: Kaiser-Patente sind alte Installationsdosen-Patente (Tom), Rechtsstand nicht geprüft, schwaches Signal.
- Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): (a) CRM: Ort/Tätigkeit des Datensatzes "Kaiser Elektroplanung GmbH" im CRM prüfen (Kundendatenbank, Excel; die Textliste hat keine Ortsangabe), ob dieselbe Einheit/Gruppe wie KAISER GmbH & Co. KG Schalksmühle; wenn dieselbe: Rot nach Zeile 1 (E5). (b) Fertigung: Welche Werke gehören zur Gruppe, und werden luftdichte Dosen/Dichtungseinsätze in Schalksmühle gefertigt und wie gedichtet? Wo: kaiser-elektro.de Unternehmen/Standorte und Datenblatt luftdichte Dosen, Stellenanzeigen Schalksmühle im Browser. (c) Impressum/AG Iserlohn HRA 3479. Aktion: erst nach (a) ansprechen.
- Nicht verwendbare Aussagen: Fertigung Schalksmühle (S); Verguss/Dichtung (A); Fertigungsrolle der Töchter (?); Mitarbeiterzahl (S). Stichprobe für Jey: ja (CRM-Einheit).

## 10. Kalitec Verbindungstechnik GmbH | Stand 143
**Ampel: GELB (Tabellenzeile 7; E2 nicht ausreichend belegt).** Ohne Browser/Web-Abruf geprüft, vorläufig. Eigene Suche bestätigt: Selbstbeschreibung "Online-Industriegroßhandel seit 2006", Implisense-Zweck "Technischer Industriehandel für elektronische und elektromechanische Bauteile ... Kabelschuhe, Steckverbinder, konfektionierte Kabel und Kabelbäume" (alle S), Adresse Lindgesfeld 8h, 42653 Solingen (Telefonbuch, S). Das spricht stark für Händler (E2), ist aber nur Snippet-Stufe; Kabelkonfektion "nach Maß" kann Eigenfertigung bedeuten. Rot verlangt Stufe V.
- Korrekturen: keine an Toms Werten. Kein Impressum/Register gefunden (ein OpenRegister-Treffer gehört zu einer anderen Firma und wurde nicht verwendet).
- CRM: neu (crm_abgleich.py "Kalitec Verbindungstechnik GmbH": kein Treffer). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?). Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, niedrige Priorität): Fertigt Kalitec Leitungen/Kabelbäume selbst in Solingen? Wo: kabelschuhe-shop.de Impressum und Seite "Kabelkonfektion", Stellenanzeigen Solingen (Konfektion). Bei reinem Handel: ROT nach E2 mit Quelle (V). Aktion: nicht priorisieren.
- Nicht verwendbare Aussagen: Handel statt Fertigung (S, Tendenz); Eigenfertigung Konfektion (?); Verguss (A). Stichprobe für Jey: nein.

---

## Konsistenz und Auffälligkeiten
- Tom nutzte die Sitzregel bei ima-tec (Tochter der SAR Group) zu großzügig; bei Konzern/Marke ist V nötig. Korrektur oben.
- JAM: Sitz-Vorgabe der Triage (Köln) nicht belegt, Quellen sagen Radevormwald; wie bei Lehre 1 Identität zuerst, daher Gelb Zeile 2 trotz sonst grüner Eingaben.
- Kaiser: Toms Satz "Jey bestätigt" ist als Aufgabe zu verstehen, nicht als Ergebnis.
- Alle Grün-Ampeln (INperfektion, Janitza) stützen sich nur auf Stufe S/A und die Sitzregel; vor Mailverwendung Stufe V nötig.

## Einschränkungen
- Browser (Chrome-Werkzeuge) und WebFetch nicht verfügbar: keine Quelle von Tom oder von mir im Volltext gelesen; kein Zitat im Browser bestätigt; keine Stufe-V-Aussage. Alle Ampeln sind deshalb vorläufig. Nach Verfügbarkeit des Browsers zuerst prüfen: Janitza, igus, INperfektion (Grün/"interessant"), dann Kaiser, JAM, INSEVIS.
- WebSearch-Budget: 21 Abfragen, verteilt auf alle Firmen (Schwerpunkt igus, Janitza, JAM, Kaiser, INSEVIS, IMPADY); Antworten sind Zusammenfassungen/Snippets. Für ima-tec, IXON, INperfektion und Kalitec jeweils nur 1 bis 2 Abfragen.
- Patentdatenbanken nicht direkt abgefragt (siehe oben); Feld 9 aller Firmen nur eingeschränkt belastbar, Batch bleibt hinsichtlich Feld 9 UNVOLLSTÄNDIG und ist im Browser nachzuholen (Regel F5).
- Handelsregister/Impressen nicht gelesen; Registerangaben sind Snippets (S). Kundendatenbank (Excel) nicht lesbar, nur Textexport verwendet.
- Größe/Umsatz und Kontakte nicht geprüft (Regeldatei D, K). Datenbankfelder nicht geändert, nichts verschickt.
