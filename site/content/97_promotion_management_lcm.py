PAGE = dict(
 slug="promotion-management-lcm-businessobjects-montee-de-version",
 nav="Promotion Management",
 title="Promotion Management et LCM : monter de version",
 desc="Promotion Management et LCMBIAR dans un projet de montée de version BusinessObjects : ce que l'outil fait, ses règles, et comment organiser le transfert.",
 h1="Promotion Management et LCM : déplacer des contenus BusinessObjects pendant une montée de version",
 lead="Quand la maintenance standard de la 4.3 s'arrête le 31 décembre 2026, beaucoup d'équipes préparent une nouvelle plateforme et doivent y transférer leurs contenus. Promotion Management, souvent appelé LCM, est l'outil intégré à la console CMC pour déplacer des objets entre environnements. Ce guide rappelle ce qu'il fait, les règles à connaître, et ce qu'il ne règle pas à lui seul.",
 published="2026-11-17", modified="2026-11-17",
 body="""
<h2>LCM, Promotion Management, LCMBIAR : les termes</h2>
<p>Le sigle LCM désigne la gestion du cycle de vie (Life Cycle Management). SAP Learning la décrit comme l'ensemble du processus de conception, de développement et de maintenance d'une solution applicative. Dans la plateforme BusinessObjects, l'outil qui en porte le nom courant est Promotion Management : une application intégrée à la console CMC qui transporte, ou « promeut », des contenus BI entre deux environnements, avec ou sans fichier LCMBIAR (SAP Learning, TutorialsPoint). Un fichier LCMBIAR est une archive compressée qui contient des objets BI ; elle peut servir de source ou de destination d'un travail de promotion (SAP Learning).</p>

<h2>Ce que fait l'outil</h2>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Fonction</th><th>Ce que décrivent les sources</th></tr></thead>
<tbody>
<tr><td>Travail de promotion</td><td>Un travail est une collection d'objets (utilisateurs, groupes, dossiers, rapports, univers, connexions, droits) que l'on crée, copie, modifie et planifie (SAP Community, SAPinsider, TutorialsPoint)</td></tr>
<tr><td>Dépendances</td><td>La fonction « Manage Dependencies » calcule les objets liés, comme les univers, connexions et images ; sans cette étape, les dépendances ne sont pas promues avec le travail (SAP Community)</td></tr>
<tr><td>Sécurité</td><td>Choix entre ne pas promouvoir la sécurité, la promouvoir, ou y ajouter les droits d'application (SAP Community, SAPinsider)</td></tr>
<tr><td>Test</td><td>« Test Promote » simule le résultat sans modifier la destination (SAP Community, SAPinsider)</td></tr>
<tr><td>Résultat</td><td>Succès, échec ou succès partiel (SAP Community, TutorialsPoint)</td></tr>
<tr><td>Retour arrière</td><td>Annulation partielle ou complète des objets promus sur la destination (SAP Learning, TutorialsPoint)</td></tr>
</tbody></table></div>

<h2>La règle des versions identiques</h2>
<p>SAP Learning, TutorialsPoint et un article de la communauté SAP indiquent que source et destination doivent exécuter la même version de la plateforme. Pour une montée de version, la compatibilité entre versions se vérifie donc avant tout transfert. SAP Learning décrit deux voies pour BI 2025 : la mise à jour sur place, possible depuis une 4.2 ou une 4.3 si le système d'exploitation est encore pris en charge, ou une installation neuve avec migration des contenus à l'aide de l'outil Promotion Management de la version 2025. TutorialsPoint présente par ailleurs l'Upgrade Management Tool, qui importe des objets d'une version précédente vers la plateforme mise à niveau, en direct ou via un fichier BIAR. Choisir entre ces voies relève de votre architecture ; voir notre <a href="/bi-2025-ou-sortir-de-businessobjects/">comparaison BI 2025 ou sortie de BusinessObjects</a>.</p>

<h2>Ce que l'outil ne règle pas</h2>
<ul>
<li><strong>Le tri du contenu.</strong> Promouvoir un parc non nettoyé reporte les problèmes sur la nouvelle plateforme. Le tri décrit dans notre guide sur le <a href="/nettoyer-parc-businessobjects-documents-inutilises/">nettoyage du parc</a> précède le transfert.</li>
<li><strong>Les contenus non repris.</strong> Les univers UNV ne sont pas pris en charge après la 4.3 : leur <a href="/convertir-univers-unv-en-unx/">conversion en UNX</a> fait partie du projet.</li>
<li><strong>Le changement continu.</strong> Pendant le projet, des rapports sont modifiés en production. Wiiisdom, éditeur de la suite 360Suite, écrit dans un livret sur la montée de version que geler les changements ou migrer à la main est peu réaliste, et présente la comparaison d'instantanés comme réponse. C'est le point de vue d'un éditeur d'outils ; l'organisation du gel ou du rattrapage reste une décision de projet.</li>
<li><strong>Les volumes de duplication.</strong> Dans un témoignage publié par Wiiisdom, un prestataire danois indique que Promotion Management ne suffisait pas pour répliquer un environnement maître vers plus de cinquante environnements clients. Ce cas est celui d'un éditeur d'outils décrivant un client à source unique ; il ne se généralise pas à un parc ordinaire.</li>
</ul>

<h2>Organiser le transfert en six étapes</h2>
<ol>
<li>Inventorier les contenus utilisés et décider ce qui est repris, refait ou supprimé.</li>
<li>Vérifier que source et destination sont dans la même version avant tout travail de promotion, sinon passer par la voie de migration retenue.</li>
<li>Promouvoir dans un ordre logique, par exemple les droits et groupes, les connexions, les univers, puis les documents, comme le suggère Wiiisdom dans son livret.</li>
<li>Utiliser « Test Promote » et relire les dépendances avant chaque travail.</li>
<li>Contrôler le statut final, traiter les succès partiels et garder le retour arrière activé tant que la recette n'est pas terminée.</li>
<li>Comparer les rapports migrés à l'original, puis documenter le résultat.</li>
</ol>
<p>Ces étapes s'intègrent à la <a href="/checklist-migration-sap-businessobjects/">checklist de migration</a> et pèsent sur la <a href="/duree-migration-sap-businessobjects-facteurs/">durée du projet</a>. Quelle que soit la cible, que vous restiez chez SAP ou que vous migriez, un transfert ordonné réduit les surprises. AM DATA n'est revendeur ni de SAP ni de Microsoft ; le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> prépare cet inventaire.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://learning.sap.com/courses/administrating-servers-in-sap-businessobjects-bi-platform/describing-the-content-management-process" rel="noopener">Describing the Content Management Process (SAP Learning)</a></li>
<li><a href="https://learning.sap.com/courses/administrating-servers-in-sap-businessobjects-bi-platform/upgrading-paths" rel="noopener">Upgrading Paths (SAP Learning)</a></li>
<li><a href="https://www.tutorialspoint.com/sap_bo_administration/sap_bo_administration_promotion_management.htm" rel="noopener">SAP BO Administration : Promotion Management (TutorialsPoint)</a></li>
<li><a href="https://tutorialspoint.com/sap_bo_administration/sap_bo_administration_upgrade_management_tool.htm" rel="noopener">SAP BO Administration : Upgrade Management Tool (TutorialsPoint)</a></li>
<li><a href="https://blogs.sap.com/2012/10/25/promotion-management-in-bi40" rel="noopener">Promotion Management in BI 4.0 (SAP Community)</a></li>
<li><a href="https://sapinsider.org/a-step-by-step-guide-for-using-promotion-management-in-businessobjects-4-1/" rel="noopener">A step-by-step guide for using Promotion Management in BusinessObjects 4.1 (SAPinsider)</a></li>
<li><a href="https://wiiisdom.com/ebook/en/wiiisdom-ebook-optimize-your-sap-businessobjects-upgrade.pdf" rel="noopener">Optimize your SAP BusinessObjects upgrade (Wiiisdom)</a></li>
<li><a href="https://wiiisdom.com/blog/how-bec-better-serves-its-customers-with-improved-sap-business-objects-promotion-management/" rel="noopener">How BEC better serves its customers with improved Promotion Management (Wiiisdom)</a></li>
</ul>
""",
 faqs=[
  ("Qu'est-ce que Promotion Management dans BusinessObjects ?", "C'est une application de la console CMC qui promeut des contenus BI entre deux environnements, avec ou sans fichier LCMBIAR, selon SAP Learning et TutorialsPoint."),
  ("Peut-on promouvoir de la 4.3 vers une version plus récente avec Promotion Management ?", "Les sources consultées indiquent que source et destination doivent exécuter la même version de la plateforme. Pour une installation neuve, SAP Learning cite l'outil Promotion Management de la version cible, et TutorialsPoint présente l'Upgrade Management Tool pour importer des objets d'une version antérieure."),
  ("Qu'est-ce qu'un fichier LCMBIAR ?", "C'est une archive compressée qui regroupe des objets BI et que l'on peut utiliser comme source ou destination d'un travail de promotion, selon SAP Learning."),
  ("Que fait « Test Promote » ?", "Il montre ce qui se passerait sans appliquer de changement à la destination, d'après la communauté SAP et SAPinsider. Il est présenté comme une bonne pratique avant chaque travail."),
  ("Peut-on annuler une promotion ?", "Oui. SAP Learning et TutorialsPoint décrivent un retour arrière partiel ou complet des objets promus sur la destination. TutorialsPoint précise qu'il est activé par défaut au niveau du système."),
 ],
 related=["checklist-migration-sap-businessobjects", "duree-migration-sap-businessobjects-facteurs", "bi-2025-ou-sortir-de-businessobjects", "nettoyer-parc-businessobjects-documents-inutilises"],
)
