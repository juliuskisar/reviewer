"""Conteúdo pedagógico da revisão Pedro — Inglês PE 2º trimestre (Units 3 e 4)."""

from __future__ import annotations

REVIEW_ID = "pedro-pe-ingles-2tri"
ASSET_PREFIX = "assets/pedro_pe_ingles_2_tri"


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
        "title": "Revisão de Inglês — PE 2º Trimestre",
        "subtitle": "Pedro · 6º ano · Units 3 (Going Places) e 4 (History)",
        "language": "pt-BR",
        "discipline": "Inglês",
        "grade": "6º ano",
        "metadata": {
            "student_name": "Pedro",
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
                    "text": "Simple Past (passado simples): afirmativo, negativo, perguntas e respostas curtas; "
                    "regras de ortografia do -ed; verbos irregulares; could/couldn't; vocabulário de transporte "
                    "e desastres naturais. Reserve cerca de 50 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "✅", "title": "Afirmativo", "text": "visited · played · tried · went"},
                        {"icon": "❌", "title": "Negativo", "text": "didn't + base (didn't go)"},
                        {"icon": "❓", "title": "Perguntas", "text": "Did you travel? · Yes, I did."},
                        {"icon": "✏️", "title": "Ortografia", "text": "-ed · -d · -ied · stop→stopped"},
                        {"icon": "🚌", "title": "Transporte", "text": "bike · bus · boat · car · plane"},
                        {"icon": "💪", "title": "Could", "text": "Habilidade no passado · couldn't = não podia"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Unit 3 — Going Places (transporte e viagem)",
                        "Unit 4 — History (passado, história e desastres)",
                        "Language Genie — resumo gramatical",
                        "Recall It! 2 — revisão das duas units",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Observe os exemplos em inglês.",
                            "tip": "Leia em voz alta: I visited London last week.",
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
                            "description": "Questões no estilo Language Ground e Recall It! do caderno.",
                            "tip": "Em questões I–IV, leia cada afirmativa separadamente.",
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
            *_topic_simple_past_regular(),
            *_topic_spelling_rules(),
            *_topic_time_expressions(),
            *_topic_transport_travel(),
            *_topic_simple_past_negative(),
            *_topic_irregular_verbs(),
            *_topic_questions_short_answers(),
            *_topic_could_couldnt(),
        ],
    }


def _topic_simple_past_regular() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "1. Simple Past — afirmativo (verbos regulares)"},
            "topic_id": "simple_past_regular",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "O Simple Past descreve ações ou situações **terminadas** no passado. "
                "Nos verbos regulares, formamos o passado com **-ed** ou **-d**. "
                "A forma é igual para todas as pessoas: I visited, he visited, they visited.",
            },
            "topic_id": "simple_past_regular",
            "sources": [_src("page-001.jpg"), _src("page-007.jpg"), _src("page-014.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Regras do caderno (Language Ground 1)",
                "headers": ["Regra", "Exemplo"],
                "rows": [
                    ["Ação terminada no passado", "They tried to ride their bike across a park."],
                    ["Referências de tempo", "yesterday · last week · two years ago · in 1909"],
                    ["Verbo regular: base + -ed/-d", "design → designed · decide → decided"],
                    ["Mesma forma para I/you/he/she/it/we/they", "He arrived in England after 37 minutes."],
                ],
            },
            "topic_id": "simple_past_regular",
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "✈️", "title": "designed", "text": "Gideon Cardozo designed the Skycar."},
                    {"icon": "🚗", "title": "decided", "text": "Frank Rinderknecht decided to build a car."},
                    {"icon": "🚲", "title": "invented", "text": "Two friends invented the Couchbike."},
                    {"icon": "🏁", "title": "arrived", "text": "Blériot arrived in England in 1909."},
                ],
            },
            "topic_id": "simple_past_regular",
        },
    ]


def _topic_spelling_rules() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "2. Ortografia do passado (-ed, -d, -ied)"},
            "topic_id": "spelling_rules",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Nem todo verbo regular recebe -ed da mesma forma. "
                "Observe a terminação do verbo na forma base antes de conjugar.",
            },
            "topic_id": "spelling_rules",
            "sources": [_src("page-003.jpg"), _src("page-009.jpg"), _src("page-015.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Quatro regras principais",
                "headers": ["Regra", "Base", "Passado"],
                "rows": [
                    ["Maioria: + -ed", "call · play · want", "called · played · wanted"],
                    ["Termina em -e: + -d", "like · use · live", "liked · used · lived"],
                    ["Consoante + y: -y + -ied", "try · cry · marry", "tried · cried · married"],
                    ["Vogal + y: + -ed", "play · enjoy", "played · enjoyed"],
                    ["Vogal tônica + consoante: duplica + -ed", "stop · plan", "stopped · planned"],
                ],
            },
            "topic_id": "spelling_rules",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Pronúncia do -ed:",
                "text": "O som pode ser /t/ (stopped), /d/ (lived) ou /ɪd/ (started, wanted). "
                "O caderno treina isso em SAY THE WORD.",
            },
            "topic_id": "spelling_rules",
        },
    ]


def _topic_time_expressions() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "3. Expressões de tempo no passado"},
            "topic_id": "time_expressions",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "O Simple Past costuma aparecer com marcadores temporais no fim da frase. "
                "Eles deixam claro **quando** a ação aconteceu.",
            },
            "topic_id": "time_expressions",
            "sources": [_src("page-011.jpg"), _src("page-015.jpg"), _src("page-014.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "📅", "title": "yesterday", "text": "I watched TV yesterday."},
                    {"icon": "🗓️", "title": "last + período", "text": "last week · last year · last night"},
                    {"icon": "⏳", "title": "ago", "text": "three months ago · two weeks ago"},
                    {"icon": "📍", "title": "in / on", "text": "in 2009 · in July · on Monday · on Tuesday"},
                ],
            },
            "topic_id": "time_expressions",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Pegadinha:",
                "text": "Dizemos on Monday (dia da semana), não in Monday. "
                "Usamos in com ano, mês ou estação: in 2015, in December.",
            },
            "topic_id": "time_expressions",
        },
    ]


def _topic_transport_travel() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "4. Transporte e viagem (Unit 3)"},
            "topic_id": "transport_travel",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "A Unit 3 «Going Places» trabalha meios de transporte e experiências de viagem. "
                "Use o passado para contar o que aconteceu em viagens, aeroportos e passeios.",
            },
            "topic_id": "transport_travel",
            "sources": [_src("page-013.jpg"), _src("page-008.jpg"), _src("page-016.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🚲", "title": "bike", "text": "ride a bike · I rode my bike last month."},
                    {"icon": "🚌", "title": "bus / train", "text": "public transportation · take the bus"},
                    {"icon": "⛵", "title": "boat / ship", "text": "sail · sail across the Atlantic"},
                    {"icon": "🚗", "title": "car / plane", "text": "drive · land · travel by plane"},
                    {"icon": "🌊", "title": "travel verbs", "text": "arrive · wait · pick · decide · return"},
                    {"icon": "🌪️", "title": "disasters (Unit 4)", "text": "earthquake · tsunami · tornado · flood"},
                ],
            },
            "topic_id": "transport_travel",
        },
    ]


def _topic_simple_past_negative() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "5. Simple Past — negativo (didn't)"},
            "topic_id": "simple_past_negative",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Para negar no passado, usamos **didn't** (did not) + **verbo na forma base**. "
                "A forma negativa é igual para verbos regulares e irregulares.",
            },
            "topic_id": "simple_past_negative",
            "sources": [_src("page-004.jpg"), _src("page-010.jpg"), _src("page-014.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Afirmativo x negativo",
                "headers": ["Afirmativo", "Negativo"],
                "rows": [
                    ["They took the potatoes.", "They didn't take the potatoes."],
                    ["Italians made ice cream.", "Italians didn't make ice cream."],
                    ["Fogg rode an elephant.", "Fogg didn't fly a hot-air balloon."],
                    ["Marco Polo discovered pasta.", "Marco Polo didn't discover pasta in China."],
                ],
            },
            "topic_id": "simple_past_negative",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Erro comum:",
                "text": "Nunca escreva didn't went ou didn't ate. "
                "Depois de didn't vem sempre o infinitivo sem to: didn't go, didn't eat.",
            },
            "topic_id": "simple_past_negative",
        },
    ]


def _topic_irregular_verbs() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "6. Verbos irregulares no passado"},
            "topic_id": "irregular_verbs",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Verbos irregulares **não** seguem a regra -ed. "
                "Cada um tem forma própria — o caderno lista os mais usados nas Units 3 e 4.",
            },
            "topic_id": "irregular_verbs",
            "sources": [_src("page-004.jpg"), _src("page-010.jpg"), _src("page-014.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Pares base → passado (do caderno)",
                "headers": ["Base", "Passado", "Base", "Passado"],
                "rows": [
                    ["go", "went", "take", "took"],
                    ["eat", "ate", "leave", "left"],
                    ["be", "was / were", "have", "had"],
                    ["make", "made", "ride", "rode"],
                    ["begin", "began", "become", "became"],
                    ["find", "found", "give", "gave"],
                ],
            },
            "topic_id": "irregular_verbs",
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🥔", "title": "History of potato", "text": "Sailors took potatoes · They ate them · Potatoes became popular."},
                    {"icon": "🍕", "title": "History of pizza", "text": "Greeks ate flatbread · People in Naples invented pizza."},
                    {"icon": "🌍", "title": "Jules Verne", "text": "He wrote the book · They rode an elephant · They didn't give up."},
                ],
            },
            "topic_id": "irregular_verbs",
        },
    ]


def _topic_questions_short_answers() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "7. Perguntas com Did e respostas curtas"},
            "topic_id": "questions_short_answers",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Perguntas no Simple Past usam **Did** + sujeito + **verbo base**. "
                "Respostas curtas: Yes, I **did**. / No, she **didn't**. — sem repetir o verbo principal.",
            },
            "topic_id": "questions_short_answers",
            "sources": [_src("page-006.jpg"), _src("page-012.jpg"), _src("page-014.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Modelo de pergunta e resposta",
                "headers": ["Pergunta", "Resposta curta"],
                "rows": [
                    ["Did your dad drive to work?", "Yes, he did. / No, he didn't."],
                    ["Did Pompeii stay hidden for 1,700 years?", "Yes, it did."],
                    ["Did Domenico Fontana discover the paintings?", "No, he didn't."],
                    ["Did the prime minister investigate the problem?", "Yes, he did."],
                ],
            },
            "topic_id": "questions_short_answers",
        },
        {
            "type": "callout",
            "content": {
                "variant": "info",
                "title": "Perguntas com Wh-:",
                "text": "Com what, where, when, how: a palavra interrogativa vem primeiro — "
                "How did he react? He covered them.",
            },
            "topic_id": "questions_short_answers",
        },
    ]


def _topic_could_couldnt() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "8. Could / Couldn't — habilidade no passado"},
            "topic_id": "could_couldnt",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Usamos **could** e **couldn't** para falar de **habilidade** ou **possibilidade** no passado. "
                "A forma é igual para todas as pessoas. Nunca use to depois: We could write (não could to write).",
            },
            "topic_id": "could_couldnt",
            "sources": [_src("page-006.jpg"), _src("page-012.jpg"), _src("page-014.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🏗️", "title": "Lisbon earthquake", "text": "Buildings could resist earthquakes."},
                    {"icon": "🔥", "title": "Fires", "text": "They couldn't stop the fires."},
                    {"icon": "🎾", "title": "Ability", "text": "I couldn't play tennis when I was 10."},
                    {"icon": "🎨", "title": "Talent", "text": "Picasso could draw well when he was young."},
                ],
            },
            "topic_id": "could_couldnt",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Could + verbo base:",
                "text": "Beethoven couldn't hear. · Messi could play soccer very well. · "
                "Dylan could read at age three, but couldn't ride a bike yet.",
            },
            "topic_id": "could_couldnt",
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
            {"type": "heading", "content": {"level": 3, "text": "1. Afirmativo regular"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "➕", "title": "Forma", "text": "base + -ed/-d · mesma para todas as pessoas"},
                        {"icon": "⏰", "title": "Uso", "text": "Ação terminada · yesterday, last year, ago"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. Ortografia"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "📝", "title": "+ -ed", "text": "call → called · look → looked"},
                        {"icon": "✂️", "title": "+ -d", "text": "use → used · like → liked"},
                        {"icon": "🔄", "title": "-ied", "text": "try → tried · stop → stopped"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Tempo"}},
            {
                "type": "comparison_table",
                "content": {
                    "caption": "Marcadores",
                    "headers": ["Expressão", "Exemplo"],
                    "rows": [
                        ["yesterday / last week", "I traveled last week."],
                        ["ago", "three months ago"],
                        ["in + ano/mês", "in 2009 · in December"],
                        ["on + dia", "on Monday · on Tuesday"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Transporte e viagem"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🚌", "title": "Nouns", "text": "bike · bus · boat · car · plane · train"},
                        {"icon": "🛫", "title": "Verbs", "text": "travel · arrive · land · drive · ride · sail"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Negativo"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "❌", "title": "Estrutura", "text": "didn't + base · They didn't go."},
                        {"icon": "⚠️", "title": "Cuidado", "text": "didn't went ✗ → didn't go ✓"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "6. Irregulares"}},
            {
                "type": "comparison_table",
                "content": {
                    "caption": "Memorize estes pares",
                    "headers": ["Base", "Past"],
                    "rows": [
                        ["go / take / eat", "went / took / ate"],
                        ["be / have / make", "was·were / had / made"],
                        ["begin / become / ride", "began / became / rode"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "7. Perguntas Did"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "❓", "title": "Pergunta", "text": "Did + subject + base?"},
                        {"icon": "✅", "title": "Resposta", "text": "Yes, I did. · No, she didn't."},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "8. Could / Couldn't"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "💪", "title": "could", "text": "Podia / conseguia no passado"},
                        {"icon": "🚫", "title": "couldn't", "text": "Não podia · sem to depois"},
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha da PE:",
                    "text": "Didn't + base (não passado). Resposta curta sem repetir verbo. "
                    "Try → tried (não tryed). On Monday, in 2009.",
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
                "id": "en-pe-001",
                "type": "multiple_choice",
                "topic": "simple_past_regular",
                "question": "Qual frase está no Simple Past afirmativo correto?",
                "options": [
                    "She visit Shakespeare's home last year.",
                    "She visited Shakespeare's home last year.",
                    "She visiting Shakespeare's home last year.",
                    "She visits Shakespeare's home last year.",
                ],
                "correct_answer": 1,
                "explanation": "Verbo regular visit → visited. Marcador last year confirma o passado.",
                "difficulty": "basic",
                "source_assets": sa("page-001.jpg"),
                "section": "exercises",
            },
            {
                "id": "en-pe-002",
                "type": "multiple_choice",
                "topic": "simple_past_regular",
                "question": (
                    "Leia as afirmativas sobre o Simple Past afirmativo:\n"
                    "I. Descreve ações terminadas no passado.\n"
                    "II. Verbos regulares recebem -ed ou -d.\n"
                    "III. A forma muda conforme he/she/it no passado regular.\n"
                    "IV. Marcadores como yesterday e ago são comuns.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e IV", "I e III", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e IV corretas. No passado regular a forma é igual para todas as pessoas (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-001.jpg"),
                "section": "exercises",
            },
            {
                "id": "en-pe-003",
                "type": "multiple_choice",
                "topic": "spelling_rules",
                "question": "Qual é a forma correta do passado de try?",
                "options": ["tryed", "tried", "tryied", "trys"],
                "correct_answer": 1,
                "explanation": "Consoante + y → omit y + -ied: try → tried.",
                "difficulty": "basic",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "en-pe-004",
                "type": "multiple_choice",
                "topic": "spelling_rules",
                "question": (
                    "Leia as afirmativas sobre ortografia do passado:\n"
                    "I. Verbos terminados em -e recebem só -d (use → used).\n"
                    "II. Stop → stopped (consoante duplicada + -ed).\n"
                    "III. Play → plaied porque termina em y.\n"
                    "IV. Marry → married (consoante + y → -ied).\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, II e IV", "III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. Play tem vogal + y → played, não plaied (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-009.jpg"),
                "section": "exercises",
            },
            {
                "id": "en-pe-005",
                "type": "multiple_choice",
                "topic": "time_expressions",
                "question": "Qual expressão de tempo está correta?",
                "options": [
                    "I traveled to the seaside the last week.",
                    "I traveled to the seaside last week.",
                    "I traveled to the seaside for three months ago.",
                    "It was my birthday in Wednesday.",
                ],
                "correct_answer": 1,
                "explanation": "last week (sem the). ago não usa for. Dia da semana: on Wednesday.",
                "difficulty": "basic",
                "source_assets": sa("page-015.jpg"),
                "section": "exercises",
            },
            {
                "id": "en-pe-006",
                "type": "multiple_choice",
                "topic": "time_expressions",
                "question": (
                    "Leia as afirmativas sobre marcadores temporais:\n"
                    "I. yesterday indica passado recente.\n"
                    "II. Usamos in com anos: in 2009.\n"
                    "III. three months ago é uma forma correta.\n"
                    "IV. on Monday significa «na segunda-feira passada» no contexto do passado.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, II e III", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e III corretas. on Monday indica o dia, mas IV é imprecisa como regra geral.",
                "difficulty": "intermediate",
                "source_assets": sa("page-011.jpg"),
                "section": "exercises",
            },
            {
                "id": "en-pe-007",
                "type": "multiple_choice",
                "topic": "transport_travel",
                "question": (
                    "Complete: «Last summer my family and I _____ to Singapore on an A380.» "
                    "Qual verbo completa corretamente?"
                ),
                "options": ["travel", "traveled", "traveling", "will travel"],
                "correct_answer": 1,
                "explanation": "Last summer = passado → traveled (verbo regular).",
                "difficulty": "basic",
                "source_assets": sa("page-008.jpg"),
                "section": "exercises",
            },
            {
                "id": "en-pe-008",
                "type": "multiple_choice",
                "topic": "transport_travel",
                "question": (
                    "No jogo Recall It!, qual palavra completa: "
                    "«Which B is a type of public transportation?»"
                ),
                "options": ["Bike", "Bus", "Boat", "Balloon"],
                "correct_answer": 1,
                "explanation": "Bus = ônibus, transporte público. Bike é individual; boat e balloon não são o foco da dica «B».",
                "difficulty": "basic",
                "source_assets": sa("page-016.jpg"),
                "section": "exercises",
            },
            {
                "id": "en-pe-009",
                "type": "multiple_choice",
                "topic": "simple_past_negative",
                "question": "Qual frase negativa está correta?",
                "options": [
                    "They didn't took the potatoes.",
                    "They didn't take the potatoes.",
                    "They not take the potatoes.",
                    "They didn't takes the potatoes.",
                ],
                "correct_answer": 1,
                "explanation": "didn't + base form: take (não took/takes).",
                "difficulty": "basic",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "en-pe-010",
                "type": "multiple_choice",
                "topic": "simple_past_negative",
                "question": (
                    "Leia as afirmativas sobre a forma negativa:\n"
                    "I. didn't funciona para verbos regulares e irregulares.\n"
                    "II. Depois de didn't vem o verbo no passado (went).\n"
                    "III. Didn't só se usa com verbos regulares.\n"
                    "IV. A forma negativa usa did not ou didn't.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "II e III", "I, II e IV", "II, III e IV"],
                "correct_answer": 0,
                "explanation": "I e IV corretas. Depois de didn't vem a base (II errada); didn't vale para todos os verbos (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "en-pe-011",
                "type": "multiple_choice",
                "topic": "irregular_verbs",
                "question": "Qual par base → passado está correto?",
                "options": [
                    "go → goed",
                    "take → took",
                    "eat → eated",
                    "be → beed",
                ],
                "correct_answer": 1,
                "explanation": "take → took. Os outros são irregulares: go→went, eat→ate, be→was/were.",
                "difficulty": "basic",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "en-pe-012",
                "type": "multiple_choice",
                "topic": "irregular_verbs",
                "question": (
                    "Leia as afirmativas sobre verbos irregulares:\n"
                    "I. Regular verbs terminam em -d ou -ed.\n"
                    "II. go → went e eat → ate são irregulares.\n"
                    "III. Todos os verbos irregulares terminam em -ed.\n"
                    "IV. was/were é o passado de be.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. Irregulares não seguem padrão -ed (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-010.jpg"),
                "section": "exercises",
            },
            {
                "id": "en-pe-013",
                "type": "multiple_choice",
                "topic": "questions_short_answers",
                "question": "Qual pergunta no Simple Past está correta?",
                "options": [
                    "Did you went to the museum?",
                    "Did you go to the museum?",
                    "Do you go to the museum yesterday?",
                    "Did you going to the museum?",
                ],
                "correct_answer": 1,
                "explanation": "Did + subject + base: Did you go…?",
                "difficulty": "basic",
                "source_assets": sa("page-012.jpg"),
                "section": "exercises",
            },
            {
                "id": "en-pe-014",
                "type": "multiple_choice",
                "topic": "questions_short_answers",
                "question": (
                    "Leia as afirmativas sobre perguntas com Did:\n"
                    "I. Did é usado para todos os sujeitos (I, you, he…).\n"
                    "II. Resposta curta: Yes, he did. (sem repetir o verbo).\n"
                    "III. Did your dad drove to work? está correta.\n"
                    "IV. No, she didn't. é resposta negativa curta válida.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, II e IV", "I, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. Com Did usa-se base drive, não drove (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-012.jpg"),
                "section": "exercises",
            },
            {
                "id": "en-pe-015",
                "type": "multiple_choice",
                "topic": "could_couldnt",
                "question": "Complete: «When I was 10, I _____ play tennis.» (não sabia jogar)",
                "options": ["could", "couldn't", "didn't could", "can"],
                "correct_answer": 1,
                "explanation": "couldn't = não tinha habilidade no passado.",
                "difficulty": "basic",
                "source_assets": sa("page-012.jpg"),
                "section": "exercises",
            },
            {
                "id": "en-pe-016",
                "type": "multiple_choice",
                "topic": "could_couldnt",
                "question": (
                    "Sobre could/couldn't, analise:\n"
                    "I. Could expressa habilidade no passado.\n"
                    "II. Nunca usamos to logo após could ou couldn't.\n"
                    "III. Couldn't é a forma negativa de could.\n"
                    "IV. Could muda de forma para he e she (coulds).\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "II e III", "I, II e III", "I, II e IV"],
                "correct_answer": 2,
                "explanation": "I, II e III corretas. Could não muda por pessoa — sem -s (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-006.jpg"),
                "section": "final_quiz",
            },
        ],
    }
