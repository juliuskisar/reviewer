"""Conteúdo pedagógico da revisão Pedro — História PE 3º trimestre (Módulos 14 e 15)."""

from __future__ import annotations

REVIEW_ID = "pedro-pe-historia-3tri"
ASSET_PREFIX = "assets/pedro_pe_historia_3_tri"


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
        "title": "Revisão de História — PE 3º Trimestre",
        "subtitle": "Pedro · 6º ano · Módulos 14 e 15",
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
                    "text": "Roma antiga: da lenda de Rômulo e Remo à república e ao império, "
                    "vida na cidade, gladiadores, cristianismo, crise, divisão e queda do "
                    "Império Romano do Ocidente (476). Reserve cerca de 1 hora.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🐺", "title": "Origens", "text": "Lenda · legado · latim e direito"},
                        {"icon": "🏛️", "title": "República", "text": "Res publica · patrícios · plebeus"},
                        {"icon": "📜", "title": "Leis", "text": "Doze Tábuas · consules · Senado"},
                        {"icon": "🗺️", "title": "Expansão", "text": "Mediterrâneo · triunfos"},
                        {"icon": "🏙️", "title": "Cidade", "text": "Insulae · termopólio · anfiteatros"},
                        {"icon": "⚔️", "title": "Crise e fim", "text": "Divisão · bárbaros · 476"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 14 — Origens dos romanos e República",
                        "Módulo 15 — Império, crise e fim do Ocidente",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Leia cards e tabelas com calma.",
                            "tip": "Monte uma linha do tempo: Monarquia → República → Império → 476.",
                        },
                        {
                            "title": "Revise o Resumo rápido",
                            "panel": "summary",
                            "panel_label": "Resumo rápido",
                            "description": "Percorra os blocos-síntese — use como mapa mental para a PE.",
                            "tip": "Compare Ocidente e Oriente depois da divisão de Teodósio.",
                        },
                        {
                            "title": "Faça os Exercícios",
                            "panel": "exercises",
                            "panel_label": "Exercícios",
                            "description": "Questões no estilo Teste do caderno: afirmativas I–IV e textos.",
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
            *_topic_roman_origins(),
            *_topic_republic_birth(),
            *_topic_republic_institutions(),
            *_topic_republic_expansion(),
            *_topic_empire_city(),
            *_topic_empire_society(),
            *_topic_empire_religion(),
            *_topic_crisis_and_fall(),
        ],
    }


def _topic_roman_origins() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "1. Origens dos romanos e legado"},
            "topic_id": "roman_origins",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "A lenda de Rômulo e Remo explica simbolicamente a fundação de Roma: gêmeos "
                "filhos de Marte, amamentados por uma loba, que mataram o tirano Amulius e "
                "fundaram uma cidade às margens do Tibre. Mesmo sendo lenda, ela mostra valores "
                "romanos — coragem, origem divina e destino político.",
            },
            "topic_id": "roman_origins",
            "sources": [_src("page-053.jpg"), _src("page-050.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🏛️", "title": "Arquitetura", "text": "Arcos, domos, concreto — inspiram monumentos até hoje"},
                    {"icon": "⚖️", "title": "Direito", "text": "Lei romana base de muitos sistemas jurídicos"},
                    {"icon": "🏛️", "title": "Política", "text": "Senado, república, cidadania"},
                    {"icon": "✝️", "title": "Religião", "text": "Cristianismo se espalhou pelo império"},
                ],
            },
            "topic_id": "roman_origins",
        },
    ]


def _topic_republic_birth() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "2. Da monarquia à república"},
            "topic_id": "republic_birth",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Depois de expulsar os reis, os romanos criaram a república: o poder público "
                "(res publica) deveria ser de interesse de todos, não de uma só pessoa. "
                "Na prática, patrícios (nobres) concentravam o Senado e os cargos; plebeus "
                "(maioria) lutaram por direitos — tribuno da plebe, assembleias e leis escritas.",
            },
            "topic_id": "republic_birth",
            "sources": [_src("page-045.jpg"), _src("page-035.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Grupo", "Papel na República (início)"],
                "rows": [
                    ["Patrícios", "Senado, magistraturas, grandes terras"],
                    ["Plebeus", "Romans de condição popular, sem direitos políticos plenos"],
                    ["Res publica", "Ideia de governo coletivo e bem comum (Cícero)"],
                ],
            },
            "topic_id": "republic_birth",
        },
    ]


def _topic_republic_institutions() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "3. Instituições republicanas e Lei das Doze Tábuas"},
            "topic_id": "republic_institutions",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Os cônsules comandavam exército e administração, mas dividiam o poder com "
                "Senado, assembleias e outros magistrados. Por volta de 450 a.C., a Lei das "
                "Doze Tábuas fixou regras por escrito — plebeus passaram a conhecer as "
                "'regras do jogo' e limitar abusos dos patrícios.",
            },
            "topic_id": "republic_institutions",
            "sources": [_src("page-035.jpg"), _src("page-030.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "👥", "title": "Cônsules", "text": "Dois por ano · exército e convocação de assembleias"},
                    {"icon": "🏛️", "title": "Senado", "text": "Patrícios · orientava política externa e finanças"},
                    {"icon": "📜", "title": "Doze Tábuas", "text": "Primeiras leis escritas · direitos dos plebeus"},
                    {"icon": "⚖️", "title": "Censor", "text": "Organizava hierarquia social e cargos"},
                ],
            },
            "topic_id": "republic_institutions",
        },
    ]


def _topic_republic_expansion() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "4. Expansão republicana"},
            "topic_id": "republic_expansion",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Entre o fim das guerras púnicas (201 a.C.) e o início do império (31 a.C.), "
                "Roma conquistou territórios em torno do Mediterrâneo — Hispania, Gália, "
                "partes da África e do Oriente. Vitórias eram celebradas com triunfos: desfiles "
                "com prisioneiros, espólios e o general em carro triunfal.",
            },
            "topic_id": "republic_expansion",
            "sources": [_src("page-040.jpg"), _src("page-030.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Mediterrâneo:",
                "text": "Controlar o 'mar interior' garantia rotas comerciais, grãos e tropas — "
                "Roma passou a chamar o mar de 'nosso'.",
            },
            "topic_id": "republic_expansion",
        },
    ]


def _topic_empire_city() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "5. Vida na cidade romana"},
            "topic_id": "empire_city",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Cidades romanas tinham ruas pavimentadas, aquedutos, fóruns e edifícios "
                "públicos. Os pobres viviam em insulae (prédios altos); no térreo havia "
                "lojas e termopólios (barracas de comida pronta). Teatros, anfiteatros e "
                "circos ofereciam lazer — gladiadores e corridas de carroças.",
            },
            "topic_id": "empire_city",
            "sources": [_src("page-025.jpg"), _src("page-002.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🏢", "title": "Insulae", "text": "Apartamentos — pobres nos andares altos"},
                    {"icon": "🍲", "title": "Termopólio", "text": "Comida pronta para quem não cozinhava em casa"},
                    {"icon": "🛣️", "title": "Estradas", "text": "Exército, comércio e ideias pelo império"},
                    {"icon": "🏟️", "title": "Anfiteatro", "text": "Lutas de gladiadores e espetáculos"},
                ],
            },
            "topic_id": "empire_city",
        },
    ]


def _topic_empire_society() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "6. Sociedade, mulheres e gladiadores"},
            "topic_id": "empire_society",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "Roma era patriarcal: homens dominavam política e exército. Mulheres ficavam "
                "sob tutela masculina, mas podiam administrar a casa (mater familias) e, "
                "no império, algumas mulheres ricas gerenciavam negócios. Gladiadores eram "
                "combates espetaculares que entreteriam e reforçavam o poder do Estado.",
            },
            "topic_id": "empire_society",
            "sources": [_src("page-020.jpg"), _src("page-003.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Sobre lutas de gladiadores (Teste do caderno)",
                "headers": ["Afirmativa", "Avaliação"],
                "rows": [
                    ["II. Espectáculo que reafirma o poder do Estado", "Correta"],
                    ["IV. Violência aceita pela sociedade romana", "Correta"],
                    ["I. Ritual religioso oferecendo vencido a Marte", "Discussão — não é a principal ideia do teste"],
                    ["III. Elite romana lutava por comando do exército", "Incorreta"],
                ],
            },
            "topic_id": "empire_society",
        },
    ]


def _topic_empire_religion() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "7. Religião: pagãos, cristianismo e Édito de Milão"},
            "topic_id": "empire_religion",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "No século II, imperadores como Marco Aurélio conduziam sacrifícios aos deuses "
                "tradicionais (Júpiter). No século IV, Constantino apoiou o cristianismo. "
                "O Édito de Milão (313) garantiu liberdade religiosa — cristãos e outros "
                "poderiam praticar sua fé sem perseguição estatal.",
            },
            "topic_id": "empire_religion",
            "sources": [_src("page-004.jpg"), _src("page-005.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🐂", "title": "Sacrifícios", "text": "Religião oficial ligada ao poder imperial"},
                    {"icon": "✝️", "title": "Cristianismo", "text": "Cresceu no império · perseguições depois tolerância"},
                    {"icon": "📜", "title": "Édito de Milão", "text": "313 — liberdade de culto"},
                    {"icon": "👑", "title": "Constantino", "text": "Aproximação Igreja e Estado"},
                ],
            },
            "topic_id": "empire_religion",
        },
    ]


def _topic_crisis_and_fall() -> list:
    return [
        {
            "type": "heading",
            "content": {"level": 3, "text": "8. Crise, divisão, bárbaros e queda (476)"},
            "topic_id": "crisis_and_fall",
        },
        {
            "type": "paragraph",
            "content": {
                "text": "No século IV, Teodósio dividiu o império: Ocidente (capital Roma) e Oriente "
                "(Constantinopla). No Ocidente, crises econômicas, ruralização, exército "
                "enfraquecido e invasões de povos chamados 'bárbaros' (germanos, hunos, alanos) "
                "fragmentaram o poder. Em 476, o último imperador do Ocidente foi deposto — "
                "marco tradicional do fim do Império Romano do Ocidente.",
            },
            "topic_id": "crisis_and_fall",
            "sources": [_src("page-015.jpg"), _src("page-006.jpg"), _src("page-010.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Conceito", "Significado no caderno"],
                "rows": [
                    ["Bárbaro", "Nome dado por povos a estrangeiros de cultura diferente — não significa 'inferior' universal"],
                    ["Ruralização", "Mudança da vida urbana para o campo"],
                    ["476", "Queda do Império Romano do Ocidente"],
                    ["Fusão cultural", "Herança romana + elementos germânicos → nova sociedade"],
                ],
            },
            "topic_id": "crisis_and_fall",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Pegadinha:",
                "text": "Édito de Milão ≠ cristianismo oficial obrigatório. "
                "Bárbaro ≠ sempre 'selvagem' — é visão do outro.",
            },
            "topic_id": "crisis_and_fall",
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
            {"type": "heading", "content": {"level": 3, "text": "1. Origens"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🐺", "title": "Lenda", "text": "Rômulo e Remo · fundação de Roma"},
                        {"icon": "🏛️", "title": "Legado", "text": "Direito · arquitetura · latim"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. República"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "📜", "title": "Res publica", "text": "Bem comum · governo coletivo"},
                        {"icon": "⚖️", "title": "Plebeus", "text": "Conquista de direitos e leis escritas"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Instituições"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "👥", "title": "Cônsules", "text": "Exército + administração"},
                        {"icon": "📜", "title": "Doze Tábuas", "text": "450 a.C. · leis conhecidas por todos"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Expansão"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🗺️", "title": "Mediterrâneo", "text": "Conquistas republicanas"},
                        {"icon": "🏆", "title": "Triunfo", "text": "Desfile de vitória militar"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Cidade"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🏢", "title": "Insulae", "text": "Moradia dos pobres"},
                        {"icon": "🏟️", "title": "Lazer", "text": "Teatro · circo · gladiadores"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "6. Sociedade"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "👩", "title": "Mulheres", "text": "Tutela · mater familias"},
                        {"icon": "⚔️", "title": "Gladiadores", "text": "Espectáculo + poder do Estado"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "7. Religião"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🐂", "title": "Pagãos", "text": "Sacrifícios a Júpiter"},
                        {"icon": "✝️", "title": "313", "text": "Édito de Milão · liberdade religiosa"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "8. Queda"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🗺️", "title": "Divisão", "text": "Ocidente × Oriente (Teodósio)"},
                        {"icon": "📅", "title": "476", "text": "Fim do Império Romano do Ocidente"},
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "Oriente (Bizâncio) continuou após 476. "
                    "Gladiadores não eram senadores lutando por comando.",
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
                "id": "hist3-pe-001",
                "type": "multiple_choice",
                "topic": "roman_origins",
                "question": (
                    "A lenda de Rômulo e Remo, presente no caderno, serve principalmente para:"
                ),
                "options": [
                    "Provar cientificamente a data exata da fundação de Roma",
                    "Explicar simbolicamente origens e valores associados à cidade de Roma",
                    "Mostrar que os romanos não tinham religião",
                    "Demonstrar que Roma foi fundada por gregos",
                ],
                "correct_answer": 1,
                "explanation": "Lendas transmitem sentido cultural — não são relatórios científicos.",
                "difficulty": "basic",
                "source_assets": sa("page-053.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-002",
                "type": "multiple_choice",
                "topic": "roman_origins",
                "question": (
                    "Leia as afirmativas sobre o legado romano:\n"
                    "I. O latim influenciou línguas europeias.\n"
                    "II. Ideias de direito e Senado ecoam até hoje.\n"
                    "III. Roma não deixou marcas na arquitetura ocidental.\n"
                    "IV. O cristianismo se difundiu pelo império.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Arcos e domos romanos inspiram monumentos (III falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-053.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-003",
                "type": "multiple_choice",
                "topic": "republic_birth",
                "question": (
                    "Para Cícero e autores citados no caderno, res publica significa:"
                ),
                "options": [
                    "Propriedade privada de cada família patrícia",
                    "A coisa pública — o que pertence a todos e deve ser cuidado coletivamente",
                    "Governo de um único rei divino",
                    "Território apenas das colônias na Gália",
                ],
                "correct_answer": 1,
                "explanation": "Res publica opõe interesse privado ao bem comum da cidade.",
                "difficulty": "basic",
                "source_assets": sa("page-045.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-004",
                "type": "multiple_choice",
                "topic": "republic_birth",
                "question": (
                    "Leia as afirmativas sobre patrícios e plebeus no início da República:\n"
                    "I. Plebeus eram maioria da população.\n"
                    "II. Patrícios concentravam decisões no Senado.\n"
                    "III. Todos os romanos tinham iguais direitos políticos desde o primeiro dia.\n"
                    "IV. Plebeus pressionaram por conquistas como leis escritas.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Igualdade política foi gradual (III falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-045.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-005",
                "type": "multiple_choice",
                "topic": "republic_institutions",
                "question": (
                    "Segundo Políbio e o caderno, os cônsules na República romana:"
                ),
                "options": [
                    "Governavam sozinhos acima de todas as instituições, como reis absolutos",
                    "Compartilhavam o governo com Senado, assembleias e outros magistrados",
                    "Eram escolhidos apenas entre plebeus sem participação patrícia",
                    "Não tinham função militar em tempo de guerra",
                ],
                "correct_answer": 1,
                "explanation": "Cônsules tinham grande poder, mas integravam sistema republicano colegiado.",
                "difficulty": "basic",
                "source_assets": sa("page-035.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-006",
                "type": "multiple_choice",
                "topic": "republic_institutions",
                "question": (
                    "A Lei das Doze Tábuas (cerca de 450 a.C.) foi importante porque:\n"
                    "I. Escreveu leis antes aplicadas de forma arbitrária por patrícios.\n"
                    "II. Permitiu que plebeus conhecessem regras e direitos.\n"
                    "III. Aboliu imediatamente toda desigualdade social.\n"
                    "IV. Limitou abusos e deu previsibilidade à justiça.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. Desigualdades persistiram — leis não igualaram ricos e pobres (III falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-030.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-007",
                "type": "multiple_choice",
                "topic": "republic_expansion",
                "question": (
                    "Conquistar regiões em torno do Mediterrâneo foi estratégico para Roma porque:"
                ),
                "options": [
                    "Impediu qualquer contato com outros povos",
                    "Garantiu rotas comerciais, suprimentos e controle militar do 'mar interior'",
                    "Serviu apenas para esportes de gladiadores",
                    "Eliminou a necessidade de estradas",
                ],
                "correct_answer": 1,
                "explanation": "O Mediterrâneo unificava economia e defesa do império em expansão.",
                "difficulty": "basic",
                "source_assets": sa("page-040.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-008",
                "type": "multiple_choice",
                "topic": "republic_expansion",
                "question": (
                    "Leia as afirmativas sobre triunfos romanos:\n"
                    "I. Celebravam vitórias militares com desfiles públicos.\n"
                    "II. Exibiam espólios e prisioneiros de guerra.\n"
                    "III. Eram rituais secretos sem população.\n"
                    "IV. Reforçavam prestígio do general e do Estado.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Triunfos eram espetáculos públicos (III falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-030.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-009",
                "type": "multiple_choice",
                "topic": "empire_city",
                "question": (
                    "Nas cidades romanas descritas no caderno, insulae eram:"
                ),
                "options": [
                    "Templos dedicados a Júpiter",
                    "Prédios de apartamentos onde moravam especialmente os mais pobres",
                    "Estradas que ligavam Roma à Gália",
                    "Mercados flutuantes em lagos",
                ],
                "correct_answer": 1,
                "explanation": "Insulae = habitações coletivas; térreo tinha comércio e termopólios.",
                "difficulty": "basic",
                "source_assets": sa("page-025.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-010",
                "type": "multiple_choice",
                "topic": "empire_city",
                "question": (
                    "Leia as afirmativas sobre vida urbana:\n"
                    "I. Termopólios vendiam comida pronta.\n"
                    "II. Estradas pavimentadas ajudavam exército e comércio.\n"
                    "III. Não havia teatros nem anfiteatros nas cidades.\n"
                    "IV. Ruas podiam ser estreitas e acumular lixo.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "I, II e IV", "II e III", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Teatros, circos e anfiteatros existiam (III falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-025.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-011",
                "type": "multiple_choice",
                "topic": "empire_society",
                "question": (
                    "Sobre lutas de gladiadores, o Teste do caderno destaca que:"
                ),
                "options": [
                    "Eram apenas rituais privados sem público",
                    "Entretiam a população e reafirmavam o poder do Estado romano",
                    "Só participavam senadores disputando comando do exército",
                    "Foram inventadas no século XX",
                ],
                "correct_answer": 1,
                "explanation": "Afirmativas II e IV do teste — espetáculo público ligado ao poder imperial.",
                "difficulty": "basic",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-012",
                "type": "multiple_choice",
                "topic": "empire_society",
                "question": (
                    "Leia as afirmativas sobre mulheres em Roma:\n"
                    "I. Viviam sob tutela de homens da família.\n"
                    "II. Podiam ser mater familias administrando a casa.\n"
                    "III. Nunca participavam de atividades fora do lar.\n"
                    "IV. Algumas mulheres ricas no império gerenciavam negócios.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Podiam ir a teatros e feiras — III exagerada.",
                "difficulty": "intermediate",
                "source_assets": sa("page-020.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-013",
                "type": "multiple_choice",
                "topic": "empire_religion",
                "question": (
                    "O Édito de Milão (313), lido no caderno, estabeleceu que:"
                ),
                "options": [
                    "Só o culto cristão seria permitido no império",
                    "Cristãos e demais pessoas poderiam seguir a religião de sua escolha",
                    "Imperadores deveriam ser sempre pagãos",
                    "Templos de Júpiter seriam destruídos imediatamente",
                ],
                "correct_answer": 1,
                "explanation": "Édito garantiu liberdade religiosa — não tornou cristianismo único oficial.",
                "difficulty": "basic",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-014",
                "type": "multiple_choice",
                "topic": "empire_religion",
                "question": (
                    "Leia as afirmativas sobre religião no império:\n"
                    "I. Marco Aurélio aparece conduzindo sacrifício a Júpiter (séc. II).\n"
                    "II. Constantino simboliza aproximação entre cristianismo e poder político.\n"
                    "III. Religião e política nunca se relacionaram em Roma.\n"
                    "IV. O Édito de Milão precede perseguições generalizadas a todos os cristãos.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I e II corretas. Religião sempre ligada ao poder (III falsa); IV confunde ordem histórica.",
                "difficulty": "intermediate",
                "source_assets": sa("page-004.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-015",
                "type": "multiple_choice",
                "topic": "crisis_and_fall",
                "question": (
                    "Teodósio dividiu o Império Romano em Ocidente e Oriente para:"
                ),
                "options": [
                    "Facilitar administração e responder à crise — com sucesso parcial",
                    "Eliminar completamente o cristianismo",
                    "Transferir a capital para Paris",
                    "Impedir invasões germanicas para sempre",
                ],
                "correct_answer": 0,
                "explanation": "Divisão buscava eficiência; Oriente resistiu melhor que o Ocidente.",
                "difficulty": "basic",
                "source_assets": sa("page-015.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-016",
                "type": "multiple_choice",
                "topic": "crisis_and_fall",
                "question": (
                    "Leia as afirmativas sobre o fim do Império Romano do Ocidente:\n"
                    "I. Ruralização indica êxodo das cidades para o campo.\n"
                    "II. Povos chamados 'bárbaros' eram sempre considerados inferiores por todos os historiadores.\n"
                    "III. 476 é marco tradicional da queda do Ocidente.\n"
                    "IV. Houve fusão de elementos romanos e germânicos.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, III e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, III e IV corretas. 'Bárbaro' é conceito relativo — não universal (II falsa).",
                "difficulty": "intermediate",
                "source_assets": sa("page-010.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-017",
                "type": "multiple_choice",
                "topic": "crisis_and_fall",
                "question": (
                    "Sobre o conceito de povos bárbaros no caderno (Attila, gauleses), conclui-se que:"
                ),
                "options": [
                    "Era termo neutro usado só por germanos",
                    "Designava povos considerados culturalmente diferentes — visão do 'outro'",
                    "Significa sempre inferioridade biológica comprovada",
                    "Foi abandonado ainda na Grécia antiga sem uso posterior",
                ],
                "correct_answer": 1,
                "explanation": "Alternativa d do teste: cada povo pode rotular o estrangeiro como 'bárbaro'.",
                "difficulty": "intermediate",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "hist3-pe-018",
                "type": "multiple_choice",
                "topic": "republic_birth",
                "question": (
                    "Segundo Floro (citado no caderno), as fases da história de Roma correspondem a:"
                ),
                "options": [
                    "Monarquia (infância), República (adolescência), Império (maturidade e velhice)",
                    "Império (infância), Monarquia (maturidade), República (velhice)",
                    "República em todas as fases sem monarquia",
                    "Apenas expansão militar sem mudança política",
                ],
                "correct_answer": 0,
                "explanation": "Questão 5 p. 193 — metáfora do ciclo de vida: monarquia → república → império.",
                "difficulty": "intermediate",
                "source_assets": sa("page-002.jpg"),
                "section": "final_quiz",
            },
        ],
    }
