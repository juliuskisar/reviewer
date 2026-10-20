"""Conteúdo pedagógico da revisão Benjamin — Ciências PE 2º trimestre."""

from __future__ import annotations

REVIEW_ID = "benjamin-pe-ciencias-2tri"
ASSET_PREFIX = "assets/benjamin_pe_ciencias_2_tri"


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
        "subtitle": "Benjamin · 4º ano · Módulos 5, 6, 7, 8 e 9",
        "language": "pt-BR",
        "discipline": "Ciências",
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
                    "text": "Alimentação dos seres vivos, fotossíntese, pigmentos e óleos das plantas, "
                    "fósseis e dinossauros, predador e presa, cadeias alimentares e decompositores. "
                    "Reserve cerca de 50 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "⚡", "title": "Energia", "text": "Herbívoros · carnívoros · onívoros"},
                        {"icon": "🌱", "title": "Fotossíntese", "text": "Luz + água + CO₂ → alimento"},
                        {"icon": "🎨", "title": "Pigmentos", "text": "Clorofila · urucum · jenipapo"},
                        {"icon": "🫒", "title": "Óleos", "text": "Essenciais · vegetais · destilação"},
                        {"icon": "🦴", "title": "Fósseis", "text": "Paleontologia · dinossauros BR"},
                        {"icon": "🦁", "title": "Cadeias", "text": "Produtores · consumidores · decompositores"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 5 — A alimentação dos seres vivos",
                        "Módulo 6 — Pigmentos e óleos das plantas",
                        "Módulo 7 — Fotossíntese nos oceanos",
                        "Módulo 8 — Fósseis e dinossauros",
                        "Módulo 9 — Cadeias alimentares",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Leia os cards e tabelas com calma.",
                            "tip": "Tente explicar para alguém como funciona a fotossíntese.",
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
            *_topic_energy_diet(),
            *_topic_photosynthesis(),
            *_topic_pigments(),
            *_topic_plant_oils(),
            *_topic_marine(),
            *_topic_fossils(),
            *_topic_predator_prey(),
            *_topic_food_chains(),
        ],
    }


def _topic_energy_diet() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Seres vivos e energia"}, "topic_id": "energy_diet"},
        {
            "type": "paragraph",
            "content": {
                "text": "Todos os seres vivos precisam de energia para nascer, crescer, se reproduzir "
                "e realizar suas atividades. A energia vem principalmente do alimento.",
            },
            "topic_id": "energy_diet",
            "sources": [_src("page-003.jpg"), _src("page-004.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🌿", "title": "Herbívoros", "text": "Comem plantas — raízes, folhas, frutos, sementes"},
                    {"icon": "🥩", "title": "Carnívoros", "text": "Comem outros animais"},
                    {"icon": "🍎", "title": "Onívoros", "text": "Comem plantas e animais"},
                ],
            },
            "topic_id": "energy_diet",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Lembre-se:",
                "text": "As plantas são a base da alimentação de quase todos os animais — "
                "até carnívoros dependem de herbívoros que comeram plantas. "
                "Plantas também oferecem abrigo.",
            },
            "topic_id": "energy_diet",
        },
    ]


def _topic_photosynthesis() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "2. Fotossíntese e partes da planta"}, "topic_id": "photosynthesis"},
        {
            "type": "paragraph",
            "content": {
                "text": "Diferente dos animais, as plantas produzem seu próprio alimento. "
                "Esse processo chama-se fotossíntese e acontece principalmente nas folhas.",
            },
            "topic_id": "photosynthesis",
            "sources": [_src("page-005.jpg"), _src("page-006.jpg"), _src("page-007.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "☀️", "title": "Luz solar", "text": "Energia absorvida pelas folhas"},
                    {"icon": "💧", "title": "Água", "text": "Absorvida pelas raízes no solo"},
                    {"icon": "💨", "title": "Gás carbônico", "text": "Vem do ar — usado nas folhas"},
                    {"icon": "🟢", "title": "Clorofila", "text": "Pigmento verde que captura a luz"},
                ],
            },
            "topic_id": "photosynthesis",
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Partes da planta e suas funções",
                "headers": ["Parte", "Função"],
                "rows": [
                    ["Raiz", "Fixa a planta e absorve água e nutrientes"],
                    ["Caule", "Sustenta e transporta água e nutrientes"],
                    ["Folha", "Absorve luz do Sol — fotossíntese"],
                    ["Flor", "Reprodução da planta"],
                    ["Fruto", "Protege a semente"],
                ],
            },
            "topic_id": "photosynthesis",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Experimento do caderno:",
                "text": "Com planta aquática (Elodea), luz e escuro: na luz aparecem bolhas de "
                "gás oxigênio; no escuro a fotossíntese quase não acontece.",
            },
            "topic_id": "photosynthesis",
        },
    ]


def _topic_pigments() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "3. Pigmentos naturais das plantas"}, "topic_id": "pigments"},
        {
            "type": "paragraph",
            "content": {
                "text": "Plantas produzem pigmentos que dão cor a folhas, pétalas, frutos, caules e raízes. "
                "A clorofila deixa as folhas verdes. Outros pigmentos aparecem em folhas amarelas, "
                "vermelhas ou listradas.",
            },
            "topic_id": "pigments",
            "sources": [_src("page-010.jpg"), _src("page-011.jpg"), _src("page-012.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🎨", "title": "Urucum e jenipapo", "text": "Povos indígenas extraem tintas naturais"},
                    {"icon": "🧪", "title": "Extração", "text": "Triturar folhas + álcool 70% para soltar pigmentos"},
                    {"icon": "📄", "title": "Cromatografia", "text": "Papel filtro separa as cores de uma folha"},
                ],
            },
            "topic_id": "pigments",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Lembre-se:",
                "text": "Folhas vermelhas também podem ter clorofila — a cromatografia mostra "
                "várias faixas de cor no papel filtro.",
            },
            "topic_id": "pigments",
        },
    ]


def _topic_plant_oils() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "4. Óleos essenciais e óleos vegetais"}, "topic_id": "plant_oils"},
        {
            "type": "paragraph",
            "content": {
                "text": "Plantas produzem substâncias úteis para medicina, perfumaria, cosméticos "
                "e culinária. Há dois tipos principais de óleos de origem vegetal.",
            },
            "topic_id": "plant_oils",
            "sources": [_src("page-013.jpg"), _src("page-014.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Dois tipos de óleo vegetal",
                "headers": ["", "Óleo essencial", "Óleo vegetal"],
                "rows": [
                    ["Origem", "Raízes, caules, folhas, flores aromáticas", "Frutos e sementes"],
                    ["Extração", "Destilação (vapor)", "Prensagem ou outras técnicas"],
                    ["Uso", "Perfumes, remédios, aromaterapia", "Cozinha — milho, soja, azeite, dendê"],
                    ["Exemplos", "Ervas aromáticas", "Azeitona, coco, girassol, canola"],
                ],
            },
            "topic_id": "plant_oils",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Otto Gottlieb:",
                "text": "Cientista brasileiro que estudou substâncias químicas de plantas do Brasil "
                "e propôs nova classificação botânica.",
            },
            "topic_id": "plant_oils",
        },
    ]


def _topic_marine() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "5. Fotossíntese nos oceanos"}, "topic_id": "marine"},
        {
            "type": "paragraph",
            "content": {
                "text": "Algas e fitoplâncton também fazem fotossíntese e liberam gás oxigênio na água "
                "e na atmosfera. Por isso, boa parte do oxigênio do planeta vem dos oceanos.",
            },
            "topic_id": "marine",
            "sources": [_src("page-020.jpg"), _src("page-021.jpg"), _src("page-022.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🌊", "title": "Fitoplâncton", "text": "Microalgas — base da cadeia marinha"},
                    {"icon": "🐟", "title": "Cadeia marinha", "text": "Fitoplâncton → peixes pequenos → peixes grandes → tubarão"},
                    {"icon": "🫁", "title": "Oxigênio", "text": "Não vem só das florestas — oceanos produzem muito O₂"},
                ],
            },
            "topic_id": "marine",
        },
    ]


def _topic_fossils() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "6. Fósseis e dinossauros brasileiros"}, "topic_id": "fossils"},
        {
            "type": "paragraph",
            "content": {
                "text": "Fósseis são restos ou marcas de seres vivos antigos preservados em rochas, "
                "gelo ou âmbar. Paleontólogos os estudam para reconstruir o passado.",
            },
            "topic_id": "fossils",
            "sources": [_src("page-023.jpg"), _src("page-024.jpg"), _src("page-025.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🦴", "title": "Tipos de fóssil", "text": "Ossos, dentes, ovos, conchas, pegadas, sementes"},
                    {"icon": "👣", "title": "Pegadas", "text": "Mostram se o animal era bípede ou quadrúpede"},
                    {"icon": "🇧🇷", "title": "Brasilotitan", "text": "Herbívoro quadrúpede ~8 m — SP"},
                    {"icon": "🦎", "title": "Pampadromaeus", "text": "Insectívoro ~1 m — RS, há 230 milhões de anos"},
                ],
            },
            "topic_id": "fossils",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Lembre-se:",
                "text": "Pegadas em linha reta sugerem animal bípede; pegadas largas e arredondadas "
                "podem indicar herbívoro grande.",
            },
            "topic_id": "fossils",
        },
    ]


def _topic_predator_prey() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "7. Predador e presa"}, "topic_id": "predator_prey"},
        {
            "type": "paragraph",
            "content": {
                "text": "Predadores capturam outros animais para se alimentar. Presas são os animais "
                "que servem de alimento. Ambos desenvolvem adaptações para sobreviver.",
            },
            "topic_id": "predator_prey",
            "sources": [_src("page-031.jpg"), _src("page-032.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Adaptações de predadores e presas",
                "headers": ["", "Predadores", "Presas"],
                "rows": [
                    ["Sentidos", "Visão, olfato e audição apurados", "Alerta — detectam perigo cedo"],
                    ["Corpo", "Força, velocidade, veneno, dentes", "Camuflagem, chifres, grupos"],
                    ["Estratégia", "Emboscada — ex.: crocodilo na água", "Fuga em bando — ex.: suricatos"],
                ],
            },
            "topic_id": "predator_prey",
        },
    ]


def _topic_food_chains() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "8. Cadeias alimentares e decompositores"}, "topic_id": "food_chains"},
        {
            "type": "paragraph",
            "content": {
                "text": "Produtores (plantas) fazem fotossíntese. Consumidores comem plantas ou outros "
                "animais. As setas da cadeia indicam quem serve de alimento para quem.",
            },
            "topic_id": "food_chains",
            "sources": [_src("page-027.jpg"), _src("page-028.jpg"), _src("page-033.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🌳", "title": "Produtor", "text": "Planta — início da cadeia"},
                    {"icon": "🦗", "title": "Consumidor primário", "text": "Herbívoro — come planta"},
                    {"icon": "🐍", "title": "Consumidor secundário", "text": "Come consumidor primário"},
                    {"icon": "🦉", "title": "Consumidor terciário/quaternário", "text": "Topo da cadeia — ex.: coruja"},
                    {"icon": "🍄", "title": "Decompositores", "text": "Fungos e bactérias — reciclam matéria orgânica"},
                ],
            },
            "topic_id": "food_chains",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Exemplo da horta:",
                "text": "Planta → pulgão → joaninha. Fungos e bactérias decompõem folhas "
                "caídas e devolvem nutrientes ao solo.",
            },
            "topic_id": "food_chains",
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
            {"type": "heading", "content": {"level": 3, "text": "1. Energia e alimentação"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🌿", "title": "Herbívoros", "text": "Comem plantas"},
                        {"icon": "🥩", "title": "Carnívoros", "text": "Comem animais"},
                        {"icon": "🍎", "title": "Onívoros", "text": "Comem plantas e animais"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. Fotossíntese"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "☀️", "title": "Precisa de", "text": "Luz + água + gás carbônico"},
                        {"icon": "🟢", "title": "Clorofila", "text": "Pigmento verde nas folhas"},
                        {"icon": "💨", "title": "Produz", "text": "Alimento e gás oxigênio"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Pigmentos"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🎨", "title": "Urucum / jenipapo", "text": "Tintas naturais indígenas"},
                        {"icon": "📄", "title": "Cromatografia", "text": "Separa cores de uma folha"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Óleos vegetais"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["", "Essencial", "Vegetal"],
                    "rows": [
                        ["De", "Folhas, flores aromáticas", "Frutos e sementes"],
                        ["Como", "Destilação", "Prensagem"],
                        ["Para", "Perfume, remédio", "Cozinha"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Oceanos"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🌊", "title": "Fitoplâncton", "text": "Produtor marinho"},
                        {"icon": "🫁", "title": "Oxigênio", "text": "Muito O₂ vem dos oceanos"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "6. Fósseis"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🦴", "title": "Fóssil", "text": "Vestígio do passado em rocha"},
                        {"icon": "👣", "title": "Pegadas", "text": "Bípede x quadrúpede"},
                        {"icon": "🇧🇷", "title": "Dinos BR", "text": "Brasilotitan · Pampadromaeus"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "7. Predador e presa"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["", "Predador", "Presa"],
                    "rows": [
                        ["Exemplo", "Crocodilo — emboscada", "Suricato — vigia em grupo"],
                        ["Recurso", "Veneno, dentes, força", "Camuflagem, fuga, sentidos"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "8. Cadeias alimentares"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🌳", "title": "Produtor", "text": "Planta (fotossíntese)"},
                        {"icon": "➡️", "title": "Setas", "text": "Indicam quem come quem"},
                        {"icon": "🍄", "title": "Decompositores", "text": "Fungos e bactérias no solo"},
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "O oxigênio da atmosfera não vem só das florestas — algas e fitoplâncton "
                    "dos oceanos produzem grande parte dele.",
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
                "topic": "energy_diet",
                "question": "Animais que se alimentam apenas de plantas e suas partes são chamados de:",
                "options": ["Carnívoros", "Herbívoros", "Onívoros", "Decompositores"],
                "correct_answer": 1,
                "explanation": "Herbívoros comem plantas — raízes, folhas, flores, frutos e sementes.",
                "difficulty": "basic",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-002",
                "type": "multiple_choice",
                "topic": "energy_diet",
                "question": (
                    "Leia as afirmativas sobre alimentação:\n"
                    "I. Onívoros comem plantas e outros animais.\n"
                    "II. Carnívoros obtêm energia comendo apenas plantas.\n"
                    "III. Plantas são importantes como alimento e abrigo.\n"
                    "IV. Todos os seres vivos precisam de energia.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, III e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, III e IV corretas. Carnívoros comem animais, não plantas (II errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-003",
                "type": "multiple_choice",
                "topic": "photosynthesis",
                "question": "A fotossíntese é um processo realizado pelas plantas que precisa de:",
                "options": [
                    "Apenas água, sem luz",
                    "Luz solar, água e gás carbônico",
                    "Somente gás oxigênio do ar",
                    "Apenas nutrientes do solo, sem luz",
                ],
                "correct_answer": 1,
                "explanation": "Fotossíntese usa luz, água (raízes) e gás carbônico (folhas).",
                "difficulty": "basic",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-004",
                "type": "multiple_choice",
                "topic": "photosynthesis",
                "question": "O pigmento verde presente principalmente nas folhas, que absorve luz para a fotossíntese, chama-se:",
                "options": ["Urucum", "Clorofila", "Jenipapo", "Amido"],
                "correct_answer": 1,
                "explanation": "Clorofila é o pigmento verde das folhas.",
                "difficulty": "basic",
                "source_assets": sa("page-006.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-005",
                "type": "multiple_choice",
                "topic": "photosynthesis",
                "question": (
                    "Leia as afirmativas sobre partes da planta:\n"
                    "I. A raiz absorve água e nutrientes do solo.\n"
                    "II. A folha é onde ocorre a fotossíntese.\n"
                    "III. O fruto protege a semente.\n"
                    "IV. O caule fixa a planta no solo.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e III", "II, III e IV", "I e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e III corretas. Quem fixa no solo é a raiz; o caule sustenta e transporta (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-007.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-006",
                "type": "multiple_choice",
                "topic": "pigments",
                "question": "Povos indígenas do Brasil usam plantas como urucum e jenipapo para:",
                "options": [
                    "Construir casas de madeira",
                    "Extrair pigmentos naturais para pintura corporal",
                    "Produzir gás oxigênio",
                    "Fazer fósseis de dinossauros",
                ],
                "correct_answer": 1,
                "explanation": "Urucum e jenipapo fornecem tintas naturais — identidade cultural de cada povo.",
                "difficulty": "basic",
                "source_assets": sa("page-010.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-007",
                "type": "multiple_choice",
                "topic": "plant_oils",
                "question": "Óleos essenciais diferem dos óleos vegetais porque:",
                "options": [
                    "São extraídos de frutos e sementes e usados só na cozinha",
                    "Vêm de partes aromáticas das plantas e são obtidos muitas vezes por destilação",
                    "Não têm origem vegetal",
                    "São iguais ao azeite de oliva",
                ],
                "correct_answer": 1,
                "explanation": "Óleos essenciais vêm de folhas/flores aromáticas (destilação); óleos vegetais de frutos/sementes (cozinha).",
                "difficulty": "intermediate",
                "source_assets": sa("page-013.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-008",
                "type": "multiple_choice",
                "topic": "marine",
                "question": (
                    "Por que NÃO é correto dizer que todo o gás oxigênio da atmosfera "
                    "vem apenas das florestas?"
                ),
                "options": [
                    "Porque plantas não produzem oxigênio",
                    "Porque algas e fitoplâncton dos oceanos também fazem fotossíntese e liberam oxigênio",
                    "Porque o oxigênio vem só de aviões",
                    "Porque dinossauros produzem oxigênio",
                ],
                "correct_answer": 1,
                "explanation": "Fitoplâncton e algas marinhas produzem grande parte do oxigênio atmosférico.",
                "difficulty": "intermediate",
                "source_assets": sa("page-021.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-009",
                "type": "multiple_choice",
                "topic": "fossils",
                "question": "Fósseis são:",
                "options": [
                    "Animais vivos encontrados na floresta",
                    "Restos ou marcas de seres vivos antigos preservados em rochas ou outros materiais",
                    "Plantas que fazem fotossíntese",
                    "Somente pegadas de pássaros modernos",
                ],
                "correct_answer": 1,
                "explanation": "Fósseis são vestígios do passado — ossos, dentes, pegadas, conchas etc.",
                "difficulty": "basic",
                "source_assets": sa("page-023.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-010",
                "type": "multiple_choice",
                "topic": "predator_prey",
                "question": (
                    "Leia as afirmativas sobre predadores e presas:\n"
                    "I. Predadores têm adaptações para capturar alimento.\n"
                    "II. Presas podem viver em grupo para detectar perigo.\n"
                    "III. Camuflagem pode ajudar predadores e presas.\n"
                    "IV. Presas nunca usam velocidade para fugir.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e III", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Presas também fogem com velocidade (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-031.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-011",
                "type": "multiple_choice",
                "topic": "food_chains",
                "question": "Na cadeia alimentar planta → pulgão → joaninha, a joaninha é:",
                "options": [
                    "Produtora",
                    "Consumidora primária",
                    "Consumidora secundária",
                    "Decompositora",
                ],
                "correct_answer": 2,
                "explanation": "Pulgão come planta (primário); joaninha come pulgão (secundário).",
                "difficulty": "intermediate",
                "source_assets": sa("page-027.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-012",
                "type": "multiple_choice",
                "topic": "food_chains",
                "question": (
                    "Leia as afirmativas sobre cadeias alimentares:\n"
                    "I. Plantas são produtoras porque fazem fotossíntese.\n"
                    "II. Fungos e bactérias decompõem matéria orgânica no solo.\n"
                    "III. As setas indicam quem serve de alimento para quem.\n"
                    "IV. Consumidores produzem seu próprio alimento pela fotossíntese.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e III", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Consumidores não fazem fotossíntese (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-033.jpg"),
                "section": "final_quiz",
            },
        ],
    }
