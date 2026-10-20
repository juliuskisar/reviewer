"""Conteúdo pedagógico da revisão Pedro — Português PE 2º trimestre."""

from __future__ import annotations

REVIEW_ID = "pedro-pe-portugues-2tri"
ASSET_PREFIX = "assets/pedro_pe_portugues_2_tri"

# Textos transcritos da apostila (base para exercícios de interpretação)
CTB_ART54 = (
    "Art. 54. Os condutores de motocicletas, motonetas e ciclomotores só poderão circular nas vias:\n"
    "I – utilizando capacete de segurança, com viseira ou óculos protetores;\n"
    "II – segurando o guidom com as duas mãos;\n"
    "III – usando vestuário de proteção, de acordo com as especificações do CONTRAN."
)

NETIQUETA_TEXT = (
    "Trecho das regras de netiqueta (Walmir Lima):\n"
    "1. Evite enviar mensagens EXCLUSIVAMENTE EM MAIÚSCULAS. Se bem empregadas, as maiúsculas podem "
    "ajudar a destacar, mas, em excesso, a prática é compreendida como se você estivesse gritando, "
    "podendo causar irritação.\n"
    "2. Para enfatizar frases e palavras use os recursos de sublinhar e negrito.\n"
    "3. Seja claro e objetivo.\n"
    "4. Produza textos de leitura fácil."
)

A_VOLTA_TEXT = (
    "Trecho da crônica «A volta», de Luis Fernando Veríssimo:\n"
    "Da janela do trem o homem avista a velha cidade. Seus olhos se enchem de lágrimas. Trinta anos. "
    "Desce na estação — a mesma do seu tempo — e respira fundo.\n"
    "Até o vendedor de bilhetes na frente do Clube Comercial parece o mesmo.\n"
    "— Você não tinha um cachorro?\n"
    "— O Cusca? Morreu, ih, faz vinte anos."
)

ANINHA_TEXT = (
    "Trecho de «Criança diz cada uma...», de Mário Prata:\n"
    "Aninha já estava com 2 anos. Nunca tinha cortado o cabelo. Um dia, a mãe resolveu cortar os "
    "cabelos. Aninha ficou apavorada com a tesoura.\n"
    "— Mamãe promete cortar só dois dedinhos.\n"
    "Aninha olhou para a tesoura, olhou para a mãozinha e perguntou:\n"
    "— Quais deles, mãe?"
)


def _src(page: str) -> dict:
    return {
        "asset": f"{ASSET_PREFIX}/{page}",
        "origin_type": "observed",
        "evidence": [f"Caderno de Português — {page}"],
    }


def build_content() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Português — PE 2º Trimestre",
        "subtitle": "Pedro · 6º ano · Módulos 19, 20, 22 e 23",
        "language": "pt-BR",
        "discipline": "Língua Portuguesa",
        "grade": "6º ano",
        "metadata": {
            "student_name": "Pedro",
            "exam_type": "Prova Específica (PE)",
            "estimated_duration_minutes": 60,
        },
        "study_route": [
            {"order": 1, "title": "Explicações", "section_id": "explain"},
            {"order": 2, "title": "Resumo rápido", "section_id": "summary"},
            {"order": 3, "title": "Jogo: Gênero certo", "section_id": "game_genre"},
            {"order": 4, "title": "Jogo: Detetive do humor", "section_id": "game_humor"},
            {"order": 5, "title": "Exercícios", "section_id": "exercises"},
        ],
        "sections": [
            _section_route(),
            _section_explain(),
            _section_summary(),
            _section_game_genre(),
            _section_game_humor(),
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
                    "text": "Gêneros normativos e instrucionais, netiqueta, sintagma verbal, modos e advérbios, "
                    "narrativas de humor e discurso direto/indireto — tudo do 2º trimestre. Reserve cerca de 60 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "📜", "title": "Normativo", "text": "Leis · regras · proibições"},
                        {"icon": "📋", "title": "Instrucional", "text": "Receitas · manuais · tutoriais"},
                        {"icon": "💬", "title": "Netiqueta", "text": "Etiqueta na internet"},
                        {"icon": "✏️", "title": "Sintagma verbal", "text": "Predicado com núcleo verbal"},
                        {"icon": "⏰", "title": "Modos e tempos", "text": "Indicativo · imperativo · advérbios"},
                        {"icon": "😄", "title": "Humor", "text": "Piada · anedota · surpresa"},
                        {"icon": "🗣️", "title": "Discurso", "text": "Direto ↔ indireto"},
                        {"icon": "🎮", "title": "Jogos", "text": "Dois jogos no final — teste qual prefere!"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 19 — Gêneros normativos e instrucionais",
                        "Módulo 20 — Sintagma verbal, modos e advérbios",
                        "Módulo 22 — Narrativas de humor",
                        "Módulo 23 — Discurso direto e indireto",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Leia os cards e tabelas.",
                            "tip": "Compare normativo (regra) com instrucional (como fazer).",
                        },
                        {
                            "title": "Revise o Resumo rápido",
                            "panel": "summary",
                            "panel_label": "Resumo rápido",
                            "description": "Percorra os blocos-síntese antes da PE.",
                        },
                        {
                            "title": "Jogue: Gênero certo",
                            "panel": "game_genre",
                            "panel_label": "Jogo: Gênero certo",
                            "description": "Classifique trechos em normativo ou instrucional.",
                            "tip": "Lei = normativo · receita = instrucional.",
                        },
                        {
                            "title": "Jogue: Detetive do humor",
                            "panel": "game_humor",
                            "panel_label": "Jogo: Detetive do humor",
                            "description": "Associe exemplos aos recursos de humor do caderno.",
                        },
                        {
                            "title": "Faça os Exercícios",
                            "panel": "exercises",
                            "panel_label": "Exercícios",
                            "description": "Questões com textos transcritos da apostila.",
                            "tip": "Leia o texto embutido antes de responder.",
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
                    "Experimente os dois jogos e veja qual ajuda mais na revisão!",
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
            *_topic_text_genres(),
            *_topic_legal_texts(),
            *_topic_netiquette(),
            *_topic_verbal_phrase(),
            *_topic_verbs_moods(),
            *_topic_adverbs(),
            *_topic_humor(),
            *_topic_speech(),
        ],
    }


def _topic_text_genres() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Gêneros normativos e instrucionais"}, "topic_id": "text_genres"},
        {
            "type": "paragraph",
            "content": {
                "text": "Gênero textual agrupa textos com função e forma parecidas. "
                "Textos normativos estabelecem regras, proibições e punições — leis, regulamentos, estatutos. "
                "Textos instrucionais ensinam a fazer algo — receitas, manuais, regras de jogo, bulas.",
            },
            "topic_id": "text_genres",
            "sources": [_src("page-001.jpg"), _src("page-002.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Tipo", "Finalidade", "Exemplos"],
                "rows": [
                    ["Normativo", "Regular conduta", "Lei, código de trânsito, regulamento escolar"],
                    ["Instrucional", "Orientar procedimento", "Receita, tutorial, manual de montagem"],
                ],
            },
            "topic_id": "text_genres",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Dica:",
                "text": "Se o texto manda ou proíbe → normativo. Se ensina passo a passo → instrucional.",
            },
            "topic_id": "text_genres",
        },
    ]


def _topic_legal_texts() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "2. Estrutura de textos legais"}, "topic_id": "legal_texts"},
        {
            "type": "paragraph",
            "content": {
                "text": "A unidade básica de um texto legal é o artigo (Art.). Pode ter parágrafos (§), "
                "incisos (I, II, III) e alíneas (a, b, c). O caput é a parte principal do artigo, "
                "antes das subdivisões.",
            },
            "topic_id": "legal_texts",
            "sources": [_src("page-003.jpg"), _src("page-004.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Parte", "Símbolo", "Função"],
                "rows": [
                    ["Artigo", "Art.", "Unidade principal"],
                    ["Parágrafo", "§", "Complementa o artigo"],
                    ["Inciso", "I, II, III", "Detalha o caput"],
                    ["Alínea", "a), b)", "Subdivide inciso ou parágrafo"],
                ],
            },
            "topic_id": "legal_texts",
        },
    ]


def _topic_netiquette() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "3. Netiqueta"}, "topic_id": "netiquette"},
        {
            "type": "paragraph",
            "content": {
                "text": "Netiqueta = net + etiqueta. São regras de boa conduta na internet: não «gritar» "
                "escrevendo tudo em MAIÚSCULAS, ser claro, respeitar os outros, usar poucos emoticons "
                "e cuidar da ortografia. As regras usam muito o modo imperativo.",
            },
            "topic_id": "netiquette",
            "sources": [_src("page-004.jpg"), _src("page-005.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🔇", "title": "Sem gritos", "text": "Evite só MAIÚSCULAS"},
                    {"icon": "✍️", "title": "Clareza", "text": "Textos curtos e objetivos"},
                    {"icon": "🤝", "title": "Respeito", "text": "Trate os outros como quer ser tratado"},
                    {"icon": "😊", "title": "Emoticons", "text": "Poucos — ajudam o tom, mas com moderação"},
                ],
            },
            "topic_id": "netiquette",
        },
    ]


def _topic_verbal_phrase() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "4. Sintagma verbal"}, "topic_id": "verbal_phrase"},
        {
            "type": "paragraph",
            "content": {
                "text": "Sintagma verbal = predicado da oração, com verbo no centro. "
                "Ex.: «Produza textos de leitura fácil» — núcleo: produza; complemento: textos de leitura fácil. "
                "Sem sintagma verbal não há oração.",
            },
            "topic_id": "verbal_phrase",
            "sources": [_src("page-017.jpg"), _src("page-018.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Exemplo do caderno:",
                "text": "«Evite palavrões / expresse sempre as suas ideias de um modo claro.» "
                "Dois sintagmas verbais: evite e expresse.",
            },
            "topic_id": "verbal_phrase",
        },
    ]


def _topic_verbs_moods() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "5. Verbos: tempos, modos e formas nominais"}, "topic_id": "verbs_moods"},
        {
            "type": "paragraph",
            "content": {
                "text": "Verbos situam fatos no tempo (presente, passado, futuro) e expressam a atitude do falante "
                "pelo modo: indicativo (fato real), subjuntivo (dúvida/possibilidade), imperativo (ordem/conselho). "
                "Formas nominais: infinitivo (-ar, -er, -ir), gerúndio (-ndo), particípio (-do).",
            },
            "topic_id": "verbs_moods",
            "sources": [_src("page-019.jpg"), _src("page-022.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Modo", "Uso", "Exemplo"],
                "rows": [
                    ["Indicativo", "Fato certo", "O aluno fecha a porta."],
                    ["Subjuntivo", "Hipótese", "Talvez o aluno feche a porta."],
                    ["Imperativo", "Ordem/conselho", "Feche a porta."],
                ],
            },
            "topic_id": "verbs_moods",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "mal × mau:",
                "text": "mal = advérbio (oposto de bem): «Não fale mal de seus amigos». "
                "mau = adjetivo (oposto de bom): «Fuja de quem é mau indivíduo».",
            },
            "topic_id": "verbs_moods",
        },
    ]


def _topic_adverbs() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "6. Advérbios e locuções adverbiais"}, "topic_id": "adverbs"},
        {
            "type": "paragraph",
            "content": {
                "text": "Advérbios indicam circunstâncias: tempo (hoje, já), lugar (aqui, lá), modo (bem, calmamente), "
                "intensidade (muito), negação (não). Locuções adverbiais têm mais de uma palavra: "
                "de repente, à direita, com vontade, em breve.",
            },
            "topic_id": "adverbs",
            "sources": [_src("page-027.jpg"), _src("page-029.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Circunstância", "Advérbio", "Locução adverbial"],
                "rows": [
                    ["Tempo", "hoje, já", "de repente, em breve"],
                    ["Lugar", "aqui, lá", "à direita, em cima"],
                    ["Modo", "bem, mal", "com vontade, em silêncio"],
                ],
            },
            "topic_id": "adverbs",
        },
    ]


def _topic_humor() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "7. Narrativas de humor"}, "topic_id": "humor"},
        {
            "type": "paragraph",
            "content": {
                "text": "Textos de humor buscam provocar riso. Piada = história curta com final surpreendente. "
                "Anedota = fato curioso ou engraçado envolvendo pessoa conhecida. "
                "Recursos: expectativa e surpresa, exagero, nonsense, jogos de palavras, subentendido.",
            },
            "topic_id": "humor",
            "sources": [_src("page-039.jpg"), _src("page-040.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🎭", "title": "Expectativa", "text": "Prepara um final inesperado"},
                    {"icon": "📢", "title": "Exagero", "text": "Amplia situação ou personagem"},
                    {"icon": "🌀", "title": "Nonsense", "text": "Absurdo proposital — ex.: Chaplin comendo bota"},
                    {"icon": "🔤", "title": "Jogo de palavras", "text": "Duplo sentido — ex.: «dois dedinhos»"},
                ],
            },
            "topic_id": "humor",
        },
    ]


def _topic_speech() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "8. Discurso direto e indireto"}, "topic_id": "speech"},
        {
            "type": "paragraph",
            "content": {
                "text": "Discurso direto reproduz a fala exata — usa travessão ou aspas e verbos de elocução "
                "(perguntou, respondeu). Discurso indireto relata a fala pelo narrador — "
                "sem travessão, com «que» ou «se» e tempos ajustados.",
            },
            "topic_id": "speech",
            "sources": [_src("page-045.jpg"), _src("page-046.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Direto", "Indireto"],
                "rows": [
                    ["A velha pergunta: — Como é mesmo o seu nome?", "A velha perguntou como era mesmo o nome dele."],
                    ["Papai me perguntou: — Você fez a tarefa?", "Papai me perguntou se eu tinha feito a tarefa."],
                ],
            },
            "topic_id": "speech",
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
                    "text": "Revise cada bloco antes de ir aos exercícios e jogos.",
                },
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "1. Gêneros normativo e instrucional",
                    "body": "Normativo = regras/proibições (lei). Instrucional = passo a passo (receita, manual).",
                },
                "topic_id": "text_genres",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "2. Textos legais",
                    "body": "Art. → § → incisos (I, II) → alíneas (a, b). Caput = parte principal do artigo.",
                },
                "topic_id": "legal_texts",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "3. Netiqueta",
                    "body": "Regras de conduta online. Imperativo predominante. Sem MAIÚSCULAS em excesso.",
                },
                "topic_id": "netiquette",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "4. Sintagma verbal",
                    "body": "Predicado com verbo núcleo. Ex.: «Seja claro e objetivo» — núcleo: seja.",
                },
                "topic_id": "verbal_phrase",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "5. Modos verbais",
                    "body": "Indicativo (fato) · subjuntivo (dúvida) · imperativo (ordem). mal ≠ mau.",
                },
                "topic_id": "verbs_moods",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "6. Advérbios",
                    "body": "Circunstâncias de tempo, lugar, modo. Locuções: de repente, à direita.",
                },
                "topic_id": "adverbs",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "7. Humor",
                    "body": "Piada × anedota. Recursos: surpresa, exagero, nonsense, duplo sentido.",
                },
                "topic_id": "humor",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "8. Discurso direto/indireto",
                    "body": "Direto = fala literal com travessão. Indireto = narrador reporta com «que/se».",
                },
                "topic_id": "speech",
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "No discurso indireto, «perguntou: —» vira «perguntou se/que» — sem travessão. "
                    "Ajuste o tempo: «fez» → «tinha feito».",
                },
            },
        ],
    }


def _section_game_genre() -> dict:
    return {
        "id": "game_genre",
        "type": "study_game",
        "title": "Jogo: Gênero certo",
        "blocks": [
            {
                "type": "panel_intro",
                "content": {
                    "title": "Classifique o gênero!",
                    "text": "Clique em um trecho e depois na categoria certa: normativo ou instrucional. "
                    "Baseado nos Módulos 19 e 20 do caderno.",
                },
            },
            {
                "type": "study_game",
                "content": {
                    "mode": "sort_buckets",
                    "game_id": "genre_sort",
                    "instructions": "Selecione um trecho e clique na categoria correta.",
                    "buckets": [
                        {"id": "normativo", "label": "Normativo", "hint": "Regras, leis, proibições"},
                        {"id": "instrucional", "label": "Instrucional", "hint": "Receitas, manuais, tutoriais"},
                    ],
                    "sort_items": [
                        {"id": "g1", "text": "Art. 54 — capacete obrigatório para motociclistas", "answer": "normativo"},
                        {"id": "g2", "text": "Dobre o papel ao meio e deixe a parte dobrada para baixo", "answer": "instrucional"},
                        {"id": "g3", "text": "Evite enviar mensagens EXCLUSIVAMENTE EM MAIÚSCULAS", "answer": "normativo"},
                        {"id": "g4", "text": "Junte os materiais: papel A4, linha, lápis, tesoura", "answer": "instrucional"},
                        {"id": "g5", "text": "§ 2º — veículos maiores respondem pela segurança dos menores", "answer": "normativo"},
                        {"id": "g6", "text": "Fixe as asas grampeando o papel no ponto marcado", "answer": "instrucional"},
                        {"id": "g7", "text": "Respeite para ser respeitado — regra de netiqueta", "answer": "normativo"},
                        {"id": "g8", "text": "Coloque a linha através do furo e dê um nó firme", "answer": "instrucional"},
                    ],
                },
            },
        ],
    }


def _section_game_humor() -> dict:
    return {
        "id": "game_humor",
        "type": "study_game",
        "title": "Jogo: Detetive do humor",
        "blocks": [
            {
                "type": "panel_intro",
                "content": {
                    "title": "Qual recurso de humor?",
                    "text": "Clique em um exemplo e depois no recurso correto. "
                    "Conteúdo do Módulo 22 — narrativas de humor.",
                },
            },
            {
                "type": "study_game",
                "content": {
                    "mode": "match_pairs",
                    "game_id": "humor_match",
                    "instructions": "Selecione um exemplo à esquerda e o recurso de humor à direita.",
                    "left": [
                        {"id": "l1", "text": "Carlitos «almoça» a bota no filme"},
                        {"id": "l2", "text": "Antônio responde «filho de anta é... Antônio!»"},
                        {"id": "l3", "text": "Aninha pergunta «Quais deles, mãe?» sobre dedinhos"},
                        {"id": "l4", "text": "Alice e o Chapeleiro falam de relógio que mostra o dia"},
                        {"id": "l5", "text": "Formiga solitária agarra o pescoço do elefante"},
                        {"id": "l6", "text": "Placa «ESCOLA: DEVAGAR» — Felipe anda devagar"},
                    ],
                    "right": [
                        {"id": "r1", "text": "Nonsense (absurdo)"},
                        {"id": "r2", "text": "Expectativa e surpresa"},
                        {"id": "r3", "text": "Jogo de palavras / duplo sentido"},
                        {"id": "r4", "text": "Exagero"},
                        {"id": "r5", "text": "Subentendido"},
                        {"id": "r6", "text": "Interpretação errada de advérbio"},
                    ],
                    "answers": {
                        "l1": "r1",
                        "l2": "r2",
                        "l3": "r3",
                        "l4": "r1",
                        "l5": "r4",
                        "l6": "r6",
                    },
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
                "id": "pt-pe-001",
                "type": "multiple_choice",
                "topic": "text_genres",
                "question": "Qual alternativa descreve corretamente um texto normativo?",
                "options": [
                    "Ensina passo a passo como fazer uma pipa de papel",
                    "Estabelece regras, proibições ou punições para regular condutas",
                    "Conta uma história engraçada com final surpreendente",
                    "Relata viagem turística com advérbios de tempo",
                ],
                "correct_answer": 1,
                "explanation": "Normativo = regras e proibições (leis, regulamentos). Instrucional ensina procedimentos.",
                "difficulty": "basic",
                "source_assets": sa("page-001.jpg"),
                "section": "exercises",
            },
            {
                "id": "pt-pe-002",
                "type": "multiple_choice",
                "topic": "text_genres",
                "question": (
                    "Leia as afirmativas sobre gêneros textuais:\n"
                    "I. Receitas culinárias são textos instrucionais.\n"
                    "II. Bulas de remédio são textos normativos.\n"
                    "III. Regulamentos escolares podem ser normativos.\n"
                    "IV. Manuais de montagem são textos instrucionais.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, III e IV", "II e IV", "I e II", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, III e IV corretas. Bula orienta uso — é instrucional, não normativo (II errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-002.jpg"),
                "section": "exercises",
            },
            {
                "id": "pt-pe-003",
                "type": "multiple_choice",
                "topic": "legal_texts",
                "question": (
                    f"Leia o trecho do Código de Trânsito:\n\n{CTB_ART54}\n\n"
                    "O artigo estabelece autorização ou proibição para condutores de motos?"
                ),
                "options": [
                    "Autorização — usa «poderão circular»",
                    "Proibição — usa «só poderão» com condições obrigatórias",
                    "Narrativa humorística sem valor normativo",
                    "Instrução para montar capacete em casa",
                ],
                "correct_answer": 1,
                "explanation": "«Só poderão» + incisos I–III impõem condições — é norma/proibição se descumprida.",
                "difficulty": "basic",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "pt-pe-004",
                "type": "multiple_choice",
                "topic": "legal_texts",
                "question": (
                    f"Leia novamente:\n\n{CTB_ART54}\n\n"
                    "Leia as afirmativas:\n"
                    "I. Os incisos I, II e III detalham o caput do artigo.\n"
                    "II. Incisos usam numeração romana seguida de travessão.\n"
                    "III. O caput autoriza circular sem capacete.\n"
                    "IV. Artigo 54 trata de condutores de motocicletas.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "II, III e IV", "I, II e IV", "I e III"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. Caput exige condições — capacete é obrigatório (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "pt-pe-005",
                "type": "multiple_choice",
                "topic": "netiquette",
                "question": (
                    f"Leia o texto:\n\n{NETIQUETA_TEXT}\n\n"
                    "Por que escrever só em MAIÚSCULAS pode ofender o interlocutor?"
                ),
                "options": [
                    "Porque indica que o texto é uma lei federal",
                    "Porque lembra «gritar» na internet e causa irritação",
                    "Porque impede o uso de emoticons",
                    "Porque torna o texto instrucional em normativo",
                ],
                "correct_answer": 1,
                "explanation": "Regra 1 da netiqueta: maiúsculas em excesso = grito virtual.",
                "difficulty": "basic",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "pt-pe-006",
                "type": "multiple_choice",
                "topic": "netiquette",
                "question": (
                    f"Leia o texto:\n\n{NETIQUETA_TEXT}\n\n"
                    "Leia as afirmativas:\n"
                    "I. «Evite» e «Seja» estão no modo imperativo.\n"
                    "II. «Produza» forma sintagma verbal com núcleo «produza».\n"
                    "III. Netiqueta é neologismo de net + etiqueta.\n"
                    "IV. Regra 2 recomenda usar só MAIÚSCULAS para negrito.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, II e III", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e III corretas. Regra 2 indica sublinhar e negrito, não maiúsculas (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "pt-pe-007",
                "type": "multiple_choice",
                "topic": "verbal_phrase",
                "question": "Na regra «Produza textos de leitura fácil», qual é o núcleo do sintagma verbal?",
                "options": ["textos", "leitura", "produza", "fácil"],
                "correct_answer": 2,
                "explanation": "O núcleo do sintagma verbal é o verbo — «produza».",
                "difficulty": "basic",
                "source_assets": sa("page-017.jpg"),
                "section": "exercises",
            },
            {
                "id": "pt-pe-008",
                "type": "multiple_choice",
                "topic": "verbs_moods",
                "question": (
                    "Leia as afirmativas sobre modos verbais:\n"
                    "I. «Talvez o aluno feche a porta» está no subjuntivo.\n"
                    "II. «Feche a porta» está no imperativo.\n"
                    "III. Regras de netiqueta usam muito o imperativo.\n"
                    "IV. Indicativo apresenta fatos como reais.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "III e IV", "I, II e III", "I, II, III e IV"],
                "correct_answer": 3,
                "explanation": "Todas corretas — são definições do caderno sobre modos verbais.",
                "difficulty": "intermediate",
                "source_assets": sa("page-022.jpg"),
                "section": "exercises",
            },
            {
                "id": "pt-pe-009",
                "type": "multiple_choice",
                "topic": "verbs_moods",
                "question": "Complete: «Não fale ___ de seus amigos!» e «Fuja de quem é ___ indivíduo.»",
                "options": ["mal / mal", "mau / mau", "mal / mau", "mau / mal"],
                "correct_answer": 2,
                "explanation": "mal = advérbio (↔ bem); mau = adjetivo (↔ bom).",
                "difficulty": "basic",
                "source_assets": sa("page-034.jpg"),
                "section": "exercises",
            },
            {
                "id": "pt-pe-010",
                "type": "multiple_choice",
                "topic": "adverbs",
                "question": "«De repente, o garoto entrou na sala» — «de repente» é:",
                "options": [
                    "Advérbio simples de intensidade",
                    "Locução adverbial de tempo",
                    "Sintagma nominal sujeito",
                    "Verbo no gerúndio",
                ],
                "correct_answer": 1,
                "explanation": "Locução adverbial = expressão com função de advérbio. «De repente» = circunstância de tempo.",
                "difficulty": "basic",
                "source_assets": sa("page-029.jpg"),
                "section": "exercises",
            },
            {
                "id": "pt-pe-011",
                "type": "multiple_choice",
                "topic": "humor",
                "question": (
                    f"Leia o texto:\n\n{ANINHA_TEXT}\n\n"
                    "O humor da fala final de Aninha vem principalmente de:"
                ),
                "options": [
                    "Exagero físico do personagem",
                    "Duplo sentido de «dois dedinhos» (medida × dedos da mão)",
                    "Nonsense absurdo sem lógica",
                    "Discurso indireto mal pontuado",
                ],
                "correct_answer": 1,
                "explanation": "A mãe quis dizer «dois dedinhos» de medida; Aninha entendeu os dedos da mão — jogo de palavras.",
                "difficulty": "basic",
                "source_assets": sa("page-040.jpg"),
                "section": "exercises",
            },
            {
                "id": "pt-pe-012",
                "type": "multiple_choice",
                "topic": "humor",
                "question": (
                    f"Leia o texto:\n\n{ANINHA_TEXT}\n\n"
                    "Leia as afirmativas:\n"
                    "I. O texto de Mário Prata é uma crônica/anedota.\n"
                    "II. O autor cria expectativa antes da pergunta final.\n"
                    "III. «Quais deles, mãe?» usa recurso de duplo sentido.\n"
                    "IV. A cena é um exemplo de texto normativo.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "II e III", "I, II e III", "III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e III corretas. É narrativa de humor, não normativa (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-040.jpg"),
                "section": "exercises",
            },
            {
                "id": "pt-pe-013",
                "type": "multiple_choice",
                "topic": "speech",
                "question": (
                    f"Leia o trecho:\n\n{A_VOLTA_TEXT}\n\n"
                    "Como ficaria em discurso indireto a fala do vendedor?"
                ),
                "options": [
                    "O vendedor perguntou: — Você não tinha um cachorro?",
                    "O vendedor perguntou se ele não tinha um cachorro.",
                    "O vendedor afirmou que o Cusca morreu faz vinte anos.",
                    "O vendedor perguntou se o Cusca morreu faz vinte anos.",
                ],
                "correct_answer": 1,
                "explanation": "Indireto: sem travessão, verbo «perguntou se» + concordância. Resposta sobre Cusca é outra fala.",
                "difficulty": "basic",
                "source_assets": sa("page-038.jpg"),
                "section": "exercises",
            },
            {
                "id": "pt-pe-014",
                "type": "multiple_choice",
                "topic": "speech",
                "question": (
                    f"Leia o trecho:\n\n{A_VOLTA_TEXT}\n\n"
                    "Leia as afirmativas:\n"
                    "I. «Morreu, ih, faz vinte anos» está em discurso direto.\n"
                    "II. Veríssimo usa travessão para marcar falas na crônica.\n"
                    "III. No indireto, «morreu» poderia virar «havia morrido».\n"
                    "IV. Discurso direto perde vivacidade das falas.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "III e IV", "I, II e III", "II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e III corretas. Direto mantém vivacidade — por isso o autor o prefere (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-046.jpg"),
                "section": "exercises",
            },
            {
                "id": "pt-pe-015",
                "type": "multiple_choice",
                "topic": "humor",
                "question": (
                    "Leia a piada:\n"
                    "«O irmão e a irmã entraram machucados. A mãe perguntou o que aconteceu. "
                    "Zezé: — Lavei a louça. Lili: — Enxaguei! Lurdinha: — Varri os cacos!»\n\n"
                    "O humor vem de:"
                ),
                "options": [
                    "Exagero sobre elefantes e formigas",
                    "Subentendido — quebraram a louça ao lavar",
                    "Nonsense sem relação entre frases",
                    "Erro de concordância nominal",
                ],
                "correct_answer": 1,
                "explanation": "«Varri os cacos» revela implicitamente que a louça quebrou — subentendido.",
                "difficulty": "basic",
                "source_assets": sa("page-043.jpg"),
                "section": "exercises",
            },
            {
                "id": "pt-pe-016",
                "type": "multiple_choice",
                "topic": "adverbs",
                "question": (
                    "Leia a anedota:\n"
                    "«Felipe chegou atrasado. A mãe perguntou por quê. "
                    "Ele respondeu: — Por causa da placa da esquina: ESCOLA — DEVAGAR.»\n\n"
                    "Estão corretas apenas:\n"
                    "I. «DEVAGAR» é advérbio de modo na placa.\n"
                    "II. Felipe interpretou «devagar» como velocidade dele, não dos motoristas.\n"
                    "III. «Logo» e «lá» na história são advérbios.\n"
                    "IV. A graça vem do duplo sentido de «devagar»."
                ),
                "options": ["I e II", "II e IV", "I, II e IV", "I, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. «Logo» e «lá» não aparecem nesta anedota (III errada neste texto).",
                "difficulty": "intermediate",
                "source_assets": sa("page-031.jpg"),
                "section": "final_quiz",
            },
        ],
    }
