"""English homepage (v2): six sections, copy supplied by the client (01.11.2026)."""

HOME = dict(
    title="Rankelo | Local SEO for Orlando Businesses",
    desc="Rankelo helps Orlando businesses show up higher in Google Maps and local search, so more nearby customers "
         "can find you, call you, and choose you. Get a free Local SEO audit.",
    # 1. HERO
    eyebrow=("Local SEO", "for Orlando businesses"),
    h1=("Be the first business locals", "find on Google."),
    sub="Rankelo helps Orlando businesses show up higher in Google Maps and local search, so more nearby customers "
        "can find you, call you, and choose you.",
    cta1="Get a Free Audit", cta2="See Services",
    note="We’ll review your Google Business Profile, website, and local competition and show you where your biggest "
         "opportunities are.",
    # 2. PROBLEM
    problem_eb="The problem",
    problem_h="Your customers are already searching for businesses like yours.",
    problem_p=[
        "When someone in Orlando searches for your service, they usually contact one of the businesses they see first.",
        "If your Google Business Profile is weak, your website is poorly optimized, or your business information is "
        "inconsistent across the web, competitors can show up ahead of you — even when you offer the better service.",
        "And keeping up with Local SEO takes time. You’re already running your business, serving customers, managing "
        "your team, and handling everything else that comes with being an owner.",
    ],
    problem_close="Every search where your business is hard to find is another opportunity for a customer to choose someone else.",
    # 3. SOLUTION
    sol_eb="What we do",
    sol_h="We make it easier for local customers to find you.",
    sol_lead="Rankelo handles the Local SEO work that helps your business appear more prominently across Google Maps "
             "and local search. We focus on the parts that matter most for local visibility, then build from there "
             "based on what your business actually needs.",
    sol_items=[
        ("gbp", "Google Business Profile",
         "We optimize your profile so Google has clear, accurate information about your business, services, and location."),
        ("web", "Website & On-Page SEO",
         "We improve the pages, structure, and local signals on your website so Google can better understand what you "
         "offer and where you offer it."),
        ("citations", "Citations & Local Presence",
         "We keep your business information consistent across trusted directories and local platforms."),
        ("pages", "Local Content",
         "When your market needs more than basic optimization, we build service and location pages that help "
         "strengthen your relevance for the searches you want to appear for."),
    ],
    sol_close="You run your business. We handle the work behind your local visibility.",
    # 4. WHY RANKELO
    why_eb="Why Rankelo",
    why_h="Local SEO without the agency runaround.",
    why_items=[
        ("chat", "Direct communication",
         "You work directly with the people handling your SEO, so questions and decisions don't get passed through "
         "layers of account managers."),
        ("target", "A strategy built around your business",
         "We start by looking at your rankings, website, competition, and local market before deciding what work "
         "actually makes sense."),
        ("reports", "Clear scope and reporting",
         "You know what we're working on, why we're doing it, and what we're measuring."),
        ("key", "Your business stays yours",
         "Your website, Google Business Profile, and business accounts remain under your ownership."),
    ],
    # 5. SERVICES + PRICING
    svc_eb="Services & pricing",
    svc_h="Pick where you want to start.",
    offers=[
        dict(t="Local SEO Campaign", featured=True, price="$750",
             d="Improve your visibility across Google Maps and local search through GBP, website optimization, "
               "citations, and local SEO work based on your market.",
             cta="Explore Local SEO", href="services/", tag=None),
        dict(t="Google Business Profile Optimization", featured=False, price="$299",
             d="Improve how your business appears in Google Maps with a properly optimized profile, categories, "
               "services, and business information.",
             cta="Explore GBP Optimization", href="services/#gbp", tag=None),
        dict(t="SEO-Ready Websites", featured=False, price="$1,500",
             d="A professional website built around your services, location, conversions, and local search visibility.",
             cta="Explore Websites", href="services/#web", tag=None),
    ],
    starting="Starting at",
    svc_all="View All Services",
    svc_note="Final pricing depends on your website, competition, service area, and the work required.",
    # 6. FAQ
    faq_eb="FAQ",
    faq_h="Frequently asked questions",
    faq=[
        ("What exactly does Local SEO include?",
         "Local SEO can include Google Business Profile optimization, website and on-page SEO, citations, local "
         "content, and rank tracking. The exact work depends on what your business needs and how competitive your "
         "market is."),
        ("How long does Local SEO take?",
         "Some improvements can happen fairly quickly, while stronger ranking changes usually take longer. We track "
         "your starting position first and measure progress throughout the campaign rather than promising an exact "
         "ranking date."),
        ("Do you optimize my website too?",
         "Yes. Your website is an important part of Local SEO. We can improve page structure, titles, headings, local "
         "relevance, internal links, and other on-page elements that help Google better understand your business."),
        ("Do I have to pay every month?",
         "No. Our initial Local SEO campaign is separate from ongoing SEO. After the campaign, you can stop or "
         "continue with optional monthly maintenance and growth support."),
        ("How much does Local SEO cost?",
         "Our Local SEO campaigns start at $750. Final pricing depends on your website, competition, service area, "
         "and the amount of work required. We review your business first and provide a clear quote before starting."),
        ("Can you guarantee that I will rank #1?",
         "No agency can control Google’s rankings or guarantee a permanent #1 position. Our goal is to improve your "
         "local visibility using measurable SEO work and track how your rankings change over time."),
    ],
    still_h="Still have questions?",
    still_p="Get a free Local SEO audit and we’ll show you what may be holding your business back.",
    still_cta="Get a Free Audit",
)

EXTRA_ICONS = {
    "chat": '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/><path d="M8.5 11h7M8.5 14.5h4"/>',
    "target": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1" fill="currentColor"/>',
    "key": '<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3M14.5 8.5l2 2"/>',
}

HOME_CSS = """
/* ---- homepage v2 ---- */
.hero-note{margin-top:1.1rem;color:var(--muted);font-size:.92rem;max-width:52ch;display:flex;gap:.6rem;align-items:flex-start}
.hero-note::before{content:"";flex:none;width:18px;height:18px;margin-top:.15rem;border-radius:6px;background:var(--gold-soft) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Ccircle cx='11' cy='11' r='6' fill='none' stroke='%231A1205' stroke-width='2.6'/%3E%3Cpath d='M16 16l4 4' stroke='%231A1205' stroke-width='2.6' stroke-linecap='round'/%3E%3C/svg%3E") center/12px no-repeat;border:1px solid #FBE3BB}
.problem{display:grid;grid-template-columns:minmax(0,.95fr) minmax(0,1.05fr);gap:2rem 4rem;align-items:start}
.problem .prose{font-size:1.08rem}
.callout{margin-top:.5rem;padding:1.4rem 1.5rem;border-radius:var(--r);background:var(--ink);color:#fff;font:500 clamp(1.05rem,2vw,1.25rem)/1.4 var(--f-display);letter-spacing:-.01em;position:relative;overflow:hidden}
.callout::before{content:"";position:absolute;width:220px;height:220px;right:-80px;top:-120px;border-radius:50%;background:radial-gradient(circle,rgba(255,181,71,.5),transparent 65%)}
.callout span{position:relative}
@media (max-width:860px){.problem{grid-template-columns:1fr}}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
@media (max-width:700px){.grid2{grid-template-columns:1fr}}
.closer{margin-top:2rem;display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:1rem;padding-top:1.75rem;border-top:1px solid var(--line)}
.closer p{font:600 clamp(1.1rem,2.2vw,1.4rem)/1.35 var(--f-display);letter-spacing:-.01em;max-width:36ch}
.why{display:grid;grid-template-columns:repeat(4,1fr);gap:1rem}
.why .card{padding:1.5rem;display:grid;gap:.7rem;align-content:start}
.why h3{font-size:1.05rem;font-weight:700}
.why p{color:var(--muted);font-size:.95rem}
@media (max-width:1000px){.why{grid-template-columns:1fr 1fr}}
@media (max-width:540px){.why{grid-template-columns:1fr}}
.offers{display:grid;grid-template-columns:repeat(3,1fr);gap:1.25rem;align-items:stretch}
.offer{padding:1.75rem;display:flex;flex-direction:column;gap:.9rem;min-width:0}
.offer h3{font-size:1.25rem;font-weight:700}
.offer p{color:var(--muted);font-size:.95rem}
.card.dark.offer p{color:#C3C3C8}
.price{display:grid;gap:.15rem;margin-top:auto;padding-top:1rem;border-top:1px solid var(--line)}
.card.dark .price{border-top-color:#2A2A2E}
.price small{font:600 .72rem/1 var(--f-mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.card.dark .price small{color:#9E9EA5}
.price b{font:700 2rem/1.1 var(--f-display);letter-spacing:-.02em}
.card.dark .price b{color:var(--gold)}
.offer .link{align-self:flex-start}
.card.dark .link{color:#fff}
.offer-tag{align-self:flex-start;font:600 .68rem/1 var(--f-mono);letter-spacing:.06em;text-transform:uppercase;background:var(--gold);color:var(--gold-ink);padding:.42rem .6rem;border-radius:999px}
.offers-foot{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:1rem;margin-top:1.75rem}
.offers-foot small{color:var(--muted);font-size:.88rem;max-width:60ch}
@media (max-width:960px){.offers{grid-template-columns:1fr}}
.still{margin-top:1.5rem;padding:1.5rem;border-radius:var(--r);background:#fff;border:1px solid var(--line);display:grid;gap:.6rem}
.still h3{font-size:1.2rem;font-weight:700}
.still p{color:var(--muted)}
.still .btn{justify-self:start;margin-top:.4rem}
"""


def render(lang, ctx):
    """ctx: dict of helpers from build.py (e, icon_svg, pack, seq, path, header, footer, head, h1, sec_head, faq_items, ld)."""
    H = HOME
    e, path = ctx["e"], ctx["path"]
    icon = ctx["icon"]
    sol = "".join(f'<div class="svc card reveal"><span class="ico">{icon(k)}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>'
                  for k, t, d in H["sol_items"])
    why = "".join(f'<div class="card reveal"><span class="ico">{icon(k)}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>'
                  for k, t, d in H["why_items"])
    offers = "".join(f"""<article class="offer card{' dark' if o['featured'] else ''} reveal">
  {f'<span class="offer-tag">{e(o["tag"])}</span>' if o['tag'] else ''}
  <h3>{e(o['t'])}</h3><p>{e(o['d'])}</p>
  <div class="price"><small>{e(H['starting'])}</small><b>{e(o['price'])}</b></div>
  <a class="link" href="/{o['href']}">{e(o['cta'])} <span class="arr" aria-hidden="true">→</span></a>
</article>""" for o in H["offers"])
    prose = "".join(f"<p>{e(p)}</p>" for p in H["problem_p"])
    contact = path(lang, "contact")
    return f"""<main id="main">
<div class="hero">
  <div class="hero-bg"><div class="glow"></div></div>
  <div class="wrap hero-grid">
    <div>
      <span class="badge in" style="--i:0"><b>{e(H['eyebrow'][0])}</b><span>{e(H['eyebrow'][1])}</span></span>
      {ctx['h1'](H['h1'], ' class="in" style="--i:1"')}
      <p class="lead in" style="--i:2">{e(H['sub'])}</p>
      <div class="hero-ctas in" style="--i:3">
        <a class="btn btn-dark shine" href="{contact}" data-magnet><span>{e(H['cta1'])}</span><span class="arr" aria-hidden="true">→</span></a>
        <a class="btn btn-ghost" href="{path(lang, 'services')}" data-magnet><span>{e(H['cta2'])}</span></a>
      </div>
      <p class="hero-note in" style="--i:4">{e(H['note'])}</p>
    </div>
    <div class="in" style="--i:2">{ctx['pack']}</div>
  </div>
</div>
<section class="alt" id="problem"><div class="wrap problem">
  <div class="sec-head reveal" style="margin-bottom:0"><p class="eyebrow">{e(H['problem_eb'])}</p><h2>{e(H['problem_h'])}</h2></div>
  <div class="reveal"><div class="prose">{prose}</div><p class="callout"><span>{e(H['problem_close'])}</span></p></div>
</div></section>
<section id="solution"><div class="wrap">
  <div class="sec-head reveal"><p class="eyebrow">{e(H['sol_eb'])}</p><h2>{e(H['sol_h'])}</h2><p class="lead">{e(H['sol_lead'])}</p></div>
  <div class="grid2">{sol}</div>
  <div class="closer reveal"><p>{e(H['sol_close'])}</p></div>
</div></section>
<section class="alt" id="why"><div class="wrap">
  <div class="sec-head reveal"><p class="eyebrow">{e(H['why_eb'])}</p><h2>{e(H['why_h'])}</h2></div>
  <div class="why">{why}</div>
</div></section>
<section id="services"><div class="wrap">
  <div class="sec-head reveal"><p class="eyebrow">{e(H['svc_eb'])}</p><h2>{e(H['svc_h'])}</h2></div>
  <div class="offers">{offers}</div>
  <div class="offers-foot reveal"><small>{e(H['svc_note'])}</small>
    <a class="btn btn-ghost" href="{path(lang, 'services')}"><span>{e(H['svc_all'])}</span><span class="arr" aria-hidden="true">→</span></a></div>
</div></section>
<section class="alt" id="faq"><div class="wrap faq-grid">
  <div>
    <div class="sec-head reveal" style="margin-bottom:0"><p class="eyebrow">{e(H['faq_eb'])}</p><h2>{e(H['faq_h'])}</h2></div>
    <div class="still reveal"><h3>{e(H['still_h'])}</h3><p>{e(H['still_p'])}</p>
      <a class="btn btn-dark" href="{contact}" data-magnet><span>{e(H['still_cta'])}</span><span class="arr" aria-hidden="true">→</span></a></div>
  </div>
  <div class="faq reveal">{ctx['faq_items'](H['faq'])}</div>
</div></section>
</main>"""
