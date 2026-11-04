// node render.js <výstupný priečinok>  → karusel 1–6 (1080×1350), story 1 + 6 (1080×1920)
// VIDEO=1 node render.js karusel_video  → slajdy pre video (bez čísel strán)
const { chromium } = require('playwright');
const out = process.argv[2] || __dirname + '/../../julebytte';
require('fs').mkdirSync(out, { recursive: true });
(async () => {
  const b = await chromium.launch();
  const jobs = [];
  if (process.env.VIDEO) { // slajdy pre video zo karuselu: bez „n / 6“ a „Bla videre“
    for (let s = 1; s <= 6; s++) jobs.push([`julebytte_karusel_${s}.jpg`, `s=${s}&single=1`, 1080, 1350]);
  } else {
  for (let s = 1; s <= 6; s++) jobs.push([`julebytte_karusel_${s}.jpg`, `s=${s}`, 1080, 1350]);
  jobs.push(['julebytte_post_1080x1350.jpg', 's=1&single=1', 1080, 1350]);
  jobs.push(['julebytte_story_1.jpg', 's=1&f=story', 1080, 1920]);
  jobs.push(['julebytte_story_2.jpg', 's=6&f=story', 1080, 1920]);
  }
  for (const [name, qs, w, h] of jobs) {
    const p = await b.newPage({ viewport: { width: w, height: h } });
    await p.goto('file://' + __dirname + '/karusel.html?' + qs);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(500);
    await p.screenshot({ path: `${out}/${name}`, type: 'jpeg', quality: 92 });
    await p.close();
  }
  await b.close();
})();
