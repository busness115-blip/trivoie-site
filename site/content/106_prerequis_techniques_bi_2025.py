PAGE = dict(
 slug="prerequis-techniques-bi-2025-systemes-java-serveur-applications",
 nav="Prérequis techniques BI 2025",
 title="Prérequis techniques de BI 2025 : OS, Java, bases",
 desc="Systèmes, Java 17, Tomcat, bases du CMS, AIX et Solaris retirés : ce que publie la matrice de disponibilité de BI 2025 et comment préparer votre parc.",
 h1="Prérequis techniques de SAP BusinessObjects BI 2025 : systèmes, Java, serveur d'applications",
 lead="Passer de la 4.3 à BI 2025 est aussi un projet d'infrastructure : système d'exploitation, version de Java, serveur d'applications et base du CMS changent ou se resserrent. Cette page reprend la matrice de disponibilité (PAM) de BI 2025 telle que publiée en mai 2025, la recoupe avec deux analyses indépendantes, et propose une liste de contrôle à passer sur votre parc avant de choisir BI 2025 ou une autre voie.",
 published="2026-11-27", modified="2026-11-27",
 body="""
<h2>D'où viennent ces informations</h2>
<p>La source principale est la matrice de disponibilité des produits (PAM) de BI 2025, document SAP dont la dernière mise à jour porte la date du 22 mai 2025, consultée dans la copie publiée par Seenovate. Elle est recoupée par deux analyses du Statement of Direction : celle de Clint Vosloo, consultant, et celle de NEED4VIZ, éditeur d'une solution concurrente. Une matrice évolue avec les correctifs : relisez la version en vigueur sur le portail de SAP avant tout engagement.</p>

<h2>Ce que la matrice indique pour BI 2025</h2>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Sujet</th><th>Ce qui est publié</th></tr></thead>
<tbody>
<tr><td>Architecture</td><td>Serveur 64 bits, architecture x86_64. Clint Vosloo écrit de même que seuls les systèmes 64 bits sont pris en charge.</td></tr>
<tr><td>Windows</td><td>Windows Server 2022 comme minimum, Windows Server 2025 comme dernière version certifiée.</td></tr>
<tr><td>Linux</td><td>SUSE SLES 15 SP03 à 15 SP06 ; Red Hat Enterprise Linux 8.8 et 9.2 à 8.10 et 9.5 ; Oracle Linux 8.8 et 9.2 à 8.8 et 9.4.</td></tr>
<tr><td>Java</td><td>La matrice indique que BI 2025 est livré avec SapMachine JRE 17 (Java 17) et ne prend en charge que celui-ci, là où la 4.3 est livrée avec SAP JVM 8 (Java 8). Clint Vosloo cite aussi Java 17.</td></tr>
<tr><td>Serveur d'applications</td><td>Apache Tomcat 9.x certifié avec Java 17, pris en charge depuis BI 2025.</td></tr>
<tr><td>Base du CMS et d'audit</td><td>Db2 11.5 et 12.1, SQL Server 2019 et 2022, MySQL 8.0, Oracle 19c et 21c, SAP HANA 2.0 SPS 06 et 07, SAP ASE 16, SQL Anywhere 17. SQL Server 2019 n'est pas pris en charge sous Linux.</td></tr>
<tr><td>Navigateurs</td><td>Chrome, Edge, Firefox ESR et Safari, en 64 bits, avec des versions minimales publiées dans la matrice.</td></tr>
</tbody></table></div>

<h2>Ce qui disparaît par rapport à la 4.3</h2>
<p>La matrice contient un tableau des supports retirés entre la 4.3 et BI 2025 : IBM AIX et Oracle Solaris, SAP NetWeaver Java Application Server, SAP WACS, les portails SAP NetWeaver Enterprise Portal, IBM WebSphere Portal et Microsoft SharePoint, ainsi que les kits d'intégration d'authentification pour Oracle E-Business Suite, JD Edwards EnterpriseOne Tools et Siebel. NEED4VIZ et Clint Vosloo confirment tous deux le retrait d'AIX et de Solaris. Clint Vosloo ajoute que les architectures ARM et Power ne sont pas prises en charge.</p>
<p>Conséquence pratique : un parc sous AIX ou Solaris ne se met pas à niveau en place. Il demande de recréer la plateforme sur Windows ou Linux, ce qui rapproche le projet d'une migration que d'une simple mise à jour.</p>

<h2>Points où les sources se distinguent</h2>
<p>Nous citons séparément ce qui n'est pas strictement concordant.</p>
<ul>
<li><strong>Serveurs d'applications externes.</strong> La matrice de mai 2025 liste WebSphere Liberty et JBoss EAP 8 dans une feuille de route de certification, sans les déclarer certifiés à cette date. NEED4VIZ écrit, en citant le Statement of Direction, que BI 2025 ne prend en charge que WebSphere Liberty 25 comme serveur externe et que seul Tomcat intégré reste à partir de BI 2027. Si vous utilisez WebSphere, JBoss ou WebLogic, ce point conditionne votre projet.</li>
<li><strong>Authentification SAML.</strong> La matrice indique que SAML est pris en charge par défaut dans BI 2025 et cite trois fournisseurs certifiés : Google, Microsoft Entra et SAP Identity Authentication Service. NEED4VIZ écrit que SAML est déprécié en 2025 et retiré en 2027, avec OAuth 2.0 et OpenID Connect pour suite. Les deux lectures se cumulent : SAML fonctionne en BI 2025 mais n'est pas, selon NEED4VIZ, une base pour la durée.</li>
<li><strong>Annuaires LDAP.</strong> La matrice cite notamment Microsoft Active Directory 2019 et 2022. Vérifiez la ligne qui correspond à votre annuaire.</li>
</ul>

<h2>Liste de contrôle avant de décider</h2>
<h3>1. Relever l'existant</h3>
<p>Système et version, architecture, version de Java, serveur d'applications, type et version de la base du CMS et de la base d'audit, annuaire, mode d'authentification. Un tableau d'une ligne par serveur suffit.</p>
<h3>2. Comparer ligne à ligne avec la matrice</h3>
<p>Marquez chaque élément en trois états : déjà conforme, à mettre à niveau, à remplacer. Les bases de données et les annuaires sont les éléments qui ralentissent le plus souvent un calendrier, car ils relèvent d'autres équipes.</p>
<h3>3. Traiter les composants applicatifs</h3>
<p>Les univers .unv, Live Office, Crystal Reports for Enterprise et Mobile ne sont pas repris : voir notre <a href="/composants-absents-bi-2025-inventaire-parc-businessobjects/">inventaire des composants absents</a>.</p>
<h3>4. Prévoir la coexistence</h3>
<p>Une plateforme BI 2025 se construit à côté de la 4.3 pendant la transition : voir la <a href="/double-exploitation-businessobjects-periode-transition/">double exploitation</a> et la <a href="/checklist-migration-sap-businessobjects/">checklist de migration</a>.</p>
<h3>5. Décider avec le calendrier</h3>
<p>La maintenance standard de la 4.3 se termine le 31 décembre 2026. Le <a href="/calendrier-fin-maintenance-sap-businessobjects-versions/">calendrier des versions</a> remet les échéances en face de votre charge d'infrastructure.</p>

<h2>Quelle suite donner</h2>
<p>Que vous restiez chez SAP ou que vous étudiiez une autre plateforme, ce relevé sert dans les deux cas : il chiffre l'effort d'infrastructure de BI 2025 et documente ce qu'il faudrait refaire ailleurs. AM DATA n'est revendeur ni de SAP ni de Microsoft. Le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> peut réaliser ce relevé et le rapprochement avec votre parc de contenus.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://www.seenovate.com/wp-content/uploads/2025/06/SBOP_BI_2025-20250522.pdf" rel="noopener">SAP BusinessObjects BI platform 2025, Product Availability Matrix, mise à jour du 22 mai 2025 (copie hébergée par Seenovate)</a></li>
<li><a href="https://clintvosloo.com/bi-2025-sap-october-statement-of-direction-is-out" rel="noopener">SAP BusinessObjects BI 2025: Key Updates &amp; Changes (Clint Vosloo)</a></li>
<li><a href="https://www.need4viz.com/businessobjects-en/understanding-saps-latest-analytics-bi-statement-of-direction/" rel="noopener">Understanding SAP's Latest Analytics BI Statement of Direction (NEED4VIZ)</a></li>
</ul>
""",
 faqs=[
  ("BI 2025 fonctionne-t-il sous AIX ou Solaris ?", "Non. La matrice de BI 2025 range AIX et Solaris parmi les supports retirés, et NEED4VIZ comme Clint Vosloo le confirment. Les systèmes pris en charge sont Windows Server et certaines distributions Linux."),
  ("Quelle version de Java faut-il pour BI 2025 ?", "La matrice indique que BI 2025 est livré avec SapMachine JRE 17, basé sur Java 17, et ne prend en charge que celui-ci. La 4.3 est livrée avec SAP JVM 8."),
  ("Quel serveur d'applications utiliser avec BI 2025 ?", "La matrice de mai 2025 certifie Apache Tomcat 9.x. NEED4VIZ écrit que seul WebSphere Liberty 25 est pris en charge comme serveur externe, et que seul Tomcat intégré subsiste à partir de BI 2027. Vérifiez la version en vigueur de la matrice."),
  ("Quelles bases de données pour le CMS de BI 2025 ?", "La matrice cite Db2, SQL Server 2019 et 2022, MySQL 8.0, Oracle 19c et 21c, SAP HANA, SAP ASE 16 et SQL Anywhere 17, avec des restrictions selon le système d'exploitation."),
 ],
 related=["composants-absents-bi-2025-inventaire-parc-businessobjects", "bi-2025-ou-sortir-de-businessobjects", "calendrier-fin-maintenance-sap-businessobjects-versions"],
)
