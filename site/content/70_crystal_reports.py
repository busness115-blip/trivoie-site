PAGE = dict(
 slug="crystal-reports-fin-maintenance-4-3-options",
 nav="Crystal Reports",
 title="Crystal Reports après la fin de maintenance de la 4.3",
 desc="Crystal Reports 2020, 2025 et Crystal Reports for Enterprise : dates de maintenance recoupées et trois options pour vos rapports après fin 2026.",
 h1="Crystal Reports après la fin de maintenance de la 4.3 : quelles options pour vos rapports",
 lead="Votre parc contient des rapports Crystal Reports et la maintenance standard de SAP BusinessObjects 4.3 s'arrête le 31 décembre 2026. Ce guide distingue les produits Crystal Reports concernés, donne les dates recoupées par plusieurs sources et présente trois options : rester, passer à Crystal Reports 2025, ou faire évoluer les rapports ailleurs.",
 published="2026-11-12", modified="2026-11-12",
 body="""
<h2>Crystal Reports n'est pas un seul produit</h2>
<p>Le nom recouvre plusieurs outils, qui n'ont pas le même calendrier. Il faut donc commencer par savoir lequel vous utilisez réellement.</p>
<ul>
<li><strong>Crystal Reports (client Windows)</strong> : l'éditeur de rapports « pixel perfect », décliné en versions 2016, 2020 et 2025.</li>
<li><strong>Crystal Reports for Enterprise</strong> : un autre éditeur, livré avec la plateforme BusinessObjects BI 4.x.</li>
<li><strong>Les rapports publiés sur la plateforme</strong> (fichiers .rpt), que les utilisateurs consultent via BI Launchpad.</li>
</ul>

<h2>Les dates de maintenance recoupées</h2>
<p>Les dates ci-dessous sont reprises par plusieurs publications indépendantes les unes des autres, qui les attribuent au calendrier de SAP. Les pages de SAP elles-mêmes n'étant pas consultables automatiquement, nous citons ces publications.</p>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Produit</th><th>Fin de la maintenance standard</th><th>Sources</th></tr></thead>
<tbody>
<tr><td>Crystal Reports 2016</td><td>Décembre 2022 ; support prioritaire terminé le 31 décembre 2024</td><td>RutterKey, Bold Reports, CxReports</td></tr>
<tr><td>Crystal Reports 2020</td><td>31 décembre 2026</td><td>DataTerrain, Bold Reports, RutterKey</td></tr>
<tr><td>Crystal Reports 2025</td><td>31 décembre 2027</td><td>DataTerrain, Bold Reports, RutterKey</td></tr>
</tbody></table></div>
<p>Pour Crystal Reports for Enterprise, Bold Reports, CxReports et NEED4VIZ indiquent qu'il n'est pas livré dans BI 2025. Les publications ne s'accordent pas sur une date de fin précise : nous n'en donnons pas.</p>
<p>Un point technique à vérifier si vous développez en .NET : DataTerrain et RutterKey indiquent que le runtime .NET 32 bits de Crystal Reports est abandonné après décembre 2025, ce qui impose le runtime 64 bits.</p>
<p>Ces quatre éditeurs (Bold Reports, CxReports, DataTerrain, RutterKey) proposent aussi des solutions de remplacement. Leurs dates concordent, mais leur lecture du risque peut être orientée vers la migration.</p>

<h2>Ce que change la fin de maintenance</h2>
<p>Elle ne désactive rien. DataTerrain et Bold Reports le rappellent : les rapports existants continuent de s'exécuter après la date. Ce qui s'arrête, ce sont les correctifs et les améliorations livrés au titre de la maintenance standard. Pour la plateforme elle-même, le détail de 2027 et 2028 est dans notre guide sur la <a href="/maintenance-specifique-client-sap-businessobjects/">maintenance spécifique client</a>.</p>

<h2>Trois options</h2>
<h3>Option 1 : rester sur l'existant</h3>
<p>Si vos rapports Crystal sont stables et peu nombreux, les laisser en place est un choix défendable, à condition de mesurer l'exposition. Un poste ou un serveur qui n'est plus corrigé doit être isolé et surveillé (<a href="/risque-securite-sap-businessobjects-4-3/">risque de sécurité</a>).</p>
<h3>Option 2 : passer à Crystal Reports 2025</h3>
<p>Elle repousse l'échéance de la maintenance standard au 31 décembre 2027, sans la supprimer. Pour les rapports construits avec Crystal Reports for Enterprise, il faut prévoir leur conversion vers Crystal Reports, puisque l'éditeur n'est plus livré dans BI 2025.</p>
<h3>Option 3 : faire évoluer les rapports vers un autre outil</h3>
<p>Bold Reports décrit deux approches : une migration assistée, qui réutilise les rapports comme point de départ avant validation, et une reconstruction manuelle. Il précise qu'il n'existe pas d'outil de migration en un clic. Quel que soit l'outil cible, comparez chaque rapport à sa version d'origine. Pour un passage vers Microsoft, voir <a href="/migration-businessobjects-power-bi/">la migration vers Power BI</a>. Pour un panorama des cibles, voir les <a href="/alternatives-sap-businessobjects/">alternatives à SAP BusinessObjects</a>.</p>

<h2>Trier avant de décider</h2>
<p>Bold Reports recommande un tri rapport par rapport : conserver ceux qui ont encore de la valeur, refaire ceux qui demandent une refonte, supprimer ceux qui ne servent plus. Cette méthode rejoint celle que nous décrivons pour le <a href="/nettoyer-parc-businessobjects-documents-inutilises/">nettoyage du parc</a>. Les <a href="/compter-documents-sap-businessobjects-query-builder/">requêtes Query Builder</a> permettent de compter les rapports réellement consultés.</p>
<p>AM DATA n'est revendeur ni de SAP ni de Microsoft : l'objectif est de documenter le choix, que vous restiez chez SAP ou que vous migriez. Le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> chiffre ce tri sur votre parc.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://dataterrain.com/bi-insights-hub/sap-crystal-reports-end-of-life" rel="noopener">SAP Crystal Reports End of Life (DataTerrain, octobre 2026)</a></li>
<li><a href="https://www.boldreports.com/crystal-reports-end-of-life/" rel="noopener">Crystal Reports End of Life (Bold Reports)</a></li>
<li><a href="https://www.boldreports.com/blog/crystal-reports-migration-vs-rebuild/" rel="noopener">Crystal Reports Migration vs. Manual Rebuild (Bold Reports)</a></li>
<li><a href="https://rutterkey.com/understanding-the-end-of-life-for-crystal-reports-and-why-modernization-matters/" rel="noopener">Understanding the End of Life for Crystal Reports (RutterKey)</a></li>
<li><a href="https://cx-reports.com/blog/crystal-reports-end-of-life" rel="noopener">Life After Crystal Reports (CxReports)</a></li>
<li><a href="https://www.need4viz.com/fr/businessobjects-fr/ce-quil-faut-comprendre-du-dernier-sod-sap-analytics-bi/" rel="noopener">Ce qu'il faut comprendre du dernier SoD SAP Analytics BI (NEED4VIZ, 14 octobre 2026)</a></li>
</ul>
<p>Les dates de maintenance peuvent évoluer. Vérifiez-les dans le portail SAP avant toute décision.</p>
""",
 faqs=[
  ("Jusqu'à quand Crystal Reports 2020 est-il maintenu ?", "Sa maintenance standard se termine le 31 décembre 2026, d'après DataTerrain, Bold Reports et RutterKey. Les rapports existants continuent de s'exécuter après cette date."),
  ("Jusqu'à quand Crystal Reports 2025 est-il maintenu ?", "Jusqu'au 31 décembre 2027 pour la maintenance standard, selon DataTerrain, Bold Reports et RutterKey."),
  ("Crystal Reports for Enterprise existe-t-il encore dans BI 2025 ?", "Non. Bold Reports, CxReports et NEED4VIZ indiquent qu'il n'est pas livré dans BI 2025. Les rapports concernés sont à convertir vers Crystal Reports ou à refaire ailleurs."),
  ("Mes rapports Crystal s'arrêtent-ils de fonctionner le 1er janvier 2027 ?", "Non. La fin de maintenance standard arrête les correctifs et améliorations, pas l'exécution des rapports existants."),
 ],
 related=["calendrier-fin-maintenance-sap-businessobjects-versions", "fin-maintenance-sap-businessobjects-4-3", "migration-businessobjects-power-bi", "nettoyer-parc-businessobjects-documents-inutilises"],
)
