"""Conteúdo pedagógico da revisão Benjamin — História PE 2º trimestre."""

from __future__ import annotations

REVIEW_ID = "benjamin-pe-historia-2tri"
ASSET_PREFIX = "assets/benjamin_pe_historia_2_tri"


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
        "title": "Revisão de História — PE 2º Trimestre",
        "subtitle": "Benjamin · 4º ano · Módulos 4, 5 e 6",
        "language": "pt-BR",
        "discipline": "História",
        "grade": "4º ano",
        "metadata": {
            "student_name": "Benjamin",
            "exam_type": "Prova Específica (PE)",
            "estimated_duration_minutes": 50,
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
                    "text": "História dos povos que viveram no território brasileiro, o comércio no passado "
                    "e as Grandes Navegações portuguesas. Reserve cerca de 50 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🪨", "title": "Pré-história", "text": "Pinturas rupestres · caçadores-coletores"},
                        {"icon": "🐚", "title": "Sambaquis", "text": "Morros de conchas no litoral"},
                        {"icon": "🏺", "title": "Ceramistas", "text": "Sedentários na Amazônia"},
                        {"icon": "🌿", "title": "Tupi-Guarani", "text": "Coivara · aldeias · migração"},
                        {"icon": "🧂", "title": "Comércio", "text": "Especiarias · trocas entre continentes"},
                        {"icon": "⛵", "title": "Navegações", "text": "Caravelas · bússola · Ceuta 1415"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 4 — Povos do território brasileiro",
                        "Módulo 5 — Comércio e século XV",
                        "Módulo 6 — Navegações portuguesas",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Leia os cards e tabelas com calma.",
                            "tip": "Tente contar para alguém o que aprendeu em cada tópico.",
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
            *_topic_prehistory(),
            *_topic_umbu_humaita(),
            *_topic_sambaquis(),
            *_topic_ceramists(),
            *_topic_tupi(),
            *_topic_commerce(),
            *_topic_travelers(),
            *_topic_navigation(),
        ],
    }


def _topic_prehistory() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Pré-história: vestígios e pinturas rupestres"}, "topic_id": "prehistory"},
        {
            "type": "paragraph",
            "content": {
                "text": "Há milhares de anos, grupos de caçadores e coletores percorriam o território "
                "brasileiro. Eram nômades: mudavam de lugar para caçar, pescar e colher frutos.",
            },
            "topic_id": "prehistory",
            "sources": [_src("page-005.jpg"), _src("page-032.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🎨", "title": "Pinturas rupestres", "text": "Desenhos em paredes de cavernas e rochas"},
                    {"icon": "🔍", "title": "Sítio arqueológico", "text": "Lugar onde arqueólogos encontram vestígios do passado"},
                    {"icon": "🪓", "title": "Pedra lascada", "text": "Ferramentas de pedra para caçar e cortar"},
                ],
            },
            "topic_id": "prehistory",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Lembre-se:",
                "text": "Achados arqueológicos (restos de fogueiras, pontas de flecha, pinturas) "
                "ajudam a reconstruir como essas pessoas viviam.",
            },
            "topic_id": "prehistory",
        },
    ]


def _topic_umbu_humaita() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "2. Tradições Umbu e Humaitá"}, "topic_id": "umbu_humaita"},
        {
            "type": "paragraph",
            "content": {
                "text": "No Sul e Sudeste do Brasil, arqueólogos estudam a Tradição Umbu e a Tradição Humaitá. "
                "Eram caçadores-coletores que usavam ferramentas de pedra.",
            },
            "topic_id": "umbu_humaita",
            "sources": [_src("page-016.jpg"), _src("page-029.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🌲", "title": "Tradição Umbu", "text": "Região do Pampa · pinhão · boleadeiras"},
                    {"icon": "🍇", "title": "Tradição Humaitá", "text": "Sul/Sudeste · coleta de frutos silvestres"},
                    {"icon": "🎯", "title": "Boleadeira", "text": "Arma de arremesso com pedras — usada na caça"},
                ],
            },
            "topic_id": "umbu_humaita",
        },
    ]


def _topic_sambaquis() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "3. Sambaquis e sambaquieiros"}, "topic_id": "sambaquis"},
        {
            "type": "paragraph",
            "content": {
                "text": "Sambaqui vem do tupi e significa amontoado de conchas. São montes formados por "
                "restos de moluscos, ossos e outros materiais deixados por grupos que viviam no litoral.",
            },
            "topic_id": "sambaquis",
            "sources": [_src("page-015.jpg"), _src("page-017.jpg"), _src("page-021.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🐚", "title": "Alimentação", "text": "Moluscos, peixes e frutos do mar"},
                    {"icon": "🏖️", "title": "Onde ficam", "text": "Litoral brasileiro — SC, PR, SP, RJ…"},
                    {"icon": "⚰️", "title": "Sepultamento", "text": "Alguns sambaquis também eram cemitérios"},
                ],
            },
            "topic_id": "sambaquis",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Curiosidade:",
                "text": "Arqueólogos comparam mapas de sambaquis com mapas atuais para entender "
                "como o litoral mudou ao longo do tempo.",
            },
            "topic_id": "sambaquis",
        },
    ]


def _topic_ceramists() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "4. Ceramistas da Amazônia"}, "topic_id": "ceramists"},
        {
            "type": "paragraph",
            "content": {
                "text": "Na Amazônia, alguns grupos passaram a viver de forma sedentária: ficavam mais tempo "
                "no mesmo lugar. Produziam vasos de argila em Santarém e na Ilha de Marajó.",
            },
            "topic_id": "ceramists",
            "sources": [_src("page-026.jpg"), _src("page-022.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Nômade x sedentário",
                "headers": ["", "Nômade", "Sedentário"],
                "rows": [
                    ["Costume", "Muda de lugar com frequência", "Fica mais tempo no mesmo local"],
                    ["Exemplo", "Caçadores-coletores antigos", "Ceramistas da Amazônia"],
                    ["Trabalho", "Caça, pesca, coleta", "Cerâmica, roça, pesca"],
                ],
            },
            "topic_id": "ceramists",
        },
    ]


def _topic_tupi() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "5. Povo Tupi-Guarani"}, "topic_id": "tupi_guarani"},
        {
            "type": "paragraph",
            "content": {
                "text": "Os Tupi-Guarani migraram da Amazônia para outras regiões do Brasil. "
                "Cultivavam milho e mandioca em áreas chamadas coivara, dentro da mata.",
            },
            "topic_id": "tupi_guarani",
            "sources": [_src("page-003.jpg"), _src("page-034.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🏘️", "title": "Aldeias", "text": "Moradias circulares organizadas em volta de um espaço comum"},
                    {"icon": "🌽", "title": "Coivara", "text": "Área da mata limpa para plantar"},
                    {"icon": "🛶", "title": "Canoas", "text": "Usadas para pescar e se deslocar pelos rios"},
                ],
            },
            "topic_id": "tupi_guarani",
        },
        {
            "type": "timeline",
            "content": {
                "events": [
                    {"date": "~12.000 anos", "title": "Caçadores-coletores nômades"},
                    {"date": "~8.000 anos", "title": "Pescadores e sambaquieiros no litoral"},
                    {"date": "~4.000 anos", "title": "Ceramistas sedentários"},
                    {"date": "Depois", "title": "Agricultores Tupi-Guarani"},
                ],
            },
            "topic_id": "tupi_guarani",
        },
    ]


def _topic_commerce() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "6. Comércio e especiarias"}, "topic_id": "commerce_spices"},
        {
            "type": "paragraph",
            "content": {
                "text": "Desde a Antiguidade, povos trocavam mercadorias entre regiões distantes. "
                "No século XV, europeus buscavam especiarias da Ásia.",
            },
            "topic_id": "commerce_spices",
            "sources": [_src("page-018.jpg"), _src("page-008.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🧂", "title": "Especiarias", "text": "Canela, cravo, pimenta, gengibre, noz-moscada"},
                    {"icon": "💰", "title": "Por que valiam tanto?", "text": "Conservar comida, tempero, perfume e remédio"},
                    {"icon": "🍝", "title": "Trocas culturais", "text": "Ex.: macarrão espalhou da China para outros continentes"},
                ],
            },
            "topic_id": "commerce_spices",
        },
    ]


def _topic_travelers() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "7. Grandes viajantes"}, "topic_id": "travelers"},
        {
            "type": "paragraph",
            "content": {
                "text": "Antes das Grandes Navegações europeias, comerciantes e exploradores já "
                "percorriam longas distâncias.",
            },
            "topic_id": "travelers",
            "sources": [_src("page-030.jpg"), _src("page-033.jpg"), _src("page-039.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Três viajantes famosos",
                "headers": ["Viajante", "Origem / época", "Destaque"],
                "rows": [
                    ["Marco Polo", "Veneziano, séc. XIII", "Rota da Seda — Ásia e China"],
                    ["Ibn Battuta", "Marroquino, séc. XIV", "Viagens pela África, Ásia e Europa"],
                    ["Zheng He", "Chinês, séc. XV", "Expedições com juncos na Ásia e África"],
                ],
            },
            "topic_id": "travelers",
        },
    ]


def _topic_navigation() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "8. Navegações portuguesas"}, "topic_id": "portuguese_navigation"},
        {
            "type": "paragraph",
            "content": {
                "text": "No século XV, portugueses passaram a navegar além do Mar Tenebroso (Atlântico). "
                "Queriam rotas comerciais e riquezas.",
            },
            "topic_id": "portuguese_navigation",
            "sources": [_src("page-031.jpg"), _src("page-037.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "⛵", "title": "Caravela", "text": "Embarcação ágil (~25 m) — usada nas primeiras expedições"},
                    {"icon": "🚢", "title": "Nau", "text": "Embarcação maior (~50 m) — mais carga e tripulação"},
                    {"icon": "🧭", "title": "Instrumentos", "text": "Bússola, astrolábio, quadrante"},
                    {"icon": "🏰", "title": "Ceuta (1415)", "text": "Primeira conquista portuguesa fora da Península"},
                ],
            },
            "topic_id": "portuguese_navigation",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Medos reais x lendas:",
                "text": "Marinheiros temiam tempestades e correntes perigosas. Mapas antigos "
                "desenhavam monstros marinhos — eram lendas, não animais reais.",
            },
            "topic_id": "portuguese_navigation",
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
            {"type": "heading", "content": {"level": 3, "text": "1. Pré-história"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🎨", "title": "Pinturas rupestres", "text": "Registram caça e vida cotidiana"},
                        {"icon": "🏃", "title": "Caçadores-coletores", "text": "Nômades · pedra lascada"},
                        {"icon": "🔍", "title": "Arqueologia", "text": "Estuda vestígios do passado"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. Umbu e Humaitá"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🌲", "title": "Umbu", "text": "Pampa · pinhão · boleadeira"},
                        {"icon": "🍇", "title": "Humaitá", "text": "Sul/Sudeste · frutos silvestres"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Sambaquis"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🐚", "title": "Significado", "text": "Amontoado de conchas (tupi)"},
                        {"icon": "🏖️", "title": "Onde", "text": "Litoral brasileiro"},
                        {"icon": "🦪", "title": "Alimentação", "text": "Moluscos e peixes"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Ceramistas"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["", "Nômade", "Sedentário"],
                    "rows": [
                        ["Onde", "Muda de lugar", "Amazônia — Santarém, Marajó"],
                        ["Trabalho", "Caça e coleta", "Cerâmica de argila"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Tupi-Guarani"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🌽", "title": "Coivara", "text": "Roça na mata — milho, mandioca"},
                        {"icon": "🏘️", "title": "Aldeias", "text": "Casas circulares"},
                        {"icon": "📈", "title": "Linha do tempo", "text": "Caçadores → pescadores → ceramistas → agricultores"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "6. Comércio e especiarias"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🧂", "title": "Especiarias", "text": "Canela, cravo, pimenta…"},
                        {"icon": "💰", "title": "Valor", "text": "Conservar, temperar, curar, perfumar"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "7. Viajantes"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["Nome", "Destaque"],
                    "rows": [
                        ["Marco Polo", "Rota da Seda"],
                        ["Ibn Battuta", "Viagens pelo mundo islâmico"],
                        ["Zheng He", "Expedições chinesas"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "8. Navegações portuguesas"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "⛵", "title": "Caravela / Nau", "text": "Embarcações do século XV"},
                        {"icon": "🧭", "title": "Bússola", "text": "Indica direções (N, S, L, O)"},
                        {"icon": "🏰", "title": "1415", "text": "Conquista de Ceuta"},
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "Sambaqui não é montanha natural — é amontoado de conchas feito por seres humanos.",
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
                "id": "hist-pe-001",
                "type": "multiple_choice",
                "topic": "prehistory",
                "question": (
                    "Leia as afirmativas sobre os primeiros grupos no território brasileiro:\n"
                    "I. Eram caçadores e coletores que mudavam de lugar com frequência.\n"
                    "II. Deixaram pinturas rupestres em cavernas e rochas.\n"
                    "III. Construíam grandes cidades de pedra como os maias.\n"
                    "IV. Arqueólogos encontram vestígios como pedras lascadas e restos de fogueiras.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Cidades maias ficam na América Central, não no Brasil antigo.",
                "difficulty": "intermediate",
                "source_assets": sa("page-011.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-002",
                "type": "multiple_choice",
                "topic": "sambaquis",
                "question": "A palavra sambaqui, de origem tupi, significa:",
                "options": [
                    "Montanha natural formada só pela natureza",
                    "Amontoado de conchas",
                    "Cidade indígena de pedra",
                    "Tipo de canoa de madeira",
                ],
                "correct_answer": 1,
                "explanation": "Sambaqui = amontoado de conchas deixado por grupos que viviam no litoral.",
                "difficulty": "basic",
                "source_assets": sa("page-017.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-003",
                "type": "multiple_choice",
                "topic": "sambaquis",
                "question": (
                    "Leia as afirmativas sobre os sambaquieiros:\n"
                    "I. Viviam principalmente no litoral brasileiro.\n"
                    "II. Alimentavam-se muito de moluscos e peixes.\n"
                    "III. Ergueram sambaquis apenas como decoração, sem relação com sua vida.\n"
                    "IV. Arqueólogos estudam sambaquis para entender o passado.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e IV", "II, III e IV", "III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Sambaquis registram hábitos alimentares e sepultamentos — não são só decoração.",
                "difficulty": "intermediate",
                "source_assets": sa("page-021.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-004",
                "type": "multiple_choice",
                "topic": "umbu_humaita",
                "question": (
                    "As Tradições Umbu e Humaitá são estudadas principalmente em qual região do Brasil?"
                ),
                "options": ["Amazônia", "Nordeste", "Sul e Sudeste", "Centro-Oeste"],
                "correct_answer": 2,
                "explanation": "Umbu (Pampa) e Humaitá estão associadas ao Sul e Sudeste.",
                "difficulty": "basic",
                "source_assets": sa("page-016.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-005",
                "type": "multiple_choice",
                "topic": "tupi_guarani",
                "question": (
                    "Leia as afirmativas sobre os Tupi-Guarani:\n"
                    "I. Cultivavam milho e mandioca em áreas chamadas coivara.\n"
                    "II. Viviam em aldeias com moradias circulares.\n"
                    "III. Nunca usavam canoas para se deslocar.\n"
                    "IV. Migraram da Amazônia para outras partes do Brasil.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e IV", "I e III", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e IV corretas. Eram bons navegadores e usavam canoas (III está errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-020.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-006",
                "type": "multiple_choice",
                "topic": "ceramists",
                "question": "Os ceramistas da Amazônia, em Santarém e Marajó, diferiam dos caçadores-coletores nômades porque:",
                "options": [
                    "Não usavam fogo",
                    "Viviam de forma mais sedentária e produziam vasos de argila",
                    "Não pescavam",
                    "Não deixaram nenhum vestígio arqueológico",
                ],
                "correct_answer": 1,
                "explanation": "Ceramistas eram sedentários e produziam cerâmica — diferente dos nômades.",
                "difficulty": "basic",
                "source_assets": sa("page-026.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-007",
                "type": "multiple_choice",
                "topic": "commerce_spices",
                "question": (
                    "No século XV, as especiarias eram muito procuradas pelos europeus porque:"
                ),
                "options": [
                    "Serviam apenas como enfeite, sem utilidade prática",
                    "Ajudavam a conservar alimentos, temperar, perfumar e até curar doenças",
                    "Cresciam em abundância na Europa",
                    "Eram usadas somente para construir navios",
                ],
                "correct_answer": 1,
                "explanation": "Especiarias tinham alto valor por conservação, sabor, perfume e uso medicinal.",
                "difficulty": "basic",
                "source_assets": sa("page-035.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-008",
                "type": "multiple_choice",
                "topic": "travelers",
                "question": (
                    "Marco Polo foi um viajante veneziano famoso por:"
                ),
                "options": [
                    "Comandar expedições chinesas com juncos",
                    "Relatar viagens pela Rota da Seda até a Ásia",
                    "Descobrir o Brasil em 1500",
                    "Inventar a bússola",
                ],
                "correct_answer": 1,
                "explanation": "Marco Polo (séc. XIII) viajou até a China e descreveu a Rota da Seda.",
                "difficulty": "basic",
                "source_assets": sa("page-033.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-009",
                "type": "multiple_choice",
                "topic": "travelers",
                "question": (
                    "Leia as afirmativas sobre grandes viajantes:\n"
                    "I. Ibn Battuta nasceu no Marrocos e viajou por África, Ásia e Europa.\n"
                    "II. Zheng He comandou expedições chinesas com grandes juncos.\n"
                    "III. Marco Polo só viajou dentro da Itália.\n"
                    "IV. Esses viajantes mostram que o comércio e as trocas existiam antes das navegações portuguesas.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Marco Polo viajou até a Ásia (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-039.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-010",
                "type": "multiple_choice",
                "topic": "portuguese_navigation",
                "question": (
                    "Leia as afirmativas sobre embarcações portuguesas no século XV:\n"
                    "I. A caravela era menor e mais ágil que a nau.\n"
                    "II. A nau era maior e podia levar mais carga e tripulação.\n"
                    "III. Caravelas e naus eram iguais em tamanho e função.\n"
                    "IV. Essas embarcações foram usadas nas Grandes Navegações.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Caravela e nau tinham tamanhos e funções diferentes (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-012.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-011",
                "type": "multiple_choice",
                "topic": "portuguese_navigation",
                "question": "A bússola era um instrumento importante para os navegadores porque:",
                "options": [
                    "Mede a temperatura do mar",
                    "Indica as direções cardeais (norte, sul, leste, oeste)",
                    "Substitui completamente o GPS moderno",
                    "Serve apenas para decorar o navio",
                ],
                "correct_answer": 1,
                "explanation": "A bússola ajuda a saber a direção da navegação.",
                "difficulty": "basic",
                "source_assets": sa("page-025.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-012",
                "type": "multiple_choice",
                "topic": "portuguese_navigation",
                "question": (
                    "Em 1415, os portugueses conquistaram Ceuta. Esse fato é importante porque:"
                ),
                "options": [
                    "Foi a primeira grande conquista portuguesa fora da Península Ibérica",
                    "Marcou o fim das Grandes Navegações",
                    "Aconteceu no Brasil",
                    "Foi quando Marco Polo nasceu",
                ],
                "correct_answer": 0,
                "explanation": "Ceuta (1415), no norte da África, foi marco inicial da expansão marítima portuguesa.",
                "difficulty": "intermediate",
                "source_assets": sa("page-037.jpg"),
                "section": "final_quiz",
            },
        ],
    }
