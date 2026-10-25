"""Conteúdo pedagógico da revisão Pedro — Espanhol PE 3º trimestre (Módulos 7–10)."""

from __future__ import annotations

REVIEW_ID = "pedro-pe-espanhol-3tri"
ASSET_PREFIX = "assets/pedro_pe_espanhol_3_tri"

_LOCALE_TOGGLE = {
    "default": "es",
    "primary": "es",
    "secondary": "pt",
    "primary_label": "Español",
    "secondary_label": "Português",
}


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
        "title": "Revisão de Espanhol — PE 3º Trimestre",
        "subtitle": "Pedro · 6º ano · Módulos 7 (A la mesa) a 10 (¿Qué hora es?)",
        "language": "pt-BR",
        "discipline": "Espanhol",
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
                    "text": "Alimentos y hábitos; el verbo gustar; frecuencia y medidas; "
                    "verbos regulares en presente; lecturas sobre alimentación; "
                    "animales con muy/mucho y saber/conocer/poner; números y la hora. "
                    "Reserve cerca de 60 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🍽️", "title": "A la mesa", "text": "Verduras · carnes · postres"},
                        {"icon": "❤️", "title": "Gustar", "text": "Me gusta / Me gustan"},
                        {"icon": "⏱️", "title": "Frecuencia", "text": "Siempre · a veces · nunca"},
                        {"icon": "⚖️", "title": "Medidas", "text": "Una docena · una barra"},
                        {"icon": "🔧", "title": "Regulares", "text": "Como · bebes · vivimos"},
                        {"icon": "📖", "title": "Lecturas", "text": "Fábulas · hambre · poemas"},
                        {"icon": "🐾", "title": "Animales", "text": "Muy vs mucho · saber/conocer"},
                        {"icon": "🕐", "title": "La hora", "text": "Son las tres y cuarto"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 7 — A la mesa (alimentos y gustar)",
                        "Módulo 8 — ¿Nosotros comemos? (verbos regulares)",
                        "Módulo 9 — Los animales (muy/mucho, saber, conocer, poner)",
                        "Módulo 10 — ¿Qué hora es? (números cardinales y horas)",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Observe os exemplos em espanhol.",
                            "tip": "En gustar, el verbo concuerda con la cosa gustada (singular o plural).",
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
                            "description": "Questões no estilo Lengua en práctica y Sigue estudiando.",
                            "tip": "Em questões I–IV, leia cada afirmativa separadamente.",
                        },
                        {
                            "title": "Prática escrita",
                            "panel": "escrita",
                            "panel_label": "Prática escrita",
                            "description": "Escreva palavras e frases curtas em espanhol — o corretor verifica na hora.",
                            "tip": "Revise acentos en números (dieciséis) y en la hora (y cuarto, y media).",
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
        "locale_toggle": _LOCALE_TOGGLE,
        "blocks": [
            *_topic_alimentos(),
            *_topic_gustar(),
            *_topic_frecuencia(),
            *_topic_medidas(),
            *_topic_regulares(),
            *_topic_lectura(),
            *_topic_animales(),
            *_topic_numeros_hora(),
        ],
    }


def _topic_alimentos() -> list:
    return [
        {
            "type": "heading",
            "content": {
                "level": 3,
                "text": "1. Alimentos y hábitos (Módulo 7)",
                "text_pt": "1. Alimentos e hábitos (Módulo 7)",
            },
            "topic_id": "alimentos_habitos",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "El **Módulo 7 — A la mesa** trabaja vocabulario de **comidas** y **hábitos**. "
                "En el caderno aparecen grupos como verduras, carnes, pescados, frutas, pastas, "
                "quesos y yogures. También lees los hábitos de Susana (desayuno con leche y pan), "
                "Carlos (sopa de pescado en la cena), Pedro (fruta en la merienda) y Rita (verdura y postre). "
                "Recuerda: **pez** = animal vivo; **pescado** = para comer.",
                "text_pt": "O **Módulo 7 — A la mesa** trabalha vocabulário de **comidas** e **hábitos**. "
                "No caderno aparecem grupos como verduras (vegetais), carnes, pescados, frutas, massas, "
                "queijos e iogurtes. Você também lê os hábitos de Susana (café da manhã com leite e pão), "
                "Carlos (sopa de peixe no jantar), Pedro (fruta no lanche da tarde) e Rita (verdura e sobremesa). "
                "Lembre: **pez** = animal vivo; **pescado** = peixe para comer.",
            },
            "topic_id": "alimentos_habitos",
            "sources": [_src("page-001.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {
                        "icon": "🌅",
                        "title": "Desayuno",
                        "title_pt": "Café da manhã",
                        "text": "leche · pan · cereales",
                        "text_pt": "leite · pão · cereais",
                    },
                    {
                        "icon": "🍲",
                        "title": "Comida/cena",
                        "title_pt": "Almoço/jantar",
                        "text": "sopa · tortilla · carne",
                        "text_pt": "sopa · tortilla · carne",
                    },
                    {
                        "icon": "🍎",
                        "title": "Merienda",
                        "title_pt": "Lanche",
                        "text": "papaya · plátano · yogur",
                        "text_pt": "mamão · banana · iogurte",
                    },
                    {
                        "icon": "🍮",
                        "title": "Postre",
                        "title_pt": "Sobremesa",
                        "text": "flan · helado · arroz con leche",
                        "text_pt": "flan · sorvete · arroz doce",
                    },
                ],
            },
            "topic_id": "alimentos_habitos",
        },
    ]


def _topic_gustar() -> list:
    return [
        {
            "type": "heading",
            "content": {
                "level": 3,
                "text": "2. El verbo gustar",
                "text_pt": "2. O verbo gustar",
            },
            "topic_id": "verbo_gustar",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "**Gustar** no funciona como «gostar» en portugués: el verbo concuerda con "
                "lo que gusta. **Me gusta** + singular o infinitivo (Me gusta la papaya · Me gusta cocinar). "
                "**Me gustan** + plural (Me gustan las manzanas). "
                "Usa pronombres átonos: **me, te, le, nos, os, les** (A mí me gusta…).",
                "text_pt": "**Gustar** não funciona igual ao «gostar» em português: o verbo concorda com "
                "a coisa de que se gosta. **Me gusta** + singular ou infinitivo (Me gusta la papaya · Me gusta cocinar). "
                "**Me gustan** + plural (Me gustan las manzanas). "
                "Use pronomes átonos: **me, te, le, nos, os, les** (A mí me gusta…).",
            },
            "topic_id": "verbo_gustar",
            "sources": [_src("page-002.jpg"), _src("page-005.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Gusta x gustan",
                "caption_pt": "Gusta x gustan",
                "headers": ["Forma", "Cuándo", "Ejemplo"],
                "headers_pt": ["Forma", "Quando", "Exemplo"],
                "rows": [
                    ["gusta", "1 cosa o infinitivo", "A María le gusta la tortilla"],
                    ["gustan", "2+ cosas (plural)", "A nosotros nos gustan los postres"],
                    ["no me gusta", "negación", "No me gusta nada cocinar"],
                ],
                "rows_pt": [
                    ["gusta", "1 coisa ou infinitivo", "A María le gusta la tortilla"],
                    ["gustan", "2+ coisas (plural)", "A nosotros nos gustan los postres"],
                    ["no me gusta", "negação", "No me gusta nada cocinar"],
                ],
            },
            "topic_id": "verbo_gustar",
        },
    ]


def _topic_frecuencia() -> list:
    return [
        {
            "type": "heading",
            "content": {
                "level": 3,
                "text": "3. Adverbios de frecuencia",
                "text_pt": "3. Advérbios de frequência",
            },
            "topic_id": "frecuencia_adverbios",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Para hablar de **con qué frecuencia** comes algo, usa adverbios del recuadro del caderno: "
                "**siempre, a menudo, frecuentemente, a veces, raramente, pocas veces, nunca, jamás**. "
                "Ejemplo del libro: «A la mañana **siempre** tomo leche con cereales. "
                "A mí **me gustan** mucho los cereales.»",
                "text_pt": "Para falar **com que frequência** você come algo, use advérbios da caixa do caderno: "
                "**siempre, a menudo, frecuentemente, a veces, raramente, pocas veces, nunca, jamás**. "
                "Exemplo do livro: «De manhã **siempre** tomo leche con cereales. "
                "A mí **me gustan** mucho los cereales.»",
            },
            "topic_id": "frecuencia_adverbios",
            "sources": [_src("page-003.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {
                        "icon": "🔁",
                        "title": "Siempre",
                        "title_pt": "Siempre (sempre)",
                        "text": "100 % del tiempo",
                        "text_pt": "100 % do tempo",
                    },
                    {
                        "icon": "📅",
                        "title": "A menudo",
                        "title_pt": "A menudo (often)",
                        "text": "muchas veces",
                        "text_pt": "muitas vezes",
                    },
                    {
                        "icon": "🎲",
                        "title": "A veces",
                        "title_pt": "A veces (às vezes)",
                        "text": "de vez en cuando",
                        "text_pt": "de vez em quando",
                    },
                    {
                        "icon": "🚫",
                        "title": "Nunca / jamás",
                        "title_pt": "Nunca / jamás",
                        "text": "0 % — negación fuerte",
                        "text_pt": "0 % — negação forte",
                    },
                ],
            },
            "topic_id": "frecuencia_adverbios",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Plural de alimentos:",
                "title_pt": "Plural dos alimentos:",
                "text": "Vocal → -s (manzana/manzanas). Consonante → -es (coliflor/coliflores). "
                "-z → -ces (pez/peces). Piña = ananá; patata = papa (según región).",
                "text_pt": "Vogal → -s (manzana/manzanas). Consoante → -es (coliflor/coliflores). "
                "-z → -ces (pez/peces). Piña = ananá; patata = papa (conforme a região).",
            },
            "topic_id": "frecuencia_adverbios",
        },
    ]


def _topic_medidas() -> list:
    return [
        {
            "type": "heading",
            "content": {
                "level": 3,
                "text": "4. Pesos, medidas y restaurante",
                "text_pt": "4. Pesos, medidas e restaurante",
            },
            "topic_id": "medidas_restaurante",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "El caderno enseña expresiones para **cantidades**: "
                "**una botella** de aceite, **una docena** de huevos, **una barra** de pan, "
                "**doscientos gramos** de jamón, **un tarro** de aceitunas, **un paquete** de mantequilla. "
                "En la **consumición** del restaurante aparecen platos como ensalada, filetes de ternera, "
                "lenguado, gaseosa y tapa de boquerones.",
                "text_pt": "O caderno ensina expressões de **quantidade**: "
                "**una botella** de aceite, **una docena** de huevos, **una barra** de pan, "
                "**doscientos gramos** de jamón, **un tarro** de aceitunas, **un paquete** de mantequilla. "
                "Na **consumición** (conta) do restaurante aparecem pratos como salada, filés de vitela, "
                "linguado, refrigerante e porção de boquerones.",
            },
            "topic_id": "medidas_restaurante",
            "sources": [_src("page-002.jpg"), _src("page-004.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Expresiones del recuadro",
                "caption_pt": "Expressões da caixa",
                "headers": ["Expresión", "Ejemplo"],
                "headers_pt": ["Expressão", "Exemplo"],
                "rows": [
                    ["una docena", "12 huevos"],
                    ["una barra", "pan tipo baguette"],
                    ["doscientos gramos", "jamón en bandeja"],
                    ["un tarro", "aceitunas en frasco"],
                ],
                "rows_pt": [
                    ["una docena", "12 ovos"],
                    ["una barra", "pão tipo baguete"],
                    ["doscientos gramos", "presunto na bandeja"],
                    ["un tarro", "azeitonas no pote"],
                ],
            },
            "topic_id": "medidas_restaurante",
        },
    ]


def _topic_regulares() -> list:
    return [
        {
            "type": "heading",
            "content": {
                "level": 3,
                "text": "5. Verbos regulares en presente",
                "text_pt": "5. Verbos regulares no presente",
            },
            "topic_id": "verbos_regulares",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "En el **Módulo 8**, los verbos regulares forman el presente así: "
                "quitas **-ar, -er, -ir** y añades las terminaciones de la persona. "
                "Ejemplos del caderno: **cenar** (cen-o, cen-as…), **comer** (com-o, com-es…), "
                "**partir** (part-o, part-es…). También practicas **desayunar, beber, lavar, cocinar, comprar**.",
                "text_pt": "No **Módulo 8**, os verbos regulares formam o presente assim: "
                "tira **-ar, -er, -ir** e acrescenta as terminações da pessoa. "
                "Exemplos do caderno: **cenar** (cen-o, cen-as…), **comer** (com-o, com-es…), "
                "**partir** (part-o, part-es…). Você também pratica **desayunar, beber, lavar, cocinar, comprar**.",
            },
            "topic_id": "verbos_regulares",
            "sources": [_src("page-007.jpg"), _src("page-009.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Terminaciones (presente de indicativo)",
                "caption_pt": "Terminações (presente de indicativo)",
                "headers": ["Persona", "-ar", "-er", "-ir"],
                "headers_pt": ["Pessoa", "-ar", "-er", "-ir"],
                "rows": [
                    ["yo", "-o", "-o", "-o"],
                    ["tú/vos", "-as", "-es", "-es"],
                    ["él/ella/usted", "-a", "-e", "-e"],
                    ["nosotros", "-amos", "-emos", "-imos"],
                    ["vosotros", "-áis", "-éis", "-ís"],
                    ["ellos/ustedes", "-an", "-en", "-en"],
                ],
                "rows_pt": [
                    ["yo (eu)", "-o", "-o", "-o"],
                    ["tú/vos (você)", "-as", "-es", "-es"],
                    ["él/ella/usted", "-a", "-e", "-e"],
                    ["nosotros (nós)", "-amos", "-emos", "-imos"],
                    ["vosotros", "-áis", "-éis", "-ís"],
                    ["ellos/ustedes", "-an", "-en", "-en"],
                ],
            },
            "topic_id": "verbos_regulares",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Pronunciación G y J:",
                "title_pt": "Pronúncia de G e J:",
                "text": "Ante **e** e **i**, las letras **g** y **j** suelen tener el **mismo sonido** "
                "(ej.: generoso, llegar, grano en la leyenda del maíz).",
                "text_pt": "Antes de **e** e **i**, as letras **g** e **j** costumam ter o **mesmo som** "
                "(ex.: generoso, llegar, grano na lenda do milho).",
            },
            "topic_id": "verbos_regulares",
            "sources": [_src("page-008.jpg")],
        },
    ]


def _topic_lectura() -> list:
    return [
        {
            "type": "heading",
            "content": {
                "level": 3,
                "text": "6. Lecturas: hambre, fábulas y poemas",
                "text_pt": "6. Leituras: fome, fábulas e poemas",
            },
            "topic_id": "lectura_hambre",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "El caderno mezcla **lectura** con reflexión social. "
                "«**A pesar de todo**» (Oche Califa) muestra una familia con poco alimento pero con cariño. "
                "El poema «**Niños de Somalia**» (Gloria Fuertes) contrasta *yo como… ellos no*. "
                "La fábula «**La lechera y el cántaro**» enseña no contar con lo que aún no tienes. "
                "Una **fábula** es narración breve, muchas veces con animales, con **moraleja**.",
                "text_pt": "O caderno mistura **leitura** com reflexão social. "
                "«**A pesar de todo**» (Oche Califa) mostra uma família com pouca comida, mas com carinho. "
                "O poema «**Niños de Somalia**» (Gloria Fuertes) contrasta *yo como… ellos no*. "
                "A fábula «**La lechera y el cántaro**» ensina a não contar com o que ainda não se tem. "
                "Uma **fábula** é narrativa curta, muitas vezes com animais, com **moraleja** (lição).",
            },
            "topic_id": "lectura_hambre",
            "sources": [_src("page-004.jpg"), _src("page-006.jpg"), _src("page-012.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {
                        "icon": "📜",
                        "title": "Fábula",
                        "title_pt": "Fábula",
                        "text": "Historia corta + moraleja",
                        "text_pt": "História curta + lição",
                    },
                    {
                        "icon": "🌍",
                        "title": "Hambre",
                        "title_pt": "Fome",
                        "text": "Derecho a la alimentación",
                        "text_pt": "Direito à alimentação",
                    },
                    {
                        "icon": "✍️",
                        "title": "Poema",
                        "title_pt": "Poema",
                        "text": "Estructura repetida de verbos",
                        "text_pt": "Estrutura repetida de verbos",
                    },
                ],
            },
            "topic_id": "lectura_hambre",
        },
    ]


def _topic_animales() -> list:
    return [
        {
            "type": "heading",
            "content": {
                "level": 3,
                "text": "7. Animales, muy/mucho y saber · conocer · poner",
                "text_pt": "7. Animais, muy/mucho e saber · conocer · poner",
            },
            "topic_id": "animales_muy_mucho",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "**Módulo 9 — Los animales**: perro, gato, ballena, jirafa, koala, murciélago… "
                "**Mucho/a/os/as** antes del sustantivo (muchos libros) o después del verbo (trabaja mucho). "
                "**Muy** antes de adjetivo o adverbio (muy calladito · muy bien) — **invariable**. "
                "Verbos irregulares en **yo**: **sé, conozco, pongo**. "
                "Con **tener/estar** describes estados: tener sed/hambre/miedo · estar cansado/contento.",
                "text_pt": "**Módulo 9 — Los animales**: cachorro (perro), gato, baleia, girafa, koala, morcego… "
                "**Mucho/a/os/as** antes do substantivo (muchos libros) ou depois do verbo (trabaja mucho). "
                "**Muy** antes de adjetivo ou advérbio (muy calladito · muy bien) — **invariável**. "
                "Verbos irregulares em **yo**: **sé, conozco, pongo**. "
                "Com **tener/estar** você descreve estados: sede/fome/medo · cansado/contento.",
            },
            "topic_id": "animales_muy_mucho",
            "sources": [_src("page-010.jpg"), _src("page-011.jpg"), _src("page-012.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Muy x mucho · saber x conocer",
                "caption_pt": "Muy x mucho · saber x conocer",
                "headers": ["Palabra", "Uso", "Ejemplo"],
                "headers_pt": ["Palavra", "Uso", "Exemplo"],
                "rows": [
                    ["mucho/a/os/as", "cantidad + sustantivo", "muchos perros"],
                    ["mucho", "después de verbo", "duermen mucho"],
                    ["muy", "intensidad + adj./adv.", "muy nervioso"],
                    ["saber", "saber datos (sé la respuesta)", "¿Sabes qué hora es?"],
                    ["conocer", "conocer personas/lugares", "Conozco a Elena"],
                    ["poner", "poner libros en estantería", "Pongo los libros aquí"],
                ],
                "rows_pt": [
                    ["mucho/a/os/as", "quantidade + substantivo", "muchos perros"],
                    ["mucho", "depois do verbo", "duermen mucho"],
                    ["muy", "intensidade + adj./adv.", "muy nervioso"],
                    ["saber", "saber fatos (sé la respuesta)", "¿Sabes qué hora es?"],
                    ["conocer", "conhecer pessoas/lugares", "Conozco a Elena"],
                    ["poner", "colocar livros na estante", "Pongo los libros aquí"],
                ],
            },
            "topic_id": "animales_muy_mucho",
        },
    ]


def _topic_numeros_hora() -> list:
    return [
        {
            "type": "heading",
            "content": {
                "level": 3,
                "text": "8. Números cardinales y la hora",
                "text_pt": "8. Números cardinais e a hora",
            },
            "topic_id": "numeros_hora",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "**Módulo 10**: números del **cero al mil** (treinta y tres, ciento seis, mil doscientos trece). "
                "Del **21 al 29** se escriben en una palabra: veintiuno… veintinueve. "
                "Para la hora preguntas **¿Qué hora es?** (singular). "
                "**Es la una** (1:00). **Son las dos y diez**, **son las tres y cuarto**, **son las seis y media**. "
                "Después de la media: **son las siete menos veinte**, **menos cuarto**, **menos cinco**.",
                "text_pt": "**Módulo 10**: números de **zero a mil** (treinta y tres, ciento seis, mil doscientos trece). "
                "Do **21 ao 29** escreve-se em uma palavra: veintiuno… veintinueve. "
                "Para a hora pergunta-se **¿Qué hora es?** "
                "**Es la una** (1:00). **Son las dos y diez**, **son las tres y cuarto**, **son las seis y media**. "
                "Depois da meia hora: **son las siete menos veinte**, **menos cuarto**, **menos cinco**.",
            },
            "topic_id": "numeros_hora",
            "sources": [_src("page-013.jpg"), _src("page-015.jpg"), _src("page-016.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Decir la hora",
                "caption_pt": "Dizer a hora",
                "headers": ["Reloj", "En español"],
                "headers_pt": ["Relógio", "Em espanhol"],
                "rows": [
                    ["1:05", "Es la una y cinco"],
                    ["3:15", "Son las tres y cuarto / y quince"],
                    ["6:30", "Son las seis y media / y treinta"],
                    ["5:45", "Son las seis menos cuarto"],
                    ["12:00", "Son las doce en punto"],
                ],
                "rows_pt": [
                    ["1:05", "Es la una y cinco (uma e cinco)"],
                    ["3:15", "Son las tres y cuarto (três e quinze)"],
                    ["6:30", "Son las seis y media (seis e meia)"],
                    ["5:45", "Son las seis menos cuarto (seis menos quarto)"],
                    ["12:00", "Son las doce en punto (doze em ponto)"],
                ],
            },
            "topic_id": "numeros_hora",
        },
    ]


def _section_summary() -> dict:
    return {
        "id": "summary",
        "type": "quick_summary",
        "title": "Resumo rápido",
        "locale_toggle": _LOCALE_TOGGLE,
        "blocks": [
            {
                "type": "panel_intro",
                "content": {
                    "title": "Mapa mental de la PE",
                    "title_pt": "Mapa mental da PE",
                    "text": "Repasa cada bloque. Si algo no quedó claro, vuelve a Explicaciones.",
                    "text_pt": "Revise cada bloco abaixo. Se algo ficou confuso, volte à aba Explicações.",
                },
            },
            {
                "type": "heading",
                "content": {
                    "level": 3,
                    "text": "1. Alimentos y gustar",
                    "text_pt": "1. Alimentos e gustar",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {
                            "icon": "🥗",
                            "title": "Vocabulario",
                            "title_pt": "Vocabulário",
                            "text": "verduras · pescado · postre",
                            "text_pt": "verduras · pescado · postre",
                        },
                        {
                            "icon": "❤️",
                            "title": "Gustar",
                            "title_pt": "Gustar",
                            "text": "me gusta / me gustan + cosa",
                            "text_pt": "me gusta / me gustan + coisa",
                        },
                    ],
                },
            },
            {
                "type": "heading",
                "content": {
                    "level": 3,
                    "text": "2. Frecuencia y medidas",
                    "text_pt": "2. Frequência e medidas",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {
                            "icon": "⏱️",
                            "title": "Adverbios",
                            "title_pt": "Advérbios",
                            "text": "siempre · a veces · nunca",
                            "text_pt": "siempre · a veces · nunca",
                        },
                        {
                            "icon": "📦",
                            "title": "Medidas",
                            "title_pt": "Medidas",
                            "text": "docena · barra · gramos",
                            "text_pt": "docena · barra · gramos",
                        },
                    ],
                },
            },
            {
                "type": "heading",
                "content": {
                    "level": 3,
                    "text": "3. Verbos regulares",
                    "text_pt": "3. Verbos regulares",
                },
            },
            {
                "type": "comparison_table",
                "content": {
                    "caption": "Raíz + terminación",
                    "caption_pt": "Raiz + terminação",
                    "headers": ["Grupo", "Ejemplo"],
                    "headers_pt": ["Grupo", "Exemplo"],
                    "rows": [
                        ["-ar", "desayuno · desayunas · desayunan"],
                        ["-er", "como · comes · comen"],
                        ["-ir", "vivo · vives · viven"],
                    ],
                    "rows_pt": [
                        ["-ar", "desayuno · desayunas · desayunan"],
                        ["-er", "como · comes · comen"],
                        ["-ir", "vivo · vives · viven"],
                    ],
                },
            },
            {
                "type": "heading",
                "content": {
                    "level": 3,
                    "text": "4. Animales y cuantificadores",
                    "text_pt": "4. Animais e quantificadores",
                },
            },
            {
                "type": "comparison_table",
                "content": {
                    "caption": "Muy / mucho",
                    "caption_pt": "Muy / mucho",
                    "headers": ["", "Regla"],
                    "headers_pt": ["", "Regra"],
                    "rows": [
                        ["mucho/a/os/as", "antes de sustantivo"],
                        ["muy", "antes de adjetivo/adverbio"],
                        ["sé / conozco / pongo", "yo irregular"],
                    ],
                    "rows_pt": [
                        ["mucho/a/os/as", "antes do substantivo"],
                        ["muy", "antes de adjetivo/advérbio"],
                        ["sé / conozco / pongo", "yo irregular"],
                    ],
                },
            },
            {
                "type": "heading",
                "content": {
                    "level": 3,
                    "text": "5. Números y hora",
                    "text_pt": "5. Números e hora",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {
                            "icon": "🔢",
                            "title": "Números",
                            "title_pt": "Números",
                            "text": "veintidós · ciento cinco · mil",
                            "text_pt": "veintidós · ciento cinco · mil",
                        },
                        {
                            "icon": "🕐",
                            "title": "Hora",
                            "title_pt": "Hora",
                            "text": "y cuarto · y media · menos diez",
                            "text_pt": "y cuarto · y media · menos diez",
                        },
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha de la PE:",
                    "title_pt": "Pegadinha da PE:",
                    "text": "Gustar concuerda con la cosa (no con «yo»). "
                    "Es la una (1 h). Mucho + sustantivo; muy + adjetivo. "
                    "Pez (vivo) ≠ pescado (comida). G/J ante e/i: mismo sonido.",
                    "text_pt": "Gustar concorda com a coisa (não com «yo»). "
                    "Es la una (1 h). Mucho + substantivo; muy + adjetivo. "
                    "Pez (vivo) ≠ pescado (comida). G/J antes de e/i: mesmo som.",
                },
            },
        ],
    }


def _written_exercises(sa) -> list[dict]:
    return [
        {
            "id": "es3-wr-001",
            "type": "written_language",
            "topic": "verbo_gustar",
            "question": "Complete em espanhol: «A mí _____ las manzanas.» (verbo gustar, plural)",
            "correct_answer": "me gustan",
            "accepted_answers": ["Me gustan"],
            "input_mode": "word",
            "explanation": "Manzanas es plural → me gustan.",
            "difficulty": "basic",
            "source_assets": sa("page-002.jpg"),
            "section": "escrita",
        },
        {
            "id": "es3-wr-002",
            "type": "written_language",
            "topic": "verbo_gustar",
            "question": "Complete: «No me _____ nada cocinar.» (gustar, singular negativo)",
            "correct_answer": "gusta",
            "accepted_answers": ["Gusta"],
            "input_mode": "word",
            "explanation": "Infinitivo cocinar → forma singular gusta.",
            "difficulty": "basic",
            "source_assets": sa("page-002.jpg"),
            "section": "escrita",
        },
        {
            "id": "es3-wr-003",
            "type": "written_language",
            "topic": "frecuencia_adverbios",
            "question": "Escreva em espanhol o advérbio que significa «sempre»:",
            "correct_answer": "siempre",
            "accepted_answers": ["Siempre"],
            "input_mode": "word",
            "explanation": "Siempre = 100 % del tiempo.",
            "difficulty": "basic",
            "source_assets": sa("page-003.jpg"),
            "section": "escrita",
        },
        {
            "id": "es3-wr-004",
            "type": "written_language",
            "topic": "medidas_restaurante",
            "question": "Complete a frase: «_____ de huevos.» (12 ovos — expressão do caderno)",
            "correct_answer": "Una docena",
            "accepted_answers": ["una docena", "Una docena de huevos"],
            "input_mode": "word",
            "explanation": "Una docena = 12 unidades.",
            "difficulty": "basic",
            "source_assets": sa("page-004.jpg"),
            "section": "escrita",
        },
        {
            "id": "es3-wr-005",
            "type": "written_language",
            "topic": "verbos_regulares",
            "question": "Conjugue «comer» para «nosotros» (uma palavra):",
            "correct_answer": "comemos",
            "accepted_answers": ["Comemos"],
            "input_mode": "word",
            "explanation": "Comer → nosotros comemos.",
            "difficulty": "basic",
            "source_assets": sa("page-007.jpg"),
            "section": "escrita",
        },
        {
            "id": "es3-wr-006",
            "type": "written_language",
            "topic": "verbos_regulares",
            "question": "Conjugue «desayunar» para «yo»:",
            "correct_answer": "desayuno",
            "accepted_answers": ["Desayuno"],
            "input_mode": "word",
            "explanation": "Verbos -ar en yo: terminación -o.",
            "difficulty": "basic",
            "source_assets": sa("page-009.jpg"),
            "section": "escrita",
        },
        {
            "id": "es3-wr-007",
            "type": "written_language",
            "topic": "animales_muy_mucho",
            "question": "Complete: «Los leones duermen _____.» (cantidad — mucho/muy)",
            "correct_answer": "mucho",
            "accepted_answers": ["Mucho"],
            "input_mode": "word",
            "mistake_hints": [{"contains": "muy", "message": "Mucho va después del verbo; muy intensifica adjetivos."}],
            "explanation": "Después del verbo duermen → mucho.",
            "difficulty": "basic",
            "source_assets": sa("page-011.jpg"),
            "section": "escrita",
        },
        {
            "id": "es3-wr-008",
            "type": "written_language",
            "topic": "animales_muy_mucho",
            "question": "Complete: «Gaturro está _____ calladito.» (intensificador)",
            "correct_answer": "muy",
            "accepted_answers": ["Muy"],
            "input_mode": "word",
            "explanation": "Muy + adjetivo calladito.",
            "difficulty": "basic",
            "source_assets": sa("page-011.jpg"),
            "section": "escrita",
        },
        {
            "id": "es3-wr-009",
            "type": "written_language",
            "topic": "numeros_hora",
            "question": "Escreva o número 33 em espanhol (com letras):",
            "correct_answer": "treinta y tres",
            "accepted_answers": ["Treinta y tres"],
            "input_mode": "word",
            "explanation": "Decenas + y + unidades.",
            "difficulty": "basic",
            "source_assets": sa("page-014.jpg"),
            "section": "escrita",
        },
        {
            "id": "es3-wr-010",
            "type": "written_language",
            "topic": "numeros_hora",
            "question": "Como se diz «São três e quarto» em espanhol?",
            "correct_answer": "Son las tres y cuarto.",
            "accepted_answers": [
                "Son las tres y cuarto",
                "son las tres y cuarto.",
                "Son las tres y quince.",
            ],
            "input_mode": "sentence",
            "explanation": "Son las + hora + y cuarto (15 minutos).",
            "difficulty": "intermediate",
            "source_assets": sa("page-015.jpg"),
            "section": "escrita",
        },
    ]


def build_exercises() -> dict:
    def sa(page: str) -> list[str]:
        return [f"{ASSET_PREFIX}/{page}"]

    mc = [
        {
            "id": "es3-pe-001",
            "type": "multiple_choice",
            "topic": "alimentos_habitos",
            "question": "Según el caderno, ¿qué desayuna Susana con sus hermanos?",
            "options": [
                "Pan con mantequilla y zumo",
                "Leche caliente con chocolate y pan con queso",
                "Solo fruta de papaya",
                "Hamburguesas con patatas fritas",
            ],
            "correct_answer": 1,
            "explanation": "Susana toma leche caliente con chocolate y come dos rebanadas de pan con queso.",
            "difficulty": "basic",
            "source_assets": sa("page-001.jpg"),
            "section": "exercises",
        },
        {
            "id": "es3-pe-002",
            "type": "multiple_choice",
            "topic": "alimentos_habitos",
            "question": (
                "Leia as afirmativas sobre vocabulario del Módulo 7:\n"
                "I. «Pescado» se refiere al animal ya preparado para comer.\n"
                "II. «Merienda» puede ser una comida ligera por la tarde.\n"
                "III. «Pez» y «pescado» son sinónimos exactos en todos los contextos.\n"
                "IV. Rita menciona postres como flan y helado de fresa.\n\n"
                "Estão corretas apenas:"
            ),
            "options": ["I e II", "I, II e IV", "II e III", "III e IV"],
            "correct_answer": 1,
            "explanation": "I, II e IV corretas. Pez = animal vivo; pescado = para comer (III errada).",
            "difficulty": "intermediate",
            "source_assets": sa("page-001.jpg"),
            "section": "exercises",
        },
        {
            "id": "es3-pe-003",
            "type": "multiple_choice",
            "topic": "verbo_gustar",
            "question": "¿Cuál frase usa **gustar** correctamente?",
            "options": [
                "Yo gusto las manzanas.",
                "Me gustan las manzanas.",
                "Me gusta las manzanas.",
                "Me gustan la manzana.",
            ],
            "correct_answer": 1,
            "explanation": "Manzanas (plural) → me gustan.",
            "difficulty": "basic",
            "source_assets": sa("page-002.jpg"),
            "section": "exercises",
        },
        {
            "id": "es3-pe-004",
            "type": "multiple_choice",
            "topic": "verbo_gustar",
            "question": (
                "Leia as afirmativas sobre gustar:\n"
                "I. «Me gusta preparar la comida» usa gusta porque el complemento es infinitivo.\n"
                "II. «A los niños les gusta mucho el chocolate» — gusta con singular chocolate.\n"
                "III. El pronombre siempre es «yo» delante de gustar.\n"
                "IV. «¿A ti te gustan las manzanas?» es una pregunta correcta.\n\n"
                "Estão corretas apenas:"
            ),
            "options": ["I e III", "II e IV", "I, II e IV", "I, II, III e IV"],
            "correct_answer": 2,
            "explanation": "I, II e IV corretas. Se usa me/te/le, no «yo» delante del verbo (III errada).",
            "difficulty": "intermediate",
            "source_assets": sa("page-002.jpg"),
            "section": "exercises",
        },
        {
            "id": "es3-pe-005",
            "type": "multiple_choice",
            "topic": "frecuencia_adverbios",
            "question": "¿Qué adverbio expresa **nunca** hacer algo?",
            "options": ["a menudo", "frecuentemente", "jamás", "a veces"],
            "correct_answer": 2,
            "explanation": "Jamás y nunca indican frecuencia cero.",
            "difficulty": "basic",
            "source_assets": sa("page-003.jpg"),
            "section": "exercises",
        },
        {
            "id": "es3-pe-006",
            "type": "multiple_choice",
            "topic": "medidas_restaurante",
            "question": "En el ejercicio de medidas, «_____ de pan» corresponde a una baguette. ¿Qué expresión completa?",
            "options": ["una docena", "una barra", "un tarro", "doscientos gramos"],
            "correct_answer": 1,
            "explanation": "Una barra de pan = pan alargado tipo baguette.",
            "difficulty": "basic",
            "source_assets": sa("page-004.jpg"),
            "section": "exercises",
        },
        {
            "id": "es3-pe-007",
            "type": "multiple_choice",
            "topic": "lectura_hambre",
            "question": (
                "Sobre la fábula «La lechera y el cántaro», ¿cuál moraleja encaja mejor "
                "con lo que ocurre cuando tropezó?"
            ),
            "options": [
                "Quien sueña demasiado puede perder lo que ya tiene.",
                "Siempre hay que comprar huevos en docena.",
                "La leche es más saludable que el pan.",
                "Los cantaros nunca se rompen.",
            ],
            "correct_answer": 0,
            "explanation": "Al tropezar, el cántaro se rompe y pierde la leche — no contar con lo no conseguido.",
            "difficulty": "basic",
            "source_assets": sa("page-004.jpg"),
            "section": "exercises",
        },
        {
            "id": "es3-pe-008",
            "type": "multiple_choice",
            "topic": "verbos_regulares",
            "question": "¿Cuál es la forma correcta de **beber** para «nosotros»?",
            "options": ["beben", "bebes", "bebemos", "bebo"],
            "correct_answer": 2,
            "explanation": "Beber → nosotros bebemos (-emos en -er).",
            "difficulty": "basic",
            "source_assets": sa("page-007.jpg"),
            "section": "exercises",
        },
        {
            "id": "es3-pe-009",
            "type": "multiple_choice",
            "topic": "verbos_regulares",
            "question": (
                "Leia as afirmativas sobre verbos regulares:\n"
                "I. La raíz de «vivir» es «viv».\n"
                "II. «Yo parto» es presente de indicativo de partir.\n"
                "III. Los verbos regulares cambian la raíz en todas las personas.\n"
                "IV. «Cocinar» termina en -ar.\n\n"
                "Estão corretas apenas:"
            ),
            "options": ["I e IV", "II e III", "I, II e IV", "I, II, III e IV"],
            "correct_answer": 2,
            "explanation": "I, II e IV corretas. Los regulares NO cambian la raíz (III errada).",
            "difficulty": "intermediate",
            "source_assets": sa("page-007.jpg"),
            "section": "exercises",
        },
        {
            "id": "es3-pe-010",
            "type": "multiple_choice",
            "topic": "lectura_hambre",
            "question": (
                "En el poema «Niños de Somalia», ¿a quién se refiere «Ellos no» "
                "al final del poema?"
            ),
            "options": [
                "A los lectores del libro",
                "A los niños de Somalia que no pueden comer",
                "A los verbos en plural",
                "A los autores del caderno",
            ],
            "correct_answer": 1,
            "explanation": "El poema contrasta quienes comen con niños que no tienen alimento.",
            "difficulty": "basic",
            "source_assets": sa("page-006.jpg"),
            "section": "exercises",
        },
        {
            "id": "es3-pe-011",
            "type": "multiple_choice",
            "topic": "animales_muy_mucho",
            "question": "¿Cuál frase usa **muy** o **mucho** correctamente?",
            "options": [
                "Hay muy libros en la estantería.",
                "Trabajan mucho en la oficina.",
                "Estoy mucho cansado.",
                "Tengo muy sed.",
            ],
            "correct_answer": 1,
            "explanation": "Mucho después del verbo. Muy + adjetivo (muy cansado); mucha sed con tener.",
            "difficulty": "basic",
            "source_assets": sa("page-011.jpg"),
            "section": "exercises",
        },
        {
            "id": "es3-pe-012",
            "type": "multiple_choice",
            "topic": "animales_muy_mucho",
            "question": (
                "Leia as afirmativas:\n"
                "I. «Conozco» es la forma yo de conocer.\n"
                "II. «Sé» puede ser yo de saber.\n"
                "III. «Pongo» es yo de poner.\n"
                "IV. «Muchas mariposas» concuerda mucho en género y número.\n\n"
                "Estão corretas apenas:"
            ),
            "options": ["I e II", "II e IV", "I, II e III", "I, II, III e IV"],
            "correct_answer": 3,
            "explanation": "Las cuatro afirmativas son correctas según el caderno.",
            "difficulty": "intermediate",
            "source_assets": sa("page-011.jpg"),
            "section": "exercises",
        },
    ]

    mc.extend([
        {
            "id": "es3-pe-013",
            "type": "multiple_choice",
            "topic": "numeros_hora",
            "question": "¿Cómo se escribe **45** en letras (como en el caderno)?",
            "options": ["cuarenta y cinco", "cincuenta y cuatro", "quince cuarenta", "cuatro cinco"],
            "correct_answer": 0,
            "explanation": "45 = cuarenta y cinco.",
            "difficulty": "basic",
            "source_assets": sa("page-014.jpg"),
            "section": "exercises",
        },
        {
            "id": "es3-pe-014",
            "type": "multiple_choice",
            "topic": "numeros_hora",
            "question": (
                "Leia as afirmativas sobre números y hora:\n"
                "I. Del 21 al 29 se escriben en una sola palabra (veintidós).\n"
                "II. A las 1:00 se dice «Es la una».\n"
                "III. «Son las cinco y veinticinco» es equivalente a y media.\n"
                "IV. Después de y media se puede usar «menos» para los minutos restantes.\n\n"
                "Estão corretas apenas:"
            ),
            "options": ["I e II", "II e IV", "I, II e IV", "I, II, III e IV"],
            "correct_answer": 2,
            "explanation": "I, II e IV corretas. Y veinticinco no es y media (III errada).",
            "difficulty": "intermediate",
            "source_assets": sa("page-015.jpg"),
            "section": "exercises",
        },
        {
            "id": "es3-pe-015",
            "type": "multiple_choice",
            "topic": "numeros_hora",
            "question": "Si el reloj marca las **6:30**, ¿cuál frase es correcta?",
            "options": [
                "Es la seis y media.",
                "Son las seis y media.",
                "Son las seis menos media.",
                "Es la seis y treinta y media.",
            ],
            "correct_answer": 1,
            "explanation": "Son las seis y media / y treinta (plural son las).",
            "difficulty": "basic",
            "source_assets": sa("page-015.jpg"),
            "section": "exercises",
        },
        {
            "id": "es3-pe-016",
            "type": "multiple_choice",
            "topic": "animales_muy_mucho",
            "question": (
                "Leia as afirmativas finales de revisión:\n"
                "I. El gato del ejercicio tiene miedo del perro → «Tiene miedo».\n"
                "II. «Saber» y «conocer» pueden traducirse ambos como «saber» en portugués, "
                "pero se usan en contextos distintos.\n"
                "III. Una fábula siempre tiene dioses griegos como protagonistas.\n"
                "IV. «Son las doce en punto» corresponde a 12:00.\n\n"
                "Estão corretas apenas:"
            ),
            "options": ["I e III", "I, II e IV", "II e IV", "I, II, III e IV"],
            "correct_answer": 1,
            "explanation": "I, II e IV corretas. Las fábulas suelen usar animales, no solo dioses (III errada).",
            "difficulty": "intermediate",
            "source_assets": sa("page-012.jpg"),
            "section": "final_quiz",
        },
    ])

    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "exercises": mc + _written_exercises(sa),
    }
