"""Conteúdo pedagógico da revisão Pedro — Espanhol PE 2º trimestre (Módulos 3 e 4)."""

from __future__ import annotations

REVIEW_ID = "pedro-pe-espanhol-2tri"
ASSET_PREFIX = "assets/pedro_pe_espanhol_2_tri"


def _src(page: str) -> dict:
    return {
        "asset": f"{ASSET_PREFIX}/{page}",
        "origin_type": "observed",
        "evidence": [f"Caderno de Espanhol — {page}"],
    }


def build_content() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Espanhol — PE 2º Trimestre",
        "subtitle": "Pedro · 6º ano · Módulos 3 (¿Cómo somos?) e 4 (¿A qué te dedicas?)",
        "language": "pt-BR",
        "discipline": "Espanhol",
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
                    "text": "Descrições físicas com ser, tener y llevar; género y número de sustantivos; "
                    "artículos; vocabulario de ropa y partes del cuerpo; profesiones y familia; "
                    "verbos trabajar, tener y estar. Reserve cerca de 55 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "👤", "title": "Descripciones", "text": "Alto · rubio · pelo liso"},
                        {"icon": "👕", "title": "Ropa", "text": "Llevar camisa · pendientes · gorra"},
                        {"icon": "🦵", "title": "Cuerpo", "text": "Brazo · pierna · ojo · nariz"},
                        {"icon": "⚖️", "title": "Género y número", "text": "Niño/niña · casas · peces"},
                        {"icon": "📰", "title": "Artículos", "text": "El/la · un/una · los/las"},
                        {"icon": "💼", "title": "Profesiones", "text": "Médico · bombero · profesor"},
                        {"icon": "👨‍👩‍👧", "title": "Familia", "text": "Padres · mellizos · abuelos"},
                        {"icon": "🔧", "title": "Verbos", "text": "Trabajar · tener · estar"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 3 — ¿Cómo somos? (descripciones y gramática)",
                        "Módulo 4 — ¿A qué te dedicas? (profesiones y familia)",
                        "Ser, tener, llevar y trabajar en presente",
                        "Recall — repaso de los dos módulos",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Observe os exemplos em espanhol.",
                            "tip": "Compare ser (permanente) con tener (partes del cuerpo) y llevar (ropa).",
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
                            "description": "Questões no estilo das atividades do caderno.",
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
            *_topic_descripciones(),
            *_topic_ser_tener_llevar(),
            *_topic_ropa_cuerpo(),
            *_topic_genero_numero(),
            *_topic_articulos(),
            *_topic_profesiones(),
            *_topic_familia(),
            *_topic_trabajar_tener_estar(),
        ],
    }


def _topic_descripciones() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "1. Descripciones físicas (Módulo 3)"},
            "topic_id": "descripciones_fisicas",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Para describir a alguien usamos información sobre **altura**, **tipo físico**, "
                "**color del pelo**, **vestimenta** y **edad**. En el caderno, Paloma, Julio, Juan y Lucía "
                "se presentan con frases como «Soy alta» o «Tengo el pelo negro».",
            },
            "topic_id": "descripciones_fisicas",
            "sources": [_src("page-001.jpg"), _src("page-003.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "📏", "title": "Altura", "text": "Alto/a · bajo/a · no muy alta"},
                    {"icon": "💇", "title": "Pelo", "text": "Negro, largo y liso · rubio y rizado"},
                    {"icon": "👕", "title": "Ropa", "text": "Camisa a rayas · top rosa · gorra roja"},
                    {"icon": "🎨", "title": "Tipo físico", "text": "Delgado/a · negro/a · rubio/a"},
                ],
            },
            "topic_id": "descripciones_fisicas",
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Ejemplos del caderno (actividad 2)",
                "headers": ["Persona", "Descripción (resumida)"],
                "rows": [
                    ["Paloma", "Pelo negro, largo y liso; alta; pendientes y camisa a rayas"],
                    ["Julio", "Negro, alto y delgado; camisa blanca"],
                    ["Juan", "Rubio, bajo; camiseta azul"],
                    ["Lucía", "Rubia, pelo largo y rizado; top rosa y gorra roja"],
                ],
            },
            "topic_id": "descripciones_fisicas",
        },
    ]


def _topic_ser_tener_llevar() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "2. Ser, tener y llevar — tres verbos para describir"},
            "topic_id": "ser_tener_llevar",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Cada verbo tiene un papel distinto: **ser + adjetivo** para rasgos más estables; "
                "**tener + sustantivo/adjetivo** para partes del cuerpo; **llevar** para ropa y accesorios.",
            },
            "topic_id": "ser_tener_llevar",
            "sources": [_src("page-007.jpg"), _src("page-008.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "¿Cuándo usar cada verbo?",
                "headers": ["Verbo", "Uso", "Ejemplo"],
                "rows": [
                    ["Ser", "Rasgos físicos generales", "Soy bajo y delgado · Ella es rubia"],
                    ["Tener", "Partes del cuerpo, edad", "Tengo el pelo negro, largo y liso · Tengo doce años"],
                    ["Llevar", "Ropa y accesorios", "Llevo pendientes y camisa a rayas · Lleva gorra roja"],
                ],
            },
            "topic_id": "ser_tener_llevar",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "¡Ojo!",
                "text": "No confundas: «Soy el pelo negro» está mal → «Tengo el pelo negro». "
                "Para ropa siempre llevar: «Llevo una camiseta azul».",
            },
            "topic_id": "ser_tener_llevar",
        },
    ]


def _topic_ropa_cuerpo() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "3. Ropa y partes del cuerpo"},
            "topic_id": "ropa_cuerpo",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "El caderno trabaja vocabulario de **prendas** (camisa, pantalones, gorra, pendientes…) "
                "y **partes del cuerpo** (brazo, pierna, ojo, nariz, rodilla…). "
                "En el poema de Rafael Alberti, **llevar** significa «usar ropa»: "
                "«Lleva falda blanca».",
            },
            "topic_id": "ropa_cuerpo",
            "sources": [_src("page-009.jpg"), _src("page-010.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "👔", "title": "Ropa", "text": "Camisa · camiseta · pantalones · vestido · gorra"},
                    {"icon": "👟", "title": "Calzado", "text": "Zapatos · zapatillas · calcetines"},
                    {"icon": "🦶", "title": "Cuerpo", "text": "Brazo · pierna · mano · pie · rodilla"},
                    {"icon": "👁️", "title": "Cara", "text": "Ojo · nariz · boca · oreja · frente · pelo"},
                ],
            },
            "topic_id": "ropa_cuerpo",
        },
        {
            "type": "callout",
            "content": {
                "variant": "info",
                "title": "¿Lo sabías?",
                "text": "En España se dice **falda**; en Hispanoamérica también **pollera**. "
                "Las gafas pueden llamarse **lentes** o **anteojos** según la región.",
            },
            "topic_id": "ropa_cuerpo",
        },
    ]


def _topic_genero_numero() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "4. Género y número de sustantivos y adjetivos"},
            "topic_id": "genero_numero",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "En español, casi todo sustantivo y adjetivo tiene **género** (masculino/femenino) "
                "y **número** (singular/plural). El cómic del caderno recuerda: **niño** termina en -o, "
                "**niña** en -a.",
            },
            "topic_id": "genero_numero",
            "sources": [_src("page-004.jpg"), _src("page-005.jpg"), _src("page-006.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Reglas principales",
                "headers": ["Regla", "Ejemplo"],
                "rows": [
                    ["-o / -e → femenino -a", "rubio → rubia · abogado → abogada"],
                    ["Consonante → +a", "profesor → profesora"],
                    ["Vocal → +s", "casa → casas · guapo → guapos"],
                    ["Consonante / í / ú → +es", "papel → papeles · rubí → rubíes"],
                    ["-z → -ces", "pez → peces · nariz → narices"],
                ],
            },
            "topic_id": "genero_numero",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Heterogenéricos:",
                "text": "Palabras con género distinto al portugués: el guante (a luva), la crema (o creme), "
                "la nariz (o nariz), el color (a cor).",
            },
            "topic_id": "genero_numero",
        },
    ]


def _topic_articulos() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "5. Artículos definidos e indefinidos"},
            "topic_id": "articulos",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Los **artículos definidos** (el, la, los, las) acompañan sustantivos conocidos. "
                "Los **indefinidos** (un, una, unos, unas) indican algo no identificado o mencionado por primera vez.",
            },
            "topic_id": "articulos",
            "sources": [_src("page-006.jpg"), _src("page-007.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Tabla de artículos",
                "headers": ["", "Singular", "Plural"],
                "rows": [
                    ["Definidos masc.", "el vestido", "los pantalones"],
                    ["Definidos fem.", "la falda", "las bufandas"],
                    ["Indefinidos masc.", "un sombrero", "unos calcetines"],
                    ["Indefinidos fem.", "una blusa", "unas gorras"],
                ],
            },
            "topic_id": "articulos",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "¡Ojo!",
                "text": "Ante sustantivo femenino singular que empieza por **a** o **ha** acentuada, "
                "se usa el artículo masculino: **el águila**, **un hada**.",
            },
            "topic_id": "articulos",
        },
    ]


def _topic_profesiones() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "6. Profesiones (Módulo 4)"},
            "topic_id": "profesiones",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "El Módulo 4 pregunta **¿A qué te dedicas?** — ¿Cuál es tu profesión? "
                "Aprendemos vocabulario de oficios y usamos **trabajar como** + profesión.",
            },
            "topic_id": "profesiones",
            "sources": [_src("page-012.jpg"), _src("page-017.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "👨‍⚕️", "title": "Salud", "text": "Médico/a · enfermero/a · dentista · veterinario/a"},
                    {"icon": "👨‍🏫", "title": "Educación", "text": "Profesor/a · dependiente"},
                    {"icon": "👨‍🚒", "title": "Servicios", "text": "Bombero · policía · cartero/a · taxista"},
                    {"icon": "🔨", "title": "Oficios", "text": "Albañil · mecánico/a · fontanero/a · pintor/a"},
                ],
            },
            "topic_id": "profesiones",
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Frases útiles",
                "headers": ["Pregunta / respuesta", "Ejemplo"],
                "rows": [
                    ["¿A qué se dedica…?", "Mi padre trabaja como dependiente"],
                    ["¿Qué es…?", "Ramón es cocinero · Alicia Elena es veterinaria"],
                    ["Profesión + género", "El abogado · la abogada · el actor · la actriz"],
                ],
            },
            "topic_id": "profesiones",
        },
    ]


def _topic_familia() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "7. Familia y parentesco"},
            "topic_id": "familia",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Los textos del caderno presentan familias variadas: Fernando y su hermana melliza Alicia; "
                "Beatriz con ocho personas en casa; Lucía que vive con sus abuelos jubilados. "
                "Preguntamos: **¿Con quién vives? ¿A qué se dedican tus familiares?**",
            },
            "topic_id": "familia",
            "sources": [_src("page-013.jpg"), _src("page-014.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Vocabulario de parentesco y situación laboral",
                "headers": ["Palabra", "Significado"],
                "rows": [
                    ["mellizos/as", "gemelos"],
                    ["ama de casa", "dona de casa"],
                    ["jubilado/a", "aposentado/a"],
                    ["en paro", "desempleado/a (sin trabajo)"],
                    ["abuelos/as", "avós"],
                    ["tía / tío", "tia / tio"],
                ],
            },
            "topic_id": "familia",
        },
        {
            "type": "callout",
            "content": {
                "variant": "info",
                "title": "Género entrevista:",
                "text": "Una **entrevista** es interacción entre entrevistador (preguntas) "
                "y entrevistado (respuestas) — como la de Alicia en el caderno.",
            },
            "topic_id": "familia",
        },
    ]


def _topic_trabajar_tener_estar() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "8. Trabajar, tener y estar en presente"},
            "topic_id": "trabajar_tener_estar",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "En el Módulo 4 conjugamos **trabajar** (trabajo, trabajas, trabaja…), "
                "**tener** (tengo, tienes, tiene…) y **estar** (estoy, estás, está…) para hablar "
                "de edad, situación laboral y estado.",
            },
            "topic_id": "trabajar_tener_estar",
            "sources": [_src("page-015.jpg"), _src("page-016.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Presente de indicativo (yo · tú · él/ella · nosotros)",
                "headers": ["Pronombre", "Trabajar", "Tener", "Estar"],
                "rows": [
                    ["Yo", "trabajo", "tengo", "estoy"],
                    ["Tú/Vos", "trabajas", "tienes", "estás"],
                    ["Él/Ella/Usted", "trabaja", "tiene", "está"],
                    ["Nosotros/as", "trabajamos", "tenemos", "estamos"],
                    ["Ellos/Ellas/Ustedes", "trabajan", "tienen", "están"],
                ],
            },
            "topic_id": "trabajar_tener_estar",
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "💼", "title": "Trabajar", "text": "Mis padres trabajan como dependientes"},
                    {"icon": "🎂", "title": "Tener", "text": "Tengo doce años · Lucía tiene dos hermanas"},
                    {"icon": "📍", "title": "Estar", "text": "Mis abuelos están jubilados · Estoy en primero"},
                    {"icon": "⚠️", "title": "Usted", "text": "¿Usted trabaja con el señor González? (3ª p.)"},
                ],
            },
            "topic_id": "trabajar_tener_estar",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Ser × Estar × Trabajar:",
                "text": "Tener doce años (edad) · Trabajar como profesor (oficio) · "
                "Estar jubilado (situación) · Ser estudiante (característica).",
            },
            "topic_id": "trabajar_tener_estar",
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
            {"type": "heading", "content": {"level": 3, "text": "1. Descripciones"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "👤", "title": "Datos", "text": "Altura · pelo · ropa · edad"},
                        {"icon": "✏️", "title": "Verbos", "text": "Ser · tener · llevar"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. Ser / Tener / Llevar"}},
            {
                "type": "comparison_table",
                "content": {
                    "caption": "Resumen",
                    "headers": ["Verbo", "Ejemplo"],
                    "rows": [
                        ["Ser", "Soy alto · Ella es rubia"],
                        ["Tener", "Tengo el pelo negro"],
                        ["Llevar", "Llevo camisa a rayas"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Ropa y cuerpo"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "👕", "title": "Prendas", "text": "Camisa · gorra · zapatillas"},
                        {"icon": "🦵", "title": "Cuerpo", "text": "Brazo · pierna · ojo · nariz"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Género y número"}},
            {
                "type": "comparison_table",
                "content": {
                    "caption": "Reglas clave",
                    "headers": ["Cambio", "Ejemplo"],
                    "rows": [
                        ["Femenino -a", "niño → niña"],
                        ["Plural -s", "casa → casas"],
                        ["Plural -es", "papel → papeles"],
                        ["-z → -ces", "nariz → narices"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Artículos"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "📌", "title": "Definidos", "text": "el · la · los · las"},
                        {"icon": "❓", "title": "Indefinidos", "text": "un · una · unos · unas"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "6. Profesiones"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "💼", "title": "Pregunta", "text": "¿A qué se dedica? · Trabaja como…"},
                        {"icon": "🏥", "title": "Ejemplos", "text": "Médico · bombero · profesor · albañil"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "7. Familia"}},
            {
                "type": "comparison_table",
                "content": {
                    "caption": "Palabras útiles",
                    "headers": ["Español", "Português"],
                    "rows": [
                        ["mellizos", "gêmeos"],
                        ["jubilado", "aposentado"],
                        ["en paro", "desempregado"],
                        ["ama de casa", "dona de casa"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "8. Trabajar / Tener / Estar"}},
            {
                "type": "comparison_table",
                "content": {
                    "caption": "Presente (yo)",
                    "headers": ["Verbo", "Forma"],
                    "rows": [
                        ["Trabajar", "trabajo · trabajamos"],
                        ["Tener", "tengo · tenemos"],
                        ["Estar", "estoy · estamos"],
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha da PE:",
                    "text": "Ser/tener/llevar en descripciones · concordancia de adjetivos · "
                    "heterogenéricos · usted con 3ª persona · trabajar como + profesión · "
                    "estar jubilado / en paro.",
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
                "id": "es-pe-001",
                "type": "multiple_choice",
                "topic": "descripciones_fisicas",
                "question": (
                    "Paloma dice: «Tengo el pelo negro, largo y liso. Soy alta y llevo pendientes "
                    "y camisa a rayas.» ¿Qué información describe sobre su vestimenta?"
                ),
                "options": [
                    "Que es rubia y baja.",
                    "Que lleva pendientes y camisa a rayas.",
                    "Que tiene el pelo rizado.",
                    "Que vive con sus abuelos.",
                ],
                "correct_answer": 1,
                "explanation": "Llevar indica ropa y accesorios: pendientes y camisa a rayas.",
                "difficulty": "basic",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "es-pe-002",
                "type": "multiple_choice",
                "topic": "descripciones_fisicas",
                "question": (
                    "Leia as afirmativas sobre descrições físicas:\n"
                    "I. «Soy alto» usa o verbo ser com adjetivo.\n"
                    "II. «Tengo el pelo negro» usa o verbo tener para partes do corpo.\n"
                    "III. «Llevo gorra roja» indica roupa ou acessório.\n"
                    "IV. «Estoy mexicano» é a forma correta para nacionalidade.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e III", "I e IV", "II e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e III corretas. Nacionalidade usa ser: Soy mexicano (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "es-pe-003",
                "type": "multiple_choice",
                "topic": "ser_tener_llevar",
                "question": (
                    "Para completar «_____ el pelo largo y rizado», ¿qué verbo es el más adecuado?"
                ),
                "options": ["Ser", "Estar", "Tener", "Llevar"],
                "correct_answer": 2,
                "explanation": "Partes del cuerpo y características del pelo usan tener: Tengo el pelo largo y rizado.",
                "difficulty": "basic",
                "source_assets": sa("page-008.jpg"),
                "section": "exercises",
            },
            {
                "id": "es-pe-004",
                "type": "multiple_choice",
                "topic": "ser_tener_llevar",
                "question": (
                    "En el poema «La niña que se va al mar», el verbo **llevar** en «Lleva falda blanca» "
                    "significa:"
                ),
                "options": [
                    "Guiar o conducir a alguien.",
                    "Estar de moda.",
                    "Llevar puesta una prenda de ropa.",
                    "Inducir una opinión.",
                ],
                "correct_answer": 2,
                "explanation": "En el poema, llevar = usar/llevar puesta la falda blanca.",
                "difficulty": "basic",
                "source_assets": sa("page-009.jpg"),
                "section": "exercises",
            },
            {
                "id": "es-pe-005",
                "type": "multiple_choice",
                "topic": "ropa_cuerpo",
                "question": (
                    "Leia as afirmativas sobre vocabulario del caderno:\n"
                    "I. «Gorra» es un accesorio para la cabeza.\n"
                    "II. «Rodilla» es una parte de la pierna.\n"
                    "III. «Camiseta» y «camisa» son exactamente la misma prenda.\n"
                    "IV. «Pendientes» son accesorios para las orejas.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, II e IV", "II e III", "III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Camiseta (manga corta) y camisa (formal) no son lo mismo (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-009.jpg"),
                "section": "exercises",
            },
            {
                "id": "es-pe-006",
                "type": "multiple_choice",
                "topic": "genero_numero",
                "question": "¿Cuál es la forma femenina correcta de «profesor»?",
                "options": ["profesora", "profesoro", "profesore", "profesoraso"],
                "correct_answer": 0,
                "explanation": "Sustantivos en consonante forman femenino con -a: profesor → profesora.",
                "difficulty": "basic",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "es-pe-007",
                "type": "multiple_choice",
                "topic": "genero_numero",
                "question": (
                    "Leia as afirmativas sobre género y número:\n"
                    "I. «Niña» es la forma femenina de «niño».\n"
                    "II. El plural de «pez» es «peces».\n"
                    "III. «El guante» es masculino en español y femenino en portugués (luva).\n"
                    "IV. «Casas» forma plural añadiendo -es a «casa».\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "II e III", "I, II e III", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e III corretas. Casa → casas (con -s, no -es) porque termina en vocal (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-006.jpg"),
                "section": "exercises",
            },
            {
                "id": "es-pe-008",
                "type": "multiple_choice",
                "topic": "articulos",
                "question": "¿Qué alternativa usa correctamente el artículo definido?",
                "options": [
                    "un vestido azul",
                    "el vestido / la falda",
                    "una pantalones",
                    "los una bufanda",
                ],
                "correct_answer": 1,
                "explanation": "Artículos definidos: el vestido (masc.), la falda (fem.). Un/una son indefinidos.",
                "difficulty": "basic",
                "source_assets": sa("page-007.jpg"),
                "section": "exercises",
            },
            {
                "id": "es-pe-009",
                "type": "multiple_choice",
                "topic": "articulos",
                "question": (
                    "Leia as afirmativas sobre artículos:\n"
                    "I. «Los pantalones» es plural masculino definido.\n"
                    "II. «Una blusa» es artículo indefinido femenino singular.\n"
                    "III. Ante «águila» acentuada se usa «la águila».\n"
                    "IV. «Unos calcetines» es indefinido masculino plural.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. Se usa el/un águila (masculino por la a acentuada) — III errada.",
                "difficulty": "intermediate",
                "source_assets": sa("page-007.jpg"),
                "section": "exercises",
            },
            {
                "id": "es-pe-010",
                "type": "multiple_choice",
                "topic": "profesiones",
                "question": (
                    "Según el caderno, ¿cuál profesión corresponde a quien apaga incendios "
                    "con manguera, casco y escalera?"
                ),
                "options": ["Albañil", "Bombero", "Fontanero", "Cartero"],
                "correct_answer": 1,
                "explanation": "La adivinanza del caderno describe al bombero (bombeiro).",
                "difficulty": "basic",
                "source_assets": sa("page-012.jpg"),
                "section": "exercises",
            },
            {
                "id": "es-pe-011",
                "type": "multiple_choice",
                "topic": "profesiones",
                "question": "¿Cuál frase expresa correctamente la profesión de alguien?",
                "options": [
                    "Mi padre es dependiente y trabaja en una tienda.",
                    "Mi padre está dependiente en una tienda.",
                    "Mi padre tiene dependiente.",
                    "Mi padre lleva dependiente.",
                ],
                "correct_answer": 0,
                "explanation": "Ser + profesión o trabajar como + oficio. «Está dependiente» no es correcto aquí.",
                "difficulty": "basic",
                "source_assets": sa("page-013.jpg"),
                "section": "exercises",
            },
            {
                "id": "es-pe-012",
                "type": "multiple_choice",
                "topic": "familia",
                "question": (
                    "Según el texto del caderno, Fernando y Alicia son…"
                ),
                "options": [
                    "Primos que viven con sus abuelos.",
                    "Mellizos (hermanos gemelos).",
                    "Padre e hija.",
                    "Compañeros de entrevista.",
                ],
                "correct_answer": 1,
                "explanation": "Fernando menciona a su hermana melliza Alicia — son gemelos.",
                "difficulty": "basic",
                "source_assets": sa("page-013.jpg"),
                "section": "exercises",
            },
            {
                "id": "es-pe-013",
                "type": "multiple_choice",
                "topic": "familia",
                "question": (
                    "Leia as afirmativas sobre los textos de familia:\n"
                    "I. Beatriz vive en una casa con ocho personas.\n"
                    "II. Lucía vive con sus abuelos jubilados.\n"
                    "III. «En paro» significa estar desempleado.\n"
                    "IV. La madre de Fernando es dependiente en una tienda de ropa.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "II e III", "I, II e III", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e III corretas. Carolina (madre de Fernando) es profesora de música (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-013.jpg"),
                "section": "exercises",
            },
            {
                "id": "es-pe-014",
                "type": "multiple_choice",
                "topic": "trabajar_tener_estar",
                "question": (
                    "Completa: «Mis padres _____ como dependientes y mis abuelos _____ jubilados.»"
                ),
                "options": [
                    "trabajan / están",
                    "trabajan / son",
                    "están / trabajan",
                    "tienen / están",
                ],
                "correct_answer": 0,
                "explanation": "Trabajar como + profesión; estar jubilados (situación laboral).",
                "difficulty": "basic",
                "source_assets": sa("page-016.jpg"),
                "section": "exercises",
            },
            {
                "id": "es-pe-015",
                "type": "multiple_choice",
                "topic": "trabajar_tener_estar",
                "question": (
                    "¿Cuál es la conjugación correcta de TENER para «yo» y «nosotros»?"
                ),
                "options": [
                    "tengo / tenemos",
                    "tienes / tenéis",
                    "tiene / tienen",
                    "tengo / tenéis",
                ],
                "correct_answer": 0,
                "explanation": "Tener: yo tengo, nosotros tenemos.",
                "difficulty": "basic",
                "source_assets": sa("page-015.jpg"),
                "section": "exercises",
            },
            {
                "id": "es-pe-016",
                "type": "multiple_choice",
                "topic": "trabajar_tener_estar",
                "question": (
                    "Leia as afirmativas sobre trabajar, tener y estar:\n"
                    "I. «Usted trabaja» usa la 3ª persona del singular.\n"
                    "II. «Tengo doce años» expresa edad con tener.\n"
                    "III. «Estoy en paro» indica situación de desempleo.\n"
                    "IV. «Trabajo como médico» usa trabajar + como + profesión.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 3,
                "explanation": "Las cuatro afirmativas son correctas según el caderno.",
                "difficulty": "intermediate",
                "source_assets": sa("page-018.jpg"),
                "section": "final_quiz",
            },
        ],
    }
