const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const sizes = { banner: [2000, 640], square: [1080, 1080], mobile: [1080, 1350] };
  for (const [f, [w, h]] of Object.entries(sizes)) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto('file://' + __dirname + '/frakt.html?f=' + f);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(500);
    await p.screenshot({ path: `/home/user/moj-agent/02_PRACA/grafika/frakt_${f}.png` });
  }
  await b.close();
})();
