---
name: audit-generated-page
description: Audita contratos JSON, gabaritos, links, dependências externas, fetch e acessibilidade básica. Produz audit-report.json com status passed/passed_with_warnings/failed. Use após compose-static-page.
---

# audit-generated-page

## Objetivo

Validar a revisão gerada — contratos, lógica de exercícios, HTML estático e requisitos de autonomia — produzindo `audit-report.json` conforme `schemas/audit-report.schema.json`.

## Quando utilizar

- Após `compose-static-page` gerar `staging/index.html`.
- Antes de `package-review` (obrigatório).
- Reexecução após correções em contratos ou HTML.

## Entradas

| Entrada | Origem | Obrigatório |
|---------|--------|-------------|
| `review_id` | contexto da revisão | sim |
| Contratos JSON | `workspace/<review-id>/` | sim |
| `index.html` | `workspace/<review-id>/staging/index.html` | recomendado |
| Schemas | `schemas/*.schema.json` | sim |

Arquivos auditados em `workspace/<review-id>/`:
- `material-map.json`
- `review-blueprint.json`
- `review-content.json`
- `exercises.json`

## Saídas

| Artefato | Destino |
|----------|---------|
| `audit-report.json` | `workspace/<review-id>/audit-report.json` |

Status global: `passed`, `passed_with_warnings` ou `failed`.

## Responsabilidades

- Validar cada contrato contra seu schema (`review_builder.schema_validator.validate_contract`).
- Executar validação lógica de exercícios (`review_builder.auditor.validate_exercises_logic`):
  - IDs únicos
  - Gabaritos presentes e índices válidos (MC)
  - Caminhos relativos em `source_assets`
- Auditar HTML (`review_builder.auditor.audit_html`):
  - Presença de `<title>` e atributo `lang`
  - Ausência de URLs externas (http, CDN, googleapis, unpkg, jsdelivr)
  - Ausência de `fetch()`, XMLHttpRequest
  - Ausência de scripts remotos
  - Caminhos relativos (sem `src="/..."`)
  - Assets referenciados existem em `staging/assets/`
- Consolidar checks com `id`, `name`, `severity`, `passed`, `message`, `details`.
- Calcular `summary` e `blocking_issues`.
- Determinar status final conforme severidades.

## Restrições

- Erros (`severity: error`) com `passed: false` → status `failed`.
- Apenas warnings → `passed_with_warnings`.
- Todos checks ok → `passed`.
- Relatório deve ser válido contra `schemas/audit-report.schema.json`.
- CLI: `python -m review_builder.cli audit --review-id ... --workspace ... [--html ...]`.

## Procedimento

1. Confirmar presença dos contratos em `workspace/<review-id>/`.
2. Executar auditoria:
   ```bash
   python -m review_builder.cli audit \
     --review-id <review-id> \
     --workspace workspace/<review-id> \
     --html workspace/<review-id>/staging/index.html
   ```
3. Revisar checks com falha; classificar como bloqueante ou warning.
4. Verificar coerência cruzada:
   - IDs de tópicos alinhados entre blueprint, content e exercises
   - Contagem de exercícios vs `exercise_plan.total`
5. Gravar `audit-report.json` (automático via CLI).
6. Reportar status ao operador; se `failed`, listar `blocking_issues`.

## Critérios de conclusão

- `audit-report.json` válido contra schema.
- Todos os contratos presentes validados.
- HTML auditado quando disponível.
- Status calculado corretamente.
- `blocking_issues` preenchido quando `failed`.

## Falhas que devem interromper o pipeline

- Status `failed` — impede `package-review`.
- Contrato obrigatório ausente (`review-content.json`, `exercises.json`).
- Gabarito inválido ou ID duplicado em exercícios.
- URL externa, `fetch()` ou caminho absoluto no HTML.
- Asset referenciado ausente em `staging/assets/`.
- Relatório inválido contra schema.

Warnings (`passed_with_warnings`) **não** interrompem empacotamento, mas devem ser documentados.

## Exemplo de entrada

Workspace `workspace/example-review/` com todos os JSONs e `staging/index.html` autocontido.

## Exemplo de saída

```json
{
  "version": "1.0",
  "review_id": "example-review",
  "status": "passed",
  "generated_at": "2026-06-15T14:30:00+00:00",
  "summary": {
    "total_checks": 12,
    "passed": 12,
    "warnings": 0,
    "errors": 0
  },
  "checks": [
    { "id": "schema-exercises", "name": "Schema exercises", "severity": "info", "passed": true, "message": "Válido" },
    { "id": "no-external", "name": "Sem URLs externas", "severity": "info", "passed": true, "message": "" },
    { "id": "html-lang", "name": "Atributo lang", "severity": "info", "passed": true, "message": "" }
  ],
  "blocking_issues": []
}
```

Exemplo com falha:

```json
{
  "status": "failed",
  "blocking_issues": [
    "Exercício ex-003: índice 4 inválido para 4 opções",
    "Detectadas referências a recursos externos"
  ]
}
```
