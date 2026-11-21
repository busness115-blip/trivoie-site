PAGE = dict(
 slug="checklist-daf-maintenance-specifique-client-businessobjects",
 nav="Checklist DAF : maintenance spécifique",
 title="Maintenance spécifique SAP BO : checklist pour le DAF",
 desc="Budget, contrat, échéances : la checklist du DAF pour décider avant le 31/12/2026 entre maintenance spécifique client, BI 2025 ou sortie de BusinessObjects.",
 h1="Maintenance spécifique client SAP BusinessObjects : checklist pour le DAF (budget, contrat, échéances)",
 lead="Pour une direction financière, la fin de maintenance standard de SAP BusinessObjects BI 4.3 le 31 décembre 2026 se traduit en trois questions : que paie-t-on en 2027, quelles dates imposent une décision, et que doit-on vérifier dans le contrat. Cette checklist rassemble les faits publiés par des analystes indépendants et les questions à poser à votre interlocuteur SAP. Elle ne constitue pas un avis juridique ni comptable.",
 published="2026-11-21", modified="2026-11-21",
 body="""
<h2>Les faits qui comptent pour le budget</h2>
<p>Selon <a href="https://wiiisdom.com/blog/sap-bi-end-of-life-stages/" rel="noopener">Wiiisdom</a>, <a href="https://nttdata-solutions.com/uk/blog/preparing-for-the-end-of-life-of-sap-businessobjects-4-3-what-should-your-business-do/" rel="noopener">NTT DATA</a> et <a href="https://clintvosloo.com/sap-customer-specific-maintenance-bi-43-ds-43-what-it-means" rel="noopener">C. Vosloo</a>, la maintenance standard de BI 4.3 se termine le 31 décembre 2026. Wiiisdom et C. Vosloo indiquent qu'après la première année de maintenance spécifique client, aucune livraison logicielle (support package, correctif) n'a plus lieu. Le détail du régime figure dans notre page sur la <a href="/maintenance-specifique-client-sap-businessobjects/">maintenance spécifique client</a>.</p>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Point</th><th>Ce que disent les sources</th><th>Source</th></tr></thead>
<tbody>
<tr><td>Fin de maintenance standard de BI 4.3</td><td>31 décembre 2026</td><td>Wiiisdom, NTT DATA, C. Vosloo</td></tr>
<tr><td>Fin de maintenance standard de BI 2025</td><td>31 décembre 2027 selon C. Vosloo ; quatrième trimestre 2027 selon Wiiisdom</td><td>C. Vosloo, Wiiisdom</td></tr>
<tr><td>Correctifs de sécurité en 2027</td><td>Limités aux failles de gravité élevée ou critique (CVSS 7,0 ou plus)</td><td>C. Vosloo</td></tr>
<tr><td>Frais de maintenance</td><td>Les frais du contrat restent dus selon C. Vosloo, qui titre « mêmes frais »</td><td>C. Vosloo</td></tr>
<tr><td>Engagements de délai de service</td><td>Plus délivrés en maintenance spécifique client</td><td>C. Vosloo</td></tr>
<tr><td>Problème nouveau, non connu</td><td>Son traitement est un service de conseil facturable</td><td>C. Vosloo</td></tr>
<tr><td>Souscription</td><td>Pas de commande explicite à passer pour entrer dans le régime</td><td>C. Vosloo</td></tr>
</tbody></table></div>
<p>Les lignes à source unique sont attribuées à leur auteur : elles décrivent l'analyse de C. Vosloo des notes SAP 3486924 et 3763590, et non un document que nous aurions consulté directement. Votre contrat reste la référence.</p>

<h2>Checklist budget</h2>
<ol>
<li>Relever le montant annuel de maintenance actuellement payé pour la plateforme, par licence ou par contrat, et la date de renouvellement.</li>
<li>Chiffrer l'hypothèse « rester » : frais de maintenance inchangés selon C. Vosloo, plus une provision pour du conseil facturable si un problème nouveau survient.</li>
<li>Chiffrer l'hypothèse « BI 2025 » : licences ou droits d'usage éventuels, projet de montée de version, tests, formation. Voir <a href="/bi-2025-ou-sortir-de-businessobjects/">BI 2025 ou sortie</a>.</li>
<li>Chiffrer l'hypothèse « sortie » : projet de migration, double exploitation, arrêt de la maintenance à terme. Voir la <a href="/migration-businessobjects-power-bi/">migration vers Power BI</a> et les <a href="/alternatives-sap-businessobjects/">alternatives</a>.</li>
<li>Prévoir une provision pour sécurité complémentaire si la plateforme reste : isolement réseau, supervision, revue des droits (voir <a href="/securite-plateforme-bi-droits-comptes-audit-businessobjects/">sécurité d'une plateforme BI</a>).</li>
<li>Comparer les trois hypothèses sur au moins deux exercices, 2027 et 2028, car le régime change au bout de la première année.</li>
</ol>

<h2>Checklist contrat</h2>
<p>Ces points sont des questions à poser, pas des affirmations sur ce que contient votre contrat :</p>
<ul>
<li>Quels sont les frais de maintenance facturés pour 2027, et selon quelle base ?</li>
<li>Quelles clauses du contrat s'appliquent à un traitement de problème facturé comme du conseil ?</li>
<li>Quelle date de renouvellement ou de préavis s'applique, et peut-on réduire le périmètre de licences non utilisées ? Le <a href="/nettoyer-parc-businessobjects-documents-inutilises/">nettoyage du parc</a> fournit les chiffres d'usage.</li>
<li>Qui, côté SAP ou partenaire, est l'interlocuteur pour les droits d'accès aux supports d'installation d'une migration ?</li>
<li>Si un prestataire intervient, qui porte le risque en cas de panne sans engagement de délai de la part de l'éditeur ?</li>
</ul>

<h2>Échéances à inscrire au calendrier</h2>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 2 (défilement horizontal)"><table>
<thead><tr><th>Date</th><th>Événement</th><th>Décision attendue</th></tr></thead>
<tbody>
<tr><td>Avant le 31 décembre 2026</td><td>Fin de maintenance standard de BI 4.3</td><td>Choisir : rester, monter en BI 2025 ou sortir</td></tr>
<tr><td>Du 1er janvier au 31 décembre 2027</td><td>Première année de maintenance spécifique client, avec correctifs de sécurité CVSS 7 ou plus</td><td>Lancer le projet retenu</td></tr>
<tr><td>31 décembre 2027</td><td>Fin de maintenance standard de BI 2025 (C. Vosloo)</td><td>Planifier la suite si BI 2025 est retenu</td></tr>
<tr><td>Début 2028</td><td>Plus de livraison logicielle sur BI 4.3 (Wiiisdom, C. Vosloo)</td><td>Avoir migré, ou assumer et documenter le risque</td></tr>
</tbody></table></div>

<h2>Ce que le DAF peut demander à la DSI</h2>
<ol>
<li>Le nombre d'utilisateurs actifs sur douze mois, de documents consultés et d'univers réellement utilisés.</li>
<li>Les trois options chiffrées, avec la même méthode de calcul.</li>
<li>Le nom du responsable du risque si la plateforme reste en maintenance spécifique client.</li>
<li>La date à laquelle la décision suivante sera prise.</li>
</ol>
<p>AM DATA n'est revendeur ni de SAP ni de Microsoft. Le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> produit ces chiffres et compare les options sans position d'éditeur : rester chez SAP est une réponse légitime quand les chiffres la justifient.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://wiiisdom.com/blog/sap-bi-end-of-life-stages/" rel="noopener">Wiiisdom : étapes de fin de vie de SAP BI (28 janvier 2026)</a></li>
<li><a href="https://nttdata-solutions.com/uk/blog/preparing-for-the-end-of-life-of-sap-businessobjects-4-3-what-should-your-business-do/" rel="noopener">NTT DATA : préparer la fin de vie de BusinessObjects 4.3</a></li>
<li><a href="https://clintvosloo.com/sap-customer-specific-maintenance-bi-43-ds-43-what-it-means" rel="noopener">C. Vosloo : maintenance spécifique client SAP, ce que cela signifie</a></li>
</ul>
""",
 faqs=[
  ("Les frais de maintenance changent-ils en maintenance spécifique client ?", "Selon l'analyse de C. Vosloo, le client continue de payer les frais de maintenance prévus par son contrat. Vérifiez votre contrat auprès de votre interlocuteur SAP."),
  ("Faut-il commander la maintenance spécifique client ?", "Selon C. Vosloo, elle n'a pas à être commandée explicitement pour s'appliquer. Confirmez les modalités propres à votre contrat auprès de SAP."),
  ("Quand faut-il décider ?", "La maintenance standard de BI 4.3 se termine le 31 décembre 2026 (Wiiisdom, NTT DATA, C. Vosloo). Plus aucune livraison logicielle n'a lieu après la première année de maintenance spécifique client (Wiiisdom, C. Vosloo)."),
  ("Qui facture un problème nouveau en 2027 ?", "Selon C. Vosloo, le traitement d'un problème non connu est considéré comme un service de conseil facturable."),
 ],
 related=["maintenance-specifique-client-sap-businessobjects", "bi-2025-ou-sortir-de-businessobjects", "diagnostic-sortie-businessobjects", "collectivites-budget-marches-publics-fin-maintenance-businessobjects"],
)
