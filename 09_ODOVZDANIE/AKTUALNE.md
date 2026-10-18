# Kde sme skončili

*Prepisuje `/odovzdaj` na konci každého rozhovoru. Agent to číta ako prvé.*

**Naposledy:** 2026-10-18 19:45 UTC, cloudová relácia (claude.ai) — práca je na vetve `ccr-a2b401e2-vudlby`, PR #1 do `main`

## Hotové naposledy
- Hĺbkový audit webu → `02_PRACA/WEB_AUDIT_2026-10-18.md` (2 body boli omyl agenta — opravené, pravidlo pridané do KÓDU #4)
- Shopify (všetko Luk schválil, zálohy v `02_PRACA/zalohy_temy/`):
  - 34 názvov produktov na nórske
  - 34 SEO titulkov + 17 SEO popisov
  - 23 nových adries produktov, staré presmerované 301
  - 2 kolekcie: „Gratis frakt på alle bestillinger“
- Rozhodnutia: 2 org. čísla ostávajú (2 firmy) · hlavné popisy produktov ostávajú · podmienka Frakt ostáva · úvodná stránka bez zmien

## Nedokončené — pokračovať tu
1. **Web audit — zvyšok** (poradie, na ktorom sme sa dohodli):
   a) Menu: skryť „Vårt Magasin“ a „For profesjonelle“, zverejniť „Om oss“ — agent vie sám, po „áno“
   b) Vilkår for bruk: nevyplnená šablóna — agent pripraví text, **Luk vloží** (konektor nemá `write_legal_policies`); treba od Luka: ktorá firma predáva produkty a ktorá robí služby
   c) Angrerett + angreskjema podľa nórskeho zákona — agent pripraví, Luk vloží (odporúčané dať pozrieť odborníkovi)
   d) Zľavy viditeľné v pruhu hore — cez kópiu témy, Luk publikuje
   e) Vypredané: FVP, Fasaderens Plus 5 l, SW 5 l — Luk rozhodne: doobjednať alebo skryť
2. Luk zmaže v admine nepublikovanú kópiu témy „Dawn – úprava úvodnej stránky 2026-10-18“ (agent témy mazať nemôže; „Oppdatert kopi av Dawn“ je Lukova — nechať)
3. Luk prejde `02_PRACA/PLAN.md` a dodá čísla pre Krok 0 (obrat, náklady, zákazky za 3 mesiace)
4. Prvý prístup: Gmail / doménová schránka (schéma `07_SCHEMY/NOVY_PRISTUP.md`) → denný prehľad pošty; doplniť poskytovateľa doménových schránok
5. #1027 (248 NOK) — Luk má označiť ako zaplatené v Shopify admin; potom overiť
6. Peisglassrens: jesenný príspevok — návrh čaká na Lukovo „áno“
7. ✅ Metricool: Facebook + Instagram pripojené (2026-10-18, cez appku Metricool)
8. Higgsfield: kľúč z chatu zrušiť a vytvoriť nový; zatiaľ netreba — Artlist stačí
9. Sprievodca: dnešný míľnik „pridať test do over.py“ ponúknutý nebol dokončený — ponúknuť znova
10. ⏸ Hroby (kampaň pred Allehelgensdag) — Luk odložil; návrh v `02_PRACA/NAVRH_HROBY_2026-10.md`, nepripomínať

## Pozor (čo by ďalšieho vypálilo)
- **Dnešná práca je na vetve `ccr-a2b401e2-vudlby` (PR #1), NIE v `main`.** Kým Luk PR nezlúči, nové okno otvorené z `main` tento stav neuvidí → najprv skontrolovať/zlúčiť PR #1.
- Shopify konektor NESMIE: zapisovať do živej témy, publikovať/mazať tému, meniť právne podmienky (overené). Viac v `05_PRISTUPY/REGISTER_PRISTUPOV.md`.
- Pri audite témy kontrolovať `disabled` na sekcii AJ bloku; dostupnosť produktu = `availableForSale`, nie sklad (KÓD #4).
- Živý web je z cloudu nedostupný (proxy 403) — rýchlosť, mobil, cookie lištu treba pozrieť Lukovými očami.
- Na konci okna VŽDY commit + push, inak sa práca stratí.

ĎALŠÍ KROK: zlúčiť PR #1 do `main`, potom pokračovať menu (audit 1a).
