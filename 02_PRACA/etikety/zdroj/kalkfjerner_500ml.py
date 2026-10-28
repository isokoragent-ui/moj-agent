# Isokor Kalkfjerner for bad 500 ml (SK: LM Descaling) — nórske texty etikety. Všetko od výrobcu ostáva, len preklad
# (08_ROZHODNUTIA/2026-10-28_etikety_len_preklad.md).
# Klasifikovaný výrobok (Skin Corr. 1C H314, Eye Dam. 1 — karta Isokor_LMD_Sikkerhetsdatablad_NO.pdf = LMS):
# SK etiketa má piktogram GHS05, ale nemá signálne slovo, H/P vety ani „Inneholder“ → doplnené z oddielu 2.2 karty.
from reportlab.lib.colors import CMYKColor

SOURCE = 'original_SK_LM_Descaling_500ml.pdf'
OUT = 'Isokor_Kalkfjerner_for_bad_500ml_etikett_NO'

TITLE = ['KALKFJERNER']
CLAIMS = ['Fjerner kalk og kalkbelegg', 'bad, sanitær, wellness, kjøkken']

BODY = [
    ('ISOKOR® KALKFJERNER',
     'er et effektivt rengjøringsmiddel for fuger og dusjhjørner som fjerner kalk og kalkavleiringer fra '
     'veggfliser, gulvfliser, badekar, dusjkabinett, servant, badstue, wellnessområder, kjøkkenbenk og andre '
     'overflater der det avsettes kalk.'),
    ('Bruksanvisning:',
     'Rist i minst 5&nbsp;sekunder før bruk. Fjern grovt smuss mekanisk. Påfør på tørr overflate og la virke '
     'i 1–5&nbsp;minutter avhengig av hvor skitten overflaten er. Ved kraftigere tilsmussing: bruk en myk '
     'børste for å løsne smusset i fuger og på andre overflater. Skyll med vann og gjenta ved behov til alt '
     'smuss og kalk er fjernet. Brukes ved temperatur mellom 5 og 30&nbsp;°C.'),
    ('Oppbevaring:',
     'Oppbevares i lukket originalemballasje ved 5–35&nbsp;°C. Brukes innen 3 år fra produksjonsdato.'),
    ('Sikkerhetstiltak:',
     'Ved hudkontakt gir produktet mild irritasjon. Hudkontakt: ta av forurenset tøy og vask huden med vann. '
     'Ved kontakt med øynene gir produktet alvorlig irritasjon. Unngå kontakt med øynene. Ved øyekontakt: '
     'fjern eventuelle kontaktlinser hvis mulig, hold øynene åpne og skyll med rennende rent vann i flere '
     'minutter, og kontakt lege. Oppbevares utilgjengelig for barn. Oppbevares i originalemballasjen, tett '
     'lukket. Unngå innånding av damp. Innånding: flytt personen ut i frisk luft og legg i stabilt sideleie. '
     'Kontakt lege ved vedvarende plager. Svelging: skyll munnen. Ikke fremkall brekninger. Drikk rikelig '
     'med vann og kontakt lege. Produktet er klart til bruk. Må ikke blandes med andre stoffer. Innhold og '
     'tom emballasje skal leveres som farlig avfall. Kun tom emballasje kan resirkuleres.'),
    ('Sammensetning:', 'vann, syreblanding, tensider, tilsetningsstoffer.'),
]

FOOT = [('Forbruk:', 'ca. 100 ml/m²'), ('Best før:', ''), ('Batchnr.:', '')]

# CLP — znenie podľa oddielu 2.2 bezpečnostnej karty (LMS/LMD)
CLP = [
    ('FARE', ''),
    ('Inneholder:', 'melkesyre.'),
    ('H314', 'Gir alvorlige etseskader på hud og øyne.'),
    ('P102', 'Oppbevares utilgjengelig for barn.'),
    ('P260', 'Ikke innånd damp/aerosoler.'),
    ('P280', 'Benytt vernehansker/verneklær/vernebriller/ansiktsskjerm.'),
    ('P301+P330+P331', 'VED SVELGING: Skyll munnen. IKKE framkall brekninger.'),
    ('P305+P351+P338', 'VED KONTAKT MED ØYNENE: Skyll forsiktig med vann i flere minutter. Fjern eventuelle '
                       'kontaktlinser dersom dette enkelt lar seg gjøre. Fortsett skyllingen.'),
    ('P310', 'Kontakt umiddelbart et GIFTINFORMASJONSSENTER/lege.'),
    ('P501', 'Innhold/beholder leveres i samsvar med nasjonale forskrifter.'),
    ('UFI:', '7S10-Y05U-900K-X6MM'),
]

PRODUCER = {
    'head': 'Importør og distributør',
    'lines': ['Isokor Skandinavia AS', 'Org.nr. 922 112 975', 'Nærestadveien 1, 4985 Vegårshei',
              'Tlf. +47 486 42 178', 'www.isokor-skandinavia.no'],
    'tail': 'PRODUSERT I EU',
}

TEAL = CMYKColor(0.82, 0.208, 0.424, 0.012)  # pás, podnadpis, 500ml
MINT = CMYKColor(0.716, 0, 0.336, 0)         # odznak „effektiv rengjøring“
WHITE = CMYKColor(0, 0, 0, 0)
LAYOUT = {
    'regions': {
        'text':      (465, 60, 850, 436),     # telo je živý text (jeden blok od 482,78); nižšie sú ikony
        'logo':      (296, 96, 446, 140),
        'nazov':     (100, 185, 440, 250),
        'podnadpis': (210, 270, 440, 318),
        'bez':       (383, 353, 413, 371),    # biely text BEZ KARTÁČOVANIA (podklad a hubka ostávajú)
        'ucinne':    (398, 397, 423, 413),    # ÚČINNÉ ČISTENIE
        'vyrobca':   (476, 500, 650, 560),
    },
    'green': TEAL,
    'band': (75.5, 180.6, 449.5, 255.1),
    'claims': (438.5, (287, 312.5), 'Khand-SemiBold', 13),
    'badges': [],
    'texts': [
        ('UTEN', 384.5, 364, 'Khand-Bold', 9, WHITE, 'l'),
        ('BØRSTING', 384.5, 369.8, 'Khand-Bold', 5, WHITE, 'l'),
        ('EFFEKTIV', 410.6, 405, 'Khand-SemiBold', 6, MINT, 'c'),
        ('RENGJØRING', 410.6, 412.2, 'Khand-SemiBold', 6, MINT, 'c'),
    ],
    'body': (480, 833, 66, 432),
    'clp': (480, 833, 436),
    'producer': (533, 509, 7.2, 7.6),
    'icon': (487, 553, 32),
}
