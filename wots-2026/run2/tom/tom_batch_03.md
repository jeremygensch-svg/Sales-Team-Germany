# WoTS 2026 (Eindhoven/Utrecht, FHI) – Batch 3 – TOM Durchlauf 2 (unabhängig neu recherchiert)

**Stand:** 2026-10-05. Messe-Modus. Messe war 22.-25.09.2026 (vorbei) -> Einstufung = Nachfass-Priorität.

## Einschränkungen
- WebFetch war für ALLE angefragten Firmendomains durch den Egress-Proxy gesperrt (dytos.eu, hortec.nl, demcon.com, hetronic.nl, frontfolies.com, eemc.nl, formit.nl, ideetron.nl). Arbeitsgrundlage: WebSearch-Snippets (Seitentexte der Firmenseiten werden dort teils wörtlich wiedergegeben) und FHI-Profile. Kein Volltext einer Firmenseite gelesen.
- `efx_verguss_wissensbasis.md` nicht im Repo auffindbar (find über /home/user ohne Treffer) -> Ableitung des Verguss-Bedarfs aus Produkttyp nach Rollenbeschreibung + Kernregel des Auftraggebers, ohne Skala der Wissensbasis.
- CRM-Dateien (bekannte_firmen_DE-AT-NL.txt, kundendatenbank_export.txt) liegen nicht vor. CRM-Status nur "laut Liste/Durchlauf 1": Spalte 'CRM-Treffer' der Ausstellerliste = "nein" bei allen 9 Firmen; Durchlauf 1 (tom_batch_03.md, Kopfzeile "CRM:") = alle 9 NEU, Hetronic-Eigentümer Methode Electronics nicht im CRM. Nicht gegen echtes CRM verifiziert -> Lücke.
- Patente: nur per WebSearch (Google Patents/USPTO-Treffer); Anmeldernamen wurden nicht direkt in Datenbanken abgefragt. "Keine Treffer" ist kein Gegenbeweis. Espacenet/DEPATISnet nicht direkt abfragbar.
- Durchlauf 1 diente nur als Hinweis. Abweichungen: Hortec-Potting ist belegt (Tom hatte "steht nicht auf der Website"); Ideetron-"Remote Power Switch" ist laut FHI-Meldung ein Produkt von RFI Engineering (Kooperation), nicht Ideetron-Eigenprodukt.

---

## 1. Demcon electronics – Halle 9, Stand 9C060
- **Produkt/Web:** Spezialisierter Elektronik- und RF-Kompetenzbereich der Demcon-Gruppe: Entwicklung (analog/digital, FPGA, Embedded) bis zertifiziertem, produktionsreifem Produkt; Produktion/Montage inhouse inkl. Reinraum (laut Snippet FHI-Profil). https://electronics.demcon.com/ ; https://fhi.nl/en/profiel/demcon/
- **Fertigung DE/AT/NL: 85 %.** Hauptsitz Enschede, weitere Standorte Eindhoven, Amsterdam, Oldenzaal, Roden, Münster (D) (kivi.nl/FHI-Snippet); "assembly in-house, advanced assembly lines, extensive cleanroom". Quelle 2 unabhängig: https://fhi.nl/en/profiel/demcon/ ; https://silicon-saxony.de/mitglieder/demcon-germany-gmbh/ . Fertigungsort der konkreten Elektronik-Serien nicht verifiziert (Münster laut Durchlauf 1/2 eher Mechatronik, nicht verifiziert).
- **Gebiet:** Rest Deutschland+Niederlande (Enschede, NL).
- **Verguss/Kleben:** (a) Endprodukt mit vergossenem Bauteil: 60 % ABGELEITET (Entwicklungsdienstleister für "demanding/safety-critical" Elektronik; Kundenprodukte unbekannt). (b) Selbst vergießen/verkleben: 35 % ABGELEITET, kein Beleg für Potting/Coating auf den gefundenen Seiten.
- **Patente:** keine Treffer gefunden (Suche "Demcon patent encapsulation/potting"; ein Overmoulding-Treffer US10913191 mit NL-Priorität 2014 – Anmelder im Snippet NICHT belegt, daher nicht zugeordnet).
- **Einstufung:** prüfenswert (60 %).
- **Demak-Bereich:** Electrical Insulation (nur falls Kundenprojekte Verguss erfordern; Entwicklungspartner-/Multiplikator-Gespräch).

## 2. Dytos – Halle 9, Stand 9C089
- **Produkt/Web:** Entwicklung, Fertigung und Lieferung kundenspezifischer HMI-Lösungen (Touchscreens, Displays, Embedded); bietet Tape-Bonding und Optical Bonding von Displays. http://www.dytos.eu ; https://dytos.eu/en_us/optical-bonding/
- **Fertigung DE/AT/NL: 90 %.** dytos.eu: Tape- und Optical Bonding "entirely in our modern production facility in the Netherlands" (Snippet); FHI-Profil "state-of-the-art production facility". Sitz Zoetermeer. Quellen: https://dytos.eu/en_us/optical-bonding/ ; https://fhi.nl/en/profiel/dytos/ (zweite Quelle = Selbstbeschreibung im FHI-Profil, nicht unabhängig).
- **Gebiet:** Rest Deutschland+Niederlande (Zoetermeer, NL).
- **Verguss/Kleben:** (b) 95 % BELEGT – Optical Bonding mit flüssigem 2K-Silikon und Silikon-Gel-Sheets plus Tape-Bonding (dytos.eu/en_us/optical-bonding). (a) 90 % ABGELEITET: Displays/Touchscreens mit Embedded-Boards. Hinweis: belegtes Material ist Silikon, Demak-OBS arbeitet mit UV-Harz – Passung der Chemie zu klären.
- **Patente:** keine Treffer gefunden.
- **Einstufung:** Kunde interessant (>=90 %, Klebstoffeinsatz belegt; Material-Passung offen).
- **Demak-Bereich:** Optical Bonding (OBS).

## 3. EEMC B.V. – Halle 9, Stand 9B069
- **Produkt/Web:** Spezialisierter Distributor für EMC-Materialien, Thermal-Interface-Materialien und Messtechnik; Hersteller u. a. Parker Chomerics, Leadertech; Import aus USA/Europa, Verkauf v. a. Benelux, gegründet 1977. https://www.eemc.nl ; https://fhi.nl/en/profiel/eemc-b-v/
- **Fertigung DE/AT/NL: 10 %** (Händler; "Eigen Productie" laut Durchlauf 1 nicht verifiziert). Quelle: FHI-Profil.
- **Gebiet:** Rest Deutschland+Niederlande (Capelle aan den IJssel).
- **Verguss/Kleben:** (a) nicht anwendbar (Handel). (b) 5 % ABGELEITET. Vertreibt Gap-Filler/TIM (Materialien, die Kunden verarbeiten) – Marktkontakt, kein Fertiger.
- **Patente:** keine Treffer gefunden.
- **Einstufung:** Wettbewerber/Lieferant (Händler von Dichtungs-/TIM-Materialien; Kanalgespräch möglich).
- **Demak-Bereich:** keiner (ggf. FIPFG/Gasketing als Kanalthema).

## 4. Formit BV – Halle 9, Stand 9C012
- **Produkt/Web:** Design, Entwicklung und Produktion von Kunststoffprodukten per CNC-Fräsen, Laserschneiden, NC-Biegen und Solvent Welding ohne Formen/Werkzeuge, Serien 1 bis 10.000 Stück. http://formit.nl ; https://fhi.nl/en/profiel/formit-bv/
- **Fertigung DE/AT/NL: 90 %** (Sitz Valkenswaard, Selbstbeschreibung als Produzent; zweite Quelle FHI-Profil, nicht unabhängig).
- **Gebiet:** Rest Deutschland+Niederlande (Valkenswaard, NL).
- **Verguss/Kleben:** (a) 15 % ABGELEITET (Kunststoffgehäuse/-teile, keine Elektronik belegt). (b) 20 % BELEGT nur für Lösemittelverklebung (Solvent Welding), kein Verguss/Dosieren von Reaktionsharzen.
- **Patente:** keine Treffer gefunden.
- **Einstufung:** unwahrscheinlich.
- **Demak-Bereich:** keiner.

## 5. Frontfolies.com – Halle 9, Stand 9B083
- **Produkt/Web:** Hersteller von HMI-Produkten: Frontfolien, Schaltfolien (Folientastaturen), Touchscreens; Materialien u. a. von 3M und MacDermid Autotype; Liefer 2-3 Wochen. https://www.frontfolies.com ; https://fhi.nl/en/profiel/frontfolies-com/
- **Fertigung DE/AT/NL: 60 %** (Selbstbeschreibung "manufacturer", Sitz Sprang-Capelle NL; Produktionsort nicht verifiziert, ggf. Zukauf/Asien – nicht verifiziert).
- **Gebiet:** Rest Deutschland+Niederlande (Sprang-Capelle, NL).
- **Verguss/Kleben:** (a) 25 % ABGELEITET (Folien/Touch ohne belegte Vergussbauteile). (b) 35 % ABGELEITET: Folienlaminierung mit Klebebändern/-folien (3M) wahrscheinlich, Optical Bonding nicht belegt.
- **Patente:** keine Treffer gefunden.
- **Einstufung:** unwahrscheinlich.
- **Demak-Bereich:** Optical Bonding nur falls gebondete Touchscreens bestätigt werden (nicht verifiziert).

## 6. Hetronic – Halle 8, Stand 8F047
- **Produkt/Web:** Industrielle Funkfernsteuerungen (Handsender in IP65-Gehäusen, ATEX-Varianten) für Kräne, Bau, Bergbau, Material Handling. Hetronic Nederland BV, Weesp: "authorized assembly partner" von Hetronic International (Oklahoma City, USA); Konzern: Methode Electronics (Übernahme Hetronic Holding). https://www.hetronic.nl ; https://www.mdm.com/premium/operations/finance/methode-electronics-acquires-hetronic-holding/ ; https://craft.co/hetronic
- **Fertigung DE/AT/NL: 55 %.** Weesp: Montage/Systemkonfiguration nach Kundenspezifikation (Snippet hetronic.nl/andwork). Konzernstandorte laut craft.co/Suchtreffern: USA, Italien, Malta, Schweiz; DE-Standort Abensberg (Öxlau 1a, Bayern) als "Hetronic Service GmbH" (stepstone/business-monitor) – Service/Vertrieb; DE-Produktion NICHT belegt. Die Elektronik-Serienfertigung des Konzerns liegt nach Durchlauf 1 außerhalb DE/AT/NL (Malta/Philippinen/USA; nicht verifiziert).
- **Gebiet:** Rest Deutschland+Niederlande (Weesp, NL); Konzern-DE-Einheit Bayern (Abensberg, Service).
- **Verguss/Kleben:** (a) 60 % ABGELEITET (Funkfernsteuerung mit Elektronik in IP65/ATEX-Gehäuse; Verguss nicht belegt). (b) 30 % ABGELEITET.
- **Patente:** US 11375633 "Electronic device" (Priorität DE 20 2018 101 401.3, März 2018) tauchte in der Suche zu Hetronic auf, Anmelder im Snippet NICHT belegt und Verguss-Bezug nicht belegt -> nicht verwertet. Sonst keine Treffer gefunden.
- **Einstufung:** prüfenswert (50 %), Entscheidungsebene vermutlich Konzern außerhalb NL.
- **Demak-Bereich:** Electrical Insulation (Gehäuse-/Elektronik-Verguss, falls Ex-Schutz per Verguss erfolgt – nicht verifiziert).

## 7. Hortec Electronics – Halle 9, Stand 9B106
- **Produkt/Web:** Entwicklung (Hortec Technology BV) und Fertigung/Montage (Hortec Assemblies BV) von Elektronik für Dritte: PCBA, Box Build, Embedded Software; ISO 9001 und AS9100. https://www.hortec.nl ; https://www.hortec.nl/en/manufacturing-services/
- **Fertigung DE/AT/NL: 90 %** (Oldenzaal, Zutphenstraat 53; "25+ years EMS"). Quellen: hortec.nl/en/manufacturing-services ; https://fhi.nl/en/profiel/hortec-electronics/ ; LinkedIn https://nl.linkedin.com/company/hortec-bv
- **Gebiet:** Rest Deutschland+Niederlande (Oldenzaal, NL).
- **Verguss/Kleben:** (b) 90 % BELEGT – hortec.nl: PCBAs können vergossen (potting) oder lackiert (coating) werden zum Schutz gegen Feuchte/Ammoniak; Hortec hat die Einrichtungen dafür (Snippet der Manufacturing-Services-Seite). Verguss-Volumen/Materialien unbekannt. (a) 80 % ABGELEITET (Lohnfertiger, Kundenbaugruppen werden vergossen).
- **Patente:** keine Treffer gefunden.
- **Einstufung:** Kunde interessant (Verguss als Dienstleistung belegt; Volumen/Chemie klären).
- **Demak-Bereich:** Electrical Insulation (ggf. E-Mobility Potting je nach Kundenprojekten).

## 8. Ideetron b.v. – Halle 9, Stand 9C079
- **Produkt/Web:** Elektronik-Entwicklung (Schaltplan/PCB, FPGA, RF/LoRa/LoRaWAN, Firmware), Prototypen und Serienfertigung (DigiKey-Eintrag). http://www.ideetron.nl ; https://www.digikey.ch/de/design-services-providers/ideetron-bv ; https://fhi.nl/en/profiel/ideetron-b-v/
- **Fertigung DE/AT/NL: 40 %** (Sitz Doorn, NL; Fertigungsort der Serien nicht verifiziert, vermutlich Zukauf EMS).
- **Gebiet:** Rest Deutschland+Niederlande (Doorn, NL).
- **Verguss/Kleben:** (a) 40 % ABGELEITET (LoRaWAN-Sensoren/Gateways für Outdoor, Kundenprodukte unbekannt). (b) 15 % ABGELEITET. Kooperation mit RFI Engineering für LoRaWAN-Remote-Power-Switch (Quelle: https://fhi.nl/nieuws/rfi-engineering-and-ideetron-conclude-cooperation-agreement-to-promote-the-new-rfi-lorawan-remote-power-switch/) – Produkt gehört RFI, nicht Ideetron.
- **Patente:** keine Treffer gefunden.
- **Einstufung:** prüfenswert (untere Grenze, 40 %).
- **Demak-Bereich:** Electrical Insulation (nur bei Outdoor-Sensorprojekten, nicht verifiziert).

## 9. InduCompWare BV – Halle 8, Stand 8F032
- **Produkt/Web:** Lieferant und Systemintegrator industrieller Computer und Embedded-Systeme (Standard und kundenspezifisch: Sondergehäuse, Displays, integrierte Systeme). Website laut Liste "?", FHI-Profil: https://fhi.nl/en/profiel/inducompware-bv/ (Domain inducompware.com aus Durchlauf 1, nicht verifiziert)
- **Fertigung DE/AT/NL: 15 %** (Integrator/Distributor; eigene Fertigung nicht belegt).
- **Gebiet:** Rest Deutschland+Niederlande (Aalsmeer, NL).
- **Verguss/Kleben:** (a) 15 % ABGELEITET, (b) 10 % ABGELEITET. Kein Beleg.
- **Patente:** keine Treffer gefunden.
- **Einstufung:** kein Fertiger (Handel/Integration).
- **Demak-Bereich:** keiner.

---

## Übersicht

| Firma | Stand | Fertigung DE/AT/NL % | Verguss (a)/(b) % | Einstufung |
|---|---|---|---|---|
| Demcon electronics | 9C060 | 85 | 60 abgel. / 35 abgel. | prüfenswert |
| Dytos | 9C089 | 90 | 90 abgel. / 95 belegt (Optical Bonding, Silikon) | Kunde interessant (Optical Bonding) |
| EEMC B.V. | 9B069 | 10 | n/a / 5 | Wettbewerber/Lieferant (Händler) |
| Formit BV | 9C012 | 90 | 15 abgel. / 20 belegt (nur Solvent Welding) | unwahrscheinlich |
| Frontfolies.com | 9B083 | 60 | 25 abgel. / 35 abgel. | unwahrscheinlich |
| Hetronic | 8F047 | 55 | 60 abgel. / 30 abgel. | prüfenswert (Konzern-Entscheidung) |
| Hortec Electronics | 9B106 | 90 | 80 abgel. / 90 belegt (Potting/Coating) | Kunde interessant (Electrical Insulation) |
| Ideetron b.v. | 9C079 | 40 | 40 abgel. / 15 abgel. | prüfenswert (niedrig) |
| InduCompWare BV | 8F032 | 15 | 15 abgel. / 10 abgel. | kein Fertiger |

CRM: alle laut Liste/Durchlauf 1 "nein/NEU", nicht gegen echtes CRM geprüft.
