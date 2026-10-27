"""Industry landing pages, English + Spanish. Each niche has a stable key; slugs per language."""

SITE_Q_EN = (
    "Do I need a website to rank on Google Maps?",
    "You can show up on Maps with only a Google Business Profile, but a website with a page for each service "
    "helps Google understand what you do and where you work. If you don't have one, we build it as part of the "
    "Website + Local SEO package.",
)
SITE_Q_ES = (
    "¿Necesito un sitio web para aparecer en Google Maps?",
    "Puede aparecer en Maps solo con un perfil de Google Business, pero un sitio web con una página para cada "
    "servicio ayuda a Google a entender qué hace y dónde trabaja. Si no tiene uno, lo creamos como parte del "
    "paquete Sitio web + SEO local.",
)

NICHES = [
    # ------------------------------------------------------------------ restaurants
    dict(
        key="restaurants",
        slug=dict(en="local-seo-for-restaurants/", es="es/seo-local-para-restaurantes/"),
        en=dict(
            name="Restaurants", one="restaurant", you="Your restaurant",
            title="Local SEO for Restaurants | Get Found on Google Maps | Rankelo",
            desc="Local SEO for restaurants: show up in Google Maps for \"restaurants near me\", your cuisine and your "
                 "neighborhood, with your menu, photos and reviews set up right. Free audit.",
            h1=("Local SEO for", "restaurants"),
            lead="Hungry people don't browse for long. They open Google Maps, look at photos, ratings and hours, "
                 "and pick one of the first places they see. We make sure that's you.",
            query="restaurants near me",
            rivals=[("Harbor Grill", "4.2", "1.1 mi"), ("Casa Verde Kitchen", "4.4", "0.8 mi")],
            why="Why restaurants lose guests to the place next door",
            problems=[
                ("Decisions happen in seconds",
                 "People choose from the top results on Maps, often while standing on the street or sitting in the car."),
                ("Photos and menu sell the meal",
                 "A profile with old photos, no menu or wrong hours loses to the place next door with a full, fresh profile."),
                ("Reviews live on many sites",
                 "Google, Yelp and TripAdvisor all shape your reputation, and unanswered reviews look like nobody is listening."),
            ],
            work=[
                ("Google Business Profile", "\"Restaurant\" plus your cuisine as categories, accurate hours including "
                 "holidays, and attributes like outdoor seating, delivery and takeout."),
                ("Menu & photos", "Your menu on Google and fresh photos of dishes, interior and team, updated regularly."),
                ("Reservations & ordering", "Reserve and order buttons on your profile, so guests can act right from Maps."),
                ("Reviews", "A simple way to ask happy guests for reviews, plus a thoughtful reply to every review."),
                ("Listings", "Consistent details on Yelp, TripAdvisor, Apple Maps, Bing and delivery apps."),
                ("Posts & events", "Specials, events and seasonal menus posted on your profile to keep it active."),
            ],
            keywords=["restaurants near me", "best [cuisine] near me", "[cuisine] restaurant [city]",
                      "brunch near me", "dinner near me open now", "takeout near me"],
            faq=[
                ("Does a restaurant really need local SEO?",
                 "Most guests find new places on Google Maps. A complete, active profile with good photos and reviews "
                 "is often the difference between a full room and a half-empty one."),
                SITE_Q_EN,
                ("Can you help with Yelp and TripAdvisor too?",
                 "Yes. We make sure your listings there are accurate and set up a simple routine for replying to "
                 "reviews. We never post fake reviews or pay for them."),
            ],
        ),
        es=dict(
            name="Restaurantes", one="restaurante", you="Su restaurante",
            title="SEO local para restaurantes | Aparezca en Google Maps | Rankelo",
            desc="SEO local para restaurantes: aparezca en Google Maps para \"restaurantes cerca de mí\", su tipo de "
                 "cocina y su zona, con menú, fotos y reseñas bien configurados. Auditoría gratis.",
            h1=("SEO local para", "restaurantes"),
            lead="Quien tiene hambre no busca por mucho tiempo. Abre Google Maps, mira fotos, calificaciones y horario, "
                 "y elige uno de los primeros lugares que ve. Nos aseguramos de que sea el suyo.",
            query="restaurantes cerca de mí",
            rivals=[("Harbor Grill", "4.2", "1.1 mi"), ("Casa Verde Kitchen", "4.4", "0.8 mi")],
            why="Por qué los restaurantes pierden clientes frente al local de al lado",
            problems=[
                ("Se decide en segundos",
                 "La gente elige entre los primeros resultados de Maps, muchas veces desde la calle o el auto."),
                ("Las fotos y el menú venden",
                 "Un perfil con fotos viejas, sin menú o con horario incorrecto pierde frente al vecino con un perfil completo."),
                ("Las reseñas están en muchos sitios",
                 "Google, Yelp y TripAdvisor forman su reputación, y las reseñas sin respuesta parecen descuido."),
            ],
            work=[
                ("Perfil de Google Business", "\"Restaurante\" y su tipo de cocina como categorías, horario correcto "
                 "(también festivos) y atributos como terraza, entrega a domicilio y para llevar."),
                ("Menú y fotos", "Su menú en Google y fotos recientes de platos, local y equipo, actualizadas con regularidad."),
                ("Reservas y pedidos", "Botones de reservar y pedir en su perfil, para que el cliente actúe desde Maps."),
                ("Reseñas", "Una forma sencilla de pedir reseñas a clientes satisfechos y una respuesta cuidada a cada una."),
                ("Directorios", "Datos coherentes en Yelp, TripAdvisor, Apple Maps, Bing y apps de entrega."),
                ("Publicaciones y eventos", "Ofertas, eventos y menús de temporada publicados para mantener el perfil activo."),
            ],
            keywords=["restaurantes cerca de mí", "mejor [cocina] cerca de mí", "restaurante [cocina] [ciudad]",
                      "brunch cerca de mí", "cena cerca de mí abierto ahora", "comida para llevar cerca de mí"],
            faq=[
                ("¿Un restaurante realmente necesita SEO local?",
                 "La mayoría de los clientes descubre lugares nuevos en Google Maps. Un perfil completo y activo, con "
                 "buenas fotos y reseñas, suele marcar la diferencia entre un salón lleno y uno medio vacío."),
                SITE_Q_ES,
                ("¿Pueden ayudar también con Yelp y TripAdvisor?",
                 "Sí. Revisamos que sus datos allí sean correctos y creamos una rutina sencilla para responder reseñas. "
                 "Nunca publicamos reseñas falsas ni pagamos por ellas."),
            ],
        ),
    ),
    # ------------------------------------------------------------------ roofers
    dict(
        key="roofers",
        slug=dict(en="local-seo-for-roofers/", es="es/seo-local-para-techadores/"),
        en=dict(
            name="Roofers", one="roofing company", you="Your roofing company",
            title="Local SEO for Roofers | Win More Roofing Jobs on Google | Rankelo",
            desc="Local SEO for roofing contractors: rank in Google Maps for \"roof repair near me\" and \"roofing "
                 "contractor\" searches and win more jobs. Free audit, first results in 2–3 weeks.",
            h1=("Local SEO for", "roofers"),
            lead="Homeowners look for a roofer after a storm or a leak, and they compare the top results on Google Maps. "
                 "We put your roofing company there, with the reviews and photos that win the job.",
            query="roof repair near me",
            rivals=[("Summit Roofing Co.", "4.2", "3.1 mi"), ("Apex Roof Pros", "4.4", "2.2 mi")],
            why="Why roofers lose jobs to competitors",
            problems=[
                ("Storm season is a race",
                 "After a storm, searches spike. The roofers already at the top of the map get the calls; everyone else waits."),
                ("A new roof is a big decision",
                 "Homeowners read reviews and look at photos before they trust anyone with their roof."),
                ("Paying per lead adds up",
                 "Lead sites charge for every inquiry. Your own Maps ranking brings calls you don't pay for one by one."),
            ],
            work=[
                ("Google Business Profile", "\"Roofing contractor\" as the primary category, your services and service "
                 "area set up properly, and your licensing details where they belong."),
                ("Before & after photos", "A steady stream of real project photos on your profile and site, the proof homeowners look for."),
                ("Service pages", "Separate pages for roof repair, roof replacement, storm damage, inspections and gutters."),
                ("Service-area pages", "Pages for the towns you cover, so you show up where the work is, not only near your office."),
                ("Reviews that sell", "A review request after every finished roof, and replies to every review, good or bad."),
                ("Directory listings", "Consistent info on BBB, Angi, Houzz, Yelp, Nextdoor, Apple Maps and Bing."),
            ],
            keywords=["roof repair near me", "roofing contractor [city]", "roof replacement [city]",
                      "storm damage roof repair", "roof inspection near me", "roof leak repair"],
            faq=[
                ("When should a roofer start local SEO?",
                 "Before your busy season. Rankings take a few weeks to build, so starting before storm season means "
                 "you're already near the top when searches spike."),
                SITE_Q_EN,
                ("Do reviews really matter that much for roofers?",
                 "Yes. For a big-ticket job like a roof, reviews and photos often decide which contractor a homeowner "
                 "picks. They also help your Maps ranking."),
            ],
        ),
        es=dict(
            name="Techadores", one="empresa de techos", you="Su empresa de techos",
            title="SEO local para techadores | Más trabajos desde Google | Rankelo",
            desc="SEO local para empresas de techos: aparezca en Google Maps para \"reparación de techos cerca de mí\" "
                 "y consiga más trabajos. Auditoría gratis, primeros resultados en 2–3 semanas.",
            h1=("SEO local para", "techadores"),
            lead="Después de una tormenta o una gotera, el propietario busca un techador y compara los primeros "
                 "resultados de Google Maps. Ponemos a su empresa ahí, con las reseñas y fotos que ganan el trabajo.",
            query="reparación de techos cerca de mí",
            rivals=[("Summit Roofing Co.", "4.2", "3.1 mi"), ("Apex Roof Pros", "4.4", "2.2 mi")],
            why="Por qué los techadores pierden trabajos frente a la competencia",
            problems=[
                ("La temporada de tormentas es una carrera",
                 "Tras una tormenta las búsquedas se disparan. Quien ya está arriba en el mapa recibe las llamadas."),
                ("Un techo nuevo es una gran decisión",
                 "El propietario lee reseñas y mira fotos antes de confiar su techo a alguien."),
                ("Pagar por cada contacto sale caro",
                 "Los sitios de leads cobran por cada consulta. Su propio posicionamiento en Maps trae llamadas sin ese costo."),
            ],
            work=[
                ("Perfil de Google Business", "\"Contratista de techos\" como categoría principal, servicios y zona de "
                 "servicio bien configurados, y sus licencias donde corresponde."),
                ("Fotos de antes y después", "Fotos reales de proyectos en su perfil y sitio, la prueba que buscan los propietarios."),
                ("Páginas de servicios", "Páginas para reparación, reemplazo, daños por tormenta, inspecciones y canaletas."),
                ("Páginas por zona", "Páginas para las ciudades que atiende, para aparecer donde está el trabajo."),
                ("Reseñas que venden", "Solicitud de reseña tras cada trabajo y respuesta a cada reseña, buena o mala."),
                ("Directorios", "Datos coherentes en BBB, Angi, Houzz, Yelp, Nextdoor, Apple Maps y Bing."),
            ],
            keywords=["reparación de techos cerca de mí", "techador en [ciudad]", "cambio de techo [ciudad]",
                      "daños de techo por tormenta", "inspección de techo cerca de mí", "reparar gotera de techo"],
            faq=[
                ("¿Cuándo debe empezar un techador con el SEO local?",
                 "Antes de su temporada alta. El posicionamiento tarda unas semanas en construirse, así que empezar "
                 "antes de las tormentas significa estar arriba cuando suben las búsquedas."),
                SITE_Q_ES,
                ("¿De verdad importan tanto las reseñas?",
                 "Sí. En un trabajo grande como un techo, las reseñas y fotos suelen decidir qué contratista se elige. "
                 "Además ayudan a su posición en Maps."),
            ],
        ),
    ),
    # ------------------------------------------------------------------ dentists
    dict(
        key="dentists",
        slug=dict(en="local-seo-for-dentists/", es="es/seo-local-para-dentistas/"),
        en=dict(
            name="Dentists", one="dental practice", you="Your dental practice",
            title="Local SEO for Dentists | Get More New Patients from Google | Rankelo",
            desc="Local SEO for dental practices: show up first in Google Maps for \"dentist near me\", emergency "
                 "dental and treatment searches. Free audit, first results in 2–3 weeks.",
            h1=("Local SEO for", "dentists"),
            lead="New patients choose a dentist from Google Maps: close by, open now, great reviews. "
                 "We help your practice show up first and look like the obvious choice.",
            query="dentist near me",
            rivals=[("Bright Smile Dental", "4.3", "1.9 mi"), ("Harbor Family Dentistry", "4.5", "2.6 mi")],
            why="Why practices lose new patients to competitors",
            problems=[
                ("Patients pick from the map",
                 "Most people searching for a dentist choose from the three practices Google shows first."),
                ("Every treatment is its own search",
                 "Implants, aligners, emergency visits and cleanings are different searches. One homepage can't rank for all of them."),
                ("Reviews decide trust",
                 "Patients compare ratings before they book. Fewer or older reviews make a practice look like the riskier choice."),
            ],
            work=[
                ("Google Business Profile", "\"Dentist\" as the primary category, plus the specialties you offer, "
                 "accurate hours, insurance info and a booking link."),
                ("Treatment pages", "A page for each treatment you want more of: implants, whitening, emergency dental, "
                 "pediatric care, aligners."),
                ("Review requests", "A simple, compliant way to ask every patient for a review, with no incentives that "
                 "break Google's rules."),
                ("Office & team photos", "Real photos of your office and team that make new patients comfortable before they arrive."),
                ("Health directories", "Consistent listings on Healthgrades, Zocdoc, Yelp, Apple Maps and Bing."),
                ("Each location covered", "If you have more than one office, each gets its own profile and its own page."),
            ],
            keywords=["dentist near me", "emergency dentist [city]", "dental implants [city]",
                      "teeth whitening near me", "pediatric dentist near me", "dentist open saturday"],
            faq=[
                ("Is it OK to ask patients for reviews?",
                 "Yes, you can ask every patient. What you can't do is offer rewards for reviews or post fake ones; "
                 "Google removes those and can penalize the profile. We set up a request flow that stays within the rules."),
                SITE_Q_EN,
                ("We have more than one location. Does that change anything?",
                 "Each location gets its own Google Business Profile and its own page on your site, so every office "
                 "can rank in its own neighborhood."),
            ],
        ),
        es=dict(
            name="Dentistas", one="clínica dental", you="Su clínica dental",
            title="SEO local para dentistas | Más pacientes nuevos desde Google | Rankelo",
            desc="SEO local para clínicas dentales: aparezca primero en Google Maps para \"dentista cerca de mí\", "
                 "urgencias y tratamientos. Auditoría gratis, primeros resultados en 2–3 semanas.",
            h1=("SEO local para", "dentistas"),
            lead="Los pacientes nuevos eligen dentista en Google Maps: cerca, abierto y con buenas reseñas. "
                 "Ayudamos a su clínica a aparecer primero y a verse como la mejor opción.",
            query="dentista cerca de mí",
            rivals=[("Bright Smile Dental", "4.3", "1.9 mi"), ("Harbor Family Dentistry", "4.5", "2.6 mi")],
            why="Por qué las clínicas pierden pacientes nuevos",
            problems=[
                ("Los pacientes eligen en el mapa",
                 "Quien busca dentista suele elegir entre las tres clínicas que Google muestra primero."),
                ("Cada tratamiento es otra búsqueda",
                 "Implantes, alineadores, urgencias y limpiezas son búsquedas distintas. Una sola página no posiciona para todas."),
                ("Las reseñas generan confianza",
                 "Los pacientes comparan calificaciones antes de reservar. Menos reseñas o reseñas viejas parecen más riesgo."),
            ],
            work=[
                ("Perfil de Google Business", "\"Dentista\" como categoría principal, sus especialidades, horario correcto, "
                 "información de seguros y enlace para reservar."),
                ("Páginas de tratamientos", "Una página por tratamiento: implantes, blanqueamiento, urgencias, "
                 "odontopediatría, alineadores."),
                ("Solicitud de reseñas", "Una forma sencilla y conforme a las reglas de pedir reseña a cada paciente, sin incentivos."),
                ("Fotos de la clínica y el equipo", "Fotos reales que dan tranquilidad al paciente nuevo antes de llegar."),
                ("Directorios de salud", "Datos coherentes en Healthgrades, Zocdoc, Yelp, Apple Maps y Bing."),
                ("Cada sede cubierta", "Si tiene más de una clínica, cada una tiene su propio perfil y su propia página."),
            ],
            keywords=["dentista cerca de mí", "dentista de urgencia [ciudad]", "implantes dentales [ciudad]",
                      "blanqueamiento dental cerca de mí", "dentista infantil cerca de mí", "dentista abierto sábado"],
            faq=[
                ("¿Se puede pedir reseñas a los pacientes?",
                 "Sí, puede pedírsela a cada paciente. Lo que no se permite es ofrecer premios por reseñas ni publicar "
                 "reseñas falsas; Google las elimina y puede penalizar el perfil. Creamos un proceso dentro de las reglas."),
                SITE_Q_ES,
                ("Tenemos más de una sede. ¿Cambia algo?",
                 "Cada sede tiene su propio perfil de Google Business y su propia página en el sitio, para que cada "
                 "clínica posicione en su zona."),
            ],
        ),
    ),
    # ------------------------------------------------------------------ HVAC
    dict(
        key="hvac",
        slug=dict(en="local-seo-for-hvac/", es="es/seo-local-para-hvac/"),
        en=dict(
            name="HVAC", one="HVAC company", you="Your HVAC company",
            title="Local SEO for HVAC Companies | Rank for AC Repair Near Me | Rankelo",
            desc="Local SEO for HVAC contractors: rank in Google Maps for \"AC repair near me\", furnace and "
                 "installation searches before your busy season. Free audit, first results in 2–3 weeks.",
            h1=("Local SEO for", "HVAC companies"),
            lead="When the AC dies in July or the heat goes out in January, people call whoever is first on Google Maps. "
                 "We get your HVAC company there before the season starts.",
            query="ac repair near me",
            rivals=[("CoolAir Services", "4.2", "2.7 mi"), ("Comfort Pro HVAC", "4.4", "1.5 mi")],
            why="Why HVAC companies lose calls in peak season",
            problems=[
                ("Demand is seasonal and urgent",
                 "Heat waves and cold snaps bring a flood of searches. If you're not already at the top, those calls go elsewhere."),
                ("Repair, install and maintenance are different searches",
                 "\"AC repair\", \"furnace replacement\" and \"heat pump installation\" each need their own page to rank."),
                ("Big service areas, one map pin",
                 "Without service-area pages, you mostly show up near your shop instead of across the area you cover."),
            ],
            work=[
                ("Google Business Profile", "\"HVAC contractor\" as the primary category, plus air conditioning repair "
                 "and heating services, with your full service list and area."),
                ("Service pages", "Pages for AC repair, AC installation, furnace repair, heat pumps, duct cleaning and maintenance plans."),
                ("Seasonal posts", "Profile posts timed to your seasons: AC tune-ups in spring, furnace checks in fall."),
                ("Service-area pages", "Pages for each town you serve, so you rank across your whole area."),
                ("Reviews after every call", "A text link your techs send after each visit, plus replies to every review."),
                ("Directory listings", "Consistent info on Angi, HomeAdvisor, Yelp, BBB, Nextdoor, Apple Maps and Bing."),
            ],
            keywords=["ac repair near me", "hvac company near me", "furnace repair [city]",
                      "ac installation [city]", "heat pump installation", "emergency ac repair"],
            faq=[
                ("When should an HVAC company start local SEO?",
                 "A month or two before your busy season. That gives your profile and pages time to climb, so you're "
                 "near the top when the first heat wave or cold snap hits."),
                SITE_Q_EN,
                ("We cover a lot of towns. Can we rank in all of them?",
                 "We set your service area on Google and build a page for each main town you serve. Towns closer to "
                 "your location are easier; farther ones take more work, and we'll tell you honestly what's realistic."),
            ],
        ),
        es=dict(
            name="HVAC", one="empresa de HVAC", you="Su empresa de HVAC",
            title="SEO local para empresas de HVAC | Aire acondicionado y calefacción | Rankelo",
            desc="SEO local para empresas de aire acondicionado y calefacción: aparezca en Google Maps para "
                 "\"reparación de aire acondicionado cerca de mí\" antes de la temporada alta. Auditoría gratis.",
            h1=("SEO local para", "empresas de HVAC"),
            lead="Cuando el aire acondicionado falla en julio o la calefacción en enero, la gente llama al primero de "
                 "Google Maps. Ponemos a su empresa ahí antes de que empiece la temporada.",
            query="reparación de aire acondicionado cerca de mí",
            rivals=[("CoolAir Services", "4.2", "2.7 mi"), ("Comfort Pro HVAC", "4.4", "1.5 mi")],
            why="Por qué las empresas de HVAC pierden llamadas en temporada alta",
            problems=[
                ("La demanda es urgente y de temporada",
                 "Las olas de calor y de frío traen muchas búsquedas. Si no está arriba, esas llamadas van a otro."),
                ("Reparar, instalar y mantener son búsquedas distintas",
                 "\"Reparación de AC\", \"cambio de calefacción\" e \"instalación de bomba de calor\" necesitan su propia página."),
                ("Zona grande, un solo pin",
                 "Sin páginas por zona, aparece sobre todo cerca de su local y no en toda el área que atiende."),
            ],
            work=[
                ("Perfil de Google Business", "\"Contratista de HVAC\" como categoría principal, más reparación de aire "
                 "acondicionado y calefacción, con todos sus servicios y su zona."),
                ("Páginas de servicios", "Páginas para reparación e instalación de AC, calefacción, bombas de calor, "
                 "limpieza de ductos y planes de mantenimiento."),
                ("Publicaciones de temporada", "Publicaciones según la época: revisión de AC en primavera y de calefacción en otoño."),
                ("Páginas por zona", "Una página por ciudad que atiende, para posicionar en toda su área."),
                ("Reseñas tras cada visita", "Un enlace que sus técnicos envían tras cada servicio y respuesta a cada reseña."),
                ("Directorios", "Datos coherentes en Angi, HomeAdvisor, Yelp, BBB, Nextdoor, Apple Maps y Bing."),
            ],
            keywords=["reparación de aire acondicionado cerca de mí", "empresa de hvac cerca de mí",
                      "reparación de calefacción [ciudad]", "instalación de aire acondicionado [ciudad]",
                      "instalación de bomba de calor", "reparación de ac de urgencia"],
            faq=[
                ("¿Cuándo debe empezar una empresa de HVAC con el SEO local?",
                 "Uno o dos meses antes de la temporada alta. Así el perfil y las páginas tienen tiempo de subir y "
                 "usted está arriba cuando llega la primera ola de calor o de frío."),
                SITE_Q_ES,
                ("Atendemos muchas ciudades. ¿Podemos posicionar en todas?",
                 "Configuramos su zona de servicio en Google y creamos una página por cada ciudad principal. Las más "
                 "cercanas son más fáciles; las lejanas requieren más trabajo, y le diremos con honestidad qué es realista."),
            ],
        ),
    ),
]
