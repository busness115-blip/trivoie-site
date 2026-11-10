PAGE = dict(
 slug="sap-businessobjects-bi-2027",
 title="SAP BusinessObjects BI 2027 : date de sortie et maintenance",
 desc="SAP BusinessObjects BI 2027 est attendu au premier trimestre 2027 : dates connues, maintenance, rythme des versions, impact pour la 4.3 et BI 2025.",
 h1="SAP BusinessObjects BI 2027 : ce que l'on sait de la prochaine version",
 lead="Après BI 2025, SAP prépare BI 2027. Voici les dates publiées à ce jour, ce qu'elles impliquent pour une plateforme encore en 4.3, et pourquoi ce rythme change le calcul entre rester chez SAP et migrer.",
 published="2026-11-10", modified="2026-11-10",
 body="""
<h2>Les dates publiées</h2>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Version</th><th>Sortie</th><th>Fin de la maintenance standard</th></tr></thead>
<tbody>
<tr><td>BI 4.3</td><td>Disponible</td><td>31 décembre 2026</td></tr>
<tr><td>BI 2025</td><td>Mars 2025 (Wiiisdom)</td><td>31 décembre 2027</td></tr>
<tr><td>BI 2027</td><td>Premier trimestre 2027 (Wiiisdom), début 2027 (Dallas Marks)</td><td>Quatrième trimestre 2029, selon Wiiisdom</td></tr>
<tr><td>BI 2029</td><td>Annoncée par Wiiisdom, sans date de sortie précise</td><td>Quatrième trimestre 2031, selon Wiiisdom</td></tr>
</tbody></table></div>
<p>Dallas Marks signale aussi une note SAP (3758205) publiée le 1er juin 2026, qui mentionne explicitement la future version 2027. Les dates de fin de maintenance de BI 2027 et BI 2029 ne sont publiées, à notre connaissance, que par Wiiisdom : nous les citons en leur attribuant la source.</p>

<h2>Ce que cela change</h2>
<p>BusinessObjects suit désormais un rythme d'une version environ tous les deux ans, chacune avec environ deux ans de maintenance standard. Rester chez SAP n'est donc pas une montée de version unique : c'est un cycle, avec à chaque fois une installation, une recette et des tests de non-régression.</p>
<ul>
<li><strong>Vous êtes en 4.3</strong> : la maintenance standard s'arrête le 31 décembre 2026. Les univers UNV ne sont plus pris en charge après la 4.3, ils doivent être convertis en UNX avant de monter (<a href="/convertir-univers-unv-en-unx/">méthode</a>).</li>
<li><strong>Vous visez BI 2025</strong> : vous gagnez un an de maintenance standard, puis une nouvelle montée vers BI 2027 sera à prévoir pour rester couvert.</li>
<li><strong>Vous hésitez avec une migration</strong> : le coût à comparer n'est pas une montée de version, mais la somme des montées de version sur l'horizon que vous visez.</li>
</ul>

<h2>Ce qui n'est pas encore connu</h2>
<p>Les chemins de montée de version vers BI 2027 (par exemple depuis la 4.3 directement) et la liste exacte des composants ne sont pas publiés de façon détaillée à ce jour. Vérifiez-les dans la Product Availability Matrix de SAP avant de planifier.</p>
<p>Sources : <a href="https://wiiisdom.com/fr/blog/sap-bi-dates-de-fin-de-vie/" rel="noopener">dates de fin de vie SAP BI (Wiiisdom)</a>, <a href="https://dallasmarks.com/toy-story-5-and-bi-2027/" rel="noopener">annonce de BI 2027 (Dallas Marks)</a>.</p>
""",
 faqs=[
  ("Quand sort SAP BusinessObjects BI 2027 ?", "BI 2027 est attendu au premier trimestre 2027 selon Wiiisdom, et au début de l'année 2027 selon Dallas Marks."),
  ("Jusqu'à quand BI 2027 sera-t-il maintenu ?", "Selon Wiiisdom, la maintenance standard de BI 2027 irait jusqu'au quatrième trimestre 2029."),
  ("Peut-on passer directement de la 4.3 à BI 2027 ?", "Les chemins de montée de version vers BI 2027 ne sont pas encore publiés de façon détaillée. Il faut les vérifier dans la Product Availability Matrix de SAP."),
  ("Les univers UNV fonctionneront-ils en BI 2027 ?", "Non. Les univers UNV ne sont plus pris en charge après la 4.3 : ils doivent être convertis en UNX avant de monter de version."),
 ],
 related=["bi-2025-ou-sortir-de-businessobjects", "fin-maintenance-sap-businessobjects-4-3", "convertir-univers-unv-en-unx", "migration-businessobjects-power-bi"],
)
