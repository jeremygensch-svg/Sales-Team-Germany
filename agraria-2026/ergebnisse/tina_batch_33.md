# Tina Batch 33 - agraria 2026 (Prüfung von tom_batch_33.md)
Erstellt: 2026-11-26 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_33.md (8 Firmen, Nr. 1 bis 8; Agrarmesse Wels 25.-28.11.2026).
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (2 Abfragen, Snippets/Kurzfassungen) und Bash zur Verfügung; WebFetch und Chrome nicht nutzbar. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Nichts ist mailtauglich.
Skripte: `python3 crm_abgleich.py` für alle 8 Firmen samt Konzern-/Alt-/Schwestern-/Kurznamen selbst wiederholt. Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum aller Einträge: 2026-11-26.
Jey-Entscheidungen angewandt: Verbände/Verlag/Versicherung/Vermittler (Prüfdienstleister, Forschung, Saatgut, Medien) raus; CRM-gleicher/sehr ähnlicher Name raus; Anlagenbauer bleiben drin, außer sie bauen selbst Verguss-/Dosieranlagen (E1).

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | Wölfleder GmbH (Halle 23 Stand 10) | GELB | 2 (Identität; Zeile 3 Konzern/CRM-Name offen) | ja |
| 2 | Yokohama TWS Austria GmbH Mitas Tires (Halle 18 Stand 290) | GELB | 7 (Rot-Kandidat E2/E3) | ja |
| 3 | Zuchtverband Stadl-Paura (Halle 24 Stand 20) | ROT (vorläufig) | Jey-Entscheidung Verband (Nähe Zeile 1) | nein |
| 4 | Ökoprofi (Halle 18 Stand 540) | GELB | 7 (Rot-Kandidat E2) | ja |
| 5 | Österreichische BauernZeitung (Halle 22 Stand 1100) | ROT (vorläufig) | Jey-Entscheidung Medien (E2-nah) | nein |
| 6 | Österreichische Hagelversicherung (Halle 21 Stand 1380) | ROT (vorläufig) | Jey-Entscheidung Versicherung | nein |
| 7 | Österreichische Jungzüchtervereinigung (ÖJV) (Halle 24 Stand 10) | GELB | 2 (Identität nicht belegt; erwartet Rot nach Jey-Entscheidung Verband) | nein |
| 8 | Österreichische Rinderbörse GmbH (Halle 24 Stand 10) | ROT (vorläufig) | Jey-Entscheidung Vermittler (E2) | nein |

Zahlen: Grün 0, Gelb 3 (Nr. 1, 2, 4) plus 1 formales Gelb (Nr. 7), Rot 4 (Nr. 3, 5, 6, 8), alle vorläufig.
Hinweis zu Rot: Tabellenzeile 1 verlangt Stufe V für E1-E4. Verbände, Verlag, Versicherung und Vermittler sind in Abschnitt E nicht wörtlich genannt; das Rot stützt sich auf Jeys ausdrückliche Entscheidung (Kategorie-Ausschluss) und die Kategorie aus Firmenbuch-/Impressum-Snippets (S). Falls Jey ein Rot nur bei V-Beleg will: diese vier wären Gelb, Auftrag "Impressum/Firmenbuch lesen", Ergebnis erwartbar Rot.

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet, DEPATISnet nicht abfragbar; ich habe keine eigene Patentsuche wiederholt. Toms Feld 9 besteht nur aus WebSearch-Abfragen ohne Datenbank und ist damit nach F5 UNVOLLSTÄNDIG bei allen 8 Firmen. Bei den vier Rot-Firmen ohne Fertigung ohne Auswirkung auf die Ampel, bei Nr. 1, 2, 4 nachzuholen, falls sie weiterverfolgt werden.
Wettbewerbereinsatz (F6): Grep auf wettbewerber_referenzen.md mit Wölfle, Yokohama, Mitas, Trelleborg, Ökoprofi, Oekoprofi, Hagel, Bauernzeitung, Rinderb: kein Treffer. Keine Einzelsuchen mit Wettbewerbernamen von mir. "Kein Hinweis" ist kein Gegenbeweis.
Messe-Signal (N2): kein Abgleich gegen Ausstellerlisten der Wettbewerber gefahren (wie Tom); unter den 8 Firmen keine Wettbewerber erkennbar.

---

## 1. Wölfleder GmbH | Halle 23 Stand 10
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt; zusätzlich Zeile 3 offen).**
- CRM selbst wiederholt: `crm_abgleich.py "Wölfleder" "Wölfle" "Woelfleder" "Wölfle GmbH"`: Kern-Name "woelfleder" hat Präfix-Treffer bekannte_firmen_DE-AT-NL.txt Zeile 2616 "Wölfle GmbH [DE]" (Kern "woelfle", Schlusszeile identisch bei der Suche nach "Wölfle"); kundendatenbank_export.txt: kein Treffer.
- Prüfung "wirklich sehr ähnlich?": Formal erfüllt der Treffer die Präfixregel (B2: Präfix >= 5 Zeichen). Inhaltlich halte ich ihn NICHT für eine Kurzform: "Wölfle" (schwäbischer Familienname) ist kein gekürzter Name von "Wölfleder" (oberösterreichischer Familienname, Endung -eder), die Firma liegt in anderem Land (AT laut Messeliste vs. [DE]). Es sind nach Augenschein zwei verschiedene Namen. Ob sie verwandt/dieselbe Gruppe sind, ist unbelegt; zu Wölfle GmbH [DE] habe ich keine Branche geprüft (offen). Meine Empfehlung: nicht automatisch "raus per Namensähnlichkeit", sondern Jey entscheiden lassen (Stichprobe).
- Eigene Suche (1 WebSearch, "Wölfleder GmbH Stalltechnik Impressum Sitz"): kein Treffer zur Firma, nur fremde Impressen. Tom fand ebenfalls nichts außer Gebrauchtinseraten. Identität bleibt unbelegt (Rechtsform/Land nur aus der Messeliste, S); Fertigungsort unbekannt. Eine weitere Suche (Wölfleder Landtechnik Oberösterreich, Firmenbuch) habe ich nicht gemacht.
- Einordnung: Stalltechnik/Entmistung (Schrapper, Klappschieber, Aufstallung), Anlagenbauer-Regel: baut keine Verguss-/Dosieranlagen, E1 nicht einschlägig (A). Verguss Niedrig bis Mittel (A; nur Antriebs-/Torsteuerungen, evtl. zugekauft). Fertigung AT: Mittel, Stufe ?. Zeile 4 nicht erfüllbar ohne Fertigungs- und Identitätsbeleg.
- Korrekturen an Toms Feldern: Feld 11 leer von mir gefüllt; Feld 12: nicht "unklar/BEKANNT-ähnlich", sondern "unklar (Präfixtreffer, Namen verschieden)". Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Gibt es eine Wölfleder GmbH (Sitz, FN, Impressum) und wo werden Produkte gefertigt? Wo: Firmenbuch/evi.gv.at, WKO-Firmenverzeichnis, Messeprofil Agraria, Firmenwebsite. (b) Besteht ein Bezug zur Wölfle GmbH [DE] (CRM Zeile 2616)? Wo: Impressum beider Firmen, Handelsregister, Branche der CRM-Firma. (c) Elektronik (Tor-/Entmistungssteuerung) selbst gebaut oder zugekauft? Datenblatt/Produktseite. Aktion: nicht kontaktieren, bis (a) und (b) geklärt; Jey entscheidet zur Namensähnlichkeit.
- Nicht verwendbare Aussagen: Gebiet/Land AT (S); Fertigung (?); Verguss (A); Produkte (S, Messeliste); Antriebe vergossen (A). Stichprobe für Jey: ja (Namensähnlichkeit, Identität).

## 2. Yokohama TWS Austria GmbH Mitas Tires | Halle 18 Stand 290
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2/E3).**
- CRM selbst wiederholt: "Yokohama TWS Austria", "Mitas Tires", "Yokohama", "Mitas", "Trelleborg", "TWS": kein Treffer, neu; kein Konzernbezug (Zeile 3 greift nicht).
- Eigene Suche (1 WebSearch): Firmenbuch-Snippet bestätigt Yokohama TWS Austria GmbH, Am Teich 1, 4300 St. Valentin (evi.gv.at/f/250690m, S), Alleingesellschafterin Yokohama TWS Holding AB (S). Mitas-Seite nennt Werke in Tschechien, Serbien, USA; St. Valentin nicht als Werk (S). Es gibt außerdem die Schwester Yokohama TWS Germany GmbH (Agritechnica-Ausstellerseite, S), nicht im CRM, nicht geprüft. Toms Identitätsangabe (Name, FN, Sitz) bestätigt, Toms Hinweis zu Yokohama TWS Czech Republic a.s. nicht nachgeprüft.
- Einordnung: Konzern mit mehreren Werken (Sitzregel greift nicht, V nötig); AT-GmbH laut Snippets Vertrieb; Reifen/Räder: Verguss Niedrig (A). Zeile 5/6 nicht anwendbar (Fertigung AT nicht belegt), daher Zeile 7. Rot nach E2/E3 erst mit V-Beleg (Vertrieb ohne Fertigung bzw. Fertigung nur im Ausland).
- Korrekturen: keine. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Hat die Yokohama TWS Austria GmbH Fertigung/Montage in St. Valentin (z. B. Rad-/Reifenmontage, Stellenanzeigen) oder ist sie reine Vertriebsgesellschaft? Wo: Impressum mitas-tires.com/de-at, Firmenbuch-Auszug (Geschäftszweig), Karriereseite. Bei V-Beleg Vertrieb ohne Fertigung: Rot nach E2 mit URL. Aktion: nicht kontaktieren, niedrige Priorität.
- Nicht verwendbare Aussagen: Rolle Vertrieb (S); Werke CZ/RS/US (S); Verguss Niedrig (A); Patentlage. Stichprobe für Jey: ja (Rot-Bestätigung per V).

## 3. Zuchtverband Stadl-Paura | Halle 24 Stand 20
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT (Jey-Entscheidung: Verbände raus; Zeile 1 nur mit der Einschränkung oben, Beleg nur S).**
Rot, weil: Pferdezuchtverband, keine Fertigung (LK-OÖ-Seite https://ooe.lko.at/zuchtverband-stadl-paura-alles-rund-ums-pferd+2400+4125728, S). CRM: kein Treffer, neu (selbst wiederholt). Keine eigene Websuche.
- Korrekturen: keine; Toms Hinweis (Pferd statt Rind) bleibt. Zitat im Browser bestätigt: nein.
- Nicht verwendbare Aussagen: Rechtsform Verein (?), Fertigung Niedrig (S). Stichprobe für Jey: nein.

## 4. Ökoprofi | Halle 18 Stand 540
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7; Rot-Kandidat E2).**
- CRM "Ökoprofi", "Oekoprofi", "Oeko Profi": kein Treffer, neu. Keine eigene Websuche; Toms Sitz Oberharrern 33, 4691 Schlatt und Rechtsform "Landmaschinenhandelsges.m.b.H." (WKO-Snippet, S) nicht gegengelesen.
- Einordnung: Händler für Ersatzteile/Zubehör; Eigenfertigung nicht belegt. E2 verlangt aber V (Impressum/Firmenbuch/Selbstbeschreibung). Verguss: nur zugekaufte Elektrozaungeräte/Lenksysteme (Mittel/Niedrig, A). Weil Händler ohne Fertigung nur S, nicht Rot.
- Korrekturen: Tom setzt "Kein Auftrag nötig" bei Gelb-Kandidat nicht um; Auftrag ergänzt. Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb, Zeile 7): Ist Ökoprofi reiner Handel oder gibt es Eigenfertigung/Montage (z. B. Eigenmarken, Elektrozaun)? Wo: Impressum und Über-uns auf oekoprofi.com, Firmenbuch/WKO-Eintrag (Gewerbe). Bei reinem Handel (V): Rot nach E2. Aktion: nicht kontaktieren, niedrige Priorität.
- Nicht verwendbare Aussagen: Händlerstatus (S), Verguss (A), Adresse (S). Stichprobe für Jey: ja (Händler/Eigenmarke offen).

## 5. Österreichische BauernZeitung | Halle 22 Stand 1100
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT (Jey-Entscheidung: Medien raus; E2-nah, nur S).**
Rot, weil: Wochenzeitung/Verlag, Medieninhaber Agrar Media Verlagsgesellschaft mbH, Wien (Impressum-PDF https://bauernzeitung.at/wp-content/uploads/2024/10/2024-10-31_Salzburg.pdf, S). CRM selbst wiederholt inkl. "Agrar Media": kein Treffer (Toms Lücke "nicht gesondert abgeglichen" damit geschlossen). Toms Widerspruch (Preislisten-Snippet nennt Raiffeisenlandesbank NÖ-Wien) bleibt offen, ohne Einfluss auf die Kategorie.
- Nicht verwendbare Aussagen: alle (S). Zitat im Browser bestätigt: nein. Stichprobe für Jey: nein.

## 6. Österreichische Hagelversicherung | Halle 21 Stand 1380
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT (Jey-Entscheidung: Versicherung raus, nur S).**
Rot, weil: Versicherungsverein auf Gegenseitigkeit, Wien, FN 106532s (https://www.evi.gv.at/f/106532s, S), keine Fertigung. CRM ("Österreichische Hagelversicherung", "Hagelversicherung"): kein Treffer. Zitat im Browser bestätigt: nein. Nicht verwendbare Aussagen: alle (S). Stichprobe für Jey: nein.

## 7. Österreichische Jungzüchtervereinigung (ÖJV) | Halle 24 Stand 10
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt; erwartet Rot nach Jey-Entscheidung Verband).**
- CRM ("Österreichische Jungzüchtervereinigung", "ÖJV", "Jungzüchter"): kein Treffer. Keine eigene Websuche; Tom fand keine Seite, Name nur aus der Messeliste (S).
- Kategorie "Vereinigung für Rinderzucht-Nachwuchs" ist nur Messelistentext (S). Nach Tabelle geht Zeile 2 vor; bei Bestätigung als Verband greift Jeys Entscheidung (Rot).
- Nachrecherche-Auftrag (Gelb, Zeile 2): Existiert die ÖJV als Verein (ZVR-Nummer, Sitz) und fertigt nichts? Wo: ZVR-Auskunft/Vereinsregister, Website des Rinderzuchtverbands (zuchtdata/rinderzucht.at), Agraria-Ausstellerprofil. Aktion: nicht aufnehmen; kein weiterer Aufwand nötig, falls Jey das formale Gelb als Rot werten will.
- Nicht verwendbare Aussagen: alle (S/?). Stichprobe für Jey: nein.

## 8. Österreichische Rinderbörse GmbH | Halle 24 Stand 10
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: ROT (Jey-Entscheidung Vermittler/E2, nur S).**
Rot, weil: Geschäftszweig Schlachtrindvermittlung, GmbH Linz, FN 154584f (https://www.evi.gv.at/f/154584f, S), keine Fertigung. CRM ("Österreichische Rinderbörse", "Rinderbörse"): kein Treffer. Zitat im Browser bestätigt: nein. Nicht verwendbare Aussagen: alle (S). Stichprobe für Jey: nein.

---

## Konsistenz und Auffälligkeiten
- Toms Stufen durchgehend korrekt niedrig (keine V-Aussage vorgetäuscht). Tom setzt die Ampel-Felder bewusst leer; Aufträge fehlten bei Nr. 2 und 4 (Kandidaten Rot nur mit V), von mir ergänzt.
- Toms Patentfeld bei den Verband-/Verlags-Firmen ist teils eine geteilte Sammelabfrage (Nr. 5, 6, 8 dieselbe Suche): sachlich ohne Folgen, formal keine firmenspezifischen zwei Suchen.
- Namensähnlichkeit Wölfleder/Wölfle: Skript meldet Präfix, nach Augenschein verschiedene Namen; Entscheidung bei Jey.
- Vorschlag Fehlerlog (nicht eingetragen): Präfix-Regel B2 präzisieren ("Kurzform derselben Wortwurzel"), da Familiennamen wie Wölfle/Wölfleder sonst Fehlalarme erzeugen.

## Einschränkungen
- Browser und WebFetch nicht verfügbar: kein Gegenlesen nach Abschnitt H, keine Impressen/Register gelesen; alle Aussagen Stufe S, A oder ?. Keine Stufe V, alle Ampeln vorläufig.
- Eigene WebSearch nur 2 Abfragen (Wölfleder, Yokohama TWS Austria). Für die übrigen 6 Firmen keine eigene Websuche, nur CRM-Abgleich und Einordnung nach Toms Angaben.
- Nicht durchgeführt: Patentrecherche (Google Patents, Espacenet, DEPATISnet) für alle Firmen; Wettbewerber-Einzelsuchen (nur Listen-Grep); Messe-Signal-Abgleich; Recherche zur Wölfle GmbH [DE] und zu Yokohama TWS Germany GmbH; Firmenbuch/ZVR-Abrufe.
- Kundendatenbank (Excel) nicht lesbar; Abgleich per Skript auf Textexporte. Keine "Verifiziert am"-Prüfung nötig (kein CRM-Treffer mit Datum).
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
