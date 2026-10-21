import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const p = await b.newPage({ viewport:{width:794,height:1123}, deviceScaleFactor:3 });
await p.goto('file://'+process.cwd()+'/messekupp_v4.html'); await p.waitForLoadState('networkidle');
await p.evaluate(() => document.fonts.ready);
await p.pdf({ path:'Messekupp_A4_v4.pdf', format:'A4', printBackground:true });
await p.screenshot({ path:'Messekupp_A4_v4.png' });
await b.close();
