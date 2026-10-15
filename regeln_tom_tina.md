# Gemeinsame Regeln für Tom (Stufe 1) und Tina (Stufe 2) – Version 2

Status: ENTWURF vom 2026-10-12, noch nicht in Betrieb. Gilt nur für die Testversionen
`recherche-mitarbeiter-v2` und `recherche-pruefer-v2`. Die alten Agenten-Dateien bleiben unverändert.
Entscheidungen von Jey (2026-10-12): Größe/Umsatz optional ohne Einfluss auf die Ampel; Tina vergibt bei
fehlendem Beleg Gelb mit Nachrecherche-Auftrag statt Rot; Tom und Tina dürfen Chrome-Werkzeuge zum Gegenlesen
nutzen; Kontakt-/Ansprechpartnersuche ist pausiert, solange Stufe 3 bis 5 ruhen.

## A. Fakten-Regel
Kein Raum für Spekulation oder Eventualitäten. Jede Angabe trägt eine Belegstufe (Abschnitt C). Unbelegtes wird als
"unbekannt" oder "angenommen" gekennzeichnet, nie als Fakt ausgegeben. Keine Kontaktdaten, Zahlen, Standorte oder
Produkte erfinden.

## B. Kontext über Demak
KONTEXT ÜBER DEMAK (Stand: Recherche 2026-09-22; Quellen: demakgroup.com, kromex.com –
siehe Quellenliste am Ende dieses Abschnitts):

Demak Group (Sitz Turin/Italien; weitere Einheiten: Demak Polymers Turin, Demak Germany
Essen, Demak North America, Demak South America, Vertriebsbüros Indien/China) stellt sowohl
die Dosier-/Misch-/Vergussanlagen (Equipment) als auch die passende Harzchemie (>200
validierte Systeme) selbst her – Maschine und Chemie aus einer Hand. Über 4.000 installierte
Anlagen weltweit, Export in 40+ Länder.

Sechs Geschäftsbereiche (Application Areas):
1. E-Mobility Potting – Verguss/Isolation für EV/HEV-Batterien, E-Motoren, ECUs,
   Ladeelektronik, Kondensatoren, Sensoren, Leiterplatten. Epoxid (RT- und heißhärtend),
   Polyurethan.
2. Electrical Insulation – elektrische Isolierung für Zünder, Tauchpumpen, Zündspulen,
   Ventile, Sensoren, Transformatoren, Kondensatoren, E-Motoren, Leiterplatten. Epoxid/
   Polyurethan, flammhemmend.
3. LED Encapsulation – Verguss von LED-Modulen/-Profilen (Architektur-/Automotive-
   Beleuchtung), meist transparentes/transluzentes Polyurethan.
4. Optical Bonding (Produkt "OBS") – UV-Harz-Verklebung von LCD-Displays/Touchscreens/
   Glas gegen Luft/Feuchtigkeit/Staub, bessere Bildschärfe + Stoßfestigkeit. Zielgruppe:
   Hersteller von Displays/Touchscreens (Consumer Electronics, Automotive).
5. FIPFG & Gasketing/Sealing (Produkt "FomexOne") – Formed-in-Place-Foam-Gasket, flüssige
   PU-Dichtung direkt appliziert. Zielbranchen: Automotive, Filter, Haushaltsgeräte,
   Beleuchtung, Schaltschrank-/Elektronikgehäuse.
6. Kromex & Doming – eigene Markenlinie für dekorative 3D-Oberflächen (siehe unten).

SONDERBEREICH KROMEX: Kromex® ist eine patentierte Demak-Markenlinie (eigene Website
kromex.com, seit 2005) für In-House-Fertigung von 3D-Emblemen/Decals mit Chrom- oder
Farbfinish, Dicke bis 25 mm. Automotive-zertifiziert (SAE J1960/J1976, ASTM G151, RoHS,
ELV). Zielbranchen: Automotive-Embleme/Badges, Marine, Haushaltsgeräte, Tuning-Produkte,
Konsumelektronik, Werbe-/Promotionartikel. Eigene Maschinenlinie (MPJ 45-30, MP 60-30,
HP 65-40, HD 100-40).

SONDERBEREICH DOMING: Doming ist kein Einzelprodukt, sondern eine Beschichtungstechnologie
– Demak-Dosieranlagen gießen eine klare Harzschicht auf Oberflächen (Label, Logos,
Aufkleber, Embleme) für einen dreidimensionalen Schutzeffekt. Zielbranchen: Sign-/
Werbetechnik, Label-/Sticker-/Badge-Hersteller. (Konkrete Doming-Maschinenmodelle sind nur
über Fachpresse belegt, nicht auf der aktuellen Demak-Hauptseite – bei Detailfragen nicht
spekulieren, sondern als "nicht offiziell verifiziert" kennzeichnen.)

Dienstleistungen: Potting Sprint (2-wöchiges Beratungsprogramm für E-Mobility-Hersteller),
Potting Lab (Testlabor), Piece Design Consulting, Outsourcing Service, Technical Support.

MATERIAL-HINWEIS: Bestätigt sind Epoxid (RT- und heißhärtend) und Polyurethan. Silikon ist
auf der aktuellen Demak-Website NICHT als eigene Materialklasse bestätigt (nur ältere/
sekundäre Quellen) – nicht als aktuellen Fakt verwenden, sondern nur "Epoxid/Polyurethan"
nennen, sofern nicht anderweitig für eine konkrete Firma verifiziert.

Zielmärkte (Vertrieb): DACH-Region als Kern, zusätzlich Italien, Niederlande, potenziell
Saudi-Arabien.

Quellen: demakgroup.com (Hauptseite, /demak-group/, /e-mobility-potting/,
/electrical-insulation/, /led-encapsulation/, /optical-bonding/, /gasketing-and-sealing/,
/kromex-doming/, /resins/, /equipment/, /potting-sprint/), kromex.com (/en/kromex/
what-kromex, /en/equipment/).

## B2. CRM-Abgleich (Normalisierung)
Pflicht-Referenzquellen im Projektordner: `bekannte_firmen_DE-AT-NL.txt` und `kundendatenbank_export.txt` (Textexport;
die .xlsx ist binär und nicht lesbar). Der Abgleich läuft vor der Kandidatenauswahl und vor der Ausgabe.

ABGLEICH-NORMALISIERUNG (auf beiden Seiten anwenden, dann vergleichen):
- Kleinschreibung; Anführungszeichen, Punkte, Kommas, Binde-/Schrägstriche, unsichtbare
  Zeichen entfernen; Mehrfach-Leerzeichen zu einem.
- Rechtsformen/Zusätze streichen: GmbH, AG, KG, mbH, SE, e.K., e.G., GmbH & Co. KG,
  GmbH + Co KG, & Co., Co. KG, UG, S.r.l., B.V., N.V., s.r.o., Inc., Ltd., Co., Group,
  Deutschland, Germany, Holding, International.
- "&" / "+" / "und" vereinheitlichen; ae/oe/ue == ä/ö/ü. Ergebnis = "Kern-Name".
- Kern-Name identisch ODER eindeutige Kurzform/Präfix (>= 5 Zeichen, gleiche Wortwurzel,
  z. B. "a.p. microele" ~ "a.p. microelectronic") => BEKANNT, nicht aufnehmen.
- Gleicher Kern-Name, aber erkennbar anderer Ort/Land => "unklar", nicht als neu aufnehmen.
Der Abgleich ist VOR der Recherche (Kandidatenauswahl) UND erneut VOR der Ausgabe zu
machen. In die Ausgabe geht nur, was nach diesem Abgleich echt neu ist; bekannte und
unklare Firmen in einem eigenen Abschnitt "nicht aufgenommen (bereits bekannt / unklar)"
mit CRM-Schreibweise + gefundener Schreibweise auflisten.

## C. Belegstufen (an jeder Aussage zu Fertigung, Produkt, Verguss)
- **V = verifiziert:** Die Quelle wurde selbst gelesen (Produktseite, Datenblatt, Pressemeldung, Stellenanzeige, Register).
  Angabe: URL plus wörtliches Kurzzitat. Ein Suchsnippet allein ist nie V.
- **A = abgeleitet:** aus Produkttyp oder Endprodukt nach `efx_verguss_wissensbasis.md` (Block A/B), kein direkter Beleg.
  Kennzeichnung "abgeleitet aus Produkttyp: ...".
- **S = nur Snippet:** Seite nicht abrufbar (z. B. 403, Cookie-Wand) oder nur eine WebFetch-Kurzzusammenfassung.
  Gilt wie A, mit Vermerk, welche Seite nachzulesen ist.
- **? = angenommen:** weder Beleg noch Ableitung. Zählt nie für Grün.
Mailtauglich ist nur V. A und S dürfen in einer Email höchstens als Frage oder über das Endprodukt formuliert werden
("in Sensoren stecken typischerweise vergossene Bauteile"), nie als Behauptung über die Firma.

## D. Bewertung (verbindlich: Endprodukt-Regel 2026-10-01, GRÜN-Regel 2026-10-05, Ergänzung 2026-10-06)
- **Endprodukt-Regel:** Es zählt, was gebaut wird und welche Teile darin typisch vergossen, verklebt, gedichtet oder
  dosiert werden (Sensor, Motor, Spule, Trafo, Netzteil, Leistungselektronik, Steuerelektronik, Akku/BMS, Heizelement,
  LED, Display für Optical Bonding). Eigenverguss muss nicht belegt sein. Auch zugekaufte, verbaute Teile zählen.
- **Sitzregel (Ergänzung 2026-10-12):** Für "Fertigung in DE/AT/NL" genügt Stufe A (Sitz = Fertigungsort), wenn die Firma
  ein Industrie-, Maschinen- oder Gerätebauer mit einem erkennbaren Standort ist (eigene Produkte, kein Händler, kein
  Konzern mit mehreren Werken, keine Hinweise auf Auslagerung ins Ausland). Stufe V (eine Quelle) ist nötig bei Konzernen
  und Marken, mehreren Werken, Auftragsfertigern sowie bei Hinweisen auf Fertigung im Ausland. Ein Montage- oder
  Produktionsjob am Sitz (Stellenanzeige) gilt als V für den Fertigungsort. Fertigung nur "engineered in Germany" belegt
  keine Fertigung.
- **Medizintechnik (Jey, 2026-10-14):** Medizinprodukte (Dentaltechnik, Röntgen, Diagnostik, Antriebe, Sensorik) enthalten
  meist vergossene oder verklebte Bauteile, oft in sehr kleinen Mengen (Mikrodosierung). Kleine Dosiermengen sind kein
  Gegenargument. Beispiel: Dentsply Sirona (Bensheim) bleibt Grün. Ein Beleg, dass ein einzelnes Bauteil (z. B. ein
  Röntgenstrahler) ölisoliert statt vergossen ist, senkt die Wahrscheinlichkeit für dieses Bauteil, nicht für das Produkt
  insgesamt: Tom und Tina prüfen die übrigen Teile (Steuerelektronik, Sensoren, Mikromotoren, LED/Optik, Dichtungen).
- **Ampel als feste Entscheidungstabelle (2026-10-14).** Eingaben: harter Ausschluss (E1-E5), Fertigung DE/AT/NL, Verguss (höchstes
  Bauteil), Identität, Konzern-/CRM-Bezug. Die Ampel folgt der ersten zutreffenden Zeile:

  | Nr. | Bedingung | Ampel |
  |---|---|---|
  | 1 | Harter Ausschluss E1 bis E4 belegt (Stufe V) oder dieselbe Einheit im CRM (E5) | ROT |
  | 2 | Identität nicht belegt (Name/Sitz widersprüchlich, Firma nicht auffindbar) | GELB, Auftrag Identität |
  | 3 | Konzern oder Schwester im CRM, Einheit unklar (Regel M) | GELB, Auftrag Einheit klären |
  | 4 | Fertigung DE/AT/NL Stufe V (oder Stufe A nach Sitzregel) UND Verguss Hoch oder Mittel (Stufe A oder V) | GRÜN |
  | 5 | Fertigung DE/AT/NL Stufe A ohne Sitzregel, S oder ? | GELB, Auftrag Fertigungsbeleg |
  | 6 | Fertigung belegt, Verguss Niedrig (alle Bauteile) | GELB, Auftrag Produkte/Bauteile |
  | 7 | sonst | GELB mit Auftrag |

  Gleiche Eingaben ergeben immer dieselbe Ampel. Tina nennt die Nummer der zutreffenden Zeile in ihrer Begründung.
- **Bauteil-Regel (Jey, 2026-10-14):** Der Verguss wird auf Firmen- und Produktebene bewertet, nach dem Bauteil mit der höchsten
  Wahrscheinlichkeit, nicht nach dem schwächsten. Ein Beleg, dass EIN Bauteil nicht vergossen wird (z. B. ölisolierter
  Röntgenstrahler), senkt weder Firmen-Ampel noch Gesamtwahrscheinlichkeit, solange andere Bauteile oder Baugruppen
  typisch vergossen werden. Tom und Tina listen dafür je Firma alle Bauteile/Baugruppen mit ihrer Vergusswahrscheinlichkeit
  und nehmen das Maximum für die Ampel. Nur wenn ALLE plausiblen Bauteile belegt nicht vergossen werden, sinkt der Wert.
- **GRÜN:** Fertigung oder Montage in DE/AT/NL (Stufe V, eine Quelle genügt, z. B. die Firmenseite; bei Sitzregel Stufe A) UND das Produkt
  enthält typisch Vergossenes/Verklebtes/Gedichtetes/Dosiertes (Stufe A genügt, V ist besser). Keine zweite
  Fertigungsquelle nötig.
- **GELB:** Grenzfall. Fertigungsumfang unklar, Konzern- oder CRM-Bezug zu klären, Beleg fehlt, aber ist beschaffbar.
  Jedes Gelb enthält einen NACHRECHERCHE-AUFTRAG: die konkrete Frage, die offen ist, und wo nachzusehen ist
  (z. B. "Wird die PV-Anschlussdose in Essen gefertigt? Produktseite und Datenblatt lesen").
- **ROT:** nur bei harten Ausschlüssen (Abschnitt E). Fehlender Beleg allein ist nie ein Rot-Grund.
- **Größe/Umsatz/Mitarbeiterzahl:** optionales Feld, kein Einfluss auf die Ampel, nur suchen, wenn es nebenbei
  auffindbar ist; sonst "unbekannt". Verwendung in einer Email nur mit Stufe V und zwei unabhängigen Quellen.

## E. Harte Ausschlüsse (nur diese führen zu Rot)
Jede Rot-Begründung nennt die Bedingung und die Quelle ("Rot, weil: ... (URL)").
1. Wettbewerber oder Materialhersteller im Demak-Kerngeschäft: Hersteller, Integratoren oder Vertrieb von Dosier-/
   Dispensing-/Vergussanlagen (z. B. GONANO, Scheugenpflug, DOPAG, ViscoTec, RAMPF, bdtronic, Hilger u. Kern,
   Sonderhoff, Marco, Nordson, Musashi) und Hersteller von Vergussmassen, Reaktionsharzen, Klebstoffen, Dichtstoffen,
   Schutzlacken (z. B. EPOXONIC, WEVO, ELANTAS, DELO, Panacol, Lohmann, OTTO-CHEMIE, Wacker, Sika, Henkel, Hexion).
2. Händler, Distributor oder Vertriebsgesellschaft ohne Fertigung in DE/AT/NL; Software, Beratung, Design-Häuser;
   Hochschulen, Studierende, Freiberufler.
3. Fertigung oder Montage ausschließlich außerhalb DE/AT/NL.
4. Treffer auf Sperrliste oder Tab "Partner & Lieferanten".
5. Firma oder Konzern steht im CRM (Bestandskontakt pflegen, kein Neukunde). Gleicher Kern-Name an anderem Ort/Land:
   nicht Rot, sondern Gelb mit Auftrag "juristische Einheit manuell klären".
   Klarstellung 2026-10-12: Rot nur, wenn dieselbe Firma (gleiche Einheit) im CRM steht. Steht nur der Konzern oder eine
   Schwester im CRM, gilt Abschnitt M (Gelb mit Auftrag, Jey bestätigt die Einheit).

## F. Suchstrategie auf Produktebene (Tom sucht, Tina prüft)
Pro Firma in dieser Reihenfolge, bis die Frage "Was wird in DE/AT/NL gebaut und was steckt darin?" beantwortet ist:
1. Produktseiten, Kategorien, Datenblätter (PDF): Produkte, IP-Klasse, Medien, Einsatzumfeld.
2. Firmen- und Standortseiten, Impressum, Register: wo wird gefertigt? Produkt dem Werk zuordnen.
3. Pressemeldungen, Fachpresse, Messeprofile: Produkt, Neuheit, Standortausbau.
4. Stellenanzeigen und Karriereseite: Vergießer, Dosieren, Kleben, Montage.
5. Patente (PFLICHT für JEDE Firma, nicht nur für Grün-Kandidaten; Regel 2026-10-12). Mindestens zwei getrennte Suchen
   je Firma: (a) Google Patents im Browser, Anmelderfilter (Firmenname, Konzern- und Schreibvarianten) allein und dazu
   Stichwörter Verguss/Vergussmasse/Verkapselung/potting/encapsulation/Dichtung/Klebung/dispensing; (b) Espacenet (worldwide.espacenet.com, Direkt-URL mit pa=... und ctxt=...) UND DEPATISnet
   mit Anmelder und Stichwort (beide Datenbanken, wenn erreichbar; sonst Grund nennen). Zusätze (Regel 2026-10-14): Anmelder-Varianten
   inkl. Konzern, Vorgänger- und Schwesterfirmen mitsuchen; je relevantem Patent den Rechtsstand (erteilt/aktiv, Anmeldung, zurückgezogen, erloschen)
   PFLICHT nennen (Google Patents zeigt ihn); zurückgezogene/erloschene Patente sind nur schwaches Zusatzsignal; Anmelder-Zuordnung prüfen (Person vs. Firma, gleichnamige Firmen aussortieren); bei großen
   Trefferlisten zusätzlich eine enge Suche (potting compound OR Vergussmasse) fahren. Je Firma melden: Zahl und die relevantesten Treffer (Nr., Titel, Jahr, Link,
   Status), Suchbegriffe und Datenbank. Bestehende Patente sind ein Signal, dass die Firma Verguss/Dichten/Kleben selbst
   entwickelt oder anwendet. "Keine Treffer" ist kein Gegenbeweis, muss aber mit den ausgeführten Suchen belegt sein.
   Das Feld 9 darf nie "nicht geprüft" lauten. Misslingt die Suche (Seite blockiert, Captcha), steht im Feld, welche Suche
   fehlt, und der Batch gilt als UNVOLLSTÄNDIG (Tina weist ihn zurück bzw. holt die Suche nach).
6. Wettbewerbereinsatz (PFLICHT für jede Firma, Regel 2026-10-12). Zuerst die Datei wettbewerber_referenzen.md lesen und die Firma samt Konzern dort abgleichen (Treffer = Hinweis mit Stufe), danach die Einzelsuche: Nutzt die Firma Anlagen, Massen oder Klebstoffe von
   Wettbewerbern (z. B. Scheugenpflug, Nordson, bdtronic, ViscoTec, DOPAG, Hilger u. Kern, Sonderhoff, Marco, Musashi,
   Henkel, Wacker, Elantas, DELO)? Quellen: Referenz-/Anwenderseiten der Wettbewerber, Pressemeldungen, Fachartikel,
   Messeberichte, Stellenanzeigen mit Anlagen-/Materialnamen, Datenblätter, Fotos. Ergebnis mit Stufe V/A/S/?, Name des
   Wettbewerbers und Quelle, oder "kein Hinweis gefunden (Suchen: ...)". Das Feld ist ein Zusatzsignal (Wechsel-/
   Erweiterungskunde vs. Neueinsteiger), hat keinen Einfluss auf die Ampel und macht nie Rot.
Bei Konzernen mit mehreren Sparten oder Standorten werden Sparte und Werk getrennt bewertet. Die tragende Aussage
benennt immer die fertigende Einheit.

## G. Ausweichweg bei nicht abrufbaren Seiten
Gilt bei 403, Cookie-Wand, nur Snippet oder WebFetch-Kurzzusammenfassung.
1. Dieselbe Information auf anderem Weg suchen: Datenblatt-PDF, Pressemeldung, Katalog- oder Händlerseite,
   Fachpresse, Messeprofil.
2. Seite im Browser lesen (Abschnitt H), falls das Werkzeug vorhanden ist.
3. Sonst Stufe S und Vermerk "Seite X nachlesen".
WebFetch liefert nur Kurzzusammenfassungen. Ein Negativbefund daraus ("steht nicht auf der Seite") ist nie ein Beleg für
"nicht vorhanden" und führt nie allein zu einer schlechteren Ampel.

## H. Browser zum Gegenlesen (Chrome-Werkzeuge, nur lesen)
Einsatz: Negativbefunde aus WebFetch bei Grün-Kandidaten, Unterseiten und Akkordeons, Stufe-S-Aussagen.
Regeln: nur öffentliche Seiten der geprüften Firma, nur lesen (nichts ausfüllen, kein Login, nichts absenden, nichts
herunterladen), menschliches Tempo, höchstens 5 Seiten je Firma. Zu Beginn `tabs_context_mcp` prüfen. Erscheint eine
Login-Wand, ein Captcha oder eine Sperrmeldung: sofort stoppen, nichts lösen oder umgehen, in der Ausgabe melden.
Ist der Browser nicht nutzbar: Vermerk "Browser nicht verfügbar" und ohne ihn weiterarbeiten.

## I. Prüftiefe nach Wichtigkeit
- Alle Firmen: Websuche, CRM-Abgleich, Belegstufen prüfen.
- Grün-Kandidaten und alle von Tom als "interessant" eingestuften Firmen: zusätzlich jede tragende Aussage
  im Browser oder per geöffneter Quelle gegenlesen.
- Tina markiert pro Batch die Firmen mit der größten Restunsicherheit als "Stichprobe für Jey".

## J. Übergabeformat (ein Format für alle Modi)
Pro Firma eine Zeile bzw. ein Block mit diesen Feldern, in dieser Reihenfolge:
1. Firma (bei Messen zusätzlich Halle, Stand aus dem Input, unverändert)
2. Segment / Demak-Geschäftsbereich
3. Gebiet nach Fertigungs- oder Firmensitz: Baden-Württemberg | Bayern | Österreich | Rest Deutschland+Niederlande | außerhalb
4. Sitz und Fertigungsort (fertigende Einheit)
5. Website
6. Was wird gebaut -> welche Bauteile darin sind typisch vergossen/verklebt/gedichtet (mit Belegstufe)
7. Fertigung DE/AT/NL: Hoch | Mittel | Niedrig + Belegstufe + Begründung (keine Prozentwerte, Skala siehe Abschnitt R)
8. Verguss/Bonding (höchstes Bauteil, Bauteil-Regel): Hoch | Mittel | Niedrig + Belegstufe + Begründung; alle Bauteile mit Einzelbewertung auflisten
9. Patentrecherche (Pflicht, mind. 2 Suchen): Anzahl, Nr./Titel/Jahr/Link/Status der relevantesten Treffer, Datenbank und Suchbegriffe; oder "keine Treffer" MIT den ausgeführten Suchen
10. Einstufung Tom: interessant (Fertigung Hoch UND Verguss Hoch) | prüfenswert (mindestens ein Mittel, keins Niedrig) | unwahrscheinlich (mindestens ein Niedrig) | Wettbewerber/Lieferant | kein Fertiger
11. Ampel (nur Tina): Grün | Gelb | Rot, mit Begründung in 1 bis 3 Sätzen
12. CRM-Status: neu | bekannt (CRM-Schreibweise) | unklar
13. Nachrecherche-Auftrag (bei Gelb Pflicht) und Aktion
14. Quellen: URL + wörtliches Kurzzitat (unter 15 Wörter) + Abrufdatum je tragender Aussage; Tina ergänzt "Zitat im Browser bestätigt: ja/nein"
15. Größe/Umsatz (optional, "unbekannt" erlaubt)
16. Wettbewerbereinsatz (Pflicht): Wettbewerber/Produkt + Stufe + Quelle oder "kein Hinweis gefunden (Suchen: ...)"
17. Identität (Pflicht): Name, Rechtsform, Adresse und Register oder Impressum (URL) stimmen überein; Abweichungen zur Vorgabe (z. B. Gemini-Sitz) benennen
Tina ergänzt: "nicht verwendbare Aussagen" (Stufen A, S, ?), Datum der Verifikation, ggf. "Stichprobe für Jey".

## K. Pausiert (Jey, 2026-10-12)
Solange Stufe 3 bis 5 ruhen: keine gezielte Suche nach Ansprechpartnern, Emailadressen oder Kontaktformularen und keine
Prüfung der Kontaktaktualität. Taucht bei der Produktrecherche zufällig ein Ansprechpartner mit Quelle auf, wird er
notiert, aber nicht gesucht.

## L. Arbeitsweise
Batchweise, ein Agent-Lauf nach dem anderen (Nutzungslimit; Websuche-Limit je Session). Ergebnis sofort als Datei im
Projektordner speichern (`tom_batch_NN.md`, `tina_batch_NN.md`). Läuft Tina ohne Websuche, steht über der Ampel der
Vermerk "ohne Web geprüft, vorläufig".


## M. Konzernabgleich (Ergänzung 2026-10-12)
Bei jeder Tochter-, Marken- oder Gruppenfirma ("Member of ...", "ein Unternehmen der ...") wird zusätzlich der Konzernname
(Normalisierung wie B2) gegen bekannte_firmen_DE-AT-NL.txt und kundendatenbank_export.txt abgeglichen. Ein Treffer
auf den Konzern wird als "CRM-Konzernbezug" gemeldet (Beispiel: Reijnen Sealing, Member of TTS Group, TTS GROUP steht im CRM).
Gelb mit Nachrecherche-Auftrag "ist es dieselbe Einheit?", nicht stillschweigend Rot oder Neu.


## N. Messemodus (Jey, 2026-10-14)
Für Ausstellerlisten (WoTS, EFX, MOTEK u. a.) gelten alle Regeln dieser Datei unverändert: Belegstufen, Sitzregel, Bauteil-Regel,
Medizintechnik-Regel, harte Ausschlüsse, Konzernabgleich (M), Pflicht-Patentrecherche (F5), Wettbewerbereinsatz (F6), Browser-
Gegenlesen (H) und Übergabeformat (J). Es gibt keine abgeschwächte Messe-Prüfung.
Zusätze: 1. Halle, Stand und Messe stehen unverändert in Feld 1. 2. Wettbewerber, die auf derselben Messe ausstellen, werden als
Hinweis genannt (Messe-Signal), ändern aber nichts an der Ampel. 3. Bereits bekannte Firmen erscheinen mit Vermerk BEKANNT. 4. Läufe
laufen batchweise (max. 10 Firmen je Batch), damit Patent- und Browserprüfung für jede Firma vollständig bleibt; ein Batch ohne
Feld 9 und 16 gilt als unvollständig. 5. Aussteller-Beschreibungstexte der Messe sind Stufe S, nie V.


## O. Zitat- und Identitätsprüfung (Regel 2026-10-14)
- Jede mit Stufe V geführte Aussage hat URL, wörtliches Kurzzitat (unter 15 Wörter) und Abrufdatum. Tina öffnet jede V-Quelle
  einer Grün-Kandidatin selbst im Browser und trägt "Zitat im Browser bestätigt: ja/nein" ein. Steht das Zitat nicht auf der Seite,
  wird die Aussage auf S oder ? herabgesetzt und die Ampel neu bestimmt.
- Identität (Feld 17): Firmenname, Rechtsform, Adresse und Register-/Impressumsquelle müssen zur Vorgabe passen. Ist die Vorgabe (z. B.
  eine Liste aus Gemini oder einer Messe) falsch oder mehrdeutig, wird die tatsächliche Firma benannt, die Abweichung steht im Feld, und
  die Ampel kann höchstens Gelb sein (Tabellenzeile 2), bis Jey die Firma bestätigt. Gleichnamige Firmen werden nicht vermischt.

## P. Nachrecherche-Schleife (Regel 2026-10-14)
Gelb bleibt nicht liegen: Nach Tinas erster Bewertung nimmt Tom jeden Nachrecherche-Auftrag auf (Runde 1, nur dieser Auftrag, im Browser),
Tina prüft das Ergebnis und setzt die Ampel neu. Höchstens zwei Runden. Wird die Frage nicht beantwortet, bleibt Gelb mit dem
Vermerk "braucht Mensch" und der konkreten Frage an Jey. Rot oder Grün aus der Schleife werden mit dem neuen Beleg begründet.

## Q. Unabhängigkeit von Tom und Tina (Regel 2026-10-14)
Tom und Tina laufen als getrennte Agenten. Tina erhält ausschließlich Toms Ergebnisdatei (tom_batch_NN.md), nicht seinen Rechercheweg, und
recherchiert eigenständig nach. Ein Agent, der beide Rollen nacheinander spielt, gilt nicht als unabhängige Prüfung. Bei Läufen mit
Gelb-Schleife gilt dasselbe: Tom-Nachrecherche und Tina-Prüfung sind getrennte Aufrufe.

## R. Skala und Lernschleife (Regel 2026-10-14)
- Stufenskala statt Prozentwerten: Hoch = direkter Beleg oder Produkttyp, der praktisch immer vergossen/gefertigt wird (früher >= 70 %);
  Mittel = plausibel, aber Typ- oder Einheitenzuordnung offen (40 bis 69 %); Niedrig = unwahrscheinlich oder widerlegt (unter 40 %).
  Jede Einstufung nennt Belegstufe und Begründung.
- Frische: Jede Quelle trägt ein Abrufdatum. Belege und CRM-Verifikationen älter als sechs Monate werden neu geprüft.
- Lernschleife: Jede Korrektur, die Jey an einem Ergebnis vornimmt, wird als Fall in fehlerlog_lehren.md eingetragen (Firma, Fehler,
  Ursache, neue Regel). Tom und Tina lesen den Abschnitt "Lehren" der Datei in Schritt 0. Wird ein Fehler wiederholt, gilt er als Regelfehler
  und die Regel wird hier geändert.
- Goldstandard: goldstandard_testset.md enthält Firmen mit Jeys eigener Bewertung (Ampel, Fertigungsort, Verguss, Begründung). Nach jeder
  Regeländerung läuft der Test; Messgrößen: falsches Grün, falsches Rot, Übereinstimmung der Ampel. Jede von Jey geprüfte Firma wird dort ergänzt.

## S. Hilfsskripte (nur Standardbibliothek von Python, Regel 2026-10-14)
- crm_abgleich.py "Firmenname" ["Konzernname" ...]: normalisiert (Abschnitt B2), vergleicht mit bekannte_firmen_DE-AT-NL.txt und
  kundendatenbank_export.txt und gibt Treffer mit Zeilennummer und Ähnlichkeit aus. Ist Bash oder Python nicht verfügbar, wird nach B2 mit Grep manuell
  gleiche Prüfung gemacht und der Grund genannt. Das Skriptergebnis ersetzt das Augenmaß.
- batch_check.py tom_batch_NN.md: prüft Vollständigkeit (Felder 1 bis 10, 12 bis 17 je Firma, Feld 9 mit mindestens zwei Suchen, Feld 16 gefüllt,
  jede V-Aussage mit URL und Zitat). Meldet UNVOLLSTÄNDIG mit Liste; ein unvollständiger Batch geht nicht an Tina.
