---
name: create-pe-review
description: Cria revisão escolar PE completa (HTML estático) no padrão aprovado Pedro/Benjamin — roteiro, explicações, resumo e exercícios autossuficientes. Use quando o usuário pedir nova revisão PE, prova específica, revisão para aluno com fotos do caderno (imagens_*), ou repetir o padrão de output/pedro-pe-geografia-2tri ou benjamin-pe-*.
---

# create-pe-review

Skill **única** para gerar revisões PE com qualidade consistente. Substitui seguir as skills genéricas em sequência — aqui o produto final já está definido.

## Antes de começar — ler obrigatoriamente

1. **`docs/playbook/pe-review-pattern.md`** — padrão visual e pedagógico aprovado.
2. **Código de referência** (escolher o mais próximo):
   - Mesmo aluno, outra disciplina → `review_builder/benjamin_ciencias_content.py` + `generate_benjamin_ciencias.py`
   - Novo aluno → `review_builder/pedro_content.py` + `generate_pedro.py`
3. **Config do aluno** → `configs/students/<aluno>-student.yaml` (criar se não existir).

> **Não usar** `tests/fixtures/example-review/` como modelo de seções — ele inclui `parent_support`, `attention_points`, etc., que o padrão PE **não** usa.

---

## Entrada mínima do usuário

Coletar (perguntar só o que faltar):

| Campo | Exemplo |
|-------|---------|
| Aluno | Benjamin |
| Idade / série | 9 anos, 4º ano |
| Disciplina | Ciências |
| Trimestre | 2º |
| Pasta de imagens | `imagens_ciencias_benjamin/` |

---

## Convenções de nomes

Ver [reference.md](reference.md) para árvore completa. Resumo:

| Artefato | Padrão |
|----------|--------|
| `review_id` | `<aluno>-pe-<disciplina>-2tri` (slug minúsculo, sem acento) |
| Pasta output | `output/<review_id>/` |
| Pasta assets | `assets/<aluno>_pe_<disciplina>_2_tri/` |
| Conteúdo | `review_builder/<aluno>_<disciplina>_content.py` |
| Gerador | `review_builder/generate_<aluno>_<disciplina>.py` |
| Disciplina config | `configs/disciplines/<disciplina>-pe-<serie>.yaml` |

Se o aluno tiver **uma única** revisão, pode omitir disciplina no nome do arquivo (`pedro_content.py`).

---

## Workflow (seguir nesta ordem)

```
Progresso:
- [ ] 1. Ler playbook + referência de código
- [ ] 2. Ler TODAS as imagens do caderno
- [ ] 3. Configs (student, discipline, manifest)
- [ ] 4. Copiar imagens → assets/
- [ ] 5. Escrever *_content.py (8 tópicos, 12 exercícios)
- [ ] 6. Escrever generate_*.py (espelhar referência)
- [ ] 7. Gerar + pytest + corrigir até auditoria passed
- [ ] 8. Atualizar .gitignore se necessário
```

### Passo 1 — Playbook e referência

- Confirmar: **3 abas de conteúdo** (roteiro, explicações, resumo) + **exercícios** (+ **desafios** opcional).
- Confirmar: **zero** blocos `image` no conteúdo; **zero** `parent_support` / `exam_tips` / `guided_examples` / `attention_points`.
- Copiar estrutura de `build_content()` e `build_exercises()` da referência — adaptar, não reinventar.

### Passo 2 — Ler todas as imagens (crítico)

- Abrir **cada** JPG/PNG da pasta `imagens_*` (ou assets existentes).
- Anotar: módulos do caderno, vocabulário destacado, tipo de atividade (Teste I–IV, completar, associar).
- Definir **6–8 tópicos** alinhados aos módulos — um acordeão por tópico nas explicações e no resumo.

### Passo 3 — Configs

**Student** (`configs/students/`): nome, idade, série, `preferred_explanation_style`, notas sobre a PE.

**Discipline** (`configs/disciplines/`): objetivos, `pe_modules`, `common_errors`, estratégias pedagógicas.

**Manifest** (`assets/.../manifest.yaml`): listar `page-001.jpg` … com `order` e `unit` por tópico.

### Passo 4 — Preparar assets

```bash
bash skills/create-pe-review/scripts/prepare-assets.sh \
  imagens_<disciplina>_<aluno> \
  assets/<aluno>_pe_<disciplina>_2_tri
```

Gera `page-001.jpg` … em ordem alfabética dos arquivos fonte. Depois editar `manifest.yaml` com metadados.

### Passo 5 — Conteúdo (`*_content.py`)

Constantes no topo:

```python
REVIEW_ID = "<aluno>-pe-<disciplina>-2tri"
ASSET_PREFIX = "assets/<aluno>_pe_<disciplina>_2_tri"
```

**`build_content()`** — estrutura fixa:

| Seção | Blocos obrigatórios |
|-------|---------------------|
| `study_route` | `panel_intro` → `concept_grid` (6 cards dos módulos) → `route_steps` (3–4 passos com `panel`) → `callout` info |
| `explanations` | 6–8 tópicos: `heading` + `paragraph` + (`concept_grid` ou `comparison_table`) + `callout` opcional |
| `quick_summary` | `panel_intro` + um bloco por tópico (mesma estética) + `callout` pegadinha no final |

Cada bloco factual: `sources: [_src("page-NNN.jpg")]`.

**`build_exercises()`** — **15–18** questões `multiple_choice` na aba Exercícios (mínimo 12):

- ~8 `basic`, ~4 `intermediate`
- 3–4 com afirmativas **I–IV** (“Estão corretas apenas:”) — ver regras de variedade abaixo
- Última(s) pode(m) ser `section: "final_quiz"`
- **Autossuficientes** — ver regras abaixo
- `source_assets` em cada exercício

**Desafios (opcional, recomendado em Matemática)** — aba separada **Desafios**:

- **10** questões `multiple_choice` com `section: "desafios"` e `difficulty: "advanced"`
- Função auxiliar `_challenge_exercises(sa)` no final de `build_exercises()`, espalhada com `*_challenge_exercises(sa)`
- Problemas mais exigentes (estilo Atividade / Teste Cesgranrio da apostila), **sempre** baseados nas imagens do caderno
- Incluir passo no `study_route` e em `route_steps` com `"panel": "desafios"`
- Referência: `review_builder/benjamin_matematica_content.py` ou `pedro_matematica_content.py`
- O compositor separa automaticamente: aba Exercícios (`exercises` + `final_quiz`) vs aba Desafios (`desafios`)

### Prática escrita — **Inglês e Espanhol PE** (obrigatório)

Revisões de **Inglês** ou **Espanhol** incluem uma aba extra **Prática escrita** (`section: "escrita"`), com exercícios **`written_language`**: o aluno digita **uma palavra** ou **frase curta** na língua-alvo; o corretor roda **offline** em `review.js` (normalização, variantes aceitas, tolerância leve a typo, dicas em `mistake_hints`).

**Quantidade:** **8–12** itens simples, alinhados ao caderno (comparativos, completar frase, vocabulário).

**Contrato (cada exercício):**

| Campo | Uso |
|-------|-----|
| `type` | `"written_language"` |
| `section` | `"escrita"` |
| `input_mode` | `"word"` ou `"sentence"` |
| `correct_answer` | Resposta modelo (string) |
| `accepted_answers` | Variantes opcionais (com/sem pontuação, contrações) |
| `mistake_hints` | Opcional: `[{"contains": "gooder", "message": "…"}]` |
| `explanation` | Feedback pedagógico após verificar |
| `question` | Enunciado em português claro; resposta esperada na língua-alvo |

**Roteiro:** passo em `route_steps` com `"panel": "escrita"`, `"panel_label": "Prática escrita"`.

**Implementação:** função auxiliar `_written_exercises(sa)` em `*_content.py`; concatenar em `build_exercises()` como em `pedro_ingles_3tri_content.py`. Infra: `schemas/exercises.schema.json`, `templates/review-page.html`, `templates/components/quiz.html`, `templates/static/review.js`.

> **Não** usar `open_response` para línguas — esse tipo é checklist sem correção automática.

### Gráficos e visuais (`bar_chart`, `pie_chart`, `line_chart`, `fraction_visual`)

Quando o caderno tiver exercícios com **gráfico de barras**, **gráfico de pizza**, **gráfico de linhas**, **figura de frações** ou interpretação visual de dados:

1. **Explicações:** incluir **um exemplo renderizado** (`bar_chart`, `pie_chart`, `line_chart` ou `fraction_visual` no `build_content`) — HTML/CSS/SVG, **nunca JPG**. Contexto e valores **próprios** (não copiar o exercício do livro).
2. **Exercícios:** incluir **pelo menos uma questão** com o **mesmo tipo de visual** (`visual` no exercício), mas **contexto e valores diferentes** do exemplo das explicações. Enunciado: “Observe o gráfico/figura…”.
3. **Variar o tipo** conforme o material: pizza para composições percentuais; barras para comparação de categorias; linhas para evolução temporal (anos, meses).
4. Manter a prática: explicação ensina o procedimento; exercício exige **análise do gráfico** embutido na página.

```python
# Explicações — pizza (composição do ar)
{"type": "pie_chart", "content": {"title": "...", "slices": [{"label": "...", "value": 78, "color": "#..."}], "unit": "%"}}

# Explicações — linhas (evolução temporal)
{"type": "line_chart", "content": {"title": "...", "points": [{"label": "2019", "value": 420}, ...]}}

# Exercício — barras (outro contexto) + campo visual
{
    "question": "Observe o gráfico…",
    "visual": {"type": "bar_chart", "content": {...}},
    ...
}
```

Tipos disponíveis: `bar_chart`, `pie_chart`, `line_chart`, `fraction_visual`, `brazil_map`. Templates: `templates/components/bar-chart.html`, `pie-chart.html`, `line-chart.html`, `fraction-visual.html`, `brazil-map.html`, `exercise-visual.html`.

### Mapas interativos (`brazil_map`) — **Geografia PE**

**Sempre** em revisões de Geografia, buscar oportunidades de mapas SVG offline (nunca JPG de atlas no HTML).

#### Aba dedicada

Incluir seção `interactive_maps` (id `maps`, título **Mapas interativos**) **entre** Resumo rápido e Exercícios:

```python
"study_route": [
    {"order": 1, "title": "Explicações", "section_id": "explain"},
    {"order": 2, "title": "Resumo rápido", "section_id": "summary"},
    {"order": 3, "title": "Mapas interativos", "section_id": "maps"},
    {"order": 4, "title": "Exercícios", "section_id": "exercises"},
],
"sections": [
    _section_route(),
    _section_explain(),
    _section_summary(),
    _section_interactive_maps(),  # todos os brazil_map aqui
],
```

- **Não** repetir os mesmos mapas nas explicações — consolidar na aba `maps`.
- Nas explicações, usar `callout` apontando à aba Mapas interativos quando o tópico pede exploração visual.
- `route_steps`: passo com `"panel": "maps"`, `"panel_label": "Mapas interativos"`.

#### Função auxiliar de conteúdo

Centralizar blocos em `_interactive_map_blocks()` (referência: `benjamin_geografia_content.py`).

#### Modos pedagógicos do mapa

| `mode` | Uso |
|--------|-----|
| `evolution` | Períodos históricos + fusão MT/MS e GO/TO |
| `regions` | Cores por região (Norte, Nordeste, etc.) |
| `capitals` | Nomes das capitais no mapa |
| `new_states` | Destaque estados criados após 1977 |
| `capital_quiz` | **Só em exercícios** — clique + digitar capital + verificar |

Mapa principal: `show_mode_toggle: True` + `show_period_toggle: True`. Mapas focados (um tema): só o toggle necessário.

#### Evolução histórica (fusões)

| Período | Geometria |
|---------|-----------|
| Após 1988 | 27 UFs separadas |
| 1977–1988 | Goiás unificado (GO+TO); MS separado |
| 1942–1977 | Mato Grosso unificado (MT+MS) + Goiás unificado |

Dados: `review_builder/map_data/brazil_states.json` (regenerar com `python -m review_builder.map_data.build_brazil_states`).

#### Exercícios com mapa

**Múltipla escolha + visual:** campo `visual` com `type: "brazil_map"` — enunciado autossuficiente + destaque (`highlight`).

```python
{
    "question": "Observe o mapa. O estado em destaque…",
    "visual": {
        "type": "brazil_map",
        "content": {
            "period": "post_1988",
            "highlight": ["TO"],
            "show_period_toggle": False,
            "interactive": True,
        },
    },
    ...
}
```

**Jogo das capitais (`capital_game`):** aba dedicada entre **Mapas interativos** e **Exercícios**. Mapa com **27 estados** — ao clicar, mostra só o **nome do estado**; o aluno digita a capital e confirma. Estados corretos ficam **verdes**; contador **acertos / 27** e **cronômetro** até completar todos.

```python
def _section_capital_game() -> dict:
    return {
        "id": "capital_game",
        "type": "capital_game",
        "title": "Jogo das capitais",
        "blocks": [
            {
                "type": "panel_intro",
                "content": {
                    "title": "Complete o mapa!",
                    "text": "Clique em um estado, digite a capital e confirme. Complete os 27!",
                },
            },
        ],
    }
```

Incluir seção `capital_game` em revisões de Geografia quando o caderno trabalha capitais ou UFs. O template `capital-game.html` injeta o mapa em modo `capital_game` automaticamente.

**Quiz pontual (`map_capital`):** exercício opcional na aba Exercícios (modo `capital_quiz`) — preferir o jogo completo na aba separada.

#### Infraestrutura (não duplicar)

| Artefato | Caminho |
|----------|---------|
| Dados SVG | `review_builder/map_data/brazil_states.json` |
| Build geometria | `review_builder/map_data/build_brazil_states.py` |
| Loader | `review_builder/brazil_map.py` |
| Template mapa | `templates/components/brazil-map.html` |
| Template jogo | `templates/components/capital-game.html` |
| JS | `templates/static/review.js` (`initBrazilMaps`, `initCapitalGame`) |
| Schema | `brazil_map` em `review-content.schema.json` e `exercises.schema.json` |

Referência completa: `review_builder/benjamin_geografia_content.py`, `output/benjamin-pe-geografia-2tri/`.

### Textos transcritos da apostila — **Português PE**

Em revisões de **Língua Portuguesa**, os exercícios devem ancorar-se em **textos reais do caderno**, transcritos no enunciado (autossuficientes — o aluno não precisa das imagens).

**Regras:**

1. Escolher **pelo menos 2 textos** distintos da apostila (trecho de lei, netiqueta, crônica, poema, anedota etc.).
2. Para **cada texto**, incluir **≥ 2 exercícios** de interpretação ou gramática contextualizada.
3. Declarar constantes no topo de `*_content.py` (ex.: `CTB_ART54`, `NETIQUETA_TEXT`) — paráfrase curta permitida, mas preservar vocabulário-chave.
4. Marcar `source_assets` com a página de origem; transcrição ≠ bloco `image` no HTML.
5. Variar tipos: compreensão, modo verbal no contexto, I–IV, discurso direto/indireto.

Referência: `review_builder/pedro_portugues_content.py`, `output/pedro-pe-portugues-2tri/`.

### Jogos interativos (`study_game`)

Quando o usuário pedir **jogos** ou for útil fixar conteúdo do caderno, incluir **≥ 2 abas** `study_game` (o usuário escolhe o preferido depois).

| `mode` | Uso |
|--------|-----|
| `sort_buckets` | Classificar itens em categorias (ex.: normativo × instrucional) |
| `match_pairs` | Associar exemplo ↔ conceito (ex.: recurso de humor) |

Seção `type: study_game` + bloco `type: study_game` com `content.mode`. Infraestrutura: `templates/components/study-game.html`, `initStudyGames` em `review.js`. Geografia continua com `capital_game`.

### Passo 6 — Gerador (`generate_*.py`)

Espelhar `generate_benjamin_ciencias.py` ou `generate_pedro.py`:

- `build_material_map()` a partir do manifest
- `build_blueprint()` com os mesmos `topic_id`s do content
- `run()`: workspace JSON → `validate_contract` → `compose_page` → `audit_and_save` → `generation-metadata.json`

Módulo executável:

```bash
python -m review_builder.generate_<aluno>_<disciplina>
```

### Passo 7 — Validar

```bash
python -m review_builder.generate_<aluno>_<disciplina>
pytest -q
```

**Output enxuto:** o compositor copia para `output/` apenas `review.css`, `review.js` e imagens em blocos `image` (padrão PE não usa imagens no HTML — JPGs ficam só em `assets/` para rastreabilidade).

- Auditoria deve retornar `passed`.
- Abrir `output/<review_id>/index.html` mentalmente: roteiro navega? exercícios resolvem sem figura?

### Passo 8 — .gitignore

Adicionar exceções se o usuário versiona outputs:

```
!assets/<aluno>_pe_<disciplina>_2_tri/
# !output/<review_id>/
```

---

## Regras de qualidade (não negociáveis)

### Conteúdo

- Paráfrasear o caderno — não copiar parágrafos longos.
- Linguagem da série em `configs/students/`.
- Blocos curtos; ícones nos `concept_grid` cards.
- `route_steps`: cada passo com `panel` = `explain` | `summary` | `maps` | `capital_game` | `exercises` | `escrita` (Inglês/Espanhol) | `desafios` (opcional).

### Exercícios

| ✅ Fazer | ❌ Evitar |
|----------|-----------|
| Afirmativas I–IV embutidas no enunciado | “Observe a ilustração/mapa/diagrama” |
| Descrever esquema em palavras | Exercício que depende de figura não renderizada |
| Explicação em toda MC | Perguntas genéricas fora do caderno |
| Distratores plausíveis | Gabarito ambíguo |
| **Variar gabarito I–IV** | Repetir sempre “I, III e IV” como corretas |
| Rotacionar posição da opção correta no array | Colocar a combinação vencedora sempre no mesmo índice |

#### Afirmativas I–IV — variedade obrigatória

Ao usar “Estão corretas apenas:”, **nunca** padronizar a resposta como **I, III e IV** (ou sempre a mesma combinação). Os alunos percebem o padrão.

Checklist por revisão:
- [ ] Cada questão I–IV tem combinação **distinta** (ex.: I e III · II e IV · II, III e IV · I e IV).
- [ ] A opção correta aparece em **índices diferentes** (`correct_answer` 0, 1, 2 e 3 distribuídos).
- [ ] Revisar todas as questões I–IV da revisão antes de entregar — buscar `"I, III e IV"` no arquivo de conteúdo.

### O que NÃO incluir

`attention_points`, `guided_examples`, `exam_tips`, `parent_support`, blocos `image`.

---

## Disciplinas já implementadas (reutilizar padrão)

| Revisão | Content | Generate |
|---------|---------|----------|
| Pedro · Geografia 6º | `pedro_content.py` | `generate_pedro.py` |
| Benjamin · História 4º | `benjamin_content.py` | `generate_benjamin.py` |
| Benjamin · Ciências 4º | `benjamin_ciencias_content.py` | `generate_benjamin_ciencias.py` |
| Benjamin · Matemática 4º | `benjamin_matematica_content.py` | `generate_benjamin_matematica.py` |
| Benjamin · Geografia 4º | `benjamin_geografia_content.py` | `generate_benjamin_geografia.py` |
| Benjamin · Português 4º | `benjamin_portugues_content.py` | `generate_benjamin_portugues.py` |
| Pedro · Matemática 6º | `pedro_matematica_content.py` | `generate_pedro_matematica.py` |
| Pedro · Ciências 6º | `pedro_ciencias_content.py` | `generate_pedro_ciencias.py` |
| Pedro · Português 6º | `pedro_portugues_content.py` | `generate_pedro_portugues.py` |
| Helena · Ciências 7º | `helena_ciencias_content.py` | `generate_helena_ciencias.py` |

Nova disciplina do **mesmo aluno** → duplicar o par mais recente do aluno e renomear.

---

## Checklist final (entregar só com tudo ✓)

- [ ] 3 seções + aba Exercícios (+ aba **Prática escrita** se Inglês/Espanhol; + aba Desafios se Matemática; + aba Mapas interativos se Geografia)
- [ ] 6–8 tópicos nas explicações e no resumo
- [ ] Roteiro com botões para abas (incl. Prática escrita / Mapas interativos / Desafios quando houver)
- [ ] Inglês/Espanhol: 8–12 exercícios `written_language` com `section: "escrita"` e passo no roteiro
- [ ] Geografia: aba `interactive_maps` com todos os `brazil_map`; aba `capital_game` com jogo das 27 capitais; ≥1 exercício MC com `visual` de mapa
- [ ] 15–18 exercícios autossuficientes (mín. 12) + 10 desafios avançados (Matemática)
- [ ] Gráficos: exemplo renderizado nas explicações + ≥1 exercício com `visual` (contexto diferente); variar pizza/barras/linhas conforme o caderno
- [ ] Questões I–IV sem padrão repetido de gabarito
- [ ] Zero imagens no HTML de conteúdo
- [ ] `pytest` passando
- [ ] `generation-metadata.json` com `audit_status: passed`
- [ ] Informar ao usuário: caminho do output e comando para regenerar

---

## Referências

- Padrão completo: [docs/playbook/pe-review-pattern.md](../../docs/playbook/pe-review-pattern.md)
- Nomes, manifest e snippets: [reference.md](reference.md)
- Orquestração geral: [AGENTS.md](../../AGENTS.md) (skills granulares são etapas internas deste fluxo)
