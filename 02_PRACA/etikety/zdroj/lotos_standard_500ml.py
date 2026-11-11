# Isokor Lotos Standard 500 ml (SK: Lotos Standard) — nórske texty etikety. Všetko od výrobcu ostáva, len preklad
# (08_ROZHODNUTIA/2026-10-28_etikety_len_preklad.md).
# Klasifikovaný výrobok (Flam. Liq. 2 H225, Eye Irrit. 2 H319, STOT SE 3 H336 — karta Lotos Standard = SW):
# SK etiketa má piktogramy GHS02 + GHS07 a UFI, ale nemá signálne slovo ani H/P vety → doplnené z oddielu 2.2 karty.
from reportlab.lib.colors import CMYKColor
from reportlab.pdfbase import pdfmetrics

SOURCE = 'original_SK_Lotos_Standard_500ml.pdf'
OUT = 'Isokor_Lotos_Standard_500ml_etikett_NO'

TITLE = ['LOTOS STANDARD']
CLAIMS = ['Nanometrisk impregnering', 'for sko, tekstiler og klær']

BODY = [
    ('ISOKOR® LOTOS STANDARD',
     'er beregnet til impregnering av nesten alle typer ikke-impregnerte tekstiler, ekte og kunstig ulakkert '
     'og slipt skinn, semsket skinn og papir. Effektiv vannavstøtende impregnering av sko, klær og tekstiler '
     'av alle slag, stoppede møbler og telt. Produktet danner et usynlig nanobelegg som dekker overflaten og '
     'beskytter mot smuss og vann. Overflaten blir motstandsdyktig mot vann, gjørme, snø, veisalt og annen '
     'tilsmussing. Materialet frastøter vannmolekyler og forlenger materialets levetid og tiden mellom '
     'rengjøringene betydelig. Til alle typer ikke-impregnerte tekstiler.'),
    ('Bruksanvisning:',
     'Rengjør overflaten grundig før behandling. Overflaten skal være ren, tørr og avfettet. Rist produktet '
     'i ca. 10&nbsp;sekunder før bruk og spray det jevnt på ønsket overflate fra en avstand på ca. '
     '15–20&nbsp;cm til den blir fuktig. Tørketiden er ca. 60&nbsp;minutter. Denne fremgangsmåten kan øke '
     'impregneringens effekt. Impregner ved temperatur 5–30&nbsp;°C. Etter ca. 12 til 24&nbsp;timer er '
     'overflaten fullt funksjonell, og impregneringen får lengre holdbarhet. Nøyaktig teknologisk '
     'fremgangsmåte for industriell bruk får du fra produsenten på forespørsel.'),
    ('OBS!',
     'Hvis du ikke er sikker på om materialet allerede er impregnert, må produktet prøves på et lite område '
     'av materialet på innsiden av klesplagget eller skoen. Er det tvil om materialet er forhåndsimpregnert, '
     'bør produktet først prøves. Hvis det dannes et hvitt belegg på materialet, skal produktet ikke brukes, '
     'fordi det betyr at materialet allerede er impregnert. Hvis det dannes bobler på overflaten under '
     'impregneringen, fjern dem forsiktig med en bomullsklut eller et papirhåndkle (ikke gni). Produktet er '
     'klart til bruk. Må ikke fortynnes eller blandes med andre stoffer!'),
    ('Oppbevaring:',
     'Oppbevares utilgjengelig for barn. Holdes borte fra åpen flamme. Eventuelle rester leveres som farlig '
     'avfall. Transport og oppbevaring kun i originalemballasjen. Kun tom emballasje kan resirkuleres. Etter '
     'åpning oppbevares produktet i originalemballasjen i maks. 6&nbsp;måneder.'),
    ('Sikkerhetstiltak:',
     'Følg vanlige sikkerhetstiltak for arbeid med kjemiske produkter. Inneholder lett antennelige stoffer. '
     'Meget brannfarlig. Det må ikke være åpen flamme i nærheten under påføring. Hold beholderen tett lukket '
     'og borte fra antennelseskilder. Røyking forbudt. Sørg for god ventilasjon under arbeidet. Irriterer '
     'øynene. Damp kan gi døsighet og svimmelhet. Unngå kontakt med hud og øyne. Ved hudkontakt: skyll med '
     'rikelig vann. Ved øyekontakt: skyll med store mengder rent vann og kontakt lege. Ved svelging: ikke '
     'fremkall brekninger, men drikk rikelig med vann og kontakt lege straks. Oppbevares utilgjengelig for barn.'),
    ('Sammensetning:',
     'isopropanol, modifiserte hybride stoffer, tilsetningsstoffer. Merket i samsvar med dekret '
     'nr. 415/2012 Coll.'),
]

FOOT = [('VOC-grense:', '750 g/l. Maks. VOC-innhold i produktet: 745 g/l (A+B-elementer)'),
        ('Best før:', 'Se emballasjen.'),
        ('Forbruk:', 'ca. 100 ml / 1–2 m²'),
        ('UFI:', '4K30-K0P5-Q00Y-UCV3')]

# CLP — znenie podľa oddielu 2.2 bezpečnostnej karty (Lotos Standard = SW); UFI je už vo FOOT (ako v origináli)
CLP = [
    ('FARE', ''),
    ('Inneholder:', 'isopropylalkohol (propan-2-ol).'),
    ('H225', 'Meget brannfarlig væske og damp.'),
    ('H319', 'Gir alvorlig øyeirritasjon.'),
    ('H336', 'Kan forårsake døsighet eller svimmelhet.'),
    ('P102', 'Oppbevares utilgjengelig for barn.'),
    ('P210', 'Holdes vekk fra varme, varme overflater, gnister, åpen flamme og andre antennelseskilder. '
             'Røyking forbudt.'),
    ('P261', 'Unngå innånding av tåke/damp/aerosoler.'),
    ('P305+P351+P338', 'VED KONTAKT MED ØYNENE: Skyll forsiktig med vann i flere minutter. Fjern eventuelle '
                       'kontaktlinser dersom dette enkelt lar seg gjøre. Fortsett skyllingen.'),
    ('P501', 'Innhold/beholder leveres i samsvar med nasjonale forskrifter.'),
]

PRODUCER = {
    'head': 'Importør og distributør',
    'lines': ['Isokor Skandinavia AS', 'Org.nr. 922 112 975', 'Nærestadveien 1, 4985 Vegårshei',
              'Tlf. +47 486 42 178', 'www.isokor-skandinavia.no'],
    'tail': 'PRODUSERT I EU',
}

BLUE = CMYKColor(0.902, 0.549, 0.085, 0.003)   # pás, podnadpis (z originálu)
TEAL = CMYKColor(0.8, 0.1, 0.45, 0)            # odznak 99 %
WHITE = CMYKColor(0, 0, 0, 0)

def _fit(t, font, size, width_px):
    while pdfmetrics.stringWidth(t, font, size) > width_px * 0.72:
        size -= 0.1
    return round(size, 1)

def _claim(t, size):
    return _fit(t, 'Khand-SemiBold', size, 262)

LAYOUT = {
    'regions': {
        'text':      (465, 58, 852, 406),     # telo až po riadok „Zloženie“ (vpravo pod ním je ikona 6M)
        'text2':     (465, 400, 776, 446),    # Limit VOC, Dátum spotreby, Výdatnosť, UFI
        'logo':      (285, 96, 446, 148),
        'nazov':     (100, 185, 440, 250),
        'podnadpis': (170, 262, 442, 322),
        'vode':      (370, 360, 414, 392),    # biely text VODE ODOLNÝ (modrý podklad a kvapky ostávajú)
        'priedus':   (366, 443, 419, 457),    # PRIEDUŠNOSŤ (99 % a oblúk ostávajú)
        'vyrobca':   (476, 500, 660, 560),
    },
    'green': BLUE,
    'band': (75.5, 180.6, 449.5, 255.1),
    'title_max': 40,
    'claims': (438, (288.5, 316.5), 'Khand-SemiBold',
               [_claim(CLAIMS[0], 19), _claim(CLAIMS[1], 17)]),
    'badges': [],
    'texts': [
        ('VANN', 392, 377.5, 'Khand-Bold', 13.5, WHITE, 'c'),
        ('AVSTØTENDE', 392, 388, 'Khand-Bold', _fit('AVSTØTENDE', 'Khand-Bold', 8, 48), WHITE, 'c'),
        ('PUSTEEVNE', 392.5, 453.5, 'Khand-Bold', _fit('PUSTEEVNE', 'Khand-Bold', 9, 50), TEAL, 'c'),
    ],
    'body': (480, 840, 64, 400),
    'clp': (480, 772, 450),     # pod tým sú piktogramy (od 455 px)
    'producer': (533, 512, 7.2, 7.6),
    'icon': (487, 556, 32),
}
