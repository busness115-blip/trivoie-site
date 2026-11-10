PAGE = dict(
 slug="audit-sap-businessobjects",
 title="Audit SAP BusinessObjects : contenu, méthode et livrables",
 desc="Que contient un audit de plateforme SAP BusinessObjects : inventaire, usage réel, univers UNV, contenus obsolètes, sécurité, planifications. Méthode et livrables.",
 h1="Audit SAP BusinessObjects : ce qu'il doit contenir",
 lead="Un audit de plateforme SAP BusinessObjects répond à une question simple : qu'avons-nous, qu'est-ce qui sert vraiment, et qu'est-ce que cela coûtera de le garder ou de le déplacer. Voici les points qu'un audit sérieux couvre, et ce que vous devez recevoir.",
 published="2026-11-10", modified="2026-11-10",
 body="""
<h2>Les six volets d'un audit</h2>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Volet</th><th>Question</th><th>Source</th></tr></thead>
<tbody>
<tr><td>Inventaire</td><td>Combien de documents par type, d'univers, de comptes, de planifications ?</td><td>Référentiel du CMS, <a href="/compter-documents-sap-businessobjects-query-builder/">Query Builder</a></td></tr>
<tr><td>Usage réel</td><td>Quels documents ont été ouverts depuis 12 mois, et par combien de personnes ?</td><td>Base d'audit</td></tr>
<tr><td>Univers</td><td>Combien d'univers UNV à convertir, et lesquels sont encore utilisés ?</td><td>Référentiel et base d'audit</td></tr>
<tr><td>Contenus obsolètes</td><td>Reste-t-il des Dashboards (Xcelsius), Desktop Intelligence, Explorer ou Lumira ?</td><td>Référentiel (<a href="/contenus-obsoletes-xcelsius-desktop-intelligence-explorer/">détail</a>)</td></tr>
<tr><td>Sécurité et comptes</td><td>Comptes inactifs, droits trop larges, version et niveau de correctifs</td><td>CMC, base d'audit</td></tr>
<tr><td>Diffusion</td><td>Publications et envois planifiés : qui reçoit quoi, et est-ce encore lu ?</td><td>Planifications du CMS</td></tr>
</tbody></table></div>

<h2>Ce que vous devez recevoir</h2>
<ul>
<li>Un inventaire chiffré, que vous pouvez recompter vous-même.</li>
<li>La liste de ce qui peut être décommissionné sans risque, avec les critères utilisés.</li>
<li>Les risques classés, avec leur échéance (en particulier la fin de maintenance de la 4.3 le 31 décembre 2026).</li>
<li>Les options possibles avec un ordre de grandeur d'effort, pour décider.</li>
</ul>

<h2>Prérequis</h2>
<p>La base d'audit doit être active, idéalement depuis au moins 12 mois. Si elle ne l'est pas, l'activer maintenant reste utile : quelques mois de données suffisent déjà à repérer une bonne partie de ce qui n'est plus ouvert.</p>
<p>Le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> couvre ces six volets à prix fixe, en 10 jours ouvrés.</p>
""",
 faqs=[
  ("Combien de temps dure un audit SAP BusinessObjects ?", "Cela dépend de la taille de la plateforme. Le Diagnostic Sortie BO de Trivoie est livré en 10 jours ouvrés, à prix fixe."),
  ("Faut-il un accès administrateur pour auditer BusinessObjects ?", "Un accès en lecture au référentiel (Query Builder, CMC) et à la base d'audit suffit pour l'essentiel. Aucune modification de la plateforme n'est nécessaire."),
  ("Que faire si la base d'audit n'est pas activée ?", "L'activer dès maintenant. Sans historique, l'usage réel ne peut pas être mesuré, mais l'inventaire et les risques restent analysables."),
 ],
 related=["diagnostic-sortie-businessobjects", "nettoyer-parc-businessobjects-documents-inutilises", "compter-documents-sap-businessobjects-query-builder", "consultant-sap-businessobjects"],
)
