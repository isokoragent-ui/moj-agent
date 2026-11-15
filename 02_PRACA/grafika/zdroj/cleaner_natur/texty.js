// Texty videa v2 ako priehľadné PNG 1080×1920: node texty.js → texty/t1.png …
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const out = __dirname + '/texty';
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
  await p.goto('file://' + __dirname + '/texty.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(600);
  for (const id of ['t1', 't2', 't3', 't4', 't5a', 't5b', 't6', 't7']) {
    await p.evaluate(id => document.querySelectorAll('.t').forEach(e => e.style.display = e.id === id ? 'block' : 'none'), id);
    await p.screenshot({ path: `${out}/${id}.png`, omitBackground: true });
  }
  await b.close();
})();
