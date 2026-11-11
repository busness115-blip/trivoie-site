/* Trivoie : moteur d'analyse du scan. Fonctions pures, aucun accès réseau. */
(function (root) {
  "use strict";

  var SOURCES = {
    csm: {
      label: "notes SAP 3486924 et 3763590, résumées par C. Vosloo",
      url: "https://clintvosloo.com/sap-customer-specific-maintenance-bi-43-ds-43-what-it-means"
    },
    eol: {
      label: "Dates de fin de maintenance SAP BI (Wiiisdom)",
      url: "https://wiiisdom.com/blog/sap-bi-end-of-life-stages/"
    },
    bi2025: {
      label: "SAP BusinessObjects BI 2025 : composants et univers (Wiiisdom)",
      url: "https://wiiisdom.com/blog/sap-businessobjects-bi-2025/"
    },
    pam: {
      label: "Product Availability Matrix SAP (portail SAP)",
      url: "https://support.sap.com/en/release-upgrade-maintenance.html"
    },
    deprecated: {
      label: "Notes SAP 2801797 et 2914654 : contenus obsolètes depuis BI 4.2 SP09 et 4.3 (Dallas Marks)",
      url: "https://dallasmarks.com/getting-ready-for-sap-businessobjects-4-3-support-pack-4/"
    },
    method: { label: "calcul sur vos chiffres (règle détaillée plus bas)", url: "#methode" }
  };

  /* Codes SI_KIND relevés dans les requêtes Query Builder publiées par la communauté SAP BO. */
  var DOC_KINDS = {
    Webi: "webi",
    CrystalReport: "crystal",
    MDAnalysis: "analysis", Analysis: "analysis", "AAD.AnalysisWorkspace": "analysis",
    "XL.XcelsiusEnterprise": "dashboards", Xcelsius: "dashboards", "XL.XcelsiusApplication": "dashboards",
    "AAD.AnalysisApplication": "lumira", VISILums: "lumira",
    FullClient: "legacy", FullClientTemplate: "legacy", FullClientAddin: "legacy",
    DataDiscovery: "legacy", DataDiscoveryAlbum: "legacy", Flash: "legacy", "XL.Query": "legacy"
  };
  var NON_DOC_KINDS = [
    "Folder", "FavoritesFolder", "Inbox", "PersonalCategory", "Category",
    "Shortcut", "Hyperlink", "Publication", "ObjectPackage", "Program",
    "AFDashboardPage", "MyInfoView", "Event", "Calendar"
  ];

  function toInt(v) {
    if (v === null || v === undefined || v === "") return null;
    var n = Number(String(v).replace(/\s/g, "").replace(",", "."));
    if (!isFinite(n) || n < 0) return NaN;
    return Math.round(n);
  }

  function validate(raw) {
    var errors = {};
    var data = {};
    var intFields = ["webi", "crystal", "analysis", "dashboards", "lumira", "legacy", "otherDocs",
      "unv", "unx", "users", "schedules"];
    intFields.forEach(function (f) {
      var n = toInt(raw[f]);
      if (n !== null && isNaN(n)) errors[f] = "Entrez un nombre entier positif.";
      data[f] = n === null || isNaN(n) ? 0 : n;
    });
    var act = toInt(raw.activeUsers);
    if (act !== null && isNaN(act)) errors.activeUsers = "Entrez un nombre entier positif.";
    else if (act !== null && act > data.users) errors.activeUsers = "Ne peut pas dépasser le nombre d'utilisateurs.";
    data.activeUsers = act === null || isNaN(act) || act > data.users ? null : act;
    data.version = raw.version || "4.3";
    data.auditActive = raw.auditActive === true || raw.auditActive === "oui";
    /* Documents non ouverts depuis 12 mois (nombre), lus dans la base d'audit.
       Vide = 0 : « je n'en ai pas identifié » donne exactement le même résultat que 0. */
    var unusedN = toInt(raw.unusedDocs);
    var totalForCap = totalDocs(data);
    data.unusedDocs = 0;
    if (data.auditActive && unusedN !== null) {
      if (isNaN(unusedN)) errors.unusedDocs = "Entrez un nombre entier positif.";
      else if (unusedN > totalForCap) errors.unusedDocs = "Ne peut pas dépasser le nombre total de documents (" + totalForCap.toLocaleString("fr-FR") + ").";
      else data.unusedDocs = unusedN;
    }
    return { data: data, errors: errors, valid: Object.keys(errors).length === 0 };
  }

  function totalDocs(d) {
    return d.webi + d.crystal + d.analysis + d.dashboards + d.lumira + (d.legacy || 0) + d.otherDocs;
  }

  function sizeOf(users, docs) {
    if (users <= 200 && docs <= 2000) return "S";
    if (users <= 1000 && docs <= 10000) return "M";
    return "L";
  }

  var PRICES = { S: 2900, M: 4900, L: 7900 };

  /* Pénalités à une décimale : chaque chiffre saisi déplace le résultat. */
  function r1(x) { return Math.round(x * 10) / 10; }

  function analyse(d) {
    var findings = [];
    var score = 100;
    var docs = totalDocs(d);

    function add(id, severity, penalty, title, detail, source) {
      score -= penalty;
      findings.push({ id: id, severity: severity, penalty: penalty, title: title, detail: detail, source: SOURCES[source] });
    }

    if (d.version === "4.3") {
      add("CSM-01", "critique", 25, "Maintenance spécifique client au 1er janvier 2027",
        "Pendant les 12 premiers mois (2027), SAP ne livre que les correctifs de sécurité notés CVSS 7.0 ou plus. À partir de 2028, plus aucun correctif, patch ni support package n'est livré. Selon l'analyse de C. Vosloo, les nouveaux problèmes non documentés deviennent aussi facturables et SAP ne s'engage plus sur un délai de résolution.", "csm");
    } else if (d.version === "4.2" || d.version === "4.1") {
      add("CSM-02", "critique", 35, "Version déjà sortie de la maintenance standard",
        "La version " + d.version + " n'est plus en maintenance standard. Vérifiez sa situation exacte dans la PAM SAP avant toute décision.", "pam");
    } else if (d.version === "2025") {
      add("CSM-03", "attention", 10, "Maintenance standard de BI 2025 jusqu'au 31 décembre 2027",
        "BI 2025 donne un an de maintenance standard supplémentaire, jusqu'au 31 décembre 2027. SAP prévoit BI 2027 au premier trimestre 2027 (Wiiisdom, Dallas Marks) : rester chez SAP implique une montée de version environ tous les deux ans. La décision suivante est à préparer dès 2027.", "csm");
    }

    if (d.unv > 0 && d.version !== "2025") {
      var credit = r1(3 * Math.min(d.unx / d.unv, 1));
      var p = r1(Math.min(20, r1(4 + 0.3 * (d.unv - 1))) - credit);
      var half = credit > 0;
      add("UNV-01", "élevé", p, d.unv + " univers UNV à convertir",
        "Les univers UNV ne sont plus pris en charge après BI 4.3. Ils doivent être convertis en UNX avant une montée en BI 2025, et les documents qui les utilisent doivent être retestés." +
        (half ? " Vous avez déjà " + d.unx.toLocaleString("fr-FR") + " univers UNX pour " + d.unv.toLocaleString("fr-FR") + " UNV : une partie du chantier semble engagée, la pénalité est réduite de " + String(credit).replace(".", ",") + " points." : ""), "bi2025");
    }

    if (d.lumira > 0) {
      add("CMP-01", "attention", r1(Math.min(5, 2 + 0.3 * (d.lumira - 1))), d.lumira + " applications ou documents Lumira",
        "Lumira Designer reste maintenu en BI 2025, mais sans nouvelle fonctionnalité. La situation de Lumira Discovery est à vérifier dans la PAM SAP. Ces contenus sont à requalifier dans le plan de sortie.", "bi2025");
    }

    var obsolete = d.dashboards + (d.legacy || 0);
    if (obsolete > 0) {
      var po = r1(Math.min(8, 2 + 0.06 * (obsolete - 1)));
      add("CMP-02", "élevé", po, obsolete + " contenus obsolètes (Dashboards, Desktop Intelligence, Explorer, Flash)",
        "Ces technologies ne sont plus prises en charge depuis BI 4.2 SP09 et BI 4.3. SAP fournit un script qui les supprime du référentiel. Elles sont à reconstruire ou à retirer avant toute montée de version.", "deprecated");
    }

    if (!d.auditActive) {
      add("USG-01", "élevé", 10, "Usage réel non mesurable",
        "Sans base d'audit active, impossible de savoir quels documents sont encore ouverts. Le risque est de migrer du contenu que personne ne lit.", "method");
    }

    var unused = null;
    /* Documents à traiter : l'audit actif permet de retirer les documents non ouverts en 12 mois
       (à décommissionner). Un champ vide ou 0 signifie « aucun identifié » : volume inchangé. */
    var toProcess = docs;
    if (d.auditActive && d.unusedDocs > 0 && docs > 0) {
      unused = Math.min(d.unusedDocs, docs);
      toProcess = docs - unused;
      findings.push({ id: "USG-02", severity: "opportunité", penalty: 0,
        title: unused.toLocaleString("fr-FR") + " documents non ouverts depuis 12 mois",
        detail: "Ces documents sont candidats au décommissionnement avant toute migration : autant de travail et de coût en moins.",
        source: SOURCES.method });
    }

    if (d.activeUsers !== null && d.activeUsers !== undefined && d.users > 0) {
      var inactive = d.users - d.activeUsers;
      if (inactive > 0 && inactive / d.users >= 0.2) {
        var share = Math.round(100 * inactive / d.users);
        var legacyV = d.version === "4.3" || d.version === "4.2" || d.version === "4.1";
        if (legacyV) {
          add("USG-03", "attention", r1(Math.min(5, Math.max(2, 10 * inactive / d.users))), inactive.toLocaleString("fr-FR") + " comptes sans connexion depuis 12 mois",
            "Soit " + share + " % des comptes. Avec une couverture de sécurité réduite, chaque compte inutile est une surface d'exposition de plus : les désactiver allège aussi la migration et peut réduire les licences.", "method");
        } else {
          findings.push({ id: "USG-03", severity: "opportunité", penalty: 0,
            title: inactive.toLocaleString("fr-FR") + " comptes sans connexion depuis 12 mois",
            detail: "Soit " + share + " % des comptes. Les désactiver allège la migration et peut réduire les licences.",
            source: SOURCES.method });
        }
      }
    }

    var volNote = toProcess < docs ? " (sur " + docs.toLocaleString("fr-FR") + " au total, hors documents non ouverts en 12 mois)" : "";
    var volPts = r1(Math.min(20, toProcess / 500));
    if (volPts > 0) {
      add("VOL-01", volPts >= 15 ? "élevé" : "attention", volPts, (volPts >= 15 ? "Volume important : " : "Volume à traiter : ") + toProcess.toLocaleString("fr-FR") + " documents" + volNote,
        "Un tri préalable du contenu est indispensable pour maîtriser le coût d'une montée de version ou d'une migration.", "method");
    }

    score = Math.round(Math.max(0, Math.min(100, score)));
    var level = score >= 70 ? "Préparée" : score >= 40 ? "À organiser" : "Urgent";
    /* Niveau de risque affiché : 100 moins l'indice. Une version 4.x a une échéance fixe :
       son risque n'est jamais présenté en dessous de « élevé ». */
    var risk = 100 - score;
    var riskLevel = risk >= 70 ? "critique" : risk >= 45 ? "élevé" : risk >= 25 ? "modéré" : "faible";
    var legacyVersion = d.version === "4.3" || d.version === "4.2" || d.version === "4.1";
    if (legacyVersion && (riskLevel === "faible" || riskLevel === "modéré")) riskLevel = "élevé";
    var order = { "critique": 0, "élevé": 1, "attention": 2, "à vérifier": 3, "opportunité": 4 };
    findings.sort(function (a, b) { return order[a.severity] - order[b.severity] || b.penalty - a.penalty; });
    var size = sizeOf(d.users, docs);

    return {
      score: score, level: level, risk: risk, riskLevel: riskLevel, docs: docs, toProcess: toProcess, size: size, price: PRICES[size],
      unused: unused, findings: findings,
      top: findings.filter(function (f) { return f.penalty > 0; }).slice(0, 3)
    };
  }

  /* Import du fichier produit par le script de collecte (formats trivoie-scan/1 et /2). */
  function fromScriptFile(json) {
    var obj;
    try { obj = typeof json === "string" ? JSON.parse(json.replace(/^\uFEFF/, "")) : json; }
    catch (e) { throw new Error("Ce fichier n'a pas été produit par le script Trivoie."); }
    var v1 = obj && obj.format === "trivoie-scan/1" && obj.counts;
    var v2 = obj && obj.format === "trivoie-scan/2" && obj.documents;
    if (!v1 && !v2) throw new Error("Ce fichier n'a pas été produit par le script Trivoie.");
    var num = function (x) { var n = Number(x); return isFinite(n) && n >= 0 ? Math.round(n) : 0; };
    var info, out;
    if (v1) {
      var app = obj.counts.CI_APPOBJECTS || {};
      var sys = obj.counts.CI_SYSTEMOBJECTS || {};
      info = obj.counts.CI_INFOOBJECTS || {};
      out = { unv: num(app.Universe), unx: num(app["DSL.MetaDataFile"]), users: num(sys.User),
        schedules: num(obj.recurringSchedules), activeUsers: null, coherent: true };
    } else {
      info = obj.documents.parType || {};
      out = { unv: num(obj.universUnv), unx: num(obj.universUnx), users: num(obj.utilisateurs),
        schedules: num(obj.planificationsRecurrentes),
        activeUsers: obj.utilisateursActifs12Mois === null || obj.utilisateursActifs12Mois === undefined ? null : num(obj.utilisateursActifs12Mois),
        coherent: obj.documents.coherent !== false };
    }
    ["webi", "crystal", "analysis", "dashboards", "lumira", "legacy", "otherDocs"].forEach(function (k) { out[k] = 0; });
    Object.keys(info).forEach(function (kind) {
      var n = num(info[kind]);
      if (DOC_KINDS[kind]) out[DOC_KINDS[kind]] += n;
      else if (NON_DOC_KINDS.indexOf(kind) === -1) out.otherDocs += n;
    });
    return out;
  }

  function summaryText(d, r) {
    var lines = [
      "Scan Trivoie du " + new Date().toLocaleDateString("fr-FR"),
      "Version : " + (d.version === "2025" ? "BI 2025" : "BI " + d.version),
      "Niveau de risque : " + r.risk + "/100 (" + r.riskLevel + ")",
      "Taille de plateforme : " + r.size,
      "Documents : " + r.docs + " · Univers UNV : " + d.unv + " · Univers UNX : " + d.unx + " · Utilisateurs : " + d.users +
        (d.activeUsers !== null && d.activeUsers !== undefined ? " (dont " + d.activeUsers + " actifs sur 12 mois)" : ""),
      "Points principaux :"
    ];
    r.findings.forEach(function (f) { lines.push("- [" + f.severity + "] " + f.title); });
    return lines.join("\n");
  }

  /* Dernier jour pour commander le diagnostic (10 jours ouvrés) et l'avoir avant l'échéance.
     Jours fériés pris en compte : ceux de fin d'année. */
  function lastOrderDate(deadline) {
    var d = new Date(deadline.getTime());
    var counted = 0;
    var holiday = function (x) { var m = x.getMonth(), j = x.getDate(); return (m === 11 && j === 25) || (m === 0 && j === 1) || (m === 4 && (j === 1 || j === 8)) || (m === 6 && j === 14) || (m === 7 && j === 15) || (m === 10 && (j === 1 || j === 11)); };
    while (counted < 10) {
      var wd = d.getDay();
      if (wd !== 0 && wd !== 6 && !holiday(d)) counted++;
      d.setDate(d.getDate() - 1);
    }
    while (d.getDay() === 0 || d.getDay() === 6 || holiday(d)) d.setDate(d.getDate() - 1);
    return d;
  }

  var api = { lastOrderDate: lastOrderDate, validate: validate, analyse: analyse, fromScriptFile: fromScriptFile,
    summaryText: summaryText, sizeOf: sizeOf, PRICES: PRICES, SOURCES: SOURCES };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.TrivoieEngine = api;
})(this);
