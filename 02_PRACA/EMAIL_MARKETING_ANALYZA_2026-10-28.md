# E-mail marketing pre existujúcich zákazníkov — analýza nástrojov

*2026-10-28 · zdroj: Shopify Admin API (aplikácie, zákazníci, súhlasy) — iba čítanie, nič nezmenené.*

## Nástroje v e-shope
| Nástroj | Čo to je | Na marketing? |
|---|---|---|
| **Messaging** (Shopify, predtým Shopify Email) | kampane e-mail/SMS/WhatsApp, šablóny, automatizácie, štatistiky (otvorenia, kliky, predaj); posiela len tým, čo majú súhlas, sám pridáva odhlásenie | ✅ **áno — tento** |
| **WorkflowMail Emails** (Intelli-ua) | posiela *transakčné* e-maily ako krok vo Flow (cez SMTP/Microsoft 365), aj s prílohami | ❌ nie — nerieši súhlas, odhlásenie ani štatistiky |
| Flow (Shopify) | automatizácie; WorkflowMail je jeho doplnok | len pomocník |
| Forms (Shopify) / Attrac | formuláre a vyskakovacie okná na zber e-mailov (obe to vedia — stačí jedno) | zber kontaktov |

**Odporúčanie:** e-maily písať a posielať **len cez Messaging**. WorkflowMail na marketing nepoužívať (porušenie súhlasov, horšie doručovanie). Neodinštalovať, kým Luk nepozrie, či ho nepoužíva nejaký Flow.

## Komu môžeme písať (stav 28. 10. 2026)
- Zákazníkov spolu 57; **s objednávkou 32**.
- Z nich **so súhlasom (SUBSCRIBED) 23** ← cieľová skupina „existujúci zákazníci“.
- Kupujúci bez súhlasu 6, odhlásení 2 (obaja v júli 2026), bez e-mailu 1.
- Navyše 6 ľudí so súhlasom bez nákupu (prihlásení na odber).
- Spolu so súhlasom: **29**.
- Súhlas je jednoduchý (single opt-in) — pre Nórsko stačí.

**Pravidlo:** posielať len SUBSCRIBED. Nórsky markedsføringsloven § 15 vyžaduje pre e-mail spotrebiteľom súhlas; výnimka pre existujúcich zákazníkov platí len pri možnosti odmietnuť už pri nákupe — kto pri pokladni políčko nezaškrtol, odmietol. Messaging to stráži sám.

## Cena a objem (NEOVERENÉ — over v aplikácii Messaging)
Podľa toho, čo agent vie: prvých ~10 000 e-mailov mesačne zdarma, potom zhruba 1 USD / 1 000. Pri 29 adresách × 3 e-maily týždenne ≈ 375 e-mailov mesačne → hlboko pod limitom.

## Názor agenta na frekvenciu
„Niekoľko do týždňa“ pri 23–29 ľuďoch je priveľa — malý zoznam sa rýchlo odhlasuje (2 odhlásenia už v júli). Návrh: **1 e-mail týždenne**, 2 len pri akcii (napr. Badepakken pred Vianocami). Rast zoznamu: zapnúť formulár na odber (Forms) v pätičke — newsletter je teraz vypnutý.

## Neoverené / treba skontrolovať
- **Odosielacia adresa a overenie domény** (SPF/DKIM/DMARC pre `isokor-skandinavia.no`) — bez nich e-maily idú „cez Shopify“ a častejšie padajú do spamu. Z cloudu sa DNS overiť nedá (proxy 403). Kde: Shopify admin → Nastavenia → Upozornenia → E-mail odosielateľa.
- Či niektorý Flow používa WorkflowMail.

## Postup (keď Luk schváli)
1. Overiť doménu odosielateľa v Messaging.
2. Segment v Messaging: „počet objednávok ≥ 1 a súhlas s e-mailovým marketingom“.
3. Agent napíše text (nórsky, tón Isokor) → Luk schváli → Messaging koncept → Luk odošle (alebo naplánuje).
4. Po každom e-maile zapísať otvorenia, kliky, odhlásenia (KÓD #23 — číslo po každej úlohe).
