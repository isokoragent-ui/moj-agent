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
