#!/usr/bin/env python3
"""Vollständigkeitsprüfung eines Tom- oder Tina-Batches (regeln_tom_tina.md Abschnitt S, nur Standardbibliothek).
Aufruf: python batch_check.py tom_batch_NN.md [--tina]
Erwartet pro Firma einen Block, der mit einer Überschrift (## ...) beginnt und nummerierte Felder "N. Label: ..." enthält."""
import re, sys
def blocks(text):
    parts = re.split(r"(?m)^#{2,3}\s+", text)
    out = []
    for p in parts[1:]:
        head, _, body = p.partition("\n")
        if re.search(r"(?m)^\s*1\.\s", body) and re.search(r"(?m)^\s*9\.\s", body):
            out.append((head.strip(), body))
    return out
def fields(body):
    f, cur = {}, None
    for line in body.split("\n"):
        m = re.match(r"^\s{0,2}(\d{1,2})\.\s+(.*)$", line)
        if m and 1 <= int(m.group(1)) <= 17 and (int(m.group(1)) == (cur or 0) + 1 or int(m.group(1)) in range(1, 18) and int(m.group(1)) not in f):
            cur = int(m.group(1)); f[cur] = m.group(2)
        elif cur: f[cur] += "\n" + line
    return f
def main(a):
    if not a: print(__doc__); return 2
    tina = "--tina" in a
    text = open(a[0], encoding="utf-8").read()
    bl = blocks(text)
    if not bl:
        print("UNVOLLSTÄNDIG: keine Firmenblöcke im Übergabeformat gefunden"); return 1
    problems = []
    for head, body in bl:
        f = fields(body); p = []
        need = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17] + ([11] if tina else [])
        for n in need:
            if n not in f or not f[n].strip(): p.append(f"Feld {n} fehlt oder leer")
        if 9 in f:
            t = f[9].lower()
            dbs = sum(1 for k in ("google patents", "espacenet", "depatis") if k in t)
            if dbs < 2: p.append("Feld 9: weniger als zwei Patent-Datenbanken genannt")
            if re.match(r"\s*(nicht geprüft|nicht gesucht|nicht recherchiert|offen)", t): p.append("Feld 9 beginnt mit 'nicht geprüft/gesucht'")
        if 16 in f and not re.search(r"(?i)such|hinweis|wevo|sonderhoff|delo|henkel|scheugenpflug|nordson|bdtronic|viscotec|dopag", f[16]):
            p.append("Feld 16: keine ausgeführten Suchen oder Treffer genannt")
        if 14 in f:
            if "http" not in f[14]: p.append("Feld 14: keine URL")
            if not re.search(r"[\"„“»]", f[14]): p.append("Feld 14: kein wörtliches Kurzzitat")
            if not re.search(r"20\d\d-\d\d-\d\d|\d\d\.\d\d\.20\d\d", f[14]): p.append("Feld 14: kein Abrufdatum")
        for n in (7, 8):
            if n in f and not re.search(r"(?i)\b(hoch|mittel|niedrig)\b", f[n]): p.append(f"Feld {n}: keine Stufe Hoch/Mittel/Niedrig")
            if n in f and re.search(r"\d\s*%", f[n]): p.append(f"Feld {n}: Prozentwert statt Stufe")
            if n in f and not re.search(r"\b[VASs?]\b|Stufe\s*[VAS?]", f[n]): p.append(f"Feld {n}: keine Belegstufe")
        if tina:
            if 11 in f and not re.search(r"(?i)gr[üu]n|gelb|rot", f[11]): p.append("Feld 11: keine Ampel")
            if 11 in f and re.search(r"(?i)gelb", f[11]) and 13 in f and len(f[13].strip()) < 15: p.append("Gelb ohne Nachrecherche-Auftrag")
            if re.search(r"(?i)gr[üu]n", f.get(11, "")) and not re.search(r"(?i)zitat.*best[aä]tigt", body): p.append("Grün ohne 'Zitat im Browser bestätigt'")
        if p: problems.append((head, p))
    print(f"{len(bl)} Firmenblöcke geprüft.")
    if not problems:
        print("VOLLSTÄNDIG"); return 0
    print("UNVOLLSTÄNDIG:")
    for head, p in problems:
        print(f"- {head[:70]}")
        for x in p: print(f"    * {x}")
    return 1
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
