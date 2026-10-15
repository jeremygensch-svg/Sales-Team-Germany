# Neuer Auftrag (2026-10-06): Drohnen + Humanoide Roboter – Hersteller und Zulieferer, ganz Deutschland

## Kundenwunsch (Zitat Jey)
- Segmente: **Drohnen** (Hersteller/Verteidigung) und **Humanoide Roboter**.
- Auswertung für **ganz Deutschland**, aufgeteilt in die **3 Vertriebsgebiete wie bei den Messelisten**: Annahme = Baden-Württemberg | Bayern | Rest Deutschland (+ Österreich/Niederlande separat markieren, falls Treffer). Spalte "Gebiet" nach Fertigungs-/Firmensitz.
- Suchkriterien (nicht vollständig): Drohnenhersteller/Verteidigung; Zulieferer/Supplier/Sub-Supplier (Komponenten, Verguss/Potting, Vakuumverguss/vacuum potting, Wärmeabfuhr/heat transfer, Gap Filler, Wärmeleitung); Isolierung/Verkapselung; Elektronik, Sensorik, Leiterplatten (PCB), Motoren, Spulen, Transformatoren, Drosseln; Feuchtigkeitsschutz, Vibrationsschutz, Schockdämpfung, Ex-Schutz, Hochspannungsschutz, Chemikalienschutz (Ölbeständigkeit); Wicklungsimprägnierung, Steuerungselektronik, Elektronikbaugruppen.
- Bekannte Drohnenhersteller (Startpunkte): Helsing, Quantum (Systems), ARX Robotics, Tytan.
- Humanoide: https://www.humanoids.fyi/ (Daten: GitHub kingjulio8238/humanoid-atlas, `src/data/companies.ts`; im Atlas nur wenige EU-OEMs: Neura Robotics [DE], PAL Robotics [ES], Engineered Arts [GB], Pollen Robotics [FR], Clone Robotics [PL]; Zulieferer-Einträge DE: Infineon, SKF, Ewellix, Bosch Sensortec; CH: Maxon, Rollvis, ORCA Dexterity, STMicro).

## Bewertungsregeln (verbindlich, Jey 2026-10-05/06)
- GRÜN = Fertigung/Montage in DE/AT/NL UND Produkt/Bauteil enthält etwas, das in der Regel vergossen/verklebt/gedichtet wird (Sensor, Motor, Spule, Trafo, Netzteil, Leistungselektronik, Steuerelektronik, Akku/BMS, Heizelement, LED, Optical Bonding). Auch zugekaufte, verbaute Bauteile zählen. KEINE zweite Fertigungsquelle nötig.
- GELB = Grenzfall (Fertigung/Eigenanteil unklar, Konzern-/CRM-Bezug klären, Produkte unbekannt). ROT = Händler, Software/Beratung, Wettbewerber/Lieferant (Dosier-/Vergussanlagen, Vergussmassen/Klebstoffe), Fertigung außerhalb DE/AT/NL.
- CRM-Abgleich Pflicht: `bekannte_firmen_DE-AT-NL.txt`, `kundendatenbank_export.txt` (Kern-Name-Regel; Konzern bekannt -> "Bestandskontakt pflegen", nicht als Neukunde).
- Drohnen/Verteidigung: Demak-Zielbereiche Electrical Insulation, E-Mobility Potting (Akkus/Motoren/Ladeelektronik), Wärmeleit-Dosierung (Gap Filler), Vakuumverguss.
- Output im bekannten Format (wie MOTEK/WoTS-Excel): Firma | Segment | Gebiet | Sitz/Fertigungsort | Website | Was gebaut wird -> typisch vergossene Bauteile | Wahrsch. Fertigung DE/AT/NL | Wahrsch. Verguss | Ampel | CRM-Status | Aktion | Bemerkung/Quellen.
- Arbeitsweise: batchweise, ein Agent-Lauf nach dem anderen (Nutzungslimit). Ergebnisse sofort als Datei in `drohnen_humanoide/` speichern.

## Plan (Batches)
1. Drohnen-OEMs/Verteidigung Deutschland (Helsing, Quantum Systems, ARX Robotics, Tytan, + weitere DE-Hersteller)
2. Humanoide-OEMs Deutschland/DACH/EU (Neura Robotics, Agile Robots, …)
3. Zulieferer Drohnen (Antriebe/Motoren, Akkus/BMS, Flugsteuerungen, Sensorik, PCB/EMS, Verguss/Wärmeleit-Dienstleister)
4. Zulieferer Humanoide (Aktuatoren, Getriebe, Sensorik, Motoren, Wicklungen, Leiterplatten)
5. Tina-Prüfung je Batch · 6. Excel (3 Gebiete, Ampel) + Übergabe
