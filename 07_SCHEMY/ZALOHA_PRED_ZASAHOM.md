# ZÁLOHA PRED ZÁSAHOM

**Kedy sa použije:** vždy, keď sa ide meniť niečo živé — web, e-shop,
databáza, DNS, plugin, nastavenie platieb. Aj keď je zmena „maličká".
**Naposledy prešla:** 3. 10. 2026

## Kroky

1. **Napíš, čo presne sa ide zmeniť.** Jednou vetou. Keď sa to nedá napísať
   jednou vetou, zmena je priveľká a treba ju rozdeliť.
2. **Nájdi ústupovú cestu a POMENUJ JU.** Nie „dá sa to vrátiť", ale
   konkrétne: *„mám FTP prístup, súbor si stiahnem do `_zaloha/` a viem ho
   nahrať späť"*. Keď sa ústupová cesta nedá pomenovať, **zásah sa nerobí.**
3. **Over ústupovú cestu SKÔR, než zmeníš čokoľvek.** Prihlás sa do FTP.
   Stiahni jeden súbor. Keď sa to nepodarí teraz, nepodarí sa to ani vtedy,
   keď bude horieť.
4. **Sprav zálohu** a povedz, kde je a ako je veľká.
5. **Zmeň jednu vec.** Nie tri naraz — pri troch nevieš, ktorá to zlomila.
6. **Over, že to funguje** skutočným volaním, nie pohľadom na stránku.
7. **Zapíš do `08_ROZHODNUTIA/`**, čo sa zmenilo a kde je záloha.

## Pasce — čo nás už vypálilo

- ⚠️ **„Vypnuté" neznamená „nepoužívané".** Vypnutý plugin býva vypnutý
  zámerne. Kým nevieš dôvod (logy, dátum vypnutia, changelog), nezapínaj ho.
- ⚠️ **Ústupová cesta sa overuje VOPRED.** Raz sme zapli optimalizačný plugin,
  ten položil celý e-shop — a prístup k súborom bol medzitým zablokovaný,
  takže sa to nedalo vrátiť. Stránka bola dole celý večer.
- ⚠️ **Panel poskytovateľa nie je záloha.** Keď spadne web, často spadne aj
  cesta k nemu. Záloha patrí na tvoj disk.
- ⚠️ **Hodina výpadku e-shopu je strata, ktorú nikto nevráti.** Pri čomkoľvek,
  čo zarába, platí dvojnásobne: radšej neurobiť než nevedieť vrátiť.

## Čo agent spraví sám / kde čaká na moje „áno"

- **sám:** zistí dôvod vypnutia, nájde a overí ústupovú cestu, spraví zálohu,
  pripraví zmenu, overí výsledok, zapíše rozhodnutie
- **čaká:** na samotný zásah do živého systému — vždy
