# Referência — create-pe-review

## Árvore de arquivos por revisão

Exemplo: Benjamin, Ciências, 4º ano, 2º trimestre.

```
configs/students/benjamin-student.yaml          # compartilhado entre revisões do aluno
configs/disciplines/science-pe-4.yaml           # uma por disciplina/série
configs/exams/pe-exam.yaml                      # reutilizar o genérico PE

imagens_ciencias_benjamin/                      # entrada do usuário (pode ficar na raiz)
assets/benjamin_pe_ciencias_2_tri/
  manifest.yaml
  page-001.jpg … page-040.jpg

review_builder/benjamin_ciencias_content.py     # build_content(), build_exercises()
review_builder/generate_benjamin_ciencias.py    # python -m review_builder.generate_benjamin_ciencias

workspace/benjamin-pe-ciencias-2tri/            # temporário (JSON intermediários)
output/benjamin-pe-ciencias-2tri/
  index.html
  review.css
  review.js
  generation-metadata.json
  page-001.jpg …                                # cópias para uso offline
```

## Slugs de disciplina

| Disciplina | Slug em review_id / pasta |
|------------|---------------------------|
| Geografia | `geografia` |
| História | `historia` |
| Ciências | `ciencias` |
| Português | `portugues` |
| Matemática | `matematica` |

## Student YAML mínimo

```yaml
version: 1
id: benjamin-student
student:
  name: Benjamin
  age: 9
  grade: "4º ano"
  language: pt-BR
learning:
  prior_knowledge: basic
  preferred_explanation_style:
    - clear
    - short_blocks
    - example_driven
accessibility:
  avoid_excessive_text_blocks: true
  minimum_font_size_px: 16
notes: >
  Aluno do 4º ano. PE de <disciplina> do 2º trimestre.
```

## Discipline YAML mínimo

```yaml
version: 1
id: science-pe-4
name: Ciências — PE 4º ano (2º trimestre)
objectives:
  - ...
preferred_components:
  - concept_grid
  - route_steps
  - comparison_table
exercise_types:
  - multiple_choice
common_errors:
  - topic: photosynthesis
    description: ...
    prevention: ...
pedagogical_strategies:
  - Organizar na ordem Módulo X → Y
  - Exercícios autossuficientes, estilo Teste do livro
pe_modules:
  primary: [5, 6, 7, 8, 9]
```

## Manifest mínimo

```yaml
version: 1
review:
  id: benjamin-pe-ciencias-2tri
  title: Revisão de Ciências — PE 2º Trimestre (Benjamin, 4º ano)
student:
  config: configs/students/benjamin-student.yaml
exam:
  config: configs/exams/pe-exam.yaml
disciplines:
  - config: configs/disciplines/science-pe-4.yaml
assets:
  - file: page-001.jpg
    subject: science
    unit: module5_feeding
    order: 1
  # … uma entrada por página
```

## Snippet `_src()` no content

```python
def _src(page: str) -> dict:
    return {
        "asset": f"{ASSET_PREFIX}/{page}",
        "origin_type": "observed",
        "evidence": [f"Caderno de Ciências — {page}"],
    }
```

## Snippet `route_steps`

```python
{
    "type": "route_steps",
    "content": {
        "modules": [
            "Módulo 5 — …",
            "Módulo 6 — …",
        ],
        "steps": [
            {
                "title": "Estude as Explicações",
                "panel": "explain",
                "panel_label": "Explicações",
                "description": "Abra cada tópico no acordeão.",
                "tip": "Conte para alguém o que aprendeu.",
            },
            {
                "title": "Revise o Resumo rápido",
                "panel": "summary",
                "panel_label": "Resumo rápido",
                "description": "Use como mapa mental.",
            },
            {
                "title": "Faça os Exercícios",
                "panel": "exercises",
                "panel_label": "Exercícios",
                "description": "Estilo Teste do caderno.",
                "tip": "Responda antes de Verificar.",
            },
        ],
    },
}
```

## Snippet exercício I–IV

```python
{
    "id": "ci-pe-002",
    "type": "multiple_choice",
    "topic": "energy_diet",
    "question": (
        "Leia as afirmativas:\n"
        "I. …\n"
        "II. …\n"
        "III. …\n"
        "IV. …\n\n"
        "Estão corretas apenas:"
    ),
    "options": ["I e II", "I, III e IV", "II, III e IV", "I, II, III e IV"],
    "correct_answer": 1,
    "explanation": "I, III e IV corretas. … (II errada).",
    "difficulty": "intermediate",
    "source_assets": [f"{ASSET_PREFIX}/page-004.jpg"],
    "section": "exercises",
}
```

## `build_blueprint()` — topic_ids

Devem coincidir com `topic_id` nos blocos de explicação e com `topic` nos exercícios:

```python
"topics": [
    {"id": "energy_diet", "label": "Energia", "depth": "basic", "order": 1},
    # … 6–8 entradas
],
"sections": [
    {"id": "route", "type": "study_route", "title": "Roteiro de estudo", "order": 1},
    {"id": "explain", "type": "explanations", "title": "Explicações", "order": 2},
    {"id": "summary", "type": "quick_summary", "title": "Resumo rápido", "order": 3},
],
"exercise_plan": {
    "total": 12,
    "distribution": [{"type": "multiple_choice", "count": 12, "difficulty": "basic"}],
},
```

## Mapeamento disciplina → subject no material-map

| Disciplina | `discipline` / `subject` |
|------------|--------------------------|
| Geografia | `geography` |
| História | `history` |
| Ciências | `science` |

## Prompt rápido para o usuário

Copie e preencha ao pedir nova revisão:

```
Nova revisão PE:
- Aluno: 
- Idade/série: 
- Disciplina: 
- Trimestre: 2º
- Imagens em: imagens_<disciplina>_<aluno>/
- Salvar em: output/<aluno>-pe-<disciplina>-2tri/
```
