---
name: build-source-map
description: Relaciona tópicos pedagógicos a assets com evidências e rastreabilidade. Enriquece material-map.json para uso pelo blueprint e conteúdo. Use após inspect-assets e antes de create-review-blueprint.
---

# build-source-map

## Objetivo

Construir o mapeamento tópico ↔ asset com evidências explícitas, consolidando inspeção inicial e configs pedagógicas em um `material-map.json` enriquecido pronto para planejamento.

## Quando utilizar

- Após `inspect-assets` produzir mapa preliminar.
- Antes de `create-review-blueprint`, quando `source_mapping_required: true`.
- Quando tópicos precisam ser normalizados, fundidos ou vinculados a múltiplos assets.
- Reexecução após revisão humana de classificações `uncertain`.

## Entradas

| Entrada | Origem | Obrigatório |
|---------|--------|-------------|
| `material-map.json` | `workspace/<review-id>/material-map.json` | sim |
| Configs de disciplina | `configs/disciplines/<disciplina>.yaml` | recomendado |
| Config de exame | `configs/exams/<tipo>.yaml` | recomendado |
| Contexto do aluno | `configs/students/<aluno>.yaml` | opcional |

## Saídas

| Artefato | Destino |
|----------|---------|
| `material-map.json` (enriquecido) | `workspace/<review-id>/material-map.json` (sobrescreve versão anterior) |

Campos principais enriquecidos: `topics[]` com `id`, `label`, `source_assets`, `confidence`; `assets[].classification` com evidências cruzadas.

## Responsabilidades

- Normalizar IDs de tópicos (snake_case, únicos no escopo da revisão).
- Agrupar assets por tópico com base em manifest, conteúdo legível e configs.
- Registrar evidência por vínculo: trecho observado, metadado ou inferência aplicada.
- Resolver conflitos (asset em múltiplos tópicos) documentando ambos os vínculos ou escolhendo o principal com justificativa.
- Atualizar `confidence` de tópicos: `observed` se ≥1 asset observado; `inferred` se só inferência; `uncertain` se ambíguo.
- Garantir rastreabilidade reversa: todo tópico referencia `source_assets`; todo asset relevante aparece em ao menos um tópico ou em `uncertainties`.

## Restrições

- Não criar tópicos sem asset associado ou evidência registrada.
- Não remover assets de `material-map.json` — apenas enriquecer metadados.
- IDs de tópico devem ser estáveis (reutilizados em blueprint e conteúdo).
- Validar saída contra `schemas/material-map.schema.json`.
- Não alterar arquivos em `assets/`.

## Procedimento

1. Carregar `workspace/<review-id>/material-map.json`.
2. Carregar configs via manifest ou disciplinas em `summary.disciplines_detected`.
3. Extrair taxonomia de tópicos esperados de `configs/disciplines/` (unidades, competências).
4. Para cada asset:
   - Consolidar tópicos de `classification.topics`.
   - Cruzar com unidades do manifest (`unit`, `subject`).
   - Adicionar evidências em `observations` / `inferences`.
5. Montar/atualizar array `topics`:
   - `id`, `label` legível, `source_assets[]`, `confidence`.
6. Resolver lacunas: assets sem tópico → novo tópico `uncertain` ou expandir tópico existente com nota.
7. Verificar cobertura: todos os tópicos do exame/disciplina relevantes têm fonte ou estão marcados como não cobertos em nota interna (não no schema — usar `uncertainties`).
8. Revalidar schema e gravar `material-map.json`.

## Critérios de conclusão

- Array `topics` presente, não vazio quando há conteúdo pedagógico identificável.
- Cada tópico tem `source_assets` não vazio.
- Nenhum vínculo tópico-asset sem evidência em `observations` ou `inferences`.
- Schema válido; `review_id` preservado.
- Tópicos `uncertain` explicitamente listados para revisão humana opcional.

## Falhas que devem interromper o pipeline

- `material-map.json` ausente ou inválido.
- Nenhum tópico mapeável após enriquecimento (pipeline não pode planejar revisão).
- Conflito irresolvível de disciplina entre assets (ex.: mathematics vs portuguese no mesmo review sem manifest).
- Saída inválida contra schema.

## Exemplo de entrada

Trecho de `workspace/example-review/material-map.json` após inspect:

```json
{
  "assets": [
    { "file": "assets/example-review/page-001.svg", "classification": { "topics": ["geometric_solids"], "confidence": "observed" } },
    { "file": "assets/example-review/teacher-notes.svg", "classification": { "topics": [], "confidence": "inferred" } }
  ]
}
```

Config: `configs/disciplines/mathematics.yaml` com unidade `geometric_solids`.

## Exemplo de saída

```json
{
  "topics": [
    {
      "id": "geometric_solids",
      "label": "Sólidos Geométricos",
      "source_assets": [
        "assets/example-review/page-001.svg",
        "assets/example-review/teacher-notes.svg"
      ],
      "confidence": "observed"
    }
  ],
  "assets": [
    {
      "file": "assets/example-review/teacher-notes.svg",
      "classification": {
        "discipline": "mathematics",
        "topics": ["geometric_solids"],
        "confidence": "inferred",
        "observations": [],
        "inferences": ["mesmo subject do manifest; notas da professora sobre sólidos"],
        "uncertainties": []
      }
    }
  ]
}
```
