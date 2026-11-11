# Agenda firmy — Isokor - Skandinavia AS

*Založené 11. 11. 2026. Jedno miesto, kde vidno, ako firma ide: čo sa kúpilo,
predalo, najazdilo a urobilo — a z toho denné, týždenné a mesačné raporty.*

## Ako to funguje
1. **Luk diktuje** kedykoľvek počas dňa: „Kúpil som v Jule vysávač na dielňu za 1 249, firemnou kartou, bloček mám.“
2. **Agent zapíše** záznam do `zaznamy/RRRR-MM.json`, zopakuje ho jednou vetou a pri nejasnosti sa spýta (jedna otázka).
3. **Stačí fotka bločku** (Luk nič neprepisuje): agent z nej prečíta obchod, dátum, sumu, MVA a položky, uloží ju do `doklady/RRRR-MM/RRRR-MM-DD_obchod.jpg`, navrhne kategóriu a **pýta sa len na to, čo na bločku nie je**: ako sa platilo (firemná karta / súkromne) a pri nejasnom nákupe načo to je. Viac bločkov naraz je v poriadku.
   - Fotka celá a ostrá, aj spodok so sumou a MVA. Nečitateľné číslo agent nehádá — spýta sa.
   - Papierový originál si Luk odloží, kým s účtovníčkou neoverí, že stačí fotka.
4. **Raporty:** `python3 _nastroje/agenda.py den|tyzden|mesiac [dátum]` → `reporty/…`
5. Commit + push → vidno to v každom okne.

## Kam čo patrí (nič sa nezapisuje dvakrát)
| Čo | Kam | Raport to berie odtiaľ |
|---|---|---|
| Výdavky (nákupy, palivo, reklama, poplatky…) | `zaznamy/` typ `vydavok` | ✔ |
| Predaj v obchode Myra, Vipps/hotovosť za služby | `zaznamy/` typ `prijem` | ✔ |
| E-shop objednávky | `zaznamy/` typ `prijem`, kanál `eshop`, `zdroj: shopify:#číslo` — **agent ich stiahne zo Shopify**, Luk ich nediktuje | ✔ |
| Faktúry | `02_PRACA/faktury/` — **sem nie** | ✔ (príjem + nezaplatené) |
| Jazdy, km | `02_PRACA/kjorebok/` — **sem nie** | ✔ |
| Marketing, stretnutia, predajné aktivity | `zaznamy/` typ `aktivita` (náklad na reklamu zvlášť ako `vydavok` / `marketing`) | ✔ |

## Čo je v raporte
Príjmy a výdavky bez MVA, **výsledok**, MVA na odvod, km · porovnanie s predchádzajúcim obdobím
(deň → rovnaký deň pred týždňom, týždeň → minulý týždeň, mesiac → minulý mesiac) · príjmy podľa kanála
(e-shop / obchod / služby / faktúry) · výdavky podľa kategórie · aktivity · mesačne aj **% z cieľa 40–50 tis.**
· sekcia **Treba riešiť**: výdavky bez dokladu, zaplatené súkromne (firma dlhuje Lukovi), nezaplatené faktúry, jazdy bez km.

## Rytmus
- **Denne** (večer, keď Luk nadiktuje deň): denný raport, krátko v chate.
- **Týždenne** (nedeľa, spolu s `/tyzden`): týždenný raport + čo z toho plynie pre marketing na ďalší týždeň.
- **Mesačne** (1. deň mesiaca): mesačný raport + kjørebok PDF pre Anne Sofie.

## Pasce
- **Suma sa zapisuje VRÁTANE MVA** (ako je na bločku); skript si MVA vyráta. Sadzba podľa kategórie (`nastavenie.json`); `strava` má 0 (väčšinou bez odpočtu).
- **MVA od 6. 11. 2026.** Nákupy a predaje pred týmto dňom sa rátajú bez MVA. Obdobie do 5. 11. (aj Faktura 19) má účtovníčka — neriešime.
- **Zaplatené súkromne** (`platba: sukromne`) = utlegg — firma to musí Lukovi vrátiť.
- **Bez dokladu** účtovníčka výdavok neuzná → agent pripomína v každom raporte.
- E-shop: pred zápisom skontrolovať `zdroj` (číslo objednávky) — `agenda.py kontrola` hlási duplicity.
- Výsledok v raporte je **pred daňou a pred Lukovou mzdou** — nie je to „čisté do vrecka“.
- Agent nemá a nežiada prístup do banky — čísla sú len z diktovania, Shopify a faktúr.
