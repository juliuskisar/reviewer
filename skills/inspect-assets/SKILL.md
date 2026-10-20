---
name: inspect-assets
description: Inspeciona assets educacionais, detecta manifest, formatos, ordem, duplicatas e arquivos ilegíveis. Produz material-map.json com classificação observed/inferred/uncertain. Use no início do pipeline ou ao receber novos materiais em assets/.
---

# inspect-assets

## Objetivo

Catalogar os materiais de entrada de uma revisão, registrar metadados observáveis e inferências documentadas, e produzir `material-map.json` conforme `schemas/material-map.schema.json`.

## Quando utilizar

- Início do pipeline de geração de revisão.
- Novos arquivos adicionados em `assets/<review-id>/`.
- Reexecução após alteração de `manifest.yaml` ou substituição de materiais.
- Quando etapas posteriores precisam saber formatos, ordem, disciplina e confiabilidade da classificação.

## Entradas

| Entrada | Origem | Obrigatório |
|---------|--------|-------------|
| `review_id` | manifest ou nome da pasta em `assets/` | sim |
| Pasta de assets | `assets/<review-id>/` | sim |
| `manifest.yaml` | `assets/<review-id>/manifest.yaml` | não |
| Configs referenciadas | `configs/students/`, `configs/exams/`, `configs/disciplines/` via manifest | se manifest existir |

## Saídas

| Artefato | Destino |
|----------|---------|
| `material-map.json` | `workspace/<review-id>/material-map.json` |
| Proposta de manifest (opcional) | `assets/<review-id>/manifest.yaml` quando ausente e inferível |

## Responsabilidades

- Listar todos os arquivos em `assets/<review-id>/`, exceto entradas em `ignore` do manifest.
- Detectar presença de `manifest.yaml` e registrar `manifest_present`.
- Extrair formato, ordem sugerida, disciplina e tópicos preliminares por asset.
- Identificar duplicatas (hash ou nome+conteúdo) e arquivos ilegíveis.
- Classificar cada asset com `confidence`: `observed`, `inferred` ou `uncertain`.
- Preencher `observations`, `inferences` e `uncertainties` em `classification`.
- Gerar `summary` com totais, formatos, disciplinas detectadas, duplicatas e ilegíveis.

## Restrições

- Não alterar arquivos originais em `assets/`.
- Não inventar tópicos sem registrar em `inferences` ou `uncertainties`.
- Caminhos de arquivo sempre relativos à raiz do projeto (ex.: `assets/example-review/page-001.svg`).
- Validar saída contra `schemas/material-map.schema.json` antes de concluir.
- Formatos esperados: imagens (jpg, png, webp, svg), PDF, texto (txt, md). Outros formatos → `uncertain` ou ilegível.

## Procedimento

1. Resolver `review_id` e localizar `assets/<review-id>/`.
2. Verificar existência de `manifest.yaml`; se presente, carregar ordem, `ignore` e metadados via `review_builder.config_loader.load_generation_context`.
3. Enumerar arquivos; calcular ordem (manifest > prefixo numérico > ordem alfabética).
4. Para cada arquivo: detectar formato, tentar leitura; se falhar, adicionar a `summary.unreadable_files`.
5. Detectar duplicatas e registrar em `summary.duplicates`.
6. Classificar disciplina/tópicos:
   - `observed`: metadados explícitos no manifest ou texto legível no arquivo.
   - `inferred`: dedução por nome, ordem ou configs em `configs/disciplines/`.
   - `uncertain`: evidência insuficiente — documentar em `uncertainties`.
7. Montar array `assets` e, se possível, `topics` preliminares.
8. Gravar `workspace/<review-id>/material-map.json` com `version: "1.0"` e `generated_at` ISO 8601.
9. Se não houver manifest e a inferência for suficiente, propor rascunho de `manifest.yaml` (não sobrescrever sem confirmação).

## Critérios de conclusão

- `material-map.json` válido contra o schema.
- Todo asset listado ou explicitamente ignorado pelo manifest.
- Cada classificação tem `confidence` e arrays de evidência coerentes.
- `summary.total_assets` corresponde ao número de entradas em `assets`.
- Duplicatas e ilegíveis documentados (arrays vazios se nenhum).

## Falhas que devem interromper o pipeline

- Pasta `assets/<review-id>/` inexistente ou vazia (sem assets utilizáveis).
- Nenhum asset legível após inspeção.
- Saída inválida contra `schemas/material-map.schema.json`.
- `review_id` ausente ou inconsistente entre manifest e pasta.

## Exemplo de entrada

```yaml
# assets/example-review/manifest.yaml
review:
  id: example-review
assets:
  - file: page-001.svg
    subject: mathematics
    unit: geometric_solids
    order: 1
```

Pasta: `assets/example-review/` com `page-001.svg`, `teacher-notes.svg`.

## Exemplo de saída

```json
{
  "version": "1.0",
  "review_id": "example-review",
  "generated_at": "2026-06-15T12:00:00+00:00",
  "manifest_present": true,
  "assets": [{
    "file": "assets/example-review/page-001.svg",
    "format": "svg",
    "order": 1,
    "classification": {
      "discipline": "mathematics",
      "topics": ["geometric_solids"],
      "confidence": "observed",
      "observations": ["unit declarada no manifest"],
      "inferences": [],
      "uncertainties": []
    }
  }],
  "summary": {
    "total_assets": 1,
    "formats": ["svg"],
    "disciplines_detected": ["mathematics"],
    "unreadable_files": [],
    "duplicates": []
  }
}
```
