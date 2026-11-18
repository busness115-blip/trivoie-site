PAGE = dict(
 slug="rgpd-plateforme-bi-donnees-personnelles-businessobjects",
 nav="RGPD et plateforme BI",
 title="RGPD et plateforme BI : données personnelles",
 desc="Données personnelles dans les rapports BusinessObjects : conservation, sécurité, registre et contrat de sous-traitance à vérifier avant une migration.",
 h1="RGPD et plateforme BI : données personnelles dans les rapports BusinessObjects et sous-traitance",
 lead="Une plateforme BI contient souvent des noms, des matricules ou des adresses dans des rapports, des univers et des exports planifiés. Un projet de montée de version ou de migration est le bon moment pour vérifier ce que le RGPD demande : durée de conservation, sécurité, registre des traitements et contrat avec le prestataire. Ce guide s'appuie sur le texte du règlement et sur les pages de la CNIL. Il ne constitue pas un avis juridique.",
 published="2026-11-18", modified="2026-11-18",
 body="""
<h2>Pourquoi le sujet se pose dans un projet BI</h2>
<p>Le RGPD s'applique dès qu'un rapport, un export ou une table contient des données permettant d'identifier une personne. Dans une plateforme BI, cela peut concerner des listes de clients, d'agents, de patients ou de salariés. Le projet de fin de maintenance de la 4.3 (31 décembre 2026) oblige à inventorier ces contenus, et cet inventaire sert aussi à la conformité. Notre guide sur le <a href="/nettoyer-parc-businessobjects-documents-inutilises/">nettoyage du parc</a> décrit le tri des documents inutilisés.</p>

<h2>Quatre points du règlement à rapprocher de votre parc</h2>
<div class="tbl" tabindex="0" role="region" aria-label="Tableau 1 (défilement horizontal)"><table>
<thead><tr><th>Sujet</th><th>Ce que dit le règlement ou la CNIL</th><th>Question à poser sur la plateforme BI</th></tr></thead>
<tbody>
<tr><td>Minimisation (article 5, 1, c)</td><td>Les données doivent être adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités</td><td>Un rapport a-t-il besoin du nom complet, ou un identifiant suffit-il ?</td></tr>
<tr><td>Conservation (article 5, 1, e)</td><td>Les données ne permettent l'identification des personnes que pendant la durée nécessaire aux finalités. La CNIL ajoute que la durée se détermine à partir de la finalité, sauf texte qui en impose une</td><td>Les instances de rapports et exports anciens sont-ils encore utiles ?</td></tr>
<tr><td>Sécurité (article 32)</td><td>Mesures adaptées au risque ; pseudonymisation et chiffrement cités parmi celles à envisager ; procédure de test régulier de leur efficacité</td><td>Qui accède à quels rapports ? Voir les <a href="/securite-plateforme-bi-droits-comptes-audit-businessobjects/">droits et comptes</a></td></tr>
<tr><td>Registre (article 30)</td><td>Le responsable de traitement tient un registre écrit : finalités, catégories de personnes et de données, destinataires, délais d'effacement et mesures de sécurité si possible. Dispense possible sous 250 personnes, avec exceptions (traitement non occasionnel, risque, données sensibles)</td><td>Les traitements alimentant la BI figurent-ils au registre ?</td></tr>
</tbody></table></div>
<p>La CNIL précise aussi qu'une même donnée peut servir à plusieurs traitements avec des durées différentes : supprimer un rapport n'efface pas la donnée du système source.</p>

<h2>Le prestataire est un sous-traitant</h2>
<p>Si un prestataire accède à votre plateforme pendant un diagnostic, une migration ou une maintenance, il traite potentiellement des données personnelles pour votre compte. L'article 28 prévoit alors :</p>
<ul>
<li>le choix d'un sous-traitant présentant des garanties suffisantes ;</li>
<li>un contrat écrit qui précise l'objet, la durée, la nature et la finalité du traitement, les types de données et les catégories de personnes ;</li>
<li>un traitement sur instruction documentée du responsable, et un engagement de confidentialité des personnes autorisées ;</li>
<li>une autorisation écrite préalable pour tout sous-traitant ultérieur, le sous-traitant initial restant responsable envers vous ;</li>
<li>au terme de la prestation, selon votre choix, la suppression ou la restitution des données et la destruction des copies, sauf obligation légale de conservation ;</li>
<li>la mise à disposition des informations nécessaires pour démontrer la conformité, et la possibilité d'audits.</li>
</ul>
<p>La CNIL recommande de signer ce contrat avant le début des travaux. Elle indique que les clauses contractuelles types publiées par la Commission européenne le 4 juin 2021 peuvent servir de base, sans être obligatoires si le contrat contient déjà les éléments de l'article 28. Voir aussi nos <a href="/questions-a-poser-prestataire-migration-businessobjects/">questions à poser à un prestataire de migration</a>.</p>

<h2>Organiser la vérification en cinq étapes</h2>
<ol>
<li>Repérer les rapports, univers et exports qui contiennent des données identifiantes.</li>
<li>Pour chacun, noter la finalité, le public autorisé et la durée de conservation utile.</li>
<li>Rapprocher cette liste du registre des traitements et corriger les écarts.</li>
<li>Avant tout accès d'un prestataire, signer le contrat de sous-traitance et définir ce qui lui est accessible.</li>
<li>Prévoir la suppression ou la restitution des données de test en fin de projet.</li>
</ol>
<p>Ces étapes valent que vous restiez sur la plateforme SAP ou que vous migriez vers une autre cible. Elles s'intègrent à la <a href="/checklist-migration-sap-businessobjects/">checklist de migration</a>. AM DATA n'est revendeur ni de SAP ni de Microsoft. Le <a href="/diagnostic-sortie-businessobjects/">Diagnostic Sortie BO</a> inclut l'inventaire du parc ; la qualification juridique d'un traitement relève de votre délégué à la protection des données ou de votre conseil.</p>

<h2>Sources</h2>
<ul>
<li><a href="https://gdpr-text.com/fr/read/article-28" rel="noopener">Article 28 du RGPD, sous-traitant (texte du règlement)</a></li>
<li><a href="https://gdpr-text.com/fr/read/article-32" rel="noopener">Article 32 du RGPD, sécurité du traitement (texte du règlement)</a></li>
<li><a href="https://gdpr-text.com/pt/read/article-5" rel="noopener">Article 5 du RGPD, principes (texte du règlement)</a></li>
<li><a href="https://gdpr-text.com/fr/read/article-30" rel="noopener">Article 30 du RGPD, registre des activités de traitement (texte du règlement)</a></li>
<li><a href="https://www.cnil.fr/limiter-la-conservation-des-donnees" rel="noopener">Les durées de conservation des données (CNIL)</a></li>
<li><a href="https://cnil.fr/fr/node/278" rel="noopener">Clauses contractuelles types entre responsable de traitement et sous-traitant (CNIL)</a></li>
<li><a href="https://cnil.fr/fr/node/1430" rel="noopener">Sécurité : gérer la sous-traitance (CNIL)</a></li>
</ul>
""",
 faqs=[
  ("Un rapport BI avec des noms de personnes relève-t-il du RGPD ?", "Oui dès qu'il permet d'identifier une personne. Le règlement demande alors que les données soient limitées à ce qui est nécessaire aux finalités (article 5) et protégées par des mesures adaptées au risque (article 32)."),
  ("Combien de temps conserver les rapports et exports contenant des données personnelles ?", "Il n'existe pas de durée unique. La CNIL indique que la durée se détermine à partir de la finalité du traitement, sauf lorsqu'un texte impose une durée."),
  ("Un prestataire de migration doit-il signer un contrat de sous-traitance ?", "Si ses travaux impliquent un traitement de données personnelles pour votre compte, l'article 28 exige un contrat écrit. La CNIL recommande de le signer avant le début des travaux."),
  ("Les clauses contractuelles types de la Commission sont-elles obligatoires ?", "Non. D'après la CNIL, elles servent de support mais ne sont pas requises si le contrat contient déjà les éléments de l'article 28."),
  ("Mon organisation de moins de 250 personnes doit-elle tenir un registre ?", "L'article 30 prévoit une dispense sous 250 personnes, qui ne joue pas si le traitement n'est pas occasionnel, présente un risque pour les droits des personnes ou porte sur des données sensibles."),
 ],
 related=["securite-plateforme-bi-droits-comptes-audit-businessobjects", "nettoyer-parc-businessobjects-documents-inutilises", "questions-a-poser-prestataire-migration-businessobjects", "checklist-migration-sap-businessobjects"],
)
