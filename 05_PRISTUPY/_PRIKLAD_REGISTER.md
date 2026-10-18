# PRÍKLAD vyplneného registra prístupov

*Pokračovanie vymyslenej Zuzany. Ukazuje, ako podrobne sa to vypĺňa — a čo
sem nikdy nepatrí.*

⚠️ **V registri nikdy nie je heslo, kľúč ani token.** Len to, KDE prístup
žije, čo umožňuje a ako sa ruší. Keby ti niekto tento súbor ukradol, nesmie
sa ním dostať nikam.

| Služba | Čo umožňuje | Kde je prístup | Rozsah | Ako zrušiť |
|---|---|---|---|---|
| E-shop (admin) | čítať objednávky, upravovať produkty | Keychain, služba `eshop-admin` | **bez** práva mazať, bez prístupu k platbám | zmeniť heslo v administrácii |
| Fakturačný nástroj | sťahovať vydané faktúry | `~/.config/moj-agent/faktury` | **len čítanie** | zrušiť API kľúč v nastaveniach nástroja |
| Instagram | čítať komentáre a správy | Keychain, služba `instagram-asistent` | **vlastný účet asistenta**, nie môj osobný | odobrať účet zo správcov stránky |
| Úložisko fotiek | nahrávať a sťahovať fotky produktov | `~/.config/moj-agent/fotky` | len priečinok `produkty/`, nie celý disk | odobrať zdieľanie priečinka |

## Nástroje, ku ktorým agent prístup NEMÁ (a nemá ho pýtať)

- **Internet banking a platobná brána.** Peniaze von schvaľujem a posielam ja.
- **Môj osobný e-mail.** Firemný áno, osobný nie.
- **Môj osobný Instagram.** Má vlastný účet asistenta.
- **Mazanie čohokoľvek v e-shope.** Ani produktov, ani objednávok.

*Toto je rovnako dôležité ako tabuľka vyššie. Keď je napísané, čo agent
nesmie, nemusí sa to zakaždým vysvetľovať — a nemá dôvod si to domýšľať.*
