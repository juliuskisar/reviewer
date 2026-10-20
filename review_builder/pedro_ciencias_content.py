"""Conteúdo pedagógico da revisão Pedro — Ciências PE 2º trimestre."""

from __future__ import annotations

REVIEW_ID = "pedro-pe-ciencias-2tri"
ASSET_PREFIX = "assets/pedro_pe_ciencias_2_tri"


def _src(page: str) -> dict:
    return {
        "asset": f"{ASSET_PREFIX}/{page}",
        "origin_type": "observed",
        "evidence": [f"Caderno de Ciências — {page}"],
    }


def build_content() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Ciências — PE 2º Trimestre",
        "subtitle": "Pedro · 6º ano · Módulos 9, 10, 11 e 12",
        "language": "pt-BR",
        "discipline": "Ciências",
        "grade": "6º ano",
        "metadata": {
            "student_name": "Pedro",
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
                    "text": "Resíduos sólidos e seus destinos, reciclagem e os 4 Rs, poluição e saúde "
                    "pública, vetores de doenças e saneamento básico — tratamento de água e esgoto. "
                    "Reserve cerca de 55 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🗑️", "title": "Resíduos", "text": "RSU · RSS · lixão · aterro"},
                        {"icon": "♻️", "title": "Reciclagem", "text": "4 Rs · coleta seletiva · PNRS"},
                        {"icon": "☣️", "title": "Poluição", "text": "Chorume · metais pesados · gases"},
                        {"icon": "🦟", "title": "Vetores", "text": "Mosquito · rato · mosca · barata"},
                        {"icon": "💧", "title": "Água", "text": "ETA · potabilidade · poços"},
                        {"icon": "🚰", "title": "Esgoto", "text": "ETE · fossa séptica · saneamento"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 9 — Resíduos sólidos e destinos",
                        "Módulo 10 — Repensar, reduzir, reutilizar, reciclar",
                        "Módulo 11 — Poluição e saúde pública",
                        "Módulo 12 — Saneamento básico",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Leia os cards e tabelas com calma.",
                            "tip": "Relacione cada destino de resíduo (lixão, aterro, reciclagem) com seus riscos.",
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
            *_topic_solid_waste(),
            *_topic_waste_destinations(),
            *_topic_recycling(),
            *_topic_pollution_health(),
            *_topic_vectors_diseases(),
            *_topic_health_sanitation(),
            *_topic_water_treatment(),
            *_topic_sewage_sanitation(),
        ],
    }


def _topic_solid_waste() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Resíduos sólidos: RSU e RSS"}, "topic_id": "solid_waste"},
        {
            "type": "paragraph",
            "content": {
                "text": "Resíduo sólido é tudo que perdeu a utilidade — cascas, embalagens, pilhas usadas. "
                "O termo é mais preciso que «lixo», porque muitos materiais ainda têm valor. "
                "No Brasil, cada pessoa produz em média mais de 1 kg de resíduos por dia.",
            },
            "topic_id": "solid_waste",
            "sources": [_src("page-005.jpg"), _src("page-014.jpg"), _src("page-027.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Dois tipos principais de resíduo",
                "headers": ["", "RSU", "RSS"],
                "rows": [
                    ["Nome", "Resíduos Sólidos Urbanos", "Resíduos de Serviços de Saúde"],
                    ["Origem", "Casas, comércio, indústria, varrição", "Hospitais, clínicas, farmácias, tatuagem"],
                    ["Exemplos", "Embalagens, restos de comida, papel", "Seringas, medicamentos, material contaminado"],
                ],
            },
            "topic_id": "solid_waste",
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🥗", "title": "Matéria orgânica", "text": "Maior parte dos RSU (~45%) — restos de comida e podas"},
                    {"icon": "🧴", "title": "Plástico", "text": "Segundo material mais comum nos RSU (~17%)"},
                    {"icon": "📦", "title": "Papel e vidro", "text": "Podem virar matéria-prima na reciclagem"},
                ],
            },
            "topic_id": "solid_waste",
        },
    ]


def _topic_waste_destinations() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "2. Destinos dos resíduos"}, "topic_id": "waste_destinations"},
        {
            "type": "paragraph",
            "content": {
                "text": "Resíduos podem ir para lixão, aterro sanitário, aterro controlado, incinerador, "
                "usina de compostagem, biodigestor ou centro de triagem. Cada destino tem impactos "
                "diferentes no solo, na água e no ar.",
            },
            "topic_id": "waste_destinations",
            "sources": [_src("page-027.jpg"), _src("page-033.jpg"), _src("page-008.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Lixão x aterro sanitário x aterro controlado",
                "headers": ["", "Lixão", "Aterro controlado", "Aterro sanitário"],
                "rows": [
                    ["Proteção do solo", "Nenhuma — chorume no lençol freático", "Parcial — manta em alguns casos", "Manta plástica + argila + coleta de chorume"],
                    ["Gases", "Liberados sem controle", "Chaminés em parte dos casos", "Coletados e tratados (biogás)"],
                    ["Risco", "Máximo — vetores e doenças", "Intermediário", "Menor — normas de segurança"],
                ],
            },
            "topic_id": "waste_destinations",
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "💧", "title": "Chorume", "text": "Líquido escuro da decomposição — contamina solo e água"},
                    {"icon": "🔥", "title": "Incineração", "text": "Queima acima de 900 °C — reduz volume; usada sobretudo para RSS"},
                    {"icon": "🌱", "title": "Compostagem", "text": "Matéria orgânica vira adubo — leiras ou biodigestores"},
                    {"icon": "🧫", "title": "Autoclave", "text": "Vapor esteriliza RSS antes do descarte final"},
                ],
            },
            "topic_id": "waste_destinations",
        },
    ]


def _topic_recycling() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "3. Reciclagem e os 4 Rs"}, "topic_id": "recycling"},
        {
            "type": "paragraph",
            "content": {
                "text": "Reciclar é transformar resíduos em matéria-prima para novos produtos. "
                "Antes disso, convém repensar hábitos de consumo, reduzir o que compramos, "
                "reutilizar o que ainda serve e só então reciclar. A PNRS (2010) divide "
                "responsabilidades entre governo, empresas e cidadãos.",
            },
            "topic_id": "recycling",
            "sources": [_src("page-010.jpg"), _src("page-018.jpg"), _src("page-039.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🤔", "title": "Repensar", "text": "Refletir antes de comprar ou jogar fora"},
                    {"icon": "📉", "title": "Reduzir", "text": "Consumir só o necessário"},
                    {"icon": "🔄", "title": "Reutilizar", "text": "Dar nova função a objetos inteiros"},
                    {"icon": "♻️", "title": "Reciclar", "text": "Transformar material em produto novo"},
                ],
            },
            "topic_id": "recycling",
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Coleta seletiva — cores das lixeiras",
                "headers": ["Cor", "Material"],
                "rows": [
                    ["Azul", "Papel e papelão"],
                    ["Verde", "Vidro"],
                    ["Amarela", "Metais"],
                    ["Vermelha", "Plástico"],
                    ["Cinza", "Não recicláveis"],
                ],
            },
            "topic_id": "recycling",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Logística reversa:",
                "text": "Fabricantes devem recolher produtos como pilhas, lâmpadas, eletrônicos "
                "e embalagens de agrotóxicos após o uso.",
            },
            "topic_id": "recycling",
        },
    ]


def _topic_pollution_health() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "4. Poluição e saúde"}, "topic_id": "pollution_health"},
        {
            "type": "paragraph",
            "content": {
                "text": "Resíduos mal dispostos poluem ar, solo e água. O chorume do lixão pode atingir "
                "o lençol freático. Gases da decomposição e queima causam doenças respiratórias. "
                "Metais pesados (chumbo, mercúrio, cádmio) se acumulam no corpo e na cadeia alimentar.",
            },
            "topic_id": "pollution_health",
            "sources": [_src("page-003.jpg"), _src("page-012.jpg"), _src("page-032.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "☣️", "title": "Substâncias tóxicas", "text": "Agrotóxicos, óleo, pneus queimados — danificam seres vivos"},
                    {"icon": "🫁", "title": "Respiratório", "text": "Asma, rinite — gases e partículas no ar"},
                    {"icon": "🖐️", "title": "Pele", "text": "Dermatite e micoses — contato direto com resíduos"},
                    {"icon": "🔋", "title": "Pilhas", "text": "Nunca no lixo comum — pontos de coleta específicos"},
                ],
            },
            "topic_id": "pollution_health",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Cadeia alimentar:",
                "text": "Metais do lixão → solo/água → plantas → peixes → pessoas. "
                "Por isso a tirinha do atum pergunta «Como está o mercúrio?» — resposta: «Pesado.»",
            },
            "topic_id": "pollution_health",
        },
    ]


def _topic_vectors_diseases() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "5. Vetores e doenças"}, "topic_id": "vectors_diseases"},
        {
            "type": "paragraph",
            "content": {
                "text": "Animais encontram comida e abrigo no lixo e podem transmitir microrganismos "
                "causadores de doenças. O vetor (ou portador) transporta o agente causador "
                "até outro ser vivo.",
            },
            "topic_id": "vectors_diseases",
            "sources": [_src("page-016.jpg"), _src("page-030.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Exemplos do caderno",
                "headers": ["Doença", "Vetor", "Agente"],
                "rows": [
                    ["Dengue, zika, chikungunya", "Mosquito Aedes aegypti", "Vírus"],
                    ["Amebíase", "Mosca", "Protozoário"],
                    ["Febre tifoide", "Barata", "Bactéria"],
                    ["Tifo endêmico", "Rato (pulga)", "Bactéria"],
                    ["Criptococose", "Pombo", "Fungo"],
                ],
            },
            "topic_id": "vectors_diseases",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Trabalhadores:",
                "text": "Catadores, garis e recicladores precisam de EPI — luvas, máscara e óculos.",
            },
            "topic_id": "vectors_diseases",
        },
    ]


def _topic_health_sanitation() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "6. Saúde e saneamento básico"}, "topic_id": "health_sanitation"},
        {
            "type": "paragraph",
            "content": {
                "text": "Saúde, segundo a OMS, é bem-estar físico, mental e social — não apenas "
                "ausência de doença. Saneamento básico inclui água tratada, coleta e "
                "tratamento de esgoto e coleta de resíduos. Sem isso, aumentam doenças "
                "de veiculação hídrica e a mortalidade infantil.",
            },
            "topic_id": "health_sanitation",
            "sources": [_src("page-034.jpg"), _src("page-013.jpg"), _src("page-017.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "💪", "title": "Físico", "text": "Corpo sem doenças — alimentação, exercício"},
                    {"icon": "🧠", "title": "Mental", "text": "Equilíbrio emocional — sem excesso de estresse"},
                    {"icon": "👥", "title": "Social", "text": "Moradia, educação, trabalho, serviços de saúde"},
                    {"icon": "🚿", "title": "Saneamento", "text": "Água potável + esgoto tratado + lixo coletado"},
                ],
            },
            "topic_id": "health_sanitation",
        },
    ]


def _topic_water_treatment() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "7. Tratamento de água (ETA)"}, "topic_id": "water_treatment"},
        {
            "type": "paragraph",
            "content": {
                "text": "Antes de chegar às torneiras, a água de rios, represas ou poços passa por "
                "uma Estação de Tratamento de Água (ETA). O objetivo é torná-la potável — "
                "livre de poluentes, sedimentos e microrganismos nocivos.",
            },
            "topic_id": "water_treatment",
            "sources": [_src("page-029.jpg"), _src("page-031.jpg"), _src("page-035.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "1️⃣", "title": "Gradeamento", "text": "Retém detritos grandes (papel, galhos)"},
                    {"icon": "2️⃣", "title": "Floculação", "text": "Químicos formam flocos com partículas"},
                    {"icon": "3️⃣", "title": "Decantação", "text": "Flocos descem — forma lodo"},
                    {"icon": "4️⃣", "title": "Filtração", "text": "Areia e cascalho removem partículas finas"},
                    {"icon": "5️⃣", "title": "Desinfecção", "text": "Cloro mata microrganismos — água potável"},
                    {"icon": "🦷", "title": "Fluoretação", "text": "Flúor previne cáries — não trata a água"},
                ],
            },
            "topic_id": "water_treatment",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Poços:",
                "text": "Água de poço artesiano vem de aquífero confinado. Mesmo limpa, "
                "precisa de análise — pode conter patógenos ou poluentes.",
            },
            "topic_id": "water_treatment",
            "sources": [_src("page-015.jpg")],
        },
    ]


def _topic_sewage_sanitation() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "8. Esgoto e saneamento no Brasil"}, "topic_id": "sewage_sanitation"},
        {
            "type": "paragraph",
            "content": {
                "text": "O esgoto doméstico segue por tubulações até a rede pública ou fossa séptica. "
                "Na ETE (Estação de Tratamento de Esgoto), passa por gradeamento, caixa de areia, "
                "decantação, aeração e decantadores secundários. Só então pode ser devolvido ao rio "
                "ou reutilizado.",
            },
            "topic_id": "sewage_sanitation",
            "sources": [_src("page-004.jpg"), _src("page-038.jpg"), _src("page-028.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Índices de saneamento por região (aproximados, caderno)",
                "headers": ["Região", "Água tratada", "Coleta esgoto", "Tratamento esgoto"],
                "rows": [
                    ["Norte", "58,9%", "13,1%", "21,4%"],
                    ["Nordeste", "74,9%", "30,3%", "34,1%"],
                    ["Centro-Oeste", "90,9%", "59,5%", "58,5%"],
                    ["Sudeste", "91,3%", "80,5%", "55,6%"],
                    ["Sul", "91,0%", "47,4%", "46,7%"],
                ],
            },
            "topic_id": "sewage_sanitation",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Desigualdade:",
                "text": "O Brasil tem mais acesso a água tratada do que a coleta e tratamento "
                "de esgoto. A região Norte apresenta os menores índices.",
            },
            "topic_id": "sewage_sanitation",
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
            {"type": "heading", "content": {"level": 3, "text": "1. Resíduos sólidos"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🏠", "title": "RSU", "text": "Casas, comércio, indústria"},
                        {"icon": "🏥", "title": "RSS", "text": "Hospitais, clínicas, farmácias"},
                        {"icon": "📊", "title": "Brasil", "text": "~1 kg/pessoa/dia · orgânica = maior parte"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. Destinos"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["Destino", "Característica"],
                    "rows": [
                        ["Lixão", "Sem proteção — máximo risco"],
                        ["Aterro sanitário", "Impermeabilizado — coleta chorume e gases"],
                        ["Incineração", "Queima — RSS e resíduos especiais"],
                        ["Compostagem", "Orgânico → adubo"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Reciclagem"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "4️⃣", "title": "4 Rs", "text": "Repensar · reduzir · reutilizar · reciclar"},
                        {"icon": "🔵", "title": "Azul", "text": "Papel"},
                        {"icon": "🟢", "title": "Verde", "text": "Vidro"},
                        {"icon": "🟡", "title": "Amarela", "text": "Metais"},
                        {"icon": "🔴", "title": "Vermelha", "text": "Plástico"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Poluição"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "💧", "title": "Chorume", "text": "Contamina lençol freático"},
                        {"icon": "⚗️", "title": "Metais pesados", "text": "Chumbo, mercúrio, cádmio — acumulam no corpo"},
                        {"icon": "🔋", "title": "Pilhas", "text": "Descarte em coleta específica"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Vetores"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["Vetor", "Doença"],
                    "rows": [
                        ["Aedes aegypti", "Dengue, zika"],
                        ["Mosca", "Amebíase"],
                        ["Barata", "Febre tifoide"],
                        ["Rato", "Tifo endêmico"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "6. Saúde"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "❤️", "title": "Saúde OMS", "text": "Físico + mental + social"},
                        {"icon": "🚿", "title": "Saneamento", "text": "Água + esgoto + resíduos"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "7. ETA"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "➡️", "title": "Etapas", "text": "Gradeamento → floculação → decantação → filtração → cloro"},
                        {"icon": "✅", "title": "Potável", "text": "Segura para beber"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "8. ETE e Brasil"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🏭", "title": "ETE", "text": "Gradeamento → aeração → lodo → água tratada"},
                        {"icon": "🗺️", "title": "Desigualdade", "text": "Norte com menores índices de esgoto"},
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "Fluoretação não trata a água — só ajuda a prevenir cáries. "
                    "Quem elimina microrganismos é a desinfecção com cloro.",
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
                "id": "ci-pe-001",
                "type": "multiple_choice",
                "topic": "solid_waste",
                "question": "Resíduos Sólidos Urbanos (RSU) são produzidos principalmente por:",
                "options": [
                    "Hospitais e clínicas veterinárias apenas",
                    "Atividades humanas em ambientes urbanos — casas, comércio e indústria",
                    "Somente restos de podas em florestas nativas",
                    "Exclusivamente material radioativo",
                ],
                "correct_answer": 1,
                "explanation": "RSU vem de cidades — doméstico, comercial, industrial, varrição e podas urbanas.",
                "difficulty": "basic",
                "source_assets": sa("page-014.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-002",
                "type": "multiple_choice",
                "topic": "solid_waste",
                "question": (
                    "Leia as afirmativas sobre resíduos sólidos:\n"
                    "I. RSS incluem material de hospitais e farmácias.\n"
                    "II. Matéria orgânica é o componente mais abundante dos RSU no Brasil.\n"
                    "III. Todo resíduo sólido deve ir para o lixão.\n"
                    "IV. Cada brasileiro produz, em média, mais de 1 kg de resíduos por dia.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e IV", "I e III", "II e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e IV corretas. Resíduos podem ir a reciclagem, compostagem, aterro etc. (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-001.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-003",
                "type": "multiple_choice",
                "topic": "waste_destinations",
                "question": "O chorume produzido em um lixão é:",
                "options": [
                    "Água limpa que pode ser bebida após filtragem simples",
                    "Líquido escuro da decomposição que contamina solo e lençol freático",
                    "Gás metano usado diretamente como combustível doméstico sem tratamento",
                    "Adubo orgânico pronto para uso imediato em hortas",
                ],
                "correct_answer": 1,
                "explanation": "Chorume é poluente — no lixão escorre sem controle para o solo e a água subterrânea.",
                "difficulty": "basic",
                "source_assets": sa("page-033.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-004",
                "type": "multiple_choice",
                "topic": "waste_destinations",
                "question": (
                    "Leia as afirmativas sobre destinos de resíduos:\n"
                    "I. Aterros sanitários possuem manta impermeabilizante e coleta de chorume.\n"
                    "II. Incineração é indicada principalmente para resíduos de serviços de saúde.\n"
                    "III. Compostagem transforma matéria orgânica em adubo.\n"
                    "IV. Lixões são a forma mais segura de dispor resíduos urbanos.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e III", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Lixão é o destino mais perigoso (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-008.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-005",
                "type": "multiple_choice",
                "topic": "recycling",
                "question": "Na coleta seletiva, embalagens de plástico devem ser descartadas na lixeira:",
                "options": ["Azul", "Verde", "Vermelha", "Cinza"],
                "correct_answer": 2,
                "explanation": "Vermelha = plástico; azul = papel; verde = vidro; amarela = metais.",
                "difficulty": "basic",
                "source_assets": sa("page-025.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-006",
                "type": "multiple_choice",
                "topic": "recycling",
                "question": (
                    "Leia as afirmativas sobre reciclagem:\n"
                    "I. Reciclar reduz a extração de matérias-primas naturais.\n"
                    "II. A PNRS estabelece responsabilidade compartilhada na gestão de resíduos.\n"
                    "III. Logística reversa obriga fabricantes a recolher produtos como pilhas e eletrônicos.\n"
                    "IV. Todos os resíduos sólidos podem ser 100% reciclados sem perdas.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, II e III", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e III corretas. Reciclagem não é solução mágica — nem tudo é reciclável (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-039.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-007",
                "type": "multiple_choice",
                "topic": "pollution_health",
                "question": (
                    "Por que pilhas e baterias não devem ser jogadas no lixo comum?"
                ),
                "options": [
                    "Porque ocupam muito espaço no aterro",
                    "Porque contêm metais pesados que contaminam solo e água",
                    "Porque são feitas apenas de plástico biodegradável",
                    "Porque não têm nenhum componente tóxico",
                ],
                "correct_answer": 1,
                "explanation": "Chumbo, mercúrio, cádmio e lítio podem causar doenças graves se liberados no ambiente.",
                "difficulty": "basic",
                "source_assets": sa("page-012.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-008",
                "type": "multiple_choice",
                "topic": "pollution_health",
                "question": (
                    "Leia as afirmativas sobre poluição por resíduos:\n"
                    "I. Queima de pneus libera gases tóxicos no ar.\n"
                    "II. Metais pesados do lixão podem chegar aos peixes pela cadeia alimentar.\n"
                    "III. Contato com resíduos pode causar dermatite e micoses.\n"
                    "IV. Resíduos sólidos nunca afetam a qualidade do ar.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "III e IV", "I, II e III", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e III corretas. Decomposição e queima poluem o ar (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-009",
                "type": "multiple_choice",
                "topic": "vectors_diseases",
                "question": "A dengue é transmitida pelo mosquito:",
                "options": ["Anopheles", "Aedes aegypti", "Culex", "Urubu"],
                "correct_answer": 1,
                "explanation": "Aedes aegypti também transmite zika e chikungunya — agente causador: vírus.",
                "difficulty": "basic",
                "source_assets": sa("page-030.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-010",
                "type": "multiple_choice",
                "topic": "vectors_diseases",
                "question": (
                    "Leia as afirmativas sobre vetores:\n"
                    "I. Mosca pode transmitir amebíase por contato com alimentos.\n"
                    "II. Barata pode transmitir febre tifoide.\n"
                    "III. Rato transmite tifo endêmico por meio de pulgas.\n"
                    "IV. Pombo nunca está associado a doenças humanas.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "I e III", "I, II e III", "II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e III corretas. Pombo pode transmitir criptococose (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-030.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-011",
                "type": "multiple_choice",
                "topic": "health_sanitation",
                "question": "Segundo a OMS, saúde é:",
                "options": [
                    "Apenas a ausência de doenças físicas",
                    "Bem-estar físico, mental e social completo",
                    "Ter acesso somente a medicamentos",
                    "Viver sem nunca sentir cansaço ou estresse",
                ],
                "correct_answer": 1,
                "explanation": "Saúde inclui corpo, mente e relações sociais — não é só «não estar doente».",
                "difficulty": "basic",
                "source_assets": sa("page-034.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-012",
                "type": "multiple_choice",
                "topic": "water_treatment",
                "question": "Na ETA, a etapa que elimina microrganismos nocivos usando cloro chama-se:",
                "options": ["Gradeamento", "Floculação", "Desinfecção", "Fluoretação"],
                "correct_answer": 2,
                "explanation": "Desinfecção (cloro) torna a água potável. Fluoretação previne cáries, mas não desinfeta.",
                "difficulty": "basic",
                "source_assets": sa("page-029.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-013",
                "type": "multiple_choice",
                "topic": "water_treatment",
                "question": (
                    "Leia as afirmativas sobre tratamento de água:\n"
                    "I. Gradeamento retém detritos grandes como papel e galhos.\n"
                    "II. Decantação faz os flocos de impurezas descerem.\n"
                    "III. Fluoretação substitui a desinfecção com cloro.\n"
                    "IV. Filtração passa a água por camadas de areia e cascalho.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Flúor complementa, mas não substitui o cloro (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-031.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-014",
                "type": "multiple_choice",
                "topic": "sewage_sanitation",
                "question": "Na ETE, a etapa em que bolhas de ar promovem o crescimento de microrganismos que consomem matéria orgânica chama-se:",
                "options": ["Gradeamento", "Aeração", "Incineração", "Compostagem"],
                "correct_answer": 1,
                "explanation": "No tanque de aeração, oxigênio alimenta bactérias que degradam o esgoto.",
                "difficulty": "basic",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-015",
                "type": "multiple_choice",
                "topic": "sewage_sanitation",
                "question": (
                    "Sobre saneamento básico no Brasil, analise:\n"
                    "I. A região Norte tem os menores índices de coleta de esgoto.\n"
                    "II. Há mais acesso a água tratada do que a tratamento de esgoto.\n"
                    "III. Esgoto a céu aberto aumenta doenças de veiculação hídrica.\n"
                    "IV. Fossas sépticas substituem completamente a necessidade de ETEs em cidades.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e III", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Fossas são alternativa local — cidades precisam de rede e ETE (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-028.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-016",
                "type": "multiple_choice",
                "topic": "recycling",
                "question": (
                    "Qual sequência representa corretamente os 4 Rs na ordem de prioridade "
                    "recomendada pelo caderno?"
                ),
                "options": [
                    "Reciclar → reduzir → repensar → reutilizar",
                    "Repensar → reduzir → reutilizar → reciclar",
                    "Reduzir → reciclar → repensar → reutilizar",
                    "Reutilizar → reciclar → reduzir → repensar",
                ],
                "correct_answer": 1,
                "explanation": "Primeiro muda o hábito (repensar/reduzir), depois reutiliza e só então recicla.",
                "difficulty": "basic",
                "source_assets": sa("page-037.jpg"),
                "section": "final_quiz",
            },
        ],
    }
