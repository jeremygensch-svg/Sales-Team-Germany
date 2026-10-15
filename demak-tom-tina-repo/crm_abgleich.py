#!/usr/bin/env python3
"""CRM-Abgleich nach regeln_tom_tina.md Abschnitt B2 (nur Standardbibliothek).
Aufruf: python crm_abgleich.py "Firmenname" ["Konzernname" ...]
Gibt Treffer aus bekannte_firmen_DE-AT-NL.txt und kundendatenbank_export.txt mit Zeilennummer aus."""
import re, sys, os, unicodedata, difflib
HERE = os.path.dirname(os.path.abspath(__file__))
FILES = ["bekannte_firmen_DE-AT-NL.txt", "kundendatenbank_export.txt"]
LEGAL = [r"gmbh\s*&\s*co\.?\s*kg", r"gmbh\s*\+\s*co\.?\s*kg", r"gmbh", r"mbh", r"ag", r"kg", r"se", r"e\.?\s?k\.?", r"e\.?\s?g\.?",
         r"ug", r"s\.?\s?r\.?\s?l\.?", r"b\.?\s?v\.?", r"n\.?\s?v\.?", r"s\.?\s?r\.?\s?o\.?", r"inc\.?", r"ltd\.?", r"co\.?",
         r"group", r"gruppe", r"deutschland", r"germany", r"holding", r"international", r"&\s*co"]
def norm(s):
    s = unicodedata.normalize("NFKC", s).lower()
    s = re.sub(r"[​-‏⁠﻿]", "", s)
    s = s.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    s = re.sub(r"\[[^\]]*\]", " ", s)            # Ländercodes wie [DE]
    s = s.replace("&", " und ").replace("+", " und ")
    s = re.sub(r"\bund\b", " ", s)
    for l in LEGAL:
        s = re.sub(r"(?<![a-z0-9])" + l + r"(?![a-z0-9])", " ", s)
    s = re.sub(r"[\"'`´.,;:/\\\-_()|]", " ", s)
    return re.sub(r"\s+", " ", s).strip()
def load():
    rows = []
    for f in FILES:
        p = os.path.join(HERE, f)
        if not os.path.exists(p):
            p = os.path.join(HERE, "daten_lokal", f)  # alternativer Ablageort
        if not os.path.exists(p):
            print(f"WARNUNG: {f} nicht gefunden"); continue
        for i, line in enumerate(open(p, encoding="utf-8", errors="replace"), 1):
            t = line.rstrip("\n")
            if not t.strip() or t.lstrip().startswith("#"): continue
            name = t.split("\t")[0]
            rows.append((f, i, t.strip(), norm(name)))
    return rows
def main(args):
    if not args:
        print(__doc__); return 1
    rows = load()
    if not rows:
        print('FEHLER: keine CRM-Dateien gefunden. Kein Abgleich moeglich, CRM-Status darf NICHT als neu gelten.'); return 2
    for q in args:
        nq = norm(q)
        print(f"\n== {q}   (Kern-Name: '{nq}')")
        hits = []
        for f, i, raw, n in rows:
            if not n or not nq: continue
            score = difflib.SequenceMatcher(None, nq, n).ratio()
            first = n.split(" ")[0]
            if n == nq: kind = "IDENTISCH"
            elif len(nq) >= 5 and (n.startswith(nq) or nq.startswith(n) and len(n) >= 5): kind = "PRAEFIX"
            elif nq in re.sub(r"\s+", " ", " " + n + " ").strip() and len(nq) >= 5: kind = "ENTHALTEN"
            elif len(first) >= 5 and first == nq.split(" ")[0] : kind = "GLEICHE WORTWURZEL"
            elif score >= 0.88: kind = f"AEHNLICH {score:.2f}"
            else: continue
            hits.append((kind, f, i, raw[:110]))
        order = {"IDENTISCH": 0, "PRAEFIX": 1, "ENTHALTEN": 2, "GLEICHE WORTWURZEL": 3}
        hits.sort(key=lambda h: (order.get(h[0], 4), h[2]))
        if not hits:
            print("kein Treffer -> CRM-Status: neu")
        for kind, f, i, raw in hits[:25]:
            print(f"  {kind:20s} {f}:{i}: {raw}")
        if len(hits) > 25: print(f"  ... {len(hits)-25} weitere")
        if hits: print("-> Treffer manuell prüfen: gleicher Kern-Name an anderem Ort = unklar (Gelb, Einheit klären); identisch = BEKANNT")
    return 0
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
