# Overenie e-mailovej domény v Shopify (DNS na One.com)

**Kedy sa použije:** Shopify hlási pri adrese odosielateľa „Oppdateres“ / overenie neprešlo, alebo pribudne nová doména či adresa.
**Naposledy prešla:** 2026-10-28 — „Autentisert“ do ~1 h 15 min po pridaní záznamov (Shopify 6× ✓; tlačidlo „Jeg har oppdatert“ ostane neaktívne, keď Shopify záznamy už vidí — netreba klikať)

## Kroky
1. Shopify → Nastavenia → **Varsler** → Avsender-e-post → **Autentisering av e-postdomene** → rozbaliť šípku pri stave → tabuľka záznamov (2026-10: **6 CNAME**).
2. One.com → Admin → doména → **DNS** → DNS-oppføringer. Najprv pozrieť zoznam „Personlige“ AJ „Standard“ — čo už existuje.
3. Opprett ny oppføring → **CNAME** → Vertsnavn = názov zo Shopify (len časť pred doménou) → Er et alias for = hodnota zo Shopify → TTL nechať → Opprett oppføring.
4. Po každom zázname snímka zoznamu → agent porovná so Shopify.
5. Shopify → „Jeg har oppdatert DNS-poster“ → čakať (do 48 h) na „Autentisert“.

## Pasce — čo nás už vypálilo
- ⚠️ **Shopify chce viac záznamov, než sa zdá.** Do 28. 10. bol na One.com len 1 zo 6 → overenie „nikdy neprešlo“. Zoznam je schovaný pod šípkou pri „Propagering pågår“ a stav „Oppdateres“ vyzerá, akoby stačilo čakať.
- ⚠️ One.com dopĺňa `.isokor-skandinavia.no` sám — do Vertsnavn písať len `iub._domainkey`, nie celú doménu.
- ⚠️ Hodnoty kopírovať, nie písať — líšia sa jediným znakom (`dkim1/2/3/4`, `p782` vs `p761`).
- ⚠️ **DMARC:** One.com má štandardný TXT `_dmarc` (len zapnúť/vypnúť, hodnota neviditeľná). Doména smie mať **len jeden** DMARC → nepridávať druhý.
- ⚠️ Štandardné záznamy One.com sa môžu vypnúť po pridaní vlastného záznamu rovnakého typu na rovnaký názov (podozrenie pri TXT koreňa = SPF, neoverené).
- ⚠️ Z cloudu sa DNS nedá čítať (proxy 403) → overovanie len cez Lukove snímky alebo stav v Shopify.

## Overenie skutočným e-mailom (KÓD #4)
Testovací e-mail z Messaging na lukas@ (preposiela sa do isokor.agent@gmail.com) → agent cez Gmail konektor `get_message` vo formáte RAW → hlavička `Authentication-Results`.
Výsledok 28. 10. 2026: **SPF pass, DKIM pass (mailer7zv…, pdk1), DMARC pass**; DMARC politika One.com je **p=REJECT** (štandardný `_dmarc` stačí, druhý nepridávať). Riadok „Oppsett av DMARC-oppføring / Vis trinn“ v Shopify je len odporúčanie bez stavu — netreba riešiť.
- ⚠️ Pri **p=REJECT** každá ďalšia služba, ktorá posiela ako @isokor-skandinavia.no (napr. nový e-mailový nástroj, formulár), musí mať vlastné overenie domény — inak jej e-maily príjemcovia odmietnu.

## Čo agent spraví sám / kde čaká na moje „áno"
- sám: pripraví tabuľku záznamov, kontroluje snímky, zapisuje stav.
- čaká: každé pridanie/zmenu na One.com robí Luk (agent nemá prístup).
