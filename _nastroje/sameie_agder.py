#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════
  SAMEIE + BORETTSLAG V AGDERI — zoznam z Enhetsregisteret (Brreg)
═══════════════════════════════════════════════════════════════════════
PREČO: B2B zmluvy na údržbu (fasády, hrdza, sklo, dlažba) pre sameie
a borettslag — `10_STUDIUM_MAJETOK/09_PREDAJNY_SYSTEM.md`. Zoznam je
verejný (Brønnøysundregistrene). Ukladajú sa LEN údaje o organizácii
(org. č., názov, adresa) — žiadne mená členov výboru.

DVA SPÔSOBY:
  1) priamo z API (treba sieťový prístup k data.brreg.no):
       python3 _nastroje/sameie_agder.py api
  2) zo súboru, ktorý Luk stiahne z brreg.no a nahrá do _inbox/ (CSV/XLSX):
       python3 _nastroje/sameie_agder.py subor _inbox/enheter.xlsx

VÝSTUP: 02_PRACA/b2b_sameie/zoznam.csv + ZOZNAM.md (zoradené podľa
priority regiónu: najbližšie k Vegårshei najprv).
"""
import csv, json, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VYSTUP = ROOT / "02_PRACA" / "b2b_sameie"
FORMY = {"BRL": "borettslag", "ESEK": "eierseksjonssameie"}

# Agder (fylke 42). Priorita 1 = do ~45 min od Vegårshei, 2 = do ~1,5 h, 3 = ďalej.
KOMUNY = {
    "4212": ("Vegårshei", 1), "4213": ("Tvedestrand", 1), "4203": ("Arendal", 1),
    "4211": ("Gjerstad", 1), "4201": ("Risør", 1), "4214": ("Froland", 1), "4217": ("Åmli", 1),
    "4202": ("Grimstad", 2), "4215": ("Lillesand", 2), "4216": ("Birkenes", 2),
    "4204": ("Kristiansand", 2), "4223": ("Vennesla", 2), "4218": ("Iveland", 2),
    "4219": ("Evje og Hornnes", 3), "4220": ("Bygland", 3), "4221": ("Valle", 3), "4222": ("Bykle", 3),
    "4224": ("Åseral", 3), "4205": ("Lindesnes", 3), "4225": ("Lyngdal", 3), "4226": ("Hægebostad", 3),
    "4227": ("Kvinesdal", 3), "4206": ("Farsund", 3), "4207": ("Flekkefjord", 3), "4228": ("Sirdal", 3),
}
POLIA = ["priorita", "kommune", "orgnr", "navn", "forma", "adresse", "postnr", "poststed", "stiftet", "konkurs_avvikling"]


def riadok(orgnr, navn, kod, komnr, adresse, postnr, poststed, stiftet, problem=""):
    kom, prio = KOMUNY.get(str(komnr), (str(komnr), 9))
    return {"priorita": prio, "kommune": kom, "orgnr": str(orgnr), "navn": navn, "forma": FORMY.get(kod, kod),
            "adresse": adresse, "postnr": postnr, "poststed": poststed, "stiftet": stiftet, "konkurs_avvikling": problem}


def z_api():
    out = []
    for kod in FORMY:
        stranka = 0
        while True:
            url = ("https://data.brreg.no/enhetsregisteret/api/enheter?organisasjonsform=" + kod
                   + "&kommunenummer=" + ",".join(KOMUNY) + f"&size=200&page={stranka}")
            d = json.load(urllib.request.urlopen(url, timeout=30))
            for e in d.get("_embedded", {}).get("enheter", []):
                a = e.get("forretningsadresse") or e.get("postadresse") or {}
                prob = ", ".join(k for k in ("konkurs", "underAvvikling", "underTvangsavviklingEllerTvangsopplosning") if e.get(k))
                out.append(riadok(e["organisasjonsnummer"], e["navn"], kod, a.get("kommunenummer", ""),
                                  " ".join(a.get("adresse", [])), a.get("postnummer", ""), a.get("poststed", ""),
                                  e.get("stiftelsesdato", ""), prob))
            p = d.get("page", {})
            if p.get("number", 0) + 1 >= p.get("totalPages", 0):
                break
            stranka += 1
    return out


def z_suboru(cesta):
    cesta = Path(cesta)
    if cesta.suffix.lower() in (".xlsx", ".xls"):
        import openpyxl
        ws = openpyxl.load_workbook(cesta, read_only=True).active
        rows = list(ws.iter_rows(values_only=True))
        hlava, data = [str(h or "") for h in rows[0]], rows[1:]
        zaznamy = [dict(zip(hlava, r)) for r in data]
    else:
        with open(cesta, encoding="utf-8-sig") as f:
            vzor = f.read(4096); f.seek(0)
            zaznamy = list(csv.DictReader(f, delimiter=";" if vzor.count(";") > vzor.count(",") else ","))

    def pole(z, *mena):
        for k, v in z.items():
            kk = (k or "").lower().replace(" ", "").replace("_", ".")
            if any(kk == m or kk.endswith(m) for m in mena):
                return "" if v is None else str(v)
        return ""
    out = []
    for z in zaznamy:
        kod = pole(z, "organisasjonsform.kode", "organisasjonsformkode", "organisasjonsform")
        kod = next((k for k in FORMY if kod.upper().startswith(k)), kod)
        komnr = pole(z, "forretningsadresse.kommunenummer", "kommunenummer")
        if kod not in FORMY or komnr not in KOMUNY:
            continue
        out.append(riadok(pole(z, "organisasjonsnummer"), pole(z, "navn"), kod, komnr,
                          pole(z, "forretningsadresse.adresse", "adresse"), pole(z, "forretningsadresse.postnummer", "postnummer"),
                          pole(z, "forretningsadresse.poststed", "poststed"), pole(z, "stiftelsesdato")))
    return out


def uloz(rows):
    rows = sorted({r["orgnr"]: r for r in rows}.values(), key=lambda r: (r["priorita"], r["kommune"], r["navn"]))
    VYSTUP.mkdir(parents=True, exist_ok=True)
    with open(VYSTUP / "zoznam.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=POLIA, delimiter=";"); w.writeheader(); w.writerows(rows)
    L = ["# Sameie a borettslag v Agderi", "", f"*Zdroj: Enhetsregisteret (Brreg). Spolu {len(rows)}. "
         "Priorita 1 = do ~45 min od Vegårshei. Len údaje o organizácii, žiadne osobné údaje.*", ""]
    L += ["| Kommune | Priorita | Borettslag | Sameie | Spolu |", "|---|---:|---:|---:|---:|"]
    po = {}
    for r in rows:
        k = po.setdefault(r["kommune"], [r["priorita"], 0, 0]); k[1 if r["forma"] == "borettslag" else 2] += 1
    for kom, (p, b, s) in sorted(po.items(), key=lambda x: (x[1][0], -(x[1][1] + x[1][2]))):
        L.append(f"| {kom} | {p} | {b} | {s} | {b + s} |")
    L += ["", "## Priorita 1", "", "| Kommune | Názov | Forma | Adresa | Org. č. |", "|---|---|---|---|---|"]
    L += [f"| {r['kommune']} | {r['navn']} | {r['forma']} | {r['adresse']}, {r['postnr']} {r['poststed']} | {r['orgnr']} |"
          for r in rows if r["priorita"] == 1 and not r["konkurs_avvikling"]]
    (VYSTUP / "ZOZNAM.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"{len(rows)} záznamov → {VYSTUP.relative_to(ROOT)}/zoznam.csv + ZOZNAM.md")


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "api":
        uloz(z_api())
    elif len(sys.argv) >= 3 and sys.argv[1] == "subor":
        uloz(z_suboru(sys.argv[2]))
    else:
        print(__doc__); sys.exit(1)
