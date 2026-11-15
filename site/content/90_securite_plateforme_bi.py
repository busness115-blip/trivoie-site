PAGE = dict(
 slug="securite-plateforme-bi-droits-comptes-audit-businessobjects",
 nav="Droits et comptes BI",
 title="Sécurité BusinessObjects : droits, comptes, audit",
 desc="Droits hérités, comptes inactifs, audit natif : que contrôler sur sa plateforme SAP BusinessObjects avant une migration ou une montée de version.",
 h1="Sécurité d'une plateforme BI : droits, comptes inactifs et audit avant migration",
 lead="Avant de migrer ou de monter de version, une plateforme SAP BusinessObjects contient souvent des années de droits empilés et de comptes dont plus personne ne sait à quoi ils servent. Ce guide présente ce qu'il vaut la peine de contrôler, avec les sources publiques qui décrivent le fonctionnement des droits et de l'audit.",
 published="2026-11-15", modified="2026-11-15",
 body="""
<h2>Pourquoi contrôler les droits avant de migrer</h2>
<p>Une migration déplace des contenus, mais aussi les règles qui disent qui peut les voir. Si ces règles sont devenues illisibles, elles seront soit recopiées telles quelles, soit refaites sans savoir ce qu'elles protégeaient. Un état des lieux des droits, des comptes et de l'audit est donc une étape du projet, que la cible soit BI 2025 ou un autre outil. Le contexte de dates est rappelé en fin de page.</p>

<h2>1. Comprendre comment les droits se combinent</h2>
<p>La formation officielle de SAP (SAP Learning) décrit les règles de calcul des droits effectifs :</p>
<ul>
<li>un sous-dossier reprend les droits de son dossier parent, et un sous-groupe ceux de son groupe parent, sauf droits définis explicitement sur lui ;</li>
<li>ces deux héritages sont activés par défaut, et SAP recommande de les conserver ;</li>
<li>quand des droits entrent en conflit, le refus l'emporte sur l'octroi, et l'octroi sur « non spécifié » ;</li>
<li>un utilisateur membre de plusieurs groupes cumule les droits de ces groupes, et les droits effectifs sont calculés à la connexion.</li>
</ul>
<p>Wiiisdom, éditeur d'outils pour BusinessObjects, constate de son côté qu'une modification de droits peut se répercuter sur tout l'environnement « comme un effet domino », et que déterminer nativement les droits hérités et doublement hérités est difficile. Les deux sources concordent sur le fond : plus l'arborescence est profonde et plus les exceptions sont nombreuses, plus il est long de dire qui a accès à quoi.</p>

<h2>2. Préférer des groupes à des droits individuels</h2>
<p>Wiiisdom recommande des modèles de sécurité aussi simples que possible, construits à partir de rôles ou de groupes plutôt que de droits attribués utilisateur par utilisateur. C'est l'avis d'un éditeur d'outils, mais il facilite concrètement la migration : un groupe se recrée dans une cible, une liste d'exceptions individuelles se reprend au cas par cas.</p>

<h2>3. Repérer les comptes inactifs et le contenu orphelin</h2>
<p>Protiviti, société de conseil, cite parmi les usages de l'audit la recherche des utilisateurs qui ne se sont jamais connectés (utile pour libérer des licences nominatives) et celle des univers qui ne sont plus utilisés. Côté cycle de vie des comptes, Wiiisdom indique que par défaut, lorsqu'un utilisateur supprimé possède des documents ou des instances, ceux-ci sont réassignés à l'administrateur, et qu'un compte peut subsister après le départ d'un employé. Ces points conduisent à vérifier trois choses :</p>
<ul>
<li>les comptes sans connexion récente, à rapprocher de la liste des départs ;</li>
<li>les contenus appartenant à des comptes supprimés et réassignés ;</li>
<li>les comptes d'administration, leur nombre et leur usage.</li>
</ul>
<p>Le comptage des documents réellement utilisés se fait par requête, voir <a href="/compter-documents-sap-businessobjects-query-builder/">compter ses documents avec Query Builder</a>.</p>

<h2>4. Savoir ce que l'audit natif enregistre</h2>
<p>D'après SAP Learning, le serveur de gestion central (CMS) joue le rôle d'auditeur : il horodate les événements et les stocke dans une base dédiée, l'Auditing Data Store. Il audite les serveurs et trois clients : BI Launch Pad, Web Intelligence Rich Client et la CMC. Le niveau d'audit se règle de Off à Complete, et la durée de conservation se fixe en jours : les événements plus anciens sont supprimés définitivement, ce qui impose d'archiver si l'on veut un historique long. La base de connaissances de Wiiisdom décrit la même fonction, avec des événements tels que les connexions, les actualisations de documents, les consultations de rapports et les planifications.</p>
<p>Deux conséquences pratiques : vérifier que l'audit est activé avant le début du projet, afin de disposer de données d'usage réelles, et vérifier la durée de conservation avant qu'elle n'efface ce dont vous avez besoin. Wiiisdom note par ailleurs que retrouver qui avait accès à quoi à une date passée suppose, sans outil complémentaire, de restaurer une sauvegarde : ce point est à intégrer à votre propre exigence de traçabilité.</p>

<h2>5. Documenter avant de décider</h2>
<p>Un état des lieux utile tient en quatre livrables : la liste des groupes et de leurs membres, les dossiers dont les droits sortent de l'héritage par défaut, la liste des comptes inactifs ou orphelins, et l'état de l'audit (niveau, conservation, dernière extraction). Il alimente directement le tri décrit dans <a href="/nettoyer-parc-businessobjects-documents-inutilises/">nettoyer son parc de documents inutilisés</a> et la <a href="/checklist-migration-sap-businessobjects/">checklist de migration</a>.</p>

<h2>Dates à garder en tête</h2>
<p>La maintenance standard de BI 4.3 se termine le 31 décembre 2026. En 2027, la maintenance spécifique client ne couvre que les correctifs de sécurité CVSS 7 ou plus ; à partir de 2028, plus aucun correctif n'est livré. BI 2025 reste en maintenance standard jusqu'au 31 décembre 2027. Le détail des risques est dans <a href="/risque-securite-sap-businessobjects-4-3/">le risque de sécurité de la 4.3</a>. Un contrôle des droits et des comptes réduit la surface exposée pendant cette période, quelle que soit la cible retenue.</p>

<h2>Accompagnement</h2>
<p>AM DATA n'est revendeur ni de SAP ni de Microsoft. Le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> inclut un état des lieux de votre parc, que vous restiez chez SAP ou que vous migriez. Pour un audit plus large, voir <a href="/audit-sap-businessobjects/">l'audit SAP BusinessObjects</a>.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://learning.sap.com/courses/securing-application-and-content-in-sap-businessobjects-bi-platform/determining-effective-rights-and-inheritance_af1e72a2-bcb2-4e81-9639-e9ce0432ec77" rel="noopener">Determining Effective Rights and Inheritance (SAP Learning)</a></li>
<li><a href="https://learning.sap.com/courses/administrating-servers-in-sap-businessobjects-bi-platform/describing-the-central-management-server-cms-system-database-for-auditing" rel="noopener">Describing the CMS System Database for Auditing (SAP Learning)</a></li>
<li><a href="https://wiiisdom.com/business-objects-security/" rel="noopener">Business Objects Security (Wiiisdom)</a></li>
<li><a href="https://service.wiiisdom.com/portal/en/kb/articles/sap-businessobjects-auditing-vs-360suite-understanding-the-difference" rel="noopener">SAP BusinessObjects Auditing vs. 360Suite (Wiiisdom)</a></li>
<li><a href="https://tcblog.protiviti.com/2020/03/13/leading-practices-for-a-well-maintained-sap-businessobjects-system/" rel="noopener">Leading practices for a well-maintained SAP BusinessObjects system (Protiviti)</a></li>
</ul>
""",
 faqs=[
  ("Comment se combinent les droits dans SAP BusinessObjects ?", "Selon SAP Learning, les dossiers et groupes enfants héritent des droits de leur parent, le refus l'emporte sur l'octroi, et un utilisateur membre de plusieurs groupes cumule leurs droits."),
  ("Que devient le contenu d'un utilisateur supprimé ?", "Wiiisdom indique que par défaut, les documents et instances d'un utilisateur supprimé sont réassignés à l'administrateur. Il faut donc les examiner avant de migrer."),
  ("L'audit natif conserve-t-il l'historique indéfiniment ?", "Non. D'après SAP Learning, la durée de conservation se règle en jours et les événements plus anciens sont supprimés définitivement : il faut archiver pour garder un historique long."),
  ("Faut-il revoir les droits même si l'on reste sur BI 4.3 ou BI 2025 ?", "Oui, c'est un contrôle utile quelle que soit la cible. Il limite la surface exposée, notamment en 2027 où seuls les correctifs de sécurité CVSS 7 ou plus sont livrés dans le cadre de la maintenance spécifique client."),
 ],
 related=["risque-securite-sap-businessobjects-4-3", "nettoyer-parc-businessobjects-documents-inutilises", "checklist-migration-sap-businessobjects", "diagnostic-sortie-businessobjects"],
)
