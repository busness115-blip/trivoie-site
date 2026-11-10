const {chromium,devices}=require("playwright");
const S="/tmp/claude-0/-home-claude/7c3dd704-d93f-5862-9b02-08c7eba755a8/scratchpad/";
const pages=require("fs").readFileSync(""+(process.env.SITE_OUT||"site/out")+"/sitemap.xml","utf8").match(/<loc>[^<]*<\/loc>/g).map(x=>x.replace(/<\/?loc>/g,"").replace("https://trivoie.fr","")).concat(["/404.html"]);
(async()=>{const b=await chromium.launch();let bad=0;
for(const [n,o] of [["desk",{viewport:{width:1280,height:900}}],["ios",{...devices["iPhone 13"]}]]){
 const c=await b.newContext(o);
 for(const u of pages){const p=await c.newPage();const errs=[];
  p.on("pageerror",e=>errs.push("js:"+e.message));p.on("console",m=>{if(m.type()==="error")errs.push("console:"+m.text())});p.on("requestfailed",r=>errs.push("req:"+r.url()));
  const r=await p.goto("http://127.0.0.1:8099"+u);await p.waitForTimeout(400);
  const w=await p.evaluate(()=>document.documentElement.scrollWidth);const vw=o.viewport?o.viewport.width:390;
  const ld=await p.evaluate(()=>[...document.querySelectorAll('script[type="application/ld+json"]')].map(s=>{try{JSON.parse(s.textContent);return 1}catch(e){return 0}}));
  const fonts=await p.evaluate(()=>[...document.fonts].filter(f=>f.status==="loaded").map(f=>f.family+f.weight).join(","));
  const h1=await p.evaluate(()=>document.querySelectorAll("h1").length);
  const ok=errs.length===0&&w<=vw&&ld.every(x=>x)&&h1===1;if(!ok)bad++;
  console.log(n,u,r.status(),"w",w,"ld",ld.join(""),"h1",h1,errs.length?errs.slice(0,3):"", ok?"OK":"PROBLEME");
  if(u==="/"&&n==="desk")console.log("fonts:",fonts);
  if(n==="ios"&&(u==="/"||u.includes("fin-maint")||u.includes("query")))await p.screenshot({path:S+"site-"+(u==="/"?"home":u.split("/")[1].slice(0,8))+"-ios.png"});
  if(n==="desk"&&u.includes("diagnostic"))await p.screenshot({path:S+"site-diag-desk.png",fullPage:false});
  await p.close();}
 await c.close();}
console.log("problemes:",bad);await b.close();})();
