"""Conteúdo pedagógico da revisão Helena — Ciências PE 2º trimestre."""

from __future__ import annotations

REVIEW_ID = "helena-pe-ciencias-2tri"
ASSET_PREFIX = "assets/helena_pe_ciencias_2_tri"


def _src(page: str) -> dict:
    return {
        "asset": f"{ASSET_PREFIX}/{page}",
        "origin_type": "observed",
        "evidence": [f"Caderno de Ciências — {page}"],
    }


def build_content() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Ciências — PE 2º Trimestre",
        "subtitle": "Helena · 7º ano · Módulos 9, 10 e 11",
        "language": "pt-BR",
        "discipline": "Ciências",
        "grade": "7º ano",
        "metadata": {
            "student_name": "Helena",
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
                    "text": "Composição do ar e poluentes atmosféricos, efeito estufa e aquecimento global, "
                    "ozônio e chuva ácida, poluição do ar interno, doenças respiratórias e inversão térmica, "
                    "saneamento básico, enchentes e doenças transmitidas pela água e por vetores. "
                    "Reserve cerca de 55 minutos.",
                },
            },
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🌬️", "title": "Ar", "text": "N₂ · O₂ · CO₂ · poluentes"},
                        {"icon": "🌍", "title": "Clima", "text": "Efeito estufa · GEE · aquecimento"},
                        {"icon": "☁️", "title": "Ozônio", "text": "Camada protetora · chuva ácida"},
                        {"icon": "🏠", "title": "Ar interno", "text": "Combustão · CO · limpeza · fumo"},
                        {"icon": "🫁", "title": "Respiração", "text": "Asma · inversão térmica"},
                        {"icon": "💧", "title": "Saneamento", "text": "ETA · ETE · enchentes · vetores"},
                    ],
                },
            },
            {
                "type": "route_steps",
                "content": {
                    "modules": [
                        "Módulo 9 — Composição do ar e poluição atmosférica",
                        "Módulo 10 — Efeito estufa, ozônio e ar interno",
                        "Módulo 11 — Saneamento, enchentes e doenças",
                    ],
                    "steps": [
                        {
                            "title": "Estude as Explicações",
                            "panel": "explain",
                            "panel_label": "Explicações",
                            "description": "Abra cada tópico no acordeão. Observe os gráficos e tabelas com calma.",
                            "tip": "Compare ozônio «bom» (estratosfera) e «ruim» (troposfera).",
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
                            "tip": "Em questões com gráfico, leia os valores antes de responder.",
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
            *_topic_air_composition(),
            *_topic_atmospheric_pollutants(),
            *_topic_greenhouse_warming(),
            *_topic_ozone_acid_rain(),
            *_topic_indoor_pollution(),
            *_topic_respiratory_thermal(),
            *_topic_sanitation_floods(),
            *_topic_diseases(),
        ],
    }


def _topic_air_composition() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "1. Composição do ar"}, "topic_id": "air_composition"},
        {
            "type": "paragraph",
            "content": {
                "text": "A atmosfera é uma mistura de gases. O nitrogênio (N₂) e o oxigênio (O₂) "
                "são os mais abundantes. Outros gases — argônio, vapor d'água e dióxido de carbono (CO₂) — "
                "compõem cerca de 1% do ar seco. Atividades humanas alteram essa composição.",
            },
            "topic_id": "air_composition",
            "sources": [_src("page-022.jpg"), _src("page-002.jpg")],
        },
        {
            "type": "pie_chart",
            "content": {
                "title": "Composição do ar seco na atmosfera terrestre",
                "slices": [
                    {"label": "Gás nitrogênio (N₂)", "value": 78, "color": "#3b82f6"},
                    {"label": "Gás oxigênio (O₂)", "value": 21, "color": "#10b981"},
                    {"label": "Outros gases", "value": 1, "color": "#f59e0b"},
                ],
                "unit": "%",
                "caption": "N₂ é o gás mais abundante. O₂ é essencial para respiração e combustão.",
                "aria_label": "Gráfico de pizza da composição do ar seco",
            },
            "topic_id": "air_composition",
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "💨", "title": "Oxigênio", "text": "Respiração celular e combustão consomem O₂"},
                    {"icon": "🌱", "title": "CO₂", "text": "~0,03% no ar — fotossíntese e combustão"},
                    {"icon": "🧪", "title": "Nitrogênio", "text": "Proteínas e DNA — adubos e amônia"},
                ],
            },
            "topic_id": "air_composition",
        },
    ]


def _topic_atmospheric_pollutants() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "2. Poluentes atmosféricos"}, "topic_id": "atmospheric_pollutants"},
        {
            "type": "paragraph",
            "content": {
                "text": "Poluição do ar é o desequilíbrio de substâncias na atmosfera. "
                "Indústrias, veículos, queimadas e lixões liberam gases tóxicos e material particulado (MP). "
                "Cada poluente tem fontes e efeitos distintos na saúde e no ambiente.",
            },
            "topic_id": "atmospheric_pollutants",
            "sources": [_src("page-011.jpg"), _src("page-017.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Principais poluentes (resumo do caderno)",
                "headers": ["Poluente", "Fonte humana", "Impacto"],
                "rows": [
                    ["Óxidos de N e SO₂", "Combustíveis fósseis, veículos", "Chuva ácida · problemas respiratórios"],
                    ["Monóxido de carbono (CO)", "Combustão incompleta", "Liga-se à hemoglobina — falta de O₂"],
                    ["CO₂ e CH₄", "Indústria, veículos, gado, aterros", "Intensificam efeito estufa"],
                    ["Ozônio (O₃) troposférico", "Reações fotoquímicas", "Irrita olhos e pulmões"],
                    ["Material particulado", "Diesel, queimadas, fuligem", "Asma · câncer (diesel)"],
                ],
            },
            "topic_id": "atmospheric_pollutants",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Óxido x monóxido:",
                "text": "Óxidos de nitrogênio e dióxido de enxofre formam chuva ácida. "
                "Monóxido de carbono (CO) é incolor, inodoro e muito tóxico — liga-se ao sangue.",
            },
            "topic_id": "atmospheric_pollutants",
        },
    ]


def _topic_greenhouse_warming() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "3. Efeito estufa e aquecimento global"}, "topic_id": "greenhouse_warming"},
        {
            "type": "paragraph",
            "content": {
                "text": "A atmosfera retém parte do calor emitido pela Terra — como uma estufa de vidro. "
                "Gases de efeito estufa (GEE) como CO₂, CH₄ e vapor d'água mantêm a temperatura média "
                "habitável. O excesso de GEE, sobretudo por queima de combustíveis fósseis, "
                "intensifica o efeito e provoca aquecimento global.",
            },
            "topic_id": "greenhouse_warming",
            "sources": [_src("page-014.jpg"), _src("page-028.jpg"), _src("page-010.jpg")],
        },
        {
            "type": "bar_chart",
            "content": {
                "title": "Destino da energia solar que chega à Terra (%)",
                "bars": [
                    {"label": "Refletida ao espaço", "value": 30, "color": "#94a3b8"},
                    {"label": "Absorvida (ar, solo, água)", "value": 70, "color": "#f59e0b"},
                ],
                "max_value": 100,
                "caption": "Cerca de 70% da radiação solar é absorvida; parte volta como calor retido pelos GEE.",
                "aria_label": "Gráfico de barras com percentual de energia solar refletida e absorvida",
            },
            "topic_id": "greenhouse_warming",
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🌡️", "title": "Sem GEE", "text": "Média de −15 °C — planeta congelado"},
                    {"icon": "🏭", "title": "Ação humana", "text": "Indústrias, veículos, desmatamento ↑ CO₂"},
                    {"icon": "🧊", "title": "Consequências", "text": "Degelo · ↑ nível do mar · secas · vetores"},
                ],
            },
            "topic_id": "greenhouse_warming",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Ciclo do carbono:",
                "text": "Fotossíntese remove CO₂; respiração, decomposição, queimadas e combustão o devolvem. "
                "A concentração atual de CO₂ sobe 250 vezes mais rápido que após a última era glacial.",
            },
            "topic_id": "greenhouse_warming",
            "sources": [_src("page-010.jpg")],
        },
    ]


def _topic_ozone_acid_rain() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "4. Ozônio e chuva ácida"}, "topic_id": "ozone_acid_rain"},
        {
            "type": "paragraph",
            "content": {
                "text": "O ozônio (O₃) na troposfera é poluente — poluição fotoquímica, formada com luz solar. "
                "Na estratosfera (~32 km), forma a camada que filtra raios UV. "
                "CFCs de sprays e refrigeradores destruíram essa camada (Protocolo de Montreal). "
                "Óxidos de enxofre e nitrogênio reagem com vapor d'água e caem como chuva ácida.",
            },
            "topic_id": "ozone_acid_rain",
            "sources": [_src("page-001.jpg"), _src("page-003.jpg"), _src("page-021.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Ozônio «ruim» x ozônio «bom»",
                "headers": ["", "Troposfera (solo)", "Estratosfera (~32 km)"],
                "rows": [
                    ["Função", "Poluente — irrita vias aéreas", "Filtra raios UV nocivos"],
                    ["Causa", "Veículos + luz solar", "Camada natural de O₃"],
                    ["Problema", "Poluição fotoquímica", "Buraco por CFCs (em recuperação)"],
                ],
            },
            "topic_id": "ozone_acid_rain",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Chuva ácida:",
                "text": "Danifica vegetação (ex.: Serra do Mar em Cubatão), lagos, solo, prédios e monumentos. "
                "Vento transporta poluentes para regiões distantes dos polos industriais.",
            },
            "topic_id": "ozone_acid_rain",
        },
    ]


def _topic_indoor_pollution() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "5. Poluição do ar interno"}, "topic_id": "indoor_pollution"},
        {
            "type": "paragraph",
            "content": {
                "text": "O ar dentro de casa pode ser mais poluído que o externo. "
                "Fogão e aquecedor a gás (GLP ou gás natural) queimam combustível fóssil. "
                "Com pouco oxigênio ocorre combustão incompleta — produz CO e fuligem. "
                "Chama azul = completa (CO₂); chama amarela = incompleta (CO).",
            },
            "topic_id": "indoor_pollution",
            "sources": [_src("page-006.jpg"), _src("page-019.jpg"), _src("page-005.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "🔵", "title": "Chama azul", "text": "Combustão completa — mais calor, CO₂"},
                    {"icon": "🟡", "title": "Chama amarela", "text": "Combustão incompleta — CO perigoso"},
                    {"icon": "🧴", "title": "Limpeza", "text": "Nunca misturar amônia + água sanitária (cloramina)"},
                    {"icon": "🚬", "title": "Cigarro", "text": "Fumaça lateral tem até 50× mais carcinógenos"},
                ],
            },
            "topic_id": "indoor_pollution",
        },
        {
            "type": "callout",
            "content": {
                "variant": "accent",
                "title": "Prevenção CO:",
                "text": "Instale aquecedores em locais ventilados — nunca no banheiro. "
                "Não deixe carro ligado em garagem fechada. COVs de tintas exigem EPI e ventilação.",
            },
            "topic_id": "indoor_pollution",
            "sources": [_src("page-008.jpg"), _src("page-015.jpg"), _src("page-025.jpg")],
        },
    ]


def _topic_respiratory_thermal() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "6. Poluição e sistema respiratório"}, "topic_id": "respiratory_thermal"},
        {
            "type": "paragraph",
            "content": {
                "text": "Poluentes atingem nariz, traqueia, brônquios e alvéolos. "
                "Podem causar asma, bronquite crônica, enfisema pulmonar e rinite alérgica. "
                "A inversão térmica — ar frio preso sob ar quente — impede dispersão de poluentes "
                "e piora a qualidade do ar nas cidades.",
            },
            "topic_id": "respiratory_thermal",
            "sources": [_src("page-013.jpg"), _src("page-018.jpg")],
        },
        {
            "type": "comparison_table",
            "content": {
                "caption": "Doenças respiratórias ligadas à poluição",
                "headers": ["Doença", "O que acontece"],
                "rows": [
                    ["Asma", "Inflamação dos brônquios — falta de ar, chiado"],
                    ["Bronquite crônica", "Excesso de muco — tosse persistente"],
                    ["Enfisema", "Destruição dos alvéolos — troca gasosa prejudicada"],
                    ["Rinite alérgica", "Inflamação nasal — espirros, nariz entupido"],
                ],
            },
            "topic_id": "respiratory_thermal",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Inversão térmica:",
                "text": "Fenômeno natural (não causado pelo homem), mas concentra poluentes perto do solo. "
                "Comum no inverno em cidades industrializadas.",
            },
            "topic_id": "respiratory_thermal",
        },
    ]


def _topic_sanitation_floods() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "7. Saneamento básico e enchentes"}, "topic_id": "sanitation_floods"},
        {
            "type": "paragraph",
            "content": {
                "text": "Saneamento básico inclui destinação de resíduos, tratamento de água (ETA) "
                "e esgoto (ETE). Enchentes e deslizamentos — como em Petrópolis (2022) — "
                "provocam desalojamento, mortes e proliferam doenças de veiculação hídrica. "
                "Lixo entupindo bueiros e moradias em encostas sem vegetação aumentam os riscos.",
            },
            "topic_id": "sanitation_floods",
            "sources": [_src("page-026.jpg"), _src("page-016.jpg"), _src("page-023.jpg")],
        },
        {
            "type": "concept_grid",
            "content": {
                "cards": [
                    {"icon": "♻️", "title": "Resíduos", "text": "Reciclagem · compostagem · aterro sanitário"},
                    {"icon": "💧", "title": "ETA", "text": "Água bruta → potável (cloro mata microrganismos)"},
                    {"icon": "🚰", "title": "ETE", "text": "Esgoto tratado antes de voltar ao rio"},
                    {"icon": "🌧️", "title": "Pluviais", "text": "Drenagem separada do esgoto — bueiros limpos"},
                ],
            },
            "topic_id": "sanitation_floods",
        },
    ]


def _topic_diseases() -> list:
    return [
        {"type": "heading", "content": {"level": 3, "text": "8. Doenças hídricas e por vetores"}, "topic_id": "diseases"},
        {
            "type": "paragraph",
            "content": {
                "text": "Agente causador ≠ agente transmissor (vetor). "
                "Doenças hídricas: cólera (bactéria), giardíase/amebíase (protozoários), "
                "hepatite A (vírus), leptospirose (bactéria — urina de ratos na água de enchente). "
                "Doenças por vetores: dengue (Aedes aegypti), malária (Anopheles), "
                "febre tifoide (mosca/barata), mal de Chagas (barbeiro).",
            },
            "topic_id": "diseases",
            "sources": [_src("page-012.jpg"), _src("page-004.jpg"), _src("page-027.jpg"), _src("page-024.jpg")],
        },
        {
            "type": "line_chart",
            "content": {
                "title": "Casos de dengue notificados — município fictício (mil casos)",
                "points": [
                    {"label": "2019", "value": 420},
                    {"label": "2020", "value": 380},
                    {"label": "2021", "value": 290},
                    {"label": "2022", "value": 210},
                    {"label": "2023", "value": 150},
                ],
                "y_unit": "",
                "caption": "Exemplo: queda após campanhas de eliminação de criadouros do Aedes.",
                "aria_label": "Gráfico de linhas com queda de casos de dengue entre 2019 e 2023",
            },
            "topic_id": "diseases",
        },
        {
            "type": "callout",
            "content": {
                "variant": "remember",
                "title": "Malária no Brasil:",
                "text": "Quase 100% dos casos na Amazônia Legal. "
                "Casos caíram de ~549 mil (2006) para ~139 mil (2021), com oscilações em 2017–2018.",
            },
            "topic_id": "diseases",
            "sources": [_src("page-024.jpg")],
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
                    "text": "Revise cada tópico nos acordeões — cards, tabelas e gráficos com o essencial.",
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "1. Composição do ar"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🔵", "title": "N₂", "text": "78% — mais abundante"},
                        {"icon": "🟢", "title": "O₂", "text": "21% — respiração e combustão"},
                        {"icon": "🟡", "title": "Outros", "text": "1% — CO₂, argônio, vapor d'água"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "2. Poluentes"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["Poluente", "Efeito principal"],
                    "rows": [
                        ["NOx e SO₂", "Chuva ácida"],
                        ["CO", "Envenenamento — hemoglobina"],
                        ["CO₂ e CH₄", "Aquecimento global"],
                        ["O₃ (solo)", "Irritação respiratória"],
                        ["MP", "Asma · câncer (diesel)"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "3. Efeito estufa"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "☀️", "title": "Natural", "text": "GEE retêm calor — vida possível"},
                        {"icon": "🏭", "title": "Intensificado", "text": "Excesso de CO₂ e CH₄"},
                        {"icon": "🌊", "title": "Impactos", "text": "Degelo · ↑ mar · vetores de doenças"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "4. Ozônio e chuva ácida"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["", "Troposfera", "Estratosfera"],
                    "rows": [
                        ["Papel", "Poluente", "Protege dos UV"],
                        ["Problema", "Poluição fotoquímica", "Buraco por CFCs"],
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "5. Ar interno"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🔵", "title": "Chama azul", "text": "Combustão completa"},
                        {"icon": "🟡", "title": "Chama amarela", "text": "CO — perigo!"},
                        {"icon": "⚠️", "title": "Limpeza", "text": "Não misturar amônia + cloro"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "6. Respiração"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "🫁", "title": "Doenças", "text": "Asma · bronquite · enfisema · rinite"},
                        {"icon": "🌡️", "title": "Inversão térmica", "text": "Poluentes presos perto do solo"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "7. Saneamento"}},
            {
                "type": "concept_grid",
                "content": {
                    "cards": [
                        {"icon": "💧", "title": "ETA", "text": "Água potável"},
                        {"icon": "🚰", "title": "ETE", "text": "Esgoto tratado"},
                        {"icon": "🌊", "title": "Enchentes", "text": "Doenças hídricas · leptospirose"},
                    ],
                },
            },
            {"type": "heading", "content": {"level": 3, "text": "8. Doenças"}},
            {
                "type": "comparison_table",
                "content": {
                    "headers": ["Doença", "Transmissão"],
                    "rows": [
                        ["Cólera", "Água contaminada (bactéria)"],
                        ["Leptospirose", "Água com urina de ratos"],
                        ["Dengue", "Picada do Aedes aegypti"],
                        ["Malária", "Picada do Anopheles (protozoário)"],
                    ],
                },
            },
            {
                "type": "callout",
                "content": {
                    "variant": "remember",
                    "title": "Pegadinha:",
                    "text": "Causador = microrganismo que adoece. Vetor = quem transporta (mosquito, rato, mosca). "
                    "Ozônio no chão é poluente; a 32 km de altitude protege dos UV.",
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
                "id": "ci-pe-001",
                "type": "multiple_choice",
                "topic": "air_composition",
                "question": "Observe o gráfico. Qual gás é o mais abundante no ar seco da atmosfera?",
                "visual": {
                    "type": "pie_chart",
                    "content": {
                        "title": "Composição do ar em laboratório escolar (simulação)",
                        "slices": [
                            {"label": "N₂", "value": 76, "color": "#6366f1"},
                            {"label": "O₂", "value": 22, "color": "#22c55e"},
                            {"label": "CO₂ + outros", "value": 2, "color": "#eab308"},
                        ],
                        "unit": "%",
                    },
                },
                "options": ["Oxigênio", "Nitrogênio", "Dióxido de carbono", "Argônio"],
                "correct_answer": 1,
                "explanation": "N₂ ocupa a maior fatia (76%). O₂ vem em segundo (22%).",
                "difficulty": "basic",
                "source_assets": sa("page-022.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-002",
                "type": "multiple_choice",
                "topic": "air_composition",
                "question": (
                    "Leia as afirmativas sobre os gases do ar:\n"
                    "I. O oxigênio é consumido na respiração celular.\n"
                    "II. O nitrogênio é usado por seres vivos para formar proteínas.\n"
                    "III. O CO₂ representa cerca de 78% da atmosfera.\n"
                    "IV. Plantas consomem CO₂ na fotossíntese.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I, II e IV", "I e III", "II e IV", "I, II, III e IV"],
                "correct_answer": 0,
                "explanation": "I, II e IV corretas. Quem tem ~78% é o N₂, não o CO₂ (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-002.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-003",
                "type": "multiple_choice",
                "topic": "atmospheric_pollutants",
                "question": "O monóxido de carbono (CO) é perigoso porque:",
                "options": [
                    "Forma chuva ácida ao reagir com a água",
                    "Liga-se à hemoglobina e reduz o transporte de oxigênio",
                    "Destrói a camada de ozônio na estratosfera",
                    "É o principal gás responsável pelo efeito estufa",
                ],
                "correct_answer": 1,
                "explanation": "CO é incolor e inodoro — impede o sangue de levar O₂ às células.",
                "difficulty": "basic",
                "source_assets": sa("page-017.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-004",
                "type": "multiple_choice",
                "topic": "atmospheric_pollutants",
                "question": (
                    "Leia as afirmativas sobre poluentes atmosféricos:\n"
                    "I. Óxidos de nitrogênio e dióxido de enxofre contribuem para a chuva ácida.\n"
                    "II. O ozônio na troposfera é benéfico por filtrar raios UV.\n"
                    "III. O material particulado pode agravar asma e bronquite.\n"
                    "IV. O metano (CH₄) intensifica o efeito estufa.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "II e IV", "I, III e IV", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, III e IV corretas. Ozônio no solo é poluente; quem filtra UV é o da estratosfera (II errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-011.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-005",
                "type": "multiple_choice",
                "topic": "greenhouse_warming",
                "question": "Observe o gráfico. Qual percentual da energia solar que chega à Terra é absorvido pelo ar, solo e água?",
                "visual": {
                    "type": "bar_chart",
                    "content": {
                        "title": "Balanço energético solar — cidade costeira (%)",
                        "bars": [
                            {"label": "Refletida", "value": 28, "color": "#cbd5e1"},
                            {"label": "Absorvida", "value": 72, "color": "#ea580c"},
                        ],
                        "max_value": 100,
                    },
                },
                "options": ["28%", "50%", "72%", "100%"],
                "correct_answer": 2,
                "explanation": "A barra «Absorvida» vale 72% — energia retida e reemitida como calor.",
                "difficulty": "basic",
                "source_assets": sa("page-014.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-006",
                "type": "multiple_choice",
                "topic": "greenhouse_warming",
                "question": (
                    "Leia as afirmativas sobre aquecimento global:\n"
                    "I. O efeito estufa natural mantém temperatura média habitável.\n"
                    "II. Queima de combustíveis fósseis aumenta CO₂ na atmosfera.\n"
                    "III. Fotossíntese libera CO₂ e consome oxigênio.\n"
                    "IV. Degelo de geleiras pode elevar o nível do mar.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Fotossíntese consome CO₂ e libera O₂ (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-010.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-007",
                "type": "multiple_choice",
                "topic": "ozone_acid_rain",
                "question": "A camada de ozônio na estratosfera é importante porque:",
                "options": [
                    "Produz chuva ácida nas cidades industrializadas",
                    "Filtra raios ultravioleta nocivos provenientes do Sol",
                    "Causa poluição fotoquímica perto do solo",
                    "É destruída pelos óxidos de enxofre dos veículos",
                ],
                "correct_answer": 1,
                "explanation": "O₃ estratosférico protege contra UV — queimaduras, câncer de pele e catarata.",
                "difficulty": "basic",
                "source_assets": sa("page-021.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-008",
                "type": "multiple_choice",
                "topic": "ozone_acid_rain",
                "question": (
                    "Leia as afirmativas sobre chuva ácida:\n"
                    "I. Forma-se quando óxidos de enxofre e nitrogênio reagem com vapor d'água.\n"
                    "II. Pode danificar vegetação, lagos e monumentos históricos.\n"
                    "III. Ocorre apenas dentro das fábricas, nunca na atmosfera.\n"
                    "IV. Vento pode transportar poluentes para regiões distantes.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e III", "II e IV", "I, II e IV", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e IV corretas. A reação ocorre na atmosfera, não só dentro de fábricas (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-003.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-009",
                "type": "multiple_choice",
                "topic": "indoor_pollution",
                "question": "Uma chama amarela no fogão a gás geralmente indica:",
                "options": [
                    "Combustão completa — apenas CO₂ e água",
                    "Combustão incompleta — risco de monóxido de carbono",
                    "Excesso de oxigênio — fogão super eficiente",
                    "Ausência de qualquer poluente no ambiente",
                ],
                "correct_answer": 1,
                "explanation": "Chama azul = completa; amarela = incompleta, com CO e fuligem.",
                "difficulty": "basic",
                "source_assets": sa("page-019.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-010",
                "type": "multiple_choice",
                "topic": "indoor_pollution",
                "question": (
                    "Leia as afirmativas sobre poluição interna:\n"
                    "I. Misturar amônia e água sanitária produz gás cloramina tóxico.\n"
                    "II. Aquecedores a gás devem ficar em locais ventilados.\n"
                    "III. Tabagismo passivo não apresenta riscos à saúde.\n"
                    "IV. COVs de tintas exigem ventilação e EPI.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Não existe nível seguro de tabagismo passivo (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-015.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-011",
                "type": "multiple_choice",
                "topic": "respiratory_thermal",
                "question": "A inversão térmica prejudica a qualidade do ar porque:",
                "options": [
                    "Elimina todos os poluentes da atmosfera",
                    "Impede a dispersão de gases tóxicos perto do solo",
                    "Só ocorre em florestas, longe das cidades",
                    "É causada exclusivamente pela queima de lixo",
                ],
                "correct_answer": 1,
                "explanation": "Ar frio fica preso sob ar quente — poluentes concentram-se na respiração das pessoas.",
                "difficulty": "basic",
                "source_assets": sa("page-018.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-012",
                "type": "multiple_choice",
                "topic": "respiratory_thermal",
                "question": (
                    "Leia as afirmativas sobre doenças respiratórias:\n"
                    "I. Asma estreita os brônquios e dificulta a respiração.\n"
                    "II. Enfisema destrói alvéolos e reduz a troca gasosa.\n"
                    "III. Poluição do ar nunca agrava bronquite crônica.\n"
                    "IV. Rinite alérgica inflama a mucosa nasal.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e IV", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Poluição agrava bronquite e asma (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-018.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-013",
                "type": "multiple_choice",
                "topic": "sanitation_floods",
                "question": "Enchentes aumentam o risco de leptospirose porque:",
                "options": [
                    "O mosquito Aedes prolifera na água parada",
                    "A urina de ratos contaminada pode entrar em contato com a pele",
                    "O vírus da hepatite A é transmitido por picada de inseto",
                    "Protozoários da malária sobrevivem apenas em água potável",
                ],
                "correct_answer": 1,
                "explanation": "Leptospirose: bactéria Leptospira — contato com água contaminada por urina de roedores.",
                "difficulty": "basic",
                "source_assets": sa("page-007.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-014",
                "type": "multiple_choice",
                "topic": "sanitation_floods",
                "question": (
                    "Leia as afirmativas sobre saneamento básico:\n"
                    "I. A ETA trata água bruta antes do consumo humano.\n"
                    "II. A ETE trata esgoto antes de devolvê-lo ao ambiente.\n"
                    "III. Lixo entupindo bueiros pode piorar enchentes urbanas.\n"
                    "IV. Água pluvial e esgoto doméstico usam sempre a mesma tubulação.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "III e IV", "I, II e III", "I, II, III e IV"],
                "correct_answer": 2,
                "explanation": "I, II e III corretas. Águas pluviais e esgoto têm sistemas separados (IV errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-026.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-015",
                "type": "multiple_choice",
                "topic": "diseases",
                "question": "Observe o gráfico. Em qual ano houve o maior número de casos de malária no gráfico?",
                "visual": {
                    "type": "bar_chart",
                    "content": {
                        "title": "Casos de malária — região Norte (milhares)",
                        "bars": [
                            {"label": "2013", "value": 178, "color": "#8b5cf6"},
                            {"label": "2015", "value": 127, "color": "#8b5cf6"},
                            {"label": "2017", "value": 194, "color": "#8b5cf6"},
                            {"label": "2019", "value": 157, "color": "#8b5cf6"},
                            {"label": "2021", "value": 139, "color": "#8b5cf6"},
                        ],
                    },
                },
                "options": ["2013", "2015", "2017", "2021"],
                "correct_answer": 2,
                "explanation": "A barra de 2017 (194 mil) é a mais alta do gráfico.",
                "difficulty": "basic",
                "source_assets": sa("page-024.jpg"),
                "section": "exercises",
            },
            {
                "id": "ci-pe-016",
                "type": "multiple_choice",
                "topic": "diseases",
                "question": (
                    "Leia as afirmativas sobre doenças e vetores:\n"
                    "I. Dengue é causada por vírus e transmitida pelo Aedes aegypti.\n"
                    "II. Malária é causada por protozoário e transmitida pelo Anopheles.\n"
                    "III. Cólera é transmitida pela picada de mosquito.\n"
                    "IV. Febre tifoide pode ser transmitida por mosca e barata.\n\n"
                    "Estão corretas apenas:"
                ),
                "options": ["I e II", "I, II e IV", "II, III e IV", "I, II, III e IV"],
                "correct_answer": 1,
                "explanation": "I, II e IV corretas. Cólera = ingestão de água/alimento contaminado (III errada).",
                "difficulty": "intermediate",
                "source_assets": sa("page-027.jpg"),
                "section": "final_quiz",
            },
        ],
    }
