const assert = require("assert");
const E = require("./engine.js");
let n = 0;
function t(name, fn) { fn(); n++; console.log("ok -", name); }

t("taille S/M/L aux bornes", () => {
  assert.equal(E.sizeOf(200, 2000), "S");
  assert.equal(E.sizeOf(201, 10), "M");
  assert.equal(E.sizeOf(10, 2001), "M");
  assert.equal(E.sizeOf(1000, 10000), "M");
  assert.equal(E.sizeOf(1001, 10), "L");
  assert.equal(E.sizeOf(10, 10001), "L");
});

t("validation : valeurs négatives et texte refusés", () => {
  const v = E.validate({ webi: "-3", unv: "abc", users: "120" });
  assert.equal(v.valid, false);
  assert.ok(v.errors.webi && v.errors.unv);
  assert.equal(v.data.users, 120);
});

t("validation : espaces et virgules acceptés", () => {
  const v = E.validate({ webi: "4 500", users: "12,0" });
  assert.equal(v.valid, true);
  assert.equal(v.data.webi, 4500);
  assert.equal(v.data.users, 12);
});

t("documents non ouverts au-delà du total refusés seulement si audit actif", () => {
  assert.equal(E.validate({ auditActive: "oui", webi: "100", unusedDocs: "140" }).valid, false);
  assert.equal(E.validate({ auditActive: "oui", webi: "100", unusedDocs: "100" }).valid, true);
  assert.equal(E.validate({ auditActive: "non", webi: "100", unusedDocs: "140" }).valid, true);
});

t("plateforme 4.3 typique", () => {
  const d = E.validate({ version: "4.3", webi: 5800, crystal: 300, unv: 23, unx: 40, users: 740,
    auditActive: "oui", unusedDocs: 3362, lumira: 0, dashboards: 12 }).data;
  const r = E.analyse(d);
  // 100 - 25 (CSM) - 7,6 (UNV 23 : 4 + 0,3 x 22 = 10,6, moins 3 car UNX 40 >= UNV 23)
  // - 2,7 (obsolètes : 12 Dashboards, 2 + 0,06 x 11) - 5,5 (volume : 2 750 documents ouverts à traiter, 1 point par 500) = 59,2 soit 59
  assert.equal(r.score, 59);
  assert.equal(r.toProcess, 6112 - 3362);
  assert.equal(r.level, "À organiser");
  assert.equal(r.size, "M");
  assert.equal(r.price, 4900);
  assert.equal(r.docs, 6112);
  assert.equal(r.unused, Math.round(6112 * 0.55));
  assert.equal(r.findings[0].id, "CSM-01");
  assert.ok(r.findings.some(f => f.id === "CMP-02" && f.penalty === 2.7));
  assert.equal(r.top.length, 3);
});

t("version 4.2 sans audit, gros volume : urgent", () => {
  const d = E.validate({ version: "4.2", webi: 12000, unv: 80, users: 1500, auditActive: "non" }).data;
  const r = E.analyse(d);
  // 100 - 35 - 20 - 10 (audit) - 20 (volume, plafond) = 15
  assert.equal(r.score, 15);
  assert.equal(r.level, "Urgent");
  assert.equal(r.size, "L");
});

t("BI 2025 : pas de pénalité UNV, échéance 2027", () => {
  const d = E.validate({ version: "2025", webi: 500, unv: 5, users: 50, auditActive: "oui", unusedDocs: 100 }).data;
  const r = E.analyse(d);
  assert.ok(!r.findings.some(f => f.id === "UNV-01"));
  assert.equal(r.score, 89);
  assert.equal(r.level, "Préparée");
});

t("score jamais négatif", () => {
  const d = E.validate({ version: "4.1", webi: 50000, unv: 500, lumira: 10, users: 5000, auditActive: "non" }).data;
  assert.ok(E.analyse(d).score >= 0);
});

t("chaque point a une source", () => {
  const d = E.validate({ version: "4.3", webi: 3000, unv: 3, lumira: 2, dashboards: 1, users: 10, auditActive: "non" }).data;
  E.analyse(d).findings.forEach(f => assert.ok(f.source && f.source.label && f.source.url, f.id));
});

t("import du fichier du script", () => {
  const file = { format: "trivoie-scan/1", counts: {
    CI_INFOOBJECTS: { Webi: 1200, CrystalReport: 40, Folder: 300, Shortcut: 12, Pdf: 30, Excel: 5, "XL.XcelsiusEnterprise": 3, "AAD.AnalysisWorkspace": 7 },
    CI_APPOBJECTS: { Universe: 18, "DSL.MetaDataFile": 25, CommonConnection: 9 },
    CI_SYSTEMOBJECTS: { User: 410, UserGroup: 35, Server: 22 } }, recurringSchedules: 88 };
  const o = E.fromScriptFile(JSON.stringify(file));
  assert.deepEqual(o, { webi: 1200, crystal: 40, analysis: 7, dashboards: 3, lumira: 0, legacy: 0, otherDocs: 35,
    unv: 18, unx: 25, users: 410, schedules: 88, activeUsers: null, coherent: true });
});

t("fichier étranger refusé", () => {
  assert.throws(() => E.fromScriptFile('{"hello":1}'), /script Trivoie/);
});

t("résumé texte complet", () => {
  const d = E.validate({ version: "4.3", webi: 100, users: 10, auditActive: "non" }).data;
  const s = E.summaryText(d, E.analyse(d));
  assert.ok(s.includes("Niveau de risque") && s.includes("BI 4.3"));
});

t("import du fichier v2 réellement produit par le script (faux serveur)", () => {
  const o = E.fromScriptFile(require("fs").readFileSync(__dirname + "/test-scan.json", "utf8"));
  assert.deepEqual(o, { webi: 2345, crystal: 61, analysis: 9, dashboards: 4, lumira: 6, legacy: 10,
    otherDocs: 56, unv: 27, unx: 33, users: 812, schedules: 1503, activeUsers: 500, coherent: true });
  const d = E.validate(Object.assign({ version: "4.3", auditActive: "non" }, o)).data;
  const r = E.analyse(d);
  assert.ok(r.findings.some(f => f.id === "CMP-01"));
  assert.ok(r.findings.some(f => f.id === "CMP-02" && f.title.startsWith("14 ")));
  assert.ok(r.findings.some(f => f.id === "USG-03" && f.title.startsWith("312 ")));
  assert.equal(r.docs, 2491);
});

t("utilisateurs actifs supérieurs au total refusés", () => {
  const v = E.validate({ users: 100, activeUsers: 150 });
  assert.ok(v.errors.activeUsers);
  assert.equal(v.data.activeUsers, null);
});

t("fichier v2 incohérent signalé", () => {
  const o = E.fromScriptFile({ format: "trivoie-scan/2", documents: { parType: { Webi: 10 }, coherent: false } });
  assert.equal(o.coherent, false);
});

t("JSON illisible : message clair", () => {
  assert.throws(() => E.fromScriptFile("pas du json"), /script Trivoie/);
});

t("risque : inverse de l'indice, plancher « élevé » pour une version 4.x", () => {
  const a = E.analyse(E.validate({ version: "4.3", webi: 100, users: 10, auditActive: "oui" }).data);
  assert.equal(a.risk, 25); assert.equal(a.riskLevel, "élevé");
  const b = E.analyse(E.validate({ version: "2025", webi: 100, users: 10, auditActive: "oui" }).data);
  assert.equal(b.risk, 10); assert.equal(b.riskLevel, "faible");
  const c = E.analyse(E.validate({ version: "4.2", webi: 12000, unv: 80, users: 1500, auditActive: "non" }).data);
  assert.equal(c.risk, 85); assert.equal(c.riskLevel, "critique");
});

t("date limite de commande : 10 jours ouvrés avant le 31/12/2026, Noël exclu", () => {
  const d = E.lastOrderDate(new Date(2026, 11, 31));
  assert.equal(d.getFullYear() + "-" + (d.getMonth() + 1) + "-" + d.getDate(), "2026-12-16");
});

console.log(n + " tests réussis");

/* Effet de chaque champ du formulaire sur le résultat. */
const base = { version: "4.3", webi: 5800, crystal: 300, analysis: 40, lumira: 0, dashboards: 12, legacy: 0, otherDocs: 150,
  unv: 23, unx: 10, users: 740, activeUsers: 740, auditActive: "oui", unusedDocs: 0 };
const run = (o) => E.analyse(E.validate(Object.assign({}, base, o)).data);
const pen = (r, id) => { const f = r.findings.find(x => x.id === id); return f ? f.penalty : 0; };

t("champ « documents non ouverts » : vide et 0 donnent exactement le même résultat", () => {
  const e = run({ unusedDocs: "" }), z = run({ unusedDocs: "0" }), u = run({ unusedDocs: undefined });
  for (const k of ["score", "risk", "riskLevel", "toProcess", "size", "price"]) { assert.equal(e[k], z[k]); assert.equal(e[k], u[k]); }
  assert.equal(e.findings.length, z.findings.length);
  assert.equal(e.unused, null);
  assert.equal(z.unused, null);
});

t("champ « documents non ouverts » : le risque ne monte jamais, baisse à chaque tranche et suit le nombre saisi", () => {
  const docs = 6302; let prev = Infinity, prevTp = Infinity; const seen = new Set();
  for (let n = 0; n <= docs; n += 100) {
    const r = run({ unusedDocs: n });
    assert.equal(r.toProcess, docs - n);
    assert.ok(r.toProcess < prevTp || n === 0);
    assert.ok(r.risk <= prev, "le risque ne monte jamais quand on retire des documents");
    prev = r.risk; prevTp = r.toProcess; seen.add(r.risk);
  }
  assert.ok(seen.size >= 10, "au moins 10 niveaux de risque différents entre 0 et le total");
  assert.equal(pen(run({ unusedDocs: docs }), "VOL-01"), 0);
  assert.equal(run({ unusedDocs: 3000 }).risk, run({ unusedDocs: 0 }).risk - 6);
  assert.equal(run({ unusedDocs: 0 }).risk, 50);
  assert.ok(run({ unusedDocs: 1 }).risk >= run({ unusedDocs: 0 }).risk - 1, "1 document de plus ne fait jamais bouger de plus d'un point");
  assert.ok(run({ unusedDocs: 4000 }).risk < run({ unusedDocs: 500 }).risk);
});

t("champ « documents non ouverts » : un pas d'un document ne déplace jamais le risque de plus d'un point", () => {
  let prev = run({ unusedDocs: 0 }).risk;
  for (let n = 1; n <= 6302; n++) {
    const r = run({ unusedDocs: n }).risk;
    assert.ok(prev - r <= 1 && r <= prev, "saut anormal à " + n + " : " + prev + " -> " + r);
    prev = r;
  }
});

t("champ « documents non ouverts » : refusé au-delà du total, ignoré si l'audit n'est pas actif", () => {
  assert.equal(E.validate(Object.assign({}, base, { unusedDocs: 6303 })).valid, false);
  assert.equal(E.validate(Object.assign({}, base, { unusedDocs: 6302 })).valid, true);
  const a = run({ auditActive: "non", unusedDocs: 100 }), b = run({ auditActive: "non", unusedDocs: 5000 }), c = run({ auditActive: "non", unusedDocs: "" });
  assert.equal(a.risk, b.risk); assert.equal(a.risk, c.risk);
  assert.equal(a.toProcess, a.docs);
  assert.equal(a.unused, null);
});

t("niveau de risque : toujours entre 0 et 100, entier, cohérent sur 20 000 combinaisons aléatoires", () => {
  let seed = 7; const rnd = () => (seed = (seed * 1103515245 + 12345) % 2147483648) / 2147483648;
  const ver = ["4.1", "4.2", "4.3", "2025"];
  for (let i = 0; i < 20000; i++) {
    const o = { version: ver[Math.floor(rnd() * 4)], webi: String(Math.floor(rnd() * 12000)), crystal: String(Math.floor(rnd() * 800)),
      analysis: String(Math.floor(rnd() * 50)), lumira: String(Math.floor(rnd() * 30)), dashboards: String(Math.floor(rnd() * 60)),
      unv: String(Math.floor(rnd() * 120)), unx: String(Math.floor(rnd() * 120)), users: String(Math.floor(rnd() * 3000)),
      auditActive: rnd() < 0.5 ? "oui" : "non" };
    const v0 = E.validate(Object.assign({}, o, { unusedDocs: "" })).data, r0 = E.analyse(v0);
    const z = E.analyse(E.validate(Object.assign({}, o, { unusedDocs: "0" })).data);
    assert.equal(r0.risk, z.risk, "vide != 0");
    assert.ok(Number.isInteger(r0.risk) && r0.risk >= 0 && r0.risk <= 100);
    assert.equal(r0.risk + r0.score, 100);
    const half = Math.floor(r0.docs / 2);
    const rh = E.analyse(E.validate(Object.assign({}, o, { unusedDocs: String(half) })).data);
    assert.ok(rh.risk <= r0.risk, "retirer des documents ne peut pas augmenter le risque");
  }
});

t("volume : 0,2 point par 100 documents à traiter, plafonné à 20", () => {
  const v = (n) => pen(run({ webi: n, crystal: 0, analysis: 0, otherDocs: 0, dashboards: 0, unusedDocs: 0 }), "VOL-01");
  assert.equal(v(20), 0);
  assert.equal(v(500), 1);
  assert.equal(v(1499), 3);
  assert.equal(v(4000), 8);
  assert.equal(v(9400), 18.8);
  assert.equal(v(10000), 20);
  assert.equal(v(50000), 20);
});

t("univers UNV : pénalité proportionnelle au nombre, plafonnée à 20", () => {
  const p = (n) => pen(run({ unv: n, unx: 0 }), "UNV-01");
  assert.equal(p(0), 0);
  assert.equal(p(1), 4);
  assert.equal(p(10), 6.7);
  assert.equal(p(23), 10.6);
  assert.equal(p(50), 18.7);
  assert.equal(p(55), 20);
  assert.equal(p(500), 20);
  for (let n = 1; n < 55; n++) assert.ok(p(n + 1) > p(n), "UNV " + n);
});

t("univers UNX : le rapport UNX / UNV réduit la pénalité de 3 points au plus", () => {
  const p = (o) => pen(run(o), "UNV-01");
  assert.equal(p({ unv: 23, unx: 0 }), 10.6);
  assert.equal(p({ unv: 23, unx: 5 }), 9.9);
  assert.equal(p({ unv: 23, unx: 12 }), 9);
  assert.equal(p({ unv: 23, unx: 23 }), 7.6);
  assert.equal(p({ unv: 23, unx: 400 }), 7.6);
  assert.equal(p({ unv: 5, unx: 0 }), 5.2);
  assert.equal(p({ unv: 5, unx: 5 }), 2.2);
  assert.ok(run({ unx: 23 }).risk < run({ unx: 0 }).risk);
});

t("comptes actifs : de 2 à 5 points selon la part d'inactifs, dès 20 %, simple économie en BI 2025", () => {
  const ok = run({ activeUsers: 740 });
  assert.ok(!ok.findings.some(f => f.id === "USG-03"));
  assert.equal(pen(run({ activeUsers: 590 }), "USG-03"), 2);
  assert.equal(pen(run({ activeUsers: 520 }), "USG-03"), 3);
  assert.equal(pen(run({ activeUsers: 450 }), "USG-03"), 3.9);
  assert.equal(pen(run({ activeUsers: 370 }), "USG-03"), 5);
  assert.equal(pen(run({ activeUsers: 100 }), "USG-03"), 5);
  assert.ok(!run({ activeUsers: 600 }).findings.some(f => f.id === "USG-03"));
  assert.equal(run({ activeUsers: 300 }).risk, ok.risk + 5);
  const y = run({ version: "2025", activeUsers: 300 });
  assert.equal(y.findings.find(f => f.id === "USG-03").penalty, 0);
  assert.equal(y.findings.find(f => f.id === "USG-03").severity, "opportunité");
  assert.equal(run({ activeUsers: "" }).findings.some(f => f.id === "USG-03"), false);
});

t("contenus obsolètes : pénalité proportionnelle, de 2 à 8", () => {
  const p = (o) => pen(run(o), "CMP-02");
  assert.equal(p({ dashboards: 1 }), 2);
  assert.equal(p({ dashboards: 10 }), 2.5);
  assert.equal(p({ dashboards: 50 }), 4.9);
  assert.equal(p({ dashboards: 100 }), 7.9);
  assert.equal(p({ dashboards: 5, legacy: 6 }), 2.6);
  assert.equal(p({ dashboards: 500 }), 8);
  assert.ok(!run({ dashboards: 0, legacy: 0 }).findings.some(f => f.id === "CMP-02"));
});

t("Lumira : de 2 à 5 points selon le nombre de contenus", () => {
  const p = (n) => pen(run({ lumira: n }), "CMP-01");
  assert.equal(p(0), 0);
  assert.equal(p(1), 2);
  assert.equal(p(3), 2.6);
  assert.equal(p(11), 5);
  assert.equal(p(300), 5);
});

t("taille et prix : comptes et documents (tous types) fixent S, M ou L", () => {
  assert.equal(run({ webi: 100, crystal: 0, analysis: 0, otherDocs: 0, dashboards: 0, users: 50, activeUsers: "" }).size, "S");
  assert.equal(run({ webi: 100, crystal: 0, analysis: 0, otherDocs: 0, dashboards: 0, users: 500, activeUsers: "" }).size, "M");
  assert.equal(run({ webi: 100, crystal: 0, analysis: 0, otherDocs: 0, dashboards: 0, users: 1500, activeUsers: "" }).price, 7900);
  assert.equal(run({ crystal: 4000, webi: 100, analysis: 0, otherDocs: 0, dashboards: 0 }).docs, 4100);
  assert.equal(run({ lumira: 12000 }).size, "L");
  assert.equal(run({ legacy: 12000 }).size, "L");
});

t("version et base d'audit : effets de base", () => {
  assert.equal(pen(run({ auditActive: "non" }), "USG-01"), 10);
  assert.equal(pen(run({ auditActive: "oui" }), "USG-01"), 0);
  assert.ok(run({ version: "4.2" }).risk > run({ version: "4.3" }).risk);
  assert.ok(run({ version: "2025" }).risk < run({ version: "4.3" }).risk);
});

t("chaque champ numérique modifie le résultat (aucun champ inerte)", () => {
  const fields = { webi: [100, 8000], crystal: [0, 3000], analysis: [0, 2000], otherDocs: [0, 3000], dashboards: [0, 60], legacy: [0, 60],
    lumira: [0, 6], unv: [0, 30], users: [100, 1500], activeUsers: [100, 700] };
  Object.keys(fields).forEach((f) => {
    const a = run(Object.assign({ unx: 0 }, { [f]: fields[f][0] })), b = run(Object.assign({ unx: 0 }, { [f]: fields[f][1] }));
    const same = a.risk === b.risk && a.docs === b.docs && a.size === b.size && JSON.stringify(a.findings.map(x => x.title)) === JSON.stringify(b.findings.map(x => x.title));
    assert.ok(!same, "champ inerte : " + f);
  });
  assert.notEqual(run({ unx: 0 }).risk, run({ unx: 23 }).risk);
});
console.log(n + " tests réussis");
