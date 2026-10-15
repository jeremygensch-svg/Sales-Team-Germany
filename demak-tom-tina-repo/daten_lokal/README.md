# daten_lokal (nicht im Repository)

Hier oder direkt im Projektstamm liegen lokal die CRM-Exporte. Sie sind per .gitignore ausgeschlossen:

- bekannte_firmen_DE-AT-NL.txt (eine Firma pro Zeile, Name in der ersten Spalte, Tab-getrennt)
- kundendatenbank_export.txt (Textexport der Kundendatenbank)

crm_abgleich.py findet sie in beiden Orten. Ohne diese Dateien meldet das Skript eine WARNUNG, und Tom/Tina dürfen keine Firma als "CRM: neu" einstufen.
