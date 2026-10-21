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
                            "description": "Mapas clicáveis: evolução histórica, regiões, capitais e novos estados.",
                            "tip": "Use o modo Regiões para localizar biomas enquanto revisa vegetação.",
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
    """Mapas interativos consolidados na aba dedicada."""
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Regiões e biomas do Brasil"}},
        {
            "type": "brazil_map",
            "content": {
                "title": "Mapa político por regiões",
                "intro": "Localize Norte, Nordeste, Centro-Oeste, Sudeste e Sul — útil para climas e vegetação.",
                "period": "post_1988",
                "mode": "regions",
                "show_period_toggle": False,
                "show_mode_toggle": True,
                "highlight": [],
                "interactive": True,
                "caption": "Amazônia no Norte; Caatinga no Nordeste; Cerrado no Centro-Oeste.",
                "aria_label": "Mapa do Brasil por regiões",
            },
            "sources": [_src("page-006.jpg"), _src("page-007.jpg")],
        },
        {"type": "heading", "content": {"level": 3, "text": "2. Capitais — Equador e Trópico de Capricórnio"}},
        {
            "type": "brazil_map",
            "content": {
                "title": "Capitais estaduais",
                "mode": "capitals",
                "show_period_toggle": False,
                "show_mode_toggle": False,
                "interactive": True,
                "caption": "Macapá (AP) é a única capital cortada pela linha do Equador.",
                "aria_label": "Mapa do Brasil com capitais",
            },
            "sources": [_src("page-029.jpg"), _src("page-028.jpg")],
        },
        {"type": "heading", "content": {"level": 3, "text": "3. Sul do Brasil — zona temperada"}},
        {
            "type": "brazil_map",
            "content": {
                "title": "Estados ao sul do Trópico de Capricórnio",
                "mode": "regions",
                "period": "post_1988",
                "show_period_toggle": False,
                "show_mode_toggle": False,
                "highlight": ["RS", "SC", "PR"],
                "interactive": True,
                "caption": "RS, SC e PR têm invernos mais frios — clima subtropical.",
                "aria_label": "Região Sul em destaque",
            },
            "sources": [_src("page-022.jpg"), _src("page-023.jpg")],
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
                    "title": "Explore o Brasil no mapa",
                    "text": "Explore regiões, capitais e estados citados nos mapas do caderno. "
                    "Tudo offline — clique nos estados para ver nomes.",
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
                    "Quando acertar, o estado fica verde. Complete todos os 27!",
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
                "text": "Na aba Mapas interativos você explora regiões e capitais enquanto fixa "
                "onde passam Equador e Trópico de Capricórnio no Brasil.",
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
                "question": "A capital brasileira cortada pela linha do Equador é:",
                "options": ["Belém", "Macapá", "Manaus", "Boa Vista"],
                "correct_answer": 1,
                "explanation": "Macapá (AP) tem o Marco Zero do Equador.",
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
                    "Observe o mapa. Os estados em destaque no Sul têm, em geral, "
                    "clima subtropical e invernos mais frios."
                ),
                "visual": {
                    "type": "brazil_map",
                    "content": {
                        "period": "post_1988",
                        "show_period_toggle": False,
                        "highlight": ["RS", "SC", "PR"],
                        "interactive": True,
                        "aria_label": "Região Sul em destaque",
                    },
                },
                "options": [
                    "Região Norte (AM, PA, RR)",
                    "Região Sul (PR, SC, RS)",
                    "Apenas o Distrito Federal",
                    "Todo o Nordeste",
                ],
                "correct_answer": 1,
                "explanation": "PR, SC e RS ficam ao sul do Trópico de Capricórnio.",
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
