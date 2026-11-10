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

t("pourcentage hors bornes refusé seulement si audit actif", () => {
  assert.equal(E.validate({ auditActive: "oui", usedPct: "140" }).valid, false);
  assert.equal(E.validate({ auditActive: "non", usedPct: "140" }).valid, true);
});

t("plateforme 4.3 typique", () => {
  const d = E.validate({ version: "4.3", webi: 5800, crystal: 300, unv: 23, unx: 40, users: 740,
    auditActive: "oui", usedPct: 45, lumira: 0, dashboards: 12 }).data;
  const r = E.analyse(d);
  // 100 - 25 (CSM) - 11 (UNV 11-50 : 14, moins 3 car UNX 40 >= UNV 23) - 5 (obsolètes : 12 Dashboards)
  // - 5 (volume moyen : 2 750 documents ouverts à traiter sur 6 112) = 54
  assert.equal(r.score, 54);
  assert.equal(r.toProcess, 6112 - Math.round(6112 * 0.55));
  assert.equal(r.level, "À organiser");
  assert.equal(r.size, "M");
  assert.equal(r.price, 4900);
  assert.equal(r.docs, 6112);
  assert.equal(r.unused, Math.round(6112 * 0.55));
  assert.equal(r.findings[0].id, "CSM-01");
  assert.ok(r.findings.some(f => f.id === "CMP-02" && f.penalty === 5));
  assert.equal(r.top.length, 3);
});

t("version 4.2 sans audit, gros volume : urgent", () => {
  const d = E.validate({ version: "4.2", webi: 12000, unv: 80, users: 1500, auditActive: "non" }).data;
  const r = E.analyse(d);
  // 100 - 35 - 20 - 10 (audit) - 10 (volume) = 25
  assert.equal(r.score, 25);
  assert.equal(r.level, "Urgent");
  assert.equal(r.size, "L");
});

t("BI 2025 : pas de pénalité UNV, échéance 2027", () => {
  const d = E.validate({ version: "2025", webi: 500, unv: 5, users: 50, auditActive: "oui", usedPct: 80 }).data;
  const r = E.analyse(d);
  assert.ok(!r.findings.some(f => f.id === "UNV-01"));
  assert.equal(r.score, 90);
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
  assert.equal(c.risk, 75); assert.equal(c.riskLevel, "critique");
});

t("date limite de commande : 10 jours ouvrés avant le 31/12/2026, Noël exclu", () => {
  const d = E.lastOrderDate(new Date(2026, 11, 31));
  assert.equal(d.getFullYear() + "-" + (d.getMonth() + 1) + "-" + d.getDate(), "2026-12-16");
});

console.log(n + " tests réussis");

/* Effet de chaque champ du formulaire sur le résultat. */
const base = { version: "4.3", webi: 5800, crystal: 300, analysis: 40, lumira: 0, dashboards: 12, legacy: 0, otherDocs: 150,
  unv: 23, unx: 10, users: 740, activeUsers: 740, auditActive: "oui", usedPct: 100 };
const run = (o) => E.analyse(E.validate(Object.assign({}, base, o)).data);

t("champ « documents ouverts (%) » : réduit le volume à traiter et donc le risque", () => {
  const hi = run({ usedPct: 100 }), lo = run({ usedPct: 20 });
  assert.equal(hi.toProcess, hi.docs);
  assert.ok(lo.toProcess < hi.toProcess);
  assert.ok(hi.findings.some(f => f.id === "VOL-02"));
  assert.ok(!lo.findings.some(f => f.id === "VOL-02"));
  assert.equal(lo.risk, hi.risk - 5);
  assert.equal(lo.size, hi.size);
  assert.equal(lo.price, hi.price);
  assert.ok(run({ usedPct: 20 }).unused > run({ usedPct: 80 }).unused);
});

t("champ « documents ouverts (%) » : ignoré si l'audit n'est pas actif", () => {
  const a = run({ auditActive: "non", usedPct: 20 }), b = run({ auditActive: "non", usedPct: 90 });
  assert.equal(a.risk, b.risk);
  assert.equal(a.toProcess, a.docs);
  assert.equal(a.unused, null);
});

t("univers UNX : au moins autant que d'UNV réduit la pénalité de 3 points", () => {
  const few = run({ unx: 5 }), many = run({ unx: 23 });
  const pen = (r) => r.findings.find(f => f.id === "UNV-01").penalty;
  assert.equal(pen(few), 14);
  assert.equal(pen(many), 11);
  assert.equal(many.risk, few.risk - 3);
  assert.equal(pen(run({ unx: 0, unv: 5 })), 8);
  assert.equal(pen(run({ unx: 5, unv: 5 })), 5);
});

t("comptes actifs : 20 % d'inactifs ou plus pénalise une 4.x, simple économie en BI 2025", () => {
  const ok = run({ activeUsers: 740 }), inact = run({ activeUsers: 300 });
  assert.ok(!ok.findings.some(f => f.id === "USG-03"));
  assert.equal(inact.findings.find(f => f.id === "USG-03").penalty, 5);
  assert.equal(inact.risk, ok.risk + 5);
  assert.equal(run({ activeUsers: 590 }).findings.find(f => f.id === "USG-03").penalty, 5);
  assert.ok(!run({ activeUsers: 600 }).findings.some(f => f.id === "USG-03"));
  const y = run({ version: "2025", activeUsers: 300 });
  assert.equal(y.findings.find(f => f.id === "USG-03").penalty, 0);
  assert.equal(y.findings.find(f => f.id === "USG-03").severity, "opportunité");
  assert.equal(run({ activeUsers: "" }).findings.some(f => f.id === "USG-03"), false);
});

t("contenus obsolètes : pénalité par palier 3 / 5 / 8", () => {
  const pen = (o) => run(o).findings.find(f => f.id === "CMP-02").penalty;
  assert.equal(pen({ dashboards: 1 }), 3);
  assert.equal(pen({ dashboards: 10 }), 3);
  assert.equal(pen({ dashboards: 11 }), 5);
  assert.equal(pen({ dashboards: 100 }), 5);
  assert.equal(pen({ dashboards: 101 }), 8);
  assert.equal(pen({ dashboards: 5, legacy: 6 }), 5);
  assert.ok(!run({ dashboards: 0, legacy: 0 }).findings.some(f => f.id === "CMP-02"));
});

t("taille et prix : comptes et documents (tous types) fixent S, M ou L", () => {
  assert.equal(run({ webi: 100, crystal: 0, analysis: 0, otherDocs: 0, dashboards: 0, users: 50, activeUsers: "" }).size, "S");
  assert.equal(run({ webi: 100, crystal: 0, analysis: 0, otherDocs: 0, dashboards: 0, users: 500, activeUsers: "" }).size, "M");
  assert.equal(run({ webi: 100, crystal: 0, analysis: 0, otherDocs: 0, dashboards: 0, users: 1500, activeUsers: "" }).price, 7900);
  assert.equal(run({ crystal: 4000, webi: 100, analysis: 0, otherDocs: 0, dashboards: 0 }).docs, 4100);
  assert.equal(run({ lumira: 12000 }).size, "L");
  assert.equal(run({ legacy: 12000 }).size, "L");
});

t("version, Lumira, base d'audit : effets de base", () => {
  assert.ok(run({ lumira: 3 }).risk === run({ lumira: 0 }).risk + 5);
  assert.equal(run({ auditActive: "non" }).risk, run({ auditActive: "oui" }).risk + 10);
  assert.ok(run({ version: "4.2" }).risk > run({ version: "4.3" }).risk);
  assert.ok(run({ version: "2025" }).risk < run({ version: "4.3" }).risk);
});
console.log(n + " tests réussis");
