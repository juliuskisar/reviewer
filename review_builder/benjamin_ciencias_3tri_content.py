"""Conteúdo pedagógico da revisão Benjamin — Ciências PE 3º trimestre (Módulos 10–13)."""

from __future__ import annotations

REVIEW_ID = "benjamin-pe-ciencias-3tri"
ASSET_PREFIX = "assets/benjamin_pe_ciencias_3_tri"


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
        "title": "Revisão de Ciências — PE 3º Trimestre",
        "subtitle": "Benjamin · 4º ano · Módulos 10, 11, 12 e 13",
        "language": "pt-BR",
        "discipline": "Ciências",
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
                    "text": "Microrganismos, higiene e alimentos seguros, resíduos e compostagem, "
                    "leveduras e fermentação, antibióticos e vacinas — Módulos 10 a 13. "
                    "Reserve cerca de 55 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🦠", "title": "Microrganismos", "text": "Bactérias · vírus · fungos"},
                        {"icon": "🔬", "title": "Laboratório", "text": "Petri · meio de cultura · microscópio"},
                        {"icon": "🧼", "title": "Higiene", "text": "Mãos · cozinha · hortaliças"},
                        {"icon": "♻️", "title": "Resíduos", "text": "Reciclável · orgânico · rejeito"},
                        {"icon": "🪱", "title": "Compostagem", "text": "Decomposição · minhocas · adubo"},
                        {"icon": "🍞", "title": "Leveduras", "text": "Fermentação · pão · etanol"},
                        {"icon": "💊", "title": "Antibióticos", "text": "Bactérias · penicilina · receita"},
                        {"icon": "💉", "title": "Vacinas", "text": "Imunização · calendário · prevenção"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 10 — Os microrganismos",
                        "Módulo 11 — Microrganismos e decomposição",
                        "Módulo 12 — As leveduras",
                        "Módulo 13 — Antibióticos e vacinas",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Leia os cards e tabelas.",
                            "tip": "Relacione o experimento das mãos (amostras A–D) com a higiene do dia a dia.",
                        },
                        {
                            "title": "Revise o Resumo rápido",
                            "panel": "summary",
                            "panel_label": "Resumo rápido",
                            "description": "Percorra os blocos-síntese antes da PE.",
                        },
                        {
                            "title": "Faça os Exercícios",
                            "panel": "exercises",
                            "panel_label": "Exercícios",
                            "description": "Questões no estilo Teste e Atividade do caderno.",
                            "tip": "Antibiótico combate bactérias; gripe é vírus — não confunda!",
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
            *_topic_micro_intro(),
            *_topic_lab_study(),
            *_topic_hand_hygiene(),
            *_topic_food_prevention(),
            *_topic_waste(),
            *_topic_composting(),
            *_topic_yeasts(),
            *_topic_antibiotics_vaccines(),
        ],
    }


def _topic_micro_intro() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Microrganismos ao nosso redor"}, "topic_id": "micro_intro"},
        {
            "type": "paragraph",
            "content": {
                "text": "Microrganismos são seres vivos tão pequenos que não vemos a olho nu. "
                "Incluem bactérias, vírus e alguns fungos. Estão no ar, na água, no solo, "
                "nos alimentos e também na pele, nas unhas e no intestino.",
            },
            "topic_id": "micro_intro",
            "sources": [_src("page-002.jpg"), _src("page-003.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🍞", "title": "Mofo", "text": "Fungo no pão — pode causar vômito e dor"},
                    {"icon": "🦷", "title": "Cárie", "text": "Bactérias produzem ácido que corrói o dente"},
                    {"icon": "🤧", "title": "Gripe e resfriado", "text": "Doenças virais contagiosas"},
                    {"icon": "🪳", "title": "Pragas", "text": "Baratas e moscas espalham microrganismos"},
                ],
            },
            "topic_id": "micro_intro",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Nem tudo é ruim:",
                "text": "Lactobacilos no intestino ajudam na digestão. Muitos microrganismos são benéficos.",
            },
            "topic_id": "micro_intro",
            "sources": [_src("page-003.jpg")],
        },
    ]


def _topic_lab_study() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "2. Investigando microrganismos"}, "topic_id": "lab_study"},
        {
            "type": "paragraph",
            "content": {
                "text": "Fungos e bactérias precisam de alimento, temperatura e umidade favoráveis. "
                "Vírus também dependem de condições adequadas, mas não se alimentam como bactérias e fungos.",
            },
            "topic_id": "lab_study",
            "sources": [_src("page-003.jpg"), _src("page-004.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["", "Bactérias", "Fungos"],
                "rows": [
                    ["Colônias na placa de Petri", "Pontos amarelados", "Aspecto aveludado, como algodão"],
                    ["Meio de cultura", "Substância com nutrientes para crescer", "Igual — favorece multiplicação"],
                ],
            },
            "topic_id": "lab_study",
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🥽", "title": "Segurança", "text": "Avental, máscara, óculos e luvas com amostras perigosas"},
                    {"icon": "🔭", "title": "Microscópio", "text": "Ocular · objetivas · platina"},
                    {"icon": "🧫", "title": "Cultivar", "text": "Crescer amostras em laboratório para estudar"},
                ],
            },
            "topic_id": "lab_study",
            "sources": [_src("page-005.jpg"), _src("page-007.jpg")],
        },
    ]


def _topic_hand_hygiene() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "3. Higiene das mãos e experimentos"}, "topic_id": "hand_hygiene"},
        {
            "type": "paragraph",
            "content": {
                "text": "No caderno você investigou microrganismos na escola (corrimão, maçaneta, carteira) "
                "e nas mãos. O meio de cultura (mingau ou gelatina) oferece alimento para multiplicarem "
                "e formarem colônias visíveis em cerca de cinco dias.",
            },
            "topic_id": "hand_hygiene",
            "sources": [_src("page-006.jpg"), _src("page-008.jpg"), _src("page-009.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Amostra", "Condição das mãos", "O que esperar"],
                "rows": [
                    ["A", "Sem lavar", "Muitas colônias"],
                    ["B", "Só álcool em gel", "Menos que A, mais que C"],
                    ["C", "Água e sabão", "Poucas colônias"],
                    ["D", "Sabão + álcool em gel", "Menor presença de microrganismos"],
                ],
            },
            "topic_id": "hand_hygiene",
            "sources": [_src("page-010.jpg"), _src("page-011.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Lavar bem:",
                "text": "Esfregue por pelo menos 20 segundos: palmas, dorso, entre os dedos, unhas e punhos. "
                "Secar as mãos também é importante — germes se espalham mais em pele molhada.",
            },
            "topic_id": "hand_hygiene",
            "sources": [_src("page-014.jpg"), _src("page-017.jpg")],
        },
    ]


def _topic_food_prevention() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "4. Alimentos seguros e prevenção"}, "topic_id": "food_prevention"},
        {
            "type": "paragraph",
            "content": {
                "text": "Estabelecimentos de alimentos passam por vigilância sanitária. Microrganismos patogênicos "
                "(que causam doença) podem contaminar utensílios e comidas se a cozinha estiver suja: "
                "lixo acumulado, pia suja, carne crua solta, mofo na parede ou animal na bancada.",
            },
            "topic_id": "food_prevention",
            "sources": [_src("page-001.jpg"), _src("page-015.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🥬", "title": "Hortaliças", "text": "Lavar · desinfetar (solução clorada 15 min) · enxaguar · secar"},
                    {"icon": "💧", "title": "Água potável", "text": "Sem impurezas — essencial nos experimentos"},
                    {"icon": "😷", "title": "COVID-19", "text": "Máscara · distância · tosse no cotovelo"},
                ],
            },
            "topic_id": "food_prevention",
            "sources": [_src("page-014.jpg"), _src("page-016.jpg"), _src("page-018.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Sabão ou álcool em gel?",
                "text": "Os dois ajudam, mas sabão e água removem sujeira visível. "
                "O gel mata coronavírus, porém não funciona bem contra todos os vírus e bactérias.",
            },
            "topic_id": "food_prevention",
            "sources": [_src("page-017.jpg")],
        },
    ]


def _topic_waste() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "5. Lixo, resíduos e decomposição"}, "topic_id": "waste"},
        {
            "type": "paragraph",
            "content": {
                "text": "Lixo (rejeito) não tem mais utilidade: papel sujo, fraldas, esponja. "
                "Resíduos podem ser reaproveitados. Vidro, plástico, papel e metal são recicláveis. "
                "Restos de comida são orgânicos — mais da metade do lixo doméstico.",
            },
            "topic_id": "waste",
            "sources": [_src("page-020.jpg"), _src("page-022.jpg"), _src("page-023.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["", "Lixão", "Aterro sanitário"],
                "rows": [
                    ["Como é", "Montes de lixo a céu aberto", "Local preparado para reduzir poluição"],
                    ["Problema", "Atrai moscas, ratos, urubus — doenças", "Mais controlado que o lixão"],
                ],
            },
            "topic_id": "waste",
        },
        {
            "type": "callout",
            "content": {
                "variant": "info",
                "title": "Revolução dos baldinhos:",
                "text": "Na comunidade Chico Mendes (Florianópolis), famílias passaram a separar orgânicos "
                "em baldinhos para compostagem — menos ratos e mais horta para todos.",
            },
            "topic_id": "waste",
            "sources": [_src("page-027.jpg"), _src("page-026.jpg")],
        },
    ]


def _topic_composting() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "6. Compostagem"}, "topic_id": "composting"},
        {
            "type": "paragraph",
            "content": {
                "text": "Compostagem transforma resíduos orgânicos em adubo. Na natureza, fungos e bactérias "
                "decompõem folhas e animais mortos, reciclando nutrientes para as plantas.",
            },
            "topic_id": "composting",
            "sources": [_src("page-028.jpg"), _src("page-034.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🌡️", "title": "Condições", "text": "Matéria orgânica · oxigênio · umidade · temperatura (5–60 °C)"},
                    {"icon": "🪱", "title": "Minhocas", "text": "Cavam túneis (ar) e produzem húmus rico em nutrientes"},
                    {"icon": "🪣", "title": "Composteira", "text": "Caixa de madeira, buraco no solo ou baldes empilhados"},
                    {"icon": "💧", "title": "Chorume", "text": "Líquido do balde 1 — diluir 1:10 antes de usar nas plantas"},
                ],
            },
            "topic_id": "composting",
            "sources": [_src("page-029.jpg"), _src("page-030.jpg"), _src("page-031.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Não coloque na composteira:",
                "text": "Comida pronta temperada, carne, queijo, fezes, papel, plantas doentes, "
                "cítricos em excesso, alho e cebola (incomodam minhocas).",
            },
            "topic_id": "composting",
            "sources": [_src("page-032.jpg")],
        },
    ]


def _topic_yeasts() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "7. Leveduras e fermentação"}, "topic_id": "yeasts"},
        {
            "type": "paragraph",
            "content": {
                "text": "Fermento biológico contém leveduras — fungos microscópicos (Saccharomyces cerevisiae). "
                "Na fermentação, a levedura usa amido ou açúcar da massa e libera gás carbônico e álcool. "
                "O gás forma bolhas e faz o pão crescer; no forno o álcool evapora.",
            },
            "topic_id": "yeasts",
            "sources": [_src("page-038.jpg"), _src("page-039.jpg"), _src("page-041.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["", "Fermento biológico", "Fermento químico"],
                "rows": [
                    ["O que é", "Fungo (levedura viva)", "Pó com bicarbonato de sódio"],
                    ["Uso comum", "Pão e pizza", "Bolos e tortas"],
                    ["Como age", "Fermentação — bolhas de CO₂", "Aquecimento libera CO₂"],
                ],
            },
            "topic_id": "yeasts",
            "sources": [_src("page-040.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Etanol no Brasil:",
                "text": "Leveduras fermentam a cana-de-açúcar (ou milho, beterraba…) e produzem etanol — "
                "usado como combustível e em produtos de limpeza e higiene.",
            },
            "topic_id": "yeasts",
            "sources": [_src("page-040.jpg"), _src("page-043.jpg")],
        },
    ]


def _topic_antibiotics_vaccines() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "8. Antibióticos e vacinas"}, "topic_id": "antibiotics_vaccines"},
        {
            "type": "paragraph",
            "content": {
                "text": "Antibióticos tratam infecções causadas por bactérias — matam ou impedem que se multipliquem. "
                "Só o médico pode receitar; cada bactéria pede um antibiótico específico. "
                "Gripe é causada por vírus: antibiótico não cura virose!",
            },
            "topic_id": "antibiotics_vaccines",
            "sources": [_src("page-046.jpg"), _src("page-054.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🍄", "title": "Penicilina", "text": "Fleming · fungo Penicillium · zona sem bactérias na placa"},
                    {"icon": "🛡️", "title": "Sistema imune", "text": "Células e órgãos que combatem microrganismos"},
                    {"icon": "💉", "title": "Vacinas", "text": "Preparam defesas sem causar a doença"},
                    {"icon": "📒", "title": "Carteira", "text": "Registra doses e idades — siga o calendário"},
                ],
            },
            "topic_id": "antibiotics_vaccines",
            "sources": [_src("page-049.jpg"), _src("page-050.jpg"), _src("page-052.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Pegadinha da PE:",
                "text": "Vacinas previnem; antibióticos tratam bactérias. "
                "Higiene pessoal e do ambiente evitam contaminação por fungos, vírus e bactérias.",
            },
            "topic_id": "antibiotics_vaccines",
        },
    ]


def _section_summary() -> dict:
    summaries = [
        ("1. Microrganismos", "micro_intro", [
            {"icon": "🔬", "title": "Tipos", "text": "Bactérias · vírus · fungos"},
            {"icon": "⚠️", "title": "Danos", "text": "Mofo · cárie · viroses"},
            {"icon": "✅", "title": "Benefício", "text": "Lactobacilos no intestino"},
        ]),
        ("2. Laboratório", "lab_study", [
            {"icon": "🧫", "title": "Petri", "text": "Meio de cultura + colônias"},
            {"icon": "🔭", "title": "Microscópio", "text": "Amplia o invisível"},
        ]),
        ("3. Higiene das mãos", "hand_hygiene", [
            {"icon": "🧼", "title": "Sabão", "text": "Melhor que só gel para sujeira"},
            {"icon": "📊", "title": "A–D", "text": "Menos microrganismos após lavar bem"},
        ]),
        ("4. Alimentos", "food_prevention", [
            {"icon": "🍳", "title": "Cozinha", "text": "Limpeza evita contaminação"},
            {"icon": "🥗", "title": "Hortaliças", "text": "Desinfecção com cloro diluído"},
        ]),
        ("5. Resíduos", "waste", [
            {"icon": "♻️", "title": "Reciclável", "text": "Papel · vidro · metal · plástico"},
            {"icon": "🗑️", "title": "Rejeito", "text": "Não recicla — ex.: fralda"},
        ]),
        ("6. Compostagem", "composting", [
            {"icon": "🪱", "title": "Decompositores", "text": "Fungos · bactérias · minhocas"},
            {"icon": "🌱", "title": "Adubo", "text": "Recicla nutrientes no solo"},
        ]),
        ("7. Leveduras", "yeasts", [
            {"icon": "🍞", "title": "Pão", "text": "CO₂ faz furinhos na massa"},
            {"icon": "⛽", "title": "Etanol", "text": "Fermentação da cana"},
        ]),
        ("8. Saúde", "antibiotics_vaccines", [
            {"icon": "💊", "title": "Antibiótico", "text": "Só bactérias — com receita"},
            {"icon": "💉", "title": "Vacina", "text": "Fortalece imunidade"},
        ]),
    ]
    blocks: list = [
        {
            "type": "panel_intro",
            "content": {
                "title": "Mapa mental da PE",
                "text": "Revise cada tópico nos acordeões — cards com o essencial dos Módulos 10 a 13.",
            },
        },
    ]
    for title, _tid, cards in summaries:
        blocks.append({"type": "heading", "content": {"level": 3, "text": title}})
        blocks.append({"type": "concept_grid", "content": {"cards": cards}})
    blocks.append(
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Pegadinha:",
                "text": "Paciente com gripe (vírus) não deve tomar antibiótico para “curar” — "
                "antibiótico é para infecção bacteriana, com orientação médica.",
            },
        }
    )
    return {"id": "summary", "type": "quick_summary", "title": "Resumo rápido", "blocks": blocks}


def build_exercises() -> dict:
    def sa(page: str) -> list[str]:
        return [f"{ASSET_PREFIX}/{page}"]

    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "exercises": [
            {
                "id": "ci3-pe-001",
                "type": "multiple_choice",
                "topic": "micro_intro",
                "question": "Microrganismos são seres vivos que:",
                "options": [
                    "Só existem dentro de hospitais",
                    "São grandes demais para ver sem lupa",
                    "São tão pequenos que normalmente não vemos a olho nu",
                    "Incluem apenas plantas aquáticas",
                ],
                "correct_answer": 2,
                "explanation": "Bactérias, vírus e fungos microscópicos estão em todo lugar.",
                "difficulty": "basic",
                "source_assets": sa("page-002.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-002",
                "type": "multiple_choice",
                "topic": "micro_intro",
                "question": (
                    "Leia as afirmativas:\n"
                    "I. O mofo é um tipo de fungo que pode crescer em alimentos.\n"
                    "II. A cárie dentária é causada por vírus que comem açúcar.\n"
                    "III. Gripe e resfriado são viroses respiratórias contagiosas.\n"
                    "IV. Baratas podem espalhar microrganismos na cozinha.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, III e IV", "I e II", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "Cárie é causada por bactérias, não vírus (II errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-002.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-003",
                "type": "multiple_choice",
                "topic": "lab_study",
                "question": "O meio de cultura em uma placa de Petri serve para:",
                "options": [
                    "Colorir as bactérias de azul no microscópio",
                    "Oferecer nutrientes para o crescimento e multiplicação de microrganismos",
                    "Eliminar todo oxigênio do laboratório",
                    "Impedir que fungos se alimentem",
                ],
                "correct_answer": 1,
                "explanation": "É a substância nutritiva onde cientistas cultivam amostras.",
                "difficulty": "basic",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-004",
                "type": "multiple_choice",
                "topic": "lab_study",
                "question": (
                    "Leia as afirmativas sobre colônias na placa de Petri:\n"
                    "I. Bactérias podem formar pontos amarelados.\n"
                    "II. Fungos podem ter aspecto aveludado, como algodão.\n"
                    "III. Uma colônia é um único microrganismo visível.\n"
                    "IV. Colônias só aparecem se as condições forem favoráveis.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "Colônia é grupo de microrganismos multiplicados (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-005",
                "type": "multiple_choice",
                "topic": "hand_hygiene",
                "question": "No experimento das mãos, a amostra D (lavadas com sabão e depois álcool em gel) tende a apresentar:",
                "options": [
                    "Mais colônias que a amostra A",
                    "A menor presença de microrganismos entre as quatro amostras",
                    "Nenhuma diferença em relação à amostra A",
                    "Apenas vírus, nunca bactérias",
                ],
                "correct_answer": 1,
                "explanation": "Lavagem com sabão remove sujeira; o gel complementa a higienização.",
                "difficulty": "basic",
                "source_assets": sa("page-010.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-006",
                "type": "multiple_choice",
                "topic": "hand_hygiene",
                "question": "Por que a água usada nos experimentos do caderno deve ser potável?",
                "options": [
                    "Porque água não potável já traz microrganismos que confundem o resultado",
                    "Porque só água salgada permite colônias",
                    "Porque água potável mata todas as leveduras instantaneamente",
                    "Porque água da chuva é sempre estéril",
                ],
                "correct_answer": 0,
                "explanation": "Água contaminada pode introduzir microrganismos extras na amostra.",
                "difficulty": "intermediate",
                "source_assets": sa("page-016.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-007",
                "type": "multiple_choice",
                "topic": "food_prevention",
                "question": "Na higienização de hortaliças, a desinfecção com solução clorada por cerca de 15 minutos serve para:",
                "options": [
                    "Deixar as folhas mais doces",
                    "Remover microrganismos que a lavagem simples não elimina",
                    "Substituir a necessidade de lavar antes",
                    "Secar as folhas instantaneamente",
                ],
                "correct_answer": 1,
                "explanation": "Desinfecção reduz microrganismos patogênicos antes do consumo.",
                "difficulty": "basic",
                "source_assets": sa("page-014.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-008",
                "type": "multiple_choice",
                "topic": "food_prevention",
                "question": (
                    "Leia as afirmativas sobre prevenção:\n"
                    "I. Máscaras ajudam a reduzir gotículas com vírus no ar.\n"
                    "II. Antibiótico caseiro cura qualquer gripe rapidamente.\n"
                    "III. Distanciamento social diminui contato entre pessoas doentes e saudáveis.\n"
                    "IV. Lavar as mãos reduz microrganismos nas mãos.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, III e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "Gripe é viral — antibiótico não trata virose (II errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-018.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-009",
                "type": "multiple_choice",
                "topic": "waste",
                "question": "Cascas de frutas e restos de verduras descartados na cozinha são classificados como:",
                "options": ["Rejeito (lixo)", "Resíduo reciclável de metal", "Resíduo orgânico", "Resíduo radioativo"],
                "correct_answer": 2,
                "explanation": "Origem biológica — podem ser compostados ou decompostos.",
                "difficulty": "basic",
                "source_assets": sa("page-023.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-010",
                "type": "multiple_choice",
                "topic": "waste",
                "question": (
                    "Leia as afirmativas sobre destino do lixo:\n"
                    "I. Lixão é área a céu aberto que atrai ratos e moscas.\n"
                    "II. Aterro sanitário é preparado para reduzir poluição.\n"
                    "III. Todo plástico sujo de comida é rejeito, nunca reciclável.\n"
                    "IV. Resíduos no rio podem causar enchentes e doenças.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e IV", "II, III e IV", "I e III", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "Plástico limpo e separado pode ser reciclável (III nem sempre correta).",
                "difficulty": "intermediate",
                "source_assets": sa("page-023.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-011",
                "type": "multiple_choice",
                "topic": "composting",
                "question": "Minhocas ajudam na compostagem porque:",
                "options": [
                    "Comem plástico e vidro",
                    "Cavam túneis que facilitam a entrada de oxigênio e produzem húmus rico em nutrientes",
                    "Impedem totalmente fungos e bactérias de agir",
                    "Substituem a necessidade de umidade",
                ],
                "correct_answer": 1,
                "explanation": "Túneis aeram o material; fezes viram húmus adubador.",
                "difficulty": "basic",
                "source_assets": sa("page-029.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-012",
                "type": "multiple_choice",
                "topic": "composting",
                "question": "Fazer furos nas laterais de um balde na composteira doméstica favorece principalmente:",
                "options": [
                    "A entrada de gás oxigênio",
                    "A evaporação total da umidade em um minuto",
                    "O crescimento de mofo apenas na tampa",
                    "A eliminação de minhocas",
                ],
                "correct_answer": 0,
                "explanation": "Oxigênio é indispensável para fungos e bactérias decomporem o orgânico.",
                "difficulty": "basic",
                "source_assets": sa("page-035.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-013",
                "type": "multiple_choice",
                "topic": "yeasts",
                "question": "Os furinhos no interior de uma fatia de pão formam-se porque:",
                "options": [
                    "O forno injeta ar com uma seringa",
                    "Bolhas de gás carbônico da fermentação expandem a massa",
                    "A farinha já vem furada da fábrica",
                    "O sal derrete e deixa buracos",
                ],
                "correct_answer": 1,
                "explanation": "Leveduras liberam CO₂ ao fermentar açúcar/amido da massa.",
                "difficulty": "basic",
                "source_assets": sa("page-041.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-014",
                "type": "multiple_choice",
                "topic": "yeasts",
                "question": (
                    "Leia as afirmativas sobre fermentos:\n"
                    "I. Fermento biológico contém leveduras vivas.\n"
                    "II. Fermento químico usa bicarbonato e age muito no aquecimento.\n"
                    "III. Leveduras produzem etanol na fermentação da cana.\n"
                    "IV. Fermento químico é um fungo chamado Saccharomyces.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e III", "II, III e IV", "I e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "Fermento químico não é fungo (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-040.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-015",
                "type": "multiple_choice",
                "topic": "antibiotics_vaccines",
                "question": "Alexander Fleming observou que, perto do fungo Penicillium na placa, as bactérias:",
                "options": [
                    "Multiplicavam mais rápido",
                    "Não se desenvolviam naquela área",
                    "Viravam plantas",
                    "Produziam vacinas automaticamente",
                ],
                "correct_answer": 1,
                "explanation": "O fungo secretava penicilina, impedindo o crescimento bacteriano.",
                "difficulty": "basic",
                "source_assets": sa("page-050.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-016",
                "type": "multiple_choice",
                "topic": "antibiotics_vaccines",
                "question": (
                    "Paciente com gripe (vírus) quer tomar antibiótico que tem em casa. "
                    "Leia as afirmativas:\n"
                    "I. Antibiótico combate bactérias, não vírus da gripe.\n"
                    "II. Vacinas ajudam o sistema imune a se preparar contra doenças.\n"
                    "III. Antibiótico no Brasil exige receita médica.\n"
                    "IV. Toda virose deve ser tratada com penicilina.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e III", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Penicilina não trata toda virose (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-054.jpg"),
                "section": "final_quiz",
            },
        ],
    }
