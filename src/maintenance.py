"""SEO Maintenance service page (/services/seo-maintenance/). Client copy, 01.11.2026."""
import service_page as sp

URL = "/services/seo-maintenance/"
P = dict(
    title="BEST Local SEO Maintenance Orlando | SEO Monitoring & Updates Near Me | Rankelo",
    desc="Ongoing Local SEO maintenance for Orlando businesses. Monitor rankings, handle smaller SEO updates, maintain "
         "your local presence, and keep an eye on competitors. Starting at $399/month.",
    crumb="SEO Maintenance",
    eyebrow="Ongoing Local SEO Support",
    h1="SEO Maintenance for Orlando Businesses",
    sub="Keep your local visibility monitored, maintained, and supported after the main SEO work is complete.",
    price_label="Starting at", price="$399", price_unit="/month",
    cta1="Talk to Rankelo About SEO Maintenance", cta2="See What’s Included",
    note="SEO Maintenance is designed for businesses that already have a solid SEO foundation and want continued "
         "attention to rankings, smaller updates, and their local search presence.",
    # 2. WHY
    why_h="Good SEO still needs attention over time.",
    why_p=[
        "Completing the initial SEO work gives your business a stronger foundation, but local search does not stay "
        "completely still.",
        "Competitors update their websites and Google profiles. Rankings can move. Business information changes. New "
        "opportunities and small issues can appear over time.",
        "SEO Maintenance gives your business continued support without starting another full campaign every month.",
    ],
    why_items=[
        ("search", "Keep an eye on your visibility",
         "Monitor how your business is performing in local search and identify meaningful changes before they are "
         "ignored for months."),
        ("key", "Maintain the foundation you already built",
         "Keep important local-search elements accurate and supported as your business changes."),
        ("track", "Continue making smaller improvements",
         "Handle ongoing SEO opportunities and smaller updates without turning every change into a new standalone project."),
    ],
    # 3. WHAT WE MAINTAIN
    inc_h="Ongoing attention where it matters.",
    inc_p=["The exact work depends on your business and what was completed during the initial campaign.",
           "SEO Maintenance can include continued attention across the areas below."],
    inc_items=[
        ("reports", "Local Ranking Monitoring",
         "We keep track of your local search visibility and watch for meaningful changes in performance."),
        ("web", "Smaller Website SEO Updates",
         "We handle smaller on-page or content-related improvements when existing pages need attention."),
        ("gbp", "Google Business Profile Attention",
         "When needed, we review and maintain important parts of your Google Business Profile so the information "
         "continues to reflect the business accurately."),
        ("citations", "Local Presence Checks",
         "We keep an eye on important local business information and address relevant consistency issues when they appear."),
        ("target", "Competitor & Opportunity Monitoring",
         "We watch the local search environment for changes that may create new risks or opportunities for your business."),
    ],
    # 4. WHO
    who_h="Best for businesses that already have a solid SEO foundation.",
    who_p="SEO Maintenance makes the most sense after the main optimization work is already complete.",
    who_lead="It may be a good fit if:",
    who_list=[
        "You have already completed a Local SEO Campaign.",
        "Your Google Business Profile and website have already been optimized.",
        "Your business has established local visibility that you want to monitor.",
        "You want smaller ongoing SEO improvements without starting another full campaign.",
        "You prefer to have someone continue watching your local search presence.",
    ],
    who_close="If your business still has major SEO problems, a Local SEO Campaign may be the better starting point.",
    # 5. VS
    vs_h="Maintenance supports the foundation. A campaign builds or repairs it.",
    vs_p="These services are designed for different stages.",
    vs_a_h="Local SEO Campaign",
    vs_a="Best when your business needs broader improvements across Google Business Profile, website SEO, local "
         "presence, content, and rankings.",
    vs_a_cta="Explore Local SEO", vs_a_href="/services/local-seo/",
    vs_b_h="SEO Maintenance",
    vs_b="Best after the major work is complete and you want continued monitoring, smaller updates, and ongoing "
         "attention to your local visibility.",
    vs_b_note="You do not need to purchase SEO Maintenance after a Local SEO Campaign. It is optional.",
    # 6. PRICING
    pr_eb="Pricing", pr_h="SEO Maintenance",
    pr_p=["The exact monthly scope depends on the size of your local presence and the amount of ongoing attention your "
          "business needs.",
          "SEO Maintenance is intended for smaller continued improvements, monitoring, and upkeep rather than repeating "
          "the full initial campaign every month."],
    pr_cta="Talk to Rankelo About SEO Maintenance",
    pr_small="We’ll review the work already completed and confirm whether ongoing maintenance makes sense for your business.",
    # 7. FAQ
    faq_h="Frequently asked questions",
    faq=[
        ("What is SEO Maintenance?",
         "SEO Maintenance is ongoing support after the main SEO work has been completed. It focuses on monitoring local "
         "visibility, maintaining important SEO elements, handling smaller updates, and identifying issues or "
         "opportunities over time."),
        ("Do I need SEO Maintenance after a Local SEO Campaign?",
         "No. SEO Maintenance is optional. You can complete the initial campaign and stop there, or continue with monthly "
         "support if you want ongoing monitoring and smaller improvements."),
        ("Is SEO Maintenance the same as a Local SEO Campaign?",
         "No. A Local SEO Campaign is designed to address larger SEO opportunities and problems. SEO Maintenance is "
         "intended to support an existing foundation after the main work is complete."),
        ("What is included each month?",
         "The exact work depends on your business and current local presence. Maintenance can include local ranking "
         "monitoring, smaller website SEO updates, Google Business Profile attention, local presence checks, and "
         "competitor monitoring."),
        ("Can I start with SEO Maintenance if I have never done Local SEO?",
         "Usually, no. If your business still has major Local SEO gaps, it normally makes more sense to address those "
         "through a Local SEO Campaign first and consider Maintenance afterward."),
        ("How much does SEO Maintenance cost?",
         "SEO Maintenance starts at $399 per month. Final pricing depends on the size of your local presence and the "
         "amount of ongoing work required."),
        ("Does SEO Maintenance guarantee my rankings will never drop?",
         "No. Google rankings can change for many reasons, and no agency controls them. Maintenance helps us monitor "
         "your visibility, respond to relevant changes, and continue supporting the SEO foundation already in place."),
    ],
    # 8. FINAL CTA
    final_h="Keep your local search presence from becoming an afterthought.",
    final_p=["If the main SEO work is already complete, ongoing maintenance can help keep your local visibility monitored "
             "and your existing foundation supported.",
             "Tell us what has already been done and we’ll let you know whether SEO Maintenance makes sense for your business."],
    final_cta="Talk to Rankelo About SEO Maintenance",
    final_small="Starting at $399/month.",
)


MON_MOCK = dict(
    en=dict(aria="Example of a monthly SEO maintenance check", vis="Local visibility", status="Monitored", live="Ongoing",
            months=["Jan", "Feb", "Mar", "Apr", "May", "Jun"], check="This month’s check", tag="Example",
            rows=["Local rankings reviewed", "Google Business Profile checked", "Website updates handled", "Local listings checked"]),
    es=dict(aria="Ejemplo de una revisión mensual de mantenimiento SEO", vis="Visibilidad local", status="Monitoreada",
            live="Continuo", months=["Ene", "Feb", "Mar", "Abr", "May", "Jun"], check="Revisión de este mes", tag="Ejemplo",
            rows=["Posiciones locales revisadas", "Perfil de Google Business revisado", "Actualizaciones del sitio web hechas",
                  "Listados locales revisados"]),
)


def monitor_mock(lang="en"):
    """Illustrative monthly monitoring card (example data only)."""
    m = MON_MOCK[lang]
    pts = [(0, 64), (40, 58), (80, 50), (120, 46), (160, 40), (200, 38), (240, 33), (280, 30), (320, 29)]
    line = " ".join(f"{x},{y}" for x, y in pts)
    area = f"0,90 {line} 320,90"
    chk = '<span class="gm-ok" aria-hidden="true"></span>'
    rows = [(t, i) for i, t in enumerate(m["rows"])]
    items = "".join(f'<li style="--d:{d}"><span>{t}</span>{chk}</li>' for t, d in rows)
    return f"""<div class="mmock" role="img" aria-label="{m['aria']}">
  <div class="mm-top"><div><small>{m['vis']}</small><b>{m['status']}</b></div><span class="mm-live"><i></i>{m['live']}</span></div>
  <svg class="mm-chart" viewBox="0 0 320 90" preserveAspectRatio="none" aria-hidden="true">
    <defs><linearGradient id="mmg" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#FFB547" stop-opacity=".35"/><stop offset="1" stop-color="#FFB547" stop-opacity="0"/></linearGradient></defs>
    <path d="M0 30H320M0 60H320" stroke="#ECEBE6" stroke-width="1"/>
    <polygon points="{area}" fill="url(#mmg)"/>
    <polyline class="mm-line" points="{line}" fill="none" stroke="#0C0C0D" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round" pathLength="1"/>
  </svg>
  <div class="mm-months">{''.join(f'<span>{x}</span>' for x in m['months'])}</div>
  <div class="mm-check"><small>{m['check']}</small><ul>{items}</ul></div>
  <span class="gm-tag">{m['tag']}</span>
</div>"""


CSS = """
/* ---- seo maintenance page ---- */
.mmock{position:relative;width:min(100%,420px);background:#fff;border:1px solid var(--line);border-radius:20px;padding:1.25rem 1.25rem 1.35rem;box-shadow:0 30px 60px -30px rgba(12,12,13,.35),0 2px 8px rgba(12,12,13,.05);display:grid;gap:.9rem}
.mm-top{display:flex;justify-content:space-between;align-items:flex-start;padding-right:4.5rem}
.mm-top small,.mm-check small{font:600 .68rem/1 var(--f-mono);letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}
.mm-top b{display:block;margin-top:.35rem;font:700 1.35rem/1 var(--f-display);letter-spacing:-.02em}
.mm-live{display:inline-flex;align-items:center;gap:.4rem;font:600 .72rem/1 var(--f-mono);color:#14955A;background:#EAF7F0;padding:.4rem .6rem;border-radius:99px;position:absolute;top:3.1rem;right:1.25rem}
.mm-live i{width:7px;height:7px;border-radius:50%;background:#14955A;animation:mm-pulse 1.8s infinite}
.mm-chart{width:100%;height:110px;display:block}
.mm-line{stroke-dasharray:1;stroke-dashoffset:1;animation:mm-draw 2s var(--ease) .6s forwards}
.mm-months{display:flex;justify-content:space-between;font:500 .7rem/1 var(--f-mono);color:var(--muted);margin-top:-.4rem}
.mm-check{display:grid;gap:.55rem;padding-top:.9rem;border-top:1px solid var(--line)}
.mm-check ul{list-style:none;margin:0;padding:0;display:grid;gap:.5rem}
.mm-check li{display:flex;justify-content:space-between;align-items:center;font-size:.9rem;color:var(--ink-2)}
.mm-check li .gm-ok{animation-delay:calc(1.4s + var(--d) * .25s)}
.mmock .gm-tag{top:1rem;right:1rem}
@keyframes mm-draw{to{stroke-dashoffset:0}}
@keyframes mm-pulse{0%{box-shadow:0 0 0 0 rgba(20,149,90,.5)}70%{box-shadow:0 0 0 7px rgba(20,149,90,0)}100%{box-shadow:0 0 0 0 rgba(20,149,90,0)}}
@media (prefers-reduced-motion:reduce){.mm-line{stroke-dashoffset:0;animation:none}.mm-live i{animation:none}}
.why3{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem;margin-top:2rem}
.why3 .card{padding:1.5rem;display:grid;gap:.7rem;align-content:start}
.why3 h3{font-size:1.08rem;font-weight:700}.why3 p{color:var(--muted);font-size:.95rem}
@media (max-width:860px){.why3{grid-template-columns:1fr}}
.vs-note{color:#C3C3C8;font-size:.92rem;padding-top:.9rem;border-top:1px solid #2A2A2E}
"""



_P = P  # English copy; Spanish comes in via ctx["P"]

def render(ctx):
    P = ctx.get("P") or _P
    lang = ctx.get("lang", "en")
    e, icon = ctx["e"], ctx["icon"]
    arr = '<span class="arr" aria-hidden="true">→</span>'
    paras = lambda ps: "".join(f"<p>{e(p)}</p>" for p in ps)
    cards = lambda items, cls="card": "".join(f'<div class="{cls} reveal"><span class="ico">{icon(k)}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>'
                                              for k, t, d in items)
    ticks = '<ul class="ticks">' + "".join(f"<li>{e(i)}</li>" for i in P["who_list"]) + "</ul>"
    H = ctx["home"]
    final_side = ("".join(f'<p class="lead">{e(p)}</p>' for p in P["final_p"])
                  + f'<p class="final-small">{e(P["final_small"])}</p>')
    form_html = ctx["form"](lang, h2=P["final_h"], side_extra=final_side, sec_id="audit", audit=dict(
        services=H["form_services"], service_label=H["form_service_label"], msg_label=H["form_msg_label"],
        submit=P["final_cta"], selected="maintenance"))
    return f"""<main id="main">
{sp.hero(ctx, P, monitor_mock(lang), ctx['crumb_items'])}
<section id="why"><div class="wrap">
  <div class="problem">
    <div class="sec-head reveal" style="margin-bottom:0"><h2>{e(P['why_h'])}</h2></div>
    <div class="prose reveal">{paras(P['why_p'])}</div>
  </div>
  <div class="why3">{cards(P['why_items'])}</div>
</div></section>
<section class="alt" id="included"><div class="wrap">
  <div class="sec-head reveal"><h2>{e(P['inc_h'])}</h2><div class="prose">{paras(P['inc_p'])}</div></div>
  <div class="five">{cards(P['inc_items'], 'svc card')}</div>
</div></section>
<section id="who"><div class="wrap problem">
  <div class="sec-head reveal" style="margin-bottom:0"><h2>{e(P['who_h'])}</h2></div>
  <div class="reveal"><div class="prose"><p>{e(P['who_p'])}</p><p><b>{e(P['who_lead'])}</b></p></div>{ticks}
    <p class="emph emph-alt" style="margin-top:1.25rem"><strong>{e(P['who_close'])}</strong></p></div>
</div></section>
<section class="alt" id="compare"><div class="wrap">
  <div class="sec-head reveal"><h2>{e(P['vs_h'])}</h2><p class="lead">{e(P['vs_p'])}</p></div>
  <div class="vs">
    <div class="card reveal"><h3>{e(P['vs_a_h'])}</h3><p>{e(P['vs_a'])}</p>
      <a class="link" href="{P['vs_a_href']}">{e(P['vs_a_cta'])} {arr}</a></div>
    <div class="card dark reveal"><h3>{e(P['vs_b_h'])}</h3><p style="color:#E4E4E8">{e(P['vs_b'])}</p>
      <p class="vs-note">{e(P['vs_b_note'])}</p></div>
  </div>
</div></section>
{sp.price_panel(ctx, P, P['pr_eb'], P['pr_h'], P['pr_p'], P['pr_cta'], P['pr_small'])}
<section class="alt" id="faq"><div class="wrap faq-grid">
  <div><div class="sec-head reveal" style="margin-bottom:0"><p class="eyebrow">FAQ</p><h2>{e(P['faq_h'])}</h2></div></div>
  <div class="faq reveal">{ctx['faq_items'](P['faq'])}</div>
</div></section>
<div class="final-cta">{form_html}</div>
</main>"""
