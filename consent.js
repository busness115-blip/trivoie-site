/* Trivoie : consentement et mesure des conversions Google Ads.
   Rien n'est chargé depuis Google tant que le visiteur n'a pas cliqué sur « Accepter ».
   Le scan n'envoie aucune donnée : les événements ci-dessous ne contiennent jamais de saisie. */
(function () {
  "use strict";
  var AW_ID = "AW-18572193911";
  var LABELS = {
    scan: AW_ID + "/sMLHCLWIubcdEPfg9JdF",
    call: AW_ID + "/e3eFCLiIubcdEPfg9JdF"
  };
  var KEY = "trivoie-consent";
  var MAX_AGE = 1000 * 60 * 60 * 24 * 180; /* 6 mois, puis on redemande */
  var loaded = false;
  var sent = {};

  function read() {
    try {
      var o = JSON.parse(localStorage.getItem(KEY) || "null");
      if (o && (o.v === "accepted" || o.v === "refused") && Date.now() - o.t < MAX_AGE) return o.v;
    } catch (e) {}
    return null;
  }
  function write(v) {
    try { localStorage.setItem(KEY, JSON.stringify({ v: v, t: Date.now() })); } catch (e) {}
  }

  function loadGoogle() {
    if (loaded) return;
    loaded = true;
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("consent", "default", { ad_storage: "denied", ad_user_data: "denied", ad_personalization: "denied", analytics_storage: "denied" });
    window.gtag("consent", "update", { ad_storage: "granted", ad_user_data: "granted", ad_personalization: "denied", analytics_storage: "denied" });
    window.gtag("js", new Date());
    window.gtag("config", AW_ID, { allow_enhanced_conversions: false });
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + AW_ID;
    document.head.appendChild(s);
  }

  function track(name) {
    if (read() !== "accepted" || !loaded || sent[name] || !LABELS[name]) return;
    sent[name] = true;
    var p = { send_to: LABELS[name] };
    if (name === "call") { p.value = 1.0; p.currency = "EUR"; }
    window.gtag("event", "conversion", p);
  }

  function forget() {
    /* Retire les cookies Google Ads posés sur ce domaine (conversion linker). */
    var names = ["_gcl_aw", "_gcl_au", "_gcl_dc", "_gac_" + AW_ID.replace("AW-", "")];
    var host = location.hostname;
    var domains = ["", host, "." + host];
    if (host.split(".").length > 2) domains.push("." + host.split(".").slice(-2).join("."));
    document.cookie.split(";").forEach(function (c) {
      var n = c.split("=")[0].trim();
      if (n.indexOf("_gcl_") === 0 || n.indexOf("_gac_") === 0 || names.indexOf(n) !== -1) {
        domains.forEach(function (d) {
          document.cookie = n + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/" + (d ? "; domain=" + d : "");
        });
      }
    });
  }

  var banner = null;
  function css() {
    if (document.getElementById("consent-css")) return;
    var st = document.createElement("style");
    st.id = "consent-css";
    st.textContent =
      "#consent{position:fixed;left:0;right:0;bottom:0;z-index:2147483000;background:var(--surface,#fff);color:var(--ink,#15212a);border-top:2px solid var(--accent,#0c5a6b);box-shadow:0 -6px 24px rgba(0,0,0,.18);font:400 15px/1.5 var(--f-body,'IBM Plex Sans','Segoe UI',Arial,sans-serif);padding:14px max(16px,env(safe-area-inset-right,0px)) calc(14px + env(safe-area-inset-bottom,0px)) max(16px,env(safe-area-inset-left,0px))}" +
      "#consent .c-in{max-width:1120px;margin:0 auto;display:flex;gap:16px 24px;align-items:center;flex-wrap:wrap}" +
      "#consent .c-tx{flex:1 1 420px;min-width:0}" +
      "#consent .c-tx strong{display:block;font-size:16px;margin-bottom:2px}" +
      "#consent .c-tx a{color:var(--accent,#0c5a6b)}" +
      "#consent .c-bt{display:flex;gap:10px;flex-wrap:wrap}" +
      "#consent button{font:600 15px var(--f-body,Arial,sans-serif);padding:11px 22px;min-height:44px;border-radius:6px;border:2px solid var(--accent,#0c5a6b);background:transparent;color:var(--accent,#0c5a6b);cursor:pointer}" +
      "#consent button:hover{filter:brightness(1.08)}" +
      "#consent button.c-ok{background:var(--accent,#0c5a6b);color:var(--accent-ink,#fff)}" +
      "#consent button:focus-visible{outline:3px solid var(--accent,#0c5a6b);outline-offset:2px}";
    document.head.appendChild(st);
  }
  function hide() { if (banner && banner.parentNode) banner.parentNode.removeChild(banner); banner = null; }
  function choose(v) {
    write(v);
    hide();
    if (v === "accepted") loadGoogle(); else forget();
    var st = document.getElementById("consent-status");
    if (st) st.textContent = v === "accepted" ? "Mesure publicitaire acceptée." : "Mesure publicitaire refusée.";
  }
  function show() {
    if (banner) return;
    css();
    banner = document.createElement("div");
    banner.id = "consent";
    banner.setAttribute("role", "dialog");
    banner.setAttribute("aria-label", "Mesure publicitaire");
    banner.innerHTML =
      '<div class="c-in"><div class="c-tx"><strong>Mesure publicitaire</strong>' +
      "Avec votre accord, la balise Google Ads mesure si une annonce a mené à un scan terminé ou à une demande d'échange. " +
      "Elle peut déposer un cookie et ne reçoit jamais vos saisies. Refuser ne change rien à l'usage du site. " +
      '<a href="/confidentialite/">Détails</a></div>' +
      '<div class="c-bt"><button type="button" class="c-ok" data-c="accepted">Accepter</button>' +
      '<button type="button" data-c="refused">Refuser</button></div></div>';
    banner.addEventListener("click", function (e) {
      var b = e.target.closest ? e.target.closest("button[data-c]") : null;
      if (b) choose(b.getAttribute("data-c"));
    });
    document.body.appendChild(banner);
  }

  function addFooterLink() {
    var nav = document.querySelector('footer nav[aria-label="Informations"]');
    if (!nav || nav.querySelector("[data-consent-open]")) return;
    var a = document.createElement("a");
    a.href = "#cookies";
    a.setAttribute("data-consent-open", "");
    a.textContent = "Gérer la mesure publicitaire";
    a.addEventListener("click", function (e) { e.preventDefault(); show(); });
    nav.appendChild(a);
    var s = document.createElement("span");
    s.id = "consent-status";
    s.setAttribute("role", "status");
    s.style.cssText = "position:absolute;left:-9999px";
    nav.appendChild(s);
  }

  function init() {
    addFooterLink();
    var v = read();
    if (v === "accepted") loadGoogle();
    else if (v === null) show();
    /* Événements fournis par la page du scan (sans aucune donnée). */
    document.addEventListener("trivoie:scan-complete", function () { track("scan"); });
    /* Clic vers la prise de rendez-vous, sur toutes les pages. */
    document.addEventListener("click", function (e) {
      var a = e.target.closest ? e.target.closest('a[href*="calendly.com"]') : null;
      if (a) track("call");
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
