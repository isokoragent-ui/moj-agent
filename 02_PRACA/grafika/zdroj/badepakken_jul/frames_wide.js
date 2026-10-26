const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const dir = __dirname + '/frames_wide';
  fs.mkdirSync(dir, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://' + __dirname + '/video_wide.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(800);
  const fps = 30, dur = 13;
  for (let i = 0; i < fps * dur; i++) {
    await p.evaluate(t => window.render(t), i / fps);
    await p.screenshot({ path: `${dir}/f${String(i).padStart(4, '0')}.jpg`, type: 'jpeg', quality: 92 });
  }
  await b.close();
})();
