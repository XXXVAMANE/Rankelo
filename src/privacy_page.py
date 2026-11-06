"""Privacy policy (/privacy/, /es/privacidad/). Plain-language summary of what the site collects."""

EN = dict(
    url="/privacy/",
    title="Privacy Policy | Rankelo",
    desc="How Rankelo collects and uses information on rankelo.org, including the request form, Google Sheets and the Meta Pixel.",
    eb="Legal", h1=("Privacy", "Policy"),
    lead="Last updated: November 6, 2026. This page explains what information rankelo.org collects and how we use it.",
    sections=[
        ("Information you send us",
         ["When you submit a request form, we receive the details you enter: your name, business name, email, phone, "
          "website, the service you’re interested in and your message. We use this only to reply to you and to prepare "
          "your audit or quote.",
          "Form submissions are delivered to our email through Web3Forms and saved to a private Google Sheet that only "
          "our team can access. We don’t sell or rent your information."]),
        ("Emails and calls",
         ["If you email contact@rankelo.org or call us, we keep that conversation so we can follow up on your request."]),
        ("Advertising and analytics (Meta Pixel)",
         ["We use the Meta Pixel, a tool from Meta Platforms, Inc. (Facebook and Instagram). It uses cookies and similar "
          "technology to record visits to our pages and whether a request form was submitted. This helps us measure our "
          "ads and show them to people who may be interested, including people who have visited our website.",
          "The Pixel does not receive the contents of the form you fill out. Meta’s use of this data is described in "
          "Meta’s Privacy Policy. You can control ad preferences in your Facebook or Instagram settings, and you can "
          "block cookies in your browser settings."]),
        ("Hosting",
         ["Our website is hosted on Cloudflare, which may process technical data such as your IP address to deliver the "
          "site securely."]),
        ("Your choices",
         ["You can ask us to see, correct or delete the information you sent us at any time. Email contact@rankelo.org "
          "and we’ll take care of it."]),
        ("Contact",
         ["Rankelo · Orlando, Florida · contact@rankelo.org · +1 (321) 616-0799"]),
    ],
)

ES = dict(
    url="/es/privacidad/",
    title="Política de privacidad | Rankelo",
    desc="Cómo Rankelo recopila y usa la información en rankelo.org, incluido el formulario de solicitud, Google Sheets y el píxel de Meta.",
    eb="Legal", h1=("Política de", "privacidad"),
    lead="Última actualización: 6 de noviembre de 2026. Esta página explica qué información recopila rankelo.org y cómo la usamos.",
    sections=[
        ("Información que usted nos envía",
         ["Cuando envía un formulario de solicitud, recibimos los datos que escribe: su nombre, el nombre de su negocio, "
          "email, teléfono, sitio web, el servicio que le interesa y su mensaje. Los usamos solo para responderle y "
          "preparar su auditoría o presupuesto.",
          "Las solicitudes llegan a nuestro correo a través de Web3Forms y se guardan en una hoja de Google privada a la "
          "que solo accede nuestro equipo. No vendemos ni alquilamos su información."]),
        ("Correos y llamadas",
         ["Si escribe a contact@rankelo.org o nos llama, guardamos esa conversación para poder dar seguimiento a su "
          "solicitud."]),
        ("Publicidad y analítica (píxel de Meta)",
         ["Usamos el píxel de Meta, una herramienta de Meta Platforms, Inc. (Facebook e Instagram). Utiliza cookies y "
          "tecnologías similares para registrar las visitas a nuestras páginas y si se envió un formulario de solicitud. "
          "Esto nos ayuda a medir nuestros anuncios y mostrarlos a personas que puedan estar interesadas, incluidas las "
          "que ya visitaron nuestro sitio web.",
          "El píxel no recibe el contenido del formulario que usted completa. El uso que Meta hace de estos datos se "
          "describe en la Política de privacidad de Meta. Puede controlar sus preferencias de anuncios en la "
          "configuración de Facebook o Instagram y bloquear las cookies en la configuración de su navegador."]),
        ("Alojamiento",
         ["Nuestro sitio web está alojado en Cloudflare, que puede procesar datos técnicos como su dirección IP para "
          "mostrar el sitio de forma segura."]),
        ("Sus opciones",
         ["Puede pedirnos en cualquier momento ver, corregir o eliminar la información que nos envió. Escriba a "
          "contact@rankelo.org y nos encargaremos."]),
        ("Contacto",
         ["Rankelo · Orlando, Florida · contact@rankelo.org · +1 (321) 616-0799"]),
    ],
)


def render(e, P):
    body = "".join(f'<h2>{e(h)}</h2>' + "".join(f"<p>{e(p)}</p>" for p in ps) for h, ps in P["sections"])
    return f'<section><div class="wrap"><div class="legal">{body}</div></div></section>'
