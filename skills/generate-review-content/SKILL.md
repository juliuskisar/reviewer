---
name: generate-review-content
description: Gera conteúdo pedagógico estruturado sem HTML — explicações progressivas, resumos, dicas e apoio aos pais. Respeita blueprint e fontes. Produz review-content.json. Use após create-review-blueprint.
---

# generate-review-content

## Objetivo

Produzir o conteúdo pedagógico estruturado da revisão em `review-content.json`, sem markup de apresentação, conforme `schemas/review-content.schema.json` e fiel ao `review-blueprint.json`.

## Quando utilizar

- Após `create-review-blueprint` aprovar o plano.
- Antes de `generate-exercises` (conteúdo e exercícios podem ser paralelos, mas ambos dependem do blueprint).
- Antes de `compose-static-page`.
- Reexecução quando conteúdo pedagógico precisa correção (não confundir com ajustes de layout).

## Entradas

| Entrada | Origem | Obrigatório |
|---------|--------|-------------|
| `review-blueprint.json` | `workspace/<review-id>/review-blueprint.json` | sim |
| `material-map.json` | `workspace/<review-id>/material-map.json` | sim |
| Configs mescladas | `configs/students/`, `configs/exams/`, `configs/disciplines/` | sim |

## Saídas

| Artefato | Destino |
|----------|---------|
| `review-content.json` | `workspace/<review-id>/review-content.json` |

## Responsabilidades

- Implementar cada seção do blueprint como `sections[]` com `blocks[]` tipados.
- Escrever explicações progressivas (simples → detalhada) adequadas à série do aluno.
- Incluir resumos (`quick_summary`) em **acordeões com concept-grid e callouts** — mesma estética das explicações.
- Preencher `study_route` com passos ordenados; usar `route_steps` com campo `panel` para links às abas.
- Referenciar fontes em `blocks[].sources[]` com `asset`, `origin_type` (`observed`/`inferred`/`supplementary`) e `evidence[]`.
- Usar `language` adequado (ex.: `pt-BR`); tom claro e encorajador.

> **Padrão PE:** use `skills/create-pe-review/SKILL.md` (workflow completo). Detalhes: `docs/playbook/pe-review-pattern.md`. Por padrão: **sem** `image`, **sem** `parent_support`, **sem** seções extras de dicas/exemplo guiado/pontos de atenção (usar callouts no resumo).

## Restrições

- **Sem HTML** — apenas JSON estruturado; apresentação fica para `compose-static-page`.
- Não alterar ordem ou tipos de seção definidos no blueprint.
- Não inventar conceitos sem fonte; conteúdo suplementar marca `origin_type: supplementary`.
- Tipos de bloco permitidos: `paragraph`, `list`, `heading`, `callout`, `comparison_table`, `timeline`, `guided_example`, `quick_summary`, `attention_point`, `exam_tip`, `concept_grid`, `panel_intro`, `route_steps`.
- Não incluir enunciados de exercícios completos — isso é `generate-exercises`.
- Validar contra `schemas/review-content.schema.json`.
- Referência: `tests/fixtures/example-review/review-content.json`.

## Procedimento

1. Carregar blueprint, material-map e configs.
2. Inicializar documento: `version`, `review_id`, `title`, `language`, `discipline`, `grade`, `metadata`.
3. Para cada seção em `blueprint.sections` (por `order`):
   - Criar `content_section` com mesmo `id`, `type`, `title`.
   - Gerar `blocks` conforme `type` e `topic_ids` associados.
4. Em explicações: progressão em parágrafos/listas; vocabulário adequado ao `student_grade`.
5. Em cada bloco factual: anexar `sources[]` rastreando assets do material-map.
6. Montar `study_route[]` espelhando seções principais.
7. Se blueprint inclui `parent_support`: preencher perguntas de discussão e critérios (sem revelar gabaritos de exercícios).
8. Revisar cobertura: todo `topic_id` do blueprint aparece em ao menos um bloco.
9. Validar schema e gravar `review-content.json`.

## Critérios de conclusão

- Todas as seções do blueprint presentes em `sections[]`.
- Conteúdo pedagógico completo para estudo autônomo (sem depender de HTML).
- Fontes rastreáveis nos blocos principais.
- `study_route` coerente com seções.
- Schema válido; idioma e metadados preenchidos.

## Falhas que devem interromper o pipeline

- Blueprint ou material-map ausentes/inválidos.
- Seção do blueprint sem conteúdo gerado.
- Afirmação factual sem fonte quando `source_mapping_required: true`.
- Saída inválida contra schema.
- Conteúdo com HTML embutido ou tags de apresentação.

## Exemplo de entrada

Trecho de `review-blueprint.json`:

```json
{
  "sections": [
    { "id": "explain", "type": "explanations", "title": "Explicações", "topic_ids": ["geometric_solids"] }
  ],
  "topics": [{ "id": "geometric_solids", "label": "Sólidos Geométricos", "depth": "basic" }]
}
```

## Exemplo de saída

```json
{
  "version": "1.0",
  "review_id": "example-review",
  "title": "Revisão de Matemática — Sólidos Geométricos",
  "language": "pt-BR",
  "sections": [{
    "id": "explain",
    "type": "explanations",
    "title": "Explicações",
    "blocks": [{
      "type": "paragraph",
      "topic_id": "geometric_solids",
      "content": "Sólidos geométricos são objetos com três dimensões: comprimento, largura e altura.",
      "sources": [{
        "asset": "assets/example-review/page-001.svg",
        "origin_type": "observed",
        "evidence": ["ilustração de cubo, esfera e cilindro"]
      }]
    }]
  }],
  "study_route": [
    { "order": 1, "title": "Ler explicações", "section_id": "explain" }
  ]
}
```
