"""Conteúdo pedagógico da revisão Pedro — Português PE 3º trimestre (Módulos 35 e 38)."""

from __future__ import annotations

REVIEW_ID = "pedro-pe-portugues-3tri"
ASSET_PREFIX = "assets/pedro_pe_portugues_3_tri"

GUERRA_PLASTICO = (
    "Trecho da carta «Guerra ao plástico» (Eduardo Domingues, O Estado de S. Paulo, 26 jun. 2019):\n"
    "A respeito da matéria sobre banir canudos de plástico no Estado de São Paulo (Estadão, 26/6, A18), "
    "a guerra parece perdida, pois quase toda a embalagem de cozinha e limpeza é de plástico. "
    "Pensar que vão resolver este grave assunto com a proibição de canudinhos parece ser uma gota d'água "
    "no oceano — aliás, o maior prejudicado ao fim desta insensata cadeia da era do plástico."
)

DESROTULANDO = (
    "Trecho da carta «Desrotulando» (caderno, sobre alimentos ultraprocessados):\n"
    "Li a matéria sobre alimentos ultraprocessados e conheci o aplicativo Desrotulando, "
    "que analisa ingredientes pelo código de barras (nota de 0 a 100). "
    "Escolher o que se come é fundamental para a qualidade de vida. "
    "Recomendo usar o app e preferir alimentos mais naturais."
)

MERGULHO_MARIANA = (
    "Trecho da notícia «Mergulho mais profundo da história encontra saco plástico» (caderno):\n"
    "O ex-oficial da marinha Victor Vescovo bateu o recorde de mergulho mais profundo, "
    "alcançando 10.927 metros na Fossa das Marianas. A expedição «As cinco profundezas» "
    "registrou quatro espécies novas, mas também lixo humano — sacos plásticos e embalagens."
)

ACAI_TIJOLO = (
    "Trecho da notícia «Paraense de 18 anos tem prêmios por criar tijolo de caroço de açaí» (caderno):\n"
    "Francielly Rodrigues Barbosa, de Moju (PA), desenvolveu tijolos com caroço de açaí carbonizado "
    "e misturado a argila. Aproximadamente 90% do açaí consumido no mundo é produzido no Pará, "
    "mas apenas 4% do fruto é aproveitado. Para criar o tijolo, ela convidou jovens de Moju para ajudá-la."
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
        "title": "Revisão de Português — PE 3º Trimestre",
        "subtitle": "Pedro · 6º ano · Módulos 35 e 38",
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
            {"order": 3, "title": "Jogo: Notícia objetiva", "section_id": "game_objectivity"},
            {"order": 4, "title": "Jogo: Citação certa", "section_id": "game_citation"},
            {"order": 5, "title": "Exercícios", "section_id": "exercises"},
        ],
        "sections": [
            _section_route(),
            _section_explain(),
            _section_summary(),
            _section_game_objectivity(),
            _section_game_citation(),
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
                    "text": "Linguagem jornalística (título, subtítulo, efeito de verdade, objetividade, verbos), "
                    "vírgula com adjunto adverbial e expressões explicativas, acentuação de paroxítonas, "
                    "notações bibliográficas e carta do leitor — Módulos 35 e 38. Reserve cerca de 60 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "📰", "title": "Título", "text": "Conciso · presente · sem ponto final"},
                        {"icon": "🔍", "title": "Efeito de verdade", "text": "Números · nomes · datas · locais"},
                        {"icon": "⚖️", "title": "Objetividade", "text": "3ª pessoa · sem opinião pessoal"},
                        {"icon": "⏱️", "title": "Verbos", "text": "Presente · pretérito · futuro"},
                        {"icon": "✉️", "title": "Carta do leitor", "text": "Opinião · marcas · referência à matéria"},
                        {"icon": "📌", "title": "Vírgula", "text": "Adjunto adverbial · aliás, isto é"},
                        {"icon": "✏️", "title": "Paroxítonas", "text": "Terminadas em -l, -r, -ps, -i(s)"},
                        {"icon": "📚", "title": "Bibliografia", "text": "Livro · jornal · site"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 35 — Linguagem jornalística: marcas linguísticas",
                        "Módulo 38 — Carta do leitor: marcas linguísticas",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão.",
                            "tip": "Compare notícia (objetiva) com carta do leitor (opinião).",
                        },
                        {
                            "title": "Revise o Resumo rápido",
                            "panel": "summary",
                            "panel_label": "Resumo rápido",
                            "description": "Percorra os blocos-síntese antes da PE.",
                        },
                        {
                            "title": "Jogue: Notícia objetiva",
                            "panel": "game_objectivity",
                            "panel_label": "Jogo: Notícia objetiva",
                            "description": "Classifique trechos objetivos ou subjetivos.",
                        },
                        {
                            "title": "Jogue: Citação certa",
                            "panel": "game_citation",
                            "panel_label": "Jogo: Citação certa",
                            "description": "Associe elemento da citação ao tipo de fonte.",
                        },
                        {
                            "title": "Faça os Exercícios",
                            "panel": "exercises",
                            "panel_label": "Exercícios",
                            "description": "Questões com textos transcritos do caderno.",
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
                    "Use os jogos para fixar objetividade jornalística e formato de citações.",
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
            *_topic_journalistic_titles(),
            *_topic_journalistic_marks(),
            *_topic_truth_effect(),
            *_topic_journalistic_verbs(),
            *_topic_adverbial_comma(),
            *_topic_paroxytones(),
            *_topic_bibliography(),
            *_topic_reader_letter(),
        ],
    }


def _topic_journalistic_titles() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "1. Título e subtítulo jornalísticos"},
            "topic_id": "journalistic_titles",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "O título é o primeiro contato do leitor: anuncia o assunto e deve ser conciso "
                "(só artigos, adjetivos e advérbios realmente necessários). "
                "Em geral usa presente do indicativo — dá sensação de fato recente. "
                "Não leva ponto final (nem subtítulo nem intertítulo). "
                "O subtítulo amplia: traz fonte, detalhe ou dado que o título não coube.",
            },
            "topic_id": "journalistic_titles",
            "sources": [_src("page-020.jpg"), _src("page-018.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Elemento", "Função", "Exemplo do caderno"],
                "rows": [
                    ["Título", "Essencial + atrativo", "4º maior produtor de lixo plástico…"],
                    ["Subtítulo", "Complementa", "Relatório WWF aponta 1% reciclado…"],
                    ["Verbo no título", "Presente", "NASCE o terceiro filhote… / DÁ À LUZ…"],
                ],
            },
            "topic_id": "journalistic_titles",
        },
    ]


def _topic_journalistic_marks() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "2. Marcas da linguagem jornalística"},
            "topic_id": "journalistic_marks",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Texto informativo busca objetividade e impessoalidade: terceira pessoa, "
                "sem palavras que revelem impressão ou opinião («suposto» antes de julgamento). "
                "Concisão = dizer em uma linha o que caberia em duas. "
                "Clareza = pontuação correta e frases sem ambiguidade. "
                "Veículos diferentes podem titular o mesmo fato (WWF e plástico) com ênfases distintas.",
            },
            "topic_id": "journalistic_marks",
            "sources": [_src("page-019.jpg"), _src("page-021.jpg"), _src("page-014.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "👤", "title": "Impersonal", "text": "Evita «eu acho» no corpo da notícia"},
                    {"icon": "📏", "title": "Conciso", "text": "Sem palavras de sobra no título"},
                    {"icon": "🎯", "title": "Preciso", "text": "Dados e nomes verificáveis"},
                    {"icon": "🚫", "title": "Evitar", "text": "«vilão», «absurdo» sem fonte"},
                ],
            },
            "topic_id": "journalistic_marks",
        },
    ]


def _topic_truth_effect() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "3. Efeito de verdade na notícia"},
            "topic_id": "truth_effect",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "O redator usa recursos que aumentam a credibilidade: números exatos (32°C, 10.927 m), "
                "marcadores de lugar (Anchorage, Fossa das Marianas), de tempo (26 jun. 2019), "
                "nomes de pessoas e instituições reais (Victor Vescovo, WWF, Nature), "
                "depoimentos e opiniões de especialistas entre aspas.",
            },
            "topic_id": "truth_effect",
            "sources": [_src("page-017.jpg"), _src("page-015.jpg"), _src("page-011.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Sinônimos no texto:",
                "text": "Para não repetir «Victor Vescovo», o redator usa «ex-oficial», «ele», «marinheiro» — "
                "coesão sem monotonia.",
            },
            "topic_id": "truth_effect",
        },
    ]


def _topic_journalistic_verbs() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "4. Tempos verbais no jornalismo"},
            "topic_id": "journalistic_verbs",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Predomina o indicativo. Presente: fato recente, descrição que ainda vale "
                "(«90% do açaí é produzido no Pará»). Pretérito: fatos já ocorridos "
                "(«ela convidou jovens», «foi dado um passo»). Futuro: ação que ainda vai acontecer "
                "(«Periquito Cara-Suja será reintroduzido»). "
                "Entrevistas citadas na notícia podem aparecer no presente («explica», «conta») "
                "para dar sensação de atualidade.",
            },
            "topic_id": "journalistic_verbs",
            "sources": [_src("page-021.jpg"), _src("page-016.jpg"), _src("page-009.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Tempo", "Uso", "Exemplo"],
                "rows": [
                    ["Presente", "Título / fato atual", "Nobel da Paz vai para…"],
                    ["Pretérito", "Fato passado", "Victor Vescovo bateu o recorde"],
                    ["Futuro", "Ainda por vir", "será reintroduzido na Serra"],
                ],
            },
            "topic_id": "journalistic_verbs",
        },
    ]


def _topic_adverbial_comma() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "5. Vírgula: adjunto adverbial e expressões explicativas"},
            "topic_id": "adverbial_comma",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Adjunto adverbial deslocado do final pede vírgula: "
                "«No ano passado, a produção de plástico aumentou» ou "
                "«A produção, no ano passado, aumentou». "
                "Adjunto de um só termo no início: vírgula opcional. "
                "Expressões explicativas ou retificadoras (aliás, isto é, ou seja, por exemplo) "
                "vêm isoladas por vírgulas: «…got a d'água no oceano — aliás, o maior prejudicado…».",
            },
            "topic_id": "adverbial_comma",
            "sources": [_src("page-013.jpg"), _src("page-008.jpg"), _src("page-003.jpg")],
        },
    ]


def _topic_paroxytones() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "6. Acentuação: paroxítonas"},
            "topic_id": "paroxytones",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Paroxítonas terminadas em -l, -r, -ps, -i ou -is levam acento gráfico: "
                "fácil, repórter, bíceps, tênis. "
                "No plural de palavras em -l, troca-se por -eis e mantém-se o acento: "
                "fáceis, amáveis, têxteis — forma-se ditongo oral (a-má-veis). "
                "Oxítonas como revolver (ferramenta) não acentuam; revólver (arma) é paroxítona em -r.",
            },
            "topic_id": "paroxytones",
            "sources": [_src("page-010.jpg"), _src("page-002.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🔤", "title": "-l / -eis", "text": "imóvel → imóveis"},
                    {"icon": "🔤", "title": "-r", "text": "repórter · cadáver"},
                    {"icon": "🔤", "title": "-ps", "text": "bíceps · tríceps"},
                    {"icon": "🎵", "title": "Ditongo", "text": "Duas vogais na mesma sílaba"},
                ],
            },
            "topic_id": "paroxytones",
        },
    ]


def _topic_bibliography() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "7. Notações bibliográficas"},
            "topic_id": "bibliography",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Ao citar fontes, siga ordem: SOBRENOME, Nome. Título do texto. "
                "Título da publicação (jornal/revista/site). Local, data, seção/páginas. "
                "Livro: SOBRENOME, Nome. Título. Cidade: Editora, ano. p. X-Y. "
                "Site: incluir «Disponível em:» URL e «Acesso em:» data.",
            },
            "topic_id": "bibliography",
            "sources": [_src("page-012.jpg"), _src("page-013.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Tipo", "Elemento extra"],
                "rows": [
                    ["Livro", "Cidade: Editora, ano"],
                    ["Jornal", "Seção e página (ex.: Metrópole, A21)"],
                    ["Eletrônico", "URL + data de acesso"],
                ],
            },
            "topic_id": "bibliography",
        },
    ]


def _topic_reader_letter() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "8. Carta do leitor"},
            "topic_id": "reader_letter",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Carta do leitor expressa opinião sobre matéria publicada. "
                "Marcas: referência ao veículo e à matéria («A respeito de…», «Estadão, 26/6»), "
                "posicionamento («não concordo», «penso que», «na minha opinião»), "
                "argumentos e metáforas («guerra ao plástico», «got a d'água no oceano»). "
                "Diferente da notícia: há voz do leitor e julgamento de valor.",
            },
            "topic_id": "reader_letter",
            "sources": [_src("page-006.jpg"), _src("page-004.jpg"), _src("page-005.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Metáfora:",
                "text": "«As recentes vilãs» para sacolas plásticas — comparação por semelhança, "
                "reforça opinião negativa sobre o plástico.",
            },
            "topic_id": "reader_letter",
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
                    "text": "Revise cada bloco antes dos exercícios. "
                    "Cartas e notícias do caderno aparecem transcritas nas questões.",
                },
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "1. Título e subtítulo",
                    "body": "Conciso · presente · sem ponto · subtítulo complementa.",
                },
                "topic_id": "journalistic_titles",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "2. Marcas jornalísticas",
                    "body": "Objetivo · impessoal · conciso · claro.",
                },
                "topic_id": "journalistic_marks",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "3. Efeito de verdade",
                    "body": "Números · locais · datas · nomes · citações.",
                },
                "topic_id": "truth_effect",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "4. Verbos",
                    "body": "Presente (atual) · pretérito (passado) · futuro (virá).",
                },
                "topic_id": "journalistic_verbs",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "5. Vírgula",
                    "body": "Adjunto deslocado · aliás, isto é, ou seja.",
                },
                "topic_id": "adverbial_comma",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "6. Paroxítonas",
                    "body": "-l, -r, -ps, -i(s) · plural em -eis.",
                },
                "topic_id": "paroxytones",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "7. Bibliografia",
                    "body": "Sobrenome maiúsculo · título da matéria · fonte completa.",
                },
                "topic_id": "bibliography",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "8. Carta do leitor",
                    "body": "Opinião · referência à matéria · marcas argumentativas.",
                },
                "topic_id": "reader_letter",
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "Notícia ≠ carta: jornalismo informativo evita opinião; carta do leitor defende posição. "
                    "Título jornalístico não leva ponto final — mas carta pode usar pontuação normal no corpo.",
                },
            },
        ],
    }


def _section_game_objectivity() -> dict:
    return {
        "id": "game_objectivity",
        "type": "study_game",
        "title": "Jogo: Notícia objetiva",
        "blocks": [
            {
                "type": "panel_intro",
                "content": {
                    "title": "Objetivo ou subjetivo?",
                    "text": "Classifique trechos no estilo do caderno (Módulo 35).",
                },
            },
            {
                "type": "study_game",
                "content": {
                    "mode": "sort_buckets",
                    "game_id": "objectivity_sort",
                    "instructions": "Clique no trecho e depois na categoria.",
                    "buckets": [
                        {"id": "obj", "label": "Objetivo", "hint": "Dado verificável, sem opinião"},
                        {"id": "subj", "label": "Subjetivo", "hint": "Impressão ou julgamento pessoal"},
                    ],
                    "sort_items": [
                        {"id": "t1", "text": "O Brasil produz 11 milhões de toneladas de lixo plástico por ano.", "answer": "obj"},
                        {"id": "t2", "text": "Só não ficamos tão feios na fita porque os EUA existem.", "answer": "subj"},
                        {"id": "t3", "text": "Victor Vescovo alcançou 10.927 metros de profundidade.", "answer": "obj"},
                        {"id": "t4", "text": "A guerra ao plástico parece perdida.", "answer": "subj"},
                        {"id": "t5", "text": "Apenas 1,2% do plástico brasileiro é reciclado.", "answer": "obj"},
                        {"id": "t6", "text": "Quantidade absurda de embalagens.", "answer": "subj"},
                    ],
                },
            },
        ],
    }


def _section_game_citation() -> dict:
    return {
        "id": "game_citation",
        "type": "study_game",
        "title": "Jogo: Citação certa",
        "blocks": [
            {
                "type": "panel_intro",
                "content": {
                    "title": "Onde entra cada parte?",
                    "text": "Associe o elemento à fonte bibliográfica correta.",
                },
            },
            {
                "type": "study_game",
                "content": {
                    "mode": "match_pairs",
                    "game_id": "citation_match",
                    "instructions": "Selecione o elemento e o tipo de fonte.",
                    "left": [
                        {"id": "l1", "text": "São Paulo: Martins Fontes, 2001"},
                        {"id": "l2", "text": "Metrópole, p. A21"},
                        {"id": "l3", "text": "Disponível em: www… Acesso em:"},
                        {"id": "l4", "text": "SOBRENOME em maiúsculas no autor"},
                    ],
                    "right": [
                        {"id": "r1", "text": "Livro"},
                        {"id": "r2", "text": "Jornal impresso"},
                        {"id": "r3", "text": "Documento eletrônico"},
                        {"id": "r4", "text": "Todos os tipos (autor)"},
                    ],
                    "answers": {"l1": "r1", "l2": "r2", "l3": "r3", "l4": "r4"},
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
                "id": "pp3-pe-001",
                "type": "multiple_choice",
                "topic": "journalistic_titles",
                "question": (
                    "Leia as afirmativas sobre títulos de notícias (caderno, Módulo 35):\n"
                    "I. Devem ser concisos e trazer a informação essencial.\n"
                    "II. Em geral usam presente do indicativo.\n"
                    "III. Terminam com ponto final, como frase comum.\n"
                    "IV. Podem ser mais atrativos quando trazem dado relevante extra.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e IV", "II e III", "I, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Título jornalístico não leva ponto final (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-020.jpg"),
                "section": "exercises",
            },
            {
                "id": "pp3-pe-002",
                "type": "multiple_choice",
                "topic": "journalistic_titles",
                "question": (
                    "Sobre os três títulos sobre o nascimento do gorila Imbi, o caderno pergunta qual é o mais conciso. "
                    "Qual alternativa corresponde à resposta esperada?"
                ),
                "options": [
                    "Título II — traz nome da gorila e recorde latino-americano",
                    "Título I — «Nasce o terceiro filhote…»",
                    "Título III — destaca extinção",
                    "Nenhum — todos têm o mesmo tamanho",
                ],
                "correct_answer": 1,
                "explanation": "Título I é o mais curto e ainda comunica o fato central.",
                "difficulty": "basic",
                "source_assets": sa("page-018.jpg"),
                "section": "exercises",
            },
            {
                "id": "pp3-pe-003",
                "type": "multiple_choice",
                "topic": "truth_effect",
                "question": (
                    f"Leia o trecho:\n\n{MERGULHO_MARIANA}\n\n"
                    "Qual recurso do texto contribui para o efeito de verdade?"
                ),
                "options": [
                    "Uso de metáfora «guerra ao plástico»",
                    "Medida exata de profundidade (10.927 m) e nome do mergulhador",
                    "Opinião «a guerra parece perdida»",
                    "Ausência total de datas",
                ],
                "correct_answer": 1,
                "explanation": "Números precisos e nomes reais aumentam credibilidade jornalística.",
                "difficulty": "basic",
                "source_assets": sa("page-015.jpg"),
                "section": "exercises",
            },
            {
                "id": "pp3-pe-004",
                "type": "multiple_choice",
                "topic": "truth_effect",
                "question": (
                    "Leia as afirmativas sobre efeito de verdade:\n"
                    "I. Números e datas concretas ajudam a credibilidade.\n"
                    "II. Nomes de instituições reais (WWF, Nature) reforçam o texto.\n"
                    "III. Metáforas substituem sempre os dados no jornalismo.\n"
                    "IV. Depoimentos entre aspas podem ser usados.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e IV", "II e IV", "I, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Metáfora aparece mais em opinião/carta (III errada para notícia objetiva).",
                "difficulty": "intermediate",
                "source_assets": sa("page-017.jpg"),
                "section": "exercises",
            },
            {
                "id": "pp3-pe-005",
                "type": "multiple_choice",
                "topic": "journalistic_marks",
                "question": (
                    "Para tornar subjetivo um trecho sobre reciclagem, o caderno troca «circulem» por «gritem» "
                    "e «enorme quantidade» por «quantidade absurda». O que isso ensina?"
                ),
                "options": [
                    "Jornalismo deve usar sempre gírias",
                    "Palavras de julgamento pessoal afetam a objetividade",
                    "Números não importam em notícias",
                    "Subtítulo deve repetir o título",
                ],
                "correct_answer": 1,
                "explanation": "Termos como «absurda» revelam opinião — jornalismo informativo evita isso.",
                "difficulty": "basic",
                "source_assets": sa("page-014.jpg"),
                "section": "exercises",
            },
            {
                "id": "pp3-pe-006",
                "type": "multiple_choice",
                "topic": "journalistic_verbs",
                "question": (
                    f"Leia o trecho:\n\n{ACAI_TIJOLO}\n\n"
                    "Por que «é produzido» está no presente e «convidou» no pretérito?"
                ),
                "options": [
                    "Erro de redação — deveriam estar no mesmo tempo",
                    "Presente para dado ainda válido; pretérito para ação já feita na reportagem",
                    "Pretérito indica futuro",
                    "Presente só pode aparecer no título",
                ],
                "correct_answer": 1,
                "explanation": "Estatística atual = presente · passos do projeto = pretérito.",
                "difficulty": "basic",
                "source_assets": sa("page-016.jpg"),
                "section": "exercises",
            },
            {
                "id": "pp3-pe-007",
                "type": "multiple_choice",
                "topic": "journalistic_verbs",
                "question": (
                    "Leia as afirmativas sobre verbos no jornalismo:\n"
                    "I. Título «Nobel da Paz vai para…» usa presente.\n"
                    "II. Futuro «será reintroduzido» indica fato ainda por ocorrer.\n"
                    "III. Citações podem aparecer no presente para sensação de atualidade.\n"
                    "IV. Notícia informativa usa predominantemente subjuntivo.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, II e III", "II e IV", "III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Indicativo predomina (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-009.jpg"),
                "section": "exercises",
            },
            {
                "id": "pp3-pe-008",
                "type": "multiple_choice",
                "topic": "adverbial_comma",
                "question": (
                    "Na carta «Guerra ao plástico», a palavra «aliás» isola uma explicação sobre "
                    "«insensata cadeia da era do plástico». Qual regra justifica a vírgula?"
                ),
                "options": [
                    "Vírgula separa sujeito de predicado",
                    "Vírgula isola expressão explicativa ou retificadora",
                    "Vírgula indica discurso direto",
                    "Nunca se usa vírgula antes de «aliás»",
                ],
                "correct_answer": 1,
                "explanation": "«Aliás, isto é, ou seja» entram isolados por vírgulas.",
                "difficulty": "basic",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "pp3-pe-009",
                "type": "multiple_choice",
                "topic": "adverbial_comma",
                "question": (
                    "Leia as afirmativas sobre adjunto adverbial:\n"
                    "I. Deslocado para o início, costuma vir seguido de vírgula.\n"
                    "II. «Brasil tentou, por duas vezes, transformar Paraty…» — vírgulas marcam o adjunto no meio.\n"
                    "III. Adjunto de um termo no início nunca leva vírgula.\n"
                    "IV. Inverter ordem pode mudar o destaque da informação.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "I, II e IV", "II e III", "I, II e III"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Com um termo no início a vírgula pode ser opcional (III absoluta errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-008.jpg"),
                "section": "exercises",
            },
            {
                "id": "pp3-pe-010",
                "type": "multiple_choice",
                "topic": "paroxytones",
                "question": "Qual alternativa está corretamente acentuada no plural?",
                "options": ["faceis", "fáceis", "facéis", "fáceís"],
                "correct_answer": 1,
                "explanation": "fácil → fáceis (paroxítona em -eis, ditongo oral).",
                "difficulty": "basic",
                "source_assets": sa("page-002.jpg"),
                "section": "exercises",
            },
            {
                "id": "pp3-pe-011",
                "type": "multiple_choice",
                "topic": "paroxytones",
                "question": (
                    "Leia as afirmativas:\n"
                    "I. Paroxítonas terminadas em -r levam acento (repórter).\n"
                    "II. revolver (ferramenta) e revólver (arma) têm sílabas tônicas diferentes.\n"
                    "III. bíceps, tríceps são paroxítonas terminadas em -ps.\n"
                    "IV. automóvel no plural vira automoveis sem acento.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e III", "II e IV", "I e III"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Plural: automóveis, com acento (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-010.jpg"),
                "section": "exercises",
            },
            {
                "id": "pp3-pe-012",
                "type": "multiple_choice",
                "topic": "bibliography",
                "question": (
                    "Na citação de livro do caderno (Gombrich), qual sequência está correta após o nome do autor?"
                ),
                "options": [
                    "Título. Cidade: Editora, ano. p. páginas",
                    "Editora, ano, título",
                    "URL, data de acesso, título",
                    "Seção Metrópole, p. A21",
                ],
                "correct_answer": 0,
                "explanation": "Livro: Título. Cidade: Editora, ano. p. X-Y.",
                "difficulty": "basic",
                "source_assets": sa("page-012.jpg"),
                "section": "exercises",
            },
            {
                "id": "pp3-pe-013",
                "type": "multiple_choice",
                "topic": "bibliography",
                "question": (
                    "Leia as afirmativas sobre citações:\n"
                    "I. Jornal: pode incluir seção e página (Metrópole, A21).\n"
                    "II. Site: «Disponível em» e «Acesso em».\n"
                    "III. Sobrenome do autor em maiúsculas é padrão.\n"
                    "IV. Revista digital não precisa de data.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, II e III", "II e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Data importa também em revistas (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-013.jpg"),
                "section": "exercises",
            },
            {
                "id": "pp3-pe-014",
                "type": "multiple_choice",
                "topic": "reader_letter",
                "question": (
                    f"Leia o trecho:\n\n{GUERRA_PLASTICO}\n\n"
                    "Qual expressão funciona como metáfora ligada ao plástico?"
                ),
                "options": [
                    "Estado de São Paulo",
                    "got a d'água no oceano",
                    "26/6, A18",
                    "canudinhos de plástico (referência literal)",
                ],
                "correct_answer": 1,
                "explanation": "«Gota d'água no oceano» = esforço pequeno diante do problema enorme.",
                "difficulty": "basic",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "pp3-pe-015",
                "type": "multiple_choice",
                "topic": "reader_letter",
                "question": (
                    f"Leia o trecho:\n\n{DESROTULANDO}\n\n"
                    "Qual é o objetivo principal da autora da carta?"
                ),
                "options": [
                    "Criticar o jornal por publicar a matéria",
                    "Informar sobre o app Desrotulando e conscientizar sobre alimentação",
                    "Pedir proibição de ultraprocessados por lei",
                    "Contar uma crônica de humor",
                ],
                "correct_answer": 1,
                "explanation": "Ela recomenda o app e defende escolhas alimentares conscientes.",
                "difficulty": "basic",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "pp3-pe-016",
                "type": "multiple_choice",
                "topic": "reader_letter",
                "question": (
                    f"Leia o trecho:\n\n{GUERRA_PLASTICO}\n\n"
                    "Leia as afirmativas:\n"
                    "I. O leitor contextualiza a matéria citando jornal, data e página.\n"
                    "II. «A guerra parece perdida» expressa posicionamento.\n"
                    "III. Carta do leitor deve ser totalmente impessoal como notícia.\n"
                    "IV. Trocar «parece» por «está» torna a afirmação mais certa.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e IV", "II e III", "I, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Carta admite opinião (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-006.jpg"),
                "section": "final_quiz",
            },
        ],
    }
