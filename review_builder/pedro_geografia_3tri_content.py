"""Conteúdo pedagógico da revisão Pedro — Geografia PE 3º trimestre (Módulos 11–13)."""

from __future__ import annotations

REVIEW_ID = "pedro-pe-geografia-3tri"
ASSET_PREFIX = "assets/pedro_pe_geografia_3_tri"


def _src(page: str) -> dict:
    return {
        "asset": f"{ASSET_PREFIX}/{page}",
        "origin_type": "observed",
        "evidence": [f"Caderno 2 — Geografia — {page}"],
    }


def build_content() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Geografia — PE 3º Trimestre",
        "subtitle": "Pedro · 6º ano · Módulos 11, 12 e 13",
        "language": "pt-BR",
        "discipline": "Geografia",
        "grade": "6º ano",
        "metadata": {
            "student_name": "Pedro",
            "exam_type": "Prova Específica (PE)",
            "estimated_duration_minutes": 65,
        },
        "study_route": [
            {"order": 1, "title": "Explicações", "section_id": "explain"},
            {"order": 2, "title": "Resumo rápido", "section_id": "summary"},
            {"order": 3, "title": "Mapas interativos", "section_id": "maps"},
            {"order": 4, "title": "Jogo das capitais", "section_id": "capital_game"},
            {"order": 5, "title": "Exercícios", "section_id": "exercises"},
        ],
        "sections": [
            _section_route(),
            _section_explain(),
            _section_summary(),
            _section_interactive_maps(),
            _section_capital_game(),
        ],
    }


def _interactive_map_blocks() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Mapa completo — regiões e evolução"}},
        {
            "type": "brazil_map",
            "content": {
                "title": "Mapa político interativo",
                "intro": "Explore regiões, capitais, novos estados e a evolução histórica dos estados.",
                "period": "post_1988",
                "mode": "regions",
                "show_period_toggle": True,
                "show_mode_toggle": True,
                "highlight": [],
                "interactive": True,
                "caption": "Use o modo Regiões para localizar biomas e bacias ao estudar o caderno.",
                "aria_label": "Mapa político do Brasil interativo",
            },
            "sources": [_src("page-034.jpg")],
        },
        {"type": "heading", "content": {"level": 3, "text": "2. Capitais das 27 UFs"}},
        {
            "type": "brazil_map",
            "content": {
                "title": "Capitais estaduais",
                "mode": "capitals",
                "show_period_toggle": False,
                "show_mode_toggle": False,
                "interactive": True,
                "caption": "Manaus, Belém e Porto Alegre aparecem no módulo de águas e vegetação.",
                "aria_label": "Mapa do Brasil com capitais",
            },
            "sources": [_src("page-009.jpg")],
        },
        {"type": "heading", "content": {"level": 3, "text": "3. Fusão MT/MS (até 1977)"}},
        {
            "type": "brazil_map",
            "content": {
                "title": "Mato Grosso antes da criação de MS",
                "mode": "evolution",
                "period": "1942_1977",
                "show_period_toggle": True,
                "show_mode_toggle": False,
                "interactive": True,
                "caption": "Pantanal e Guarani aquifer passam por GO, MT e MS — veja os contornos atuais.",
                "aria_label": "Evolução de Mato Grosso e Mato Grosso do Sul",
            },
            "sources": [_src("page-046.jpg")],
        },
    ]


def _section_interactive_maps() -> dict:
    return {
        "id": "maps",
        "type": "interactive_maps",
        "title": "Mapas interativos",
        "blocks": [
            {
                "type": "panel_intro",
                "content": {
                    "title": "Localize no mapa",
                    "text": "Biomas, bacias e capitais citadas nas explicações ficam mais fáceis "
                    "com o mapa clicável. Alterne modos e períodos históricos.",
                },
            },
            *_interactive_map_blocks(),
        ],
    }


def _section_capital_game() -> dict:
    return {
        "id": "capital_game",
        "type": "capital_game",
        "title": "Jogo das capitais",
        "blocks": [
            {
                "type": "panel_intro",
                "content": {
                    "title": "Complete o mapa!",
                    "text": "Clique em um estado, digite a capital e confirme. "
                    "Estados corretos ficam verdes — meta: 27 acertos.",
                },
            },
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
                    "text": "Paisagens vegetais no mundo e no Brasil, biodiversidade e hotspots, "
                    "águas do planeta, bacias hidrográficas, navegação, hidrelétricas, "
                    "poluição e aquíferos. Reserve cerca de 65 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🌎", "title": "Mundo", "text": "Biomas · clima · tundra a floresta tropical"},
                        {"icon": "🔥", "title": "Hotspots", "text": "Endemismo · desmatamento · Mata Atlântica e Cerrado"},
                        {"icon": "🇧🇷", "title": "Biomas BR", "text": "Amazônia · Cerrado · Caatinga · Pantanal"},
                        {"icon": "💧", "title": "Água doce", "text": "2,5% do planeta · Brasil = grandes reservas"},
                        {"icon": "🛶", "title": "Rios", "text": "Bacias · navegação · Itaipu · Belo Monte"},
                        {"icon": "🌊", "title": "Poluição", "text": "Esgoto · plástico · aquíferos Guarani e SAGA"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 11 — Paisagens vegetais e biodiversidade",
                        "Módulo 12 — Vegetação do Brasil",
                        "Módulo 13 — Águas do mundo e do Brasil",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Oito tópicos em acordeão: leia parágrafos, tabelas e gráficos embutidos.",
                            "tip": "Relacione cada bioma ao clima antes de ir ao resumo.",
                        },
                        {
                            "title": "Revise o Resumo rápido",
                            "panel": "summary",
                            "panel_label": "Resumo rápido",
                            "description": "Síntese por tópico — use como cola mental na véspera da PE.",
                        },
                        {
                            "title": "Explore os Mapas interativos",
                            "panel": "maps",
                            "panel_label": "Mapas interativos",
                            "description": "Regiões, capitais e evolução dos estados — útil para bacias e biomas.",
                            "tip": "Destaque estados da Amazônia, Nordeste e Sul ao revisar água e vegetação.",
                        },
                        {
                            "title": "Jogue o Jogo das capitais",
                            "panel": "capital_game",
                            "panel_label": "Jogo das capitais",
                            "description": "Fixe capitais citadas no caderno (Manaus, Belém, Brasília, Porto Alegre…).",
                        },
                        {
                            "title": "Faça os Exercícios",
                            "panel": "exercises",
                            "panel_label": "Exercícios",
                            "description": "16 questões autossuficientes, incluindo afirmativas I–IV e gráficos.",
                            "tip": "Responda sem olhar o gabarito; depois leia a explicação de cada item.",
                        },
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "info",
                    "title": "Como navegar",
                    "text": "Cada passo tem botão para a aba correspondente. "
                    "Mapas e gráficos estão no HTML — você não precisa das fotos do caderno.",
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
            *_topic_world_vegetation(),
            *_topic_biodiversity(),
            *_topic_brazil_biomes(),
            *_topic_forests_savannas(),
            *_topic_coastal_wetlands(),
            *_topic_water_earth(),
            *_topic_hydrography(),
            *_topic_pollution_aquifers(),
        ],
    }


def _topic_world_vegetation() -> list:
    tid = "world_vegetation"
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Paisagens vegetais do mundo"}, "topic_id": tid},
        {
            "type": "paragraph",
            "content": {
                "text": "Bioma é o conjunto de vegetação, clima, relevo e solo que forma uma paisagem "
                "reconhecível. Do polo à equator existem tundra, taiga (floresta boreal), florestas "
                "temperada e tropical, savanas, desertos e mangues — cada um com adaptações diferentes.",
            },
            "topic_id": tid,
            "sources": [_src("page-033.jpg"), _src("page-022.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Três formações frias/temperadas (Módulo 11)",
                "headers": ["Bioma", "Clima", "Vegetação típica"],
                "rows": [
                    ["Tundra", "Polar, inverno longo", "Musgos, liquens, arbustos baixos"],
                    ["Floresta boreal (taiga)", "Inverno rigoroso, verão ~20 °C", "Coníferas em agulha, até ~30 m"],
                    ["Floresta temperada", "Quatro estações, chuvas regulares", "Carvalhos e nogueiras; folhas caem no outono"],
                ],
            },
            "topic_id": tid,
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🌴", "title": "Floresta tropical", "text": "Calor o ano todo · dossel contínuo · lixiviação do solo"},
                    {"icon": "🦁", "title": "Savana", "text": "Estação seca e chuvosa · árvores retorcidas · Cerrado africano e brasileiro"},
                    {"icon": "🌵", "title": "Deserto", "text": "Pouca chuva · xerófitas (cactos) ou steppes frias"},
                ],
            },
            "topic_id": tid,
            "sources": [_src("page-035.jpg"), _src("page-015.jpg")],
        },
    ]


def _topic_biodiversity() -> list:
    tid = "biodiversity_hotspots"
    return [
        {"type": "heading", "content": {"level": 3, "text": "2. Biodiversidade, desmatamento e hotspots"}, "topic_id": tid},
        {
            "type": "paragraph",
            "content": {
                "text": "Biodiversidade é a variedade de espécies nos ambientes terrestres e aquáticos. "
                "Estima-se 8,7 milhões de espécies no planeta, mas só ~1,5 milhão foram descritas. "
                "Zonas tropicais quentes e úmidas concentram mais da metade das espécies.",
            },
            "topic_id": tid,
            "sources": [_src("page-032.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "warning",
                "title": "Hotspot (Norman Myers)",
                "text": "Região com >1.500 espécies endêmicas e perda de ≥70% da vegetação original. "
                "No Brasil: Mata Atlântica e Cerrado. Hotspot não significa «bem preservado» — "
                "significa urgência de conservação.",
            },
            "topic_id": tid,
            "sources": [_src("page-014.jpg"), _src("page-038.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🪓", "title": "Desmatamento", "text": "Pasto, lavoura, madeira, cidades — perda de habitat"},
                    {"icon": "🐒", "title": "Consequências", "text": "Extinções, erosão, assoreamento, clima local"},
                    {"icon": "♻️", "title": "Sustentável", "text": "Usar recursos sem esgotar — equilíbrio social e econômico"},
                ],
            },
            "topic_id": tid,
        },
    ]


def _topic_brazil_biomes() -> list:
    tid = "brazil_biomes"
    return [
        {"type": "heading", "content": {"level": 3, "text": "3. Cobertura vegetal e biomas do Brasil"}, "topic_id": tid},
        {
            "type": "paragraph",
            "content": {
                "text": "O Brasil tem grande diversidade de vegetação original ligada a clima e solo. "
                "Mapas de «cobertura vegetal original» mostram floresta equatorial, Mata Atlântica, "
                "Cerrado, Caatinga, Pantanal, campos, cocais e manguezais. "
                "Mapas de biomas (IBGE) agrupam áreas com flora, fauna e clima semelhantes.",
            },
            "topic_id": tid,
            "sources": [_src("page-004.jpg"), _src("page-046.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "info",
                "title": "Mapas interativos",
                "text": "Abra a aba Mapas interativos para ver regiões e estados enquanto "
                "memoriza onde ficam Amazônia, Cerrado e Mata Atlântica.",
            },
            "topic_id": tid,
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Vegetação x clima (ideias do Teste)",
                "headers": ["Vegetação", "Clima dominante"],
                "rows": [
                    ["Floresta equatorial (Amazônia)", "Equatorial quente e úmido"],
                    ["Cerrado", "Tropical com estação seca marcada"],
                    ["Caatinga", "Semiárido"],
                    ["Campos (Pampa)", "Subtropical com chuvas regulares"],
                ],
            },
            "topic_id": tid,
            "sources": [_src("page-016.jpg"), _src("page-045.jpg")],
        },
    ]


def _topic_forests_savannas() -> list:
    tid = "brazil_forests_savannas"
    return [
        {"type": "heading", "content": {"level": 3, "text": "4. Florestas, Cerrado e Caatinga"}, "topic_id": tid},
        {
            "type": "paragraph",
            "content": {
                "text": "A Floresta Amazônica ocupa quase metade do território original, com árvores altas "
                "e copas sempre verdes. A Mata Atlântica seguia a faixa litorânea — hoje restam "
                "fragmentos; é hotspot. O Cerrado tem árvores retorcidas e casca grossa, clima "
                "tropical com verão chuvoso e inverno seco (veja climograma de Brasília). "
                "A Caatinga perde folhas na seca («mata branca») no semiárido nordestino.",
            },
            "topic_id": tid,
            "sources": [_src("page-019.jpg"), _src("page-029.jpg"), _src("page-020.jpg"), _src("page-024.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🌳", "title": "Mata Atlântica", "text": "Alta densidade · faixa litorânea original · muito desmatada"},
                    {"icon": "🌾", "title": "Cerrado", "text": "Savana mais rica do mundo · soja e gado · hotspot"},
                    {"icon": "☀️", "title": "Caatinga", "text": "Decidua na seca · babaçu e carnaúba na Mata dos Cocais (MA/PI)"},
                ],
            },
            "topic_id": tid,
            "sources": [_src("page-047.jpg")],
        },
    ]


def _topic_coastal_wetlands() -> list:
    tid = "brazil_coastal_wetlands"
    return [
        {"type": "heading", "content": {"level": 3, "text": "5. Pantanal, manguezais e litoral"}, "topic_id": tid},
        {
            "type": "paragraph",
            "content": {
                "text": "O Pantanal (MS/MT) alterna cheia e seca — mistura de cerrado, florestas e campos; "
                "grande planície alagável. Manguezais são halófitas na foz dos rios: raízes aéreas, "
                "berçário de peixes e crustáceos. Sofrem com esgoto, lixo e urbanização costeira. "
                "O litoral brasileiro (7.367 km) concentra portos como Santos e pesca artesanal.",
            },
            "topic_id": tid,
            "sources": [_src("page-031.jpg"), _src("page-049.jpg"), _src("page-043.jpg"), _src("page-011.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Pressões sobre mangue e pantanal",
                "headers": ["Ambiente", "Ameaça principal"],
                "rows": [
                    ["Manguezal", "Esgoto/domesticos · apenas ~46% do esgoto coletado é tratado no BR"],
                    ["Pantanal", "Desmatamento (>15% da área original)"],
                    ["Costa", "Poluição por portos e cidades"],
                ],
            },
            "topic_id": tid,
        },
    ]


def _topic_water_earth() -> list:
    tid = "water_earth_cycle"
    return [
        {"type": "heading", "content": {"level": 3, "text": "6. Água na Terra e ciclo hidrológico"}, "topic_id": tid},
        {
            "type": "paragraph",
            "content": {
                "text": "Teoria mais aceita: água surgiu por degaseificação vulcânica na formação da Terra. "
                "Cerca de 70% da superfície é água líquida, mas 97,5% é salgada. "
                "Só 2,5% é doce — a maior parte em geleiras e aquíferos. "
                "O Brasil detém ~12% da água doce mundial, porém a distribuição interna é desigual.",
            },
            "topic_id": tid,
            "sources": [_src("page-012.jpg"), _src("page-051.jpg")],
        },
        {
            "type": "paragraph",
            "content": {
                "text": "No ciclo hidrológico, o Sol evapora água dos mares e superfícies; vapor condensa "
                "em nuvens; precipitação alimenta rios e infiltração no solo (lençol freático). "
                "Em cidades, pavimentação aumenta escoamento superficial e enchentes.",
            },
            "topic_id": tid,
            "sources": [_src("page-018.jpg"), _src("page-017.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "info",
                "title": "Estresse hídrico",
                "text": "Mapa de 2019: Brasil tem risco baixo na maior parte do território, "
                "mas o Nordeste semiárido enfrenta pressão — disponibilidade ≠ acesso para todos.",
            },
            "topic_id": tid,
        },
    ]


def _topic_hydrography() -> list:
    tid = "hydrography_energy"
    return [
        {"type": "heading", "content": {"level": 3, "text": "7. Bacias, navegação e energia hidrelétrica"}, "topic_id": tid},
        {
            "type": "paragraph",
            "content": {
                "text": "Bacia hidrográfica: rio principal + afluentes drenando uma área; divisores de água "
                "separam bacias. Rios perenes fluem o ano todo; intermitentes secam na estiagem. "
                "No Brasil: Amazônica (maior volume), Tocantins-Araguaia, São Francisco, Paraná… "
                "Navegação fluvial é barata, mas só ~5% da carga nacional — eclusas vencem desníveis.",
            },
            "topic_id": tid,
            "sources": [_src("page-034.jpg"), _src("page-013.jpg"), _src("page-050.jpg")],
        },
        {
            "type": "pie_chart",
            "content": {
                "title": "Exemplo didático — matriz elétrica (%)",
                "slices": [
                    {"label": "Hidrelétrica", "value": 65, "color": "#2563eb"},
                    {"label": "Biomassa + eólica + solar", "value": 19, "color": "#16a34a"},
                    {"label": "Fósseis (gás, carvão, petróleo)", "value": 13, "color": "#ca8a04"},
                    {"label": "Nuclear", "value": 3, "color": "#9333ea"},
                ],
                "unit": "%",
                "caption": "Valores aproximados do Brasil (2021) — no mundo a hidrelétrica fica perto de 16%.",
            },
            "topic_id": tid,
            "sources": [_src("page-041.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "⚡", "title": "Usina hidrelétrica", "text": "Represa · turbina · gerador — energia mecânica → elétrica"},
                    {"icon": "🌊", "title": "Itaipu / Tucuruí", "text": "Paraná e Tocantins — grandes potências e impactos sociais"},
                    {"icon": "🐟", "title": "Belo Monte", "text": "Altera pulso de cheia no Xingu — peixes e populações ribeirinhas"},
                ],
            },
            "topic_id": tid,
            "sources": [_src("page-023.jpg"), _src("page-027.jpg")],
        },
    ]


def _topic_pollution_aquifers() -> list:
    tid = "water_pollution_aquifers"
    return [
        {"type": "heading", "content": {"level": 3, "text": "8. Usos da água, poluição e aquíferos"}, "topic_id": tid},
        {
            "type": "paragraph",
            "content": {
                "text": "Agropecuária consome ~70% da água doce global (irrigação por pivô ou gotejamento). "
                "Indústria ~22%; uso doméstico urbano pode ser muito maior que no campo. "
                "Poluição: esgoto e lixo nos rios, agrotóxicos no lençol, plástico nos oceanos (85% "
                "do lixo marinho), maré negra de petróleo.",
            },
            "topic_id": tid,
            "sources": [_src("page-006.jpg"), _src("page-003.jpg"), _src("page-008.jpg"), _src("page-044.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Grandes aquíferos brasileiros",
                "headers": ["Aquífero", "Extensão / volume", "Destaque"],
                "rows": [
                    ["SAGA (Grande Amazônia)", "~1,3 mi km² · ~162 mil km³", "Maior área e volume no BR"],
                    ["Guarani", "~1,2 mi km² (840 mil km² no BR)", "BR, AR, PY, UY — abastece cidades"],
                ],
            },
            "topic_id": tid,
            "sources": [_src("page-002.jpg"), _src("page-011.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "warning",
                "title": "Pegada d'água",
                "text": "Produtos industrializados escondem água: 1 kg de carne bovina pode exigir "
                "dezenas de milhares de litros no processo — consumo vai além da torneira.",
            },
            "topic_id": tid,
            "sources": [_src("page-044.jpg")],
        },
    ]


def _section_summary() -> dict:
    blocks = [
        {
            "type": "panel_intro",
            "content": {
                "title": "Mapa mental da PE",
                "text": "Oito blocos — mesma ordem das explicações. Feche o acordeão e recite de memória.",
            },
        },
    ]
    summaries = [
        ("1. Mundo", "world_vegetation", [
            {"icon": "❄️", "title": "Frio", "text": "Tundra · taiga · inverno longo"},
            {"icon": "🍂", "title": "Temperada", "text": "Quatro estações · folhas caem"},
            {"icon": "🌧️", "title": "Tropical", "text": "Calor + chuvas · dossel · savana com estação seca"},
        ]),
        ("2. Hotspots", "biodiversity_hotspots", [
            {"icon": "📉", "title": "Critério", "text": ">1.500 endêmicas · perdeu ≥70% da vegetação"},
            {"icon": "🇧🇷", "title": "Brasil", "text": "Mata Atlântica e Cerrado"},
            {"icon": "🪓", "title": "Causas", "text": "Desmatamento · erosão · espécies ameaçadas"},
        ]),
        ("3. Biomas BR", "brazil_biomes", [
            {"icon": "🗺️", "title": "Mapas", "text": "Cobertura original x biomas IBGE"},
            {"icon": "🌡️", "title": "Clima", "text": "Vegetação acompanha o clima dominante"},
            {"icon": "🏙️", "title": "Antropização", "text": "Litoral e Centro-Oeste muito alterados"},
        ]),
        ("4. Florestas e sertão", "brazil_forests_savannas", [
            {"icon": "🌳", "title": "Amazônia", "text": "Equatorial · maior floresta equatorial"},
            {"icon": "🌊", "title": "Mata Atlântica", "text": "Faixa litorânea · hotspot"},
            {"icon": "🌾", "title": "Cerrado/Caatinga", "text": "Retorcidos · mata branca na seca"},
        ]),
        ("5. Úmidos e mar", "brazil_coastal_wetlands", [
            {"icon": "🐊", "title": "Pantanal", "text": "Cheia e seca · MS/MT"},
            {"icon": "🌿", "title": "Mangue", "text": "Raízes aéreas · berçário marinho"},
            {"icon": "⚓", "title": "Litoral", "text": "Portos · pesca · poluição"},
        ]),
        ("6. Água doce", "water_earth_cycle", [
            {"icon": "🌍", "title": "Estoque", "text": "97,5% salgada · 2,5% doce"},
            {"icon": "🇧🇷", "title": "Brasil", "text": "~12% da doce mundial · mal distribuída"},
            {"icon": "🔄", "title": "Ciclo", "text": "Evaporação · chuva · infiltração"},
        ]),
        ("7. Rios e energia", "hydrography_energy", [
            {"icon": "🛶", "title": "Bacias", "text": "Amazônica · SF · Paraná · Tocantins"},
            {"icon": "⚡", "title": "BR vs mundo", "text": "BR ~65% hidro · mundo ~16% hidro"},
            {"icon": "🏗️", "title": "Impactos", "text": "Alagamentos · deslocamento · peixes"},
        ]),
        ("8. Poluição", "water_pollution_aquifers", [
            {"icon": "🚜", "title": "Usos", "text": "Agro 70% · indústria · casa"},
            {"icon": "🛢️", "title": "Poluição", "text": "Esgoto · plástico · petróleo"},
            {"icon": "💎", "title": "Aquíferos", "text": "SAGA maior · Guarani transfronteiriço"},
        ]),
    ]
    for title, _tid, cards in summaries:
        blocks.append({"type": "heading", "content": {"level": 3, "text": title}})
        blocks.append({"type": "concept_grid", "content": {"cards": cards}})
    blocks.append({
        "type": "callout",
        "content": {
            "variant": "warning",
            "title": "Pegadinha da PE",
            "text": "Hotspot não é «área preservada». Matriz elétrica brasileira não é igual à mundial. "
            "Guarani é enorme, mas SAGA é maior dentro do Brasil.",
        },
    })
    return {"id": "summary", "type": "quick_summary", "title": "Resumo rápido", "blocks": blocks}


def build_exercises() -> dict:
    def sa(page: str) -> list[str]:
        return [f"{ASSET_PREFIX}/{page}"]

    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "exercises": [
            {
                "id": "geo3-pe-001",
                "type": "multiple_choice",
                "topic": "world_vegetation",
                "question": (
                    "A floresta boreal (taiga) apresenta, como adaptação principal ao clima:"
                ),
                "options": [
                    "Folhas largas que caem no outono",
                    "Coníferas com folhas em forma de agulha",
                    "Cactos armazenando água no caule",
                    "Raízes aéreas na beira do mar",
                ],
                "correct_answer": 1,
                "explanation": "Taiga = coníferas que reduzem perda de água no inverno rigoroso.",
                "difficulty": "basic",
                "source_assets": sa("page-026.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo3-pe-002",
                "type": "multiple_choice",
                "topic": "world_vegetation",
                "question": (
                    "Leia as afirmativas sobre floresta tropical:\n"
                    "I. O dossel forma cobertura contínua de copas.\n"
                    "II. Lixiviação empobrece solos expostos à chuva intensa.\n"
                    "III. Ocorre apenas na Europa.\n"
                    "IV. Calor e umidade elevados favorecem grande biodiversidade.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Florestas tropicais dominam faixa equatorial, não Europa (III).",
                "difficulty": "intermediate",
                "source_assets": sa("page-035.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo3-pe-003",
                "type": "multiple_choice",
                "topic": "biodiversity_hotspots",
                "question": "Um «hotspot» de biodiversidade exige, entre outros critérios:",
                "options": [
                    "Ter menos de 100 espécies endêmicas",
                    "Manter mais de 90% da vegetação original intacta",
                    "Possuir mais de 1.500 espécies endêmicas e perder ≥70% da vegetação original",
                    "Localizar-se somente fora dos trópicos",
                ],
                "correct_answer": 2,
                "explanation": "Myers: endemismo alto + destruição acentuada — Mata Atlântica e Cerrado no BR.",
                "difficulty": "basic",
                "source_assets": sa("page-014.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo3-pe-004",
                "type": "multiple_choice",
                "topic": "biodiversity_hotspots",
                "question": (
                    "Sobre desmatamento e hotspots no Brasil:\n"
                    "I. Hotspot significa região com biodiversidade ameaçada, não «bem protegida».\n"
                    "II. Apenas o Cerrado é hotspot brasileiro.\n"
                    "III. Desmatamento acelera erosão e assoreamento.\n"
                    "IV. Mata Atlântica também é hotspot.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, III e IV", "II e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, III e IV corretas. Dois hotspots principais: Mata Atlântica e Cerrado (II falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-037.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo3-pe-005",
                "type": "multiple_choice",
                "topic": "brazil_biomes",
                "question": (
                    "A cobertura vegetal original do Cerrado encontra-se sob clima:"
                ),
                "options": ["Equatorial", "Tropical com estação seca", "Polar", "Mediterrâneo"],
                "correct_answer": 1,
                "explanation": "Cerrado = tropical com verão chuvoso e inverno seco (climograma de Brasília).",
                "difficulty": "basic",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo3-pe-006",
                "type": "multiple_choice",
                "topic": "brazil_forests_savannas",
                "question": (
                    "Sobre Mata Atlântica, é correto afirmar:"
                ),
                "options": [
                    "Ocorria originalmente ao longo de grande parte da faixa litorânea brasileira",
                    "É dominada por pinheiros do Paraná em todo o território",
                    "Nunca sofreu desmatamento intenso",
                    "Equivale à floresta boreal da América do Norte",
                ],
                "correct_answer": 0,
                "explanation": "Mata Atlântica litorânea, densa e muito desmatada — alternativa d do Teste p. 276.",
                "difficulty": "basic",
                "source_assets": sa("page-016.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo3-pe-007",
                "type": "multiple_choice",
                "topic": "brazil_forests_savannas",
                "question": (
                    "Árvores retorcidas, casca grossa e arbustos espaçados indicam vegetação de:"
                ),
                "options": ["Caatinga semiárida", "Cerrado", "Floresta equatorial", "Tundra"],
                "correct_answer": 1,
                "explanation": "Adaptações ao fogo e à seca do Cerrado — foto do Teste p. 276.",
                "difficulty": "basic",
                "source_assets": sa("page-045.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo3-pe-008",
                "type": "multiple_choice",
                "topic": "brazil_coastal_wetlands",
                "question": (
                    "Manguezais são importantes porque:"
                ),
                "options": [
                    "Ocorrem apenas no interior semiárido",
                    "Servem de berçário para peixes e crustáceos",
                    "Não sofrem impacto de cidades costeiras",
                    "São formações exclusivamente andinas",
                ],
                "correct_answer": 1,
                "explanation": "Raízes em água salobra/ambar; ameaçados por esgoto e urbanização.",
                "difficulty": "basic",
                "source_assets": sa("page-049.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo3-pe-009",
                "type": "multiple_choice",
                "topic": "water_earth_cycle",
                "question": (
                    "Leia as afirmativas sobre água doce no planeta:\n"
                    "I. Cerca de 97,5% da água da Terra é salgada.\n"
                    "II. Geleiras e aquíferos concentram boa parte da água doce.\n"
                    "III. Ter grandes reservas garante água potável para toda população.\n"
                    "IV. O Brasil possui parcela relevante das reservas mundiais.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "III e IV", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. Reservas ≠ acesso universal (III falsa) — Teste p. 299.",
                "difficulty": "intermediate",
                "source_assets": sa("page-051.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo3-pe-010",
                "type": "multiple_choice",
                "topic": "water_earth_cycle",
                "question": (
                    "Em áreas urbanas com muito asfalto, aumenta principalmente:"
                ),
                "options": [
                    "Infiltração no lençol freático",
                    "Escoamento superficial para rios",
                    "Formação de geleiras",
                    "Evaporação oceânica",
                ],
                "correct_answer": 1,
                "explanation": "Impermeabilização → mais água corre na superfície → enchentes.",
                "difficulty": "basic",
                "source_assets": sa("page-017.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo3-pe-011",
                "type": "multiple_choice",
                "topic": "hydrography_energy",
                "question": (
                    "Observe o gráfico. Qual fatia representa a maior fonte na matriz elétrica "
                    "ilustrada (mix didático de país com rios caudalosos)?"
                ),
                "visual": {
                    "type": "pie_chart",
                    "content": {
                        "title": "Matriz elétrica — país A (exemplo)",
                        "slices": [
                            {"label": "Hidrelétrica", "value": 58, "color": "#1d4ed8"},
                            {"label": "Biomassa e eólica", "value": 22, "color": "#15803d"},
                            {"label": "Gás natural", "value": 12, "color": "#b45309"},
                            {"label": "Carvão", "value": 8, "color": "#57534e"},
                        ],
                        "unit": "%",
                    },
                },
                "options": ["Biomassa e eólica", "Hidrelétrica", "Gás natural", "Carvão"],
                "correct_answer": 1,
                "explanation": "58% hidrelétrica — padrão próximo ao Brasil, diferente do mundo (~16% hidro).",
                "difficulty": "intermediate",
                "source_assets": sa("page-021.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo3-pe-012",
                "type": "multiple_choice",
                "topic": "hydrography_energy",
                "question": (
                    "Leia as afirmativas sobre matriz elétrica (dados do caderno):\n"
                    "I. No mundo, carvão mineral lidera a geração (~37% em 2020).\n"
                    "II. No Brasil, hidrelétrica supera 60% da capacidade.\n"
                    "III. No mundo, hidrelétrica é a fonte majoritária.\n"
                    "IV. Usinas hidrelétricas transformam energia mecânica das turbinas em elétrica.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "II e III", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. Mundialmente predomina fóssil, não hidro (III falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-041.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo3-pe-013",
                "type": "multiple_choice",
                "topic": "hydrography_energy",
                "question": "Observe o mapa. O estado em destaque (TO) integra principalmente a bacia:",
                "visual": {
                    "type": "brazil_map",
                    "content": {
                        "period": "post_1988",
                        "highlight": ["TO"],
                        "show_period_toggle": False,
                        "interactive": True,
                    },
                },
                "options": [
                    "Do rio São Francisco",
                    "Tocantins-Araguaia",
                    "Do rio Paraná apenas",
                    "Exclusivamente amazônica ocidental",
                ],
                "correct_answer": 1,
                "explanation": "Tocantins nasce em GO, passa por TO e deságua na Amazônia — bacia Tocantins-Araguaia.",
                "difficulty": "intermediate",
                "source_assets": sa("page-028.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo3-pe-014",
                "type": "multiple_choice",
                "topic": "water_pollution_aquifers",
                "question": (
                    "Segundo o caderno, o uso consuntivo de água que mais consome reservas de água doce globalmente é:"
                ),
                "options": [
                    "Navegação de cabotagem",
                    "Irrigação na agropecuária",
                    "Pesca esportiva",
                    "Turismo em cachoeiras",
                ],
                "correct_answer": 1,
                "explanation": "Agropecuária ~70% da água doce; irrigação é uso consuntivo — ANA / Módulo 13.",
                "difficulty": "basic",
                "source_assets": sa("page-051.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo3-pe-015",
                "type": "multiple_choice",
                "topic": "water_pollution_aquifers",
                "question": (
                    "Observe o gráfico de barras (pegada d'água ilustrativa — litros por unidade). "
                    "Qual item exige MAIS água em produção?"
                ),
                "visual": {
                    "type": "bar_chart",
                    "content": {
                        "title": "Água incorporada (exemplo didático)",
                        "unit": "L/unidade",
                        "bars": [
                            {"label": "Folha A4", "value": 10},
                            {"label": "Camisa algodão", "value": 2700},
                            {"label": "1 kg frango", "value": 3900},
                            {"label": "1 kg queijo", "value": 5500},
                        ],
                    },
                },
                "options": ["Folha A4", "Camisa de algodão", "1 kg de queijo", "1 kg de frango"],
                "correct_answer": 2,
                "explanation": "Queijo (5.500 L) > frango > camisa > papel — ordem didática inspirada no infográfico p. 286.",
                "difficulty": "intermediate",
                "source_assets": sa("page-044.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo3-pe-016",
                "type": "multiple_choice",
                "topic": "water_pollution_aquifers",
                "question": (
                    "Comparando SAGA e Aquífero Guarani:\n"
                    "I. SAGA tem maior extensão dentro do Brasil.\n"
                    "II. Guarani se estende a Argentina, Paraguai e Uruguai.\n"
                    "III. Guarani possui maior volume que SAGA.\n"
                    "IV. Ambos são reservatórios subterrâneos de água doce.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. SAGA ~162 mil km³ vs Guarani ~39 mil km³ (III falsa).",
                "difficulty": "advanced",
                "source_assets": sa("page-011.jpg"),
                "section": "final_quiz",
            },
        ],
    }
