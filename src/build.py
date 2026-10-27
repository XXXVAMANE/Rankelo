"""Build the Rankelo static site (EN at /, ES at /es/) into ./out and zip it.

Usage: python3 src/build.py [SITE_URL] [WEB3FORMS_KEY]
The Web3Forms access key is passed at build time and is not stored in this repository.
"""
import json, html, shutil, sys, math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from content import T, SLUGS, SERVICES, PACKAGES, PKG_UI, STEPS, PROMISES, FAQ, PAGES, PATHS, PHONE_DISPLAY, PHONE_E164, AREAS
from niches_v2 import NICHES

SITE = (sys.argv[1] if len(sys.argv) > 1 else "https://rankelo.org").rstrip("/")
KEY = sys.argv[2] if len(sys.argv) > 2 else "YOUR_WEB3FORMS_KEY"
OUT = HERE.parent / "dist"
FONTS = HERE.parent / "fonts"  # Unbounded + Manrope (SIL OFL), used for social preview images
VER = "8"  # cache-buster for css/js
LANGS = ("en", "es")
e = html.escape

LOGO = ('<svg width="{s}" height="{s}" viewBox="0 0 30 30" aria-hidden="true"><rect x="2" y="2" width="26" height="26" rx="6.5" fill="#FFB547"/>'
        '<rect x="7.6" y="16" width="4" height="7" rx="1.5" fill="#1A1205"/><rect x="13" y="11.5" width="4" height="11.5" rx="1.5" fill="#1A1205"/>'
        '<rect x="18.4" y="7" width="4" height="16" rx="1.5" fill="#1A1205"/></svg>')

ICONS = {
    "gbp": '<path d="M3 21h18M5 21V9l7-5 7 5v12M9 21v-6h6v6"/>',
    "maps": '<path d="M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>',
    "reviews": '<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
    "citations": '<path d="M4 6h16M4 12h16M4 18h10"/>',
    "pages": '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V9z"/><path d="M14 3v6h6M8 13h8M8 17h5"/>',
    "web": '<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M8 21h8M7 9l2.5 2L7 13M12 13h4"/>',
    "reports": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "restaurants": '<path d="M7 3v8a2 2 0 0 0 2 2v8M11 3v8a2 2 0 0 1-2 2M17 21V3c-2 1-3 3.5-3 7s1.5 4 3 4"/>',
    "roofers": '<path d="M3 11 12 4l9 7M5 10v10h14V10M10 20v-5h4v5"/>',
    "dentists": '<path d="M12 5c-1.5-1.5-5-2-6.5.5S5 11 6 14s1.5 7 3 7 1.5-5 3-5 1.5 5 3 5 2-4 3-7 2-6 .5-8.5S13.5 3.5 12 5z"/>',
    "hvac": '<path d="M12 3v18M4.5 7.5l15 9M19.5 7.5l-15 9"/><circle cx="12" cy="12" r="2.5"/>',
}


def icon(k, size=22):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[k]}</svg>')


def path(lang, key):
    return "/" + SLUGS[key][lang]


def npath(lang, n):
    return "/" + n["slug"][lang]


def h1(parts, cls=""):
    return f'<h1{cls}>{e(parts[0])} <em>{e(parts[1])}</em></h1>'


# ------------------------------------------------------------------ shared chrome
def head(lang, title, desc, url_path, alts, ld, og):
    alt_html = ""
    if alts:
        alt_html = "".join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{p}">\n' for l, p in alts.items())
        alt_html += f'<link rel="alternate" hreflang="x-default" href="{SITE}{alts["en"]}">\n'
    other = "es_US" if lang == "en" else "en_US"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{SITE}{url_path}">
{alt_html}<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#FFFFFF">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Rankelo">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{SITE}{url_path}">
<meta property="og:image" content="{SITE}/{og}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{T[lang]['locale']}">
<meta property="og:locale:alternate" content="{other}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}/{og}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@500;700&family=Manrope:wght@400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap">
<link rel="stylesheet" href="/assets/site.css?v={VER}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
<body>
"""


def header(lang, current, alts):
    tx = T[lang]
    links = "".join(
        f'<a href="{path(lang, k)}"{" aria-current=\"page\"" if k == current else ""}>{e(lbl)}</a>' for k, lbl in tx["nav"])
    mlinks = "".join(f'<a class="m" href="{path(lang, k)}">{e(lbl)}</a>' for k, lbl in tx["nav"])
    sw = "".join(
        f'<a href="{alts.get(l, path(l, "home"))}" hreflang="{l}" lang="{l}"{" aria-current=\"page\"" if l == lang else ""}>{l.upper()}</a>'
        for l in LANGS)
    return f"""<a class="skip" href="#main">{e(tx['skip'])}</a>
<header class="site">
  <div class="wrap nav">
    <a class="logo" href="{path(lang, 'home')}" aria-label="Rankelo">{LOGO.format(s=30)}Rankelo</a>
    <nav class="nav-links" aria-label="Main">{links}</nav>
    <div class="nav-right">
      <div class="lang" data-active="{lang}" role="group" aria-label="Language">{sw}</div>
      <a class="btn btn-dark btn-cta" href="{path(lang, 'contact')}">{e(tx['cta'])}</a>
      <button class="burger" type="button" aria-expanded="false" aria-controls="mnav" aria-label="{e(tx['menu'])}"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<nav class="mnav" id="mnav" aria-label="Mobile" aria-hidden="true">{mlinks}<a class="btn btn-dark" href="{path(lang, 'contact')}">{e(tx['cta'])} <span class="arr" aria-hidden="true">→</span></a></nav>
"""


def footer(lang):
    tx = T[lang]
    comp = "".join(f'<li><a href="{path(lang, k)}">{e(lbl)}</a></li>' for k, lbl in tx["nav"] if k in ("about", "pricing", "faq"))
    comp += f'<li><a href="{path(lang, "contact")}">{e(tx["foot_contact_page"])}</a></li>'
    svc = "".join(f'<li><a href="{path(lang, k)}#{a}">{e(lbl)}</a></li>' for lbl, k, a in tx["svc_links"])
    ind = "".join(f'<li><a href="{npath(lang, n)}">{e(n[lang]["name"])}</a></li>' for n in NICHES)
    return f"""<footer class="site">
  <div class="wrap">
    <div class="foot">
      <div><a class="logo" href="{path(lang, 'home')}">{LOGO.format(s=28)}Rankelo</a><p>{e(tx['foot_tag'])}</p></div>
      <div><h4>{e(tx['foot_company'])}</h4><ul>{comp}</ul></div>
      <div><h4>{e(tx['foot_services'])}</h4><ul>{svc}</ul></div>
      <div><h4>{e(tx['foot_industries'])}</h4><ul>{ind}</ul></div>
      <div><h4>{e(tx['foot_contact'])}</h4><ul>
        <li><a href="tel:{PHONE_E164}">{PHONE_DISPLAY}</a></li>
        <li>{e(tx['hours'])}</li>
        <li>{e(' · '.join(AREAS))}, FL</li>
      </ul></div>
    </div>
    <div class="foot-bot"><span>© <span id="yr">2026</span> Rankelo. {e(tx['rights'])}</span><span>rankelo.org</span></div>
  </div>
</footer>
"""


def i18n_script(lang):
    f = T[lang]["f"]
    data = dict(menu=T[lang]["menu"], close=T[lang]["close"], sending=f["sending"],
                err_name=f["err_name"], err_email=f["err_email"], err_site=f["err_site"], err_send=f["err_send"])
    return (f'<script type="application/json" id="rk-i18n">{json.dumps(data, ensure_ascii=False)}</script>\n'
            f'<script src="/assets/site.js?v={VER}" defer></script>\n</body>\n</html>\n')


# ------------------------------------------------------------------ components
def pack(lang, seq):
    p = T[lang]["pack"]
    first = seq[0]
    rivals = "".join(
        f'<div class="biz"><span class="n">{i + 1}</span><span class="nm"><span class="nm-t">{e(r[0])}</span>'
        f'<span class="meta"><span class="st">★★★★</span>☆ <span class="rt">{r[1]} · {r[2]}</span></span></span><span class="tag"></span></div>'
        for i, r in enumerate(first["rivals"]))
    you = (f'<div class="biz you"><span class="n">3</span><span class="nm"><span class="nm-t">{e(first["you"])}</span>'
           f'<span class="meta"><span class="st">★★★★★</span> 4.9 · 0.6 mi</span></span><span class="tag">{e(p["tag"])}</span></div>')
    seq_attr = e(json.dumps(seq, ensure_ascii=False))
    return f"""<div class="pack" id="pack" data-seq="{seq_attr}" aria-label="{e(p['label'])}">
  <div class="q"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><span class="q-text" id="qtext">{e(first['q'])}</span><span class="caret" aria-hidden="true"></span></div>
  <div class="map"><svg viewBox="0 0 360 140" aria-hidden="true">
    <rect width="360" height="140" fill="#F1F1EE"/>
    <path d="M-10 92 C 60 70, 120 120, 190 96 S 320 60, 380 84" stroke="#DCE9F2" stroke-width="16" fill="none"/>
    <g stroke="#FFFFFF" stroke-width="6" fill="none" stroke-linecap="round"><path d="M0 30 H360"/><path d="M0 128 H360"/><path d="M70 0 V140"/><path d="M175 0 V140"/><path d="M285 0 V140"/><path d="M0 0 L140 140"/></g>
    <g stroke="#E4E4DF" stroke-width="2" fill="none"><path d="M0 60 H360"/><path d="M120 0 V140"/><path d="M230 0 V140"/><path d="M330 0 V140"/></g>
    <g class="pin-drop" style="animation-delay:.5s"><path d="M245 52c-6 0-10 4.5-10 10 0 7.5 10 18 10 18s10-10.5 10-18c0-5.5-4-10-10-10z" fill="#BDBDB8"/><text x="245" y="66" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="9" font-weight="600" fill="#FFFFFF">2</text></g>
    <g class="pin-drop" style="animation-delay:.7s"><path d="M95 70c-6 0-10 4.5-10 10 0 7.5 10 18 10 18s10-10.5 10-18c0-5.5-4-10-10-10z" fill="#BDBDB8"/><text x="95" y="84" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="9" font-weight="600" fill="#FFFFFF">3</text></g>
    <circle class="pin-pulse" cx="180" cy="68" r="12" fill="#FFB547"/>
    <g class="pin-drop" style="animation-delay:.9s"><path d="M180 38c-8 0-13 6-13 13 0 10 13 23 13 23s13-13 13-23c0-7-5-13-13-13z" fill="#0C0C0D"/><circle cx="180" cy="51" r="5" fill="#FFB547"/></g>
  </svg></div>
  <div class="list" id="list">{rivals}{you}</div>
  <div class="pack-foot"><span class="delta">{e(p['delta'])}</span><span class="pack-note">{e(p['note'])}</span></div>
  <div class="float"><span>{e(p['calls'])}</span><b>{e(p['more'])}</b></div>
</div>"""


def seq_for(lang, niches):
    return [dict(q=n[lang]["query"], rivals=n[lang]["rivals"], you=n[lang]["you"]) for n in niches]


def form(lang, niche_name=None, eb=None, h2=None, lead=None, steps=None, side_extra="", sec_id="contact"):
    f = T[lang]["f"]
    svc_opts = "".join(f'<option value="{v}">{e(l)}</option>' for v, l in f["services"])
    bud_opts = "".join(f'<option value="{e(v)}">{e(l)}</option>' for v, l in f["budgets"])
    niche_in = f'<input type="hidden" name="niche" value="{e(niche_name)}">' if niche_name else ""
    steps_html = ("<ol class=\"olist\">" + "".join(f"<li>{e(s)}</li>" for s in steps) + "</ol>") if steps else ""
    opt = f'<span class="opt">{e(f["opt"])}</span>'
    side = f"""<div class="contact-side reveal">
      {f'<p class="eyebrow">{e(eb)}</p>' if eb else ''}
      {f'<h2>{e(h2)}</h2>' if h2 else ''}
      {f'<p class="lead">{e(lead)}</p>' if lead else ''}
      {steps_html}{side_extra}
    </div>"""
    return f"""<section id="{sec_id}">
  <div class="wrap contact-grid">
    {side}
    <div class="form-card reveal">
      <form id="lead-form" novalidate>
        <input type="hidden" name="access_key" value="{e(KEY)}">
        <input type="hidden" name="subject" value="{e(f['subject'])}">
        <input type="hidden" name="from_name" value="Rankelo website">
        <input type="hidden" name="language" value="{lang}">
        {niche_in}
        <input type="checkbox" name="botcheck" tabindex="-1" autocomplete="off" style="display:none" aria-hidden="true">
        <div class="row">
          <div class="field"><label for="f-name">{e(f['name'])}</label><input id="f-name" name="name" autocomplete="name" placeholder="{e(f['name_ph'])}" required><span class="err" id="e-name"></span></div>
          <div class="field"><label for="f-company">{e(f['company'])} {opt}</label><input id="f-company" name="company" autocomplete="organization" placeholder="{e(f['company_ph'])}"></div>
        </div>
        <div class="row">
          <div class="field"><label for="f-email">{e(f['email'])}</label><input id="f-email" name="email" type="email" autocomplete="email" placeholder="you@company.com" required><span class="err" id="e-email"></span></div>
          <div class="field"><label for="f-phone">{e(f['phone'])} {opt}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" placeholder="+1 (555) 000-0000"></div>
        </div>
        <div class="row">
          <div class="field"><label for="f-site">{e(f['site'])}</label><input id="f-site" name="website" inputmode="url" placeholder="www.yourbusiness.com">
            <label class="check" for="f-nosite"><input type="checkbox" id="f-nosite" name="no_website_box"><span>{e(f['nosite'])}</span></label><span class="err" id="e-site"></span></div>
          <div class="field"><label for="f-city">{e(f['city'])}</label><input id="f-city" name="city" autocomplete="address-level2" placeholder="{e(f['city_ph'])}"></div>
        </div>
        <div class="row">
          <div class="field"><label for="f-service">{e(f['service'])}</label><select id="f-service" name="service">{svc_opts}</select></div>
          <div class="field"><label for="f-budget">{e(f['budget'])}</label><select id="f-budget" name="budget">{bud_opts}</select></div>
        </div>
        <div class="field"><label for="f-msg">{e(f['msg'])} {opt}</label><textarea id="f-msg" name="message" placeholder="{e(f['msg_ph'])}"></textarea></div>
        <div class="form-foot"><small>{e(f['privacy'])}</small>
          <button class="btn btn-dark" type="submit" id="f-submit"><span>{e(f['submit'])}</span><span class="arr" aria-hidden="true">→</span></button></div>
        <p class="err" id="e-form" role="alert"></p>
      </form>
      <div class="done" id="done" hidden>
        <svg width="64" height="64" viewBox="0 0 64 64" fill="none" aria-hidden="true"><circle cx="32" cy="32" r="27" stroke="#14955A" stroke-width="3"/><path d="M21 33l7 7 15-15" stroke="#14955A" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        <h3>{e(f['done_t'])}</h3><p>{e(f['done_d'])}</p><p id="d-preview" hidden>{e(f['preview'])}</p>
      </div>
    </div>
  </div>
</section>"""


def band(lang, text=None, cta=None, href=None):
    tx = T[lang]
    return f"""<section class="tight"><div class="wrap"><div class="band reveal">
  <h2>{e(text or tx['band_t'])}</h2>
  <a class="btn btn-gold" href="{href or path(lang, 'contact')}" data-magnet><span>{e(cta or tx['band_cta'])}</span><span class="arr" aria-hidden="true">→</span></a>
</div></div></section>"""


def sec_head(eb, h, lead=None, more=None):
    lead_html = f'<p class="lead">{e(lead)}</p>' if lead else ""
    inner = f'<div class="sec-head reveal"><p class="eyebrow">{e(eb)}</p><h2>{e(h)}</h2>{lead_html}</div>'
    if more:
        return f'<div class="sec-row">{inner}<a class="link reveal" href="{more[1]}">{e(more[0])} <span class="arr" aria-hidden="true">→</span></a></div>'
    return inner


def ticks(items):
    return '<ul class="ticks">' + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"


def faq_items(qs):
    return "".join(f"<details><summary>{e(q)}</summary><p>{e(a)}</p></details>" for q, a in qs)


def packages(lang):
    ui = PKG_UI[lang]
    out = []
    for i, p in enumerate(PACKAGES[lang]):
        dark = " dark" if p["featured"] else ""
        btn = "btn-gold" if p["featured"] else "btn-dark"
        out.append(f"""<div class="pkg card{dark} reveal">
  <div class="pkg-top"><span class="pkg-code">0{i + 1}</span><span class="pkg-badge">{e(p['tag'])}</span></div>
  <h3>{e(p['t'])}</h3><p class="pkg-for">{e(p['f'])}</p>{ticks(p['pts'])}
  <p class="pkg-price">{e(ui['price'])}</p>
  <a class="btn {btn}" href="{path(lang, 'contact')}?service={p['key']}"><span>{e(ui['cta'])}</span><span class="arr" aria-hidden="true">→</span></a>
</div>""")
    return '<div class="pkgs">' + "".join(out) + "</div>"


def industry_cards(lang, go):
    return '<div class="ind-grid">' + "".join(
        f'<a class="ind card reveal" href="{npath(lang, n)}"><span class="ico">{icon(n["key"])}</span>'
        f'<span class="ind-q">&ldquo;{e(n[lang]["query"])}&rdquo;</span><h3>{e(n[lang]["name"])}</h3>'
        f'<span class="ind-go">{e(go)} <span class="arr" aria-hidden="true">→</span></span></a>' for n in NICHES) + "</div>"


def business_node():
    return {
        "@type": "ProfessionalService", "@id": f"{SITE}/#business", "name": "Rankelo",
        "url": f"{SITE}/", "logo": f"{SITE}/apple-touch-icon.png", "image": f"{SITE}/og-image.png",
        "description": PAGES["en"]["home"]["desc"], "telephone": PHONE_E164,
        "areaServed": [{"@type": "City", "name": f"{c}, FL"} for c in AREAS],
        "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                                       "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                                       "opens": "09:00", "closes": "20:00"}],
        "knowsLanguage": ["en", "es"],
        "serviceType": ["Local SEO", "Google Business Profile optimization", "Website design"],
    }


def ld_graph(lang, url_path, title, desc, crumbs=None, extra=()):
    g = [business_node(),
         {"@type": "WebSite", "@id": f"{SITE}/#website", "name": "Rankelo", "url": f"{SITE}/", "inLanguage": list(LANGS),
          "publisher": {"@id": f"{SITE}/#business"}},
         {"@type": "WebPage", "url": f"{SITE}{url_path}", "name": title, "description": desc, "inLanguage": lang,
          "isPartOf": {"@id": f"{SITE}/#website"}}]
    if crumbs:
        g.append({"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": f"{SITE}{p}"} for i, (n, p) in enumerate(crumbs)]})
    g.extend(extra)
    return {"@context": "https://schema.org", "@graph": g}


def faq_ld(url_path, lang, qs):
    return {"@type": "FAQPage", "url": f"{SITE}{url_path}", "inLanguage": lang,
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qs]}


def crumbs_html(items):
    parts = []
    for i, (n, p) in enumerate(items):
        parts.append(f'<a href="{p}">{e(n)}</a>' if i < len(items) - 1 else f'<span>{e(n)}</span>')
    return '<nav class="crumbs in" style="--i:0" aria-label="Breadcrumb">' + '<span aria-hidden="true">/</span>'.join(parts) + "</nav>"


def page_hero(lang, eb, h, lead, crumbs, extra=""):
    return f"""<div class="phero"><div class="hero-bg"><div class="glow"></div></div><div class="wrap">
  {crumbs_html(crumbs)}
  {h1(h, ' class="in" style="--i:1"')}
  <p class="lead in" style="--i:2">{e(lead)}</p>{extra}
</div></div>"""


def og_for(lang):
    return "og-image.png" if lang == "en" else "og-image-es.png"


# ------------------------------------------------------------------ pages
def page_home(lang):
    tx, P = T[lang], PAGES[lang]["home"]
    url = path(lang, "home")
    alts = {l: path(l, "home") for l in LANGS}
    faq_short = FAQ[lang][0][1][:1] + FAQ[lang][1][1][:2]
    paths_html = "".join(f"""<article class="path card{' dark' if p['featured'] else ''} reveal">
  <span class="path-tag">{e(p['tag'])}</span><h3>{e(p['t'])}</h3><p class="lead">{e(p['lead'])}</p>{ticks(p['pts'])}
  <a class="btn {'btn-gold' if p['featured'] else 'btn-dark'}" href="#contact" data-pick="{p['pick']}"><span>{e(p['cta'])}</span><span class="arr" aria-hidden="true">→</span></a>
</article>""" for p in PATHS[lang])
    svcs = [s for s in SERVICES[lang] if s["id"] != "reports"]
    svc_html = "".join(f"""<a class="svc card reveal" href="{path(lang, 'services')}#{s['id']}"><span class="ico">{icon(s['id'])}</span><code>{s['code']}</code><h3>{e(s['t'])}</h3><p>{e(s['short'])}</p></a>""" for s in svcs)
    steps_html = "".join(f'<div class="step reveal"><span class="step-n">0{i + 1}</span><span class="step-t">{e(w)}</span><h3>{e(t_)}</h3><p>{e(d)}</p></div>'
                         for i, (w, t_, d) in enumerate(STEPS[lang]))
    prom = "".join(f'<div class="promise card reveal"><b>{e(a)}</b><p>{e(b)}</p></div>' for a, b in PROMISES[lang])
    mq = "".join(f"<li>{e(m)}</li>" for m in P["marquee"])
    body = f"""<main id="main">
<div class="hero">
  <div class="hero-bg"><div class="glow"></div></div>
  <div class="wrap hero-grid">
    <div>
      <span class="badge in" style="--i:0"><b>{e(P['badge'][0])}</b><span>{e(P['badge'][1])}</span></span>
      {h1(P['h1'], ' class="in" style="--i:1"')}
      <p class="lead in" style="--i:2">{e(P['lead'])}</p>
      <div class="hero-ctas in" style="--i:3">
        <a class="btn btn-dark shine" href="{path(lang, 'contact')}" data-magnet><span>{e(P['cta1'])}</span><span class="arr" aria-hidden="true">→</span></a>
        <a class="btn btn-ghost" href="{path(lang, 'services')}" data-magnet><span>{e(P['cta2'])}</span></a>
      </div>
      <div class="hero-meta in" style="--i:4">{''.join(f'<span>{e(m)}</span>' for m in tx['meta_bar'])}</div>
    </div>
    <div class="in" style="--i:2">{pack(lang, seq_for(lang, NICHES))}</div>
  </div>
</div>
<div class="marquee" aria-hidden="true"><div class="track"><ul>{mq}</ul><ul>{mq}</ul></div></div>
<section><div class="wrap">{sec_head(P['paths_eb'], P['paths_h'])}<div class="paths">{paths_html}</div></div></section>
<section class="alt"><div class="wrap">{sec_head(P['svc_eb'], P['svc_h'], more=(P['svc_all'], path(lang, 'services')))}<div class="svc-grid">{svc_html}</div>
  <div class="soon reveal"><b>{e(P['soon'][0])}</b><span>{e(P['soon'][1])}</span></div></div></section>
<section><div class="wrap">{sec_head(P['steps_eb'], P['steps_h'])}<div class="steps">{steps_html}</div></div></section>
<section class="alt"><div class="wrap">{sec_head(P['ind_eb'], P['ind_h'], more=(P['ind_all'], path(lang, 'industries')))}{industry_cards(lang, P['ind_go'])}</div></section>
<section><div class="wrap">{sec_head(P['pk_eb'], P['pk_h'], P['pk_lead'], more=(P['pk_all'], path(lang, 'pricing')))}{packages(lang)}</div></section>
<section class="tight"><div class="wrap promises">{prom}</div></section>
<section class="alt"><div class="wrap faq-grid">
  <div>{sec_head(P['faq_eb'], P['faq_h'])}<a class="link reveal" href="{path(lang, 'faq')}">{e(P['faq_all'])} <span class="arr" aria-hidden="true">→</span></a></div>
  <div class="faq reveal">{faq_items(faq_short)}</div>
</div></section>
{form(lang, eb=P['c_eb'], h2=P['c_h'], lead=P['c_lead'], steps=P['c_steps'])}
{band(lang)}
</main>"""
    ld = ld_graph(lang, url, P["title"], P["desc"], extra=[faq_ld(url, lang, faq_short)])
    return url, alts, head(lang, P["title"], P["desc"], url, alts, ld, og_for(lang)) + header(lang, "home", alts) + body + footer(lang) + i18n_script(lang)


def simple_page(lang, key, body_fn, extra_ld=()):
    P = PAGES[lang][key]
    url = path(lang, key)
    alts = {l: path(l, key) for l in LANGS}
    crumbs = [(T[lang]["home"], path(lang, "home")), (P["eb"], url)]
    hero = page_hero(lang, P["eb"], P["h1"], P["lead"], crumbs)
    body = f'<main id="main">{hero}{body_fn(lang, P)}</main>'
    ld = ld_graph(lang, url, P["title"], P["desc"], crumbs=crumbs, extra=[x(url, lang) for x in extra_ld])
    return url, alts, head(lang, P["title"], P["desc"], url, alts, ld, og_for(lang)) + header(lang, key, alts) + body + footer(lang) + i18n_script(lang)


def body_services(lang, P):
    items = "".join(f"""<article class="sd reveal" id="{s['id']}">
  <div class="sd-h"><span class="sd-n">0{i + 1} · {s['code']}</span><span class="ico">{icon(s['id'])}</span><h2>{e(s['t'])}</h2></div>
  <div class="sd-b"><p class="lead">{e(s['lead'])}</p><span class="lbl">{e(P['incl'])}</span>{ticks(s['pts'])}</div>
</article>""" for i, s in enumerate(SERVICES[lang]))
    soon = PAGES[lang]["home"]["soon"]
    return f"""<section><div class="wrap">{items}<div class="soon reveal"><b>{e(soon[0])}</b><span>{e(soon[1])}</span></div></div></section>
<section class="alt"><div class="wrap">{sec_head(PAGES[lang]['home']['pk_eb'], PAGES[lang]['home']['pk_h'], PAGES[lang]['home']['pk_lead'], more=(PAGES[lang]['home']['pk_all'], path(lang, 'pricing')))}{packages(lang)}</div></section>
{band(lang)}"""


def body_industries(lang, P):
    more = "".join(f'<span class="chip">{e(m)}</span>' for m in P["more"])
    return f"""<section><div class="wrap">{industry_cards(lang, PAGES[lang]['home']['ind_go'])}</div></section>
<section class="tight"><div class="wrap"><div class="sec-head reveal"><h2>{e(P['more_h'])}</h2><p class="lead">{e(P['more_p'])}</p></div>
<div class="chips reveal">{more}</div></div></section>
{band(lang)}"""


def body_pricing(lang, P):
    how = "".join(f'<div class="num card reveal"><b>{e(a)}</b><p>{e(b)}</p></div>' for a, b in P["how"])
    pr_faq = FAQ[lang][2][1]
    return f"""<section><div class="wrap">{packages(lang)}</div></section>
<section class="alt"><div class="wrap">{sec_head(P['eb'], P['how_h'])}<div class="nums">{how}</div></div></section>
<section><div class="wrap two">
  <div class="sec-head reveal"><h2>{e(P['affects_h'])}</h2></div>
  <div class="reveal">{ticks(P['affects'])}</div>
</div></section>
<section class="tight"><div class="wrap faq-grid">
  <div>{sec_head(PAGES[lang]['home']['faq_eb'], FAQ[lang][2][0])}<a class="link reveal" href="{path(lang, 'faq')}">{e(PAGES[lang]['home']['faq_all'])} <span class="arr" aria-hidden="true">→</span></a></div>
  <div class="faq reveal">{faq_items(pr_faq)}</div>
</div></section>
{band(lang)}"""


def body_about(lang, P):
    why = "".join(f"<p>{e(x)}</p>" for x in P["why"])
    prom = "".join(f'<div class="promise card reveal"><b>{e(a)}</b><p>{e(b)}</p></div>' for a, b in PROMISES[lang])
    return f"""<section><div class="wrap two">
  <div class="sec-head reveal"><h2>{e(P['why_h'])}</h2></div><div class="prose reveal">{why}</div>
</div></section>
<section class="alt"><div class="wrap">{sec_head(P['eb'], P['how_h'])}<div class="promises">{prom}</div></div></section>
<section><div class="wrap two">
  <div class="sec-head reveal"><h2>{e(P['who_h'])}</h2></div><div class="prose reveal"><p>{e(P['who'])}</p>
  <div class="chips">{''.join(f'<a class="chip" href="{npath(lang, n)}">{e(n[lang]["name"])}</a>' for n in NICHES)}</div></div>
</div></section>
<section class="tight"><div class="wrap two">
  <div class="sec-head reveal"><h2>{e(P['team_h'])}</h2></div><div class="prose reveal"><p>{e(P['team'])}</p></div>
</div></section>
{band(lang)}"""


def body_faq(lang, P):
    cats = "".join(f'<p class="faq-cat">{e(c)}</p>{faq_items(qs)}' for c, qs in FAQ[lang])
    return f"""<section><div class="wrap"><div class="faq reveal" style="max-width:860px">{cats}</div></div></section>
{band(lang)}"""


def faq_all_ld(url, lang):
    return faq_ld(url, lang, [q for _, qs in FAQ[lang] for q in qs])


def body_contact(lang, P):
    tx = T[lang]
    info = f"""<div class="info">
  <div><small>{e(P['phone_h'])}</small><a href="tel:{PHONE_E164}">{PHONE_DISPLAY}</a></div>
  <div><small>{e(P['hours_h'])}</small><span>{e(tx['hours'])}</span></div>
  <div><small>{e(tx['areas_label'])}</small><span>{e(', '.join(AREAS))}, FL</span></div>
</div>"""
    return form(lang, h2=P["next_h"], steps=P["next"], side_extra=info, sec_id="form")


def page_niche(lang, n):
    N, U = n[lang], PAGES[lang]["niche"]
    url = npath(lang, n)
    alts = {l: npath(l, n) for l in LANGS}
    crumbs = [(T[lang]["home"], path(lang, "home")), (T[lang]["crumbs_ind"], path(lang, "industries")), (N["name"], url)]
    hero = f"""<div class="hero"><div class="hero-bg"><div class="glow"></div></div><div class="wrap hero-grid">
  <div>
    {crumbs_html(crumbs)}
    {h1(N['h1'], ' class="in" style="--i:1"')}
    <p class="lead in" style="--i:2">{e(N['lead'])}</p>
    <div class="hero-ctas in" style="--i:3">
      <a class="btn btn-dark shine" href="#contact" data-magnet><span>{e(U['cta1'])}</span><span class="arr" aria-hidden="true">→</span></a>
      <a class="btn btn-ghost" href="#how" data-magnet><span>{e(U['cta2'])}</span></a>
    </div>
    <div class="hero-meta in" style="--i:4">{''.join(f'<span>{e(m)}</span>' for m in T[lang]['meta_bar'])}</div>
  </div>
  <div class="in" style="--i:2">{pack(lang, seq_for(lang, [n]))}</div>
</div></div>"""
    problems = "".join(f'<div class="num card reveal"><b>{e(a)}</b><p>{e(b)}</p></div>' for a, b in N["problems"])
    work = "".join(f'<div class="svc card reveal"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in N["work"])
    kws = "".join(f'<span class="chip q">{e(k)}</span>' for k in N["keywords"])
    others = "".join(f'<a class="chip" href="{npath(lang, o)}">{e(o[lang]["name"])}</a>' for o in NICHES if o is not n)
    body = f"""<main id="main">{hero}
<section class="alt"><div class="wrap">{sec_head(U['problem'], N['why'])}<div class="nums">{problems}</div></div></section>
<section id="how"><div class="wrap">{sec_head(U['what'], U['what_h'].format(one=N['one']))}<div class="svc-grid">{work}</div></div></section>
<section class="tight"><div class="wrap">{sec_head(U['searches'], U['searches_h'], U['searches_p'])}<div class="chips reveal">{kws}</div></div></section>
{band(lang, U['band'], U['band_cta'], path(lang, 'pricing'))}
<section class="alt"><div class="wrap faq-grid">
  <div>{sec_head('FAQ' if lang == 'en' else PAGES[lang]['home']['faq_eb'], U['faq_h'].format(one=N['one']))}</div>
  <div class="faq reveal">{faq_items(N['faq'])}</div>
</div></section>
{form(lang, niche_name=n['en']['name'], eb=PAGES[lang]['home']['c_eb'], h2=PAGES[lang]['home']['c_h'], lead=PAGES[lang]['home']['c_lead'], steps=PAGES[lang]['home']['c_steps'])}
<section class="tight"><div class="wrap"><div class="sec-head reveal" style="margin-bottom:1.25rem"><p class="eyebrow">{e(U['other'])}</p></div><div class="chips">{others}</div></div></section>
</main>"""
    service_ld = {"@type": "Service", "@id": f"{SITE}{url}#service", "name": " ".join(N["h1"]), "serviceType": "Local SEO",
                  "description": N["desc"], "provider": {"@id": f"{SITE}/#business"},
                  "audience": {"@type": "BusinessAudience", "audienceType": n["en"]["name"]},
                  "areaServed": [{"@type": "City", "name": f"{c}, FL"} for c in AREAS], "url": f"{SITE}{url}"}
    ld = ld_graph(lang, url, N["title"], N["desc"], crumbs=crumbs, extra=[service_ld, faq_ld(url, lang, N["faq"])])
    return url, alts, head(lang, N["title"], N["desc"], url, alts, ld, og_for(lang)) + header(lang, "industries", alts) + body + footer(lang) + i18n_script(lang)


# ------------------------------------------------------------------ images
GOLD, DEEP, INK_ON, INK, MUTED, LINE = "#FFB547", "#D98A12", "#1A1205", "#0C0C0D", "#6C6C72", "#E6E6E2"


def font(name, size, wght):
    f = ImageFont.truetype(str(FONTS / f"{name}.ttf"), size)
    try:
        f.set_variation_by_axes([wght])
    except Exception:
        pass
    return f


def draw_mark(d, x, y, s):
    k = s / 30
    P = lambda px, py: (x + px * k, y + py * k)
    d.rounded_rectangle([P(2, 2), P(28, 28)], radius=6.5 * k, fill=GOLD)
    for bx, by, bh in ((7.6, 16, 7), (13, 11.5, 11.5), (18.4, 7, 16)):
        d.rounded_rectangle([P(bx, by), P(bx + 4, by + bh)], radius=1.5 * k, fill=INK_ON)


def star(d, cx, cy, r, color):
    pts = [(cx + (r if i % 2 == 0 else r * .45) * math.cos(-math.pi / 2 + i * math.pi / 5),
            cy + (r if i % 2 == 0 else r * .45) * math.sin(-math.pi / 2 + i * math.pi / 5)) for i in range(10)]
    d.polygon(pts, fill=color)


def og_image(lang, fname):
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), "#FFFFFF")
    d = ImageDraw.Draw(img)
    for gx in range(14, W, 28):
        for gy in range(14, H, 28):
            d.ellipse([gx - 1.2, gy - 1.2, gx + 1.2, gy + 1.2], fill="#E3E3DE")
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse([780, -240, 1340, 320], fill=(255, 181, 71, 90))
    gb = glow.filter(ImageFilter.GaussianBlur(90))
    img.paste(gb, (0, 0), gb)
    d = ImageDraw.Draw(img)
    draw_mark(d, 72, 66, 56)
    d.text((142, 74), "Rankelo", font=font("Unbounded", 36, 700), fill=INK)
    if lang == "en":
        l1, l2, l3, sub, pill = "Be the first business", "locals find", "on Google.", "Local SEO  ·  Google Maps  ·  Websites", "First results in 2–3 weeks"
        you = "Your business"
    else:
        l1, l2, l3, sub, pill = "Sea el primer negocio", "que sus clientes", "encuentran en Google.", "SEO local  ·  Google Maps  ·  Sitios web", "Primeros resultados en 2–3 semanas"
        you = "Su negocio"
    size = 64
    while True:
        hf = font("Unbounded", size, 700)
        if max(d.textlength(t_, font=hf) for t_ in (l1, l2, l3)) <= 660:
            break
        size -= 2
    d.text((72, 190), l1, font=hf, fill=INK)
    d.text((72, 270), l2, font=hf, fill=INK)
    w3 = d.textlength(l3, font=hf)
    d.rectangle([68, 350 + size * .62, 76 + w3, 350 + size * .98], fill=GOLD)
    d.text((72, 350), l3, font=hf, fill=INK)
    d.text((72, 470), sub, font=font("Manrope", 28, 600), fill=MUTED)
    pf = font("Manrope", 24, 700)
    tw = d.textlength(pill, font=pf)
    d.rounded_rectangle([72, 528, 72 + tw + 44, 576], radius=24, fill="#E5F6EC")
    d.ellipse([90, 546, 102, 558], fill="#14955A")
    d.text((112, 538), pill, font=pf, fill="#14955A")
    x0, y0 = 800, 200
    rows = [("1", you, 5, "4.9", True), ("2", "Casa Verde Kitchen", 4, "4.4", False), ("3", "Harbor Grill", 4, "4.2", False)]
    d.rounded_rectangle([x0 - 24, y0 - 24, 1140, y0 + 3 * 92 + 4], radius=26, fill="#FFFFFF", outline=LINE, width=2)
    for i, (n, nm, full, rt, me) in enumerate(rows):
        y = y0 + i * 92
        d.rounded_rectangle([x0, y, 1116, y + 76], radius=16, fill=INK if me else "#FFFFFF", outline=INK if me else LINE, width=2)
        d.rounded_rectangle([x0 + 16, y + 20, x0 + 52, y + 56], radius=10, fill=GOLD if me else "#EFEFEC")
        d.text((x0 + 34, y + 38), n, font=font("Manrope", 20, 700), fill=INK_ON if me else MUTED, anchor="mm")
        d.text((x0 + 70, y + 14), nm, font=font("Manrope", 22, 700), fill="#FFFFFF" if me else INK)
        for k in range(5):
            star(d, x0 + 80 + k * 20, y + 54, 8, (GOLD if me else DEEP) if k < full else ("#4A4A50" if me else "#D4D4CF"))
        d.text((x0 + 186, y + 54), rt, font=font("Manrope", 17, 600), fill=GOLD if me else DEEP, anchor="lm")
    img.save(OUT / fname, optimize=True)


def icons_out():
    for size, name, bg in ((180, "apple-touch-icon.png", "#FFFFFF"), (32, "favicon-32.png", None)):
        S = size * 8
        big = Image.new("RGBA", (S, S), bg or (0, 0, 0, 0))
        d = ImageDraw.Draw(big)
        pad = S * (0.12 if bg else 0)
        draw_mark(d, pad, pad, S - 2 * pad)
        big.resize((size, size), Image.LANCZOS).save(OUT / name)
    (OUT / "favicon.svg").write_text(LOGO.format(s=30).replace('width="30" height="30" ', 'xmlns="http://www.w3.org/2000/svg" ').replace(' aria-hidden="true"', ""))


def page_404():
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found | Rankelo</title><meta name="robots" content="noindex">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@700&family=Manrope:wght@500;600&display=swap">
<style>html,body{{margin:0;height:100%}}body{{background:#fff;color:#0C0C0D;font-family:Manrope,system-ui,sans-serif;display:grid;place-items:center;text-align:center;padding:0 18px}}
h1{{font-family:Unbounded,system-ui,sans-serif;font-size:clamp(3rem,12vw,6rem);margin:0;background:linear-gradient(transparent 60%,#FFB547 60%,#FFB547 92%,transparent 92%);display:inline}}
p{{color:#6C6C72;margin:1.25rem 0 2rem}}.b{{display:flex;gap:.75rem;justify-content:center;flex-wrap:wrap}}
a{{display:inline-block;background:#0C0C0D;color:#fff;font-weight:600;text-decoration:none;padding:1rem 1.5rem;border-radius:999px}}a+a{{background:#fff;color:#0C0C0D;border:1.5px solid #D4D4CF}}</style></head>
<body><main><h1>404</h1><p>This page doesn't exist. · Esta página no existe.</p><div class="b"><a href="/">Homepage →</a><a href="/es/">Inicio en español →</a></div></main></body></html>
"""


# ------------------------------------------------------------------ build
def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    shutil.copy(HERE / "assets" / "site.css", OUT / "assets" / "site.css")
    shutil.copy(HERE / "assets" / "site.js", OUT / "assets" / "site.js")
    pages = []
    for lang in LANGS:
        pages.append(page_home(lang))
        pages.append(simple_page(lang, "services", body_services))
        pages.append(simple_page(lang, "industries", body_industries))
        pages.append(simple_page(lang, "pricing", body_pricing, extra_ld=[lambda u, l: faq_ld(u, l, FAQ[l][2][1])]))
        pages.append(simple_page(lang, "about", body_about))
        pages.append(simple_page(lang, "faq", body_faq, extra_ld=[faq_all_ld]))
        pages.append(simple_page(lang, "contact", body_contact))
        for n in NICHES:
            pages.append(page_niche(lang, n))
    seen = {}
    for url, alts, doc in pages:
        d = OUT / url.strip("/")
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(doc)
        seen[url] = alts
    # sitemap with language alternates
    rows = []
    for url, alts in seen.items():
        alt = "".join(f'    <xhtml:link rel="alternate" hreflang="{l}" href="{SITE}{p}"/>\n' for l, p in alts.items())
        alt += f'    <xhtml:link rel="alternate" hreflang="x-default" href="{SITE}{alts["en"]}"/>\n'
        rows.append(f"  <url>\n    <loc>{SITE}{url}</loc>\n{alt}  </url>\n")
    (OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                                     'xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "".join(rows) + "</urlset>\n")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    # old addresses -> new ones (Cloudflare Pages _redirects)
    (OUT / "_redirects").write_text(
        "/ru /es/ 301\n/ru/ /es/ 301\n/ru/* /es/ 301\n"
        "/local-seo-for-plumbers /local-seo-for-restaurants/ 301\n/local-seo-for-plumbers/ /local-seo-for-restaurants/ 301\n")
    (OUT / "404.html").write_text(page_404())
    icons_out()
    og_image("en", "og-image.png")
    og_image("es", "og-image-es.png")
    zp = shutil.make_archive(str(HERE.parent / "rankelo-site"), "zip", OUT)
    print("pages:", len(seen), "->", zp)


if __name__ == "__main__":
    main()
