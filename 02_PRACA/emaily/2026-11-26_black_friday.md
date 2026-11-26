# Black Friday 2026 — 15 % pre kupujúcich (pi 27. 11.)

*Stav: ✅ zľava vytvorená 26. 11. (Luk „áno“ na 15 %), overená čítaním — stav SCHEDULED. ⏳ E-maily zadáva Luk v Messaging.*

## Zľava v e-shope — VYTVORENÁ (`gid://shopify/DiscountCodeNode/1278774313139`)
- **15 %** (agent odporúča 15 namiesto 12 — pozri nižšie).
- Kód **BLACKFRIDAY15**, zákazník ho nepíše: tlačidlo v e-maile ho vloží do košíka samo
  (odkaz `https://isokor-skandinavia.no/discount/BLACKFRIDAY15?redirect=/collections/all`).
- Platí **len pre segment „Kunder som har handlet minst én gang“** (kto už nakúpil; kontrola podľa e-mailu v pokladni).
- Čas: **pi 27. 11. 00:00 – 23:59 Oslo** (UTC 26. 11. 23:00 – 27. 11. 22:59).
- Len jednotlivé produkty (31 ks). **Bez:** Badepakken, Kjøkkenpakken, Baderomssett (pevné ceny), Gravsteinvask – tjeneste a 5× Hytteservice (služby).
- Nekombinuje sa s inými zľavami (napr. Fera kód za recenziu). Doprava sa účtuje normálne podľa nastavenia.
- Jedno použitie na zákazníka: nie (môže kúpiť aj dvakrát za deň).

### Prečo 15 a nie 12
- 149 kr fľaša: 15 % = −22 kr (126,65 kr), 12 % = −18 kr (131,12 kr). Rozdiel 4,50 kr na fľašu.
- Marža (ANALYZA_CIEN): štandard 50 % → pri 15 % ~41 %; najnižšia (Glass Profi 31 %) → ~19 %. Stále v pluse.
- E-mail ide 23 ľuďom → pár objednávok; rozdiel 12 vs 15 je v desiatkach korún. „15 %“ sa lepšie číta a na Black Friday 12 pôsobí lakomo.

## E-mail 1 — štvrtok 26. 11. po obede (~13:00)
**Príjemcovia:** segment „Nyhetsbrev – kunder med kjøp“ (23 ľudí, overené 26. 11.)
**Predmet:** Black Friday: 15 % for deg som har handlet hos oss
**Text náhľadu:** Fredag 27. november, hele dagen. Rabatten legges inn automatisk.
**Obrázok:** `02_PRACA/grafika/black_friday_2026_email.png` → odkaz = discount link vyššie, alt „Black Friday hos Isokor – 15 % på alle enkeltprodukter fredag 27. november“
**Tlačidlo:** Handle med 15 % rabatt → discount link

---

Hei,

takk for at du har handlet hos oss tidligere. Som takk får du som allerede er kunde 15 % rabatt på alle enkeltprodukter i nettbutikken på fredag 27. november.

Rabatten gjelder hele fredagen, fra midnatt til midnatt. Du trenger ingen kode: trykk på knappen under på fredag, så ligger rabatten klar i handlekurven. Bruk samme e-postadresse som sist du handlet, så kjenner kassen deg igjen.

Tilbudet gjelder alle enkeltprodukter – rengjøring, impregnering og avkalking. Badepakken, Kjøkkenpakken og Baderomssettet har allerede faste priser og er ikke med. Frakten beregnes som vanlig i kassen.

Hvis du har tenkt å fylle på før jul, er dette en fin anledning.

[ Handle med 15 % rabatt ]

Med vennlig hilsen,

Lukas
Isokor Skandinavia
www.isokor-skandinavia.no

---

## E-mail 2 — piatok 27. 11. ráno (naplánovať na 9:00 Oslo)
**Príjemcovia:** rovnaký segment
**Predmet:** I dag: 15 % på alle enkeltprodukter
**Text náhľadu:** Gjelder til midnatt i kveld – rabatten ligger klar i handlekurven.
**Obrázok:** `02_PRACA/grafika/black_friday_2026_email_paminnelse.png` (rovnaký odkaz a alt)
**Tlačidlo:** Handle med 15 % rabatt → discount link

---

Hei,

en kort påminnelse: i dag, fredag 27. november, får du 15 % rabatt på alle enkeltprodukter hos oss. Tilbudet gjelder til midnatt i kveld.

Trykk på knappen, så legges rabatten inn automatisk i handlekurven. Bruk samme e-postadresse som sist du handlet. Pakkene og settet har faste priser og er ikke med, og frakten beregnes som vanlig.

[ Handle med 15 % rabatt ]

God helg!

Lukas
Isokor Skandinavia
www.isokor-skandinavia.no

---

## Poznámky agenta
- Postup v Messaging ako `07_SCHEMY/NEDELNY_EMAIL.md` (Prázdny → logo → obrázok → text → tlačidlo → test → naplánovať).
- Test e-mailu 1 sa dá poslať hneď, ale klik na tlačidlo **dnes** ukáže v pokladni „kód ešte neplatí“ — zľava začína o polnoci. To je v poriadku.
- Grafika: zdroj `02_PRACA/grafika/zdroj/black_friday/` → `node render.js`.
- Pondelok 30. 11.: zapísať otvorenia, kliky, počet objednávok s kódom BLACKFRIDAY15 a tržbu.
