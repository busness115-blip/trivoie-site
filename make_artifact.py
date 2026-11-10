# Génère artifact-home.html : trivoie.html + section guides et pied de page de l'accueil du site,
# avec des liens absolus vers https://trivoie.fr. À lancer après build.py et site/build_site.py.
import re
D = "https://trivoie.fr"
absol = lambda h: re.sub(r'href="/(?!/)', 'href="%s/' % D, h)
t = open("trivoie.html", encoding="utf-8").read()
idx = open("site/out/index.html", encoding="utf-8").read()
gsec = re.search(r'<section class="guides-home".*?</section>', idx, re.S).group(0)
navs = re.search(r'<nav aria-label="Guides">.*?</nav><nav aria-label="Informations">.*?</nav>', idx, re.S).group(0)
css = re.search(r'footer nav \{.*?\.gh-grid span \{[^}]*\}\n', idx, re.S).group(0)
assert t.count("<footer>") == 1 and t.count('<footer>\n  <div class="wrap">') == 1
t = t.replace("<footer>", absol(gsec) + "\n<footer>", 1)
t = t.replace('<footer>\n  <div class="wrap">', '<footer>\n  <div class="wrap">\n    ' + absol(navs), 1)
t = t.replace("</style>", css + "</style>", 1)
open("artifact-home.html", "w", encoding="utf-8").write(t)
print("artifact-home.html", len(t), "liens guides :", len(re.findall(r'<nav aria-label="Guides">.*?</nav>', t, re.S)[0].split("<a ")) - 1)
