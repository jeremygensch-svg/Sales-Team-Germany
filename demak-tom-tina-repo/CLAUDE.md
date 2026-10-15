# Projektkontext: DEMAK Recherche-Team (Tom und Tina)

DEMAK (Aulendorf) baut Dosier- und Vergussanlagen. Dieses Repo enthält die Recherche-Agenten für Neukunden und Messen. Es wird nie automatisch etwas versendet; alle Ergebnisse gehen zur Freigabe an Jey.

Lies zuerst `regeln_tom_tina.md` (verbindliche Regeln, Ampel-Entscheidungstabelle) und `fehlerlog_lehren.md`.

Ablauf: 00a linkedin-profil-leser → 00b linkedin-akquise-filter → 01 Tom (recherche-mitarbeiter) → 02 Tina (recherche-pruefer) → 03 email-autor → 04 email-pruefer → 05 finale-qualitaetskontrolle. Stufe 03 bis 05 ruhen.

Wichtige Regeln in Kurzform:
- Tom und Tina laufen als getrennte Agenten. Tina bekommt nur Toms Batch-Datei (`tom_batch_NN.md`), nie dessen Zwischenschritte.
- Vor jeder Übergabe: `python batch_check.py tom_batch_NN.md` (Tina: mit `--tina`). Unvollständig heißt: nicht abgeben.
- CRM-Abgleich pro Firma: `python crm_abgleich.py "Firma" "Konzern" "frühere Namen"`.
- Belegstufen V/A/S/?; Ampel nur nach Entscheidungstabelle; Patente (mindestens zwei Datenbanken, Rechtsstand) und Wettbewerbereinsatz sind Pflicht.
- Keine Captchas lösen, Cookie-Banner ablehnen, keine Archive oder Mirror-Seiten.
- Kunden- und CRM-Daten bleiben lokal (siehe .gitignore).
