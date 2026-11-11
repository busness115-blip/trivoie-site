PAGE = dict(
 slug="calendrier-fin-maintenance-sap-businessobjects-versions",
 nav="Calendrier des versions",
 title="Fin de maintenance SAP BusinessObjects : calendrier",
 desc="Dates de fin de maintenance de SAP BusinessObjects 4.1, 4.2, 4.3, BI 2025 et BI 2027, avec leurs sources, et ce que cela change pour votre parc.",
 h1="Calendrier de fin de maintenance de SAP BusinessObjects : 4.1, 4.2, 4.3, BI 2025 et BI 2027",
 lead="Quelle version de SAP BusinessObjects est encore maintenue, et jusqu'à quand ? Ce guide réunit les dates de fin de maintenance standard de chaque version, chacune rattachée à ses sources, et explique comment les lire pour décider de la suite : rester chez SAP ou migrer.",
 published="2026-11-11", modified="2026-11-11",
 body="""
<h2>Les dates version par version</h2>
<p>Chez SAP, une version passe par une maintenance standard, puis par une phase de support prioritaire (Priority-one) limitée aux problèmes critiques, puis par la maintenance spécifique client. Voici les dates publiées pour chaque version de la plateforme BI.</p>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Version</th><th>Fin de la maintenance standard</th><th>Phase suivante</th></tr></thead>
<tbody>
<tr><td>BI 4.1</td><td>31 décembre 2018</td><td>Support prioritaire jusqu'au 31 décembre 2020</td></tr>
<tr><td>BI 4.2</td><td>31 décembre 2022</td><td>Support prioritaire jusqu'au 31 décembre 2024</td></tr>
<tr><td>BI 4.3</td><td>31 décembre 2026</td><td>2027 : correctifs de sécurité graves seulement (CVSS 7 ou plus). Support prioritaire jusqu'au 31 décembre 2027 selon Wiiisdom. Plus aucun correctif à partir de 2028.</td></tr>
<tr><td>BI 2025</td><td>31 décembre 2027 (quatrième trimestre 2027)</td><td>Correctifs de sécurité jusqu'au quatrième trimestre 2028, selon Wiiisdom</td></tr>
<tr><td>BI 2027</td><td>Quatrième trimestre 2029, selon Wiiisdom</td><td>Sortie attendue au premier trimestre 2027, selon Wiiisdom</td></tr>
</tbody></table></div>
<p>Les dates de BI 4.1 viennent d'une annonce publiée sur le blog SAP Community et sont reprises par le site endoflife.ai. Celles de BI 4.2 sont données à l'identique par Wiiisdom, InfoSol et endoflife.ai. Celles de BI 4.3 et BI 2025 sont données par Wiiisdom, NTT DATA et endoflife.ai, qui renvoie à la note SAP 3763590. Les dates de BI 2027 ne sont publiées, à notre connaissance, que par Wiiisdom : nous les lui attribuons.</p>

<h2>Comment lire ce calendrier</h2>
<h3>Une version non maintenue n'est pas une version arrêtée</h3>
<p>Une plateforme dont la maintenance standard est terminée continue de fonctionner. Ce qui change, c'est la couverture : moins de correctifs, des délais non garantis, et à terme plus aucun correctif. Wiiisdom précise que toutes les versions peuvent bénéficier de la maintenance spécifique client dès la fin de la maintenance standard. Les conditions applicables à votre cas figurent dans votre contrat et auprès de votre interlocuteur SAP.</p>
<h3>Pour les versions 4.1 et 4.2</h3>
<p>Ces versions sont sorties de la maintenance standard depuis plusieurs années. InfoSol rappelle que BI 4.2 est hors maintenance standard depuis le 31 décembre 2022 et que son support prioritaire s'est terminé le 31 décembre 2024. Rester sur ces versions expose la plateforme à des vulnérabilités qui ne seront plus corrigées : le sujet est détaillé dans notre guide sur le <a href="/risque-securite-sap-businessobjects-4-3/">risque de sécurité</a>.</p>
<h3>Pour la version 4.3</h3>
<p>C'est l'échéance la plus proche : la maintenance standard s'arrête le 31 décembre 2026. Le détail de 2027 et de 2028 est dans le guide sur la <a href="/maintenance-specifique-client-sap-businessobjects/">maintenance spécifique client</a>. Autre point à ne pas oublier : les univers UNV ne sont plus pris en charge après la 4.3, ils doivent être convertis en UNX avant toute montée de version (<a href="/convertir-univers-unv-en-unx/">méthode de conversion</a>).</p>
<h3>Pour BI 2025 et BI 2027</h3>
<p>BI 2025 gagne un an de maintenance standard sur la 4.3. SAP suit un rythme d'une version environ tous les deux ans : monter en BI 2025 repousse l'échéance, mais ne la supprime pas. Le calcul à faire compare le coût de montées de version successives à celui d'une sortie de la plateforme (<a href="/sap-businessobjects-bi-2027/">ce que l'on sait de BI 2027</a>).</p>

<h2>Que faire de ces dates</h2>
<ol>
<li><strong>Identifier votre version et votre niveau de correctif</strong> exacts, dans la console d'administration (CMC).</li>
<li><strong>Mesurer ce qui est réellement utilisé</strong> : sur beaucoup de plateformes, une partie des documents n'est plus ouverte depuis des mois. Les <a href="/compter-documents-sap-businessobjects-query-builder/">requêtes Query Builder</a> donnent ces chiffres.</li>
<li><strong>Choisir l'horizon</strong> : rester en 4.3 sous maintenance spécifique, monter en BI 2025, ou migrer. Les deux premières options laissent une échéance en vue, la troisième demande un projet (<a href="/bi-2025-ou-sortir-de-businessobjects/">comparaison</a>).</li>
<li><strong>Faire cadrer le plan</strong> par un diagnostic chiffré si le périmètre est important.</li>
</ol>
<p>AM DATA n'est revendeur ni de SAP ni de Microsoft : l'objectif est de documenter le choix, que vous restiez chez SAP ou que vous migriez.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://wiiisdom.com/fr/blog/sap-bi-dates-de-fin-de-vie/" rel="noopener">SAP BI : dates de fin de vie (Wiiisdom)</a></li>
<li><a href="https://nttdata-solutions.com/uk/blog/preparing-for-the-end-of-life-of-sap-businessobjects-4-3-what-should-your-business-do/" rel="noopener">Fin de vie de SAP BusinessObjects 4.3 (NTT DATA)</a></li>
<li><a href="https://www.infosol.com/?p=15007" rel="noopener">SAP BusinessObjects BI 4.2 : l'équipe sécurité est-elle informée ? (InfoSol)</a></li>
<li><a href="https://endoflife.ai/sap-businessobjects" rel="noopener">Cycle de vie de SAP BusinessObjects BI (endoflife.ai)</a></li>
<li><a href="https://blogs.sap.com/2014/12/05/new-maintenance-dates-for-sap-businessobjects-bi41" rel="noopener">Nouvelles dates de maintenance de BI 4.1 (SAP Community, 2014)</a></li>
</ul>
<p>Les dates et règles de maintenance peuvent évoluer. Vérifiez-les dans le portail SAP (Product Availability Matrix et notes citées) avant toute décision.</p>
""",
 faqs=[
  ("Jusqu'à quand SAP BusinessObjects BI 4.2 est-il maintenu ?", "La maintenance standard de BI 4.2 s'est terminée le 31 décembre 2022, et son support prioritaire le 31 décembre 2024, selon Wiiisdom et InfoSol."),
  ("Quand s'arrête la maintenance standard de BI 4.3 ?", "Le 31 décembre 2026. En 2027, seuls les correctifs de sécurité graves (CVSS 7 ou plus) sont livrés, puis plus aucun correctif à partir de 2028."),
  ("Jusqu'à quand BI 2025 est-il maintenu ?", "La maintenance standard de BI 2025 va jusqu'au 31 décembre 2027. Wiiisdom indique des correctifs de sécurité jusqu'au quatrième trimestre 2028."),
  ("Quelle est la date de fin de maintenance de BI 4.1 ?", "La maintenance standard de BI 4.1 s'est terminée le 31 décembre 2018 et son support prioritaire le 31 décembre 2020, d'après une annonce de SAP Community."),
  ("Que devient une plateforme dont la maintenance est terminée ?", "Elle continue de fonctionner, mais avec une couverture réduite puis nulle en correctifs. La maintenance spécifique client peut s'appliquer, selon votre contrat."),
 ],
 related=["fin-maintenance-sap-businessobjects-4-3", "sap-businessobjects-bi-2027", "maintenance-specifique-client-sap-businessobjects", "bi-2025-ou-sortir-de-businessobjects"],
)
