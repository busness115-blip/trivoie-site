# Contenu des pages éditoriales de trivoie.fr. Faits : uniquement ceux déjà sourcés sur la page d'accueil.
# Pas de tiret cadratin. Chaque fait est attribué à une source nommée.

SRC_CSM = '<a href="https://clintvosloo.com/sap-customer-specific-maintenance-bi-43-ds-43-what-it-means" rel="noopener">notes SAP 3486924 et 3763590, résumées par C. Vosloo</a>'
SRC_EOL = '<a href="https://wiiisdom.com/blog/sap-bi-end-of-life-stages/" rel="noopener">dates de fin de maintenance SAP BI (Wiiisdom)</a>'
SRC_2025 = '<a href="https://wiiisdom.com/blog/sap-businessobjects-bi-2025/" rel="noopener">SAP BusinessObjects BI 2025 : composants et univers (Wiiisdom)</a>'
SRC_DEP = '<a href="https://dallasmarks.com/getting-ready-for-sap-businessobjects-4-3-support-pack-4/" rel="noopener">notes SAP 2801797 et 2914654 (Dallas Marks)</a>'
SRC_2027 = '<a href="https://wiiisdom.com/fr/blog/sap-bi-dates-de-fin-de-vie/" rel="noopener">dates de fin de vie SAP BI (Wiiisdom)</a> et <a href="https://dallasmarks.com/toy-story-5-and-bi-2027/" rel="noopener">annonce de BI 2027 (Dallas Marks)</a>'
SRC_PAM = '<a href="https://support.sap.com/en/release-upgrade-maintenance.html" rel="noopener">Product Availability Matrix SAP</a>'

SOURCES_BLOCK = """<section class="sources"><h2>Sources</h2><ul>
<li>%s</li><li>%s</li><li>%s</li><li>%s</li><li>%s</li><li>%s</li></ul>
<p>Les dates et règles de maintenance peuvent évoluer. Vérifiez-les dans le portail SAP (Product Availability Matrix et notes citées) avant toute décision.</p></section>""" % (SRC_CSM, SRC_EOL, SRC_2025, SRC_2027, SRC_DEP, SRC_PAM)

PAGES = [
# ---------------------------------------------------------------------------------------------
dict(
 slug="fin-maintenance-sap-businessobjects-4-3",
 title="Fin de maintenance SAP BusinessObjects 4.3 au 31/12/2026",
 desc="La maintenance standard de SAP BusinessObjects 4.3 s'arrête le 31 décembre 2026. Dates, conséquences probables, options et premières décisions à prendre.",
 h1="Fin de maintenance de SAP BusinessObjects 4.3 : ce qui change le 31 décembre 2026",
 lead="La maintenance standard de SAP BusinessObjects BI 4.3 s'arrête le 31 décembre 2026. Ce guide résume ce qui change en 2027 et en 2028, qui est concerné, quelles options existent et par quoi commencer.",
 body="""
<h2>Les dates à retenir</h2>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Date</th><th>Ce qui change pour SAP BusinessObjects BI 4.3</th></tr></thead>
<tbody>
<tr><td>31 décembre 2026</td><td>Fin de la maintenance standard de la version 4.3.</td></tr>
<tr><td>2027</td><td>Maintenance spécifique client : seuls les correctifs de sécurité jugés graves (score CVSS de 7 ou plus) sont livrés pendant les 12 premiers mois.</td></tr>
<tr><td>2028</td><td>Plus aucun correctif, patch ni support package n'est livré pour la version 4.3.</td></tr>
<tr><td>Premier trimestre 2027</td><td>Sortie prévue de SAP BusinessObjects BI 2027, la version qui suit BI 2025.</td></tr>
<tr><td>Fin 2027</td><td>Fin de la maintenance standard de SAP BusinessObjects BI 2025.</td></tr>
</tbody></table></div>
<p>Sources : """ + SRC_CSM + """ et """ + SRC_EOL + """. Ces dates concordent entre plusieurs analyses indépendantes : Wiiisdom, C. Vosloo, InfoSol et NTT DATA. Les conditions détaillées figurent dans les notes SAP 3486924 et 3763590. Pour BI 2027 : """ + SRC_2027 + """. Selon Wiiisdom, sa maintenance standard irait jusqu'au quatrième trimestre 2029.</p>

<h2>Ce que change la maintenance spécifique client</h2>
<p>Après le 31 décembre 2026, les clients qui restent en 4.3 passent en maintenance spécifique client (Customer-Specific Maintenance). Selon les notes SAP 3486924 et 3763590, analysées par C. Vosloo :</p>
<ul>
<li>en 2027, seuls les correctifs de sécurité dont le score CVSS est de 7 ou plus sont livrés, pendant les 12 premiers mois ;</li>
<li>SAP ne s'engage plus sur un délai de traitement ;</li>
<li>les nouveaux problèmes non documentés deviennent du conseil facturable ;</li>
<li>à partir de 2028, plus aucun correctif n'est livré ;</li>
<li>les frais de maintenance de votre contrat continuent de s'appliquer, sans option de maintenance spécifique à commander.</li>
</ul>
<p>Le prix de la maintenance ne baisse donc pas alors que la couverture se réduit. C'est un sujet pour la direction financière et le responsable de la sécurité des systèmes d'information, pas seulement pour l'équipe BI.</p>

<h2>Qui est concerné</h2>
<p>Toute organisation qui exploite SAP BusinessObjects BI 4.3 en production : rapports Web Intelligence, Crystal Reports, tableaux de bord, univers, planifications et comptes utilisateurs. Les versions 4.1 et 4.2 sont déjà sorties de la maintenance standard. Vérifiez la situation exacte de votre version dans la """ + SRC_PAM + """.</p>

<h2>Les trois options</h2>
<ol>
<li><strong>Rester en 4.3</strong> sous maintenance spécifique client, en acceptant la couverture réduite et en prévoyant des mesures de sécurité complémentaires.</li>
<li><strong>Monter en SAP BusinessObjects BI 2025</strong>, ce qui donne un an de maintenance standard supplémentaire (jusqu'au 31 décembre 2027) et impose de traiter les univers UNV et les contenus obsolètes. SAP prévoit ensuite BI 2027 au premier trimestre 2027 : rester chez SAP revient à monter de version environ tous les deux ans.</li>
<li><strong>Sortir de BusinessObjects</strong> vers une autre plateforme décisionnelle, ce qui demande un inventaire précis de ce qui est réellement utilisé.</li>
</ol>
<p>Le détail des critères de choix est dans <a href="/bi-2025-ou-sortir-de-businessobjects/">BI 2025 ou sortir de BusinessObjects : comment choisir</a>.</p>

<h2>Ce qui peut bloquer une montée de version</h2>
<ul>
<li><strong>Les univers UNV</strong> ne sont plus pris en charge après la 4.3. Ils doivent être convertis en UNX, et les documents qui les utilisent doivent être retestés (""" + SRC_2025 + """).</li>
<li><strong>Les contenus obsolètes</strong> : Xcelsius et Dashboards, Desktop Intelligence, Explorer et les contenus Flash sont concernés par des dépréciations (""" + SRC_DEP + """).</li>
<li><strong>Lumira Designer</strong> reste maintenu mais sans nouvelle fonctionnalité.</li>
</ul>

<h2>Par quoi commencer : l'inventaire</h2>
<p>Avant de choisir une option, il faut des chiffres. Les cinq nombres qui orientent la décision :</p>
<ul>
<li>le nombre de documents par type (Web Intelligence, Crystal Reports, Analysis, tableaux de bord, Lumira) ;</li>
<li>le nombre d'univers, en distinguant UNV et UNX ;</li>
<li>le nombre de contenus obsolètes ;</li>
<li>le nombre de comptes utilisateurs, dont ceux réellement actifs sur les 12 derniers mois ;</li>
<li>le nombre de planifications récurrentes.</li>
</ul>
<p>Vous pouvez obtenir ces chiffres vous-même avec <a href="/compter-documents-sap-businessobjects-query-builder/">les requêtes Query Builder</a>, ou laisser le scan gratuit de Trivoie calculer votre niveau de risque à partir d'eux, directement dans votre navigateur.</p>
""",
 faqs=[
  ("Quand la maintenance de SAP BusinessObjects 4.3 s'arrête-t-elle ?", "La maintenance standard de SAP BusinessObjects BI 4.3 s'arrête le 31 décembre 2026. Ensuite, la maintenance spécifique client ne livre en 2027 que les correctifs de sécurité jugés graves (CVSS 7 ou plus), puis plus aucun correctif à partir de 2028."),
  ("Que se passe-t-il si je reste en 4.3 après 2026 ?", "Votre plateforme continue de fonctionner, mais la couverture se réduit : correctifs de sécurité graves seulement en 2027, sans engagement de délai, nouveaux problèmes facturables, puis plus aucun correctif à partir de 2028. Les frais de maintenance de votre contrat continuent de s'appliquer. Votre contrat et votre interlocuteur SAP précisent les conditions applicables à votre cas."),
  ("Jusqu'à quand SAP BusinessObjects BI 2025 est-il maintenu ?", "La maintenance standard de SAP BusinessObjects BI 2025 va jusqu'au 31 décembre 2027, soit un an de plus que la 4.3. Les correctifs de sécurité de BI 2025 sont ensuite prévus jusqu'au quatrième trimestre 2028 (Wiiisdom). La version suivante, BI 2027, est attendue au premier trimestre 2027."),
  ("Faut-il migrer avant le 31 décembre 2026 ?", "Pas nécessairement. L'urgence est de décider : un diagnostic chiffré prend 10 jours ouvrés et permet de choisir en connaissance de cause plutôt que de subir la maintenance spécifique client."),
 ],
 related=["bi-2025-ou-sortir-de-businessobjects","diagnostic-sortie-businessobjects"],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug="bi-2025-ou-sortir-de-businessobjects",
 title="BI 2025 ou sortir de BusinessObjects : comment choisir",
 desc="Rester en 4.3, monter en SAP BusinessObjects BI 2025 ou migrer vers une autre solution : les critères pour décider, sans parti pris d'éditeur.",
 h1="BI 2025 ou sortir de BusinessObjects : comment choisir",
 lead="Avec la fin de la maintenance standard de la version 4.3 au 31 décembre 2026, trois voies s'ouvrent. Voici les critères qui permettent de choisir, et les chiffres à réunir avant de décider.",
 body="""
<h2>Les trois voies</h2>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 2 (défilement horizontal)"><table>
<thead><tr><th>Voie</th><th>Ce qu'elle apporte</th><th>Ce qu'il faut regarder</th></tr></thead>
<tbody>
<tr><td>Rester en 4.3</td><td>Aucun projet technique immédiat.</td><td>Couverture réduite à partir de 2027 et plus aucun correctif à partir de 2028.</td></tr>
<tr><td>Monter en BI 2025</td><td>Un an de maintenance standard de plus (jusqu'au 31 décembre 2027).</td><td>Conversion des univers UNV en UNX, contenus obsolètes, tests de non-régression, puis une nouvelle montée de version (BI 2027, attendue au premier trimestre 2027) à prévoir pour rester en maintenance standard.</td></tr>
<tr><td>Sortir de BusinessObjects</td><td>Une plateforme décidée pour les années suivantes, un parc nettoyé.</td><td>Inventaire de l'usage réel, refonte des rapports utiles, formation, période de double exploitation.</td></tr>
</tbody></table></div>
<p>Sources : """ + SRC_CSM + """, """ + SRC_2025 + """.</p>

<h2>Les critères qui décident</h2>
<h3>1. L'horizon</h3>
<p>BI 2025 ne repousse l'échéance que d'un an (31 décembre 2027). SAP prévoit ensuite BI 2027 au premier trimestre 2027, dont la maintenance standard irait jusqu'au quatrième trimestre 2029 selon Wiiisdom. Rester chez SAP, c'est donc entrer dans un cycle : une montée de version environ tous les deux ans, chacune avec sa recette. C'est ce coût répété qu'il faut comparer à une migration.</p>
<h3>2. L'état du parc</h3>
<p>Le nombre d'univers UNV, de contenus obsolètes et de documents réellement utilisés change complètement l'effort d'une montée de version comme d'une migration. Un parc dont une grande partie n'est plus ouverte par personne se migre moins cher une fois nettoyé.</p>
<h3>3. L'usage réel</h3>
<p>Quels rapports sont ouverts, par qui, à quelle fréquence ? Les comptes inactifs et les documents jamais ouverts sont les premiers à décommissionner, quelle que soit la voie retenue.</p>
<h3>4. Le risque et la conformité</h3>
<p>Rester sous maintenance spécifique client expose à des failles de gravité moyenne ou faible qui ne sont plus corrigées. C'est une question à poser au responsable de la sécurité et à la direction financière.</p>
<h3>5. Les compétences et les contrats</h3>
<p>Équipe disponible, contrat de maintenance en cours, calendrier budgétaire : ces contraintes pèsent autant que la technique.</p>

<h2>Les chiffres à réunir avant de choisir</h2>
<p>Documents par type, univers UNV et UNX, contenus obsolètes, comptes actifs et inactifs, planifications récurrentes. La page <a href="/compter-documents-sap-businessobjects-query-builder/">Compter ses documents avec Query Builder</a> explique comment les obtenir en quelques minutes.</p>

<h2>Décider avec un diagnostic indépendant</h2>
<p>Le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> compare les trois voies pour votre plateforme : coût, délai, risque et prérequis, en 10 jours ouvrés, à prix fixe. Trivoie est un service d'AM DATA, qui n'est revendeur ni de SAP ni de Microsoft et ne perçoit aucune commission d'éditeur.</p>
""",
 faqs=[
  ("Vaut-il mieux monter en BI 2025 ou migrer vers une autre solution ?", "Cela dépend de l'état du parc, de l'usage réel, de l'horizon souhaité et du budget. BI 2025 ne donne qu'un an de maintenance standard supplémentaire, jusqu'au 31 décembre 2027, et SAP prévoit BI 2027 au premier trimestre 2027 : rester chez SAP implique une montée de version environ tous les deux ans. Un diagnostic chiffré compare les options pour une plateforme précise."),
  ("Que faut-il faire des univers UNV ?", "Les univers UNV ne sont plus pris en charge après la 4.3. Pour monter en BI 2025, ils doivent être convertis en UNX et les documents qui les utilisent doivent être retestés."),
  ("Peut-on réduire le coût d'une migration ?", "Oui, en décommissionnant d'abord ce qui n'est plus utilisé : comptes inactifs, documents jamais ouverts, contenus obsolètes. Un inventaire précis est le préalable."),
 ],
 related=["fin-maintenance-sap-businessobjects-4-3","diagnostic-sortie-businessobjects"],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug="diagnostic-sortie-businessobjects",
 title="Diagnostic Sortie BO : décision chiffrée en 10 jours",
 desc="Diagnostic indépendant de votre plateforme SAP BusinessObjects 4.3, à prix fixe (2 900 à 7 900 € HT), livré en 10 jours ouvrés : inventaire, usage, trois options chiffrées.",
 h1="Diagnostic Sortie BO : une décision chiffrée en 10 jours ouvrés",
 lead="Un diagnostic indépendant de votre plateforme SAP BusinessObjects 4.3, à prix fixe, qui compare les trois voies après la fin de maintenance et vous donne une décision défendable devant votre direction.",
 body="""
<h2>Ce que vous recevez</h2>
<ol>
<li><strong>Inventaire complet</strong> de la plateforme (fichier Excel) : documents, univers, connexions, utilisateurs, planifications, composants.</li>
<li><strong>Analyse de l'usage</strong> : contenu réellement utilisé, contenu à décommissionner.</li>
<li><strong>Matrice de décision</strong> comparant les trois options : coût, délai, risque, prérequis.</li>
<li><strong>Note de risque</strong> d'une page pour la direction financière et le RSSI.</li>
<li><strong>Rapport de diagnostic</strong> (PDF) avec plan d'action recommandé.</li>
<li><strong>Restitution de 60 minutes</strong> devant votre comité.</li>
</ol>
<p>Sans supplément : un modèle de cahier des charges pour la suite du projet, et une session de questions-réponses de 30 minutes dans les 30 jours suivant la restitution.</p>

<h2>Déroulement</h2>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 3 (défilement horizontal)"><table>
<thead><tr><th>Étape</th><th>Délai</th><th>Contenu</th></tr></thead>
<tbody>
<tr><td>Lancement</td><td>J0</td><td>Bon de commande, accord de confidentialité, accord de sous-traitance des données</td></tr>
<tr><td>Collecte</td><td>J1</td><td>Exports de la plateforme ou session de 2 heures avec votre administrateur</td></tr>
<tr><td>Analyse</td><td>J2 à J6</td><td>Inventaire, usage, complexité, dépendances</td></tr>
<tr><td>Chiffrage</td><td>J7 à J8</td><td>Comparaison des trois options</td></tr>
<tr><td>Rédaction</td><td>J9</td><td>Rapport, note de risque, support de restitution</td></tr>
<tr><td>Restitution</td><td>J10</td><td>Présentation au comité</td></tr>
</tbody></table></div>
<p>Les délais courent à partir de la réception complète des données. Aucun accès permanent à vos serveurs n'est nécessaire, et les identifiants des utilisateurs peuvent être pseudonymisés avant transmission.</p>

<h2>Prix fermes et forfaitaires</h2>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 4 (défilement horizontal)"><table>
<thead><tr><th>Taille de plateforme</th><th>Critères</th><th>Prix HT</th></tr></thead>
<tbody>
<tr><td>S</td><td>Jusqu'à 200 utilisateurs et 2 000 documents</td><td>2 900 €</td></tr>
<tr><td>M</td><td>Jusqu'à 1 000 utilisateurs et 10 000 documents</td><td>4 900 €</td></tr>
<tr><td>L</td><td>Au-delà</td><td>7 900 €</td></tr>
</tbody></table></div>
<p>Le <a href="/#scan">scan gratuit</a> indique la taille de votre plateforme.</p>

<h2>Nos engagements</h2>
<ul>
<li><strong>Délai</strong> : si le diagnostic n'est pas livré dans les 10 jours ouvrés suivant la réception complète des données, 20 % du prix sont remboursés. Le délai est suspendu pendant les retards de transmission ou de disponibilité de votre côté.</li>
<li><strong>Neutralité</strong> : aucune commission, rétrocession ou avantage d'un éditeur ou d'un revendeur.</li>
<li><strong>Confidentialité</strong> : vos données ne servent qu'à ce diagnostic, puis sont supprimées ou restituées.</li>
</ul>

<h2>Conditions</h2>
<p>Paiement : 50 % à la commande, 50 % à la restitution. Pour les acheteurs publics : paiement à la restitution, dans le délai légal applicable. Les conditions générales de vente d'AM DATA s'appliquent. Tarif de lancement valable pour toute commande signée avant le 31 janvier 2027.</p>

<h2>Qui réalise le diagnostic</h2>
<p>Un expert SAP BusinessObjects de plus de 10 ans d'expérience, avec sa méthode d'audit BI Pulse. Trivoie est un service d'AM DATA.</p>
""",
 faqs=[
  ("Combien coûte le Diagnostic Sortie BO ?", "Le prix est forfaitaire et dépend de la taille de la plateforme : 2 900 € HT jusqu'à 200 utilisateurs et 2 000 documents, 4 900 € HT jusqu'à 1 000 utilisateurs et 10 000 documents, 7 900 € HT au-delà."),
  ("En combien de temps le diagnostic est-il livré ?", "En 10 jours ouvrés à partir de la réception complète des données. Si le délai n'est pas tenu, 20 % du prix sont remboursés."),
  ("Faut-il donner un accès à nos serveurs ?", "Non. Il faut des exports de la plateforme ou une session de 2 heures avec votre administrateur. Aucun accès permanent n'est nécessaire."),
  ("Le diagnostic est-il indépendant des éditeurs ?", "Oui. AM DATA n'est revendeur ni de SAP ni de Microsoft et ne perçoit aucune commission d'éditeur."),
 ],
 related=["fin-maintenance-sap-businessobjects-4-3","bi-2025-ou-sortir-de-businessobjects"],
 service=True,
),
# ---------------------------------------------------------------------------------------------
dict(
 slug="compter-documents-sap-businessobjects-query-builder",
 title="Compter ses documents BusinessObjects avec Query Builder",
 desc="Les requêtes Query Builder pour compter documents, univers UNV et UNX, utilisateurs actifs d'une plateforme SAP BusinessObjects 4.3, sans la limite de 1 000 lignes.",
 h1="Compter ses documents, univers et utilisateurs SAP BusinessObjects avec Query Builder",
 lead="Avant de décider quoi faire de la plateforme, il faut des chiffres fiables. Query Builder, l'outil d'administration de SAP BusinessObjects, permet de les obtenir en quelques requêtes en lecture seule.",
 body="""
<h2>Ouvrir Query Builder</h2>
<p>Query Builder se trouve en général à l'adresse <code>http://votre-serveur:8080/AdminTools</code>. Connectez-vous avec un compte qui voit tout le référentiel, en pratique un administrateur. Avec un compte limité, les chiffres sont plus bas que la réalité.</p>

<h2>Pourquoi utiliser COUNT</h2>
<p>Sans clause <code>TOP</code>, une requête renvoie au plus 1 000 lignes par défaut. Si votre plateforme compte plus de 1 000 documents, une simple liste donne donc un faux total. La fonction <code>COUNT(SI_ID)</code> renvoie le nombre exact, dans un seul objet, sous l'attribut <code>SI_AGGREGATE_COUNT</code>.</p>

<h2>Les requêtes</h2>
<p>Chaque requête renvoie un nombre à noter. Le filtre <code>SI_INSTANCE = 0</code> exclut les instances de documents pour ne compter que les documents eux-mêmes.</p>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 5 (défilement horizontal)"><table>
<thead><tr><th>À compter</th><th>Requête</th></tr></thead>
<tbody>
<tr><td>Documents Web Intelligence</td><td><code>SELECT COUNT(SI_ID) FROM CI_INFOOBJECTS WHERE SI_INSTANCE = 0 AND SI_KIND = 'Webi'</code></td></tr>
<tr><td>Documents Crystal Reports</td><td><code>SELECT COUNT(SI_ID) FROM CI_INFOOBJECTS WHERE SI_INSTANCE = 0 AND SI_KIND = 'CrystalReport'</code></td></tr>
<tr><td>Documents Analysis (OLAP)</td><td><code>SELECT COUNT(SI_ID) FROM CI_INFOOBJECTS WHERE SI_INSTANCE = 0 AND SI_KIND IN ('MDAnalysis', 'Analysis', 'AAD.AnalysisWorkspace')</code></td></tr>
<tr><td>Applications Lumira et Design Studio</td><td><code>SELECT COUNT(SI_ID) FROM CI_INFOOBJECTS WHERE SI_INSTANCE = 0 AND SI_KIND IN ('AAD.AnalysisApplication', 'VISILums')</code></td></tr>
<tr><td>Tableaux de bord Xcelsius</td><td><code>SELECT COUNT(SI_ID) FROM CI_INFOOBJECTS WHERE SI_INSTANCE = 0 AND SI_KIND IN ('XL.XcelsiusEnterprise', 'Xcelsius', 'XL.XcelsiusApplication')</code></td></tr>
<tr><td>Contenus obsolètes (Desktop Intelligence, Explorer, Flash)</td><td><code>SELECT COUNT(SI_ID) FROM CI_INFOOBJECTS WHERE SI_INSTANCE = 0 AND SI_KIND IN ('FullClient', 'DataDiscovery', 'DataDiscoveryAlbum', 'Flash')</code></td></tr>
<tr><td>Univers UNV</td><td><code>SELECT COUNT(SI_ID) FROM CI_APPOBJECTS WHERE SI_KIND = 'Universe'</code></td></tr>
<tr><td>Univers UNX</td><td><code>SELECT COUNT(SI_ID) FROM CI_APPOBJECTS WHERE SI_KIND = 'DSL.MetaDataFile'</code></td></tr>
<tr><td>Comptes utilisateurs</td><td><code>SELECT COUNT(SI_ID) FROM CI_SYSTEMOBJECTS WHERE SI_KIND = 'User'</code></td></tr>
</tbody></table></div>
<p>Pour les comptes actifs sur 12 mois, ajoutez à la requête des comptes une condition sur <code>SI_LASTLOGONTIME</code>, au format <code>AAAA.MM.JJ.00.00.00</code>, avec la date d'il y a un an.</p>

<h2>Ce qu'il faut noter</h2>
<p>Reportez chaque nombre dans un tableau : c'est l'inventaire de départ du choix entre rester en 4.3, monter en BI 2025 ou sortir de BusinessObjects. Le détail de la décision est dans <a href="/fin-maintenance-sap-businessobjects-4-3/">le guide sur la fin de maintenance</a>.</p>

<h2>Calculer son niveau de risque</h2>
<p>Le <a href="/#scan">scan gratuit de Trivoie</a> reprend ces chiffres et calcule un niveau de risque et la taille de votre plateforme, dans votre navigateur, sans rien envoyer. Il propose aussi un script de collecte automatique en lecture seule.</p>
<p>Source : les limites de Query Builder sont documentées par la communauté SAP (note SAP KBA 1693396).</p>
""",
 faqs=[
  ("Pourquoi Query Builder ne renvoie-t-il que 1 000 lignes ?", "Sans clause TOP, une requête est limitée à 1 000 lignes par défaut. Pour obtenir un total exact, utilisez COUNT(SI_ID), qui renvoie le nombre dans l'attribut SI_AGGREGATE_COUNT."),
  ("Ces requêtes modifient-elles la plateforme ?", "Non. Ce sont des requêtes SELECT en lecture seule sur le référentiel du CMS."),
  ("Quels droits faut-il pour lancer ces requêtes ?", "Un compte qui voit tout le référentiel, en pratique un administrateur. Avec un compte limité, les chiffres sont plus bas que la réalité."),
 ],
 related=["fin-maintenance-sap-businessobjects-4-3","bi-2025-ou-sortir-de-businessobjects"],
 sources=False,
),
]
