# WoTS 2026 – Tina (Stufe 2) Prüfung Batch 01 – Stand 2026-10-05

Geprüft: wots-2026/tom/tom_batch_01.md gegen wots-2026/batches/batch_01.md. Messe WoTS 2026 = 22.–25.09.2026, Jaarbeurs Utrecht (laut Tina Batch 05); vorbei, nur rückblickender Bezug ("waren auf der WoTS 2026 vertreten"), kein "wir sehen uns am Stand".

## Grenzen / Lücken (bitte lesen)
- CRM-Dateien (bekannte_firmen, kundendatenbank_export) lagen Tina NICHT vor -> Schritt 0 nicht selbst durchführbar. Alle CRM-Aussagen sind "laut Tom" (AME bekannt; übrige neu). Tom hat zudem bekannte_firmen nur bis Zeile 1099 gelesen (A-E). Vor Stufe 3 CRM-Abgleich nachholen.
- WebFetch war für alle Zielseiten blockiert (Egress-Proxy: eti.nl, a1electronics.nl, ame.nu, avt-connecting.com, aemics.nl, fhi.nl, gimv.com, aemics). Prüfung daher NUR über WebSearch-Ergebnistexte/Snippets. Direkte Seitenzitate (z. B. "Pots in a housing or using a mould" bei A1, Imprägnierung/Vakuumverguss bei ETI) konnte Tina NICHT selbst nachlesen -> "von Tom übernommen, nicht unabhängig bestätigt".
- Patente: nur WebSearch (Google Patents-Treffer), kein Espacenet/DEPATISnet direkt. Kombinierte Suche nach Applicant-Namen + Potting/Encapsulation: keine Treffer = kein Gegenbeweis. Kein einziger Patentbeleg für eine der Firmen.
- Registerdaten (KvK/Handelsregister) nicht direkt abrufbar.

## Ergebnis

| Firma (Stand) | Ampel | Fertigung NL (Tina) | Verguss (Tina) | Belegt / nicht verwenden |
|---|---|---|---|---|
| ETI B.V. (Teil ARA-Stand 9C056) | GRÜN (Endprodukt-Regel) | 90 % – Vierde Broekdijk 16, 7122 JD Aalten; Quellen: Firmenverzeichnisse (Oozo, bedrijvenopdekaart, transfirm) + emworks-Testimonial ("Netherlands-based", Trafos >50 Jahre); Webseite = Selbstdarstellung zählt als eine. | 95 % Endprodukt enthält vergossenes Bauteil: Trafos, Drosseln, DC-Netzteile/Power Units sind klassische Vergussprodukte. Zusätzlich Suchtreffer eti.nl: "recently potted cable work with electronics in polyurethane for a customer" (Eigenverguss-Indiz, nur Snippet). Vakuumverguss/Imprägnierung laut Tom, von Tina nicht bestätigt. | Belegt: Produkte, Standort, Kontakt sales@eti.nl, Tel. +31 543 47 24 31 (Suchtreffer). NICHT verwenden: "Vakuumverguss" als Fakt, Mitarbeiterzahl, konkrete Verguss-Materialien (außer PU-Einzelprojekt), Patente (keine Treffer). Vorgehen: ETI direkt ansprechen, nicht "ARA" pauschal. |
| ARA Industries (Gruppe; LBHBox, EMKwadraad) (9C056) | GELB | 85 % (Aalten; Nivoge-Stiftung, 51-200 MA nur Verzeichnisangabe, 1 Quelle) | ARA selbst ~50 % (Schaltschrank/Mechatronik: Steuergeräte-/Elektronikbaugruppen möglich, unbelegt); FIPFG bei LBHBox/EMKwadraad nur Vermutung Toms | NICHT verwenden: FIPFG-Bedarf, Mitarbeiterzahl, Struktur-Aussagen (Stiftung). Adresse abweichend: WoTS-Liste "Tweede Broekdijk 6", ETI "Vierde Broekdijk 16" -> getrennte Einheiten. info@ara-industries.nl laut Tom, nicht verifiziert. |
| A1 Electronics Netherlands B.V. (9D084) | GRÜN mit Auflage CRM-Abgleich | 90 % – Almelo (Kolthofsingel 8); Gimv-Meldung 27.03.2024 (Metis Group "Eindhoven, Veendam, Drachten, Almelo") + CB Insights (gegründet 2001, Almelo, ~100 Kunden) – zwei Quellen, plus WoTS-Profil. | 90 % belegt als Fähigkeit: Gimv "adds potting and cable assembly capabilities" (unabhängige Dritt-Quelle). WoTS-Text "Pots in a housing or using a mould" von Tom, nicht von Tina nachgelesen. | Typ Auftragsfertiger (high-mix/low-volume EMS): Kunden-Produkte (Medizin, Industrie, Automotive) werden vergossen -> Eigenverguss UND Endprodukt-Regel. Strukton verkaufte an Metis Group (2024). Ansprechpartner: Rudy/Rob Oude Vrielink, Lamber Voortman (Gimv, GF). NICHT verwenden: Mitarbeiterzahl, Umsatz einzeln, Email (keine auffindbar), Verguss-Materialien. Abgestimmter Zugang mit AME/Variass (Metis) sinnvoll – wegen AME-CRM-Treffer Rücksprache Jey. |
| AVT Wiring & Connecting (9A067) | GELB | 80 % – Freddy van Riemsdijkweg 7, Eindhoven (fhi-Profil + werkenindekempen.nl; fhi-Profil = Selbstdarstellung). WoTS-Text: AVT ist AUCH Distributor ("we distribute electrical components and produce custom wiring harnesses"). "international locations" ungeklärt. | 80 % Eigenverguss/Overmolding von Kabeln/Steckern/PCBs belegt (fhi-Profil: "protects connectors and PCBs against dust, moisture, mechanical stress"); Verfahren/Material (Niederdruck? Epoxid? PU?) nicht benannt -> Einstufung "prüfenswert" bleibt, nicht 90 %. | NICHT verwenden: "Verguss mit Epoxid/PU", Mitarbeiterzahl ~90 (nur Toms Angabe, nicht nachprüfbar), Kundenliste (Landmaschinen, Kaffeemaschinen). Telefonnummer laut Tom, nicht von Tina geprüft. WoTS-Liste nennt Website avtic.com, Tom avt-connecting.com – Domain-Klärung offen. |
| AEMICS B.V. (9C055) | GELB (niedrige Prio) | 85 % – Oldenzaal (WoTS-Text + village.ai-Eintrag "headquartered in Oldenzaal"; KvK 6078378 laut Tom, nicht geprüft). | 45–50 % unbelegt: Embedded/PCBA für Industrie/Medizin/Defense; Sensor-Referenzen (WILA) laut Tom. Keine Potting-/IP-Angabe auffindbar. Endprodukt-Regel greift nur, wenn ein Kundenprodukt als Sensor/Modul vergossen wird – nicht belegt. | NICHT verwenden: Potting-Behauptung, Referenzkunden (WILA, Qmicro, Dekkers), 24-25 MA. info@aemics.nl laut Tom. Erst Datenblatt/IP-Angaben klären. |
| Applied Micro Electronics "AME" (9D084) | ROT (BEKANNT, laut Tom) | 90 % (Eindhoven Esp 100; Gimv, WoTS) | 90 % (Fähigkeit: Spritzguss, Potting, Coating laut ame.nu via Tom; Suchtreffer bestätigt Spritzguss, Systemmontage, Power Conversion, Sensorik) | Laut Tom CRM-Treffer (bekannte_firmen + Leads-Tab "Stufe 1 ausstehend") – Tina konnte nicht verifizieren. Kein Weitergang; nur Lead-Ergänzung. Gleiche Gruppe wie A1 (Metis Group) -> Konzernkontext beachten. WoTS-Liste von Tom als "CRM-Treffer: nein" geführt – Widerspruch zu Toms eigenem CRM-Befund, klären. |
| Amkor Zeefdruk BV (9C027) | ROT | 90 % (Ede; Selbstdarstellung "in-house", ISO 9001:2008-Angabe veraltet) | 25–30 % | Folientastaturen/Frontfolien: kein vergossener Bauteil im Endprodukt; Doming nicht belegt. Nicht verwenden: Doming-Bedarf. |
| Added Value Electronics AVE (8F043) | ROT | kein Fertiger | <=5 % | Eigenbeschreibung "electronics distributor" (WoTS-Text, Quelle Batch-Liste). |
| Alantys Technology (9B051) | ROT | kein Fertiger | <=5 % | Distributor/Sales-Büro laut Tom; WoTS-Text leer; von Tina nicht eigenständig geprüft. |
| AQC BV (9C105) | ROT | kein Fertiger | <=5 % | PCB-Lieferant ("more than just a PCB supplier", WoTS-Text); EMS-Thema gelistet, aber Handel/Engineering; von Tina nicht tiefer geprüft. |

## Kritik an Tom
- ETI: Hebel ist die Endprodukt-Regel (Trafo/Netzteil), nicht nur "Website nennt Potting". Tina stuft ETI daher höher als die Gruppe ARA.
- AVT: 85 % Verguss und 70 % Fertigung nicht ausreichend belegt; Tina ändert auf je ~80 % und nennt AVT zusätzlich als Distributor.
- Patente: Tom hat keine einzelnen Treffer; Tina auch nicht – Lücke bleibt.

## Weiter an Stufe 3
ETI B.V. (GRÜN), A1 Electronics (GRÜN, vorher CRM-Abgleich), ARA Industries (GELB, nur im Verbund mit ETI), AVT (GELB), AEMICS (GELB, niedrige Prio). NICHT weiter: AME (BEKANNT), Amkor, AVE, Alantys, AQC.
Auflage an alle: CRM-Abgleich vor Kontakt manuell durch Jey; Verifiziert am 2026-10-05 (nur teilweise, siehe Grenzen).

## Quellen
- https://www.gimv.com/en/node/4744 (A1 joins Metis Group, via Suchtext)
- https://www.gimv.com/en/node/4956 (Metis Group)
- https://www.gimv.com/en/node/4543 (AME, via Suchtext)
- https://www.cbinsights.com/compare/a1-electronics-vs-applied-micro-electronics
- https://eti.nl/contact/
- https://www.oozo.nl/bedrijven/aalten/aalten-kern/aalten-kern-zuid-1/53802/electrotechnische-industrie-eti-b-v
- https://bedrijvenopdekaart.nl/electrotechnische-industrie-eti-bv-342979.html
- https://www.emworks.com/testimonials/electrotechnische-industrie-eti-b.v
- https://fhi.nl/en/wots/exposant/avt-wiring-connecting/
- https://www.werkenindekempen.nl/werken-bij/avt-industrial-components-b-v
- https://village.ai/company/aemics
- https://fhi.nl/en/profiel/amkor-zeefdruk-bv/
- https://patents.google.com/ (Sammelabfrage, keine Treffer)
