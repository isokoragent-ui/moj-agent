// Vipps plagát: PNG A5 300 dpi + PDF A5 a A4 (vektor)  →  node render.js
const { chromium } = require('playwright');
const out = __dirname + '/..', W = 874, H = 1240;
(async () => {
  const b = await chromium.launch();
  const url = 'file://' + __dirname + '/vipps.html';
  const p = await b.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 2 });
  await p.goto(url); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
  await p.screenshot({ path: out + '/vipps_qr_a5.png' });              // 1748 × 2480 px
  const q = await b.newPage({ viewport: { width: W, height: H } });
  await q.goto(url); await q.evaluate(() => document.fonts.ready); await q.waitForTimeout(500);
  const pdf = (name, wmm, hmm) => q.pdf({ path: `${out}/${name}`, width: wmm + 'mm', height: hmm + 'mm',
    printBackground: true, scale: (wmm / 25.4 * 96) / W, margin: { top: 0, right: 0, bottom: 0, left: 0 }, pageRanges: '1' });
  await pdf('vipps_qr_a5.pdf', 148, 210);
  await pdf('vipps_qr_a4.pdf', 210, 297);
  await b.close();
})();
