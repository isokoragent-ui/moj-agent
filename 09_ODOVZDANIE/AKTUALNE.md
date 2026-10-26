# Kde sme skončili

*Prepisuje `/odovzdaj` na konci každého rozhovoru. Agent to číta ako prvé.*

**Naposledy:** 2026-10-19 ~21:00 UTC, cloudová relácia (claude.ai) — všetko je v `main`

## Hotové naposledy
- **Google Kalendár pripojený** (isokor.agent@gmail.com, pásmo UTC): „Stretnutie Butik Mira“ št 29. 10. (celý deň) + samostatná udalosť‑pripomienka st 28. 10. 17:00 Oslo
- **Pošta pripojená a overená:** lukas@ + info@isokor-skandinavia.no (One.com) → preposielanie do isokor.agent@gmail.com
- Gmail: štítky **Faktúry/Na tlač** a **Faktúry/Vytlačené**; prvé upratanie (24 konverzácií do koša, Luk schválil)
- Pravidlá pošty v `08_ROZHODNUTIA/2026-10-19_posta_cez_preposielanie_do_gmailu.md`

## Nedokončené — pokračovať tu
1. ✅ **Peisglassrens zverejnený** 2026-10-18 23:01 (Luk ručne, test) — overené v Metricoole: FB https://facebook.com/122216737250920172/posts/122216741084920172 · IG https://www.instagram.com/p/DepmmyTCQED/ → o pár dní pozrieť dosah
   - ✅ Prázdny TikTok draft Luk zmazal ručne (overené v Metricoole 18. 10.)
2. **Web audit — zvyšok** (poradie, na ktorom sme sa dohodli):
   a) ✅ Menu hotové 2026-10-26: Vårt Magasin a For profesjonelle vyradené z menu (stránka a kolekcia ostali), Om oss zverejnená a v menu pred Kontakt. Záloha menu: `02_PRACA/zalohy/menu_hovedmeny_2026-10-26.json`. Zostáva: preklep „hudsensitiive“ na Om oss → opraviť po „áno“
   b) Vilkår for bruk: nevyplnená šablóna — agent pripraví text, **Luk vloží** (konektor nemá `write_legal_policies`); treba od Luka: ktorá firma predáva produkty a ktorá robí služby
   c) Angrerett + angreskjema podľa nórskeho zákona — agent pripraví, Luk vloží (odporúčané dať pozrieť odborníkovi)
   d) Zľavy viditeľné v pruhu hore — cez kópiu témy, Luk publikuje
   e) Vypredané: FVP, Fasaderens Plus 5 l, SW 5 l — Luk rozhodne: doobjednať alebo skryť
3. Marketing ďalej: navrhnúť Lukovi pravidelný rytmus príspevkov (napr. 2× týždenne, produkty podľa sezóny) — zatiaľ nedohodnuté
4. Luk zmaže v admine nepublikovanú kópiu témy „Dawn – úprava úvodnej stránky 2026-10-18“ (agent témy mazať nemôže; „Oppdatert kopi av Dawn“ je Lukova — nechať)
5. Luk prejde `02_PRACA/PLAN.md` a dodá čísla pre Krok 0 (obrat, náklady, zákazky za 3 mesiace)
6. ✅ **Pošta:** lukas@ + info@ sa preposielajú do isokor.agent@gmail.com (overené 2026-10-19). Ďalej: denný prehľad pošty; faktúry štítkom Faktúry/Na tlač; spam navrhnúť na zmazanie (pravidlá v `08_ROZHODNUTIA/2026-10-19_posta_cez_preposielanie_do_gmailu.md`)
   - 2026-10-26: Gmail upratný (21 do koša, Luk schválil). V doručenej: 6 návodov Metricool (Luk si pozrie, potom zmazať) + Anthropic faktúra. Mittanbud prehľady sa odteraz mažú.
   - Nápad: bezplatný Google firemný profil (Vyhľadávanie + Mapy) pre Isokor — ponúknuť Lukovi
7. #1027 (248 NOK) — Luk má označiť ako zaplatené v Shopify admin; potom overiť
8. Higgsfield: kľúč z chatu zrušiť a vytvoriť nový; zatiaľ netreba — Artlist stačí
9. Sprievodca: míľnik „pridať test do over.py“ (napr. Metricool `getBrandSettings`) — ponúknuť znova
10. ✅ **Video Peisglassrens** — finál 26 s, 9:16 odovzdaný Lukovi 2026-10-19 (z 360p; hudba OK podľa Luka). Ostrejšia verzia z originálu 1080p len ak Luk nahrá časti pod 10 MB. Schéma `07_SCHEMY/UPRAVA_VIDEA.md`. Luk ho zverejní **sám ručne, postupne po sieťach** (rozhodol 2026-10-19, do Shopify Súborov nenahrávať). Nórsky text príspevku je v `07_SCHEMY/UPRAVA_VIDEA.md` → Príloha.
11. ⏸ Hroby (kampaň pred Allehelgensdag) — Luk odložil; návrh v `02_PRACA/NAVRH_HROBY_2026-10.md`, nepripomínať

## Pozor (čo by ďalšieho vypálilo)
- Príspevky na siete: vždy najprv **draft**, zverejniť/naplánovať až po „áno“. Na produkt reálna fotka zo Shopify, nie AI.
- Pripájanie sietí: web Metricoolu na tablete nefunguje → appka Metricool.
- Shopify konektor NESMIE: zapisovať do živej témy, publikovať/mazať tému, meniť právne podmienky (overené). Viac v `05_PRISTUPY/REGISTER_PRISTUPOV.md`.
- Pri audite témy kontrolovať `disabled` na sekcii AJ bloku; dostupnosť produktu = `availableForSale`, nie sklad (KÓD #4).
- Živý web je z cloudu nedostupný (proxy 403) — rýchlosť, mobil, cookie lištu treba pozrieť Lukovými očami.
- Na konci okna VŽDY commit + push, inak sa práca stratí.
- Gmail konektor **nevie stiahnuť prílohy** → faktúry tlačí Luk priamo z e-mailu, každú zvlášť (nie spájať).
- Kalendár je v UTC: pri celodenných udalostiach počítať pripomienky od polnoci UTC; časové udalosti zadávať s pásmom Europe/Oslo.
- Mazanie pošty: vždy najprv zoznam, maže sa až po „áno“. Dopyty z Mittanbud a správy od klientov nemazať.
- Sprievodca pri štarte prepisuje počítadlo dní v `09_ODOVZDANIE/SPRIEVODCA.md` → commitnúť do `main`, nie do vetvy.

ĎALŠÍ KROK: Luk pozrie menu na mobile; potom audit 2b (Vilkår — treba od Luka: ktorá firma predáva produkty a ktorá robí služby).
