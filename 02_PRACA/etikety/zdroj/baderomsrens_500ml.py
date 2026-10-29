# Isokor Baderomsrens 500 ml (SK: Bath Cleaner) — nórske texty etikety. Všetko od výrobcu ostáva, len preklad
# (08_ROZHODNUTIA/2026-10-28_etikety_len_preklad.md). „Isokor Polisher“ → web „Isokor Polish“.
from reportlab.lib.colors import CMYKColor

SOURCE = 'original_SK_Bath_Cleaner_500ml.pdf'
OUT = 'Isokor_Baderomsrens_500ml_etikett_NO'

TITLE = ['BADEROMSRENS']
CLAIMS = ['Antimikrobielt rensemiddel', 'for baderom']

BODY = [
    ('ISOKOR® BADEROMSRENS',
     'er et miljøvennlig, naturlig rengjøringsmiddel for baderom. Fjerner effektivt all vanlig smuss, rengjør '
     'perfekt og avfetter. Spesielt anbefalt til rengjøring av baderomsarmaturer, dusjkabinetter, speil, '
     'badekar, fliser og veggfliser. Anbefales til vanlig vedlikehold. Holder lenge friskt og etterlater en '
     'behagelig duft og glans. Egnet ikke bare i hjemmet, men også i utdanningsinstitusjoner, hoteller, '
     'pensjonater, frisør- og skjønnhetssalonger og spesialklinikker. Produktet fjerner opptil 99,99&nbsp;% '
     'av proteinforurensning og nøytraliserer effektivt ubehagelig lukt. Overflatene trenger ikke skylles med '
     'vann etter bruk. Svært godt biologisk nedbrytbart, trygt for mennesker og husdyr. Som et av få produkter '
     'er det sertifisert med den prestisjetunge sveitsiske utmerkelsen V-Label. For langvarig hygienisk renhet '
     'anbefaler vi å polere blanke overflater etter rengjøring med Isokor Polish (finnes i vårt sortiment).'),
    ('Egnet til:',
     'glass, keramikk, plast, lakkerte overflater, rustfritt stål, krom, tekstiler, mineralske overflater.'),
    ('Bruksanvisning:',
     'Rist i ca.&nbsp;5&nbsp;sekunder før bruk. Påfør på overflaten som skal rengjøres og la virke i '
     'ca.&nbsp;3–5&nbsp;minutter; produktet kan samtidig bearbeides forsiktig med svamp eller mikrofiberklut. '
     'Tørk forsiktig av eller skyll med vann. Gjenta ved behov. Bruk en myk børste på særlig hardnakket '
     'smuss. Produktet er klart til bruk – skal ikke fortynnes eller blandes med andre stoffer. Produktet kan '
     'endre farge og konsistens ved temperaturpåvirkning, men dette påvirker ikke egenskapene. Trygt for '
     'mennesker og husdyr, biologisk nedbrytbart og ufarlig for barn.'),
    ('Sikkerhetstiltak:',
     'Unngå kontakt med øynene – kan gi lett irritasjon, som ved bruk av såpe. Ved øyekontakt: hold øynene '
     'åpne og skyll straks med rent vann. Ved svelging: ikke fremkall brekninger, men drikk rikelig med '
     'væske. Oppbevares utilgjengelig for barn. Oppbevares ved 15–35&nbsp;°C. Beskyttes mot frost og sollys.'),
    ('Sammensetning:',
     'Kan inneholde noen eller alle av følgende ekstrakter og tilsetninger: organisk alkohol (97-99-4), '
     'mandelolje (8007-69-0), appelsinolje (8016-20-4), jojobaolje (61789-91-1), sitronolje (8007-02-1), '
     'soyaolje (8001-22-7), prosessert *glukonsyre (526-95-4), prosesserte *ekstrakter av sukkerrør '
     '(57-50-1), ekstrakt av solsikkeolje (8001-23-8), natron, sederolje (8000-27-9), kanelolje '
     '(8007-80-5), maisolje (8001-30-7), geraniumolje (8000-46-2), hvitløksekstrakt (8008-99-9), '
     'fruktkjerneekstrakt (68916-04-1), ammoniumbikarbonat av næringsmiddelkvalitet (1066-33-7), '
     'bearbeidet havsalt (11062-32-1), vann. *lyofilisater eller konsentrater.'),
    ('Inneholder ikke:',
     'glyserol, parabener, silikoner, parafiner, ceresin, fosfater, SLES, SLS, kunstige fargestoffer, '
     'syntetiske dufter (terpener), syntetiske fortykningsmidler (anti-cyanidiner), petrokjemikalier, '
     'stoffer av animalsk opprinnelse, metallforbindelser.'),
    ('Oppbevaring:',
     'Oppbevares i lukket originalemballasje ved 15–35&nbsp;°C. Må ikke utsettes for direkte sollys. '
     'Beskyttes mot frost. Oppbevares utilgjengelig for barn. Produktet kan endre farge og konsistens ved '
     'temperaturpåvirkning, men dette påvirker ikke egenskapene. Kun tom emballasje kan resirkuleres.'),
]

FOOT = [('Holdbarhet:', 'Se emballasjen'), ('Forbruk:', 'ca. 100 ml/m²')]

PRODUCER = {
    'head': 'Importør og distributør',
    'lines': ['Isokor Skandinavia AS', 'Org.nr. 922 112 975', 'Nærestadveien 1, 4985 Vegårshei',
              'Tlf. +47 486 42 178', 'www.isokor-skandinavia.no'],
    'tail': None,          # blok je nižšie než pri Cleaneri — „Produsert i EU“ by siahal k orezu (nie je povinné)
}

TEAL = CMYKColor(0.65, 0, 0.323, 0)          # podnadpis z originálu
LAYOUT = {
    'regions': {
        'text':      (465, 55, 850, 449),
        'text2':     (465, 440, 640, 476),
        'logo':      (296, 96, 446, 140),
        'nazov':     (100, 185, 440, 250),
        'podnadpis': (215, 272, 442, 338),
        'vyrobca':   (476, 522, 650, 580),
    },
    'green': TEAL,
    'band': (75.5, 180.6, 449.5, 255.1),
    'claims': (439.5, (294.5, 327.5), 'Khand-SemiBold', 16),
    'badges': [],
    'body': (480, 833, 65, 432),
    'producer': (533, 531, 7.0, 7.4),
    'icon': (487, 573, 32),
}
