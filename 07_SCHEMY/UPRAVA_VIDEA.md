# ÚPRAVA VIDEA (strih pre nórsky trh)

**Kedy sa použije:** Luk má video (produkt, ukážka práce) a chce ho
prestrihať a upraviť na sociálne siete.
**Naposledy prešla:** 19. 10. 2026 (Peisglassrens, 47 s → 26 s, 9:16)

## Kroky
1. **Dostať video k agentovi:** najjednoduchšie je nahrať ho priamo do chatu
   (príloha). Google Disk ide len do 10 MB.
2. **Analýza:** `ffprobe` (rozlíšenie, dĺžka, zvuk) + kontaktný hárok
   1 snímka/s s časom (`fps=1,drawtext=%{pts\:hms},tile=8x6`) → pozrieť sa
   na obrázok a rozpísať zábery.
3. **Strih:** ponechať hák (prvé 2 s), dôkaz (špinavý papier), výsledok
   (čisté sklo), produkt na konci. Opakované utieranie zrýchliť 2–2,5×.
4. **Formát 9:16 (1080×1920):** zábery na šírku = štvorcový výrez v strede
   + rozmazané stmavené pozadie; zábery na výšku = výrez na celú plochu.
5. **Úprava:** `eq=contrast=1.08:saturation=1.15`, `unsharp`, zvuk
   `loudnorm=I=-14`, na konci fade out 1,5 s.
6. **Texty po nórsky** (Inter ExtraBold, tmavý box pod textom) — len tvrdenia
   z popisu produktu v e-shope. Záver: názov produktu + isokor-skandinavia.no.
7. Pred odovzdaním pozrieť kontrolný hárok (každé 2 s) → opraviť → poslať
   Lukovi návrh, až po „áno" finál.

## Pasce — čo nás už vypálilo
- ⚠️ **Konektor Google Disku stiahne max. 10 MB**; priame adresy Disku a
  Canvy sú v sieti cloudu blokované (403). Riešenie: menší súbor do chatu.
- ⚠️ **Biely text na rozmazanom bielom pozadí nie je čitateľný** → vždy box.
- ⚠️ **Výrez treba nastaviť podľa polohy objektu**, inak sa odreže kraj
  dvierok — skontrolovať na hárku.
- ⚠️ **Pôvodné logo na kraji záberu** sa pri výreze oreže na „ISOK" →
  zakryť nepriehľadným pásom so záverečným textom.
- ⚠️ Zdroj 360p sa ostrým nestane — finál ideálne z originálu 1080p.
  AI „vylepšenie" (video-to-video) nepoužívať: mení reálny záber produktu.
- Hudba v Lukových videách je v poriadku (Luk potvrdil 19. 10.).

## Čo agent spraví sám / kde čaká na „áno"
- **sám:** analýza, strih, návrh textov, kontrola
- **čaká:** na schválenie strihu a textov; zverejnenie vždy až po „áno"

## Príloha — text k videu Peisglassrens (2026-10-19, cena opravená 2026-10-26)
Sotet peisglass etter fyringen?

Isokor Peisglassrens er et ferdigblandet skum som løser sot, tjære og fett fra peis- og ovnsglass. Spray på, vent litt og tørk av – så er glasset klart igjen.

149 kr. Gratis frakt ved kjøp over 700 kr.
isokor-skandinavia.no/products/peisglassrens

#peis #vedovn #rengjøring #isokor

- ⚠️ **Artlist hudba sa z cloudu nestiahne** (`cms-public-artifacts.artlist.io` blokované proxy, overené 29. 10. 2026), hoci `download_track` vráti odkaz. Náhrada: vlastná krátka hudba z `02_PRACA/grafika/hytteservice/hudba.py` (numpy → WAV → ffmpeg mux), bez licenčných problémov.

## Realistické video z AI fotiek (prvýkrát 2026-11-15, Cleaner v2)
- **Cesta, ktorá funguje:** agent napíše prompty (EN, 9:16, *bez fliaš, bez textu*), Luk vygeneruje v **Gemini** a vloží do chatu → agent rozpohybuje (`02_PRACA/grafika/zdroj/cleaner_natur/video2.py`) a **skutočnú fľašu vloží sám** — etiketa ostane presná, sprej sa dá nasmerovať z hubice.
- Pred/po (špinavé → čisté) = **dva obrázky z toho istého rozhovoru v Gemini** („Edit the previous image… change nothing else“) → sedia na pixel, stieranie je prelínanie cez pohyblivú masku.
- ⚠️ **Canva a Artlist sa z cloudu nestiahnu** (sieť blokuje `www.canva.com`, `media.canva.com`, `export-download.canva.com`, `cms-public-artifacts.artlist.io`; overené 15. 11.). Canva vráti len náhľad 112 px. Povolenie cez mobilnú appku nejde → Luk musí z počítača (Prostredie → Edit → Allowed domains).
- ⚠️ **OpenCV `warpAffine` s float64 vstupom ignoruje okraj „reflect“ → čierne pásy** na okraji. Vždy pretypovať na float32.
- ⚠️ Kamera (zoom/otočenie) nesmie vyjsť z obrázka → zrkadlové artefakty. Pri otočení ~2° treba zoom aspoň 1,12.
- ⚠️ Fľašu a hmlu kresliť **až vo výstupe (po kamere)**, nie do zdrojovej fotky — inak ju okraj fotky oreže rovnou čiarou.
- Ústie hubice v `flaska_fett.png`: bod (1145, 200), strieka doprava → pri zrkadlení strieka doľava.
