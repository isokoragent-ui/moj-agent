const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  fs.mkdirSync(__dirname + '/frames', { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + __dirname + '/video_norsk.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);
  const fps = 30, dur = 14;
  for (let i = 0; i < fps * dur; i++) {
    await p.evaluate(t => window.render(t), i / fps);
    await p.screenshot({ path: `${__dirname}/frames/f${String(i).padStart(4, '0')}.jpg`, type: 'jpeg', quality: 92 });
  }
  await b.close();
})();
