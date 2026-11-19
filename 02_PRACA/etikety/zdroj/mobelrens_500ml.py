# Isokor Møbelrens 500 ml (SK: Furniture Cleaner) — nórske texty etikety. Všetko od výrobcu ostáva, len preklad
# (08_ROZHODNUTIA/2026-10-28_etikety_len_preklad.md). Okrem úvodu je text zhodný s Fridge/Bath Cleaner → preberá
# preklad z baderomsrens_500ml (bez odseku „Egnet til“) ako kjoleskapsrens_500ml. Rozloženie ako Fridge Cleaner.
# SK originál má preklep „FURNATURE CLEANER“ a „Isokor Polisher“ → NO „Isokor Polish“ (názov na webe).
from reportlab.lib.colors import CMYKColor
import baderomsrens_500ml as bad

SOURCE = 'original_SK_Furniture_Cleaner_500ml.pdf'
OUT = 'Isokor_Mobelrens_500ml_etikett_NO'

TITLE = ['MØBELRENS']
CLAIMS = ['Miljøvennlig middel for rengjøring', 'og pleie av møbler']

BODY = [
    ('ISOKOR® MØBELRENS',
     'er et miljøvennlig, naturlig middel for rengjøring av møbler med antistatiske egenskaper. Fjerner '
     'skånsomt og effektivt støv, smuss og vanskelige flekker. Egnet til alle vanlige overflater: tre (vokset '
     'eller lakkert), plast, metall, glass, marmor og akryl. Rengjør og avfetter hygienisk perfekt, gir glans '
     'og etterlater en behagelig duft. Etterlater ikke striper og riper ikke overflaten. Har antistatiske '
     'egenskaper og fjerner opptil 99,99&nbsp;% av proteinforurensning. Egnet til bruk ikke bare i hjemmet, '
     'men også i bedrifter, klubber, kafeer, utdanningsinstitusjoner, lekerom, skjønnhetssalonger og hoteller. '
     'Svært godt biologisk nedbrytbart, trygt for mennesker og husdyr. Som et av få produkter er det '
     'sertifisert med den prestisjetunge sveitsiske utmerkelsen V-Label. For langvarig hygienisk renhet '
     'anbefaler vi å polere blanke overflater etter rengjøring med Isokor Polish (finnes i vårt sortiment).'),
] + [p for p in bad.BODY if p[0] != 'Egnet til:'][1:]

FOOT = [('Best før:', ''), ('Batchnr.:', '10201FC'), ('Forbruk:', 'ca. 100 ml/m²')]

PRODUCER = {
    'head': 'Importør og distributør',
    'lines': ['Isokor Skandinavia AS', 'Org.nr. 922 112 975', 'Nærestadveien 1, 4985 Vegårshei',
              'Tlf. +47 486 42 178', 'www.isokor-skandinavia.no'],
    'tail': 'PRODUSERT I EU',
}

BROWN = CMYKColor(0.35, 0.6, 0.8, 0.25)      # podnadpis (z originálu); pás 0/50/100/0 ostáva originál
LAYOUT = {
    'regions': {
        'text':      (465, 60, 850, 442),
        'text2':     (465, 436, 618, 472),
        'logo':      (296, 96, 446, 140),
        'nazov':     (100, 185, 440, 250),
        'podnadpis': (205, 265, 440, 322),
        'vyrobca':   (476, 510, 660, 572),
    },
    'green': BROWN,
    'band': (75.5, 180.6, 449.5, 255.1),
    'claims': (438, (289.5, 312.5), 'Khand-SemiBold', 14),
    'badges': [],
    'body': (480, 833, 66, 428),
    'producer': (533, 528, 7.0, 7.3),
    'icon': (487, 570, 30),
}
