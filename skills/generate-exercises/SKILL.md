---
name: generate-exercises
description: Gera exercícios estruturados com gabaritos, explicações e rastreabilidade a fontes. Produz exercises.json sem ambiguidade. Use após create-review-blueprint, em paralelo ou sequência com generate-review-content.
---

# generate-exercises

## Objetivo

Criar exercícios e quiz final alinhados ao `exercise_plan` do blueprint, com gabaritos inequívocos e explicações pedagógicas, em `exercises.json` conforme `schemas/exercises.schema.json`.

## Quando utilizar

- Após `create-review-blueprint` definir `exercise_plan`.
- Antes de `compose-static-page` e `audit-generated-page`.
- Reexecução quando auditoria detecta gabaritos inválidos ou ambiguidade.

## Entradas

| Entrada | Origem | Obrigatório |
|---------|--------|-------------|
| `review-blueprint.json` | `workspace/<review-id>/review-blueprint.json` | sim |
| `material-map.json` | `workspace/<review-id>/material-map.json` | sim |
| `review-content.json` | `workspace/<review-id>/review-content.json` | recomendado |

## Saídas

| Artefato | Destino |
|----------|---------|
| `exercises.json` | `workspace/<review-id>/exercises.json` |

## Responsabilidades

- Gerar exatamente `exercise_plan.total` exercícios respeitando `distribution[]`.
- Atribuir IDs únicos (`ex-001`, `quiz-001`, etc.).
- Redigir enunciados claros, **autossuficientes** (resolvíveis sem imagem/mapa/diagrama externo).
- Fornecer gabaritos corretos por tipo:
  - `multiple_choice`: `options[]` + `correct_answer` (índice 0-based) + `explanation`.
  - `true_false`: `correct_answer` boolean + `explanation`.
  - `open_response`: `open_response_checklist[]` + `correct_answer` modelo opcional.
  - `matching`: `matching_pairs[]` com correspondências únicas.
- Vincular `topic`, `difficulty`, `source_assets` e `section` (`exercises` ou `final_quiz`).
- Alinhar dificuldade e tipos ao perfil do aluno e ao exame.

## Restrições

- **Sem ambiguidade** — uma única resposta correta para MC/VF; critérios explícitos para abertas.
- Não repetir IDs; não duplicar enunciados quase idênticos.
- `correct_answer` para MC deve ser índice válido em `options`.
- Caminhos em `source_assets` relativos (ex.: `assets/example-review/page-001.svg`).
- Não incluir HTML nos enunciados.
- **Não referenciar** “observe a ilustração/mapa/diagrama” se o visual não estiver na página HTML.
- Preferir estilo **Teste/Atividade do caderno**: afirmativas I–IV, textos curtos embutidos, esquemas descritos em palavras.
- **Gráficos:** exemplo `bar_chart`/`fraction_visual` nas explicações + exercício com `visual` (contexto/valores diferentes). Ver `skills/create-pe-review/SKILL.md`.
- **I–IV:** variar combinação correta; proibir padrão fixo “I, III e IV”; rotacionar índice de `correct_answer`.
- Validar contra `schemas/exercises.schema.json` e regras em `review_builder.auditor.validate_exercises_logic`.
- **PE:** seguir `skills/create-pe-review/SKILL.md`. Referência: `review_builder/pedro_content.py` (`build_exercises`) e `docs/playbook/pe-review-pattern.md`.

## Procedimento

1. Carregar blueprint, material-map e conteúdo (para coerência terminológica).
2. Iterar `exercise_plan.distribution`: para cada entrada, gerar `count` exercícios do `type` e `difficulty` indicados.
3. Distribuir entre `section: exercises` e `section: final_quiz` (últimos ~20% como quiz final, ou conforme blueprint).
4. Por exercício:
   - Escolher tópico com fonte disponível.
   - Redigir pergunta e opções (MC: 3–4 opções plausíveis, uma correta).
   - Definir gabarito e explicação que reforce o conceito.
   - Registrar `source_assets`.
5. Verificar unicidade de IDs e soma de counts = `total`.
6. Executar validação lógica (índices, gabaritos presentes, caminhos relativos).
7. Gravar `exercises.json`.

## Critérios de conclusão

- Contagem de exercícios = `exercise_plan.total`.
- Distribuição por tipo/dificuldade respeitada.
- Todo exercício MC/VF tem gabarito e explicação.
- Todo exercício aberto tem checklist de correção.
- Schema válido; IDs únicos; sem caminhos absolutos/HTTP em assets.

## Falhas que devem interromper o pipeline

- Blueprint ausente ou `exercise_plan` inválido.
- Impossível cobrir tópico exigido por falta de fonte.
- Gabarito ausente, índice inválido ou enunciado ambíguo detectado na auto-revisão.
- Saída inválida contra schema.
- Total gerado ≠ `exercise_plan.total`.

## Exemplo de entrada

```json
{
  "exercise_plan": {
    "total": 2,
    "distribution": [
      { "type": "multiple_choice", "count": 1, "difficulty": "basic" },
      { "type": "true_false", "count": 1, "difficulty": "basic" }
    ]
  },
  "topics": [{ "id": "geometric_solids", "source_assets": ["assets/example-review/page-001.svg"] }]
}
```

## Exemplo de saída

```json
{
  "version": "1.0",
  "review_id": "example-review",
  "exercises": [
    {
      "id": "ex-001",
      "type": "multiple_choice",
      "topic": "geometric_solids",
      "question": "Qual sólido tem duas bases circulares?",
      "options": ["Cubo", "Cilindro", "Pirâmide", "Esfera"],
      "correct_answer": 1,
      "explanation": "O cilindro tem duas bases circulares paralelas.",
      "difficulty": "basic",
      "source_assets": ["assets/example-review/page-001.svg"],
      "section": "exercises"
    },
    {
      "id": "ex-002",
      "type": "true_false",
      "topic": "geometric_solids",
      "question": "A esfera é um poliedro.",
      "correct_answer": false,
      "explanation": "A esfera não tem faces planas; poliedros têm faces poligonais.",
      "difficulty": "basic",
      "source_assets": ["assets/example-review/page-001.svg"],
      "section": "exercises"
    }
  ]
}
```
