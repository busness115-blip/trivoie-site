PAGE = dict(
 slug="composants-absents-bi-2025-inventaire-parc-businessobjects",
 nav="Composants absents de BI 2025",
 title="Composants absents de BI 2025 : inventaire de votre parc",
 desc="Quels outils BusinessObjects 4.3 ne sont pas livrés dans BI 2025 : univers UNV, Live Office, Crystal Enterprise, Mobile. Méthode d'inventaire et sources.",
 h1="Composants absents de BI 2025 : comment inventorier votre parc BusinessObjects",
 lead="Passer de BusinessObjects 4.3 à BI 2025 ne se résume pas à une montée de version : certains outils de la 4.3 ne sont pas repris. Ce guide recense ce que disent deux analyses publiées sur ce sujet, distingue ce qui est recoupé de ce qui ne repose que sur une analyse, et propose une méthode simple pour savoir ce que votre parc utilise vraiment.",
 published="2026-11-25", modified="2026-11-25",
 body="""
<h2>Pourquoi faire cet inventaire maintenant</h2>
<p>La maintenance standard de la 4.3 s'arrête le 31 décembre 2026. Que vous visiez BI 2025, une autre plateforme ou un maintien en 4.3 sous <a href="/maintenance-specifique-client-sap-businessobjects/">maintenance spécifique client</a>, la première question est la même : quels composants votre parc utilise-t-il, et lesquels n'existent plus dans la version suivante ? Sans cette liste, un chiffrage de projet reste approximatif.</p>

<h2>Ce que deux analyses indépendantes confirment</h2>
<p>Wiiisdom et NEED4VIZ concordent sur plusieurs points.</p>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Composant</th><th>Situation dans BI 2025</th></tr></thead>
<tbody>
<tr><td>Univers .unv et Universe Design Tool</td><td>Plus pris en charge après la 4.3 : conversion en .unx nécessaire. Voir <a href="/convertir-univers-unv-en-unx/">notre guide</a>.</td></tr>
<tr><td>Univers multi-sources</td><td>Absents de BI 2025 (derniers livrés en 4.3)</td></tr>
<tr><td>Lumira Designer</td><td>Maintenu sans nouvelles fonctionnalités. Voir <a href="/lumira-designer-design-studio-avenir/">notre page dédiée</a>.</td></tr>
<tr><td>Web Intelligence, univers .unx, Crystal Reports Classic, Analysis for Microsoft Office, plateforme BI</td><td>Repris dans BI 2025 (liste citée par Wiiisdom)</td></tr>
</tbody></table></div>
<p>Wiiisdom ajoute que les composants laissés de côté restent dans la 4.3, mais que leur maintenance standard s'y termine en 2026.</p>

<h2>Ce qu'indique NEED4VIZ seul</h2>
<p>NEED4VIZ, éditeur d'une solution concurrente, analyse le Statement of Direction de SAP. Sa lecture n'est recoupée par aucune autre source consultée : nous la lui attribuons nommément, et vous pouvez la comparer au document d'origine de SAP.</p>
<ul>
<li>Selon NEED4VIZ, la fin de maintenance standard est fixée à fin 2026 pour Crystal Reports for Enterprise, Live Office, SAP Lumira Discovery, Analysis edition for OLAP et BusinessObjects Mobile, et ces outils ne sont pas livrés dans BI 2025.</li>
<li>NEED4VIZ indique que Crystal Reports sur Linux est retiré dans BI 2025.</li>
<li>Côté infrastructure, NEED4VIZ écrit qu'AIX et Solaris ne sont plus pris en charge après la 4.3, que BI 2025 ne prend en charge que IBM WebSphere Liberty 25 comme serveur d'applications externe, que seul Tomcat intégré le serait à partir de BI 2027, et que l'authentification SAML est dépréciée en 2025 et supprimée en 2027.</li>
</ul>
<p>Pour les alternatives, NEED4VIZ cite Web Intelligence, Crystal Reports ou SAP Analytics Cloud selon l'outil. Ces choix dépendent de vos usages : un outil absent de BI 2025 ne devient pas un problème s'il n'est plus ouvert par personne.</p>

<h2>Comment lire ces informations</h2>
<p>Deux précautions s'imposent. D'abord, ces deux publications sont des analyses de partenaires et d'éditeurs tiers : elles ne remplacent pas la documentation officielle de SAP, que vous pouvez consulter avant toute décision. Ensuite, la liste des composants évolue avec chaque mise à jour du Statement of Direction : relisez-la avant de figer un plan de migration. Enfin, un composant absent de BI 2025 n'est pas forcément un obstacle, car de nombreux parcs n'utilisent plus la moitié des outils installés.</p>

<h2>Méthode d'inventaire en quatre étapes</h2>
<h3>1. Lister les composants installés</h3>
<p>Relevez, côté serveur et postes, ce qui est réellement déployé : Live Office dans Office, clients Crystal, applications mobiles, Lumira Discovery, univers .unv. L'inventaire installé est souvent plus large que l'usage réel.</p>
<h3>2. Mesurer l'usage sur douze mois</h3>
<p>La base d'audit permet de savoir ce qui a été ouvert. Un composant sans usage ne demande ni migration ni remplacement. Le guide sur le <a href="/nettoyer-parc-businessobjects-documents-inutilises/">nettoyage du parc</a> détaille cette étape.</p>
<h3>3. Rapprocher la liste de vos prérequis techniques</h3>
<p>Comparez le système d'exploitation, le serveur d'applications et le mode d'authentification en place avec ce que décrit NEED4VIZ, puis avec la documentation de SAP.</p>
<h3>4. Décider outil par outil</h3>
<p>Pour chaque composant utilisé : rester en 4.3 sous maintenance spécifique client, remplacer par un outil présent dans BI 2025, ou reconstruire sur une autre plateforme. AM DATA n'est revendeur ni de SAP ni de Microsoft : l'inventaire sert à documenter le choix, que vous restiez chez SAP ou que vous migriez. Le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> réalise cette étape sur votre parc.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://wiiisdom.com/blog/sap-businessobjects-bi-2025/" rel="noopener">SAP BusinessObjects BI 2025 : what do we know about it ? (Wiiisdom)</a></li>
<li><a href="https://www.need4viz.com/businessobjects-en/understanding-saps-latest-analytics-bi-statement-of-direction/" rel="noopener">Understanding SAP's Latest Analytics BI Statement of Direction (NEED4VIZ)</a></li>
</ul>
""",
 faqs=[
  ("Les univers .unv fonctionnent-ils dans BI 2025 ?", "Non. Wiiisdom et NEED4VIZ indiquent qu'ils ne sont plus pris en charge après la 4.3. Il faut les convertir en univers .unx."),
  ("Live Office existe-t-il dans BI 2025 ?", "Selon NEED4VIZ, Live Office n'est pas livré dans BI 2025 et sa maintenance standard s'arrête fin 2026. Cette information provient d'une seule analyse."),
  ("Que deviennent les outils non repris, s'ils restent installés en 4.3 ?", "Wiiisdom indique qu'ils restent dans la 4.3, avec une maintenance standard qui se termine en 2026. La suite relève de la maintenance spécifique client."),
  ("Comment savoir si un composant absent de BI 2025 me concerne ?", "Mesurez son usage sur douze mois avec la base d'audit. Un outil qui n'est plus ouvert ne demande ni migration ni remplacement."),
 ],
 related=["calendrier-fin-maintenance-sap-businessobjects-versions", "bi-2025-ou-sortir-de-businessobjects", "crystal-reports-fin-maintenance-4-3-options"],
)
