# Pipeline de geração — decisões arquiteturais

Este documento aprofunda decisões de arquitetura. Para visão operacional, consulte o [README.md](../README.md).

---

## Por que dividir em etapas?

A geração direta `assets → prompt → HTML` apresenta problemas previsíveis:

1. **Opacidade:** não há como auditar o que foi inventado vs. extraído dos materiais.
2. **Acoplamento:** mudanças visuais arriscam alterar conteúdo pedagógico.
3. **Retrabalho:** um erro em exercícios exige regenerar toda a página.
4. **Validação impossível:** schemas e testes não se aplicam a HTML monolítico.

Cada etapa produz um artefato JSON validável, versionável e inspecionável manualmente.

```
assets → material-map → blueprint → content + exercises → HTML → audit → package
```

---

## Por que separar conteúdo e HTML?

| Camada | Responsável | Artefato |
|--------|-------------|----------|
| Pedagógica | Skills de geração | `review-content.json`, `exercises.json` |
| Visual | `compose-static-page` + templates | `index.html` |

O compositor **não decide** respostas, conceitos ou regras pedagógicas. Ele recebe dados estruturados e monta a apresentação. Isso garante que:

- Templates podem evoluir sem regenerar conteúdo.
- Conteúdo pode ser revisado por humanos antes da composição.
- Testes podem validar gabaritos independentemente do CSS.

---

## Rastreabilidade

Cada bloco de conteúdo e exercício deve referenciar origens via `sources` / `source_assets`:

```json
{
  "asset": "assets/example-review/teacher-notes.svg",
  "origin_type": "observed",
  "evidence": ["cilindro: 2 bases circulares"]
}
```

Tipos de origem:

- `observed` — informação explicitamente presente no asset
- `inferred` — deduzida com base no material, mas não literal
- `supplementary` — complemento pedagógico não presente nos assets (deve ser explícito)

A skill `build-source-map` consolida essas relações antes da geração de conteúdo.

---

## Combinação de configurações

Configurações YAML em três eixos ortogonais:

- **Aluno** — idade, série, estilo de explicação, acessibilidade
- **Prova** — duração, seções da página, quantidade de exercícios, política de fontes
- **Disciplina** — objetivos, componentes preferidos, erros comuns, validações específicas

**Precedência** (maior vence):

```
execução (manifest) > prova > disciplina > aluno > student-default
```

**Decisão:** a configuração de prova tem precedência sobre disciplina porque define o *formato* da revisão (simulado vs. revisão rápida). A disciplina define *o quê* ensinar; a prova define *como* estruturar a sessão de estudo.

Conflitos de chaves são resolvidos por merge profundo (`review_builder/config_loader.py`).

---

## Fronteiras de responsabilidade

| Componente | Pode | Não pode |
|------------|------|----------|
| Skills de geração | Criar/alterar JSON pedagógico | Emitir HTML final |
| `compose-static-page` | Renderizar templates, copiar assets | Alterar gabaritos ou conceitos |
| `audit-generated-page` | Bloquear empacotamento | Corrigir erros automaticamente |
| Templates | Layout, CSS, JS de UI | Textos pedagógicos hardcoded |
| Schemas | Validar estrutura | Validar correção pedagógica |
| `workspace/` | Artefatos temporários | Fonte definitiva de config |
| `output/` | Resultado empacotado | Edição manual (exceto debug) |

---

## Como implementar uma nova skill

1. Criar `skills/<nome>/SKILL.md` com contrato de entrada/saída.
2. Se produzir JSON novo, criar schema em `schemas/` e testes em `tests/`.
3. Registrar a skill neste pipeline e no `README.md`.
4. Se houver lógica determinística, implementar em `review_builder/` (opcional).
5. Atualizar `AGENTS.md` se a skill integrar o fluxo principal.

---

## Workspace vs. output

- **`workspace/<review-id>/`** — rascunhos, contratos intermediários, staging HTML. Pode ser apagado e regenerado.
- **`output/<review-id>/`** — entrega final mínima: `index.html` + `assets/` + `generation-metadata.json`. Só é criado após auditoria aprovada.

---

## Evolução dos contratos

Schemas usam `"version": "1.0"`. Mudanças incompatíveis incrementam a versão major e exigem:

1. Atualização do schema
2. Atualização dos fixtures de teste
3. Migração documentada no README

Campos novos opcionais podem ser adicionados sem incrementar versão major.
