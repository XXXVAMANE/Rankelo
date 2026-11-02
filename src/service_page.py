"""Shared building blocks for Rankelo service pages (Local SEO, GBP, ...).
Service pages use their own focused hero so they don't read as the homepage."""


def crumbs(e, items):
    """items: [(name, href)], last one is the current page. Rendered as 'Services → Page'."""
    parts = []
    for i, (n, p) in enumerate(items):
        parts.append(f'<a href="{p}">{e(n)}</a>' if i < len(items) - 1 else f'<span aria-current="page">{e(n)}</span>')
    return '<nav class="scrumbs in" style="--i:0" aria-label="Breadcrumb">' + '<span aria-hidden="true">→</span>'.join(parts) + "</nav>"


def hero(ctx, P, visual, crumb_items):
    e = ctx["e"]
    arr = '<span class="arr" aria-hidden="true">→</span>'
    unit = f'<i>{e(P["price_unit"])}</i>' if P.get("price_unit") else ""
    return f"""<div class="shero">
  <div class="wrap shero-grid">
    <div>
      {crumbs(e, crumb_items)}
      <p class="eyebrow in" style="--i:1">{e(P['eyebrow'])}</p>
      <h1 class="in" style="--i:1">{e(P['h1'])}</h1>
      <p class="lead in" style="--i:2">{e(P['sub'])}</p>
      <div class="sprice in" style="--i:3"><small>{e(P['price_label'])}</small><b>{e(P['price'])}{unit}</b></div>
      <div class="hero-ctas in" style="--i:3">
        <a class="btn btn-dark shine" href="#audit" data-magnet><span>{e(P['cta1'])}</span>{arr}</a>
        <a class="btn btn-ghost btn-quiet" href="#included"><span>{e(P['cta2'])}</span></a>
      </div>
      <p class="hero-note in" style="--i:4">{e(P['note'])}</p>
    </div>
    <div class="shero-visual in" style="--i:2">{visual}</div>
  </div>
</div>"""


def price_panel(ctx, P, eb, h, paras, cta, small):
    e = ctx["e"]
    arr = '<span class="arr" aria-hidden="true">→</span>'
    unit = f' <i>{e(P["price_unit"])}</i>' if P.get("price_unit") else ""
    body = "".join(f"<p>{e(p)}</p>" for p in paras)
    return f"""<section id="pricing"><div class="wrap">
  <div class="price-panel card dark reveal">
    <div>
      <p class="eyebrow">{e(eb)}</p>
      <h2>{e(h)}</h2>
      <div class="price"><small>{e(P['price_label'])}</small><b>{e(P['price'])}{unit}</b></div>
    </div>
    <div class="price-panel-body">
      {body}
      <a class="btn btn-gold" href="#audit" data-magnet><span>{e(cta)}</span>{arr}</a>
      <small>{e(small)}</small>
    </div>
  </div>
</div></section>"""


GBP_MOCK = dict(
    en=dict(aria="Example of an optimized Google Business Profile", name="Your Business Name",
            cat="Roofing contractor · Orlando, FL", acts=["Call", "Directions", "Website", "Save"],
            area="Orlando, FL · Serves Central Florida", open="Open", closes="Closes 6 PM", svc="Services",
            chips=["Roof repair", "Roof replacement", "Inspections", "Storm damage"],
            meter="Profile completeness", tag="Example profile"),
    es=dict(aria="Ejemplo de un perfil de Google Business optimizado", name="Nombre de su negocio",
            cat="Contratista de techos · Orlando, FL", acts=["Llamar", "Cómo llegar", "Sitio web", "Guardar"],
            area="Orlando, FL · Atiende el centro de Florida", open="Abierto", closes="Cierra a las 6 PM", svc="Servicios",
            chips=["Reparación de techos", "Techos nuevos", "Inspecciones", "Daños por tormenta"],
            meter="Perfil completo", tag="Perfil de ejemplo"),
)


def gbp_mock(lang="en"):
    """Illustrative Google Business Profile card (generic, no real business)."""
    m = GBP_MOCK[lang]
    star = '<svg viewBox="0 0 24 24" width="13" height="13" aria-hidden="true"><path fill="currentColor" d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/></svg>'
    act = lambda ico, t: f'<span class="gm-act"><span>{ico}</span>{t}</span>'
    i = lambda d: f'<svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
    call = i('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>')
    dirs = i('<path d="M12 2 22 12 12 22 2 12z"/><path d="M9 13v-2h5V9l3 2.5-3 2.5v-2h-3v1"/>')
    web = i('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>')
    save = i('<path d="M6 3h12v18l-6-4-6 4z"/>')
    pin = i('<path d="M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>')
    clock = i('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>')
    phone = i('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>')
    chk = '<span class="gm-ok" aria-hidden="true"></span>'
    return f"""<div class="gmock" role="img" aria-label="{m['aria']}">
  <div class="gm-photos"><span></span><span></span><span></span></div>
  <div class="gm-body">
    <div class="gm-head">
      <b class="gm-name">{m['name']}</b>
      <span class="gm-rate">4.9 <span class="gm-stars">{star*5}</span> <span class="gm-muted">(128)</span></span>
      <span class="gm-cat">{m['cat']} {chk}</span>
    </div>
    <div class="gm-acts">{act(call, m['acts'][0])}{act(dirs, m['acts'][1])}{act(web, m['acts'][2])}{act(save, m['acts'][3])}</div>
    <ul class="gm-info">
      <li>{pin}<span>{m['area']}</span>{chk}</li>
      <li>{clock}<span><b class="gm-open">{m['open']}</b> · {m['closes']}</span>{chk}</li>
      <li>{phone}<span>(407) 555-0100</span>{chk}</li>
    </ul>
    <div class="gm-svc"><small>{m['svc']}</small>
      <div>{''.join(f'<span>{c}</span>' for c in m['chips'])}</div></div>
    <div class="gm-meter"><div class="gm-meter-top"><small>{m['meter']}</small><b>100%</b></div><div class="gm-bar"><span></span></div></div>
  </div>
  <span class="gm-tag">{m['tag']}</span>
</div>"""


CSS = """
/* ---- service pages (shared) ---- */
.shero{position:relative;background:var(--bg-2,#F6F5F2);border-bottom:1px solid var(--line);padding-block:clamp(2rem,5vw,3.5rem) clamp(2.5rem,5vw,4rem);overflow:hidden}
.shero::before{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(12,12,13,.07) 1px,transparent 1px);background-size:22px 22px;mask-image:linear-gradient(90deg,transparent 30%,#000 75%);pointer-events:none}
.shero-grid{position:relative;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:3rem;align-items:center}
@media (max-width:960px){.shero-grid{grid-template-columns:1fr}}
.scrumbs{display:flex;flex-wrap:wrap;align-items:center;gap:.5rem;font:500 .8rem/1.4 var(--f-mono);color:var(--muted);margin-bottom:1.4rem}
.scrumbs a{color:var(--ink-2);text-decoration:none;border-bottom:1px solid var(--line-2)}
.scrumbs a:hover{color:var(--ink);border-bottom-color:var(--gold)}
.scrumbs span[aria-current]{color:var(--ink);font-weight:600}
.shero h1{font-size:clamp(2.1rem,4.6vw,3.35rem);margin-block:.9rem 1rem;max-width:18ch}
.shero .lead{max-width:52ch}
.sprice{margin-top:1.5rem;display:inline-grid;gap:.35rem;padding:.95rem 1.25rem;background:#fff;border:1px solid var(--line);border-left:4px solid var(--gold);border-radius:0 14px 14px 0}
.sprice small{font:600 .72rem/1 var(--f-mono);letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.sprice b{font:700 2.2rem/1 var(--f-display);letter-spacing:-.03em}
.sprice b i,.price-panel .price b i{font:500 1rem/1 var(--f-body);font-style:normal;letter-spacing:0;color:var(--muted);margin-left:.4rem}
.price-panel .price b i{color:#C3C3C8}
.sprice + .hero-ctas{margin-top:1.5rem}
.shero-visual{display:flex;justify-content:center}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:1rem}
.grid3 .card,.why .card{padding:1.5rem;display:grid;gap:.7rem;align-content:start}
.grid3 h3{font-size:1.08rem;font-weight:700}
.grid3 p{color:var(--muted);font-size:.95rem}
@media (max-width:960px){.grid3{grid-template-columns:1fr 1fr}}
@media (max-width:600px){.grid3{grid-template-columns:1fr}}
.vs{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:2rem}
.vs .card{padding:1.75rem;display:grid;gap:1rem;align-content:start}
.vs h3{font-size:1.2rem;font-weight:700}
.vs .card.dark h3{color:#fff}
@media (max-width:760px){.vs{grid-template-columns:1fr}}
.vs-foot{margin-top:1.5rem}
.vs .link{justify-self:start}
/* GBP mockup */
.gmock{position:relative;width:min(100%,420px);background:#fff;border:1px solid var(--line);border-radius:22px;box-shadow:0 30px 60px -30px rgba(12,12,13,.35),0 2px 8px rgba(12,12,13,.05);overflow:hidden;font-size:.9rem}
.gm-photos{display:grid;grid-template-columns:2fr 1fr 1fr;gap:3px;height:96px}
.gm-photos span{background:linear-gradient(135deg,#FFE3B3,#FFB547)}
.gm-photos span:nth-child(2){background:linear-gradient(135deg,#E9E7E1,#CFCBC2)}
.gm-photos span:nth-child(3){background:linear-gradient(135deg,#DDE8F3,#B9CBE0)}
.gm-body{padding:1.1rem 1.2rem 1.25rem;display:grid;gap:.9rem}
.gm-head{display:grid;gap:.3rem}
.gm-name{font:700 1.2rem/1.2 var(--f-display);letter-spacing:-.02em}
.gm-rate{display:flex;align-items:center;gap:.35rem;font-weight:600}
.gm-stars{display:inline-flex;color:#F2A20C}
.gm-muted{color:var(--muted);font-weight:400}
.gm-cat{display:flex;align-items:center;gap:.45rem;color:var(--muted)}
.gm-acts{display:grid;grid-template-columns:repeat(4,1fr);gap:.4rem;padding-block:.15rem .2rem;border-bottom:1px solid var(--line);padding-bottom:.9rem}
.gm-act{display:grid;justify-items:center;gap:.35rem;font-size:.76rem;font-weight:600;color:#1A5FB4}
.gm-act>span{width:36px;height:36px;border-radius:50%;display:grid;place-items:center;border:1px solid var(--line-2);color:#1A5FB4}
.gm-info{list-style:none;margin:0;padding:0;display:grid;gap:.55rem}
.gm-info li{display:grid;grid-template-columns:18px 1fr auto;gap:.6rem;align-items:center;color:var(--ink-2)}
.gm-info svg{color:var(--muted)}
.gm-open{color:#14955A}
.gm-svc{display:grid;gap:.45rem}
.gm-svc small,.gm-meter small{font:600 .68rem/1 var(--f-mono);letter-spacing:.07em;text-transform:uppercase;color:var(--muted)}
.gm-svc div{display:flex;flex-wrap:wrap;gap:.35rem}
.gm-svc div span{padding:.32rem .6rem;border-radius:999px;background:var(--bg-2,#F6F5F2);border:1px solid var(--line);font-size:.78rem;font-weight:500;opacity:0;animation:gm-in .5s var(--ease) forwards}
.gm-svc div span:nth-child(1){animation-delay:1.1s}.gm-svc div span:nth-child(2){animation-delay:1.3s}
.gm-svc div span:nth-child(3){animation-delay:1.5s}.gm-svc div span:nth-child(4){animation-delay:1.7s}
.gm-meter{display:grid;gap:.45rem;padding-top:.85rem;border-top:1px solid var(--line)}
.gm-meter-top{display:flex;justify-content:space-between;align-items:center}
.gm-meter-top b{font:700 .95rem/1 var(--f-mono);color:#14955A}
.gm-bar{height:8px;border-radius:99px;background:var(--line);overflow:hidden}
.gm-bar span{display:block;height:100%;width:100%;border-radius:99px;background:linear-gradient(90deg,var(--gold),#14955A);transform-origin:left;transform:scaleX(.38);animation:gm-fill 1.8s var(--ease) .8s forwards}
.gm-ok{width:16px;height:16px;border-radius:50%;background:#14955A url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M6 12.5l4 4 8-9' fill='none' stroke='%23fff' stroke-width='3.2' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center/11px no-repeat;opacity:0;transform:scale(.4);animation:gm-pop .45s var(--ease) forwards}
.gm-cat .gm-ok{animation-delay:1.9s}.gm-info li:nth-child(1) .gm-ok{animation-delay:2.1s}
.gm-info li:nth-child(2) .gm-ok{animation-delay:2.3s}.gm-info li:nth-child(3) .gm-ok{animation-delay:2.5s}
.gm-tag{position:absolute;top:.75rem;right:.75rem;font:600 .66rem/1 var(--f-mono);letter-spacing:.06em;text-transform:uppercase;background:rgba(255,255,255,.92);color:var(--ink-2);padding:.4rem .55rem;border-radius:999px}
@keyframes gm-fill{to{transform:scaleX(1)}}
@keyframes gm-pop{to{opacity:1;transform:none}}
@keyframes gm-in{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion:reduce){.gm-bar span{transform:none;animation:none}.gm-ok,.gm-svc div span{opacity:1;transform:none;animation:none}}
"""
