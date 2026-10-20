---
name: create-review-blueprint
description: Cria plano pedagógico da revisão com objetivos, ordem de tópicos, seções, componentes e plano de exercícios. Produz review-blueprint.json. Use após build-source-map e antes de generate-review-content.
---

# create-review-blueprint

## Objetivo

Definir o plano pedagógico da revisão — objetivos, sequência, seções, componentes de UI e distribuição de exercícios — em `review-blueprint.json` conforme `schemas/review-blueprint.schema.json`.

## Quando utilizar

- Após `build-source-map` enriquecer `material-map.json`.
- Antes de `generate-review-content` e `generate-exercises`.
- Ao adaptar revisão para perfil de aluno (`configs/students/`) ou tipo de exame (`configs/exams/`).
- Quando o plano precisa ser revisado/aprovado antes da geração de conteúdo.

## Entradas

| Entrada | Origem | Obrigatório |
|---------|--------|-------------|
| `material-map.json` | `workspace/<review-id>/material-map.json` | sim |
| Config de aluno | `configs/students/*.yaml` | sim |
| Config de exame | `configs/exams/*.yaml` | sim |
| Config de disciplina | `configs/disciplines/*.yaml` | sim |
| Contexto mesclado | via `review_builder.config_loader.merge_configs` | derivado |

## Saídas

| Artefato | Destino |
|----------|---------|
| `review-blueprint.json` | `workspace/<review-id>/review-blueprint.json` |

## Responsabilidades

- Formular objetivos de aprendizagem mensuráveis alinhados aos tópicos mapeados.
- Ordenar tópicos (`topics[].order`) respeitando pré-requisitos e material disponível.
- Definir `sections[]` com tipos válidos: `study_route`, `explanations`, `quick_summary`, `attention_points`, `guided_examples`, `exercises`, `final_quiz`, `exam_tips`, `parent_support`.
- Selecionar `components[]` compatíveis com templates em `templates/components/`.
- Elaborar `exercise_plan` (total e distribuição por tipo/dificuldade).
- Registrar `common_errors` e `prerequisites` quando aplicável.
- Vincular tópicos a `source_assets` do material-map.
- Respeitar `source_mapping_required: true` — nenhum tópico sem fonte.

## Restrições

- Não gerar conteúdo pedagógico final (textos, enunciados) — apenas o plano.
- Tipos de seção e componentes devem existir no schema e ter template correspondente.
- `exercise_plan.total` deve igualar a soma de `distribution[].count`.
- Tipos de exercício permitidos: `multiple_choice`, `true_false`, `open_response`, `matching`.
- Validar contra `schemas/review-blueprint.schema.json`.
- Referência: fixture em `tests/fixtures/example-review/review-blueprint.json`.

## Procedimento

1. Carregar `material-map.json` e configs (`student`, `exam`, `discipline`).
2. Mesclar configs com precedência: `student-default` < `student` < `discipline` < `exam`.
3. Derivar `review_id`, `title`, `discipline`, `student_grade` do contexto.
4. Redigir 3–6 `objectives` alinhados aos tópicos e ao tipo de exame.
5. Para cada tópico em `material-map.topics`: definir `depth` (`introductory`…`advanced`), `order`, `source_assets`, `prerequisites`.
6. Montar `sections` em ordem pedagógica lógica (roteiro → explicações → resumo → exercícios…).
7. Escolher `components` necessários às seções planeadas.
8. Calcular `exercise_plan` conforme exigências do exame (ex.: `configs/exams/school-test.yaml`).
9. Listar `common_errors` típicos por `topic_id`.
10. Validar schema e gravar `workspace/<review-id>/review-blueprint.json`.

## Critérios de conclusão

- `review-blueprint.json` válido contra schema.
- Todo `topic_id` em seções existe em `topics[]`.
- Todo tópico referencia `source_assets` do material-map.
- `exercise_plan` coerente com tipo de exame e tempo estimado.
- Seções cobrem roteiro, explicações e avaliação conforme config do exame.

## Falhas que devem interromper o pipeline

- `material-map.json` ausente ou sem tópicos utilizáveis.
- Configs obrigatórias ilegíveis ou incompletas.
- Plano de exercícios com total zero ou distribuição inconsistente.
- Tópico planeado sem asset fonte quando `source_mapping_required: true`.
- Saída inválida contra schema.

## Exemplo de entrada

`material-map.json` com tópico `geometric_solids`; config `configs/exams/school-test.yaml` pedindo revisão curta; aluno 4º ano em `configs/students/example-student.yaml`.

## Exemplo de saída

```json
{
  "version": "1.0",
  "review_id": "example-review",
  "title": "Revisão de Matemática — Sólidos Geométricos",
  "discipline": "mathematics",
  "student_grade": "4º ano",
  "objectives": [
    "Identificar e nomear sólidos geométricos comuns",
    "Diferenciar cilindro, cone, esfera e prisma"
  ],
  "topics": [{
    "id": "geometric_solids",
    "label": "Sólidos Geométricos",
    "depth": "basic",
    "order": 1,
    "source_assets": ["assets/example-review/page-001.svg"]
  }],
  "sections": [
    { "id": "route", "type": "study_route", "title": "Roteiro de estudo", "order": 1 },
    { "id": "explain", "type": "explanations", "title": "Explicações", "order": 2, "topic_ids": ["geometric_solids"] }
  ],
  "components": ["guided_example", "quick_summary", "quiz"],
  "exercise_plan": {
    "total": 3,
    "distribution": [
      { "type": "multiple_choice", "count": 2, "difficulty": "basic" },
      { "type": "open_response", "count": 1, "difficulty": "basic" }
    ]
  },
  "source_mapping_required": true
}
```
