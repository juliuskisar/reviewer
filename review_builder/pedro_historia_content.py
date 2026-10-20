"""Conteúdo pedagógico da revisão Pedro — História PE 2º trimestre."""

from __future__ import annotations

REVIEW_ID = "pedro-pe-historia-2tri"
ASSET_PREFIX = "assets/pedro_pe_historia_2_tri"


def _src(page: str) -> dict:
    return {
        "asset": f"{ASSET_PREFIX}/{page}",
        "origin_type": "observed",
        "evidence": [f"Caderno de História — {page}"],
    }


def build_content() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de História — PE 2º Trimestre",
        "subtitle": "Pedro · 6º ano · Módulos 9, 10 e 11",
        "language": "pt-BR",
        "discipline": "História",
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
                    "text": "Civilizações pré-colombianas (maias, astecas e incas), a diversidade "
                    "africana com seus reinos e comércio trans-saara, e o Egito antigo — Nilo, "
                    "faraós, teocracia e religião. Reserve cerca de 1 hora.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🌎", "title": "América", "text": "Sociedades igualitárias e hierárquicas · códices"},
                        {"icon": "🏛️", "title": "Maias", "text": "Calendário · zero · estelas · aguadas"},
                        {"icon": "🦅", "title": "Astecas", "text": "Tenochtitlán · chinampas · pirâmide social"},
                        {"icon": "☀️", "title": "Incas", "text": "Cuzco · quipu · terraços · chasquis"},
                        {"icon": "🌍", "title": "África", "text": "Griôs · berberes · Gana · Congo"},
                        {"icon": "🏺", "title": "Egito", "text": "Nilo · nomos · teocracia · mumiificação"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 9 — América: maias, astecas e incas",
                        "Módulo 10 — África: diversidade e muitas histórias",
                        "Módulo 11 — Egito antigo",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Leia os cards e tabelas com calma.",
                            "tip": "Tente explicar cada civilização com suas palavras antes de avançar.",
                        },
                        {
                            "title": "Revise o Resumo rápido",
                            "panel": "summary",
                            "panel_label": "Resumo rápido",
                            "description": "Percorra os blocos-síntese — use como mapa mental para a PE.",
                            "tip": "Compare maias, astecas e incas: o que têm em comum e o que é diferente?",
                        },
                        {
                            "title": "Faça os Exercícios",
                            "panel": "exercises",
                            "panel_label": "Exercícios",
                            "description": "Questões no estilo Teste do caderno (p. 151, 169, 180): afirmativas I–IV e textos.",
                            "tip": "Responda sem olhar a explicação. Só depois clique em Verificar.",
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
                    "Você também pode usar as abas no topo a qualquer momento.",
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
            *_topic_america_peoples(),
            *_topic_mayans(),
            *_topic_aztecs(),
            *_topic_incas(),
            *_topic_africa_sources(),
            *_topic_africa_trade(),
            *_topic_africa_kingdoms(),
            *_topic_ancient_egypt(),
        ],
    }


def _topic_america_peoples() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "1. América pré-colombiana: povos e fontes"},
            "topic_id": "america_peoples",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Antes de 1492, milhares de povos habitavam a América. Alguns viviam em pequenos "
                "grupos igualitários (caça, pesca, coleta); outros formaram sociedades hierárquicas "
                "com cidades, agricultura e impérios.",
            },
            "topic_id": "america_peoples",
            "sources": [_src("page-012.jpg"), _src("page-025.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["", "Igualitárias", "Hierárquicas"],
                "rows": [
                    ["Organização", "Decisões coletivas, sem governo permanente", "Imperadores, nobres, tributos"],
                    ["Economia", "Caça, pesca, coleta", "Agricultura, artesanato, comércio"],
                    ["Exemplos", "Caçadores-coletores", "Maias, astecas, incas"],
                ],
            },
            "topic_id": "america_peoples",
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "📜", "title": "Códices", "text": "Livros manuscritos maias e astecas — calendário, história, rituais"},
                    {"icon": "🔥", "title": "Destruição", "text": "Conquistadores queimaram registros para apagar o passado indígena"},
                    {"icon": "🌽", "title": "Milho", "text": "Domesticado na Mesoamérica — alimento sagrado para maias e astecas"},
                ],
            },
            "topic_id": "america_peoples",
        },
    ]


def _topic_mayans() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "2. Maias"}, "topic_id": "mayans"},
        {
            "type": "paragraph",
            "content": {
                "text": "Os maias viveram em cidades independentes que compartilhavam tradições. "
                "Construíram centros cerimoniais com pirâmides, estelas e praças orientadas "
                "pelos pontos cardeais. Chichén Itzá e Tikal são exemplos famosos.",
            },
            "topic_id": "mayans",
            "sources": [_src("page-034.jpg"), _src("page-015.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "📅", "title": "Calendário", "text": "365 dias (18 meses de 20 + 5 extras) · observatórios astronômicos"},
                    {"icon": "0️⃣", "title": "Números", "text": "Sistema com conceito de zero — pontos e barras"},
                    {"icon": "💧", "title": "Água", "text": "Aguadas e canais em Tikal — reservatórios de pedra"},
                    {"icon": "🌽", "title": "Mitologia", "text": "Deuses criaram os 'homens de milho' — milho era sagrado"},
                ],
            },
            "topic_id": "mayans",
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Pirâmide social maia (do topo à base)",
                "headers": ["Camada", "Grupos"],
                "rows": [
                    ["1", "Soberano"],
                    ["2", "Corte: guerreiros, sacerdotes, funcionários"],
                    ["3", "Nobres"],
                    ["4", "Artesãos, mercadores, camponeses"],
                    ["5", "Escravizados (prisioneiros ou dívidas)"],
                ],
            },
            "topic_id": "mayans",
        },
    ]


def _topic_aztecs() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "3. Astecas"}, "topic_id": "aztecs"},
        {
            "type": "paragraph",
            "content": {
                "text": "No século XIV, os astecas se fixaram no vale do México e fundaram Tenochtitlán "
                "numa lagoa. A capital tinha templos, palácios, aquedutos e o grande mercado de "
                "Tlatelolco — descrito por Hernán Cortés como enorme e movimentado.",
            },
            "topic_id": "aztecs",
            "sources": [_src("page-014.jpg"), _src("page-033.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🦅", "title": "Fundação", "text": "Águia sobre cacto = sinal divino para fundar a cidade (Códice Mendoza)"},
                    {"icon": "🌱", "title": "Chinampas", "text": "Canteiros flutuantes em lagos — milho, feijão, tomate, cacau"},
                    {"icon": "🪙", "title": "Cacau", "text": "Sementes usadas como moeda além de bebida especial"},
                    {"icon": "👑", "title": "Huey Tlatoani", "text": "Imperador no topo da pirâmide social"},
                ],
            },
            "topic_id": "aztecs",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Lembre-se:",
                "text": "Roupas indicavam status: nobres usavam penas e algodão fino; "
                "camponeses usavam fibras de cacto. Mulheres teciam tecidos usados como tributo.",
            },
            "topic_id": "aztecs",
        },
    ]


def _topic_incas() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "4. Incas"}, "topic_id": "incas"},
        {
            "type": "paragraph",
            "content": {
                "text": "A partir do século XII, os incas expandiram um império nos Andes com capital em "
                "Cuzco. Construíram estradas, pontes, cidades (Machu Picchu) e terraços agrícolas "
                "para cultivar em terrenos montanhosos.",
            },
            "topic_id": "incas",
            "sources": [_src("page-032.jpg"), _src("page-041.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🧵", "title": "Quipu", "text": "Cordas com nós coloridos — registros de tributos e população"},
                    {"icon": "🏔️", "title": "Terraços", "text": "Degraus em encostas + canais de irrigação (Moray, Machu Picchu)"},
                    {"icon": "🦙", "title": "Lhamas", "text": "Transporte, lã, carne e couro"},
                    {"icon": "🏃", "title": "Chasquis", "text": "Mensageiros nos tambos — notícias rápidas pela estrada"},
                ],
            },
            "topic_id": "incas",
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Divisão da terra no império inca",
                "headers": ["Parte", "Destino"],
                "rows": [
                    ["Ayllus", "Comunidades camponesas — subsistência e troca"],
                    ["Sol", "Colheita para sacerdotes"],
                    ["Inca", "Suprimento do imperador e nobreza"],
                ],
            },
            "topic_id": "incas",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Sapa Inca:",
                "text": "O imperador era considerado filho do deus Sol. "
                "Adoravam Sol, Lua e Viracocha (deus criador).",
            },
            "topic_id": "incas",
        },
    ]


def _topic_africa_sources() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "5. África: diversidade e fontes históricas"},
            "topic_id": "africa_sources",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "A África é um continente vasto e diverso — desertos, florestas, cidades modernas "
                "e tradições milenares. Estudar sua história exige ir além de preconceitos sobre "
                "sociedades 'sem escrita'.",
            },
            "topic_id": "africa_sources",
            "sources": [_src("page-004.jpg"), _src("page-045.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🗣️", "title": "Griôs", "text": "Contadores de histórias — guardam memória de reinos e feitos"},
                    {"icon": "📖", "title": "Tradição oral", "text": "Mitos, poemas e relatos transmitidos por gerações"},
                    {"icon": "🏺", "title": "Arqueologia", "text": "Ferramentas, pinturas, múmias — vestígios materiais"},
                    {"icon": "✨", "title": "Orixás", "text": "Divindades iorubás — Xangô, Iemanjá, Ogum (influência no Brasil)"},
                ],
            },
            "topic_id": "africa_sources",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Lembre-se:",
                "text": "Sociedade sem escrita não significa sociedade sem cultura. "
                "O cérebro humano foi o primeiro 'arquivo' da história.",
            },
            "topic_id": "africa_sources",
        },
    ]


def _topic_africa_trade() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "6. Berberes e comércio trans-saara"}, "topic_id": "africa_trade"},
        {
            "type": "paragraph",
            "content": {
                "text": "Os berberes, povos nômades do Saara, organizaram caravanas com centenas de camelos "
                "desde o século V. Trocavam sal e cobre (norte) por ouro e noz-de-cola (sul). "
                "O sal era tão valioso quanto o ouro em algumas regiões.",
            },
            "topic_id": "africa_trade",
            "sources": [_src("page-039.jpg"), _src("page-027.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🐪", "title": "Caravanas", "text": "Até 1.000 camelos · viagens de ~3 meses"},
                    {"icon": "🧂", "title": "Sal ↔ Ouro", "text": "Troca essencial entre norte e sul do Saara"},
                    {"icon": "🔄", "title": "Trocas culturais", "text": "Berberes levavam notícias, crenças e costumes entre povos"},
                    {"icon": "🏜️", "title": "Oásis", "text": "Paradas com água e vegetação no deserto"},
                ],
            },
            "topic_id": "africa_trade",
        },
    ]


def _topic_africa_kingdoms() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "7. Reinos e impérios africanos"}, "topic_id": "africa_kingdoms"},
        {
            "type": "paragraph",
            "content": {
                "text": "Diversos reinos floresceram na África: Egito antigo, Meroé, Axum, Gana, Mali, "
                "Swahili e o Reino do Congo. Cada um tinha economia, hierarquia social e "
                "organização política próprias.",
            },
            "topic_id": "africa_kingdoms",
            "sources": [_src("page-011.jpg"), _src("page-035.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Dois reinos importantes do caderno",
                "headers": ["", "Império de Gana", "Reino do Congo"],
                "rows": [
                    ["Povo", "Soninké — agricultores e pastores", "Bantos — aldeias que formaram tribos"],
                    ["Riqueza", "Ouro trocado por sal", "Tributos em conchas (zimbo), sorgo, peles"],
                    ["Líder", "Caia-maga / gana", "Manicongo (ntotila) — figura sagrada"],
                    ["Sociedade", "Nobres, livres, servos, escravizados", "Pirâmide: corte, guarda, nobres, artesãos, camponeses"],
                ],
            },
            "topic_id": "africa_kingdoms",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Influência no Brasil:",
                "text": "Povos bantos e iorubás foram trazidos como escravizados. "
                "Palavras como moleque, cafuné, samba e alimentos como quiabo e dendê "
                "têm origem africana.",
            },
            "topic_id": "africa_kingdoms",
        },
    ]


def _topic_ancient_egypt() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "8. Egito antigo"}, "topic_id": "ancient_egypt"},
        {
            "type": "paragraph",
            "content": {
                "text": "Por volta de 4000 a.C., pastores nômades se fixaram no vale do Nilo. "
                "O rio inundava de julho a outubro, deixando húmus fértil — a 'terra negra' "
                "(Egito). Vilarejos formaram nomos; depois Menés unificou Alto e Baixo Egito (~3200 a.C.).",
            },
            "topic_id": "ancient_egypt",
            "sources": [_src("page-001.jpg"), _src("page-007.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🌊", "title": "Ciclo do Nilo", "text": "Cheia (jul–out) · vazante (nov–mar) · plantio e colheita"},
                    {"icon": "👑", "title": "Faraó", "text": "Poder absoluto · teocracia — representante dos deuses na Terra"},
                    {"icon": "🔺", "title": "Pirâmides", "text": "Túmulos monumentais com provisões para a vida após a morte"},
                    {"icon": "⚖️", "title": "Osíris", "text": "Julgamento: coração pesado na balança de Maat = condenação"},
                ],
            },
            "topic_id": "ancient_egypt",
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Estrutura social egípcia (resumo)",
                "headers": ["Camada", "Função"],
                "rows": [
                    ["Faraó", "Governante supremo — política, religião, exército"],
                    ["Vizir, escribas, sacerdotes", "Administração, registros, cultos"],
                    ["Militares, artesãos, comerciantes", "Defesa, produção, trocas"],
                    ["Camponeses", "Agricultura — trabalhavam em obras na cheia do Nilo"],
                    ["Escravizados", "Prisioneiros de guerra ou devedores do Estado"],
                ],
            },
            "topic_id": "ancient_egypt",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Pegadinha:",
                "text": "Mumiificação não garantia vida eterna para todos — "
                "pobres enterravam parentes na areia; o clima seco às vezes preservava os corpos.",
            },
            "topic_id": "ancient_egypt",
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
                    "text": "Revise cada tópico nos acordeões — cards e tabelas com o essencial.",
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "1. América pré-colombiana"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "⚖️", "title": "Igualitárias", "text": "Pequenos grupos · caça e coleta"},
                        {"icon": "🏛️", "title": "Hierárquicas", "text": "Cidades · impérios · tributos"},
                        {"icon": "📜", "title": "Fontes", "text": "Códices, arqueologia, tradição oral"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. Maias"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "📅", "title": "Calendário", "text": "365 dias · astronomia"},
                        {"icon": "0️⃣", "title": "Zero", "text": "Sistema numérico avançado"},
                        {"icon": "💧", "title": "Aguadas", "text": "Reservatórios de água em Tikal"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Astecas"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🦅", "title": "Tenochtitlán", "text": "Águia no cacto · capital na lagoa"},
                        {"icon": "🌱", "title": "Chinampas", "text": "Agricultura em canteiros flutuantes"},
                        {"icon": "🪙", "title": "Cacau", "text": "Moeda e bebida especial"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Incas"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🧵", "title": "Quipu", "text": "Registros com cordas e nós"},
                        {"icon": "🏔️", "title": "Terraços", "text": "Agricultura nas montanhas"},
                        {"icon": "🏃", "title": "Chasquis", "text": "Mensageiros nas estradas"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Fontes africanas"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🗣️", "title": "Griôs", "text": "Memória oral dos reinos"},
                        {"icon": "🏺", "title": "Arqueologia", "text": "Vestígios materiais"},
                        {"icon": "✨", "title": "Mitos", "text": "Narrativas sobre origem do mundo"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "6. Comércio trans-saara"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🐪", "title": "Berberes", "text": "Caravanas pelo Saara"},
                        {"icon": "🧂", "title": "Sal ↔ Ouro", "text": "Troca entre norte e sul"},
                        {"icon": "🔄", "title": "Cultura", "text": "Intercâmbio de ideias e costumes"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "7. Reinos africanos"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["Reino", "Destaque"],
                    "rows": [
                        ["Gana", "Ouro · caia-maga · Soninké"],
                        ["Congo", "Manicongo · zimbo · pirâmide social"],
                        ["Egito", "Nilo · faraó · ~3100 a.C."],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "8. Egito antigo"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🌊", "title": "Nilo", "text": "Cheia traz húmus · base da economia"},
                        {"icon": "👑", "title": "Teocracia", "text": "Faraó = deus vivo · poder absoluto"},
                        {"icon": "🔺", "title": "Pirâmides", "text": "Religião + poder · túmulos com provisões"},
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "Quipu não é escrita — é registro contábil. "
                    "Chinampas são astecas, terraços são incas, aguadas são maias.",
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
                "id": "hist-pe-001",
                "type": "multiple_choice",
                "topic": "america_peoples",
                "question": (
                    "Antes de 1492, no continente americano, havia povos com organizações "
                    "sociais muito diferentes. Assinale a alternativa correta:"
                ),
                "options": [
                    "Todos viviam em impérios com imperadores e tributos",
                    "Alguns grupos eram igualitários; outros formaram sociedades hierárquicas com cidades",
                    "Não havia agricultura em nenhuma região da América",
                    "Todos os povos usavam o mesmo idioma e a mesma religião",
                ],
                "correct_answer": 1,
                "explanation": "Havia desde caçadores-coletores em grupos pequenos até impérios como maias, astecas e incas.",
                "difficulty": "basic",
                "source_assets": sa("page-025.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-002",
                "type": "multiple_choice",
                "topic": "america_peoples",
                "question": (
                    "Leia as afirmativas sobre fontes da história americana:\n"
                    "I. Códices maias e astecas registravam calendários, rituais e história.\n"
                    "II. Conquistadores espanhóis destruíram muitos registros indígenas.\n"
                    "III. Arqueologia não ajuda a conhecer povos pré-colombianos.\n"
                    "IV. A tradição oral e vestígios materiais complementam o estudo.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Arqueologia é fundamental (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-036.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-003",
                "type": "multiple_choice",
                "topic": "mayans",
                "question": (
                    "Os maias se destacaram por avanços em astronomia, calendário e matemática. "
                    "Qual alternativa descreve corretamente um desses avanços?"
                ),
                "options": [
                    "Usavam apenas contagem com dedos, sem símbolos",
                    "Desenvolveram calendário de 365 dias e sistema numérico com zero",
                    "Não construíam observatórios astronômicos",
                    "Copiaram toda a astronomia dos europeus",
                ],
                "correct_answer": 1,
                "explanation": "Maias tinham calendário solar, observatórios (Chichén Itzá) e conceito de zero.",
                "difficulty": "basic",
                "source_assets": sa("page-034.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-004",
                "type": "multiple_choice",
                "topic": "mayans",
                "question": (
                    "Leia as afirmativas sobre os maias:\n"
                    "I. Construíram aguadas e canais para armazenar água da chuva.\n"
                    "II. Viviam em cidades independentes com tradições comuns.\n"
                    "III. Acreditavam que os deuses criaram os 'homens de milho'.\n"
                    "IV. Não praticavam agricultura intensiva.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "II e III", "I, II e III", "II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e III corretas. Maias praticavam agricultura intensiva com terraços e irrigação (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-047.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-005",
                "type": "multiple_choice",
                "topic": "aztecs",
                "question": (
                    "Segundo a lenda registrada no Códice Mendoza, os astecas fundaram Tenochtitlán "
                    "quando viram qual sinal divino?"
                ),
                "options": [
                    "Um leão sobre uma montanha",
                    "Uma águia pousada sobre um cacto no meio de uma lagoa",
                    "Um bastão de ouro que afundou facilmente no solo",
                    "Um lobo amamentando gêmeos",
                ],
                "correct_answer": 1,
                "explanation": "Huitzilopochtli indicou o lugar pelo sinal da águia no cacto (Códice Mendoza).",
                "difficulty": "basic",
                "source_assets": sa("page-033.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-006",
                "type": "multiple_choice",
                "topic": "aztecs",
                "question": (
                    "Leia as afirmativas sobre a economia asteca:\n"
                    "I. As chinampas eram canteiros flutuantes para cultivo em lagos.\n"
                    "II. Sementes de cacau eram usadas como moeda.\n"
                    "III. A agricultura era coletiva e garantia subsistência e tributos.\n"
                    "IV. Não havia comércio entre regiões do império.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e III", "I e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e III corretas. Tlatelolco era um grande mercado — havia comércio intenso (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-040.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-007",
                "type": "multiple_choice",
                "topic": "incas",
                "question": (
                    "O quipu era um sistema inca de cordas com nós coloridos usado principalmente para:"
                ),
                "options": [
                    "Escrever poemas e histórias em alfabeto",
                    "Registrar tributos, população e provisões armazenadas",
                    "Decorar templos sem função prática",
                    "Substituir completamente a agricultura",
                ],
                "correct_answer": 1,
                "explanation": "Quipu registrava dados administrativos — não era escrita alfabética.",
                "difficulty": "basic",
                "source_assets": sa("page-006.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-008",
                "type": "multiple_choice",
                "topic": "incas",
                "question": (
                    "Leia as afirmativas sobre os incas:\n"
                    "I. Construíram terraços agrícolas em encostas montanhosas.\n"
                    "II. Os chasquis eram mensageiros que percorriam estradas do império.\n"
                    "III. Toda a terra pertencia ao imperador e era dividida em ayllus, Sol e Inca.\n"
                    "IV. Não usavam lhamas para transporte de cargas.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e III", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Lhamas eram essenciais para transporte (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-044.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-009",
                "type": "multiple_choice",
                "topic": "africa_sources",
                "question": (
                    "Os griôs desempenham papel importante na história africana porque:"
                ),
                "options": [
                    "São reis que comandam exércitos",
                    "Guardam e transmitem oralmente a memória de reinos e feitos",
                    "Inventaram a escrita hieroglífica egípcia",
                    "Só existiam na Europa medieval",
                ],
                "correct_answer": 1,
                "explanation": "Griôs são 'sacos de palavras' — preservam nomes de reis e tradições por gerações.",
                "difficulty": "basic",
                "source_assets": sa("page-021.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-010",
                "type": "multiple_choice",
                "topic": "africa_sources",
                "question": (
                    "Leia o trecho: «Sociedades sem escrita não tinham cultura» — essa ideia é "
                    "preconceituosa. Sobre fontes africanas:\n"
                    "I. Mitos e tradição oral explicam origens e modos de pensar.\n"
                    "II. Arqueologia revela ferramentas, construções e objetos do passado.\n"
                    "III. Só documentos escritos europeus valem como fonte histórica.\n"
                    "IV. Griôs, poemas e música transmitem memória coletiva.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e IV", "II e III", "III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Fontes africanas vão além de documentos europeus (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-017.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-011",
                "type": "multiple_choice",
                "topic": "africa_trade",
                "question": (
                    "Além de trocar produtos, os berberes estimularam relações entre o norte "
                    "e o sul do Saara porque:"
                ),
                "options": [
                    "Impediam qualquer contato entre povos diferentes",
                    "Levavam informações sobre crenças, costumes e ideias entre os grupos",
                    "Só comerciavam com povos de mesma língua",
                    "Substituíam completamente sua cultura pela dos europeus",
                ],
                "correct_answer": 1,
                "explanation": "Caravanas berberes eram também mensageiros de cultura e conhecimento.",
                "difficulty": "basic",
                "source_assets": sa("page-017.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-012",
                "type": "multiple_choice",
                "topic": "africa_trade",
                "question": (
                    "Leia as afirmativas sobre o comércio trans-saara:\n"
                    "I. O sal era trocado por ouro em algumas regiões.\n"
                    "II. Caravanas podiam ter centenas de camelos.\n"
                    "III. Berberes viviam apenas em cidades europeias.\n"
                    "IV. Oásis eram paradas essenciais no deserto.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. Berberes são povos do norte da África, não europeus (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-039.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-013",
                "type": "multiple_choice",
                "topic": "africa_kingdoms",
                "question": (
                    "No Reino do Congo, o manicongo era visto como figura sagrada responsável por:"
                ),
                "options": [
                    "Apenas organizar festas, sem poder político",
                    "Justiça, fertilidade, abundância e proteção espiritual dos súditos",
                    "Comandar apenas exércitos europeus",
                    "Substituir o comércio de sal e ouro",
                ],
                "correct_answer": 1,
                "explanation": "O manicongo unia poder político e crença em poderes divinos sobre a natureza.",
                "difficulty": "basic",
                "source_assets": sa("page-019.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-014",
                "type": "multiple_choice",
                "topic": "africa_kingdoms",
                "question": (
                    "Leia as afirmativas sobre o Império de Gana:\n"
                    "I. Era rico em ouro, trocado por sal trazido por berberes.\n"
                    "II. O caia-maga demonstrava poder com roupas e joias de ouro.\n"
                    "III. A sociedade era totalmente igualitária, sem distinções.\n"
                    "IV. Foi fundado pelos Soninké, agricultores e pastores.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Gana tinha sociedade estratificada — nobres, livres, servos (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-035.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-015",
                "type": "multiple_choice",
                "topic": "ancient_egypt",
                "question": (
                    "A cheia anual do rio Nilo era fundamental para o Egito antigo porque:"
                ),
                "options": [
                    "Destruía todas as plantações sem deixar benefício",
                    "Deixava húmus fértil que permitia agricultura no deserto",
                    "Impedia qualquer forma de organização social",
                    "Só interessava aos comerciantes estrangeiros",
                ],
                "correct_answer": 1,
                "explanation": "A cheia (jul–out) depositava lodo fértil — base da economia agrícola egípcia.",
                "difficulty": "basic",
                "source_assets": sa("page-001.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-016",
                "type": "multiple_choice",
                "topic": "ancient_egypt",
                "question": (
                    "Leia as afirmativas sobre mumiificação e crenças egípcias:\n"
                    "I. Pobres também buscavam preservar os mortos para a vida após a morte.\n"
                    "II. Todo morto mummificado tinha garantia absoluta de vida eterna.\n"
                    "III. A secura do deserto às vezes preservava corpos enterrados na areia.\n"
                    "IV. Os egípcios não acreditavam em vida após a morte.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I e III", "II e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I e III corretas (Teste p. 180). II exagera; IV contradiz toda a religião egípcia.",
                "difficulty": "intermediate",
                "source_assets": sa("page-028.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-017",
                "type": "multiple_choice",
                "topic": "ancient_egypt",
                "question": (
                    "No Egito antigo, teocracia significa que o poder do faraó era baseado:"
                ),
                "options": [
                    "Apenas em eleições democráticas",
                    "Na crença de que ele era representante dos deuses na Terra",
                    "Somente no comércio com a Ásia",
                    "Na ausência total de religião na vida pública",
                ],
                "correct_answer": 1,
                "explanation": "Teo (deus) + cracia (poder): faraó era deus vivo — religião sustentava o governo.",
                "difficulty": "intermediate",
                "source_assets": sa("page-020.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist-pe-018",
                "type": "multiple_choice",
                "topic": "america_peoples",
                "question": (
                    "Maias, astecas e incas tinham pontos em comum, como:"
                ),
                "options": [
                    "Viver todos no mesmo território do atual Brasil",
                    "Sociedades hierárquicas, arquitetura complexa e culto a divindades ligadas ao céu",
                    "Ausência total de agricultura e de organização social",
                    "Uso exclusivo de quipus para registrar história",
                ],
                "correct_answer": 1,
                "explanation": "Três civilizações andinas e mesoamericanas: hierarquia, templos e astronomia/religião.",
                "difficulty": "intermediate",
                "source_assets": sa("page-010.jpg"),
                "section": "final_quiz",
            },
        ],
    }
