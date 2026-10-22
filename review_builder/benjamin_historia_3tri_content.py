"""Conteúdo pedagógico da revisão Benjamin — História PE 3º trimestre (Módulos 8, 9 e 10)."""

from __future__ import annotations

REVIEW_ID = "benjamin-pe-historia-3tri"
ASSET_PREFIX = "assets/benjamin_pe_historia_3_tri"


def _src(page: str) -> dict:
    return {
        "asset": f"{ASSET_PREFIX}/{page}",
        "origin_type": "observed",
        "evidence": [f"Caderno de História — {page}"],
    }


def build_content() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de História — PE 3º Trimestre",
        "subtitle": "Benjamin · 4º ano · Módulos 8, 9 e 10",
        "language": "pt-BR",
        "discipline": "História",
        "grade": "4º ano",
        "metadata": {
            "student_name": "Benjamin",
            "exam_type": "Prova Específica (PE)",
            "estimated_duration_minutes": 55,
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
                    "text": "África e reinos bantus, comércio e escravização, engenhos de açúcar, "
                    "bandeirantes, febre do ouro e a sociedade nas minas. Reserve cerca de 55 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "👑", "title": "Reinos africanos", "text": "Bantus · Congo · Ndongo"},
                        {"icon": "⛵", "title": "Tráfico", "text": "Navios negreiros · diáspora"},
                        {"icon": "🌾", "title": "Açúcar", "text": "Engenho · São Vicente · Nordeste"},
                        {"icon": "🔨", "title": "Tecnologia", "text": "Metalurgia africana na colônia"},
                        {"icon": "🗺️", "title": "Bandeirantes", "text": "São Paulo · sertão · bandeiras"},
                        {"icon": "🥇", "title": "Ouro", "text": "Aluvião · filões · lavras"},
                        {"icon": "🐴", "title": "Tropeiros", "text": "Mulas · abastecimento · ouro"},
                        {"icon": "⛪", "title": "Vilas", "text": "Mariana · Ouro Preto · Sabará"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 8 — Novo Mundo: África e início da colônia",
                        "Módulo 9 — Escravização, engenhos e influências africanas",
                        "Módulo 10 — Bandeirantes, ouro e sociedade mineradora",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Leia os cards e tabelas com calma.",
                            "tip": "Monte uma linha do tempo: África → tráfico → engenhos → ouro.",
                        },
                        {
                            "title": "Revise o Resumo rápido",
                            "panel": "summary",
                            "panel_label": "Resumo rápido",
                            "description": "Percorra os blocos-síntese — use como mapa mental para a PE.",
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


def _section_explain() -> dict:
    return {
        "id": "explain",
        "type": "explanations",
        "title": "Explicações",
        "blocks": [
            *_topic_africa_kingdoms(),
            *_topic_portugal_africa(),
            *_topic_slave_trade(),
            *_topic_colonial_sugar(),
            *_topic_african_influence(),
            *_topic_bandeirantes(),
            *_topic_gold_cycle(),
            *_topic_mining_society(),
        ],
    }


def _topic_africa_kingdoms() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "1. Reinos africanos e povos bantus"},
            "topic_id": "africa_kingdoms",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Os bantus foram grupos africanos com línguas parecidas que ocuparam grande parte "
                "do continente, do sul até regiões próximas ao Equador. Formaram reinos organizados "
                "com agricultura, comércio, artesanato e, em alguns lugares, mineração e metalurgia.",
            },
            "topic_id": "africa_kingdoms",
            "sources": [_src("page-050.jpg"), _src("page-052.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Reino", "Onde / destaque"],
                "rows": [
                    ["Congo", "Centro-oeste africano · capital Mbanza Congo · rei manicongo · moeda nzimbu (conchas)"],
                    ["Monomotapa", "Região de Grande Zimbábue · cidades grandes · ouro e caça"],
                    ["Ndongo", "Atual Angola · divisão de trabalho · comércio de tecidos e marfim"],
                ],
            },
            "topic_id": "africa_kingdoms",
        },
        {
            "type": "callout",
            "content": {
                "variant": "tip",
                "title": "Njinga a Mbande",
                "text": "Rainha guerreira do Ndongo que resistiu à ocupação portuguesa e negociou com "
                "outros reinos — símbolo de liderança e resistência africanas.",
            },
            "topic_id": "africa_kingdoms",
            "sources": [_src("page-035.jpg")],
        },
    ]


def _topic_portugal_africa() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "2. Comércio dos portugueses na África"},
            "topic_id": "portugal_africa_trade",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "A partir do século XV, portugueses buscaram riquezas na África. Construíram "
                "feitorias e fortalezas no litoral para trocar mercadorias com povos do interior "
                "sem precisar atravessar todo o continente. Com o tempo, passaram a negociar também "
                "pessoas escravizadas, trocando-as por armas, tecidos, joias, tabaco e aguardente.",
            },
            "topic_id": "portugal_africa_trade",
            "sources": [_src("page-048.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🏰", "title": "Fortes no litoral", "text": "Base para comércio e controle"},
                    {"icon": "🐪", "title": "Caravanas", "text": "Comerciantes islâmicos no norte da África"},
                    {"icon": "🤝", "title": "Parcerias", "text": "Reis africanos e portugueses nas trocas"},
                ],
            },
            "topic_id": "portugal_africa_trade",
        },
    ]


def _topic_slave_trade() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "3. Tráfico, diáspora e quilombos"},
            "topic_id": "slave_trade",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Milhões de africanos foram arrancados de suas terras e transportados em navios "
                "negreiros (tumbeiros) em condições horríveis: porões apertados, pouca comida e ar. "
                "Historiadores usam a palavra diáspora para falar dessa dispersão forçada para a América.",
            },
            "topic_id": "slave_trade",
            "sources": [_src("page-025.jpg"), _src("page-040.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🚢", "title": "Navio negreiro", "text": "Lucro às custas de centenas no porão"},
                    {"icon": "🏷️", "title": "Chegada ao Brasil", "text": "Nomes portugueses · vendidos aos senhores"},
                    {"icon": "🌳", "title": "Quilombos", "text": "Refúgio de fugidos · resistência à escravização"},
                ],
            },
            "topic_id": "slave_trade",
        },
    ]


def _topic_colonial_sugar() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "4. Primeiras expedições e engenhos de açúcar"},
            "topic_id": "colonial_sugar",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Em 1532, Martim Afonso de Sousa fundou São Vicente (litoral paulista) e, em 1534, "
                "mandou construir um dos primeiros engenhos das Américas — o Engenho dos Erasmos. "
                "A cana era moída com roda d'água; o caldo fervia e virava pão de açúcar para exportar. "
                "No início indígenas escravizados trabalhavam; depois vieram mais africanos escravizados.",
            },
            "topic_id": "colonial_sugar",
            "sources": [_src("page-030.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "info",
                "title": "Nordeste",
                "text": "A partir do século XVII, o Nordeste ganhou importância na produção de açúcar "
                "por causa do clima e do solo favoráveis — e dos ataques de piratas no Sudeste.",
            },
            "topic_id": "colonial_sugar",
        },
    ]


def _topic_african_influence() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "5. Influências africanas no Brasil colonial"},
            "topic_id": "african_influence",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Na África, a metalurgia era antiga e respeitada. Africanos escravizados trouxeram "
                "esse conhecimento e ajudaram a melhorar engenhos de cana, fornos, ferramentas e "
                "máquinas na colônia — parte importante do desenvolvimento tecnológico do trabalho.",
            },
            "topic_id": "african_influence",
            "sources": [_src("page-020.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🔥", "title": "Fornos e engenhos", "text": "Produção de açúcar e aguardente"},
                    {"icon": "🛠️", "title": "Ferramentas", "text": "Utensílios de metal no dia a dia colonial"},
                    {"icon": "🌍", "title": "Língua portuguesa", "text": "Países africanos de língua portuguesa (lusofonia)"},
                ],
            },
            "topic_id": "african_influence",
        },
    ]


def _topic_bandeirantes() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "6. Bandeirantes e expedições ao sertão"},
            "topic_id": "bandeirantes",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "No século XVII, a vila de São Paulo de Piratininga, no planalto paulista, virou "
                "ponto de partida das bandeiras — expedições ao interior (sertão) em busca de "
                "indígenas para escravizar, riquezas e, mais tarde, ouro. Mamelucos (filhos de "
                "portugueses e indígenas) eram parte importante dessa população.",
            },
            "topic_id": "bandeirantes",
            "sources": [_src("page-015.jpg"), _src("page-012.jpg"), _src("page-003.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "⛰️", "title": "Serra do Mar", "text": "Obstáculo entre litoral e planalto"},
                    {"icon": "🚶", "title": "Bandeiras", "text": "Grupos armados em longas caminhadas"},
                    {"icon": "📍", "title": "Rotas", "text": "Do Sudeste para interior, Norte e Sul"},
                ],
            },
            "topic_id": "bandeirantes",
        },
    ]


def _topic_gold_cycle() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "7. Descoberta do ouro e febre do ouro"},
            "topic_id": "gold_cycle",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Entre os séculos XVII e XVIII, confirmou-se ouro em Minas Gerais — muito em "
                "aluvião (partículas soltas na areia dos rios). Multidões migraram para o interior. "
                "Nas lavras, escravizados lavavam o minério sob olho de feitores; nas encostas "
                "exploravam filões (veios de metal na rocha). Formaram-se vilas e cidades no relevo acidentado.",
            },
            "topic_id": "gold_cycle",
            "sources": [_src("page-010.jpg"), _src("page-009.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Tipo de depósito", "Onde / como"],
                "rows": [
                    ["Aluvião", "Leito dos rios · ouro em partículas · lavagem com bateia"],
                    ["Filão", "Veio estreito na rocha · exploração a céu aberto"],
                ],
            },
            "topic_id": "gold_cycle",
        },
    ]


def _topic_mining_society() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "8. Sociedade mineradora: trabalho, tropeiros e vilas"},
            "topic_id": "mining_society",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Mineradores não tinham tempo de plantar nem fabricar tudo — tropeiros levavam mulas "
                "carregadas de feijão, milho, carne-seca e couro de longe, cobrando caro em ouro. "
                "Indígenas escravizados trabalharam primeiro nas minas; depois predominaram africanos "
                "escravizados, inclusive escravizados de ganho nas ruas das vilas.",
            },
            "topic_id": "mining_society",
            "sources": [_src("page-008.jpg"), _src("page-006.jpg"), _src("page-005.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Região fornecedora", "Exemplos de mercadorias"],
                "rows": [
                    ["Nordeste", "Couro, carne-seca, escravizados"],
                    ["Sul", "Mulas, couro e carne-seca"],
                    ["Sudeste", "Feijão, milho, doces (marmelada)"],
                ],
            },
            "topic_id": "mining_society",
        },
        {
            "type": "callout",
            "content": {
                "variant": "tip",
                "title": "Primeiras vilas (1711–1730)",
                "text": "Portugal criou vilas para controlar a região — entre elas Mariana (Vila do Carmo), "
                "Ouro Preto (Vila Rica) e Sabará.",
            },
            "topic_id": "mining_society",
            "sources": [_src("page-005.jpg"), _src("page-002.jpg")],
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
                    "text": "Revise na ordem dos módulos. Cada bloco resume um tópico das Explicações.",
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "1. Reinos africanos"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "👑", "title": "Bantus", "text": "Reinos · comércio · nzimbu"},
                        {"icon": "⚔️", "title": "Njinga", "text": "Resistência no Ndongo"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. Portugal na África"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🏰", "title": "Fortes", "text": "Comércio no litoral"},
                        {"icon": "⛓️", "title": "Escravização", "text": "Trocas por armas e aguardente"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Tráfico e quilombos"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🚢", "title": "Diáspora", "text": "Navios tumbeiros · porões"},
                        {"icon": "🌳", "title": "Quilombos", "text": "Fuga e resistência"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Engenhos"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🌾", "title": "São Vicente", "text": "1532 · Martim Afonso"},
                        {"icon": "🍬", "title": "Açúcar", "text": "Roda d'água · pão de açúcar"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Influência africana"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🔨", "title": "Metalurgia", "text": "Engenhos e ferramentas"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "6. Bandeirantes"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "📍", "title": "São Paulo", "text": "Bandeiras ao sertão"},
                        {"icon": "⛰️", "title": "Serras", "text": "Caminho até Minas"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "7. Ouro"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["", "Aluvião", "Filão"],
                    "rows": [
                        ["Onde", "Rios", "Rocha (veio)"],
                        ["Trabalho", "Lavagem", "Escavação a céu aberto"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "8. Minas"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🐴", "title": "Tropeiros", "text": "Abastecimento · preços altos"},
                        {"icon": "🏘️", "title": "Vilas", "text": "Mariana · Ouro Preto · Sabará"},
                        {"icon": "🐄", "title": "Pastoreio", "text": "Vaqueiros · sertão · couro"},
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "Na região das minas nem tudo era produzido localmente — tropeiros traziam "
                    "comida e mercadorias de outras regiões, e isso encarecia a vida.",
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
                "id": "hist3-pe-001",
                "type": "multiple_choice",
                "topic": "africa_kingdoms",
                "question": "No reino do Congo, os comerciantes usavam como moeda conchas chamadas:",
                "options": ["Nzimbu", "Coivara", "Sambaqui", "Aluvião"],
                "correct_answer": 0,
                "explanation": "Nzimbu eram conchas usadas nas trocas pelos bantus do Congo.",
                "difficulty": "basic",
                "source_assets": sa("page-050.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-002",
                "type": "multiple_choice",
                "topic": "africa_kingdoms",
                "question": (
                    "Leia as afirmativas sobre os reinos africanos estudados:\n"
                    "I. Os bantus ocuparam grande parte do continente africano.\n"
                    "II. O reino do Congo tinha capital em Mbanza Congo.\n"
                    "III. Monomotapa ficava na Europa.\n"
                    "IV. Ndongo ficava em região que hoje é Angola.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e IV", "I e III", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e IV corretas. Monomotapa ficava na África (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-052.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-003",
                "type": "multiple_choice",
                "topic": "portugal_africa_trade",
                "question": (
                    "No século XV, os portugueses construíram fortes no litoral africano principalmente para:"
                ),
                "options": [
                    "Facilitar o comércio com povos do interior",
                    "Plantar cana-de-açúcar em larga escala",
                    "Fundar cidades como Ouro Preto",
                    "Evitar totalmente qualquer contato com africanos",
                ],
                "correct_answer": 0,
                "explanation": "Fortes serviam de base para trocas comerciais no litoral.",
                "difficulty": "basic",
                "source_assets": sa("page-048.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-004",
                "type": "multiple_choice",
                "topic": "slave_trade",
                "question": (
                    "Leia as afirmativas sobre o tráfico de pessoas escravizadas:\n"
                    "I. Navios negreiros tinham porões apertados e sem higiene.\n"
                    "II. Diáspora descreve a dispersão forçada de africanos.\n"
                    "III. Quilombos eram lugares de resistência e refúgio.\n"
                    "IV. Todos chegavam saudáveis e livres ao Brasil.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "I, II e III", "II, III e IV", "III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Muitos morriam no trajeto (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-025.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-005",
                "type": "multiple_choice",
                "topic": "colonial_sugar",
                "question": "Em 1532, Martim Afonso de Sousa fundou a vila de:",
                "options": ["São Vicente", "Ouro Preto", "Salvador", "Recife"],
                "correct_answer": 0,
                "explanation": "São Vicente, no litoral paulista, marcou a ocupação europeia da região.",
                "difficulty": "basic",
                "source_assets": sa("page-030.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-006",
                "type": "multiple_choice",
                "topic": "colonial_sugar",
                "question": (
                    "Nos primeiros engenhos de açúcar, quem foi substituído gradualmente "
                    "como principal mão de obra escravizada?"
                ),
                "options": [
                    "Indígenas por africanos escravizados",
                    "Africanos por indígenas",
                    "Tropeiros por bandeirantes",
                    "Plebeus por patrícios",
                ],
                "correct_answer": 0,
                "explanation": "Primeiro indígenas; com o tempo aumentou o tráfico de africanos escravizados.",
                "difficulty": "basic",
                "source_assets": sa("page-030.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-007",
                "type": "multiple_choice",
                "topic": "african_influence",
                "question": (
                    "Leia as afirmativas sobre influências africanas na colônia:\n"
                    "I. Africanos escravizados tinham conhecimento de metalurgia.\n"
                    "II. Ajudaram a melhorar engenhos e ferramentas.\n"
                    "III. Não participaram de nenhuma atividade técnica.\n"
                    "IV. Países lusófonos na África falam português por causa da colonização.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["II e IV", "I, II e IV", "I e III", "II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Africanos contribuíram muito na técnica colonial (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-020.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-008",
                "type": "multiple_choice",
                "topic": "bandeirantes",
                "question": (
                    "As expedições bandeirantes do século XVII tinham como principal ponto de partida:"
                ),
                "options": [
                    "São Paulo de Piratininga",
                    "Salvador",
                    "Rio de Janeiro",
                    "Belém",
                ],
                "correct_answer": 0,
                "explanation": "A vila paulista no planalto era base das bandeiras ao sertão.",
                "difficulty": "basic",
                "source_assets": sa("page-015.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-009",
                "type": "multiple_choice",
                "topic": "bandeirantes",
                "question": (
                    "Leia as afirmativas sobre bandeirantes:\n"
                    "I. Cruzavam serras como a do Mar em direção ao interior.\n"
                    "II. Buscavam riquezas, indígenas e, depois, ouro.\n"
                    "III. Só atuavam no litoral nordestino.\n"
                    "IV. Mamelucos faziam parte da população paulista.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e IV", "I e III", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e IV corretas. Bandeiras partiam do Sudeste, não só do Nordeste (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-012.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-010",
                "type": "multiple_choice",
                "topic": "gold_cycle",
                "question": "O ouro encontrado em partículas soltas na areia dos rios é chamado de:",
                "options": ["Aluvião", "Filão", "Sambaqui", "Nzimbu"],
                "correct_answer": 0,
                "explanation": "Aluvião = depósito em leito de rio; filão = veio na rocha.",
                "difficulty": "basic",
                "source_assets": sa("page-010.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-011",
                "type": "multiple_choice",
                "topic": "gold_cycle",
                "question": (
                    "Nas lavras coloniais, escravizados lavavam ouro nos rios sob vigilância de:"
                ),
                "options": ["Feitores", "Manicongos", "Tribunos", "Gladiadores"],
                "correct_answer": 0,
                "explanation": "Feitores fiscalizavam o trabalho para evitar fugas e roubo de ouro.",
                "difficulty": "basic",
                "source_assets": sa("page-009.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-012",
                "type": "multiple_choice",
                "topic": "mining_society",
                "question": (
                    "Tropeiros eram comerciantes que:"
                ),
                "options": [
                    "Transportavam mercadorias com tropas de mulas até a região das minas",
                    "Governavam o reino do Congo",
                    "Pintavam apenas cavernas pré-históricas",
                    "Comandavam caravelas portuguesas no século XV",
                ],
                "correct_answer": 0,
                "explanation": "Tropeiros ligavam outras regiões às minas, cobrando caro em ouro.",
                "difficulty": "basic",
                "source_assets": sa("page-008.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-013",
                "type": "multiple_choice",
                "topic": "mining_society",
                "question": (
                    "Leia as afirmativas sobre abastecimento das vilas mineradoras:\n"
                    "I. Nordeste enviava couro e carne-seca.\n"
                    "II. Sul contribuía com mulas.\n"
                    "III. Tudo era produzido só dentro de Minas — nada vinha de fora.\n"
                    "IV. Feijão e milho vinham também do Sudeste.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e IV", "I e III", "II, III e IV", "III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e IV corretas. Havia forte comércio entre regiões (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-014",
                "type": "multiple_choice",
                "topic": "mining_society",
                "question": (
                    "Escravizados de ganho, nas vilas mineradoras, eram aqueles que:"
                ),
                "options": [
                    "Trabalhavam nas ruas vendendo ou prestando serviços e entregavam parte do ganho ao senhor",
                    "Eram livres e donos das minas",
                    "Só trabalhavam em navios negreiros",
                    "Fundaram São Vicente em 1532",
                ],
                "correct_answer": 0,
                "explanation": "Escravizados de ganho atuavam na cidade e repassavam parte do pagamento.",
                "difficulty": "basic",
                "source_assets": sa("page-006.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-015",
                "type": "multiple_choice",
                "topic": "mining_society",
                "question": (
                    "Leia as afirmativas sobre ocupação do território colonial:\n"
                    "I. Agricultura ocupou litorais como Pernambuco e São Paulo.\n"
                    "II. Mineração ocupou o interior.\n"
                    "III. Pastoreio ajudou a ocupar o sertão com vaqueiros e tropeiros.\n"
                    "IV. Ouro foi descoberto no século XXI.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["II e IV", "I, II e III", "I e IV", "III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Ouro colonial é dos sécs. XVII–XVIII (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-002.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-016",
                "type": "multiple_choice",
                "topic": "mining_society",
                "question": (
                    "Entre 1711 e 1730, Portugal mandou criar vilas na região das minas. "
                    "Qual alternativa traz três exemplos corretos?"
                ),
                "options": [
                    "Mariana, Ouro Preto e Sabará",
                    "Ceuta, Lisboa e Roma",
                    "Salvador, Recife e Belém",
                    "São Vicente, Santos e Campinas",
                ],
                "correct_answer": 0,
                "explanation": "Vila do Carmo (Mariana), Vila Rica (Ouro Preto) e Sabará foram vilas mineradoras.",
                "difficulty": "intermediate",
                "source_assets": sa("page-005.jpg"),
                "section": "final_quiz",
            },
        ],
    }
