PAGE = dict(
 slug="duree-migration-sap-businessobjects-facteurs",
 nav="Durée de migration",
 title="Durée d'une migration BusinessObjects : les facteurs",
 desc="Combien de temps dure une migration SAP BusinessObjects ? Les facteurs qui font varier la durée, avec les sources, sans chiffre moyen inventé.",
 h1="Combien de temps prend une migration SAP BusinessObjects : les facteurs qui font varier la durée",
 lead="La maintenance standard de SAP BusinessObjects 4.3 s'arrête le 31 décembre 2026 et la question revient à chaque comité de pilotage : combien de temps faut-il ? Il n'existe pas de durée moyenne fiable. Ce guide présente les facteurs qui font varier la durée, appuyés sur des publications d'intégrateurs, d'éditeurs et de la presse spécialisée.",
 published="2026-11-14", modified="2026-11-14",
 body="""
<h2>Pourquoi aucune durée moyenne ne tient</h2>
<p>Decivision, société de conseil en données, écrit qu'il n'existe pas de durée moyenne fiable pour une migration de ce type, et que le calendrier dépend de la taille du patrimoine à migrer, des composants dont l'organisation dépend et de sa capacité à mener le projet en parallèle de l'exploitation courante. Le rythme du projet est donc fixé par votre parc, pas par la date de fin de maintenance.</p>
<p>Les ordres de grandeur publiés existent, mais ils décrivent des cas particuliers et viennent d'acteurs qui ont une offre à vendre :</p>
<ul>
<li>Decivision décrit un projet public avec un horizon cible d'environ 18 mois, mené par itérations d'une à deux semaines. Il le présente comme un cas, pas comme une référence.</li>
<li>NEED4VIZ, qui commercialise une alternative à la migration, indique qu'une migration BI complète représente généralement un projet de deux à trois ans, avec une exploitation en parallèle des deux plateformes pendant un à trois mois.</li>
</ul>
<p>Les deux ordres de grandeur diffèrent nettement : c'est précisément ce qu'il faut retenir. Ils ne se transposent pas à votre parc.</p>

<h2>Les facteurs qui allongent ou raccourcissent le projet</h2>
<h3>Le volume réel de contenus</h3>
<p>Le nombre de documents recensés n'est pas le nombre de documents à migrer. Wiiisdom recommande un audit qui repère les contenus non utilisés depuis longtemps, pour réduire la charge avant de commencer. LeMagIT rapporte, dans le cas d'un grand distributeur, qu'environ 40 % des rapports recensés étaient inutilisés et destinés à l'archivage. Trier d'abord est le levier de durée le plus direct : voir <a href="/nettoyer-parc-businessobjects-documents-inutilises/">nettoyer son parc de documents inutilisés</a>.</p>

<h3>La couche sémantique : les univers</h3>
<p>Wiiisdom rappelle que BI 2025 ne prend pas en charge les univers UNV, qui doivent être convertis en UNX. Pour une cible hors SAP, NEED4VIZ indique que les univers doivent être reconstruits. Dans les deux cas, plus les univers sont nombreux et complexes, plus le projet est long. Voir <a href="/convertir-univers-unv-en-unx/">convertir ses univers UNV en UNX</a>.</p>

<h3>Les règles de gestion non documentées</h3>
<p>Decivision observe que des rapports d'apparence identique peuvent reposer sur des sources, des univers, des variables et des flux ETL différents, et que les règles de gestion implicites dans les univers n'ont pas toujours été documentées. NEED4VIZ ajoute que certaines connaissances ne reposent que sur une seule personne. Documenter l'existant fait partie du projet, pas du préalable gratuit.</p>

<h3>Le choix de la cible</h3>
<p>Monter de version vers BI 2025, passer à un autre outil ou combiner les deux ne demande pas le même travail. Wiiisdom note que le repointage manuel des documents est très long et que l'automatisation et les tests de non-régression changent l'ordre de grandeur sur un projet de montée de version, d'après un cas client qu'il rapporte. Pour un changement d'outil, voir <a href="/migration-businessobjects-power-bi/">la migration vers Power BI</a>.</p>

<h3>L'automatisation, avec prudence</h3>
<p>Dans le cas rapporté par LeMagIT, un responsable du projet indique que l'automatisation a ramené le portage et les tests d'un rapport de 6 jours estimés en manuel à 2 jours. C'est une déclaration d'un projet précis, qui a aussi dû revoir sa modélisation après une première approche qui avait causé des latences et des écarts de résultats.</p>

<h3>La validation métier et la conduite du changement</h3>
<p>Decivision cite la capacité à mobiliser les équipes métier pour valider les livrables parmi les déterminants de la durée. LeMagIT rapporte que, pour le même projet, la phase la plus complexe reste la conduite du changement auprès des unités métier pour décommissionner leurs rapports.</p>

<h3>La période de double exploitation</h3>
<p>Decivision indique que les deux plateformes coexistent pendant toute la durée de la transition et recommande une maintenance applicative active sur l'environnement existant. Cette coexistence a un coût en licences et en infrastructure, que NEED4VIZ cite comme un poste du projet. Elle doit figurer dans le calendrier. Pour la sécurité de la plateforme pendant cette période, voir le <a href="/risque-securite-sap-businessobjects-4-3/">risque de sécurité de la 4.3</a>.</p>

<h2>Dates à garder en tête</h2>
<p>La maintenance standard de BI 4.3 se termine le 31 décembre 2026. En 2027, la maintenance spécifique client ne couvre que les correctifs de sécurité CVSS 7 ou plus ; à partir de 2028, plus aucun correctif n'est livré. BI 2025 reste en maintenance standard jusqu'au 31 décembre 2027. Détail : <a href="/maintenance-specifique-client-sap-businessobjects/">maintenance spécifique client</a>.</p>

<h2>Comment cadrer une durée pour votre parc</h2>
<ol>
<li>Compter ce qui est réellement utilisé, à partir des données de la plateforme (<a href="/compter-documents-sap-businessobjects-query-builder/">requêtes Query Builder</a>).</li>
<li>Classer les contenus : à migrer, à refaire, à supprimer.</li>
<li>Recenser les univers et les sources de données dont ils dépendent.</li>
<li>Identifier les validateurs métier et leur disponibilité.</li>
<li>Choisir la cible, puis seulement chiffrer la durée.</li>
</ol>
<p>AM DATA n'est revendeur ni de SAP ni de Microsoft : le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> produit ce cadrage sur votre parc, que vous restiez chez SAP ou que vous migriez. Le plan détaillé est dans la <a href="/checklist-migration-sap-businessobjects/">checklist de migration</a>.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://www.decivision.com/insights/migration-modernisation/migration-businessobjects-fin-support" rel="noopener">Migration BusinessObjects fin support : migrer ou attendre ? (Decivision)</a></li>
<li><a href="https://www.need4viz.com/fr/ia/quitter-sap-businessobjects-pour-power-bi-ou-tableau-lurgence-est-de-ne-pas-se-precipiter/" rel="noopener">Quitter SAP BusinessObjects pour Power BI ou Tableau ? (NEED4VIZ)</a></li>
<li><a href="https://www.lemagit.fr/etude/Adeo-migre-ses-rapports-BI-par-milliers" rel="noopener">Migration de rapports BI par milliers (LeMagIT)</a></li>
<li><a href="https://wiiisdom.com/blog/how-to-prepare-for-sap-businessobjects-bi-2025/" rel="noopener">How to prepare for SAP BusinessObjects BI 2025 (Wiiisdom)</a></li>
</ul>
""",
 faqs=[
  ("Combien de temps dure une migration SAP BusinessObjects ?", "Il n'existe pas de durée moyenne fiable, selon Decivision. La durée dépend du volume réel de contenus, des univers, de la documentation existante, de la cible et de la disponibilité des équipes métier."),
  ("Faut-il avoir terminé avant le 31 décembre 2026 ?", "Pas nécessairement. La fin de maintenance standard n'arrête pas la plateforme. En 2027, seuls les correctifs de sécurité CVSS 7 ou plus sont livrés dans le cadre de la maintenance spécifique client, puis plus aucun correctif à partir de 2028."),
  ("Qu'est-ce qui réduit le plus la durée d'un projet ?", "Trier avant de migrer. Wiiisdom recommande d'identifier les contenus inutilisés, et LeMagIT rapporte qu'environ 40 % des rapports d'un parc recensé étaient inutilisés dans un cas précis."),
  ("La double exploitation est-elle obligatoire ?", "Decivision indique que les deux plateformes coexistent pendant la transition. Sa durée varie selon le projet : elle est à prévoir dans le calendrier et le budget."),
 ],
 related=["checklist-migration-sap-businessobjects", "nettoyer-parc-businessobjects-documents-inutilises", "convertir-univers-unv-en-unx", "diagnostic-sortie-businessobjects"],
)
