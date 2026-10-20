"""Conteúdo pedagógico da revisão Benjamin — Português PE 2º trimestre."""

from __future__ import annotations

REVIEW_ID = "benjamin-pe-portugues-2tri"
ASSET_PREFIX = "assets/benjamin_pe_portugues_2_tri"

# Textos transcritos da apostila (base para exercícios de interpretação)
JOCA_TEXT = (
    "Trecho do Jornal Joca («Brincar e jogar colabora para o desenvolvimento do seu filho»):\n"
    "A brincadeira é uma necessidade do ser humano em qualquer idade, porém na infância deve ser vista "
    "não apenas como diversão, mas também como uma possibilidade de desenvolver as potencialidades da criança. "
    "É uma forma de interagir com o mundo e descobri-lo, de construir valores e experimentar sensações."
)

JOCA_EXTENDED = (
    "Trecho ampliado da matéria do Jornal Joca:\n"
    "Tanto o brinquedo quanto o jogo e a brincadeira são fundamentais e importantes para o crescimento das crianças. "
    "O brincar e o jogar são formas de expressão e comunicação que os seres humanos possuem desde o nascimento.\n"
    "Com a tecnologia moderna, muitos aspectos importantes para o desenvolvimento global da criança vêm se perdendo. "
    "Assim, há que se resgatar as brincadeiras e os jogos de outros tempos, permitir que as crianças brinquem mais livremente, "
    "utilizar materiais reciclados.\n"
    "Um bom começo é o diálogo entre pais e filhos, avós e netos, para que possam conhecer e trocar informações "
    "sobre os jogos e as brincadeiras tradicionais, bem como os atuais."
)

BRINQUEDO_ARTICLE = (
    "Trecho do artigo enciclopédico «brinquedo» (Britannica Escola):\n"
    "Crianças de todas as partes do mundo gostam de brinquedos. Um brinquedo pode ser uma simples bola, "
    "um jogo de tabuleiro ou uma máquina cara que utiliza a mais alta tecnologia. "
    "Os brinquedos podem distrair, educar, estimular a criatividade e ajudar no desenvolvimento infantil. "
    "Anos atrás, a maioria dos brinquedos era feita de madeira e de tecido. Hoje, o material mais comum é o plástico.\n"
    "Os brinquedos fazem parte da história do ser humano. Os arqueólogos muitas vezes encontram sinais de brinquedos "
    "nas ruínas que escavam: bolas, bonecas, vagões de trem e barcos de brinquedo."
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
        "subtitle": "Benjamin · 4º ano · Módulos 5 e 6",
        "language": "pt-BR",
        "discipline": "Língua Portuguesa",
        "grade": "4º ano",
        "metadata": {
            "student_name": "Benjamin",
            "exam_type": "Prova Específica (PE)",
            "estimated_duration_minutes": 55,
        },
        "study_route": [
            {"order": 1, "title": "Explicações", "section_id": "explain"},
            {"order": 2, "title": "Resumo rápido", "section_id": "summary"},
            {"order": 3, "title": "Jogo: Brincadeira certa", "section_id": "game_brincadeira"},
            {"order": 4, "title": "Jogo: Detetive do sufixo", "section_id": "game_sufixo"},
            {"order": 5, "title": "Exercícios", "section_id": "exercises"},
        ],
        "sections": [
            _section_route(),
            _section_explain(),
            _section_summary(),
            _section_game_brincadeira(),
            _section_game_sufixo(),
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
                    "text": "Infográficos e textos sobre brincadeiras, sufixos derivacionais, nasalidade, "
                    "pesquisa escolar, verbetes de dicionário e artigos enciclopédicos — tudo do 2º trimestre. "
                    "Reserve cerca de 55 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "📊", "title": "Infográfico", "text": "Texto + imagens · importância de brincar"},
                        {"icon": "📰", "title": "Texto Joca", "text": "Notícia informativa · potencialidades"},
                        {"icon": "🎨", "title": "Recursos visuais", "text": "Cores · setas · ilustrações"},
                        {"icon": "🔤", "title": "Sufixos", "text": "-agem · -esa/-ês · -eza/-ez"},
                        {"icon": "👃", "title": "Nasalidade", "text": "Til · m · n"},
                        {"icon": "🔍", "title": "Pesquisa", "text": "Fontes · citação · infográfico escolar"},
                        {"icon": "📖", "title": "Dicionário", "text": "Verbete · entrada · sílaba tônica"},
                        {"icon": "🌍", "title": "Enciclopédia", "text": "Artigo · brinquedo · verbete de animal"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 5 — Infográfico do brincar e sufixos",
                        "Módulo 5 — Ortografia e pesquisa escolar",
                        "Módulo 6 — Verbetes e enciclopédia",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Leia os cards e tabelas.",
                            "tip": "Compare texto verbal puro com infográfico.",
                        },
                        {
                            "title": "Revise o Resumo rápido",
                            "panel": "summary",
                            "panel_label": "Resumo rápido",
                            "description": "Percorra os blocos-síntese antes da PE.",
                        },
                        {
                            "title": "Jogue: Brincadeira certa",
                            "panel": "game_brincadeira",
                            "panel_label": "Jogo: Brincadeira certa",
                            "description": "Classifique brincadeiras pelo benefício que desenvolvem.",
                            "tip": "Xadrez = cognitivo · pular corda = motor.",
                        },
                        {
                            "title": "Jogue: Detetive do sufixo",
                            "panel": "game_sufixo",
                            "panel_label": "Jogo: Detetive do sufixo",
                            "description": "Associe palavra primitiva ao sufixo correto.",
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
            *_topic_infographic(),
            *_topic_joca(),
            *_topic_visual(),
            *_topic_suffixes(),
            *_topic_nasal(),
            *_topic_research(),
            *_topic_dictionary(),
            *_topic_encyclopedia(),
        ],
    }


def _topic_infographic() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Infográfico e importância de brincar"}, "topic_id": "infographic"},
        {
            "type": "paragraph",
            "content": {
                "text": "Infográfico = texto informativo + recursos gráfico-visuais (ilustrações, cores, setas, números). "
                "O caderno apresenta «A IMPORTÂNCIA DO BRINCAR» com 12 benefícios: fortalece funções cognitivas, "
                "desenvolve coordenação motora, estabelece vínculos afetivos, favorece cooperação, entre outros. "
                "Brincar não é só diversão — é aprendizagem.",
            },
            "topic_id": "infographic",
            "sources": [_src("page-001.jpg"), _src("page-004.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🧠", "title": "Cognitivo", "text": "Memória · atenção · raciocínio"},
                    {"icon": "🤸", "title": "Motor", "text": "Correr · pular · pedalar"},
                    {"icon": "❤️", "title": "Afetivo", "text": "Vínculos · empatia · colo"},
                    {"icon": "🤝", "title": "Social", "text": "Cooperação · autonomia · cidadania"},
                ],
            },
            "topic_id": "infographic",
        },
    ]


def _topic_joca() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "2. Texto informativo — Jornal Joca"}, "topic_id": "joca_reading"},
        {
            "type": "paragraph",
            "content": {
                "text": "O Jornal Joca é um jornal para crianças e adolescentes. A matéria «Brincar e jogar colabora para o "
                "desenvolvimento do seu filho» explica que brincadeira é necessidade humana em qualquer idade. "
                "Na infância, desenvolve potencialidades, permite interagir com o mundo e construir valores. "
                "Glossário: potencialidades = capacidades a desenvolver; interagir = comunicar-se, relacionar-se.",
            },
            "topic_id": "joca_reading",
            "sources": [_src("page-002.jpg"), _src("page-003.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Dica:",
                "text": "Texto informativo = apresenta fatos e explicações sobre um assunto, sem inventar história.",
            },
            "topic_id": "joca_reading",
        },
    ]


def _topic_visual() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "3. Recursos gráfico-visuais"}, "topic_id": "visual_resources"},
        {
            "type": "paragraph",
            "content": {
                "text": "Recursos gráfico-visuais são ilustrações, tamanho das letras, cores, gráficos, setas, números e barras "
                "usados em um texto. No infográfico, eles complementam o texto verbal e facilitam a leitura rápida. "
                "A principal característica do infográfico: mistura texto verbal e recursos gráfico-visuais.",
            },
            "topic_id": "visual_resources",
            "sources": [_src("page-005.jpg"), _src("page-010.jpg")],
        },
        {
            "type": "bar_chart",
            "content": {
                "title": "Exemplo: espécies animais do Brasil (dados do caderno)",
                "bars": [
                    {"label": "Mamíferos", "value": 720, "color": "#e67e22"},
                    {"label": "Aves", "value": 1924, "color": "#3498db"},
                    {"label": "Répteis", "value": 759, "color": "#27ae60"},
                    {"label": "Anfíbios", "value": 986, "color": "#9b59b6"},
                    {"label": "Peixes", "value": 4388, "color": "#2980b9"},
                ],
                "unit": "espécies",
            },
            "topic_id": "visual_resources",
            "sources": [_src("page-027.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Leia o gráfico:",
                "text": "Quanto maior a barra, maior o número de espécies. Peixes têm a barra mais longa. "
                "A flora brasileira (46 mil espécies) seria mais de dez vezes maior que a barra dos peixes.",
            },
            "topic_id": "visual_resources",
        },
    ]


def _topic_suffixes() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "4. Sufixos derivacionais"}, "topic_id": "suffixes"},
        {
            "type": "paragraph",
            "content": {
                "text": "Sufixo = terminação que forma palavra nova. Palavra primitiva (base) + sufixo = palavra derivada. "
                "Principais sufixos do caderno: -agem (lavagem, viagem), -esa/-ês (francesa/francês), "
                "-eza/-ez (beleza, surdez), títulos de nobreza (-esa: duquesa, baronesa).",
            },
            "topic_id": "suffixes",
            "sources": [_src("page-010.jpg"), _src("page-011.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Sufixo", "Exemplo", "Regra ortográfica"],
                "rows": [
                    ["-agem", "lavar → lavagem", "Sempre com g"],
                    ["-ês / -esa", "polonês / polonesa", "Nacionalidade — sempre com s"],
                    ["-eza / -ez", "riqueza / surdez", "De adjetivo — sempre com z"],
                ],
            },
            "topic_id": "suffixes",
        },
    ]


def _topic_nasal() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "5. Marcas de nasalidade"}, "topic_id": "nasal"},
        {
            "type": "paragraph",
            "content": {
                "text": "O som nasal pode ser indicado por: til (~) em sílaba final (maçã, limão), "
                "vogal + m antes de p/b (campo, também) ou vogal + n antes de outras consoantes (quente, andar). "
                "Regra: o til só aparece no interior da palavra quando se acrescenta sufixo (-zinho, -mente): pãozinho.",
            },
            "topic_id": "nasal",
            "sources": [_src("page-017.jpg"), _src("page-018.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Marca", "Exemplos", "Quando usar"],
                "rows": [
                    ["Til (~)", "maçã, limão, pão", "Sílaba tônica final"],
                    ["Vogal + m", "campo, samba, tombo", "Antes de p ou b"],
                    ["Vogal + n", "quente, santo, nunca", "Antes de outras consoantes"],
                ],
            },
            "topic_id": "nasal",
        },
    ]


def _topic_research() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "6. Pesquisa escolar"}, "topic_id": "research"},
        {
            "type": "paragraph",
            "content": {
                "text": "Pesquisa escolar = investigar um assunto em fontes confiáveis (livros, enciclopédias, jornais, sites). "
                "Etapas: definir tema, levantar fontes, selecionar dados, produzir texto (sem copiar!) e registrar fontes. "
                "No Módulo 5, o grupo produz infográfico sobre «Brincadeiras pelo Brasil» para mostra escolar.",
            },
            "topic_id": "research",
            "sources": [_src("page-020.jpg"), _src("page-021.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Citar fontes:",
                "text": "Livro: autor, título, editora, ano. Site: autor, título, link e data de acesso. "
                "Informações do infográfico devem ser verdadeiras — vêm de pesquisa.",
            },
            "topic_id": "research",
        },
    ]


def _topic_dictionary() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "7. Verbetes de dicionário"}, "topic_id": "dictionary"},
        {
            "type": "paragraph",
            "content": {
                "text": "Verbete = conjunto de informações sobre uma palavra: significados, classe gramatical, "
                "divisão silábica, sílaba tônica e exemplos. A entrada aparece em destaque no início. "
                "Exemplo do Aurelinho — brinquedo (brin.que.do) substantivo masculino: "
                "1. Objeto que serve para brincar. 2. Jogo, distração.",
            },
            "topic_id": "dictionary",
            "sources": [_src("page-032.jpg"), _src("page-034.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Parte do verbete", "Exemplo «brinquedo»", "Função"],
                "rows": [
                    ["Entrada", "brinquedo", "Palavra em destaque"],
                    ["Sílabas", "brin.que.do", "Divisão + tônica (que)"],
                    ["Classe", "substantivo masculino", "Tipo gramatical"],
                    ["Definição", "Objeto que serve para brincar", "Significado"],
                ],
            },
            "topic_id": "dictionary",
        },
    ]


def _topic_encyclopedia() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "8. Artigo enciclopédico"}, "topic_id": "encyclopedia"},
        {
            "type": "paragraph",
            "content": {
                "text": "Enciclopédia traz informações sobre assuntos (animais, brinquedos, países) — não só definições de palavras. "
                "Artigo enciclopédico usa linguagem objetiva, verbos no presente e 3ª pessoa. "
                "O caderno apresenta artigo sobre brinquedos e orienta produção de verbete sobre animal ameaçado.",
            },
            "topic_id": "encyclopedia",
            "sources": [_src("page-037.jpg"), _src("page-041.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Dicionário × enciclopédia:",
                "text": "Dicionário = o que a palavra significa. Enciclopédia = tudo sobre o assunto da palavra.",
            },
            "topic_id": "encyclopedia",
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
                    "title": "1. Infográfico",
                    "body": "Texto + recursos visuais. Brincar desenvolve cognição, motor, afetivo e social.",
                },
                "topic_id": "infographic",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "2. Texto Joca",
                    "body": "Informativo · brincadeira = potencialidades + interação · não só diversão.",
                },
                "topic_id": "joca_reading",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "3. Recursos visuais",
                    "body": "Cores, setas, gráficos complementam texto. Barras = comparar quantidades.",
                },
                "topic_id": "visual_resources",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "4. Sufixos",
                    "body": "-agem (g) · -ês/-esa (s) · -eza/-ez (z). Primitiva + sufixo = derivada.",
                },
                "topic_id": "suffixes",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "5. Nasalidade",
                    "body": "Til no final · m antes de p/b · n antes de outras consoantes.",
                },
                "topic_id": "nasal",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "6. Pesquisa",
                    "body": "Fontes confiáveis · anotar · citar · produzir infográfico original.",
                },
                "topic_id": "research",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "7. Dicionário",
                    "body": "Verbete = entrada + sílabas + classe + definição + exemplo.",
                },
                "topic_id": "dictionary",
            },
            {
                "type": "accordion_item",
                "content": {
                    "title": "8. Enciclopédia",
                    "body": "Artigo informativo · presente · 3ª pessoa · linguagem objetiva.",
                },
                "topic_id": "encyclopedia",
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "Infográfico ≠ texto só com palavras. Precisa ter recursos gráfico-visuais junto. "
                    "Nacionalidade = -ês com s, nunca com z.",
                },
            },
        ],
    }


def _section_game_brincadeira() -> dict:
    return {
        "id": "game_brincadeira",
        "type": "study_game",
        "title": "Jogo: Brincadeira certa",
        "blocks": [
            {
                "type": "panel_intro",
                "content": {
                    "title": "Qual benefício?",
                    "text": "Clique em uma brincadeira e depois no benefício que ela mais desenvolve. "
                    "Conteúdo do infográfico «A IMPORTÂNCIA DO BRINCAR» — Módulo 5.",
                },
            },
            {
                "type": "study_game",
                "content": {
                    "mode": "sort_buckets",
                    "game_id": "brincadeira_sort",
                    "instructions": "Selecione uma brincadeira e clique no benefício correto.",
                    "buckets": [
                        {"id": "cognitivo", "label": "Cognitivo", "hint": "Memória · raciocínio · atenção"},
                        {"id": "motor", "label": "Motor", "hint": "Coordenação · força · habilidade física"},
                        {"id": "afetivo", "label": "Afetivo", "hint": "Vínculos · emoções · empatia"},
                        {"id": "social", "label": "Social", "hint": "Cooperação · autonomia · cidadania"},
                    ],
                    "sort_items": [
                        {"id": "b1", "text": "Jogar xadrez", "answer": "cognitivo"},
                        {"id": "b2", "text": "Pular corda", "answer": "motor"},
                        {"id": "b3", "text": "Esconde-esconde com amigos", "answer": "afetivo"},
                        {"id": "b4", "text": "Jogar bola em equipe", "answer": "social"},
                        {"id": "b5", "text": "Montar quebra-cabeça", "answer": "cognitivo"},
                        {"id": "b6", "text": "Andar de bicicleta", "answer": "motor"},
                        {"id": "b7", "text": "Construir objetos com sucata", "answer": "cognitivo"},
                        {"id": "b8", "text": "Pular amarelinha em grupo", "answer": "social"},
                    ],
                },
            },
        ],
    }


def _section_game_sufixo() -> dict:
    return {
        "id": "game_sufixo",
        "type": "study_game",
        "title": "Jogo: Detetive do sufixo",
        "blocks": [
            {
                "type": "panel_intro",
                "content": {
                    "title": "Qual sufixo formou a palavra?",
                    "text": "Clique em uma palavra derivada e depois no sufixo que a formou. "
                    "Estudo da língua — Módulo 5.",
                },
            },
            {
                "type": "study_game",
                "content": {
                    "mode": "match_pairs",
                    "game_id": "sufixo_match",
                    "instructions": "Selecione a palavra derivada à esquerda e o sufixo correto à direita.",
                    "left": [
                        {"id": "l1", "text": "lavagem (de lavar)"},
                        {"id": "l2", "text": "francesa (de França)"},
                        {"id": "l3", "text": "riqueza (de rico)"},
                        {"id": "l4", "text": "polonês (de Polônia)"},
                        {"id": "l5", "text": "viagem (de viajar)"},
                        {"id": "l6", "text": "surdez (de surdo)"},
                    ],
                    "right": [
                        {"id": "r1", "text": "Sufixo -agem (com g)"},
                        {"id": "r2", "text": "Sufixo -esa (com s)"},
                        {"id": "r3", "text": "Sufixo -eza (com z)"},
                        {"id": "r4", "text": "Sufixo -ês (com s)"},
                        {"id": "r5", "text": "Sufixo -ez (com z)"},
                    ],
                    "answers": {
                        "l1": "r1",
                        "l2": "r2",
                        "l3": "r3",
                        "l4": "r4",
                        "l5": "r1",
                        "l6": "r5",
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
                "id": "bp-pe-001",
                "type": "multiple_choice",
                "topic": "infographic",
                "question": "Qual é a principal característica de um infográfico, segundo o caderno?",
                "options": [
                    "Usar apenas palavras, sem imagens",
                    "Misturar texto verbal e recursos gráfico-visuais",
                    "Contar uma história de ficção com personagens",
                    "Apresentar só definições de palavras em ordem alfabética",
                ],
                "correct_answer": 1,
                "explanation": "Infográfico combina texto escrito com ilustrações, cores, gráficos e setas.",
                "difficulty": "basic",
                "source_assets": sa("page-007.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp-pe-002",
                "type": "multiple_choice",
                "topic": "infographic",
                "question": (
                    "Leia as afirmativas sobre infográficos:\n"
                    "I. Informam por meio de texto verbal e recursos gráfico-visuais.\n"
                    "II. Podem aparecer em jornais, revistas e sites.\n"
                    "III. As informações devem ser verdadeiras, pois vêm de pesquisa.\n"
                    "IV. Nunca usam números ou barras coloridas.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e III", "II e IV", "III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Infográficos usam números e barras (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-007.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp-pe-003",
                "type": "multiple_choice",
                "topic": "joca_reading",
                "question": (
                    f"Leia o texto:\n\n{JOCA_TEXT}\n\n"
                    "Segundo o texto, a brincadeira na infância serve apenas para diversão?"
                ),
                "options": [
                    "Sim — brincar é só passatempo sem aprendizado",
                    "Não — também desenvolve potencialidades e permite interagir com o mundo",
                    "Sim — só adultos aprendem brincando",
                    "Não — porque brincadeira é proibida na escola",
                ],
                "correct_answer": 1,
                "explanation": "O texto diz que brincadeira desenvolve potencialidades e permite interagir.",
                "difficulty": "basic",
                "source_assets": sa("page-002.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp-pe-004",
                "type": "multiple_choice",
                "topic": "joca_reading",
                "question": (
                    f"Leia o texto:\n\n{JOCA_TEXT}\n\n"
                    "Leia as afirmativas:\n"
                    "I. «Potencialidades» significa capacidades a serem desenvolvidas.\n"
                    "II. «Interagir» significa comunicar-se e relacionar-se.\n"
                    "III. O texto é uma notícia do Jornal Joca.\n"
                    "IV. Brincadeira é necessidade só das crianças.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e III", "II, III e IV", "I e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Texto diz «em qualquer idade» (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-002.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp-pe-005",
                "type": "multiple_choice",
                "topic": "joca_reading",
                "question": (
                    f"Leia o texto:\n\n{JOCA_EXTENDED}\n\n"
                    "Por que o autor sugere diálogo entre pais, filhos, avós e netos?"
                ),
                "options": [
                    "Para proibir videogames definitivamente",
                    "Para trocar informações sobre brincadeiras tradicionais e atuais",
                    "Para substituir a aula de Português por jogos",
                    "Porque avós não sabem usar a internet",
                ],
                "correct_answer": 1,
                "explanation": "O texto propõe conhecer e trocar informações sobre jogos antigos e atuais.",
                "difficulty": "basic",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp-pe-006",
                "type": "multiple_choice",
                "topic": "visual_resources",
                "question": (
                    "Observe o gráfico de barras sobre espécies animais do Brasil.\n\n"
                    "Qual grupo tem o MAIOR número de espécies catalogadas?"
                ),
                "visual": {
                    "type": "bar_chart",
                    "content": {
                        "title": "Espécies animais do Brasil",
                        "bars": [
                            {"label": "Mamíferos", "value": 520, "color": "#e67e22"},
                            {"label": "Aves", "value": 1800, "color": "#3498db"},
                            {"label": "Répteis", "value": 680, "color": "#27ae60"},
                            {"label": "Peixes", "value": 3200, "color": "#2980b9"},
                        ],
                        "unit": "espécies",
                    },
                },
                "options": ["Mamíferos", "Aves", "Répteis", "Peixes"],
                "correct_answer": 3,
                "explanation": "Peixes têm a barra mais longa (3 200) — maior quantidade entre os grupos.",
                "difficulty": "basic",
                "source_assets": sa("page-027.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp-pe-007",
                "type": "multiple_choice",
                "topic": "visual_resources",
                "question": (
                    "Leia as afirmativas sobre recursos gráfico-visuais:\n"
                    "I. Incluem ilustrações, cores, setas e gráficos.\n"
                    "II. No infográfico, facilitam a leitura rápida das informações.\n"
                    "III. Substituem totalmente o texto verbal.\n"
                    "IV. Barras de tamanhos diferentes indicam quantidades distintas.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. Recursos complementam, não substituem o texto (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp-pe-008",
                "type": "multiple_choice",
                "topic": "suffixes",
                "question": "A palavra «viagem» é derivada de qual verbo, usando o sufixo -agem?",
                "options": ["viajar", "viaje", "viável", "viaduto"],
                "correct_answer": 0,
                "explanation": "viajar → viagem (verbo perde o -r e ganha -agem).",
                "difficulty": "basic",
                "source_assets": sa("page-011.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp-pe-009",
                "type": "multiple_choice",
                "topic": "suffixes",
                "question": (
                    "Leia as afirmativas sobre sufixos:\n"
                    "I. O sufixo -ês indica nacionalidade e é escrito com s.\n"
                    "II. «Riqueza» deriva de «rico» com sufixo -eza (letra z).\n"
                    "III. «Lavagem» deriva de «lavar» com sufixo -agem (letra g).\n"
                    "IV. «Surdez» usa sufixo -ez escrito com s.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "III e IV", "I, II e III", "II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e III corretas. -ez é escrito com z, não s (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-015.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp-pe-010",
                "type": "multiple_choice",
                "topic": "nasal",
                "question": "A palavra «campo» usa qual marca de nasalidade?",
                "options": [
                    "Til (~) no final",
                    "Vogal + m antes de p",
                    "Vogal + n antes de outras consoantes",
                    "Não tem som nasal",
                ],
                "correct_answer": 1,
                "explanation": "cam-po: m antes de p indica nasalidade.",
                "difficulty": "basic",
                "source_assets": sa("page-018.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp-pe-011",
                "type": "multiple_choice",
                "topic": "nasal",
                "question": (
                    "Leia as afirmativas sobre nasalidade:\n"
                    "I. «Maçã» usa til em sílaba final.\n"
                    "II. «Quente» usa vogal + n antes de t.\n"
                    "III. O til pode aparecer no interior da palavra com sufixos como -zinho.\n"
                    "IV. «Samba» usa vogal + n antes de b.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e III", "II e IV", "III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Samba usa m, não n (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-017.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp-pe-012",
                "type": "multiple_choice",
                "topic": "research",
                "question": "Qual é a primeira etapa de uma pesquisa escolar, segundo o caderno?",
                "options": [
                    "Copiar textos inteiros da internet",
                    "Definir o assunto e a pergunta investigativa",
                    "Imprimir imagens sem citar a fonte",
                    "Entregar o infográfico sem revisar",
                ],
                "correct_answer": 1,
                "explanation": "Pesquisa começa definindo tema e o que se quer investigar.",
                "difficulty": "basic",
                "source_assets": sa("page-021.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp-pe-013",
                "type": "multiple_choice",
                "topic": "dictionary",
                "question": (
                    "Leia o verbete:\n"
                    "brinquedo (brin.que.do) substantivo masculino\n"
                    "1. Objeto que serve para brincar. 2. Jogo, distração.\n\n"
                    "Qual é a sílaba tônica de «brinquedo»?"
                ),
                "options": ["brin", "que", "do", "brinque"],
                "correct_answer": 1,
                "explanation": "No verbete, «que» aparece em destaque — é a sílaba tônica.",
                "difficulty": "basic",
                "source_assets": sa("page-034.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp-pe-014",
                "type": "multiple_choice",
                "topic": "dictionary",
                "question": (
                    "Leia as afirmativas sobre verbetes:\n"
                    "I. A entrada é a palavra em destaque no início.\n"
                    "II. Apresentam classe gramatical e exemplos de uso.\n"
                    "III. Enciclopédias e dicionários têm a mesma função.\n"
                    "IV. As palavras são organizadas em ordem alfabética.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "II e III", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. Dicionário = palavras; enciclopédia = assuntos (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-033.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp-pe-015",
                "type": "multiple_choice",
                "topic": "encyclopedia",
                "question": (
                    f"Leia o texto:\n\n{BRINQUEDO_ARTICLE}\n\n"
                    "Qual material era mais comum nos brinquedos antigos, segundo o artigo?"
                ),
                "options": [
                    "Plástico",
                    "Madeira e tecido",
                    "Metal e vidro",
                    "Papel e cola apenas",
                ],
                "correct_answer": 1,
                "explanation": "Texto diz: «Anos atrás, a maioria era feita de madeira e de tecido. Hoje, plástico.»",
                "difficulty": "basic",
                "source_assets": sa("page-037.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp-pe-016",
                "type": "multiple_choice",
                "topic": "encyclopedia",
                "question": (
                    f"Leia o texto:\n\n{BRINQUEDO_ARTICLE}\n\n"
                    "Leia as afirmativas:\n"
                    "I. Brinquedos podem educar e estimular a criatividade.\n"
                    "II. Arqueólogos encontram sinais de brinquedos em escavações.\n"
                    "III. O artigo é enciclopédico — trata do assunto «brinquedo».\n"
                    "IV. Todos os brinquedos atuais são feitos de madeira.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, II e III", "III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e III corretas. Hoje o comum é plástico, não madeira (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-037.jpg"),
                "section": "final_quiz",
            },
        ],
    }
