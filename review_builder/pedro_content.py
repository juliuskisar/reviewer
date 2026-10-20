"""Conteúdo pedagógico da revisão Pedro — Geografia PE 2º trimestre."""

from __future__ import annotations

REVIEW_ID = "pedro-pe-geografia-2tri"
ASSET_PREFIX = "assets/pedro_pe_geografia_2_tri"


def _src(page: str) -> dict:
    return {
        "asset": f"{ASSET_PREFIX}/{page}",
        "origin_type": "observed",
        "evidence": [f"Material do Caderno 2 — {page}"],
    }


def build_content() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Geografia — PE 2º Trimestre",
        "subtitle": "Pedro · 6º ano · Módulos 5 e 6 do Caderno 2",
        "language": "pt-BR",
        "discipline": "Geografia",
        "grade": "6º ano",
        "metadata": {
            "student_name": "Pedro",
            "exam_type": "Prova Específica (PE)",
            "estimated_duration_minutes": 60,
        },
        "study_route": [
            {"order": 1, "title": "Explicações", "section_id": "explain"},
            {"order": 2, "title": "Resumo rápido", "section_id": "summary"},
            {"order": 3, "title": "Exercícios", "section_id": "exercises"},
        ],
        "sections": [
            _section_route(),
            _section_explain(),
            _section_summary(),
        ],
    }


def _section_route() -> dict:
    return {
        "id": "route",
        "type": "study_route",
        "title": "Roteiro de estudo",
        "blocks": [
            {
                "type": "panel_intro",
                "content": {
                    "title": "O que vamos revisar",
                    "text": "Conteúdo dos Módulos 5 e 6: a Terra no Sistema Solar, estrutura interna, "
                    "tectônica de placas, tipos de rochas, agentes do relevo e formas do relevo "
                    "— com destaque para o Brasil. Reserve cerca de 1 hora para percorrer tudo com calma.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🪐", "title": "Sistema Solar", "text": "8 planetas, heliocentrismo, origem da Terra"},
                        {"icon": "🌍", "title": "Estrutura da Terra", "text": "Crosta, manto, núcleo · litosfera e placas"},
                        {"icon": "🗺️", "title": "Tectônica", "text": "Pangeia, deriva continental, dorsais e colisões"},
                        {"icon": "🪨", "title": "Rochas", "text": "Magmática, sedimentar, metamórfica · ciclo das rochas"},
                        {"icon": "⛰️", "title": "Relevo", "text": "Agentes internos/externos · planícies, planaltos, serras"},
                        {"icon": "🇧🇷", "title": "Brasil", "text": "Altimetria, picos mais altos, formas predominantes"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": ["Módulo 5 — Terra e placas", "Módulo 6 — Rochas e relevo"],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Leia os blocos curtos, quadros de conceitos e tabelas.",
                            "tip": "Feche o acordeão e tente explicar o tópico com suas palavras antes de avançar.",
                        },
                        {
                            "title": "Revise o Resumo rápido",
                            "panel": "summary",
                            "panel_label": "Resumo rápido",
                            "description": "Percorra os blocos-síntese de todos os tópicos — use como mapa mental para a PE.",
                            "tip": "Cada acordeão resume um tópico em cards e tabelas, no mesmo estilo das explicações.",
                        },
                        {
                            "title": "Faça os Exercícios",
                            "panel": "exercises",
                            "panel_label": "Exercícios",
                            "description": "Questões no estilo do Teste do caderno (p. 216–218): notícias, afirmativas I–IV e ciclo das rochas.",
                            "tip": "Responda sem olhar a explicação. Só depois clique em Verificar.",
                        },
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "info",
                    "title": "Como navegar:",
                    "text": "Cada passo acima tem um botão que leva direto à aba correspondente. "
                    "Você também pode usar as abas no topo da página a qualquer momento.",
                },
            },
        ],
    }


def _section_explain() -> dict:
    return {
        "id": "explain",
        "type": "explanations",
        "title": "Explicações",
        "blocks": [
            *_topic_solar_system(),
            *_topic_earth_origin(),
            *_topic_earth_structure(),
            *_topic_plate_tectonics(),
            *_topic_rocks(),
            *_topic_relief_agents(),
            *_topic_relief_forms(),
            *_topic_brazilian_relief(),
        ],
    }


def _topic_solar_system() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. A Terra no Sistema Solar"}, "topic_id": "solar_system"},
        {
            "type": "paragraph",
            "content": {
                "text": "O Universo reúne bilhões de galáxias. A nossa é a Via Láctea. Dentro dela está o "
                "Sistema Solar: o Sol (uma estrela) e oito planetas que giram ao seu redor.",
            },
            "topic_id": "solar_system",
            "sources": [_src("page-010.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "☀️", "title": "Sol", "text": "Estrela central — fonte de luz e calor"},
                    {"icon": "🪐", "title": "8 planetas", "text": "Mercúrio, Vênus, Terra, Marte, Júpiter, Saturno, Urano, Netuno"},
                    {"icon": "🌙", "title": "Outros corpos", "text": "Luas, asteroides, cometas, meteoroides e satélites"},
                ],
            },
            "topic_id": "solar_system",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Lembre-se:",
                "text": "Desde 2006, Plutão é planeta-anão (UAI). A trajetória de um corpo celeste ao redor de "
                "outro se chama órbita.",
            },
            "topic_id": "solar_system",
        },
        {"type": "heading", "content": {"level": 3, "text": "2. Distâncias e Teoria Heliocêntrica"}, "topic_id": "solar_system"},
        {
            "type": "list",
            "content": {
                "ordered": False,
                "items": [
                    "Terra → Sol: cerca de 150 milhões de km",
                    "Terra → Lua: cerca de 384 mil km",
                    "Luz solar até a Terra: 8 minutos e 18 segundos",
                ],
            },
            "topic_id": "solar_system",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Até o século XVI, acreditava-se que a Terra era o centro do Universo. Nicolau Copérnico "
                "(1473–1543) propôs a Teoria Heliocêntrica: o Sol é o centro do Sistema Solar e os planetas "
                "giram ao seu redor.",
            },
            "topic_id": "solar_system",
        },
    ]


def _topic_earth_origin() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "3. Origem e idade da Terra"}, "topic_id": "earth_structure"},
        {
            "type": "paragraph",
            "content": {
                "text": "Segundo a teoria das nebulosas, o Sistema Solar surgiu de uma nuvem de gases e poeira "
                "cósmica. Parte formou o Sol; o restante originou os planetas.",
            },
            "topic_id": "earth_structure",
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🔥", "title": "Início incandescente", "text": "A Terra nasceu quente e foi esfriando"},
                    {"icon": "🪨", "title": "Crosta", "text": "Primeira camada sólida externa"},
                    {"icon": "💧", "title": "Oceanos", "text": "Vapor condensado → chuvas longas → mares"},
                ],
            },
            "topic_id": "earth_structure",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Idade:",
                "text": "A Terra tem cerca de 4,6 bilhões de anos — não confunda com a idade do Universo (~13,8 bi).",
            },
            "topic_id": "earth_structure",
        },
    ]


def _topic_earth_structure() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "4. Estrutura interna da Terra"}, "topic_id": "earth_structure"},
        {
            "type": "paragraph",
            "content": {"text": "Por composição química, a Terra tem três camadas principais:"},
            "topic_id": "earth_structure",
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Camadas por composição química",
                "headers": ["Camada", "Espessura", "Característica"],
                "rows": [
                    ["Crosta", "5–70 km", "Sólida; continental (antiga) ou oceânica (recente)"],
                    ["Manto", "~2.900 km", "Silício, ferro e magnésio"],
                    ["Núcleo", "~3.500 km", "Externo líquido + interno sólido (Fe-Ni); > 5.000 °C"],
                ],
            },
            "topic_id": "earth_structure",
            "sources": [_src("page-030.jpg")],
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Por características físicas: litosfera → astenosfera → mesosfera → endosfera. "
                "A litosfera é fragmentada em placas tectônicas que flutuam sobre a astenosfera.",
            },
            "topic_id": "earth_structure",
        },
    ]


def _topic_plate_tectonics() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "5. Tectônica de placas e Deriva continental"}, "topic_id": "plate_tectonics"},
        {
            "type": "paragraph",
            "content": {
                "text": "Alfred Wegener (1880–1930) propôs a Deriva Continental: há centenas de milhões de anos "
                "existia a Pangeia (supercontinente) rodeada pela Pantalassa (oceano único). Depois veio a "
                "divisão em Laurásia (norte) e Gondwana (sul).",
            },
            "topic_id": "plate_tectonics",
            "sources": [_src("page-001.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "↔️", "title": "Separação", "text": "Placas se afastam → magma sobe → dorsal meso-oceânica"},
                    {"icon": "💥", "title": "Colisão", "text": "Placas se chocam → montanhas, fossas, subducção"},
                    {"icon": "🌋", "title": "Instabilidade", "text": "Terremotos e vulcões nas bordas das placas"},
                ],
            },
            "topic_id": "plate_tectonics",
            "sources": [_src("page-006.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Por que o Brasil quase não tem vulcões?",
                "text": "Estamos no interior da placa Sul-Americana, longe das bordas onde ocorrem colisões "
                "e separações intensas.",
            },
            "topic_id": "plate_tectonics",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "O movimento das placas é provocado pelas correntes de convecção do manto: material "
                "aquecido sobe, esfria e desce, empurrando a litosfera.",
            },
            "topic_id": "plate_tectonics",
        },
    ]


def _topic_rocks() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "6. Rochas, minerais e ciclo das rochas"}, "topic_id": "rock_types"},
        {
            "type": "comparison_table",
            "content": {
                "caption": "Três tipos de rochas",
                "headers": ["Tipo", "Como se forma", "Exemplo"],
                "rows": [
                    ["Magmática (ígnea)", "Resfriamento do magma", "Granito (plutônica), basalto (vulcânica)"],
                    ["Sedimentar", "Acúmulo e compactação de sedimentos", "Arenito, calcário"],
                    ["Metamórfica", "Calor e pressão sobre outras rochas", "Granito → gnaisse; calcário → mármore"],
                ],
            },
            "topic_id": "rock_types",
            "sources": [_src("page-025.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "1️⃣", "title": "Solidificação", "text": "Magma resfria → rocha magmática"},
                    {"icon": "2️⃣", "title": "Intemperismo", "text": "Rochas se desgastam → sedimentos"},
                    {"icon": "3️⃣", "title": "Compactação", "text": "Sedimentos acumulados → rocha sedimentar"},
                    {"icon": "4️⃣", "title": "Metamorfismo", "text": "Calor/pressão transformam rochas"},
                    {"icon": "5️⃣", "title": "Fusão", "text": "Rochas fundem → magma de novo"},
                ],
            },
            "topic_id": "rock_types",
            "sources": [_src("page-010.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "info",
                "title": "Ciclo contínuo:",
                "text": "Magmática → sedimentos → sedimentar → metamórfica → magma. Os processos se repetem "
                "ao longo de milhões de anos.",
            },
            "topic_id": "rock_types",
        },
    ]


def _topic_relief_agents() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "7. Agentes transformadores do relevo"}, "topic_id": "relief_forms"},
        {
            "type": "comparison_table",
            "content": {
                "caption": "Agentes internos x externos",
                "headers": ["", "Internos (endógenos)", "Externos (exógenos)"],
                "rows": [
                    ["De onde vêm", "Interior da Terra", "Superfície terrestre"],
                    ["Exemplos", "Tectonismo, vulcanismo, terremotos", "Água, vento, gelo, seres vivos"],
                    ["Efeito", "Constroem o relevo", "Desgastam (intemperismo e erosão)"],
                ],
            },
            "topic_id": "relief_forms",
        },
    ]


def _topic_relief_forms() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "8. Formas do relevo"}, "topic_id": "relief_forms"},
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🏔️", "title": "Cadeia de montanhas", "text": "Maiores elevações, encostas íngremes — Andes, Himalaia"},
                    {"icon": "🌾", "title": "Planície", "text": "Área plana e baixa; predomina sedimentação"},
                    {"icon": "🕳️", "title": "Depressão", "text": "100–500 m, área baixa; predomina erosão — ex.: Depressão Sertaneja"},
                    {"icon": "⛰️", "title": "Planalto", "text": "Acima de ~300 m, com serras e escarpas"},
                    {"icon": "🔗", "title": "Serra", "text": "Relevo alongado — Mantiqueira, Serra do Mar"},
                    {"icon": "📐", "title": "Escarpa", "text": "Queda abrupta entre formas de relevo"},
                ],
            },
            "topic_id": "relief_forms",
            "sources": [_src("page-022.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Cuidado:",
                "text": "Escarpa ≠ serra. A Serra do Mar vista do litoral é, na verdade, uma escarpa "
                "(declive abrupto na borda do planalto).",
            },
            "topic_id": "relief_forms",
        },
    ]


def _topic_brazilian_relief() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "9. Relevo brasileiro"}, "topic_id": "brazilian_relief"},
        {
            "type": "paragraph",
            "content": {
                "text": "A altimetria mostra as altitudes em um mapa. No Brasil, altitudes baixas (0–500 m) "
                "predominam — observe as cores claras (verde e amarelo) na legenda.",
            },
            "topic_id": "brazilian_relief",
            "sources": [_src("page-008.jpg")],
        },
        {
            "type": "list",
            "content": {
                "ordered": False,
                "items": [
                    "Pico da Neblina (AM): 2.995 m — ponto mais alto do Brasil",
                    "Pico 31 de Março (AM): 2.974 m",
                    "Pico da Bandeira (MG/ES): 2.891 m",
                    "Pedra da Mina (SP/MG): 2.798 m",
                ],
            },
            "topic_id": "brazilian_relief",
            "sources": [_src("page-014.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Por que não temos montanhas altíssimas?",
                "text": "O Brasil está no centro da placa Sul-Americana, longe de colisões recentes entre "
                "placas — diferente dos Andes ou do Himalaia.",
            },
            "topic_id": "brazilian_relief",
        },
    ]


def _section_summary() -> dict:
    return {
        "id": "summary",
        "type": "quick_summary",
        "title": "Resumo rápido",
        "blocks": [
            {
                "type": "panel_intro",
                "content": {
                    "title": "Mapa mental da PE",
                    "text": "Cada tópico abre em um acordeão com cards e tabelas — o essencial para revisar antes da prova.",
                },
            },
            *_summary_solar_system(),
            *_summary_earth_origin(),
            *_summary_earth_structure(),
            *_summary_plate_tectonics(),
            *_summary_rocks(),
            *_summary_relief_agents(),
            *_summary_relief_forms(),
            *_summary_brazilian_relief(),
        ],
    }


def _summary_solar_system() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Sistema Solar"}},
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🌌", "title": "Via Láctea", "text": "Nossa galáxia · Sol = estrela central"},
                    {"icon": "🪐", "title": "8 planetas", "text": "Mercúrio → Netuno · Plutão = planeta-anão (2006)"},
                    {"icon": "📏", "title": "Distâncias", "text": "Terra–Sol ~150 mi km · luz solar: 8 min 18 s"},
                    {"icon": "☀️", "title": "Heliocentrismo", "text": "Copérnico (séc. XVI): Sol no centro"},
                ],
            },
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Pegadinha:",
                "text": "Idade do Universo (~13,8 bi) ≠ idade do Sistema Solar/Terra (~4,6 bi).",
            },
        },
    ]


def _summary_earth_origin() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "2. Origem da Terra"}},
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "☁️", "title": "Nebulosa", "text": "Nuvem de gases → Sol + planetas"},
                    {"icon": "🔥", "title": "4,6 bi anos", "text": "Terra incandescente → esfriamento → crosta"},
                    {"icon": "🌊", "title": "Oceanos", "text": "Vapor condensado → chuvas → mares"},
                ],
            },
        },
    ]


def _summary_earth_structure() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "3. Estrutura interna"}},
        {
            "type": "comparison_table",
            "content": {
                "caption": "Por composição química",
                "headers": ["Camada", "Espessura", "Destaque"],
                "rows": [
                    ["Crosta", "5–70 km", "Continental (antiga) ou oceânica (recente)"],
                    ["Manto", "~2.900 km", "Silício, ferro, magnésio"],
                    ["Núcleo", "~3.500 km", "Externo líquido + interno sólido (Fe-Ni)"],
                ],
            },
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🪨", "title": "Litosfera", "text": "Crosta + manto superior · fragmentada em placas"},
                    {"icon": "🌊", "title": "Astenosfera", "text": "Placas flutuam sobre ela"},
                    {"icon": "⬇️", "title": "Mesosfera + Endosfera", "text": "Camadas profundas, muito densas"},
                ],
            },
        },
    ]


def _summary_plate_tectonics() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "4. Tectônica e Deriva continental"}},
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🌍", "title": "Wegener", "text": "Pangeia + Pantalassa → Laurásia + Gondwana"},
                    {"icon": "↔️", "title": "Separação", "text": "Dorsal meso-oceânica · magma → novas rochas"},
                    {"icon": "💥", "title": "Colisão", "text": "Montanhas · fossa · subducção · vulcões"},
                    {"icon": "🇧🇷", "title": "Brasil", "text": "Centro da placa → poucos vulcões/terremotos"},
                ],
            },
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Mecanismo:",
                "text": "Correntes de convecção do manto empurram as placas tectônicas.",
            },
        },
    ]


def _summary_rocks() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "5. Rochas e ciclo"}},
        {
            "type": "comparison_table",
            "content": {
                "caption": "Tipos de rochas",
                "headers": ["Tipo", "Origem", "Exemplo"],
                "rows": [
                    ["Magmática", "Magma resfria", "Granito, basalto"],
                    ["Sedimentar", "Sedimentos compactados", "Arenito, calcário"],
                    ["Metamórfica", "Calor + pressão", "Gnaisse, mármore"],
                ],
            },
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "1️⃣", "title": "Solidificação", "text": "Magma → magmática"},
                    {"icon": "2️⃣", "title": "Intemperismo", "text": "Rochas → sedimentos"},
                    {"icon": "3️⃣", "title": "Compactação", "text": "Sedimentos → sedimentar (X)"},
                    {"icon": "4️⃣", "title": "Metamorfismo", "text": "→ metamórfica (Y)"},
                    {"icon": "5️⃣", "title": "Fusão", "text": "→ magma (ciclo recomeça)"},
                ],
            },
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Pegadinha:",
                "text": "Dinossauros = Era Mesozoica · Carbonífero = Paleozoico (não Mesozoico).",
            },
        },
    ]


def _summary_relief_agents() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "6. Agentes do relevo"}},
        {
            "type": "comparison_table",
            "content": {
                "headers": ["", "Internos (endógenos)", "Externos (exógenos)"],
                "rows": [
                    ["Origem", "Interior da Terra", "Superfície"],
                    ["Exemplos", "Tectonismo, vulcanismo, terremotos", "Água, vento, gelo, seres vivos"],
                    ["Efeito", "Constroem o relevo", "Desgastam (intemperismo, erosão)"],
                ],
            },
        },
    ]


def _summary_relief_forms() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "7. Formas do relevo"}},
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🏔️", "title": "Montanhas", "text": "Maiores elevações · Andes, Himalaia"},
                    {"icon": "🌾", "title": "Planície", "text": "Baixa · sedimentação predominante"},
                    {"icon": "🕳️", "title": "Depressão", "text": "100–500 m · erosão predominante"},
                    {"icon": "⛰️", "title": "Planalto", "text": ">300 m · serras e escarpas · erosão"},
                    {"icon": "🔗", "title": "Serra", "text": "Relevo alongado · Mantiqueira, Serra do Mar"},
                    {"icon": "📐", "title": "Escarpa", "text": "Queda abrupta · Serra do Mar vista do litoral"},
                ],
            },
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Pegadinha:",
                "text": "Planície (baixa, sedimentação) ≠ planalto (alto, erosão). Escarpa ≠ serra.",
            },
        },
    ]


def _summary_brazilian_relief() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "8. Relevo brasileiro"}},
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🗺️", "title": "Altimetria", "text": "0–500 m predominam (verde/amarelo no mapa)"},
                    {"icon": "🏔️", "title": "Pico da Neblina", "text": "2.995 m (AM) — ponto mais alto"},
                    {"icon": "📍", "title": "Maiores altitudes", "text": "Ao norte · fronteira com Venezuela/Guiana"},
                    {"icon": "🌄", "title": "Sudeste", "text": "Pico da Bandeira 2.891 m · Pedra da Mina 2.798 m"},
                ],
            },
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Por quê?",
                "text": "Brasil no centro da placa Sul-Americana — sem colisões recentes, sem cadeias como os Andes.",
            },
        },
    ]


def build_exercises() -> dict:
    def sa(page: str) -> list[str]:
        return [f"{ASSET_PREFIX}/{page}"]

    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "exercises": [
            {
                "id": "geo-pe-001",
                "type": "multiple_choice",
                "topic": "solar_system",
                "question": (
                    "Leia as afirmativas:\n"
                    "I. O Sistema Solar é formado por oito planetas. Até 2006 eram nove, "
                    "mas Plutão passou a ser classificado como planeta-anão.\n"
                    "II. A Terra é o terceiro planeta mais próximo do Sol.\n"
                    "III. Mercúrio, Vênus, Terra e Marte são menores que Júpiter, Saturno, Urano e Netuno.\n"
                    "IV. A origem do Sistema Solar está relacionada à origem do Universo, "
                    "ocorrida há 4,6 bilhões de anos.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "I, II e III", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": (
                    "I, II e III estão corretas. IV está errada: 4,6 bi de anos é a idade do "
                    "Sistema Solar/Terra, não do Universo (~13,8 bi)."
                ),
                "difficulty": "advanced",
                "source_assets": sa("page-010.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-002",
                "type": "multiple_choice",
                "topic": "rock_types",
                "question": (
                    "As eras geológicas ajudam a compreender a evolução da Terra. "
                    "Em se tratando das eras geológicas e dos principais acontecimentos, é correto afirmar que:"
                ),
                "options": [
                    "No Paleozoico formaram-se as cadeias dos Andes e dos Alpes e surgiu o ser humano.",
                    "Nos eons Arcaico e Proterozoico ocorreram a solidificação da crosta, "
                    "a formação dos primeiros oceanos e das primeiras formas de vida.",
                    "No Cenozoico os dinossauros dominaram o planeta por milhões de anos.",
                    "No Mesozoico, especialmente no Carbonífero, predominou a vida nos oceanos "
                    "e formaram-se reservas de carvão mineral.",
                ],
                "correct_answer": 1,
                "explanation": (
                    "Arcaico e Proterozoico = crosta sólida, oceanos e primeiras formas de vida. "
                    "Dinossauros = Mesozoico; Carbonífero = Paleozoico; humanos = Cenozoico."
                ),
                "difficulty": "advanced",
                "source_assets": sa("page-030.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-003",
                "type": "multiple_choice",
                "topic": "plate_tectonics",
                "question": (
                    "Leia a notícia:\n"
                    "«Vulcão entra em erupção no sul do Japão» — Erupção na ilha de Kuchinoerabu. "
                    "O Japão está no Cinturão de Fogo do Pacífico, onde placas tectônicas se encontram. "
                    "O país possui 127 vulcões ativos.\n\n"
                    "Com base na notícia e em seus conhecimentos, assinale a alternativa correta:"
                ),
                "options": [
                    "Vulcões encontram-se em áreas de colisão e separação de placas tectônicas. "
                    "Nessas regiões podem surgir ilhas formadas pela liberação de lava, como no Japão.",
                    "Vulcões formam-se apenas em áreas de dobramento, e a solidificação da lava "
                    "origina cadeias montanhosas em qualquer região do planeta.",
                    "O vulcanismo faz as placas se afastar porque a pressão das erupções "
                    "empurra as placas tectônicas.",
                    "O Brasil é conhecido por intensa atividade vulcânica, com dezenas de vulcões ativos.",
                ],
                "correct_answer": 0,
                "explanation": (
                    "Vulcanismo concentra-se nas bordas das placas. O Brasil fica no interior da placa "
                    "Sul-Americana — quase não há vulcões ativos."
                ),
                "difficulty": "advanced",
                "source_assets": sa("page-010.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-004",
                "type": "multiple_choice",
                "topic": "rock_types",
                "question": (
                    "Observe o esquema do ciclo das rochas:\n"
                    "Magma → (resfriamento) → 1 → (intemperismo) → Sedimentos → (compactação) → 2 "
                    "→ (calor e pressão) → 3 → (fusão) → Magma.\n\n"
                    "Assinale a alternativa que completa corretamente o diagrama (1, 2 e 3):"
                ),
                "options": [
                    "1. sedimentar; 2. ígnea; 3. metamórfica",
                    "1. metamórfica; 2. sedimentar; 3. ígnea",
                    "1. ígnea; 2. sedimentar; 3. metamórfica",
                    "1. ígnea; 2. metamórfica; 3. sedimentar",
                ],
                "correct_answer": 2,
                "explanation": "1 = ígnea/magmática · 2 = sedimentar · 3 = metamórfica — como no Teste do caderno.",
                "difficulty": "advanced",
                "source_assets": sa("page-010.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-005",
                "type": "multiple_choice",
                "topic": "rock_types",
                "question": (
                    "Leia as afirmativas sobre o ciclo das rochas:\n"
                    "I. A solidificação do magma forma rochas magmáticas (ígneas).\n"
                    "II. A compactação de sedimentos forma rochas metamórficas.\n"
                    "III. O intemperismo e a erosão produzem sedimentos a partir de rochas expostas.\n"
                    "IV. A fusão de rochas no interior da Terra pode gerar magma novamente.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, III e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": (
                    "I, III e IV estão corretas. II está errada: compactação de sedimentos forma "
                    "rocha sedimentar, não metamórfica."
                ),
                "difficulty": "advanced",
                "source_assets": sa("page-018.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-006",
                "type": "multiple_choice",
                "topic": "brazilian_relief",
                "question": (
                    "Considerando as características gerais do relevo brasileiro, podemos afirmar "
                    "que elevadas altitudes (acima de 1.200 m) predominam no território brasileiro?"
                ),
                "options": [
                    "Sim, porque o Pico da Neblina prova que todo o país é montanhoso.",
                    "Não, porque a maior parte do território apresenta altitudes baixas, "
                    "predominantemente entre 0 e 500 m.",
                    "Sim, porque as serras do Sudeste cobrem a maior área do território.",
                    "Não, porque o Brasil não possui nenhuma forma de relevo acima de 300 m.",
                ],
                "correct_answer": 1,
                "explanation": (
                    "Altitudes baixas (0–500 m) cobrem a maior parte do Brasil. Os picos mais altos "
                    "são exceções regionais, como a Neblina (2.995 m) no norte."
                ),
                "difficulty": "advanced",
                "source_assets": sa("page-008.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-007",
                "type": "multiple_choice",
                "topic": "brazilian_relief",
                "question": (
                    "Leia as afirmativas sobre o relevo brasileiro:\n"
                    "I. No Brasil predominam altitudes baixas (0–500 m).\n"
                    "II. As maiores altitudes ficam ao sul, no Rio Grande do Sul.\n"
                    "III. O Pico da Neblina (2.995 m) é o ponto mais alto do território.\n"
                    "IV. O Brasil possui cadeias montanhosas recentes semelhantes aos Andes.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I e III", "II e IV", "III e IV"],
                "correct_answer": 1,
                "explanation": (
                    "I e III corretas. Maiores altitudes ao norte (AM). Sem cadeias recentes como os Andes "
                    "— o Brasil está no centro da placa."
                ),
                "difficulty": "advanced",
                "source_assets": sa("page-014.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-008",
                "type": "multiple_choice",
                "topic": "plate_tectonics",
                "question": (
                    "Observe o esquema de separação entre placas tectônicas (dorsal meso-oceânica). "
                    "Quando duas placas se separam, o magma sobe e forma novas rochas. "
                    "Esse processo explica a formação de:"
                ),
                "options": [
                    "Fossas oceânicas profundas e cadeias de montanhas dobradas",
                    "Dorsais meso-oceânicas e renovação da crosta oceânica",
                    "Planícies costeiras e deltas sedimentares",
                    "Depressões absolutas no interior dos continentes",
                ],
                "correct_answer": 1,
                "explanation": "Separação = dorsal meso-oceânica + novas rochas magmáticas (p. 212–213).",
                "difficulty": "intermediate",
                "source_assets": sa("page-006.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-009",
                "type": "multiple_choice",
                "topic": "plate_tectonics",
                "question": (
                    "Nas áreas de choque entre placas tectônicas, é correto afirmar que:"
                ),
                "options": [
                    "Uma placa pode mergulhar sob a outra (subducção), formando fossas, "
                    "vulcões e cadeias montanhosas.",
                    "As placas sempre se afastam, formando apenas planícies oceânicas.",
                    "Não ocorrem terremotos porque a crosta está estável nessas regiões.",
                    "Fósseis marinhos nunca aparecem em regiões montanhosas elevadas.",
                ],
                "correct_answer": 0,
                "explanation": (
                    "Colisão = dobramentos, subducção, vulcões. Fósseis marinhos no alto das montanhas "
                    "comprovam a deriva continental."
                ),
                "difficulty": "intermediate",
                "source_assets": sa("page-006.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-010",
                "type": "multiple_choice",
                "topic": "plate_tectonics",
                "question": (
                    "Alfred Wegener propôs que, há cerca de 225 milhões de anos, existia o supercontinente "
                    "Pangeia, rodeado pelo oceano Pantalassa. Depois ocorreu a divisão em:"
                ),
                "options": [
                    "América e Eurásia",
                    "Laurásia (norte) e Gondwana (sul)",
                    "Atlântico e Pacífico",
                    "Brasil e África como continentes separados desde sempre",
                ],
                "correct_answer": 1,
                "explanation": "Pangeia → Laurásia + Gondwana → continentes atuais (p. 210–211).",
                "difficulty": "intermediate",
                "source_assets": sa("page-001.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-011",
                "type": "multiple_choice",
                "topic": "earth_structure",
                "question": (
                    "Por composição química, a camada mais externa, fina e sólida, onde vivemos, é a crosta. "
                    "Ela pode ser continental (30–70 km) ou oceânica (5–10 km). "
                    "Por características físicas, a crosta integra a:"
                ),
                "options": ["Astenosfera", "Litosfera", "Mesosfera", "Endosfera"],
                "correct_answer": 1,
                "explanation": "Litosfera = crosta + parte superior do manto; fragmentada em placas (p. 209).",
                "difficulty": "intermediate",
                "source_assets": sa("page-030.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-012",
                "type": "multiple_choice",
                "topic": "rock_types",
                "question": (
                    "O granito, rocha magmática plutônica usada no Monumento às Bandeiras (SP), "
                    "pode transformar-se em gnaisse. O calcário pode transformar-se em mármore. "
                    "Essas transformações ocorrem por:"
                ),
                "options": [
                    "Acúmulo e compactação de sedimentos ao longo de milhões de anos",
                    "Resfriamento rápido do magma na superfície terrestre",
                    "Altas temperaturas e/ou pressão no interior da Terra",
                    "Ação exclusiva de agentes externos de intemperismo e erosão",
                ],
                "correct_answer": 2,
                "explanation": "Metamorfismo = calor + pressão sobre rochas preexistentes (p. 215–218).",
                "difficulty": "intermediate",
                "source_assets": sa("page-025.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-013",
                "type": "multiple_choice",
                "topic": "relief_forms",
                "question": (
                    "Leia as afirmativas sobre formas de relevo:\n"
                    "I. Planaltos sedimentares tendem a ser mais planos e são chamados de chapadas.\n"
                    "II. Depressões são áreas baixas (100–500 m) com predomínio de erosão.\n"
                    "III. Escarpas são transições abruptas; a Serra do Mar vista do litoral é, "
                    "na verdade, uma escarpa.\n"
                    "IV. Planícies são áreas altas com predomínio de processos de erosão.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e III", "I e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": (
                    "I, II e III corretas. Planície é baixa, com sedimentação — IV está errada (p. 224–225)."
                ),
                "difficulty": "advanced",
                "source_assets": sa("page-022.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-014",
                "type": "multiple_choice",
                "topic": "relief_forms",
                "question": (
                    "Os agentes internos (endógenos) e externos (exógenos) transformam o relevo. "
                    "Assinale a alternativa que associa corretamente agente e efeito:"
                ),
                "options": [
                    "Vulcanismo — desgasta o relevo pela ação do vento e da chuva",
                    "Erosão pela água da chuva — desgasta o relevo (agente externo)",
                    "Tectonismo — compacta sedimentos formando rochas sedimentares",
                    "Terremotos — formam apenas planícies costeiras baixas",
                ],
                "correct_answer": 1,
                "explanation": "Agentes externos desgastam (erosão). Internos constroem (tectonismo, vulcanismo).",
                "difficulty": "intermediate",
                "source_assets": sa("page-022.jpg"),
                "section": "final_quiz",
            },
            {
                "id": "geo-pe-015",
                "type": "multiple_choice",
                "topic": "brazilian_relief",
                "question": (
                    "«Pensar representações» — Por que o relevo brasileiro não apresenta altitudes "
                    "tão elevadas quanto os Andes ou o Himalaia?"
                ),
                "options": [
                    "Porque o clima tropical impede a formação de montanhas altas",
                    "Porque o Brasil está no centro da placa Sul-Americana, longe das bordas "
                    "onde ocorrem colisões entre placas",
                    "Porque os agentes externos de erosão destruíram todas as montanhas brasileiras",
                    "Porque o território brasileiro é totalmente plano, sem variações de altitude",
                ],
                "correct_answer": 1,
                "explanation": "Posição tectônica central = poucos soerguimentos recentes (p. 227–228).",
                "difficulty": "advanced",
                "source_assets": sa("page-014.jpg"),
                "section": "final_quiz",
            },
        ],
    }
