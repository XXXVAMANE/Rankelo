/* Rankelo site script: header, mobile menu, hero local-pack demo, pointer effects, request form. */
(function () {
  "use strict";
  var reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
  var fine = matchMedia("(pointer: fine)").matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var I18N = {};
  try { I18N = JSON.parse(($("#rk-i18n") || {}).textContent || "{}"); } catch (_) {}
  var t = function (k) { return I18N[k] || k; };

  /* ---------- header & menu ---------- */
  var hdr = $("header.site");
  if (hdr) addEventListener("scroll", function () { hdr.classList.toggle("scrolled", scrollY > 8); }, { passive: true });
  var burger = $(".burger"), mnav = $(".mnav");
  function setMenu(open) {
    if (!burger || !mnav) return;
    burger.setAttribute("aria-expanded", String(open));
    burger.setAttribute("aria-label", open ? t("close") : t("menu"));
    mnav.classList.toggle("open", open);
    mnav.setAttribute("aria-hidden", String(!open));
    document.body.classList.toggle("menu-open", open);
  }
  if (burger) {
    burger.addEventListener("click", function () { setMenu(burger.getAttribute("aria-expanded") !== "true"); });
    $$("a", mnav).forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
    addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });
    addEventListener("resize", function () { if (innerWidth > 940) setMenu(false); });
  }
  var yr = $("#yr"); if (yr) yr.textContent = new Date().getFullYear();

  /* ---------- hero: type a search, then climb to #1 (cycles through examples) ---------- */
  var pack = $("#pack");
  if (pack) {
    var seq = [];
    try { seq = JSON.parse(pack.getAttribute("data-seq") || "[]"); } catch (_) {}
    var q = $("#qtext"), list = $("#list");
    var you = $(".biz.you", list);
    var rivals = $$(".biz:not(.you)", list);
    var timer = null;
    var wait = function (ms) { return new Promise(function (r) { timer = setTimeout(r, ms); }); };
    function setItem(item) {
      rivals.forEach(function (el, i) {
        var r = item.rivals[i]; if (!r) return;
        $(".nm-t", el).textContent = r[0];
        $(".rt", el).textContent = r[1] + " · " + r[2];
      });
      $(".nm-t", you).textContent = item.you;
      list.appendChild(rivals[0]); list.appendChild(rivals[1]); list.appendChild(you);
      $$(".biz", list).forEach(function (el, i) { $(".n", el).textContent = i + 1; });
    }
    function climb() {
      var items = $$(".biz", list);
      var first = new Map(items.map(function (el) { return [el, el.getBoundingClientRect().top]; }));
      list.insertBefore(you, list.firstChild);
      $$(".biz", list).forEach(function (el, i) { $(".n", el).textContent = i + 1; });
      if (reduce) return;
      $$(".biz", list).forEach(function (el) {
        var dy = first.get(el) - el.getBoundingClientRect().top;
        el.animate([{ transform: "translateY(" + dy + "px)" }, { transform: "none" }], { duration: 900, easing: "cubic-bezier(.2,.8,.2,1)" });
      });
      you.animate([{ boxShadow: "0 0 0 0 rgba(255,181,71,.7)" }, { boxShadow: "0 0 0 12px rgba(255,181,71,0)" }], { duration: 900, delay: 700 });
    }
    async function type(text) {
      q.textContent = "";
      for (var i = 1; i <= text.length; i++) { q.textContent = text.slice(0, i); await wait(45 + Math.random() * 55); }
    }
    // Plays once per page load: type a search, then move the client's business to #1 and stop there.
    // On pages with several examples (home), a random one is shown on each load.
    async function run() {
      if (!seq.length) return;
      var item = seq[Math.floor(Math.random() * seq.length)];
      setItem(item);
      if (reduce) { q.textContent = item.q; climb(); return; }
      q.textContent = "";
      await wait(500);
      await type(item.q);
      await wait(650);
      climb();
    }
    run();
    if (fine && !reduce) {
      pack.addEventListener("pointermove", function (e) {
        var r = pack.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
        pack.style.transform = "perspective(900px) rotateY(" + (x * 6) + "deg) rotateX(" + (-y * 6) + "deg)";
      });
      pack.addEventListener("pointerleave", function () { pack.style.transform = ""; });
    }
  }

  /* ---------- pointer effects ---------- */
  if (fine && !reduce) {
    $$(".card").forEach(function (el) {
      el.addEventListener("pointermove", function (e) {
        var r = el.getBoundingClientRect();
        el.style.setProperty("--mx", (e.clientX - r.left) + "px");
        el.style.setProperty("--my", (e.clientY - r.top) + "px");
      });
    });
    $$("[data-magnet]").forEach(function (el) {
      el.addEventListener("pointermove", function (e) {
        var r = el.getBoundingClientRect(), x = e.clientX - r.left - r.width / 2, y = e.clientY - r.top - r.height / 2;
        el.style.transform = "translate(" + (x * .18) + "px," + (y * .3) + "px)";
      });
      el.addEventListener("pointerleave", function () { el.style.transform = ""; });
    });
  }

  /* ---------- request form (Web3Forms) ---------- */
  var form = $("#lead-form");
  if (!form) return;
  var key = form.querySelector('input[name="access_key"]').value;
  var LIVE = !/^YOUR_/.test(key) && /^https?:$/.test(location.protocol) && !/localhost|127\.0\.0\.1|claude/.test(location.hostname);
  var site = $("#f-site"), nosite = $("#f-nosite"), service = $("#f-service");
  function syncSite() { site.disabled = nosite.checked; if (nosite.checked) { site.value = ""; clr("site"); } }
  nosite.addEventListener("change", function () {
    syncSite();
    if (nosite.checked) service.value = "site"; else if (service.value === "site") service.value = "seo";
  });
  function pick(v) {
    if (!v || !service.querySelector('option[value="' + v + '"]')) return;
    service.value = v; nosite.checked = (v === "site"); syncSite();
  }
  $$("[data-pick]").forEach(function (a) {
    a.addEventListener("click", function () {
      pick(a.getAttribute("data-pick"));
      setTimeout(function () { $("#f-name").focus({ preventScroll: true }); }, 700);
    });
  });
  try { pick(new URLSearchParams(location.search).get("service")); } catch (_) {}
  function err(id, msg) {
    $("#e-" + id).textContent = msg;
    var f = $("#f-" + id); if (f) { f.classList.remove("invalid"); void f.offsetWidth; f.classList.add("invalid"); }
  }
  function clr(id) { $("#e-" + id).textContent = ""; var f = $("#f-" + id); if (f) f.classList.remove("invalid"); }
  ["name", "email", "site"].forEach(function (id) { $("#f-" + id).addEventListener("input", function () { clr(id); }); });
  var btn = $("#f-submit"), btnHTML = btn.innerHTML;
  function busy(on) {
    btn.disabled = on;
    btn.innerHTML = on ? '<span class="spin" aria-hidden="true"></span><span>' + t("sending") + "</span>" : btnHTML;
  }
  function showDone(preview) {
    busy(false); form.hidden = true;
    $("#d-preview").hidden = !preview; $("#done").hidden = false;
  }
  form.addEventListener("submit", async function (ev) {
    ev.preventDefault();
    ["name", "email", "site"].forEach(clr); $("#e-form").textContent = "";
    var fd = new FormData(form), ok = true, first = null;
    if (!String(fd.get("name") || "").trim()) { err("name", t("err_name")); ok = false; first = first || "f-name"; }
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(fd.get("email") || "").trim())) { err("email", t("err_email")); ok = false; first = first || "f-email"; }
    if (!nosite.checked && !site.value.trim()) { err("site", t("err_site")); ok = false; first = first || "f-site"; }
    if (!ok) { $("#" + first).focus(); return; }
    fd.set("need_website", nosite.checked ? "yes" : "no");
    fd.set("page", location.pathname);
    busy(true);
    if (!LIVE) { setTimeout(function () { showDone(true); }, 700); return; }
    // Copy of the request to Google Sheets (Apps Script web app). Fire-and-forget: email is the source of truth.
    var sheetUrl = form.getAttribute("data-sheet");
    if (sheetUrl && !fd.get("botcheck")) {
      var sp = new URLSearchParams(fd); sp.delete("access_key"); sp.delete("subject"); sp.delete("from_name");
      try { fetch(sheetUrl, { method: "POST", mode: "no-cors", keepalive: true, body: sp }).catch(function () {}); } catch (_) {}
    }
    try {
      var r = await fetch("https://api.web3forms.com/submit", {
        method: "POST", headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify(Object.fromEntries(fd))
      });
      if (!r.ok) throw new Error(r.status);
      showDone(false);
    } catch (_) { $("#e-form").textContent = t("err_send"); busy(false); }
  });
})();
