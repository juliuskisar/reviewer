# Padrão de revisão PE (aprendizados — Pedro / Geografia)

**Skill operacional:** `skills/create-pe-review/SKILL.md` — use esta skill para criar novas revisões PE.

Guia de referência visual/pedagógico abaixo. Implementação de exemplo: `review_builder/pedro_content.py`, `review_builder/generate_pedro.py`, `output/pedro-pe-geografia-2tri/`.

---

## Estrutura da página

### Seções (abas)

| Aba | Tipo | Conteúdo |
|-----|------|----------|
| Roteiro de estudo | `study_route` | Intro, concept-grid dos módulos, passos com links |
| Explicações | `explanations` | Acordeões por tópico |
| Resumo rápido | `quick_summary` | **Mesma estética** — acordeões + concept-grid + tabelas |
| Mapas interativos | `interactive_maps` | **Geografia** — mapas SVG clicáveis (`brazil_map`) reunidos numa aba |
| Exercícios | (aba separada) | Quiz interativo — `section: exercises` ou `final_quiz` |
| Prática escrita | (aba separada, **Inglês/Espanhol**) | 8–12 itens `written_language` — `section: escrita`; correção offline |
| Desafios | (aba separada, opcional) | 10 questões avançadas — `section: desafios` |

**Não incluir por padrão:** `attention_points`, `guided_examples`, `exam_tips`, `parent_support` — pegadinhas e dicas vão em callouts dentro do resumo/explicações.

### Blocos visuais (sem imagens no HTML)

- `panel_intro` — abertura de seção
- `concept_grid` — cards com ícone, título e texto curto (estilo OBA)
- `callout` — variantes: `remember`, `accent`, `info`
- `comparison_table` — tabelas sintéticas
- `route_steps` — passos numerados com `panel` + botão navegável

**Não usar** blocos `image` no conteúdo — a página deve funcionar offline só com texto estruturado.

**Exceção — visuais HTML:** blocos `bar_chart`, `fraction_visual` e `brazil_map` renderizam gráficos, frações e mapas em HTML/SVG (sem JPG, offline).

### Roteiro com links

Cada passo em `route_steps` deve ter:

```json
{
  "title": "Estude as Explicações",
  "panel": "explain",
  "panel_label": "Explicações",
  "description": "...",
  "tip": "..."
}
```

O template renderiza `data-goto-panel="panel-{panel}"` — o aluno clica e vai à aba.

---

## Conteúdo pedagógico

1. **Ler todas as imagens** do material antes de redigir (pasta `imagens_*` ou `assets/`).
2. **Paráfrasear** — não copiar trechos longos do caderno.
3. **Blocos curtos** — adequados à série (`configs/students/`).
4. **Profundidade** — cobrir todos os tópicos dos módulos da PE, não só vocabulário solto.
5. **Resumo completo** — um acordeão por tópico principal, não lista única.

---

## Exercícios

### Estilo

- Basear nos **Testes** e **Atividades** do caderno (afirmativas I–IV, notícias curtas, completar raciocínio).
- Dificuldade alinhada ao material, não genérica.

### Regras obrigatórias

1. **Autossuficientes** — enunciado completo sem exigir imagem, mapa ou diagrama que não está na página.
2. **Não escrever** “Observe a ilustração/mapa/diagrama” se o asset não for exibido no HTML.
3. **Preferir** texto contextual embutido (notícia, lista de afirmativas, descrição do esquema em palavras).
4. **Explicação** sempre presente em múltipla escolha.
5. **`source_assets`** para rastreabilidade interna — não implica exibir JPG na página.
6. **Análise de gráfico:** use campo `visual` no exercício (`bar_chart` ou `fraction_visual`) quando a resolução exige interpretar um gráfico — enunciado começa com “Observe o gráfico/figura…”. Nas **explicações**, inclua exemplo renderizado com **outro contexto**.
7. **Afirmativas I–IV:** variar a combinação correta — **nunca** repetir “I, III e IV” como padrão em toda a revisão; distribuir `correct_answer` entre 0–3.

---

## Arquivos por revisão

```
configs/students/<aluno>.yaml
configs/disciplines/<disciplina-pe>.yaml
assets/<review_assets>/
  manifest.yaml
  page-001.jpg …
review_builder/<aluno>_content.py   # build_content(), build_exercises()
review_builder/generate_<aluno>.py  # pipeline completo
output/<review-id>/
  index.html
  review.css
  review.js
  generation-metadata.json
```

Comando: `python -m review_builder.generate_<aluno>`

---

## Checklist antes de entregar

- [ ] 3 seções de conteúdo + aba Exercícios (+ Desafios se Matemática)
- [ ] Explicações e resumo em acordeões com concept-grids
- [ ] Roteiro com botões que navegam às abas
- [ ] Zero imagens no HTML de conteúdo
- [ ] Exercícios resolvíveis sem material visual externo
- [ ] Linguagem adequada à série do aluno
- [ ] `pytest` passando
- [ ] Auditoria `passed`
