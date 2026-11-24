PAGE = dict(
 slug="lire-niveau-risque-scan-sap-businessobjects",
 nav="Lire son niveau de risque",
 title="Scan BusinessObjects : comment lire son niveau de risque",
 desc="Comment lire le résultat du scan gratuit Trivoie sur SAP BusinessObjects : niveau de risque, points retirés, exemple chiffré et suites possibles.",
 h1="Comment lire le niveau de risque du scan SAP BusinessObjects",
 lead="Le scan gratuit de la page d'accueil donne un niveau de risque de 0 à 100 et une liste de constats. Cette page explique ce que ces chiffres représentent, comment ils sont calculés et ce qu'il est raisonnable d'en faire. Le scan est une aide à la décision calculée sur vos chiffres, pas un audit : il ne remplace pas l'inventaire détaillé d'un <a href=\"/diagnostic-sortie-businessobjects/\">diagnostic</a>.",
 published="2026-11-24", modified="2026-11-24",
 body="""
<h2>Ce que mesure le niveau de risque</h2>
<p>Le scan part d'un indice de 100 et retire des points pour chaque constat. Le niveau de risque affiché est 100 moins cet indice. Plus il est élevé, plus la plateforme demande de travail ou d'attention avant et après l'échéance de la version 4.3. Quatre niveaux sont utilisés :</p>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Risque (0 à 100)</th><th>Niveau affiché</th></tr></thead>
<tbody>
<tr><td>Moins de 25</td><td>Faible</td></tr>
<tr><td>25 à 44</td><td>Modéré</td></tr>
<tr><td>45 à 69</td><td>Élevé</td></tr>
<tr><td>70 et plus</td><td>Critique</td></tr>
</tbody></table></div>
<p>Pour une plateforme en version 4.1, 4.2 ou 4.3, le niveau n'est jamais présenté en dessous de « élevé », car l'échéance de la version est la même quel que soit l'état du parc.</p>

<h2>D'où viennent les points retirés</h2>
<p>Chaque constat a un identifiant et une pénalité, calculée sur les chiffres saisis ou importés depuis le fichier du script de collecte.</p>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 2 (défilement horizontal)"><table>
<thead><tr><th>Constat</th><th>Points retirés</th></tr></thead>
<tbody>
<tr><td>Version 4.3 (maintenance spécifique client dès le 1er janvier 2027)</td><td>25</td></tr>
<tr><td>Version 4.1 ou 4.2</td><td>35</td></tr>
<tr><td>Version BI 2025</td><td>10</td></tr>
<tr><td>Univers UNV à convertir</td><td>4 pour un univers, plus 0,3 par univers supplémentaire, plafonné à 20, réduit jusqu'à 3 points si des UNX existent déjà</td></tr>
<tr><td>Contenus obsolètes (Dashboards, Desktop Intelligence, Explorer, Flash)</td><td>2 pour un contenu, plus 0,06 par contenu supplémentaire, plafonné à 8</td></tr>
<tr><td>Applications ou documents Lumira</td><td>2 pour un, plus 0,3 par supplémentaire, plafonné à 5</td></tr>
<tr><td>Base d'audit inactive (usage non mesurable)</td><td>10</td></tr>
<tr><td>Comptes sans connexion depuis 12 mois (à partir de 20 % des comptes, versions 4.x)</td><td>de 2 à 5</td></tr>
<tr><td>Volume de documents à traiter</td><td>1 point par tranche de 500 documents, plafonné à 20</td></tr>
</tbody></table></div>
<p>Les documents non ouverts depuis 12 mois, lus dans la base d'audit, sont retirés du volume à traiter : ils ne coûtent aucun point et apparaissent comme une opportunité de décommissionnement.</p>

<h2>Un exemple chiffré</h2>
<p>Prenons une plateforme 4.3 de 500 utilisateurs, dont 350 actifs, avec 1 523 documents, 40 univers UNV dont 10 déjà convertis en UNX, 20 contenus obsolètes, 3 contenus Lumira et aucune base d'audit active. Les pénalités sont : 25 (version), 14,9 (univers), 10 (audit), 3,1 (contenus obsolètes), 3 (comptes inactifs), 3 (volume) et 2,6 (Lumira). L'indice est de 38 et le niveau de risque de 62 : « élevé ».</p>
<p>Si la même plateforme active l'audit et y relève 500 documents non ouverts depuis 12 mois, la pénalité d'audit disparaît et le volume tombe à 1 023 documents. Le niveau de risque passe à 51, toujours « élevé » parce que la version 4.3 impose ce plancher. Ce qui change, c'est le travail réel : moins de documents à migrer, et un usage enfin mesuré.</p>

<h2>Les faits d'échéance derrière les constats</h2>
<p>Les constats de version reposent sur des faits publiés par plusieurs sources. La fin de la maintenance standard de BI 4.3 au 31 décembre 2026 est donnée par <a href="https://nttdata-solutions.com/uk/blog/preparing-for-the-end-of-life-of-sap-businessobjects-4-3-what-should-your-business-do/" rel="noopener">NTT DATA</a>, <a href="https://www.riministreet.com/blog/sap-end-of-mainstream-maintenance-deadlines-are-looming-for-gts-bobj-bpc-bw-hybris/" rel="noopener">Rimini Street</a> et <a href="https://wiiisdom.com/blog/sap-bi-end-of-life-stages/" rel="noopener">Wiiisdom</a>. NTT DATA indique que des correctifs de sécurité restent fournis une année supplémentaire, puis que le support passe par la maintenance spécifique client ; Rimini Street précise que ces correctifs concernent les failles notées CVSS 7.0 ou plus. Wiiisdom écrit que SAP ne livre ni mises à jour ni correctifs au-delà de cette première année de correctifs de sécurité.</p>
<p>Pour la version suivante, Rimini Street et Wiiisdom situent la fin de la maintenance standard de BI 2025 fin 2027. Wiiisdom et NTT DATA indiquent que les univers UNV ne sont plus pris en charge après BI 4.3 : les univers doivent être convertis en UNX pour passer en BI 2025. Pour Lumira, NTT DATA écrit que Lumira Discovery est retiré de BI 2025 et que Lumira Designer reste pris en charge. Voir aussi la <a href="/fin-maintenance-sap-businessobjects-4-3/">page sur la fin de maintenance de la 4.3</a>.</p>

<h2>Que faire de son résultat</h2>
<ol>
<li>Lire d'abord les trois constats qui retirent le plus de points : ce sont les chantiers qui pèseront le plus sur le budget.</li>
<li>Activer ou exploiter la base d'audit si elle ne l'est pas : c'est le seul constat qui se corrige en quelques jours et qui améliore tous les autres chiffres.</li>
<li>Trier le contenu avant toute décision, avec la page <a href="/trier-rapports-web-intelligence-migrer-refaire-supprimer/">trier les rapports</a> et celle sur le <a href="/nettoyer-parc-businessobjects-documents-inutilises/">nettoyage du parc</a>.</li>
<li>Choisir ensuite un chemin : rester chez SAP en montant en BI 2025, ou migrer. Les deux sont légitimes et se chiffrent avec les mêmes données.</li>
</ol>
<p>La taille de plateforme affichée (S, M ou L) sert uniquement à orienter vers la formule du Diagnostic Sortie BO : 2 900, 4 900 ou 7 900 € HT, en 10 jours ouvrés. AM DATA n'est revendeur ni de SAP ni de Microsoft.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://nttdata-solutions.com/uk/blog/preparing-for-the-end-of-life-of-sap-businessobjects-4-3-what-should-your-business-do/" rel="noopener">NTT DATA : Preparing for the end of life of SAP BusinessObjects 4.3</a></li>
<li><a href="https://www.riministreet.com/blog/sap-end-of-mainstream-maintenance-deadlines-are-looming-for-gts-bobj-bpc-bw-hybris/" rel="noopener">Rimini Street : SAP end of mainstream maintenance deadlines</a></li>
<li><a href="https://wiiisdom.com/blog/sap-bi-end-of-life-stages/" rel="noopener">Wiiisdom : SAP BI end of life stages</a></li>
<li><a href="https://wiiisdom.com/blog/sap-businessobjects-bi-2025/" rel="noopener">Wiiisdom : SAP BusinessObjects BI 2025</a></li>
</ul>
""",
 faqs=[
  ("Le niveau de risque du scan est-il un audit ?", "Non. Il est calculé par une règle publique sur les chiffres que vous saisissez ou importez. Il oriente les priorités ; l'inventaire détaillé relève d'un diagnostic."),
  ("Pourquoi mon niveau reste-t-il élevé alors que mon parc est propre ?", "Parce qu'une plateforme en version 4.x a une échéance de maintenance fixe : le scan ne l'affiche jamais en dessous de « élevé ». Un parc propre réduit le travail, pas l'échéance."),
  ("Comment faire baisser rapidement mon niveau de risque ?", "En activant la base d'audit et en identifiant les documents non ouverts depuis 12 mois, en désactivant les comptes inutilisés et en commençant la conversion des univers UNV."),
  ("Mes données sont-elles envoyées quelque part pendant le scan ?", "Non. Le calcul se fait dans votre navigateur et rien n'est transmis. Vous ne nous envoyez le résumé que si vous le décidez, et il ne contient que des nombres."),
 ],
 related=["diagnostic-sortie-businessobjects", "fin-maintenance-sap-businessobjects-4-3", "nettoyer-parc-businessobjects-documents-inutilises"],
)
