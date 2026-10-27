const { chromium } = require('playwright');
(async () => {
  const [html, out] = process.argv.slice(2);
  const b = await chromium.launch(); const pg = await b.newPage();
  await pg.goto('file://' + html); await pg.evaluate(() => document.fonts.ready);
  const r = await pg.evaluate(() => [...document.querySelectorAll('.body')].map((e,i)=>{
    const mm=(e.lastElementChild.getBoundingClientRect().bottom-e.getBoundingClientRect().top)/3.7795;
    if (mm > e.clientHeight/3.7795) e.classList.add('over'); return (i+1)+':'+mm.toFixed(0)}));
  console.log('content mm (max 220):', r.join(' '));
  await pg.pdf({ path: out, printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
