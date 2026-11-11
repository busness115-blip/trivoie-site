"""Construit le site statique Trivoie (dossier site/out) pour hébergement OVH.
Usage : python3 site/build_site.py [https://trivoie.fr]
Prérequis : python3 build.py (génère trivoie.html) et polices dans site/fonts_src."""
import html, json, os, re, shutil, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from pages import PAGES, SOURCES_BLOCK
from pages2 import PAGES2
PAGES = PAGES + PAGES2
# Pages ajoutées au fil du temps : site/content/*.py, chacun définit un dict PAGE (mêmes clés que pages2.py, plus published/modified en AAAA-MM-JJ)
import glob
for _f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "content", "*.py"))):
    _ns = {}
    exec(compile(open(_f, encoding="utf-8").read(), _f, "exec"), _ns)
    PAGES.append(_ns["PAGE"])
# Maillage interne vers les pages ajoutées
EXTRA_RELATED = {
    "fin-maintenance-sap-businessobjects-4-3": ["sap-businessobjects-bi-2027", "migration-businessobjects-power-bi"],
    "bi-2025-ou-sortir-de-businessobjects": ["sap-businessobjects-bi-2027", "alternatives-sap-businessobjects", "migration-businessobjects-power-bi"],
    "diagnostic-sortie-businessobjects": ["audit-sap-businessobjects", "consultant-sap-businessobjects"],
    "nettoyer-parc-businessobjects-documents-inutilises": ["audit-sap-businessobjects", "migration-businessobjects-power-bi"],
    "checklist-migration-sap-businessobjects": ["migration-businessobjects-power-bi", "alternatives-sap-businessobjects"],
    "convertir-univers-unv-en-unx": ["sap-businessobjects-bi-2027"],
    "questions-a-poser-prestataire-migration-businessobjects": ["consultant-sap-businessobjects", "audit-sap-businessobjects"],
}
for _p in PAGES:
    _p["related"] = _p["related"] + [x for x in EXTRA_RELATED.get(_p["slug"], []) if x not in _p["related"]]
MONTHS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
def fr_date(iso):
    y, m, d = iso.split("-")
    return "%d %s %s" % (int(d), MONTHS[int(m) - 1], y)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "site", "out")
DOMAIN = (sys.argv[1] if len(sys.argv) > 1 else "https://trivoie.fr").rstrip("/")
TODAY = "2026-11-09"
MODIFIED = "2026-11-10"
EMAIL = "contact@trivoie.fr"
ORG = {
    "@type": "ProfessionalService", "@id": DOMAIN + "/#org", "name": "Trivoie", "legalName": "AM DATA",
    "url": DOMAIN + "/", "email": EMAIL, "taxID": "939 133 781",
    "description": "Diagnostic indépendant et à prix fixe de la sortie de SAP BusinessObjects 4.3, avant la fin de maintenance du 31 décembre 2026.",
    "address": {"@type": "PostalAddress", "streetAddress": "32 rue Boyer", "postalCode": "75020", "addressLocality": "Paris", "addressCountry": "FR"},
    "areaServed": "FR", "founder": {"@type": "Person", "name": "Abderrahim Mouloud"}, "knowsLanguage": "fr", "knowsAbout": ["SAP BusinessObjects", "Web Intelligence", "Crystal Reports", "Migration BI", "Maintenance logicielle"],
}

FONTS_CSS = """@font-face{font-family:"Archivo";font-style:normal;font-weight:100 900;font-stretch:62% 125%;font-display:swap;src:url(/fonts/archivo-wdth.woff2) format("woff2")}
@font-face{font-family:"IBM Plex Sans";font-style:normal;font-weight:400;font-display:swap;src:url(/fonts/plex-sans-400.woff2) format("woff2")}
@font-face{font-family:"IBM Plex Sans";font-style:normal;font-weight:500;font-display:swap;src:url(/fonts/plex-sans-500.woff2) format("woff2")}
@font-face{font-family:"IBM Plex Sans";font-style:normal;font-weight:600;font-display:swap;src:url(/fonts/plex-sans-600.woff2) format("woff2")}
@font-face{font-family:"IBM Plex Mono";font-style:normal;font-weight:400;font-display:swap;src:url(/fonts/plex-mono-400.woff2) format("woff2")}
@font-face{font-family:"IBM Plex Mono";font-style:normal;font-weight:500;font-display:swap;src:url(/fonts/plex-mono-500.woff2) format("woff2")}
"""
PRELOAD = '<link rel="preload" href="/fonts/archivo-wdth.woff2" as="font" type="font/woff2" crossorigin>\n<link rel="preload" href="/fonts/plex-sans-400.woff2" as="font" type="font/woff2" crossorigin>'
FAVICON = '<link rel="icon" href="/favicon.svg" type="image/svg+xml">'

def tokens_css():
    t = open(os.path.join(ROOT, "template.html"), encoding="utf-8").read()
    a = t.index(":root {"); b = t.index("* { box-sizing")
    return t[a:b]

ART_CSS = """
.gloss dt { font-weight: 600; margin-top: 16px; }
.gloss dd { margin: 4px 0 0; color: var(--muted); }
.steps li { margin: 10px 0; }
.hub-list { list-style: none; padding: 0; display: grid; gap: 12px; }
.hub-list li { background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); padding: 14px 16px; }
.hub-list a { font-weight: 600; }
.hub-list p { margin: 6px 0 0; color: var(--muted); }

* { box-sizing: border-box; }
[hidden] { display: none !important; }
body { margin: 0; background: var(--bg); color: var(--ink); font-family: var(--f-body); font-size: 17px; line-height: 1.65; }
a { color: var(--accent); }
:focus-visible { outline: 3px solid var(--accent); outline-offset: 2px; }
.wrap { max-width: 780px; margin: 0 auto; padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); }
header.top { background: var(--board); color: #fff; }
header.top .wrap { display: flex; align-items: center; justify-content: space-between; gap: 12px; padding-block: 14px; flex-wrap: wrap; }
.brand { font-family: var(--f-display); font-stretch: 85%; font-weight: 800; font-size: 1.5rem; color: #fff; text-decoration: none; letter-spacing: .01em; }
.brand span { color: var(--board-ink); }
header.top nav { display: flex; gap: 16px; flex-wrap: wrap; }
header.top nav a { color: #dbe6ea; text-decoration: none; font-size: .95rem; }
header.top nav a:hover { text-decoration: underline; }
main { padding-block: 40px 56px; }
.crumbs { font-size: .9rem; color: var(--muted); margin: 0 0 18px; }
.crumbs a { color: var(--muted); }
h1, h2, h3 { font-family: var(--f-display); font-stretch: 88%; line-height: 1.15; text-wrap: balance; margin: 0; }
h1 { font-size: clamp(1.9rem, 5vw, 2.7rem); font-weight: 800; }
h2 { font-size: 1.55rem; font-weight: 750; margin-top: 2.2em; }
h3 { font-size: 1.15rem; font-weight: 700; margin-top: 1.4em; }
p, li { max-width: 68ch; }
.lead { font-size: 1.15rem; color: var(--muted); margin: 18px 0 0; }
.meta { font-size: .88rem; color: var(--muted); margin-top: 14px; }
ul, ol { padding-left: 1.3em; }
li { margin: .35em 0; }
code { font-family: var(--f-mono); font-size: .86em; background: var(--accent-soft); padding: 1px 5px; border-radius: 4px; overflow-wrap: anywhere; }
.tbl { overflow-x: auto; margin: 16px 0; border: 1px solid var(--line); border-radius: var(--radius); background: var(--surface); }
table { border-collapse: collapse; width: 100%; min-width: 520px; font-size: .95rem; }
th, td { text-align: left; padding: 10px 12px; border-bottom: 1px solid var(--line); vertical-align: top; }
th { font-family: var(--f-display); font-stretch: 90%; background: var(--accent-soft); }
tr:last-child td { border-bottom: 0; }
.cta { margin: 44px 0 0; padding: 22px; background: var(--board); color: #fff; border-radius: var(--radius); }
.cta h2 { margin: 0 0 8px; font-size: 1.4rem; color: #fff; }
.cta p { margin: 0 0 14px; color: #dbe6ea; }
.btn { display: inline-block; padding: 12px 20px; background: var(--board-ink); color: #15212a; font-weight: 700; border-radius: var(--radius); text-decoration: none; }
.btn:hover { filter: brightness(1.05); }
.faq details { background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); padding: 12px 16px; margin: 8px 0; }
.faq summary { cursor: pointer; font-weight: 600; }
.faq p { margin: 8px 0 0; color: var(--muted); }
.related ul { list-style: none; padding: 0; }
.related li { margin: 8px 0; }
.sources { margin-top: 2.2em; font-size: .92rem; color: var(--muted); }
.sources h2 { font-size: 1.1rem; margin-top: 0; }
footer.site { border-top: 1px solid var(--line); background: var(--surface); }
footer.site .wrap { padding-block: 24px; font-size: .88rem; color: var(--muted); }
footer.site nav { display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 10px; }
footer.site p { margin: 6px 0; max-width: none; }
@media (max-width: 600px) { body { font-size: 16px; } main { padding-block: 28px 40px; } }
"""

# Pied de page généré depuis PAGES : chaque nouvelle page y apparaît automatiquement.
FOOT_LABELS = {
    "fin-maintenance-sap-businessobjects-4-3": "Fin de maintenance 4.3",
    "bi-2025-ou-sortir-de-businessobjects": "BI 2025 ou sortie",
    "diagnostic-sortie-businessobjects": "Diagnostic Sortie BO",
    "compter-documents-sap-businessobjects-query-builder": "Query Builder",
    "maintenance-specifique-client-sap-businessobjects": "Maintenance spécifique client",
    "risque-securite-sap-businessobjects-4-3": "Risque de sécurité 4.3",
    "convertir-univers-unv-en-unx": "Convertir UNV en UNX",
    "contenus-obsoletes-xcelsius-desktop-intelligence-explorer": "Contenus obsolètes",
    "nettoyer-parc-businessobjects-documents-inutilises": "Nettoyer son parc",
    "checklist-migration-sap-businessobjects": "Checklist de migration",
    "questions-a-poser-prestataire-migration-businessobjects": "Choisir son prestataire",
    "diagnostic-businessobjects-secteur-public-marche-60000-euros": "Secteur public",
    "glossaire-sap-businessobjects": "Glossaire",
    "migration-businessobjects-power-bi": "Migrer vers Power BI",
    "sap-businessobjects-bi-2027": "BI 2027",
    "consultant-sap-businessobjects": "Consultant SAP BusinessObjects",
    "audit-sap-businessobjects": "Audit SAP BusinessObjects",
    "alternatives-sap-businessobjects": "Alternatives à BusinessObjects",
}
# Mesure d'audience (Umami Cloud, sans cookie). Tant que WEBSITE_ID est vide, rien n'est chargé,
# la politique de sécurité reste fermée et la page confidentialité annonce « aucun outil de mesure ».
ANALYTICS = {"website_id": os.environ.get("TRIVOIE_UMAMI_ID", "4396576b-6679-48bc-9158-52b20910a3ea"), "script": "https://cloud.umami.is/script.js",
             "script_host": "https://cloud.umami.is", "api_host": "https://api-gateway.umami.dev"}


def csp(frame_ancestors=False):
    a = ANALYTICS
    on = bool(a["website_id"])
    return ("default-src 'self'; script-src 'self' 'unsafe-inline'%s; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src %s;%s base-uri 'self'; form-action 'none'"
            % (" " + a["script_host"] if on else "", ("'self' " + a["api_host"] + " " + a["script_host"]) if on else "'none'", " frame-ancestors 'none';" if frame_ancestors else ""))


def analytics_tag():
    a = ANALYTICS
    if not a["website_id"]:
        return ""
    return '<script defer src="%s" data-website-id="%s" data-do-not-track="true"></script>' % (a["script"], a["website_id"])


def foot_label(p):
    return p.get("nav") or FOOT_LABELS.get(p["slug"]) or p["h1"].split(" : ")[0]
NAV_FOOT = ('<nav aria-label="Guides"><a href="/guides/">Tous les guides</a>'
            + "".join('<a href="/%s/">%s</a>' % (p["slug"], html.escape(foot_label(p))) for p in PAGES)
            + '</nav><nav aria-label="Informations"><a href="/mentions-legales/">Mentions légales</a><a href="/confidentialite/">Confidentialité</a></nav>')

FOOT_TXT = ('<p><strong>Trivoie</strong> est un service d\'AM DATA, entreprise individuelle, SIREN 939 133 781, 32 rue Boyer, 75020 Paris. Contact : %s</p>'
            '<p>SAP, BusinessObjects, Crystal Reports, Lumira et Power BI sont des marques de leurs propriétaires respectifs. Trivoie n\'est affilié ni à SAP, ni à Microsoft.</p>') % EMAIL


def head(title, desc, path, extra_ld=None, og_type="website", css=True, noindex=False):
    url = DOMAIN + path
    ld = {"@context": "https://schema.org", "@graph": [ORG] + (extra_ld or [])}
    h = ['<meta charset="utf-8">', '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">',
         '<meta http-equiv="Content-Security-Policy" content="%s">' % csp(),
         "<title>%s | Trivoie</title>" % html.escape(title) if "Trivoie" not in title else "<title>%s</title>" % html.escape(title),
         '<meta name="description" content="%s">' % html.escape(desc, quote=True),
         '<link rel="canonical" href="%s">' % url,
         '<meta name="robots" content="%s">' % ("noindex, follow" if noindex else "index, follow, max-image-preview:large, max-snippet:-1"),
         '<meta property="og:locale" content="fr_FR">', '<meta property="og:site_name" content="Trivoie">',
         '<meta property="og:type" content="%s">' % og_type, '<meta property="og:title" content="%s">' % html.escape(title, quote=True),
         '<meta property="og:description" content="%s">' % html.escape(desc, quote=True), '<meta property="og:url" content="%s">' % url,
         '<meta property="og:image" content="%s/og.png">' % DOMAIN, '<meta property="og:image:width" content="1200">', '<meta property="og:image:height" content="630">',
         '<meta property="og:image:alt" content="Trivoie : la fin de maintenance de SAP BusinessObjects 4.3, trois voies">',
         '<link rel="alternate" hreflang="fr" href="%s">' % url, '<link rel="alternate" hreflang="x-default" href="%s">' % url,
         '<meta name="twitter:card" content="summary_large_image">', '<meta name="twitter:title" content="%s">' % html.escape(title, quote=True),
         '<meta name="twitter:description" content="%s">' % html.escape(desc, quote=True), '<meta name="twitter:image" content="%s/og.png">' % DOMAIN, '<meta name="theme-color" content="#15212a">',
         FAVICON, PRELOAD, analytics_tag(),
         '<script type="application/ld+json">%s</script>' % json.dumps(ld, ensure_ascii=False, separators=(",", ":"))]
    return "\n".join(h)


def page_shell(title, desc, path, body_html, extra_ld=None, og_type="website", noindex=False):
    return """<!doctype html>
<html lang="fr">
<head>
%s
<style>
%s
%s
%s
</style>
</head>
<body>
<header class="top"><div class="wrap"><a class="brand" href="/">Tri<span>voie</span></a>
<nav aria-label="Navigation"><a href="/#scan">Scan gratuit</a><a href="/fin-maintenance-sap-businessobjects-4-3/">Fin de maintenance</a><a href="/diagnostic-sortie-businessobjects/">Diagnostic</a></nav></div></header>
%s
<footer class="site"><div class="wrap">%s%s</div></footer>
</body>
</html>
""" % (head(title, desc, path, extra_ld, og_type, noindex=noindex), FONTS_CSS, tokens_css(), ART_CSS, body_html, NAV_FOOT, FOOT_TXT)


def write(path, content):
    full = os.path.join(OUT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(content)


def build_article(p, allp):
    path = "/%s/" % p["slug"]
    url = DOMAIN + path
    faq_ld = {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faqs"]]}
    art_ld = {"@type": "Article", "@id": url + "#article", "headline": p["h1"], "description": p["desc"], "inLanguage": "fr-FR",
              "datePublished": p.get("published", TODAY), "dateModified": p.get("modified", MODIFIED), "inLanguage": "fr-FR", "mainEntityOfPage": url,
              "author": {"@id": DOMAIN + "/#org"}, "publisher": {"@id": DOMAIN + "/#org"}, "image": DOMAIN + "/og.png"}
    bc_ld = {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Trivoie", "item": DOMAIN + "/"},
        {"@type": "ListItem", "position": 2, "name": p["h1"], "item": url}]}
    ld = [art_ld, bc_ld, faq_ld]
    if p.get("service"):
        ld.append({"@type": "Service", "@id": url + "#service", "name": "Diagnostic Sortie SAP BusinessObjects 4.3", "serviceType": "Diagnostic de plateforme décisionnelle",
                   "provider": {"@id": DOMAIN + "/#org"}, "areaServed": "FR", "description": p["desc"],
                   "offers": [{"@type": "Offer", "name": "Diagnostic Sortie BO, taille %s" % s, "price": pr, "priceCurrency": "EUR",
                               "description": d + ", prix hors taxes", "url": url}
                              for s, pr, d in [("S", "2900", "Jusqu'à 200 utilisateurs et 2 000 documents"),
                                               ("M", "4900", "Jusqu'à 1 000 utilisateurs et 10 000 documents"),
                                               ("L", "7900", "Au-delà de 1 000 utilisateurs ou 10 000 documents")]]})
    faq_html = '<section class="faq"><h2>Questions fréquentes</h2>%s</section>' % "".join(
        "<details><summary>%s</summary><p>%s</p></details>" % (html.escape(q), html.escape(a)) for q, a in p["faqs"])
    rel = {x["slug"]: x for x in allp}
    rel_html = '<section class="related"><h2>À lire aussi</h2><ul>%s</ul></section>' % "".join(
        '<li><a href="/%s/">%s</a></li>' % (s, html.escape(rel[s]["h1"])) for s in p["related"])
    cta = ('<aside class="cta"><h2>Mesurez votre risque en 5 minutes</h2><p>Le scan est gratuit, sans inscription. Il calcule dans votre navigateur un niveau de risque et la taille de votre plateforme.</p>'
           '<a class="btn" href="/#scan">Mesurer mon risque</a></aside>')
    src = SOURCES_BLOCK if p.get("sources", True) else ""
    body = ('<main><div class="wrap"><p class="crumbs"><a href="/">Trivoie</a> &rsaquo; %s</p><h1>%s</h1><p class="lead">%s</p>'
            '<p class="meta">Par AM DATA, expert SAP BusinessObjects. Mis à jour le %s.</p>%s%s%s%s%s</div></main>'
            % (html.escape(p["title"]), html.escape(p["h1"]), html.escape(p["lead"]), fr_date(p.get("modified", MODIFIED)), p["body"], faq_html, src, cta, rel_html))
    write(path + "index.html", page_shell(p["title"], p["desc"], path, body, ld, "article"))


def build_hub():
    items = "".join('<li><a href="/%s/">%s</a><p>%s</p></li>' % (p["slug"], html.escape(p["h1"]), html.escape(p["desc"])) for p in PAGES)
    body = ('<main><div class="wrap"><p class="crumbs"><a href="/">Trivoie</a> &rsaquo; Guides</p><h1>Guides : fin de maintenance de SAP BusinessObjects 4.3</h1>'
            '<p class="lead">Tout ce qu\'il faut savoir pour décider avant le 31 décembre 2026 : dates, risques, options, méthode et prix.</p>'
            '<p class="meta">Par AM DATA, expert SAP BusinessObjects. Mis à jour le 10 novembre 2026.</p><ul class="hub-list">%s</ul>'
            '<aside class="cta"><h2>Mesurez votre risque en 5 minutes</h2><p>Le scan est gratuit, sans inscription. Il calcule dans votre navigateur un niveau de risque et la taille de votre plateforme.</p>'
            '<a class="btn" href="/#scan">Mesurer mon risque</a></aside></div></main>') % items
    ld = [{"@type": "CollectionPage", "@id": DOMAIN + "/guides/#page", "name": "Guides : fin de maintenance de SAP BusinessObjects 4.3", "inLanguage": "fr-FR",
           "isPartOf": {"@id": DOMAIN + "/#site"} if False else {"@type": "WebSite", "url": DOMAIN + "/"},
           "hasPart": [{"@type": "Article", "headline": p["h1"], "url": "%s/%s/" % (DOMAIN, p["slug"])} for p in PAGES]}]
    write("/guides/index.html", page_shell("Guides : fin de maintenance SAP BusinessObjects 4.3 | Trivoie", "Tous les guides Trivoie sur la fin de maintenance de SAP BusinessObjects 4.3 : dates, risque, BI 2025, univers UNV, checklist, prix du diagnostic.", "/guides/", body, ld))


LEGAL = """<main><div class="wrap"><p class="crumbs"><a href="/">Trivoie</a> &rsaquo; Mentions légales</p><h1>Mentions légales</h1>
<h2>Éditeur du site</h2>
<p>Trivoie est un service édité par <strong>AM DATA</strong>, entreprise individuelle.<br>SIREN : 939 133 781<br>Adresse : 32 rue Boyer, 75020 Paris<br>Courriel : %(mail)s<br>Directeur de la publication : Abderrahim Mouloud<br>Numéro de TVA intracommunautaire : FR77939133781</p>
<h2>Hébergement</h2>
<p>Site hébergé par GitHub, Inc. (GitHub Pages), 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis (github.com). Le nom de domaine est enregistré chez OVH SAS, 2 rue Kellermann, 59100 Roubaix, France.</p>
<h2>Propriété intellectuelle</h2>
<p>Les textes et l'interface de ce site sont la propriété d'AM DATA. SAP, BusinessObjects, Crystal Reports, Lumira et Power BI sont des marques de leurs propriétaires respectifs. Trivoie n'est affilié ni à SAP, ni à Microsoft. Les logos de clients affichés sur la page d'accueil appartiennent à leurs titulaires.</p>
<h2>Responsabilité</h2>
<p>Les informations de ce site sont fournies à titre indicatif et ne remplacent pas la documentation officielle de SAP. Les dates et règles de maintenance doivent être vérifiées auprès de SAP avant toute décision.</p>
<p><a href="/">Retour à l'accueil</a></p></div></main>""" % {"mail": EMAIL}

if ANALYTICS["website_id"]:
    AUDIENCE = ("<p>Ce site ne dépose aucun cookie. Pour savoir combien de personnes le consultent et d'où elles viennent, il utilise Umami Cloud, un outil de mesure d'audience dont le script n'utilise pas de cookie (source : documentation d'Umami). "
                "Sont comptés les pages consultées, le site d'origine du visiteur, le pays, le type d'appareil et de navigateur, et quelques actions sans lien avec vos saisies (par exemple un clic sur un bouton de contact). "
                "Les nombres saisis dans le scan ne sont jamais transmis. Les statistiques servent uniquement à AM DATA, pour améliorer le site, et ne sont ni croisées avec d'autres données ni revendues. "
                "L'outil respecte le signal « Ne pas suivre » de votre navigateur. Vous pouvez vous opposer à cette mesure en écrivant à %s.</p>"
                "<p>Comme tout hébergeur, GitHub Pages traite techniquement l'adresse IP des visiteurs pour délivrer les pages ; ce traitement peut avoir lieu hors de l'Union européenne. AM DATA n'a pas accès à ces journaux.</p>") % EMAIL
else:
    AUDIENCE = ("<p>Ce site ne dépose aucun cookie et n'utilise aucun outil de mesure d'audience ni aucune police ou ressource hébergée par un tiers. Comme tout hébergeur, GitHub Pages traite techniquement l'adresse IP des visiteurs pour délivrer les pages et assurer la sécurité du service ; ce traitement peut avoir lieu hors de l'Union européenne. AM DATA n'a pas accès à ces journaux et ne les utilise pas.</p>")

PRIVACY = """<main><div class="wrap"><p class="crumbs"><a href="/">Trivoie</a> &rsaquo; Confidentialité</p><h1>Politique de confidentialité</h1>
<h2>Responsable du traitement</h2>
<p>AM DATA, entreprise individuelle, SIREN 939 133 781, 32 rue Boyer, 75020 Paris. Contact : %(mail)s</p>
<h2>Le scan gratuit</h2>
<p>Le calcul du scan s'effectue entièrement dans votre navigateur. Les nombres que vous saisissez ne sont pas transmis à nos serveurs. Le script de collecte automatique ne lit que des nombres et n'exporte aucun nom de document, d'utilisateur ou de serveur, et le mot de passe n'est jamais enregistré. Vous ne nous envoyez le résumé que si vous décidez de nous écrire.</p>
<h2>Quand vous nous écrivez</h2>
<p>Si vous nous envoyez un courriel, nous traitons votre adresse et le contenu du message pour répondre à votre demande, sur la base de notre intérêt légitime à répondre aux sollicitations professionnelles ou de l'exécution de mesures précontractuelles. Ces données sont conservées au plus 3 ans après le dernier échange.</p>
<h2>Prise de rendez-vous</h2>
<p>Le bouton « Échange gratuit de 20 minutes » ouvre, dans un nouvel onglet, la page de réservation du service Calendly. Les informations saisies sur cette page (nom, adresse de courriel, message) sont traitées par Calendly selon sa propre politique de confidentialité, et peuvent l'être hors de l'Union européenne. AM DATA les utilise uniquement pour organiser l'échange demandé. Tant que vous ne cliquez pas sur ce bouton, aucune donnée n'est transmise à Calendly.</p>
<h2>Cookies et mesure d'audience</h2>
%(audience)s
<h2>Vos droits</h2>
<p>Vous pouvez demander l'accès, la rectification ou l'effacement de vos données, vous opposer à leur traitement ou en demander la limitation en écrivant à %(mail)s. Vous pouvez aussi saisir la CNIL (www.cnil.fr).</p>
<p><a href="/">Retour à l'accueil</a></p></div></main>""" % {"mail": EMAIL, "audience": AUDIENCE}


def build_index():
    s = open(os.path.join(ROOT, "trivoie.html"), encoding="utf-8").read()
    title = "Fin de maintenance BusinessObjects 4.3 : scan gratuit | Trivoie"
    desc = ("Scan gratuit : mesurez votre risque après la fin de maintenance de SAP BusinessObjects 4.3 (31/12/2026). "
            "Puis diagnostic indépendant à prix fixe en 10 jours.")
    # fonts, title, meta
    s = re.sub(r'<link rel="preconnect"[^>]*>\s*', "", s)
    s = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>', "", s)
    s = s.replace("<title>Trivoie</title>", "")
    s = re.sub(r'<meta name="viewport"[^>]*>\s*', "", s)
    s = re.sub(r'<meta name="description"[^>]*>', "", s)
    s = s.replace('<meta name="claude:viewport-fit-sides" content="cover">', "")
    faq = re.findall(r"<details><summary>(.*?)</summary><p>(.*?)</p></details>", s, flags=re.S)
    def plain(x): return html.unescape(re.sub(r"<[^>]+>", "", x)).strip()
    faq_ld = {"@type": "FAQPage", "@id": DOMAIN + "/#faq", "mainEntity": [
        {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(a)}} for q, a in faq if "<code>" not in q][:8]}
    web_ld = {"@type": "WebSite", "@id": DOMAIN + "/#site", "url": DOMAIN + "/", "name": "Trivoie", "inLanguage": "fr-FR", "publisher": {"@id": DOMAIN + "/#org"}}
    svc = [p for p in PAGES if p.get("service")][0]
    extra = [web_ld, faq_ld]
    hd = head(title, desc, "/", extra)
    s = s.replace("<style>", hd + "\n<style>\n" + FONTS_CSS, 1)
    s = s.replace("<head>", "<head>", 1)
    # nombre de jours statique à jour pour les robots
    days = (datetime.date(2026, 12, 31) - datetime.date.fromisoformat(TODAY)).days
    s = re.sub(r'(id="heroDays">)\d+(<)', r"\g<1>%d\2" % days, s)
    # section visible "Guides" avant le pied de page (mobile et ordinateur)
    cards = "".join('<li><a href="/%s/"><strong>%s</strong><span>%s</span></a></li>' % (q["slug"], html.escape(q["title"]), html.escape(q["desc"])) for q in PAGES)
    gsec = ('<section class="guides-home" aria-labelledby="guidesH"><div class="wrap"><p class="eyebrow">Guides</p>'
            '<h2 id="guidesH">Comprendre la fin de maintenance de SAP BusinessObjects 4.3</h2>'
            '<ul class="gh-grid">%s</ul><p><a href="/guides/">Voir tous les guides</a></p></div></section>\n' % cards)
    assert s.count("<footer>") == 1
    s = s.replace("<footer>", gsec + "<footer>", 1)
    # maillage interne dans le pied de page
    s = s.replace("<footer>\n  <div class=\"wrap\">", "<footer>\n  <div class=\"wrap\">\n    " + NAV_FOOT.replace("\n", "") , 1)
    s = s.replace("</style>", "footer nav { display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 10px; }\nfooter nav a { color: var(--muted); }\n.guides-home { border-top: 1px solid var(--line); padding-block: 40px; }\n.guides-home .wrap { display: grid; gap: 16px; }\n.gh-grid { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 280px), 1fr)); gap: 12px; }\n.gh-grid a { display: grid; gap: 6px; align-content: start; height: 100%; padding: 14px 16px; background: var(--surface); border: 1px solid var(--line); border-radius: var(--radius); text-decoration: none; color: var(--ink); }\n.gh-grid a:hover { border-color: var(--accent); }\n.gh-grid strong { font-family: var(--f-display); font-stretch: 95%; font-size: 1.02rem; line-height: 1.25; }\n.gh-grid span { color: var(--muted); font-size: 0.9rem; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }\n</style>", 1)
    assert "fonts.googleapis" not in s and "fonts.gstatic" not in s
    k = s.index("</style>") + len("</style>")
    s = '<!doctype html>\n<html lang="fr">\n<head>\n' + s[:k].strip() + '\n</head>\n<body>\n' + s[k:].strip() + '\n</body>\n</html>\n'
    write("/index.html", s)


def build_static():
    for src, dst in [("archivo-latin-wdth-normal.woff2", "archivo-wdth.woff2"), ("ibm-plex-sans-latin-400-normal.woff2", "plex-sans-400.woff2"),
                     ("ibm-plex-sans-latin-500-normal.woff2", "plex-sans-500.woff2"), ("ibm-plex-sans-latin-600-normal.woff2", "plex-sans-600.woff2"),
                     ("ibm-plex-mono-latin-400-normal.woff2", "plex-mono-400.woff2"), ("ibm-plex-mono-latin-500-normal.woff2", "plex-mono-500.woff2")]:
        os.makedirs(os.path.join(OUT, "fonts"), exist_ok=True)
        shutil.copy(os.path.join(ROOT, "site", "fonts_src", src), os.path.join(OUT, "fonts", dst))
    shutil.copy(os.path.join(ROOT, "site", "assets", "og.png"), os.path.join(OUT, "og.png"))
    for lic in ["LICENSE-archivo.txt", "LICENSE-plex.txt"]:
        shutil.copy(os.path.join(ROOT, "site", "fonts_src", lic), os.path.join(OUT, "fonts", lic))
    write("/favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#15212a"/>'
          '<g fill="none" stroke-width="5" stroke-linecap="round"><path d="M10 32h16" stroke="#f2c94c"/><path d="M26 32c10 0 14-14 28-14" stroke="#56b6c8"/>'
          '<path d="M26 32h28" stroke="#f2c94c"/><path d="M26 32c10 0 14 14 28 14" stroke="#e57a68"/></g></svg>')
    LASTMOD = {"/%s/" % p["slug"]: p.get("modified", MODIFIED) for p in PAGES}
    urls = ["/", "/guides/"] + ["/%s/" % p["slug"] for p in PAGES] + ["/mentions-legales/", "/confidentialite/"]
    write("/sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % "".join(
        "  <url><loc>%s%s</loc><lastmod>%s</lastmod></url>\n" % (DOMAIN, u, LASTMOD.get(u, MODIFIED)) for u in urls))
    write("/robots.txt", """User-agent: *
Allow: /

# Moteurs de recherche et assistants IA : tout le site est public.
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: Bingbot
Allow: /

Sitemap: %s/sitemap.xml
""" % DOMAIN)
    lines = ["# Trivoie", "",
             "> Trivoie est un service d'AM DATA : un scan gratuit pour mesurer son risque après la fin de maintenance de SAP BusinessObjects 4.3 (31 décembre 2026), puis un diagnostic indépendant à prix fixe (2 900 à 7 900 € HT) livré en 10 jours ouvrés. AM DATA n'est revendeur ni de SAP ni de Microsoft.", "",
             "## Pages", "",
             "- [Accueil et scan gratuit](%s/): calcul d'un niveau de risque dans le navigateur, sans envoi de données" % DOMAIN,
             "- [Index des guides](%s/guides/): liste de tous les guides" % DOMAIN]
    for p in PAGES:
        lines.append("- [%s](%s/%s/): %s" % (p["h1"], DOMAIN, p["slug"], p["desc"]))
    lines += ["", "## Faits clés", "",
              "- La maintenance standard de SAP BusinessObjects BI 4.3 s'arrête le 31 décembre 2026.",
              "- À partir du 1er janvier 2027, maintenance spécifique client : correctifs de sécurité de score CVSS 7 ou plus seulement pendant 12 mois (notes SAP 3486924 et 3763590) ; à partir de 2028, plus aucun correctif.",
              "- La maintenance standard de SAP BusinessObjects BI 2025 va jusqu'au 31 décembre 2027.",
              "- SAP BusinessObjects BI 2027 est attendu au premier trimestre 2027 (Wiiisdom, Dallas Marks) ; sa maintenance standard irait jusqu'au quatrième trimestre 2029 selon Wiiisdom.",
              "- Les univers UNV ne sont plus pris en charge après la 4.3 et doivent être convertis en UNX pour monter en BI 2025.",
              "", "## Contact", "", "- %s" % EMAIL, "- AM DATA, 32 rue Boyer, 75020 Paris, SIREN 939 133 781", ""]
    write("/llms.txt", "\n".join(lines))
    write("/.htaccess", """# Hébergement mutualisé OVH (Apache). Vérifiez que le module mod_headers est actif.
DirectoryIndex index.html
ErrorDocument 404 /404.html
RewriteEngine On
RewriteCond %{HTTPS} !=on
RewriteRule ^(.*)$ https://%{HTTP_HOST}/$1 [R=301,L]

<IfModule mod_headers.c>
Header always set Strict-Transport-Security "max-age=31536000"
Header always set X-Content-Type-Options "nosniff"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
Header always set Permissions-Policy "camera=(), microphone=(), geolocation=()"
Header always set Content-Security-Policy "__CSP__"
<FilesMatch "\\.(woff2|png|svg)$">
Header set Cache-Control "public, max-age=31536000, immutable"
</FilesMatch>
</IfModule>
""".replace("__CSP__", csp(True)))
    write("/404.html", page_shell("Page introuvable", "Cette page n'existe pas.", "/404.html",
          '<main><div class="wrap"><h1>Page introuvable</h1><p>Cette page n\'existe pas ou a été déplacée.</p><p><a href="/">Retour à l\'accueil</a></p></div></main>', noindex=True))


if __name__ == "__main__":
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    build_static()
    build_index()
    for p in PAGES:
        build_article(p, PAGES)
    build_hub()
    write("/mentions-legales/index.html", page_shell("Mentions légales", "Mentions légales du site Trivoie, service d'AM DATA.", "/mentions-legales/", LEGAL))
    write("/confidentialite/index.html", page_shell("Politique de confidentialité", "Données traitées par le site Trivoie : aucune pour le scan, aucun cookie.", "/confidentialite/", PRIVACY))
    print("ok", DOMAIN)
