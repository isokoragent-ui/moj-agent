// Texty videa ako priehľadné PNG: node texty.js → texty/ (1080×1920);  WIDE=1 node texty.js → texty_wide/ (1920×1080)
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const out = __dirname + '/' + (process.env.WIDE ? 'texty_wide' : 'texty');
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: process.env.WIDE ? 1920 : 1080, height: process.env.WIDE ? 1080 : 1920 } });
  await p.goto('file://' + __dirname + '/' + (process.env.WIDE ? 'texty_wide.html' : 'texty.html') + '');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(600);
  for (const id of ['t1', 't2', 't3', 't4', 't5a', 't5b', 't6', 't7']) {
    await p.evaluate(id => document.querySelectorAll('.t').forEach(e => e.style.display = e.id === id ? 'block' : 'none'), id);
    await p.screenshot({ path: `${out}/${id}.png`, omitBackground: true });
  }
  await b.close();
})();
