# B2B — sameie a borettslag v Agderi (od 2026-11-20)

**Čo:** zmluvy na údržbu (fasády, hrdza, sklo/zábradlia, dlažba) pre sameie
a borettslag — strategické zdôvodnenie v `10_STUDIUM_MAJETOK/09_PREDAJNY_SYSTEM.md`.
**Firma:** Isokor - Skandinavia AS.

## Zoznam
- Nástroj: `python3 _nastroje/sameie_agder.py api` (priamo z Brreg) alebo
  `python3 _nastroje/sameie_agder.py subor _inbox/<súbor>.csv|xlsx` (stiahnuté z brreg.no).
- Výstup: `zoznam.csv` (všetko) + `ZOZNAM.md` (súhrn podľa obcí + priorita 1 = do ~45 min od Vegårshei).
- Len údaje o organizácii — **žiadne mená členov výboru** do repozitára.

## Stav
- 2026-11-20: nástroj hotový a otestovaný na vzorke. **Dáta zatiaľ nie sú** — `data.brreg.no`
  je v cloude blokovaný (proxy 403); pridať host do prostredia sa z mobilnej appky nedá
  (stará verzia). Cesty: (a) Luk otvorí session na claude.ai v počítači → agent navrhne
  prostredie s `data.brreg.no` → `api`; (b) Luk stiahne export z brreg.no a nahrá do `_inbox/`.

## Ďalší krok (po zozname)
1. Agent vyberie prioritu 1 (Vegårshei, Tvedestrand, Arendal, Risør, Gjerstad, Froland, Åmli).
2. Agent pripraví ponuku po nórsky (ročná zmluva, pevná cena) → Luk schváli.
3. Kontakt na výbor (styre) — kanál a text až po Lukovom „áno“. Ponuka do jan–feb (rozpočet na jar ⚠️ over).
