# Vipps QR pre ISOKOR-SKANDINAVIA AS (#62769) — vektorové SVG
# Odkaz prečítaný z Vipps appky (fotka 17. 11. 2026). Zmeň len, ak Vipps vydá nový kód.
import segno, pathlib
URL = 'https://qr.vipps.no/vp/naP8rFUcM'
q = segno.make(URL, error='h', micro=False)
q.save(pathlib.Path(__file__).with_name('qr.svg'), scale=1, border=0, dark='#000', light=None,
       xmldecl=False, omitsize=True)
print('QR verzia', q.version, 'oprava chýb', q.error, '→ qr.svg')
