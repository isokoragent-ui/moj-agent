const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  for (const v of ['', 'paminnelse']) {
    const p = await b.newPage({ viewport: { width: 1200, height: 1000 } });
    await p.goto('file://' + __dirname + '/bf.html?' + v);
    await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(600);
    await p.screenshot({ path: __dirname + '/../../black_friday_2026_email' + (v ? '_' + v : '') + '.png' });
  }
  await b.close();
})();
