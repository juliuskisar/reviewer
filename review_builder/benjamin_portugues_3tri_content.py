"""Conteúdo pedagógico da revisão Benjamin — Português PE 3º trimestre (Módulos 9–11)."""

from __future__ import annotations

REVIEW_ID = "benjamin-pe-portugues-3tri"
ASSET_PREFIX = "assets/benjamin_pe_portugues_3_tri"

VIRAVEZ_SCENE = (
    "Trecho da peça «Viravez, o cortês» (Cena 3 — casinha modesta):\n"
    "A casa está cheia de cestos de frutas e legumes. Inácia cozinha.\n"
    "INÁCIA — Não entendo essa fartura. Essa montoeira de comida. Assim, de repente! "
    "Só da nossa roça não pode ser...\n"
    "VIRAVEZ — Já falei que é uma herança.\n"
    "INÁCIA — Do tio Hipólito. Já sei. Mas o dinheiro, onde está?\n"
    "VIRAVEZ — Não tem dinheiro, Inacinha... O tio Hipólito só deixou comida.\n"
    "INÁCIA — Coisa mais esquisita, Viravez! Não me lembro desse seu tio..."
)

ANEDOTA_MOSQUITOS = (
    "Anedota (caderno, Atividade 4):\n"
    "Um menino chamou o pai no meio da noite e disse:\n"
    "— Pai, tem muitos mosquitos no meu quarto!\n"
    "— Apague a luz que eles vão embora!\n"
    "Logo depois apareceu um vaga-lume. O menino chamou o pai outra vez:\n"
    "— Pai, socorro! Agora os mosquitos estão vindo com lanternas!"
)

JOANNA_JOCA = (
    "Trecho da entrevista com a jornalista Joanna Cataldo (Jornal Joca):\n"
    "Larissa (10 anos) pergunta dicas para quem quer ser repórter. Joanna responde que é preciso "
    "ser curiosa, gostar de histórias e ter determinação; ler livros, revistas e jornais; "
    "acompanhar o que acontece no mundo; praticar escrevendo notícias, crônicas ou diários.\n"
    "Victor pergunta como fazer um jornal da escola. Joanna convida a mandar exemplos para "
    "joca@magiadeler.com.br."
)

TARSILA_BIO = (
    "Trecho biográfico sobre Tarsila do Amaral (caderno):\n"
    "Tarsila do Amaral nasceu em 1886, em Capivari (SP). Passou a infância nas fazendas de seu pai. "
    "Estudou em São Paulo e em Barcelona, onde pintou seu primeiro quadro em 1904. "
    "Em Minas, viu as cores que gostava desde sua infância — seus mestres diziam que eram caipiras, "
    "mas ela passou a usá-las em suas telas."
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
        "title": "Revisão de Português — PE 3º Trimestre",
        "subtitle": "Benjamin · 4º ano · Módulos 9, 10 e 11",
        "language": "pt-BR",
        "discipline": "Língua Portuguesa",
        "grade": "4º ano",
        "metadata": {
            "student_name": "Benjamin",
            "exam_type": "Prova Específica (PE)",
            "estimated_duration_minutes": 60,
        },
        "study_route": [
            {"order": 1, "title": "Explicações", "section_id": "explain"},
            {"order": 2, "title": "Resumo rápido", "section_id": "summary"},
            {"order": 3, "title": "Jogo: Fala certa", "section_id": "game_speech"},
            {"order": 4, "title": "Jogo: Detetive do pronome", "section_id": "game_pronoun"},
            {"order": 5, "title": "Exercícios", "section_id": "exercises"},
        ],
        "sections": [
            _section_route(),
            _section_explain(),
            _section_summary(),
            _section_game_speech(),
            _section_game_pronoun(),
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
                    "text": "Teatro «Viravez, o cortês», telejornal sobre Tarsila do Amaral, pronomes, "
                    "entrevista «Entrevistando Personalidades», recursos do texto oral e produção de "
                    "texto e vídeo instrucional — Módulos 9, 10 e 11. Reserve cerca de 60 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🎭", "title": "Peça teatral", "text": "Viravez · Saci · rubricas"},
                        {"icon": "💬", "title": "Discurso", "text": "Direto com — · indireto na narrativa"},
                        {"icon": "📺", "title": "Telejornal", "text": "Imagem · som · entonação"},
                        {"icon": "🎨", "title": "Tarsila", "text": "Abaporu · reportagem · pronomes"},
                        {"icon": "🎙️", "title": "Entrevista", "text": "Roteiro · perguntas · respeito"},
                        {"icon": "🗣️", "title": "Texto oral", "text": "Voz · gestos · formal × informal"},
                        {"icon": "📋", "title": "Instrucional", "text": "Objetivo · materiais · passos"},
                        {"icon": "🎬", "title": "Vídeo tutorial", "text": "Planejar · ensaiar · gravar"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 9 — Texto teatral e encenação",
                        "Módulo 10 — Telejornal, Tarsila, entrevista e pronomes",
                        "Módulo 11 — Texto oral, instrucional e vídeo tutorial",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão.",
                            "tip": "Relacione rubricas com gestos na peça.",
                        },
                        {
                            "title": "Revise o Resumo rápido",
                            "panel": "summary",
                            "panel_label": "Resumo rápido",
                            "description": "Percorra os blocos-síntese antes da PE.",
                        },
                        {
                            "title": "Jogue: Fala certa",
                            "panel": "game_speech",
                            "panel_label": "Jogo: Fala certa",
                            "description": "Associe frase ao tipo de discurso.",
                        },
                        {
                            "title": "Jogue: Detetive do pronome",
                            "panel": "game_pronoun",
                            "panel_label": "Jogo: Detetive do pronome",
                            "description": "Classifique pronomes destacados.",
                        },
                        {
                            "title": "Faça os Exercícios",
                            "panel": "exercises",
                            "panel_label": "Exercícios",
                            "description": "Questões com textos transcritos do caderno.",
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
                    "Use os jogos para fixar discurso direto/indireto e tipos de pronome.",
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
            *_topic_theater(),
            *_topic_direct_indirect(),
            *_topic_staging(),
            *_topic_tv(),
            *_topic_tarsila(),
            *_topic_interview(),
            *_topic_oral(),
            *_topic_instructional(),
        ],
    }


def _topic_theater() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Peça «Viravez, o cortês» e o Saci"}, "topic_id": "theater_viravez"},
        {
            "type": "paragraph",
            "content": {
                "text": "Texto dramático = diálogos + rubricas (indicações de cena). Viravez é o protagonista: "
                "peão bondoso que solta o Saci preso. O Saci recompensa com comida abundante, "
                "desde que Viravez mantenha segredo e alimente os filhotes do Saci. Inácia desconfia "
                "da fartura repentina — Viravez inventa a «herança do tio Hipólito».",
            },
            "topic_id": "theater_viravez",
            "sources": [_src("page-038.jpg"), _src("page-037.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "👤", "title": "Protagonista", "text": "Personagem principal — Viravez"},
                    {"icon": "🧚", "title": "Saci", "text": "Recompensa comida · exige segredo"},
                    {"icon": "🤨", "title": "Conflito", "text": "Inácia desconfia da fartura"},
                    {"icon": "🎭", "title": "Gênero", "text": "Peça teatral · falas em destaque"},
                ],
            },
            "topic_id": "theater_viravez",
        },
    ]


def _topic_direct_indirect() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "2. Discurso direto e indireto"}, "topic_id": "direct_indirect"},
        {
            "type": "paragraph",
            "content": {
                "text": "Discurso direto reproduz a fala exata: verbo de dizer + dois-pontos + travessão (—). "
                "Discurso indireto: o narrador conta o que foi dito, sem travessão — "
                "«Viravez pediu a Inácia que recebesse os convidados». "
                "Ao transformar peça em narrativa, use pretérito nos trechos narrativos e mantenha — nas falas.",
            },
            "topic_id": "direct_indirect",
            "sources": [_src("page-035.jpg"), _src("page-030.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Tipo", "Marca", "Exemplo"],
                "rows": [
                    ["Direto", "— após dois-pontos", "Viravez disse: — É uma herança."],
                    ["Indireto", "Sem travessão", "Viravez disse que era uma herança."],
                    ["Narrativa + direto", "Pretérito + —", "Inácia perguntou: — Onde está o dinheiro?"],
                ],
            },
            "topic_id": "direct_indirect",
        },
    ]


def _topic_staging() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "3. Rubricas, encenação e Festival de cenas"}, "topic_id": "theater_staging"},
        {
            "type": "paragraph",
            "content": {
                "text": "Rubricas de cena descrevem movimento, gesto e reação (ex.: «Vivaldino se inclina e beija a mão de Inácia»). "
                "Rubricas de fala indicam tom («descrente», «em tom brincalhão»). "
                "No Festival de cenas: ler o roteiro, distribuir personagens, colorir falas, planejar adereços e sonoplastia, "
                "ensaiar voz, gestos e expressões faciais.",
            },
            "topic_id": "theater_staging",
            "sources": [_src("page-034.jpg"), _src("page-032.jpg"), _src("page-033.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Adjetivos na peça:",
                "text": "«Incomparável» e «indescritível» elogiam a comida; «intragável» é crítica disfarçada de rima.",
            },
            "topic_id": "theater_staging",
        },
    ]


def _topic_tv() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "4. Telejornal e reportagem na TV"}, "topic_id": "tv_journalism"},
        {
            "type": "paragraph",
            "content": {
                "text": "Telejornal combina imagens, sons, entonação, gestos e expressões — recursos que o jornal impresso não tem. "
                "A âncora apresenta o programa; a repórter transmite ao vivo do local da notícia. "
                "No caderno, a reportagem sobre a exposição «Tarsila para Crianças» usa linguagem coloquial "
                "(«prontinho», «dá uma olhada») para aproximar o telespectador.",
            },
            "topic_id": "tv_journalism",
            "sources": [_src("page-028.jpg"), _src("page-026.jpg"), _src("page-024.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "📡", "title": "Ao vivo", "text": "Repórter no local · câmera mostra cenário"},
                    {"icon": "😊", "title": "Coloquial", "text": "Tom próximo · expressões do dia a dia"},
                    {"icon": "🎤", "title": "Âncora", "text": "Apresenta · chama a matéria"},
                    {"icon": "🔊", "title": "Som", "text": "Efeitos · música · ambiente da exposição"},
                ],
            },
            "topic_id": "tv_journalism",
        },
    ]


def _topic_tarsila() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "5. Tarsila do Amaral e pronomes"}, "topic_id": "tarsila_pronouns"},
        {
            "type": "paragraph",
            "content": {
                "text": "Abaporu (1928): nome tupi aba + poru — ligação ao movimento antropofágico. "
                "Pronomes evitam repetição: pessoais (eu, ele, eles, o, a), possessivos (meu, sua, seus), "
                "demonstrativos (este, isso). Objetos diretos: o, a, os, as («Maria viu a rosa e a colocou no vaso»). "
                    "Verbos em -car no pretérito: c → qu antes de e (toco → toquei, brinco → brinquei).",
            },
            "topic_id": "tarsila_pronouns",
            "sources": [_src("page-022.jpg"), _src("page-021.jpg"), _src("page-018.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "headers": ["Tipo", "Função", "Exemplo no caderno"],
                "rows": [
                    ["Pessoal", "Substitui sujeito/objeto", "eles (mosquitos) · nós"],
                    ["Possessivo", "Indica posse", "meu quarto · suas telas"],
                    ["Demonstrativo", "Aponta", "isso (refere-se à frase anterior)"],
                ],
            },
            "topic_id": "tarsila_pronouns",
        },
    ]


def _topic_interview() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "6. Entrevista — roteiro e produção oral"}, "topic_id": "interview"},
        {
            "type": "paragraph",
            "content": {
                "text": "Programa «Entrevistando Personalidades»: planejar convidado, elaborar roteiro com saudação, "
                "perguntas abertas (não só sim/não), agradecimento final. "
                "Durante a entrevista: respeito, linguagem adequada, entonação nas perguntas, "
                "não interromper, pode improvisar repescagem. "
                "Ensaio com rubrica: velocidade da fala, modulação, gestos seguros.",
            },
            "topic_id": "interview",
            "sources": [_src("page-012.jpg"), _src("page-016.jpg"), _src("page-014.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Checklist do roteiro:",
                "text": "Saudação no 1.º parágrafo · parágrafos organizados · perguntas claras · "
                "ponto de interrogação · linguagem adequada à entrevistada.",
            },
            "topic_id": "interview",
        },
    ]


def _topic_oral() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "7. Recursos do texto oral"}, "topic_id": "oral_resources"},
        {
            "type": "paragraph",
            "content": {
                "text": "Texto falado usa voz (volume, tom, entonação), expressões faciais e gestos — "
                "recursos que o texto escrito não registra sozinho. "
                "Linguagem informal = família e amigos; formal = formatura, telejornal, aula expositiva. "
                "Anedota ou vídeo ficam mais vivos quando ouvimos modulação e vemos gestos.",
            },
            "topic_id": "oral_resources",
            "sources": [_src("page-006.jpg"), _src("page-005.jpg"), _src("page-027.jpg")],
        },
    ]


def _topic_instructional() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "8. Texto instrucional e vídeo tutorial"}, "topic_id": "instructional_text"},
        {
            "type": "paragraph",
            "content": {
                "text": "Texto instrucional ensina como fazer algo: tema do jogo, objetivo, jogadores, materiais, "
                "passo a passo (ex.: «Garrafa de papel» — derrubar garrafa em pé no jogo da velha). "
                "Vídeo tutorial: planejar título, objetivo, foco (apresentador ou imagens), "
                "materiais de gravação, despedida; ensaiar fala, voz e postura; "
                "etapas instrucionais seguem sequência planejada (como no vídeo do artista Wem na cozinha).",
            },
            "topic_id": "instructional_text",
            "sources": [_src("page-004.jpg"), _src("page-003.jpg"), _src("page-008.jpg")],
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Segurança:",
                "text": "No vídeo com utensílios de cozinha, pedir ajuda dos adultos para evitar acidentes.",
            },
            "topic_id": "instructional_text",
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
                    "text": "Revise cada bloco antes de ir aos exercícios. "
                    "Lembre-se dos textos transcritos nas questões.",
                },
            },
            {
                "type": "accordion_item",
                "content": {"title": "1. Viravez e Saci", "body": "Protagonista · recompensa · segredo · Inácia desconfia."},
                "topic_id": "theater_viravez",
            },
            {
                "type": "accordion_item",
                "content": {"title": "2. Discurso direto/indireto", "body": "— + dois-pontos · narrativa no pretérito."},
                "topic_id": "direct_indirect",
            },
            {
                "type": "accordion_item",
                "content": {"title": "3. Encenação", "body": "Rubricas de cena e fala · Festival de cenas."},
                "topic_id": "theater_staging",
            },
            {
                "type": "accordion_item",
                "content": {"title": "4. Telejornal", "body": "Imagem + som + gesto · coloquial × formal."},
                "topic_id": "tv_journalism",
            },
            {
                "type": "accordion_item",
                "content": {"title": "5. Tarsila e pronomes", "body": "Abaporu · o/a/os/as · -car → -quei."},
                "topic_id": "tarsila_pronouns",
            },
            {
                "type": "accordion_item",
                "content": {"title": "6. Entrevista", "body": "Roteiro · perguntas abertas · rubrica oral."},
                "topic_id": "interview",
            },
            {
                "type": "accordion_item",
                "content": {"title": "7. Texto oral", "body": "Voz · gestos · entonação · anedota."},
                "topic_id": "oral_resources",
            },
            {
                "type": "accordion_item",
                "content": {"title": "8. Instrucional", "body": "Planejar jogo · tutorial · sequência de passos."},
                "topic_id": "instructional_text",
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "Telejornal ≠ jornal impresso: na TV há recursos sonoros e visuais ao vivo. "
                    "Tutorial instrucional exige ordem lógica — não embaralhe as etapas.",
                },
            },
        ],
    }


def _section_game_speech() -> dict:
    return {
        "id": "game_speech",
        "type": "study_game",
        "title": "Jogo: Fala certa",
        "blocks": [
            {
                "type": "panel_intro",
                "content": {
                    "title": "Direto ou indireto?",
                    "text": "Associe cada frase ao tipo de discurso. Módulo 9 — Viravez, o cortês.",
                },
            },
            {
                "type": "study_game",
                "content": {
                    "mode": "match_pairs",
                    "game_id": "speech_match",
                    "instructions": "Selecione a frase à esquerda e o tipo à direita.",
                    "left": [
                        {"id": "l1", "text": "Viravez disse: — É uma herança."},
                        {"id": "l2", "text": "Viravez explicou que era uma herança."},
                        {"id": "l3", "text": "Inácia perguntou: — Onde está o dinheiro?"},
                        {"id": "l4", "text": "Inácia quis saber onde estava o dinheiro."},
                    ],
                    "right": [
                        {"id": "r1", "text": "Discurso direto"},
                        {"id": "r2", "text": "Discurso indireto"},
                    ],
                    "answers": {"l1": "r1", "l2": "r2", "l3": "r1", "l4": "r2"},
                },
            },
        ],
    }


def _section_game_pronoun() -> dict:
    return {
        "id": "game_pronoun",
        "type": "study_game",
        "title": "Jogo: Detetive do pronome",
        "blocks": [
            {
                "type": "panel_intro",
                "content": {
                    "title": "Qual tipo de pronome?",
                    "text": "Classifique as palavras destacadas. Módulo 10 — Tarsila e anedota.",
                },
            },
            {
                "type": "study_game",
                "content": {
                    "mode": "sort_buckets",
                    "game_id": "pronoun_sort",
                    "instructions": "Clique na palavra e depois no tipo de pronome.",
                    "buckets": [
                        {"id": "pessoal", "label": "Pessoal", "hint": "Substitui nome (ele, eles)"},
                        {"id": "possessivo", "label": "Possessivo", "hint": "Indica dono (meu, sua)"},
                        {"id": "objeto", "label": "Objeto (o/a)", "hint": "Substitui complemento"},
                    ],
                    "sort_items": [
                        {"id": "w1", "text": "meu (quarto)", "answer": "possessivo"},
                        {"id": "w2", "text": "eles (mosquitos)", "answer": "pessoal"},
                        {"id": "w3", "text": "seu (pai — de Tarsila)", "answer": "possessivo"},
                        {"id": "w4", "text": "ela (Tarsila)", "answer": "pessoal"},
                        {"id": "w5", "text": "a (colocou no vaso)", "answer": "objeto"},
                        {"id": "w6", "text": "os (vestidos)", "answer": "objeto"},
                    ],
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
                "id": "bp3-pe-001",
                "type": "multiple_choice",
                "topic": "theater_viravez",
                "question": (
                    f"Leia o trecho:\n\n{VIRAVEZ_SCENE}\n\n"
                    "Quem é o protagonista da cena e qual problema ele esconde de Inácia?"
                ),
                "options": [
                    "Inácia — esconde que não gosta de cozinhar",
                    "Viravez — esconde que a comida vem do Saci, não de herança",
                    "Tio Hipólito — esconde que é rico",
                    "O Saci — esconde que não existe",
                ],
                "correct_answer": 1,
                "explanation": "Viravez é protagonista; a fartura vem do Saci, disfarçada de «herança».",
                "difficulty": "basic",
                "source_assets": sa("page-038.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp3-pe-002",
                "type": "multiple_choice",
                "topic": "theater_viravez",
                "question": (
                    "Leia as afirmativas sobre a peça «Viravez, o cortês»:\n"
                    "I. O Saci recompensa Viravez por tê-lo solto.\n"
                    "II. Viravez deve manter segredo sobre a origem da comida.\n"
                    "III. Inácia acredita imediatamente na história do tio Hipólito.\n"
                    "IV. Texto dramático usa rubricas e falas de personagens.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e IV", "II, III e IV", "I e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Inácia desconfia (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-037.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp3-pe-003",
                "type": "multiple_choice",
                "topic": "direct_indirect",
                "question": "Qual alternativa está em discurso direto, como no caderno?",
                "options": [
                    "Viravez contou que era uma herança.",
                    "Viravez disse: — Já falei que é uma herança.",
                    "Viravez falou sobre a herança para Inácia.",
                    "Inácia soube da herança pelo marido.",
                ],
                "correct_answer": 1,
                "explanation": "Discurso direto usa dois-pontos e travessão com a fala exata.",
                "difficulty": "basic",
                "source_assets": sa("page-035.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp3-pe-004",
                "type": "multiple_choice",
                "topic": "direct_indirect",
                "question": (
                    "Leia as afirmativas sobre discurso direto e indireto:\n"
                    "I. O direto reproduz a fala com travessão.\n"
                    "II. O indireto usa as palavras do narrador para resumir a fala.\n"
                    "III. Na narrativa do caderno, os verbos do narrador ficam no pretérito.\n"
                    "IV. Discurso indireto exige sempre ponto de exclamação.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e III", "II e IV", "III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Indireto não exige exclamação (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-030.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp3-pe-005",
                "type": "multiple_choice",
                "topic": "theater_staging",
                "question": (
                    "Na peça, Vivaldino elogia com «Incomparável!» e Marcolino com «Indescritível!», "
                    "mas Felismino diz «Intragável!». O que isso mostra?"
                ),
                "options": [
                    "Todos elogiam igualmente a comida",
                    "Dois elogiam; Felismino critica de forma humorada",
                    "Ninguém fala sobre comida",
                    "Só Inácia pode opinar sobre o almoço",
                ],
                "correct_answer": 1,
                "explanation": "Incomparável/indescritível = elogio · intragável = comida ruim, piada de rima.",
                "difficulty": "basic",
                "source_assets": sa("page-036.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp3-pe-006",
                "type": "multiple_choice",
                "topic": "theater_staging",
                "question": (
                    "Leia as afirmativas sobre encenação:\n"
                    "I. Rubricas de cena indicam movimentos e gestos.\n"
                    "II. Rubricas de fala podem indicar tom (descrente, brincalhão).\n"
                    "III. No ensaio, avaliam-se voz, modulação e movimentação corporal.\n"
                    "IV. Texto teatral não precisa do nome do personagem antes da fala.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, II e III", "II e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e III corretas. Nome do personagem em destaque é obrigatório (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-031.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp3-pe-007",
                "type": "multiple_choice",
                "topic": "tv_journalism",
                "question": (
                    "O que a reportagem de telejornal pode usar e o jornal impresso, em geral, não registra da mesma forma?"
                ),
                "options": [
                    "Apenas títulos em letras maiúsculas",
                    "Entonação da voz, imagens ao vivo e efeitos sonoros",
                    "Ordem alfabética de notícias",
                    "Texto escrito sem autor",
                ],
                "correct_answer": 1,
                "explanation": "TV combina voz, imagem e som — recursos audiovisuais.",
                "difficulty": "basic",
                "source_assets": sa("page-023.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp3-pe-008",
                "type": "multiple_choice",
                "topic": "tv_journalism",
                "question": (
                    f"Leia o contexto: reportagem «Tarsila para Crianças».\n\n"
                    "Leia as afirmativas:\n"
                    "I. A matéria trata de obras de Tarsila do Amaral.\n"
                    "II. A exposição foi pensada também para crianças.\n"
                    "III. Telejornal não usa linguagem coloquial.\n"
                    "IV. Repórter pode transmitir ao vivo do local da exposição.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e IV", "II, III e IV", "I e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Coloquialismo aparece («prontinho») — III errada.",
                "difficulty": "intermediate",
                "source_assets": sa("page-026.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp3-pe-009",
                "type": "multiple_choice",
                "topic": "tarsila_pronouns",
                "question": (
                    f"Leia o texto:\n\n{TARSILA_BIO}\n\n"
                    "Na frase «Passou a infância nas fazendas de seu pai», «seu» é pronome:"
                ),
                "options": ["Pessoal do caso reto", "Possessivo", "Demonstrativo", "Relativo"],
                "correct_answer": 1,
                "explanation": "«Seu» indica posse (pai de Tarsila).",
                "difficulty": "basic",
                "source_assets": sa("page-019.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp3-pe-010",
                "type": "multiple_choice",
                "topic": "tarsila_pronouns",
                "question": (
                    f"Leia o texto:\n\n{ANEDOTA_MOSQUITOS}\n\n"
                    "Quais pronomes a atividade pede para identificar?"
                ),
                "options": [
                    "Demonstrativo «isso» e relativo «que»",
                    "Possessivo «meu» e pessoal «eles»",
                    "Apenas «Pai» repetido",
                    "Artigo definido «o»",
                ],
                "correct_answer": 1,
                "explanation": "«meu quarto» = possessivo · «eles vão embora» = pessoal.",
                "difficulty": "basic",
                "source_assets": sa("page-010.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp3-pe-011",
                "type": "multiple_choice",
                "topic": "tarsila_pronouns",
                "question": (
                    "Leia as afirmativas sobre pronomes e ortografia:\n"
                    "I. «Brinco» no pretérito → «brinquei» (c → qu).\n"
                    "II. «Maria viu a rosa e a colocou no vaso» — «a» substitui «rosa».\n"
                    "III. Pronome «nós» substitui «eu e meus colegas».\n"
                    "IV. Abaporu significa «homem que come gente» em tupi.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, III e IV", "I, II, III e IV"],
                "correct_answer": 3,
                "explanation": "Todas corretas — regras vistas no Módulo 10.",
                "difficulty": "intermediate",
                "source_assets": sa("page-018.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp3-pe-012",
                "type": "multiple_choice",
                "topic": "interview",
                "question": (
                    f"Leia o trecho:\n\n{JOANNA_JOCA}\n\n"
                    "Qual conselho Joanna dá para quem quer ser repórter?"
                ),
                "options": [
                    "Evitar ler jornais para não copiar",
                    "Ser curiosa, ler bastante e praticar escrita",
                    "Usar só gírias nas matérias",
                    "Entrevistar apenas famosos de TV",
                ],
                "correct_answer": 1,
                "explanation": "Ela destaca curiosidade, leitura e prática de escrita.",
                "difficulty": "basic",
                "source_assets": sa("page-011.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp3-pe-013",
                "type": "multiple_choice",
                "topic": "interview",
                "question": (
                    f"Leia o trecho:\n\n{JOANNA_JOCA}\n\n"
                    "Leia as afirmativas sobre entrevistas:\n"
                    "I. Roteiro deve ter saudação e apresentação do convidado.\n"
                    "II. Perguntas abertas permitem descrever experiências.\n"
                    "III. Durante a entrevista, deve-se interromper sempre que quiser.\n"
                    "IV. No final, agradece-se ao convidado e à audiência.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "I, II e IV", "II e III", "III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Não interromper convidado (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-012.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp3-pe-014",
                "type": "multiple_choice",
                "topic": "oral_resources",
                "question": (
                    "Segundo o caderno, quando usamos linguagem mais formal?"
                ),
                "options": [
                    "Sempre com amigos íntimos",
                    "Em situações sem intimidade: formatura, telejornal, aula expositiva",
                    "Apenas em mensagens de celular",
                    "Somente ao contar anedotas",
                ],
                "correct_answer": 1,
                "explanation": "Formal = contextos públicos ou institucionais; informal = família e amigos.",
                "difficulty": "basic",
                "source_assets": sa("page-005.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp3-pe-015",
                "type": "multiple_choice",
                "topic": "instructional_text",
                "question": (
                    "Leia as afirmativas sobre texto instrucional e vídeo tutorial:\n"
                    "I. Deve informar objetivo, materiais e passos em ordem lógica.\n"
                    "II. No vídeo do artista Wem, as etapas podem ser embaralhadas livremente.\n"
                    "III. Planejamento inclui como apresentar título e finalizar o vídeo.\n"
                    "IV. Avaliam-se fala, voz e postura corporal na apresentação oral.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "I, III e IV", "II e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, III e IV corretas. Vídeo instrucional exige sequência planejada (II errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-007.jpg"),
                "section": "exercises",
            },
            {
                "id": "bp3-pe-016",
                "type": "multiple_choice",
                "topic": "oral_resources",
                "question": (
                    "Leia as afirmativas finais:\n"
                    "I. Gestos e expressões faciais enriquecem o texto oral.\n"
                    "II. Anedota ou vídeo podem ser mais expressivos quando ouvidos/vistos.\n"
                    "III. Telejornal e peça teatral não usam modulação de voz.\n"
                    "IV. Rubrica «descrente» indica tom de desconfiança na fala.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e IV", "II, III e IV", "I e III"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Telejornal e teatro usam voz modulada (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-027.jpg"),
                "section": "final_quiz",
            },
        ],
    }
