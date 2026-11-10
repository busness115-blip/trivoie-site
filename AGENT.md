# Trivoie : consignes pour ajouter des pages (agent planifié)

Site : https://trivoie.fr (GitHub Pages, branche `main` = site publié, branche `source` = ce dossier, générateur).
Éditeur : AM DATA (Abderrahim Mouloud). Cible : directions, DSI, RSSI, achats et équipes BI sous SAP BusinessObjects 4.3.

## Règles non négociables
1. Zéro erreur factuelle. Chaque fait (date, règle, chiffre, texte réglementaire) doit venir d'une source retrouvée par recherche web pendant ce run, citée dans la page avec un lien. Un fait non confirmé est soit retiré, soit écrit « à confirmer auprès de SAP ». Ne jamais inventer de prix, statistique, client, témoignage ou cas.
2. Pas de tiret cadratin ni demi-cadratin. Français soigné, ton factuel, sans superlatifs.
3. Indépendance : AM DATA n'est revendeur ni de SAP ni de Microsoft. Ne pas dénigrer d'éditeur. Ne citer aucun nom de client.
4. Offre et prix : uniquement ceux déjà sur le site (Diagnostic Sortie BO, S 2 900, M 4 900, L 7 900 € HT, 10 jours ouvrés).
5. Faits déjà établis (ne pas les contredire) : fin de maintenance standard BI 4.3 le 31/12/2026 ; 2027 maintenance spécifique client, correctifs CVSS 7 ou plus seulement ; 2028 plus aucun correctif ; frais inchangés ; BI 2025 maintenue jusqu'à fin 2027 ; UNV non pris en charge après 4.3. Si une recherche montre un changement, corriger les pages concernées et le signaler.
6. Maximum 2 nouvelles pages par exécution. Qualité avant quantité. Chaque page : 600 à 1 000 mots, un h1 unique avec la requête cible, 3 questions fréquentes ou plus, sources liées, 2 à 3 liens internes dans `related`, titre de 60 caractères maximum, description de 155 caractères maximum.
7. Pas de doublon : vérifier slug et sujet contre les pages existantes (pages.py, pages2.py, content/).

## Procédure
1. Lire `BACKLOG.md`, prendre le premier sujet non fait (ou en proposer un meilleur après recherche de ce que cherchent les prospects).
2. Rechercher les sources (WebSearch). Noter les URL.
3. Créer `site/content/NNN-slug.py` définissant `PAGE = dict(slug=..., title=..., desc=..., h1=..., lead=..., body="""...""", faqs=[(q, a), ...], related=[slugs existants], sources=False, published="AAAA-MM-JJ", modified="AAAA-MM-JJ")`. Le corps utilise h2/h3, listes, tableaux `<div class="tbl" tabindex="0" role="region" aria-label="Tableau N (défilement horizontal)">` (aria-label unique par page). Liens externes avec `rel="noopener"`. Voir `site/pages2.py` pour des exemples.
4. Construire : `python3 build.py` seulement si template.html a changé (sinon `trivoie.html` est déjà à jour), puis `python3 site/build_site.py`.
5. Tester si Node et Playwright sont disponibles : `python3 tools/serve.py &` puis `SITE_OUT=site/out node tools/site_test.js` et `node tools/audit.js`. Sinon, au minimum : vérifier que chaque lien interne existe dans site/out, que le JSON-LD est valide, qu'aucun « — » n'apparaît (`grep -rl "—" site/out`).
6. Publier : copier le contenu de `site/out` dans un clone de la branche `main`, en conservant `CNAME`, `.nojekyll`, `README.md` et sans `.htaccess` ; commit puis push `main`. Commit des sources sur la branche `source`.
7. Mettre à jour `BACKLOG.md` (sujet fait, date). Ajouter 2 nouveaux sujets issus de la recherche si pertinents.
8. Ajouter le lien de la nouvelle page dans `related` d'une page existante proche si utile (pages2.py ou content/).
9. Rapport final court à l'utilisateur : pages ajoutées, sources, tests, points à confirmer.

## Ne pas faire
Ne pas modifier mentions légales, confidentialité, prix, logos, ni la page d'accueil. Ne pas publier si un test échoue : laisser le travail sur la branche `source`, sans toucher `main`, et le signaler.
