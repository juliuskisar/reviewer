# school_review

Pipeline de revisões escolares PE em HTML estático (offline, `file://`). Orquestração: `AGENTS.md`, skill principal PE: `skills/create-pe-review/SKILL.md`.

## Abas de exercícios na página

| Aba | `section` | Tipos |
|-----|-----------|--------|
| Exercícios | `exercises`, `final_quiz` | `multiple_choice`, etc. |
| Prática escrita | `escrita` | `written_language` (Inglês/Espanhol — correção em `review.js`) |
| Desafios | `desafios` | `multiple_choice` avançado |

Contratos: `schemas/exercises.schema.json`. Composição: `review_builder/composer.py`.
