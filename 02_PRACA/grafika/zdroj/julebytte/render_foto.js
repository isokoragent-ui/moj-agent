// node render_foto.js <priečinok> [video]  → julebytte_foto_1…6.jpg (1080×1350); „video" = bez „n / 6"
const { chromium } = require('playwright');
const out = process.argv[2] || __dirname + '/../../julebytte';
const video = process.argv[3] === 'video';
require('fs').mkdirSync(out, { recursive: true });
(async () => {
  const b = await chromium.launch();
  for (let s = 1; s <= 6; s++) {
    const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
    await p.goto('file://' + __dirname + '/fotokarusel.html?s=' + s + (video ? '&single=1' : ''));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(500);
    await p.screenshot({ path: `${out}/julebytte_foto_${s}.jpg`, type: 'jpeg', quality: 92 });
    await p.close();
  }
  await b.close();
})();
