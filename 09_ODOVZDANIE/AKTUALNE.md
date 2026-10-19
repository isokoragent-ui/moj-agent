# Kde sme skončili

*Prepisuje `/odovzdaj` na konci každého rozhovoru. Agent to číta ako prvé.*

**Naposledy:** 2026-10-18 21:40 UTC, cloudová relácia (claude.ai) — všetko je v `main` (PR #1 aj PR #2 zlúčené)

## Hotové naposledy
- **Sociálne siete pripojené cez Metricool** (overené volaním): Facebook, Instagram @isokor_skandinavia, TikTok, YouTube, Google Business Profile, Facebook Ads
- **Prvý príspevok Peisglassrens zverejnený na FB + IG** (Luk ho pustil ručne ako test, 18. 10. 23:01) — overené: PUBLISHED na oboch
- Nová schéma `07_SCHEMY/PRISPEVOK_SOCIALNE_SIETE.md` · rozhodnutie `08_ROZHODNUTIA/2026-10-18_socialne_siete_cez_metricool.md` · register prístupov aktualizovaný
- Skôr v ten deň: web audit + opravy e-shopu (názvy, SEO, adresy, doprava) — PR #1 zlúčený

## Nedokončené — pokračovať tu
1. ✅ **Peisglassrens zverejnený** 2026-10-18 23:01 (Luk ručne, test) — overené v Metricoole: FB https://facebook.com/122216737250920172/posts/122216741084920172 · IG https://www.instagram.com/p/DepmmyTCQED/ → o pár dní pozrieť dosah
   - ✅ Prázdny TikTok draft Luk zmazal ručne (overené v Metricoole 18. 10.)
2. **Web audit — zvyšok** (poradie, na ktorom sme sa dohodli):
   a) Menu: skryť „Vårt Magasin“ a „For profesjonelle“, zverejniť „Om oss“ — agent vie sám, po „áno“
   b) Vilkår for bruk: nevyplnená šablóna — agent pripraví text, **Luk vloží** (konektor nemá `write_legal_policies`); treba od Luka: ktorá firma predáva produkty a ktorá robí služby
   c) Angrerett + angreskjema podľa nórskeho zákona — agent pripraví, Luk vloží (odporúčané dať pozrieť odborníkovi)
   d) Zľavy viditeľné v pruhu hore — cez kópiu témy, Luk publikuje
   e) Vypredané: FVP, Fasaderens Plus 5 l, SW 5 l — Luk rozhodne: doobjednať alebo skryť
3. Marketing ďalej: navrhnúť Lukovi pravidelný rytmus príspevkov (napr. 2× týždenne, produkty podľa sezóny) — zatiaľ nedohodnuté
4. Luk zmaže v admine nepublikovanú kópiu témy „Dawn – úprava úvodnej stránky 2026-10-18“ (agent témy mazať nemôže; „Oppdatert kopi av Dawn“ je Lukova — nechať)
5. Luk prejde `02_PRACA/PLAN.md` a dodá čísla pre Krok 0 (obrat, náklady, zákazky za 3 mesiace)
6. ✅ **Pošta:** lukas@ + info@ sa preposielajú do isokor.agent@gmail.com (overené 2026-10-19). Ďalej: denný prehľad pošty; faktúry štítkom Faktúry/Na tlač; spam navrhnúť na zmazanie (pravidlá v `08_ROZHODNUTIA/2026-10-19_posta_cez_preposielanie_do_gmailu.md`)
7. #1027 (248 NOK) — Luk má označiť ako zaplatené v Shopify admin; potom overiť
8. Higgsfield: kľúč z chatu zrušiť a vytvoriť nový; zatiaľ netreba — Artlist stačí
9. Sprievodca: míľnik „pridať test do over.py“ (napr. Metricool `getBrandSettings`) — ponúknuť znova
10. ⏸ Hroby (kampaň pred Allehelgensdag) — Luk odložil; návrh v `02_PRACA/NAVRH_HROBY_2026-10.md`, nepripomínať

## Pozor (čo by ďalšieho vypálilo)
- Príspevky na siete: vždy najprv **draft**, zverejniť/naplánovať až po „áno“. Na produkt reálna fotka zo Shopify, nie AI.
- Pripájanie sietí: web Metricoolu na tablete nefunguje → appka Metricool.
- Shopify konektor NESMIE: zapisovať do živej témy, publikovať/mazať tému, meniť právne podmienky (overené). Viac v `05_PRISTUPY/REGISTER_PRISTUPOV.md`.
- Pri audite témy kontrolovať `disabled` na sekcii AJ bloku; dostupnosť produktu = `availableForSale`, nie sklad (KÓD #4).
- Živý web je z cloudu nedostupný (proxy 403) — rýchlosť, mobil, cookie lištu treba pozrieť Lukovými očami.
- Na konci okna VŽDY commit + push, inak sa práca stratí.

ĎALŠÍ KROK: pokračovať menu (audit 2a); o 2–3 dni (cca st 21. 10.) pozrieť dosah príspevku Peisglassrens.
