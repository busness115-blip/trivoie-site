PAGE = dict(
 slug="lumira-designer-design-studio-avenir",
 nav="Lumira Designer",
 title="Lumira Designer et Design Studio : quel avenir ?",
 desc="Lumira Discovery absent de BI 2025, Lumira Designer maintenu sans nouveautés : ce que disent les sources et trois options pour vos tableaux de bord.",
 h1="Lumira Designer et Design Studio : quel avenir pour vos tableaux de bord",
 lead="Votre parc BusinessObjects contient des applications Design Studio ou Lumira, et la maintenance standard de la 4.3 s'arrête le 31 décembre 2026. Ce guide distingue les produits concernés, rapporte ce que disent plusieurs analyses indépendantes de BI 2025, et présente trois options : rester sur Lumira Designer, passer à SAP Analytics Cloud, ou reconstruire ailleurs.",
 published="2026-11-16", modified="2026-11-16",
 body="""
<h2>Design Studio, Lumira Designer, Lumira Discovery : de quoi parle-t-on ?</h2>
<p>Les noms ont changé avec le temps, ce qui brouille l'inventaire. Il faut donc commencer par savoir ce que vous utilisez réellement.</p>
<ul>
<li><strong>Design Studio</strong> : l'outil de création d'applications de tableaux de bord. Il a été renommé SAP Lumira Designer 2.0, comme le rappellent un article de la communauté SAP consacré à BI 2025 et NEED4VIZ.</li>
<li><strong>Lumira Designer</strong> : le nom actuel de cet outil, avec une version compatible BI 2025.</li>
<li><strong>Lumira Discovery</strong> : l'outil de visualisation et d'exploration en libre-service, issu de Lumira Desktop. Il est distinct de Lumira Designer.</li>
</ul>

<h2>Ce qui est recoupé pour BI 2025</h2>
<p>Plusieurs publications indépendantes concordent sur les deux points suivants.</p>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Produit</th><th>Situation dans BI 2025</th><th>Sources</th></tr></thead>
<tbody>
<tr><td>Lumira Designer</td><td>Maintenu et pris en charge, sans nouvelles fonctionnalités</td><td>Wiiisdom, communauté SAP (article de membre), NEED4VIZ, Decinova</td></tr>
<tr><td>Lumira Discovery</td><td>Non pris en charge dans BI 2025 ; reste disponible dans la 4.3</td><td>Communauté SAP (article de membre), NEED4VIZ, Decinova, D. Marks (BOB Board)</td></tr>
</tbody></table></div>
<p>Wiiisdom écrit que Lumira Designer continuera d'être maintenu et supporté dans BI 2025 sans nouvelles fonctionnalités. L'article de la communauté SAP résume : « supported does not mean enhanced ». NEED4VIZ désigne SAP Analytics Cloud comme successeur désigné de Lumira pour les tableaux de bord.</p>
<p>Pour Design Studio, il n'y a pas de calendrier distinct à chercher : l'outil a été renommé et suit celui de Lumira Designer.</p>

<h2>Dates annoncées par une seule analyse</h2>
<p>NEED4VIZ, dans son analyse du dernier Statement of Direction, indique que la fin de la maintenance standard de Lumira Designer se situe à la fin de 2031, que sa dernière version est celle de BI 2029, et que la fin de la maintenance standard de Lumira Discovery est fixée à la fin de 2026. Le blog de graphomate reprend la date de 2031, en précisant qu'il s'appuie sur un webinaire de NEED4VIZ : ce n'est donc pas une confirmation indépendante. Nous attribuons ces dates à NEED4VIZ.</p>
<p>NEED4VIZ ajoute qu'aucune équivalence avec Web Intelligence n'est annoncée : SAP recommande une transition, sans garantir que Web Intelligence couvre tous les usages de Lumira Designer. Il note aussi que BI 2027 doit apporter deux types de rapports Web Intelligence, dont l'un pourrait reprendre une partie des usages de Lumira Designer, sans que son périmètre soit connu. Pour BI 2027, voir notre <a href="/sap-businessobjects-bi-2027/">guide dédié</a>.</p>

<h2>Ce que cela change pour vous</h2>
<p>Rien ne s'arrête brutalement. Les applications existantes continuent de s'exécuter tant que la plateforme tourne. En revanche, aucune nouveauté n'est attendue pour Lumira Designer, et Lumira Discovery ne suit pas vers BI 2025. Si votre plateforme reste en 4.3 après le 31 décembre 2026, le cadre est celui de la <a href="/maintenance-specifique-client-sap-businessobjects/">maintenance spécifique client</a> décrite dans nos autres guides.</p>

<h2>Trois options</h2>
<h3>Option 1 : rester sur Lumira Designer</h3>
<p>Il est maintenu dans BI 2025. Cette voie convient si vos applications sont stables, peu nombreuses et que personne ne demande d'évolution. Elle repousse la question sans la résoudre : plus de nouveautés, et une dépendance à un outil dont le successeur désigné est ailleurs.</p>
<h3>Option 2 : passer à SAP Analytics Cloud</h3>
<p>C'est la voie indiquée par NEED4VIZ et Decinova comme alternative à Lumira. Elle reste dans l'écosystème SAP, mais elle suppose de reconstruire les applications, car un tableau de bord Lumira ne se convertit pas à l'identique. Prévoyez la comparaison de chaque application avec sa version d'origine.</p>
<h3>Option 3 : reconstruire avec un autre outil</h3>
<p>NEED4VIZ, qui édite une solution concurrente, propose la sienne comme remplacement. Il faut lire cette position en sachant qu'elle est celle d'un éditeur. D'autres cibles existent : voir les <a href="/alternatives-sap-businessobjects/">alternatives à SAP BusinessObjects</a> et la <a href="/migration-businessobjects-power-bi/">migration vers Power BI</a>.</p>

<h2>Inventorier avant de choisir</h2>
<p>Comptez les applications Design Studio et Lumira réellement ouvertes ces douze derniers mois. Beaucoup de parcs en contiennent qui ne servent plus : le tri décrit dans notre guide sur le <a href="/nettoyer-parc-businessobjects-documents-inutilises/">nettoyage du parc</a> s'applique aussi à elles. AM DATA n'est revendeur ni de SAP ni de Microsoft : l'objectif est de documenter le choix, que vous restiez chez SAP ou que vous migriez. Le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> chiffre ce tri sur votre parc.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://wiiisdom.com/blog/sap-businessobjects-bi-2025/" rel="noopener">SAP BusinessObjects BI 2025 : what do we know about it ? (Wiiisdom)</a></li>
<li><a href="https://community.sap.com/t5/technology-blog-posts-by-members/all-that-you-can-t-leave-behind-preparing-for-sap-businessobjects-bi-2025/ba-p/13992468" rel="noopener">All That You Can't Leave Behind : Preparing for SAP BusinessObjects BI 2025 (communauté SAP)</a></li>
<li><a href="https://www.need4viz.com/businessobjects-en/understanding-saps-latest-analytics-bi-statement-of-direction/" rel="noopener">Understanding SAP's Latest Analytics BI Statement of Direction (NEED4VIZ)</a></li>
<li><a href="https://www.need4viz.com/businessobjects-en/after-lumira-and-design-studio-what-are-your-options/" rel="noopener">After Lumira and Design Studio : what are your options ? (NEED4VIZ)</a></li>
<li><a href="https://decinova.com/en/blog/sap-bo-bi-2025" rel="noopener">SAP BO BI 2025 : what's changing, what's retiring (Decinova)</a></li>
<li><a href="https://bobj-board.org/t/end-of-life-for-lumira/255834" rel="noopener">End of life for Lumira (BusinessObjects Board)</a></li>
<li><a href="https://www.graphomate.com/en/2026/02/der-support-fuer-sap-lumira-designer-endet-erst-2031/" rel="noopener">Support for SAP Lumira Designer ends not until 2031 (graphomate)</a></li>
</ul>
""",
 faqs=[
  ("Lumira Designer est-il pris en charge dans BI 2025 ?", "Oui. Wiiisdom, NEED4VIZ, Decinova et un article de la communauté SAP indiquent qu'il est maintenu dans BI 2025, sans nouvelles fonctionnalités."),
  ("Lumira Discovery existe-t-il dans BI 2025 ?", "Non. Il n'est pas pris en charge dans BI 2025 selon la communauté SAP, NEED4VIZ et Decinova. Il reste disponible dans la 4.3."),
  ("Design Studio et Lumira Designer, est-ce le même outil ?", "Oui. Design Studio a été renommé SAP Lumira Designer 2.0, comme l'indiquent un article de la communauté SAP et NEED4VIZ."),
  ("Mes applications Lumira s'arrêtent-elles le 1er janvier 2027 ?", "Non. Les applications existantes continuent de s'exécuter. Ce qui change, ce sont les correctifs et nouveautés livrés au titre de la maintenance standard."),
  ("Quelle est la cible recommandée pour remplacer Lumira ?", "NEED4VIZ et Decinova citent SAP Analytics Cloud comme alternative désignée. D'autres cibles existent, et le choix dépend de votre parc et de vos usages."),
 ],
 related=["calendrier-fin-maintenance-sap-businessobjects-versions", "sap-businessobjects-bi-2027", "alternatives-sap-businessobjects", "bi-2025-ou-sortir-de-businessobjects"],
)
