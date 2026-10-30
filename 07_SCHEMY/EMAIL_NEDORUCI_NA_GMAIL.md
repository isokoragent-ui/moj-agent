# E-MAIL Z VLASTNEJ DOMÉNY NEDORUČÍ NA GMAIL

**Kedy sa použije:** schránka na vlastnej doméne (One.com a pod.) prijíma, inam posiela, ale Gmail vracia „550 5.7.26 … unauthenticated“.
**Naposledy prešla:** 2026-10-30 (monika@skredderstuen.no)

## Kroky
1. Vypýtať snímku vráteného e-mailu → kód `550 5.7.26` + či zlyhal SPF/DKIM.
2. Zistiť, **KDE je DNS domény**: One.com → doména → DNS → záložka **Navnetjenere**. Ak nie je ns01/ns02.one.com, zmeny v One.com DNS nemajú účinok.
3. V skutočnom DNS (napr. Wix → Domény → „…“ → Spravovat záznamy DNS → TXT) pozrieť, či už SPF existuje.
4. Pridať / zlúčiť JEDEN TXT na koreň domény (názov hostiteľa prázdny):
   `v=spf1 include:_custspf.one.com ~all` (zdroj: help.one.com/hc/en-us/articles/115005595945)
5. Počkať ~1 h, test na isokor.agent@gmail.com → agent v Gmail RAW overí `spf=pass`.

## Pasce — čo nás už vypálilo
- ⚠️ Doména zaplatená na One.com, ale **DNS na Wixe** (web je na Wixe). Prepínač TXT v One.com sa zapol, 2 h nič — strata večera. Najprv krok 2!
- ⚠️ **Nikdy neprepínať navnetjenere späť na One.com** — spadne web na Wixe.
- ⚠️ Len **jeden** SPF záznam na doménu — existujúci zlúčiť, nepridávať druhý.
- ⚠️ DNS z cloudu sa čítať nedá (DoH blokované, UDP DNS vracia falošné NXDOMAIN) → overovať hlavičkami prijatého e-mailu.
- ⚠️ Chat One.com: robot sa najprv pýta meno a e-mail, správa max 128 znakov, v noci reálna podpora nedostupná.
- ⚠️ „Predtým to fungovalo“ = Gmail sprísnil pravidlá (od 2024 vyžaduje SPF alebo DKIM), nie výpadok.

## Čo agent spraví sám / kde čaká na moje „áno"
- sám: diagnostika z vrátenej správy, overenie hodnoty SPF v dokumentácii, kontrola hlavičiek testu.
- čaká: zmenu DNS robí Luk (prístup do Wixu/One.com má on).
