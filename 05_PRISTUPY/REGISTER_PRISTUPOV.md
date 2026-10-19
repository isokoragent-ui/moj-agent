# Register prístupov — KDE sú, nikdy ČO

⚠️ Tu nikdy nie je heslo, kľúč, token ani `.env`. Len odkaz, kde prístup
žije a čo umožňuje. `preveruj.sh` tento súbor prehľadáva ako prvý.

| Služba | Čo umožňuje | Kde je prístup | Rozsah | Ako zrušiť |
|---|---|---|---|---|
| Gmail (niekoľko schránok) | čítať poštu, pripravovať koncepty, štítky, kôš | ✅ Gmail konektor v claude.ai na **isokor.agent@gmail.com** (overené 2026-10-19); prílohy sťahovať nevie | najprv len čítanie + koncepty | odobrať prístup v nastaveniach Google účtu |
| Doménové schránky @isokor-skandinavia.no | čítať poštu, pripravovať koncepty | ✅ poskytovateľ **One.com**; **lukas@ a info@** preposielajú kópie → isokor.agent@gmail.com, agent číta cez Gmail konektor (overené 2026-10-19 skúšobnými e-mailmi na obe adresy) | najprv len čítanie + koncepty | zmeniť heslo / zrušiť heslo aplikácie |
| Facebook | príspevky, stránka Isokor (+ Facebook Ads účet) | ✅ cez Metricool — pripojené v appke Metricool, overené volaním 2026-10-18 (web na tablete nefungoval) | návrhy → publikuje sa až po „áno“ | odpojiť v Metricoole → Pripojenia, alebo odobrať v nastaveniach stránky |
| Instagram | príspevky (@isokor_skandinavia) | ✅ cez Metricool, overené volaním 2026-10-18 | návrhy → publikuje sa až po „áno“ | odpojiť v Metricoole → Pripojenia |
| X (Twitter) | príspevky | ⏳ zatiaľ nepripojené | návrhy → publikuje sa až po „áno“ | odobrať v nastaveniach |
| Kalendár (Google) | plánovanie, termíny — doteraz ho veľmi nepoužívam, môžeš ho začať viesť | ✅ Google Calendar konektor v claude.ai, kalendár **isokor.agent@gmail.com** = Lukov kalendár v telefóne (overené 2026-10-19 zápisom udalosti). ⚠️ Časové pásmo kalendára je **UTC**, nie Oslo — pripomienky pri celodenných udalostiach počítať od polnoci UTC | čítanie + zápis po dohode | odobrať v Google účte / claude.ai → Connectors |
| Google nástroje (Drive, Docs, Sheets) | dokumenty, tabuľky, podklady | ⏳ zatiaľ nepripojené | podľa dohody | odobrať v Google účte |
| Excel, Word | faktúry, dokumenty | lokálne súbory | čítanie; úpravy len po potvrdení | — |
| E-shop Shopify (www.isokor-skandinavia.no) | objednávky, produkty, zákazníci, analytika | ✅ Shopify konektor v claude.ai (overené 2026-10-17 čítaním) | len čítanie — zásahy nikdy bez schválenia | — |
| Higgsfield (AI video/obrázky) | tvorba videí a obrázkov na marketing | ⏳ plánované — účet na firmu (AS), platený plán kvôli komerčným právam | — | zrušiť predplatné |
| Metricool (plánovanie príspevkov) | plánovať príspevky, analytika | ✅ konektor v claude.ai (overené 2026-10-18); značka isokorskandinavia napojená na **Facebook, Instagram, TikTok, YouTube, Google Business Profile, Facebook Ads** | príspevky ako draft → naplánovať až po „áno“ (`07_SCHEMY/PRISPEVOK_SOCIALNE_SIETE.md`) | odpojiť v claude.ai → Connectors |
| Artlist (AI obrázky, videá, hlas, hudba) | tvorba marketingového obsahu | ✅ konektor v claude.ai (overené 2026-10-17); plán AI Suite 16500, ostáva 6 723 kreditov, obnova 10. 11. | generovanie míňa kredity → vopred povedať cenu | odpojiť v claude.ai → Connectors |
| PostNord app | odosielanie zásielok | Luk ručne | agent len pripraví údaje | — |

*Prístupy pridávame priebežne, jeden po druhom (schéma `07_SCHEMY/NOVY_PRISTUP.md`).*

## Nástroje, ku ktorým agent prístup NEMÁ (a nemá ho pýtať)
- **Bankové účty** — nikdy (pozri Hranice v `AGENT.md`)

### Shopify konektor — čo nejde (overené volaním 2026-10-18)
- Zmazanie témy (`themeDelete`) → odmietnuté bezpečnostnou politikou konektora: „Use Shopify admin.“
- Podľa popisu konektora (netestované): zápis do živej témy, publikovanie témy, refundy, darčekové karty, zamestnanci.
- Úprava právnych podmienok (`shopPolicyUpdate`: Frakt, Vilkår, Angrerett…) → „Access denied… `write_legal_policies`“ (overené 2026-10-18). Texty vloží Luk v admine: Nastavenia → Pravidlá.
- Funguje: kópia témy (`themeDuplicate`) a úpravy nepublikovanej kópie → Luk publikuje sám.
