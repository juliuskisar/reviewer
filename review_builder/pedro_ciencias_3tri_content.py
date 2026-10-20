"""Conteúdo pedagógico da revisão Pedro — Ciências PE 3º trimestre (Módulos 22, 23 e 24)."""

from __future__ import annotations

REVIEW_ID = "pedro-pe-ciencias-3tri"
ASSET_PREFIX = "assets/pedro_pe_ciencias_3_tri"


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
        "subtitle": "Pedro · 6º ano · Módulos 22, 23 e 24",
        "language": "pt-BR",
        "discipline": "Ciências",
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
                    "text": "Caminhos do impulso nervoso, reflexos e tempo de reação, neurônios "
                    "e sinapses, drogas psicoativas e sistema sensorial — visão, audição, "
                    "receptores e inclusão. Reserve cerca de 1 hora.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "⚡", "title": "Impulso", "text": "Aferente · eferente · SNC"},
                        {"icon": "🦵", "title": "Reflexo", "text": "Arco reflexo · patelar · régua"},
                        {"icon": "🧠", "title": "Neurônio", "text": "Dendrito · axônio · sinapse"},
                        {"icon": "💊", "title": "Drogas", "text": "Estimulante · depressora · perturbadora"},
                        {"icon": "👁️", "title": "Visão", "text": "Retina · pupila · acomodação"},
                        {"icon": "👂", "title": "Audição", "text": "Cóclea · equilíbrio · mecanorreceptores"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 22 — Caminhos do impulso nervoso",
                        "Módulo 23 — Neurônios, sinapses e drogas",
                        "Módulo 24 — Sistema sensorial e inclusão",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Leia cards e tabelas com calma.",
                            "tip": "Ligue nervo aferente = sensorial e eferente = motor.",
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
            *_topic_impulse_paths(),
            *_topic_reflex_reaction(),
            *_topic_spine_safety(),
            *_topic_neurons_synapses(),
            *_topic_psychoactive_drugs(),
            *_topic_substances(),
            *_topic_sensory_receptors(),
            *_topic_vision_hearing_inclusion(),
        ],
    }


def _topic_impulse_paths() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "1. Caminhos do impulso nervoso"},
            "topic_id": "impulse_paths",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Informações do ambiente chegam ao Sistema Nervoso Central (encéfalo + medula) "
                "como impulsos elétricos pelos nervos sensitivos ou aferentes. O SNC interpreta "
                "e manda respostas pelos nervos motores ou eferentes até músculos e glândulas "
                "(efetores). Órgãos que captam estímulos são receptores.",
            },
            "topic_id": "impulse_paths",
            "sources": [_src("page-027.jpg"), _src("page-026.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Tipo de nervo", "Direção", "Função"],
                "rows": [
                    ["Aferente (sensorial)", "Receptor → SNC", "Leva sensações (visão, dor, calor…)"],
                    ["Eferente (motor)", "SNC → efetor", "Comanda contração muscular ou secreção"],
                ],
            },
            "topic_id": "impulse_paths",
        },
        {
            "type": "callout",
            "content": {
                "variant": "tip",
                "title": "Experimento da régua:",
                "text": "Com olhos abertos, a visão avisa que a régua caiu; vendado, falta o estímulo "
                "visual e a reação fica mais lenta — o cérebro precisa de outro sentido (ouvido).",
            },
            "topic_id": "impulse_paths",
            "sources": [_src("page-028.jpg"), _src("page-025.jpg")],
        },
    ]


def _topic_reflex_reaction() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "2. Reflexos e tempo de reação"},
            "topic_id": "reflex_reaction",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Atos reflexos são respostas rápidas e involuntárias — o impulso vai ao SNC "
                "(medula), volta pelo nervo motor e o músculo reage antes do cérebro registrar "
                "dor. No arco reflexo: estímulo → nervo aferente → medula → (nervo de associação) "
                "→ nervo eferente → músculo. Exemplos: retirar a mão do calor, reflexo patelar, "
                "espirro e tosse.",
            },
            "topic_id": "reflex_reaction",
            "sources": [_src("page-020.jpg"), _src("page-023.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🔥", "title": "Calor", "text": "Mão retira-se antes de sentir dor consciente"},
                    {"icon": "🦵", "title": "Patelar", "text": "Martelo na rótula → perna estica sozinha"},
                    {"icon": "⏱️", "title": "Reação", "text": "Goleira e motociclista dependem de treino + SNC"},
                ],
            },
            "topic_id": "reflex_reaction",
        },
    ]


def _topic_spine_safety() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "3. Coluna vertebral e proteção do SNC"},
            "topic_id": "spine_safety",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Neurônios não se dividem — lesões na medula espinhal são permanentes. "
                "Lesão cervical alta pode causar tetraplegia (sem movimento/sensação no corpo) "
                "e até comprometer respiração. Lesão lombar pode causar paraplegia (pernas). "
                "Capacete protege o encéfalo; placa rígida na jaqueta protege a coluna.",
            },
            "topic_id": "spine_safety",
            "sources": [_src("page-022.jpg"), _src("page-026.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "warning",
                "title": "Anestesia raquidiana:",
                "text": "Aplicada na região lombar (L3/L4 ou L4/L5) bloqueia nervos da medula — "
                "indicada para cirurgias na parte inferior do tronco e pernas, não no tórax ou pescoço.",
            },
            "topic_id": "spine_safety",
            "sources": [_src("page-024.jpg")],
        },
    ]


def _topic_neurons_synapses() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "4. Neurônios, excitabilidade e sinapses"},
            "topic_id": "neurons_synapses",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Excitabilidade é a capacidade de responder rapidamente a estímulos. Neurônios "
                "têm dendritos (recebem), corpo celular, axônio (conduz impulso) e terminais. "
                "Na sinapse, o impulso chega ao axônio terminal, libera neurotransmissores na "
                "fenda sináptica e ativa o dendrito do neurônio seguinte — sentido único.",
            },
            "topic_id": "neurons_synapses",
            "sources": [_src("page-019.jpg"), _src("page-016.jpg"), _src("page-017.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🧬", "title": "Partes", "text": "Dendrito → corpo → axônio → terminais"},
                    {"icon": "🔗", "title": "Sinapse", "text": "Neurotransmissor na fenda — unidirecional"},
                    {"icon": "🐙", "title": "Evolução", "text": "Rede difusa → cefalização → SNC/SNP"},
                ],
            },
            "topic_id": "neurons_synapses",
        },
    ]


def _topic_psychoactive_drugs() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "5. Drogas psicoativas e sinapses"},
            "topic_id": "psychoactive_drugs",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Segundo a OMS, droga é substância que altera funções celulares e comportamento "
                "(inclui remédios e cafeína). Psicotrópicas agem no cérebro, muitas nas sinapses. "
                "Classificação por efeito: depressoras (álcool), estimulantes (nicotina, cocaína, "
                "cafeína), perturbadoras (maconha/THC). Uso prolongado pode gerar tolerância, "
                "dependência e síndrome de abstinência.",
            },
            "topic_id": "psychoactive_drugs",
            "sources": [_src("page-018.jpg"), _src("page-014.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Conceito", "Significado"],
                "rows": [
                    ["Tolerância", "Precisa de doses maiores para o mesmo efeito"],
                    ["Dependência", "Dificuldade de viver sem a substância"],
                    ["Abstinência", "Mal-estar ao parar de usar"],
                ],
            },
            "topic_id": "psychoactive_drugs",
        },
    ]


def _topic_substances() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "6. Álcool, cigarro e outras substâncias"},
            "topic_id": "substances",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Álcool deprime o SNC — reflexos e raciocínio ficam lentos (risco no trânsito). "
                "Nicotina estimula sinapses e dopamina (dependência); fumaça traz milhares de "
                "substâncias tóxicas. Cocaína estimula e pode parar o coração; maconha (THC) "
                "perturba humor e coordenação. PeNSE 2019 mostrou alto uso de álcool entre "
                "escolares — começar cedo aumenta risco de dependência.",
            },
            "topic_id": "substances",
            "sources": [_src("page-013.jpg"), _src("page-015.jpg"), _src("page-009.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Cafeína:",
                "text": "Bloqueia receptores de adenosina (cansaço) e estimula adrenalina — "
                "classifica-se como droga psicotrópica estimulante.",
            },
            "topic_id": "substances",
        },
    ]


def _topic_sensory_receptors() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "7. Sistema sensorial e receptores"},
            "topic_id": "sensory_receptors",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Só vira sensação quando o cérebro interpreta impulsos dos nervos sensoriais. "
                "Receptores classificam-se pelo estímulo: quimiorreceptores (olfato, paladar), "
                "mecanorreceptores (tato, som na orelha), fotorreceptores (visão), termorreceptores "
                "(temperatura), nociceptores (dor). Por local: exteriorreceptores, interorreceptores "
                "e propriorreceptores (posição do corpo).",
            },
            "topic_id": "sensory_receptors",
            "sources": [_src("page-010.jpg"), _src("page-012.jpg"), _src("page-006.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Receptor", "Exemplo no corpo"],
                "rows": [
                    ["Quimiorreceptor", "Olfato e paladar — moléculas no nariz/boca"],
                    ["Mecanorreceptor", "Pele, cóclea, linha lateral dos peixes"],
                    ["Fotorreceptor", "Cones e bastonetes da retina"],
                ],
            },
            "topic_id": "sensory_receptors",
        },
    ]


def _topic_vision_hearing_inclusion() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "8. Visão, audição e inclusão"},
            "topic_id": "vision_hearing_inclusion",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Olho: luz passa por córnea, humor aquoso, cristalino (acomodação) e foca na "
                "retina; nervo óptico leva ao cérebro. Pupila abre no escuro e fecha na luz. "
                "Orelha: som vibra tímpano → ossículos → cóclea (mecanorreceptores); ductos "
                "semicirculares cuidam do equilíbrio. Gustação e olfato trabalham juntos. "
                "Pessoas cegas desenvolvem outros sentidos com prática — não são 'super-heróis'. "
                "Acessibilidade: piso tátil, Braille, botoeira sonora, futebol de 5 (bola com guizo).",
            },
            "topic_id": "vision_hearing_inclusion",
            "sources": [
                _src("page-008.jpg"),
                _src("page-007.jpg"),
                _src("page-005.jpg"),
                _src("page-004.jpg"),
                _src("page-011.jpg"),
                _src("page-003.jpg"),
                _src("page-002.jpg"),
            ],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "👁️", "title": "Visão", "text": "Retina · cones/bastonetes · nervo óptico"},
                    {"icon": "👂", "title": "Ouvido", "text": "Cóclea = audição · semicirculares = equilíbrio"},
                    {"icon": "♿", "title": "Inclusão", "text": "Lei 10.098 · Art. 205 CF · escola regular"},
                ],
            },
            "topic_id": "vision_hearing_inclusion",
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
            {"type": "heading", "content": {"level": 3, "text": "1. Impulso nervoso"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "⬅️", "title": "Aferente", "text": "Sensorial · receptor → SNC"},
                        {"icon": "➡️", "title": "Eferente", "text": "Motor · SNC → músculo/glândula"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. Reflexos"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🔄", "title": "Arco reflexo", "text": "Medula responde sem esperar o cérebro"},
                        {"icon": "🦵", "title": "Patelar", "text": "Teste médico de reflexo na rótula"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Coluna"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🪖", "title": "Proteção", "text": "Capacete · placa nas costas"},
                        {"icon": "⚠️", "title": "Lesões", "text": "Tetraplegia · paraplegia · irreversível"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Neurônio"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🧠", "title": "Sinapse", "text": "Neurotransmissor · sentido único"},
                        {"icon": "⚡", "title": "Excitabilidade", "text": "Resposta rápida a estímulos"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Drogas"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "📉", "title": "Depressora", "text": "Álcool — reflexos lentos"},
                        {"icon": "📈", "title": "Estimulante", "text": "Nicotina · cocaína · cafeína"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "6. Substâncias"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🚭", "title": "Cigarro", "text": "Nicotina · câncer · fumante passivo"},
                        {"icon": "🍺", "title": "Álcool", "text": "PeNSE · proibido para menores"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "7. Receptores"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "👃", "title": "Quimio", "text": "Olfato · paladar"},
                        {"icon": "✋", "title": "Mecano", "text": "Tato · cóclea · linha lateral"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "8. Sentidos e inclusão"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🔦", "title": "Olho", "text": "Pupila · cristalino · retina"},
                        {"icon": "⚽", "title": "Futebol de 5", "text": "Guizo · chamador · inclusão"},
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "Cóclea e semicirculares têm mecanorreceptores — não confunda audição com equilíbrio. "
                    "Reflexo patelar passa pela medula, mas ainda envolve o SNC (não é 'sem cérebro').",
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
                "id": "ci3-pe-001",
                "type": "multiple_choice",
                "topic": "impulse_paths",
                "question": (
                    "Nervos sensitivos ou aferentes transportam informações:"
                ),
                "options": [
                    "Do SNC para os músculos apenas",
                    "Dos receptores em direção ao SNC",
                    "Somente da medula para a pele, nunca do olho",
                    "Apenas de glândulas para o estômago",
                ],
                "correct_answer": 1,
                "explanation": "Aferente = sensorial: estímulo captado → central nervosa.",
                "difficulty": "basic",
                "source_assets": sa("page-027.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-002",
                "type": "multiple_choice",
                "topic": "impulse_paths",
                "question": (
                    "Leia as afirmativas sobre impulsos nervosos:\n"
                    "I. Nervos motores ou eferentes ligam o SNC aos efetores.\n"
                    "II. Receptores captam estímulos do meio externo ou interno.\n"
                    "III. Todo impulso passa sempre pelo cérebro antes de qualquer resposta.\n"
                    "IV. Músculos esqueléticos podem ser efetores.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e IV", "II e III", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Reflexos podem ser processados na medula (III falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-027.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-003",
                "type": "multiple_choice",
                "topic": "reflex_reaction",
                "question": (
                    "No arco reflexo ao tocar uma superfície quente, a retirada rápida da mão ocorre porque:"
                ),
                "options": [
                    "O cérebro analisa a dor antes de mandar mover o músculo",
                    "A medula coordena resposta rápida pelo nervo motor antes da sensação consciente de dor",
                    "Somente os músculos decidem sem participação nervosa",
                    "O calor não gera impulso nervoso",
                ],
                "correct_answer": 1,
                "explanation": "Arco reflexo na medula — resposta mais rápida que a interpretação cerebral da dor.",
                "difficulty": "basic",
                "source_assets": sa("page-020.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-004",
                "type": "multiple_choice",
                "topic": "reflex_reaction",
                "question": (
                    "Leia as afirmativas sobre reflexos e experimentos:\n"
                    "I. O reflexo patelar é testado com martelo abaixo da rótula.\n"
                    "II. Com olhos vendados na régua, falta estímulo visual e a reação tende a piorar.\n"
                    "III. Atos reflexos são sempre conscientes e voluntários.\n"
                    "IV. Espirro e tosse protegem vias respiratórias.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Reflexos são involuntários (III falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-023.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-005",
                "type": "multiple_choice",
                "topic": "spine_safety",
                "question": (
                    "Lesão na região cervical da medula espinhal pode resultar em:"
                ),
                "options": [
                    "Apenas formigamento nos dedos, sem perda de movimento",
                    "Tetraplegia — perda de movimento e sensação ampliada no corpo",
                    "Melhora automática porque neurônios se multiplicam",
                    "Paraplegia restrita só aos dedos da mão",
                ],
                "correct_answer": 1,
                "explanation": "Lesão alta na medula afeta braços e pernas (tetraplegia) e pode comprometer respiração.",
                "difficulty": "basic",
                "source_assets": sa("page-022.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-006",
                "type": "multiple_choice",
                "topic": "spine_safety",
                "question": (
                    "Leia as afirmativas sobre nervos e SNC:\n"
                    "I. Informação de pele fria chega ao SNC por nervo aferente.\n"
                    "II. Ordem para mover a perna ao caminhar usa nervo eferente.\n"
                    "III. Batimentos cardíacos dependem sempre de comando consciente do cérebro.\n"
                    "IV. Neurônios destruídos na medula não se regeneram como pele.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "I, II e IV", "II e III", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Coração tem controle autônomo (III exagerada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-022.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-007",
                "type": "multiple_choice",
                "topic": "neurons_synapses",
                "question": (
                    "Na sinapse entre dois neurônios, o impulso nervoso segue preferencialmente:"
                ),
                "options": [
                    "Do dendrito do primeiro para o axônio do segundo, em qualquer sentido",
                    "Do neurônio pré-sináptico (axônio) para o pós-sináptico (dendrito), via neurotransmissor",
                    "Diretamente pelo contato físico entre axônio e axônio, sem substância química",
                    "Apenas dentro do núcleo celular",
                ],
                "correct_answer": 1,
                "explanation": "Neurotransmissores na fenda sináptica propagam o sinal em um sentido.",
                "difficulty": "basic",
                "source_assets": sa("page-009.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-008",
                "type": "multiple_choice",
                "topic": "neurons_synapses",
                "question": (
                    "Leia as afirmativas sobre neurônios:\n"
                    "I. Dendritos recebem impulsos de outros neurônios.\n"
                    "II. Axônio conduz impulso para longe do corpo celular.\n"
                    "III. Cefalização concentra sentidos e neurônios na região da cabeça.\n"
                    "IV. Todos os animais possuem encéfalo igual ao humano.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, II e III", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e III corretas. Complexidade nervosa varia muito entre grupos (IV falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-019.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-009",
                "type": "multiple_choice",
                "topic": "psychoactive_drugs",
                "question": (
                    "Drogas psicoativas depressoras, como o álcool, agem principalmente:"
                ),
                "options": [
                    "Acelerando reflexos e raciocínio para dirigir melhor",
                    "Diminuindo atividade nervosa — reflexos e equilíbrio ficam lentos",
                    "Eliminando completamente a necessidade de sono por meses",
                    "Curando lesões na medula espinal",
                ],
                "correct_answer": 1,
                "explanation": "Álcool deprime o SNC — campanhas de trânsito combatem direção embriagada.",
                "difficulty": "basic",
                "source_assets": sa("page-013.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-010",
                "type": "multiple_choice",
                "topic": "psychoactive_drugs",
                "question": (
                    "Leia as afirmativas sobre uso de drogas:\n"
                    "I. Tolerância exige doses maiores para o mesmo efeito.\n"
                    "II. Dependência dificulta viver sem a substância.\n"
                    "III. Abstinência traz sintomas desagradáveis ao parar o uso.\n"
                    "IV. Drogas ilícitas nunca alteram sinapses.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["II e IV", "I, II e III", "I e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Psicotrópicas atuam no cérebro e nas sinapses (IV falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-018.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-011",
                "type": "multiple_choice",
                "topic": "substances",
                "question": (
                    "A nicotina do cigarro é classificada como droga:"
                ),
                "options": [
                    "Depressora, porque acalma totalmente o coração",
                    "Estimulante, que aumenta dopamina e favorece dependência",
                    "Perturbadora, porque causa alucinações em toda dose",
                    "Inerte, sem efeito no sistema nervoso",
                ],
                "correct_answer": 1,
                "explanation": "Nicotina estimula sinapses e libera dopamina — usuário precisa de mais com o tempo.",
                "difficulty": "basic",
                "source_assets": sa("page-015.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-012",
                "type": "multiple_choice",
                "topic": "substances",
                "question": (
                    "Leia as afirmativas sobre substâncias do caderno:\n"
                    "I. Cafeína imita adenosina e reduz sensação de cansaço.\n"
                    "II. Cocaína estimula o sistema nervoso e pode elevar frequência cardíaca.\n"
                    "III. THC da maconha perturba o funcionamento cerebral.\n"
                    "IV. Álcool é permitido para adolescentes em festas escolares.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e III", "II e IV", "I e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e III corretas. Venda/consumo por menores é proibido (IV falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-009.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-013",
                "type": "multiple_choice",
                "topic": "sensory_receptors",
                "question": (
                    "A linha lateral dos peixes detecta vibrações na água. Esses receptores são:"
                ),
                "options": [
                    "Quimiorreceptores, como o olfato humano",
                    "Mecanorreceptores, comparáveis ao tato humano",
                    "Fotorreceptores, como cones da retina",
                    "Termorreceptores exclusivos de peixes tropicais",
                ],
                "correct_answer": 1,
                "explanation": "Vibração e pressão = estímulo mecânico — resposta b do Teste p. 375.",
                "difficulty": "basic",
                "source_assets": sa("page-001.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-014",
                "type": "multiple_choice",
                "topic": "sensory_receptors",
                "question": (
                    "Leia as afirmativas sobre receptores:\n"
                    "I. Olfato usa quimiorreceptores no epitélio nasal.\n"
                    "II. Cóclea e canais semicirculares têm mecanorreceptores.\n"
                    "III. Cones e bastonetes são fotorreceptores.\n"
                    "IV. Nociceptores detectam estímulos de prazer apenas.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, II e III", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Nociceptores = dor (IV falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-012.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-015",
                "type": "multiple_choice",
                "topic": "vision_hearing_inclusion",
                "question": (
                    "Para focar objeto próximo, o cristalino do olho humano:"
                ),
                "options": [
                    "Fica mais fino, relaxando os músculos ciliares",
                    "Aumenta a curvatura — fica mais 'espesso'",
                    "Deixa de receber luz pela pupila",
                    "Move-se para fora da cavidade ocular",
                ],
                "correct_answer": 1,
                "explanation": "Acomodação visual: perto = cristalino mais curvo; longe = mais fino.",
                "difficulty": "basic",
                "source_assets": sa("page-007.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-016",
                "type": "multiple_choice",
                "topic": "vision_hearing_inclusion",
                "question": (
                    "Leia as afirmativas sobre sentidos e inclusão:\n"
                    "I. Lei 10.098 trata de acessibilidade como direito.\n"
                    "II. Futebol de 5 usa bola com guizos e jogadores de campo vendados.\n"
                    "III. Cegos nascem sempre com audição 'sobrehumana' garantida.\n"
                    "IV. Piso tátil orienta pessoas com deficiência visual.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. Outros sentidos podem ser treinados, mas não são 'superpoderes' (III falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-017",
                "type": "multiple_choice",
                "topic": "sensory_receptors",
                "question": (
                    "Segundo o caderno, uma sensação só existe quando:"
                ),
                "options": [
                    "O estímulo atinge a pele, mesmo sem cérebro",
                    "O cérebro recebe e interpreta impulsos dos nervos sensoriais",
                    "O músculo se contrai antes de qualquer estímulo",
                    "A pupila dilata independentemente de luz",
                ],
                "correct_answer": 1,
                "explanation": "Sistema sensorial inclui células, nervos e áreas cerebrais de interpretação.",
                "difficulty": "basic",
                "source_assets": sa("page-010.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci3-pe-018",
                "type": "multiple_choice",
                "topic": "vision_hearing_inclusion",
                "question": (
                    "Leia as afirmativas sobre deficiência visual (Teste p. 375):\n"
                    "I. Pessoas que nascem cegas podem desenvolver audição mais aguçada.\n"
                    "II. Cegos usam apenas o tato para se localizar.\n"
                    "III. Pessoas com deficiência visual devem estudar em escolas regulares.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I", "II", "III", "I e III"],
                "correct_answer": 3,
                "explanation": "I e III corretas no caderno — usam vários sentidos e têm direito à escola regular (II falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-001.jpg"),
                "section": "final_quiz",
            },
        ],
    }
