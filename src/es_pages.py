"""Spanish (/es/) copy for the new pages. Translated from the client's English copy (01.11.2026), formal "usted"."""

U = dict(  # Spanish URLs
    home="/es/",
    services="/es/servicios/",
    local="/es/servicios/seo-local/",
    gbp="/es/servicios/perfil-de-google-business/",
    web="/es/servicios/sitio-web-seo-local/",
    maint="/es/servicios/mantenimiento-seo/",
    about="/es/nosotros/",
    audit="/es/auditoria-gratis/",
)

FORM_SERVICES = [("seo", "SEO local"), ("gbp", "Perfil de Google Business"), ("site", "Sitio web + SEO local"),
                 ("maintenance", "Mantenimiento SEO"), ("unsure", "Aún no lo sé")]

# ------------------------------------------------------------------ HOME
HOME = dict(
    title="Rankelo | SEO local para negocios de Orlando",
    desc="Rankelo ayuda a los negocios de Orlando a aparecer más arriba en Google Maps y en la búsqueda local, para "
         "que más clientes cercanos puedan encontrarlo, llamarlo y elegirlo. Solicite una auditoría de SEO local gratis.",
    eyebrow=("SEO local", "para negocios de Orlando"),
    h1=("Sea el primer negocio que la gente", "encuentra en Google."),
    sub="Rankelo ayuda a los negocios de Orlando a aparecer más arriba en Google Maps y en la búsqueda local, para que "
        "más clientes cercanos puedan encontrarlo, llamarlo y elegirlo.",
    cta1="Solicitar auditoría gratis", cta2="Ver servicios",
    note="Revisaremos su perfil de Google Business, su sitio web y su competencia local, y le mostraremos dónde están "
         "sus mayores oportunidades.",
    problem_h="Sus clientes ya están buscando negocios como el suyo.",
    problem_p=[
        "Cuando alguien en Orlando busca su servicio, normalmente contacta a uno de los primeros negocios que ve.",
        "Si su perfil de Google Business está incompleto, su sitio web no está bien optimizado o la información de su "
        "negocio no coincide en internet, la competencia puede aparecer antes que usted, incluso cuando usted ofrece "
        "un mejor servicio.",
        "Y mantenerse al día con el SEO local lleva tiempo. Usted ya está al frente de su negocio, atendiendo clientes, "
        "dirigiendo a su equipo y ocupándose de todo lo demás que implica ser dueño.",
    ],
    problem_close="Cada búsqueda en la que es difícil encontrar su negocio es otra oportunidad para que un cliente "
                  "elija a otro.",
    sol_h="Hacemos que a los clientes locales les sea más fácil encontrarlo.",
    sol_lead="Rankelo se encarga del trabajo de SEO local que ayuda a que su negocio aparezca de forma más destacada "
             "en Google Maps y en la búsqueda local. Nos enfocamos en lo que más importa para la visibilidad local y, "
             "a partir de ahí, avanzamos según lo que su negocio realmente necesita.",
    sol_items=[
        ("gbp", "Perfil de Google Business",
         "Optimizamos su perfil para que Google tenga información clara y exacta sobre su negocio, sus servicios y su "
         "ubicación."),
        ("web", "Sitio web y SEO on-page",
         "Mejoramos las páginas, la estructura y las señales locales de su sitio web para que Google entienda mejor qué "
         "ofrece y dónde lo ofrece."),
        ("citations", "Citas y presencia local",
         "Mantenemos la información de su negocio consistente en directorios y plataformas locales de confianza."),
        ("pages", "Contenido local",
         "Cuando su mercado necesita algo más que una optimización básica, creamos páginas de servicios y de zonas que "
         "refuerzan su relevancia para las búsquedas en las que quiere aparecer."),
    ],
    sol_close="Usted se ocupa de su negocio. Nosotros nos ocupamos del trabajo detrás de su visibilidad local.",
    why_eb="Por qué Rankelo",
    why_h="SEO local sin las vueltas de una agencia.",
    why_items=[
        ("chat", "Comunicación directa",
         "Usted trabaja directamente con las personas que se encargan de su SEO, así que las preguntas y decisiones no "
         "pasan por varios gerentes de cuenta."),
        ("target", "Una estrategia pensada para su negocio",
         "Empezamos por revisar sus posiciones, su sitio web, su competencia y su mercado local antes de decidir qué "
         "trabajo tiene sentido."),
        ("reports", "Alcance e informes claros",
         "Usted sabe en qué estamos trabajando, por qué lo hacemos y qué estamos midiendo."),
        ("key", "Su negocio sigue siendo suyo",
         "Su sitio web, su perfil de Google Business y las cuentas de su negocio siguen siendo de su propiedad."),
    ],
    how_eb="Cómo funciona",
    how_h="Un camino claro desde la auditoría hasta una mejor visibilidad local.",
    how_steps=[
        ("Auditoría gratis", "Revisamos su perfil de Google Business, su sitio web, su visibilidad local actual y su "
                             "competencia."),
        ("Estrategia", "Identificamos las mayores oportunidades y decidimos qué trabajo tiene más sentido para su negocio."),
        ("Optimización", "Trabajamos en las áreas que necesitan atención, como su perfil de Google Business, su sitio "
                         "web, sus citas y el contenido local cuando hace falta."),
        ("Seguimiento y mejora", "Monitoreamos sus posiciones locales, medimos el avance y ajustamos el trabajo según lo "
                                 "que muestran los datos."),
    ],
    how_cta="Solicitar auditoría gratis",
    svc_eb="Servicios",
    svc_h="Servicios de SEO local según el punto en el que está su negocio hoy.",
    svc_lead="Empiece con el servicio que se ajusta a su situación actual. Revisaremos su sitio web, su perfil de "
             "Google Business, su competencia y su mercado local antes de confirmar el alcance final.",
    offers=[
        dict(t="Campaña de SEO local", featured=True, price="$749", unit="",
             d="Mejore su visibilidad en Google Maps y en la búsqueda local con la optimización de su perfil de Google "
               "Business, SEO para su sitio web, citas, seguimiento de posiciones y trabajo adicional de SEO local "
               "cuando su mercado lo requiera.",
             cta="Ver SEO local", href="es/servicios/seo-local/", pick="seo"),
        dict(t="Optimización del perfil de Google Business", featured=False, price="$299", unit="pago único",
             d="Mejore cómo aparece su negocio en Google Maps con un perfil bien optimizado: categorías, servicios e "
               "información del negocio.",
             cta="Ver optimización del perfil", href="es/servicios/perfil-de-google-business/", pick="gbp"),
        dict(t="Sitio web + SEO local", featured=False, price="$1,999", unit="",
             d="Un sitio web profesional para su negocio local, pensado desde el principio en sus servicios, su "
               "ubicación, las conversiones y la visibilidad en la búsqueda local.",
             cta="Ver sitio web + SEO local", href="es/servicios/sitio-web-seo-local/", pick="site"),
        dict(t="Mantenimiento SEO", featured=False, price="$399", unit="/mes",
             d="Apoyo continuo y opcional después de su campaña inicial para monitorear posiciones, mantener su "
               "presencia en la búsqueda local, hacer actualizaciones menores de SEO y vigilar a la competencia.",
             cta="Ver mantenimiento SEO", href="es/servicios/mantenimiento-seo/", pick="maintenance"),
    ],
    starting="Desde",
    svc_all="Ver todos los servicios",
    svc_note="El precio final depende de su sitio web, su competencia, su zona de servicio y la cantidad de trabajo "
             "necesaria. Recibirá un alcance y un presupuesto claros antes de empezar.",
    faq_eb="Preguntas",
    faq_h="Preguntas frecuentes",
    faq=[
        ("¿Qué incluye exactamente el SEO local?",
         "El SEO local puede incluir la optimización del perfil de Google Business, SEO para el sitio web y on-page, "
         "citas, contenido local y seguimiento de posiciones. El trabajo exacto depende de lo que necesita su negocio y "
         "de lo competitivo que es su mercado."),
        ("¿Cuánto tarda el SEO local?",
         "Algunas mejoras pueden notarse con relativa rapidez, mientras que los cambios más fuertes en las posiciones "
         "suelen tardar más. Primero registramos su punto de partida y medimos el avance durante toda la campaña, en "
         "lugar de prometer una fecha exacta."),
        ("¿También optimizan mi sitio web?",
         "Sí. Su sitio web es una parte importante del SEO local. Podemos mejorar la estructura de las páginas, los "
         "títulos, los encabezados, la relevancia local, los enlaces internos y otros elementos on-page que ayudan a "
         "Google a entender mejor su negocio."),
        ("¿Tengo que pagar todos los meses?",
         "No. La campaña inicial de SEO local es independiente del SEO continuo. Al terminar la campaña, puede parar o "
         "continuar con el mantenimiento SEO mensual, que es opcional."),
        ("¿Cuánto cuesta el SEO local?",
         "Nuestras campañas de SEO local empiezan desde $749. El precio final depende de su sitio web, su competencia, "
         "su zona de servicio y la cantidad de trabajo necesaria. Primero revisamos su negocio y le damos un "
         "presupuesto claro antes de empezar."),
        ("¿Pueden garantizar que voy a estar en el puesto #1?",
         "Ninguna agencia controla las posiciones de Google ni puede garantizar un puesto #1 permanente. Nuestro "
         "objetivo es mejorar su visibilidad local con trabajo de SEO medible y hacer seguimiento de cómo cambian sus "
         "posiciones con el tiempo."),
    ],
    still_h="¿Todavía tiene preguntas?",
    still_p="Solicite una auditoría de SEO local gratis y le mostraremos qué puede estar frenando a su negocio.",
    still_cta="Solicitar auditoría gratis",
    final_h="Descubra qué está frenando a su negocio en Google.",
    final_p=[
        "Solicite una auditoría de SEO local gratis y revisaremos su perfil de Google Business, su sitio web, sus "
        "posiciones locales y su competencia.",
        "Tendrá una idea clara de qué necesita atención y qué le recomendaríamos hacer después.",
    ],
    final_cta="Solicitar auditoría de SEO local gratis",
    final_small="Sin compromiso. Solo un punto de partida claro.",
    form_service_label="¿Con qué necesita ayuda?",
    form_services=FORM_SERVICES,
    form_msg_label="Cuéntenos con qué le gustaría recibir ayuda",
)

# ------------------------------------------------------------------ LOCAL SEO
LOCAL = dict(
    url=U["local"],
    title="SEO local en Orlando | Google Maps, perfil de Google y SEO web | Rankelo",
    desc="Rankelo ayuda a los negocios de Orlando a mejorar su visibilidad en Google Maps y en la búsqueda local con el "
         "perfil de Google Business, SEO para el sitio web, citas y campañas de SEO local a la medida. Desde $749.",
    crumb="Campaña de SEO local",
    eyebrow="Campaña de SEO local",
    h1="SEO local para negocios de Orlando",
    sub="Mejore su visibilidad en Google Maps y en la búsqueda local para que más clientes cercanos encuentren su "
        "negocio cuando buscan los servicios que usted ofrece.",
    price_label="Desde", price="$749",
    cta1="Solicitar auditoría de SEO local gratis", cta2="Ver qué incluye",
    note="Revisaremos su visibilidad local actual, su sitio web, su perfil de Google Business y su competencia antes de "
         "recomendarle el alcance adecuado para su negocio.",
    res_h="Haga que más clientes de su zona lo encuentren.",
    res_lead="Cuando las personas necesitan un servicio local, Google suele ser uno de los primeros lugares donde buscan. "
             "Una mejor visibilidad local le da a su negocio más oportunidades de aparecer cuando los clientes cercanos "
             "están listos para llamar, visitar o pedir un presupuesto.",
    res_items=[
        ("maps", "Más visibilidad en Google Maps",
         "Construya una presencia más fuerte donde los clientes cercanos comparan negocios locales y deciden a quién "
         "contactar."),
        ("search", "Más visibilidad en la búsqueda local",
         "Aumente sus posibilidades de aparecer en búsquedas relacionadas con los servicios que su negocio realmente ofrece."),
        ("web", "Visitas al sitio web más calificadas",
         "Ayude a quienes buscan en su zona a llegar a las páginas que coinciden con lo que ya están buscando."),
        ("phone", "Más oportunidades de recibir la llamada",
         "Facilite que los clientes potenciales de su zona encuentren su negocio, entiendan lo que ofrece y den el "
         "siguiente paso."),
    ],
    prob_h="Un gran negocio también puede ser difícil de encontrar.",
    prob_p=[
        "Usted puede dar un servicio excelente y aun así perder clientes locales cuando la competencia aparece antes que "
        "usted en Google Maps y en la búsqueda.",
        "Google necesita señales claras y consistentes sobre qué hace su negocio, dónde trabaja y para qué búsquedas es "
        "relevante. Cuando esas señales son débiles o están incompletas, su visibilidad local puede verse afectada.",
        "Mientras tanto, su competencia sigue apareciendo cuando los clientes buscan.",
    ],
    prob_close="Si su negocio es difícil de encontrar, cada búsqueda local puede convertirse en una oportunidad para otro.",
    inc_h="Reforzamos las partes de su presencia en línea que importan para la búsqueda local.",
    inc_lead="Una campaña de SEO local analiza su negocio en conjunto. Identificamos lo que está frenando su visibilidad "
             "local y enfocamos la campaña en lo que su negocio realmente necesita.",
    inc_items=[
        ("gbp", "Perfil de Google Business",
         "Mejoramos cómo Google entiende y muestra su negocio en la búsqueda local y en Google Maps."),
        ("web", "Sitio web y SEO on-page",
         "Reforzamos su sitio web para que los buscadores entiendan con más claridad sus servicios, su ubicación y su "
         "relevancia local."),
        ("citations", "Citas y presencia local",
         "Mejoramos la consistencia y la credibilidad de la información de su negocio en las plataformas relevantes de "
         "internet."),
        ("pages", "Contenido local",
         "Cuando su mercado necesita más profundidad, reforzamos su sitio web con contenido adicional sobre servicios o "
         "zonas que apoya las búsquedas en las que quiere competir."),
        ("track", "Seguimiento de posiciones locales",
         "Registramos el punto de partida de su negocio y seguimos los cambios en su visibilidad local a lo largo de la "
         "campaña."),
    ],
    fit_h="Su campaña debe ajustarse a su mercado.",
    fit_p=[
        "Cada negocio local parte de una situación distinta. Algunos ya tienen un buen sitio web, pero necesitan más "
        "visibilidad local. Otros tienen carencias en su perfil de Google Business, su sitio web o su presencia local "
        "en general.",
        "Primero revisamos su situación actual y su competencia, y luego enfocamos la campaña en las áreas con mayor "
        "oportunidad de mejora.",
        "Los mercados más competitivos pueden requerir contenido adicional en el sitio web o una optimización más "
        "profunda. Le explicaremos el alcance recomendado antes de empezar.",
    ],
    fit_close="Usted paga por el trabajo que su negocio necesita, no por una lista genérica de tareas de SEO innecesarias.",
    how_eb="Cómo funciona",
    how_h="Un camino claro desde su visibilidad actual hasta una presencia local más fuerte.",
    how_steps=[
        ("Auditoría", "Revisamos su visibilidad local actual, su perfil de Google Business, su sitio web y su competencia "
                      "para entender dónde está."),
        ("Estrategia", "Identificamos las mayores oportunidades y definimos el trabajo que tiene más sentido para su "
                       "negocio y su mercado."),
        ("Mejora", "Reforzamos las áreas que afectan su visibilidad local: su perfil de Google Business, su sitio web, su "
                   "presencia local y el contenido cuando hace falta."),
        ("Seguimiento", "Monitoreamos sus posiciones locales y revisamos cómo cambia su visibilidad a lo largo de la "
                        "campaña."),
    ],
    how_cta="Solicitar auditoría de SEO local gratis",
    orl_h="SEO local pensado para negocios de Orlando.",
    orl_p=[
        "La búsqueda local depende de dónde está ubicado un negocio, desde dónde buscan sus clientes y qué tan "
        "competitivo es el mercado de alrededor.",
        "Por eso el SEO local es distinto de intentar posicionarse en todas partes a la vez. El objetivo es reforzar su "
        "visibilidad en la zona donde su negocio realmente puede atender clientes.",
        "Para los negocios de Orlando, analizamos su mercado local y su competencia para construir una campaña en torno "
        "a las búsquedas que importan en su zona de servicio.",
    ],
    orl_line="Rankelo trabaja con negocios locales en Orlando y sus alrededores.",
    pr_eb="Precio", pr_h="Campaña de SEO local",
    pr_p=[
        "El precio final depende de su sitio web actual, su competencia local, su zona de servicio y la cantidad de "
        "trabajo necesaria para reforzar su visibilidad.",
        "Primero revisamos su negocio y le damos un alcance y un presupuesto claros antes de empezar la campaña.",
    ],
    pr_cta="Solicitar auditoría de SEO local gratis",
    pr_small="Sin compromiso. Le mostraremos qué necesita atención antes de que decida si quiere avanzar.",
    after_h="No tiene que quedarse en un plan de SEO mensual.",
    after_p=[
        "La campaña inicial de SEO local tiene un alcance definido. Cuando ese trabajo termina, puede parar ahí o "
        "continuar con el mantenimiento SEO, que es opcional.",
        "El mantenimiento está pensado para negocios que quieren monitoreo continuo de posiciones, actualizaciones "
        "menores de SEO y atención constante a su presencia local después de la campaña inicial.",
    ],
    after_cta="Ver mantenimiento SEO", after_href=U["maint"],
    faq_h="Preguntas frecuentes",
    faq=[
        ("¿Qué incluye una campaña de SEO local?",
         "Una campaña puede incluir la optimización del perfil de Google Business, SEO para el sitio web y on-page, citas "
         "y presencia local, contenido local cuando hace falta, análisis de la competencia y seguimiento de posiciones "
         "locales. El alcance exacto depende de su negocio y su mercado."),
        ("¿Incluye la optimización del perfil de Google Business?",
         "Sí. Su perfil de Google Business es una parte importante de la visibilidad local, así que lo revisamos y lo "
         "mejoramos como parte de la campaña cuando hace falta."),
        ("¿Hacen cambios en mi sitio web?",
         "Sí, cuando las mejoras al sitio web forman parte del alcance recomendado. Podemos mejorar páginas existentes, "
         "la estructura y la relevancia local para ayudar a los buscadores a entender mejor su negocio."),
        ("¿Cuánto tarda el SEO local?",
         "El SEO local lleva tiempo, y los plazos dependen de su punto de partida y de su competencia. Primero "
         "establecemos una base y seguimos el avance durante toda la campaña, en lugar de prometer una fecha exacta."),
        ("¿Tengo que pagar todos los meses?",
         "No. La campaña inicial de SEO local es independiente del mantenimiento SEO continuo. El apoyo mensual es "
         "opcional después de la campaña."),
        ("¿Cuánto cuesta el SEO local?",
         "Nuestras campañas de SEO local empiezan desde $749. El precio final depende de su sitio web actual, su "
         "competencia, su zona de servicio y la cantidad de trabajo necesaria."),
        ("¿Solo trabajan con negocios de Orlando?",
         "Orlando es nuestro mercado local principal. Si su negocio atiende una zona cercana del centro de Florida, "
         "podemos revisar su ubicación y su zona de servicio para ver si el SEO local es una buena opción."),
        ("¿Pueden garantizar que voy a estar en el puesto #1?",
         "Ninguna agencia controla las posiciones de Google ni puede garantizar un puesto #1 permanente. Nos enfocamos en "
         "mejorar los factores en los que podemos influir, medir su visibilidad local y construir una base más sólida "
         "para competir en la búsqueda local."),
    ],
    final_h="Descubra qué está frenando a su negocio en la búsqueda local.",
    final_p=[
        "Solicite una auditoría de SEO local gratis y revisaremos su perfil de Google Business, su sitio web, su "
        "visibilidad local actual y su competencia.",
        "Tendrá una idea más clara de dónde están las mayores oportunidades y qué le recomendaríamos mejorar primero.",
    ],
    final_cta="Solicitar auditoría de SEO local gratis",
    final_small="Sin compromiso. Solo un punto de partida claro.",
)

# ------------------------------------------------------------------ GBP
GBP = dict(
    url=U["gbp"],
    title="Optimización del perfil de Google Business en Orlando | Rankelo",
    desc="Optimización del perfil de Google Business para negocios de Orlando. Mejore cómo aparece su negocio en Google "
         "Maps y en la búsqueda local con un perfil más claro y completo. Desde $299, pago único.",
    crumb="Optimización del perfil de Google Business",
    eyebrow="Optimización para Google Maps",
    h1="Optimización del perfil de Google Business en Orlando",
    sub="Haga que su negocio sea más fácil de entender y más fácil de elegir cuando los clientes locales lo encuentran "
        "en Google Maps y en la búsqueda local.",
    price_label="Desde", price="$299", price_unit="pago único",
    cta1="Solicitar auditoría del perfil gratis", cta2="Ver qué incluye",
    note="Revisaremos su perfil de Google Business actual y su competencia local antes de recomendarle qué necesita "
         "atención.",
    res_h="Cause una mejor primera impresión en Google.",
    res_lead=[
        "Su perfil de Google Business suele ser una de las primeras cosas que ve un cliente potencial cuando busca un "
        "negocio local.",
        "Un perfil más sólido y completo puede ayudar a Google a entender su negocio con más claridad y facilitar que los "
        "clientes vean qué ofrece, dónde está y cómo contactarlo.",
    ],
    res_items=[
        ("maps", "Más presencia en Google Maps",
         "Dele a su negocio una mejor base para competir cuando los clientes cercanos buscan en Google Maps."),
        ("pages", "Servicios e información más claros",
         "Ayude a Google y a los clientes potenciales a entender lo que su negocio realmente ofrece."),
        ("gbp", "Un perfil local más completo",
         "Reduzca la información faltante, poco clara o inconsistente que puede debilitar cómo aparece su negocio en "
         "internet."),
        ("phone", "Más oportunidades de que los clientes actúen",
         "Facilite que las personas llamen, visiten su sitio web, pidan indicaciones o den el siguiente paso después de "
         "encontrar su negocio."),
    ],
    prob_h="Un perfil incompleto puede hacer que su negocio pase desapercibido.",
    prob_p=[
        "Un perfil de Google Business puede existir sin estar bien configurado para la visibilidad local.",
        "Si Google no tiene una idea clara de su negocio, sus servicios y su ubicación, su perfil puede ser menos "
        "competitivo cuando los clientes cercanos buscan.",
        "Además, su competencia puede tener perfiles más completos que dan a los clientes más información antes de que "
        "lleguen a su sitio web.",
    ],
    prob_close="Su perfil debe dejar claro de inmediato qué hace su negocio y por qué un cliente local debería "
               "considerarlo.",
    inc_h="Dele a Google y a sus clientes una idea más clara de su negocio.",
    inc_lead="Revisamos las partes clave de su perfil de Google Business y reforzamos las áreas que pueden mejorar la "
             "claridad, lo completo que está y la relevancia local.",
    inc_items=[
        ("gbp", "Información del negocio",
         "Nos aseguramos de que el perfil represente claramente su negocio y de que la información importante sea "
         "exacta y consistente."),
        ("citations", "Categorías del negocio",
         "Revisamos cómo está categorizado su negocio para que Google entienda con más claridad qué tipo de negocio tiene."),
        ("pages", "Servicios",
         "Mejoramos cómo se presentan sus servicios para que su perfil dé a Google y a los clientes potenciales una idea "
         "más completa de lo que ofrece."),
        ("target", "Perfil completo",
         "Buscamos elementos del perfil que faltan o están poco desarrollados y que pueden limitar lo útil y competitivo "
         "que es su ficha."),
        ("maps", "Relevancia local",
         "Nos aseguramos de que el perfil respalde la ubicación y el mercado que su negocio realmente atiende."),
        ("reviews", "Reseñas y recomendaciones para el perfil",
         "Identificamos las áreas del perfil que conviene mantener con el tiempo y le damos recomendaciones prácticas "
         "para mantener su presencia activa y creíble."),
    ],
    fit_h="Su perfil debe reflejar lo que su negocio realmente hace.",
    fit_p=[
        "Optimizar el perfil de Google Business no consiste en llenar todos los campos posibles ni en agregar "
        "información que no corresponde.",
        "Revisamos su negocio, sus servicios, su perfil actual y su competencia local antes de decidir qué se debe mejorar.",
        "El objetivo es que su perfil sea más completo y relevante sin convertirlo en una ficha genérica o "
        "sobreoptimizada.",
    ],
    fit_close="Nos enfocamos en la información que ayuda a Google y a los clientes reales a entender mejor su negocio.",
    vs_h="¿Es suficiente optimizar el perfil de Google Business para su negocio?",
    vs_p=[
        "Para algunos negocios, el perfil de Google Business es la mayor oportunidad inmediata. Si el sitio web y la "
        "presencia local en general ya están en buen estado, un servicio enfocado en el perfil puede ser el mejor punto "
        "de partida.",
        "Para otros negocios, el perfil es solo una parte del problema.",
        "La visibilidad local también puede depender de su sitio web, el SEO on-page, las citas, el contenido local y la "
        "fuerza de la competencia en su mercado.",
    ],
    vs_a_h="Elija la optimización del perfil si:",
    vs_a=[
        "Lo que más quiere es que revisemos y mejoremos su perfil de Google Business actual.",
        "Su sitio web ya está en buen estado.",
        "Quiere un servicio único más pequeño antes de comprometerse con una campaña de SEO más amplia.",
        "Sus carencias más visibles están dentro de su perfil de Google Business.",
    ],
    vs_b_h="Considere una campaña de SEO local si:",
    vs_b=[
        "Su sitio web también necesita trabajo de SEO.",
        "Le cuesta aparecer tanto en Google Maps como en la búsqueda orgánica local.",
        "La información de su negocio no coincide en distintos sitios de internet.",
        "Su mercado es competitivo y requiere una estrategia de búsqueda local más amplia.",
    ],
    vs_cta="Ver SEO local", vs_href=U["local"],
    pr_eb="Precio", pr_h="Optimización del perfil de Google Business",
    pr_p=[
        "El precio final depende del estado actual de su perfil y de la cantidad de trabajo necesaria.",
        "Primero revisamos su perfil y confirmamos el alcance antes de empezar cualquier trabajo pagado.",
    ],
    pr_cta="Solicitar auditoría del perfil gratis",
    pr_small="El servicio de optimización es un pago único y no requiere ningún compromiso mensual.",
    faq_h="Preguntas frecuentes",
    faq=[
        ("¿Qué es la optimización del perfil de Google Business?",
         "Es el proceso de mejorar la información, la estructura, lo completo que está y la relevancia local de su perfil "
         "de Google Business para que Google y los clientes potenciales entiendan mejor su negocio."),
        ("¿Qué optimizan en mi perfil de Google Business?",
         "Revisamos las partes importantes de su perfil, como la información del negocio, las categorías, los servicios, "
         "lo completo que está y la relevancia local. El trabajo exacto depende del estado actual de su perfil."),
        ("¿Es lo mismo que el SEO local?",
         "No. La optimización del perfil de Google Business es una parte del SEO local. Una campaña completa de SEO local "
         "también puede incluir SEO para el sitio web, citas y presencia local, contenido local, análisis de la "
         "competencia y seguimiento de posiciones."),
        ("¿Necesito un sitio web para optimizar el perfil?",
         "No todas las mejoras del perfil de Google Business requieren un sitio web, pero un buen sitio web puede apoyar "
         "su visibilidad local en general. Si su sitio web también necesita trabajo, una campaña completa de SEO local "
         "puede ser una mejor opción."),
        ("¿Es un servicio de pago único?",
         "Sí. Nuestro servicio de optimización del perfil de Google Business empieza como un proyecto único. Si más "
         "adelante quiere apoyo continuo de SEO local, puede elegir por separado una campaña más amplia o el "
         "mantenimiento SEO."),
        ("¿Cuánto cuesta optimizar el perfil?",
         "La optimización del perfil de Google Business empieza desde $299, pago único. El precio final depende del "
         "estado actual del perfil y de la cantidad de trabajo necesaria."),
        ("¿Me garantiza estar en el puesto #1 de Google Maps?",
         "No. Las posiciones en Google Maps dependen de varios factores, y ninguna agencia controla las posiciones de "
         "Google. La optimización del perfil refuerza una parte importante de su presencia en la búsqueda local, pero "
         "algunos negocios necesitan un trabajo de SEO local más amplio para competir."),
        ("¿Solo trabajan con negocios de Orlando?",
         "Orlando es nuestro mercado local principal. Si su negocio está en una zona cercana del centro de Florida o la "
         "atiende, podemos revisar su perfil y su ubicación para ver si el servicio es una buena opción."),
    ],
    final_h="Descubra qué le puede faltar a su perfil de Google Business.",
    final_p=[
        "Solicite una auditoría gratis del perfil y revisaremos su perfil actual y su competencia local para identificar "
        "las áreas que pueden necesitar atención.",
        "Tendrá una idea más clara de qué se puede mejorar antes de decidir si quiere que nos encarguemos de la "
        "optimización.",
    ],
    final_cta="Solicitar auditoría del perfil gratis",
    final_small="Sin compromiso. Solo un punto de partida claro.",
)

# ------------------------------------------------------------------ WEBSITE + LOCAL SEO
WEB = dict(
    url=U["web"],
    title="Diseño web con SEO local en Orlando | Sitios web listos para SEO | Rankelo",
    desc="Diseño de sitios web listos para SEO para negocios de Orlando. Un sitio web profesional pensado en sus "
         "servicios, su ubicación, sus clientes y su visibilidad en la búsqueda local. Desde $1,999.",
    crumb="Sitio web + SEO local",
    eyebrow="Sitios web listos para SEO",
    h1="Diseño web con SEO local para negocios de Orlando",
    sub="Tenga un sitio web profesional pensado en sus servicios, su ubicación y la forma en que buscan los clientes "
        "locales, para que su sitio sea más fácil de entender, más fácil de navegar y esté mejor preparado para la "
        "visibilidad local.",
    price_label="Desde", price="$1,999",
    cta1="Solicitar consulta gratis sobre su sitio web", cta2="Ver qué incluye",
    note="Revisaremos su negocio, su sitio web actual si tiene uno, sus servicios principales y su mercado local antes "
         "de recomendarle la estructura adecuada.",
    res_h="Un sitio web hecho para que los clientes lo encuentren y lo elijan.",
    res_lead=[
        "Su sitio web debe hacer más que verse profesional.",
        "Debe explicar sus servicios con claridad, darles a los clientes locales un camino fácil para contactarlo y "
        "ayudar a los buscadores a entender qué hace su negocio y dónde trabaja.",
    ],
    res_items=[
        ("maps", "Pensado para la visibilidad local",
         "Cree una base más sólida para aparecer cuando los clientes cercanos buscan los servicios que ofrece su negocio."),
        ("pages", "Pensado en lo que usted vende",
         "Dele a cada servicio importante su propio espacio claro, en lugar de esconderlo todo en una sola página general."),
        ("chat", "Pensado para clientes reales",
         "Facilite que los visitantes entiendan su negocio, exploren sus servicios y den el siguiente paso."),
        ("track", "Pensado para crecer con su negocio",
         "Empiece con una estructura que pueda crecer a medida que agregue servicios, contenido o nuevas zonas de servicio."),
    ],
    prob_h="Un sitio web bonito no es suficiente.",
    prob_p=[
        "Un sitio web puede verse moderno y aun así hacer que a Google y a los clientes potenciales les cueste entender "
        "el negocio que hay detrás.",
        "Los servicios importantes pueden quedar escondidos en una sola página. La relevancia local puede no estar clara. "
        "Las páginas pueden no conectarse de forma lógica, y a los visitantes puede costarles encontrar la información "
        "que necesitan antes de contactarlo.",
        "Crear o rediseñar un sitio web sin tener en cuenta el SEO local puede dejar los mismos problemas de visibilidad.",
    ],
    prob_close="Su sitio web debe diseñarse según la forma en que su negocio realmente se encuentra, se entiende y se "
               "contacta.",
    ready_h="Pensado en sus servicios, su ubicación y sus clientes.",
    ready_lead="Estructuramos el sitio web para que las personas y los buscadores entiendan claramente qué ofrece su "
               "negocio y cómo se conectan las partes más importantes del sitio.",
    ready_items=[
        ("web", "Estructura clara del sitio",
         "Organizamos el sitio en torno a la información que los clientes realmente necesitan, con caminos claros entre "
         "sus páginas principales y sus servicios."),
        ("pages", "Páginas enfocadas en cada servicio",
         "Sus servicios más importantes pueden tener páginas propias para que los clientes y los buscadores entiendan "
         "mejor lo que ofrece."),
        ("maps", "Relevancia local",
         "Incorporamos el contexto de su ubicación en el sitio web para darle a su negocio una base más sólida en el "
         "mercado local que realmente atiende."),
        ("search", "Base de SEO on-page",
         "Las páginas principales se estructuran pensando en la visibilidad en buscadores desde el principio, no como algo "
         "secundario."),
        ("citations", "Conexión entre páginas",
         "Conectamos las páginas relacionadas de forma natural para que los visitantes se muevan fácilmente por el sitio "
         "y los buscadores entiendan mejor cómo encaja su contenido."),
        ("phone", "Páginas enfocadas en la conversión",
         "Cada página importante debe dejar claro cuál es el siguiente paso para un cliente potencial: llamar, pedir un "
         "presupuesto o contactar al negocio."),
    ],
    st_h="Dele a cada servicio importante espacio para competir.",
    st_p=[
        "El sitio web de un negocio local debe reflejar cómo funciona realmente el negocio.",
        "En lugar de meter todos los servicios en una sola página, creamos una estructura en torno a los servicios y la "
        "información que más importan a sus clientes.",
        "El número exacto de páginas y la estructura dependen del negocio, pero un sitio puede incluir:",
    ],
    st_list=["Página de inicio", "Páginas de servicios principales", "Páginas de servicios de apoyo cuando hace falta",
             "Página «Nosotros»", "Página de contacto", "Contenido sobre zonas de servicio cuando hace falta"],
    st_after=[
        "Algunos negocios solo necesitan un sitio web básico y enfocado. Otros necesitan más contenido de servicios o "
        "local para representar bien lo que ofrecen.",
        "Definimos la estructura según el negocio, en lugar de obligar a todos los clientes a usar la misma plantilla.",
    ],
    rel_h="Ayude a Google a entender qué hace y dónde lo hace.",
    rel_p=[
        "Un buen sitio web para un negocio local debe comunicar dos cosas con claridad: para qué es relevante el negocio "
        "y dónde ofrece esos servicios.",
        "El contenido sobre sus servicios ayuda a construir relevancia sobre lo que hace. El contenido local ayuda a "
        "establecer dónde trabaja el negocio.",
        "Cuando esas páginas están organizadas y conectadas de forma lógica, el sitio web es más fácil de navegar para "
        "los clientes y más fácil de entender para los buscadores.",
    ],
    rel_close="El objetivo es un sitio web que tenga sentido primero para las personas y que, al mismo tiempo, dé a los "
              "buscadores una idea clara del negocio que hay detrás.",
    vs_h="¿Necesita un sitio web nuevo o SEO para el que ya tiene?",
    vs_p=[
        "No necesita un sitio web nuevo solo porque quiere un mejor SEO local.",
        "Si su sitio web actual es sólido, puede tener más sentido mejorar el que ya tiene. Si el sitio está anticuado, "
        "mal estructurado, le faltan páginas de servicios importantes o ya no encaja con el negocio, rehacerlo pensando "
        "en el SEO local puede darle una base más sólida.",
    ],
    vs_a_h="Elija sitio web + SEO local si:",
    vs_a=["Necesita un sitio web nuevo para su negocio.", "Su sitio actual ya no representa bien sus servicios.",
          "Sus servicios importantes no tienen páginas claras.",
          "La estructura de su sitio web actual es difícil de ampliar.",
          "Quiere que el SEO local se tenga en cuenta desde el inicio del proyecto."],
    vs_b_h="Considere una campaña de SEO local si:",
    vs_b=["Su sitio web actual ya es funcional y profesional.",
          "El sitio necesita sobre todo mejoras de SEO, no rehacerse.",
          "También necesita un trabajo de SEO local más amplio, más allá del sitio web.",
          "Quiere mejorar su perfil de Google Business, sus citas, su presencia local y sus posiciones junto con el sitio "
          "web que ya tiene."],
    vs_cta="Ver SEO local", vs_href=U["local"],
    inc_h="¿Qué incluye sitio web + SEO local?",
    inc_lead="El alcance exacto depende del tamaño de su negocio y del sitio web que necesita, pero el servicio se basa "
             "desde el principio en una base sólida para la búsqueda local.",
    inc_items=[
        ("Estructura del sitio y páginas principales", "Una estructura clara basada en su negocio, sus servicios y el "
                                                      "recorrido de sus clientes."),
        ("Base de SEO local", "El sitio web se construye teniendo en cuenta desde el principio su ubicación y su "
                              "relevancia en la búsqueda local."),
        ("Optimización on-page", "Las páginas principales se organizan y optimizan para que los buscadores entiendan con "
                                 "más claridad su propósito."),
        ("Páginas de servicios", "Los servicios importantes reciben la estructura de páginas que necesitan, en lugar de "
                                 "quedar escondidos en textos genéricos."),
        ("Información del negocio local", "Los datos importantes de su negocio se presentan de forma clara y consistente "
                                          "en el sitio donde corresponde."),
        ("Enlaces internos", "Las páginas relacionadas se conectan de forma natural para que la navegación sea más clara "
                             "para los clientes y los buscadores."),
        ("Configuración básica para buscadores", "Preparamos el sitio web con los elementos esenciales para buscadores "
                                                 "que se necesitan para un buen lanzamiento y para el trabajo de SEO futuro."),
    ],
    pr_eb="Precio", pr_h="Sitio web + SEO local",
    pr_p=[
        "El precio final depende del número de páginas, la cantidad de contenido necesario, la complejidad del sitio web "
        "y la estructura de SEO local que necesita su negocio.",
        "Primero revisamos el proyecto y le damos un alcance y un presupuesto claros antes de empezar a construirlo.",
    ],
    pr_cta="Solicitar consulta gratis sobre su sitio web",
    pr_small="El precio inicial corresponde a sitios web más pequeños para negocios locales. Los sitios más grandes o "
             "complejos se cotizan según el alcance.",
    faq_h="Preguntas frecuentes",
    faq=[
        ("¿Qué es un sitio web listo para SEO?",
         "Un sitio web listo para SEO está estructurado para que los buscadores entiendan con claridad el negocio, sus "
         "servicios y su relevancia local. También ofrece a los visitantes una forma clara de navegar por el sitio y de "
         "dar el siguiente paso."),
        ("¿El sitio web incluye SEO local?",
         "El sitio web incluye una base de SEO local: relevancia local, estructura on-page, páginas de servicios y enlaces "
         "internos. El trabajo de SEO local más amplio, como la optimización del perfil de Google Business, las citas, el "
         "seguimiento continuo de posiciones o el crecimiento a largo plazo, puede requerir una campaña de SEO local "
         "aparte."),
        ("¿Necesito una página para cada servicio?",
         "No necesariamente. La estructura adecuada depende de su negocio y de la importancia de cada servicio. "
         "Recomendamos páginas propias cuando ayudan a los clientes a entender su oferta y refuerzan la relevancia del "
         "sitio en los buscadores."),
        ("¿Pueden rehacer mi sitio web actual?",
         "Sí. Si su sitio web actual ya no encaja con su negocio o tiene problemas de estructura que dificultan el SEO y "
         "el crecimiento futuro, podemos recomendarle rehacerlo en lugar de seguir parchando el sitio existente."),
        ("¿Y si mi sitio web actual ya es bueno?",
         "Entonces puede que no necesite uno nuevo. Una campaña de SEO local puede ser mejor opción si el sitio actual se "
         "puede mejorar sin rehacerlo."),
        ("¿Cuánto cuesta sitio web + SEO local?",
         "Sitio web + SEO local empieza desde $1,999. El precio final depende del número de páginas, el contenido "
         "necesario, la complejidad del sitio y la estructura de SEO que requiere su negocio."),
        ("¿El sitio web estará en el puesto #1 en cuanto se publique?",
         "No. Un buen sitio web le da a su negocio una mejor base de SEO, pero las posiciones dependen de muchos factores "
         "además del propio sitio. Algunos negocios también necesitan optimizar su perfil de Google Business, citas, "
         "trabajo continuo de SEO local y tiempo para competir."),
        ("¿Solo crean sitios web para negocios de Orlando?",
         "Orlando es nuestro mercado local principal. Si su negocio está en una zona cercana del centro de Florida o la "
         "atiende, podemos revisar el proyecto y ver si el servicio es una buena opción."),
    ],
    final_h="Construya su sitio web pensando en los clientes que quiere atraer.",
    final_p=[
        "Cuéntenos sobre su negocio, sus servicios y su sitio web actual.",
        "Revisaremos lo que necesita y le recomendaremos una estructura que apoye tanto a sus clientes como a su "
        "presencia en la búsqueda local.",
    ],
    final_cta="Solicitar consulta gratis sobre su sitio web",
    final_small="Sin compromiso. Solo un punto de partida claro para su proyecto web.",
)

# ------------------------------------------------------------------ SEO MAINTENANCE
MAINT = dict(
    url=U["maint"],
    title="Mantenimiento SEO local en Orlando | Monitoreo y actualizaciones SEO | Rankelo",
    desc="Mantenimiento continuo de SEO local para negocios de Orlando. Monitoreo de posiciones, actualizaciones menores "
         "de SEO, mantenimiento de su presencia local y vigilancia de la competencia. Desde $399/mes.",
    crumb="Mantenimiento SEO",
    eyebrow="Apoyo continuo de SEO local",
    h1="Mantenimiento SEO para negocios de Orlando",
    sub="Mantenga su visibilidad local monitoreada, cuidada y con apoyo después de terminar el trabajo principal de SEO.",
    price_label="Desde", price="$399", price_unit="/mes",
    cta1="Hablar con Rankelo sobre mantenimiento SEO", cta2="Ver qué incluye",
    note="El mantenimiento SEO está pensado para negocios que ya tienen una base sólida de SEO y quieren atención "
         "continua a sus posiciones, actualizaciones menores y su presencia en la búsqueda local.",
    why_h="Un buen SEO sigue necesitando atención con el tiempo.",
    why_p=[
        "Terminar el trabajo inicial de SEO le da a su negocio una base más sólida, pero la búsqueda local no se queda "
        "completamente quieta.",
        "La competencia actualiza sus sitios web y sus perfiles de Google. Las posiciones pueden moverse. La información "
        "del negocio cambia. Con el tiempo pueden aparecer nuevas oportunidades y pequeños problemas.",
        "El mantenimiento SEO le da a su negocio apoyo continuo sin empezar otra campaña completa cada mes.",
    ],
    why_items=[
        ("search", "Vigile su visibilidad",
         "Monitoree cómo le va a su negocio en la búsqueda local e identifique los cambios importantes antes de que pasen "
         "meses sin atenderse."),
        ("key", "Mantenga la base que ya construyó",
         "Mantenga exactos y bien cuidados los elementos importantes de la búsqueda local a medida que su negocio cambia."),
        ("track", "Siga haciendo mejoras menores",
         "Aproveche las oportunidades de SEO y haga actualizaciones menores sin convertir cada cambio en un proyecto nuevo."),
    ],
    inc_h="Atención continua donde importa.",
    inc_p=["El trabajo exacto depende de su negocio y de lo que se hizo durante la campaña inicial.",
           "El mantenimiento SEO puede incluir atención continua en las siguientes áreas."],
    inc_items=[
        ("reports", "Monitoreo de posiciones locales",
         "Seguimos su visibilidad en la búsqueda local y estamos atentos a los cambios importantes en sus resultados."),
        ("web", "Actualizaciones menores de SEO en el sitio web",
         "Nos encargamos de mejoras menores on-page o de contenido cuando las páginas existentes necesitan atención."),
        ("gbp", "Atención al perfil de Google Business",
         "Cuando hace falta, revisamos y mantenemos las partes importantes de su perfil de Google Business para que la "
         "información siga reflejando su negocio con exactitud."),
        ("citations", "Revisión de la presencia local",
         "Vigilamos la información importante de su negocio local y corregimos los problemas de consistencia relevantes "
         "cuando aparecen."),
        ("target", "Monitoreo de la competencia y de oportunidades",
         "Observamos el entorno de la búsqueda local para detectar cambios que puedan crear nuevos riesgos u oportunidades "
         "para su negocio."),
    ],
    who_h="Ideal para negocios que ya tienen una base sólida de SEO.",
    who_p="El mantenimiento SEO tiene más sentido cuando el trabajo principal de optimización ya está terminado.",
    who_lead="Puede ser una buena opción si:",
    who_list=[
        "Ya completó una campaña de SEO local.",
        "Su perfil de Google Business y su sitio web ya están optimizados.",
        "Su negocio ya tiene una visibilidad local establecida que quiere monitorear.",
        "Quiere mejoras menores y continuas de SEO sin empezar otra campaña completa.",
        "Prefiere que alguien siga vigilando su presencia en la búsqueda local.",
    ],
    who_close="Si su negocio todavía tiene problemas importantes de SEO, una campaña de SEO local puede ser un mejor punto "
              "de partida.",
    vs_h="El mantenimiento cuida la base. Una campaña la construye o la repara.",
    vs_p="Estos servicios están pensados para etapas distintas.",
    vs_a_h="Campaña de SEO local",
    vs_a="Ideal cuando su negocio necesita mejoras más amplias en el perfil de Google Business, el SEO del sitio web, la "
         "presencia local, el contenido y las posiciones.",
    vs_a_cta="Ver SEO local", vs_a_href=U["local"],
    vs_b_h="Mantenimiento SEO",
    vs_b="Ideal cuando el trabajo principal ya está hecho y quiere monitoreo continuo, actualizaciones menores y atención "
         "constante a su visibilidad local.",
    vs_b_note="No tiene que contratar el mantenimiento SEO después de una campaña de SEO local. Es opcional.",
    pr_eb="Precio", pr_h="Mantenimiento SEO",
    pr_p=["El alcance mensual exacto depende del tamaño de su presencia local y de la atención continua que necesita su "
          "negocio.",
          "El mantenimiento SEO está pensado para mejoras menores continuas, monitoreo y cuidado, no para repetir la "
          "campaña inicial completa cada mes."],
    pr_cta="Hablar con Rankelo sobre mantenimiento SEO",
    pr_small="Revisaremos el trabajo ya realizado y confirmaremos si el mantenimiento continuo tiene sentido para su "
             "negocio.",
    faq_h="Preguntas frecuentes",
    faq=[
        ("¿Qué es el mantenimiento SEO?",
         "El mantenimiento SEO es el apoyo continuo después de terminar el trabajo principal de SEO. Se enfoca en "
         "monitorear la visibilidad local, mantener los elementos importantes de SEO, hacer actualizaciones menores e "
         "identificar problemas u oportunidades con el tiempo."),
        ("¿Necesito mantenimiento SEO después de una campaña de SEO local?",
         "No. El mantenimiento SEO es opcional. Puede terminar la campaña inicial y parar ahí, o continuar con apoyo "
         "mensual si quiere monitoreo continuo y mejoras menores."),
        ("¿El mantenimiento SEO es lo mismo que una campaña de SEO local?",
         "No. Una campaña de SEO local está pensada para resolver problemas y oportunidades de SEO más grandes. El "
         "mantenimiento SEO está pensado para cuidar una base que ya existe después de terminar el trabajo principal."),
        ("¿Qué incluye cada mes?",
         "El trabajo exacto depende de su negocio y de su presencia local actual. El mantenimiento puede incluir monitoreo "
         "de posiciones locales, actualizaciones menores de SEO en el sitio web, atención al perfil de Google Business, "
         "revisión de la presencia local y monitoreo de la competencia."),
        ("¿Puedo empezar con mantenimiento SEO si nunca he hecho SEO local?",
         "Por lo general, no. Si su negocio todavía tiene carencias importantes de SEO local, normalmente tiene más sentido "
         "resolverlas primero con una campaña de SEO local y considerar el mantenimiento después."),
        ("¿Cuánto cuesta el mantenimiento SEO?",
         "El mantenimiento SEO empieza desde $399 al mes. El precio final depende del tamaño de su presencia local y de la "
         "cantidad de trabajo continuo necesaria."),
        ("¿El mantenimiento SEO garantiza que mis posiciones nunca van a bajar?",
         "No. Las posiciones en Google pueden cambiar por muchas razones, y ninguna agencia las controla. El mantenimiento "
         "nos ayuda a monitorear su visibilidad, responder a los cambios relevantes y seguir cuidando la base de SEO que "
         "ya tiene."),
    ],
    final_h="Que su presencia en la búsqueda local no quede en segundo plano.",
    final_p=["Si el trabajo principal de SEO ya está hecho, el mantenimiento continuo puede ayudar a mantener su "
             "visibilidad local monitoreada y su base actual bien cuidada.",
             "Cuéntenos qué se ha hecho hasta ahora y le diremos si el mantenimiento SEO tiene sentido para su negocio."],
    final_cta="Hablar con Rankelo sobre mantenimiento SEO",
    final_small="Desde $399/mes.",
)

# ------------------------------------------------------------------ SERVICES HUB
HUB = dict(
    url=U["services"],
    title="Servicios de SEO local en Orlando | Perfil de Google, SEO web y mantenimiento | Rankelo",
    desc="Conozca los servicios de SEO local de Rankelo para negocios de Orlando: campañas de SEO local, optimización del "
         "perfil de Google Business, sitios web listos para SEO y mantenimiento SEO continuo.",
    home_href=U["home"], crumb_home="Inicio", crumb="Servicios", idx_aria="Servicios en esta página",
    eyebrow="Servicios de Rankelo",
    h1="Servicios de SEO local en Orlando",
    sub="Ya sea que necesite más visibilidad local, un mejor perfil de Google Business, un sitio web nuevo listo para SEO "
        "o apoyo continuo, Rankelo ofrece servicios enfocados según el punto en el que está su negocio hoy.",
    cta="Solicitar auditoría de SEO local gratis",
    note="¿No sabe qué servicio necesita? Revisaremos su negocio y le mostraremos dónde está la mayor oportunidad.",
    need_h="Empiece por lo que su negocio más necesita.",
    need_p=["No necesita diagnosticar su propio problema de SEO antes de contactarnos.",
            "Use estas opciones como un punto de partida sencillo."],
    rec="Servicio recomendado",
    needs=[
        ("Ya tiene un sitio web, pero a los clientes les cuesta encontrarlo en Google.", "Campaña de SEO local",
         "Mejore su visibilidad en Google Maps y en la búsqueda local sin rehacer un sitio web que ya funciona para su "
         "negocio.", "Ver SEO local", U["local"]),
        ("Lo que más le preocupa es su perfil de Google Business.", "Optimización del perfil de Google Business",
         "Mejore el perfil que ven los clientes cuando encuentran su negocio en Google Maps y en la búsqueda local.",
         "Ver optimización del perfil", U["gbp"]),
        ("Necesita un sitio web nuevo o el actual ya no encaja con su negocio.", "Sitio web + SEO local",
         "Construya un sitio web profesional pensado desde el principio en sus servicios, su ubicación, sus clientes y su "
         "visibilidad en la búsqueda local.", "Ver sitio web + SEO local", U["web"]),
        ("Ya terminó el trabajo principal de SEO y quiere apoyo continuo.", "Mantenimiento SEO",
         "Mantenga su presencia local monitoreada y cuidada después de la campaña inicial.", "Ver mantenimiento SEO",
         U["maint"]),
    ],
    svc_h="Conozca los servicios de Rankelo",
    svc_p="Cada servicio resuelve un problema distinto. Elija la opción que mejor se ajusta al punto en el que está su "
          "negocio, o empiece con una auditoría de SEO local gratis si no está seguro.",
    best="Ideal para:", starting="Desde",
    services=[
        dict(id="local-seo", n="01", t="Campaña de SEO local", out="Haga que más clientes de su zona lo encuentren.",
             p=["Una campaña de SEO local más amplia para negocios que quieren más visibilidad en Google Maps y en la "
                "búsqueda local.",
                "La campaña puede abarcar su perfil de Google Business, el SEO de su sitio web, su presencia local, el "
                "contenido y las posiciones, según lo que su negocio realmente necesita."],
             best="Negocios que ya tienen un sitio web pero necesitan más visibilidad en la búsqueda local.",
             price="$749", unit="", cta="Ver SEO local", href=U["local"], icon="maps"),
        dict(id="gbp", n="02", t="Optimización del perfil de Google Business",
             out="Refuerce el perfil que ven los clientes en Google Maps.",
             p=["Un servicio único y enfocado para negocios que quieren que revisemos y mejoremos su perfil de Google "
                "Business.",
                "Reforzamos la información, los servicios, lo completo que está y la relevancia local del perfil para que "
                "Google y los clientes potenciales tengan una idea más clara del negocio."],
             best="Negocios cuya mayor oportunidad inmediata está dentro de su perfil de Google Business.",
             price="$299", unit="pago único", cta="Ver optimización del perfil", href=U["gbp"], icon="gbp"),
        dict(id="website", n="03", t="Sitio web + SEO local",
             out="Construya su sitio web pensando en los clientes que quiere atraer.",
             p=["Un sitio web profesional para negocios locales, estructurado en torno a sus servicios, su ubicación, el "
                "recorrido de sus clientes y su visibilidad en la búsqueda local.",
                "En lugar de dejar el SEO para después, el sitio web se construye desde el principio con una base sólida "
                "para la búsqueda local."],
             best="Negocios que necesitan un sitio web nuevo, rehacer el actual o una base más sólida para el SEO local "
                  "futuro.",
             price="$1,999", unit="", cta="Ver sitio web + SEO local", href=U["web"], icon="web"),
        dict(id="maintenance", n="04", t="Mantenimiento SEO", out="Mantenga su presencia local monitoreada y cuidada.",
             p=["Apoyo continuo y opcional después de terminar el trabajo principal de SEO.",
                "El mantenimiento SEO está pensado para monitorear posiciones, hacer actualizaciones menores de SEO, "
                "vigilar su presencia local e identificar problemas que puedan necesitar atención con el tiempo."],
             best="Negocios que ya completaron su trabajo inicial de SEO y quieren apoyo continuo.",
             price="$399", unit="/mes", cta="Ver mantenimiento SEO", href=U["maint"], icon="track"),
    ],
    cmp_h="Compare los servicios de Rankelo",
    cmp_p="Esta es la forma más sencilla de ver en qué se diferencian los cuatro servicios.",
    cmp_cols=["Campaña de SEO local", "Optimización del perfil", "Sitio web + SEO local", "Mantenimiento SEO"],
    cmp_rows=[
        ("Objetivo principal", ["Mejorar la visibilidad local en general", "Mejorar el perfil de Google Business",
                                "Crear un sitio web nuevo listo para SEO", "Mantener y monitorear el SEO existente"]),
        ("Trabajo en el perfil de Google Business", ["Incluido cuando hace falta", "Enfoque principal",
                                                     "No es el enfoque principal", "Atención continua cuando hace falta"]),
        ("SEO del sitio web", ["Incluido cuando hace falta", "No", "Incluido en el sitio web",
                               "Actualizaciones menores continuas"]),
        ("Sitio web nuevo", ["No", "No", "Sí", "No"]),
        ("Citas locales / presencia local más amplia", ["Incluido cuando hace falta", "No", "No es el enfoque principal",
                                                        "Mantenimiento cuando corresponde"]),
        ("Servicio mensual continuo", ["No es obligatorio", "No", "No", "Sí"]),
        ("Precio inicial", ["$749", "$299 pago único", "$1,999", "$399/mes"]),
    ],
    cmp_note="El alcance final depende del estado actual de su negocio, su sitio web, su perfil de Google Business, su "
             "competencia y su mercado local.",
    ns_h="¿No sabe qué servicio es el adecuado para su negocio?",
    ns_p=["No necesita elegir un servicio antes de hablar con nosotros.",
          "Podemos revisar su perfil de Google Business, su sitio web, su visibilidad local actual y su competencia para "
          "identificar dónde está la mayor oportunidad.",
          "Si su negocio solo necesita mejorar el perfil, se lo diremos.",
          "Si el problema es más amplio y requiere SEO local o un sitio web nuevo, le explicaremos por qué."],
    ns_cta="Solicitar auditoría de SEO local gratis",
    ns_small="Sin compromiso. Solo una idea más clara de lo que su negocio realmente necesita.",
    faq_h="Preguntas frecuentes",
    faq=[
        ("¿Qué servicio de Rankelo es el adecuado para mi negocio?",
         "Depende de dónde está el problema principal. Si su sitio web actual es sólido pero su visibilidad local en "
         "general es baja, una campaña de SEO local puede ser la mejor opción. Si el problema principal es su perfil de "
         "Google Business, el servicio enfocado de optimización del perfil puede ser suficiente. Si necesita un sitio web "
         "nuevo, sitio web + SEO local es el mejor punto de partida."),
        ("¿Cuál es la diferencia entre optimizar el perfil y el SEO local?",
         "La optimización del perfil de Google Business se enfoca solo en mejorar su perfil de Google Business. Una "
         "campaña de SEO local es más amplia y también puede incluir SEO para el sitio web, citas y presencia local, "
         "contenido local, análisis de la competencia y seguimiento de posiciones."),
        ("¿Necesito un sitio web nuevo para hacer SEO local?",
         "No. Si su sitio web actual funciona y se puede mejorar, podemos trabajar con el sitio que ya tiene. Sitio web + "
         "SEO local está pensado para negocios que realmente necesitan un sitio nuevo o rehacer el actual."),
        ("¿Puedo empezar optimizando el perfil y pasar al SEO local después?",
         "Sí. Optimizar el perfil puede ser un primer paso más pequeño. Si más adelante su negocio necesita un trabajo más "
         "amplio en el sitio web y en la búsqueda local, puede pasar a una campaña de SEO local."),
        ("¿El mantenimiento SEO es obligatorio después de una campaña de SEO local?",
         "No. El mantenimiento SEO es opcional. La campaña inicial de SEO local tiene su propio alcance, y después usted "
         "decide si quiere monitoreo y apoyo continuos."),
        ("¿Hacen presupuestos a medida?",
         "Sí. Los precios que aparecen en el sitio web son precios iniciales. El precio final depende del estado actual de "
         "su presencia en línea, su competencia, su zona de servicio, el tamaño del sitio web y la cantidad de trabajo "
         "necesaria."),
    ],
    final_h="Empiece con el servicio que su negocio realmente necesita.",
    final_p=["Cuéntenos sobre su negocio y qué quiere mejorar.",
             "Revisaremos su presencia local actual y le ayudaremos a definir el siguiente paso más útil."],
    final_cta="Solicitar auditoría de SEO local gratis",
    final_small="Sin compromiso. Solo un punto de partida claro.",
)

# ------------------------------------------------------------------ ABOUT
ABOUT = dict(
    url=U["about"],
    title="Sobre Rankelo | Empresa de SEO local en Orlando, FL",
    desc="Conozca Rankelo, un estudio de SEO local en Orlando que ayuda a pequeños negocios a mejorar su visibilidad en "
         "Google Maps, en la búsqueda local y en internet.",
    home_href=U["home"], crumb_home="Inicio", crumb="Nosotros", all_href=U["services"],
    eyebrow="Sobre Rankelo",
    h1="Un estudio de SEO local creado para pequeños negocios",
    sub="Rankelo ayuda a los negocios de Orlando a mejorar cómo aparecen en Google Maps, en la búsqueda local y en internet.",
    support="Nos enfocamos en un trabajo práctico de SEO local, pensado según lo que cada negocio realmente necesita.",
    cta="Solicitar auditoría de SEO local gratis",
    why_h="Los buenos negocios locales no deberían ser invisibles en Google.",
    why_p=["La mayoría de los dueños de negocios no empezaron su empresa para convertirse en expertos en SEO. La empezaron "
           "porque son buenos en lo que hacen.",
           "Pero hoy, los clientes suelen buscar en Google antes de decidir a quién llamar, visitar, reservar o contratar.",
           "Rankelo nació para ayudar a los pequeños negocios a reforzar su visibilidad local sin que el SEO se convierta "
           "en otro trabajo de tiempo completo para el dueño."],
    bel_h="Así entendemos el SEO local.",
    beliefs=[
        ("Comunicación directa", "Usted se comunica directamente con las personas que hacen el trabajo, así que las "
                                 "preguntas y las decisiones son sencillas."),
        ("Alcance claro", "Usted debe saber en qué estamos trabajando, por qué importa y qué está pagando."),
        ("Estrategia centrada en el negocio", "Revisamos su visibilidad actual, su sitio web, su competencia y su mercado "
                                              "local antes de recomendar lo que realmente necesita atención."),
        ("SEO responsable", "Nos enfocamos en un trabajo de SEO local legítimo, no en atajos arriesgados que puedan poner "
                            "en peligro su presencia en Google."),
    ],
    help_h="En qué ayuda Rankelo",
    help_p="Nuestros servicios están pensados para los problemas de visibilidad local más comunes de los pequeños negocios.",
    services=[
        ("Campaña de SEO local", "Un trabajo de SEO local más amplio para negocios que necesitan más visibilidad en Google "
                                 "Maps y en la búsqueda local.", "Ver SEO local", U["local"]),
        ("Optimización del perfil de Google Business", "Mejoras enfocadas en el perfil que ven los clientes cuando "
                                                      "encuentran su negocio en Google.",
         "Ver optimización del perfil", U["gbp"]),
        ("Sitio web + SEO local", "Sitios web profesionales para negocios locales, pensados desde el principio en sus "
                                  "servicios, sus clientes y su visibilidad en la búsqueda local.",
         "Ver sitio web + SEO local", U["web"]),
        ("Mantenimiento SEO", "Apoyo continuo y opcional después de terminar el trabajo inicial de SEO.",
         "Ver mantenimiento SEO", U["maint"]),
    ],
    all_cta="Ver todos los servicios",
    local_h="Pensado para negocios que dependen de clientes locales.",
    local_p=["Rankelo se enfoca en pequeños negocios cuyos clientes buscan localmente antes de decidir a quién llamar, "
             "visitar o contratar.",
             "Eso puede incluir negocios de servicios para el hogar, consultorios profesionales, restaurantes, tiendas "
             "locales y otros negocios que atienden clientes en Orlando y sus alrededores."],
    local_goal="Nuestro objetivo es sencillo: ayudar a que más clientes locales adecuados encuentren el negocio cuando ya "
               "están buscando lo que ofrece.",
    final_h="Vea en qué posición está su negocio en Google.",
    final_p=["Solicite una auditoría de SEO local gratis y revisaremos su visibilidad local actual, su sitio web, su perfil "
             "de Google Business y su competencia.",
             "Le mostraremos dónde vemos las mayores oportunidades y qué le recomendaríamos mejorar primero."],
    final_cta="Solicitar auditoría de SEO local gratis",
    final_small="Sin compromiso. Solo un punto de partida claro.",
)

# ------------------------------------------------------------------ FREE AUDIT
FREE_AUDIT = dict(
    title="Auditoría de SEO local gratis | Contacte a Rankelo en Orlando",
    desc="Solicite una auditoría de SEO local gratis o háganos una pregunta. Escriba a contact@rankelo.org o llame al "
         "+1 (321) 616-0799. Revisamos su perfil de Google Business, su sitio web y su competencia y respondemos en "
         "24 horas.",
    crumb_home="Inicio", crumb="Auditoría gratis",
    eyebrow="Auditoría de SEO local gratis",
    h1="Solicite su auditoría local gratis o háganos una pregunta",
    lead="Cuéntenos sobre su negocio. Revisaremos su perfil de Google, su sitio web y su competencia, y le responderemos "
         "en 24 horas.",
    email_l="Escríbanos", email_cta="Enviar un correo →", mail_subject="Pregunta para Rankelo",
    phone_l="Llámenos", phone_cta="Toque para llamar →", hours_l="Horario",
    form_h="Cuéntenos sobre su negocio",
    steps_h="Qué pasa después",
    steps=["Revisamos su perfil de Google Business, su sitio web y su competencia principal",
           "Le respondemos en 24 horas con lo que encontramos",
           "Si encajamos, confirmamos el alcance y un presupuesto claro antes de empezar cualquier trabajo"],
    submit="Enviar mi solicitud",
)
