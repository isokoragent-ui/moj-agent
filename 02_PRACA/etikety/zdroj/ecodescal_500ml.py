# Isokor EcoDescal 500 ml (SK: Eco Descal) — nórske texty etikety. Všetko od výrobcu ostáva, len preklad
# (08_ROZHODNUTIA/2026-10-28_etikety_len_preklad.md). Web: „Isokor EcoDescal avkalker for vannkoker og kaffemaskin“.
# Klasifikovaný výrobok (Skin Corr. 1C H314, Eye Dam. 1 — karta Isokor_EcoDescal_Sikkerhetsdatablad_NO.pdf = LMS):
# SK etiketa má piktogram GHS05, ale nemá signálne slovo ani H/P vety → doplnené z oddielu 2.2 karty.
# Pozn.: SK text „Bez nebezpečných látok … nie je nebezpečný pri náhodnom požití“ je v rozpore s H314 — ponechané (len preklad).
from reportlab.lib.colors import CMYKColor

SOURCE = 'original_SK_Eco_Descal_500ml.pdf'
OUT = 'Isokor_EcoDescal_500ml_etikett_NO'

TITLE = ['ECODESCAL']
CLAIMS = ['Avkalkingsmiddel', 'Ideell for halv-/helautomatiske kaffemaskiner,', 'espressomaskiner og kapselmaskiner']

BODY = [
    ('ISOKOR® ECODESCAL',
     'er et avkalkingsmiddel for vannkokere, helautomatiske og halvautomatiske kaffemaskiner, laget av naturlige '
     'fruktsyrer og fruktekstrakter. Uten farlige stoffer, inneholder ingen kjente kreftfremkallende stoffer, '
     'ikke farlig ved utilsiktet svelging av en liten mengde. Fjerner raskt, effektivt, trygt, skånsomt og uten '
     'å skade vannkokeren eller kaffemaskinen kalkavleiringer i vannkokere og i hel- og halvautomatiske '
     'kaffemaskiner. Takket være fruktekstraktene gir det glans til krom- og rustfrie overflater og beskytter '
     'dem mot overdreven kalkavleiring.'),
    ('Bruksanvisning:',
     'Hell produktet i vannkokeren og vent til alle kalkavleiringer har løst seg. Prosessen kan fremskyndes med '
     'en myk børste eller ved å varme opp blandingen. Skyll deretter vannkokeren med rent vann. For hel- og '
     'halvautomatiske kaffemaskiner: følg avkalkingsanvisningen fra produsenten av maskinen. Hvis produsenten '
     'ikke oppgir en avkalkingsanvisning, hell produktet i vanntanken og fyll opp til 1&nbsp;liter. Start '
     'maskinen og la hele væskemengden gå gjennom kaffemaskinen. Skyll den tomme tanken med rent vann. Skyll '
     'maskinen med minst to fulle tanker rent vann for å fjerne rester av oppløst kalk og produkt.'),
    ('Oppbevaring:',
     'Oppbevares i lukket originalemballasje ved 5–35&nbsp;°C. Må ikke utsettes for direkte sollys. Beskyttes '
     'mot frost. Oppbevares utilgjengelig for barn. Produktet kan endre farge eller konsistens ved '
     'temperaturpåvirkning, men dette påvirker ikke egenskapene. Kun tom emballasje kan resirkuleres. '
     'Beskyttes mot frost og sollys.'),
    ('Sammensetning:', 'vann, fruktsyrer: vinsyre, oksalsyre, sitronsyre, fruktekstrakter.'),
]

FOOT = [('Best før:', ''), ('Forbruk:', 'ca. 100 ml/m²')]

# CLP — znenie podľa oddielu 2.2 bezpečnostnej karty (EcoDescal = LMS), UFI z karty aj SK etikety
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
    ('UFI:', 'W120-G081-7002-X7CT'),
]

PRODUCER = {
    'head': 'Importør og distributør',
    'lines': ['Isokor Skandinavia AS', 'Org.nr. 922 112 975', 'Nærestadveien 1, 4985 Vegårshei',
              'Tlf. +47 486 42 178', 'www.isokor-skandinavia.no'],
    'tail': 'PRODUSERT I EU',
}

STEEL = CMYKColor(0.408, 0.196, 0.147, 0.009)  # pás, podnadpis, 500ml
LAYOUT = {
    'regions': {
        'text':      (465, 60, 850, 440),
        'text2':     (465, 425, 640, 470),
        'logo':      (296, 98, 446, 144),
        'nazov':     (100, 185, 440, 250),
        'podnadpis': (210, 270, 441, 328),
        'vyrobca':   (476, 500, 650, 560),
    },
    'green': STEEL,
    'band': (73.4, 180.6, 447.4, 255.1),
    'claims': (439, (286.5, 305.8, 322), ['Khand-SemiBold', 'Khand-SemiBold', 'Khand-SemiBold'], [14, 10.2, 10.2]),
    'badges': [],
    'body': (480, 836, 66, 438),
    'clp': (480, 836, 440),
    'logo': (371, 143, 118),
    'producer': (533, 509, 7.2, 7.6),
    'icon': (487, 553, 32),
}
