// node render.js → antidugg_hylle_a5.pdf + .png (300 dpi) do 02_PRACA/grafika/
const { chromium } = require('playwright');
const out = __dirname + '/../..';
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 559, height: 794 }, deviceScaleFactor: 300 / 96 * 559.37 / 559 });
  await p.goto('file://' + __dirname + '/hylle.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);
  await p.screenshot({ path: out + '/antidugg_hylle_a5.png' });
  await p.pdf({ path: out + '/antidugg_hylle_a5.pdf', width: '148mm', height: '210mm', printBackground: true });
  await b.close();
})();
