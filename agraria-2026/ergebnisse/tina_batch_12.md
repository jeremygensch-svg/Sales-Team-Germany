# Tina Batch 12 - agraria 2026 (Prüfung von tom_batch_12.md)
Erstellt: 2026-11-25 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe zur Firmenrecherche: ausschließlich agraria-2026/ergebnisse/tom_batch_12.md (10 Firmen, Nr. 111 bis 120, Länder DE/AT/NL laut Messeliste, alle AT). Die Messehinweise (Halle/Stand) stehen unverändert aus Toms Datei.
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (Kurzfassungen/Snippets) und Bash zur Verfügung; WebFetch und Chrome nicht genutzt bzw. nicht verfügbar. Es gibt in diesem Batch KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Grün ist mailtauglich (hier ohnehin keines vergeben).
Skripte: `python3 crm_abgleich.py` für alle Firmen samt Konzern-/Alt-/Schwester-/Schreibvarianten selbst wiederholt (Varianten je Block). Tabellenzeile = Zeile der Ampel-Tabelle D (regeln_tom_tina.md). Verifikationsdatum aller Einträge: 2026-11-25.
Entscheidungen von Jey, angewandt: Verbände/Prüfdienstleister/Forschung raus (im Batch keiner); Firmen im CRM mit gleichem/sehr ähnlichem Namen raus (im Batch keiner); Anlagenbauer bleiben drin, außer sie bauen selbst Verguss-/Dosieranlagen (E1; im Batch keiner). Da ein harter Ausschluss nur mit Stufe V Rot ergibt (Tabellenzeile 1) und es hier keine V-Quelle gibt, stehen Händler/Verlag/Saatgut/Dünger als Gelb (Zeile 7, "Rot-Kandidat E2") mit Empfehlung "aussortieren", wie in Batch 52 bei Smart Systems Hub. Jey entscheidet.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 111 | DIE SAAT (Halle 20, Stand F20) | GELB (Rot-Kandidat E2) | 2 | nein |
| 112 | diebauern.app GmbH (Halle 17, Stand 110) | GELB (Rot-Kandidat E2) | 2 | nein |
| 113 | DILA Fenstersanierung (Halle 17, Stand 260) | GELB | 6 | nein |
| 114 | DKW GmbH (Freigelände, Stand 20) | GELB | 2 | ja |
| 115 | Donut (Halle 20, Stand 1120) | GELB (Rot-Kandidat E2) | 2 | nein |
| 116 | Edtmayer Türen & Tore (Halle 24, Stand 75) | GELB | 4 nicht erfüllt, Zeile 5 (Fertigung A ohne belegte Sitzregel-Voraussetzung, Verguss Mittel) | ja |
| 117 | Einböck GmbH (Halle 21, Stand C20) | GELB (grünnah) | 5 | ja |
| 118 | ENdorado GmbH (Halle 17, Stand 20) | GELB | 5 | ja |
| 119 | ERBER AGRO GMBH (Halle 19, Stand 220) | GELB (Rot-Kandidat E2/E3) | 2 | nein |
| 120 | Ertl-Auer e.U. (Halle 22, Stand B40) | GELB (Rot-Kandidat E2) | 2 | nein |

Zahlen: Grün 0, Gelb 10, Rot 0.
Hinweis zur Zeile bei Nr. 116/117: Die Sitzregel (Stufe A genügt) greift bei Industrie-/Maschinenbauern mit erkennbarem Standort. Bei Einböck (Zeile 4 wäre erfüllbar) setze ich bewusst Zeile 5/Gelb, weil die Fertigungsquellen nur Fachpresse-Snippets sind und die Elektronik (Kamera) nach meiner Suche zugekauft ist (siehe Block 7); das Verguss-Argument tragen damit nur zugekaufte Teile. Das ist Auslegungssache und eine Stichprobe für Jey (Frage: genügt "Endprodukt-Regel, auch zugekaufte verbaute Teile zählen" für Grün?). Nach Endprodukt-Regel (Abschnitt D: "Auch zugekaufte, verbaute Teile zählen") wäre Einböck Grün nach Zeile 4; ich markiere das ausdrücklich als Entscheidungsfrage an Jey statt es stillschweigend zu setzen.

Patente (Prüfpunkt 8, Regel F5): Google Patents, Espacenet und DEPATISnet waren nicht direkt abfragbar. Eigene Patent-Websuche per WebSearch nur für Einböck (1 Abfrage, kein Patentdatensatz im Index); für die übrigen Firmen keine eigene Wiederholung, Toms Suchen werden weder übernommen noch widerlegt. Feld 9 ist damit bei ALLEN 10 Firmen ohne Datenbankabfrage: nach F5 UNVOLLSTÄNDIG, Nachholen im Browser nötig (Toms Batch ist laut seiner Einschränkung ebenfalls unvollständig). "Keine Treffer" ist kein Gegenbeweis. Rechtsstand nirgends geprüft.
Wettbewerbereinsatz (F6): Grep auf wettbewerber_referenzen.md mit Einböck, Einboeck, Edtmayer, ENdorado, DILA, DKW, Ertl, RWA, Erber, Donut, diebauern: nur Zufallstreffer bei "Erber" in Wörtern/Namen anderer Art und "RWA" als Teilzeichenfolge, keine Firmenbezüge (bei Erber/RWA Trefferzeilen nicht einzeln als Firmenbezug geprüft; keine Firma des Batches steht dort als Kunde). Keine Einzelsuchen mit Wettbewerbernamen von mir, außer Einböck (Suche nach Elektronik/Zulieferer). Messe-Signal (Wettbewerber aus E1 als Aussteller der agraria): nicht geprüft, offen.
Nicht durchgeführt: Browser-Gegenlesen jeder Quelle, Impressen, Firmenbuch/Registerabfragen im Original, Google Patents/Espacenet/DEPATISnet, Stellenanzeigen auf Firmenseiten, Messekatalog agraria.at.

---
