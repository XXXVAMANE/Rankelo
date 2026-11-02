"""Website + Local SEO service page (/services/website-local-seo/). Client copy, 01.11.2026; price set to $1,999 by the client."""
import service_page as sp

URL = "/services/website-local-seo/"
P = dict(
    title="BEST Local SEO Website Design Orlando | SEO-Ready Business Websites Near Me | Rankelo",
    desc="SEO-ready website design for Orlando businesses. Get a professional business website built around your "
         "services, location, customers, and local search visibility. Starting at $1,999.",
    crumb="Website + Local SEO",
    # 1. HERO
    eyebrow="SEO-Ready Business Websites",
    h1="Local SEO Website Design for Orlando Businesses",
    sub="Get a professional business website built around your services, location, and the way local customers search "
        "— so your site is easier to understand, easier to navigate, and better prepared for local visibility.",
    price_label="Starting at", price="$1,999",
    cta1="Get a Free Website Consultation", cta2="See What’s Included",
    note="We’ll review your business, current website if you have one, core services, and local market before "
         "recommending the right site structure.",
    # 2. SELL THE RESULT
    res_h="A website built to help customers find you and choose you.",
    res_lead=[
        "Your website should do more than look professional.",
        "It should make your services easy to understand, give local customers a clear path to contact you, and help "
        "search engines understand what your business does and where it operates.",
    ],
    res_items=[
        ("maps", "Built for local visibility",
         "Create a stronger foundation for showing up when nearby customers search for the services your business offers."),
        ("pages", "Built around what you sell",
         "Give your most important services clear, dedicated space instead of hiding everything inside one general page."),
        ("chat", "Built for real customers",
         "Make it easy for visitors to understand your business, explore your services, and take the next step."),
        ("track", "Built to grow with your business",
         "Start with a website structure that can expand as you add services, content, or additional service areas."),
    ],
    # 3. PROBLEM
    prob_h="A good-looking website is not enough.",
    prob_p=[
        "A website can look modern and still make it difficult for Google and potential customers to understand the "
        "business behind it.",
        "Important services may be buried on one page. Local relevance may be unclear. Pages may not connect logically, "
        "and visitors may struggle to find the information they need before contacting you.",
        "Building or redesigning a website without considering Local SEO can leave the same visibility problems in place.",
    ],
    prob_close="Your website should be designed around how your business actually gets found, understood, and contacted.",
    # 4. WHAT MAKES THE WEBSITE SEO-READY
    ready_h="Built around your services, location, and customers.",
    ready_lead="We structure the website so people and search engines can clearly understand what your business offers "
               "and how the most important parts of the site connect.",
    ready_items=[
        ("web", "Clear Website Structure",
         "We organize the site around the information customers actually need, with clear paths between your main "
         "pages and services."),
        ("pages", "Service-Focused Pages",
         "Your most important services can receive dedicated pages so customers and search engines have a clearer "
         "understanding of what you offer."),
        ("maps", "Local Relevance",
         "We build location context into the website so your business has a stronger foundation for the local market "
         "it actually serves."),
        ("search", "On-Page SEO Foundation",
         "Core pages are structured with search visibility in mind from the beginning instead of treating SEO as an "
         "afterthought."),
        ("citations", "Internal Page Connections",
         "We connect related pages naturally so visitors can move through the site easily and search engines can "
         "better understand how your content fits together."),
        ("phone", "Conversion-Focused Pages",
         "Each important page should make it easy for a potential customer to understand the next step, whether that "
         "is calling, requesting a quote, or contacting the business."),
    ],
    # 5. STRUCTURE
    st_h="Give every important service room to compete.",
    st_p=[
        "A local business website should reflect the way the business actually operates.",
        "Instead of forcing every service onto one page, we build a structure around the services and information that "
        "matter most to your customers.",
        "The exact page count and structure depend on the business, but a site may include:",
    ],
    st_list=["Homepage", "Main service pages", "Supporting service pages when needed", "About page", "Contact page",
             "Relevant service-area content when needed"],
    st_after=[
        "Some businesses only need a focused core website. Others need more service or local content to properly "
        "represent what they offer.",
        "We determine the structure around the business rather than forcing every client into the same website template.",
    ],
    # 6. LOCAL + TOPICAL RELEVANCE
    rel_h="Help Google understand what you do and where you do it.",
    rel_p=[
        "A strong local business website needs to communicate two things clearly: what the business is relevant for and "
        "where it provides those services.",
        "Your service content helps build relevance around what you do. Local content helps establish where the "
        "business operates.",
        "When those pages are organized and connected logically, the website becomes easier for customers to navigate "
        "and easier for search engines to understand.",
    ],
    rel_close="The goal is a website that makes sense to real people first while giving search engines a clear picture "
              "of the business behind it.",
    # 7. VS
    vs_h="Do you need a new website or SEO for the one you already have?",
    vs_p=[
        "You do not need a new website just because you want better Local SEO.",
        "If your current website is solid, improving the site you already have may make more sense. If the website is "
        "outdated, poorly structured, missing important service pages, or no longer fits the business, rebuilding it "
        "with Local SEO in mind can give you a stronger foundation.",
    ],
    vs_a_h="Choose Website + Local SEO if:",
    vs_a=["You need a new business website.", "Your current site no longer represents your services properly.",
          "Important services do not have clear pages.", "Your existing website structure is difficult to expand.",
          "You want Local SEO considered from the beginning of the build."],
    vs_b_h="Consider a Local SEO Campaign if:",
    vs_b=["Your existing website is already usable and professional.",
          "The site mainly needs SEO improvements rather than a rebuild.",
          "You also need broader Local SEO work beyond the website.",
          "You want to improve your Google Business Profile, citations, local presence, and rankings alongside the "
          "existing website."],
    vs_cta="Explore Local SEO", vs_href="/services/local-seo/",
    # 8. WHAT'S INCLUDED
    inc_h="What’s included in Website + Local SEO?",
    inc_lead="The exact scope depends on the size of your business and the website you need, but the service is built "
             "around a strong local-search foundation from the start.",
    inc_items=[
        ("Website Structure & Core Pages", "A clear site structure based on your business, services, and customer journey."),
        ("Local SEO Foundation", "The website is built with your location and local search relevance considered from the beginning."),
        ("On-Page Optimization", "Core pages are organized and optimized so search engines can more clearly understand their purpose."),
        ("Service Page Setup", "Important services receive the page structure they need instead of being buried inside generic website copy."),
        ("Local Business Information", "Your important business details are presented clearly and consistently throughout the site where appropriate."),
        ("Internal Linking", "Related pages are connected naturally to make navigation clearer for customers and search engines."),
        ("Essential Search Setup", "We prepare the website with the core search-engine elements needed for a strong launch and future SEO work."),
    ],
    # 9. PRICING
    pr_eb="Pricing",
    pr_h="Website + Local SEO",
    pr_p=[
        "Final pricing depends on the number of pages, the amount of content required, the complexity of the website, "
        "and the Local SEO structure your business needs.",
        "We review the project first and provide a clear scope and quote before the build begins.",
    ],
    pr_cta="Get a Free Website Consultation",
    pr_small="The starting price applies to smaller local-business websites. Larger or more complex sites are quoted "
             "based on scope.",
    # 10. FAQ
    faq_h="Frequently asked questions",
    faq=[
        ("What is an SEO-ready website?",
         "An SEO-ready website is structured so search engines can clearly understand the business, its services, and "
         "its local relevance. It also gives visitors a clear way to navigate the site and take action."),
        ("Is Local SEO included with the website?",
         "The website includes a Local SEO foundation, including local relevance, on-page structure, service-page setup, "
         "and internal linking. Broader Local SEO work such as Google Business Profile optimization, citations, ongoing "
         "rank tracking, or continued growth can require a separate Local SEO Campaign."),
        ("Do I need a separate page for every service?",
         "Not necessarily. The right structure depends on your business and the importance of each service. We "
         "recommend dedicated pages where they help customers understand your offer and strengthen the site’s search "
         "relevance."),
        ("Can you rebuild my existing website?",
         "Yes. If your current website no longer fits your business or has structural problems that make SEO and future "
         "growth difficult, we can recommend a rebuild instead of continuing to patch the existing site."),
        ("What if my current website is already good?",
         "Then you may not need a new one. A Local SEO Campaign may be the better option if the existing website can be "
         "improved without rebuilding it."),
        ("How much does Website + Local SEO cost?",
         "Website + Local SEO starts at $1,999. Final pricing depends on the number of pages, content requirements, site "
         "complexity, and the SEO structure required for your business."),
        ("Will the website automatically rank #1 after launch?",
         "No. A strong website gives your business a better SEO foundation, but rankings depend on multiple factors "
         "beyond the website itself. Some businesses also need Google Business Profile optimization, citations, ongoing "
         "Local SEO work, and time to compete effectively."),
        ("Do you only build websites for Orlando businesses?",
         "Orlando is our primary local market. If your business is based in or serves a nearby Central Florida area, we "
         "can review the project and determine whether the service is a good fit."),
    ],
    # 11. FINAL CTA
    final_h="Build your website around the customers you want to reach.",
    final_p=[
        "Tell us about your business, services, and current website.",
        "We’ll review what you need and recommend a website structure that supports both your customers and your local "
        "search presence.",
    ],
    final_cta="Get a Free Website Consultation",
    final_small="No obligation. Just a clear starting point for your website project.",
)


SITE_MOCK = dict(
    en=dict(aria="Example structure of an SEO-ready local business website", url="yourbusiness.com", home="Homepage",
            services="Services", about="About", contact="Contact", svc="Service", svc_l="Service pages",
            area_l="Service areas", tag="Example structure"),
    es=dict(aria="Ejemplo de estructura de un sitio web local listo para SEO", url="sunegocio.com", home="Inicio",
            services="Servicios", about="Nosotros", contact="Contacto", svc="Servicio", svc_l="Páginas de servicio",
            area_l="Zonas de servicio", tag="Estructura de ejemplo"),
)


def site_mock(lang="en"):
    """Illustrative site structure inside a browser frame (generic pages, no real business)."""
    m = SITE_MOCK[lang]
    node = lambda t, cls="", d=0: f'<span class="sm-node {cls}" style="--d:{d}">{t}</span>'
    return f"""<div class="smock" role="img" aria-label="{m['aria']}">
  <div class="sm-bar"><span></span><span></span><span></span><b>{m['url']}</b></div>
  <div class="sm-body">
    <div class="sm-row sm-top">{node(m['home'], 'home', 0)}</div>
    <div class="sm-row sm-mid">{node(m['services'], 'hub', 1)}{node(m['about'], '', 2)}{node(m['contact'], 'cta', 3)}</div>
    <div class="sm-row sm-leaf">{node(m['svc'] + ' A', 'svc', 4)}{node(m['svc'] + ' B', 'svc', 5)}{node(m['svc'] + ' C', 'svc', 6)}</div>
    <div class="sm-row sm-area">{node('Orlando', 'area', 7)}{node('Winter Park', 'area', 8)}{node('Kissimmee', 'area', 9)}</div>
    <div class="sm-legend"><span><i class="k k-svc"></i>{m['svc_l']}</span><span><i class="k k-area"></i>{m['area_l']}</span></div>
  </div>
  <span class="gm-tag">{m['tag']}</span>
</div>"""


CSS = """
/* ---- website + local seo page ---- */
.smock{position:relative;width:min(100%,440px);background:#fff;border:1px solid var(--line);border-radius:18px;box-shadow:0 30px 60px -30px rgba(12,12,13,.35),0 2px 8px rgba(12,12,13,.05);overflow:hidden}
.sm-bar{display:flex;align-items:center;gap:.4rem;padding:.7rem .9rem;border-bottom:1px solid var(--line);background:var(--bg-2,#F6F5F2)}
.sm-bar span{width:10px;height:10px;border-radius:50%;background:#E0DED8}
.sm-bar b{margin-left:.6rem;flex:0 1 auto;font:500 .78rem/1 var(--f-mono);color:var(--muted);background:#fff;border:1px solid var(--line);border-radius:99px;padding:.45rem .8rem}
.sm-body{position:relative;padding:1.6rem 1.2rem 1.2rem;display:grid;gap:1.35rem}
.sm-row{position:relative;display:flex;justify-content:center;gap:.6rem}
.sm-row + .sm-row::before{content:"";position:absolute;left:16%;right:16%;top:-.7rem;height:1.5px;background:var(--line-2)}
.sm-row + .sm-row::after{content:"";position:absolute;left:50%;top:-1.35rem;width:1.5px;height:.65rem;background:var(--line-2)}
.sm-top::before,.sm-top::after{display:none}
.sm-node{position:relative;flex:1;max-width:130px;text-align:center;padding:.6rem .4rem;border-radius:10px;border:1px solid var(--line);background:#fff;font:600 .8rem/1.2 var(--f-body);color:var(--ink-2);
  opacity:0;transform:translateY(6px);animation:gm-in .5s var(--ease) forwards;animation-delay:calc(.5s + var(--d) * .14s)}
.sm-node::before{content:"";position:absolute;left:50%;top:-.7rem;width:1.5px;height:.7rem;background:var(--line-2)}
.sm-top .sm-node::before{display:none}
.sm-node.home{max-width:180px;background:var(--ink);color:#fff;border-color:var(--ink)}
.sm-node.hub{border-color:var(--gold);background:var(--gold-soft,#FFF4E0)}
.sm-node.svc{border-color:#F6CF8C;background:#FFFAF0}
.sm-node.area{border-style:dashed;border-color:#9DC3E6;background:#F3F8FD;color:#1A5FB4}
.sm-node.cta{border-color:#9BD7B8;background:#F1FAF5;color:#14955A}
.sm-legend{display:flex;justify-content:center;gap:1rem;padding-top:.9rem;border-top:1px solid var(--line);font-size:.75rem;color:var(--muted)}
.sm-legend span{display:flex;align-items:center;gap:.4rem}
.k{flex:none;width:10px;height:10px;padding:0;border-radius:3px;border:1px solid}
.k.k-svc{border-color:#F6CF8C;background:#FFFAF0}.k.k-area{border-color:#9DC3E6;border-style:dashed;background:#F3F8FD}
@media (max-width:520px){.smock .gm-tag{display:none}}
@media (prefers-reduced-motion:reduce){.sm-node{opacity:1;transform:none;animation:none}}
.plist{list-style:none;margin:.5rem 0 1rem;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:.5rem}
.plist li{display:flex;align-items:center;gap:.6rem;padding:.7rem .85rem;background:#fff;border:1px solid var(--line);border-radius:12px;font-weight:600;font-size:.95rem}
.plist li span{font:600 .7rem/1 var(--f-mono);color:var(--gold-deep)}
@media (max-width:520px){.plist{grid-template-columns:1fr}}
.inc-list{display:grid;grid-template-columns:1fr 1fr;gap:0 3rem;border-top:1px solid var(--line)}
.inc-list > div{display:grid;grid-template-columns:2.4rem 1fr;gap:.2rem 1rem;padding:1.25rem 0;border-bottom:1px solid var(--line)}
.inc-list b{grid-row:span 2;font:600 .8rem/1.6 var(--f-mono);color:var(--gold-deep)}
.inc-list h3{font-size:1.05rem;font-weight:700}
.inc-list p{color:var(--muted);font-size:.95rem}
@media (max-width:760px){.inc-list{grid-template-columns:1fr}}
.emph-alt{background:var(--bg-2,#F6F5F2)}
"""



_P = P  # English copy; Spanish comes in via ctx["P"]

def render(ctx):
    P = ctx.get("P") or _P
    lang = ctx.get("lang", "en")
    e, icon = ctx["e"], ctx["icon"]
    arr = '<span class="arr" aria-hidden="true">→</span>'
    paras = lambda ps: "".join(f"<p>{e(p)}</p>" for p in ps)
    cards = lambda items: "".join(f'<div class="card reveal"><span class="ico">{icon(k)}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>'
                                  for k, t, d in items)
    ticks = lambda items: '<ul class="ticks">' + "".join(f"<li>{e(i)}</li>" for i in items) + "</ul>"
    plist = '<ul class="plist">' + "".join(f"<li><span>0{i + 1}</span>{e(t)}</li>" for i, t in enumerate(P["st_list"])) + "</ul>"
    inc = "".join(f'<div class="reveal"><b>0{i + 1}</b><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(P["inc_items"]))
    H = ctx["home"]
    final_side = ("".join(f'<p class="lead">{e(p)}</p>' for p in P["final_p"])
                  + f'<p class="final-small">{e(P["final_small"])}</p>')
    form_html = ctx["form"](lang, h2=P["final_h"], side_extra=final_side, sec_id="audit", audit=dict(
        services=H["form_services"], service_label=H["form_service_label"], msg_label=H["form_msg_label"],
        submit=P["final_cta"], selected="site"))
    return f"""<main id="main">
{sp.hero(ctx, P, site_mock(lang), ctx['crumb_items'])}
<section id="results"><div class="wrap">
  <div class="sec-head reveal"><h2>{e(P['res_h'])}</h2>{''.join(f'<p class="lead">{e(p)}</p>' for p in P['res_lead'])}</div>
  <div class="why">{cards(P['res_items'])}</div>
</div></section>
<section class="alt" id="problem"><div class="wrap problem">
  <div class="sec-head reveal" style="margin-bottom:0"><h2>{e(P['prob_h'])}</h2></div>
  <div class="reveal"><div class="prose">{paras(P['prob_p'])}</div><p class="callout"><strong>{e(P['prob_close'])}</strong></p></div>
</div></section>
<section id="seo-ready"><div class="wrap">
  <div class="sec-head reveal"><h2>{e(P['ready_h'])}</h2><p class="lead">{e(P['ready_lead'])}</p></div>
  <div class="grid3">{cards(P['ready_items'])}</div>
</div></section>
<section class="alt" id="structure"><div class="wrap problem">
  <div class="sec-head reveal" style="margin-bottom:0"><h2>{e(P['st_h'])}</h2></div>
  <div class="reveal"><div class="prose">{paras(P['st_p'])}</div>{plist}<div class="prose">{paras(P['st_after'])}</div></div>
</div></section>
<section id="relevance"><div class="wrap problem">
  <div class="sec-head reveal" style="margin-bottom:0"><h2>{e(P['rel_h'])}</h2></div>
  <div class="reveal"><div class="prose">{paras(P['rel_p'])}</div><p class="emph emph-alt"><strong>{e(P['rel_close'])}</strong></p></div>
</div></section>
<section class="alt" id="compare"><div class="wrap">
  <div class="sec-head reveal"><h2>{e(P['vs_h'])}</h2><div class="prose">{paras(P['vs_p'])}</div></div>
  <div class="vs">
    <div class="card reveal"><h3>{e(P['vs_a_h'])}</h3>{ticks(P['vs_a'])}</div>
    <div class="card dark reveal"><h3>{e(P['vs_b_h'])}</h3>{ticks(P['vs_b'])}
      <a class="link" href="{P['vs_href']}">{e(P['vs_cta'])} {arr}</a></div>
  </div>
</div></section>
<section id="included"><div class="wrap">
  <div class="sec-head reveal"><h2>{e(P['inc_h'])}</h2><p class="lead">{e(P['inc_lead'])}</p></div>
  <div class="inc-list">{inc}</div>
</div></section>
{sp.price_panel(ctx, P, P['pr_eb'], P['pr_h'], P['pr_p'], P['pr_cta'], P['pr_small'])}
<section class="alt" id="faq"><div class="wrap faq-grid">
  <div><div class="sec-head reveal" style="margin-bottom:0"><p class="eyebrow">FAQ</p><h2>{e(P['faq_h'])}</h2></div></div>
  <div class="faq reveal">{ctx['faq_items'](P['faq'])}</div>
</div></section>
<div class="final-cta">{form_html}</div>
</main>"""
