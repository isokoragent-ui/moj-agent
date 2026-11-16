const { chromium } = require('playwright');
const out = process.argv[2] || __dirname + '/../..';
const v = process.argv[3] || '';            // 'butikk' = verzia do obchodu
const only = process.argv[4];               // napr. 'a4' = len tento formát
(async () => {
  const b = await chromium.launch();
  const sizes = { portrait: [1080, 1350], square: [1080, 1080], story: [1080, 1920], a4: [1240, 1754] };
  for (const [f, [w, h]] of Object.entries(sizes)) {
    if (only ? f !== only : f === 'a4') continue;   // A4 len na požiadanie
    const dsf = f === 'a4' ? 2 : 1;                  // A4: 2480 × 3508 px = 300 dpi
    const name = `${out}/badepakken_${v || 'jul'}_${f}`;
    const url = 'file://' + __dirname + '/jul.html?f=' + f + (v ? '&v=' + v : '');
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: dsf });
    await p.goto(url);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(600);
    await p.screenshot({ path: name + '.png' });
    if (f === 'a4') {                                // PDF na tlač, 210 × 297 mm
      const q = await b.newPage({ viewport: { width: w, height: h } });
      await q.goto(url);
      await q.evaluate(() => document.fonts.ready);
      await q.waitForTimeout(600);
      await q.pdf({ path: name + '.pdf', width: '210mm', height: '297mm', printBackground: true,
        scale: 793.7 / w, margin: { top: 0, right: 0, bottom: 0, left: 0 }, pageRanges: '1' });
    }
  }
  await b.close();
})();
