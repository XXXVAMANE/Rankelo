"""All Services hub (/services/, English). Client copy 01.11.2026. Local SEO price kept at the client's later $749."""

URL = "/services/"
MAINT = "/services/seo-maintenance/"
P = dict(
    title="BEST Local SEO Services Orlando | GBP, Website SEO & Maintenance Near Me | Rankelo",
    desc="Explore Rankelo’s Local SEO services for Orlando businesses, including Local SEO campaigns, Google Business "
         "Profile optimization, SEO-ready websites, and ongoing SEO maintenance.",
    # 1. HERO
    eyebrow="Rankelo Services",
    h1="Local SEO Services in Orlando",
    sub="Whether you need stronger local visibility, a better Google Business Profile, a new SEO-ready website, or "
        "ongoing support, Rankelo offers focused services based on where your business is today.",
    cta="Get a Free Local SEO Audit",
    note="Not sure which service you need? We’ll review your business and show you where the biggest opportunity is.",
    # 2. NEEDS
    need_h="Start with what your business needs most.",
    need_p=["You do not need to diagnose your own SEO problem before contacting us.",
            "Use the options below as a simple starting point."],
    rec="Recommended service",
    needs=[
        ("You already have a website, but customers struggle to find you on Google.", "Local SEO Campaign",
         "Improve your visibility across Google Maps and local search without rebuilding a website that is already "
         "working for your business.", "Explore Local SEO", "/services/local-seo/"),
        ("Your main concern is your Google Business Profile.", "Google Business Profile Optimization",
         "Improve the profile customers see when they find your business in Google Maps and local search.",
         "Explore GBP Optimization", "/services/google-business-profile/"),
        ("You need a new website or your current one no longer fits the business.", "Website + Local SEO",
         "Build a professional website around your services, location, customers, and local search visibility from "
         "the beginning.", "Explore Website + Local SEO", "/services/website-local-seo/"),
        ("You have already completed the main SEO work and want ongoing support.", "SEO Maintenance",
         "Keep your local presence monitored and maintained after the initial campaign.", "Explore SEO Maintenance", MAINT),
    ],
    # 3. MAIN SERVICES
    svc_h="Explore Rankelo services",
    svc_p="Each service solves a different problem. Choose the option that best matches where your business is now, or "
          "start with a Free Local SEO Audit if you are unsure.",
    best="Best for:", starting="Starting at",
    services=[
        dict(id="local-seo", n="01", t="Local SEO Campaign", out="Get found by more customers in your area.",
             p=["A broader Local SEO campaign for businesses that want stronger visibility across Google Maps and local search.",
                "The campaign can address your Google Business Profile, website SEO, local presence, content, and rankings "
                "based on what your business actually needs."],
             best="Businesses that already have a website but need stronger local search visibility.",
             price="$749", unit="", cta="Explore Local SEO", href="/services/local-seo/", icon="maps"),
        dict(id="gbp", n="02", t="Google Business Profile Optimization", out="Strengthen the profile customers see on Google Maps.",
             p=["A focused one-time service for businesses that want their Google Business Profile reviewed and improved.",
                "We strengthen the information, services, completeness, and local relevance of the profile so Google and "
                "potential customers have a clearer picture of the business."],
             best="Businesses whose biggest immediate opportunity is inside their Google Business Profile.",
             price="$299", unit="one-time", cta="Explore GBP Optimization", href="/services/google-business-profile/", icon="gbp"),
        dict(id="website", n="03", t="Website + Local SEO", out="Build your website around the customers you want to reach.",
             p=["A professional local-business website structured around your services, location, customer journey, and "
                "local search visibility.",
                "Instead of treating SEO as an afterthought, the website is built with a strong local-search foundation "
                "from the beginning."],
             best="Businesses that need a new website, a major rebuild, or a stronger foundation for future Local SEO.",
             price="$1,999", unit="", cta="Explore Website + Local SEO", href="/services/website-local-seo/", icon="web"),
        dict(id="maintenance", n="04", t="SEO Maintenance", out="Keep your local presence monitored and maintained.",
             p=["Optional ongoing support after the main SEO work is complete.",
                "SEO Maintenance is designed to help monitor rankings, handle smaller SEO updates, keep an eye on your local "
                "presence, and identify issues that may need attention over time."],
             best="Businesses that have already completed their initial SEO work and want continued support.",
             price="$399", unit="/month", cta="Explore SEO Maintenance", href="/services/seo-maintenance/", icon="track"),
    ],
    # 4. COMPARE
    cmp_h="Compare Rankelo services",
    cmp_p="Here is the simplest way to see how the four services differ.",
    cmp_cols=["Local SEO Campaign", "GBP Optimization", "Website + Local SEO", "SEO Maintenance"],
    cmp_rows=[
        ("Main goal", ["Improve overall local visibility", "Improve Google Business Profile", "Build a new SEO-ready website", "Maintain and monitor existing SEO"]),
        ("Google Business Profile work", ["Included when needed", "Main focus", "Not the main focus", "Ongoing attention when needed"]),
        ("Website SEO", ["Included when needed", "No", "Built into the website", "Smaller ongoing updates"]),
        ("New website", ["No", "No", "Yes", "No"]),
        ("Local citations / broader local presence", ["Included when needed", "No", "Not the main focus", "Maintenance when relevant"]),
        ("Ongoing monthly service", ["No requirement", "No", "No", "Yes"]),
        ("Starting price", ["$749", "$299 one-time", "$1,999", "$399/month"]),
    ],
    cmp_note="Final scope depends on the current condition of your business, website, Google Business Profile, "
             "competition, and local market.",
    # 5. NOT SURE
    ns_h="Not sure which service is right for your business?",
    ns_p=["You do not need to choose a service before speaking with us.",
          "We can review your Google Business Profile, website, current local visibility, and competition to identify "
          "where the biggest opportunity is.",
          "If your business only needs a focused profile improvement, we will tell you.",
          "If the problem is broader and requires Local SEO or a new website, we will explain why."],
    ns_cta="Get a Free Local SEO Audit",
    ns_small="No obligation. Just a clearer picture of what your business actually needs.",
    # 6. FAQ
    faq_h="Frequently asked questions",
    faq=[
        ("Which Rankelo service is right for my business?",
         "It depends on where the biggest problem is. If your existing website is solid but your overall local visibility "
         "is weak, a Local SEO Campaign may be the best fit. If the main issue is your Google Business Profile, the focused "
         "GBP Optimization service may be enough. If you need a new website, Website + Local SEO is the better starting point."),
        ("What is the difference between GBP Optimization and Local SEO?",
         "Google Business Profile Optimization focuses specifically on improving your Google Business Profile. A Local SEO "
         "Campaign is broader and can also include website SEO, citations and local presence, local content, competitor "
         "analysis, and rank tracking."),
        ("Do I need a new website for Local SEO?",
         "No. If your current website is usable and can be improved, we can work with the site you already have. Website + "
         "Local SEO is intended for businesses that genuinely need a new site or major rebuild."),
        ("Can I start with GBP Optimization and move to Local SEO later?",
         "Yes. GBP Optimization can be a smaller first step. If your business later needs broader work across the website "
         "and local search presence, you can move into a Local SEO Campaign."),
        ("Is SEO Maintenance required after a Local SEO Campaign?",
         "No. SEO Maintenance is optional. The initial Local SEO Campaign has its own scope, and you can decide afterward "
         "whether you want ongoing monitoring and support."),
        ("Do you provide custom quotes?",
         "Yes. The prices shown on the website are starting prices. Final pricing depends on the condition of your current "
         "online presence, competition, service area, website size, and the amount of work required."),
    ],
    # 7. FINAL CTA
    final_h="Start with the service your business actually needs.",
    final_p=["Tell us about your business and what you are trying to improve.",
             "We’ll review your current local presence and help you determine the most useful next step."],
    final_cta="Get a Free Local SEO Audit",
    final_small="No obligation. Just a clear starting point.",
)


def render(ctx):
    e, icon = ctx["e"], ctx["icon"]
    arr = '<span class="arr" aria-hidden="true">→</span>'
    paras = lambda ps: "".join(f"<p>{e(p)}</p>" for p in ps)
    unit = lambda u: f" <i>{e(u)}</i>" if u else ""
    index = "".join(f'<a class="hx-row" href="#{s["id"]}"><b>{s["n"]}</b><span>{e(s["t"])}</span>'
                    f'<em>{e(s["price"])}{unit(s["unit"])}</em></a>' for s in P["services"])
    needs = "".join(f"""<article class="need card reveal">
  <h3>“{e(q)}”</h3>
  <div class="need-rec"><small>{e(P['rec'])}</small><b>{e(svc)}</b></div>
  <p>{e(d)}</p>
  <a class="link" href="{href}">{e(cta)} {arr}</a>
</article>""" for q, svc, d, cta, href in P["needs"])
    rows = "".join(f"""<article class="srow reveal" id="{s['id']}">
  <div class="srow-head">
    <span class="srow-n">{s['n']}</span>
    <span class="ico">{icon(s['icon'])}</span>
    <h2>{e(s['t'])}</h2>
    <p class="srow-out">{e(s['out'])}</p>
  </div>
  <div class="srow-body">
    <div class="prose">{paras(s['p'])}</div>
    <p class="srow-best"><b>{e(P['best'])}</b> {e(s['best'])}</p>
    <div class="srow-foot">
      <div class="srow-price"><small>{e(P['starting'])}</small><b>{e(s['price'])}{unit(s['unit'])}</b></div>
      <a class="btn btn-dark" href="{s['href']}"{f' data-pick="{s["pick"]}"' if s.get('pick') else ''}><span>{e(s['cta'])}</span>{arr}</a>
    </div>
  </div>
</article>""" for s in P["services"])
    head_cells = "".join(f'<th scope="col"><a href="#{s["id"]}">{e(c)}</a></th>' for c, s in zip(P["cmp_cols"], P["services"]))
    body_rows = "".join(f'<tr{" class=\"cmp-price\"" if i == len(P["cmp_rows"]) - 1 else ""}><th scope="row">{e(lbl)}</th>'
                        + "".join(f"<td>{e(v)}</td>" for v in vals) + "</tr>"
                        for i, (lbl, vals) in enumerate(P["cmp_rows"]))
    H = ctx["home"]
    final_side = ("".join(f'<p class="lead">{e(p)}</p>' for p in P["final_p"])
                  + f'<p class="final-small">{e(P["final_small"])}</p>')
    form_html = ctx["form"]("en", h2=P["final_h"], side_extra=final_side, sec_id="audit", audit=dict(
        services=H["form_services"], service_label=H["form_service_label"], msg_label=H["form_msg_label"],
        submit=P["final_cta"], selected="unsure"))
    crumbs = ('<nav class="scrumbs in" style="--i:0" aria-label="Breadcrumb"><a href="/">Home</a>'
              '<span aria-hidden="true">→</span><span aria-current="page">Services</span></nav>')
    return f"""<main id="main">
<div class="hhero">
  <div class="wrap hhero-grid">
    <div>
      {crumbs}
      <p class="eyebrow in" style="--i:1">{e(P['eyebrow'])}</p>
      <h1 class="in" style="--i:1">{e(P['h1'])}</h1>
      <p class="lead in" style="--i:2">{e(P['sub'])}</p>
      <div class="hero-ctas in" style="--i:3"><a class="btn btn-dark shine" href="#audit" data-magnet><span>{e(P['cta'])}</span>{arr}</a></div>
      <p class="hero-note in" style="--i:4">{e(P['note'])}</p>
    </div>
    <nav class="hx in" style="--i:2" aria-label="Services on this page">{index}</nav>
  </div>
</div>
<section id="needs"><div class="wrap">
  <div class="sec-head reveal"><h2>{e(P['need_h'])}</h2><div class="prose">{paras(P['need_p'])}</div></div>
  <div class="needs">{needs}</div>
</div></section>
<section class="alt" id="all"><div class="wrap">
  <div class="sec-head reveal"><h2>{e(P['svc_h'])}</h2><p class="lead">{e(P['svc_p'])}</p></div>
  <div class="srows">{rows}</div>
</div></section>
<section id="compare"><div class="wrap">
  <div class="sec-head reveal"><h2>{e(P['cmp_h'])}</h2><p class="lead">{e(P['cmp_p'])}</p></div>
  <div class="cmp-wrap reveal" tabindex="0" role="region" aria-label="{e(P['cmp_h'])}"><table class="cmp">
    <thead><tr><td></td>{head_cells}</tr></thead><tbody>{body_rows}</tbody></table></div>
  <p class="cmp-note">{e(P['cmp_note'])}</p>
</div></section>
<section id="not-sure"><div class="wrap">
  <div class="ns card dark reveal">
    <h2>{e(P['ns_h'])}</h2>
    <div class="ns-body">{paras(P['ns_p'])}
      <a class="btn btn-gold" href="#audit" data-magnet><span>{e(P['ns_cta'])}</span>{arr}</a>
      <small>{e(P['ns_small'])}</small></div>
  </div>
</div></section>
<section class="alt" id="faq"><div class="wrap faq-grid">
  <div><div class="sec-head reveal" style="margin-bottom:0"><p class="eyebrow">FAQ</p><h2>{e(P['faq_h'])}</h2></div></div>
  <div class="faq reveal">{ctx['faq_items'](P['faq'])}</div>
</div></section>
<div class="final-cta">{form_html}</div>
</main>"""


CSS = """
/* ---- services hub ---- */
.hhero{border-bottom:1px solid var(--line);padding-block:clamp(2rem,5vw,3.5rem) clamp(2.5rem,5vw,4rem)}
.hhero-grid{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:3rem;align-items:center}
.hhero h1{font-size:clamp(2.2rem,5vw,3.6rem);margin-block:.9rem 1rem;max-width:16ch}
.hhero .lead{max-width:54ch}
@media (max-width:960px){.hhero-grid{grid-template-columns:1fr}}
.hx{display:grid;border:1px solid var(--line);border-radius:18px;background:#fff;overflow:hidden;box-shadow:0 24px 50px -32px rgba(12,12,13,.3)}
.hx-row{display:grid;grid-template-columns:2.6rem 1fr auto;gap:.8rem;align-items:center;padding:1.05rem 1.2rem;text-decoration:none;color:var(--ink);border-bottom:1px solid var(--line);transition:background .2s}
.hx-row:last-child{border-bottom:0}
.hx-row:hover{background:var(--bg-2,#F6F5F2)}
.hx-row b{font:600 .85rem/1 var(--f-mono);color:var(--gold-deep)}
.hx-row span{font-weight:600}
.hx-row em{font:700 1.05rem/1 var(--f-display);font-style:normal;letter-spacing:-.02em;white-space:nowrap}
.hx-row em i{font:500 .75rem/1 var(--f-body);font-style:normal;color:var(--muted)}
.needs{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.need{padding:1.6rem;display:grid;gap:.9rem;align-content:start}
.need h3{font-size:1.12rem;font-weight:600;line-height:1.35;letter-spacing:-.015em}
.need-rec{display:grid;gap:.3rem;padding:.75rem .9rem;border-radius:12px;background:var(--bg-2,#F6F5F2);border-left:3px solid var(--gold)}
.need-rec small{font:600 .68rem/1 var(--f-mono);letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}
.need-rec b{font-size:1rem}
.need p{color:var(--muted);font-size:.95rem}
.need .link{justify-self:start}
@media (max-width:760px){.needs{grid-template-columns:1fr}}
.srows{display:grid;gap:1.25rem}
.srow{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:2rem 3.5rem;padding:clamp(1.5rem,3.5vw,2.75rem);background:#fff;border:1px solid var(--line);border-radius:var(--r);scroll-margin-top:90px}
.srow:nth-child(even) .srow-head{order:2}
.srow-head{display:grid;gap:.75rem;align-content:start;position:relative}
.srow-n{font:700 clamp(3.5rem,8vw,5.5rem)/.9 var(--f-display);letter-spacing:-.05em;color:transparent;-webkit-text-stroke:1.5px var(--ink)}
.srow-head .ico{position:absolute;top:0;right:0}
.srow-head h2{font-size:clamp(1.5rem,2.8vw,2rem)}
.srow-out{font-size:1.1rem;font-weight:600;color:var(--ink-2)}
.srow-body{display:grid;gap:1rem;align-content:start}
.srow-best{padding:.85rem 1rem;border-radius:12px;background:var(--bg-2,#F6F5F2);font-size:.95rem}
.srow-foot{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:1rem;padding-top:1rem;border-top:1px solid var(--line)}
.srow-price{display:grid;gap:.3rem}
.srow-price small{font:600 .72rem/1 var(--f-mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.srow-price b{font:700 2.2rem/1 var(--f-display);letter-spacing:-.03em}
.srow-price b i{font:500 1rem/1 var(--f-body);font-style:normal;color:var(--muted);margin-left:.3rem;letter-spacing:0}
@media (max-width:860px){.srow{grid-template-columns:1fr}.srow:nth-child(even) .srow-head{order:0}}
.cmp-wrap{overflow-x:auto;border:1px solid var(--line);border-radius:var(--r);background:#fff;-webkit-overflow-scrolling:touch}
.cmp{width:100%;min-width:820px;border-collapse:collapse;font-size:.93rem}
.cmp th,.cmp td{padding:.95rem 1rem;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}
.cmp thead th{font-weight:700;background:var(--bg-2,#F6F5F2)}
.cmp thead th a{color:var(--ink);text-decoration:none}
.cmp thead th a:hover{color:var(--gold-deep)}
.cmp thead th:nth-child(2){background:var(--ink)}.cmp thead th:nth-child(2) a{color:#fff}
.cmp thead td{background:var(--bg-2,#F6F5F2)}
.cmp tbody th{font-weight:600;width:20%;position:sticky;left:0;background:#fff}
.cmp td{color:var(--ink-2)}
.cmp tbody td:nth-child(2){background:#FFFBF2}
.cmp tr:last-child th,.cmp tr:last-child td{border-bottom:0}
.cmp-price td{font:700 1.05rem/1.2 var(--f-display);color:var(--ink)}
.cmp-note{margin-top:1rem;color:var(--muted);font-size:.9rem}
.ns{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:2rem 4rem;padding:clamp(1.75rem,4vw,3rem)}
.ns h2{color:#fff}
.ns-body{display:grid;gap:.8rem;justify-items:start;color:#C3C3C8}
.ns-body .btn{margin-top:.6rem}
.ns-body small{color:#9E9EA5;font-size:.88rem}
@media (max-width:820px){.ns{grid-template-columns:1fr}}
"""
