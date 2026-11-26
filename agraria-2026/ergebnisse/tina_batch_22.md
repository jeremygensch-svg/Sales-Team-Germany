# Tina Batch 22 - agraria 2026, Wels (Prüfung von tom_batch_22.md)
Erstellt: 2026-11-25 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_22.md (10 Firmen, Tom-Nr. 1 bis 10 = Messeliste Nr. 211 bis 220). Länder DE/AT/NL, alle zehn laut Messeliste AT.
**VERMERK ÜBER ALLEN AMPELN: ohne Browser geprüft, vorläufig.** Nur WebSearch (4 Abfragen, Snippets) und Bash. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün ist mailtauglich.
Verifikationsdatum aller Einträge: 2026-11-25. Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md).
Entscheidungen Jey angewandt: Verbände/Prüfdienstleister/Forschung raus; CRM-Namensgleiche raus (hier keine); Anlagenbauer bleiben, außer sie bauen selbst Verguss-/Dosieranlagen (E1; hier trifft das auf keine Firma zu).

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 (211) | Mammut Maschinenbau GmbH (H19/St50) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 2 (212) | MAS Seeds (H23/St305) | GELB | 2 (Rot-Kandidat: kein Fertiger) | nein |
| 3 (213) | Maschinen Mauritz GmbH (H18/St520) | GELB | 7 (Rot-Kandidat E2) | nein |
| 4 (214) | Maschinenhandel Zauner (H18/St510) | GELB | 7 (Rot-Kandidat E2) | nein |
| 5 (215) | Maschinenring Österreich Happy am Hof (H21/St1320) | ROT | 1 (E2 Verband, Entscheidung Jey) | nein |
| 6 (216) | Mauch Ges.m.b.H & Co.KG (H21/C60) | GELB | 7 (Rot-Kandidat E2) | ja |
| 7 (217) | MAVUM Vertrieb und Marketing GmbH (H23/St480) | GELB | 2 (Rot-Kandidat E2) | nein |
| 8 (218) | Maxwald Maschinen GmbH (H20/A20) | GRÜN (schwach) | 4 (Sitzregel) | ja |
| 9 (219) | Medl GmbH (H22/C40) | GELB | 7 (Rot-Kandidat E2) | ja |
| 10 (220) | Milkivit & Milkiwean (H23/St190) | GELB | 2 (Rot-Kandidat: kein Fertiger) | nein |

Zahlen: Grün 2 (beide schwach, ohne V), Gelb 7, Rot 1.

CRM (Regel B2/M): `python3 crm_abgleich.py` selbst wiederholt für Mammut (Maschinenbau/Kurz), MAS Seeds, MAS-Austria, Maisadour, Maschinen Mauritz, Mauritz, Maschinenhandel Zauner, Zauner, Maschinenring, Happy am Hof, Mauch (beide Schreibweisen), MAVUM, Maxwald (beide), Medl (beide), Milkivit, Milkiwean, Trouw Nutrition, Nutreco sowie Herstellernamen Weidemann, Merlo, Pedrotti, Telenot, Hetronic, Thaler, Kongskilde: überall "kein Treffer -> CRM-Status: neu". Kein CRM-Konzernbezug, kein E5.
Patente (F5): Google Patents, Espacenet, DEPATISnet nicht direkt abfragbar. Eigene Patent-Websuche nur für Mammut (1) und Maxwald (1 Patent-/Funk-Suche); beide ohne zuordenbaren Anmelder. Für die übrigen acht keine eigene Patentsuche (Händler/Verband/Saatgut/Futter). Feld 9 ist damit bei ALLEN 10 Firmen ohne Datenbankabfrage: nach F5 UNVOLLSTÄNDIG, Nachholen im Browser nötig. "Keine Treffer" ist kein Gegenbeweis. Wettbewerbereinsatz (F6): Grep auf wettbewerber_referenzen.md von Tom übernommen, nicht wiederholt (Toms Ergebnis: kein Eintrag). Messe-Signal (E1-Namen unter den Ausstellern): von Tom übernommen (kein Treffer), ohne Einfluss auf die Ampel.

---

## 1. Mammut Maschinenbau GmbH | Halle 19 Stand 50
**ohne Browser geprüft, vorläufig. Ampel: GRÜN (schwach), Tabellenzeile 4 (Sitzregel).** Kein E-Ausschluss (Hersteller von Silage-/Fütterungstechnik und Betonmischern, keine Dosier-/Vergussanlagen, also kein E1). Industrie-/Maschinenbauer mit eigenen Produkten und erkennbarem Standort Gurten, kein Konzern, kein Auslagerungshinweis: Fertigung Stufe A genügt nach Sitzregel. Verguss Mittel (A): Wiegeelektronik PROFI MIX, Akku/Antriebsregler PM 2.5 SF, Magnetventile/Steuerungen.
- Eigene Prüfung (S): mammut.at-Firmenseite im Snippet: "In our plant in Gurten (Upper Austria), silage technology, animal feeding technology and concrete mixers are all produced and completed on a daily basis" (Wortlaut laut Suchmaschine, stützt Tom). PROFI-MIX-Broschüre: elektronisches Wiegesystem als Option (S). Patent-Websuche (Mammut Maschinenbau, Gurten, Anmelder): kein zuordenbares Patent, Datenbanken nicht abgefragt. Stellenanzeige Gurten (Elektriker/Montage): keine gefunden (kein Gegenbeleg, kein Beleg). Firmenbuch nicht selbst gelesen.
- Korrekturen an Toms Feldern: keine. Hinweis: Wiegeelektronik ist laut Broschüre eine Option, nicht in jedem Gerät; Verguss bleibt Mittel (A) nach Bauteil-Regel, Akku/Regler als stärkstes Bauteil.
- Nachrecherche-Auftrag: keiner nötig für Grün; zur Absicherung (Jey-Stichprobe): Zitat "Werk in Gurten" im Browser auf mammut.at/en/company/ bestätigen (V) und Impressum/Firmenbuch (FN) lesen; Datenblatt PM 2.5 SF: Akku/BMS/Regler selbst gebaut oder zugekauft.
- Nicht verwendbare Aussagen: Fertigung Gurten (A/S); Verguss Mittel (A); Firmenbuch (S); Patentlage. Stichprobe für Jey: ja (Grün ohne V).

## 2. MAS Seeds | Halle 23 Stand 305
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Messename ohne Rechtsform; ausstellende Einheit unklar (MAS-Austria GmbH Wien, MAS Seeds Deutschland, Maïsadour-Gruppe FR). Produkt Saatgut: Verguss Niedrig (A, alle Bauteile), kein Demak-Bezug, kein Gerätefertiger. Kein harter Ausschluss im Wortlaut von E1-E4 belegt, daher nicht Rot. CRM: neu (MAS Seeds, MAS-Austria, Maisadour).
- Korrekturen: keine. Eigene Websuche nicht ausgeführt (Tom: Sitzregel/Segment eindeutig).
- Nachrecherche-Auftrag (Gelb, Zeile 2, niedrige Priorität): Welche Gesellschaft stellt aus (Firmenbuch MAS-Austria GmbH, FN 680567 i)? Praktisch irrelevant, da Saatgut ohne Verguss-Bezug; Empfehlung an Jey: aus der Liste streichen. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle (S/A). Stichprobe für Jey: nein.

## 3. Maschinen Mauritz GmbH | Halle 18 Stand 520
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7, Rot-Kandidat E2).** Händlerprofil (landwirt.com, S): Thaler-Hoflader, Forst-/Holzgeräte, Teleskoplader; keine Fertigung belegt. E2 verlangt Beleg V, daher nicht Rot. CRM: neu (Maschinen Mauritz, Mauritz).
- Korrekturen: keine. Keine eigene Websuche (Händler: CRM + Einordnung).
- Nachrecherche-Auftrag (Gelb, Zeile 7): Hat die Firma Eigenfertigung/Aufbauten? maschinen-mauritz.at (Impressum, Sortiment) im Browser lesen; Firmenbuch (GmbH/GesmbH). Ohne Eigenfertigung: Rot nach E2. Empfehlung: nur auf Wunsch von Jey.
- Nicht verwendbare Aussagen: alle. Stichprobe für Jey: nein.

## 4. Maschinenhandel Zauner | Halle 18 Stand 510
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7, Rot-Kandidat E2).** Händler Forst-/Holzbearbeitung, Berndorf (S). Rechtsform offen. CRM: neu (Maschinenhandel Zauner, Zauner).
- Korrekturen: keine. Keine eigene Websuche.
- Nachrecherche-Auftrag (Gelb, Zeile 7): mhzauner.at Impressum/Sortiment im Browser: Eigenaufbauten oder Fertigung? Ohne: Rot nach E2.
- Nicht verwendbare Aussagen: alle. Stichprobe für Jey: nein.

## 5. Maschinenring Österreich Happy am Hof | Halle 21 Stand 1320
**Ampel: ROT (Tabellenzeile 1, E2 analog: Verband/Genossenschaft, Entscheidung Jey "Verbände raus").** Bedingung: Dienstleistungs-/Selbsthilfeorganisation (reg. Gen. m.b.H., Rechtsform nur aus URL-Pfad, S) und Mehrträger-Präventionsinitiative; keine Produktion. Quelle der Entscheidung: Jeys Vorgabe, nicht ein V-Beleg; Quellen Tom: topagrar-Artikel (S). Fehlender Fertigungsbeleg allein wäre nicht Rot, hier trägt die Organisationsform/Jey-Entscheidung. CRM: neu (Maschinenring, Happy am Hof).
- Korrekturen: keine. Kein Nachrecherche-Auftrag (Rot).
- Nicht verwendbare Aussagen: Rechtsform (S). Stichprobe für Jey: nein.

## 6. Mauch Ges.m.b.H & Co.KG | Halle 21 Stand C60
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7, Rot-Kandidat E2).** Familienbetrieb seit 1962, Generalimporteur Weidemann/Merlo, Burgkirchen (S). Unklar, ob die unter "Mauch" inserierten Anbaugeräte (Mulcher, Schneefräse) Eigenprodukte sind. Verguss für die Gesellschaft Niedrig (A); bei Eigenprodukten mechanisch, ebenfalls Niedrig. CRM: neu (beide Schreibweisen; Weidemann, Merlo kein Treffer, kein Konzernbezug).
- Korrekturen: keine. Keine eigene Websuche.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Wer fertigt die Anbaugeräte "Mauch" (Mulcher, Schneefräse)? Firmenseite/Impressum und Produktdatenblätter im Browser; Firmenbuch. Falls Eigenfertigung: Verguss trotzdem Niedrig (mechanisch), dann Gelb Zeile 6; falls reiner Importeur: Rot E2.
- Nicht verwendbare Aussagen: alle. Stichprobe für Jey: ja (Herkunft der Anbaugeräte offen).

## 7. MAVUM Vertrieb und Marketing GmbH | Halle 23 Stand 480
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt; Rot-Kandidat E2).** Sitz, Adresse, Firmenbuch nicht ermittelt; nur Kleinanzeigenprofil (Pedrotti-Trockner, Vertrieb). Name "Vertrieb und Marketing" spricht für Vertriebsgesellschaft. CRM: neu (MAVUM, Pedrotti kein Treffer).
- Korrekturen: keine; Toms Suche war durch das Limit unvollständig, von mir nicht nachgeholt.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Sitz und Firmenbuchnummer von MAVUM (evi.gv.at, mavum.at/Impressum, Messeprofil agraria.at) im Browser klären; Eigenfertigung ja/nein. Ohne Fertigung: Rot E2.
- Nicht verwendbare Aussagen: alle. Stichprobe für Jey: nein.

## 8. Maxwald Maschinen GmbH | Halle 20 Stand A20
**ohne Browser geprüft, vorläufig. Ampel: GRÜN (schwach), Tabellenzeile 4 (Sitzregel).** Kein E-Ausschluss (Seilwindenhersteller, keine Dosier-/Vergussanlagen). Familienunternehmen mit erkennbarem Standort Ohlsdorf, eigene Produkte, kein Konzern: Fertigung Stufe A nach Sitzregel. Verguss Mittel (A): Funkfernsteuerung/Empfänger, Magnetventile/Spulen, Sensorik, Kabelbaum/Stecker.
- Eigene Prüfung (S): Firmenbuch-Snippet evi.gv.at/f/105753w: "Maxwald-Maschinen, Gesellschaft m.b.H.", FN 105753 w, Sitz Ohlsdorf, Irresbergstraße 1, 4694 Ohlsdorf, eingetragen 30.06.1994 (Identität damit stimmig). Verzeichnis (salzkammergut.at/Herold, S): "Hauptgeschäft ist die Herstellung von Seilwinden", internationaler Vertrieb. Händlerinserate (S): Funkanlage Telenot an Maxwald-Winde, Zukauffunk (Bestätigung der Zukaufelektronik, Tom stimmt). Patent-Websuche: kein Patent mit Anmelder Maxwald zuordenbar; nur EP2336074 (Nachrüstsatz mechanische Winde auf elektrohydraulisch/Funk), Anmelder im Snippet nicht genannt, nicht zugeordnet.
- Korrekturen an Toms Feldern: Feld 17: Firmenbuch nennt FN 105753 w, eingetragen 1994 (Herold nennt Gründung 1979 und Vorgänger-KG FN 26173 s: Rechtsnachfolge weiter ungeklärt, aber ohne Folge für die Ampel). Sonst bestätigt.
- Nachrecherche-Auftrag: keiner nötig für Grün; zur Absicherung (Jey-Stichprobe): maxwald.eu Impressum und "Über uns" im Browser (Fertigung Ohlsdorf V), Datenblatt Funkseilwinde (Elektronik, Ventilblock), EP2336074 in Espacenet: Anmelder prüfen.
- Nicht verwendbare Aussagen: Fertigung Ohlsdorf (A/S); Verguss Mittel (A); Funk-Zukauf Telenot/Hetronic (S, nur Inserate); Patent. Stichprobe für Jey: ja (Grün ohne V).

## 9. Medl GmbH | Halle 22 Stand C40
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7, Rot-Kandidat E2).** Selbstbeschreibung "Landtechnik Großhandel", Marbach an der Donau, Firmenbuch-Snippet bestätigt Sitz (S). Medl-gelabelte Produkte (Bronty, Pflanzenschutzspritzen, Stockputzer): Hersteller offen. CRM: neu (Medl, Medl GmbH; Marken Kongskilde u. a. ohne Treffer).
- Korrekturen: keine. Keine eigene Websuche.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Fertigt Medl die Medl-Marken selbst (Bronty, Pflanzenschutzspritzen)? Impressum/Produktseiten medl.at im Browser, Stellenanzeigen Marbach (Montage/Elektrik). Bei Eigenfertigung Spritzensteuerung: Verguss Mittel, dann Grün erwartbar; sonst Rot E2.
- Nicht verwendbare Aussagen: alle zu Fertigung und Verguss. Stichprobe für Jey: ja (einziger Händler mit offener Eigenmarken-Frage).

## 10. Milkivit & Milkiwean | Halle 23 Stand 190
**ohne Browser geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Zwei Marken, keine Firma; Hersteller laut Etiketten Trouw Nutrition Deutschland GmbH, Burgheim (S), Konzern Nutreco. Produkt Futtermittel: Verguss Niedrig (A). Kein Demak-Bezug. CRM: neu (Milkivit, Milkiwean, Trouw Nutrition, Nutreco), kein Konzernbezug.
- Korrekturen: keine. Keine eigene Websuche.
- Nachrecherche-Auftrag (Gelb, Zeile 2, niedrige Priorität): Ausstellende Gesellschaft klären (AT-Vertretung oder Trouw Nutrition). Empfehlung an Jey: streichen (Futtermittel ohne Vergussbauteile).
- Nicht verwendbare Aussagen: alle. Stichprobe für Jey: nein.

---

## Einschränkungen
- Kein Browser, WebFetch nicht eingesetzt: keine Stufe V, alle Ampeln vorläufig, Zitate nirgends im Browser bestätigt.
- Eigene WebSearch nur 4 Abfragen (je 2 für Mammut und Maxwald: Patent/Produkt, Stellen bzw. Firmenbuch). Stellensuche Mammut ergab keine Treffer (kein Gegenbeleg). Für Nr. 2 bis 7, 9, 10 keine eigene Websuche, nur CRM-Skript und Einordnung nach Toms Quellen.
- Patentrecherche (F5) bei allen Firmen ohne Datenbankabfrage: UNVOLLSTÄNDIG; EP2336074 Anmelder offen. F6 (Wettbewerber) nicht von mir wiederholt.
- Zwei Grün-Einstufungen beruhen auf Sitzregel (Stufe A) und Bauteil-Regel (A): vor einer Mail Fertigung und Elektronik im Browser mit V belegen.
- Nr. 5 Rot stützt sich auf Jeys Entscheidung, nicht auf einen V-Beleg.
- Kontaktdaten nicht geprüft (Regel K). Kein git commit, keine Datenbankfelder geändert.
