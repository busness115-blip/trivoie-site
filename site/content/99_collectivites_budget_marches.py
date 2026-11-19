PAGE = dict(
 slug="collectivites-budget-marches-publics-fin-maintenance-businessobjects",
 nav="Collectivités : budget et marchés",
 title="Collectivités : budget et marchés pour BusinessObjects",
 desc="Calendrier budgétaire local, règles avant le vote du budget et seuils de marchés publics 2026 : organiser le traitement de la fin de maintenance de la 4.3.",
 h1="Collectivités et secteur public : calendrier budgétaire et marchés publics pour traiter la fin de maintenance de BusinessObjects",
 lead="Pour une collectivité ou un établissement public sous SAP BusinessObjects 4.3, la fin de maintenance standard du 31 décembre 2026 tombe à un moment particulier : le budget 2027 est en cours d'exécution ou en préparation, et la forme de l'achat dépend de seuils qui ont changé en 2026. Ce guide rapproche le calendrier budgétaire local, les règles applicables avant le vote du budget et les seuils de la commande publique. Il ne constitue pas un avis juridique : votre service des finances ou des marchés reste juge de la procédure applicable.",
 published="2026-11-19", modified="2026-11-19",
 body="""
<h2>Ce qui arrive le 31 décembre 2026</h2>
<p>Selon <a href="https://wiiisdom.com/blog/sap-bi-end-of-life-stages/" rel="noopener">Wiiisdom</a> et <a href="https://nttdata-solutions.com/uk/blog/preparing-for-the-end-of-life-of-sap-businessobjects-4-3-what-should-your-business-do/" rel="noopener">NTT DATA</a>, la maintenance standard de SAP BusinessObjects BI 4.3 se termine le 31 décembre 2026. La suite (maintenance spécifique client, correctifs de sécurité) est détaillée dans notre guide sur la <a href="/maintenance-specifique-client-sap-businessobjects/">maintenance spécifique client</a> et sur le <a href="/calendrier-fin-maintenance-sap-businessobjects-versions/">calendrier des versions</a>. Rester sur la plateforme SAP, passer à BI 2025 ou migrer vers une autre solution sont trois choix légitimes ; la question est de les chiffrer à temps pour le budget.</p>

<h2>Le calendrier budgétaire d'une collectivité</h2>
<p>Le site <a href="https://www.info.gouv.fr/actualite/comment-fonctionne-le-budget-dune-collectivite-territoriale" rel="noopener">info.gouv.fr</a> et <a href="https://www.maire-info.com/budgets-primitifs/budget-primitif-et-debat-dorientation-avant-ou-apres-les-municipales-article-23754" rel="noopener">Maire-info</a> rappellent les mêmes règles :</p>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Étape</th><th>Règle</th><th>Conséquence pour un projet BI</th></tr></thead>
<tbody>
<tr><td>Débat d'orientation budgétaire</td><td>Il doit avoir lieu dans les deux mois qui précèdent le vote du budget. Les communes de moins de 3 500 habitants n'y sont pas tenues</td><td>Le besoin BI doit être connu et chiffré avant ce débat pour y figurer</td></tr>
<tr><td>Vote du budget primitif</td><td>La loi accorde un délai jusqu'au 15 avril, porté au 30 avril les années de renouvellement de l'assemblée</td><td>Un crédit non voté en début d'année peut attendre le printemps</td></tr>
</tbody></table></div>
<p>Pour 2027, la fenêtre de décision est donc courte : le calendrier de la maintenance ne suit pas celui du budget. Si votre budget 2027 est déjà voté, une décision modificative ou une réaffectation de crédits peut être nécessaire ; la forme dépend de votre règlement budgétaire et de votre comptable public.</p>

<h2>Engager une dépense avant le vote du budget</h2>
<p>D'après <a href="https://www.maire-info.com/budgets-primitifs/budget-primitif-et-debat-dorientation-avant-ou-apres-les-municipales-article-23754" rel="noopener">Maire-info</a>, qui s'appuie sur une note de l'Association des maires de France, si le budget n'est pas adopté avant le 1er janvier, l'exécutif peut mandater les dépenses de fonctionnement dans la limite de celles inscrites au budget de l'année précédente. Pour l'investissement, il peut, avec l'autorisation de l'assemblée, engager des dépenses dans la limite du quart des crédits ouverts l'année précédente, hors remboursement de la dette, la délibération précisant le montant et l'affectation. La nature de la dépense (fonctionnement ou investissement) relève de votre comptable public.</p>

<h2>Les seuils de la commande publique en 2026</h2>
<p>D'après <a href="https://entreprendre.service-public.gouv.fr/actualites/A18673" rel="noopener">service-public.gouv.fr</a> et <a href="https://expertisemarchespublics.fr/2026/04/05/seuils-marches-publics-2026/" rel="noopener">Expertise Marchés Publics 360°</a>, pour les fournitures et services :</p>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 2 (défilement horizontal)"><table>
<thead><tr><th>Montant estimé (HT)</th><th>Règle</th></tr></thead>
<tbody>
<tr><td>Moins de 60 000 €</td><td>Dispense de publicité et de mise en concurrence préalables, depuis le 1er avril 2026 (le seuil était de 40 000 € auparavant)</td></tr>
<tr><td>À partir de 90 000 €</td><td>Publicité obligatoire au BOAMP ou dans un support habilité</td></tr>
<tr><td>216 000 € pour les collectivités et autres acheteurs</td><td>Seuil de procédure formalisée pour 2026 et 2027</td></tr>
</tbody></table></div>
<p>Ces seuils concernent la valeur estimée du marché et ne dispensent pas du respect des principes de la commande publique : choix d'une offre pertinente, bonne utilisation des deniers publics, traçabilité. Notre page sur le <a href="/diagnostic-businessobjects-secteur-public-marche-60000-euros/">seuil de 60 000 €</a> applique ce cadre à un diagnostic. Les établissements de santé suivent une procédure budgétaire propre ; leur service financier et leur ARS précisent les échéances qui les concernent.</p>

<h2>Organiser la décision en quatre temps</h2>
<ol>
<li>Faire l'inventaire de l'usage réel de la plateforme (documents consultés, univers, utilisateurs). Voir le <a href="/nettoyer-parc-businessobjects-documents-inutilises/">nettoyage du parc</a>.</li>
<li>Chiffrer au moins trois options : rester sous maintenance spécifique, passer à BI 2025, migrer. Voir <a href="/bi-2025-ou-sortir-de-businessobjects/">BI 2025 ou sortie</a>.</li>
<li>Présenter ces options avant le débat d'orientation budgétaire.</li>
<li>Choisir la forme d'achat selon le montant estimé et l'avis du service des marchés.</li>
</ol>
<p>AM DATA n'est revendeur ni de SAP ni de Microsoft : le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> compare ces options sans position d'éditeur.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://wiiisdom.com/blog/sap-bi-end-of-life-stages/" rel="noopener">Wiiisdom : étapes de fin de vie de SAP BI</a></li>
<li><a href="https://nttdata-solutions.com/uk/blog/preparing-for-the-end-of-life-of-sap-businessobjects-4-3-what-should-your-business-do/" rel="noopener">NTT DATA : préparer la fin de vie de BusinessObjects 4.3</a></li>
<li><a href="https://www.info.gouv.fr/actualite/comment-fonctionne-le-budget-dune-collectivite-territoriale" rel="noopener">info.gouv.fr : comment fonctionne le budget d'une collectivité territoriale</a></li>
<li><a href="https://www.maire-info.com/budgets-primitifs/budget-primitif-et-debat-dorientation-avant-ou-apres-les-municipales-article-23754" rel="noopener">Maire-info : budget primitif et débat d'orientation</a></li>
<li><a href="https://entreprendre.service-public.gouv.fr/actualites/A18673" rel="noopener">service-public.gouv.fr : nouveaux seuils des marchés publics</a></li>
<li><a href="https://expertisemarchespublics.fr/2026/04/05/seuils-marches-publics-2026/" rel="noopener">Expertise Marchés Publics 360° : seuils 2026</a></li>
</ul>
""",
 faqs=[
  ("Quand une collectivité doit-elle voter son budget ?", "La loi accorde un délai jusqu'au 15 avril, porté au 30 avril les années de renouvellement de l'assemblée (info.gouv.fr, Maire-info)."),
  ("Faut-il un débat d'orientation budgétaire avant le vote ?", "Oui, dans les deux mois qui précèdent le vote, sauf pour les communes de moins de 3 500 habitants (info.gouv.fr, Maire-info)."),
  ("Peut-on acheter un diagnostic sans mise en concurrence ?", "Depuis le 1er avril 2026, les fournitures et services de moins de 60 000 € HT peuvent être achetés sans publicité ni mise en concurrence préalables, dans le respect des principes de la commande publique (service-public.gouv.fr)."),
  ("À partir de quel montant la publicité est-elle obligatoire ?", "À partir de 90 000 € HT pour les fournitures et services, au BOAMP ou dans un support habilité (service-public.gouv.fr, Expertise Marchés Publics 360°)."),
 ],
 related=["diagnostic-businessobjects-secteur-public-marche-60000-euros", "maintenance-specifique-client-sap-businessobjects", "checklist-migration-sap-businessobjects", "bi-2025-ou-sortir-de-businessobjects"],
)
