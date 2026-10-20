---
name: package-review
description: Empacota revisão final após auditoria — copia arquivos, grava metadados de geração e bloqueia se audit failed. Use como última etapa do pipeline após audit-generated-page com status passed ou passed_with_warnings.
---

# package-review

## Objetivo

Publicar a revisão aprovada em `output/<review-id>/`, copiando artefatos necessários e registrando metadados de geração, bloqueando quando a auditoria falhar.

## Quando utilizar

- Após `audit-generated-page` com status `passed` ou `passed_with_warnings`.
- Etapa final do pipeline de geração.
- Entrega ao aluno/responsável ou deploy local.

## Entradas

| Entrada | Origem | Obrigatório |
|---------|--------|-------------|
| `review_id` | contexto da revisão | sim |
| `staging/` | `workspace/<review-id>/staging/` | sim |
| `audit-report.json` | `workspace/<review-id>/audit-report.json` | sim |
| Metadados opcionais | título, série, timestamp | opcional |

## Saídas

| Artefato | Destino |
|----------|---------|
| `index.html` | `output/<review-id>/index.html` |
| `assets/` | `output/<review-id>/assets/` |
| `generation-metadata.json` | `output/<review-id>/generation-metadata.json` |

## Responsabilidades

- Verificar `audit-report.json`: **bloquear** se `status == "failed"`.
- Copiar `index.html` de `staging/` para `output/<review-id>/`.
- Copiar árvore `staging/assets/` integralmente.
- Gerar `generation-metadata.json` com:
  - `review_id`, `packaged_at` (ISO 8601)
  - `audit_status`
  - `generator: "review_builder"`
  - metadados adicionais (título, série) quando fornecidos
- Substituir pasta de destino existente (reempacotamento limpo).
- Reportar caminho final ao operador.

## Restrições

- **Não empacotar** se auditoria `failed` — levantar `PackagingError`.
- Não incluir contratos JSON intermediários em `output/` (apenas página final + metadata).
- Não modificar conteúdo durante cópia.
- Destino padrão: `output/` na raiz do projeto.
- CLI: `python -m review_builder.cli package --review-id ... --source ... --audit ... [--output ...]`.

## Procedimento

1. Carregar `workspace/<review-id>/audit-report.json`.
2. Se `status == "failed"`: abortar com lista de `blocking_issues`; **não** criar pasta em `output/`.
3. Verificar `workspace/<review-id>/staging/index.html` existe.
4. Executar empacotamento:
   ```bash
   python -m review_builder.cli package \
     --review-id <review-id> \
     --source workspace/<review-id>/staging \
     --audit workspace/<review-id>/audit-report.json \
     --output output
   ```
5. Confirmar estrutura em `output/<review-id>/`.
6. Validar abertura local de `output/<review-id>/index.html`.
7. Informar caminho final e `audit_status` registrado.

## Critérios de conclusão

- Pasta `output/<review-id>/` criada com `index.html`, `assets/` e `generation-metadata.json`.
- `generation-metadata.json` reflete status de auditoria e timestamp.
- Revisão anterior no mesmo `review_id` substituída limpa.
- Pipeline marcado como concluído com sucesso.

## Falhas que devem interromper o pipeline

- `audit-report.json` com `status: "failed"`.
- `index.html` ausente em `staging/`.
- `audit-report.json` ausente ou ilegível.
- Erro de I/O na cópia de arquivos.

Estes são terminais — exigem correção upstream e reexecução de auditoria antes de novo empacotamento.

## Exemplo de entrada

- `workspace/example-review/staging/index.html` + `assets/`
- `workspace/example-review/audit-report.json` com `"status": "passed"`

## Exemplo de saída

Estrutura em `output/example-review/`:

```text
output/example-review/
├── index.html
├── generation-metadata.json
└── assets/
    ├── review.css
    ├── review.js
    ├── page-001.svg
    └── teacher-notes.svg
```

`generation-metadata.json`:

```json
{
  "review_id": "example-review",
  "packaged_at": "2026-06-15T15:00:00+00:00",
  "audit_status": "passed",
  "generator": "review_builder",
  "title": "Revisão de Matemática — Sólidos Geométricos",
  "student_grade": "4º ano"
}
```

Pipeline completo (referência):

```text
assets/ → inspect-assets → build-source-map → create-review-blueprint
  → generate-review-content + generate-exercises → compose-static-page
  → audit-generated-page → package-review → output/
```
