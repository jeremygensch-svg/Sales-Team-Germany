# Tina Batch 12 - agraria 2026 (Prüfung von tom_batch_12.md)
Erstellt: 2026-11-25 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_12.md (10 Firmen, Nr. 111 bis 120, Messe agraria Wels 2026, Länder DE/AT/NL; laut Messeliste alle AT). Halle/Stand stehen unverändert aus Toms Datei.
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (8 Abfragen, Kurzfassungen/Snippets) und Bash zur Verfügung; Chrome nicht verfügbar, WebFetch nicht genutzt. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün vergeben, nichts mailtauglich.
Skripte: `python3 crm_abgleich.py` für alle Firmen samt Konzern-/Alt-/Schwester-/Schreibvarianten selbst wiederholt (Varianten je Block). Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum aller Einträge: 2026-11-25.
Entscheidungen von Jey, angewandt: Verbände/Prüfdienstleister/Forschung raus (im Batch keiner); Firmen im CRM mit gleichem/sehr ähnlichem Namen raus (im Batch keiner: alle zehn kein Treffer); Anlagenbauer bleiben drin, außer sie bauen selbst Verguss-/Dosieranlagen (E1; im Batch kein Anlagenbauer und kein E1-Fall erkennbar). Ein harter Ausschluss ergibt nur mit Stufe V Rot (Zeile 1); da keine V-Quelle existiert, stehen Saatgut/Verlag/Händler/Dünger als Gelb mit Vermerk "Rot-Kandidat E2" und Empfehlung "aussortieren" (wie Smart Systems Hub in Batch 52). Jey bestätigt das Aussortieren.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 111 | DIE SAAT (Halle 20, Stand F20) | GELB (Rot-Kandidat E2) | 2 | nein |
| 112 | diebauern.app GmbH (Halle 17, Stand 110) | GELB (Rot-Kandidat E2) | 2 | nein |
| 113 | DILA Fenstersanierung (Halle 17, Stand 260) | GELB | 6 | nein |
| 114 | DKW GmbH (Freigelände, Stand 20) | GELB | 2 | ja |
| 115 | Donut (Halle 20, Stand 1120) | GELB (Rot-Kandidat E2) | 2 | nein |
| 116 | Edtmayer Türen & Tore (Halle 24, Stand 75) | GELB | 2 | ja |
| 117 | Einböck GmbH (Halle 21, Stand C20) | GELB (grünnah) | 5 | ja |
| 118 | ENdorado GmbH (Halle 17, Stand 20) | GELB | 5 | ja |
| 119 | ERBER AGRO GMBH (Halle 19, Stand 220) | GELB (Rot-Kandidat E2) | 2 | nein |
| 120 | Ertl-Auer e.U. (Halle 22, Stand B40) | GELB (Rot-Kandidat E2) | 2 | nein |

Zahlen: Grün 0, Gelb 10, Rot 0. Aussichtsreichste Firmen für die Nachrecherche: Nr. 117 Einböck (zuerst), Nr. 116 Edtmayer, Nr. 118 ENdorado.

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Eigene Patent-Websuche per WebSearch für die aussichtsreichsten Firmen: Einböck (1 Abfrage: kein Patentdatensatz im Index) und ENdorado (1 Abfrage: DPMA-Patentblätter 2025/2026 im Index ohne ENdorado als Anmelder; die behauptete Patentnummer bleibt unbekannt). Edtmayer: keine eigene Patentabfrage (nur Registersuche). Für die übrigen sieben Firmen keine eigene Patentsuche (Händler/Verlag/Saatgut/Dünger/Nicht-Identifizierbare, Priorisierung wegen Sitzungslimit). Toms Suchen werden weder übernommen noch widerlegt. Feld 9 ist damit bei ALLEN 10 Firmen ohne Datenbankabfrage: nach F5 UNVOLLSTÄNDIG, Nachholen im Browser (Google Patents, Espacenet, DEPATISnet, ggf. Österreichisches Patentamt) nötig; Toms Batch ist laut seiner Einschränkung ebenfalls unvollständig. "Keine Treffer" ist kein Gegenbeweis; Rechtsstand nirgends geprüft.
Wettbewerbereinsatz (F6): Grep auf wettbewerber_referenzen.md (mit Wortgrenzen und als Teilzeichenfolge) mit Einböck, Einboeck, Edtmayer, ENdorado, DILA, DKW, Ertl, RWA, Erber, Donut, diebauern, Die Saat: kein Firmenbezug (reine Teilzeichenfolgen in Fremdwörtern). Einzelsuchen mit Wettbewerbernamen von mir nur zu Einböck (Elektronik/Zulieferer, kein Hinweis). Messe-Signal (Aussteller aus E1 auf der agraria): nicht geprüft, offen.
Nicht durchgeführt: Browser-Gegenlesen jeder Quelle, Impressen, Registerabfragen im Original, Google Patents/Espacenet/DEPATISnet, Stellenanzeigen auf Firmenseiten, Messekatalog agraria.at.

---

## 111. DIE SAAT | Halle 20, Stand F20
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt; Rot-Kandidat E2/Saatgut, kein Fertiger).** Zeile 1 nicht anwendbar (kein V-Beleg für Ausschluss). Zeile 2 trifft: Name ohne Rechtsform, Sitz und Register nicht gefunden, Zuordnung zu RWA nur aus einer Ertragstabelle (S).
- Eigene Prüfung: CRM-Skript "DIE SAAT", "Die Saat", "RWA", "Raiffeisen Ware Austria": kein Treffer, neu. Wettbewerber-Grep: kein Eintrag. Keine eigene Websuche (Saatgutanbieter, Verguss Niedrig A nach Wissensbasis Block C, kein Elektronikprodukt).
- Korrekturen an Toms Feldern: keine. Toms Einordnung "kein Fertiger" nachvollziehbar.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer ist der Rechtsträger von "DIE SAAT" (RWA/Saatbau/anderer)? Wo: Messekatalog agraria.at (Ausstellerprofil), Firmenbuch/Impressum der Marke, danach CRM-Konzernabgleich wiederholen. Empfehlung: aussortieren, kein Auftrag nötig, wenn Jey Saatgut ausschließt (E2/E3-nahe, nicht V-belegt).
- Nicht verwendbare Aussagen: alles (Sitz S/?, Produkt S, Verguss A). Stichprobe für Jey: nein. Verifikation: 2026-11-25.

## 112. diebauern.app GmbH | Halle 17, Stand 110
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Firma nicht auffindbar; Rot-Kandidat E2 Verlag/Software/Dienstleistung).**
- Eigene Prüfung: CRM-Skript "diebauern.app", "Die Bauern", "diebauern.app GmbH": kein Treffer, neu. Messe-Stichwörter (Verlage, Zeitschriften, Vermarktungskonzepte, S) führen zu keiner Hardware; Verguss Niedrig (A, Block C). Keine eigene Websuche.
- Korrekturen: keine. Website-Angabe in Feld 5 ist nur aus dem Namen abgeleitet (?).
- Nachrecherche-Auftrag (Gelb, Zeile 2): Firmenbuchnummer/Sitz und Tätigkeit klären (Messekatalog, Impressum diebauern.app). Empfehlung: aussortieren (E2, wenn Verlag/Plattform bestätigt).
- Nicht verwendbare Aussagen: Sitz, Website, Tätigkeit (S/?). Stichprobe: nein. Verifikation: 2026-11-25.

## 113. DILA Fenstersanierung | Halle 17, Stand 260
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6, Verguss Niedrig bei allen Bauteilen).** Identität wahrscheinlich DILA Sanieren GmbH, Eberschwang (FN 359244a laut Register-Snippet S), nicht durch Impressum belegt; die Messebezeichnung nennt "sonstige Dienstleistungen". Fertigung nach Sitzregel A (Handwerks-/Systembetrieb, ein Standort), Zeile 2 nicht ausgelöst, weil Name und Register zusammenpassen.
- Eigene Prüfung: CRM-Skript "DILA Fenstersanierung", "DILA Sanieren GmbH", "DILA", "ALDURA": kein Treffer, neu. Keine eigene Websuche. Bauteile: Aluminium-Sanierungssysteme (ALDURA), Dichtprofile (zugekauft) Niedrig, Glas-/Profilverklebung Niedrig bis Mittel (Handwerk, keine Serien-Dosierung), Elektronik keine (alle A). Maximum bleibt Niedrig.
- Korrekturen: keine.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Welche Bauteile/Profile stellt DILA selbst her, mit eingeklebten/eingespritzten Dichtungen oder verklebten Profilen in Serie? Wo: Produktseite ALDURA, Impressum DILA Sanieren GmbH. Aktion: nicht kontaktieren; vermutlich uninteressant.
- Nicht verwendbare Aussagen: Fertigungsort (A/S), Verguss (A). Stichprobe: nein. Verifikation: 2026-11-25.

## 114. DKW GmbH | Freigelände, Stand 20
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität und Tätigkeit nicht belegt).**
- Eigene Prüfung (WebSearch "DKW GmbH Eugendorf Photovoltaik Solar", S): Firmenbuch-Snippet (evi.gv.at/f/589032z) bestätigt DKW GmbH, Moosstraße 33, 5301 Eugendorf, eingetragen 21.09.2022; WKO-Eintrag Salzburg gleiche Adresse ohne Branchenangabe. Gesellschafter laut Snippet vier Einheiten (u. a. Holding-GmbHs). Kein Beleg, dass diese Firma Photovoltaik/Solar betreibt; ein ähnlich lokalisierter PV-Installateur (Salzburg PV, Eugendorf) ist eine andere Firma und nicht zugeordnet. CRM-Skript "DKW GmbH", "DKW": kein Treffer, neu.
- Korrekturen an Toms Feldern: Feld 17 bestätigt (Identität nicht belegt), Feld 4 (Eugendorf) bleibt Kandidat. Bauteile (Wechselrichter/Steuerung) Mittel (A), Eigenfertigung nicht belegt; Maximum für die Ampel wegen fehlender Fertigung nicht Hoch.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Ist die ausstellende "DKW GmbH" die Firma aus Eugendorf, und was fertigt sie (Solarsteuerung/Systeme selbst oder Installation)? Wo: Impressum/Website (Domain nicht ermittelt), Messekatalog agraria.at (Ausstellerprofil), Firmenbuch FN 589032z (Geschäftszweig). Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: Zuordnung, Tätigkeit, Fertigung, Verguss (S/A/?). Stichprobe für Jey: ja (Identität völlig offen). Verifikation: 2026-11-25.

## 115. Donut | Halle 20, Stand 1120
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Firma nicht identifizierbar; Rot-Kandidat E2, voraussichtlich Gastronomie/Imbiss, nicht belegt).**
- Eigene Prüfung: CRM-Skript "Donut": kein Treffer, neu. Messeliste ohne Produktangabe; keine eigene Websuche (Name nicht identifizierbar, Treffer wären nicht zuordenbar).
- Korrekturen: keine. Toms Feld 9 bleibt unvollständig (nur eine Suche; Lücke von Tom offen benannt, bei dieser Firma kein Nachholen sinnvoll, solange die Identität fehlt).
- Nachrecherche-Auftrag (Gelb, Zeile 2): Rechtsform, Produkte und Sitz klären. Wo: Messekatalog agraria.at, Eintrag Halle 20 Stand 1120. Empfehlung: aussortieren, wenn dort Gastronomie/kein Fertiger steht.
- Nicht verwendbare Aussagen: alle. Stichprobe: nein. Verifikation: 2026-11-25.

## 116. Edtmayer Türen & Tore | Halle 24, Stand 75
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht sicher zugeordnet).** Andernfalls läge Zeile 4 nahe: Sitzregel (Torbauer, ein Standort, Natternbach) für Fertigung, Verguss Mittel (A, Antriebe/Steuerungen/Endschalter nur falls verbaut, Messe-Stichwort "Antriebe" ist S).
- Eigene Prüfung (WebSearch "Edtmayer Torsysteme GmbH Natternbach", S): Firmenbuch-Snippet evi.gv.at/f/187349p: Gschaid 8, 4723 Natternbach, Geschäftsfeld "Produktion und Vertrieb von Torsystemen" (Toms Zitat lautet "Produktion von Türen und Toren"). Eine zweite Registerseite (evi.gv.at/f/186599k) mit anderer FN nennt "Türen- und Torerzeugung", gleiches Stammkapital und gleiche Geschäftsführerin: zwei Registerauszüge/Einheiten, Zuordnung widersprüchlich. Advantage Austria: Familienunternehmen "Edtmayer GmbH", Natternbach, Tore, Flügeltore, CNC-gefräste Designs für die Landwirtschaft. Ob Messename = eine dieser Einheiten, ist offen. CRM-Skript "Edtmayer Türen & Tore", "Edtmayer Torsysteme GmbH", "Edtmayer", "Edtmayer GmbH": kein Treffer, neu.
- Korrekturen an Toms Feldern: Feld 4/17: zweite Registernummer (186599k) neben FN 187349p ergänzen; Geschäftszweck-Zitat weicht im Wortlaut ab. Fertigung Hoch A bleibt (Sitzregel), Verguss Mittel A bleibt (zugekaufte Teile zählen nach Endprodukt-Regel). Stellenanzeigensuche von mir: keine Anzeige von Edtmayer gefunden (kein Gegenbeleg).
- Nachrecherche-Auftrag (Gelb, Zeile 2): (a) Welche Einheit tritt als "Edtmayer Türen & Tore" auf (Edtmayer Torsysteme-GmbH FN 187349p oder zweite FN 186599k)? Wo: Impressum der Firmenwebsite (Domain nicht ermittelt), Firmenbuch beider FN. (b) Werden Torantriebe/Steuerungen verbaut und selbst oder zugekauft? Wo: Produktseite Antriebe. (c) Fertigung Natternbach V-Beleg (Impressum, Stellenanzeige). Danach Zeile 4 neu prüfen (Grün-Kandidat, schwach).
- Nicht verwendbare Aussagen: Identität, Fertigungsort (A/S), Antriebe, Verguss (A). Stichprobe für Jey: ja. Verifikation: 2026-11-25.

## 117. Einböck GmbH | Halle 21, Stand C20
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Fertigungsbeleg Stufe V fehlt; Sitzregel gilt nicht ohne Weiteres, weil mehrere Werke).** Stärkste Firma im Batch: Identität stimmig (Einböck GmbH, Dorf an der Pram), Fertigung am Sitz laut Fachpresse/Firmenprospekt (S), Verguss Mittel (A). Mit einer V-Quelle zu Fertigung und Elektronik wäre Zeile 4 erreichbar.
- Eigene Prüfung (WebSearch, S): Fachpresse nennt Einböck als Spezialmaschinenhersteller in Dorf an der Pram; ein Prospekt der Einböck-Lohnfertigung (einboeck.at, Snippet) nennt Fertigung "zu 100 % in Dorf an der Pram" und einen neuen "Werk Dobl" (Lackieranlage, Hochregallager, Montage, Versand). Kamerasteuerung Row-Guard/Chopstar: nach einer Fachpresse-Kurzfassung kommt die Kamera ("Culti Cam") von Claas und wird zugekauft (S, nicht im Original gelesen). Zu Elektronik, Eigenentwicklung oder Zukauf von Steuergeräten keine Belege; Stellenanzeigensuche: keine Einböck-Anzeige gefunden. Patent-Websuche: kein Patentdatensatz. CRM-Skript "Einböck GmbH", "Einboeck", "Einböck GmbH & Co KG Metallverarbeitung": kein Treffer, neu (Metallverarbeitung als mögliche Schwestereinheit, nicht als Treffer).
- Korrekturen an Toms Feldern: Feld 4: zusätzlich "Werk Dobl" (Lage nicht belegt) und die Lohnfertigung als Geschäftsfeld (S); damit Mehrwerk-Hinweis, Sitzregel nur eingeschränkt. Feld 6/8: Kamera nach Snippet zugekauft (Claas), Verguss Mittel A bleibt wegen Steuergeräten, Hydraulikventilen/Magnetspulen, Sensoren (alle Zukauf wahrscheinlich; Endprodukt-Regel zählt sie). Feld 15: Produktionsfläche widersprüchlich bleibt.
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Wo liegt Werk Dobl, und wo wird die Maschinenmontage (Elektronik/Kabelbaum der Kamerahacke INVERA/Chopstar) gefertigt? Wo: einboeck.at Impressum/Standortseite/Karriereseite, Stellenanzeigen "Elektriker/Elektroniker/Montage". (b) Baut Einböck Steuergeräte/Kabelkonfektion selbst (Eigenverguss) oder nur Zukauf? Wo: Produktinfoblatt INVERA/Row-Guard (PDF), Stellenanzeigen. (c) Patent-Nachholsuche in Google Patents/Espacenet/DEPATISnet (Anmelder "Einböck", "Einboeck GmbH"). (d) Wettbewerbereinsatz: Referenzseiten von Scheugenpflug/Nordson/Henkel/DELO mit "Einböck" prüfen. Aktion: nicht kontaktieren, Priorität 1 der Nachrecherche.
- Nicht verwendbare Aussagen: Fertigung Dorf an der Pram (S), Werke (S), Kamera Zukauf (S), alle Bauteile (A). Stichprobe für Jey: ja (Entscheidungsfrage: reicht Zeile 4 trotz Mehrwerk-Hinweis, oder erst V?). Verifikation: 2026-11-25.

## 118. ENdorado GmbH | Halle 17, Stand 20
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Fertigung Stufe S, Hersteller vs. Installateur offen).** Identität stimmig (ENdorado GmbH, Wiesenberg 45, 4742 Pram, FN 451225t; ENF-Verzeichnis gleiche Adresse).
- Eigene Prüfung (WebSearch, S): Broschüre 2026 (energiesparmesse.at/.../digitint_EN_Brochure0126.pdf): Gründung 2016 mit Sitz Haag, 2020 neuer Firmensitz Pram, "PV-EnergieDACH" als dachintegriertes System; Module laut Broschüre aus "österreichischer oder deutscher Produktion" (Zukauf von Modulen wahrscheinlich, S); Wechselrichter Fronius (ENF, S). Case Study 2024: 16 Mitarbeiter, Quereinsteiger-Einschulung, keine Stellenanzeige gefunden. Patent: nur die Überschrift "Das Dach mit Patent", keine Nummer; DPMA-Patentblätter 2025/2026 im Index ohne ENdorado. CRM-Skript "ENdorado GmbH", "Endorado", "ENdorado": kein Treffer, neu.
- Korrekturen an Toms Feldern: Feld 9: Patentbehauptung weiterhin ohne Nummer/Status; Toms Hinweis auf LU102428B1 bleibt ungewertet. Feld 6: Module vermutlich Zukauf (Broschüre), eigene Fertigung des Dachsystems unbelegt; Verguss Mittel A bleibt über zugekaufte Anschlussdosen/Wechselrichter/Speicher (Endprodukt-Regel).
- Nachrecherche-Auftrag (Gelb, Zeile 5): (a) Wird das EnergieDACH-System (Profile/Montageelemente) in Pram gefertigt oder nur geplant und montiert? Wo: Produktseite/Impressum endorado.at, Stellenanzeigen Produktion/Montage, Case Study im Volltext. (b) Patent-Nummer, Anmelder und Rechtsstand in Espacenet/DEPATISnet/Österr. Patentamt (Anmelder "ENdorado"). Aktion: nicht kontaktieren; falls nur Installateur, wahrscheinlich Rot-Kandidat E2/E3-nah (nur mit V).
- Nicht verwendbare Aussagen: Fertigung (S), Patent (Behauptung ohne Nr.), Bauteile (A). Stichprobe für Jey: ja. Verifikation: 2026-11-25.

## 119. ERBER AGRO GMBH | Halle 19, Stand 220
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Adresse widersprüchlich; Rot-Kandidat: Düngemittel, kein Fertiger).**
- Eigene Prüfung: CRM-Skript "ERBER AGRO GMBH", "Erber Agro", "ERBER AG", "Erber Group": nur Teilzeichenfolgen-Treffer in Waldmann/WEISSGERBER und in einer Regeltextzeile der Kundendatenbank, kein Namensbezug; Konzernbezug zur ERBER AG im CRM nicht vorhanden. Wettbewerber-Grep: kein Firmenbezug. Verguss Niedrig (A, Düngemittel). Keine eigene Websuche.
- Korrekturen an Toms Feldern: keine. Beziehung zur ERBER AG weiter offen (Konzernabgleich Regel M wäre nur bei Beleg einer Konzernzugehörigkeit nötig; CRM-Treffer fehlen).
- Nachrecherche-Auftrag (Gelb, Zeile 2): Welche Adresse gilt (Gleisdorf, Business Park 6, oder Obergroßau 155) und ist die Firma Teil der ERBER Group? Wo: Firmenbuch, Impressum erber-agro.at, Advantage-Austria-Profil. Empfehlung: aussortieren.
- Nicht verwendbare Aussagen: Sitz, Fertigung, Konzern (S/?). Stichprobe: nein. Verifikation: 2026-11-25.

## 120. Ertl-Auer e.U. | Halle 22, Stand B40
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Rechtsform/Identität widersprüchlich; Rot-Kandidat E2 Landtechnikhändler).**
- Eigene Prüfung: CRM-Skript "Ertl-Auer e.U.", "Ertl-Auer GmbH", "Ertl Auer": kein Treffer, neu. Keine eigene Websuche. Händlerprofil (landwirt.com, S) und Bauteile: Handelsware fremder Hersteller; Verguss Niedrig (A). Messe-Rechtsform e.U. widerspricht dem Register-Snippet (GmbH, laut Tom "gelöscht am 10.04.2026" gegenüber KSV "aktiv", beides S).
- Korrekturen: keine. Registerstatus der GmbH (gelöscht vs. aktiv) ungeklärt.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Welche Rechtsform/Einheit tritt auf (e.U. oder GmbH, gelöscht oder aktiv)? Wo: Firmenbuch FN 114519k, Impressum ertl-auer.at. Empfehlung: aussortieren (Händler ohne Fertigung, E2, erst mit V Rot).
- Nicht verwendbare Aussagen: alle. Stichprobe: nein. Verifikation: 2026-11-25.

## Nicht aufgenommen (bereits bekannt / unklar)
Keine Firma des Batches ist nach meinem Skriptlauf im CRM bekannt. Skript-Treffer für "Erber" (Waldmann, WEISSGERBER, Regeltextzeile der Kundendatenbank) sind Teilzeichenfolgen und kein Namensbezug. Nach Jeys Entscheidung zu weiter ausgesonderten Firmen: Vorschlag aussortieren für 111, 112, 115, 119, 120 (und 113, falls Jey Dichtungsverklebung im Handwerk ausschließt).

## Einschränkungen
- Kein Browser, WebFetch nicht genutzt: keine Stufe V, keine Impressen, keine Zitatbestätigung. Alle Ampeln vorläufig.
- WebSearch ist US-orientiert und liefert Kurzfassungen; 8 Abfragen (Einböck 3, Edtmayer 2 inkl. Stellen, ENdorado 2, DKW 1). Für 111 bis 115, 119 und 120 keine eigene Websuche.
- Patente: keine Datenbankabfrage; Feld 9 bei allen zehn Firmen unvollständig; Nachholen im Browser nötig.
- Messe-Signal (E1-Wettbewerber unter den Ausstellern) nicht geprüft.
- Unklar bleibt, ob Einböck in Dorf an der Pram und Dobl mehrere Werke betreibt (Sitzregel).
