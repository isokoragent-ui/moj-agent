const { chromium } = require('playwright');
const out = process.argv[2] || __dirname + '/../..';
const v = process.argv[3] || '';  // 'butikk' = verzia do obchodu
(async () => {
  const b = await chromium.launch();
  const sizes = { portrait: [1080, 1350], square: [1080, 1080], story: [1080, 1920] };
  for (const [f, [w, h]] of Object.entries(sizes)) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto('file://' + __dirname + '/norsk.html?f=' + f + (v ? '&v=' + v : ''));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(600);
    await p.screenshot({ path: `${out}/kjokkenpakken_${v || 'norsk'}_${f}.png` });
  }
  await b.close();
})();
