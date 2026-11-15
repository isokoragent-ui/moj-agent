// Snímky videa: node frames.js  (OUT=priečinok, KONTROLA=časy oddelené čiarkou → len vybrané snímky)
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const out = process.env.OUT || __dirname + '/frames';
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + __dirname + '/video.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);
  const fps = 30, dur = 15;
  const times = process.env.KONTROLA ? process.env.KONTROLA.split(',').map(Number) : [...Array(fps * dur).keys()].map(i => i / fps);
  for (let i = 0; i < times.length; i++) {
    await p.evaluate(t => window.render(t), times[i]);
    await p.screenshot({ path: `${out}/f${String(i).padStart(4, '0')}.jpg`, type: 'jpeg', quality: 92 });
  }
  await b.close();
})();
