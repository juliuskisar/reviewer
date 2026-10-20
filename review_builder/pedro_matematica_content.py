"""Conteúdo pedagógico da revisão Pedro — Matemática PE 2º trimestre."""

from __future__ import annotations

REVIEW_ID = "pedro-pe-matematica-2tri"
ASSET_PREFIX = "assets/pedro_pe_matematica_2_tri"


def _src(page: str) -> dict:
    return {
        "asset": f"{ASSET_PREFIX}/{page}",
        "origin_type": "observed",
        "evidence": [f"Caderno de Matemática — {page}"],
    }


def build_content() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Matemática — PE 2º Trimestre",
        "subtitle": "Pedro · 6º ano · Módulos 18, 19 e 24",
        "language": "pt-BR",
        "discipline": "Matemática",
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
            {"order": 4, "title": "Desafios", "section_id": "desafios"},
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
                    "text": "Expressões numéricas, multiplicação e divisão de decimais, divisão com resto, "
                    "relação com frações, razões, médias e leitura de gráficos. Reserve cerca de 1 hora.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🔢", "title": "Expressões", "text": "Ordem das operações · parênteses · potências"},
                        {"icon": "✖️", "title": "Multiplicação", "text": "Compensação · casas decimais"},
                        {"icon": "➗", "title": "Divisão decimal", "text": "×10/×100 no dividendo e divisor"},
                        {"icon": "🧩", "title": "Resto", "text": "Com quebra x sem quebra"},
                        {"icon": "➗", "title": "Frações", "text": "7 ÷ 4 = 7/4 = 1 + 3/4"},
                        {"icon": "📊", "title": "Estatística", "text": "Razões · média · gráficos"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 18 — Expressões e multiplicação decimal",
                        "Módulo 19 — Divisão decimal",
                        "Módulo 24 — Frações, razões e estatística",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Revise procedimentos e exemplos.",
                            "tip": "Refaça um exemplo de cada procedimento no caderno.",
                        },
                        {
                            "title": "Revise o Resumo rápido",
                            "panel": "summary",
                            "panel_label": "Resumo rápido",
                            "description": "Use como mapa mental antes da PE.",
                        },
                        {
                            "title": "Faça os Exercícios",
                            "panel": "exercises",
                            "panel_label": "Exercícios",
                            "description": "Questões no estilo Teste do caderno.",
                            "tip": "Responda primeiro; só depois clique em Verificar.",
                        },
                        {
                            "title": "Encare os Desafios",
                            "panel": "desafios",
                            "panel_label": "Desafios",
                            "description": "Problemas mais exigentes — estilo Atividade e Teste Cesgranrio da apostila.",
                            "tip": "Só depois de revisar explicações e exercícios regulares.",
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
            *_topic_expressions(),
            *_topic_decimal_multiply(),
            *_topic_decimal_divide(),
            *_topic_division_break(),
            *_topic_division_fractions(),
            *_topic_ratios(),
            *_topic_mean(),
            *_topic_statistics(),
        ],
    }


def _topic_expressions() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Expressões numéricas"}, "topic_id": "expressions"},
        {
            "type": "paragraph",
            "content": {
                "text": "Uma expressão numérica combina operações (+, −, ×, ÷, potência). "
                "Há convenções para a ordem de cálculo.",
            },
            "topic_id": "expressions",
            "sources": [_src("page-001.jpg"), _src("page-004.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "1️⃣", "title": "Parênteses", "text": "Resolve primeiro o que está dentro"},
                    {"icon": "2️⃣", "title": "× e ÷", "text": "Da esquerda para a direita"},
                    {"icon": "3️⃣", "title": "+ e −", "text": "Por último, da esquerda para a direita"},
                    {"icon": "²", "title": "Potência", "text": "2³ = 2 × 2 × 2 = 8"},
                ],
            },
            "topic_id": "expressions",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Exemplo:",
                "text": "50 − (12 + 3 × 10) → dentro dos parênteses: 3×10=30, 12+30=42, 50−42=8.",
            },
            "topic_id": "expressions",
        },
    ]


def _topic_decimal_multiply() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "2. Multiplicação de decimais"}, "topic_id": "decimal_multiply"},
        {
            "type": "paragraph",
            "content": {
                "text": "Para multiplicar decimais, você pode usar o procedimento da compensação "
                "ou contar as casas decimais dos fatores.",
            },
            "topic_id": "decimal_multiply",
            "sources": [_src("page-005.jpg"), _src("page-006.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Dois procedimentos",
                "headers": ["", "Compensação", "Contagem de casas"],
                "rows": [
                    ["Ideia", "Transformar decimal em natural (×10, ×100) e compensar no final", "Somar casas decimais dos fatores no produto"],
                    ["Exemplo", "24 × 0,3 → 24×3=72 → 72÷10=7,2", "0,2 × 0,3 → 2×3=6 → duas casas → 0,06"],
                    ["Quando usar", "Um fator decimal simples", "Qualquer multiplicação decimal"],
                ],
            },
            "topic_id": "decimal_multiply",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Atenção:",
                "text": "Multiplicar por número entre 0 e 1 diminui o valor (ex.: 4 × 0,25 = 1).",
            },
            "topic_id": "decimal_multiply",
        },
    ]


def _topic_decimal_divide() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "3. Divisão de decimais"}, "topic_id": "decimal_divide"},
        {
            "type": "paragraph",
            "content": {
                "text": "Para dividir com decimais, multiplique dividendo e divisor pelo mesmo número "
                "(10, 100, 1000…) até o divisor virar natural — o quociente não muda.",
            },
            "topic_id": "decimal_divide",
            "sources": [_src("page-010.jpg"), _src("page-011.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "×2", "title": "Dividendo ×2", "text": "Quociente também dobra"},
                    {"icon": "÷2", "title": "Divisor ×2", "text": "Quociente cai pela metade"},
                    {"icon": "⚖️", "title": "Ambos ×2", "text": "Quociente permanece igual"},
                    {"icon": "📐", "title": "Exemplo", "text": "2,4 ÷ 0,75 → 240 ÷ 75 = 3,2"},
                ],
            },
            "topic_id": "decimal_divide",
        },
    ]


def _topic_division_break() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "4. Divisão com e sem quebra"}, "topic_id": "division_break"},
        {
            "type": "paragraph",
            "content": {
                "text": "Em alguns problemas o resto pode ser subdividido (densidade, média, razão). "
                "Em outros, não dá para repartir o que sobrou (chaveiros, cadernos inteiros).",
            },
            "topic_id": "division_break",
            "sources": [_src("page-008.jpg"), _src("page-009.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Dois tipos de situação",
                "headers": ["", "Com quebra (decimal)", "Sem quebra (resto)"],
                "rows": [
                    ["Exemplo", "234 candidatos ÷ 27 vagas ≈ 8,67", "53 chaveiros ÷ 8 sobrinhos = 6 cada, resto 5"],
                    ["Resposta", "Quociente com vírgula", "Parte inteira + resto que sobra"],
                    ["Contexto", "Densidade, média, razão", "Objetos indivisíveis"],
                ],
            },
            "topic_id": "division_break",
        },
    ]


def _topic_division_fractions() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "5. Divisão e frações"}, "topic_id": "division_fractions"},
        {
            "type": "paragraph",
            "content": {
                "text": "Toda divisão de naturais (divisor ≠ 0) pode ser escrita como fração. "
                "Quando o dividendo é maior que o divisor, o resultado vira número misto.",
            },
            "topic_id": "division_fractions",
            "sources": [_src("page-014.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "➗", "title": "7 ÷ 4", "text": "Fração imprópria 7/4"},
                    {"icon": "➕", "title": "Número misto", "text": "1 + 3/4 (1 inteiro e 3 quartos)"},
                    {"icon": "🔗", "title": "Relação", "text": "Quociente = parte inteira; resto = numerador"},
                ],
            },
            "topic_id": "division_fractions",
        },
        {
            "type": "fraction_visual",
            "content": {
                "title": "Visualizando 8/3 com barras de chocolate",
                "intro": "Cada barra inteira é dividida em 3 partes iguais (terços). "
                "Assim fica fácil enxergar 2 barras completas e mais 2 terços.",
                "bars": [
                    {"segments": 3, "filled": 3, "label": "1ª barra"},
                    {"segments": 3, "filled": 3, "label": "2ª barra"},
                    {"segments": 3, "filled": 2, "label": "2/3"},
                ],
                "summary": "Total: 8 terços = 8/3 = 2 + 2/3",
                "caption": "Fração imprópria: numerador maior que o denominador.",
                "aria_label": "Duas barras de chocolate inteiras e dois terços de uma terceira barra",
            },
            "topic_id": "division_fractions",
        },
    ]


def _topic_ratios() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "6. Razões e densidade"}, "topic_id": "ratios"},
        {
            "type": "paragraph",
            "content": {
                "text": "Razão compara duas grandezas. Ex.: candidatos por vaga = candidatos ÷ vagas. "
                "Densidade demográfica = população ÷ área (hab/km²).",
            },
            "topic_id": "ratios",
            "sources": [_src("page-002.jpg"), _src("page-003.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Exemplo:",
                "text": "1.358 candidatos ÷ 27 vagas ≈ 50,3 candidatos por vaga.",
            },
            "topic_id": "ratios",
        },
    ]


def _topic_mean() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "7. Média aritmética"}, "topic_id": "mean"},
        {
            "type": "paragraph",
            "content": {
                "text": "A média aritmética é a soma de todos os valores dividida pela quantidade de dados.",
            },
            "topic_id": "mean",
            "sources": [_src("page-012.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Fórmula:",
                "text": "Média = (valor₁ + valor₂ + … + valorₙ) ÷ n",
            },
            "topic_id": "mean",
        },
    ]


def _topic_statistics() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "8. Gráficos e frações do total"}, "topic_id": "statistics"},
        {
            "type": "paragraph",
            "content": {
                "text": "Gráficos de barras mostram quantidades. Para achar a fração de um item no total, "
                "some todos os valores, depois divida a quantidade do item pelo total.",
            },
            "topic_id": "statistics",
            "sources": [_src("page-002.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "📊", "title": "Total", "text": "Soma de todas as barras"},
                    {"icon": "🏆", "title": "Maior valor", "text": "Barra mais longa"},
                    {"icon": "➗", "title": "Fração", "text": "Parte ÷ total (simplifique)"},
                ],
            },
            "topic_id": "statistics",
        },
        {
            "type": "bar_chart",
            "content": {
                "title": "Ingressos vendidos na bilheteria da escola (por gênero de filme)",
                "bars": [
                    {"label": "Ação", "value": 45, "color": "#ef4444"},
                    {"label": "Animação", "value": 36, "color": "#3b82f6"},
                    {"label": "Comédia", "value": 27, "color": "#f59e0b"},
                    {"label": "Fic. científica", "value": 24, "color": "#8b5cf6"},
                    {"label": "Drama", "value": 18, "color": "#10b981"},
                ],
                "caption": "Exemplo: o gênero mais vendido (ação, 45) representa 45/150 = 3/10 do total.",
                "aria_label": "Gráfico de barras horizontais com ingressos por gênero de filme",
            },
            "topic_id": "statistics",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Como resolver:",
                "text": "Some todas as barras (total). Divida o maior valor pelo total e simplifique a fração.",
            },
            "topic_id": "statistics",
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
                    "text": "Revise cada tópico nos acordeões — procedimentos e pegadinhas.",
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "1. Expressões"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "()", "title": "Ordem", "text": "Parênteses → ×÷ → +−"},
                        {"icon": "²", "title": "Potência", "text": "Antes de + e −"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. Multiplicação decimal"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "↔️", "title": "Compensação", "text": "×10 no fator, ÷10 no produto"},
                        {"icon": "🔢", "title": "Casas decimais", "text": "Soma das casas dos fatores"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Divisão decimal"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "×100", "title": "Regra", "text": "Mesmo fator em dividendo e divisor"},
                        {"icon": "📐", "title": "Medida", "text": "Quantas vezes o divisor cabe no dividendo?"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Com/sem quebra"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["", "Com quebra", "Sem quebra"],
                    "rows": [
                        ["Quando", "Razões, médias", "Objetos inteiros"],
                        ["Resultado", "Decimal", "Quociente + resto"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Divisão e frações"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "7/4", "title": "Fração", "text": "Dividendo ÷ divisor"},
                        {"icon": "1¾", "title": "Misto", "text": "Inteiro + fração própria"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "6. Razões"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "👥", "title": "Por vaga", "text": "Candidatos ÷ vagas"},
                        {"icon": "🗺️", "title": "Densidade", "text": "População ÷ área"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "7. Média"}},
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Fórmula:",
                    "text": "Soma dos valores ÷ quantidade de dados.",
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "8. Gráficos"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "➕", "title": "Total", "text": "Soma das barras"},
                        {"icon": "➗", "title": "Fração", "text": "Maior valor ÷ total"},
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "Errar a vírgula em 254,88 ÷ 0,177 — use a relação com 144 × 177 = 25.488.",
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
                "id": "mat-pe-001",
                "type": "multiple_choice",
                "topic": "expressions",
                "question": "Qual é o valor de 50 − (12 + 3 × 10)?",
                "options": ["8", "38", "420", "470"],
                "correct_answer": 0,
                "explanation": "Dentro dos parênteses: 3×10=30, 12+30=42. Depois: 50−42=8.",
                "difficulty": "basic",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-002",
                "type": "multiple_choice",
                "topic": "expressions",
                "question": (
                    "Leia as afirmativas sobre expressões numéricas:\n"
                    "I. Operações dentro de parênteses são feitas primeiro.\n"
                    "II. Multiplicação sempre vem depois da adição.\n"
                    "III. 16 + 2³ = 16 + 8 = 24.\n"
                    "IV. 48 ÷ 2 × 0,5 = 48.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I e III", "I, II e IV"],
                "correct_answer": 2,
                "explanation": "I e III corretas. II errada (× antes de +). IV errada (48÷2×0,5=12, não 48).",
                "difficulty": "intermediate",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-003",
                "type": "multiple_choice",
                "topic": "decimal_multiply",
                "question": "Usando compensação, 24 × 0,3 é igual a:",
                "options": ["0,72", "7,2", "72", "720"],
                "correct_answer": 1,
                "explanation": "24×3=72; compensando ÷10 → 7,2.",
                "difficulty": "basic",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-004",
                "type": "multiple_choice",
                "topic": "decimal_multiply",
                "question": "Sabendo que 25 × 13 = 325, o produto 0,25 × 0,13 é:",
                "options": ["0,0325", "0,325", "3,25", "32,5"],
                "correct_answer": 0,
                "explanation": "Duas casas decimais em cada fator → quatro casas no produto: 0,0325.",
                "difficulty": "intermediate",
                "source_assets": sa("page-006.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-005",
                "type": "multiple_choice",
                "topic": "decimal_divide",
                "question": "Para calcular 2,4 ÷ 0,75, multiplicamos dividendo e divisor por 100 e obtemos:",
                "options": ["24 ÷ 75 = 0,32", "240 ÷ 75 = 3,2", "2400 ÷ 75 = 32", "2,4 ÷ 75 = 0,032"],
                "correct_answer": 1,
                "explanation": "2,4×100=240 e 0,75×100=75. 240÷75=3,2.",
                "difficulty": "intermediate",
                "source_assets": sa("page-011.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-006",
                "type": "multiple_choice",
                "topic": "decimal_divide",
                "question": (
                    "Leia as afirmativas sobre propriedades da divisão (base 16 ÷ 2 = 8):\n"
                    "I. Se o dividendo dobra, o quociente também dobra.\n"
                    "II. Se o divisor dobra, o quociente também dobra.\n"
                    "III. Se dividendo e divisor dobram, o quociente triplica.\n"
                    "IV. Se dividendo e divisor são multiplicados por 10, o quociente não muda.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "II e III", "I, II e IV", "III e IV"],
                "correct_answer": 0,
                "explanation": "I e IV corretas. II errada (quociente cai pela metade). III errada (quociente não muda).",
                "difficulty": "intermediate",
                "source_assets": sa("page-010.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-007",
                "type": "multiple_choice",
                "topic": "division_break",
                "question": (
                    "Marcelo distribui 53 chaveiros igualmente entre 8 sobrinhos, "
                    "sem partir os chaveiros. Cada sobrinho recebe:"
                ),
                "options": [
                    "6 chaveiros e sobram 5",
                    "6,625 chaveiros cada um",
                    "7 chaveiros e sobra 1",
                    "5 chaveiros e sobram 13",
                ],
                "correct_answer": 0,
                "explanation": "53÷8=6 resto 5 — objetos indivisíveis: resposta inteira + resto.",
                "difficulty": "basic",
                "source_assets": sa("page-008.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-008",
                "type": "multiple_choice",
                "topic": "division_fractions",
                "question": (
                    "Observe a representação das barras de chocolate abaixo. "
                    "Cada barra foi dividida em 4 pedaços iguais (quartos). "
                    "A quantidade total de chocolate equivale a:"
                ),
                "visual": {
                    "type": "fraction_visual",
                    "content": {
                        "title": "Barras de chocolate — feira de ciências",
                        "bars": [
                            {"segments": 4, "filled": 4, "label": "1ª barra"},
                            {"segments": 4, "filled": 4, "label": "2ª barra"},
                            {"segments": 4, "filled": 3, "label": "3/4"},
                        ],
                        "aria_label": "Duas barras inteiras e três quartos de uma terceira barra de chocolate",
                    },
                },
                "options": ["11/4 ou 2 + 3/4", "8/4 ou 2", "7/4 ou 1 + 3/4", "3/4"],
                "correct_answer": 0,
                "explanation": (
                    "Contando os quartos: 4 + 4 + 3 = 11 quartos → 11/4 = 2 + 3/4."
                ),
                "difficulty": "intermediate",
                "source_assets": sa("page-014.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-009",
                "type": "multiple_choice",
                "topic": "statistics",
                "question": (
                    "Observe o gráfico de vendas na feira de ciências. "
                    "Qual fração do total de lanches vendidos corresponde ao item mais vendido?"
                ),
                "visual": {
                    "type": "bar_chart",
                    "content": {
                        "title": "Vendas de lanches — feira de ciências",
                        "bars": [
                            {"label": "Esfiha", "value": 30, "color": "#f97316"},
                            {"label": "Pastel", "value": 24, "color": "#3b82f6"},
                            {"label": "Coxinha", "value": 18, "color": "#eab308"},
                            {"label": "Empada", "value": 16, "color": "#10b981"},
                            {"label": "Kibe", "value": 12, "color": "#8b5cf6"},
                        ],
                        "aria_label": "Gráfico de barras com vendas de lanches na feira de ciências",
                    },
                },
                "options": ["3/10", "1/4", "2/5", "3/8"],
                "correct_answer": 0,
                "explanation": (
                    "Some as barras: 30+24+18+16+12=100. Mais vendido: esfiha (30). 30/100=3/10."
                ),
                "difficulty": "intermediate",
                "source_assets": sa("page-002.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-010",
                "type": "multiple_choice",
                "topic": "ratios",
                "question": (
                    "Uma empresa abriu 27 vagas e recebeu 1.358 currículos. "
                    "A razão candidatos por vaga é aproximadamente:"
                ),
                "options": ["1,5", "13", "18", "50"],
                "correct_answer": 3,
                "explanation": "1358÷27 ≈ 50,3 candidatos por vaga.",
                "difficulty": "intermediate",
                "source_assets": sa("page-002.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-011",
                "type": "multiple_choice",
                "topic": "mean",
                "question": (
                    "Marcelo usou a internet (minutos): seg 230, ter 338, qua 95, qui 129, "
                    "sex 314, sáb 408, dom 250. A média diária da semana é:"
                ),
                "options": ["250 min", "252 min", "266 min", "280 min"],
                "correct_answer": 1,
                "explanation": "Soma=1764 minutos. 1764÷7=252 min de média por dia.",
                "difficulty": "intermediate",
                "source_assets": sa("page-012.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-012",
                "type": "multiple_choice",
                "topic": "decimal_divide",
                "question": (
                    "Sabendo que 144 × 177 = 25.488, o quociente de 254,88 ÷ 0,177 é:"
                ),
                "options": ["1440", "144", "14,4", "1,44"],
                "correct_answer": 0,
                "explanation": "254,88 = 25.488÷100 e 0,177 = 177÷1000 → quociente ×10 em relação a 144 → 1440.",
                "difficulty": "intermediate",
                "source_assets": sa("page-013.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-013",
                "type": "multiple_choice",
                "topic": "expressions",
                "question": "Qual é o valor de (4 × 1,5 + 9) ÷ 3?",
                "options": ["5", "6", "7,5", "13"],
                "correct_answer": 0,
                "explanation": "Parênteses: 4×1,5=6; 6+9=15. Depois: 15÷3=5.",
                "difficulty": "basic",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-014",
                "type": "multiple_choice",
                "topic": "decimal_multiply",
                "question": (
                    "A tarifa de ônibus é R$ 4,30. Uma pessoa usou o ônibus 25 vezes no mês. "
                    "Quanto gastou com passagens?"
                ),
                "options": ["R$ 107,50", "R$ 29,30", "R$ 430,00", "R$ 21,50"],
                "correct_answer": 0,
                "explanation": "25 × 4,30 = 107,50.",
                "difficulty": "basic",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-015",
                "type": "multiple_choice",
                "topic": "division_break",
                "question": (
                    "Uma creche recebeu 238 barrinhas de cereal para repartir igualmente "
                    "entre 32 crianças, sem partir as barrinhas. Cada criança recebe:"
                ),
                "options": [
                    "7 barrinhas e sobram 14",
                    "7,4375 barrinhas cada uma",
                    "8 barrinhas e sobra 1",
                    "6 barrinhas e sobram 46",
                ],
                "correct_answer": 0,
                "explanation": "238÷32=7 resto 14 — divisão sem quebra do resto.",
                "difficulty": "intermediate",
                "source_assets": sa("page-012.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-016",
                "type": "multiple_choice",
                "topic": "division_fractions",
                "question": "A divisão 11 ÷ 5 escrita como número misto é:",
                "options": ["2 + 1/5", "1 + 5/11", "5 + 1/11", "2 + 5/11"],
                "correct_answer": 0,
                "explanation": "11÷5=2 resto 1 → 2 + 1/5.",
                "difficulty": "basic",
                "source_assets": sa("page-014.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-017",
                "type": "multiple_choice",
                "topic": "decimal_multiply",
                "question": (
                    "Leia as afirmativas sobre multiplicação decimal:\n"
                    "I. 0,5 × 0,5 = 2,5.\n"
                    "II. 0,5 × 0,5 = 0,25.\n"
                    "III. 1,2 × 0,5 = 6.\n"
                    "IV. 2 × 0,5 = 1.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, II e III", "III e IV"],
                "correct_answer": 1,
                "explanation": "II e IV corretas. I errada (0,25). III errada (1,2×0,5=0,6).",
                "difficulty": "intermediate",
                "source_assets": sa("page-006.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-018",
                "type": "multiple_choice",
                "topic": "ratios",
                "question": (
                    "Leia as afirmativas sobre razões:\n"
                    "I. Densidade demográfica = área ÷ população.\n"
                    "II. Candidatos por vaga = candidatos ÷ vagas.\n"
                    "III. 234 candidatos para 27 vagas ≈ 8,67 candidatos por vaga.\n"
                    "IV. Uma razão pode relacionar unidades diferentes (ex.: hab/km²).\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II, III e IV", "I e III", "I, II e III"],
                "correct_answer": 1,
                "explanation": "II, III e IV corretas. I errada (densidade = população ÷ área, não o contrário).",
                "difficulty": "intermediate",
                "source_assets": sa("page-008.jpg"),
                "section": "final_quiz",
            },
            *_challenge_exercises(sa),
        ],
    }


def _challenge_exercises(sa) -> list:
    """10 desafios avançados — adaptados da apostila Pedro (imagens_matematica_pedro)."""
    return [
        {
            "id": "mat-des-001",
            "type": "multiple_choice",
            "topic": "expressions",
            "question": (
                "Paula tinha R$ 80,00. Comprou 6 cadernos de R$ 5,00 e 4 canetas de R$ 3,00. "
                "Qual expressão representa o troco e qual é o seu valor?"
            ),
            "options": [
                "80 − (6 × 5 + 4 × 3) = R$ 38,00",
                "80 − 6 × 5 + 4 × 3 = R$ 62,00",
                "80 − (6 + 5) × (4 + 3) = R$ 3,00",
                "6 × 5 + 4 × 3 − 80 = R$ −38,00",
            ],
            "correct_answer": 0,
            "explanation": "Gastos dentro dos parênteses: 6×5=30 e 4×3=12 → 42. Troco: 80−42=R$ 38,00.",
            "difficulty": "advanced",
            "source_assets": sa("page-004.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat-des-002",
            "type": "multiple_choice",
            "topic": "expressions",
            "question": (
                "Leia as afirmativas sobre expressões numéricas:\n"
                "I. 16 + 2³ = 16 + 6 = 22.\n"
                "II. 48 ÷ 2 × 0,5 = 12.\n"
                "III. O que está entre parênteses é calculado antes das demais operações.\n"
                "IV. 2 + 3 × 4 = 20.\n\n"
                "Estão corretas apenas:"
            ),
            "options": ["II e III", "Apenas III", "I e IV", "II, III e IV"],
            "correct_answer": 0,
            "explanation": "II e III corretas. I errada (2³=8 → 24). IV errada (2+3×4=14, não 20).",
            "difficulty": "advanced",
            "source_assets": sa("page-004.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat-des-003",
            "type": "multiple_choice",
            "topic": "decimal_multiply",
            "question": "Usando compensação ou contagem de casas decimais, 0,48 × 0,25 é igual a:",
            "options": ["0,012", "0,12", "1,2", "12"],
            "correct_answer": 1,
            "explanation": "48×25=1.200. Quatro casas decimais (duas em cada fator) → 0,12.",
            "difficulty": "advanced",
            "source_assets": sa("page-006.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat-des-004",
            "type": "multiple_choice",
            "topic": "decimal_divide",
            "question": (
                "Para cada receita de milk-shake são necessários 0,2 L de leite. "
                "Com 2 L na geladeira, quantas receitas completas é possível fazer?"
            ),
            "options": ["4 receitas", "10 receitas", "20 receitas", "0,4 receita"],
            "correct_answer": 1,
            "explanation": "2 ÷ 0,2 = 10 — multiplique dividendo e divisor por 10: 20 ÷ 2 = 10 receitas.",
            "difficulty": "advanced",
            "source_assets": sa("page-011.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat-des-005",
            "type": "multiple_choice",
            "topic": "division_break",
            "question": (
                "Marta tem R$ 100,00 e quer comprar cadernos de R$ 7,30 cada, "
                "sem poder comprar fração de caderno. Quantos cadernos ela consegue comprar?"
            ),
            "options": ["13 cadernos", "14 cadernos", "10 cadernos", "7 cadernos"],
            "correct_answer": 0,
            "explanation": "100 ÷ 7,30 ≈ 13,7 → no máximo 13 cadernos inteiros (13×7,30=R$ 94,90).",
            "difficulty": "advanced",
            "source_assets": sa("page-012.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat-des-006",
            "type": "multiple_choice",
            "topic": "division_break",
            "question": (
                "Uma creche recebeu 238 barrinhas de cereal para repartir igualmente "
                "entre 32 crianças, sem partir as barrinhas. Quantas barrinhas a mais "
                "precisariam ser compradas para que cada criança recebesse a mesma "
                "quantidade inteira e nenhuma sobrasse?"
            ),
            "options": ["14 barrinhas", "18 barrinhas", "32 barrinhas", "6 barrinhas"],
            "correct_answer": 1,
            "explanation": "238÷32=7 resto 14. Próximo múltiplo de 32: 8×32=256. Faltam 256−238=18 barrinhas.",
            "difficulty": "advanced",
            "source_assets": sa("page-012.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat-des-007",
            "type": "multiple_choice",
            "topic": "division_fractions",
            "question": (
                "Três amigos dividem barras de chocolate. Cada um recebe 2 barras inteiras "
                "mais 2/3 de uma barra. Quantos terços de barra cada um recebeu no total?"
            ),
            "options": ["6 terços", "8 terços", "2 terços", "5 terços"],
            "correct_answer": 1,
            "explanation": "2 + 2/3 = 6/3 + 2/3 = 8/3 → cada um recebe 8 terços de barra.",
            "difficulty": "advanced",
            "source_assets": sa("page-014.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat-des-008",
            "type": "multiple_choice",
            "topic": "statistics",
            "question": (
                "Observe o gráfico de doces vendidos por Cecília. "
                "Qual fração do total vendido corresponde ao doce mais vendido?"
            ),
            "visual": {
                "type": "bar_chart",
                "content": {
                    "title": "Doces vendidos por Cecília",
                    "bars": [
                        {"label": "Olho de sogra", "value": 10, "color": "#f97316"},
                        {"label": "Cajuzinho", "value": 25, "color": "#3b82f6"},
                        {"label": "Brigadeiro", "value": 32, "color": "#eab308"},
                        {"label": "Bem-casado", "value": 17, "color": "#10b981"},
                        {"label": "Beijinho", "value": 20, "color": "#8b5cf6"},
                    ],
                    "aria_label": "Gráfico de barras com quantidades de doces vendidos",
                },
            },
            "options": ["3/13", "4/13", "5/13", "1/4"],
            "correct_answer": 1,
            "explanation": "Total: 10+25+32+17+20=104. Mais vendido: brigadeiro (32). 32/104=4/13.",
            "difficulty": "advanced",
            "source_assets": sa("page-002.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat-des-009",
            "type": "multiple_choice",
            "topic": "ratios",
            "question": (
                "No vestibular da Unicamp, o curso de Medicina teve 25.273 candidatos "
                "para 86 vagas. A razão aproximada candidatos por vaga é:"
            ),
            "options": ["≈ 294 candidatos/vaga", "≈ 250 candidatos/vaga", "≈ 86 candidatos/vaga", "≈ 25 candidatos/vaga"],
            "correct_answer": 0,
            "explanation": "25.273 ÷ 86 ≈ 293,8 → cerca de 294 candidatos por vaga.",
            "difficulty": "advanced",
            "source_assets": sa("page-002.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat-des-010",
            "type": "multiple_choice",
            "topic": "mean",
            "question": (
                "Marcelo usou a internet (minutos): seg 230, ter 338, qua 95, qui 129, "
                "sex 314, sáb 408. A média diária da semana inteira (7 dias) foi 252 min. "
                "Quantos minutos ele usou no domingo?"
            ),
            "options": ["250 min", "252 min", "266 min", "1764 min"],
            "correct_answer": 0,
            "explanation": "Total da semana: 252×7=1.764 min. Soma seg–sáb: 1.514 min. Domingo: 1.764−1.514=250 min.",
            "difficulty": "advanced",
            "source_assets": sa("page-012.jpg"),
            "section": "desafios",
        },
    ]
