# Tina Batch 04 – all about automation Düsseldorf 2026 (Prüfung von tom_batch_04.md)
Erstellt: 2026-10-15 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe: ausschließlich aaa_ergebnisse/tom_batch_04.md (10 Firmen). Halle nicht angegeben, Standnummer unverändert in Feld 1.
**VERMERK über allen Ampeln: ohne Browser/Web-Abruf geprüft, vorläufig.** Chrome-Werkzeuge nicht vorhanden; WebFetch liefert ENOTFOUND (Test: fuhrmeister-gmbh.de). Es stand nur WebSearch (Zusammenfassungen, Stufe S) zur Verfügung; keine Quelle wurde von mir selbst geöffnet. "Zitat im Browser bestätigt" ist deshalb bei allen Firmen: nein. Es gibt keine Stufe-V-Aussage.
Skripte: `python3 batch_check.py aaa_ergebnisse/tom_batch_04.md --tina` meldet bei allen 10 Blöcken nur "Feld 11: keine Ampel" (erwartet, Tina vergibt sie hier); sonst vollständig im Sinn des Skripts. Inhaltlich sind Feld 9 und 16 bei mehreren Firmen von Tom selbst als UNVOLLSTÄNDIG gekennzeichnet (Websuche-Limit). `python3 crm_abgleich.py` für alle 10 Firmen samt Marken/Konzern/Altnamen selbst ausgeführt: 10 von 10 neu; einzige Skripttreffer (Franz Binder) sind Zufallstreffer (Franz Kessler Z. 828, Franz Steger Z. 829, "Solero (vormals Kendrion Binder Magnete)" Z. 2229, andere Firmen), Toms Bewertung bestätigt. kundendatenbank_export.txt: keine Treffer, daher keine "Verifiziert am"-Prüfung nötig.
Verifikationsdatum aller Einträge: 2026-10-15. Tabellenzeile = Zeilennummer aus Regeldatei D.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 1 | EXTRA Computer GmbH (242) | GRÜN (schwach, vorläufig) | 4 (Sitzregel) | ja |
| 2 | Fibox GmbH (306) | GELB | 5 | ja (Vertrieb oder Fertigung?) |
| 3 | FIBRO Rundtische GmbH (134) | GRÜN (schwach, vorläufig) | 4 (Sitzregel) | ja |
| 4 | Franz Binder GmbH & Co. Elektrische Bauelemente KG (313) | GELB | 5 | nein |
| 5 | Fuhrmeister + Co GmbH (126) | GELB | 5 | nein |
| 6 | fünfeinhalb Funksysteme GmbH (424) | GELB | 2 | ja (Identität) |
| 7 | gbm mbH (836) | GELB | 5 | nein |
| 8 | Georg Schlegel GmbH & Co. KG (120) | GRÜN (vorläufig) | 4 (Sitzregel) | ja |
| 9 | Gerdt Seefrid GmbH (501) | GELB | 5 | ja (Händler, E2?) |
| 10 | GMK Electronic Design GmbH (203) | GRÜN (schwach, vorläufig) | 4 (Sitzregel) | ja |

Summe: 4 Grün, 6 Gelb, 0 Rot. Kein harter Ausschluss E1 bis E5 mit Quelle belegt; die E2-Verdachtsfälle (Fibox, Seefrid) sind nicht belegt und bleiben deshalb Gelb.

Patent-Nachholung (Regel F5): DEPATISnet, Espacenet und Google Patents waren für mich nicht erreichbar (kein Browser, WebFetch ENOTFOUND). Ersatz: je eine Websuche mit Anmelder und Verguss-/Dichtungs-Stichwörtern für Schlegel, Binder, FIBRO, EXTRA, GMK, Fuhrmeister (Ergebnisse jeweils unten); für Fibox, gbm, Seefrid, fünfeinhalb keine eigene Patentsuche (Budget), Toms Befunde gelten als Stufe S. Damit bleibt Feld 9 bei ALLEN 10 Firmen UNVOLLSTÄNDIG (keine zwei Datenbanken ausgeführt, kein Rechtsstand geprüft). Das ändert keine Ampel (Patente sind nur Zusatzsignal), die Nachholung bleibt Auftrag. Feld 16 (Wettbewerbereinsatz) bleibt bei EXTRA, FIBRO, Fuhrmeister, fünfeinhalb, gbm, Seefrid Lücke; ich habe es nicht gefüllt.

---

## 1. EXTRA Computer GmbH | Stand 242
*ohne Browser/Web-Abruf geprüft, vorläufig.*
**Ampel: GRÜN, schwach (Tabellenzeile 4, Fertigung nach Sitzregel Stufe A).** Inhabergeführter Gerätebauer mit eigenen Marken (Calmo, Pokini, exone) am Sitz Giengen; Panel-PCs/Rugged Tablets enthalten typisch verklebte/gedichtete Teile (Display/Touch, Gehäusedichtung; Verguss Mittel, A).
- Korrekturen an Toms Feldern: Feld 4/7: Eine Websuche liefert als Firmenaussage "in-house development, assembly and quality control ... in Giengen an der Brenz" (S). Neu: Ein Fachpressetext nennt die Calmo-Gehäuse als in Norddeutschland gefertigt (zugekauft, aber DE) und die Mainboards von Kontron Augsburg (S). Die Fertigungsaussage gilt damit für die Systemmontage, nicht für Gehäuse. Feld 17: Adresse Brühlstr. 12, 89537 Giengen-Sachsenhausen (Websuche-Zusammenfassung, S); Geschäftsführung Heinz und Wolfgang Fetzer (S, nicht Ampel-relevant, Regel K: nicht weiterverfolgen). Feld 9: eigene Websuche "EXTRA Computer Patent OR Gebrauchsmuster Pokini OR Calmo": keine Treffer (S, kein Gegenbeweis). Feld 8 unverändert Mittel (A); Beleg für IP-Dichtung der Pokini-Tablets fehlt auch bei mir.
- Zitat im Browser bestätigt: nein (nicht öffenbar).
- CRM: neu (crm_abgleich.py "EXTRA Computer GmbH", "exone", "Pokini", "Calmo": kein Treffer). Wettbewerbereinsatz: nicht ermittelt (Lücke, nicht gefüllt).
- Nicht verwendbare Aussagen: Fertigung Giengen (S); Verguss/Verklebung/Dichtung aller Bauteile (A); Pokini-IP-Dichtung (A); Mitarbeiterzahl (S); Calmo-Gehäuse Norddeutschland (S).
- Stichprobe für Jey: ja (Grün stützt sich auf Sitzregel plus Produkttyp A; Fertigungsbeleg nur S). Hinweis zur Nachrecherche (empfohlen, kein Gelb): Datenblatt Calmo/Pokini (IP-Klasse, Frontdichtung/Optical Bonding), Stellenanzeige Montage Giengen im Browser lesen.

## 2. Fibox GmbH | Stand 306
*ohne Browser/Web-Abruf geprüft, vorläufig.*
**Ampel: GELB (Tabellenzeile 5).** Fibox GmbH (Porta Westfalica) gehört zur finnischen Fibox Oy Ab; Fertigung in DE ist nicht belegt, es gibt Hinweise auf Fertigung im Ausland (Finnland, Polen, China, Korea), Verguss/Dichtung (PUR-Schaum) wäre Hoch (S), ist aber keinem DE-Werk zugeordnet. Kein Rot, weil E2 (Vertrieb ohne Fertigung) nicht belegt ist.
- Korrekturen: Feld 7 Niedrig/S bleibt im Kern, wird aber nicht als "unwahrscheinlich" festgeschrieben: eine Websuche gibt als Aussage der Fibox-Seite an, die GmbH führe Anpassungsarbeiten (Lackieren, Bedrucken, Gravieren, mechanische Bearbeitung) auf, Gehäuseproduktion dort nicht (S); ein Händlerprofil (nhp.com.au) nennt Werke in Finnland, Deutschland und Korea, ein anderes Verzeichnis nur Finnland und Korea (beide S, widersprüchlich). Feld 10 Tom "unwahrscheinlich" bleibt vertretbar, die Ampel ist nach Tabelle trotzdem Gelb (Fertigung nicht V und nicht widerlegt). Feld 12: kein CRM-Treffer für Fibox GmbH/Fibox Oy Ab/Fibox, kein Konzernbezug (neu). Feld 9: Toms Befund (nur US-Designpatente, Justia) bleibt S; eigene Patentsuche nicht ausgeführt.
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): (a) Gibt es in Porta Westfalica Fertigung oder nur Konfektionierung/Vertrieb? Wo nachsehen: fibox.com/about-fibox (Standortliste, im Browser), Impressum fibox.de, Stellenanzeigen Porta Westfalica (Produktion/Montage). (b) Wo wird die PUR-Dichtung der PCT-Serie eingeschäumt (Lempäälä, Kiuruvesi, Warschau, Korea)? Datenblatt PCT-Serie, Fibox-Produktionsseiten. Ist nur Konfektionierung/Vertrieb: ROT nach E2 mit Quelle. Aktion: nicht kontaktieren.
- Nicht verwendbare Aussagen: alle Fertigungs- und Verguss-Angaben (S/A); Standortliste der Gruppe (S, widersprüchlich); "Mutter Fibox Oy Ab" (S).
- Stichprobe für Jey: ja (E2-Frage entscheidet zwischen Rot und Gelb mit Potenzial).

## 3. FIBRO Rundtische GmbH | Stand 134
*ohne Browser/Web-Abruf geprüft, vorläufig.*
**Ampel: GRÜN, schwach (Tabellenzeile 4, Sitzregel).** Maschinenbauer mit Sitz und Hauptbelegschaft in Weinsberg, seit Management-Buyout 2024 eigenständig; die serienmäßige Elektronik (Smart Evaluation Module, Absolutwertgeber, IP65) enthält typisch vergossene/gedichtete Teile (Mittel, A).
- Korrekturen: Fertigung Hoch/S bestätigt durch Toms Angaben (128 von 168 Mitarbeitern am Sitz, S); Töchter USA/Indien/China: ob dort gefertigt wird, ist unbelegt (Sitzregel setzt "kein Konzern mit mehreren Werken" voraus). Eigene Websuche: kein Hinweis, wer die S.E.M.-Elektronik fertigt (S). Feld 9: eigene Websuche (Anmelder Fibro, Dichtung/Vergussmasse/Encoder): keine Anmeldungen der Firma, nur EPO-Beschwerde T 1603/16 (Fibro als Einsprechende) (S); Anmelder-Varianten Läpple/FIBRO GmbH nicht geprüft. Gleichnamige FIBRO GmbH (Haßmersheim) nicht vermischt, ebenfalls nicht im CRM.
- Zitat im Browser bestätigt: nein.
- CRM: neu (crm_abgleich.py "FIBRO Rundtische GmbH", "FIBRO": kein Treffer). Wettbewerbereinsatz: Lücke.
- Nicht verwendbare Aussagen: Fertigung/Montage Weinsberg (S, Stellenanzeigen-Snippet); Elektronikfertigung in Weinsberg (?); Verguss aller Bauteile (A); Mitarbeiterzahlen (S).
- Stichprobe für Jey: ja (Verguss nur A, Elektronik evtl. zugekauft; Fertigungsbeleg nur S). Empfohlene Nachrecherche: Stellenanzeigen Weinsberg im Browser lesen, Datenblatt FIBROTOR/S.E.M., Produktionsstätten der Töchter.

## 4. Franz Binder GmbH & Co. Elektrische Bauelemente KG | Stand 313
*ohne Browser/Web-Abruf geprüft, vorläufig.*
**Ampel: GELB (Tabellenzeile 5).** Verguss/Umspritzung ist beim Produkttyp Hoch (A: umspritzte Anschlussleitungen bis IP68), der Hauptsitz Neckarsulm ist Produktionsstandort, aber die binder Gruppe hat sieben Produktionsstätten (Konzern/Mehrwerk, Regel D verlangt Stufe V, nicht erreicht) und Standorte weltweit.
- Korrekturen: Feld 4/7: Websuche bestätigt "sieben Produktionsstätten" und weitere Standorte in CH, AT, FR, UK, NL, SE, CN, SG, USA; als weiterer deutscher Standort deutet ein Job auf Vohburg a. d. Donau (nicht bestätigt, S). Neu: Die Arbeitsagentur führt eine Ausbildung "Kunststoff-/Kautschuktechnologe/-in Formteile" bei der Franz Binder GmbH & Co. KG in Neckarsulm (Beginn 01.09.2027, S): Hinweis auf Spritzguss/Formteilfertigung am Sitz, kein Verguss-Beleg. Zukäufe: Introbest (Fellbach, Elektronikbaugruppen) und Eucrea-Gruppe (Pforzheim, 2019) (S). Feld 9: eigene Websuche "Franz Binder Vergussmasse OR umspritzt patent": keine Binder-Anmeldung (nur fremde Siemens-/Hochspannungs-Vergussmasse-Patente); Toms alte Binder-Patente (1970er/80er, kein Verguss) unverändert, Rechtsstand ungeprüft. Feld 12 bestätigt (siehe Kopf).
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): Welche Produktionsstätten liegen in DE/AT/NL und wo werden Leitungen umspritzt/vergossen (Neckarsulm, Vohburg, Fellbach, Pforzheim, Ausland)? Wo nachsehen: binder-connector.de Standortseite (Browser), Impressum, Stellenanzeigen Spritzguss/Verguss/Montage Neckarsulm. Ist dort V für die Werke erreicht: Grün (Zeile 4). Außerdem Domain und Impressum ermitteln. Aktion: vorrangig nachrecherchieren (hohes Verguss-Potenzial).
- Nicht verwendbare Aussagen: Zahl und Orte der Werke (S); Verguss/Umspritzung im Haus (A); Mitarbeiterzahlen (S, widersprüchlich: 1.200 / 1.400 / 1.800); "Produktion überwiegend in Deutschland" (S, Händlerpressetext).
- Stichprobe für Jey: nein.

## 5. Fuhrmeister + Co GmbH | Stand 126
*ohne Browser/Web-Abruf geprüft, vorläufig.*
**Ampel: GELB (Tabellenzeile 5).** Eigene Produkte (Filterlüfter, Klimageräte, Leuchten) sind erkennbar, Eigenfertigung in Hückeswagen ist aber nur durch ein Verzeichnis ("Vertrieb und Produktion", S) gestützt; Händleranteil (Lüfter, Kühler) nicht ausgeräumt, daher keine Sitzregel. Verguss Mittel (A: Lüftermotor/-elektronik, LED-Leuchten, Netzteile, Gehäusedichtung).
- Korrekturen: Feld 17: Adressabweichung bestätigt (Stahlschmidtsbrücke 61 in Firmendatenblättern und Schaltplänen 2015/2024 gegenüber Nr. 38 im Verzeichnis, S). Neu: Schaltpläne der Serie RAM (Verdichter, Verflüssiger, Verdampfer) zeigen eigene Kühlgeräte, sagen aber nichts über Fertigungstiefe (S). Feld 9: Tom führte gar keine Suche aus; meine eine Websuche (Fuhrmeister, Patent/Gebrauchsmuster Filterlüfter) ergab keine Treffer (S); Feld 9 bleibt UNVOLLSTÄNDIG (DEPATISnet, Espacenet, Google Patents offen).
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): Was fertigt/montiert Fuhrmeister in Hückeswagen selbst und was ist Handelsware? Wo nachsehen: Impressum und "Über uns" auf fuhrmeister-gmbh.de (Browser), Stellenanzeigen Montage/Produktion Hückeswagen (Websuche fand keine), Datenblatt Herstellerangabe. Zusätzlich Patente nachholen (DEPATISnet/Espacenet "Fuhrmeister"). Aktion: nicht kontaktieren.
- CRM: neu. Wettbewerbereinsatz: Lücke.
- Nicht verwendbare Aussagen: "Produktion" am Sitz (S, Verzeichnis); Eigenfertigung der Lüfter/Elektronik (?); Verguss aller Bauteile (A).
- Stichprobe für Jey: nein.

## 6. fünfeinhalb Funksysteme GmbH | Stand 424
*ohne Browser/Web-Abruf geprüft, vorläufig.*
**Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Zwei eigene Websuchen fanden die Firma nur in Interview-/Startup-Texten (Selbstdarstellung, Ausgründung TU Dresden 2023, Geschäftsführer Dr. Lucas Scheuvens, S); weder Impressum noch Handelsregister, Website oder unabhängige Quelle. Die Frage der Hardwarefertigung (BlitzFunk Access Points/Clients) ist offen; bei Software/Dienstleistung wäre E2 zu prüfen.
- Korrekturen: Feld 7 Mittel/? bleibt ohne Beleg, ist faktisch "unbekannt"; Tom bezeichnet die Beleglage selbst als dünn. Meine Suche "fünfeinhalb Funksysteme GmbH Handelsregister" lieferte keinen Registertreffer (Suchmaschinen-Negativbefund, kein Beleg für Nichtexistenz). Feld 9: keine eigene Suche, Toms Befund S.
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): (a) Identität: Impressum, Rechtsform, Adresse, Register (Amtsgericht Dresden) der fünfeinhalb Funksysteme GmbH. Wo nachsehen: handelsregister.de / unternehmensregister.de, Firmenwebsite über Interview-Link (startupvalley.news, computer-automation.de) ermitteln. (b) Wird die BlitzFunk-Hardware selbst gefertigt/montiert und wo? Produktseite, Datenblatt (Schutzart), Stellenanzeigen. Ist es Software/Systemhaus mit zugekaufter Hardware: ROT nach E2. Aktion: nicht kontaktieren.
- CRM: neu (crm_abgleich.py auch mit "5,5 Funksysteme": kein Treffer). Wettbewerbereinsatz: Lücke.
- Nicht verwendbare Aussagen: alle (Fertigung ?, Verguss A, Identität S).
- Stichprobe für Jey: ja (Firma nicht unabhängig auffindbar).

## 7. gbm mbH (Gesellschaft für Bildanalyse und Messwerterfassung) | Stand 836
*ohne Browser/Web-Abruf geprüft, vorläufig.*
**Ampel: GELB (Tabellenzeile 5).** Entwickler von Industrie-PCs, I/O-Modulen und Messtechnik in Mönchengladbach (Verzeichnisse, S); weder Eigenfertigung noch Montage am Sitz belegt, Sitzregel nicht tragfähig ("Entwickler" kann auch Zukauf/Auftragsfertigung bedeuten). Verguss Mittel (A).
- Korrekturen: Eigene Websuche bestätigt Adresse Lehmkuhlenweg 16, 41065 Mönchengladbach, Website gbm.de, Gründung 1994 und Produktliste (PC-Messtechnik, dezentrale I/O, Industrie-/Panel-PCs), aber nichts zur Fertigung (S). Feld 9: keine eigene Suche; Toms Befund bleibt S.
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): Fertigt oder montiert gbm Industrie-PCs und I/O-Module am Sitz? Wo nachsehen: gbm.de Produkt- und Unternehmensseiten, Impressum (Browser), Stellenanzeigen Elektronikmontage/Fertigung Mönchengladbach, Datenblatt (Schutzart, Panel-PC). Zusätzlich Patente (Espacenet/DEPATISnet, Anmelder "gbm"). Aktion: Beobachtung.
- CRM: neu. Wettbewerbereinsatz: Lücke.
- Nicht verwendbare Aussagen: Fertigung/Montage am Sitz (?/S); Verguss aller Bauteile (A); Panel-PC-Verklebung (A).
- Stichprobe für Jey: nein.

## 8. Georg Schlegel GmbH & Co. KG | Stand 120
*ohne Browser/Web-Abruf geprüft, vorläufig.*
**Ampel: GRÜN, vorläufig (Tabellenzeile 4, Sitzregel).** Familiengeführter Hersteller von Tastern, Leuchtdrucktastern, Not-Halt und RFID mit Hauptsitz Dürmentingen und Schwesterwerk Leipzig (beide DE); beleuchtete IP65/IP67-Taster mit integrierter LED und M12-Anschlüsse enthalten typisch vergossene/gedichtete Teile (Verguss Hoch, A).
- Korrekturen: Fertigung Hoch/S bestätigt: Eigene Websuche gibt einen Regionalzeitungsbericht wieder ("entwickelt und produziert in Dürmentingen", ca. 250 Mitarbeiter, Neubau erhöht Fläche von ca. 5.700 auf ca. 8.500 m²) (S, Schwäbische Zeitung, Seite nicht geöffnet). Leipzig: Schlegel Elektrokontakt GmbH (vormals DUX, 1993 gekauft, 2013 umbenannt) produziert Taster, Schalter, Gehäuse, Endschalter, Schaltfelder (S, Schlegel-Katalog); die Werkszuordnung der LED-Taster zu Dürmentingen oder Leipzig bleibt offen, beide liegen in DE (nur Zusatz, ändert die Tabellenzeile nicht). Die Singapur-Gesellschaft Schlegel Elektrokontakt Co (FE) Pte Ltd ist eine andere Einheit. Feld 9: eigene Websuche (Anmelder "Schlegel Georg", Vergussmasse/potted/encapsulated): keine Patentseiten, kein Verguss-Patent (S); Toms alte DE-Patente (Taster, Not-Aus) und Design D570300 bleiben Stufe S, Rechtsstand ungeprüft; Espacenet/DEPATISnet fehlen. Stellenanzeigen: Suche "Schlegel Dürmentingen Montage" ergab keine einschlägige Anzeige.
- Zitat im Browser bestätigt: nein.
- CRM: neu (crm_abgleich.py "Georg Schlegel GmbH & Co. KG", "Schlegel Elektrokontakt", "Schlegel": kein Treffer). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?; Tom: wettbewerber_referenzen.md ohne Schlegel, eine Websuche ohne Treffer; ich habe dort nichts ergänzt, Lücke bei Einzelsuche).
- Nicht verwendbare Aussagen: Verguss/Vergießen im Haus (A, kein Beleg); Fertigung Dürmentingen als aktuell (S); Mitarbeiterzahl (S); Werkszuordnung Dürmentingen/Leipzig (offen); IP65/IP67-Dichtmethode (A).
- Stichprobe für Jey: ja (Toms "interessant", Grün stützt sich auf Sitzregel und Produkttyp A, Fertigung nur S). Empfohlene Nachrecherche: schlegel.biz Standort-/Karriereseite, Impressum im Browser, Datenblatt Leuchttaster.

## 9. Gerdt Seefrid GmbH | Stand 501
*ohne Browser/Web-Abruf geprüft, vorläufig.*
**Ampel: GELB (Tabellenzeile 5).** Katalog von 36 DC-/BLDC-Motorserien und Reglern (Verguss Hoch, A: Wicklungen, Regler), aber die Firma beschreibt ihre Wurzeln im Vertrieb elektromechanischer Komponenten (Handelsvertretung seit 1949); Eigenfertigung der Motoren ist nicht belegt, nur Tragschienen-Zuschnitt/-Stanzung und "Sonderversionen im Rahmen der Fertigungsmöglichkeiten". E2 (Händler) ist nicht belegt und deshalb nicht Rot.
- Korrekturen: Eigene Websuche bestätigt: GlobalSpec führt die Firma als "Manufacturer" (S, Verzeichnis), das Firmenprofil nennt Vertrieb als Wurzel, Lagerhaltung der Antriebe in Bad Vilbel, Zuschnitt/Stanzen von Profilschienen; keine Wicklung/Motorfertigung erwähnt (S). Feld 9: keine eigene Suche; Toms Befund (keine Treffer, Schreibvarianten ungeprüft) bleibt S.
- Zitat im Browser bestätigt: nein.
- Nachrecherche-Auftrag (Gelb): Fertigt Seefrid Motoren/Regler selbst oder bezieht es Handelsware (ggf. mit Sonderanpassung)? Wo nachsehen: Firmenwebsite (Website bisher unbekannt, über allaboutautomation-Ausstellerprofil ermitteln), Impressum, Katalog (Herstellerangaben/Typenschild), Stellenanzeigen Montage/Wicklerei Bad Vilbel. Nur Handel: ROT nach E2 mit Quelle. Patente mit Schreibvarianten Seefried/Seifried nachholen. Aktion: nicht kontaktieren.
- CRM: neu. Wettbewerbereinsatz: Lücke.
- Nicht verwendbare Aussagen: Motorfertigung (?); Verguss der Motoren/Regler (A, gilt nur bei Eigenfertigung); "Manufacturer" im Verzeichnis (S).
- Stichprobe für Jey: ja (Händleranteil hoch, E2 möglich).

## 10. GMK Electronic Design GmbH | Stand 203
*ohne Browser/Web-Abruf geprüft, vorläufig.*
**Ampel: GRÜN, schwach (Tabellenzeile 4, Sitzregel).** Inhabergeführter Hersteller von Industrietastaturen, Touch-Keyboards und kundenspezifischen Elektronikbaugruppen mit einem erkennbaren Standort Wernberg-Köblitz ("Entwicklung, Produktion und Vertrieb", ISO 9001 Zertifikat gleicher Adresse, S); IP65-Frontabdichtung und Touch-Glasfront (Bonding) sind typisch verklebt/gedichtet (Mittel, A).
- Korrekturen: Schreibweise der Firma "GMK electronic design GmbH" (klein) bestätigt; Eigene Websuche: Datenblätter QT100 (Aluminiumgehäuse, Glas-Bedienfeld, IP65 frontseitig) und QM70 (Abdichtung nach IP65, Aluminium) (S); wie abgedichtet wird, steht in den Treffern nicht. Gründer Güntner, Meinhardt (ausgeschieden), Kredler; GMK ist Muttergesellschaft der Marke UNIQEY (Deskthority, S). Feld 9: eigene Websuche (Gebrauchsmuster/Patent, Anmelder GMK, Güntner, Kredler): keine Treffer (S, kein Gegenbeweis).
- Zitat im Browser bestätigt: nein.
- CRM: neu (crm_abgleich.py "GMK Electronic Design GmbH", "UNIQEY", "GMK": kein Treffer). Wettbewerbereinsatz: kein Hinweis gefunden (Stufe ?; Tom-Suche; ich habe keine eigene ausgeführt).
- Nicht verwendbare Aussagen: Fertigung am Sitz (S, Verzeichnis/Zertifikatszusammenfassung); Verklebung/Bonding der Gläser und Dichtmethode (A); Mitarbeiter/Struktur (S).
- Stichprobe für Jey: ja (Verguss nur A, keine Beschreibung der Abdichtung; Beleg nur S). Empfohlene Nachrecherche: Datenblatt QT100/QM70 im Browser lesen, Stellenanzeigen Wernberg (Montage/Kleben), Impressum.

---

## Konsistenz und Auffälligkeiten
- Tom hat alle Ampeln offen gelassen (korrekt, Feld 11 leer). Seine Tom-Einstufungen widersprechen meinen Ampeln nicht; zwei Abweichungen: Fibox (Tom "unwahrscheinlich") und Seefrid/gbm (Tom "prüfenswert") sind bei mir Gelb mit Auftrag, weil Fertigung nicht belegt ist und kein Ausschluss E1 bis E5 belegt ist.
- Alle Grün-Ampeln beruhen auf der Sitzregel (Fertigung A/S) plus Produkttyp (Verguss A) und sind ohne Stufe V vorläufig. Vor jeder Mail-Verwendung gilt: nur V ist mailtauglich (Regel C); aktuell wäre keine Aussage mailtauglich.
- Messe-Signal: Toms Grep auf aaa_duesseldorf_2026.csv nennt keinen Wettbewerber unter den Ausstellern; von mir nicht neu geprüft.
- Vorschlag für fehlerlog_lehren.md (nicht eingetragen, Jey gibt frei): Läuft ein Tom-Batch ohne Browser und ohne Patentdatenbanken, entstehen nur Stufe-S/A-Ampeln; solche Batches vor Tina-Freigabe im Browser nachholen (Patent-Pflichtsuchen F5, Impressum Feld 17).

## Einschränkungen
- Kein Browser, kein Web-Abruf: Chrome-Werkzeuge nicht vorhanden, WebFetch ENOTFOUND (einmal getestet). Keine einzige Quelle von mir selbst geöffnet; alle Aussagen aus WebSearch-Zusammenfassungen (Stufe S). Zitatprüfung (Regel O) nicht möglich: bei allen Firmen "nein".
- Websuche-Budget: ca. 28 Abfragen (Schätzung) auf 10 Firmen verteilt; priorisiert: Grün-Kandidaten (Schlegel, EXTRA, FIBRO, GMK), Identitäts- und Konzernfragen (fünfeinhalb, Fibox, Binder), Händlerfragen (Seefrid, Fuhrmeister, gbm).
- Patente: DEPATISnet, Espacenet, Google Patents nicht erreichbar; nur Websuche-Ersatz für 6 von 10 Firmen, Rechtsstand bei keinem Patent geprüft (Lehre 14). Feld 9 daher bei allen Firmen UNVOLLSTÄNDIG, Feld 16 bei sechs Firmen Lücke (EXTRA, FIBRO, Fuhrmeister, fünfeinhalb, gbm, Seefrid).
- Impressum/Handelsregister (Feld 17) bei keiner Firma gelesen; fünfeinhalb Funksysteme nicht unabhängig auffindbar.
- Kontakte nicht geprüft (Regel K), Größe/Umsatz nicht geprüft. Datenbankfelder nicht geändert, nichts verschickt, nicht committet.
