& {
# Trivoie : collecte des volumes d'une plateforme SAP BusinessObjects (BI 4.2 SP03 et versions ultérieures)
#
# Utilisation : copiez tout ce bloc, collez-le dans une fenêtre PowerShell, appuyez sur Entrée,
# puis répondez aux trois questions. Rien à installer, aucun fichier à enregistrer.
#
# Ce que fait le script : il interroge le référentiel CMS par l'API REST officielle (/biprws),
# en lecture seule. Il ne compte que des objets par type. Aucun nom de document, d'utilisateur,
# de dossier ou de serveur n'est exporté. Le fichier produit reste sur votre poste.
#
# Prérequis : l'application « RESTful Web Services » autorisée pour le compte dans la CMC.
# Les chiffres dépendent des droits du compte : un compte administrateur voit tout.

$ErrorActionPreference = "Stop"
$TaillePage = 1000
$VersionScript = "2"
try { [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12 } catch { }

function Ecrire-Erreur([string]$texte) { Write-Host ""; Write-Host $texte -ForegroundColor Red; Write-Host "" }

Write-Host ""
Write-Host "Trivoie : collecte des volumes de votre plateforme BusinessObjects" -ForegroundColor Cyan
Write-Host "Lecture seule. Seuls des nombres sont enregistrés."
Write-Host ""

# 1. Adresse du serveur (acceptée sous forme de nom simple, de nom:port ou d'adresse complète)
$saisie = Read-Host "1/3  Nom ou adresse du serveur BusinessObjects (Entrée = localhost)"
if ([string]::IsNullOrWhiteSpace($saisie)) { $saisie = "localhost" }
$saisie = $saisie.Trim().TrimEnd("/")
if ($saisie -notmatch "^https?://") {
  if ($saisie -notmatch ":\d+") { $saisie = "$($saisie):6405" }
  $saisie = "http://$saisie"
}
if ($saisie -notmatch "/biprws$") { $saisie = "$saisie/biprws" }
$Serveur = $saisie
Write-Host "     Adresse utilisée : $Serveur" -ForegroundColor DarkGray

# 2. Compte et type d'authentification
$Utilisateur = Read-Host "2/3  Compte BusinessObjects (Entrée = Administrator)"
if ([string]::IsNullOrWhiteSpace($Utilisateur)) { $Utilisateur = "Administrator" }
$choix = Read-Host "     Type de compte : 1 = Enterprise, 2 = LDAP, 3 = Windows AD (Entrée = 1)"
$Authentification = switch ($choix) { "2" { "secLDAP" } "3" { "secWinAD" } default { "secEnterprise" } }

# 3. Mot de passe (masqué, jamais enregistré)
$motDePasseSecurise = Read-Host -AsSecureString "3/3  Mot de passe"
$bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($motDePasseSecurise)
try { $motDePasse = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr) }
finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr) }

function Echapper([string]$texte) { [System.Security.SecurityElement]::Escape($texte) }

$corpsConnexion = @"
<attrs xmlns="http://www.sap.com/rws/bip">
  <attr name="userName" type="string">$(Echapper $Utilisateur)</attr>
  <attr name="password" type="string">$(Echapper $motDePasse)</attr>
  <attr name="auth" type="string">$Authentification</attr>
</attrs>
"@

$jeton = $null
try {
  Write-Host ""
  Write-Host "Connexion..."
  try {
    $reponse = Invoke-WebRequest -Uri "$Serveur/logon/long" -Method Post -Body $corpsConnexion `
      -ContentType "application/xml" -Headers @{ Accept = "application/xml" } -UseBasicParsing
  }
  catch {
    $detail = $_.Exception.Message
    $conseil = "Vérifiez le nom du serveur, le port de l'API REST (souvent 6405), le compte, le mot de passe et le type de compte."
    if ($detail -match "401|403") { $conseil = "Compte ou mot de passe refusé, ou application RESTful Web Services non autorisée pour ce compte dans la CMC." }
    elseif ($detail -match "SSL|TLS|certificat|certificate|trust") { $conseil = "Le certificat HTTPS du serveur n'est pas reconnu par ce poste. Essayez l'adresse en http, ou lancez le script depuis le serveur BusinessObjects lui-même." }
    elseif ($detail -match "resolve|résoudre|connect|connexion|refused|refusée|timed out|délai") { $conseil = "Serveur injoignable depuis ce poste. Vérifiez le nom du serveur et le port de l'API REST (souvent 6405), ou lancez le script depuis le serveur BusinessObjects lui-même." }
    throw "Connexion impossible à $Serveur. $conseil Détail technique : $detail"
  }
  finally { $motDePasse = $null }
  $jeton = @($reponse.Headers["X-SAP-LogonToken"])[0]
  if (-not $jeton) { throw "Connexion refusée : aucun jeton reçu. Vérifiez l'adresse du serveur et le compte." }
  $entetes = @{ "X-SAP-LogonToken" = $jeton; Accept = "application/json" }
  Write-Host "Connecté." -ForegroundColor Green

  function Interroger([string]$requete, [int]$page, [int]$taille = $TaillePage) {
    $corps = @{ query = $requete } | ConvertTo-Json -Compress
    Invoke-RestMethod -Uri "$Serveur/v1/cmsquery?page=$page&pagesize=$taille" `
      -Method Post -Headers $entetes -ContentType "application/json; charset=utf-8" -Body $corps
  }

  # COUNT(SI_ID) renvoie un seul objet portant SI_AGGREGATE_COUNT (voir les requêtes Query Builder de la communauté).
  # La forme exacte de la réponse JSON pouvant varier, la lecture est tolérante ; en cas de doute, on renvoie $null.
  function Compter([string]$table, [string]$condition) {
    $requete = "SELECT COUNT(SI_ID) FROM $table"
    if ($condition) { $requete += " WHERE $condition" }
    try { $resultat = Interroger $requete 1 } catch { return $null }
    $ligne = @($resultat.entries)[0]
    if (-not $ligne) { return $null }
    foreach ($p in $ligne.PSObject.Properties) {
      if ($p.Name -like "SI_AGGREGATE_COUNT*") {
        $valeurs = @()
        if ($p.Value -is [System.Management.Automation.PSCustomObject]) { $valeurs = @($p.Value.PSObject.Properties | ForEach-Object { $_.Value }) }
        else { $valeurs = @($p.Value) }
        foreach ($v in $valeurs) { $n = [int64]0; if ([int64]::TryParse([string]$v, [ref]$n)) { return $n } }
      }
    }
    return $null
  }

  # Liste les objets avec TOP N pour lever la limite implicite de 1 000 lignes, page par page.
  # On s'arrête quand une page n'apporte plus aucun identifiant nouveau : cela protège contre
  # une taille de page plafonnée par le serveur et contre une pagination ignorée.
  function Lister([string]$table, [string]$condition, $attendu, [int]$taille = $TaillePage) {
    $top = 100000000
    if ($null -ne $attendu) { $top = [Math]::Max([int64]$attendu, 1) }
    $requete = "SELECT TOP $top SI_ID, SI_KIND FROM $table"
    if ($condition) { $requete += " WHERE $condition" }
    $vus = New-Object "System.Collections.Generic.HashSet[string]"
    $parType = @{}
    $page = 1
    while ($true) {
      $lignes = @((Interroger $requete $page $taille).entries)
      $nouveaux = 0
      foreach ($l in $lignes) {
        if ($vus.Add([string]$l.SI_ID)) {
          $nouveaux++
          $type = [string]$l.SI_KIND
          if ($type) { if ($parType.ContainsKey($type)) { $parType[$type]++ } else { $parType[$type] = 1 } }
        }
      }
      if ($lignes.Count -eq 0 -or $nouveaux -eq 0) { break }
      $page++
      if ($page -gt 100000) { throw "Nombre de pages anormal : collecte interrompue." }
    }
    return @{ parType = $parType; total = $vus.Count }
  }

  function Compter-Sur([string]$table, [string]$condition) {
    $n = Compter $table $condition
    if ($null -ne $n) { return @{ valeur = $n; methode = "count" } }
    return @{ valeur = (Lister $table $condition $null).total; methode = "liste" }
  }

  Write-Host "Comptage des documents (peut prendre une à deux minutes sur une grosse plateforme)..."
  $totalDocuments = Compter "CI_INFOOBJECTS" "SI_INSTANCE = 0"
  $liste = if ($totalDocuments -eq 0) { @{ parType = @{}; total = 0 } } else { Lister "CI_INFOOBJECTS" "SI_INSTANCE = 0" $totalDocuments }
  if ($null -ne $totalDocuments -and $totalDocuments -ne $liste.total) {
    # Pagination non respectée par ce serveur : on redemande tout en une seule page.
    $liste = Lister "CI_INFOOBJECTS" "SI_INSTANCE = 0" $totalDocuments ([int][Math]::Max($totalDocuments, 1))
  }
  $coherent = ($null -eq $totalDocuments) -or ($totalDocuments -eq $liste.total)

  Write-Host "Comptage des univers..."
  $unv = Compter-Sur "CI_APPOBJECTS" "SI_KIND = 'Universe'"
  $unx = Compter-Sur "CI_APPOBJECTS" "SI_KIND = 'DSL.MetaDataFile'"

  Write-Host "Comptage des utilisateurs..."
  $utilisateurs = Compter-Sur "CI_SYSTEMOBJECTS" "SI_KIND = 'User'"
  $depuis = (Get-Date).AddDays(-365).ToString("yyyy.MM.dd") + ".00.00.00"
  $actifs = Compter "CI_SYSTEMOBJECTS" "SI_KIND = 'User' AND SI_LASTLOGONTIME >= '$depuis'"

  Write-Host "Comptage des planifications récurrentes..."
  $recurrentes = Compter-Sur "CI_INFOOBJECTS" "SI_RECURRING = 1"

  $tri = [ordered]@{}
  foreach ($k in ($liste.parType.Keys | Sort-Object)) { $tri[$k] = $liste.parType[$k] }

  $fichier = [ordered]@{
    format = "trivoie-scan/2"
    script = $VersionScript
    genere = (Get-Date).ToString("s")
    documents = [ordered]@{
      parType = $tri
      totalListe = $liste.total
      totalCompte = $totalDocuments
      coherent = $coherent
    }
    universUnv = $unv.valeur
    universUnx = $unx.valeur
    utilisateurs = $utilisateurs.valeur
    utilisateursActifs12Mois = $actifs
    planificationsRecurrentes = $recurrentes.valeur
    methodes = [ordered]@{ univers = $unv.methode; utilisateurs = $utilisateurs.methode; planifications = $recurrentes.methode }
  }

  $dossier = [Environment]::GetFolderPath("Desktop")
  if (-not $dossier -or -not (Test-Path $dossier)) { $dossier = (Get-Location).Path }
  $chemin = Join-Path $dossier "trivoie-scan.json"
  $fichier | ConvertTo-Json -Depth 6 | Out-File -FilePath $chemin -Encoding utf8

  Write-Host ""
  Write-Host "Terminé." -ForegroundColor Green
  Write-Host ("  Objets du référentiel (hors instances) : {0}" -f $liste.total)
  Write-Host ("  Univers UNV : {0}   Univers UNX : {1}" -f $unv.valeur, $unx.valeur)
  Write-Host ("  Utilisateurs : {0}   dont connectés depuis 12 mois : {1}" -f $utilisateurs.valeur, $(if ($null -eq $actifs) { "non mesuré" } else { $actifs }))
  Write-Host ("  Planifications récurrentes : {0}" -f $recurrentes.valeur)
  if (-not $coherent) {
    Write-Host ("  Attention : le total compté ({0}) diffère du total listé ({1}). Signalez-le à Trivoie." -f $totalDocuments, $liste.total) -ForegroundColor Yellow
  }
  Write-Host ""
  Write-Host "Fichier créé : $chemin" -ForegroundColor Cyan
  Write-Host "Déposez-le sur la page du scan Trivoie, onglet « Collecte automatique »."
  try { Start-Process explorer.exe -ArgumentList "/select,`"$chemin`"" } catch { }
}
catch {
  Ecrire-Erreur ([string]$_.Exception.Message -replace "^Exception calling .*?: ", "")
}
finally {
  if ($jeton) {
    try { Invoke-WebRequest -Uri "$Serveur/logoff" -Method Post -Headers @{ "X-SAP-LogonToken" = $jeton } -UseBasicParsing | Out-Null } catch { }
  }
}
}
