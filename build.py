import html, os, base64
CLIENTS=[('enedis','Enedis'),('totalenergies','TotalEnergies'),('securitas-direct','Securitas<br>Direct'),('region-idf','Région<br>Île‑de‑France'),('la-poste','La Poste')]
MIME={'svg':'image/svg+xml','png':'image/png','webp':'image/webp','jpg':'image/jpeg'}
def item(slug,label):
    for ext,m in MIME.items():
        p='logos/%s.%s'%(slug,ext)
        if os.path.exists(p):
            d=base64.b64encode(open(p,'rb').read()).decode()
            return '<li><img src="data:%s;base64,%s" alt="%s" loading="lazy"></li>'%(m,d,label.replace('<br>',' '))
    return '<li>%s</li>'%label
items=''.join(item(s,l) for s,l in CLIENTS)
JS="""<script>
(function(){var box=document.getElementById('arc');if(!box)return;
var base=[].slice.call(box.children);for(var k=0;k<2;k++)base.forEach(function(e){var c=e.cloneNode(true);c.setAttribute('aria-hidden','true');c.removeAttribute('role');box.appendChild(c);});var els=[].slice.call(box.children),N=els.length,reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches,off=0,last=0;
function lay(){var W=box.clientWidth,iw=els[0].offsetWidth,S=iw+6,L=Math.max(N*S,W+S*2),depth=Math.min(box.clientHeight-els[0].offsetHeight-8,W*0.09);
els.forEach(function(e,i){var x=((i*S+off)%L+L)%L-S;var c=x+iw/2;var u=(c-W/2)/(W/2);var y=4+depth*(1-u*u);var ang=-Math.atan(2*depth*u/(W/2))*180/Math.PI;
e.style.transform='translate('+x+'px,'+y.toFixed(1)+'px) rotate('+ang.toFixed(2)+'deg)';});}
function tick(t){if(!last)last=t;off+=(t-last)*0.045;last=t;lay();requestAnimationFrame(tick);}
lay();window.addEventListener('resize',lay);if(!reduce)requestAnimationFrame(tick);})();
</script>"""
REFS='<div class="arc" id="arc" role="list" aria-label="Clients">'+''.join(x.replace('<li>','<div class="arc-item" role="listitem">').replace('</li>','</div>') for x in [item(s,l) for s,l in CLIENTS])+'</div>'+JS
t=open('template.html',encoding='utf-8').read()
eng=open('engine.js',encoding='utf-8').read()
ps=open('trivoie-collecte.ps1',encoding='utf-8').read()
assert '</script' not in eng.lower()
out=t.replace('{{ENGINE}}',eng).replace('{{REFS}}',REFS).replace('{{SCRIPT}}',html.escape(ps,quote=False))
open('trivoie.html','w',encoding='utf-8').write(out)
print(len(out))
