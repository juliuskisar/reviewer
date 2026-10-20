"""Conteúdo pedagógico da revisão Pedro — Inglês PE 3º trimestre (Units 6 e 7)."""

from __future__ import annotations

REVIEW_ID = "pedro-pe-ingles-3tri"
ASSET_PREFIX = "assets/pedro_pe_ingles_3_tri"


def _src(page: str) -> dict:
    return {
        "asset": f"{ASSET_PREFIX}/{page}",
        "origin_type": "observed",
        "evidence": [f"Caderno de Inglês — {page}"],
    }


def build_content() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Inglês — PE 3º Trimestre",
        "subtitle": "Pedro · 6º ano · Units 6 (Going Shopping) e 7 (Amazing Places)",
        "language": "pt-BR",
        "discipline": "Inglês",
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
                    "text": "Comparativos e superlativos de adjetivos; estrutura (not) as ... as; "
                    "vocabulário de compras; quantificadores a/an, some, any, much, many e a lot of. "
                    "Reserve cerca de 55 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "📊", "title": "Comparative", "text": "older · bigger · more expensive + than"},
                        {"icon": "🏆", "title": "Superlative", "text": "the oldest · the biggest · the most famous"},
                        {"icon": "⚖️", "title": "As ... as", "text": "as high as · not as big as"},
                        {"icon": "🛍️", "title": "Shopping", "text": "Look at this... · I'll take it"},
                        {"icon": "🔢", "title": "Some / Any", "text": "some (afirm.) · any (neg./perg.)"},
                        {"icon": "💻", "title": "Much / Many", "text": "much + incontável · many + contável"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Unit 6 — Going Shopping (comparativos e quantificadores)",
                        "Unit 7 — Amazing Places (superlativos e lugares)",
                        "Language Ground 1 e 2 — regras gramaticais",
                        "Speak Up / Listen Up — diálogos do caderno",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Observe exemplos em inglês.",
                            "tip": "Compare: taller than x the tallest.",
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
                            "description": "Questões no estilo Language Ground e Speak Up.",
                            "tip": "Em questões I–IV, leia cada afirmativa separadamente.",
                        },
                        {
                            "title": "Prática escrita",
                            "panel": "escrita",
                            "panel_label": "Prática escrita",
                            "description": "Escreva palavras e frases curtas em inglês — o corretor verifica na hora.",
                            "tip": "Revise ortografia de comparativos (-er, more) e superlativos (the -est, the most).",
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
            *_topic_comparative_adjectives(),
            *_topic_comparative_spelling(),
            *_topic_not_as_as(),
            *_topic_going_shopping(),
            *_topic_superlative_forms(),
            *_topic_superlative_rules(),
            *_topic_a_an_some_any(),
            *_topic_much_many(),
        ],
    }


def _topic_comparative_adjectives() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "1. Comparativos — adjetivos + than"},
            "topic_id": "comparative_adjectives",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Usamos o **comparativo** para comparar **duas** coisas ou pessoas. "
                "A estrutura típica é: **adjetivo comparativo + than**. "
                "Ex.: My feet are smaller than my dad's feet. · Is math more difficult than history?",
            },
            "topic_id": "comparative_adjectives",
            "sources": [_src("page-003.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Formação (Language Ground 1 — Unit 6)",
                "headers": ["Tipo", "Regra", "Exemplo"],
                "rows": [
                    ["Curto (1 sílaba)", "adjetivo + -er + than", "old → older than · small → smaller than"],
                    ["Termina em -e", "+ -r + than", "large → larger than"],
                    ["CVC (vogal+consoante+vogal)", "duplica + -er", "big → bigger than"],
                    ["2 sílabas em -y", "-y → -ier + than", "heavy → heavier than"],
                    ["Longo (2+ sílabas)", "more + adj. + than", "expensive → more expensive than"],
                    ["Irregular", "forma própria + than", "good → better than · bad → worse than"],
                ],
            },
            "topic_id": "comparative_adjectives",
        },
    ]


def _topic_comparative_spelling() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "2. Ortografia dos comparativos"},
            "topic_id": "comparative_spelling",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "O caderno pede completar tabelas com adjetivos como **interesting, old, busy, smart, pretty, famous, bad, sad, big**. "
                "Observe se o adjetivo é curto ou longo antes de escolher -er ou more.",
            },
            "topic_id": "comparative_spelling",
            "sources": [_src("page-003.jpg"), _src("page-005.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "📏", "title": "1 sílaba", "text": "old → older · smart → smarter"},
                    {"icon": "🔁", "title": "CVC", "text": "big → bigger · sad → sadder"},
                    {"icon": "✨", "title": "-y", "text": "pretty → prettier · busy → busier"},
                    {"icon": "📚", "title": "Longo", "text": "famous → more famous · interesting → more interesting"},
                    {"icon": "⚡", "title": "Irregular", "text": "good → better · bad → worse · far → farther/further"},
                ],
            },
            "topic_id": "comparative_spelling",
        },
    ]


def _topic_not_as_as() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "3. (Not) as ... as — igualdade e diferença"},
            "topic_id": "not_as_as",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "**As + adjetivo + as** compara duas coisas **no mesmo nível**: "
                "The Pyrenees are as high as the Alps. "
                "**Not as + adjetivo + as** (ou **isn't as ... as**) indica que uma coisa é **menos** que a outra — "
                "equivalente a um comparativo: Rome isn't as old as Athens = Athens is older than Rome.",
            },
            "topic_id": "not_as_as",
            "sources": [_src("page-001.jpg"), _src("page-007.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Modelos do caderno",
                "headers": ["Estrutura", "Exemplo"],
                "rows": [
                    ["as + adj. + as", "This exercise is as easy as ABC."],
                    ["not as + adj. + as", "The London Eye is not as high as the Eiffel Tower."],
                    ["aren't / isn't as ... as", "You're not as white as a sheet!"],
                    ["Erro comum", "❌ as bigger as → ✅ as big as"],
                ],
            },
            "topic_id": "not_as_as",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Reescrever com not as ... as:",
                "text": "The Parthenon is older than the Colosseum → "
                "The Colosseum is not as old as the Parthenon.",
            },
            "topic_id": "not_as_as",
        },
    ]


def _topic_going_shopping() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "4. Going Shopping — linguagem útil"},
            "topic_id": "going_shopping",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Na Unit 6, Marion e John comparam roupas na loja. "
                "Use estas frases para falar de preço, estilo e decisão de compra.",
            },
            "topic_id": "going_shopping",
            "sources": [_src("page-006.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "👀", "title": "Mostrar", "text": "Look at this / these..."},
                    {"icon": "😍", "title": "Opinião", "text": "It's lovely / gorgeous · It looks good on me"},
                    {"icon": "💰", "title": "Comparar preço", "text": "more expensive than · cheaper than · nicer than"},
                    {"icon": "👗", "title": "Combinar", "text": "It goes well with my black pants."},
                    {"icon": "🛒", "title": "Decidir", "text": "I'll take it. / I'll get the red sweater."},
                    {"icon": "👟", "title": "Roupas", "text": "hat · sweater · pants · sneakers · shoes"},
                ],
            },
            "topic_id": "going_shopping",
        },
    ]


def _topic_superlative_forms() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "5. Superlativos — the + adjetivo"},
            "topic_id": "superlative_forms",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "O **superlativo** destaca **uma** coisa entre **três ou mais**. "
                "Quase sempre usamos **the** antes: the biggest pyramid · the most famous painter. "
                "Exemplos do caderno: the loveliest building · the best Roman ruins · the most popular sport.",
            },
            "topic_id": "superlative_forms",
            "sources": [_src("page-002.jpg"), _src("page-005.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Comparativo x superlativo (exemplos)",
                "headers": ["Adjetivo", "Comparativo", "Superlativo"],
                "rows": [
                    ["short", "shorter", "the shortest"],
                    ["new / hot / sad", "newer / hotter / sadder", "the newest / hottest / saddest"],
                    ["funny / pretty", "funnier / prettier", "the funniest / prettiest"],
                    ["interesting / beautiful", "more interesting", "the most interesting"],
                    ["good / bad", "better / worse", "the best / the worst"],
                ],
            },
            "topic_id": "superlative_forms",
        },
    ]


def _topic_superlative_rules() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "6. Regras de ortografia — superlativos"},
            "topic_id": "superlative_rules",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "As regras espelham os comparativos, mas com **-est** ou **the most**. "
                "Unit 7 traz lugares famosos: Great Pyramid, Taj Mahal, Amazon rainforest.",
            },
            "topic_id": "superlative_rules",
            "sources": [_src("page-005.jpg"), _src("page-002.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Três regras principais (Language Ground 1 — Unit 7)",
                "headers": ["Regra", "Exemplo"],
                "rows": [
                    ["Curto: the + adj. + -est", "small → the smallest · old → the oldest"],
                    ["Longo: the most + adj.", "famous → the most famous"],
                    ["Irregular", "good → the best · bad → the worst"],
                    ["Sempre", "Use **the** before all superlatives (caderno)."],
                ],
            },
            "topic_id": "superlative_rules",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Pegadinha:",
                "text": "❌ the goodest / the more important → ✅ the best / the most important.",
            },
            "topic_id": "superlative_rules",
        },
    ]


def _topic_a_an_some_any() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "7. A / An, Some, Any"},
            "topic_id": "a_an_some_any",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "**A / an** = um/uma (singular contável): a keyboard · an 18.5-inch screen. "
                "**Some** = algum(ns) em frases afirmativas (contável plural ou incontável). "
                "**Any** em negativas e perguntas: don't have any money · Do you have any games?",
            },
            "topic_id": "a_an_some_any",
            "sources": [_src("page-004.jpg"), _src("page-008.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Uso rápido (Language Ground 2)",
                "headers": ["Situação", "Escolha"],
                "rows": [
                    ["Singular contável (primeira vez)", "a / an (vogal → an)"],
                    ["Afirmativa plural/incontável", "some (some interesting features)"],
                    ["Negativa", "any (doesn't have any memory)"],
                    ["Pergunta", "any (Does it have any speakers?)"],
                ],
            },
            "topic_id": "a_an_some_any",
        },
    ]


def _topic_much_many() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "8. Much, Many, A lot of — How much / How many"},
            "topic_id": "much_many",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "**Many** + substantivos **contáveis** no plural: many computers · How many teachers? "
                "**Much** + **incontáveis**: much memory · much ink · How much money? "
                "**A lot of** funciona com ambos em frases afirmativas: a lot of movies · a lot of memory.",
            },
            "topic_id": "much_many",
            "sources": [_src("page-004.jpg"), _src("page-008.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🖥️", "title": "Many", "text": "How many flash drives? · many pictures"},
                    {"icon": "💾", "title": "Much", "text": "much information · doesn't have much memory"},
                    {"icon": "📦", "title": "A lot of", "text": "a lot of DVDs · a lot of homework"},
                    {"icon": "❓", "title": "Perguntas", "text": "How much = incontável · How many = contável"},
                ],
            },
            "topic_id": "much_many",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Negativa:",
                "text": "Em negativas preferimos much/many, não a lot of: "
                "It doesn't have much memory (não many memory).",
            },
            "topic_id": "much_many",
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
                    "text": "Revise cada bloco abaixo. Se algo ficou confuso, volte à aba Explicações.",
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "1. Comparativo + than"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "➕", "title": "Curto", "text": "-er + than · bigger than"},
                        {"icon": "📖", "title": "Longo", "text": "more + adj. + than"},
                        {"icon": "⚡", "title": "Irregular", "text": "better · worse · more · less"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. (Not) as ... as"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "=", "title": "Igual", "text": "as + adj. + as"},
                        {"icon": "≠", "title": "Menos", "text": "not as + adj. + as"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Superlativo"}},
            {
                "type": "comparison_table",
                "content": {
                    "caption": "Formas",
                    "headers": ["Tipo", "Forma"],
                    "rows": [
                        ["Curto", "the + -est (the oldest)"],
                        ["Longo", "the most + adj."],
                        ["Irregular", "the best / the worst"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Shopping"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🛍️", "title": "Frases", "text": "Look at this · more expensive than · I'll take it"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Some / Any / Much / Many"}},
            {
                "type": "comparison_table",
                "content": {
                    "caption": "Quantificadores",
                    "headers": ["Palavra", "Uso"],
                    "rows": [
                        ["a / an", "singular contável"],
                        ["some", "afirmativa"],
                        ["any", "negativa / pergunta"],
                        ["many / much", "contável / incontável"],
                        ["a lot of", "afirmativa (ambos)"],
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha da PE:",
                    "text": "The before superlatives. As big as (não as bigger as). "
                    "Didn't + base só vale para passado — aqui: some/any e much/many. "
                    "Good → better (comp.) / the best (super.).",
                },
            },
        ],
    }


def _written_exercises(sa) -> list[dict]:
    """Prática escrita — aba Prática escrita (section: escrita)."""
    return [
        {
            "id": "en3-wr-001",
            "type": "written_language",
            "topic": "comparative_adjectives",
            "question": "Escreva o comparativo de «old» (uma palavra, em inglês):",
            "correct_answer": "older",
            "accepted_answers": ["Older"],
            "input_mode": "word",
            "explanation": "Adjetivo curto de uma sílaba → -er: old → older.",
            "difficulty": "basic",
            "source_assets": sa("page-003.jpg"),
            "section": "escrita",
        },
        {
            "id": "en3-wr-002",
            "type": "written_language",
            "topic": "comparative_adjectives",
            "question": "Escreva o comparativo de «good» (irregular):",
            "correct_answer": "better",
            "accepted_answers": ["Better"],
            "input_mode": "word",
            "mistake_hints": [
                {"contains": "gooder", "message": "Good é irregular — não use -er."},
                {"contains": "more good", "message": "Good não usa more … than."},
            ],
            "explanation": "Comparativo irregular: good → better + than.",
            "difficulty": "basic",
            "source_assets": sa("page-003.jpg"),
            "section": "escrita",
        },
        {
            "id": "en3-wr-003",
            "type": "written_language",
            "topic": "comparative_spelling",
            "question": "Escreva o comparativo de «big» (lembre da consoante duplicada):",
            "correct_answer": "bigger",
            "accepted_answers": ["Bigger"],
            "input_mode": "word",
            "explanation": "Padrão CVC: big → bigger.",
            "difficulty": "basic",
            "source_assets": sa("page-003.jpg"),
            "section": "escrita",
        },
        {
            "id": "en3-wr-004",
            "type": "written_language",
            "topic": "comparative_adjectives",
            "question": (
                "Complete a frase em inglês: «Are video games _____ than DVDs?» "
                "(use o comparativo de cheap)"
            ),
            "correct_answer": "Are video games cheaper than DVDs?",
            "accepted_answers": [
                "Are video games cheaper than dvds?",
                "are video games cheaper than DVDs?",
            ],
            "input_mode": "sentence",
            "explanation": "Cheap → cheaper + than.",
            "difficulty": "basic",
            "source_assets": sa("page-003.jpg"),
            "section": "escrita",
        },
        {
            "id": "en3-wr-005",
            "type": "written_language",
            "topic": "not_as_as",
            "question": (
                "Reescreva usando not as … as: «The Eiffel Tower is higher than the London Eye.»"
            ),
            "correct_answer": "The London Eye is not as high as the Eiffel Tower.",
            "accepted_answers": [
                "The London Eye isn't as high as the Eiffel Tower.",
                "the london eye is not as high as the eiffel tower.",
            ],
            "input_mode": "sentence",
            "explanation": "Inverta sujeitos e use not as + adjetivo base + as.",
            "difficulty": "intermediate",
            "source_assets": sa("page-001.jpg"),
            "section": "escrita",
        },
        {
            "id": "en3-wr-006",
            "type": "written_language",
            "topic": "superlative_forms",
            "question": "Escreva o superlativo de «popular» (com the):",
            "correct_answer": "the most popular",
            "accepted_answers": ["The most popular", "the Most Popular"],
            "input_mode": "word",
            "explanation": "Adjetivo longo → the most + adjetivo.",
            "difficulty": "basic",
            "source_assets": sa("page-002.jpg"),
            "section": "escrita",
        },
        {
            "id": "en3-wr-007",
            "type": "written_language",
            "topic": "superlative_rules",
            "question": "Escreva o superlativo de «good» (duas palavras, com the):",
            "correct_answer": "the best",
            "accepted_answers": ["The best"],
            "input_mode": "word",
            "mistake_hints": [
                {"contains": "goodest", "message": "Good → the best (irregular)."},
            ],
            "explanation": "Irregular: good → the best.",
            "difficulty": "basic",
            "source_assets": sa("page-005.jpg"),
            "section": "escrita",
        },
        {
            "id": "en3-wr-008",
            "type": "written_language",
            "topic": "a_an_some_any",
            "question": "Complete em inglês: «I don't have _____ money.» (negativa, incontável)",
            "correct_answer": "I don't have any money.",
            "accepted_answers": [
                "I do not have any money.",
                "i don't have any money.",
            ],
            "input_mode": "sentence",
            "explanation": "Negativa + incontável → any.",
            "difficulty": "basic",
            "source_assets": sa("page-004.jpg"),
            "section": "escrita",
        },
        {
            "id": "en3-wr-009",
            "type": "written_language",
            "topic": "much_many",
            "question": "Complete a pergunta: «_____ computers are there in your home?»",
            "correct_answer": "How many computers are there in your home?",
            "accepted_answers": [
                "How many computers are there in your home",
                "how many computers are there in your home?",
            ],
            "input_mode": "sentence",
            "explanation": "Computers = contável plural → How many.",
            "difficulty": "intermediate",
            "source_assets": sa("page-004.jpg"),
            "section": "escrita",
        },
        {
            "id": "en3-wr-010",
            "type": "written_language",
            "topic": "going_shopping",
            "question": (
                "No diálogo da loja, Marion compara suéteres. Complete: "
                "«I think it's _____ than the blue one.» (comparativo de nice)"
            ),
            "correct_answer": "I think it's nicer than the blue one.",
            "accepted_answers": [
                "I think it is nicer than the blue one.",
                "i think it's nicer than the blue one.",
            ],
            "input_mode": "sentence",
            "explanation": "Nice → nicer (consoante + y → -ier).",
            "difficulty": "basic",
            "source_assets": sa("page-006.jpg"),
            "section": "escrita",
        },
    ]


def build_exercises() -> dict:
    def sa(page: str) -> list[str]:
        return [f"{ASSET_PREFIX}/{page}"]

    mc_exercises = [
            {
                "id": "en3-pe-001",
                "type": "multiple_choice",
                "topic": "comparative_adjectives",
                "question": "Qual frase usa o comparativo corretamente?",
                "options": [
                    "My cat is old than Mary's cat.",
                    "My cat is older than Mary's cat.",
                    "My cat is more old than Mary's cat.",
                    "My cat is the older than Mary's cat.",
                ],
                "correct_answer": 1,
                "explanation": "Adjetivo curto old → older + than.",
                "difficulty": "basic",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "en3-pe-002",
                "type": "multiple_choice",
                "topic": "comparative_adjectives",
                "question": (
                    "Leia as afirmativas sobre comparativos:\n"
                    "I. Comparativos comparam duas coisas.\n"
                    "II. Adjetivos longos usam more ... than.\n"
                    "III. Good → gooder than é a forma correta.\n"
                    "IV. Than aparece depois do comparativo.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e IV", "II e III", "I e III", "III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e IV corretas. Good é irregular → better (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "en3-pe-003",
                "type": "multiple_choice",
                "topic": "comparative_spelling",
                "question": "Qual é o comparativo correto de big?",
                "options": ["biger", "bigger", "more big", "the bigger"],
                "correct_answer": 1,
                "explanation": "Padrão CVC: big → bigger (consoante duplicada + -er).",
                "difficulty": "basic",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "en3-pe-004",
                "type": "multiple_choice",
                "topic": "comparative_spelling",
                "question": (
                    "Sobre ortografia comparativa:\n"
                    "I. Pretty → prettier (y → i + -er).\n"
                    "II. Famous → famousest.\n"
                    "III. Busy → busier.\n"
                    "IV. Intelligent → more intelligent.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, III e IV", "I, II e III"],
                "correct_answer": 2,
                "explanation": "I, III e IV corretas. Famous é longo → more famous, não famousest (II errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "en3-pe-005",
                "type": "multiple_choice",
                "topic": "not_as_as",
                "question": "Qual frase está correta?",
                "options": [
                    "Rome isn't as older as Athens.",
                    "Rome isn't as old as Athens.",
                    "Rome isn't old as Athens.",
                    "Rome is not as older as Athens.",
                ],
                "correct_answer": 1,
                "explanation": "Not as + adjetivo **base** + as: as old as.",
                "difficulty": "basic",
                "source_assets": sa("page-001.jpg"),
                "section": "exercises",
            },
            {
                "id": "en3-pe-006",
                "type": "multiple_choice",
                "topic": "not_as_as",
                "question": (
                    "The Eiffel Tower is higher than the London Eye. "
                    "Qual reescrita usa not as ... as corretamente?"
                ),
                "options": [
                    "The London Eye is not as high as the Eiffel Tower.",
                    "The London Eye is not as higher as the Eiffel Tower.",
                    "The London Eye is not high as the Eiffel Tower.",
                    "The Eiffel Tower is not as high as the London Eye.",
                ],
                "correct_answer": 0,
                "explanation": "Inverte a comparação: London Eye not as high as Eiffel Tower.",
                "difficulty": "intermediate",
                "source_assets": sa("page-001.jpg"),
                "section": "exercises",
            },
            {
                "id": "en3-pe-007",
                "type": "multiple_choice",
                "topic": "going_shopping",
                "question": (
                    "No diálogo Going Shopping, Marion diz que o suéter vermelho é "
                    "_____ than the blue one. Qual adjetivo comparativo completa o sentido de «mais bonito»?"
                ),
                "options": ["nice", "nicer", "the nicest", "more nice"],
                "correct_answer": 1,
                "explanation": "Comparação entre dois suéteres → nicer than.",
                "difficulty": "basic",
                "source_assets": sa("page-006.jpg"),
                "section": "exercises",
            },
            {
                "id": "en3-pe-008",
                "type": "multiple_choice",
                "topic": "going_shopping",
                "question": (
                    "Leia as afirmativas sobre Speak Up — Going Shopping:\n"
                    "I. Look at this / these identifica um item na loja.\n"
                    "II. I'll take it expressa decisão de compra.\n"
                    "III. More expensive than compara preços.\n"
                    "IV. Goes well with indica que combina com outra peça.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, III e IV", "I, II, III e IV"],
                "correct_answer": 3,
                "explanation": "Todas as afirmativas descrevem frases do Useful Language do caderno.",
                "difficulty": "intermediate",
                "source_assets": sa("page-006.jpg"),
                "section": "exercises",
            },
            {
                "id": "en3-pe-009",
                "type": "multiple_choice",
                "topic": "superlative_forms",
                "question": "Complete: «Soccer is _____ sport worldwide.» (popular)",
                "options": [
                    "the more popular",
                    "the most popular",
                    "most popular",
                    "the popularest",
                ],
                "correct_answer": 1,
                "explanation": "Adjetivo longo → the most popular.",
                "difficulty": "basic",
                "source_assets": sa("page-002.jpg"),
                "section": "exercises",
            },
            {
                "id": "en3-pe-010",
                "type": "multiple_choice",
                "topic": "superlative_forms",
                "question": (
                    "Sobre superlativos:\n"
                    "I. Usamos the antes da maioria dos superlativos.\n"
                    "II. Good → the best.\n"
                    "III. Short → the shorter.\n"
                    "IV. Interesting → the most interesting.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e IV", "II, III e IV", "I e III"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Short → the shortest, não the shorter (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-002.jpg"),
                "section": "exercises",
            },
            {
                "id": "en3-pe-011",
                "type": "multiple_choice",
                "topic": "superlative_rules",
                "question": "Qual frase está correta (Unit 7 — Amazing Places)?",
                "options": [
                    "I think New York is the goodest city for music.",
                    "I think New York is the best city for music.",
                    "I think New York is the better city for music.",
                    "I think New York is best city for music.",
                ],
                "correct_answer": 1,
                "explanation": "Good → the best (irregular). The antes do superlativo.",
                "difficulty": "basic",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "en3-pe-012",
                "type": "multiple_choice",
                "topic": "superlative_rules",
                "question": (
                    "Leia as afirmativas:\n"
                    "I. The Amazon hosts the most important rainforest (long adj.).\n"
                    "II. Small → the smallest segue regra de uma sílaba.\n"
                    "III. Bad → the baddest.\n"
                    "IV. The loveliest usa -iest após consoante + y.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, II e IV", "II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. Bad → the worst (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "en3-pe-013",
                "type": "multiple_choice",
                "topic": "a_an_some_any",
                "question": "Qual frase está correta?",
                "options": [
                    "I need a hour to finish.",
                    "I need an hour to finish.",
                    "I need any hour to finish.",
                    "I need some hour to finish.",
                ],
                "correct_answer": 1,
                "explanation": "Hour começa com som de vogal → an hour.",
                "difficulty": "basic",
                "source_assets": sa("page-008.jpg"),
                "section": "exercises",
            },
            {
                "id": "en3-pe-014",
                "type": "multiple_choice",
                "topic": "a_an_some_any",
                "question": (
                    "Sobre a / an / some / any:\n"
                    "I. There isn't some fruit — usa any na negativa.\n"
                    "II. Do you have any good games? — pergunta.\n"
                    "III. I have an amazing new computer.\n"
                    "IV. Some of these exercises are easy — some com plural.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e III", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "II, III e IV corretas. Negativa: isn't any fruit (I errada — não some).",
                "difficulty": "intermediate",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "en3-pe-015",
                "type": "multiple_choice",
                "topic": "much_many",
                "question": "Qual pergunta está correta?",
                "options": [
                    "How much computers are there in your home?",
                    "How many computers are there in your home?",
                    "How many memory is on the laptop?",
                    "How much teachers are in your school?",
                ],
                "correct_answer": 1,
                "explanation": "Computers = contável plural → How many.",
                "difficulty": "basic",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "en3-pe-016",
                "type": "multiple_choice",
                "topic": "much_many",
                "question": (
                    "Leia as afirmativas sobre much / many / a lot of:\n"
                    "I. Much + substantivos incontáveis (much ink).\n"
                    "II. Many + substantivos contáveis no plural.\n"
                    "III. A lot of só com incontáveis.\n"
                    "IV. How much pergunta quantidade incontável.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "I, II e IV", "II e III", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. A lot of funciona com contáveis e incontáveis (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-008.jpg"),
                "section": "final_quiz",
            },
        ]

    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "exercises": mc_exercises + _written_exercises(sa),
    }
