PAGE = dict(
 slug="analysis-for-microsoft-office-bi-2025-maintenu-changements",
 nav="Analysis for Office et BI 2025",
 title="Analysis for Microsoft Office dans BI 2025 : ce qui change",
 desc="Analysis for Microsoft Office est repris dans BI 2025, sans nouvelles fonctions. Ce que disent les analyses publiées et comment auditer vos classeurs.",
 h1="Analysis for Microsoft Office dans BI 2025 : ce qui est maintenu, ce que cela change",
 lead="Beaucoup d'utilisateurs de BusinessObjects travaillent dans Excel avec Analysis for Microsoft Office. Cette page rassemble ce que disent les analyses publiées sur son avenir dans BI 2025, distingue Analysis for Microsoft Office de l'édition pour OLAP, et propose une méthode pour auditer vos classeurs avant la fin de maintenance standard de la 4.3.",
 published="2026-11-26", modified="2026-11-26",
 body="""
<h2>Deux outils différents sous un nom proche</h2>
<p>Le Statement of Direction de SAP, tel que le lit NEED4VIZ, traite séparément deux produits qu'il ne faut pas confondre. <strong>Analysis for Microsoft Office</strong> (parfois abrégé AO) est le complément Excel et PowerPoint. <strong>Analysis, edition for OLAP</strong> est un outil distinct, qui figure dans la liste des composants dont la maintenance standard s'arrête fin 2026. Un parc peut utiliser l'un, l'autre ou les deux : vérifiez lequel avant de lire la suite.</p>

<h2>Ce que disent les analyses publiées</h2>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Point</th><th>Ce qui est écrit</th><th>Source</th></tr></thead>
<tbody>
<tr><td>Présence dans BI 2025</td><td>Analysis for Microsoft Office figure parmi les outils les plus adoptés sur lesquels BI 2025 se concentre.</td><td>Wiiisdom</td></tr>
<tr><td>Maintenance</td><td>L'outil reste maintenu et pris en charge au rythme des versions de BI, sans nouvelle fonctionnalité prévue.</td><td>NEED4VIZ</td></tr>
<tr><td>Développements futurs</td><td>SAP concentre ses développements futurs sur le complément Excel de SAP Analytics Cloud ; Analysis for Microsoft Office est en mode maintenance (article de juin 2024).</td><td>Nextlytics</td></tr>
<tr><td>Edition for OLAP</td><td>Dernière version en 4.3, fin de maintenance standard fin 2026. Alternatives citées : SAP Analytics Cloud ou Web Intelligence. NTT DATA range aussi Analysis for OLAP parmi les composants retirés de BI 2025.</td><td>NEED4VIZ, NTT DATA</td></tr>
<tr><td>Live Office</td><td>Fin de maintenance standard fin 2026 ; Analysis for Microsoft Office est l'une des alternatives citées, avec Web Intelligence et Crystal Reports.</td><td>NEED4VIZ</td></tr>
</tbody></table></div>
<p>Aucune des sources consultées ne donne de date de fin de maintenance propre à Analysis for Microsoft Office : nous n'en indiquons donc pas. La seule formulation disponible est celle de NEED4VIZ, qui l'attribue au rythme des versions de BI.</p>

<h2>Ce que cela change concrètement</h2>
<h3>Pour ceux qui restent chez SAP</h3>
<p>Le maintien de l'outil dans BI 2025 est une bonne nouvelle pour les classeurs existants, à condition d'accepter qu'il n'évolue plus. Selon Nextlytics, les nouveaux modèles SAP Analytics Cloud et les jeux de données analytiques de Datasphere ne se lisent que depuis le complément Excel de SAP Analytics Cloud, et ce dernier ne se connecte pas directement à SAP BW. Les deux compléments ne sont donc pas interchangeables : le choix dépend de vos sources de données.</p>
<h3>Pour ceux qui migrent</h3>
<p>Si vous quittez la plateforme, les classeurs Excel branchés sur des univers ou des requêtes demandent une reconstruction côté nouvelle plateforme. Les sources branchées directement sur BW, BPC, HANA ou S/4HANA suivent une autre logique, que Nextlytics décrit comme prise en charge par Analysis for Microsoft Office. Elles se traitent donc à part de la migration des rapports.</p>
<h3>Le rappel sur les échéances de la 4.3</h3>
<p>NTT DATA rappelle que la maintenance standard de BusinessObjects 4.3 se termine le 31 décembre 2026. Voir notre <a href="/calendrier-fin-maintenance-sap-businessobjects-versions/">calendrier des versions</a> et la page sur la <a href="/maintenance-specifique-client-sap-businessobjects/">maintenance spécifique client</a>.</p>

<h2>Méthode d'audit des classeurs Excel</h2>
<h3>1. Lister les classeurs réellement utilisés</h3>
<p>Interrogez la base d'audit de la plateforme et le suivi d'usage des postes : un classeur non ouvert depuis douze mois n'a ni à être migré ni à être maintenu.</p>
<h3>2. Identifier la source de chaque classeur</h3>
<p>Séparez les classeurs branchés sur une source SAP directe (BW, HANA, S/4HANA), ceux branchés sur la plateforme BI et ceux qui s'appuient sur un composant absent de BI 2025, comme décrit dans notre <a href="/composants-absents-bi-2025-inventaire-parc-businessobjects/">inventaire des composants</a>.</p>
<h3>3. Classer par criticité</h3>
<p>Repérez les classeurs qui alimentent la clôture, le reporting réglementaire ou le pilotage de direction, car ce sont ceux dont l'interruption coûte le plus.</p>
<h3>4. Décider classeur par classeur</h3>
<p>Conserver, convertir vers un autre outil, ou retirer. AM DATA n'est revendeur ni de SAP ni de Microsoft : cet audit documente un choix, que vous restiez chez SAP ou non. Le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> le réalise sur votre parc.</p>

<h2>Limites de ces informations</h2>
<p>Ces publications sont des analyses de partenaires et d'éditeurs tiers, dont certains proposent des offres dans ce domaine. Elles ne remplacent pas le Statement of Direction de SAP, que vous pouvez consulter avant toute décision. L'article de Nextlytics date de 2024 et la liste des composants évolue à chaque mise à jour du document de SAP.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://wiiisdom.com/blog/sap-businessobjects-bi-2025/" rel="noopener">SAP BusinessObjects BI 2025 : what do we know about it ? (Wiiisdom)</a></li>
<li><a href="https://www.need4viz.com/businessobjects-en/understanding-saps-latest-analytics-bi-statement-of-direction/" rel="noopener">Understanding SAP's Latest Analytics BI Statement of Direction (NEED4VIZ)</a></li>
<li><a href="https://www.nextlytics.com/blog/sap-analysis-for-office-vs.-sap-analytics-cloud-excel-add-in" rel="noopener">SAP Analysis for Office vs. SAP Analytics Cloud Add-In (Nextlytics)</a></li>
<li><a href="https://nttdata-solutions.com/uk/blog/preparing-for-the-end-of-life-of-sap-businessobjects-4-3-what-should-your-business-do/" rel="noopener">Preparing for the End of Life of SAP BusinessObjects 4.3 (NTT DATA)</a></li>
</ul>
""",
 faqs=[
  ("Analysis for Microsoft Office existe-t-il dans BI 2025 ?", "Oui. Wiiisdom le cite parmi les outils sur lesquels BI 2025 se concentre, et NEED4VIZ indique qu'il reste maintenu au rythme des versions de BI."),
  ("Analysis for Microsoft Office va-t-il recevoir de nouvelles fonctions ?", "NEED4VIZ écrit que SAP ne prévoit pas de nouvelle fonctionnalité. Nextlytics précise que SAP concentre ses développements futurs sur le complément Excel de SAP Analytics Cloud."),
  ("Quelle différence avec Analysis, edition for OLAP ?", "Ce sont deux outils distincts. Selon NEED4VIZ, l'édition pour OLAP a sa dernière version en 4.3 et sa maintenance standard s'arrête fin 2026. NTT DATA la range parmi les composants retirés de BI 2025."),
  ("Mes classeurs Excel doivent-ils être refaits ?", "Cela dépend de leur source. Auditez-les un par un : un classeur sans usage sur douze mois n'a pas besoin d'être migré."),
 ],
 related=["composants-absents-bi-2025-inventaire-parc-businessobjects", "bi-2025-ou-sortir-de-businessobjects", "calendrier-fin-maintenance-sap-businessobjects-versions"],
)
