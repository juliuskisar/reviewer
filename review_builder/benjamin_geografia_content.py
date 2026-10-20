"""Conteúdo pedagógico da revisão Benjamin — Geografia PE 2º trimestre."""

from __future__ import annotations

REVIEW_ID = "benjamin-pe-geografia-2tri"
ASSET_PREFIX = "assets/benjamin_pe_geografia_2_tri"


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
        "title": "Revisão de Geografia — PE 2º Trimestre",
        "subtitle": "Benjamin · 4º ano · Módulo 6",
        "language": "pt-BR",
        "discipline": "Geografia",
        "grade": "4º ano",
        "metadata": {
            "student_name": "Benjamin",
            "exam_type": "Prova Específica (PE)",
            "estimated_duration_minutes": 50,
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
                    "text": "Bandeira do Brasil, estrelas e unidades federativas, mapas políticos "
                    "históricos, criação de novos estados, divisas e mapas físicos do Sudeste. "
                    "Reserve cerca de 50 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🇧🇷", "title": "Bandeira", "text": "Cores · estrelas · símbolos"},
                        {"icon": "⭐", "title": "Estrelas", "text": "27 UFs hoje · mudam com novos estados"},
                        {"icon": "🗺️", "title": "Mapa político", "text": "Divisas · evolução 1942–hoje"},
                        {"icon": "✂️", "title": "Novos estados", "text": "MT/MS · Goiás/Tocantins"},
                        {"icon": "🪨", "title": "Divisas", "text": "Marcos · propostas de divisão"},
                        {"icon": "🏔️", "title": "Mapa físico", "text": "Altitude · relevo · rios"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 6 — Bandeira e unidades federativas",
                        "Módulo 6 — Mapas políticos históricos",
                        "Módulo 6 — Criação de novos estados",
                        "Módulo 6 — Divisas e propostas",
                        "Módulo 6 — Mapas físicos",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Leia os cards e tabelas com calma.",
                            "tip": "Tente explicar por que a bandeira tem 27 estrelas hoje.",
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
                            "tip": "Alterne o período para ver Mato Grosso e Goiás antes das divisões.",
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
        {"type": "heading", "content": {"level": 3, "text": "1. Mapa completo — evolução, regiões e capitais"}},
        {
            "type": "brazil_map",
            "content": {
                "title": "Mapa político interativo",
                "intro": "Explore o Brasil de quatro formas: evolução histórica, regiões, capitais e novos estados.",
                "period": "post_1988",
                "mode": "evolution",
                "show_period_toggle": True,
                "show_mode_toggle": True,
                "highlight": [],
                "interactive": True,
                "caption": "No modo Evolução, alterne o período — Mato Grosso e Goiás aparecem maiores antes das divisões.",
                "aria_label": "Mapa político do Brasil interativo",
            },
            "sources": [_src("page-018.jpg")],
        },
        {"type": "heading", "content": {"level": 3, "text": "2. Estrelas da bandeira e capitais"}},
        {
            "type": "brazil_map",
            "content": {
                "title": "27 unidades federativas",
                "mode": "capitals",
                "show_period_toggle": False,
                "show_mode_toggle": False,
                "interactive": True,
                "caption": "Cada estrela na bandeira representa um estado ou o Distrito Federal.",
                "aria_label": "Mapa do Brasil com capitais",
            },
            "sources": [_src("page-014.jpg")],
        },
        {"type": "heading", "content": {"level": 3, "text": "3. Divisão de Mato Grosso (1977)"}},
        {
            "type": "brazil_map",
            "content": {
                "title": "Mato Grosso: antes e depois de 1977",
                "mode": "evolution",
                "period": "1942_1977",
                "show_period_toggle": True,
                "show_mode_toggle": False,
                "interactive": True,
                "caption": "Até 1977, Mato Grosso do Sul fazia parte de um único estado maior.",
                "aria_label": "Evolução do estado de Mato Grosso",
            },
            "sources": [_src("page-009.jpg")],
        },
        {"type": "heading", "content": {"level": 3, "text": "4. Divisão de Goiás e Tocantins (1988)"}},
        {
            "type": "brazil_map",
            "content": {
                "title": "Goiás antes de Tocantins",
                "mode": "evolution",
                "period": "1977_1988",
                "show_period_toggle": True,
                "show_mode_toggle": False,
                "interactive": True,
                "caption": "Até 1988, o norte de Goiás (hoje Tocantins) pertencia ao estado de Goiás.",
                "aria_label": "Evolução de Goiás e Tocantins",
            },
            "sources": [_src("page-002.jpg")],
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
                    "text": "Clique nos estados, alterne períodos históricos e teste os modos "
                    "de visualização. Os mesmos mapas usados nas explicações, reunidos aqui.",
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
            *_topic_flag(),
            *_topic_stars(),
            *_topic_political_maps(),
            *_topic_new_states(),
            *_topic_mato_grosso(),
            *_topic_goias_tocantins(),
            *_topic_borders_proposals(),
            *_topic_physical_maps(),
        ],
    }


def _topic_flag() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Nossa bandeira"}, "topic_id": "flag"},
        {
            "type": "paragraph",
            "content": {
                "text": "A bandeira é um símbolo nacional — uma imagem que representa o país. "
                "O Brasil adotou a bandeira atual em 19 de novembro de 1889, quatro dias após "
                "a Proclamação da República. Esse dia é o Dia da Bandeira.",
            },
            "topic_id": "flag",
            "sources": [_src("page-017.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🟢", "title": "Verde", "text": "Família real portuguesa; popularmente, as matas"},
                    {"icon": "🟡", "title": "Amarelo", "text": "Família de Leopoldina; popularmente, o ouro"},
                    {"icon": "🔵", "title": "Azul", "text": "Nossa Senhora; céu, rios e mares"},
                    {"icon": "⚪", "title": "Branco", "text": "Desejo de paz do povo brasileiro"},
                ],
            },
            "topic_id": "flag",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Símbolo:",
                "text": "Bandeiras de países aparecem em cerimônias e em lugares como a sede da ONU — "
                "cada uma representa um país diferente.",
            },
            "topic_id": "flag",
        },
    ]


def _topic_stars() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "2. Estrelas e unidades federativas"}, "topic_id": "stars"},
        {
            "type": "paragraph",
            "content": {
                "text": "Cada estrela na bandeira representa uma unidade federativa do Brasil — "
                "um estado ou o Distrito Federal. Quando um novo estado é criado, uma nova estrela "
                "é adicionada à bandeira.",
            },
            "topic_id": "stars",
            "sources": [_src("page-014.jpg"), _src("page-011.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Período", "Estrelas", "O que mudou"],
                "rows": [
                    ["1942 a 1977", "22 (sem Guanabara)", "Sem MS e sem TO"],
                    ["1977 a 1988", "26", "Criação de Mato Grosso do Sul (1977)"],
                    ["Após 1988", "27", "Criação de Tocantins (1988)"],
                ],
            },
            "topic_id": "stars",
        },
        {
            "type": "callout",
            "content": {
                "variant": "info",
                "title": "Mapa interativo:",
                "text": "Na aba Mapas interativos, veja as capitais de todas as unidades federativas.",
            },
            "topic_id": "stars",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Guanabara:",
                "text": "Entre 1960 e 1975 existiu o estado da Guanabara (capital: Rio de Janeiro). "
                "Depois ele voltou a ser município do Rio de Janeiro.",
            },
            "topic_id": "stars",
        },
    ]


def _topic_political_maps() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "3. Mapas políticos históricos"}, "topic_id": "political_maps"},
        {
            "type": "paragraph",
            "content": {
                "text": "O mapa político mostra as divisas — as linhas que separam os estados. "
                "O mapa político do Brasil não é definitivo: ele muda quando novos estados são criados.",
            },
            "topic_id": "political_maps",
            "sources": [_src("page-015.jpg"), _src("page-006.jpg"), _src("page-018.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Mapa", "Unidades federativas", "Destaque"],
                "rows": [
                    ["1942–1977", "25 + Guanabara", "Goiás e MT ainda unidos"],
                    ["1977–1988", "27", "MS criado; TO ainda parte de Goiás"],
                    ["Após 1988", "27", "TO separado de Goiás — 26 estados + DF"],
                ],
            },
            "topic_id": "political_maps",
        },
        {
            "type": "callout",
            "content": {
                "variant": "info",
                "title": "Mapa interativo:",
                "text": "Na aba Mapas interativos você pode explorar a evolução do mapa político "
                "e clicar em cada estado.",
            },
            "topic_id": "political_maps",
        },
        {
            "type": "callout",
            "content": {
                "variant": "info",
                "title": "Leitura de mapa:",
                "text": "Observe o título do mapa — ele indica o período histórico. "
                "Compare com o mapa atual para ver o que mudou.",
            },
            "topic_id": "political_maps",
        },
    ]


def _topic_new_states() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "4. Por que criar novos estados?"}, "topic_id": "new_states"},
        {
            "type": "paragraph",
            "content": {
                "text": "Estados podem ser divididos quando áreas distantes da capital ficam isoladas "
                "e com problemas de desenvolvimento. Diferenças culturais entre regiões do mesmo "
                "estado também podem motivar a separação.",
            },
            "topic_id": "new_states",
            "sources": [_src("page-011.jpg"), _src("page-007.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "📏", "title": "Distância", "text": "Capitais longe de cidades importantes"},
                    {"icon": "🏚️", "title": "Isolamento", "text": "Falta de estradas, escolas e serviços"},
                    {"icon": "⚔️", "title": "Rivalidades", "text": "Disputas entre cidades do mesmo estado"},
                    {"icon": "🗳️", "title": "Plebiscito", "text": "Consulta ao povo antes de dividir"},
                ],
            },
            "topic_id": "new_states",
        },
    ]


def _topic_mato_grosso() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "5. Divisão de Mato Grosso"}, "topic_id": "mato_grosso"},
        {
            "type": "paragraph",
            "content": {
                "text": "Em 11 de outubro de 1977, o presidente Ernesto Geisel assinou a lei que dividiu "
                "Mato Grosso e criou Mato Grosso do Sul. A capital do norte, Cuiabá, ficou longe "
                "da cidade mais rica do sul, Campo Grande. Havia rivalidades entre as duas regiões.",
            },
            "topic_id": "mato_grosso",
            "sources": [_src("page-009.jpg"), _src("page-011.jpg"), _src("page-012.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["", "Mato Grosso", "Mato Grosso do Sul"],
                "rows": [
                    ["Capital", "Cuiabá (continua)", "Campo Grande"],
                    ["Criado em", "Estado original", "11 de outubro de 1977"],
                    ["Reação", "Norte lamentou", "Sul comemorou"],
                ],
            },
            "topic_id": "mato_grosso",
        },
        {
            "type": "callout",
            "content": {
                "variant": "info",
                "title": "Mapa interativo:",
                "text": "Na aba Mapas interativos, compare Mato Grosso unido (até 1977) e dividido (após 1977).",
            },
            "topic_id": "mato_grosso",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Feriado:",
                "text": "O dia 11 de outubro virou feriado estadual em Mato Grosso do Sul — "
                "marca o fim de uma luta de mais de 100 anos.",
            },
            "topic_id": "mato_grosso",
        },
    ]


def _topic_goias_tocantins() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "6. Divisão de Goiás e Tocantins"}, "topic_id": "goias_tocantins"},
        {
            "type": "paragraph",
            "content": {
                "text": "Em 5 de outubro de 1988, o estado de Tocantins foi criado com a divisão de Goiás. "
                "A população do norte de Goiás queria acabar com o isolamento e o abandono pelo governo. "
                "A nova capital, Palmas, foi planejada às margens do rio Tocantins.",
            },
            "topic_id": "goias_tocantins",
            "sources": [_src("page-002.jpg"), _src("page-004.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🏛️", "title": "Goiás", "text": "Capital: Goiânia (antes e depois)"},
                    {"icon": "🌴", "title": "Tocantins", "text": "Capital: Palmas (nova cidade)"},
                    {"icon": "🛣️", "title": "Depois da divisão", "text": "Estradas, prédios, universidades"},
                    {"icon": "🌾", "title": "Economia", "text": "Agropecuária moderna"},
                ],
            },
            "topic_id": "goias_tocantins",
        },
        {
            "type": "callout",
            "content": {
                "variant": "info",
                "title": "Mapa interativo:",
                "text": "Na aba Mapas interativos, veja Goiás antes da criação de Tocantins em 1988.",
            },
            "topic_id": "goias_tocantins",
        },
    ]


def _topic_borders_proposals() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "7. Divisas e propostas de divisão"}, "topic_id": "borders"},
        {
            "type": "paragraph",
            "content": {
                "text": "A divisa é a linha no mapa que separa o território de cada estado. "
                "Marcos são placas ou construções de pedra que mostram no chão onde termina "
                "um estado e começa outro — como na divisa entre Paraná e Santa Catarina.",
            },
            "topic_id": "borders",
            "sources": [_src("page-008.jpg")],
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Em 2011, houve plebiscito para dividir o Pará em três estados: Tapajós, "
                "Carajás e Pará. A população votou contra. Quem defendia a divisão dizia que "
                "o estado era muito grande para administrar; quem era contra argumentava que "
                "os recursos ficariam divididos e mais fracos.",
            },
            "topic_id": "borders",
            "sources": [_src("page-010.jpg"), _src("page-007.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Plebiscito:",
                "text": "Consulta em que o povo aprova ou rejeita uma proposta antes de ela virar lei.",
            },
            "topic_id": "borders",
        },
    ]


def _topic_physical_maps() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "8. Mapas físicos e altitude"}, "topic_id": "physical_maps"},
        {
            "type": "paragraph",
            "content": {
                "text": "O mapa físico mostra elementos naturais: rios, planaltos, serras e planícies. "
                "No mapa político vemos as divisas dos estados; no físico, as cores indicam a altitude — "
                "a distância em metros de um ponto até o nível do mar.",
            },
            "topic_id": "physical_maps",
            "sources": [_src("page-013.jpg"), _src("page-001.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Cor", "Altitude", "Relevo"],
                "rows": [
                    ["Verde-claro", "Até 100 m", "Áreas baixas, planícies"],
                    ["Amarelo", "101 a 500 m", "Áreas de altitude média"],
                    ["Laranja", "501 a 1200 m", "Planaltos e serras"],
                    ["Marrom", "Acima de 1201 m", "Montanhas altas"],
                ],
            },
            "topic_id": "physical_maps",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Região Sudeste:",
                "text": "Rios importantes: Paraná, Paranapanema, Grande, Paranaíba e Paraíba do Sul. "
                "Parte da região tem como fronteira o Oceano Atlântico.",
            },
            "topic_id": "physical_maps",
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
                    "text": "Revise cada tópico nos acordeões — cards e tabelas com o essencial.",
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "1. Bandeira"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🟢", "title": "Verde", "text": "Matas · família real"},
                        {"icon": "🟡", "title": "Amarelo", "text": "Ouro · Leopoldina"},
                        {"icon": "🔵", "title": "Azul", "text": "Céu · rios · mares"},
                        {"icon": "📅", "title": "19/11/1889", "text": "Dia da Bandeira"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. Estrelas"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "⭐", "title": "Hoje", "text": "27 estrelas = 26 estados + DF"},
                        {"icon": "➕", "title": "Novo estado", "text": "Nova estrela na bandeira"},
                        {"icon": "📊", "title": "1977", "text": "26 estrelas (MS criado)"},
                        {"icon": "📊", "title": "1988", "text": "27 estrelas (TO criado)"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Mapas políticos"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["Período", "UFs", "Falta"],
                    "rows": [
                        ["1942–77", "25 + Guanabara", "MS e TO"],
                        ["1977–88", "27 no mapa", "TO (ainda em Goiás)"],
                        ["Após 1988", "27", "Mapa atual"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Novos estados"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "📏", "title": "Causas", "text": "Distância · isolamento · rivalidades"},
                        {"icon": "🗳️", "title": "Plebiscito", "text": "Povo decide na consulta"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Mato Grosso"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["", "MT", "MS"],
                    "rows": [
                        ["Capital", "Cuiabá", "Campo Grande"],
                        ["Data", "Estado original", "11/10/1977"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "6. Goiás / Tocantins"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🏛️", "title": "Goiânia", "text": "Capital de Goiás"},
                        {"icon": "🌴", "title": "Palmas", "text": "Capital de Tocantins"},
                        {"icon": "📅", "title": "5/10/1988", "text": "Criação de Tocantins"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "7. Divisas"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "📍", "title": "Divisa", "text": "Linha que separa estados"},
                        {"icon": "🪨", "title": "Marco", "text": "Placa ou pedra na fronteira"},
                        {"icon": "❌", "title": "Pará 2011", "text": "Plebiscito rejeitou divisão"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "8. Mapa físico"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["Cor", "Altitude"],
                    "rows": [
                        ["Verde-claro", "Até 100 m"],
                        ["Amarelo", "101–500 m"],
                        ["Marrom", "Acima de 1201 m"],
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "Cuiabá sempre foi capital de Mato Grosso — Campo Grande é capital "
                    "de Mato Grosso do Sul, não de Mato Grosso.",
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
                "id": "geo-pe-001",
                "type": "multiple_choice",
                "topic": "flag",
                "question": "Popularmente, a cor amarela da bandeira do Brasil representa:",
                "options": [
                    "As matas brasileiras",
                    "A riqueza mineral, principalmente o ouro",
                    "O desejo de paz",
                    "O Oceano Atlântico",
                ],
                "correct_answer": 1,
                "explanation": "Amarelo representa popularmente o ouro e a riqueza mineral do Brasil.",
                "difficulty": "basic",
                "source_assets": sa("page-017.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-002",
                "type": "multiple_choice",
                "topic": "flag",
                "question": (
                    "Leia as afirmativas sobre a bandeira do Brasil:\n"
                    "I. A bandeira é um símbolo nacional.\n"
                    "II. O azul representa popularmente o céu, rios e mares.\n"
                    "III. A bandeira atual foi adotada em 1889.\n"
                    "IV. O branco representa o desejo de guerra.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e III", "II, III e IV", "I e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e III corretas. Branco representa paz, não guerra (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-017.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-003",
                "type": "multiple_choice",
                "topic": "stars",
                "question": "As estrelas na bandeira do Brasil representam:",
                "options": [
                    "Os presidentes do país",
                    "As unidades federativas (estados e o Distrito Federal)",
                    "Os rios mais importantes",
                    "Os continentes do mundo",
                ],
                "correct_answer": 1,
                "explanation": "Cada estrela = um estado ou o Distrito Federal.",
                "difficulty": "basic",
                "source_assets": sa("page-014.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-004",
                "type": "multiple_choice",
                "topic": "stars",
                "question": "Se um novo estado for criado no Brasil, o que acontece com a bandeira?",
                "options": [
                    "Muda só a cor verde",
                    "Adiciona-se uma nova estrela",
                    "Remove-se uma estrela",
                    "A bandeira não pode mudar",
                ],
                "correct_answer": 1,
                "explanation": "Novo estado = nova estrela na bandeira.",
                "difficulty": "basic",
                "source_assets": sa("page-014.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-005",
                "type": "multiple_choice",
                "topic": "stars",
                "question": "Na bandeira adotada após 1988, quantas estrelas há?",
                "options": ["21", "26", "27", "30"],
                "correct_answer": 2,
                "explanation": "27 estrelas = 26 estados + Distrito Federal.",
                "difficulty": "basic",
                "source_assets": sa("page-014.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-006",
                "type": "multiple_choice",
                "topic": "political_maps",
                "question": (
                    "Entre 1942 e 1977, quais unidades federativas atuais NÃO constavam "
                    "no mapa político do Brasil?"
                ),
                "options": [
                    "Rio de Janeiro e São Paulo",
                    "Mato Grosso do Sul e Tocantins",
                    "Bahia e Pernambuco",
                    "Amazonas e Pará",
                ],
                "correct_answer": 1,
                "explanation": "MS foi criado em 1977; TO em 1988 — ambos não existiam antes de 1977.",
                "difficulty": "intermediate",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-007",
                "type": "multiple_choice",
                "topic": "political_maps",
                "question": (
                    "Leia as afirmativas sobre mapas políticos:\n"
                    "I. Mostram as divisas entre estados.\n"
                    "II. O mapa político do Brasil nunca muda.\n"
                    "III. Novos estados alteram o mapa político.\n"
                    "IV. O mapa político é igual ao mapa físico.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, II e III", "II, III e IV"],
                "correct_answer": 0,
                "explanation": "I e III corretas. O mapa muda (II errada) e é diferente do físico (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-015.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-008",
                "type": "multiple_choice",
                "topic": "new_states",
                "question": "Uma causa comum para a divisão de estados é:",
                "options": [
                    "Aumentar o número de estrelas na bandeira de outros países",
                    "Grande distância de áreas isoladas em relação à capital",
                    "Diminuir o tamanho do Oceano Atlântico",
                    "Eliminar todas as divisas",
                ],
                "correct_answer": 1,
                "explanation": "Isolamento e distância da capital causam problemas de desenvolvimento.",
                "difficulty": "basic",
                "source_assets": sa("page-011.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-009",
                "type": "multiple_choice",
                "topic": "mato_grosso",
                "question": "Mato Grosso do Sul foi criado em:",
                "options": [
                    "5 de outubro de 1988",
                    "11 de outubro de 1977",
                    "19 de novembro de 1889",
                    "1 de janeiro de 2000",
                ],
                "correct_answer": 1,
                "explanation": "A divisão de Mato Grosso ocorreu em 11 de outubro de 1977.",
                "difficulty": "basic",
                "source_assets": sa("page-009.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-010",
                "type": "multiple_choice",
                "topic": "mato_grosso",
                "question": (
                    "Leia as afirmativas sobre a divisão de Mato Grosso:\n"
                    "I. Cuiabá continua sendo capital de Mato Grosso.\n"
                    "II. Campo Grande é capital de Mato Grosso do Sul.\n"
                    "III. A população do sul comemorou a divisão.\n"
                    "IV. Campo Grande é capital de Mato Grosso.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e III", "II, III e IV", "I e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e III corretas. Campo Grande é capital de MS, não de MT (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-012.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-011",
                "type": "multiple_choice",
                "topic": "goias_tocantins",
                "question": (
                    "Observe o mapa. O estado em destaque (amarelo) ao norte de Goiás, "
                    "criado em 1988, é:"
                ),
                "visual": {
                    "type": "brazil_map",
                    "content": {
                        "period": "post_1988",
                        "show_period_toggle": False,
                        "highlight": ["TO"],
                        "interactive": True,
                        "aria_label": "Mapa com Tocantins em destaque",
                    },
                },
                "options": ["Mato Grosso do Sul", "Tocantins", "Rondônia", "Maranhão"],
                "correct_answer": 1,
                "explanation": "Tocantins foi criado em 1988 com a divisão de Goiás; capital: Palmas.",
                "difficulty": "intermediate",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-012",
                "type": "multiple_choice",
                "topic": "goias_tocantins",
                "question": (
                    "O principal argumento de quem queria dividir Goiás era:"
                ),
                "options": [
                    "Acabar com o isolamento e abandono do norte",
                    "Eliminar o estado de Goiás completamente",
                    "Mudar a capital do Brasil para Palmas",
                    "Unir Goiás com o Paraná",
                ],
                "correct_answer": 0,
                "explanation": "O norte de Goiás sofria isolamento e abandono pelo governo estadual.",
                "difficulty": "intermediate",
                "source_assets": sa("page-002.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-013",
                "type": "multiple_choice",
                "topic": "borders",
                "question": "Marcos construídos ao longo de uma divisa entre estados servem para:",
                "options": [
                    "Medir a temperatura do ar",
                    "Mostrar no chão onde termina um estado e começa outro",
                    "Indicar a altitude das montanhas",
                    "Contar as estrelas da bandeira",
                ],
                "correct_answer": 1,
                "explanation": "Marcos são placas ou pedras que demarcam a fronteira entre estados.",
                "difficulty": "basic",
                "source_assets": sa("page-008.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-014",
                "type": "multiple_choice",
                "topic": "borders",
                "question": (
                    "Leia as afirmativas sobre a proposta de divisão do Pará em 2011:\n"
                    "I. Foi proposta a criação de Tapajós, Carajás e Pará.\n"
                    "II. O plebiscito aprovou a divisão.\n"
                    "III. Quem era contra dizia que os recursos ficariam divididos.\n"
                    "IV. O estado do Pará é o segundo maior do Brasil.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, II e IV", "II, III e IV"],
                "correct_answer": 0,
                "explanation": "I e III corretas. O plebiscito rejeitou a divisão (II errada). IV não é o foco da questão.",
                "difficulty": "intermediate",
                "source_assets": sa("page-010.jpg"),
                "section": "exercises",
            },
            {
                "id": "geo-pe-015",
                "type": "multiple_choice",
                "topic": "physical_maps",
                "question": "No mapa físico, a cor marrom geralmente indica:",
                "options": [
                    "Áreas com altitude até 100 metros",
                    "Áreas com altitude acima de 1201 metros",
                    "O Oceano Atlântico",
                    "As divisas entre estados",
                ],
                "correct_answer": 1,
                "explanation": "Marrom = altitude acima de 1201 m (montanhas altas).",
                "difficulty": "basic",
                "source_assets": sa("page-013.jpg"),
                "section": "final_quiz",
            },
            {
                "id": "geo-pe-016",
                "type": "multiple_choice",
                "topic": "physical_maps",
                "question": (
                    "Leia as afirmativas sobre mapas físicos e a região Sudeste:\n"
                    "I. O mapa físico mostra rios e relevo.\n"
                    "II. Verde-claro indica altitude até 100 m.\n"
                    "III. O Paraíba do Sul é um rio da região Sudeste.\n"
                    "IV. O mapa físico mostra apenas divisas de estados.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e III", "II, III e IV", "I e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e III corretas. Divisas são do mapa político (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-001.jpg"),
                "section": "final_quiz",
            },
        ],
    }
