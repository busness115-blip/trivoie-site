PAGE = dict(
 slug="trier-rapports-web-intelligence-migrer-refaire-supprimer",
 nav="Trier Web Intelligence",
 title="Trier ses rapports Web Intelligence avant la migration",
 desc="Web Intelligence : classez vos rapports en trois groupes, à migrer, à refaire ou à supprimer, avant la fin de maintenance de la 4.3. Méthode et sources.",
 h1="Web Intelligence : trier ses rapports à migrer, à refaire ou à supprimer",
 lead="Les documents Web Intelligence forment l'essentiel du parc d'un grand nombre d'installations SAP BusinessObjects. Avant de choisir entre rester chez SAP, passer à BI 2025 ou migrer ailleurs, un tri en trois groupes évite de payer pour déplacer des rapports que personne n'ouvre. Voici la méthode, avec les points techniques recoupés par plusieurs sources.",
 published="2026-11-13", modified="2026-11-13",
 body="""
<h2>Pourquoi trier avant de décider</h2>
<p>La maintenance standard de BI 4.3 s'arrête le 31 décembre 2026 (voir notre <a href="/fin-maintenance-sap-businessobjects-4-3/">guide sur la fin de maintenance</a>). Quel que soit le scénario retenu, le coût dépend d'abord du nombre de documents à traiter. Wiiisdom écrit que le nettoyage réduit la charge de travail, raccourcit la migration et facilite le dépannage. Trier est donc la première étape, avant tout chiffrage.</p>

<h2>Web Intelligence reste au catalogue de BI 2025</h2>
<p>Web Intelligence n'est pas retiré. SAP consacre un article de la communauté aux nouveautés de Web Intelligence dans BI 2025, et Dallas Marks, contributeur de la communauté SAP, le décrit comme l'une des applications les plus populaires de la suite, modernisée pour BI 2025. Rester sur la plateforme SAP est donc une option crédible pour les documents qui ont de la valeur. Ce sont les éléments qui les entourent qui peuvent imposer des travaux.</p>

<h2>Les trois groupes</h2>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Groupe</th><th>Critères de classement</th><th>Action</th></tr></thead>
<tbody>
<tr><td>À supprimer</td><td>Aucune ouverture récente, propriétaire parti, doublon d'un autre document, version de test</td><td>Archiver puis retirer du parc avant tout travail</td></tr>
<tr><td>À migrer</td><td>Utilisé régulièrement, source de données supportée, mise en page simple</td><td>Conserver tel quel (BI 2025) ou transposer vers l'outil cible</td></tr>
<tr><td>À refaire</td><td>Utilisé, mais dépendant d'une source ou d'un composant qui disparaît, ou devenu trop complexe</td><td>Reconstruire en partant du besoin, pas du document</td></tr>
</tbody></table></div>
<p>Cette grille est une méthode de travail, pas une règle de SAP. Les seuils (durée d'inactivité, nombre d'utilisateurs) sont à fixer avec les métiers.</p>

<h2>Repérer ce qui ne sert plus</h2>
<p>Le plus fiable est de mesurer l'usage réel plutôt que de demander aux équipes. Les <a href="/compter-documents-sap-businessobjects-query-builder/">requêtes Query Builder</a> permettent de compter les documents et leur dernière consultation, et le guide sur le <a href="/nettoyer-parc-businessobjects-documents-inutilises/">nettoyage du parc</a> détaille la démarche. À titre d'exemple de seuil, l'outil d'audit de Wiiisdom signale les contenus non utilisés depuis 13 mois ; ce choix est celui de cet éditeur, vous pouvez en retenir un autre. Avant toute suppression, faites une sauvegarde : Wiiisdom insiste sur ce point, car une conversion peut échouer ou créer des problèmes.</p>

<h2>Repérer ce qui doit être refait</h2>
<p>Trois points techniques font passer un document du groupe « à migrer » au groupe « à refaire » si vous visez BI 2025.</p>
<ul>
<li><strong>Les univers UNV.</strong> Le format UNV n'est pas pris en charge dans BI 2025, selon SAP (article sur les nouveautés de Web Intelligence) et Dallas Marks. Les univers doivent être convertis en UNX, voir <a href="/convertir-univers-unv-en-unx/">convertir un univers UNV en UNX</a>. Selon l'article de SAP, un document bâti sur un univers supprimé peut encore être ouvert pour changer sa source, mais plus actualisé.</li>
<li><strong>Les univers multisources.</strong> Dallas Marks indique qu'il n'existe pas de chemin automatique pour les ramener à une source unique : ils sont à reconstruire. Wiiisdom donne la même consigne pour les univers multisources UNX, à convertir en univers à source unique.</li>
<li><strong>Les documents Live Office, Analysis for OLAP et Lumira.</strong> Wiiisdom les classe parmi les contenus à reconstruire dans Web Intelligence ou dans un autre outil SAP. Dallas Marks précise de son côté que Live Office ne sera pas dans BI 2025 et que Crystal Reports for Enterprise n'en fait plus partie (voir <a href="/crystal-reports-fin-maintenance-4-3-options/">Crystal Reports après la 4.3</a>).</li>
</ul>
<p>Si vous visez un autre outil que BI 2025, la grille change : le critère devient la possibilité de reproduire le document, pas son format. Les pistes sont dans le guide <a href="/migration-businessobjects-power-bi/">migrer vers Power BI</a> et dans le panorama des <a href="/alternatives-sap-businessobjects/">alternatives</a>.</p>

<h2>Valider après chaque lot</h2>
<p>Wiiisdom recommande de vérifier que les documents fonctionnent après une conversion, avec des tests de régression automatisés si le volume le justifie, en commençant par les documents publics, qui ont le plus d'exposition, et par les rapports sensibles. Dans tous les cas, comparez les chiffres du rapport d'origine à ceux du rapport migré sur un même jeu de données.</p>

<h2>Et si le tri ne se fait pas en interne</h2>
<p>AM DATA n'est revendeur ni de SAP ni de Microsoft. Le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> réalise ce tri sur votre parc et en tire un scénario chiffré, que vous restiez chez SAP ou que vous partiez.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://community.sap.com/t5/technology-blog-posts-by-sap/sap-bi-2025-what-s-new-in-web-intelligence-and-semantic-layer/ba-p/14033408" rel="noopener">SAP BI 2025: What's new in Web Intelligence and Semantic Layer (SAP Community)</a></li>
<li><a href="https://community.sap.com/t5/technology-blog-posts-by-members/all-that-you-can-t-leave-behind-preparing-for-sap-businessobjects-bi-2025/ba-p/13992468" rel="noopener">All that you can't leave behind: preparing for SAP BusinessObjects BI 2025 (Dallas Marks, SAP Community)</a></li>
<li><a href="https://wiiisdom.com/blog/how-to-prepare-for-sap-businessobjects-bi-2025/" rel="noopener">How to prepare for SAP BusinessObjects BI 2025 (Wiiisdom)</a></li>
</ul>
<p>Les fonctions prises en charge évoluent avec les versions. Vérifiez-les dans la documentation SAP de la version visée.</p>
""",
 faqs=[
  ("Web Intelligence disparaît-il avec la fin de maintenance de la 4.3 ?", "Non. Web Intelligence figure dans BI 2025, avec des nouveautés décrites par SAP. Ce sont certains composants autour (univers UNV, Live Office) qui imposent des travaux."),
  ("Comment savoir quels rapports Web Intelligence sont inutilisés ?", "En mesurant l'usage plutôt qu'en interrogeant les équipes : les requêtes Query Builder donnent la dernière consultation de chaque document. Le seuil d'inactivité est à fixer avec les métiers."),
  ("Mes documents Web Intelligence sur univers UNV fonctionneront-ils dans BI 2025 ?", "Le format UNV n'y est pas pris en charge. Selon l'article de SAP sur BI 2025, un document bâti sur un univers supprimé peut être ouvert pour changer sa source, mais plus actualisé. Il faut convertir l'univers en UNX puis repointer le document."),
  ("Faut-il supprimer avant de migrer ?", "Oui, c'est le plus rentable, après sauvegarde. Wiiisdom indique que le nettoyage réduit la charge de travail et la durée de la migration."),
 ],
 related=["nettoyer-parc-businessobjects-documents-inutilises", "convertir-univers-unv-en-unx", "diagnostic-sortie-businessobjects", "checklist-migration-sap-businessobjects"],
)
