PAGE = dict(
 slug="univers-unx-bonnes-pratiques-apres-conversion-businessobjects",
 nav="Univers UNX : après la conversion",
 title="Univers UNX : bonnes pratiques après la conversion",
 desc="Après la conversion UNV vers UNX dans SAP BusinessObjects : ce qui ne se convertit pas, quoi vérifier, repointer les documents, alléger l'univers.",
 h1="Univers UNX : bonnes pratiques de conception après la conversion depuis UNV",
 lead="Convertir un univers UNV en UNX ne s'arrête pas à l'assistant de conversion. Il reste à contrôler le résultat, à repointer les documents Web Intelligence et à profiter de l'occasion pour alléger les univers. Cette page rassemble ce que disent des publications de SAP Community, d'un consultant indépendant et d'un cabinet, avec leurs sources. Elle complète la page sur la <a href=\"/convertir-univers-unv-en-unx/\">méthode de conversion</a>.",
 published="2026-11-23", modified="2026-11-23",
 body="""
<h2>Ce que la conversion produit</h2>
<p>Selon un <a href="https://community.sap.com/t5/technology-blog-posts-by-sap/sap-bi-2025-information-design-tool-overview/ba-p/14072941" rel="noopener">article de SAP Community consacré à l'Information Design Tool dans BI 2025</a>, la conversion d'un UNV crée une couche de données (data foundation) et une couche métier (business layer). Les tables, tables dérivées, alias, jointures et contextes sont recréés dans la couche de données ; les dossiers, objets et invites le sont dans la couche métier. L'univers converti est généré à côté de la source.</p>
<p>Le même article indique que les droits de l'univers source sont repris : les droits généraux sont copiés, les droits spécifiques sont mis en correspondance, et les restrictions de lignes deviennent des profils de sécurité attribués aux mêmes utilisateurs et groupes. Il précise que les mots de passe d'univers ne sont pas convertis.</p>

<h2>Ce qui demande un traitement à part</h2>
<p>Plusieurs publications convergent sur les cas qui ne passent pas par la conversion automatique.</p>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Cas</th><th>Ce que disent les sources</th><th>Conséquence pratique</th></tr></thead>
<tbody>
<tr><td>Univers OLAP</td><td>SAP Community (deux articles) et <a href="https://clintvosloo.com/bi-2025-farewell-to-universe-design-tool-udt-and-unv-universes" rel="noopener">C. Vosloo</a> : ils ne se convertissent pas</td><td>Les recréer dans l'Information Design Tool</td></tr>
<tr><td>Sources Data Federator</td><td>Article IDT de SAP Community et C. Vosloo : non convertis</td><td>Revoir la source avant la montée de version</td></tr>
<tr><td>Fonction @Script</td><td>Article IDT de SAP Community : non convertie</td><td>Repérer les objets concernés avant conversion</td></tr>
<tr><td>Applications COM SDK</td><td>Article IDT de SAP Community : à réécrire avec le Semantic Layer Java SDK</td><td>Inventorier les applications qui l'utilisent</td></tr>
<tr><td>Univers multisources</td><td>Article IDT de SAP Community : retirés de BI 2025</td><td>Convertir en univers monosources</td></tr>
</tbody></table></div>
<p>Pour les fonctions @Select, @Where ou @Variable, les avis divergent. L'article IDT de SAP Community les indique comme converties. <a href="https://decinova.com/en/blog/conversion-unv-unx-sap-bo" rel="noopener">Decinova</a> estime qu'elles n'ont pas toujours d'équivalent direct et demandent parfois une reprise manuelle de la couche métier. La conséquence est la même : contrôler chaque objet utilisant une fonction @ après conversion.</p>

<h2>Les contextes et les jointures neutres</h2>
<p>L'article IDT de SAP Community décrit une nouvelle méthode de conversion des contextes à partir de BI 4.3 SP4 : les jointures d'un contexte sont converties en jointures incluses ou exclues, alors que les versions antérieures produisaient des jointures neutres. Il ajoute que les jointures neutres augmentent le temps d'exécution des requêtes Web Intelligence. Decinova range les contextes parmi les points de friction de la conversion. À vérifier : pour chaque univers qui utilisait des contextes, comparer les requêtes générées avant et après.</p>

<h2>Repointer les documents Web Intelligence</h2>
<p>Les trois sources s'accordent sur ce point : le plus lourd n'est pas la conversion de l'univers mais le repointage des documents. Un <a href="https://community.sap.com/t5/technology-blog-posts-by-sap/unv-is-dead-long-live-unx/ba-p/13568331" rel="noopener">article de SAP Community</a> juge le changement de source manuel peu praticable sur un grand parc. C. Vosloo indique que des documents construits sur un UNV ne s'actualisent plus tant qu'ils ne sont pas repointés vers un UNX. Pour les volumes importants, l'article de SAP Community cite l'assistant de workflow de SAP, des scripts SDK et des solutions de partenaires, dont APOS Migrator et Wiiisdom.</p>

<h2>Valider avant de basculer</h2>
<p>Decinova propose de convertir par lots de 5 à 10 univers en commençant par les plus simples, puis de comparer ligne à ligne les résultats des 5 à 10 rapports les plus utilisés sur l'ancien et le nouvel univers. Ces chiffres sont une recommandation de ce cabinet, pas une règle. Un autre <a href="https://community.sap.com/t5/technology-blog-posts-by-sap/unv-to-unx-conversion-guide-a-step-by-step-approach/ba-p/13623619" rel="noopener">article de SAP Community</a> décrit un processus outillé par Wiiisdom : comparaison côte à côte des valeurs, formats, structures et graphiques, avec un statut concordant ou non concordant, puis export pour validation métier. C. Vosloo recommande de tester l'ensemble, en particulier les planifications et les paramètres de sécurité.</p>
<p>Le tri préalable des rapports réduit le travail : inutile de repointer un document que personne n'ouvre (voir <a href="/trier-rapports-web-intelligence-migrer-refaire-supprimer/">trier les rapports</a> et <a href="/nettoyer-parc-businessobjects-documents-inutilises/">nettoyer le parc</a>).</p>

<h2>Profiter de la conversion pour alléger les univers</h2>
<p>L'article IDT de SAP Community recommande de se servir de la conversion pour revoir les univers : certains peuvent être devenus très volumineux, et même si l'outil n'impose pas de limite, il conseille une taille raisonnable, car de très grands schémas pénalisent l'édition comme l'interrogation. Il cite comme leviers :</p>
<ul>
<li>les familles et les vues de la couche de données, pour n'afficher qu'une partie des tables et des jointures ;</li>
<li>les dossiers et sous-dossiers de la couche métier ;</li>
<li>le partage d'une même connexion par plusieurs couches de données, et d'une même couche de données par plusieurs couches métier ;</li>
<li>les univers liés construits sur un univers noyau.</li>
</ul>
<p>Cette liste vient d'une seule source : elle illustre les possibilités de l'outil, et le bon découpage dépend de vos usages.</p>

<h2>Un ordre de travail possible</h2>
<ol>
<li>Inventorier les univers par type et repérer les cas du tableau 1.</li>
<li>Convertir par lots, en commençant par les univers simples.</li>
<li>Contrôler contextes, fonctions @, sécurité et mots de passe.</li>
<li>Repointer les documents, avec un outil si le parc est important.</li>
<li>Comparer les résultats sur les rapports les plus utilisés.</li>
<li>Alléger les univers, puis conserver l'ancien UNV jusqu'à la validation.</li>
</ol>
<p>AM DATA n'est revendeur ni de SAP ni de Microsoft. Que vous restiez sur BusinessObjects, montiez en BI 2025 ou migriez ailleurs, ce travail sur les univers aide à chiffrer le projet. Le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> inclut cet inventaire.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://community.sap.com/t5/technology-blog-posts-by-sap/sap-bi-2025-information-design-tool-overview/ba-p/14072941" rel="noopener">SAP Community : SAP BI 2025, Information Design Tool overview</a></li>
<li><a href="https://community.sap.com/t5/technology-blog-posts-by-sap/unv-is-dead-long-live-unx/ba-p/13568331" rel="noopener">SAP Community : UNV is dead, long live UNX</a></li>
<li><a href="https://community.sap.com/t5/technology-blog-posts-by-sap/unv-to-unx-conversion-guide-a-step-by-step-approach/ba-p/13623619" rel="noopener">SAP Community : UNV to UNX conversion guide, a step-by-step approach</a></li>
<li><a href="https://clintvosloo.com/bi-2025-farewell-to-universe-design-tool-udt-and-unv-universes" rel="noopener">C. Vosloo : BI 2025, farewell to Universe Design Tool and UNV universes</a></li>
<li><a href="https://decinova.com/en/blog/conversion-unv-unx-sap-bo" rel="noopener">Decinova : conversion UNV vers UNX, guide pragmatique</a></li>
</ul>
""",
 faqs=[
  ("Que faut-il vérifier après la conversion d'un univers UNV en UNX ?", "Les contextes, les objets utilisant des fonctions @, la sécurité et les mots de passe, puis le fonctionnement des documents Web Intelligence repointés. Les sources citées sur cette page convergent sur ces points."),
  ("Tous les univers UNV peuvent-ils être convertis ?", "Non. Selon SAP Community et C. Vosloo, les univers OLAP et ceux fondés sur Data Federator ne sont pas convertis ; les premiers doivent être recréés dans l'Information Design Tool."),
  ("Comment repointer les documents Web Intelligence vers l'UNX ?", "Avec la fonction de changement de source, document par document, ou avec des outils pour un grand parc : assistant de workflow de SAP, scripts SDK ou solutions de partenaires, selon un article de SAP Community."),
  ("Comment valider qu'un univers converti donne les mêmes résultats ?", "En comparant les résultats des rapports les plus utilisés sur l'ancien et le nouvel univers. Decinova propose de le faire par lots de 5 à 10 univers, avec 5 à 10 rapports par univers : c'est une recommandation, pas une règle."),
 ],
 related=["convertir-univers-unv-en-unx", "trier-rapports-web-intelligence-migrer-refaire-supprimer", "nettoyer-parc-businessobjects-documents-inutilises"],
)
