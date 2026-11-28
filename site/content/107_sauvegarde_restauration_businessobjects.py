PAGE = dict(
 slug="sauvegarde-restauration-businessobjects-avant-montee-de-version",
 nav="Sauvegarde avant montée de version",
 title="Sauvegarde BusinessObjects avant montée de version",
 desc="CMS, FileStore, base d'audit, clé de cluster, test de restauration : ce que recommandent les sources avant de monter de version une plateforme BusinessObjects.",
 h1="Sauvegarde et restauration d'une plateforme BusinessObjects avant une montée de version",
 lead="Avant de passer de la 4.3 à BI 2025 ou de lancer une migration, une sauvegarde qui n'a jamais été restaurée reste une hypothèse. Cette page rassemble les points sur lesquels plusieurs sources indépendantes se rejoignent : ce qu'il faut sauvegarder, comment garder les sauvegardes cohérentes entre elles, quelles informations conserver pour restaurer, et pourquoi tester la restauration.",
 published="2026-11-28", modified="2026-11-28",
 body="""
<h2>D'où viennent ces informations</h2>
<p>Nous avons recoupé quatre sources publiques : un article de Wiiisdom sur la sauvegarde des contenus BusinessObjects (publié en 2016, modifié en avril 2024) et sa liste de contrôle de montée de version (modifiée en novembre 2025), un article du blog Umang SAP BOBI Consultant (juin 2013), un billet du blog SAP BI 4.x Knowledge Toolkit sur la copie de système (janvier 2015) et un message publié sur SAP Community à propos d'une migration de la 4.3 vers BI 2025. Plusieurs de ces textes visent des versions plus anciennes que la 4.3 : les principes se retrouvent d'une version à l'autre, mais les détails d'exécution doivent être vérifiés dans la documentation d'administration de votre version, que nous n'avons pas pu consulter automatiquement.</p>

<h2>Ce qu'il faut sauvegarder</h2>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Élément</th><th>Ce que disent les sources</th></tr></thead>
<tbody>
<tr><td>Base du CMS</td><td>Wiiisdom, Umang et le blog SAP BI 4.x la placent au premier rang. Umang écrit que l'environnement ne peut pas être restauré sans une base CMS correctement sauvegardée.</td></tr>
<tr><td>FileStore (FRS), dossiers Input et Output</td><td>Wiiisdom et le blog SAP BI 4.x citent les deux dossiers. Umang précise que le dossier Temp peut être ignoré. Wiiisdom rapporte un cas où seul Output était sauvegardé : les deux sont nécessaires.</td></tr>
<tr><td>Base d'audit</td><td>Citée par la liste de contrôle de Wiiisdom et par le message de SAP Community. Umang la recommande vivement, car une restauration du CMS sans les tables d'audit de la même sauvegarde peut produire une base d'audit corrompue, à cause d'identifiants d'événements en double.</td></tr>
<tr><td>Personnalisations de serveur</td><td>La liste de contrôle de Wiiisdom mentionne les fichiers de paramétrage modifiés (par exemple les fichiers .PRM et .SBO). Source unique pour ce point : attribuée à Wiiisdom.</td></tr>
<tr><td>Planifications et définitions de publications</td><td>Citées dans le message de SAP Community.</td></tr>
</tbody></table></div>

<h2>Garder les sauvegardes cohérentes entre elles</h2>
<p>Wiiisdom écrit que la base du CMS et le FileStore doivent être sauvegardés en même temps pour rester synchronisés. Umang va dans le même sens : sauvegarder le dépôt de fichiers et les tables du CMS à des moments différents expose à des objets orphelins. Pour une sauvegarde à froid, Umang indique d'arrêter le CMS, ce qui interdit l'accès aux utilisateurs, et prévient qu'en sauvegarde à chaud les trois éléments peuvent être capturés dans un état désynchronisé. Le blog SAP BI 4.x décrit de son côté, pour une copie de système, l'arrêt du SIA depuis le CCM, la sauvegarde de la base CMS, la copie des dossiers Input et Output, puis le redémarrage du SIA.</p>
<p>En pratique, la fenêtre de sauvegarde se cale sur un gel des modifications, comme le recommande aussi le message de SAP Community pour la bascule d'un projet vers BI 2025.</p>

<h2>Conserver ce qui permet de restaurer</h2>
<ul>
<li><strong>Les mots de passe.</strong> Wiiisdom écrit qu'il faut connaître le mot de passe de l'administrateur et celui de la clé de cluster du serveur où la sauvegarde a été prise. Le blog SAP BI 4.x dit de même qu'il faut connaître la clé de cluster en vigueur au moment de la sauvegarde pour se connecter à la base restaurée. Notez-les dans le coffre de mots de passe de l'équipe, pas dans un fichier à côté de la sauvegarde.</li>
<li><strong>Le nom du cluster.</strong> Le blog SAP BI 4.x indique de choisir, sur la machine de restauration, un nom de cluster différent de celui de la production avant de démarrer le SIA.</li>
<li><strong>La version.</strong> Wiiisdom décrit la restauration sur un serveur de même version, la montée de version venant ensuite.</li>
</ul>

<h2>Tester la restauration</h2>
<p>Wiiisdom constate que beaucoup d'équipes n'ont jamais testé une restauration complète des sauvegardes qu'elles réalisent chaque jour ou chaque semaine, et indique qu'une restauration complète peut prendre un à deux jours. Sa liste de contrôle de 2025 demande un plan de test de sauvegarde documenté et des tests réguliers. Le message de SAP Community conseille de documenter et de tester la restauration et de prévoir un plan de retour arrière.</p>
<p>Une restauration d'essai sur une machine séparée sert deux objectifs : vérifier que les sauvegardes sont exploitables et mesurer la durée réelle, donnée utile pour dimensionner la fenêtre de bascule. Pour ne jamais risquer la production, utilisez un nom de cluster distinct et un réseau isolé des utilisateurs.</p>

<h2>Liste de contrôle avant la montée de version</h2>
<ol>
<li>Lister les éléments à sauvegarder : base du CMS, base d'audit, FileStore Input et Output, fichiers de paramétrage modifiés.</li>
<li>Fixer une fenêtre de sauvegarde synchronisée, avec gel des modifications.</li>
<li>Consigner la clé de cluster, le compte administrateur et la version exacte de la plateforme.</li>
<li>Restaurer sur une machine de test et mesurer la durée.</li>
<li>Prévoir le retour arrière si la montée de version échoue.</li>
</ol>
<p>Ces étapes s'intègrent à la <a href="/checklist-migration-sap-businessobjects/">checklist de migration</a>. Si vous construisez une plateforme cible à côté de l'existante, voir aussi la <a href="/double-exploitation-businessobjects-periode-transition/">double exploitation</a> et la <a href="/promotion-management-lcm-businessobjects-montee-de-version/">promotion de contenus avec le LCM</a>. Pour les échéances, le <a href="/calendrier-fin-maintenance-sap-businessobjects-versions/">calendrier des versions</a> rappelle que la maintenance standard de la 4.3 se termine le 31 décembre 2026.</p>

<h2>Quelle suite donner</h2>
<p>Que vous montiez vers BI 2025 ou que vous étudiiez une autre plateforme, une sauvegarde restaurée avec succès est le point de départ commun. AM DATA n'est revendeur ni de SAP ni de Microsoft. Le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> peut inclure ce relevé d'infrastructure.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://wiiisdom.com/blog/business-objects-content-backup/" rel="noopener">Don't learn the hard way with SAP BusinessObjects backups (Wiiisdom)</a></li>
<li><a href="https://wiiisdom.com/ebook/the-ultimate-sap-businessobjects-upgrade-checklist/" rel="noopener">The Ultimate SAP BusinessObjects Upgrade Checklist (Wiiisdom)</a></li>
<li><a href="https://umangsapbobiconsultant.wordpress.com/2013/06/16/sap-businessobjects-enterprise-backup-and-recovery-best-practices/" rel="noopener">SAP BusinessObjects Enterprise Backup and Recovery Best Practices (Umang SAP BOBI Consultant)</a></li>
<li><a href="https://sapbi4.wordpress.com/" rel="noopener">SAP BusinessObjects BI 4.x Knowledge Toolkit, billet « SAP BI 4.x System Copy »</a></li>
<li><a href="https://community.sap.com/t5/technology-q-a/bi-4-3-to-sap-business-objects-bi-2025-migration/qaq-p/14263280" rel="noopener">BI 4.3 to SAP Business Objects BI 2025 migration (SAP Community)</a></li>
</ul>
""",
 faqs=[
  ("Que faut-il sauvegarder avant de monter de version BusinessObjects ?", "Les sources citent la base du CMS, le FileStore (dossiers Input et Output) et la base d'audit. Wiiisdom ajoute les fichiers de paramétrage modifiés."),
  ("Faut-il sauvegarder la base du CMS et le FileStore en même temps ?", "Oui. Wiiisdom et Umang recommandent de les capturer ensemble pour éviter un état désynchronisé et des objets orphelins."),
  ("Quelle information faut-il conserver pour restaurer ?", "Le mot de passe administrateur et la clé de cluster du serveur d'origine, selon Wiiisdom et le blog SAP BI 4.x."),
  ("À quelle fréquence tester la restauration ?", "Wiiisdom demande des tests réguliers et documentés. Aucune fréquence chiffrée n'est donnée par les sources : fixez-la selon la criticité de la plateforme, et testez au minimum avant chaque montée de version."),
 ],
 related=["checklist-migration-sap-businessobjects", "double-exploitation-businessobjects-periode-transition", "promotion-management-lcm-businessobjects-montee-de-version"],
)
