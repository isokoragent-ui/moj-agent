# OBRÁZKY PRE WEB (generované AI)

**Kedy sa použije:** keď treba sadu obrázkov, ktoré majú držať spolu —
bannery sekcií, titulné obrázky článkov, obaly produktov.
**Naposledy prešla:** 3. 10. 2026

## Kroky

1. **Napíš si master prompt.** Časť, ktorá sa NEMENÍ (optika, realizmus,
   kompozícia, zrno), a premenné, ktoré sa menia pri každom obrázku:
   `[PREDMET]`, `[SVETLO]`, `[PALETA]`.
2. **Nechaj miesto na text.** Do promptu patrí veta, že jeden roh ostáva
   prázdny a pokojný — tam pôjde nadpis.
3. **Vygeneruj šesť variantov** jedného predmetu, nie jeden. Prvý nikdy nie
   je najlepší a porovnanie šiestich trvá minútu.
4. **Nadpis vysádzaj sám, mimo generátora.** Vygeneruj obraz BEZ textu
   a písmo doň pridaj až potom (Pillow, Figma, Canva — čokoľvek, nad čím máš
   kontrolu).
5. **Vyber podľa malej veľkosti.** Posudzuj obrázok v tej veľkosti, v akej
   bude na webe, nie na celú obrazovku. Veľa návrhov vyzerá skvele veľkých
   a v dlaždici sa rozsype.
6. **Ulož si surové výstupy mimo gitu** a do projektu daj len hotové súbory.

## Pasce — čo nás už vypálilo

- ⚠️ **Generátor komolí text a diakritiku.** Nadpisy si nenechaj kresliť —
  jeden model si napriek výslovnému zákazu vymyslel do obrazu nápis, ktorý
  nebol slovo v žiadnom jazyku.
- ⚠️ **Natvrdo zapísaná paleta vyrobí „jedno kopyto".** Keď je v master
  prompte pevná farebnosť („tmavá modrozelená, studený akcent"), vyjde
  rovnaký obrázok pri každom námete. **Svetlo a paleta musia byť premenná.**
- ⚠️ **Stmavenie pod textom zje obraz.** Keď sa pod nadpis kreslí tmavý
  prechod, pri svetlej fotke z nej spraví zasa tmavú. Daj mu silu ako
  parameter a pod písmo radšej pridaj jemný tieň.
- ⚠️ **Skutočné produkty sa NELEPIA, generujú sa s referenciou.** Vlepený
  výrez do hotového pozadia je vidieť na prvý pohľad — nesedí svetlo ani
  odraz. Pošli fotku produktu generátoru ako referenciu a nechaj ho postaviť
  ho do scény; etikety zvládne presne, aj s diakritikou.
- ⚠️ **Netvrď, že niečo model nezvládne, kým to neskúsiš.** Práve na tomto
  sme sa raz pomýlili a zbytočne sme obrázky lepili ručne.
- ⚠️ **Surové výstupy sú obrovské.** Za jeden deň narástli na 95 MB. Do
  verzovania patria len hotové obrázky.

## Čo agent spraví sám / kde čaká na moje „áno"

- **sám:** napíše prompt, vygeneruje varianty, vysadí nadpisy, pripraví
  prehľad na výber
- **čaká:** na výber variantu — a až potom nasadzuje
