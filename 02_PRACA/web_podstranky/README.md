# Podstránky e-shopu — nový dizajn (od 2026-11-17)

**Pracovná téma:** „Isokor – JUL 2026 + nové podstránky“ (premenovaná 17. 11.; predtým „PRACOVNÁ (podstránky)“) `gid://shopify/OnlineStoreTheme/156287008947` (kópia živej JUL, NEZVEREJNENÁ).
Náhľad LMS: https://isokor-skandinavia.no/products/lms?preview_theme_id=156287008947
⚠️ Po pozretí náhľadu: https://isokor-skandinavia.no/?preview_theme_id= (inak prehliadač ukazuje náhľad ďalej).

## Čo je hotové v pracovnej téme
- **Vzhľad celého webu** (`assets/isokor-global.css`, načíta ho sekcia `isokor-stil` v hlavičke): zelené oblé tlačidlá, nadpisy Fraunces, zaoblené fotky, tmavá pätička.
- **Pruh hore** (2 správy): doprava 99/49/zdarma · Vipps + 14 dní angrerett. Hlavička sa pri posune nahor ukáže.
- **Pätička:** firma, adresa, org. č. 922 112 975 MVA, telefón, e-mail · menu „Butikk“ (`isokor-butikk`) a „Kundeservice“ (`isokor-kundeservice`) · ikony platieb. (Menu sú nové, živú pätičku neovplyvnili.) „Vilkår“ zámerne nie — podmienky sú nevyplnená šablóna (audit).
- **Košík:** lišta „X kr til billigere / gratis frakt“ + doba doručenia.
- **Stránka produktu – 1 šablóna pre všetky** (`product.json`, skopírovaná aj do 9 starých `product.*.json`):
  kategória · názov · hviezdičky (len ak sú recenzie) · krátky popis + štítky · cena · „På lager · levering 6–10 virkedager“ · výber · množstvo · Kúpiť + Vipps · **box dôvery** (`snippets/isokor-tillit.liquid`: koľko do lacnejšej/bezplatnej dopravy, platby, doručenie, angrerett, telefón) · popis ·
  sekcia `isokor-produkt-info`: Slik gjør du · pred/po s posuvníkom · Passer til / Ikke bruk på / bezpečnostný list · otázky · Passer godt sammen med · na mobile lišta „Legg i kurven“ dole.
- **Kolekcie:** fotky sa už neorezávajú (CSS).

## Obsah produktu = metapolia „Isokor – …“ (Shopify → Produkt → dole Metapolia)
`isokor.kategori` · `kort` · `fordeler` (štítky) · `steg` (kroky) · `passer_til` · `ikke_bruk` · `faq` (JSON `[{"q":"…","a":"…"}]`) · `sds` (odkaz na PDF) · `for_bilde` / `etter_bilde` (fotky pred/po) · `passer_med` (súvisiace produkty).
Prázdne pole = tá časť sa neukáže. Bez `passer_med` sa ukážu produkty z prvej kolekcie.

| Produkt | Stav |
|---|---|
| LMS rustfjerner | ✅ vyplnené 17. 11. (texty z karuselu + SDS 10.5), fotky pred/po čakajú na Luka |
| ostatné | ⏳ produkt po produkte |

## Pasce
- Hlavička: `padding_top/bottom` musí byť násobok 4 (14 neprešlo).
- Živú tému (JUL) agent nemení → všetko v pracovnej; po dokončení Luk zverejní pracovnú. Potom to isté do „po sviatkoch“ (homepage index.json sa líši, ostatné súbory rovnaké).
- Fotky z cloudu do Shopify nenahrám (blokované) → fotky pred/po nahrá Luk priamo do metapoľa produktu.

## Platby — overené 17. 11. 2026
- Shopify `paymentSettings.supportedDigitalWallets` = **Shop Pay, Apple Pay, Google Pay** → zákazník platí telefónom; Luk ich mať nemusí.
- Karta / Apple Pay / Google Pay / Shop Pay = Shopify Payments → **automatická výplata na bankový účet** (napr. #1040 248 kr zo 4. 11. → výplata 9. 11. 236,58 kr, „settes inn på bankkontoen din i løpet av 1–2 virkedager“; poplatok ~11 kr).
- Vipps (#1038) ide cez Vipps/MobilePay. **PayPal je na e-shope deaktivovaný** (Luk 17. 11.; účet PayPal má len na platobný terminál) — posledná PayPal objednávka #1027 bola v júli, keď ešte bol zapnutý. Na webe PayPal neuvádzať.
- Účet na výplaty Luk zmenil 10. 11. → výplata zadržaná do 14. 11. (bezpečnostné pravidlo Shopify).
- Agent nevidí číslo účtu ani rozvrh výplat (konektor bez oprávnenia `read_shopify_payments`).

## Zverejnenie (17. 11.)
Luk chce LMS online hneď → zverejniť „Isokor – JUL 2026 + nové podstránky“ (vianočná úvodná + nové podstránky). Overené: JUL naposledy zmenená 20:59, kópia vznikla 21:33 → nič sa nestratí. Návrat: „Isokor – JUL 2026 (teraz)“ → Publikovať. **Potom** nahrať tie isté súbory podstránok do „po sviatkoch 2027“.

## ✅ ZVEREJNENÉ 17. 11. 2026 ~21:58 (Luk) — overené `themes(roles:MAIN)`
- **Živá:** „Isokor – JUL 2026 + nové podstránky“ `…/156287008947`.
- **Po sviatkoch:** „Isokor – PO SVIATKOCH 2027 (s podstránkami)“ `…/156287566003` = kópia živej + bežná úvodná (index.json bez `jul`). Po Novom roku Luk zverejní túto.
- „ZASTARANÉ – nepoužívať“ `…/156285272243` (stará po-sviatkoch bez podstránok) — Luk môže zmazať.
- Návrat: „Isokor – JUL 2026 (teraz)“ alebo „Dawn“.

## Ďalšie produkty = len metapolia (nie téma!)
Obsah produktu je v metapoliach → po zápise je **hneď na živom webe**. Preto: agent pripraví texty → Luk schváli → agent zapíše.
Zmena kódu šablóny = nová pracovná kópia živej + to isté do „po sviatkoch“.
