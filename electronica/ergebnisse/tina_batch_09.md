# Tina Batch 09 – electronica 2026 (Prüfung von tom_batch_09.md)
Erstellt: 2026-10-15 (Tina, Stufe 2, Version 2, getrennter Agent, Regel Q). Eingabe: ausschließlich electronica/ergebnisse/tom_batch_09.md (10 Firmen, Nr. 94 bis 103). Eigene Suchen, kein Übernehmen von Toms Rechercheweg.
**VERMERK ÜBER ALLEN AMPELN: ohne Browser/Web-Abruf geprüft, vorläufig.** Es standen nur WebSearch (24 Abfragen, Kurzfassungen/Snippets) und Bash zur Verfügung; WebFetch und Chrome nicht nutzbar. In diesem Batch gibt es KEINE Stufe-V-Aussage, auch nicht aus meiner Prüfung. "Zitat im Browser bestätigt" ist überall: nein (nicht möglich). Kein Ergebnis ist mailtauglich.
Skripte: `python3 batch_check.py` = VOLLSTÄNDIG (10 Blöcke; erkennt nur Felder, nicht die Qualität der Patentsuche). `python3 crm_abgleich.py` für alle Firmen samt Konzern-/Alt-/Schwesternamen selbst wiederholt (Ergebnis je Firma unten). Tabellenzeile = Zeilennummer der Ampel-Tabelle D. Verifikationsdatum aller Einträge: 2026-10-15.

## Gesamtübersicht
| Nr | Firma (Stand) | Ampel | Tabellenzeile | Stichprobe Jey |
|---|---|---|---|---|
| 94 | Calterah Semiconductor (B4.420) | GELB | 7 | nein |
| 95 | Caltest Instruments GmbH (A4.349) | GELB | 5 | ja |
| 96 | Camtek Germany GmbH (B1.510) | GELB | 7 | nein |
| 97 | Catalonia Trade & Investment (C2.119) | GELB | 7 | nein |
| 98 | Cathedy GmbH (A5.200) | GELB | 5 | ja |
| 99 | CCI Eurolam GmbH (A1.563) | GELB | 7 | ja |
| 100 | CCI Europe GmbH (C4.240) | GELB | 2 | ja |
| 101 | C.C.P. Kontakt GmbH (B1.221) | GELB | 5 | ja |
| 102 | CEFEG GmbH Federn- und Verbindungstechnik Chemnitz (B2.428) | GELB | 6 | ja |
| 103 | CELUS GmbH (C5.558) | GELB | 7 | nein |

Zahlen: Grün 0, Gelb 10, Rot 0. Grund für Rot 0: E2/E3 sind bei mehreren Firmen sehr wahrscheinlich (Calterah, Camtek, Catalonia, CCI Eurolam, CELUS, Cathedy, CCP), aber nirgends mit Stufe V belegt; Rot verlangt V (Zeile 1). Alle Rot-Kandidaten haben einen Auftrag zur V-Bestätigung.

## Querschnitt: Patente (F5), Wettbewerber (F6), Messe-Signal
- Patente: Google Patents, Espacenet, DEPATISnet waren nicht direkt abfragbar. Eigene Anmelder-Websuchen (Stichwort-Suchen, keine Datenbankfilter): CEFEG (2 Suchen: Chemnitz/Anmelder/Gebrauchsmuster und Google-Patents-Anmelder), Caltest (1), Cathedy (1, Patent/Gebrauchsmuster/utility model), CCP (1, waterproof/sealing/potting): keine Datensätze mit der Firma als Anmelder. Für Calterah, Camtek, Catalonia, CCI Eurolam, CCI Europe, CELUS keine eigene Wiederholung. Feld 9 bleibt bei ALLEN 10 Firmen ohne Direktabfrage: schwacher Befund, kein Gegenbeweis. Der Batch ist nach F5 UNVOLLSTÄNDIG im Sinne der Datenbankabfrage; Nachholen im Browser (Google Patents mit Anmelderfilter, Espacenet pa=..., DEPATISnet) nötig, bevor ein Grün final wird. Zusatzhinweis: CCP-Präsentation nennt ein Probe-Patent M453149 (Taiwan, Hochstromstift, kein Verguss, S).
- Wettbewerbereinsatz (F6): eigener Grep auf wettbewerber_referenzen.md (alle Firmen- und Konzernnamen, inkl. Chang Chun, CCI, CCP): kein Eintrag, Toms Angabe bestätigt. Keine Einzelsuche mit Wettbewerbernamen; "kein Hinweis" ist kein Gegenbeweis.
- Messe-Signal (N2): Toms Liste (bdtronic, ELANTAS, Momentive, Nordson Test&Inspection, RAMPF) nicht von mir wiederholt; ändert keine Ampel.
- Frische (Regel 5, Prüfpunkt): Keine der Firmen steht im CRM, daher keine "Verifiziert am"-Prüfung.

---

## 94. Calterah Semiconductor | B4.420
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Fabless-Halbleiterdesigner mit Shanghaier Konzern (Dealroom/CB Insights, S); Münchner Einheit nur als "first overseas site" (S), Rechtsträger und Fertigung nicht belegt. Fertigung DE Niedrig, Verguss Niedrig (Chips; Radarmodule gehören Kunden). Keine Zeile 1 mangels V.
- Eigene Prüfung: Suche nach Handelsregister/Calterah Germany: kein Registertreffer, Dealroom nennt ca. 11,5 % der Belegschaft in Deutschland (S, ohne Entität). Fabless-Status bleibt Einordnung aus Profilen (S), keine eigene Fabrik gefunden. CRM: `crm_abgleich.py "Calterah Semiconductor" "Calterah Semiconductor Technology"`: neu.
- Korrekturen an Toms Feldern: keine inhaltlichen. Feld 17 bleibt offen (Rechtsträger München).
- Nachrecherche-Auftrag (Gelb, Zeile 7): Welche Gesellschaft steht hinter dem Münchner Stand (Rechtsform, Adresse, Tätigkeit: nur Entwicklung/Vertrieb?) und ist Fertigung in DE ausgeschlossen? Wo nachsehen: calterah.com (Impressum/Contact), Handelsregister München, electronica-Ausstellerprofil. Bei Bestätigung "reiner Designer/Vertrieb": Rot nach E2/E3 mit Quelle.
- Zitat im Browser bestätigt: nein. Nicht verwendbare Aussagen: Fabless (S/A); Münchner Einheit (S); Verguss Chip/Gehäuse (A). Stichprobe für Jey: nein.

## 95. Caltest Instruments GmbH | A4.349
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5).** Eigendarstellung "specialist distributor"; zugleich "power electronics specialist" mit BSFZ-Siegel (Forschungszulage, Nov. 2025, S) und Produktlinien programmierbare AC/DC-Quellen, Lasten, regenerative Lösungen (S). Ob eigene Geräte gebaut oder Partnermarken (Pacific Power, APS, IKONIX, Gustav Klein, GW Instek) vertrieben werden, ist nicht entschieden; Sitzregel greift wegen Händler-Hinweis nicht.
- Eigene Prüfung: Adresse Binzigstraße 21, 77876 Kappelrodeck (chemie.de, elektroniknet, S). Zwei Quellen widersprechen sich (Distributor vs. "manufacturer" bei ProvenExpert); eine Stellenanzeige "Applikations- und Support-Ingenieur" (S) nennt Show-Room/Demonstration, keine Montage. Keine Patentdatensätze (Suche zu Anmelder Kappelrodeck). CRM: `crm_abgleich.py "Caltest Instruments GmbH" "Caltest"`: neu.
- Korrekturen: Toms "kein Fertiger" ist nicht gesichert; Feld 8: zugekaufte Leistungselektronik zählt nach Endprodukt-Regel (A, Mittel bis Hoch), nur die Fertigungsfrage bleibt offen. Das senkt nicht auf Zeile 6.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Werden Leistungsquellen/Prüfsysteme in Kappelrodeck entwickelt UND gebaut oder nur Partnerprodukte vertrieben und Racks integriert? Wo nachsehen: caltest.de Produktseiten (eigene Marke? "Made in"), Impressum, Karriereseite (Stellen Montage/Test/Fertigung), BSFZ-Pressemeldung (Mesago/power-and-beyond) im Volltext. Bei reinem Vertrieb Rot nach E2 mit Quelle.
- Zitat im Browser bestätigt: nein. Nicht verwendbare Aussagen: Fertigung Kappelrodeck (S/?); Verguss (A); "manufacturer" (S, ProvenExpert, Widerspruch). Stichprobe für Jey: ja (Händler-/Hersteller-Widerspruch, Verguss könnte Hoch sein).

## 96. Camtek Germany GmbH | B1.510
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Verzeichnisse (a-leads, craft.co, S) nennen "Camtek Germany GmbH, Liebigstr. 6, 85551 Kirchheim b. München"; craft.co beschreibt Wartung, Applikationssupport, Training (S). Das deutet auf Vertrieb/Service der israelischen Camtek Ltd; die Fertigung der Anlagen liegt nicht in Kirchheim (nicht belegt). Verguss Niedrig (Inspektionsanlagen).
- Eigene Prüfung: Identität gegenüber Toms Befund verbessert (Adresse in zwei Verzeichnissen, S); Rechtsträger/Register weiter ungelesen. Gleichnamige Camtek GmbH Weinstadt (CAD/CAM) ist eine andere Firma. FRT Bergisch Gladbach (Camtek-Sparte) ist eine andere Einheit, deren Fertigungsumfang ungeklärt ist. CRM: `crm_abgleich.py "Camtek Germany GmbH" "Camtek" "FRT"`: neu.
- Korrekturen an Toms Feldern: Feld 4/17: Kirchheim-Adresse ist durch Suche (S) bestätigt, Tom fand sie nicht. Toms Fertigung Niedrig bleibt (S).
- Nachrecherche-Auftrag (Gelb, Zeile 7): Ist die Kirchheimer Einheit reine Vertriebs-/Serviceniederlassung (dann Rot nach E2/E3 mit Quelle) oder gibt es Montage/Fertigung (FRT Bergisch Gladbach getrennt bewerten)? Wo nachsehen: camtek.com Standortseite/Impressum, Handelsregister München (Camtek Germany GmbH), Stellenanzeigen Kirchheim.
- Zitat im Browser bestätigt: nein. Nicht verwendbare Aussagen: Rolle Vertrieb/Service (S/A); Fertigungsort (S/?). Stichprobe für Jey: nein.

## 97. Catalonia Trade & Investment | C2.119
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Büro Berlin der katalanischen Agentur ACCIÓ (S): "International Office in Berlin opened in 1990", Zuständigkeit DACH, Team mit acht Beratern (accio.gencat.cat, Snippet). Keine Fertigung, kein Produkt. Rot-Kandidat E2 (Beratung/Förderagentur), nicht mit V gelesen.
- Eigene Prüfung: SEMI-Verzeichnis nennt Friedrichstraße 185, 10117 Berlin (S), PLZ deckt sich mit der Messeliste. CRM: `crm_abgleich.py "Catalonia Trade & Investment" "ACCIO" "Generalitat de Catalunya"`: neu.
- Korrekturen: keine. Patent: keine eigene Suche (Agentur ohne Produkt, Feld 9 formal offen).
- Nachrecherche-Auftrag (Gelb, Zeile 7): E2 mit Stufe V belegen: Stuttgart-/Berlin-Seite von accio.gencat.cat im Browser lesen (Beratung/Förderung ohne eigene Produkte). Dabei prüfen, ob die Firma als Organisator eines Gemeinschaftsstandes auftritt (katalanische Aussteller wären Einzelfirmen, nicht Teil dieses Auftrags). Bei Bestätigung Rot nach E2.
- Zitat im Browser bestätigt: nein. Nicht verwendbare Aussagen: keine Fertigung (S); Rechtsträger (S). Stichprobe für Jey: nein.

## 98. Cathedy GmbH | A5.200
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Hinweis auf Fertigung im Ausland).** Externe AC/DC-Netzteile (Wand- und Tischnetzteile bis 330 W): Verguss Hoch (A, Netzteile). Fertigung in DE nicht belegt; die Firma selbst nennt "Produktionsstätten in Shenzhen" (eBay, S).
- Eigene Prüfung: eBay-Impressumsdaten (S): Gutenbergring 54, 22848 Norderstedt, HRB 136694 "Amtsgericht Hamburg", Geschäftsführer Weidong Su; eigene Website/Impressum nicht gefunden. Global-Sources-Profile nennen "Shenzhen Cathedy Technology Co. Ltd." mit 6.000-m²-Fabrik (2016/2018, S); Verbindung zur GmbH nicht belegt. Eine Ausgabe von Tom (Adresse Norderstedt, Register Hamburg) wird bestätigt; Tom kannte die Straße noch nicht. Ob das Registergericht zum Sitz passt, ist ungeprüft (nicht von mir bewertet). Patente/Gebrauchsmuster: eigene Suche, kein Treffer. Datenblatt/Vergussbauweise: nicht auffindbar (eBay-Listings ohne Angabe). CRM: `crm_abgleich.py "Cathedy GmbH" "Cathedy"`: neu.
- Korrekturen: Feld 17 ergänzt um Adresse und Geschäftsführer (S). Tom: Einstufung "unwahrscheinlich" folgt der Skala (Fertigung Niedrig), wird nicht geändert. E3 nicht mit V belegt, daher nicht Rot.
- Nachrecherche-Auftrag (Gelb, Zeile 5): Wird in Norderstedt gefertigt/montiert/vergossen oder nur importiert (Fertigung in Shenzhen)? Wo nachsehen: Firmenimpressum/Website (Domain suchen, Shop-Impressum auf ebay.de im Browser lesen), Handelsregister (Registergericht, Gegenstand der Gesellschaft), Stellenanzeigen Norderstedt, Produktetikett "Made in". Bei Bestätigung der Importrolle Rot nach E3/E2.
- Zitat im Browser bestätigt: nein. Nicht verwendbare Aussagen: Fertigung Shenzhen und Norderstedt (S); Verguss der Netzteile (A); Verbindung zur Shenzhen-Firma (?). Stichprobe für Jey: ja (Verguss Hoch gegen Fertigung im Ausland; Rot-Kandidat).

## 99. CCI Eurolam GmbH | A1.563
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** Distributor für Leiterplatten-Basismaterial (Isola, Arlon, Doosan, Rogers laut PCD&F/Evertiq, S), Standorte Dreieich und Düren, Hauptsitz Frankreich (S). Fertigung nicht belegt, Verguss Niedrig. E2 (Händler) stark wahrscheinlich, aber nicht V.
- Eigene Prüfung: Tom vermutete Chang Chun Group als Mutter (E1-Umfeld). Meine Suchen finden diese Verbindung nicht; sie nennen eine "CCI Eurolam Group, French-headquartered distributor" (Alain Kahn, president), Übernahme von Adeon Technologies BV (NL). Ich werte die Chang-Chun-Hypothese als nicht belegt. CRM: `crm_abgleich.py "CCI Eurolam GmbH" "CCI Eurolam" "Chang Chun" "CCI Group"`: neu. Konzernabgleich M: Gruppe mit Frankreich-Sitz (S), kein CRM-Konzernbezug.
- Korrekturen an Toms Feldern: Feld 13/17: Gruppenzugehörigkeit = französische CCI Eurolam Group (S, Presse 2007 bis 2021), nicht Chang Chun. Toms Hinweis auf Epoxid-Materialhersteller (E1) entfällt als Hypothese.
- Nachrecherche-Auftrag (Gelb, Zeile 7): E2 mit V belegen: Impressum/Standortseite der CCI Eurolam GmbH (Dreieich, Düren) lesen (Handel ohne Eigenfertigung? Ausnahme: PCB-Service/Equipment-Montage durch Adeon in NL, Fertigung dort?). Wo nachsehen: cci-eurolam Website (Domain suchen), Handelsregister Offenbach/Darmstadt, Stellenanzeigen Dreieich/Düren.
- Zitat im Browser bestätigt: nein. Nicht verwendbare Aussagen: Distributorrolle (S, überwiegend 2007 bis 2021, veraltet); Mutter Chang Chun (nicht belegt). Stichprobe für Jey: ja (Konzernhypothese korrigiert).

## 100. CCI Europe GmbH | C4.240
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 2, Identität nicht belegt).** Eine Firma "CCI Europe GmbH" in 32760 Detmold ist durch meine Suchen nicht auffindbar (zwei Suchen: Exaktname + Detmold; mit Chang Chun/electronica). Treffer waren nur die IHK Lippe zu Detmold ("CCI" = Chamber of Commerce and Industry), "CCI Manufacturing Germany GmbH" (DQS, Kühl-/Bremsflüssigkeit, Ort nicht angegeben, nicht zuzuordnen) und Fremdfirmen.
- Eigene Prüfung: Der Name "CCI" wird von der französischen CCI Eurolam Group für europäische Einheiten genutzt (S), aber ein Bezug zu "CCI Europe" ist nicht belegt (Inferenz, nicht verwenden). CRM: `crm_abgleich.py "CCI Europe GmbH" "CCI Europe" "Chang Chun Group"`: neu. Keine eigene Patentsuche möglich ohne Identität.
- Korrekturen: keine am Befund; Toms Hypothese Chang Chun bleibt unbelegt. Zwei Alternativen für die Klärung: (a) Aussteller ist Vertriebseinheit der Chang Chun Group (dann E1 möglich), (b) Einheit der französischen CCI Eurolam Group (dann E2). Keine ist belegt.
- Nachrecherche-Auftrag (Gelb, Zeile 2): Wer ist der Aussteller (Rechtsform, Gruppe, Produkt, Sitz Detmold)? Wo nachsehen: electronica-Ausstellerprofil "CCI Europe GmbH" im Browser (Produktgruppen, Website), Handelsregister Lemgo/Detmold, Website-Impressum. Bei Bestätigung Materialhersteller: Rot nach E1; bei Handel: E2.
- Zitat im Browser bestätigt: nein. Nicht verwendbare Aussagen: Alles zur Firma (Sitz, Produkt, Gruppe: ?). Stichprobe für Jey: ja (Identität offen).

## 101. C.C.P. Kontakt GmbH | B1.221
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 5, Hinweis auf Konzern mit Fertigung im Ausland).** Deutsche Tochter der taiwanischen C.C.P. Contact Probes Co., Ltd. (börsennotiert TW 6217, gegründet 1986; Silicon Saxony, CCP-Präsentation, S). Fertigung in Langen nicht belegt, Konzern: V nötig. Verguss Mittel: CCP-Präsentationen nennen wasserdichte Pogo-Pin-Steckverbinder per Insert-Molding, Glue-Sealing (IPX7) und O-Ring (IPX8) (S, Konzernprodukt, Fertigungsort unbekannt).
- Eigene Prüfung: Suche nach Stellenanzeigen/Produktion Langen: keine Treffer für CCP (S). Die Präsentation von 2023 nennt einen europäischen Standort in Frankfurt (S), nicht dieselbe Adresse. CRM: `crm_abgleich.py "C.C.P. Kontakt GmbH" "CCP Contact Probes" "CCP"`: neu. Patent: eigene Suche (waterproof/sealing/potting): kein CCP-Patent zu Verguss/Dichtung, Hochstromstift-Patent M453149 (Taiwan, nicht relevant, S).
- Korrekturen an Toms Feldern: Feld 8: Verguss Mittel, jetzt mit konkreterem Hinweis (Klebe-/Insert-Molding-Dichtung bei wasserdichten Steckern, S), Quelle: CCP_Contact_Probes_Company_Presentation_20231016. Feld 7 bleibt Niedrig (S).
- Nachrecherche-Auftrag (Gelb, Zeile 5): Werden in Langen Sockel/Stecker montiert, abgedichtet oder vergossen, oder ist es reiner Vertrieb/Applikation? Wo nachsehen: ccpcontactprobes.com Standortseite "Germany", Impressum der C.C.P. Kontakt GmbH, Handelsregister Offenbach, Stellenanzeigen Langen. Bei reinem Vertrieb Rot nach E2/E3 mit Quelle.
- Zitat im Browser bestätigt: nein. Nicht verwendbare Aussagen: Fertigung Langen (S/?); wasserdichte Steckverbinder als Produkt der Tochter (S, nur Konzern); Frankfurt-Standort (S). Stichprobe für Jey: ja.

## 102. CEFEG GmbH Federn- und Verbindungstechnik Chemnitz | B2.428
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 6).** Fertigung Chemnitz Hoch (A, Sitzregel: Winklhoferstraße 3, 09116 Chemnitz, 8.000 m² Produktion, IATF 16949, rund 110 bis 125 Beschäftigte, kein Konzern erkennbar, alles S). Verguss: Federn und Stanzbiegeteile Niedrig; "Baugruppen" nicht näher beschrieben.
- Eigene Prüfung: Wirtschaftsforum-Interview nennt Konstruktion, Werkzeugbau und Fertigungstechnik; Produktliste: Flachfedern, Stanzteile, Biegeteile, Baugruppen, Kunden Automotive, Maschinenbau, Elektrotechnik (S). Kein Hinweis auf Umspritzen/Kleben/Dichten. Geschäftsführung Dr. Denise Klinger (S). Patente: zwei eigene Suchen (Anmelder Gebrauchsmuster; Google-Patents-Anmelder): kein Patent mit CEFEG als Anmelder (nur Matratzen-/Rohrverbindungsfedern anderer Anmelder). CRM: `crm_abgleich.py "CEFEG GmbH Federn- und Verbindungstechnik Chemnitz" "CEFEG"`: neu.
- Korrekturen an Toms Feldern: INKONSISTENZ in Feld 8: Kopfwert "Niedrig", aber Einzelbewertung "elektrische Kontaktbaugruppen Mittel (A, nur falls Isolierteile/Verkleben dabei, nicht belegt)". Nach Bauteil-Regel zählt das Maximum; ein Mittel ohne Produktbeleg ist aber Stufe ?, zählt nicht. Ich werte Verguss als Niedrig (alle belegbaren Bauteile) und setze Zeile 6. Sollte die Nachrecherche Elektronik-/Sensorbaugruppen mit Kleben/Dichten belegen, wird es Grün (Zeile 4). Mitarbeiterzahl 26 (bouncewatch) ist veraltet, ignoriert.
- Nachrecherche-Auftrag (Gelb, Zeile 6): Welche Baugruppen (Elektronik/Sensor/Medizintechnik, Steckverbinder-Kontakte) fertigt CEFEG, und enthalten sie Kleb-, Dicht-, Umspritz- oder Vergussschritte (auch zugekaufte, verbaute Teile)? Wo nachsehen: cefeg.de Produktseite "Baugruppen", Kundenbranchen, Stellenanzeigen Montage/Baugruppenfertigung Chemnitz, Impressum (Sitz = Fertigungsort, V).
- Zitat im Browser bestätigt: nein. Nicht verwendbare Aussagen: Fertigung Chemnitz (A/S); Verguss aller Bauteile (A); Mitarbeiterzahl (S, zwei abweichende). Stichprobe für Jey: ja (Inkonsistenz Toms; Grenzfall Zeile 4 oder 6).

## 103. CELUS GmbH | C5.558
**ohne Browser/Web-Abruf geprüft, vorläufig. Ampel: GELB (Tabellenzeile 7).** KI-Software für Elektronikdesign (CUBOs, Series A 2022, S); keine Fertigung. Rot-Kandidat E2 (Software), noch nicht mit V gelesen.
- Eigene Prüfung: Impressum-Seite celus.io/legal/imprint laut Suchtreffer (S): CELUS GmbH, Ridlerstr. 57, 80339 München, HRB 254386 Amtsgericht München, Geschäftsführer Alexander und Tobias Pohl; ergänzt Toms Feld 17 (Tom las Register nicht). CRM: `crm_abgleich.py "CELUS GmbH" "Contunity" "Celus"`: neu. Nahtreffer "CEUS [DE]" und "Ceus UG [DE]" (bekannte_firmen_DE-AT-NL.txt Zeilen 399, 400, Ähnlichkeit 0,89) sind anderer Name (ohne L): nicht dieselbe Firma, neu bestätigt.
- Korrekturen: keine am Befund; Feld 12 ergänzt (Sichtprüfung erledigt).
- Nachrecherche-Auftrag (Gelb, Zeile 7): E2 mit V belegen: celus.io/about und /legal/imprint im Browser lesen (reine Software/Plattform, keine Hardware-Eigenprodukte). Bei Bestätigung Rot nach E2.
- Zitat im Browser bestätigt: nein. Nicht verwendbare Aussagen: Software-Rolle (S); Register/Impressum (S, Snippet). Stichprobe für Jey: nein.

---

## Konsistenz und Auffälligkeiten
- Toms Stufen sind durchgängig korrekt niedrig angesetzt (keine V-Aussage vorgetäuscht, Einschränkungen offen genannt). Seine Fehlerquellen sind inhaltlich: CEFEG Feld 8 (Kopfwert Niedrig gegen Einzelwert Mittel), CCI Eurolam (Chang-Chun-Hypothese in Feld 13/17 ohne Beleg, meine Suche weist auf französische Gruppe), Camtek Kirchheim (Adresse fand er nicht).
- Keine Firma ist Grün: Die Ausstellerfirmen mit denkbarem Verguss (Cathedy, CCP, Caltest) haben keinen Fertigungsbeleg in DE; CEFEG hat Fertigung, aber keinen belegten Vergussbezug.
- Vorschlag Fehlerlog (Jey gibt frei, nicht eingetragen): (1) Gruppenhypothesen aus Namensähnlichkeit ("CCI" = Chang Chun?) nie in Feld 13/17 als Fakt führen (CCI Eurolam). (2) Kopfwert Feld 8 und Einzelbewertung müssen übereinstimmen (CEFEG).
- Priorität für die Nachrecherche-Schleife (P) nach Nutzen: 1 Cathedy, 2 CCP Kontakt, 3 CEFEG, 4 Caltest; Rot-Bestätigung (E2/E3): Calterah, Camtek, Catalonia, CCI Eurolam, CELUS; CCI Europe zuerst Identität.

## Einschränkungen
- Browser und WebFetch nicht verfügbar: kein Gegenlesen nach Abschnitt H, kein Impressum, Datenblatt oder Ausstellerprofil gelesen; alle Aussagen Stufe S oder A. Keine "Zitat im Browser bestätigt: ja".
- WebSearch: 24 Abfragen verbraucht (Identität/Fertigung zu Cathedy 3, CCI Europe 2, CCI Eurolam 2, Camtek 2, CEFEG 3, Caltest 3, CCP 3, Calterah 2, CELUS 1, Catalonia 1; Patent-Zusatz: Cathedy, CCP, CEFEG, Caltest, siehe oben). Ergebnisse sind Kurzfassungen der Suche; Abrufe nicht als Seitentext gesichert.
- Patente (F5): Pflichtsuche mit Direktabfrage der Datenbanken nicht erfüllt (alle 10 Firmen); Rechtsstände entfallen mangels Treffer. Anmeldervarianten (Konzern, Vorgänger) nur teilweise mitgesucht.
- Wettbewerbereinsatz (F6): nur Abgleich mit wettbewerber_referenzen.md (kein Treffer) und Toms Messe-Signal; keine Einzelsuche mit Wettbewerbernamen.
- Handels-/Unternehmensregister nicht abgerufen. Kundendatenbank (Excel) nicht lesbar; kundendatenbank_export.txt ohne Treffer, daher keine "Verifiziert am"-Prüfung.
- Nichts verschickt, keine Datenbankfelder geändert, nichts committet. Größe/Umsatz und Kontakte nicht geprüft (Regeln D, K).
