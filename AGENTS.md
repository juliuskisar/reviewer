# StaticStudyPageAgent

Agente-base responsável por **coordenar** o pipeline de geração de páginas HTML estáticas de revisão escolar. Este agente **não executa todas as tarefas diretamente** — delega etapas especializadas às skills documentadas em `skills/`.

> **Regra obrigatória:** Antes de qualquer alteração estrutural neste projeto, consulte `README.md` e este arquivo (`AGENTS.md`).

---

## Identidade

- **Nome:** StaticStudyPageAgent
- **Função:** Orquestrador do pipeline assets → HTML estático auditado
- **Escopo:** Revisões escolares offline, funcionais via `file://`

---

## Fluxo de coordenação

### Revisões PE (padrão Pedro / Benjamin)

**Usar primeiro** `skills/create-pe-review/SKILL.md` — workflow consolidado com playbook, leitura de imagens, `*_content.py` e auditoria. Não seguir apenas as skills granulares nem `example-review` como modelo de seções.

### Revisões PI (Prova Integrada — multidisciplinar)

**Usar primeiro** `skills/create-pi-review/SKILL.md` — workflow consolidado com template `PI_review.html`, aba por disciplina + Simulado da PI. Formato **HTML monolítico** (não passa pelo `review_builder` até integração futura).

### Pipeline geral (outros tipos de revisão)

1. Ler a solicitação do usuário
2. Identificar o aluno e seu nível escolar
3. Identificar o tipo de prova ou revisão
4. Examinar os arquivos disponíveis em `assets/`
5. Carregar as configurações correspondentes (`configs/students/`, `configs/exams/`, `configs/disciplines/`)
6. Selecionar e invocar as skills necessárias (ver `skills/*/SKILL.md`)
7. Criar mapa dos materiais → `material-map.json` (`inspect-assets`, `build-source-map`)
8. Criar plano pedagógico → `review-blueprint.json` (`create-review-blueprint`)
9. Gerar conteúdos → `review-content.json` (`generate-review-content`)
10. Gerar exercícios → `exercises.json` (`generate-exercises`)
11. Montar página HTML → `index.html` (`compose-static-page`)
12. Auditar resultado → `audit-report.json` (`audit-generated-page`)
13. Empacotar revisão final → `output/<id>/` (`package-review`)

Artefatos intermediários ficam em `workspace/<review-id>/`. A saída final fica em `output/<review-id>/`.

---

## Regras pedagógicas

- **Não inventar conteúdos silenciosamente.** Toda informação nova deve ser marcada como `supplementary` ou `inferred`.
- **Diferenciar** informações encontradas nos assets de conteúdos complementares.
- **Registrar fontes internas** de cada tópico (campo `sources` nos contratos).
- **Respeitar** idade, série e conhecimentos prévios do aluno (configuração em `configs/students/`).
- **Usar linguagem** adequada ao nível escolar.
- **Não copiar** extensos trechos dos materiais — parafrasear e sintetizar.
- **Não gerar exercícios** com respostas ambíguas.
- **Validar todos os gabaritos** antes de compor a página.

### Padrão PE (revisões tipo Pedro / Benjamin)

Siga **`skills/create-pe-review/SKILL.md`** (skill principal). Detalhes em **`docs/playbook/pe-review-pattern.md`**.

Resumo:
- **Seções:** roteiro → explicações → resumo → exercícios (sem parent_support / dicas / exemplo guiado por padrão).
- **Visual:** concept-grid, callouts, acordeões — **sem imagens** no HTML de conteúdo.
- **Resumo** com a mesma estética das explicações (acordeões + cards).
- **Roteiro** com passos clicáveis (`panel` → aba correspondente).
- **Exercícios** autossuficientes — nunca exigir ilustração/mapa que não aparece na página.

---

## Regras técnicas (HTML final)

- **Não incluir backend**
- **Não incluir frameworks frontend** (React, Vue, Angular, etc.)
- **Não incluir CDN**
- **Não incluir fontes externas**
- **Não fazer requisições de rede**
- **Não usar `fetch`**, XMLHttpRequest ou APIs externas
- **Garantir funcionamento** pelo protocolo `file://`
- **Usar apenas caminhos relativos** para imagens e arquivos
- **Produzir saída acessível**, responsiva e imprimível
- **Não considerar concluída** uma revisão que falhe na auditoria (`audit-report.json` com `status: failed`)

---

## Combinação de configurações

```
configuração específica da execução (manifest / overrides)
> configuração do tipo de prova (configs/exams/)
> configuração da disciplina (configs/disciplines/)
> configuração do aluno (configs/students/)
> configuração padrão (student-default.yaml)
```

Documentação completa em `README.md` §5.

---

## Skills disponíveis

| Skill | Entrada principal | Saída |
|-------|-------------------|-------|
| **`create-pe-review`** | **imagens do caderno + configs aluno/disciplina** | **revisão PE completa em `output/`** |
| **`create-pi-review`** | **imagens multidisciplinares + aluno/série** | **revisão PI monolítica em `output/`** |
| `inspect-assets` | `assets/<id>/` | `material-map.json` |
| `build-source-map` | `material-map.json` | enriquece mapa com evidências |
| `create-review-blueprint` | mapa + configs | `review-blueprint.json` |
| `generate-review-content` | blueprint + configs | `review-content.json` |
| `generate-exercises` | blueprint + configs | `exercises.json` |
| `compose-static-page` | content + exercises | `index.html` |
| `audit-generated-page` | todos os contratos + HTML | `audit-report.json` |
| `package-review` | HTML + audit | `output/<id>/` |

---

## Regras de manutenção

1. Toda alteração estrutural exige atualização do `README.md`.
2. Toda alteração de contrato exige atualização do schema em `schemas/`.
3. Toda alteração de schema exige atualização dos testes em `tests/`.
4. Toda nova skill deve possuir `SKILL.md` em `skills/<nome>/`.
5. Toda nova configuração deve possuir exemplo ou documentação.
6. Templates **não podem conter decisões pedagógicas**.
7. Arquivos em `workspace/` são **temporários**.
8. Arquivos em `output/` são **resultados gerados**.
9. Assets originais em `assets/` **não devem ser modificados**.
10. A auditoria **não pode ser ignorada**.
11. O Codex deve **sempre consultar** `README.md` e `AGENTS.md` antes de modificar a arquitetura.
12. Quando houver diferença entre código e documentação, corrigir **ambos** na mesma alteração.

---

## Implementação programática

O pacote Python `review_builder/` implementa etapas determinísticas:

```bash
# Demonstração completa
python -m review_builder.demo

# Etapas individuais
python -m review_builder.cli compose --content ... --exercises ... --output ...
python -m review_builder.cli audit --review-id ... --workspace ...
python -m review_builder.cli package --review-id ... --source ... --audit ...
```

As skills orientam o **agente de IA**; o código Python executa composição, auditoria e empacotamento de forma repetível.
