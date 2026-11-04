// node render_pres.js <priečinok> → Isokor_Julebytte_presentasjon.pdf + JPG každej strany
const { chromium } = require('playwright');
const out = process.argv[2] || __dirname + '/../../julebytte';
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://' + __dirname + '/presentasjon.html');
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(600);
  await p.pdf({ path: `${out}/Isokor_Julebytte_presentasjon.pdf`, width: '1920px', height: '1080px', printBackground: true });
  const pages = await p.$$('section.page');
  for (const [i, el] of pages.entries()) {
    await el.screenshot({ path: `${out}/julebytte_presentasjon_${i + 1}.jpg`, type: 'jpeg', quality: 90 });
  }
  await b.close();
})();
