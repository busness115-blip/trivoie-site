# Pages éditoriales supplémentaires. Mêmes règles que pages.py : faits attribués à une source nommée, pas de tiret cadratin.
from pages import SRC_CSM, SRC_EOL, SRC_2025, SRC_DEP, SRC_PAM

def tbl(n):
    return '<div class="tbl" tabindex="0" role="region" aria-label="Tableau %d (défilement horizontal)">' % n

PAGES2 = [
# ---------------------------------------------------------------------------------------------
dict(
 slug="maintenance-specifique-client-sap-businessobjects",
 title="Maintenance spécifique client SAP BusinessObjects : ce que ça couvre",
 desc="Ce que couvre (et ne couvre pas) la maintenance spécifique client de SAP BusinessObjects BI 4.3 après le 31 décembre 2026 : correctifs, délais, facturation, frais.",
 h1="Maintenance spécifique client SAP BusinessObjects : ce que ça couvre vraiment",
 lead="Après le 31 décembre 2026, les plateformes SAP BusinessObjects BI 4.3 qui ne migrent pas passent en maintenance spécifique client. Voici, point par point, ce que cela change par rapport à la maintenance standard.",
 body="""
<h2>Standard et spécifique client : la différence</h2>
""" + tbl(1) + """<table>
<thead><tr><th>Point</th><th>Maintenance standard (jusqu'au 31/12/2026)</th><th>Maintenance spécifique client (2027)</th></tr></thead>
<tbody>
<tr><td>Correctifs de sécurité</td><td>Livrés selon le cycle habituel de SAP.</td><td>Seuls les correctifs dont le score CVSS est de 7 ou plus, pendant les 12 premiers mois.</td></tr>
<tr><td>Délai de traitement</td><td>Engagements de service du contrat.</td><td>Pas d'engagement de délai (analyse de C. Vosloo).</td></tr>
<tr><td>Nouveaux problèmes</td><td>Pris en charge par le support.</td><td>Facturés comme du conseil (analyse de C. Vosloo).</td></tr>
<tr><td>Année 2028</td><td>Sans objet.</td><td>Plus aucun correctif, patch ni support package.</td></tr>
<tr><td>Frais de maintenance</td><td>Selon contrat.</td><td>Les frais du contrat continuent de s'appliquer (analyse de C. Vosloo).</td></tr>
</tbody></table></div>
<p>Sources : """ + SRC_CSM + """. Les dates et le seuil CVSS concordent avec les analyses d'InfoSol et de NTT DATA. Les conditions exactes dépendent de votre contrat : votre interlocuteur SAP peut les préciser.</p>

<h2>Ce que cela veut dire en pratique</h2>
<ul>
<li><strong>Votre plateforme continue de fonctionner.</strong> Rien ne s'arrête le 1er janvier 2027 : rapports, planifications et connexions restent actifs.</li>
<li><strong>Les failles de gravité moyenne ou faible ne sont plus corrigées</strong> à partir de 2027, et plus aucune faille ne l'est à partir de 2028.</li>
<li><strong>Le support change de nature.</strong> Sans délai garanti, une panne ou une régression en production pourrait durer plus longtemps qu'aujourd'hui.</li>
<li><strong>Le coût ne baisse pas.</strong> Les frais de maintenance du contrat continuent de s'appliquer pour une couverture réduite, selon l'analyse de C. Vosloo : un point à présenter à la direction financière.</li>
</ul>

<h2>Pour qui c'est un choix raisonnable</h2>
<p>Rester en 4.3 sous maintenance spécifique client peut être une option défendable pour un an, par exemple pour une plateforme peu exposée, bien isolée du réseau, dont l'usage est limité et dont la sortie est déjà planifiée. Ce n'est pas une option « par défaut » : elle doit être décidée, documentée et assortie de mesures de sécurité complémentaires.</p>

<h2>Ce qu'il faut décider avant la fin de l'année</h2>
<ol>
<li>Rester en 4.3, monter en BI 2025 ou sortir de BusinessObjects (<a href="/bi-2025-ou-sortir-de-businessobjects/">les critères</a>).</li>
<li>Si l'on reste : qui porte le risque, et quelles mesures compensatoires (isolement réseau, accès restreints, supervision) ?</li>
<li>Quand sera prise la décision suivante, puisqu'une année 2028 sans correctif n'est pas tenable pour une plateforme exposée ?</li>
</ol>
""",
 faqs=[
  ("Qu'est-ce que la maintenance spécifique client de SAP BusinessObjects ?", "C'est le régime appliqué aux clients qui restent sur SAP BusinessObjects BI 4.3 après la fin de la maintenance standard, le 31 décembre 2026. En 2027, seuls les correctifs de sécurité graves (CVSS 7 ou plus) sont livrés, sans engagement de délai, et les nouveaux problèmes peuvent être facturés. À partir de 2028, plus aucun correctif n'est livré."),
  ("Les frais de maintenance baissent-ils en maintenance spécifique client ?", "Selon l'analyse de C. Vosloo, non : les frais de maintenance de votre contrat continuent de s'appliquer alors que la couverture se réduit. Les conditions exactes dépendent de votre contrat."),
  ("La plateforme s'arrête-t-elle le 1er janvier 2027 ?", "Non. La plateforme continue de fonctionner. Ce qui change, c'est le niveau de protection et de support."),
 ],
 related=["fin-maintenance-sap-businessobjects-4-3","risque-securite-sap-businessobjects-4-3","bi-2025-ou-sortir-de-businessobjects"],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug="risque-securite-sap-businessobjects-4-3",
 title="Risque de sécurité SAP BusinessObjects 4.3 : le point pour un RSSI",
 desc="Ce que la fin de maintenance de SAP BusinessObjects 4.3 pourrait changer pour la sécurité, mesures compensatoires et questions à poser.",
 h1="Risque de sécurité SAP BusinessObjects 4.3 : le point pour un RSSI",
 lead="Une plateforme décisionnelle donne souvent accès à des données sensibles : finance, ressources humaines, clients. Voici comment inscrire la fin de maintenance de SAP BusinessObjects 4.3 dans un registre des risques.",
 body="""
<h2>Ce qui est corrigé, et ce qui ne l'est plus</h2>
""" + tbl(2) + """<table>
<thead><tr><th>Période</th><th>Failles corrigées</th><th>Failles qui restent ouvertes</th></tr></thead>
<tbody>
<tr><td>Jusqu'au 31/12/2026</td><td>Cycle de correctifs standard.</td><td>Selon le cycle de SAP.</td></tr>
<tr><td>2027</td><td>Gravité élevée ou critique (score CVSS de 7 ou plus), selon les informations publiées.</td><td>Gravité moyenne et faible.</td></tr>
<tr><td>2028</td><td>Aucune, selon les informations publiées.</td><td>Toutes les nouvelles failles.</td></tr>
</tbody></table></div>
<p>Source : """ + SRC_CSM + """. Analyse des notes SAP 3486924 et 3763590, recoupée avec InfoSol et NTT DATA.</p>
<p>Le score CVSS (Common Vulnerability Scoring System) note la gravité d'une faille de 0 à 10. Un score de 7 à 8,9 est qualifié d'élevé, de 9 à 10 de critique.</p>

<h2>Comment l'écrire dans un registre des risques</h2>
<ul>
<li><strong>Actif concerné :</strong> la plateforme SAP BusinessObjects 4.3 et les données qu'elle expose.</li>
<li><strong>Événement :</strong> exploitation d'une faille non corrigée (moyenne ou faible en 2027, toute faille en 2028, si les informations publiées se confirment).</li>
<li><strong>Facteurs aggravants :</strong> plateforme accessible depuis internet ou par de nombreux comptes, données sensibles, comptes inactifs jamais supprimés.</li>
<li><strong>Échéance de décision :</strong> avant le 31 décembre 2026 pour choisir la voie, avant fin 2027 au plus tard pour ne pas entrer en 2028 sans correctif, si les informations publiées se confirment.</li>
</ul>

<h2>Mesures compensatoires à examiner</h2>
<ul>
<li>Limiter l'accès réseau à la plateforme (pas d'exposition directe à internet si ce n'est pas nécessaire).</li>
<li>Supprimer les comptes inactifs et revoir les droits : moins de comptes, moins de surface.</li>
<li>Maintenir à jour le système d'exploitation, la base de données du référentiel et les composants tiers, qui ne dépendent pas de la maintenance BusinessObjects.</li>
<li>Superviser les connexions et activer l'audit de la plateforme.</li>
<li>Documenter la décision de rester, sa durée et son responsable.</li>
</ul>
<p>Ces mesures réduisent l'exposition mais ne remplacent pas les correctifs : elles servent à tenir une année, pas plusieurs.</p>

<h2>Les chiffres à fournir au RSSI</h2>
<p>Nombre de comptes (dont actifs sur 12 mois), nombre de documents et d'univers, contenus obsolètes, connexions à des sources sensibles. Les <a href="/compter-documents-sap-businessobjects-query-builder/">requêtes Query Builder</a> les donnent en lecture seule, et le <a href="/#scan">scan gratuit</a> les transforme en niveau de risque.</p>
""",
 faqs=[
  ("Quel score CVSS est encore corrigé en 2027 ?", "Seuls les correctifs de sécurité dont le score CVSS est de 7 ou plus sont livrés en 2027, pendant les 12 premiers mois de la maintenance spécifique client (notes SAP 3486924 et 3763590, analysées par C. Vosloo)."),
  ("Que se passe-t-il pour la sécurité en 2028 ?", "À partir de 2028, plus aucun correctif n'est livré pour SAP BusinessObjects BI 4.3. Toute nouvelle faille reste alors ouverte."),
  ("Les mesures compensatoires suffisent-elles ?", "Elles réduisent l'exposition à court terme mais ne remplacent pas les correctifs. Elles servent à tenir le temps d'une migration, pas à prolonger la plateforme durablement."),
 ],
 related=["maintenance-specifique-client-sap-businessobjects","fin-maintenance-sap-businessobjects-4-3","diagnostic-sortie-businessobjects"],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug="convertir-univers-unv-en-unx",
 title="Convertir ses univers UNV en UNX : méthode et points de vigilance",
 desc="Les univers UNV ne sont plus pris en charge après SAP BusinessObjects 4.3. Comment compter, convertir en UNX et retester les documents Web Intelligence.",
 h1="Convertir ses univers UNV en UNX : méthode et points de vigilance",
 lead="Les univers UNV ne sont plus pris en charge après la version 4.3. Avant de monter en BI 2025, il faut les convertir en UNX et vérifier que les documents qui en dépendent fonctionnent toujours.",
 body="""
<h2>Pourquoi c'est un chantier à part</h2>
<p>Un univers est la couche sémantique sur laquelle s'appuient les documents Web Intelligence. Le format historique est l'UNV, le format actuel l'UNX. Les univers UNV ne sont plus pris en charge dans SAP BusinessObjects BI 2025 : l'outil Universe Design Tool n'est plus livré (""" + SRC_2025 + """). Une montée de version impose donc de les traiter.</p>

<h2>Les étapes</h2>
<ol>
<li><strong>Compter.</strong> Nombre d'univers UNV et UNX : voir <a href="/compter-documents-sap-businessobjects-query-builder/">les requêtes Query Builder</a>.</li>
<li><strong>Trier.</strong> Repérer les univers réellement utilisés (par des documents ouverts dans les 12 derniers mois) et ceux qui ne le sont plus. Les seconds se décommissionnent au lieu de se convertir.</li>
<li><strong>Convertir.</strong> L'outil de conception d'univers (Information Design Tool) permet de convertir un univers UNV en UNX. Gardez l'UNV d'origine tant que la validation n'est pas terminée.</li>
<li><strong>Repointer les documents.</strong> Les documents Web Intelligence doivent ensuite utiliser l'univers UNX, avec la fonction de changement de source de données.</li>
<li><strong>Retester.</strong> Comparer les résultats d'un échantillon de documents avant et après : mêmes chiffres, mêmes filtres, mêmes invites, même performance.</li>
<li><strong>Basculer et suivre.</strong> Mettre en production par lots, avec un retour arrière possible.</li>
</ol>

<h2>Points de vigilance</h2>
<ul>
<li>Un univers très ancien ou très personnalisé peut demander des corrections après conversion.</li>
<li>Les documents dont le périmètre n'est pas connu sont les plus risqués : sans propriétaire identifié, personne ne valide les résultats.</li>
<li>Le travail est proportionnel au nombre d'univers et de documents rattachés : l'inventaire précède le chiffrage.</li>
</ul>
<p>Le détail exact des fonctions de conversion et de leurs limites dépend de votre version : consultez la documentation de SAP avant de lancer la conversion.</p>
""",
 faqs=[
  ("Les univers UNV fonctionnent-ils en SAP BusinessObjects BI 2025 ?", "Les univers UNV ne sont plus pris en charge dans BI 2025, car l'outil Universe Design Tool n'est plus livré. Ils doivent être convertis en UNX avant la montée de version."),
  ("Comment convertir un univers UNV en UNX ?", "Avec l'outil de conception d'univers (Information Design Tool), qui permet de convertir un UNV en UNX. Gardez l'original, convertissez, puis repointez et retestez les documents Web Intelligence."),
  ("Faut-il convertir tous les univers ?", "Non. Les univers qu'aucun document récent n'utilise peuvent être décommissionnés plutôt que convertis, ce qui réduit l'effort."),
 ],
 related=["compter-documents-sap-businessobjects-query-builder","bi-2025-ou-sortir-de-businessobjects","fin-maintenance-sap-businessobjects-4-3"],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug="contenus-obsoletes-xcelsius-desktop-intelligence-explorer",
 title="Xcelsius, Desktop Intelligence, Explorer : que faire de ces contenus",
 desc="Xcelsius, Dashboards, Desktop Intelligence, Explorer et contenus Flash : comment les repérer sur une plateforme SAP BusinessObjects 4.3 et décider de leur sort.",
 h1="Xcelsius, Desktop Intelligence, Explorer : que faire de ces contenus obsolètes",
 lead="Certains contenus d'une plateforme SAP BusinessObjects n'ont pas d'avenir au-delà de la version 4.3. Les repérer tôt évite de les découvrir pendant le projet de migration.",
 body="""
<h2>Les contenus concernés</h2>
<p>D'après les notes SAP résumées par la communauté (""" + SRC_DEP + """), Xcelsius et Dashboards, Desktop Intelligence, Explorer et les contenus Flash font partie des composants concernés par des dépréciations. Lumira Designer reste maintenu mais sans nouvelle fonctionnalité. Vérifiez la situation exacte de chacun dans la Product Availability Matrix de SAP (""" + SRC_PAM + """).</p>

<h2>Comment les compter</h2>
<p>Une requête Query Builder en lecture seule donne le nombre de contenus obsolètes sur le référentiel : voir <a href="/compter-documents-sap-businessobjects-query-builder/">la liste des requêtes</a>. Notez aussi, pour chacun, la date de dernière ouverture.</p>

<h2>Trois décisions possibles par contenu</h2>
""" + tbl(3) + """<table>
<thead><tr><th>Décision</th><th>Quand</th><th>Effort</th></tr></thead>
<tbody>
<tr><td>Supprimer</td><td>Personne ne l'ouvre depuis longtemps, aucune obligation de conservation.</td><td>Faible. Archiver avant suppression.</td></tr>
<tr><td>Refaire</td><td>Le besoin existe encore (tableau de bord suivi, rapport réglementaire).</td><td>Réécriture dans un outil pris en charge.</td></tr>
<tr><td>Conserver à l'identique</td><td>Obligation d'archivage ou usage très restreint, plateforme isolée.</td><td>Faible, mais risque à porter.</td></tr>
</tbody></table></div>

<h2>L'ordre à suivre</h2>
<ol>
<li>Compter les contenus obsolètes et leur dernière ouverture.</li>
<li>Identifier un propriétaire métier pour chaque contenu encore utilisé.</li>
<li>Supprimer ce qui n'est plus ouvert, après archivage.</li>
<li>Chiffrer la refonte du reste : c'est souvent le poste qui oriente le choix entre BI 2025 et une autre plateforme.</li>
</ol>
""",
 faqs=[
  ("Xcelsius est-il encore pris en charge ?", "D'après les notes SAP résumées par la communauté, Xcelsius et Dashboards font partie des composants concernés par des dépréciations. Vérifiez la situation exacte dans la Product Availability Matrix de SAP."),
  ("Que faire des documents Desktop Intelligence ?", "Les compter, identifier ceux qui sont encore ouverts, puis supprimer les autres après archivage et refaire les rapports utiles dans un outil pris en charge."),
 ],
 related=["fin-maintenance-sap-businessobjects-4-3","nettoyer-parc-businessobjects-documents-inutilises","bi-2025-ou-sortir-de-businessobjects"],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug="nettoyer-parc-businessobjects-documents-inutilises",
 title="Nettoyer son parc BusinessObjects : repérer les documents inutilisés",
 desc="Avant de migrer SAP BusinessObjects, repérez les documents jamais ouverts, les comptes inactifs et les planifications mortes : méthode, audit et décisions.",
 h1="Nettoyer son parc BusinessObjects avant de migrer : repérer l'inutilisé",
 lead="Sur une plateforme installée depuis longtemps, une partie du contenu n'est plus ouverte par personne. La migrer, c'est payer pour déplacer des documents que personne ne lit. Voici comment le repérer.",
 body="""
<h2>Pourquoi nettoyer d'abord</h2>
<p>Le coût d'une montée de version ou d'une migration dépend du nombre de documents, d'univers et de comptes à traiter. Retirer l'inutilisé avant de chiffrer réduit l'effort, le risque et la durée de la double exploitation.</p>

<h2>Ce qu'il faut repérer</h2>
<ul>
<li><strong>Les documents jamais ouverts ou ouverts il y a très longtemps</strong> (Web Intelligence, Crystal Reports et autres).</li>
<li><strong>Les comptes inactifs</strong> : la date de dernière connexion de chaque compte figure dans le référentiel (<a href="/compter-documents-sap-businessobjects-query-builder/">requêtes Query Builder</a>).</li>
<li><strong>Les planifications récurrentes</strong> qui produisent des rapports que personne ne consulte.</li>
<li><strong>Les univers sans document actif</strong>, qui n'ont pas besoin d'être convertis.</li>
<li><strong>Les doublons</strong> : mêmes rapports copiés par plusieurs équipes.</li>
</ul>

<h2>La source des chiffres : l'audit de la plateforme</h2>
<p>La consultation réelle des documents se lit dans la base d'audit de la plateforme, à condition que l'audit ait été activé et qu'il ait tourné assez longtemps pour couvrir un cycle complet d'usage (par exemple 12 mois, pour inclure les rapports de clôture annuelle). Si l'audit n'était pas actif, il est encore temps de l'activer : même quelques mois de données valent mieux que rien pour un premier tri.</p>

<h2>Méthode en quatre temps</h2>
<ol>
<li><strong>Mesurer</strong> : dernière ouverture par document, dernière connexion par compte.</li>
<li><strong>Classer</strong> : actif, rare (une ou deux fois par an), inactif.</li>
<li><strong>Valider</strong> avec les propriétaires métier : un document rarement ouvert peut être obligatoire (clôture, réglementaire).</li>
<li><strong>Archiver puis supprimer</strong> l'inactif, de façon traçable.</li>
</ol>
<p>Le résultat se retrouve directement dans le chiffrage : moins de documents à migrer, moins d'utilisateurs à former, une décision plus claire entre rester, monter en BI 2025 ou sortir.</p>
""",
 faqs=[
  ("Comment savoir quels documents BusinessObjects ne sont jamais ouverts ?", "Avec la base d'audit de la plateforme, si l'audit est activé : elle enregistre les consultations. Croisez-la avec la liste des documents du référentiel pour repérer ceux qui n'apparaissent jamais."),
  ("Combien de temps d'audit faut-il ?", "Idéalement un cycle complet d'usage, par exemple 12 mois, pour ne pas supprimer un rapport annuel. Quelques mois suffisent pour un premier tri des documents évidemment inutilisés."),
  ("Peut-on supprimer directement ce qui n'est pas ouvert ?", "Mieux vaut valider avec les propriétaires métier, archiver, puis supprimer : un rapport rarement ouvert peut être obligatoire."),
 ],
 related=["compter-documents-sap-businessobjects-query-builder","contenus-obsoletes-xcelsius-desktop-intelligence-explorer","diagnostic-sortie-businessobjects"],
),
# ---------------------------------------------------------------------------------------------
dict(
 slug="checklist-migration-sap-businessobjects",
 title="Checklist de migration SAP BusinessObjects en 10 étapes",
 desc="10 étapes pour préparer la sortie ou la montée de version de SAP BusinessObjects 4.3 : inventaire, usage, univers, sécurité, chiffrage, décision et plan.",
 h1="Checklist de migration SAP BusinessObjects en 10 étapes",
 lead="Dix étapes pour passer de « la maintenance 4.3 s'arrête » à une décision chiffrée, que l'on monte en BI 2025, que l'on reste ou que l'on sorte de BusinessObjects.",
 body="""
<ol class="steps">
<li><strong>Fixer l'échéance.</strong> Fin de maintenance standard de la 4.3 le 31 décembre 2026 (<a href="/fin-maintenance-sap-businessobjects-4-3/">détail des dates</a>).</li>
<li><strong>Nommer un responsable</strong> côté métier et côté technique, avec un sponsor qui décide.</li>
<li><strong>Inventorier</strong> : documents par type, univers UNV et UNX, connexions, comptes, planifications (<a href="/compter-documents-sap-businessobjects-query-builder/">requêtes</a>).</li>
<li><strong>Mesurer l'usage réel</strong> : dernières ouvertures, comptes actifs sur 12 mois (<a href="/nettoyer-parc-businessobjects-documents-inutilises/">méthode</a>).</li>
<li><strong>Repérer les points bloquants</strong> : univers UNV (<a href="/convertir-univers-unv-en-unx/">conversion</a>), contenus obsolètes (<a href="/contenus-obsoletes-xcelsius-desktop-intelligence-explorer/">que faire</a>).</li>
<li><strong>Évaluer le risque de sécurité</strong> et les mesures compensatoires (<a href="/risque-securite-sap-businessobjects-4-3/">point pour un RSSI</a>).</li>
<li><strong>Décommissionner</strong> ce qui n'est plus utilisé, après validation et archivage.</li>
<li><strong>Chiffrer les trois voies</strong> : rester en 4.3, monter en BI 2025, sortir de BusinessObjects. Coût, délai, risque de chacune (<a href="/bi-2025-ou-sortir-de-businessobjects/">critères</a>).</li>
<li><strong>Décider</strong> en comité avec une recommandation argumentée, y compris le scénario « on ne migre pas ».</li>
<li><strong>Planifier</strong> : lots, tests de non-régression, formation, période de double exploitation, plan de retour arrière.</li>
</ol>
<p>Les étapes 3 à 8 se réalisent en dix jours ouvrés dans le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a>, à prix fixe. Le <a href="/#scan">scan gratuit</a> donne un premier niveau de risque à partir des chiffres de l'étape 3.</p>
""",
 faqs=[
  ("Par quoi commencer une migration SAP BusinessObjects ?", "Par l'inventaire : nombre de documents par type, d'univers UNV et UNX, de comptes et de planifications, puis l'usage réel. Ces chiffres orientent le choix entre rester, monter en BI 2025 ou sortir."),
  ("Combien de temps prend la préparation de la décision ?", "Un diagnostic de décision, de l'inventaire au chiffrage des trois voies, prend 10 jours ouvrés dans le Diagnostic Sortie BO de Trivoie. Le projet de migration lui-même dépend de la voie choisie."),
 ],
 related=["diagnostic-sortie-businessobjects","fin-maintenance-sap-businessobjects-4-3","questions-a-poser-prestataire-migration-businessobjects"],
 sources=False,
),
# ---------------------------------------------------------------------------------------------
dict(
 slug="questions-a-poser-prestataire-migration-businessobjects",
 title="Migration BusinessObjects : 7 questions à poser à votre prestataire",
 desc="Avant de signer une migration ou une montée de version SAP BusinessObjects, les questions qui révèlent l'indépendance, le périmètre et le vrai coût de la proposition.",
 h1="Migration BusinessObjects : les questions à poser à votre prestataire",
 lead="La proposition d'un prestataire dit moins que ses réponses à quelques questions simples. Voici celles à poser avant de signer une migration ou une montée de version.",
 body="""
<ol class="steps">
<li><strong>« Avez-vous chiffré le scénario où l'on ne migre pas ? »</strong> Une proposition qui ne compare qu'une seule voie ne vous aide pas à décider.</li>
<li><strong>« Percevez-vous une rémunération de l'éditeur que vous recommandez ? »</strong> Revendeur, partenaire ou indépendant : la réponse éclaire la recommandation.</li>
<li><strong>« Quelle part de notre contenu proposez-vous de ne pas migrer ? »</strong> Un prestataire qui migre tout n'a pas regardé l'usage réel.</li>
<li><strong>« Quels sont les chiffres sur lesquels repose votre estimation ? »</strong> Documents, univers UNV, contenus obsolètes, comptes actifs : sans inventaire, le chiffrage est une hypothèse.</li>
<li><strong>« Que se passe-t-il pour les univers UNV et les contenus obsolètes ? »</strong> C'est là que se cachent les dépassements (<a href="/convertir-univers-unv-en-unx/">conversion UNV en UNX</a>).</li>
<li><strong>« Quel est le prix, fixe ou au temps passé, et que comprend-il ? »</strong> Un prix fixe sur un périmètre écrit protège des dérives.</li>
<li><strong>« Quelle est la suite après 2027 ? »</strong> Monter en BI 2025 ne repousse l'échéance que d'un an (<a href="/bi-2025-ou-sortir-de-businessobjects/">critères de choix</a>).</li>
</ol>
<h2>Ce qu'AM DATA répond à ces questions</h2>
<p>Trivoie est un service d'AM DATA, indépendant : AM DATA n'est revendeur ni de SAP ni de Microsoft. Le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> est à prix fixe (2 900 à 7 900 € HT selon la taille de la plateforme) et chiffre les trois voies, dont celle où l'on ne migre pas.</p>
""",
 faqs=[
  ("Comment choisir un prestataire pour migrer SAP BusinessObjects ?", "Demandez s'il a chiffré le scénario sans migration, s'il perçoit une rémunération d'un éditeur, quelle part du contenu il propose de ne pas migrer et sur quels chiffres repose son estimation."),
  ("Un diagnostic indépendant est-il utile avant un appel d'offres ?", "Oui : il fournit un inventaire chiffré et trois options comparées, qui servent de base au cahier des charges et permettent de juger les propositions reçues."),
 ],
 related=["checklist-migration-sap-businessobjects","diagnostic-sortie-businessobjects","bi-2025-ou-sortir-de-businessobjects"],
 sources=False,
),
# ---------------------------------------------------------------------------------------------
dict(
 slug="diagnostic-businessobjects-secteur-public-marche-60000-euros",
 title="Secteur public : diagnostic BusinessObjects sous le seuil de 60 000 €",
 desc="Depuis le 1er avril 2026, un achat public sous 60 000 € HT peut se faire sans publicité ni mise en concurrence préalables : ce que cela permet pour un diagnostic BusinessObjects.",
 h1="Secteur public : engager un diagnostic BusinessObjects sans attendre une consultation",
 lead="Pour les acheteurs publics (hôpitaux, collectivités, établissements publics) sous SAP BusinessObjects 4.3, le relèvement du seuil de dispense de procédure facilite l'engagement rapide d'un diagnostic avant la fin d'année.",
 body="""
<h2>Ce qui a changé</h2>
<p>Le décret n° 2025-1386 du 29 décembre 2025 a relevé le seuil de dispense de publicité et de mise en concurrence préalables à 60 000 € HT, avec effet au 1er avril 2026 pour les achats de services (<a href="https://blog.landot-avocats.net/2026/04/01/marches-publics-relevement-du-seuil-de-dispense-de-procedure-a-60-000-e-des-aujourdhui/" rel="noopener">analyse du cabinet Landot et associés</a> ; <a href="https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053222294" rel="noopener">Code de la commande publique sur Légifrance</a>).</p>
<p>Les règles de bonne utilisation des deniers publics continuent de s'appliquer : choisir une offre pertinente, ne pas contracter systématiquement avec le même opérateur lorsqu'il existe plusieurs offres, et conserver la trace de la démarche. La situation de chaque acheteur doit être confirmée par son service achats ou juridique.</p>

<h2>Ce que cela permet ici</h2>
<p>Le Diagnostic Sortie BO est à prix fixe : 2 900 € HT (taille S), 4 900 € HT (M) ou 7 900 € HT (L), livré en 10 jours ouvrés. Ces montants se situent sous le seuil de 60 000 € HT. Un acheteur peut donc, sous réserve de la confirmation de son service achats, engager un diagnostic sans lancer une consultation de plusieurs mois, et arriver à la décision avant l'échéance du 31 décembre 2026.</p>

<h2>Ce qu'il faut préparer</h2>
<ul>
<li>Un besoin décrit : inventaire de la plateforme SAP BusinessObjects 4.3, usage réel, trois options chiffrées.</li>
<li>Une justification du choix du prestataire (indépendance, prix fixe, délai, expérience).</li>
<li>Un engagement de confidentialité et, si des données personnelles sont accessibles, un accord de sous-traitance RGPD (AM DATA les fournit).</li>
<li>L'accord de votre service achats ou juridique sur la procédure applicable.</li>
</ul>
<p>Voir le détail de l'offre sur <a href="/diagnostic-sortie-businessobjects/">la page du Diagnostic Sortie BO</a>.</p>
""",
 faqs=[
  ("Peut-on commander un diagnostic BusinessObjects sans appel d'offres ?", "Depuis le 1er avril 2026, les achats de services dont le montant est inférieur à 60 000 € HT peuvent être conclus sans publicité ni mise en concurrence préalables (décret n° 2025-1386), sous réserve du respect des principes de la commande publique et de la confirmation de votre service achats."),
  ("Quel est le prix du Diagnostic Sortie BO ?", "De 2 900 € HT (taille S) à 7 900 € HT (taille L), à prix fixe, livré en 10 jours ouvrés."),
 ],
 related=["diagnostic-sortie-businessobjects","checklist-migration-sap-businessobjects","fin-maintenance-sap-businessobjects-4-3"],
 sources=False,
),
# ---------------------------------------------------------------------------------------------
dict(
 slug="glossaire-sap-businessobjects",
 title="Glossaire SAP BusinessObjects : CMS, UNV, UNX, Webi, CVSS",
 desc="Les termes à connaître pour comprendre la fin de maintenance de SAP BusinessObjects 4.3 : CMS, CMC, UNV, UNX, Web Intelligence, Query Builder, CVSS, maintenance spécifique client.",
 h1="Glossaire SAP BusinessObjects : les termes de la fin de maintenance",
 lead="Les termes qui reviennent dans les discussions sur la fin de maintenance de SAP BusinessObjects 4.3, expliqués simplement pour les directions, les achats et les équipes sécurité.",
 body="""
<dl class="gloss">
<dt>SAP BusinessObjects BI (SAP BO, BO)</dt><dd>Plateforme décisionnelle de SAP qui regroupe la création, la planification et la diffusion de rapports et de tableaux de bord.</dd>
<dt>BI 4.3</dt><dd>Version de la plateforme dont la maintenance standard s'arrête le 31 décembre 2026.</dd>
<dt>BI 2025</dt><dd>Version suivante, dont la maintenance standard va jusqu'au 31 décembre 2027.</dd>
<dt>Maintenance standard</dt><dd>Régime normal de support et de correctifs prévu par le contrat de maintenance de l'éditeur.</dd>
<dt>Maintenance spécifique client</dt><dd>Régime appliqué après la fin de la maintenance standard : correctifs de sécurité graves seulement en 2027, aucun en 2028, sans engagement de délai (<a href="/maintenance-specifique-client-sap-businessobjects/">détail</a>).</dd>
<dt>CVSS</dt><dd>Common Vulnerability Scoring System : note de 0 à 10 qui mesure la gravité d'une faille de sécurité. À partir de 7, la faille est qualifiée d'élevée.</dd>
<dt>CMS</dt><dd>Central Management Server : le serveur qui gère le référentiel de la plateforme (documents, utilisateurs, droits, planifications).</dd>
<dt>CMC</dt><dd>Central Management Console : l'interface d'administration de la plateforme, utilisée notamment pour les comptes, les droits et l'audit.</dd>
<dt>Query Builder</dt><dd>Outil d'interrogation en lecture seule du référentiel du CMS, qui permet de compter documents, univers et comptes (<a href="/compter-documents-sap-businessobjects-query-builder/">requêtes</a>).</dd>
<dt>Web Intelligence (Webi)</dt><dd>Outil de création de rapports et d'analyses interrogeant une source de données par l'intermédiaire d'un univers.</dd>
<dt>Crystal Reports</dt><dd>Outil de rapports mis en page, souvent utilisé pour des documents imprimables ou réglementaires.</dd>
<dt>Univers</dt><dd>Couche sémantique qui présente les données de façon compréhensible aux utilisateurs métier, sans écrire de requête.</dd>
<dt>UNV</dt><dd>Format historique d'univers, qui n'est plus pris en charge après la 4.3 (<a href="/convertir-univers-unv-en-unx/">conversion</a>).</dd>
<dt>UNX</dt><dd>Format actuel d'univers, créé avec l'outil Information Design Tool.</dd>
<dt>Information Design Tool (IDT)</dt><dd>Outil de conception des univers UNX, qui permet aussi de convertir des univers UNV.</dd>
<dt>Xcelsius, Dashboards, Desktop Intelligence, Explorer</dt><dd>Anciens composants dont l'avenir est limité (<a href="/contenus-obsoletes-xcelsius-desktop-intelligence-explorer/">que faire</a>).</dd>
<dt>Audit de la plateforme</dt><dd>Enregistrement des événements (connexions, consultations de documents) dans une base dédiée, qui permet de mesurer l'usage réel (<a href="/nettoyer-parc-businessobjects-documents-inutilises/">méthode</a>).</dd>
<dt>Diagnostic Sortie BO</dt><dd>Diagnostic indépendant à prix fixe proposé par Trivoie : inventaire, usage, trois options chiffrées en 10 jours ouvrés (<a href="/diagnostic-sortie-businessobjects/">offre</a>).</dd>
</dl>
""",
 faqs=[
  ("Que signifie CMS dans SAP BusinessObjects ?", "CMS signifie Central Management Server : le serveur qui gère le référentiel de la plateforme (documents, utilisateurs, droits, planifications)."),
  ("Quelle est la différence entre UNV et UNX ?", "UNV est le format historique d'univers, non pris en charge après la 4.3. UNX est le format actuel, créé avec l'Information Design Tool."),
 ],
 related=["fin-maintenance-sap-businessobjects-4-3","convertir-univers-unv-en-unx","checklist-migration-sap-businessobjects"],
 sources=False,
),
]
