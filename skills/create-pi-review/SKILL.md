---
name: create-pi-review
description: Cria revisão multidisciplinar PI completa (HTML estático monolítico) — aba por disciplina (percurso, conteúdo, exercícios, dicas) + Simulado da PI com texto-base. Use quando o usuário pedir revisão PI, Prova Integrada, revisão multidisciplinar, pasta imagens_pi_* ou repetir o padrão de PI_review.html.
---

# create-pi-review

Skill **única** para gerar revisões **PI (Prova Integrada)** — formato multidisciplinar em **uma página HTML**, distinto das revisões PE (disciplina única via `review_builder`).

> **Referência canônica de formato:** [`PI_review.html`](../../PI_review.html) (Pedro, 6º ano — 8 disciplinas + Simulado).

---

## Antes de começar — ler obrigatoriamente

1. **`PI_review.html`** — estrutura visual, objeto `subjects`, `simulado`, `SECTION_TEMPLATE` e JS de renderização.
2. **`configs/exams/pi-exam.yaml`** — escopo e metas de exercícios.
3. **Config do aluno** → `configs/students/<aluno>-student.yaml` (criar se não existir).

> **Não usar** o pipeline PE (`review_builder/*_content.py`) nem `tests/fixtures/example-review/` como modelo — a PI é HTML monolítico até integração futura ao compositor.

---

## Entrada mínima do usuário

Coletar (perguntar só o que faltar):

| Campo | Exemplo |
|-------|---------|
| Aluno | Pedro |
| Série | 6º ano |
| Pasta de imagens | `imagens_pi_pedro/` |
| Disciplinas | inferir das subpastas ou listar |
| Output | `output/pedro-pi-6ano/` |

**Pasta de imagens — layout recomendado:**

```
imagens_pi_pedro/
  ingles/       ← JPGs do caderno de Inglês
  geografia/
  matematica/
  desenho/
  ciencias/
  portugues/
  espanhol/
  historia/
```

Se a pasta for **plana** (sem subpastas), pedir ao usuário como agrupar por disciplina.

---

## Convenções de nomes

Ver [reference.md](reference.md). Resumo:

| Artefato | Padrão |
|----------|--------|
| `review_id` | `<aluno>-pi-<serie-slug>` ex.: `pedro-pi-6ano` |
| Pasta output | `output/<review_id>/index.html` |
| Pasta assets | `assets/<aluno>_pi_<serie_slug>/` |
| Arquivo fonte | `review_builder/<aluno>_pi_content.py` **ou** editar dados em `PI_review.html` |
| Exam config | `configs/exams/pi-exam.yaml` |

**Slugs de disciplina** (chaves do objeto `subjects`):

| Disciplina | Chave | Ícone sugerido |
|------------|-------|----------------|
| Inglês | `ingles` | EN |
| Geografia | `geografia` | GE |
| Matemática | `matematica` | MA |
| Desenho Geométrico | `desenho` | DG |
| Ciências | `ciencias` | CI |
| Língua Portuguesa | `portugues` | PT |
| Espanhol | `espanhol` | ES |
| História | `historia` | HI |

Adaptar lista conforme série e materiais disponíveis (4º ano pode não ter Espanhol, etc.).

---

## Estrutura da revisão PI (inferida de `PI_review.html`)

### Navegação

- **Cabeçalho:** «Revisão Multidisciplinar — {Nome} ({Série})»
- **Abas:** uma por disciplina + aba **Simulado da PI** (ícone ★)
- **Sticky nav** no topo; scroll suave ao trocar aba

### Por disciplina (4 acordeões)

Ordem fixa (`SECTION_TEMPLATE`):

| # | Seção | Campo em `sections` | Conteúdo |
|---|-------|---------------------|----------|
| 1 | Percurso de estudo | `percurso` | HTML: módulos cobertos + ordem sugerida de estudo |
| 2 | Conteúdo | `resumo` + `explicacao` | Switch **Resumo** ↔ **Conteúdo geral** (tabelas vs explicação detalhada) |
| 3 | Exercícios interativos | `exercises[]` | 5–12 questões por disciplina |
| 4 | Dicas finais de prova | `dicas` | HTML: pegadinhas, o que decorar, checklist |

### Simulado da PI

Objeto `simulado` separado:

| Campo | Descrição |
|-------|-----------|
| `title` | «Simulado da PI» |
| `intro` | Instruções (quantidade de questões, ligação com texto-base) |
| `textTitle` | Título do texto-base |
| `text` | HTML do texto integrador (tema único que permite questões de várias disciplinas) |
| `questions[]` | MC com `discipline`, `question`, `options`, `correctAnswer`, `explanation` |

**Metas:** 20–32 questões no simulado; **2–5 por disciplina**; todas ligadas ao texto-base **e/ou** ao conteúdo das abas.

---

## Workflow (seguir nesta ordem)

```
Progresso:
- [ ] 1. Ler PI_review.html + pi-exam.yaml
- [ ] 2. Ler TODAS as imagens (por disciplina)
- [ ] 3. Configs (student, manifest por disciplina)
- [ ] 4. Copiar imagens → assets/ (prepare-assets.sh)
- [ ] 5. Montar conteúdo por disciplina (percurso, resumo, explicação, dicas)
- [ ] 6. Escrever exercícios por disciplina + simulado
- [ ] 7. Gerar HTML final e validar offline
- [ ] 8. Atualizar .gitignore se necessário
```

### Passo 1 — Template e formato

- Copiar estrutura de `PI_review.html` — **não reinventar** CSS/JS de abas, acordeões, progresso e simulado.
- Manter: barra de progresso por disciplina, botões Verificar / Mostrar resposta, feedback visual.
- **Zero** CDN, fetch ou dependências externas — funciona em `file://`.

### Passo 2 — Ler todas as imagens (crítico)

- Abrir **cada** JPG/PNG **de cada disciplina**.
- Anotar: módulos, vocabulário, tipo de atividade, tópicos que caem na PI.
- Definir **percurso** e **dicas** alinhados ao material real — não inventar módulos ausentes.

### Passo 3 — Configs

**Student** (`configs/students/`): nome, idade, série, estilo preferido.

**Manifest** (`assets/.../manifest.yaml`): listar imagens **por disciplina**:

```yaml
disciplines:
  - id: geografia
    assets: [geografia/page-001.jpg, …]
  - id: portugues
    assets: [portugues/page-001.jpg, …]
```

### Passo 4 — Preparar assets

```bash
bash skills/create-pi-review/scripts/prepare-assets.sh \
  imagens_pi_<aluno> \
  assets/<aluno>_pi_<serie_slug>
```

### Passo 5 — Conteúdo por disciplina

Para **cada** disciplina, preencher no objeto `subjects`:

```javascript
geografia: {
  title: "Geografia",
  icon: "GE",
  sections: {
    percurso: `<p>…</p><ol>…</ol>`,
    explicacao: `<h3>1. …</h3><p>…</p>…`,  // conteúdo detalhado
    resumo: `<h3>…</h3><table>…</table>…`, // síntese com tabelas
    dicas: `<ul><li>…</li></ul>`,
  },
  exercises: [ … ],
}
```

**Resumo vs Explicação:**
- **Resumo** = tabelas, listas curtas, callouts de atenção — revisão rápida pré-prova.
- **Explicação** = desenvolvimento pedagógico com `<h3>` numerados, parágrafos e exemplos.

Usar classes CSS do template: `.hl`, `.callout`, `.callout--remember`, `.callout--attention`.

### Passo 6 — Exercícios

**Por disciplina** (`exercises[]`):

| Tipo | Campos |
|------|--------|
| `multiple-choice` | `question`, `options[]`, `correctAnswer` (índice 0-based), `explanation`, `modelAnswer` |
| `short-answer` | `question`, `keywords[]` (palavras-chave aceitas), `explanation`, `modelAnswer` |

**Simulado** (`simulado.questions[]`):

- Campo extra `discipline` (nome legível: «Geografia», «Matemática»…)
- Texto-base **autossuficiente** — aluno não precisa de material externo
- Variar gabaritos (não repetir sempre a mesma posição correta)
- Incluir afirmativas I–IV quando couber (especialmente Português)

**Escolher texto-base do simulado:**
- Tema atual, rico em dados (números, datas, lugares) que permita questões de várias disciplinas
- Exemplo em `PI_review.html`: Copa do Mundo 2026 (Geografia, Matemática, Inglês, História, etc.)
- Transcrever/parafrasear — não copiar parágrafos longos de fontes externas sem adaptar

### Passo 7 — Gerar e validar

**Entrega atual (monolítico):**

1. Duplicar `PI_review.html` → `output/<review_id>/index.html`
2. Substituir objeto `subjects` e `simulado` com dados do aluno
3. Atualizar `<title>`, cabeçalho e metadados
4. Salvar `generation-metadata.json` em `output/<review_id>/`

**Checklist de validação manual:**

- [ ] Abrir `index.html` via `file://` — todas as abas funcionam
- [ ] Acordeões abrem/fecham; switch Resumo ↔ Conteúdo geral funciona
- [ ] Exercícios verificam gabarito; barra de progresso atualiza
- [ ] Simulado agrupa questões por disciplina; texto-base visível
- [ ] Nenhum link externo ou CDN
- [ ] Linguagem adequada à série
- [ ] Exercícios autossuficientes (sem «observe a figura» sem figura renderizada)

**Futuro:** quando existir `review_builder/*_pi_content.py` + compositor PI, migrar para pipeline com auditoria — até lá, monolítico é o padrão aprovado.

### Passo 8 — .gitignore

```
!assets/<aluno>_pi_<serie_slug>/
# !output/<review_id>/
```

---

## Regras de qualidade (não negociáveis)

### Conteúdo

- Paráfrasear cadernos — não copiar parágrafos longos.
- **Percurso** indica ordem de estudo dentro da disciplina (Resumo → Explicação → Exercícios → Dicas).
- **Dicas** focam pegadinhas reais da PI, não conteúdo genérico.
- Cobrir **todas** as disciplinas que o aluno terá na prova.

### Exercícios

| ✅ Fazer | ❌ Evitar |
|----------|-----------|
| MC + resposta curta por disciplina | Questões que dependem de figura não incluída |
| Texto-base rico para o simulado | Simulado desconectado das abas |
| `explanation` + `modelAnswer` em toda questão | Gabarito ambíguo |
| 2–5 questões/disciplina no simulado | Repetir sempre mesma alternativa correta |
| Variar `correctAnswer` entre 0, 1, 2, 3 | Copiar enunciados idênticos do livro |

### O que NÃO incluir

- Backend, frameworks, CDN, fontes externas
- Blocos que exijam imagem do caderno sem transcrever/d descrever o necessário
- Disciplinas sem material de apoio (imagens ou conteúdo explícito do usuário)

---

## Diferença PI × PE

| | **PE** | **PI** |
|--|--------|--------|
| Escopo | 1 disciplina | Multidisciplinar |
| Pipeline | `review_builder` + auditoria | HTML monolítico (`PI_review.html`) |
| Navegação | Roteiro → Explicar → Resumo → Exercícios | Aba por disciplina + Simulado |
| Simulado | Não (quiz final na mesma aba) | Texto-base integrador + ~28 MC |
| Skill | `create-pe-review` | `create-pi-review` |

---

## Reutilizar revisões PE existentes

Se o aluno já tem revisões PE em `output/<aluno>-pe-<disciplina>-2tri/`, **parafrasear e condensar** conteúdo delas para `resumo` / `explicacao` da PI — não copiar JSON/schemas diretamente (formatos diferentes).

---

## Checklist final (entregar só com tudo ✓)

- [ ] Uma aba por disciplina da PI + aba Simulado
- [ ] 4 acordeões por disciplina (percurso, conteúdo, exercícios, dicas)
- [ ] Switch Resumo ↔ Conteúdo geral na seção 2
- [ ] 5–12 exercícios por disciplina (MC + opcional resposta curta)
- [ ] Simulado com texto-base + 20–32 MC (2–5/disciplina)
- [ ] Barra de progresso e feedback funcionando
- [ ] HTML abre offline (`file://`)
- [ ] `generation-metadata.json` com caminho do output
- [ ] Informar ao usuário: caminho do HTML e disciplinas cobertas

---

## Referências

- Template: [`PI_review.html`](../../PI_review.html)
- Config prova: [`configs/exams/pi-exam.yaml`](../../configs/exams/pi-exam.yaml)
- Nomes, manifest e snippets: [reference.md](reference.md)
- Revisões PE (condensar conteúdo): `skills/create-pe-review/SKILL.md`
- Orquestração: [AGENTS.md](../../AGENTS.md)
