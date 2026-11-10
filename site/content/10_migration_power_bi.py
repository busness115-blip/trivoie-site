PAGE = dict(
 slug="migration-businessobjects-power-bi",
 title="Migration SAP BusinessObjects vers Power BI : méthode",
 desc="Migrer SAP BusinessObjects (Webi, Crystal, univers) vers Power BI : correspondances, étapes, pièges, et pourquoi trier le parc avant de convertir quoi que ce soit.",
 h1="Migrer SAP BusinessObjects vers Power BI : méthode, correspondances et pièges",
 lead="Avec la fin de la maintenance standard de la 4.3 le 31 décembre 2026, beaucoup d'organisations envisagent de passer de SAP BusinessObjects à Power BI. Ce guide décrit ce qui se transpose, ce qui se refait, et l'ordre qui évite de payer la migration de rapports que personne n'ouvre.",
 published="2026-11-10", modified="2026-11-10",
 body="""
<h2>Ce qui se transpose, ce qui se refait</h2>
<p>Il n'existe pas de conversion automatique complète d'un parc BusinessObjects vers Power BI. Des outils tiers en automatisent une partie, mais chaque objet doit être revu. Les correspondances habituelles :</p>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>SAP BusinessObjects</th><th>Équivalent Power BI</th><th>Point d'attention</th></tr></thead>
<tbody>
<tr><td>Univers UNX ou UNV</td><td>Modèle sémantique</td><td>Les objets, filtres et jointures de l'univers sont à reconstruire. C'est souvent le plus gros du travail.</td></tr>
<tr><td>Rapport Web Intelligence interactif</td><td>Rapport Power BI</td><td>Un document Webi à plusieurs requêtes fusionnées demande de repenser le modèle, pas seulement la page.</td></tr>
<tr><td>Rapport Webi très mis en page, Crystal Reports</td><td>Rapport paginé (Power BI Report Builder)</td><td>Adapté aux documents imprimables, avec sections et ruptures.</td></tr>
<tr><td>Planifications et publications</td><td>Abonnements et actualisations planifiées</td><td>Les diffusions personnalisées par destinataire sont à recenser une par une.</td></tr>
<tr><td>Droits sur dossiers et restrictions d'univers</td><td>Espaces de travail et sécurité au niveau des lignes</td><td>Les règles de sécurité doivent être réécrites et testées.</td></tr>
</tbody></table></div>

<h2>Les étapes dans le bon ordre</h2>
<ol>
<li><strong>Inventorier</strong> : nombre de documents par type, univers UNV et UNX, comptes, planifications. Les <a href="/compter-documents-sap-businessobjects-query-builder/">requêtes Query Builder</a> donnent ces chiffres en une heure.</li>
<li><strong>Mesurer l'usage réel</strong> avec la base d'audit : quels documents ont été ouverts depuis 12 mois, et par qui. Ce qui n'est pas utilisé ne se migre pas (<a href="/nettoyer-parc-businessobjects-documents-inutilises/">méthode</a>).</li>
<li><strong>Regrouper</strong> les rapports qui se ressemblent : plusieurs documents Webi proches deviennent souvent un seul rapport Power BI avec des filtres.</li>
<li><strong>Reconstruire les modèles sémantiques</strong> à partir des univers réellement utilisés.</li>
<li><strong>Recetter</strong> chaque rapport en comparant les chiffres avec BusinessObjects, sur les mêmes données.</li>
<li><strong>Faire tourner les deux outils en parallèle</strong> le temps de la recette, puis décommissionner BusinessObjects.</li>
</ol>

<h2>Les pièges les plus coûteux</h2>
<ul>
<li><strong>Migrer tout le parc</strong> sans tri préalable : on paie la reconstruction et la recette de documents abandonnés.</li>
<li><strong>Sous-estimer la couche sémantique</strong> : les règles métier codées dans les univers depuis des années ne sont documentées nulle part ailleurs.</li>
<li><strong>Oublier les diffusions</strong> : publications, envois par e-mail et exports planifiés sont souvent ce que les métiers remarquent en premier quand ils disparaissent.</li>
<li><strong>Laisser la 4.3 sans plan</strong> pendant la migration : à partir de 2027, seuls les correctifs de sécurité graves sont livrés, et plus aucun à partir de 2028 (<a href="/maintenance-specifique-client-sap-businessobjects/">détail</a>).</li>
</ul>

<h2>Power BI, BI 2025 ou autre chose ?</h2>
<p>Power BI n'est pas la seule voie. Monter en BI 2025, puis en BI 2027, garde les rapports existants mais impose une montée de version environ tous les deux ans. Le bon choix dépend du volume réellement utilisé, du nombre d'univers et de l'horizon souhaité (<a href="/bi-2025-ou-sortir-de-businessobjects/">comparaison</a>).</p>
""",
 faqs=[
  ("Peut-on convertir automatiquement des rapports Webi en Power BI ?", "Pas entièrement. Des outils tiers automatisent une partie de la conversion, mais les univers, les requêtes fusionnées, la sécurité et la mise en page demandent une reprise et une recette rapport par rapport."),
  ("Combien coûte une migration de BusinessObjects vers Power BI ?", "Le coût dépend surtout du nombre de documents réellement utilisés et du nombre d'univers à reconstruire. C'est pourquoi l'inventaire et la mesure de l'usage passent avant toute estimation."),
  ("Par quoi remplacer Crystal Reports dans Power BI ?", "Les rapports paginés, conçus avec Power BI Report Builder, sont l'équivalent le plus proche pour les documents mis en page et imprimables."),
  ("Faut-il migrer avant le 31 décembre 2026 ?", "Pas forcément, mais il faut avoir choisi sa voie. À partir de 2027, la 4.3 ne reçoit plus que les correctifs de sécurité graves, et plus aucun à partir de 2028."),
 ],
 related=["bi-2025-ou-sortir-de-businessobjects", "nettoyer-parc-businessobjects-documents-inutilises", "diagnostic-sortie-businessobjects", "alternatives-sap-businessobjects"],
)
