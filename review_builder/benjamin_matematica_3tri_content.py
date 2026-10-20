"""Conteúdo pedagógico da revisão Benjamin — Matemática PE 3º trimestre (Módulos 19–23)."""

from __future__ import annotations

REVIEW_ID = "benjamin-pe-matematica-3tri"
ASSET_PREFIX = "assets/benjamin_pe_matematica_3_tri"


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
        "title": "Revisão de Matemática — PE 3º Trimestre",
        "subtitle": "Benjamin · 4º ano · Módulos 19, 20, 21, 22 e 23",
        "language": "pt-BR",
        "discipline": "Matemática",
        "grade": "4º ano",
        "metadata": {
            "student_name": "Benjamin",
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
                    "text": "Igualdade e operações inversas, regularidades da tabuada, quadriláteros "
                    "(trapézios, paralelogramos, retângulos e losangos) e números decimais no sistema "
                    "monetário — Módulos 19 a 23. Reserve cerca de 60 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "⚖️", "title": "Igualdade", "text": "Mesma mudança nos dois lados"},
                        {"icon": "🔄", "title": "Inversas", "text": "Adição ↔ subtração"},
                        {"icon": "✖️", "title": "Tabuada", "text": "Comutativa · dobrar fatores"},
                        {"icon": "⬡", "title": "Quadriláteros", "text": "4 lados · classificação"},
                        {"icon": "▱", "title": "Trapézio", "text": "Um par de lados paralelos"},
                        {"icon": "▭", "title": "Retângulo", "text": "4 ângulos retos"},
                        {"icon": "◆", "title": "Losango", "text": "4 lados iguais"},
                        {"icon": "💰", "title": "Decimais", "text": "Décimos · centésimos · R$"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 19 — Relações entre as operações",
                        "Módulo 20 — Regularidades na tabuada",
                        "Módulo 21 — Quadriláteros e trapézios",
                        "Módulo 22 — Retângulos e losangos",
                        "Módulo 23 — Números decimais e dinheiro",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Leia os cards e a reta numérica.",
                            "tip": "Desenhe um trapézio e um retângulo no caderno e nomeie os lados paralelos.",
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
                            "description": "Questões no estilo Teste e Em casa do caderno.",
                            "tip": "Em decimais, alinhe a vírgula antes de comparar.",
                        },
                        {
                            "title": "Encare os Desafios",
                            "panel": "desafios",
                            "panel_label": "Desafios",
                            "description": "Problemas mais exigentes — balanças, tabuada e dinheiro.",
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
            *_topic_equality(),
            *_topic_inverse(),
            *_topic_tabuada(),
            *_topic_quadrilaterals(),
            *_topic_trapezoids(),
            *_topic_rect_rhombus(),
            *_topic_decimals(),
            *_topic_money(),
        ],
    }


def _topic_equality() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "1. Igualdade e balança"},
            "topic_id": "equality_balance",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Uma balança de dois pratos fica equilibrada quando os dois lados têm a mesma "
                "massa. Em matemática, uma igualdade funciona igual: se você fizer a mesma operação "
                "nos dois membros (somar, subtrair, multiplicar ou dividir pelo mesmo número), "
                "a igualdade continua verdadeira.",
            },
            "topic_id": "equality_balance",
            "sources": [_src("page-060.jpg"), _src("page-064.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "➕", "title": "Somar igual", "text": "47 + 36 = 83 → +7 nos dois lados"},
                    {"icon": "➖", "title": "Subtrair igual", "text": "58 − 21 = 37 → −10 nos dois lados"},
                    {"icon": "⚖️", "title": "Balança", "text": "Dobrar objetos dos dois pratos mantém equilíbrio"},
                    {"icon": "✓", "title": "Membro", "text": "Esquerda e direita do sinal ="},
                ],
            },
            "topic_id": "equality_balance",
        },
    ]


def _topic_inverse() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "2. Operações inversas"},
            "topic_id": "inverse_operations",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Adição e subtração são operações inversas: se 8 + 7 = 15, então 15 − 7 = 8. "
                "Para achar um número que falta, use a operação contrária. "
                "Em problemas com esquema (? + 38 = 92), subtraia 38 de 92 para achar o número pensado.",
            },
            "topic_id": "inverse_operations",
            "sources": [_src("page-055.jpg"), _src("page-060.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Completar sentenças",
                "headers": ["Sentença", "Operação inversa", "Resposta"],
                "rows": [
                    ["45 + ? = 72", "72 − 45", "27"],
                    ["? − 83 = 37", "37 + 83", "120"],
                    ["? + 36 = 121", "121 − 36", "85"],
                ],
            },
            "topic_id": "inverse_operations",
        },
    ]


def _topic_tabuada() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "3. Regularidades da tabuada"},
            "topic_id": "multiplication_table",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "No tabuleiro da tabuada (2 a 9), a diagonal separa produtos iguais: "
                "3 × 4 = 4 × 3 (propriedade comutativa). As tabuadas do 1 e do 10 são fáceis "
                "e podem ser eliminadas do quadro. Dobrar um fator dobra o produto: "
                "2 × 7 = 14 → 4 × 7 = 28 → 8 × 7 = 56.",
            },
            "topic_id": "multiplication_table",
            "sources": [_src("page-045.jpg"), _src("page-050.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "↔️", "title": "Comutativa", "text": "a × b = b × a"},
                    {"icon": "2️⃣", "title": "Tabuada do 2", "text": "Números pares: 2, 4, 6…"},
                    {"icon": "×2", "title": "Dobrar", "text": "Fator ×2 → produto ×2"},
                    {"icon": "×3", "title": "Triplicar", "text": "3×6=18 → 6×6=36 → 9×6=54"},
                ],
            },
            "topic_id": "multiplication_table",
        },
    ]


def _topic_quadrilaterals() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "4. Quadriláteros e polígonos"},
            "topic_id": "quadrilaterals",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Quadrilátero é polígono de 4 lados. Classificamos pelo paralelismo: "
                "lados opostos paralelos (paralelogramo e trapézio) ou nem todos paralelos "
                "(quadrilátero convexo irregular). Todo trapézio é quadrilátero; "
                "todo quadrilátero é polígono.",
            },
            "topic_id": "quadrilaterals",
            "sources": [_src("page-040.jpg"), _src("page-038.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Figura", "Lados", "Paralelos?"],
                "rows": [
                    ["Triângulo", "3", "Não é quadrilátero"],
                    ["Trapézio", "4", "Um par de opostos"],
                    ["Paralelogramo", "4", "Dois pares de opostos"],
                    ["Pentágono", "5", "Polígono, não quadrilátero"],
                ],
            },
            "topic_id": "quadrilaterals",
        },
    ]


def _topic_trapezoids() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "5. Trapézios e paralelogramos"},
            "topic_id": "trapezoids_parallelograms",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Trapézio tem exatamente um par de lados paralelos (bases). "
                "Paralelogramo tem dois pares de lados opostos paralelos e congruentes. "
                "Trapézio com dois ângulos retos é trapézio retângulo. "
                "Use T = trapézio, P = paralelogramo, R = retângulo nas atividades do caderno.",
            },
            "topic_id": "trapezoids_parallelograms",
            "sources": [_src("page-035.jpg"), _src("page-015.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Hierarquia:",
                "text": "Todo retângulo é paralelogramo. Nem todo paralelogramo é retângulo. "
                "Trapézio não é paralelogramo (só um par paralelo).",
            },
            "topic_id": "trapezoids_parallelograms",
        },
    ]


def _topic_rect_rhombus() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "6. Retângulos, losangos e quadrados"},
            "topic_id": "rectangles_rhombuses",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Retângulo: 4 ângulos retos; lados opostos iguais. Losango: 4 lados de mesma medida. "
                "Quadrado: retângulo e losango ao mesmo tempo (4 lados iguais e 4 ângulos retos). "
                "Na arte de Mondrian, os quadriláteros da grade têm todos ângulos retos.",
            },
            "topic_id": "rectangles_rhombuses",
            "sources": [_src("page-030.jpg"), _src("page-025.jpg"), _src("page-020.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "▭", "title": "Retângulo", "text": "4 retos · lados opostos iguais"},
                    {"icon": "◆", "title": "Losango", "text": "4 lados iguais · ângulos variados"},
                    {"icon": "⬜", "title": "Quadrado", "text": "Losango retângulo"},
                    {"icon": "🎨", "title": "Mondrian", "text": "Grade com retângulos coloridos"},
                ],
            },
            "topic_id": "rectangles_rhombuses",
        },
    ]


def _topic_decimals() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "7. Números decimais"},
            "topic_id": "decimals_intro",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Números decimais aparecem na balança (66,6 kg), no termômetro (36,3 °C) "
                "e nos preços (R$ 9,99). A vírgula separa a parte inteira da parte decimal. "
                "Décimo = 0,1 (décima parte da unidade). Centésimo = 0,01. "
                "Dividir por 10 desloca o algarismo uma casa à direita (208 ÷ 10 = 20,8).",
            },
            "topic_id": "decimals_intro",
            "sources": [_src("page-012.jpg"), _src("page-007.jpg"), _src("page-010.jpg")],
        },
        {
            "type": "line_chart",
            "content": {
                "title": "Reta numérica de 0 a 1 (cada intervalo = 0,1)",
                "points": [
                    {"label": "0", "value": 0},
                    {"label": "0,1", "value": 0.1},
                    {"label": "0,2", "value": 0.2},
                    {"label": "0,3", "value": 0.3},
                    {"label": "0,4", "value": 0.4},
                    {"label": "0,5", "value": 0.5},
                    {"label": "0,6", "value": 0.6},
                    {"label": "0,7", "value": 0.7},
                    {"label": "0,8", "value": 0.8},
                    {"label": "0,9", "value": 0.9},
                    {"label": "1", "value": 1},
                ],
                "y_axis_label": "Posição na reta",
                "x_axis_label": "Décimos",
            },
            "topic_id": "decimals_intro",
            "sources": [_src("page-010.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Comparar decimais:",
                "text": "3,5 > 3,05 porque 5 décimos > zero décimos na mesma unidade. "
                "0,77 > 0,75 (compare centésimos).",
            },
            "topic_id": "decimals_intro",
        },
    ]


def _topic_money() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "8. Sistema monetário brasileiro"},
            "topic_id": "money_decimals",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Escrevemos valores com R$ e vírgula: R$ 42,75 = quarenta e dois reais e "
                "setenta e cinco centavos. A parte após a vírgula são centavos (centésimos do real). "
                "R$ 2,70 é o mesmo que R$ 2,7 (zero centésimo à direita). "
                "Em postos de gasolina aparecem três casas decimais (milésimos) — diferente do dinheiro comum.",
            },
            "topic_id": "money_decimals",
            "sources": [_src("page-003.jpg"), _src("page-004.jpg"), _src("page-001.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "💵", "title": "Cédulas", "text": "Reais antes da vírgula"},
                    {"icon": "🪙", "title": "Moedas", "text": "Centavos · 100 centavos = 1 real"},
                    {"icon": "0,01", "title": "Centésimo", "text": "1 : 100 = 0,01"},
                    {"icon": "🛒", "title": "Troco", "text": "Pagar − preço = troco"},
                ],
            },
            "topic_id": "money_decimals",
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
                    "text": "Revise cada tópico — igualdade, tabuada, quadriláteros e decimais.",
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "1. Igualdade"}},
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Regra:",
                    "text": "Mesma transformação nos dois membros → igualdade mantida.",
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. Inversas"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "+/−", "title": "Adição", "text": "Achar ? em ? + a = b → b − a"},
                        {"icon": "−/+", "title": "Subtração", "text": "Achar ? em ? − a = b → b + a"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Tabuada"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "↔️", "title": "Comutativa", "text": "Metade do tabuleiro repete"},
                        {"icon": "×2", "title": "Dobrar fator", "text": "Dobra o produto"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Quadriláteros"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["Nome", "Paralelos"],
                    "rows": [
                        ["Trapézio", "1 par"],
                        ["Paralelogramo", "2 pares"],
                        ["Retângulo", "2 pares + 4 retos"],
                        ["Losango", "2 pares + 4 lados iguais"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Quadrado"}},
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Definição:",
                    "text": "Losango que também é retângulo = quadrado.",
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "6. Decimais"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "0,1", "title": "Décimo", "text": "10 décimos = 1 unidade"},
                        {"icon": "0,01", "title": "Centésimo", "text": "100 centésimos = 1 unidade"},
                        {"icon": "0,5", "title": "Metade", "text": "Metade de 1 = 0,5"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "7. Dinheiro"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "R$", "title": "Escrita", "text": "Reais, vírgula, centavos"},
                        {"icon": "🪙", "title": "Moedas", "text": "Some cédulas + moedas para total"},
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "R$ 2,7 e R$ 2,70 representam o mesmo valor. "
                    "Compare decimais casa a casa, da esquerda para a direita.",
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
                "id": "mat3-pe-001",
                "type": "multiple_choice",
                "topic": "equality_balance",
                "question": (
                    "Na igualdade 52 + 26 = 78, foi feito 52 + 26 − 5 = 78 − 5. "
                    "O que foi feito para manter a igualdade?"
                ),
                "options": [
                    "Subtrair 5 só do primeiro membro",
                    "Subtrair 5 dos dois membros",
                    "Somar 5 só ao segundo membro",
                    "Dividir os dois membros por 5",
                ],
                "correct_answer": 1,
                "explanation": "A mesma subtração (−5) foi aplicada em ambos os lados.",
                "difficulty": "basic",
                "source_assets": sa("page-060.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-002",
                "type": "multiple_choice",
                "topic": "equality_balance",
                "question": (
                    "Leia as afirmativas sobre igualdades:\n"
                    "I. Se adicionar 10 ao 1º membro, deve adicionar 10 ao 2º para manter a igualdade.\n"
                    "II. Só o 1º membro pode ser transformado.\n"
                    "III. Subtrair 20 dos dois membros mantém a igualdade.\n"
                    "IV. Multiplicar só um membro por 2 mantém a igualdade.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, II e III", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I e III corretas. Transformação deve ser igual nos dois lados (II e IV erradas).",
                "difficulty": "intermediate",
                "source_assets": sa("page-060.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-003",
                "type": "multiple_choice",
                "topic": "inverse_operations",
                "question": "Complete: 45 + ? = 72. O número que falta é:",
                "options": ["17", "27", "37", "117"],
                "correct_answer": 1,
                "explanation": "Operação inversa: 72 − 45 = 27.",
                "difficulty": "basic",
                "source_assets": sa("page-055.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-004",
                "type": "multiple_choice",
                "topic": "inverse_operations",
                "question": (
                    "Caio perdeu 25 kg e ficou com 118 kg. Quantos quilos ele tinha antes? "
                    "A operação correta é:"
                ),
                "options": ["118 − 25", "118 + 25", "118 × 25", "25 − 118"],
                "correct_answer": 1,
                "explanation": "Perdeu peso → antes era maior: 118 + 25 = 143 kg.",
                "difficulty": "basic",
                "source_assets": sa("page-055.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-005",
                "type": "multiple_choice",
                "topic": "multiplication_table",
                "question": "Sabendo que 2 × 7 = 14, o produto 8 × 7 é:",
                "options": ["28", "42", "56", "70"],
                "correct_answer": 2,
                "explanation": "8 é o quadruplo de 2 → 14 × 4 = 56.",
                "difficulty": "basic",
                "source_assets": sa("page-050.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-006",
                "type": "multiple_choice",
                "topic": "multiplication_table",
                "question": (
                    "Leia as afirmativas sobre a tabuada:\n"
                    "I. 3 × 4 = 4 × 3 por causa da comutativa.\n"
                    "II. Dobrar um fator dobra o produto.\n"
                    "III. A tabuada do 10 só muda o número de zeros.\n"
                    "IV. 9 × 6 = 54 e 6 × 9 = 45.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e III", "II, III e IV", "I e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e III corretas. 6 × 9 também é 54, não 45 (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-045.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-007",
                "type": "multiple_choice",
                "topic": "quadrilaterals",
                "question": (
                    "Um polígono de 4 lados, com exatamente um par de lados opostos paralelos, é:"
                ),
                "options": ["Triângulo", "Trapézio", "Pentágono", "Hexágono"],
                "correct_answer": 1,
                "explanation": "Quadrilátero com um par de lados paralelos = trapézio.",
                "difficulty": "basic",
                "source_assets": sa("page-038.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-008",
                "type": "multiple_choice",
                "topic": "trapezoids_parallelograms",
                "question": (
                    "Leia as afirmativas:\n"
                    "I. Todo trapézio é quadrilátero.\n"
                    "II. Todo paralelogramo é trapézio.\n"
                    "III. Trapézio tem dois pares de lados paralelos.\n"
                    "IV. Paralelogramo tem lados opostos paralelos.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "II e III", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I e IV corretas. Paralelogramo não é trapézio (II errada). Trapézio: 1 par (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-035.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-009",
                "type": "multiple_choice",
                "topic": "rectangles_rhombuses",
                "question": "Existem losangos que são retângulos. Como são chamados?",
                "options": ["Trapézios", "Quadrados", "Pentágonos", "Triângulos"],
                "correct_answer": 1,
                "explanation": "Quadrado tem 4 lados iguais (losango) e 4 ângulos retos (retângulo).",
                "difficulty": "basic",
                "source_assets": sa("page-020.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-010",
                "type": "multiple_choice",
                "topic": "rectangles_rhombuses",
                "question": (
                    "Leia as afirmativas sobre retângulo e losango:\n"
                    "I. Retângulo tem 4 ângulos retos.\n"
                    "II. Losango tem 4 lados de mesma medida.\n"
                    "III. Todo retângulo é quadrado.\n"
                    "IV. Quadrado é losango e retângulo ao mesmo tempo.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e IV", "II, III e IV", "I e III", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e IV corretas. Retângulo com lados diferentes não é quadrado (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-025.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-011",
                "type": "multiple_choice",
                "topic": "decimals_intro",
                "question": "Quantos décimos formam uma unidade inteira?",
                "options": ["2", "5", "10", "100"],
                "correct_answer": 2,
                "explanation": "0,1 + 0,1 … dez vezes = 1. Dez décimos = 1 unidade.",
                "difficulty": "basic",
                "source_assets": sa("page-010.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-012",
                "type": "multiple_choice",
                "topic": "decimals_intro",
                "question": (
                    "Observe o gráfico de linhas (notas de ciências — 4 bimestres). "
                    "Em qual bimestre a nota foi 8,4?"
                ),
                "visual": {
                    "type": "line_chart",
                    "content": {
                        "title": "Nota de Ciências de Luísa — por bimestre",
                        "points": [
                            {"label": "1º", "value": 7.2},
                            {"label": "2º", "value": 8.4},
                            {"label": "3º", "value": 7.9},
                            {"label": "4º", "value": 9.1},
                        ],
                        "y_axis_label": "Nota",
                        "x_axis_label": "Bimestre",
                    },
                },
                "options": ["1º bimestre", "2º bimestre", "3º bimestre", "4º bimestre"],
                "correct_answer": 1,
                "explanation": "O ponto mais alto no 2º bimestre marca 8,4.",
                "difficulty": "intermediate",
                "source_assets": sa("page-012.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-013",
                "type": "multiple_choice",
                "topic": "decimals_intro",
                "question": "Entre 3,5 e 3,05, o maior número é:",
                "options": ["3,05", "3,5", "São iguais", "3,50 e 3,5 são diferentes"],
                "correct_answer": 1,
                "explanation": "3,5 = 3,50 → cinco décimos; 3,05 tem zero décimos e cinco centésimos.",
                "difficulty": "basic",
                "source_assets": sa("page-002.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-014",
                "type": "multiple_choice",
                "topic": "money_decimals",
                "question": "R$ 2,70 representa o mesmo valor que:",
                "options": ["R$ 2,07", "R$ 27,0", "R$ 2,7", "R$ 0,27"],
                "correct_answer": 2,
                "explanation": "Zero centésimo à direita não muda o valor: 2,70 = 2,7.",
                "difficulty": "basic",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-015",
                "type": "multiple_choice",
                "topic": "money_decimals",
                "question": (
                    "Maria tem três cédulas de R$ 10, uma de R$ 50, dez moedas de R$ 0,10 "
                    "e quatro moedas de R$ 0,50. Qual é o total?"
                ),
                "options": ["R$ 81,00", "R$ 83,00", "R$ 85,00", "R$ 93,00"],
                "correct_answer": 1,
                "explanation": "50 + 30 = 80; moedas: 1,00 + 2,00 = 3,00 → R$ 83,00.",
                "difficulty": "intermediate",
                "source_assets": sa("page-001.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-016",
                "type": "multiple_choice",
                "topic": "money_decimals",
                "question": (
                    "Leia as afirmativas sobre o Real:\n"
                    "I. Centésimo do real vale R$ 0,01.\n"
                    "II. R$ 0,70 são setenta centavos.\n"
                    "III. Em R$ 42,75 os algarismos 75 são reais inteiros.\n"
                    "IV. 100 moedas de 1 centavo somam R$ 1,00.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e IV", "II, III e IV", "I e III", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "75 são centavos, não reais inteiros (III errada). I, II e IV corretas.",
                "difficulty": "intermediate",
                "source_assets": sa("page-003.jpg"),
                "section": "final_quiz",
            },
            *_challenge_exercises(sa),
        ],
    }


def _challenge_exercises(sa) -> list:
    return [
        {
            "id": "mat3-des-001",
            "type": "multiple_choice",
            "topic": "equality_balance",
            "question": (
                "Na balança, 3 cubos verdes equilibram 2 esferas azuis. "
                "Se no prato esquerdo houver 6 cubos verdes, quantas esferas azuis "
                "devem ir ao prato direito para equilibrar?"
            ),
            "options": ["2 esferas", "3 esferas", "4 esferas", "6 esferas"],
            "correct_answer": 2,
            "explanation": "Dobrou os cubos (3→6) → dobrar as esferas: 2×2 = 4 esferas.",
            "difficulty": "advanced",
            "source_assets": sa("page-064.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-002",
            "type": "multiple_choice",
            "topic": "inverse_operations",
            "question": (
                "Em uma festa havia ? convidados; compraram mais 38 copos e ficaram 92 copos no total. "
                "Quantos convidados havia no início?"
            ),
            "options": ["54", "64", "74", "130"],
            "correct_answer": 0,
            "explanation": "? + 38 = 92 → 92 − 38 = 54 convidados.",
            "difficulty": "advanced",
            "source_assets": sa("page-055.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-003",
            "type": "multiple_choice",
            "topic": "inverse_operations",
            "question": (
                "Desafio das balanças: 2 copos altos = 1 jarra; 1 jarra = 4 xícaras pequenas. "
                "Quantas xícaras pequenas equivalem a 1 copo alto?"
            ),
            "options": ["1", "2", "3", "4"],
            "correct_answer": 1,
            "explanation": "2 copos = 4 xícaras → 1 copo = 2 xícaras.",
            "difficulty": "advanced",
            "source_assets": sa("page-055.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-004",
            "type": "multiple_choice",
            "topic": "multiplication_table",
            "question": "Usando 3 × 8 = 24, calcule 9 × 8:",
            "options": ["48", "56", "72", "81"],
            "correct_answer": 2,
            "explanation": "9 é o triplo de 3 → 24 × 3 = 72.",
            "difficulty": "advanced",
            "source_assets": sa("page-050.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-005",
            "type": "multiple_choice",
            "topic": "multiplication_table",
            "question": (
                "Juliano e Marco arrecadaram R$ 454 no ano passado (3×100 + 3×50 + 2×2). "
                "Este ano querem o dobro. Qual a meta?"
            ),
            "options": ["R$ 454", "R$ 808", "R$ 908", "R$ 1 816"],
            "correct_answer": 2,
            "explanation": "454 × 2 = 908 reais.",
            "difficulty": "advanced",
            "source_assets": sa("page-005.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-006",
            "type": "multiple_choice",
            "topic": "quadrilaterals",
            "question": (
                "Classifique: quadrilátero com dois pares de lados opostos paralelos e "
                "todos os lados com mesma medida, mas sem ângulos retos obrigatórios."
            ),
            "options": ["Trapézio", "Losango", "Retângulo", "Triângulo"],
            "correct_answer": 1,
            "explanation": "4 lados iguais e opostos paralelos → losango (pode não ser retângulo).",
            "difficulty": "advanced",
            "source_assets": sa("page-020.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-007",
            "type": "multiple_choice",
            "topic": "trapezoids_parallelograms",
            "question": (
                "Um quadrilátero convexo que NÃO é trapézio e tem quatro ângulos retos é:"
            ),
            "options": ["Losango obliquo", "Retângulo ou quadrado", "Pentágono", "Trapézio isósceles"],
            "correct_answer": 1,
            "explanation": "4 retos e 4 lados → retângulo (ou quadrado se lados iguais).",
            "difficulty": "advanced",
            "source_assets": sa("page-038.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-008",
            "type": "multiple_choice",
            "topic": "decimals_intro",
            "question": "208 ÷ 10, escrito em forma decimal, é:",
            "options": ["2,08", "20,8", "208,0", "0,208"],
            "correct_answer": 1,
            "explanation": "Dividir por 10 desloca o 8 das unidades para os décimos: 20,8.",
            "difficulty": "advanced",
            "source_assets": sa("page-010.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-009",
            "type": "multiple_choice",
            "topic": "decimals_intro",
            "question": (
                "Leia as afirmativas:\n"
                "I. 0,01 é 100 vezes menor que 1.\n"
                "II. 10 centésimos formam 1 décimo.\n"
                "III. 0,5 é a metade da unidade.\n"
                "IV. 1 : 100 = 0,1.\n\n"
                "Estão corretas apenas:"
            ),
            "options": ["I, II e III", "II, III e IV", "I e IV", "I, II, III e IV"],
            "correct_answer": 0,
            "explanation": "1:100 = 0,01, não 0,1 (IV errada). I, II e III corretas.",
            "difficulty": "advanced",
            "source_assets": sa("page-007.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-010",
            "type": "multiple_choice",
            "topic": "money_decimals",
            "question": (
                "O menor número possível de cédulas e moedas para representar R$ 53,25 é: "
                "uma cédula de R$ 50, uma de R$ 2, uma moeda de R$ 1 e uma de R$ 0,25. "
                "Quantas peças de dinheiro são usadas nessa combinação?"
            ),
            "options": ["3", "4", "5", "7"],
            "correct_answer": 1,
            "explanation": "50 + 2 + 1 + 0,25 = 53,25 com 4 peças (mínimo no caderno).",
            "difficulty": "advanced",
            "source_assets": sa("page-001.jpg"),
            "section": "desafios",
        },
    ]
