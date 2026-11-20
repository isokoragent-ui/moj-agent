#!/usr/bin/env python3
"""Kalkulačka minimálnej hodinovej sadzby (ENK / živnosť, Nórsko).

Spätný výpočet: koľko čistého chcem mesačne → koľko zisku firmy treba
(po dani a trygdeavgift) → + náklady firmy → ÷ fakturované hodiny → + MVA.

Daňové sadzby: Nórsko 2025 (skatteetaten.no). Pre 2026 sa mierne líšia —
⚠️ pred použitím na ceny over aktuálne sadzby. Výsledok je odhad, nie
daňové poradenstvo.

Použitie:  python3 kalkulacka_hodinovka.py
Čísla na úpravu sú v sekcii NASTAVENIE.
"""

# ── NASTAVENIE (uprav podľa reality) ─────────────────────────────────────
CISTE_MESACNE = 50_000          # čo chcem mať čisté na účet mesačne (kr)
DOCHODOK_PERCENTO = 0.05        # ENK nemá OTP → sporenie na dôchodok z čistého

NAKLADY_FIRMY_ROCNE = {         # ⚠️ ODHADY — prepíš skutočnými číslami
    "auto (palivo, servis, poistenie, odpisy)": 80_000,
    "náradie, opravy, odpisy": 25_000,
    "poistenie zodpovednosti + úrazové": 10_000,
    "telefón, internet, softvér, web": 12_000,
    "účtovníčka": 15_000,
    "marketing (reklama, tlač)": 15_000,
    "pracovné oblečenie, ochranné pomôcky": 5_000,
    "sykepengeforsikring NAV (krytie od 1. dňa) ⚠️": 10_000,
}
REZERVA_NA_NECAKANE = 0.10      # +10 % k nákladom

TYZDNE_DOVOLENKA = 5
TYZDNE_SVIATKY = 2              # ~10 štátnych sviatkov
TYZDNE_CHOROBA = 1
HODIN_TYZDENNE = 40             # koľko reálne pracuješ (všetko spolu)

MVA = 0.25
# ─────────────────────────────────────────────────────────────────────────


def dan_enk_2025(zisk):
    """Daň + odvody z čistého zisku ENK (personinntekt = zisk), sadzby 2025."""
    trygd = 0.108 * zisk                              # trygdeavgift næring
    personfradrag = 108_550
    alminnelig = max(0, zisk - personfradrag) * 0.22  # daň z príjmu
    trinn = 0.0
    pasma = [(217_400, 306_050, 0.017), (306_050, 697_150, 0.040),
             (697_150, 942_400, 0.137), (942_400, 1_410_750, 0.167),
             (1_410_750, 10**12, 0.177)]
    for od, do, s in pasma:
        if zisk > od:
            trinn += (min(zisk, do) - od) * s
    return trygd + alminnelig + trinn


def potrebny_zisk(ciste_rocne):
    """Nájde zisk firmy, z ktorého po daniach ostane ciste_rocne."""
    lo, hi = 0, 5_000_000
    for _ in range(100):
        mid = (lo + hi) / 2
        if mid - dan_enk_2025(mid) < ciste_rocne:
            lo = mid
        else:
            hi = mid
    return hi


def main():
    ciste_rocne = CISTE_MESACNE * 12 / (1 - DOCHODOK_PERCENTO)
    zisk = potrebny_zisk(ciste_rocne)
    dane = dan_enk_2025(zisk)
    naklady = sum(NAKLADY_FIRMY_ROCNE.values()) * (1 + REZERVA_NA_NECAKANE)
    obrat = zisk + naklady
    tyzdne = 52 - TYZDNE_DOVOLENKA - TYZDNE_SVIATKY - TYZDNE_CHOROBA
    hodiny_spolu = tyzdne * HODIN_TYZDENNE

    print(f"Cieľ: {CISTE_MESACNE:,.0f} kr čisté/mes. + {DOCHODOK_PERCENTO:.0%} na dôchodok".replace(",", " "))
    print(f"  potrebný zisk firmy:     {zisk:>10,.0f} kr/rok".replace(",", " "))
    print(f"  z toho daň + trygd:      {dane:>10,.0f} kr/rok ({dane/zisk:.0%})".replace(",", " "))
    print(f"  náklady firmy (+rezerva):{naklady:>10,.0f} kr/rok".replace(",", " "))
    print(f"  OBRAT bez MVA:           {obrat:>10,.0f} kr/rok = {obrat/12:,.0f} kr/mes.".replace(",", " "))
    print(f"  pracovné hodiny spolu:   {hodiny_spolu:>10,.0f} h/rok ({tyzdne} týždňov × {HODIN_TYZDENNE} h)".replace(",", " "))
    print()
    print("Podiel fakturovaných hodín | fakturované h/rok | MIN. sadzba bez MVA | s MVA 25 %")
    for podiel in (0.50, 0.60, 0.70, 0.80):
        h = hodiny_spolu * podiel
        sadzba = obrat / h
        print(f"   {podiel:>4.0%} (kancelária+cesty {1-podiel:.0%}) |"
              f" {h:>8,.0f} h | {sadzba:>10,.0f} kr/h | {sadzba*(1+MVA):>8,.0f} kr/h".replace(",", " "))


if __name__ == "__main__":
    main()
