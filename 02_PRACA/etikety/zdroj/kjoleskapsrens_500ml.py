# Isokor Kjøleskapsrens 500 ml (SK: Fridge Cleaner) — nórske texty etikety. Všetko od výrobcu ostáva, len preklad
# (08_ROZHODNUTIA/2026-10-28_etikety_len_preklad.md). Text je okrem úvodu zhodný s Bath Cleaner → preberá preklad
# z baderomsrens_500ml (bez odseku „Egnet til“, ktorý Fridge nemá).
from reportlab.lib.colors import CMYKColor
import baderomsrens_500ml as bad

SOURCE = 'original_SK_Fridge_Cleaner_500ml.pdf'
OUT = 'Isokor_Kjoleskapsrens_500ml_etikett_NO'

TITLE = ['KJØLESKAPSRENS']
CLAIMS = ['Rengjøringsmiddel for vask av', 'kjøleskap utvendig og innvendig']

BODY = [
    ('ISOKOR® KJØLESKAPSRENS',
     'er et naturlig og trygt middel uten farlig kjemi for hygienisk vask av kjøleskap, frysebokser og andre '
     'kjøleapparater, innvendig og utvendig. Trygt og egnet til rengjøring av overflater som kommer i kontakt '
     'med matvarer. Fjerner effektivt matrester og avfetter overflatene perfekt uten å etterlate striper og '
     'flekker. Produktet fjerner opptil 99,99&nbsp;% av proteinforurensning og nøytraliserer effektivt '
     'ubehagelig lukt. Overflatene trenger ikke skylles med vann etter bruk. Svært godt biologisk nedbrytbart, '
     'trygt for mennesker og husdyr. Som et av få produkter er det sertifisert med den prestisjetunge '
     'sveitsiske utmerkelsen V-Label. For langvarig hygienisk renhet anbefaler vi å polere blanke overflater '
     'etter rengjøring med Isokor Polish (finnes i vårt sortiment).'),
] + [p for p in bad.BODY if p[0] != 'Egnet til:'][1:]

FOOT = [('Best før:', ''), ('Batchnr.:', '10201CF'), ('Forbruk:', 'ca. 100 ml/m²')]

PRODUCER = {
    'head': 'Importør og distributør',
    'lines': ['Isokor Skandinavia AS', 'Org.nr. 922 112 975', 'Nærestadveien 1, 4985 Vegårshei',
              'Tlf. +47 486 42 178', 'www.isokor-skandinavia.no'],
    'tail': 'PRODUSERT I EU',
}

BLUE = CMYKColor(0.522, 0.03, 0, 0)          # pás, podnadpis, 500ml
LAYOUT = {
    'regions': {
        'text':      (465, 60, 850, 436),
        'text2':     (465, 425, 620, 452),
        'logo':      (296, 96, 446, 140),
        'nazov':     (100, 185, 440, 250),
        'podnadpis': (205, 270, 440, 319),
        'vyrobca':   (476, 500, 650, 560),
    },
    'green': BLUE,
    'band': (75.5, 180.6, 449.5, 255.1),
    'claims': (438, (290.6, 314.7), 'Khand-SemiBold', 14),
    'badges': [],
    'body': (480, 833, 66, 432),
    'producer': (533, 509, 7.2, 7.6),
    'icon': (487, 553, 32),
}
