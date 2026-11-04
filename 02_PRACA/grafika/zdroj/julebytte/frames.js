// OUT=<priečinok> [WIDE=1] [PREVIEW=1] node frames.js  → snímky videa (30 fps, 16 s)
const { chromium } = require('playwright');
const fs = require('fs');
const OUT = process.env.OUT || __dirname + '/frames';
fs.mkdirSync(OUT, { recursive: true });
(async () => {
  const b = await chromium.launch();
  const wide = !!process.env.WIDE;
  const p = await b.newPage({ viewport: { width: wide ? 1920 : 1080, height: wide ? 1080 : 1920 } });
  await p.goto('file://' + __dirname + '/video.html' + (wide ? '?f=wide' : ''));
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);
  const fps = 30, dur = 16;
  const times = process.env.PREVIEW ? [2, 3.6, 5.8, 10.5, 15] : Array.from({ length: fps * dur }, (_, i) => i / fps);
  for (const [i, t] of times.entries()) {
    await p.evaluate(t => window.render(t), t);
    await p.screenshot({ path: `${OUT}/f${String(i).padStart(4, '0')}.jpg`, type: 'jpeg', quality: 92 });
  }
  await b.close();
})();
