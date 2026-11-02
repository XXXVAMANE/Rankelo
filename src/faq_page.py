"""FAQ page (/faq/, /es/preguntas-frecuentes/). Client copy 01.11.2026; same accordion design as before.
Answers: (question, answer, extra) where extra is None, ("link", label, href) or ("list", [...], tail)."""

EN = dict(
    title="Local SEO FAQ | Rankelo Orlando",
    desc="Quick answers about Rankelo’s Local SEO services, Google Business Profile optimization, websites, pricing, "
         "timelines, and SEO Maintenance.",
    eb="FAQ", h1=("Questions,", "answered"),
    lead="Quick answers about our services, pricing, Local SEO, websites, and working with Rankelo.",
    groups=[
        ("Getting started", [
            ("How do I get started?",
             "Start with a free Local SEO audit or contact us about a specific service. We’ll review your business and "
             "recommend the best next step.", None),
            ("I don’t have a website. Can you still help?",
             "Yes. Our Website + Local SEO service is for businesses that need a new SEO-ready website.",
             ("link", "Explore Website + Local SEO", "/services/website-local-seo/")),
            ("What do I need to provide?",
             "Usually, basic business information plus access to your website or Google Business Profile when needed. "
             "We’ll tell you exactly what we need before starting.", None),
            ("Which service is right for my business?",
             "It depends on what needs improvement. You can compare all four services on our Services page, or start "
             "with a free audit.", ("link", "View All Services", "/services/")),
        ]),
        ("Results", [
            ("How fast will I see results?",
             "It varies. Some improvements can happen quickly, while stronger ranking changes usually take more time.", None),
            ("Can you guarantee the #1 position?",
             "No. No agency controls Google’s rankings or can guarantee a permanent #1 position.", None),
            ("What do you track?",
             "Depending on the service, we may track local rankings, website visibility, Google Business Profile "
             "performance, and relevant customer actions.", None),
            ("Will Local SEO keep working forever once the campaign is finished?",
             "Not automatically. Rankings and competition can change, which is why optional SEO Maintenance is available.",
             ("link", "Explore SEO Maintenance", "/services/seo-maintenance/")),
        ]),
        ("Pricing & contracts", [
            ("How much does it cost?", "Current starting prices:",
             ("list", ["Local SEO Campaign: $749", "Google Business Profile Optimization: $299 one-time",
                       "Website + Local SEO: $1,999", "SEO Maintenance: $399/month"], "Final pricing depends on scope.")),
            ("Do I have to pay every month?", "No. Only SEO Maintenance is an ongoing monthly service.", None),
            ("Is there a long-term contract?",
             "The main services do not require ongoing monthly SEO. Any Maintenance terms will be explained before you "
             "start.", None),
            ("Is the audit really free?", "Yes. The initial Local SEO audit is free and comes with no obligation.", None),
            ("Why are the prices listed as “starting at”?",
             "Because every business needs a different amount of work. We confirm the final price after reviewing your "
             "project.", None),
        ]),
        ("Working together", [
            ("Which areas do you serve?",
             "Orlando is our primary market. We also consider nearby Central Florida businesses when the project is a "
             "good fit.", None),
            ("Can I contact you in Spanish?", "Yes. You can contact us in English or Spanish.", None),
            ("Do you do SEO beyond Orlando?",
             "Yes, for some local businesses outside Orlando. Our focus is Local SEO rather than nationwide or e-commerce "
             "SEO.", None),
            ("Will I still own my website and Google Business Profile?",
             "Yes. Your website, Google Business Profile, and business accounts remain yours.", None),
            ("Do you use risky SEO tactics?",
             "No. We focus on legitimate Local SEO practices and avoid tactics that could put your Google presence at "
             "unnecessary risk.", None),
        ]),
    ],
    c_eb="Still have questions?", c_h="Didn’t find what you were looking for?",
    c_p="Send us a message and we’ll help.", c_cta="Contact Us", c_cta2="Get a Free Local SEO Audit",
)

ES = dict(
    title="Preguntas frecuentes sobre SEO local | Rankelo Orlando",
    desc="Respuestas rápidas sobre los servicios de SEO local de Rankelo, la optimización del perfil de Google Business, "
         "los sitios web, los precios, los plazos y el mantenimiento SEO.",
    eb="Preguntas", h1=("Preguntas", "frecuentes"),
    lead="Respuestas rápidas sobre nuestros servicios, precios, SEO local, sitios web y cómo es trabajar con Rankelo.",
    groups=[
        ("Cómo empezar", [
            ("¿Cómo empiezo?",
             "Empiece con una auditoría de SEO local gratis o contáctenos sobre un servicio concreto. Revisaremos su "
             "negocio y le recomendaremos el mejor siguiente paso.", None),
            ("No tengo sitio web. ¿Pueden ayudarme igual?",
             "Sí. Nuestro servicio de sitio web + SEO local es para negocios que necesitan un sitio web nuevo listo para SEO.",
             ("link", "Ver sitio web + SEO local", "/es/servicios/sitio-web-seo-local/")),
            ("¿Qué tengo que proporcionar?",
             "Normalmente, la información básica del negocio y acceso a su sitio web o a su perfil de Google Business "
             "cuando hace falta. Le diremos exactamente qué necesitamos antes de empezar.", None),
            ("¿Qué servicio es el adecuado para mi negocio?",
             "Depende de lo que necesite mejorar. Puede comparar los cuatro servicios en nuestra página de servicios o "
             "empezar con una auditoría gratis.", ("link", "Ver todos los servicios", "/es/servicios/")),
        ]),
        ("Resultados", [
            ("¿Qué tan rápido veré resultados?",
             "Depende. Algunas mejoras pueden notarse rápido, mientras que los cambios más fuertes en las posiciones "
             "suelen tardar más.", None),
            ("¿Pueden garantizar el puesto #1?",
             "No. Ninguna agencia controla las posiciones de Google ni puede garantizar un puesto #1 permanente.", None),
            ("¿Qué miden?",
             "Según el servicio, podemos hacer seguimiento de las posiciones locales, la visibilidad del sitio web, el "
             "rendimiento del perfil de Google Business y las acciones relevantes de los clientes.", None),
            ("¿El SEO local seguirá funcionando para siempre cuando termine la campaña?",
             "No de forma automática. Las posiciones y la competencia pueden cambiar; por eso ofrecemos el mantenimiento "
             "SEO opcional.", ("link", "Ver mantenimiento SEO", "/es/servicios/mantenimiento-seo/")),
        ]),
        ("Precios y contratos", [
            ("¿Cuánto cuesta?", "Precios iniciales actuales:",
             ("list", ["Campaña de SEO local: $749", "Optimización del perfil de Google Business: $299, pago único",
                       "Sitio web + SEO local: $1,999", "Mantenimiento SEO: $399/mes"],
              "El precio final depende del alcance.")),
            ("¿Tengo que pagar todos los meses?", "No. Solo el mantenimiento SEO es un servicio mensual continuo.", None),
            ("¿Hay un contrato a largo plazo?",
             "Los servicios principales no requieren SEO mensual continuo. Las condiciones del mantenimiento se le "
             "explicarán antes de empezar.", None),
            ("¿La auditoría es realmente gratis?", "Sí. La auditoría inicial de SEO local es gratis y sin compromiso.", None),
            ("¿Por qué los precios aparecen como «desde»?",
             "Porque cada negocio necesita una cantidad de trabajo distinta. Confirmamos el precio final después de "
             "revisar su proyecto.", None),
        ]),
        ("Cómo trabajamos", [
            ("¿En qué zonas trabajan?",
             "Orlando es nuestro mercado principal. También consideramos negocios cercanos del centro de Florida cuando "
             "el proyecto encaja.", None),
            ("¿Puedo comunicarme con ustedes en español?", "Sí. Puede escribirnos en español o en inglés.", None),
            ("¿Hacen SEO fuera de Orlando?",
             "Sí, para algunos negocios locales fuera de Orlando. Nos enfocamos en el SEO local, no en el SEO nacional ni "
             "en el de tiendas en línea.", None),
            ("¿Seguiré siendo dueño de mi sitio web y de mi perfil de Google Business?",
             "Sí. Su sitio web, su perfil de Google Business y las cuentas de su negocio siguen siendo suyos.", None),
            ("¿Usan tácticas de SEO arriesgadas?",
             "No. Nos enfocamos en prácticas legítimas de SEO local y evitamos tácticas que puedan poner en riesgo "
             "innecesario su presencia en Google.", None),
        ]),
    ],
    c_eb="¿Todavía tiene preguntas?", c_h="¿No encontró lo que buscaba?",
    c_p="Envíenos un mensaje y le ayudaremos.", c_cta="Contáctenos", c_cta2="Solicitar auditoría de SEO local gratis",
)


def answer_text(a, extra):
    """Plain-text answer for FAQPage schema."""
    if extra and extra[0] == "list":
        return a + " " + "; ".join(extra[1]) + ". " + extra[2]
    return a


def render(e, P, contact_url):
    arr = '<span class="arr" aria-hidden="true">→</span>'

    def item(q, a, extra):
        more = ""
        if extra and extra[0] == "link":
            more = f'<p><a class="link" href="{extra[2]}">{e(extra[1])} {arr}</a></p>'
        elif extra and extra[0] == "list":
            more = '<ul class="ticks faq-ticks">' + "".join(f"<li>{e(x)}</li>" for x in extra[1]) + f"</ul><p>{e(extra[2])}</p>"
        return f"<details><summary>{e(q)}</summary><p>{e(a)}</p>{more}</details>"

    cats = "".join(f'<h2 class="faq-cat">{e(c)}</h2>' + "".join(item(*x) for x in qs) for c, qs in P["groups"])
    return f"""<section><div class="wrap"><div class="faq reveal" style="max-width:860px">{cats}</div></div></section>
<section class="tight" id="contact-us"><div class="wrap"><div class="ns card dark reveal">
  <div><p class="eyebrow" style="color:#C3C3C8">{e(P['c_eb'])}</p><h2 style="margin-top:.6rem">{e(P['c_h'])}</h2></div>
  <div class="ns-body"><p>{e(P['c_p'])}</p>
    <a class="btn btn-gold" href="{contact_url}" data-magnet><span>{e(P['c_cta'])}</span>{arr}</a>
    <a class="link" style="color:#fff" href="{contact_url}#audit">{e(P['c_cta2'])} {arr}</a></div>
</div></div></section>"""
