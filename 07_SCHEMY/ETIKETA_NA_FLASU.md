# NÓRSKA ETIKETA NA FOTKU FĽAŠE

**Kedy sa použije:** keď treba fotku fľaše s novou (nórskou) etiketou a skutočná fľaša ju ešte nemá.
**Naposledy prešla:** 30. 10. 2026 (Kjøkkenpakken — Kjøleskapsrens + Fett- og flekkfjerner)

## Kroky
1. Lukova fotka fľaše spredu → `rembg` (isnet-general-use) vystrihne (`zdroj/kjokkenpakken_jul/cut.py`).
2. Na mriežke (čiary po 100 px) odmerať: hornú/spodnú hranu etikety na bokoch, prehnutie hrany v strede, ľavý/pravý okraj fľaše hore a dole.
3. `python3 nalep.py <etiketa_NO.png> <vystup.png>` — etiketa z `02_PRACA/etikety/` sa ohne po valci (asin), stred čelného panelu ide doprostred fľaše, zvyšok etikety pokračuje okolo (modulo šírky).
4. Svetlo: farba „bielej" etikety po stĺpcoch sa berie z fotky (prázdne miesto starej etikety) → nová etiketa ju násobí. Potom vyrovnanie expozície (99,5 percentil → biela).
5. Jedna vystrihnutá fľaša stačí pre všetky 500 ml produkty — mení sa len etiketa.

## Pasce
- ⚠️ Na pravom okraji starej etikety je text → farbu svetla tam brať z plastu NAD etiketou, inak vznikne tmavý pruh.
- ⚠️ `rembg` nechá zúbky pozadia pri spúšti → ponechať len najväčší súvislý kus + orezať prvých ~40 px.
- ⚠️ Fotka z miestnosti je šedá — bez vyrovnania vyzerá fľaša na tmavom pozadí špinavá.
- Pasca z `OBRAZKY_PRE_WEB.md` („produkty sa nelepia do scény") platí pre **scény**. Na samostatnú fľašu na jednofarebnom pozadí lepenie etikety funguje — svetlo je z tej istej fotky.

## Agent sám / čaká na „áno"
- **sám:** výrez, nalepenie, grafika, produkt ako DRAFT
- **čaká:** zverejnenie produktu a príspevkov
