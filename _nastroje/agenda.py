#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════
  AGENDA AS — denné záznamy firmy → denné, týždenné a mesačné raporty
═══════════════════════════════════════════════════════════════════════
PREČO: Luk každý deň diktuje, čo firma Isokor - Skandinavia AS kúpila,
predala a urobila. Agent to zapisuje sem a robí z toho raporty, aby
Luk videl, ako firma ide (cieľ 40–50 tis. NOK čistého mesačne), a aby
marketing stál na číslach, nie na pocite.

JEDEN ZDROJ PRAVDY PRE KAŽDÚ VEC (nič sa nezapisuje dvakrát):
    výdavky, príjmy e-shop/obchod/služby, aktivity → 02_PRACA/agenda_as/zaznamy/RRRR-MM.json
    faktúry (príjem)                              → 02_PRACA/faktury/data/  (číta sa odtiaľ)
    jazdy (km)                                    → 02_PRACA/kjorebok/jazdy/ (číta sa odtiaľ)

POUŽITIE:
    python3 _nastroje/agenda.py den 2026-11-12        # denný raport
    python3 _nastroje/agenda.py tyzden 2026-11-12     # ISO týždeň, v ktorom je dátum
    python3 _nastroje/agenda.py mesiac 2026-11        # mesačný raport
    python3 _nastroje/agenda.py termin 2026-11-12     # MVA termín (2 mesiace), v ktorom je dátum
    python3 _nastroje/agenda.py prehlad               # priebežná rozvaha od 6. 11. 2026 po dnes + aktuálny termín
    python3 _nastroje/agenda.py kontrola 2026-11      # skontroluje záznamy mesiaca
    (bez dátumu = dnes / tento týždeň / tento mesiac)

ZÁZNAM (v zaznamy/RRRR-MM.json → {"zaznamy": [...]}):
    {"datum": "2026-11-12", "typ": "vydavok",            # vydavok / prijem / aktivita
     "suma": 1249.00, "mva": 25,                         # suma VRÁTANE MVA (ako na bločku); mva v %
     "kategoria": "naradie",                             # výdavok: z nastavenie.json
     "kanal": "obchod",                                  # príjem: eshop / obchod / sluzby / ine
     "druh": "marketing",                                # aktivita: marketing / predaj / stretnutie / ...
     "kto": "Jula Arendal", "popis": "Vysávač na dielňu",
     "platba": "firemna_karta",                          # sukromne = firma dlhuje Lukovi
     "doklad": true,                                     # Luk má papierový bloček/faktúru (odovzdá Anne Sofie); false = chýba
     "zdroj": "diktovane",                               # alebo "shopify:#1031" (proti duplicitám)
     "poznamka": ""}
"""
import importlib.util, json, sys
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KOREN = ROOT / "02_PRACA" / "agenda_as"
FAKTURY = ROOT / "02_PRACA" / "faktury"
KJOREBOK = ROOT / "02_PRACA" / "kjorebok" / "jazdy"
DNI = ["pondelok", "utorok", "streda", "štvrtok", "piatok", "sobota", "nedeľa"]


# ───────────────────────── pomocné
def kr(x):
    x = round(x + 0.0, 2)
    s = f"{abs(x):,.2f}".replace(",", " ").replace(".", ",")
    if s.endswith(",00"):
        s = s[:-3]
    return ("−" if x < 0 else "") + s


def dt(d):
    return f"{d.day}. {d.month}. {d.year}"


def rozdiel(teraz, predtym):
    if not predtym:
        return "—"
    p = (teraz - predtym) / abs(predtym) * 100
    return f"{'+' if p >= 0 else ''}{p:.0f} %"


def nast():
    return json.loads((KOREN / "nastavenie.json").read_text(encoding="utf-8"))


def mesiace_v(od, do):
    m = date(od.year, od.month, 1)
    while m <= do:
        yield f"{m.year}-{m.month:02d}"
        m = date(m.year + (m.month == 12), m.month % 12 + 1, 1)


# ───────────────────────── načítanie dát
def zaznamy(od, do):
    out = []
    for m in mesiace_v(od, do):
        p = KOREN / "zaznamy" / f"{m}.json"
        if p.exists():
            for z in json.loads(p.read_text(encoding="utf-8")).get("zaznamy", []):
                if od <= date.fromisoformat(z["datum"]) <= do:
                    out.append(z)
    return sorted(out, key=lambda z: z["datum"])


def faktury(od, do):
    if not (FAKTURY / "data").exists():
        return []
    spec = importlib.util.spec_from_file_location("faktura", ROOT / "_nastroje" / "faktura.py")
    fm = importlib.util.module_from_spec(spec); spec.loader.exec_module(fm)
    n = fm.nacitaj_nastavenie()
    out = []
    for c in fm.vsetky_cisla():
        f = fm.nacitaj(c); fm.prepocitaj(f, n)
        f["_d"] = date.fromisoformat(f["fakturadato"])
        if od <= f["_d"] <= do:
            out.append(f)
    return out


def nezaplatene_faktury():
    return [f for f in faktury(date(2000, 1, 1), date(2100, 1, 1)) if f.get("stav", "vystavená") != "zaplatená"]


def jazdy(od, do):
    out = []
    for m in mesiace_v(od, do):
        p = KJOREBOK / f"{m}.json"
        if p.exists():
            for j in json.loads(p.read_text(encoding="utf-8")).get("jazdy", []):
                if od <= date.fromisoformat(j["dato"]) <= do:
                    out.append(j)
    return out


# ───────────────────────── výpočty
def mva_plati(d, n):
    od = n.get("mva_registrovana_od")
    return od is None or d >= date.fromisoformat(od)


def rozloz(z, n):
    """brutto → (netto, mva) so zohľadnením dátumu registrácie MVA"""
    b = float(z["suma"])
    sadzba = float(z.get("mva", 0)) if mva_plati(date.fromisoformat(z["datum"]), n) else 0
    netto = round(b / (1 + sadzba / 100), 2)
    return netto, round(b - netto, 2)


def spocitaj(od, do, n):
    zz, ff, jj = zaznamy(od, do), faktury(od, do), jazdy(od, do)
    r = {"prijmy": defaultdict(lambda: [0.0, 0.0, 0.0, 0]),   # kanál → brutto, netto, mva, počet
         "vydavky": defaultdict(lambda: [0.0, 0.0, 0.0, 0]),
         "aktivity": [], "bez_dokladu": [], "sukromne": [], "zz": zz, "ff": ff, "jj": jj}
    for z in zz:
        if z["typ"] == "aktivita":
            r["aktivity"].append(z); continue
        net, mva = rozloz(z, n)
        kluc = z.get("kanal", "ine") if z["typ"] == "prijem" else z.get("kategoria", "ine")
        tab = r["prijmy"] if z["typ"] == "prijem" else r["vydavky"]
        v = tab[kluc]; v[0] += float(z["suma"]); v[1] += net; v[2] += mva; v[3] += 1
        if z["typ"] == "vydavok":
            if not z.get("doklad"):
                r["bez_dokladu"].append(z)
            if z.get("platba") == "sukromne":
                r["sukromne"].append(z)
    for f in ff:
        v = r["prijmy"]["faktura"]
        v[0] += f["spolu"]; v[1] += f["netto"]; v[2] += f["mva_spolu"]; v[3] += 1
    r["prijem_netto"] = sum(v[1] for v in r["prijmy"].values())
    r["prijem_brutto"] = sum(v[0] for v in r["prijmy"].values())
    r["vydavok_netto"] = sum(v[1] for v in r["vydavky"].values())
    r["mva_von"] = sum(v[2] for v in r["prijmy"].values())
    r["mva_dnu"] = sum(v[2] for v in r["vydavky"].values())
    r["vysledok"] = r["prijem_netto"] - r["vydavok_netto"]
    r["km"] = sum(j.get("km") or 0 for j in jj)
    r["km_chyba"] = sum(1 for j in jj if not j.get("km"))
    return r


# ───────────────────────── raport
def raport(druh, od, do, pred_od, pred_do, nazov, subor):
    n = nast()
    r, p = spocitaj(od, do, n), spocitaj(pred_od, pred_do, n)
    kan, kat = n["kanaly_prijmov"], n["kategorie_vydavkov"]
    L = [f"# {nazov}", "", f"*{n['firma']} · {dt(od)}" + (f" – {dt(do)}" if od != do else "")
         + f" · vygenerované {dt(date.today())} · sumy v NOK*", ""]

    L += ["## Prehľad", "", "| | Toto obdobie | Predchádzajúce | Zmena |", "|---|---:|---:|---:|",
          f"| Príjmy bez MVA | {kr(r['prijem_netto'])} | {kr(p['prijem_netto'])} | {rozdiel(r['prijem_netto'], p['prijem_netto'])} |",
          f"| Výdavky bez MVA | {kr(r['vydavok_netto'])} | {kr(p['vydavok_netto'])} | {rozdiel(r['vydavok_netto'], p['vydavok_netto'])} |",
          f"| **Výsledok** | **{kr(r['vysledok'])}** | {kr(p['vysledok'])} | {rozdiel(r['vysledok'], p['vysledok'])} |",
          f"| MVA na odvod (výstup − vstup) | {kr(r['mva_von'] - r['mva_dnu'])} | {kr(p['mva_von'] - p['mva_dnu'])} | |",
          f"| Najazdené km | {r['km']}" + (f" (jazdy bez km: {r['km_chyba']})" if r["km_chyba"] else "") + f" | {p['km']} | |", ""]

    if druh == "prehlad":
        L[4:14] = ["## Rozvaha od začiatku", "", "| | Spolu |", "|---|---:|",
                   f"| Príjmy bez MVA | {kr(r['prijem_netto'])} |", f"| Výdavky bez MVA | {kr(r['vydavok_netto'])} |",
                   f"| **Výsledok** | **{kr(r['vysledok'])}** |",
                   f"| MVA vybraná (výstup) | {kr(r['mva_von'])} |", f"| MVA zaplatená (vstup, odpočet) | {kr(r['mva_dnu'])} |",
                   f"| MVA na odvod | {kr(r['mva_von'] - r['mva_dnu'])} |", f"| Najazdené km | {r['km']} |", ""]
        dni = (do - od).days + 1
        L += [f"Priemer na mesiac (30 dní): výsledok **{kr(r['vysledok'] / dni * 30)}** · cieľ {kr(n['ciel_mesacne_cisty'][0])}–{kr(n['ciel_mesacne_cisty'][1])}.", ""]
    if druh == "termin":
        L += ["*MVA termín: tieto čísla sú podklad pre Anne Sofie — presné priznanie robí ona z papierových dokladov.*", ""]
    if druh == "mesiac":
        lo, hi = n["ciel_mesacne_cisty"]
        pct = r["vysledok"] / lo * 100 if lo else 0
        L += [f"**Cieľ {kr(lo)}–{kr(hi)} čistého mesačne:** výsledok {kr(r['vysledok'])} = **{pct:.0f} %** dolnej hranice. "
              "*(Výsledok firmy pred daňou a pred Lukovou mzdou — čo si z toho reálne vezme, rieši s účtovníčkou.)*", ""]

    L += ["## Príjmy podľa kanála", ""]
    if r["prijmy"]:
        L += ["| Kanál | Počet | S MVA | Bez MVA | MVA |", "|---|---:|---:|---:|---:|"]
        for k, v in sorted(r["prijmy"].items(), key=lambda x: -x[1][1]):
            L.append(f"| {kan.get(k, k)} | {v[3]} | {kr(v[0])} | {kr(v[1])} | {kr(v[2])} |")
    else:
        L.append("*Žiadne príjmy.*")
    L.append("")

    L += ["## Výdavky podľa kategórie", ""]
    if r["vydavky"]:
        L += ["| Kategória | Počet | S MVA | Bez MVA | MVA na odpočet |", "|---|---:|---:|---:|---:|"]
        for k, v in sorted(r["vydavky"].items(), key=lambda x: -x[1][1]):
            L.append(f"| {kat.get(k, {}).get('popis', k)} | {v[3]} | {kr(v[0])} | {kr(v[1])} | {kr(v[2])} |")
    else:
        L.append("*Žiadne výdavky.*")
    L.append("")

    # zoznam pohybov — pri dni a týždni celý, pri mesiaci top 10 výdavkov
    pohyby = [z for z in r["zz"] if z["typ"] != "aktivita"]
    if druh in ("mesiac", "termin", "prehlad"):
        vyd = sorted([z for z in pohyby if z["typ"] == "vydavok"], key=lambda z: -float(z["suma"]))[:10]
        if vyd:
            L += ["## 10 najväčších výdavkov", "", "| Dátum | Kto | Čo | Suma |", "|---|---|---|---:|"]
            L += [f"| {dt(date.fromisoformat(z['datum']))} | {z.get('kto', '')} | {z.get('popis', '')} | {kr(float(z['suma']))} |" for z in vyd]
            L.append("")
    elif pohyby or r["ff"]:
        L += ["## Pohyby", "", "| Dátum | Typ | Kto | Čo | Suma s MVA |", "|---|---|---|---|---:|"]
        for z in pohyby:
            znam = "+" if z["typ"] == "prijem" else "−"
            L.append(f"| {dt(date.fromisoformat(z['datum']))} | {'príjem' if znam == '+' else 'výdavok'} | {z.get('kto', '')} | {z.get('popis', '')} | {znam}{kr(float(z['suma']))} |")
        for f in r["ff"]:
            L.append(f"| {dt(f['_d'])} | faktúra {f['cislo']} | {f['kunde']['navn']} | {f.get('stav', 'vystavená')} | +{kr(f['spolu'])} |")
        L.append("")

    if r["jj"]:
        L += ["## Jazdy (z Kjørebok)", ""]
        L += [f"- {dt(date.fromisoformat(j['dato']))}: {j.get('til', '')} — {str(j['km']) + ' km' if j.get('km') else '**km chýba**'}" for j in r["jj"]]
        L.append("")

    L += ["## Aktivity (marketing, predaj, stretnutia)", ""]
    if r["aktivity"]:
        L += [f"- {dt(date.fromisoformat(a['datum']))} · **{a.get('druh', '')}** · {a.get('popis', '')}"
              + (f" — {a['kto']}" if a.get("kto") else "") + (f" *({a['poznamka']})*" if a.get("poznamka") else "")
              for a in r["aktivity"]]
    else:
        L.append("*Žiadne zapísané aktivity.*")
    L.append("")

    # čo treba riešiť
    pozor = []
    if r["bez_dokladu"]:
        pozor.append(f"**Výdavky bez papierového dokladu: {len(r['bez_dokladu'])}** — bez bločku/faktúry ich Anne Sofie neuzná: "
                     + "; ".join(f"{z['datum']} {z.get('kto', '')} {kr(float(z['suma']))}" for z in r["bez_dokladu"]))
    if r["sukromne"]:
        s = sum(float(z["suma"]) for z in r["sukromne"])
        pozor.append(f"**Zaplatené súkromne: {kr(s)}** — firma to dlhuje Lukovi (utlegg), treba preplatiť z firemného účtu.")
    nz = nezaplatene_faktury()
    po = [f for f in nz if date.fromisoformat(f["forfallsdato"]) < date.today()]
    if nz:
        pozor.append(f"Nezaplatené faktúry: {len(nz)} za {kr(sum(f['spolu'] for f in nz))}"
                     + (f", **po splatnosti: {', '.join(str(f['cislo']) for f in po)}**" if po else ""))
    if r["km_chyba"]:
        pozor.append(f"Jazdy bez km v Kjørebok: {r['km_chyba']}.")
    if n.get("mva_registrovana_od") is None:
        pozor.append("Chýba dátum registrácie MVA v `nastavenie.json` — MVA sa zatiaľ ráta pri všetkých záznamoch.")
    L += ["## Treba riešiť", ""] + ([f"- {x}" for x in pozor] or ["*Nič.*"]) + [""]

    subor.parent.mkdir(parents=True, exist_ok=True)
    subor.write_text("\n".join(L), encoding="utf-8")
    print("\n".join(L)); print(f"\n→ {subor.relative_to(ROOT)}")


# ───────────────────────── kontrola
def kontrola(mesiac):
    n = nast()
    p = KOREN / "zaznamy" / f"{mesiac}.json"
    zz = json.loads(p.read_text(encoding="utf-8")).get("zaznamy", []) if p.exists() else []
    chyby, zdroje = [], set()
    for i, z in enumerate(zz, 1):
        m = f"záznam {i} ({z.get('datum', '?')} {z.get('kto', '')})"
        if not str(z.get("datum", "")).startswith(mesiac):
            chyby.append(f"{m}: dátum nepatrí do {mesiac}")
        t = z.get("typ")
        if t not in ("vydavok", "prijem", "aktivita"):
            chyby.append(f"{m}: neznámy typ '{t}'"); continue
        if t != "aktivita":
            try:
                float(z["suma"])
            except Exception:
                chyby.append(f"{m}: suma chýba alebo nie je číslo")
        if t == "vydavok" and z.get("kategoria") not in n["kategorie_vydavkov"]:
            chyby.append(f"{m}: neznáma kategória '{z.get('kategoria')}'")
        if t == "prijem":
            if z.get("kanal") == "faktura":
                chyby.append(f"{m}: faktúry sem nepatria — počítajú sa z 02_PRACA/faktury")
            elif z.get("kanal") not in n["kanaly_prijmov"]:
                chyby.append(f"{m}: neznámy kanál '{z.get('kanal')}'")
        if t == "vydavok" and z.get("platba") and z["platba"] not in n["sposoby_platby"]:
            chyby.append(f"{m}: neznámy spôsob platby '{z['platba']}'")
        if t == "vydavok" and "doklad" not in z:
            chyby.append(f"{m}: chýba pole doklad (true = papier mám, false = nemám)")
        zd = z.get("zdroj", "")
        if zd and zd != "diktovane":
            if zd in zdroje:
                chyby.append(f"{m}: duplicita — zdroj {zd} je zapísaný dvakrát")
            zdroje.add(zd)
    print(f"{mesiac}: {len(zz)} záznamov — " + ("v poriadku" if not chyby else f"{len(chyby)} problémov"))
    for c in chyby:
        print("  ✗", c)
    return not chyby


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    druh, arg = sys.argv[1], (sys.argv[2] if len(sys.argv) > 2 else None)
    dnes = date.today()
    if druh == "kontrola":
        sys.exit(0 if kontrola(arg or dnes.strftime("%Y-%m")) else 2)
    if druh == "den":
        d = date.fromisoformat(arg) if arg else dnes
        raport("den", d, d, d - timedelta(days=7), d - timedelta(days=7),
               f"Denný raport — {DNI[d.weekday()]} {dt(d)}", KOREN / "reporty" / "den" / f"{d}.md")
        print("(porovnanie: rovnaký deň pred týždňom)")
    elif druh == "tyzden":
        d = date.fromisoformat(arg) if arg else dnes
        od = d - timedelta(days=d.weekday()); do = od + timedelta(days=6)
        y, w, _ = od.isocalendar()
        raport("tyzden", od, do, od - timedelta(days=7), do - timedelta(days=7),
               f"Týždenný raport — týždeň {w}/{y}", KOREN / "reporty" / "tyzden" / f"{y}-T{w:02d}.md")
    elif druh == "mesiac":
        y, m = map(int, (arg or dnes.strftime("%Y-%m")).split("-"))
        od = date(y, m, 1); do = date(y + (m == 12), m % 12 + 1, 1) - timedelta(days=1)
        pdo = od - timedelta(days=1); pod = date(pdo.year, pdo.month, 1)
        raport("mesiac", od, do, pod, pdo, f"Mesačný raport — {m:02d}/{y}",
               KOREN / "reporty" / "mesiac" / f"{y}-{m:02d}.md")
    elif druh == "termin":
        d = date.fromisoformat(arg) if arg else dnes
        od, do = termin_rozsah(d)
        pdo = od - timedelta(days=1); pod, _ = termin_rozsah(pdo)
        c = (od.month + 1) // 2
        raport("termin", od, do, pod, pdo, f"MVA termín {c}/{od.year} ({MES[od.month - 1]}–{MES[do.month - 1]})",
               KOREN / "reporty" / "termin" / f"{od.year}-T{c}.md")
    elif druh == "prehlad":
        od = date.fromisoformat(nast().get("agenda_od") or nast()["mva_registrovana_od"])
        do = date.fromisoformat(arg) if arg else dnes
        raport("prehlad", od, do, od, od - timedelta(days=1), f"Priebežná rozvaha k {dt(do)}",
               KOREN / "reporty" / "ROZVAHA.md")
        t_od, t_do = termin_rozsah(do)
        r = spocitaj(t_od, min(t_do, do), nast())
        print(f"\nAktuálny MVA termín {dt(t_od)} – {dt(t_do)}: zatiaľ na odvod {kr(r['mva_von'] - r['mva_dnu'])}")
    else:
        print(__doc__); sys.exit(1)


def termin_rozsah(d):
    """Nórske MVA termíny: jan–feb, mar–apr, máj–jún, júl–aug, sep–okt, nov–dec."""
    m1 = d.month - (d.month - 1) % 2
    od = date(d.year, m1, 1)
    do = date(d.year + (m1 + 2 > 12), (m1 + 1) % 12 + 1, 1) - timedelta(days=1)
    return od, do


MES = ["január", "február", "marec", "apríl", "máj", "jún", "júl", "august", "september", "október", "november", "december"]


if __name__ == "__main__":
    main()
