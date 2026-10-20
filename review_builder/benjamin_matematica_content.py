"""Conteúdo pedagógico da revisão Benjamin — Matemática PE 2º trimestre."""

from __future__ import annotations

REVIEW_ID = "benjamin-pe-matematica-2tri"
ASSET_PREFIX = "assets/benjamin_pe_matematica_2_tri"


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
        "subtitle": "Benjamin · 4º ano · Módulos 10, 11, 12, 13, 14 e 15",
        "language": "pt-BR",
        "discipline": "Matemática",
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
                    "text": "Números naturais e ordens, compensação na subtração, gráficos de barras, "
                    "segmentos paralelos e perpendiculares, multiplicação e divisão por 10/100/1000, "
                    "divisão exata e não exata e ângulos. Reserve cerca de 55 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🔢", "title": "Números", "text": "Pares · ímpares · comparação"},
                        {"icon": "➖", "title": "Compensação", "text": "Mesma mudança nos dois termos"},
                        {"icon": "📊", "title": "Gráficos", "text": "Barras · total · maior valor"},
                        {"icon": "📐", "title": "Segmentos", "text": "Paralelos · perpendiculares"},
                        {"icon": "✖️", "title": "× e ÷", "text": "Por 10 · 100 · 1000"},
                        {"icon": "➗", "title": "Divisão", "text": "Exata · resto · repertório"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 10 — Números naturais e ordens",
                        "Módulo 11 — Compensação e gráficos",
                        "Módulo 12 — Paralelismo e perpendicularismo",
                        "Módulo 13 — Multiplicação por 10, 100 e 1000",
                        "Módulo 14 — Divisão exata e não exata",
                        "Módulo 15 — Noção de ângulos",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Leia os cards e tabelas com calma.",
                            "tip": "Refaça um exemplo de cada procedimento no caderno.",
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
                        {
                            "title": "Encare os Desafios",
                            "panel": "desafios",
                            "panel_label": "Desafios",
                            "description": "Problemas mais difíceis — para testar o que aprendeu de verdade.",
                            "tip": "Só depois de revisar as explicações e os exercícios regulares.",
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
            *_topic_natural_numbers(),
            *_topic_place_value(),
            *_topic_compensation(),
            *_topic_bar_charts(),
            *_topic_parallel_perpendicular(),
            *_topic_multiply_powers(),
            *_topic_division(),
            *_topic_angles(),
        ],
    }


def _topic_natural_numbers() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Números naturais"}, "topic_id": "natural_numbers"},
        {
            "type": "paragraph",
            "content": {
                "text": "Os números naturais servem para contar e ordenar. O conjunto começa em zero "
                "e não tem fim. Podemos classificá-los em pares e ímpares e comparar usando "
                ">, < ou =.",
            },
            "topic_id": "natural_numbers",
            "sources": [_src("page-019.jpg"), _src("page-021.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "0️⃣", "title": "Conjunto ℕ", "text": "0, 1, 2, 3… sem último número"},
                    {"icon": "2️⃣", "title": "Pares", "text": "0, 2, 4, 6… terminam em 0, 2, 4, 6 ou 8"},
                    {"icon": "1️⃣", "title": "Ímpares", "text": "1, 3, 5, 7… terminam em 1, 3, 5, 7 ou 9"},
                    {"icon": "↔️", "title": "Consecutivos", "text": "Um ao lado do outro, sem intervalo"},
                ],
            },
            "topic_id": "natural_numbers",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Antecessor e sucessor:",
                "text": "O antecessor vem antes; o sucessor vem depois. O zero não tem antecessor natural.",
            },
            "topic_id": "natural_numbers",
        },
    ]


def _topic_place_value() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "2. Unidade, dezena, centena e milhar"}, "topic_id": "place_value"},
        {
            "type": "paragraph",
            "content": {
                "text": "Cada algarismo de um número tem uma ordem: unidade, dezena, centena, "
                "unidade de milhar, dezena de milhar e centena de milhar. "
                "Agrupamos em classes: unidades simples e milhares.",
            },
            "topic_id": "place_value",
            "sources": [_src("page-031.jpg"), _src("page-021.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Ordens e agrupamentos",
                "headers": ["Ordem", "Agrupamento", "Exemplo em 356 800"],
                "rows": [
                    ["Unidade", "1", "0 unidades"],
                    ["Dezena", "10", "0 dezenas"],
                    ["Centena", "100", "8 centenas"],
                    ["Unidade de milhar", "1 000", "6 milhares"],
                    ["Dezena de milhar", "10 000", "5 dezenas de milhar"],
                    ["Centena de milhar", "100 000", "3 centenas de milhar"],
                ],
            },
            "topic_id": "place_value",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Leitura:",
                "text": "356 800 = trezentos e cinquenta e seis mil e oitocentos.",
            },
            "topic_id": "place_value",
        },
    ]


def _topic_compensation() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "3. Propriedade da compensação"}, "topic_id": "compensation"},
        {
            "type": "paragraph",
            "content": {
                "text": "Na subtração, se você somar (ou subtrair) o mesmo valor ao minuendo e ao subtraendo, "
                "a diferença não muda. Isso facilita o cálculo — como dar R$ 2 a mais na compra "
                "para receber troco em cédula de R$ 20.",
            },
            "topic_id": "compensation",
            "sources": [_src("page-020.jpg"), _src("page-022.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "O que acontece com o resto?",
                "headers": ["Mudança", "Exemplo", "Efeito no resto"],
                "rows": [
                    ["Só minuendo +2", "50+2 − 32 = 20", "Aumenta 2"],
                    ["Só subtraendo +2", "50 − (32+2) = 16", "Diminui 2"],
                    ["Ambos +2", "(50+2) − (32+2) = 18", "Fica igual"],
                    ["Ambos −2", "(50−2) − (32−2) = 18", "Fica igual"],
                ],
            },
            "topic_id": "compensation",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Exemplo da livraria:",
                "text": "Compra R$ 32, paga R$ 50. Cliente dá mais R$ 2 → paga R$ 52. "
                "Preço vira R$ 34. Troco: R$ 52 − R$ 34 = R$ 18 (igual a 50 − 32).",
            },
            "topic_id": "compensation",
        },
    ]


def _topic_bar_charts() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "4. Gráficos de barras"}, "topic_id": "bar_charts"},
        {
            "type": "paragraph",
            "content": {
                "text": "Gráficos de barras mostram quantidades de cada categoria. "
                "Para interpretar: identifique a barra maior, some todas para achar o total "
                "e compare diferenças entre categorias.",
            },
            "topic_id": "bar_charts",
            "sources": [_src("page-017.jpg"), _src("page-018.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "📊", "title": "Eixo", "text": "Categorias e escala de valores"},
                    {"icon": "➕", "title": "Total", "text": "Soma de todas as barras"},
                    {"icon": "🏆", "title": "Maior", "text": "Barra mais longa ou mais alta"},
                ],
            },
            "topic_id": "bar_charts",
        },
        {
            "type": "bar_chart",
            "content": {
                "title": "Materiais recicláveis arrecadados — campanha da escola (kg)",
                "bars": [
                    {"label": "Papel", "value": 2000, "color": "#3b82f6"},
                    {"label": "Plástico", "value": 1500, "color": "#f59e0b"},
                    {"label": "Vidro", "value": 600, "color": "#10b981"},
                    {"label": "Metal", "value": 400, "color": "#8b5cf6"},
                ],
                "caption": "Exemplo: papel (2 000 kg) é o material mais arrecadado. Total: 4 500 kg.",
                "aria_label": "Gráfico de barras com materiais recicláveis arrecadados em quilogramas",
            },
            "topic_id": "bar_charts",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Como resolver:",
                "text": "Some todas as barras (total). Compare valores: diferença = maior − menor.",
            },
            "topic_id": "bar_charts",
        },
    ]


def _topic_parallel_perpendicular() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "5. Segmentos paralelos e perpendiculares"}, "topic_id": "parallel_perpendicular"},
        {
            "type": "paragraph",
            "content": {
                "text": "Dois segmentos são paralelos quando estão na mesma direção e nunca se cruzam. "
                "São concorrentes quando se cruzam em um ponto. "
                "São perpendiculares quando formam ângulos retos (90°) na interseção.",
            },
            "topic_id": "parallel_perpendicular",
            "sources": [_src("page-007.jpg"), _src("page-013.jpg"), _src("page-014.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "═", "title": "Paralelos", "text": "Mesma direção, nunca se encontram"},
                    {"icon": "✕", "title": "Concorrentes", "text": "Cruzam-se em um ponto"},
                    {"icon": "⊾", "title": "Perpendiculares", "text": "Formam 4 ângulos retos"},
                    {"icon": "🏛️", "title": "Exemplo", "text": "Vigas e colunas do MASP"},
                ],
            },
            "topic_id": "parallel_perpendicular",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Ruas de uma cidade:",
                "text": "Avenidas paralelas nunca se cruzam. Uma rua que encontra outra formando "
                "“canto reto” é perpendicular à outra.",
            },
            "topic_id": "parallel_perpendicular",
        },
    ]


def _topic_multiply_powers() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "6. Multiplicação por 10, 100 e 1000"}, "topic_id": "multiply_powers"},
        {
            "type": "paragraph",
            "content": {
                "text": "Multiplicar por 10, 100 ou 1000 desloca os algarismos: "
                "×10 acrescenta um zero; ×100 acrescenta dois; ×1000 acrescenta três. "
                "A ordem dos fatores não altera o produto.",
            },
            "topic_id": "multiply_powers",
            "sources": [_src("page-011.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Regularidade",
                "headers": ["Operação", "Estratégia", "Resultado"],
                "rows": [
                    ["8 × 9 = 72", "Base", "72"],
                    ["8 × 90 = ?", "×10 no 2º fator", "720"],
                    ["8 × 900 = ?", "×100 no 2º fator", "7 200"],
                    ["100 × 20", "Contar zeros", "2 000"],
                ],
            },
            "topic_id": "multiply_powers",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Situação-problema:",
                "text": "100 saquinhos com 20 amêndoas cada → 100 × 20 = 2 000 amêndoas.",
            },
            "topic_id": "multiply_powers",
        },
    ]


def _topic_division() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "7. Divisão exata, resto e potências de 10"}, "topic_id": "division"},
        {
            "type": "paragraph",
            "content": {
                "text": "A divisão pode ser repartição (quantos em cada grupo) ou medida (quantos grupos). "
                "Quando sobra, a divisão é não exata — o resto precisa ser interpretado "
                "(mais uma caixa, mais um ônibus). Dividir por 10, 100 ou 1000 remove zeros.",
            },
            "topic_id": "division",
            "sources": [_src("page-001.jpg"), _src("page-008.jpg"), _src("page-018.jpg"), _src("page-002.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "📦", "title": "Exata", "text": "Resto zero — tudo cabe igualmente"},
                    {"icon": "🚌", "title": "Resto", "text": "Sobra → pode precisar +1 grupo"},
                    {"icon": "📝", "title": "Repertório", "text": "Estimativas: 5×9=45, 3×9=27"},
                    {"icon": "÷10", "title": "Por 10/100", "text": "7 000÷10=700; 7 000÷100=70"},
                ],
            },
            "topic_id": "division",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Exemplo:",
                "text": "74 ÷ 9 → quociente 8, resto 2. "
                "74 ovos em caixas de 9 → 8 caixas cheias e sobram 2 ovos.",
            },
            "topic_id": "division",
        },
    ]


def _topic_angles() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "8. Ângulos: reto, agudo e obtuso"}, "topic_id": "angles"},
        {
            "type": "paragraph",
            "content": {
                "text": "Ângulo reto mede 90° (canto de quadrado). Agudo é menor que 90°. "
                "Obtuso é maior que 90°. Um giro completo vale 360°. "
                "No tangram, o quadrado tem 4 ângulos retos; triângulos têm 45° e 90°.",
            },
            "topic_id": "angles",
            "sources": [_src("page-004.jpg"), _src("page-005.jpg"), _src("page-015.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "⊾", "title": "Reto", "text": "90° — símbolo do quadradinho"},
                    {"icon": "◢", "title": "Agudo", "text": "Menor que 90°"},
                    {"icon": "◣", "title": "Obtuso", "text": "Maior que 90°"},
                    {"icon": "🔄", "title": "Giro", "text": "360° = volta completa"},
                ],
            },
            "topic_id": "angles",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Sentido do giro:",
                "text": "Horário = como o ponteiro do relógio. Anti-horário = sentido contrário.",
            },
            "topic_id": "angles",
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
            {"type": "heading", "content": {"level": 3, "text": "1. Números naturais"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "2/4", "title": "Pares/ímpares", "text": "Último algarismo define"},
                        {"icon": "↔️", "title": "Antec./suc.", "text": "Zero não tem antecessor"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. Ordens e classes"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "1000", "title": "Classes", "text": "Unidades · milhares"},
                        {"icon": "🔤", "title": "Leitura", "text": "356 800 = trezentos e cinquenta e seis mil e oitocentos"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Compensação"}},
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Regra:",
                    "text": "Mesma mudança no minuendo e no subtraendo → resto igual.",
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Gráficos"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "➕", "title": "Total", "text": "Soma das barras"},
                        {"icon": "📊", "title": "Comparar", "text": "Maior − menor = diferença"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Segmentos"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["", "Paralelos", "Perpendiculares"],
                    "rows": [
                        ["Definição", "Nunca se cruzam", "Formam ângulos retos"],
                        ["Exemplo", "Trilhos de trem", "Canto de parede"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "6. × por 10/100/1000"}},
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Atalho:",
                    "text": "Acrescente zeros ao fator ou desloque algarismos.",
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "7. Divisão"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "➗", "title": "Resto", "text": "Interpretar na situação"},
                        {"icon": "÷100", "title": "Por 100", "text": "Remove dois zeros do dividendo"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "8. Ângulos"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "90°", "title": "Reto", "text": "Canto de quadrado"},
                        {"icon": "45°", "title": "Tangram", "text": "Triângulos têm 45° e 90°"},
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "Quando sobra resto em transporte ou embalagem, "
                    "geralmente é preciso mais um ônibus ou caixa — não ignore o resto!",
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
                "topic": "natural_numbers",
                "question": "O sucessor imediato de 406 400 é:",
                "options": ["406 399", "406 401", "406 410", "406 500"],
                "correct_answer": 1,
                "explanation": "Sucessor = número que vem depois. 406 400 + 1 = 406 401.",
                "difficulty": "basic",
                "source_assets": sa("page-021.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-002",
                "type": "multiple_choice",
                "topic": "natural_numbers",
                "question": (
                    "Leia as afirmativas sobre números naturais:\n"
                    "I. O zero é um número par.\n"
                    "II. Todo número ímpar termina em 1, 3, 5, 7 ou 9.\n"
                    "III. O número 1 não tem antecessor natural.\n"
                    "IV. Números consecutivos têm diferença 2.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e III", "II e IV", "I e IV", "II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e III corretas. Consecutivos diferem de 1, não de 2 (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-019.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-003",
                "type": "multiple_choice",
                "topic": "place_value",
                "question": "No número 356 800, o algarismo 5 está na ordem das:",
                "options": ["Unidades", "Centenas", "Dezenas de milhar", "Centenas de milhar"],
                "correct_answer": 2,
                "explanation": "356 800 → o 5 está na casa das dezenas de milhar (50 000).",
                "difficulty": "basic",
                "source_assets": sa("page-031.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-004",
                "type": "multiple_choice",
                "topic": "place_value",
                "question": "Compare: 89 989 ___ 89 990. O sinal correto é:",
                "options": [">", "<", "=", "≥"],
                "correct_answer": 1,
                "explanation": "89 989 é menor que 89 990 (diferença de 1 na unidade).",
                "difficulty": "basic",
                "source_assets": sa("page-021.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-005",
                "type": "multiple_choice",
                "topic": "compensation",
                "question": (
                    "Na livraria, a compra custa R$ 32 e o cliente paga R$ 50. "
                    "Se ambos recebem R$ 2 a mais (preço vira R$ 34 e pagamento R$ 52), "
                    "o troco será:"
                ),
                "options": ["R$ 16", "R$ 18", "R$ 20", "R$ 22"],
                "correct_answer": 1,
                "explanation": "Compensação: 52 − 34 = 18. Igual a 50 − 32 = 18.",
                "difficulty": "basic",
                "source_assets": sa("page-022.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-006",
                "type": "multiple_choice",
                "topic": "compensation",
                "question": (
                    "Leia as afirmativas sobre a propriedade da compensação:\n"
                    "I. Somar 5 ao minuendo e ao subtraendo mantém o resto.\n"
                    "II. Somar 5 só ao minuendo aumenta o resto em 5.\n"
                    "III. Subtrair 3 dos dois termos também mantém o resto.\n"
                    "IV. Somar 5 só ao subtraendo aumenta o resto em 5.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I e III", "III e IV"],
                "correct_answer": 2,
                "explanation": "I e III corretas. Só minuendo +5 → resto +5 (II errada). Só subtraendo +5 → resto −5 (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-020.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-007",
                "type": "multiple_choice",
                "topic": "bar_charts",
                "question": (
                    "Observe o gráfico de livros doados à biblioteca da escola. "
                    "Quantos livros a mais foram doados de Aventura do que de Biografia?"
                ),
                "visual": {
                    "type": "bar_chart",
                    "content": {
                        "title": "Livros doados à biblioteca — semana da leitura",
                        "bars": [
                            {"label": "Aventura", "value": 48, "color": "#ef4444"},
                            {"label": "Fantasia", "value": 36, "color": "#3b82f6"},
                            {"label": "HQ", "value": 24, "color": "#f59e0b"},
                            {"label": "Biografia", "value": 12, "color": "#10b981"},
                        ],
                        "aria_label": "Gráfico de barras com livros doados por gênero literário",
                    },
                },
                "options": ["12 livros", "24 livros", "36 livros", "48 livros"],
                "correct_answer": 2,
                "explanation": "Aventura: 48. Biografia: 12. Diferença: 48 − 12 = 36 livros.",
                "difficulty": "intermediate",
                "source_assets": sa("page-017.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-008",
                "type": "multiple_choice",
                "topic": "parallel_perpendicular",
                "question": (
                    "Duas ruas se cruzam formando quatro cantos retos (como um +). "
                    "Essas ruas são:"
                ),
                "options": [
                    "Paralelas",
                    "Perpendiculares",
                    "Concorrentes sem serem perpendiculares",
                    "Coincidentes",
                ],
                "correct_answer": 1,
                "explanation": "Cantos retos (90°) indicam segmentos perpendiculares.",
                "difficulty": "basic",
                "source_assets": sa("page-014.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-009",
                "type": "multiple_choice",
                "topic": "parallel_perpendicular",
                "question": (
                    "Leia as afirmativas sobre posição de segmentos:\n"
                    "I. Segmentos paralelos nunca se cruzam.\n"
                    "II. Segmentos perpendiculares formam ângulos retos.\n"
                    "III. Todo par de segmentos concorrentes é perpendicular.\n"
                    "IV. Trilhos de trem são um exemplo de segmentos paralelos.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. Concorrentes cruzam-se, mas nem sempre formam 90° (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-007.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-010",
                "type": "multiple_choice",
                "topic": "multiply_powers",
                "question": "Sabendo que 8 × 9 = 72, o produto 8 × 900 é:",
                "options": ["720", "7 200", "72 000", "702"],
                "correct_answer": 1,
                "explanation": "8 × 900 = 8 × 9 × 100 = 72 × 100 = 7 200.",
                "difficulty": "basic",
                "source_assets": sa("page-011.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-011",
                "type": "multiple_choice",
                "topic": "multiply_powers",
                "question": (
                    "Leia as afirmativas sobre multiplicação por 10, 100 e 1000:\n"
                    "I. 14 × 60 = 840 porque 14 × 6 = 84 e há um zero.\n"
                    "II. 9 × 800 = 7 200.\n"
                    "III. Multiplicar por 100 remove dois zeros do fator.\n"
                    "IV. 900 × 5 = 5 × 900 (comutativa).\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e IV", "I e III", "II e III", "III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e IV corretas. Multiplicar por 100 acrescenta zeros, não remove (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-011.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-012",
                "type": "multiple_choice",
                "topic": "division",
                "question": (
                    "Paula embalou 74 sacos de doces em caixas com 8 sacos cada. "
                    "Quantas caixas ficaram completamente cheias e quantos sacos sobraram?"
                ),
                "options": [
                    "9 caixas cheias e sobram 2 sacos",
                    "8 caixas cheias e sobram 10 sacos",
                    "9 caixas cheias e nenhum saco sobra",
                    "10 caixas cheias e sobram 6 sacos",
                ],
                "correct_answer": 0,
                "explanation": "74 ÷ 8 = 9 com resto 2. Nove caixas cheias; sobram 2 sacos.",
                "difficulty": "basic",
                "source_assets": sa("page-001.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-013",
                "type": "multiple_choice",
                "topic": "division",
                "question": (
                    "112 alunos, 3 professores e 3 monitores vão ao teatro de ônibus de 40 lugares. "
                    "Quantos ônibus são necessários?"
                ),
                "options": ["2", "3", "4", "118"],
                "correct_answer": 1,
                "explanation": "Total: 112+3+3=118. 118÷40=2 resto 38 → precisam de 3 ônibus.",
                "difficulty": "intermediate",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-014",
                "type": "multiple_choice",
                "topic": "division",
                "question": (
                    "Leia as afirmativas sobre divisão:\n"
                    "I. 48 ÷ 6 = 8 é uma divisão exata.\n"
                    "II. Na divisão 74 ÷ 9 o quociente é 8 e o resto é 2.\n"
                    "III. 7 000 ÷ 100 = 700.\n"
                    "IV. Dividir por 10 sempre dá resto zero.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e III", "II e IV", "I e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e III corretas. 7÷10=0 resto 7 — dividir por 10 nem sempre é exato (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-025.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-015",
                "type": "multiple_choice",
                "topic": "division",
                "question": "O quociente de 4 500 ÷ 100 é:",
                "options": ["45", "450", "4 500", "450 000"],
                "correct_answer": 0,
                "explanation": "Dividir por 100 remove dois zeros: 4 500 → 45.",
                "difficulty": "basic",
                "source_assets": sa("page-002.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat-pe-016",
                "type": "multiple_choice",
                "topic": "angles",
                "question": (
                    "Leia as afirmativas sobre ângulos:\n"
                    "I. Um ângulo reto mede 90°.\n"
                    "II. Um giro completo mede 360°.\n"
                    "III. Todo ângulo agudo mede exatamente 45°.\n"
                    "IV. Um ângulo obtuso é maior que 90°.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Agudo é menor que 90°, não necessariamente 45° (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-015.jpg"),
                "section": "final_quiz",
            },
            *_challenge_exercises(sa),
        ],
    }


def _challenge_exercises(sa) -> list:
    """10 desafios avançados — adaptados da apostila Benjamin (imagens_matematica_benjamin)."""
    return [
            {
                "id": "mat-des-001",
                "type": "multiple_choice",
                "topic": "natural_numbers",
                "question": (
                    "Entre 9 998 e 10 005, quantos números consecutivos são pares?"
                ),
                "options": ["2", "3", "4", "6"],
                "correct_answer": 1,
                "explanation": "Consecutivos: 9 999, 10 000, 10 001, 10 002, 10 003, 10 004, 10 005. Pares: 10 000, 10 002 e 10 004 → 3 números.",
                "difficulty": "advanced",
                "source_assets": sa("page-021.jpg"),
                "section": "desafios",
            },
            {
                "id": "mat-des-002",
                "type": "multiple_choice",
                "topic": "compensation",
                "question": (
                    "Usando a propriedade da compensação, calcule 9 000 − 452 "
                    "(some 48 ao minuendo e ao subtraendo):"
                ),
                "options": ["8 548", "8 448", "8 648", "9 548"],
                "correct_answer": 0,
                "explanation": "9 000+48=9 048 e 452+48=500 → 9 048−500=8 548.",
                "difficulty": "advanced",
                "source_assets": sa("page-017.jpg"),
                "section": "desafios",
            },
            {
                "id": "mat-des-003",
                "type": "multiple_choice",
                "topic": "compensation",
                "question": (
                    "A biblioteca da escola tem 3 018 livros no acervo. "
                    "Até hoje, 1 922 estão emprestados. Quantos livros estão disponíveis para empréstimo?"
                ),
                "options": ["1 096", "1 196", "1 896", "4 940"],
                "correct_answer": 0,
                "explanation": "3 018 − 1 922 = 1 096 livros disponíveis (como no exercício da professora Augusta).",
                "difficulty": "advanced",
                "source_assets": sa("page-034.jpg"),
                "section": "desafios",
            },
            {
                "id": "mat-des-004",
                "type": "multiple_choice",
                "topic": "bar_charts",
                "question": (
                    "Observe o gráfico da campanha de reciclagem da escola de Mayra (2021). "
                    "Quantos quilogramas a mais de papel foram arrecadados do que de vidro?"
                ),
                "visual": {
                    "type": "bar_chart",
                    "content": {
                        "title": "Materiais recicláveis arrecadados — campanha 2021 (kg)",
                        "bars": [
                            {"label": "Papel", "value": 3200, "color": "#3b82f6"},
                            {"label": "Plástico", "value": 1800, "color": "#f59e0b"},
                            {"label": "Vidro", "value": 950, "color": "#10b981"},
                            {"label": "Metal", "value": 650, "color": "#8b5cf6"},
                        ],
                        "aria_label": "Gráfico de barras com materiais recicláveis da campanha escolar",
                    },
                },
                "options": ["2 250 kg", "1 850 kg", "950 kg", "650 kg"],
                "correct_answer": 0,
                "explanation": "Papel: 3 200 kg. Vidro: 950 kg. Diferença: 3 200 − 950 = 2 250 kg.",
                "difficulty": "advanced",
                "source_assets": sa("page-017.jpg"),
                "section": "desafios",
            },
            {
                "id": "mat-des-005",
                "type": "multiple_choice",
                "topic": "division",
                "question": (
                    "Resolva 548 ÷ 8 com estimativas em grupos maiores. "
                    "Quantas caixas completamente cheias e quantos sobram?"
                ),
                "options": [
                    "68 caixas cheias e sobram 4",
                    "68 caixas cheias e sobram 6",
                    "69 caixas cheias e sobra 1",
                    "67 caixas cheias e sobram 12",
                ],
                "correct_answer": 0,
                "explanation": "548 ÷ 8 = 68 com resto 4 (68×8=544; 548−544=4).",
                "difficulty": "advanced",
                "source_assets": sa("page-024.jpg"),
                "section": "desafios",
            },
            {
                "id": "mat-des-006",
                "type": "multiple_choice",
                "topic": "division",
                "question": (
                    "Resolva 197 ÷ 17 usando o repertório de estimativas. "
                    "Qual é o quociente e o resto?"
                ),
                "options": [
                    "Quociente 11 e resto 10",
                    "Quociente 12 e resto 0",
                    "Quociente 10 e resto 27",
                    "Quociente 11 e resto 0",
                ],
                "correct_answer": 0,
                "explanation": "17×11=187. 197−187=10 → quociente 11, resto 10.",
                "difficulty": "advanced",
                "source_assets": sa("page-016.jpg"),
                "section": "desafios",
            },
            {
                "id": "mat-des-007",
                "type": "multiple_choice",
                "topic": "division",
                "question": (
                    "Guilherme precisa ler um livro de 57 páginas em 6 dias. "
                    "Ele pretende ler 9 páginas por dia. Ele conseguirá terminar no prazo?"
                ),
                "options": [
                    "Não — faltarão 3 páginas após 6 dias",
                    "Sim — terminará exatamente no 6º dia",
                    "Sim — sobrará 1 dia",
                    "Não — faltarão 9 páginas",
                ],
                "correct_answer": 0,
                "explanation": "6×9=54 páginas lidas. 57−54=3 páginas que faltam — não termina no prazo.",
                "difficulty": "advanced",
                "source_assets": sa("page-001.jpg"),
                "section": "desafios",
            },
            {
                "id": "mat-des-008",
                "type": "multiple_choice",
                "topic": "multiply_powers",
                "question": (
                    "Luan serviu 10 embalagens de 2 000 mL de suco de maçã. "
                    "Quantos litros de suco foram servidos?"
                ),
                "options": ["2 L", "20 L", "200 L", "2 000 L"],
                "correct_answer": 1,
                "explanation": "10×2 000=20 000 mL. Como 1 L=1 000 mL → 20 000÷1 000=20 litros.",
                "difficulty": "advanced",
                "source_assets": sa("page-012.jpg"),
                "section": "desafios",
            },
            {
                "id": "mat-des-009",
                "type": "multiple_choice",
                "topic": "division",
                "question": (
                    "Uma granja produziu 252 ovos. Se forem embalados em caixas de 6 unidades, "
                    "serão necessárias 42 caixas. E se forem embalados em caixas de 12 unidades, "
                    "quantas caixas a menos serão necessárias?"
                ),
                "options": ["21 caixas a menos", "42 caixas a menos", "12 caixas a menos", "6 caixas a menos"],
                "correct_answer": 0,
                "explanation": "252÷12=21 caixas. 42−21=21 caixas a menos quando se usa caixa de 12.",
                "difficulty": "advanced",
                "source_assets": sa("page-003.jpg"),
                "section": "desafios",
            },
            {
                "id": "mat-des-010",
                "type": "multiple_choice",
                "topic": "angles",
                "question": (
                    "Um giro completo mede 360°. Quatro ângulos retos cabem exatamente "
                    "num giro completo. Quanto mede um meio giro?"
                ),
                "options": ["90°", "180°", "270°", "360°"],
                "correct_answer": 1,
                "explanation": "Meio giro = metade de 360° = 180°.",
                "difficulty": "advanced",
                "source_assets": sa("page-042.jpg"),
                "section": "desafios",
            },
    ]
