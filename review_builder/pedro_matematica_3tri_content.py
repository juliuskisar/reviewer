"""Conteúdo pedagógico da revisão Pedro — Matemática PE 3º trimestre (Módulos 16, 21, 27 e 31)."""

from __future__ import annotations

REVIEW_ID = "pedro-pe-matematica-3tri"
ASSET_PREFIX = "assets/pedro_pe_matematica_3_tri"


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
        "subtitle": "Pedro · 6º ano · Módulos 16, 21, 27 e 31",
        "language": "pt-BR",
        "discipline": "Matemática",
        "grade": "6º ano",
        "metadata": {
            "student_name": "Pedro",
            "exam_type": "Prova Específica (PE)",
            "estimated_duration_minutes": 65,
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
                    "text": "Múltiplos, divisores, números primos, critérios de divisibilidade, paridade, "
                    "MMC, grandezas e medidas, área, perímetro e conversões de m². Reserve cerca de 1 hora.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🔗", "title": "Múltiplos e divisores", "text": "Tabuada · fator · divisível"},
                        {"icon": "🔢", "title": "Primos", "text": "Dois divisores · primos entre si"},
                        {"icon": "✓", "title": "Divisibilidade", "text": "2, 3, 4, 5, 6, 9 e 10"},
                        {"icon": "➕", "title": "Paridade", "text": "Par/ímpar na soma e no produto"},
                        {"icon": "📏", "title": "Medidas", "text": "Comprimento · massa · capacidade"},
                        {"icon": "📐", "title": "Área", "text": "Malha · perímetro · ha e alqueire"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 16/21 — Divisibilidade e primos",
                        "Módulo 31 — Múltiplos, paridade e MMC",
                        "Módulo 27 — Grandezas, área e perímetro",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Revise regras e exemplos.",
                            "tip": "Monte uma tabelinha dos critérios de divisibilidade.",
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
                            "description": "Questões no estilo Teste e Em casa do caderno.",
                            "tip": "Responda primeiro; só depois clique em Verificar.",
                        },
                        {
                            "title": "Encare os Desafios",
                            "panel": "desafios",
                            "panel_label": "Desafios",
                            "description": "Problemas mais exigentes — estilo Teste Cesgranrio/Cefet da apostila.",
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
            *_topic_multiples(),
            *_topic_primes(),
            *_topic_divisibility(),
            *_topic_mmc_extra(),
            *_topic_parity(),
            *_topic_measures(),
            *_topic_area_perimeter(),
            *_topic_area_units(),
        ],
    }


def _topic_multiples() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "1. Múltiplos e divisores"},
            "topic_id": "multiples_divisors",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Na tabuada, 30 aparece em várias multiplicações. Dizemos que 30 é múltiplo de 3, de 5 e de 10. "
                "Recíproco: 3, 5 e 10 são divisores (ou fatores) de 30. "
                "“É múltiplo de” = “é divisível por”; “é divisor de” = “é fator de”.",
            },
            "topic_id": "multiples_divisors",
            "sources": [_src("page-017.jpg"), _src("page-014.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "×", "title": "Múltiplo", "text": "Resultado de n × k (k natural)"},
                    {"icon": "➗", "title": "Divisor", "text": "Divide o número sem resto"},
                    {"icon": "0", "title": "Zero", "text": "Múltiplo de qualquer natural (exceto 0)"},
                    {"icon": "📅", "title": "Periodicidade", "text": "Eventos a cada n anos → múltiplos de n"},
                ],
            },
            "topic_id": "multiples_divisors",
        },
    ]


def _topic_primes() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "2. Números primos e primos entre si"},
            "topic_id": "prime_numbers",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Número primo tem exatamente dois divisores naturais: 1 e ele mesmo (ex.: 2, 3, 11, 13). "
                "O 1 não é primo nem composto. Dois números são primos entre si quando o único divisor comum é 1 "
                "(ex.: 8 e 9 — nenhum é primo, mas são primos entre si).",
            },
            "topic_id": "prime_numbers",
            "sources": [_src("page-016.jpg"), _src("page-014.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Tipos de números",
                "headers": ["", "Primos", "Compostos", "Primos entre si"],
                "rows": [
                    ["Divisores", "Exatamente 2", "Mais de 2", "MDC = 1 (podem ser compostos)"],
                    ["Exemplos", "2, 3, 11", "4, 9, 30", "15 e 16 · 32 e 15"],
                    ["Cuidado", "1 não é primo", "9 = 3×3", "72 e 140 têm MDC 4 → não"],
                ],
            },
            "topic_id": "prime_numbers",
        },
    ]


def _topic_divisibility() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "3. Critérios de divisibilidade"},
            "topic_id": "divisibility",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Com os critérios você descobre divisibilidade sem fazer a divisão completa. "
                "No caderno você investigou padrões na tabuada do 3 e do 9.",
            },
            "topic_id": "divisibility",
            "sources": [_src("page-011.jpg"), _src("page-009.jpg"), _src("page-007.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Regras principais",
                "headers": ["Por", "Como verificar", "Exemplo"],
                "rows": [
                    ["2", "Algarismo das unidades par", "434 → divisível"],
                    ["3", "Soma dos algarismos múltipla de 3", "165 → 1+6+5=12"],
                    ["5", "Termina em 0 ou 5", "305 → divisível"],
                    ["9", "Soma dos algarismos múltipla de 9", "117 → 1+1+7=9"],
                    ["10", "Termina em 0", "2010 → divisível"],
                ],
            },
            "topic_id": "divisibility",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Soma de três consecutivos:",
                "text": "n + (n+1) + (n+2) = 3n + 3 = 3(n+1) → sempre múltiplo de 3 (pode ser par ou ímpar).",
            },
            "topic_id": "divisibility",
        },
    ]


def _topic_mmc_extra() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "4. Divisibilidade por 4 e 6 · MMC"},
            "topic_id": "divisibility_extra",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Divisível por 4: os dois últimos algarismos formam número divisível por 4 (ex.: 1.924 → 24÷4). "
                "Divisível por 6: divisível por 2 e por 3 ao mesmo tempo (6 = 2×3, primos entre si). "
                "MMC de dois números é o menor múltiplo comum — útil em encontros periódicos.",
            },
            "topic_id": "divisibility_extra",
            "sources": [_src("page-008.jpg"), _src("page-005.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "4️⃣", "title": "Por 4", "text": "Últimos dois algarismos ÷ 4"},
                    {"icon": "6️⃣", "title": "Por 6", "text": "Par + soma dos algarismos ÷ 3"},
                    {"icon": "🚶", "title": "MMC", "text": "João a cada 4 dias · Pedro a cada 6 → reencontro em 12"},
                    {"icon": "9️⃣", "title": "Completar p/ 9", "text": "Soma dos algarismos até múltiplo de 9"},
                ],
            },
            "topic_id": "divisibility_extra",
        },
    ]


def _topic_parity() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "5. Paridade (par e ímpar)"},
            "topic_id": "parity",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Paridade descreve se um natural é par (múltiplo de 2) ou ímpar. "
                "Investigue somas e produtos de pares e ímpares — o padrão aparece no fluxograma do caderno.",
            },
            "topic_id": "parity",
            "sources": [_src("page-006.jpg"), _src("page-004.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Soma e produto",
                "headers": ["Operação", "Par + par", "Ímpar + ímpar", "Par + ímpar", "Qualquer × par"],
                "rows": [
                    ["Resultado", "Par", "Par", "Ímpar", "Par"],
                    ["Ideia", "2a+2b=2(a+b)", "2k+2m par", "2k+1 ímpar", "Fator 2 no produto"],
                ],
            },
            "topic_id": "parity",
        },
    ]


def _topic_measures() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "6. Grandezas e medidas"},
            "topic_id": "measures",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Medir é comparar uma grandeza com uma unidade padrão. "
                "Comprimento (m), massa (kg), capacidade (L) usam sistema decimal: cada passo ×10 ou ÷10. "
                "Escreva símbolo sem plural: 5 m, 2 kg, 250 mL.",
            },
            "topic_id": "measures",
            "sources": [_src("page-041.jpg"), _src("page-036.jpg"), _src("page-033.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "📏", "title": "Comprimento", "text": "km → hm → dam → m → dm → cm → mm"},
                    {"icon": "⚖️", "title": "Massa", "text": "kg ↔ g (×1000) · 1 t = 1000 kg"},
                    {"icon": "🥤", "title": "Capacidade", "text": "L ↔ mL (×1000)"},
                    {"icon": "✏️", "title": "Grafia", "text": "Espaço antes do símbolo · L maiúsculo"},
                ],
            },
            "topic_id": "measures",
        },
    ]


def _topic_area_perimeter() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "7. Área e perímetro na malha"},
            "topic_id": "area_perimeter",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Área mede a superfície (unidade quadrada). Perímetro mede o contorno (unidade de comprimento). "
                "Polígonos iguais em área podem ter perímetros diferentes — e vice-versa.",
            },
            "topic_id": "area_perimeter",
            "sources": [_src("page-029.jpg"), _src("page-019.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "⬜", "title": "Contar quadrados", "text": "Área na malha = nº de u.a."},
                    {"icon": "📐", "title": "Perímetro", "text": "Some lados do contorno"},
                    {"icon": "↔️", "title": "Retângulo", "text": "Dobrar lados → perímetro dobra; área ×4"},
                    {"icon": "≠", "title": "Cuidado", "text": "Mesma área ≠ mesmo perímetro"},
                ],
            },
            "topic_id": "area_perimeter",
        },
    ]


def _topic_area_units() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "8. Conversão de unidades de área"},
            "topic_id": "area_conversion",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Cada unidade de área é 100 vezes a anterior (porque cada lado ×10). "
                "1 m² = 10.000 cm². Unidades agrícolas: 1 ha = 10.000 m²; 1 are = 100 m²; "
                "alqueire varia por região (paulista ≈ 24.200 m²).",
            },
            "topic_id": "area_conversion",
            "sources": [_src("page-030.jpg"), _src("page-023.jpg"), _src("page-031.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Conversões úteis",
                "headers": ["De → para", "Operação", "Exemplo"],
                "rows": [
                    ["m² → cm²", "× 10.000", "50 m² = 500.000 cm²"],
                    ["m² → km²", "÷ 1.000.000", "320 m² = 0,00032 km²"],
                    ["ha → m²", "× 10.000", "120 ha = 1.200.000 m²"],
                    ["alqueire paulista → m²", "× 24.200", "15 alq. = 363.000 m²"],
                ],
            },
            "topic_id": "area_conversion",
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
                    "text": "Revise cada tópico nos acordeões — critérios, medidas e pegadinhas.",
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "1. Múltiplos e divisores"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🔗", "title": "Vocabulário", "text": "Múltiplo ↔ divisível · divisor = fator"},
                        {"icon": "📊", "title": "Tabuada", "text": "Acha todas as multiplicações do número"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. Primos"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "2", "title": "Primo", "text": "Divisores: 1 e ele"},
                        {"icon": "🤝", "title": "Entre si", "text": "MDC = 1"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Divisibilidade"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["Por", "Regra rápida"],
                    "rows": [
                        ["2", "Unidade par"],
                        ["3 / 9", "Soma dos algarismos"],
                        ["5 / 10", "Termina em 0 ou 5 / só 0"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Por 4, 6 e MMC"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "4", "title": "Por 4", "text": "Dois últimos algarismos"},
                        {"icon": "6", "title": "Por 6", "text": "Par e soma ÷ 3"},
                        {"icon": "🔄", "title": "MMC", "text": "Menor múltiplo comum"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Paridade"}},
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Produto:",
                    "text": "Se um fator é par, o produto é par. Ímpar × ímpar = ímpar.",
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "6. Medidas"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "×10", "title": "Decimal", "text": "Comprimento, massa, capacidade"},
                        {"icon": "L", "title": "Litro", "text": "L maiúsculo · mL"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "7. Área × perímetro"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "⬜", "title": "Área", "text": "u.a. na malha"},
                        {"icon": "➰", "title": "Perímetro", "text": "Contorno em u.c."},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "8. m², ha, alqueire"}},
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Regra:",
                    "text": "Cada degrau de área ×100 (não ×10).",
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "Confundir múltiplo de 3 com múltiplo de 9 — todo múltiplo de 9 é de 3, mas nem todo múltiplo de 3 é de 9.",
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
                "topic": "multiples_divisors",
                "question": "Considerando 30 : 10 = 3, qual frase está correta?",
                "options": [
                    "10 é múltiplo de 30",
                    "30 é divisível por 10",
                    "3 é divisor de 10",
                    "30 é fator de 3",
                ],
                "correct_answer": 1,
                "explanation": "30 = 10 × 3 → 30 é múltiplo de 10 e divisível por 10; 10 é divisor de 30.",
                "difficulty": "basic",
                "source_assets": sa("page-017.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-002",
                "type": "multiple_choice",
                "topic": "multiples_divisors",
                "question": (
                    "Leia as afirmativas:\n"
                    "I. 0 é múltiplo de 10.\n"
                    "II. 104 é divisor de 10.\n"
                    "III. 9 é fator de 45.\n"
                    "IV. 8 não é fator de 48.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, II e III", "III e IV"],
                "correct_answer": 0,
                "explanation": "I e III corretas. II falsa (10÷104 não é inteiro). IV falsa (48÷8=6).",
                "difficulty": "intermediate",
                "source_assets": sa("page-015.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-003",
                "type": "multiple_choice",
                "topic": "prime_numbers",
                "question": "Qual alternativa lista apenas divisores de 30 que são números primos?",
                "options": ["1, 2, 3, 5", "2, 3, 5", "2, 3, 5, 6", "3, 5, 10"],
                "correct_answer": 1,
                "explanation": "D₃₀ = {1,2,3,5,6,10,15,30}. Primos entre eles: 2, 3 e 5 (1 não é primo).",
                "difficulty": "basic",
                "source_assets": sa("page-016.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-004",
                "type": "multiple_choice",
                "topic": "prime_numbers",
                "question": "Os números 72 e 140 são primos entre si?",
                "options": [
                    "Sim, porque 72 e 140 são compostos",
                    "Sim, porque não há divisor comum",
                    "Não, porque MDC(72, 140) = 4",
                    "Não, porque 72 é par",
                ],
                "correct_answer": 2,
                "explanation": "Primos entre si exigem MDC = 1. 72 e 140 dividem por 4.",
                "difficulty": "intermediate",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-005",
                "type": "multiple_choice",
                "topic": "divisibility",
                "question": "Entre 72, 305, 2001, 90, 45, 26, 1065, 434, 2010 e 149, quantos são divisíveis por 2?",
                "options": ["3", "4", "5", "6"],
                "correct_answer": 2,
                "explanation": "Pares: 72, 90, 26, 434, 2010 → cinco números.",
                "difficulty": "basic",
                "source_assets": sa("page-002.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-006",
                "type": "multiple_choice",
                "topic": "divisibility",
                "question": "Qual algarismo falta em 247□ para o número ser divisível por 3 e por 5?",
                "options": ["0", "2", "5", "8"],
                "correct_answer": 2,
                "explanation": "Por 5: termina em 0 ou 5. Por 3: soma 2+4+7+5=18 → 2475 funciona.",
                "difficulty": "intermediate",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-007",
                "type": "multiple_choice",
                "topic": "divisibility",
                "question": (
                    "Leia as afirmativas sobre divisibilidade:\n"
                    "I. 570 é divisível por 2, 3, 5 e 10.\n"
                    "II. 115 é divisível por 10.\n"
                    "III. Todo múltiplo de 10 é múltiplo de 2 e de 5.\n"
                    "IV. 117 é múltiplo de 9.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "II e III", "I, III e IV", "II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, III e IV corretas. 115 termina em 5, não é divisível por 10 (II falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-008",
                "type": "multiple_choice",
                "topic": "divisibility_extra",
                "question": "João caminha a cada 4 dias e Pedro a cada 6 dias. Se se encontraram hoje, em quantos dias se encontrarão de novo?",
                "options": ["10", "12", "18", "24"],
                "correct_answer": 1,
                "explanation": "MMC(4, 6) = 12 — menor múltiplo comum.",
                "difficulty": "basic",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-009",
                "type": "multiple_choice",
                "topic": "divisibility_extra",
                "question": "Qual é o menor número que deve ser somado a 1.433 para obter um múltiplo de 9?",
                "options": ["1", "3", "5", "7"],
                "correct_answer": 3,
                "explanation": "Soma dos algarismos: 1+4+3+3=11. Próximo múltiplo de 9 é 18 → falta 7. 1433+7=1440.",
                "difficulty": "intermediate",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-010",
                "type": "multiple_choice",
                "topic": "parity",
                "question": "A soma de dois números naturais ímpares é sempre:",
                "options": ["Ímpar", "Par", "Primo", "Múltiplo de 3"],
                "correct_answer": 1,
                "explanation": "Ímpar + ímpar = par (ex.: 3+5=8).",
                "difficulty": "basic",
                "source_assets": sa("page-006.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-011",
                "type": "multiple_choice",
                "topic": "parity",
                "question": "O produto de um número par por um número ímpar é sempre:",
                "options": ["Par", "Ímpar", "Primo", "Múltiplo de 5"],
                "correct_answer": 0,
                "explanation": "Par × qualquer = par (fator 2).",
                "difficulty": "basic",
                "source_assets": sa("page-006.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-012",
                "type": "multiple_choice",
                "topic": "measures",
                "question": "Qual grafia está correta para a distância entre duas cidades?",
                "options": ["3 kms", "3 Km", "3 km", "3 KM"],
                "correct_answer": 2,
                "explanation": "Símbolo km em minúsculas, sem plural: 3 km.",
                "difficulty": "basic",
                "source_assets": sa("page-026.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-013",
                "type": "multiple_choice",
                "topic": "measures",
                "question": "7,5 km correspondem a quantos metros?",
                "options": ["750 m", "7.500 m", "75.000 m", "750.000 m"],
                "correct_answer": 1,
                "explanation": "1 km = 1000 m → 7,5 × 1000 = 7.500 m.",
                "difficulty": "basic",
                "source_assets": sa("page-037.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-014",
                "type": "multiple_choice",
                "topic": "measures",
                "question": (
                    "Leia as afirmativas sobre medidas:\n"
                    "I. 2,5 L = 2.500 mL.\n"
                    "II. 500 g = 0,5 kg.\n"
                    "III. 940 mm = 9,4 m.\n"
                    "IV. 258 mm = 25,8 cm.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, II e IV", "III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. 940 mm = 0,94 m, não 9,4 m (III falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-026.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-015",
                "type": "multiple_choice",
                "topic": "area_perimeter",
                "question": (
                    "Dois polígonos na malha têm área 16 u.a. Um é um quadrado 4×4 (perímetro 16 u.c.) "
                    "e outro tem forma em U com perímetro 26 u.c. Isso mostra que:"
                ),
                "options": [
                    "Mesma área implica mesmo perímetro",
                    "Mesma área não garante mesmo perímetro",
                    "Perímetro maior sempre dá área maior",
                    "Área e perímetro usam a mesma unidade",
                ],
                "correct_answer": 1,
                "explanation": "Polígonos C e D do caderno: mesma área 16, perímetros 26 e 16.",
                "difficulty": "intermediate",
                "source_assets": sa("page-019.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-016",
                "type": "multiple_choice",
                "topic": "area_conversion",
                "question": "50 m² equivalem a quantos cm²?",
                "options": ["500 cm²", "5.000 cm²", "50.000 cm²", "500.000 cm²"],
                "correct_answer": 3,
                "explanation": "1 m² = 10.000 cm² → 50 × 10.000 = 500.000 cm².",
                "difficulty": "intermediate",
                "source_assets": sa("page-025.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-017",
                "type": "multiple_choice",
                "topic": "area_conversion",
                "question": "120 hectares correspondem a quantos km²?",
                "options": ["0,12 km²", "1,2 km²", "12 km²", "120 km²"],
                "correct_answer": 1,
                "explanation": "1 ha = 10.000 m²; 1 km² = 1.000.000 m² → 120 ha = 1.200.000 m² = 1,2 km².",
                "difficulty": "intermediate",
                "source_assets": sa("page-025.jpg"),
                "section": "exercises",
            },
            {
                "id": "mat3-pe-018",
                "type": "multiple_choice",
                "topic": "divisibility",
                "question": (
                    "Leia as afirmativas:\n"
                    "I. A soma de três naturais consecutivos é sempre múltipla de 3.\n"
                    "II. Essa soma é sempre par.\n"
                    "III. 165 é múltiplo de 3.\n"
                    "IV. Todo múltiplo de 6 é múltiplo de 3.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, III e IV", "I, II e III"],
                "correct_answer": 2,
                "explanation": "I, III e IV corretas. Soma consecutiva pode ser par ou ímpar (II falsa).",
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
            "topic": "prime_numbers",
            "question": (
                "Qual é o menor número de três algarismos divisível por 2 e por 3 simultaneamente?"
            ),
            "options": ["100", "102", "105", "110"],
            "correct_answer": 1,
            "explanation": "Precisa ser par e soma dos algarismos múltipla de 3. 102: par e 1+0+2=3.",
            "difficulty": "advanced",
            "source_assets": sa("page-001.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-002",
            "type": "multiple_choice",
            "topic": "divisibility",
            "question": (
                "Quantos números naturais de três algarismos são múltiplos de 5?"
            ),
            "options": ["179", "180", "200", "900"],
            "correct_answer": 1,
            "explanation": "De 100 a 999: 100,105,…,995 → (995−100)/5 + 1 = 180.",
            "difficulty": "advanced",
            "source_assets": sa("page-001.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-003",
            "type": "multiple_choice",
            "topic": "divisibility_extra",
            "question": "O número 1.924 é divisível por 4?",
            "options": [
                "Não, porque 1.924 é ímpar",
                "Sim, porque 24 ÷ 4 = 6",
                "Não, porque a soma dos algarismos é 16",
                "Sim, porque termina em 4",
            ],
            "correct_answer": 1,
            "explanation": "Critério de 4: dois últimos algarismos 24, divisível por 4.",
            "difficulty": "advanced",
            "source_assets": sa("page-008.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-004",
            "type": "multiple_choice",
            "topic": "divisibility_extra",
            "question": (
                "Leia as afirmativas:\n"
                "I. 42 é divisível por 6.\n"
                "II. 42 é divisível por 4.\n"
                "III. Se um número é divisível por 6, é divisível por 2 e por 3.\n"
                "IV. Se um número é divisível por 4, é divisível por 6.\n\n"
                "Estão corretas apenas:"
            ),
            "options": ["I e III", "II e IV", "I, II e III", "III e IV"],
            "correct_answer": 0,
            "explanation": "I e III corretas. 42÷4 não é inteiro (II falsa). 8÷4 mas não ÷6 (IV falsa).",
            "difficulty": "advanced",
            "source_assets": sa("page-008.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-005",
            "type": "multiple_choice",
            "topic": "measures",
            "question": (
                "Uma escada tem 7 degraus iguais e altura total 1,54 m. "
                "A altura de cada degrau, em centímetros, é:"
            ),
            "options": ["14 cm", "22 cm", "154 cm", "2,2 cm"],
            "correct_answer": 1,
            "explanation": "1,54 m = 154 cm. 154 ÷ 7 = 22 cm por degrau.",
            "difficulty": "advanced",
            "source_assets": sa("page-026.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-006",
            "type": "multiple_choice",
            "topic": "measures",
            "question": (
                "De um retângulo 18 cm × 13 cm retiraram-se dois quadrados iguais de lado 3 cm "
                "(cantos opostos). Qual é o perímetro da figura resultante?"
            ),
            "options": ["56 cm", "68 cm", "74 cm", "80 cm"],
            "correct_answer": 1,
            "explanation": "Perímetro do retângulo 18×13 é 62 cm; os recortes nos cantos acrescentam 6 cm ao contorno → 68 cm.",
            "difficulty": "advanced",
            "source_assets": sa("page-022.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-007",
            "type": "multiple_choice",
            "topic": "measures",
            "question": (
                "A distância entre a estação de tratamento e um consumidor é 23,632 km. "
                "Cada tubo tem 2,5 m. Quantos tubos, no mínimo, são necessários?"
            ),
            "options": ["945", "9453", "946", "9.453"],
            "correct_answer": 1,
            "explanation": "23,632 km = 23.632 m. 23.632 ÷ 2,5 = 9.452,8 → arredonda para cima: 9.453 tubos.",
            "difficulty": "advanced",
            "source_assets": sa("page-037.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-008",
            "type": "multiple_choice",
            "topic": "area_conversion",
            "question": "15 alqueires paulistas equivalem a quantos m²? (1 alq. paulista = 24.200 m²)",
            "options": ["363.000 m²", "36.300 m²", "3.630.000 m²", "242.000 m²"],
            "correct_answer": 0,
            "explanation": "15 × 24.200 = 363.000 m².",
            "difficulty": "advanced",
            "source_assets": sa("page-025.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-009",
            "type": "multiple_choice",
            "topic": "area_perimeter",
            "question": (
                "Um retângulo A na malha mede 3 cm × 2 cm. "
                "O retângulo B tem lados com o dobro das medidas de A. "
                "A área de B é quantas vezes a área de A?"
            ),
            "options": ["2", "3", "4", "6"],
            "correct_answer": 2,
            "explanation": "Lados dobram → área multiplica por 2×2 = 4.",
            "difficulty": "advanced",
            "source_assets": sa("page-021.jpg"),
            "section": "desafios",
        },
        {
            "id": "mat3-des-010",
            "type": "multiple_choice",
            "topic": "prime_numbers",
            "question": (
                "Considerando os cinco primeiros números primos (2, 3, 5, 7, 11), "
                "qual é o algarismo das unidades do produto 2 × 3 × 5 × 7 × 11?"
            ),
            "options": ["0", "2", "5", "6"],
            "correct_answer": 0,
            "explanation": "O produto inclui 2 e 5 → múltiplo de 10 → termina em 0.",
            "difficulty": "advanced",
            "source_assets": sa("page-005.jpg"),
            "section": "desafios",
        },
    ]
