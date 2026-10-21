"""Conteúdo pedagógico — Pedro · Desenho Geométrico PE 3º trimestre (Módulos 22 e 28)."""

from __future__ import annotations

from review_builder import geometric_figure as gf

REVIEW_ID = "pedro-pe-dg-3tri"
ASSET_PREFIX = "assets/pedro_pe_dg_3_tri"


def _src(page: str) -> dict:
    return {
        "asset": f"{ASSET_PREFIX}/{page}",
        "origin_type": "observed",
        "evidence": [f"Caderno DG / Matemática — {page}"],
    }


def sa(*pages: str) -> list[str]:
    return [f"{ASSET_PREFIX}/{p}" for p in pages]


def build_content() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Desenho Geométrico — PE 3º Trimestre",
        "subtitle": "Pedro · 6º ano · Módulos 22 e 28",
        "language": "pt-BR",
        "discipline": "Desenho Geométrico",
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
                    "text": "Quadriláteros notáveis e diagrama de inclusão, diagonais de polígonos, "
                    "fórmulas de área (retângulo, quadrado, triângulo, paralelogramo) e figuras "
                    "compostas — como no Módulo 22 e no Módulo 28 do caderno. Reserve cerca de 1 hora.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "⬜", "title": "Notáveis", "text": "Trapézio · paralelogramo · retângulo · losango · quadrado"},
                        {"icon": "↔️", "title": "Diagonais", "text": "Vértices não consecutivos · retângulo"},
                        {"icon": "📐", "title": "Retângulo", "text": "A = b × c · malha de 1 cm²"},
                        {"icon": "🔲", "title": "Quadrado", "text": "A = ℓ × ℓ"},
                        {"icon": "🔺", "title": "Triângulo", "text": "Metade do retângulo"},
                        {"icon": "🧩", "title": "Compostas", "text": "Decompor · somar áreas"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 22 — Quadriláteros notáveis e diagonais",
                        "Módulo 28 — Áreas de figuras planas",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Observe as figuras geométricas desenhadas na página.",
                            "tip": "Desenhe no caderno o diagrama de Venn dos quadriláteros.",
                        },
                        {
                            "title": "Revise o Resumo rápido",
                            "panel": "summary",
                            "panel_label": "Resumo rápido",
                            "description": "Percorra os cards-síntese antes da PE.",
                        },
                        {
                            "title": "Faça os Exercícios",
                            "panel": "exercises",
                            "panel_label": "Exercícios",
                            "description": "Questões no estilo Teste e Atividade — várias trazem figura na tela.",
                            "tip": "Leia as medidas na figura antes de calcular.",
                        },
                        {
                            "title": "Encare os Desafios",
                            "panel": "desafios",
                            "panel_label": "Desafios",
                            "description": "Problemas mais exigentes do caderno (Teste, figuras compostas, malhas).",
                            "tip": "Decomponha figuras irregulares em retângulos e triângulos.",
                        },
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "info",
                    "title": "Como navegar:",
                    "text": "Use os botões do roteiro ou as abas no topo. As figuras dos exercícios aparecem logo abaixo do enunciado.",
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
            *_topic_notable_quadrilaterals(),
            *_topic_quadrilateral_hierarchy(),
            *_topic_polygon_diagonals(),
            *_topic_rectangle_area(),
            *_topic_square_area(),
            *_topic_triangle_area(),
            *_topic_composite_area(),
            *_topic_area_applications(),
        ],
    }


def _topic_notable_quadrilaterals() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "1. Quadriláteros notáveis"},
            "topic_id": "notable_quadrilaterals",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Quadriláteros notáveis são os que têm pelo menos um par de lados paralelos "
                "(ou propriedades especiais de lados e ângulos). Memorize a característica principal de cada um.",
            },
            "topic_id": "notable_quadrilaterals",
            "sources": [_src("page-020.jpg"), _src("page-022.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Nome", "Característica principal"],
                "rows": [
                    ["Trapézio", "Um par de lados paralelos"],
                    ["Paralelogramo", "Dois pares de lados paralelos"],
                    ["Retângulo", "Quatro ângulos retos"],
                    ["Losango", "Quatro lados congruentes"],
                    ["Quadrado", "Quatro ângulos retos e quatro lados iguais"],
                ],
            },
            "topic_id": "notable_quadrilaterals",
        },
        {
            "type": "callout",
            "content": {
                "variant": "tip",
                "title": "Quadrado é duplo:",
                "text": "Todo quadrado é ao mesmo tempo retângulo e losango — encaixa na interseção do diagrama de Venn.",
            },
            "topic_id": "notable_quadrilaterals",
        },
    ]


def _topic_quadrilateral_hierarchy() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "2. Inclusão entre quadriláteros"},
            "topic_id": "quadrilateral_hierarchy",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "No caderno, trapézio é qualquer quadrilátero com um par de lados paralelos. "
                "Por isso paralelogramos, retângulos, losangos e quadrados também são trapézios. "
                "Paralelogramo exige dois pares de lados paralelos — retângulo e losango são casos especiais.",
            },
            "topic_id": "quadrilateral_hierarchy",
            "sources": [_src("page-019.jpg"), _src("page-017.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "✅", "title": "Verdadeiro", "text": "Todo retângulo é paralelogramo"},
                    {"icon": "✅", "title": "Verdadeiro", "text": "Todo losango é paralelogramo"},
                    {"icon": "❌", "title": "Falso", "text": "Todo trapézio é paralelogramo"},
                    {"icon": "❌", "title": "Falso", "text": "Todo retângulo é quadrado"},
                ],
            },
            "topic_id": "quadrilateral_hierarchy",
        },
    ]


def _topic_polygon_diagonals() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "3. Diagonais de polígonos"},
            "topic_id": "polygon_diagonals",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Diagonal é segmento que liga dois vértices não consecutivos. "
                "Em um retângulo, a diagonal é a maior distância em linha reta entre dois pontos da borda "
                "(como no campo de futebol 105 m × 68 m). Triângulo não tem diagonal. "
                "Quadrilatero convexo: duas diagonais; pentágono: cinco diagonais.",
            },
            "topic_id": "polygon_diagonals",
            "sources": [_src("page-015.jpg"), _src("page-016.jpg"), _src("page-013.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Polígono", "Nº de diagonais (convexo)"],
                "rows": [
                    ["Quadrilátero", "2"],
                    ["Pentágono", "5"],
                    ["Hexágono", "9 (padrão do caderno)"],
                ],
            },
            "topic_id": "polygon_diagonals",
        },
        {
            "type": "callout",
            "content": {
                "variant": "tip",
                "title": "Retângulo:",
                "text": "As duas diagonais têm a mesma medida e se cortam no ponto médio de ambas. "
                "Se PA = 8 cm (metade de uma diagonal), então PB = 8 cm e BD = 16 cm.",
            },
            "topic_id": "polygon_diagonals",
            "sources": [_src("page-009.jpg"), _src("page-011.jpg")],
        },
    ]


def _topic_rectangle_area() -> list:
    grid = gf.unit_grid(
        5,
        4,
        title="Exemplo — retângulo na malha",
        unit_label="1 cm",
        aria_label="Retângulo de 5 cm por 4 cm formado por 20 quadrados de 1 cm",
    )
    grid["topic_id"] = "rectangle_area"
    grid["sources"] = [_src("page-008.jpg")]
    rect = gf.rectangle(
        4,
        2.5,
        w_label="4 cm",
        h_label="2,5 cm",
        title="Fórmula A = b × c",
        aria_label="Retângulo 4 cm por 2,5 cm",
    )
    rect["topic_id"] = "rectangle_area"
    rect["sources"] = [_src("page-006.jpg")]
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "4. Área do retângulo"},
            "topic_id": "rectangle_area",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Contando quadrados de 1 cm² na malha: um retângulo 5 cm × 4 cm tem 20 quadrados → 20 cm². "
                "A fórmula resume isso: A = b × c (base × altura adjacente). "
                "Funciona mesmo com decimais: 4 × 2,5 = 10 cm².",
            },
            "topic_id": "rectangle_area",
            "sources": [_src("page-008.jpg"), _src("page-006.jpg")],
        },
        grid,
        rect,
    ]


def _topic_square_area() -> list:
    sq = gf.rectangle(
        3,
        3,
        w_label="ℓ = 3 cm",
        h_label="ℓ = 3 cm",
        title="Quadrado — lados iguais",
        fill="#fcd34d",
        stroke="#b45309",
    )
    sq["topic_id"] = "square_area"
    sq["sources"] = [_src("page-007.jpg")]
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "5. Área do quadrado"},
            "topic_id": "square_area",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "No quadrado, os dois lados adjacentes são iguais (ℓ). "
                "A área é ℓ × ℓ = ℓ². Exemplo: lado 3 cm → 3 × 3 = 9 cm². "
                "Quadrado é caso especial de retângulo.",
            },
            "topic_id": "square_area",
            "sources": [_src("page-007.jpg"), _src("page-005.jpg")],
        },
        sq,
    ]


def _topic_triangle_area() -> list:
    tri = gf.right_triangle(
        7,
        4,
        b_label="7 cm",
        h_label="4 cm",
        title="Triângulo retângulo",
    )
    tri["topic_id"] = "triangle_area"
    tri["sources"] = [_src("page-004.jpg")]
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "6. Área do triângulo retângulo"},
            "topic_id": "triangle_area",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Cortar um retângulo pela diagonal forma dois triângulos retângulos iguais. "
                "Cada um tem metade da área do retângulo: A = (b × h) ÷ 2. "
                "Exemplo: base 7 cm, altura 4 cm → (7 × 4) ÷ 2 = 14 cm².",
            },
            "topic_id": "triangle_area",
            "sources": [_src("page-004.jpg")],
        },
        tri,
    ]


def _topic_composite_area() -> list:
    para = gf.parallelogram(
        7,
        4,
        base_label="7 cm",
        height_label="4 cm (altura)",
        title="Paralelogramo — use a altura perpendicular",
    )
    para["topic_id"] = "composite_area"
    para["sources"] = [_src("page-002.jpg")]
    trap = gf.trapezoid(
        8,
        10,
        4,
        top_label="8 cm",
        bottom_label="10 cm",
        height_label="4 cm",
        title="Trapézio — média das bases × altura",
    )
    trap["topic_id"] = "composite_area"
    trap["sources"] = [_src("page-004.jpg")]
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "7. Paralelogramo, trapézio e figuras compostas"},
            "topic_id": "composite_area",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Paralelogramo: mesma área de um retângulo com mesma base e mesma altura perpendicular (A = b × h). "
                "Trapézio: A = (B + b) × h ÷ 2. Figuras em L ou em degrau: decomponha em retângulos, "
                "some as áreas. Collage da Taís: retângulo 10 × 5 menos um triângulo no canto.",
            },
            "topic_id": "composite_area",
            "sources": [_src("page-002.jpg"), _src("page-005.jpg"), _src("page-003.jpg")],
        },
        para,
        trap,
    ]


def _topic_area_applications() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "8. Aplicações e malhas"},
            "topic_id": "area_applications",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Problemas de pintura: calcule área de cada parede e do teto, subtraia portas e janelas. "
                "Malhas (como bandeira da Escócia 40 × 24): conte quadrados ou use frações do total. "
                "Plano cartesiano: vértices dados → desenhe e use base × altura no quadrado.",
            },
            "topic_id": "area_applications",
            "sources": [_src("page-003.jpg"), _src("page-001.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "warning",
                "title": "Pegadinha da PE:",
                "text": "Perímetro e área são grandezas diferentes — não some lados quando o enunciado pede m².",
            },
            "topic_id": "area_applications",
        },
    ]


def _section_summary() -> dict:
    summaries = [
        ("1. Notáveis", "⬜", "Trapézio → 1 par || · Paralelogramo → 2 pares ||"),
        ("2. Inclusão", "🔗", "Quadrado ∈ retângulo ∩ losango · Paralelogramo ⊂ trapézio"),
        ("3. Diagonais", "↔️", "Vértices não vizinhos · Retângulo: iguais e bissectam"),
        ("4. Retângulo", "📐", "A = b × c · malha 1 cm²"),
        ("5. Quadrado", "🔲", "A = ℓ²"),
        ("6. Triângulo", "🔺", "A = b × h ÷ 2"),
        ("7. Compostas", "🧩", "Decompor · paralelogramo · trapézio"),
        ("8. Aplicações", "🎨", "Pintura · malha · subtrair vãos"),
    ]
    blocks: list = [
        {
            "type": "panel_intro",
            "content": {
                "title": "Mapa mental da PE",
                "text": "Revise os oito blocos abaixo — mesmo estilo das explicações.",
            },
        },
    ]
    for title, icon, text in summaries:
        blocks.append({"type": "heading", "content": {"level": 3, "text": title}})
        blocks.append({
            "type": "concept_grid",
            "content": {"cards": [{"icon": icon, "title": title.split(". ", 1)[1], "text": text}]},
        })
    blocks.append({
        "type": "callout",
        "content": {
            "variant": "warning",
            "title": "Na prova:",
            "text": "Trapézio isósceles ou retângulo pode ser paralelogramo? Só se tiver dois pares de lados paralelos.",
        },
    })
    return {"id": "summary", "type": "quick_summary", "title": "Resumo rápido", "blocks": blocks}


def build_exercises() -> dict:
    base = _base_exercises(sa)
    challenges = _challenge_exercises(sa)
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "exercises": base + challenges,
    }


def _base_exercises(sa) -> list:
    return [
        {
            "id": "dg-pe-001",
            "type": "multiple_choice",
            "topic": "notable_quadrilaterals",
            "question": "Qual quadrilátero notável possui quatro ângulos internos retos e quatro lados de mesma medida?",
            "options": ["Losango", "Trapézio", "Quadrado", "Paralelogramo qualquer"],
            "correct_answer": 2,
            "explanation": "Quadrado: quatro retos e quatro lados iguais. Losango não exige ângulo reto.",
            "difficulty": "basic",
            "source_assets": sa("page-020.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-002",
            "type": "multiple_choice",
            "topic": "quadrilateral_hierarchy",
            "question": "Segundo o caderno (definição inclusiva), todo paralelogramo também é:",
            "options": ["Apenas losango", "Trapézio", "Sempre quadrado", "Nunca retângulo"],
            "correct_answer": 1,
            "explanation": "Paralelogramo tem um par (na verdade dois pares) de lados paralelos → é trapézio.",
            "difficulty": "basic",
            "source_assets": sa("page-019.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-003",
            "type": "multiple_choice",
            "topic": "polygon_diagonals",
            "question": "Quantas diagonais tem um pentágono convexo, como no caderno?",
            "options": ["2", "4", "5", "10"],
            "correct_answer": 2,
            "explanation": "Pentágono convexo: 5 diagonais (cada vértice liga a 2 não consecutivos).",
            "difficulty": "basic",
            "source_assets": sa("page-009.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-004",
            "type": "multiple_choice",
            "topic": "polygon_diagonals",
            "question": (
                "Em um retângulo, as diagonais se cruzam no ponto P. Se PA = 8 cm, "
                "qual é a medida de BD (diagonal completa)?"
            ),
            "options": ["8 cm", "12 cm", "16 cm", "4 cm"],
            "correct_answer": 2,
            "explanation": "Diagonais iguais e bissectam: PA = PB = 8 cm → diagonal inteira BD = 16 cm.",
            "difficulty": "intermediate",
            "source_assets": sa("page-009.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-005",
            "type": "multiple_choice",
            "topic": "rectangle_area",
            "question": (
                "Observe o retângulo na figura (malha de 1 cm). "
                "Quantos quadrados de 1 cm² cabem dentro dele?"
            ),
            "visual": gf.unit_grid(5, 4, unit_label="1 cm", aria_label="Retângulo 5 por 4 na malha"),
            "options": ["9", "18", "20", "25"],
            "correct_answer": 2,
            "explanation": "5 × 4 = 20 quadrados de 1 cm² → área 20 cm².",
            "difficulty": "basic",
            "source_assets": sa("page-008.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-006",
            "type": "multiple_choice",
            "topic": "rectangle_area",
            "question": "Observe o retângulo. Usando A = b × c, a área é:",
            "visual": gf.rectangle(4, 2.5, w_label="4 cm", h_label="2,5 cm"),
            "options": ["6,5 cm²", "8 cm²", "10 cm²", "12,5 cm²"],
            "correct_answer": 2,
            "explanation": "4 × 2,5 = 10 cm².",
            "difficulty": "basic",
            "source_assets": sa("page-006.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-007",
            "type": "multiple_choice",
            "topic": "square_area",
            "question": "Um quadrado tem lado 1,5 mm. Sua área vale:",
            "options": ["3 mm²", "2,25 mm²", "6 mm²", "1,5 mm²"],
            "correct_answer": 1,
            "explanation": "A = ℓ² = 1,5 × 1,5 = 2,25 mm².",
            "difficulty": "basic",
            "source_assets": sa("page-001.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-008",
            "type": "multiple_choice",
            "topic": "triangle_area",
            "question": "Observe o triângulo retângulo. A área, em cm², é:",
            "visual": gf.right_triangle(7, 4, b_label="7 cm", h_label="4 cm"),
            "options": ["11", "14", "28", "7"],
            "correct_answer": 1,
            "explanation": "(7 × 4) ÷ 2 = 14 cm².",
            "difficulty": "basic",
            "source_assets": sa("page-004.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-009",
            "type": "multiple_choice",
            "topic": "composite_area",
            "question": "Observe o trapézio. A área é:",
            "visual": gf.trapezoid(8, 10, 4, top_label="8 cm", bottom_label="10 cm", height_label="4 cm"),
            "options": ["32 cm²", "36 cm²", "40 cm²", "80 cm²"],
            "correct_answer": 1,
            "explanation": "(8 + 10) × 4 ÷ 2 = 36 cm².",
            "difficulty": "intermediate",
            "source_assets": sa("page-004.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-010",
            "type": "multiple_choice",
            "topic": "composite_area",
            "question": "Observe o paralelogramo (base 7 cm, altura perpendicular 4 cm). A área é:",
            "visual": gf.parallelogram(7, 4, base_label="7 cm", height_label="4 cm"),
            "options": ["28 cm²", "14 cm²", "11 cm²", "35 cm²"],
            "correct_answer": 0,
            "explanation": "Paralelogramo: base × altura = 7 × 4 = 28 cm² (não use o lado inclinado 5 cm como altura).",
            "difficulty": "intermediate",
            "source_assets": sa("page-002.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-011",
            "type": "multiple_choice",
            "topic": "area_applications",
            "question": (
                "Folha retangular 30 cm × 20 cm. Qual é a área, em cm²?"
            ),
            "options": ["50", "100", "600", "1200"],
            "correct_answer": 2,
            "explanation": "30 × 20 = 600 cm².",
            "difficulty": "basic",
            "source_assets": sa("page-004.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-012",
            "type": "multiple_choice",
            "topic": "quadrilateral_hierarchy",
            "question": (
                "Analise as afirmativas:\n"
                "I. Todo retângulo é paralelogramo.\n"
                "II. Todo trapézio é paralelogramo.\n"
                "III. Existem retângulos que são quadrados.\n"
                "IV. Nenhum losango é paralelogramo.\n\n"
                "Estão corretas apenas:"
            ),
            "options": ["I e III", "II e IV", "I, II e III", "III e IV"],
            "correct_answer": 0,
            "explanation": "I e III corretas. II falsa; IV falsa (losango é paralelogramo).",
            "difficulty": "intermediate",
            "source_assets": sa("page-017.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-013",
            "type": "multiple_choice",
            "topic": "notable_quadrilaterals",
            "question": (
                "Luísa montou um quadrilátero convexo com quatro palitos idênticos. "
                "A figura formada é necessariamente um:"
            ),
            "options": ["Retângulo", "Losango", "Quadrado", "Paralelogramo"],
            "correct_answer": 1,
            "explanation": "Quatro lados iguais → losango (não precisa ter ângulo reto).",
            "difficulty": "intermediate",
            "source_assets": sa("page-010.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-014",
            "type": "multiple_choice",
            "topic": "area_applications",
            "question": (
                "Um muro retangular mede 8 m de comprimento por 3 m de altura. "
                "A área de uma face desse muro é:"
            ),
            "options": ["11 m²", "22 m²", "24 m²", "48 m²"],
            "correct_answer": 2,
            "explanation": "8 × 3 = 24 m² por face (problema da pintura no caderno).",
            "difficulty": "basic",
            "source_assets": sa("page-001.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-015",
            "type": "multiple_choice",
            "topic": "composite_area",
            "question": (
                "Retângulo laranja 10 cm × 5 cm teve um canto triangular recortado "
                "(como a collage da Taís). A área laranja que restou ainda é:"
            ),
            "options": ["50 cm²", "Menor que 50 cm²", "Maior que 50 cm²", "25 cm²"],
            "correct_answer": 1,
            "explanation": "Área original 50 cm²; ao remover um pedaço, a área diminui.",
            "difficulty": "intermediate",
            "source_assets": sa("page-002.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-016",
            "type": "multiple_choice",
            "topic": "polygon_diagonals",
            "question": (
                "Leia as afirmativas sobre diagonais:\n"
                "I. Triângulo não possui diagonal.\n"
                "II. Em quadrilátero côncavo, alguma diagonal pode ficar fora da figura.\n"
                "III. Retângulo tem diagonais de mesma medida.\n"
                "IV. Pentágono tem 2 diagonais.\n\n"
                "Estão corretas apenas:"
            ),
            "options": ["I, II e III", "II e IV", "I e IV", "I, III e IV"],
            "correct_answer": 0,
            "explanation": "I, II e III corretas. IV errada (pentágono tem 5 diagonais).",
            "difficulty": "intermediate",
            "source_assets": sa("page-016.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-017",
            "type": "multiple_choice",
            "topic": "square_area",
            "question": (
                "Quadrado maior: lado 10 cm. Quadrado menor interno: lado 4 cm. "
                "A área de cada um dos quatro trapézios idênticos entre eles vale:"
            ),
            "options": ["42 cm²", "84 cm²", "21 cm²", "100 cm²"],
            "correct_answer": 2,
            "explanation": (
                "Área total 10² = 100 cm²; quadrado interno 4² = 16 cm². "
                "Resto 84 cm² dividido em 4 trapézios → 21 cm² cada."
            ),
            "difficulty": "intermediate",
            "source_assets": sa("page-003.jpg"),
            "section": "exercises",
        },
        {
            "id": "dg-pe-018",
            "type": "multiple_choice",
            "topic": "area_applications",
            "question": (
                "Sala 5 m × 4 m (teto). Pintar só o teto. Área a pintar:"
            ),
            "options": ["9 m²", "18 m²", "20 m²", "40 m²"],
            "correct_answer": 2,
            "explanation": "Teto = retângulo 5 × 4 = 20 m².",
            "difficulty": "basic",
            "source_assets": sa("page-003.jpg"),
            "section": "final_quiz",
        },
    ]


def _challenge_exercises(sa) -> list:
    items = [
        {
            "id": "dg-des-001",
            "type": "multiple_choice",
            "topic": "area_applications",
            "question": (
                "Marina montou quadrado EFGH com dois quadrados de áreas 36 cm² e 4 cm² "
                "e dois retângulos iguais. Cada retângulo tem área:"
            ),
            "options": ["12 cm²", "16 cm²", "20 cm²", "24 cm²"],
            "correct_answer": 0,
            "explanation": "Lados √36=6 cm e √4=2 cm. Lado grande 8 cm → área total 64 cm². "
            "64 − 36 − 4 = 24 cm² nos dois retângulos → 12 cm² cada.",
            "difficulty": "advanced",
            "source_assets": sa("page-001.jpg"),
            "section": "desafios",
        },
        {
            "id": "dg-des-002",
            "type": "multiple_choice",
            "topic": "triangle_area",
            "question": "Observe o triângulo retângulo (base 5 cm, altura 5 cm). A área é:",
            "visual": gf.right_triangle(5, 5, b_label="5 cm", h_label="5 cm"),
            "options": ["25 cm²", "12,5 cm²", "10 cm²", "20 cm²"],
            "correct_answer": 1,
            "explanation": "(5 × 5) ÷ 2 = 12,5 cm².",
            "difficulty": "advanced",
            "source_assets": sa("page-004.jpg"),
            "section": "desafios",
        },
        {
            "id": "dg-des-003",
            "type": "multiple_choice",
            "topic": "rectangle_area",
            "question": "Observe o retângulo 11 cm × 13 cm. A área é:",
            "visual": gf.rectangle(11, 13, w_label="11 cm", h_label="13 cm"),
            "options": ["143 cm²", "48 cm²", "121 cm²", "130 cm²"],
            "correct_answer": 0,
            "explanation": "11 × 13 = 143 cm².",
            "difficulty": "advanced",
            "source_assets": sa("page-001.jpg"),
            "section": "desafios",
        },
        {
            "id": "dg-des-004",
            "type": "multiple_choice",
            "topic": "composite_area",
            "question": (
                "Quadrado PQRS tem lado 4 cm. Usando A = ℓ² e também base × altura, "
                "a área obtida é:"
            ),
            "visual": gf.rectangle(4, 4, w_label="4 cm", h_label="4 cm", fill="#fcd34d", stroke="#b45309"),
            "options": ["8 cm²", "12 cm²", "16 cm²", "20 cm²"],
            "correct_answer": 2,
            "explanation": "4 × 4 = 16 cm² — quadrado é retângulo especial.",
            "difficulty": "advanced",
            "source_assets": sa("page-005.jpg"),
            "section": "desafios",
        },
        {
            "id": "dg-des-005",
            "type": "multiple_choice",
            "topic": "area_applications",
            "question": (
                "Quatro muros iguais (8 m × 3 m), duas faces cada um. "
                "Área total a pintar:"
            ),
            "options": ["96 m²", "192 m²", "24 m²", "48 m²"],
            "correct_answer": 1,
            "explanation": "Um muro: 24 m² × 2 faces = 48 m². Quatro muros: 48 × 4 = 192 m².",
            "difficulty": "advanced",
            "source_assets": sa("page-001.jpg"),
            "section": "desafios",
        },
        {
            "id": "dg-des-006",
            "type": "multiple_choice",
            "topic": "area_applications",
            "question": (
                "Teto 5 m × 4 m e quatro paredes (5×2,5 e 4×2,5), descontando porta 2×0,8 "
                "e janela 1×1. Ordem correta de raciocínio:"
            ),
            "options": [
                "Somar áreas úteis e subtrair vãos",
                "Multiplicar todas as medidas juntas",
                "Usar só o perímetro",
                "Somar apenas alturas",
            ],
            "correct_answer": 0,
            "explanation": "Calcule cada superfície, some teto + paredes, subtraia porta e janela.",
            "difficulty": "advanced",
            "source_assets": sa("page-003.jpg"),
            "section": "desafios",
        },
        {
            "id": "dg-des-007",
            "type": "multiple_choice",
            "topic": "notable_quadrilaterals",
            "question": (
                "Sobre quadriláteros do Teste do caderno:\n"
                "I. Um losango na malha triangular tem quatro lados congruentes.\n"
                "II. O trapézio azul na malha não é paralelogramo.\n"
                "III. Todo quadrado é retângulo.\n"
                "IV. Todo trapézio possui dois pares de lados paralelos.\n\n"
                "Estão corretas apenas:"
            ),
            "options": ["I, II e III", "II e IV", "I e IV", "II, III e IV"],
            "correct_answer": 0,
            "explanation": "I, II e III corretas. IV é falsa — trapézio tem apenas um par de lados paralelos.",
            "difficulty": "advanced",
            "source_assets": sa("page-010.jpg"),
            "section": "desafios",
        },
        {
            "id": "dg-des-008",
            "type": "multiple_choice",
            "topic": "composite_area",
            "question": "Trapézio com bases 8 cm e 10 cm e altura 4 cm (item b do caderno). Área:",
            "visual": gf.trapezoid(8, 10, 4, top_label="8 cm", bottom_label="10 cm", height_label="4 cm"),
            "options": ["36 cm²", "32 cm²", "40 cm²", "18 cm²"],
            "correct_answer": 0,
            "explanation": "(8+10)×4÷2 = 36 cm².",
            "difficulty": "advanced",
            "source_assets": sa("page-004.jpg"),
            "section": "desafios",
        },
        {
            "id": "dg-des-009",
            "type": "multiple_choice",
            "topic": "square_area",
            "question": (
                "Quadrado de perímetro 52 cm. Medida do lado e área:"
            ),
            "options": ["Lado 13 cm, área 169 cm²", "Lado 26 cm, área 676 cm²", "Lado 13 cm, área 52 cm²", "Lado 52 cm, área 2704 cm²"],
            "correct_answer": 0,
            "explanation": "Lado = 52 ÷ 4 = 13 cm. Área = 13² = 169 cm².",
            "difficulty": "advanced",
            "source_assets": sa("page-001.jpg"),
            "section": "desafios",
        },
        {
            "id": "dg-des-010",
            "type": "multiple_choice",
            "topic": "polygon_diagonals",
            "question": (
                "Campo retangular 105 m × 68 m. A maior distância em linha reta "
                "dentro do campo (diagonal) é aproximadamente:"
            ),
            "options": ["173 m", "125 m", "105 m", "68 m"],
            "correct_answer": 1,
            "explanation": "Diagonal do retângulo — no caderno ≈ 125 m (maior que qualquer lado).",
            "difficulty": "advanced",
            "source_assets": sa("page-015.jpg"),
            "section": "desafios",
        },
    ]
    return items
