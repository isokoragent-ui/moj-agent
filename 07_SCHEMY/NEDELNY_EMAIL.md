# Nedeľný e-mail zákazníkom (Shopify Messaging)

**Kedy sa použije:** každý týždeň — 1 e-mail, odoslanie v nedeľu 9:30 Oslo (rozhodnutie `08_ROZHODNUTIA/2026-10-28_email_marketing_nedela.md`).
**Naposledy prešla:** 2026-10-28 — nyhetsbrev č. 1 „Julen starter med et rent bad“ naplánovaný na 1. 11. (Luk overil testom: obrázok aj tlačidlo vedú na produkt, alt text uložený).

## Kroky
1. **Do štvrtka:** agent napíše text (nórsky, `03_STYL/HLAS.md`) do `02_PRACA/emaily/RRRR-MM-DD_nyhetsbrev_<tema>.md` → Luk schváli.
2. Messaging → **Vytvoriť správu** → E-mail → šablóna **Prázdny** → Vybrať.
3. Príjemca: segment **„Nyhetsbrev – kunder med kjøp“** (kupujúci so súhlasom; vytvorený agentom cez API, 23 ľudí k 28. 10.). Predmet + Text ukážky.
4. Obsah zhora: logo → obrázok (URL = produkt, alt text) → jeden textový blok (skopírovať celý text naraz) → tlačidlo s odkazom na produkt.
5. **Odoslať test** → Luk otvorí na mobile, klikne na obrázok aj tlačidlo.
6. Skontrolovať → **Naplánovať** (NIE „Odoslať ihneď“) → ne 9:30.
7. Pondelok: agent zapíše otvorenia / kliky / predaje / odhlásenia do súboru e-mailu.

## Pasce — čo nás už vypálilo
- ⚠️ Messaging **nemá API na kampane** — agent vie len segmenty (`segmentCreate`) a čítanie zákazníkov; e-mail zadáva Luk podľa krokov.
- ⚠️ Doména odosielateľa musela mať **6 CNAME** na One.com, inak e-maily idú cez `store+…@shopifyemail.com` → `07_SCHEMY/OVERENIE_DOMENY_EMAIL.md`.
- ⚠️ `customersCount(query:)` ignoruje filter súhlasu (vráti všetkých) — počty overovať cez `customerSegmentMembers(query:)`.
- ⚠️ Tvrdenia: žiadne „antimikrobielt“, „dreper bakterier“ (biocíd) ani „trygg/ufarlig“ pri výrobkoch so znakom nebezpečnosti. Luk 28. 10.: obrázky od výrobcu/kampane môžu ostať.
- ⚠️ Text, ktorý ďakuje za nákup, len pre kupujúcich (nie pre „Všetci odberatelia“).

## Čo agent spraví sám / kde čaká na moje „áno"
- sám: text, segment, kontrola snímok, vyhodnotenie čísel.
- čaká: schválenie textu, zadanie v Messaging a naplánovanie robí Luk.
