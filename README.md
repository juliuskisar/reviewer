# school_review

Pipeline de revisões escolares PE em HTML estático (offline, `file://`). Orquestração: `AGENTS.md`, skill principal PE: `skills/create-pe-review/SKILL.md`.

## Abas de exercícios na página

| Aba | `section` | Tipos |
|-----|-----------|--------|
| Exercícios | `exercises`, `final_quiz` | `multiple_choice`, etc. |
| Prática escrita | `escrita` | `written_language` (Inglês/Espanhol — correção em `review.js`) |
| Desafios | `desafios` | `multiple_choice` avançado |

Contratos: `schemas/exercises.schema.json`. Composição: `review_builder/composer.py`.

## Componentes interativos de Geografia (SVG offline)

| Componente | Tipo | Onde |
|------------|------|------|
| Mapa do Brasil | bloco `brazil_map` — modos `evolution`, `regions`, `capitals`, `new_states`, `imaginary_lines`, `climates`, `vegetation`, `capital_quiz` | `review_builder/map_data/build_brazil_states.py` → `brazil_states.json`; `templates/components/brazil-map.html` |
| Globo de zonas térmicas | bloco `thermal_globe` — modos `explore`, `paint` | `review_builder/thermal_globe.py`; `templates/components/thermal-globe.html` |
| Jogo das capitais | seção `capital_game` | `templates/components/capital-game.html` |
| Jogo temático no mapa | seção `map_theme_game` (`theme`: `climates` / `vegetation` / `imaginary_lines`) | `templates/components/map-theme-game.html` |
| Jogos de revisão | seção `study_game` (`sort_buckets`, `match_pairs`) | `templates/components/study-game.html` |

Dados de clima e vegetação por estado são **aproximações didáticas** (legenda avisa). Regenerar geometria: `python -m review_builder.map_data.build_brazil_states`. Testes: `tests/test_geography_components.py`.
