# Kniha jázd (Kjørebok) — súkromné auto pre Isokor Skandinavia AS

**Prečo:** Luk jazdí vlastným autom pre firmu. Firma mu môže kilometre preplatiť
(kjøregodtgjørelse) len na základe knihy jázd. Luk diktuje, agent zapisuje,
raz mesačne z toho vznikne PDF → Luk ho vytlačí a odovzdá **Anne Sofie**.

## Ako to funguje
1. **Luk nadiktuje jazdu** (kedykoľvek, aj viac naraz, aj spätne). Stačí napr.:
   „Utorok 10. 11., z domu do Arendalu a späť, rozvoz tovaru pre zákazníka X,
   tachometer 123 400 → 123 512, mýto 45 kr."
2. **Agent zapíše** do `jazdy/RRRR-MM.json`, povie jednou vetou „Rozumiem: …"
   a spustí `python3 _nastroje/kjorebok.py RRRR-MM --kontrola`.
   Ak niečo chýba (účel, odkiaľ/kam, km), spýta sa — **jedna otázka**.
3. **1. deň v mesiaci** (alebo keď Luk povie): agent vyrobí PDF za predošlý mesiac
   `python3 _nastroje/kjorebok.py RRRR-MM` → `pdf/Kjorebok_RRRR-MM.pdf`,
   pošle ho Lukovi a commitne. Účtovníčke ho **posiela/odovzdáva Luk** (alebo
   agent pripraví koncept e-mailu — až po „áno").

## Čo musí mať každá jazda (nórske pravidlá pre kjørebok)
| Pole | Príklad | Povinné |
|---|---|---|
| `dato` | 2026-11-10 | ✅ |
| `fra` / `til` | Vegårshei → Arendal (adresa alebo miesto) | ✅ |
| `formal` — účel jazdy | Levering av varer / Hyttetilsyn / Befaring / Innkjøp | ✅ |
| `besokt` — koho/čo navštívil | meno zákazníka, firma, kód chaty (H01) | ✅ ak sa dá |
| `km_start` / `km_slutt` — stav tachometra | 123400 / 123512 | odporúčané (alebo aspoň `km`) |
| `km` | 112 | ✅ ak nie je tachometer |
| `tur_retur` | true = cesta tam aj späť v jednom riadku | — |
| `bom`, `parkering` | v kr — **účtenky odložiť** | — |
| `merknad` | poznámka | — |

PDF je po nórsky (pre účtovníčku), pracovné poznámky po slovensky.

## Pasce
- **Len firemné jazdy.** Cesta z domu do práce a súkromné jazdy sem nepatria.
  Medzery v tachometri medzi jazdami = súkromné km, to je v poriadku.
- **Firma vs. živnosť (KÓD #25):** táto kniha je **len pre Isokor Skandinavia AS**.
  Keď jazda patrí živnosti, nezapisovať sem — spýtať sa.
- **Sadzba za km — zatiaľ žiadna (Luk 11. 11.).** Kniha jázd slúži ako
  **prehľad najazdených km**; preplácanie si Luk prípadne dorieši s Anne Sofie.
  `sats_per_km` nechať `null`, neodhadovať (KÓD #8). PDF ukáže len km.
- **Stav tachometra k 1. 1.** sa v Nórsku pri knihe jázd zvykne evidovať —
  zapísať do `nastavenie.json`, keď ho Luk povie.
- Skript **nevyrobí PDF**, kým sú v dátach chyby (tachometer dozadu, chýba účel…).

## Súbory
- `nastavenie.json` — firma, vodič, auto (EČV **DL 61036**), sadzba
- `jazdy/RRRR-MM.json` — jazdy po mesiacoch
- `pdf/Kjorebok_RRRR-MM.pdf` — hotové mesačné výkazy
- Generátor: `_nastroje/kjorebok.py`
