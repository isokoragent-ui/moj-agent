# Sofarens — video na siete (návrh 17. 11. 2026)

**Produkt:** Isokor Sofarens · 149 kr · 20 ks na sklade · isokor-skandinavia.no/products/isokor-sofarens
**Z popisu na webe (smieme tvrdiť):** sofa, lenestoler, tepper, bilseter · kaldpressede oljer og planteekstrakter · V-Label · fjerner selv de mest motstandsdyktige flekkene · fjerner lukt.
**Nehovoríme:** „100 % naturlig“, „antibakteriell“, konkrétne rastliny (zloženie Sofarens nemáme overené — bylinky vo videu sú nálada, nie zoznam zložiek).

**Uhol pre Nórsko (november–december):** julebord, gløgg, rødvin, tyttebær, rød saft od detí → „Flekker hører julen til. Det gjør ikke de på sofaen.“

## Scenár — 19 s, 9:16 (aj 16:9)
| Čas | Obraz | Text (NO) |
|---|---|---|
| 0–2,5 s | **Hák:** pohár červeného vína sa prevráti na svetlú sofu | **Rødvin på sofaen?** |
| 2,5–5 s | rýchle strihy po 0,6 s: čučoriedky · paradajková polievka · krv · sirup | **Blåbær. Tomatsuppe. Blod. Sirup.** |
| 5–8,5 s | prírodné extrakty: kvapka oleja, bylinky, sklenené fľaštičky | **Kaldpressede oljer og planteekstrakter** |
| 8,5–11 s | nástrek na škvrnu, jemná hmla v protisvetle | **Spray. Vent litt. Tørk av.** |
| 11–14 s | čistá sofa, útulná nórska obývačka, sviečky, sneh za oknom | **Ren sofa – klar for julebesøket** |
| 14–19 s | skutočná fľaša Sofarens + cena | **Isokor Sofarens · 149,-** · Sofa · tepper · bilseter · V-Label · isokor-skandinavia.no |

Hudba: vlastná (`hytteservice/hudba.py`), ako pri predošlých videách.

## Prompty do Gemini
**Ako na to:**
1. Najprv vygeneruj **obrázok 0 (čistá sofa)**. Keď sa ti páči, v ďalších promptoch ho **prilož ako referenciu** a napíš na začiatok: *„Use the attached image. Keep exactly the same sofa, fabric, room and light.“* — inak bude v každom zábere iná sofa.
2. Fľašu nech AI **nekreslí** (vymyslí falošnú etiketu). V zábere s nástrekom je fľaša bez etikety a skutočnú fľašu dám do videa ja.
3. Pomer strán: do promptu je zapísaný **9:16**; ak ho Gemini ignoruje, nevadí, orežem.

**0 — základná sofa (referencia)**
> Photorealistic interior photo, vertical 9:16. A light oatmeal-beige woven fabric three-seater sofa in a Scandinavian living room: light oak floor, white walls, a chunky knitted wool blanket, a sheepskin, a low oak coffee table with lit candles. Large window with snowy pine trees outside, soft blue-hour winter light mixed with warm candlelight. Calm, cozy Norwegian "hygge" mood. Shot on a full-frame camera, 35mm lens, natural colors, no people, no text, no logos.

**1 — hák: červené víno**
> Use the attached image, keep exactly the same sofa, fabric and room. Close-up, vertical 9:16: a stemmed glass of red wine tipping over onto the light sofa seat cushion, dark red wine splashing out and droplets frozen mid-air, the first wine already soaking into the fabric. Evening party mood, blurred candles and a plate of Christmas cookies in the background. High-speed photography, photorealistic, 50mm lens, shallow depth of field, no people's faces, no text.

**2a — čučoriedky**
> Use the attached image, keep the same sofa fabric. Macro close-up, vertical 9:16: a small bowl of fresh blueberries tipped over on the sofa cushion, several berries crushed into the fabric leaving deep purple-blue juice stains. Soft daylight, photorealistic texture of the woven fabric, shallow depth of field, no text.

**2b — paradajková polievka**
> Use the attached image, keep the same sofa fabric. Close-up, vertical 9:16: a ceramic bowl of tomato soup spilled on the sofa armrest, thick orange-red soup soaking into the light fabric, a spoon lying next to it. Warm indoor light, photorealistic, shallow depth of field, no text.

**2c — krv**
> Use the attached image, keep the same sofa fabric. Close-up, vertical 9:16: a few small dark red, partly dried blood spots on the light sofa cushion, as after a nosebleed, a crumpled white tissue lying beside them. Realistic and everyday, not gory, soft daylight, photorealistic fabric texture, no people, no text.

**2d — sirup**
> Use the attached image, keep the same sofa fabric. Close-up, vertical 9:16: sticky red berry syrup dripping from an overturned glass bottle onto the sofa cushion, glossy syrup puddle soaking into the light fabric, a child's plastic cup tipped over nearby. Bright daylight, photorealistic, shallow depth of field, no text, no labels.

**3a — prírodné extrakty (kvapka oleja)**
> Macro product-style photo, vertical 9:16: a single golden drop of cold-pressed plant oil falling from a glass pipette into a small glass bowl, surrounded by fresh green leaves, sprigs of lavender, chamomile flowers and thin citrus slices on a light oak board. Soft Nordic morning light from the side, clean and minimalist, beige and green tones, backlit droplet glowing, photorealistic, no text, no brand names.

**3b — pripravené extrakty**
> Photorealistic still life, vertical 9:16: small amber and clear glass bottles and bowls with freshly prepared plant extracts in green, golden and pale amber colors, a stone mortar with crushed herbs, fresh leaves and flowers scattered around, on a light oak table by a window with soft snowy winter daylight. Calm, natural, premium Scandinavian look, shallow depth of field, no text, no labels, no logos.

**4 — nástrek**
> Use the attached image, keep the same sofa and the red wine stain on the seat cushion. Close-up, vertical 9:16: a hand in a knitted sleeve spraying a fine mist from a plain white spray bottle without any label onto the red wine stain, the mist clearly visible and glowing in the window backlight. Photorealistic, 50mm lens, shallow depth of field, no text, no logos.

**5 — čistá sofa (koniec)**
> Use the attached image, keep exactly the same sofa and room. Vertical 9:16: the sofa is spotless and fresh, cushions neatly arranged, knitted blanket folded on the armrest, a cup of coffee and a bowl of clementines on the coffee table, candles lit, snow falling outside the window. Warm, inviting Norwegian Christmas evening mood, photorealistic, no people, no text.

**6 — pozadie pre fľašu**
> Use the attached image, keep the same room. Vertical 9:16: an empty light oak side table next to the sofa, a small sprig of fresh green herbs and a folded linen cloth on it, plenty of empty space in the center of the table for a product to be placed, soft warm light, background softly blurred, photorealistic, no text, no products.

## Pasce
- ⚠️ **„Pred/po“ z AI nesmie vyzerať ako skutočný výsledok** (markedsføringsloven + pravidlá Meta; to isté sme riešili pri dlažbe LMS). Riešenie: v rohu malé „Illustrasjonsbilder“, **alebo** záber 4–5 natočiť naozaj (víno + čučoriedky na kúsku látky, 15 s mobilom) — reálny záber predáva najviac.
- ⚠️ Gemini môže odmietnuť „blood“ → použi „dark red nosebleed spots“.
- ⚠️ Hlavná fotka Sofarens v e-shope vyzerá ako AI → do videa skutočná fotka fľaše.
- ✅ 17. 11.: fľaša s novou nórskou etiketou z Lukovej skutočnej fotky → `grafika/sofarens_flaska_bez_pozadia.png` (záverečný záber) a `grafika/sofarens_produkt.jpg`.

## Hotové video (18. 11.)
`grafika/sofarens_video_story_1080x1920.mp4` — 20 s, z Lukových obrázkov z Gemini + skutočná fľaša. Čaká na Lukovo „áno“; potom 16:9 a Metricool.
