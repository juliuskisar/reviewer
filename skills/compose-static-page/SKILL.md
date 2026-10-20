---
name: compose-static-page
description: Compõe página HTML estática a partir de conteúdo estruturado, aplicando templates Jinja2 e caminhos relativos. Produz index.html sem alterar conteúdo pedagógico. Use após generate-review-content e generate-exercises.
---

# compose-static-page

## Objetivo

Transformar `review-content.json` e `exercises.json` em uma página HTML estática autocontida (`index.html`), aplicando templates de `templates/` sem modificar o conteúdo pedagógico.

## Quando utilizar

- Após `generate-review-content` e `generate-exercises` concluírem.
- Antes de `audit-generated-page`.
- Reexecução apenas para correções de layout/template (nunca para reescrever explicações).

## Entradas

| Entrada | Origem | Obrigatório |
|---------|--------|-------------|
| `review-content.json` | `workspace/<review-id>/review-content.json` | sim |
| `exercises.json` | `workspace/<review-id>/exercises.json` | sim |
| Templates | `templates/review-page.html`, `templates/components/` | sim |
| Assets estáticos | `templates/static/review.css`, `templates/static/review.js` | sim |
| Assets de conteúdo | `assets/<review-id>/` (via `--assets`) | recomendado |

## Saídas

| Artefato | Destino |
|----------|---------|
| `index.html` | `workspace/<review-id>/staging/index.html` |
| CSS/JS | `workspace/<review-id>/staging/assets/review.css`, `review.js` |
| Imagens referenciadas | `workspace/<review-id>/staging/assets/<arquivo>` |

## Responsabilidades

- Renderizar seções e blocos via Jinja2 (`review_builder.composer.compose_page`).
- Mapear tipos de bloco aos componentes em `templates/components/` (tabs, accordion, quiz, etc.).
- Copiar `review.css` e `review.js` para `staging/assets/`.
- Copiar imagens referenciadas em `sources` e `source_assets`.
- Garantir caminhos relativos (`assets/...`, sem `/` absoluto ou URLs externas).
- Incluir `<title>`, `lang` e dados JSON embutidos para interatividade local.
- **Preservar integralmente** textos, enunciados e gabaritos dos JSONs de entrada.

## Restrições

- **NÃO alterar conteúdo pedagógico** — sem reescrita, resumo ou correção de exercícios.
- **Sem dependências externas** — proibido CDN, Google Fonts, `fetch()`, XHR, scripts remotos.
- Apenas templates e assets do projeto; sem bibliotecas adicionais.
- Autoescape HTML ativo (Jinja2) para prevenir XSS.
- Saída deve abrir offline via `file://` ou servidor local simples.
- CLI: `python -m review_builder.cli compose --content ... --exercises ... --output ... [--assets ...]`.

## Procedimento

1. Validar que `review-content.json` e `exercises.json` existem no workspace.
2. Criar diretório `workspace/<review-id>/staging/` (limpar se reexecução).
3. Invocar composição:
   ```bash
   python -m review_builder.cli compose \
     --content workspace/<review-id>/review-content.json \
     --exercises workspace/<review-id>/exercises.json \
     --output workspace/<review-id>/staging \
     --assets assets/<review-id>
   ```
4. Verificar que `index.html` foi gerado.
5. Confirmar presença de `staging/assets/review.css` e `review.js`.
6. Confirmar cópia de imagens referenciadas nos contratos.
7. Inspeção rápida: nenhuma URL `http://`, `https://` ou caminho `/absoluto`.

## Critérios de conclusão

- `staging/index.html` existe e renderiza seções do conteúdo.
- Assets estáticos e imagens copiados para `staging/assets/`.
- Caminhos relativos em `src`/`href`.
- Conteúdo textual idêntico ao dos JSONs (diff semântico zero).
- Página abre sem erros de recursos 404 locais.

## Falhas que devem interromper o pipeline

- JSONs de entrada ausentes ou inválidos.
- Template principal `templates/review-page.html` ausente.
- Referência a asset inexistente que impede renderização.
- Detecção de URL externa ou caminho absoluto na saída.
- Alteração acidental de texto pedagógico durante composição.

## Exemplo de entrada

`workspace/example-review/review-content.json` + `exercises.json`; templates em `templates/`; assets em `assets/example-review/`.

## Exemplo de saída

Estrutura em `workspace/example-review/staging/`:

```text
staging/
├── index.html          # HTML renderizado, lang="pt-BR", title da revisão
└── assets/
    ├── review.css
    ├── review.js
    ├── page-001.svg
    └── teacher-notes.svg
```

Trecho de `index.html` (estrutura, não conteúdo alterado):

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <title>Revisão de Matemática — Sólidos Geométricos</title>
  <link rel="stylesheet" href="assets/review.css">
</head>
<body>
  <!-- seções renderizadas a partir de review-content.json -->
  <script src="assets/review.js"></script>
</body>
</html>
```
