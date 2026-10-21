import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
const b = await chromium.launch();
for (const [f,w,h,out] of [['social_1x1.html',1080,1080,'Messekupp_Instagram_1x1'],['social_9x16.html',1080,1920,'Messekupp_TikTok_9x16']]) {
  const p = await b.newPage({ viewport:{width:w,height:h}, deviceScaleFactor:1 });
  await p.goto('file://'+process.cwd()+'/'+f); await p.waitForLoadState('networkidle');
  await p.evaluate(() => document.fonts.ready);
  await p.screenshot({ path: out+'.jpg', type:'jpeg', quality:95 });
  await p.close();
}
await b.close();
