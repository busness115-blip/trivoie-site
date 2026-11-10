const {chromium,devices}=require("playwright");const fs=require("fs");
const axe=fs.readFileSync("/tmp/axe/node_modules/axe-core/axe.min.js","utf8");
const pages=require("fs").readFileSync(""+(process.env.SITE_OUT||"site/out")+"/sitemap.xml","utf8").match(/<loc>[^<]*<\/loc>/g).map(x=>x.replace(/<\/?loc>/g,"").replace("https://trivoie.fr","")).concat(["/404.html"]);
(async()=>{const b=await chromium.launch();
for(const [n,o] of [["desk",{viewport:{width:1280,height:900}}],["ios",{...devices["iPhone 13"]}],["desk-dark",{viewport:{width:1280,height:900},colorScheme:"dark"}],["ios-dark",{...devices["iPhone 13"],colorScheme:"dark"}]]){
 const c=await b.newContext(o);
 for(const u of pages){const p=await c.newPage();await p.goto("http://127.0.0.1:8099"+u);await p.waitForTimeout(500);
  await p.evaluate(axe);const r=await p.evaluate(async()=>{const x=await axe.run({runOnly:["wcag2a","wcag2aa","wcag21a","wcag21aa","wcag22aa","best-practice"]});return x.violations.map(v=>v.id+" ("+v.impact+") x"+v.nodes.length+" "+v.nodes[0].target.join(" ").slice(0,80))});
  const m=await p.evaluate(()=>({t:document.title.length,d:(document.querySelector('meta[name=description]')||{}).content?.length||0,can:!!document.querySelector('link[rel=canonical]'),lang:document.documentElement.lang,imgNoAlt:[...document.images].filter(i=>!i.hasAttribute('alt')).length,small:[...document.querySelectorAll('a,button')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&(r.height<24||r.width<24)}).length}));
  console.log(n,u,JSON.stringify(m),r.length?r:"axe OK");await p.close()}
 await c.close()}
await b.close()})();
