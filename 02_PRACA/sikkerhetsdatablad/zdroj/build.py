import sys, os, importlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# použitie: python3 build.py <modul s textom, napr. baderomsrens>
M = importlib.import_module(sys.argv[1])
PAGES, PRODUCT, DATE = M.PAGES, M.PRODUCT, M.DATE

D = os.path.dirname(os.path.abspath(__file__))
N = len(PAGES)

CSS = """
@font-face{font-family:K;font-weight:300;src:url(Khand-Light.ttf)}
@font-face{font-family:K;font-weight:400;src:url(Khand-Regular.ttf)}
@font-face{font-family:K;font-weight:500;src:url(Khand-Medium.ttf)}
@font-face{font-family:K;font-weight:600;src:url(Khand-SemiBold.ttf)}
@font-face{font-family:K;font-weight:700;src:url(Khand-Bold.ttf)}
@page{size:A4;margin:0}
*{box-sizing:border-box}
html,body{margin:0;padding:0;background:#fff}
body{font-family:K;color:#000;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{position:relative;width:210mm;height:297mm;overflow:hidden;page-break-after:always}
.page:last-child{page-break-after:auto}
.hdr{position:absolute;top:7.6mm;left:0;width:210mm}
.wm{position:absolute;left:38mm;top:223.3mm;width:134.1mm}
.ht{position:absolute;right:12.6mm;top:12.2mm;text-align:right;color:#fff;line-height:6.35mm;font-size:12.2pt;font-weight:400}
.ht b{font-weight:600}
.sub{position:absolute;right:12.6mm;top:37.9mm;font-size:7.6pt;font-weight:500;letter-spacing:-.05pt}
.foot{position:absolute;right:25mm;top:282.2mm;font-size:14pt;font-weight:500}
.body{position:absolute;left:22.3mm;top:54mm;width:163.5mm;height:220mm;font-size:9.6pt;font-weight:300;line-height:1.45}
.body.over{outline:2px solid red}
h1{font-size:13pt;font-weight:600;margin:6mm 0 3.2mm}
h2{font-size:12pt;font-weight:600;margin:5mm 0 .6mm}
h3{font-size:11pt;font-weight:600;margin:4.2mm 0 .8mm;line-height:1.25}
.first,.body>:first-child{margin-top:0 !important}
.gap{margin-top:6mm}
.gap2{margin-top:8mm}
h3.inline{display:inline-block;margin:4mm 6mm 2mm 0}
.iv{font-size:10.5pt;font-weight:400}
p{margin:0}
p.sp{margin:2.6mm 0 0}
p.tight{margin:.4mm 0 0}
p.small{margin-top:2mm;font-size:9pt}
p.lbl{font-weight:400;font-size:10.2pt;margin-top:3.4mm;line-height:1.3}
p.lbl.s{font-size:9.6pt}
p.lbl.m{font-size:11pt}
p.it,.it{font-style:italic}
p.light{font-weight:300}
p.u,.u{text-decoration:underline}
p.b{font-weight:600}
.k{font-weight:400}
.just{text-align:justify}
.lh{line-height:1.95}
.ref{font-style:italic;text-decoration:underline;font-weight:700;font-size:12pt}
table{border-collapse:collapse;font-weight:600;font-size:9.4pt;line-height:1.25;text-align:center}
td{border:1px solid #555;padding:1.2mm 1.6mm}
table.props{margin:5mm 0 0 3.2mm;width:154.5mm}
table.props td{width:50%;padding:1.3mm 2mm}
table.props i{font-weight:600}
table.tox{margin:12mm 0 0 3.6mm;width:155mm}
table.tox td{height:13.4mm;padding:1mm 2mm}
table.tox td:first-child{width:47%}
table.abbr{margin:5mm 0 0 3.2mm;width:154mm;font-size:9pt}
table.abbr td{padding:1mm 2mm}
table.abbr td:first-child{width:18mm}
ol.laws{margin:3.4mm 0 0;padding-left:5.8mm;line-height:1.75}
ol.laws li{margin:0 0 1.9mm;padding-left:.8mm}
""" + getattr(M, "EXTRA_CSS", "")

def page(i, html):
    return f"""<div class="page">
<img class="wm" src="watermark.jpg">
<img class="hdr" src="header.jpg">
<div class="ht"><b>Sikkerhetsdatablad</b><br>{PRODUCT}<br>Utgivelsesdato: {DATE}<br>NO versjon: 1.0</div>
<div class="sub">Dette sikkerhetsdatabladet er i samsvar med forordning (EF) nr. 1907/2006 av 18.12.2006 – REACH og forordning (EU) 2020/878 av 18.6.2020.</div>
<div class="body">{html}</div>
<div class="foot">Side {i} av {N}</div>
</div>"""

doc = f"""<!doctype html><html lang="nb"><head><meta charset="utf-8">
<title>Sikkerhetsdatablad – {PRODUCT}</title>
<style>{CSS}</style></head><body>
{''.join(page(i+1, h) for i, h in enumerate(PAGES))}
</body></html>"""
html_path = os.path.join(D, sys.argv[1] + ".html")
open(html_path, "w", encoding="utf-8").write(doc)

print("html", html_path)
