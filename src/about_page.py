"""About page (/about/, English). Client copy, 01.11.2026. Editorial layout, no team section."""

URL = "/about/"
P = dict(
    title="About Rankelo | Local SEO Company in Orlando, FL",
    desc="Meet Rankelo, an Orlando Local SEO studio helping small businesses improve visibility across Google Maps, "
         "local search, and the web.",
    eyebrow="About Rankelo",
    h1="A Local SEO Studio Built for Small Businesses",
    sub="Rankelo helps Orlando businesses improve how they appear across Google Maps, local search, and the web.",
    support="We focus on practical Local SEO work built around what each business actually needs.",
    cta="Get a Free Local SEO Audit",
    why_h="Good local businesses shouldn’t be invisible on Google.",
    why_p=["Most business owners did not start their company to become SEO experts. They started it because they are "
           "good at what they do.",
           "But today, customers often search Google before deciding who to call, visit, book, or hire.",
           "Rankelo was built to help small businesses strengthen their local visibility without making SEO another "
           "full-time job for the owner."],
    bel_h="The way we think about Local SEO.",
    beliefs=[
        ("Direct communication", "You communicate directly with the people handling the work, so questions and decisions stay simple."),
        ("Clear scope", "You should know what we are working on, why it matters, and what you are paying for."),
        ("Business-first strategy", "We look at your current visibility, website, competition, and local market before "
                                    "recommending what actually needs attention."),
        ("Responsible SEO", "We focus on legitimate Local SEO work rather than risky shortcuts that could put your Google "
                            "presence at risk."),
    ],
    help_h="What Rankelo helps with",
    help_p="Our services are built around the most common local visibility problems small businesses face.",
    services=[
        ("Local SEO Campaign", "Broader Local SEO work for businesses that need stronger visibility across Google Maps and local search.",
         "Explore Local SEO", "/services/local-seo/"),
        ("Google Business Profile Optimization", "Focused improvements to the profile customers see when they find your business on Google.",
         "Explore GBP Optimization", "/services/google-business-profile/"),
        ("Website + Local SEO", "Professional local-business websites built around your services, customers, and local search "
                                "visibility from the beginning.", "Explore Website + Local SEO", "/services/website-local-seo/"),
        ("SEO Maintenance", "Optional ongoing support after the initial SEO work is complete.",
         "Explore SEO Maintenance", "/services/seo-maintenance/"),
    ],
    all_cta="View All Services",
    local_h="Built for businesses that depend on local customers.",
    local_p=["Rankelo focuses on small businesses whose customers search locally before deciding who to call, visit, or hire.",
             "That can include home-service businesses, professional practices, restaurants, local shops, and other "
             "businesses serving customers in and around Orlando."],
    local_goal="Our goal is simple: help more of the right local customers find the business when they are already "
               "searching for what it offers.",
    final_h="See where your business stands on Google.",
    final_p=["Get a free Local SEO audit and we’ll review your current local visibility, website, Google Business Profile, "
             "and competition.",
             "We’ll show you where we see the biggest opportunities and what we would recommend improving first."],
    final_cta="Get a Free Local SEO Audit",
    final_small="No obligation. Just a clear starting point.",
)


def render(ctx):
    e = ctx["e"]
    audit = ctx["audit_url"]
    arr = '<span class="arr" aria-hidden="true">→</span>'
    paras = lambda ps: "".join(f"<p>{e(p)}</p>" for p in ps)
    beliefs = "".join(f'<div class="bel reveal"><b>0{i + 1}</b><h3>{e(t)}</h3><p>{e(d)}</p></div>'
                      for i, (t, d) in enumerate(P["beliefs"]))
    svcs = "".join(f'<a class="arow reveal" href="{h}"><h3>{e(t)}</h3><p>{e(d)}</p><span class="arow-cta">{e(c)} {arr}</span></a>'
                   for t, d, c, h in P["services"])
    return f"""<main id="main">
<div class="ahero"><div class="wrap">
  <nav class="scrumbs in" style="--i:0" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">→</span><span aria-current="page">About</span></nav>
  <p class="eyebrow in" style="--i:1">{e(P['eyebrow'])}</p>
  <h1 class="in" style="--i:1">{e(P['h1'])}</h1>
  <p class="ahero-sub in" style="--i:2">{e(P['sub'])}</p>
  <p class="ahero-support in" style="--i:2">{e(P['support'])}</p>
  <div class="hero-ctas in" style="--i:3"><a class="btn btn-dark shine" href="{audit}" data-magnet><span>{e(P['cta'])}</span>{arr}</a></div>
</div></div>
<section id="why"><div class="wrap ed">
  <h2 class="reveal">{e(P['why_h'])}</h2>
  <div class="ed-body reveal">{paras(P['why_p'])}</div>
</div></section>
<section class="alt" id="beliefs"><div class="wrap">
  <div class="sec-head reveal"><h2>{e(P['bel_h'])}</h2></div>
  <div class="bels">{beliefs}</div>
</div></section>
<section id="help"><div class="wrap">
  <div class="sec-head reveal"><h2>{e(P['help_h'])}</h2><p class="lead">{e(P['help_p'])}</p></div>
  <div class="arows">{svcs}</div>
  <a class="link" style="margin-top:1.75rem" href="/services/">{e(P['all_cta'])} {arr}</a>
</div></section>
<section class="alt" id="local"><div class="wrap ed">
  <h2 class="reveal">{e(P['local_h'])}</h2>
  <div class="ed-body reveal">{paras(P['local_p'])}<p class="ed-goal">{e(P['local_goal'])}</p></div>
</div></section>
<section id="start"><div class="wrap">
  <div class="ns card dark reveal">
    <h2>{e(P['final_h'])}</h2>
    <div class="ns-body">{paras(P['final_p'])}
      <a class="btn btn-gold" href="{audit}" data-magnet><span>{e(P['final_cta'])}</span>{arr}</a>
      <small>{e(P['final_small'])}</small></div>
  </div>
</div></section>
</main>"""


CSS = """
/* ---- about page (editorial) ---- */
.ahero{padding-block:clamp(2.5rem,7vw,5.5rem) clamp(2.5rem,6vw,4.5rem);border-bottom:1px solid var(--line)}
.ahero h1{font-size:clamp(2.4rem,6vw,4.6rem);max-width:15ch;margin-block:1rem 1.4rem;line-height:1.02}
.ahero-sub{font-size:clamp(1.2rem,2.2vw,1.5rem);line-height:1.45;max-width:38ch;color:var(--ink);letter-spacing:-.01em}
.ahero-support{margin-top:.9rem;color:var(--muted);font-size:1.05rem;max-width:52ch}
.ed{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:2rem 5rem;align-items:start}
.ed h2{font-size:clamp(1.9rem,3.6vw,2.8rem);line-height:1.08}
.ed-body{display:grid;gap:1.1rem;font-size:clamp(1.08rem,1.6vw,1.22rem);line-height:1.6;color:var(--ink-2)}
.ed-goal{padding-top:1.1rem;border-top:2px solid var(--gold);color:var(--ink);font-weight:600}
@media (max-width:860px){.ed{grid-template-columns:1fr}}
.bels{display:grid;grid-template-columns:1fr 1fr;gap:0 4rem}
.bel{display:grid;grid-template-columns:3rem 1fr;gap:.35rem 1rem;padding:1.6rem 0;border-top:1px solid var(--line-2)}
.bel b{grid-row:span 2;font:600 .85rem/1.9 var(--f-mono);color:var(--gold-deep)}
.bel h3{font-size:1.3rem;font-weight:700}
.bel p{color:var(--ink-2);font-size:1.02rem}
@media (max-width:760px){.bels{grid-template-columns:1fr}}
.arows{display:grid;border-top:1px solid var(--line)}
.arow{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.3fr) auto;gap:.5rem 2.5rem;align-items:center;padding:1.4rem .25rem;border-bottom:1px solid var(--line);text-decoration:none;color:var(--ink);transition:background .25s,padding .3s var(--ease)}
.arow:hover{background:var(--bg-2,#F6F5F2);padding-inline:1rem}
.arow h3{font-size:1.15rem;font-weight:700}
.arow p{color:var(--muted);font-size:.97rem}
.arow-cta{font-weight:600;font-size:.92rem;white-space:nowrap;border-bottom:1.5px solid var(--gold);padding-bottom:2px}
@media (max-width:860px){.arow{grid-template-columns:1fr}.arow-cta{justify-self:start}}
#help .link{display:inline-flex}
"""
