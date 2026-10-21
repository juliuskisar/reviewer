"""Conteúdo pedagógico da revisão Benjamin — Geografia PE 3º trimestre (Módulos 10–11)."""

from __future__ import annotations

REVIEW_ID = "benjamin-pe-geografia-3tri"
ASSET_PREFIX = "assets/benjamin_pe_geografia_3_tri"


def _src(page: str) -> dict:
    return {
        "asset": f"{ASSET_PREFIX}/{page}",
        "origin_type": "observed",
        "evidence": [f"Caderno de Geografia — {page}"],
    }


def build_content() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Geografia — PE 3º Trimestre",
        "subtitle": "Benjamin · 4º ano · Módulos 10 e 11",
        "language": "pt-BR",
        "discipline": "Geografia",
        "grade": "4º ano",
        "metadata": {
            "student_name": "Benjamin",
            "exam_type": "Prova Específica (PE)",
            "estimated_duration_minutes": 55,
        },
        "study_route": [
            {"order": 1, "title": "Explicações", "section_id": "explain"},
            {"order": 2, "title": "Resumo rápido", "section_id": "summary"},
            {"order": 3, "title": "Mapas interativos", "section_id": "maps"},
            {"order": 4, "title": "Jogo dos climas", "section_id": "climate_game"},
            {"order": 5, "title": "Jogos de revisão", "section_id": "study_games"},
            {"order": 6, "title": "Jogo das capitais", "section_id": "capital_game"},
            {"order": 7, "title": "Exercícios", "section_id": "exercises"},
        ],
        "sections": [
            _section_route(),
            _section_explain(),
            _section_summary(),
            _section_interactive_maps(),
            _section_climate_game(),
            _section_study_games(),
            _section_capital_game(),
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
                    "text": "Linhas imaginárias e zonas térmicas, incidência solar, Brasil tropical, "
                    "climas e vegetação, relevo brasileiro e preservação ambiental — Módulos 10 e 11. "
                    "Reserve cerca de 55 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🌐", "title": "Linhas imaginárias", "text": "Equador · trópicos · meridianos"},
                        {"icon": "☀️", "title": "Zonas térmicas", "text": "Intertropical · temperada · polar"},
                        {"icon": "🇧🇷", "title": "Brasil tropical", "text": "Capricórnio · Sul mais frio"},
                        {"icon": "🌦️", "title": "Climas", "text": "Equatorial · tropical · subtropical"},
                        {"icon": "🌳", "title": "Vegetação", "text": "Biomas · formações originais"},
                        {"icon": "⛰️", "title": "Relevo", "text": "Planaltos · planícies · depressões"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 10 — Linhas imaginárias e incidência solar",
                        "Módulo 10 — Zonas térmicas e Brasil tropical",
                        "Módulo 11 — Relevo e paisagens do Brasil",
                        "Módulo 11 — Climas e vegetação",
                        "Módulo 11 — Desmatamento e cuidado ambiental",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Leia os cards e tabelas com calma.",
                            "tip": "Relacione Equador e Trópico de Capricórnio com calor e frio no Brasil.",
                        },
                        {
                            "title": "Revise o Resumo rápido",
                            "panel": "summary",
                            "panel_label": "Resumo rápido",
                            "description": "Percorra os blocos-síntese — use como mapa mental para a PE.",
                        },
                        {
                            "title": "Explore os Mapas interativos",
                            "panel": "maps",
                            "panel_label": "Mapas interativos",
                            "description": "Os mapas da apostila, clicáveis: Equador e Trópico sobre o Brasil, "
                            "globo das zonas térmicas, climas e vegetação por estado.",
                            "tip": "No globo, use o modo Pintar — é a mesma atividade da página 174.",
                        },
                        {
                            "title": "Jogue o Jogo dos climas",
                            "panel": "climate_game",
                            "panel_label": "Jogo dos climas",
                            "description": "O jogo sorteia um estado; você escolhe o clima que predomina nele até pintar o mapa inteiro.",
                            "tip": "Pense primeiro na região: Norte, Nordeste, Centro-Oeste, Sudeste ou Sul.",
                        },
                        {
                            "title": "Faça os Jogos de revisão",
                            "panel": "study_games",
                            "panel_label": "Jogos de revisão",
                            "description": "Classifique lugares nas zonas térmicas e associe formas de relevo às definições.",
                        },
                        {
                            "title": "Jogue o Jogo das capitais",
                            "panel": "capital_game",
                            "panel_label": "Jogo das capitais",
                            "description": "Clique em cada estado e digite a capital. Complete o mapa inteiro!",
                            "tip": "Estados corretos ficam verdes. Veja seu tempo no final.",
                        },
                        {
                            "title": "Faça os Exercícios",
                            "panel": "exercises",
                            "panel_label": "Exercícios",
                            "description": "Questões no estilo Teste e Atividade do caderno.",
                            "tip": "Responda primeiro; só depois clique em Verificar.",
                        },
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "info",
                    "title": "Como navegar:",
                    "text": "Cada passo tem um botão que leva à aba correspondente. "
                    "Você também pode usar as abas no topo.",
                },
            },
        ],
    }


def _interactive_map_blocks() -> list:
    """Um mapa por tema da apostila (Módulos 10–11) — sem repetir nas explicações."""
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Linhas imaginárias sobre o Brasil (p. 173 e 180)"}},
        {
            "type": "paragraph",
            "content": {
                "text": "Na apostila você traçou a linha do Equador e o Trópico de Capricórnio no mapa "
                "político e pintou as zonas. Aqui as duas linhas aparecem sobre os estados: "
                "clique em um estado para saber se ele é cortado por uma linha e em que zona térmica fica.",
            },
        },
        {
            "type": "brazil_map",
            "content": {
                "title": "Equador e Trópico de Capricórnio",
                "intro": "Vermelho: estados ao norte do Trópico (zona intertropical). "
                "Amarelo: estados ao sul do Trópico (zona temperada Sul). Os tons mais fortes marcam os estados cortados pelas linhas.",
                "period": "post_1988",
                "mode": "imaginary_lines",
                "show_period_toggle": False,
                "show_mode_toggle": False,
                "highlight": [],
                "interactive": True,
                "caption": "O Equador corta AP, AM, PA e RR — Macapá fica exatamente na linha. "
                "O Trópico de Capricórnio corta MS, SP e PR; SC e RS ficam inteiros na zona temperada.",
                "aria_label": "Mapa do Brasil com Equador e Trópico de Capricórnio",
            },
            "sources": [_src("page-022.jpg"), _src("page-016.jpg"), _src("page-028.jpg")],
        },
        {"type": "heading", "content": {"level": 3, "text": "2. Zonas térmicas no globo (p. 170 e 174)"}},
        {
            "type": "paragraph",
            "content": {
                "text": "Igual à atividade do caderno: o globo tem os cinco paralelos principais e três zonas "
                "térmicas. No modo Explorar, clique em uma faixa ou linha para ler como os raios do Sol chegam. "
                "No modo Pintar, escolha a cor certa para cada faixa e clique em Verificar.",
            },
        },
        {
            "type": "thermal_globe",
            "content": {
                "globe_id": "zonas",
                "title": "Globo terrestre — zonas térmicas",
                "mode": "explore",
                "show_mode_toggle": True,
                "caption": "Lembre: vermelho entre os trópicos (zona intertropical), amarelo entre trópico e círculo polar "
                "(zona temperada), cinza além dos círculos polares (zona polar).",
                "aria_label": "Globo terrestre com zonas térmicas",
            },
            "sources": [_src("page-023.jpg"), _src("page-027.jpg"), _src("page-021.jpg")],
        },
        {"type": "heading", "content": {"level": 3, "text": "3. Climas do Brasil (p. 190 e 196)"}},
        {
            "type": "paragraph",
            "content": {
                "text": "O mapa Climas do Brasil da apostila tem seis climas. Aqui cada estado recebe a cor do "
                "clima que predomina nele — clique para ver a característica e os outros climas que também ocorrem no estado.",
            },
        },
        {
            "type": "brazil_map",
            "content": {
                "title": "Clima predominante por estado",
                "intro": "Quatro dos seis climas são «tropicais»: o Brasil está quase todo na zona intertropical.",
                "period": "post_1988",
                "mode": "climates",
                "show_period_toggle": False,
                "show_mode_toggle": False,
                "interactive": True,
                "caption": "Equatorial no Norte; semiárido no interior do Nordeste; subtropical ao sul do Trópico de Capricórnio.",
                "aria_label": "Mapa do Brasil por clima predominante",
            },
            "sources": [_src("page-007.jpg"), _src("page-002.jpg")],
        },
        {"type": "heading", "content": {"level": 3, "text": "4. Vegetação original do Brasil (p. 192 e 193)"}},
        {
            "type": "paragraph",
            "content": {
                "text": "O mapa de formações vegetais originais mostra nove tipos. Compare com o mapa de climas: "
                "onde é quente e úmido há floresta; onde é seco há Caatinga; nos planaltos frios do Sul, araucárias.",
            },
        },
        {
            "type": "brazil_map",
            "content": {
                "title": "Formação vegetal predominante por estado",
                "intro": "Clique em um estado para ver a formação predominante e as outras que também aparecem nele.",
                "period": "post_1988",
                "mode": "vegetation",
                "show_period_toggle": False,
                "show_mode_toggle": False,
                "interactive": True,
                "caption": "Clima, relevo, solo e água explicam a vegetação de cada lugar.",
                "aria_label": "Mapa do Brasil por formação vegetal original",
            },
            "sources": [_src("page-006.jpg"), _src("page-014.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "info",
                "title": "Relevo e desmatamento:",
                "text": "Os mapas de relevo (p. 187) e de vegetação nativa em 2015 (p. 194) não seguem as divisas "
                "dos estados, por isso ficam nas Explicações em cards e tabela — não em mapa aproximado.",
            },
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
                    "title": "Os mapas da apostila, clicáveis",
                    "text": "Quatro representações dos Módulos 10 e 11: linhas imaginárias, globo das zonas "
                    "térmicas, climas e vegetação. Tudo offline — clique nos estados e nas faixas para explorar.",
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
                    "text": "Clique em um estado — você verá só o nome do estado. "
                    "Digite a capital no campo e clique em Confirmar. "
                    "Quando acertar, o estado fica verde. Complete todos os 27! "
                    "Dica do módulo: Macapá fica na linha do Equador e São Paulo, perto do Trópico de Capricórnio.",
                },
            },
        ],
    }


def _section_climate_game() -> dict:
    return {
        "id": "climate_game",
        "type": "map_theme_game",
        "title": "Jogo dos climas",
        "theme": "climates",
        "question_prefix": "Qual clima predomina em",
        "blocks": [
            {
                "type": "panel_intro",
                "content": {
                    "title": "Pinte o mapa de climas!",
                    "text": "O jogo sorteia um estado (em azul). Escolha o clima que predomina nele. "
                    "Acertou? O estado ganha a cor do clima — como no mapa Climas do Brasil da apostila. "
                    "Complete os 27 estados e veja seu tempo.",
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pistas:",
                    "text": "Norte = Equatorial · interior do Nordeste = Tropical semiárido · "
                    "Centro-Oeste e boa parte do Sudeste = Tropical · litoral do ES e RJ = Tropical litorâneo · "
                    "Sul = Subtropical.",
                },
            },
        ],
    }


def _section_study_games() -> dict:
    return {
        "id": "study_games",
        "type": "study_game",
        "title": "Jogos de revisão",
        "blocks": [
            {
                "type": "panel_intro",
                "content": {
                    "title": "Dois jogos rápidos",
                    "text": "Classifique lugares nas zonas térmicas e associe cada forma de relevo à sua definição. "
                    "Clique em um item e depois no destino.",
                },
            },
            {
                "type": "study_game",
                "content": {
                    "game_id": "zonas-termicas",
                    "mode": "sort_buckets",
                    "title": "Jogo 1 — Em que zona térmica fica?",
                    "instructions": "Clique em um lugar ou característica e depois na zona térmica correta.",
                    "pool_title": "Lugares e pistas",
                    "buckets": [
                        {"id": "intertropical", "label": "Zona intertropical", "hint": "Entre os trópicos — raios perpendiculares"},
                        {"id": "temperate", "label": "Zona temperada", "hint": "Entre trópico e círculo polar — raios inclinados"},
                        {"id": "polar", "label": "Zona polar", "hint": "Além dos círculos polares — muito frio"},
                    ],
                    "sort_items": [
                        {"id": "z1", "text": "Macapá, na linha do Equador", "answer": "intertropical"},
                        {"id": "z2", "text": "Santa Catarina e Rio Grande do Sul", "answer": "temperate"},
                        {"id": "z3", "text": "Lugar onde nevou em Urupema (SC)", "answer": "temperate"},
                        {"id": "z4", "text": "Região onde o Sol some por dois meses do ano", "answer": "polar"},
                        {"id": "z5", "text": "Floresta Amazônica, quente o ano todo", "answer": "intertropical"},
                        {"id": "z6", "text": "Terra dos pinguins e dos iglus", "answer": "polar"},
                        {"id": "z7", "text": "Raios solares caem bem perpendiculares (90°)", "answer": "intertropical"},
                        {"id": "z8", "text": "Quatro estações bem definidas", "answer": "temperate"},
                        {"id": "z9", "text": "Praia de Porto de Galinhas (PE), calor o ano inteiro", "answer": "intertropical"},
                    ],
                },
                "sources": [_src("page-024.jpg"), _src("page-023.jpg"), _src("page-027.jpg")],
            },
            {
                "type": "study_game",
                "content": {
                    "game_id": "relevo",
                    "mode": "match_pairs",
                    "title": "Jogo 2 — Formas de relevo",
                    "instructions": "Clique em uma forma de relevo e depois na definição que combina com ela.",
                    "left_title": "Forma de relevo",
                    "right_title": "Definição",
                    "left": [
                        {"id": "r1", "text": "Planalto"},
                        {"id": "r2", "text": "Planície"},
                        {"id": "r3", "text": "Depressão"},
                        {"id": "r4", "text": "Chapada"},
                        {"id": "r5", "text": "Serra"},
                        {"id": "r6", "text": "Escarpa"},
                    ],
                    "right": [
                        {"id": "d3", "text": "Superfície mais baixa que as áreas vizinhas"},
                        {"id": "d1", "text": "Superfície acima de 300 m, plana ou ondulada, com bordas íngremes"},
                        {"id": "d5", "text": "Relevo acidentado, com picos e desníveis"},
                        {"id": "d2", "text": "Superfície plana e baixa (até cerca de 100 m)"},
                        {"id": "d6", "text": "Borda ou descida íngreme do planalto"},
                        {"id": "d4", "text": "Área elevada de topo plano e grande extensão, sobre o planalto"},
                    ],
                    "answers": {"r1": "d1", "r2": "d2", "r3": "d3", "r4": "d4", "r5": "d5", "r6": "d6"},
                },
                "sources": [_src("page-009.jpg")],
            },
        ],
    }


def _section_explain() -> dict:
    return {
        "id": "explain",
        "type": "explanations",
        "title": "Explicações",
        "blocks": [
            *_topic_imaginary_lines(),
            *_topic_thermal_zones(),
            *_topic_brazil_tropical(),
            *_topic_brazil_climates(),
            *_topic_relief(),
            *_topic_vegetation(),
            *_topic_deforestation(),
            *_topic_environment(),
        ],
    }


def _topic_imaginary_lines() -> list:
    tid = "imaginary_lines"
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Linhas imaginárias nos mapas"}, "topic_id": tid},
        {
            "type": "paragraph",
            "content": {
                "text": "Cartógrafos traçam linhas que não existem na natureza — paralelos (horizontais) "
                "e meridianos (verticais, do polo Norte ao polo Sul). Elas ajudam a localizar lugares "
                "e ler mapas como o da América do Sul.",
            },
            "topic_id": tid,
            "sources": [_src("page-032.jpg"), _src("page-033.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "➖", "title": "Equador", "text": "Paralelo 0° — divide Norte e Sul"},
                    {"icon": "🧭", "title": "Meridiano de Greenwich", "text": "Meridiano 0° — divide Leste e Oeste"},
                    {"icon": "🌴", "title": "Trópicos", "text": "Câncer (N) e Capricórnio (S)"},
                    {"icon": "❄️", "title": "Círculos polares", "text": "Ártico e Antártico"},
                ],
            },
            "topic_id": tid,
        },
        {
            "type": "callout",
            "content": {
                "variant": "info",
                "title": "Mapas interativos",
                "text": "Na aba Mapas interativos, o primeiro mapa mostra o Equador e o Trópico de "
                "Capricórnio desenhados sobre o Brasil; o globo mostra as zonas térmicas.",
            },
            "topic_id": tid,
        },
    ]


def _topic_thermal_zones() -> list:
    tid = "thermal_zones"
    return [
        {"type": "heading", "content": {"level": 3, "text": "2. Incidência solar e zonas térmicas"}, "topic_id": tid},
        {
            "type": "paragraph",
            "content": {
                "text": "A Terra é arredondada: perto do Equador os raios solares incidem de forma "
                "mais perpendicular (concentram calor). Longe do Equador a incidência é inclinada — "
                "a luz se dispersa e esquenta menos. Trópicos e círculos polares delimitam três "
                "zonas térmicas: intertropical (quente), temperada (média) e polar (fria).",
            },
            "topic_id": tid,
            "sources": [_src("page-026.jpg"), _src("page-025.jpg"), _src("page-027.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Zona", "Onde fica", "Calor e luz"],
                "rows": [
                    ["Intertropical", "Entre os trópicos", "Raios mais perpendiculares — mais quente"],
                    ["Temperada N e S", "Entre trópicos e círculos polares", "Raios inclinados — temperaturas médias"],
                    ["Polar N e S", "Além dos círculos polares", "Raios muito inclinados — muito frio"],
                ],
            },
            "topic_id": tid,
        },
    ]


def _topic_brazil_tropical() -> list:
    tid = "brazil_tropical"
    return [
        {"type": "heading", "content": {"level": 3, "text": "3. Moro num país (quase todo) tropical"}, "topic_id": tid},
        {
            "type": "paragraph",
            "content": {
                "text": "A maior parte do Brasil está ao norte do Trópico de Capricórnio, na zona "
                "intertropical — por isso predomina calor ao longo do ano. Só uma faixa ao sul "
                "do trópico (partes de MS, SP, PR e os estados SC e RS) está na zona temperada Sul, "
                "com invernos mais frios, inclusive neve em serras catarinenses.",
            },
            "topic_id": tid,
            "sources": [_src("page-024.jpg"), _src("page-022.jpg"), _src("page-023.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "📍", "title": "Equador no BR", "text": "Corta AP, AM, PA e RR — Macapá na linha"},
                    {"icon": "📍", "title": "Capricórnio", "text": "Corta MS, SP, PR, SC e RS"},
                    {"icon": "🌡️", "title": "Mais quente", "text": "Norte e centro — incidência perpendicular"},
                    {"icon": "🧥", "title": "Mais frio", "text": "Sul — incidência inclinada no inverno"},
                ],
            },
            "topic_id": tid,
            "sources": [_src("page-016.jpg"), _src("page-029.jpg")],
        },
    ]


def _topic_brazil_climates() -> list:
    tid = "brazil_climates"
    return [
        {"type": "heading", "content": {"level": 3, "text": "4. Os climas do Brasil"}, "topic_id": tid},
        {
            "type": "paragraph",
            "content": {
                "text": "No mapa de climas aparecem seis tipos. Quatro têm a palavra «tropical» no nome "
                "porque o Brasil está na zona intertropical. Cada tipo combina temperatura e chuvas "
                "de um jeito diferente.",
            },
            "topic_id": tid,
            "sources": [_src("page-007.jpg"), _src("page-002.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Resumo dos climas (caderno)",
                "headers": ["Clima", "Característica principal", "Onde ocorre"],
                "rows": [
                    ["Equatorial", "Quente e úmido o ano todo", "Amazônia, norte de MT e MA"],
                    ["Tropical", "Quente; chuvas no verão", "Nordeste, Sudeste, Centro-Oeste"],
                    ["Tropical litorâneo", "Quente e mais úmido (ventos do mar)", "Faixa litorânea"],
                    ["Tropical semiárido", "Pouca chuva; secas longas", "Interior do Nordeste"],
                    ["Tropical de altitude", "Inverno mais frio em áreas altas", "Serras do Sudeste e norte do PR"],
                    ["Subtropical", "Quatro estações; inverno frio", "Sul do Capricórnio — RS, SC, PR, sul de SP"],
                ],
            },
            "topic_id": tid,
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Diferença importante:",
                "text": "Tropical semiárido tem menos chuva que o tropical comum. Subtropical é o "
                "único com inverno realmente frio no Brasil.",
            },
            "topic_id": tid,
            "sources": [_src("page-005.jpg")],
        },
    ]


def _topic_relief() -> list:
    tid = "relief_forms"
    return [
        {"type": "heading", "content": {"level": 3, "text": "5. Relevo e paisagens do Brasil"}, "topic_id": tid},
        {
            "type": "paragraph",
            "content": {
                "text": "Relevo é o conjunto das formas da superfície terrestre — planas, onduladas, "
                "altas ou baixas. Forças internas (terremotos, movimentos no interior) e externas "
                "(chuva, vento, rios) modelam o relevo. No Brasil predominam planaltos e depressões; "
                "não há montanhas muito altas.",
            },
            "topic_id": tid,
            "sources": [_src("page-011.jpg"), _src("page-010.jpg"), _src("page-008.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🏔️", "title": "Planalto", "text": "Acima de 300 m — pode ter chapada e serra"},
                    {"icon": "🏖️", "title": "Planície", "text": "Baixa altitude (até ~100 m)"},
                    {"icon": "🕳️", "title": "Depressão", "text": "Área mais baixa que a vizinhança"},
                    {"icon": "⛰️", "title": "Serra / escarpa", "text": "Picos e bordas íngremes do planalto"},
                ],
            },
            "topic_id": tid,
            "sources": [_src("page-009.jpg")],
        },
    ]


def _topic_vegetation() -> list:
    tid = "vegetation_biomes"
    return [
        {"type": "heading", "content": {"level": 3, "text": "6. Vegetação original do Brasil"}, "topic_id": tid},
        {
            "type": "paragraph",
            "content": {
                "text": "Clima, relevo, solo e água determinam a vegetação. O mapa de formações "
                "originais mostra floresta Amazônica, Mata Atlântica, Cerrado, Caatinga, Pantanal, "
                "campos, cocais, araucárias e vegetação litorânea — cada uma ligada a condições "
                "ambientais diferentes.",
            },
            "topic_id": tid,
            "sources": [_src("page-006.jpg"), _src("page-014.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🌳", "title": "Amazônia", "text": "Floresta densa e úmida"},
                    {"icon": "🌵", "title": "Caatinga", "text": "Semiárido — cactos e arbustos"},
                    {"icon": "🌾", "title": "Cerrado", "text": "Savana brasileira — estação seca"},
                    {"icon": "🌊", "title": "Pantanal", "text": "Planície alagável — grande biodiversidade"},
                ],
            },
            "topic_id": tid,
        },
    ]


def _topic_deforestation() -> list:
    tid = "deforestation"
    return [
        {"type": "heading", "content": {"level": 3, "text": "7. Desmatamento da vegetação nativa"}, "topic_id": tid},
        {
            "type": "paragraph",
            "content": {
                "text": "Mapas comparativos mostram que grande parte da vegetação original foi "
                "substituída por áreas desmatadas (pastagens, lavouras, cidades). Isso acontece "
                "há décadas e continua — especialmente na Mata Atlântica, Cerrado e bordas da Amazônia.",
            },
            "topic_id": tid,
            "sources": [_src("page-004.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "warning",
                "title": "Consequências:",
                "text": "Perda de habitat, erosão, rios poluídos ou assoreados e menos biodiversidade. "
                "Preservar matas e plantar árvores ajuda a equilibrar o ambiente.",
            },
            "topic_id": tid,
        },
    ]


def _topic_environment() -> list:
    tid = "environment_care"
    return [
        {"type": "heading", "content": {"level": 3, "text": "8. Observar e cuidar da natureza"}, "topic_id": tid},
        {
            "type": "paragraph",
            "content": {
                "text": "Relevo, clima e vegetação aparecem no dia a dia — nas árvores da rua, no tempo "
                "do ano, nas enchentes ou rios sujos. Pequenas ações contam: plantar árvores, não "
                "jogar lixo, economizar água. A frase de Wangari Maathai lembra que «são as pequenas "
                "coisas que os cidadãos fazem» que fazem diferença.",
            },
            "topic_id": tid,
            "sources": [_src("page-001.jpg"), _src("page-003.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Projeto Estado:",
                "text": "Continue pesquisando o relevo, clima e vegetação do seu estado no Anexo 5.",
            },
            "topic_id": tid,
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
                    "text": "Revise cada tópico — cards e tabelas com o essencial dos Módulos 10 e 11.",
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "1. Linhas imaginárias"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "➖", "title": "Paralelos", "text": "Equador · trópicos · polares"},
                        {"icon": "🧭", "title": "Meridianos", "text": "Greenwich = 0° · Leste/Oeste"},
                        {"icon": "🗺️", "title": "Mapa", "text": "Fronteiras · oceanos · rosa dos ventos"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. Zonas térmicas"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["Zona", "Calor"],
                    "rows": [
                        ["Intertropical", "Mais quente — raios perpendiculares"],
                        ["Temperada", "Médio — raios inclinados"],
                        ["Polar", "Muito frio"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Brasil tropical"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "☀️", "title": "Maior parte", "text": "Zona intertropical"},
                        {"icon": "🧊", "title": "Sul", "text": "Abaixo do Capricórnio — mais frio"},
                        {"icon": "🏟️", "title": "Macapá", "text": "Capital na linha do Equador"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Climas"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["Clima", "Marca"],
                    "rows": [
                        ["Equatorial", "Úmido o ano todo"],
                        ["Tropical semiárido", "Pouca chuva — seca"],
                        ["Subtropical", "Quatro estações — Sul"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Relevo"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "📐", "title": "Definição", "text": "Formas da superfície terrestre"},
                        {"icon": "🏔️", "title": "Predominam", "text": "Planaltos e depressões"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "6. Vegetação"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🌳", "title": "Amazônia", "text": "Norte"},
                        {"icon": "🌵", "title": "Caatinga", "text": "Semiárido NE"},
                        {"icon": "🌾", "title": "Cerrado", "text": "Centro"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "7. Desmatamento"}},
            {
                "type": "paragraph",
                "content": {
                    "text": "Vermelho no mapa = áreas desmatadas; verde = vegetação original restante. "
                    "Proteger florestas evita erosão e perda de espécies.",
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "Brasil está nos hemisférios Ocidental e Sul — mas uma pequena parte "
                    "fica ao norte do Equador (hemisfério Norte).",
                },
            },
        ],
    }


def build_exercises() -> dict:
    def sa(page: str) -> list[str]:
        return [f"{ASSET_PREFIX}/{page}"]

    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "exercises": [
            {
                "id": "bg3-pe-001",
                "type": "multiple_choice",
                "topic": "imaginary_lines",
                "question": "As linhas traçadas horizontalmente e verticalmente nos mapas são chamadas de:",
                "options": [
                    "Fronteiras e divisas",
                    "Paralelos e meridianos",
                    "Biomas e bacias",
                    "Planaltos e planícies",
                ],
                "correct_answer": 1,
                "explanation": "Paralelos (como o Equador) e meridianos (como Greenwich) são linhas imaginárias.",
                "difficulty": "basic",
                "source_assets": sa("page-032.jpg"),
                "section": "exercises",
            },
            {
                "id": "bg3-pe-002",
                "type": "multiple_choice",
                "topic": "imaginary_lines",
                "question": (
                    "Leia as afirmativas:\n"
                    "I. O meridiano de Greenwich é o meridiano 0°.\n"
                    "II. Ele divide o globo em hemisfério Oriental e Ocidental.\n"
                    "III. O Equador divide Leste e Oeste.\n"
                    "IV. Paralelos são traçados paralelamente ao Equador.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e IV", "II, III e IV", "I e III", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "Equador divide Norte e Sul, não Leste/Oeste (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-019.jpg"),
                "section": "exercises",
            },
            {
                "id": "bg3-pe-003",
                "type": "multiple_choice",
                "topic": "imaginary_lines",
                "question": (
                    "Observe o mapa: a linha tracejada ao norte é a linha do Equador e o estado "
                    "destacado é o Amapá. A capital brasileira cortada pela linha do Equador é:"
                ),
                "visual": {
                    "type": "brazil_map",
                    "content": {
                        "period": "post_1988",
                        "mode": "imaginary_lines",
                        "show_period_toggle": False,
                        "show_mode_toggle": False,
                        "highlight": ["AP"],
                        "interactive": True,
                        "aria_label": "Mapa com a linha do Equador e o Amapá destacado",
                    },
                },
                "options": ["Belém", "Macapá", "Manaus", "Boa Vista"],
                "correct_answer": 1,
                "explanation": "Macapá (AP) tem o Marco Zero do Equador e o estádio Zerão, com um time em cada hemisfério.",
                "difficulty": "basic",
                "source_assets": sa("page-029.jpg"),
                "section": "exercises",
            },
            {
                "id": "bg3-pe-004",
                "type": "multiple_choice",
                "topic": "thermal_zones",
                "question": "Na zona intertropical, os raios solares incidem de forma:",
                "options": [
                    "Muito inclinada, esfriando o ar",
                    "Perpendicular, concentrando calor",
                    "Apenas à noite",
                    "Igual aos polos",
                ],
                "correct_answer": 1,
                "explanation": "Incidência perpendicular perto do Equador — zona mais quente.",
                "difficulty": "basic",
                "source_assets": sa("page-026.jpg"),
                "section": "exercises",
            },
            {
                "id": "bg3-pe-005",
                "type": "multiple_choice",
                "topic": "thermal_zones",
                "question": (
                    "Sobre zonas térmicas:\n"
                    "I. Entre os trópicos fica a zona intertropical.\n"
                    "II. Zonas polares recebem raios muito inclinados.\n"
                    "III. Zona temperada é a mais quente do planeta.\n"
                    "IV. Trópicos limitam onde o Sol pode incidir perpendicularmente.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "Intertropical é a mais quente (III errada). I, II e IV corretas.",
                "difficulty": "intermediate",
                "source_assets": sa("page-025.jpg"),
                "section": "exercises",
            },
            {
                "id": "bg3-pe-006",
                "type": "multiple_choice",
                "topic": "brazil_tropical",
                "question": (
                    "Observe o mapa com as duas linhas imaginárias. A linha tracejada mais ao sul "
                    "é o Trópico de Capricórnio. Quais estados ficam INTEIRAMENTE ao sul dela, "
                    "na zona temperada Sul?"
                ),
                "visual": {
                    "type": "brazil_map",
                    "content": {
                        "period": "post_1988",
                        "mode": "imaginary_lines",
                        "show_period_toggle": False,
                        "show_mode_toggle": False,
                        "highlight": ["RS", "SC"],
                        "interactive": True,
                        "aria_label": "Mapa com Equador e Trópico de Capricórnio; SC e RS destacados",
                    },
                },
                "options": [
                    "Amazonas e Pará",
                    "Santa Catarina e Rio Grande do Sul",
                    "São Paulo e Minas Gerais",
                    "Bahia e Sergipe",
                ],
                "correct_answer": 1,
                "explanation": "O Trópico corta MS, SP e PR; só SC e RS ficam inteiros ao sul dele — por isso têm o inverno mais frio.",
                "difficulty": "intermediate",
                "source_assets": sa("page-023.jpg"),
                "section": "exercises",
            },
            {
                "id": "bg3-pe-007",
                "type": "multiple_choice",
                "topic": "brazil_tropical",
                "question": "No Brasil, as temperaturas mais baixas no inverno ocorrem principalmente:",
                "options": [
                    "Na faixa equatorial amazonense",
                    "Na região Sul, longe do Equador",
                    "No litoral nordestino o ano inteiro",
                    "Apenas no estado do Amapá",
                ],
                "correct_answer": 1,
                "explanation": "O Sul é a porção mais distante do Equador — inverno mais frio.",
                "difficulty": "basic",
                "source_assets": sa("page-023.jpg"),
                "section": "exercises",
            },
            {
                "id": "bg3-pe-008",
                "type": "multiple_choice",
                "topic": "brazil_climates",
                "question": "O clima predominante em grande parte do norte do Brasil é:",
                "options": ["Subtropical", "Equatorial", "Polar", "Mediterrâneo"],
                "correct_answer": 1,
                "explanation": "Quente e úmido o ano todo — próximo ao Equador.",
                "difficulty": "basic",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "bg3-pe-009",
                "type": "multiple_choice",
                "topic": "brazil_climates",
                "question": "O clima tropical semiárido diferencia-se do tropical comum porque:",
                "options": [
                    "É mais frio o ano inteiro",
                    "Tem menos chuvas e períodos de seca",
                    "Só ocorre no Sul do Brasil",
                    "Não existe no Nordeste",
                ],
                "correct_answer": 1,
                "explanation": "Semiárido = pouca umidade; chuvas escassas (Caatinga).",
                "difficulty": "basic",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "bg3-pe-010",
                "type": "multiple_choice",
                "topic": "brazil_climates",
                "question": (
                    "Sobre climas brasileiros:\n"
                    "I. Vários tipos levam «tropical» no nome.\n"
                    "II. Subtropical ocorre ao sul do Trópico de Capricórnio.\n"
                    "III. Equatorial é quente e úmido.\n"
                    "IV. Tropical litorâneo é mais seco que o semiárido.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, II e III", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "Litorâneo é mais úmido (IV errada). I, II e III corretas.",
                "difficulty": "intermediate",
                "source_assets": sa("page-007.jpg"),
                "section": "exercises",
            },
            {
                "id": "bg3-pe-011",
                "type": "multiple_choice",
                "topic": "relief_forms",
                "question": "Relevo é o nome dado:",
                "options": [
                    "Somente a terremotos e vulcões",
                    "Ao conjunto das formas da superfície terrestre",
                    "Apenas às planícies costeiras",
                    "Exclusivamente ao clima de montanhas",
                ],
                "correct_answer": 1,
                "explanation": "Definição do caderno — formas altas, baixas, planas ou onduladas.",
                "difficulty": "basic",
                "source_assets": sa("page-011.jpg"),
                "section": "exercises",
            },
            {
                "id": "bg3-pe-012",
                "type": "multiple_choice",
                "topic": "relief_forms",
                "question": (
                    "Sobre relevo brasileiro:\n"
                    "I. Predominam planaltos e depressões.\n"
                    "II. Planícies são a forma mais comum em todo o país.\n"
                    "III. Planalto pode ter mais de 300 m de altitude.\n"
                    "IV. Escarpa é a borda íngreme do planalto.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I e III corretas. Planaltos e depressões predominam (II errada); escarpa existe (IV).",
                "difficulty": "intermediate",
                "source_assets": sa("page-008.jpg"),
                "section": "exercises",
            },
            {
                "id": "bg3-pe-013",
                "type": "multiple_choice",
                "topic": "vegetation_biomes",
                "question": "A Caatinga está associada principalmente ao clima:",
                "options": ["Equatorial úmido", "Tropical semiárido", "Subtropical com neve", "Polar"],
                "correct_answer": 1,
                "explanation": "Vegetação adaptada à seca do interior nordestino.",
                "difficulty": "basic",
                "source_assets": sa("page-014.jpg"),
                "section": "exercises",
            },
            {
                "id": "bg3-pe-014",
                "type": "multiple_choice",
                "topic": "deforestation",
                "question": "No mapa de vegetação nativa (2015), as áreas em vermelho indicam:",
                "options": [
                    "Floresta preservada",
                    "Áreas desmatadas",
                    "Somente rios",
                    "Capitais estaduais",
                ],
                "correct_answer": 1,
                "explanation": "Legenda: vermelho = desmatamento; verde = vegetação original.",
                "difficulty": "basic",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "bg3-pe-015",
                "type": "multiple_choice",
                "topic": "environment_care",
                "question": "Plantar árvores e cuidar de rios ajuda principalmente a:",
                "options": [
                    "Aumentar terremotos",
                    "Preservar o ambiente e a qualidade de vida",
                    "Eliminar todos os climas tropicais",
                    "Apagar fronteiras entre estados",
                ],
                "correct_answer": 1,
                "explanation": "Ações citadas no caderno com Wangari Maathai — preservação local.",
                "difficulty": "basic",
                "source_assets": sa("page-001.jpg"),
                "section": "final_quiz",
            },
            {
                "id": "bg3-pe-016",
                "type": "multiple_choice",
                "topic": "imaginary_lines",
                "question": (
                    "Sobre localização do Brasil:\n"
                    "I. O meridiano de Greenwich passa pelo território brasileiro.\n"
                    "II. Há território brasileiro ao norte da linha do Equador.\n"
                    "III. Todo o país está no hemisfério Oriental.\n"
                    "IV. O Trópico de Capricórnio atravessa estados do Sul e Sudeste.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, II e IV", "II, III e IV"],
                "correct_answer": 1,
                "explanation": "II e IV corretas. Greenwich não passa pelo BR (I); Brasil é Ocidental (III).",
                "difficulty": "intermediate",
                "source_assets": sa("page-017.jpg"),
                "section": "final_quiz",
            },
        ],
    }
