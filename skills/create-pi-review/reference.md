# Referência — create-pi-review

## Árvore de arquivos por revisão

Exemplo: Pedro, 6º ano, PI multidisciplinar.

```
configs/students/pedro-student.yaml
configs/exams/pi-exam.yaml

imagens_pi_pedro/                    # entrada do usuário
  ingles/*.jpg
  geografia/*.jpg
  matematica/*.jpg
  …

assets/pedro_pi_6_ano/
  manifest.yaml
  ingles/page-001.jpg …
  geografia/page-001.jpg …
  …

output/pedro-pi-6ano/
  index.html                         # HTML monolítico (derivado de PI_review.html)
  generation-metadata.json

review_builder/pedro_pi_content.py   # opcional — dados exportáveis para o HTML
```

---

## Manifest multidisciplinar

```yaml
version: 1
review:
  id: pedro-pi-6ano
  title: Revisão Multidisciplinar — PI (Pedro, 6º ano)
student:
  config: configs/students/pedro-student.yaml
exam:
  config: configs/exams/pi-exam.yaml
disciplines:
  - id: ingles
    label: Inglês
    assets_dir: ingles
    assets:
      - file: ingles/page-001.jpg
        order: 1
  - id: geografia
    label: Geografia
    assets_dir: geografia
    assets:
      - file: geografia/page-001.jpg
        order: 1
  # … uma entrada por disciplina
```

---

## Objeto `subjects` — estrutura mínima

```javascript
const subjects = {
  geografia: {
    title: "Geografia",
    icon: "GE",
    sections: {
      percurso: `<p>Módulos 5 e 6: …</p><ol><li>Comece pelo <strong>Resumo</strong>…</li></ol>`,
      explicacao: `<h3>1. Tópico</h3><p>…</p>`,
      resumo: `<h3>Síntese</h3><table>…</table>`,
      dicas: `<ul><li>Pegadinha: …</li></ul>`,
    },
    exercises: [
      {
        type: "multiple-choice",
        question: "…",
        options: ["A", "B", "C", "D"],
        correctAnswer: 1,
        explanation: "…",
        modelAnswer: "Resposta correta: B.",
      },
      {
        type: "short-answer",
        question: "…",
        keywords: ["palavra-chave", "sinônimo"],
        explanation: "…",
        modelAnswer: "Resposta esperada: …",
      },
    ],
  },
  // … demais disciplinas
};
```

---

## Objeto `simulado` — estrutura mínima

```javascript
const simulado = {
  title: "Simulado da PI",
  icon: "★",
  intro: "Um teste com N questões, ligadas ao texto abaixo e ao conteúdo das disciplinas.",
  textTitle: "Texto-base — Título do tema integrador",
  text: `
    <p>Parágrafo 1 com <strong>dados</strong> exploráveis em várias disciplinas…</p>
    <p>Parágrafo 2…</p>
  `,
  questions: [
    {
      discipline: "Geografia",
      question: "…",
      options: ["…", "…", "…", "…"],
      correctAnswer: 1,
      explanation: "…",
    },
    {
      discipline: "Matemática",
      question: "…",
      options: ["…", "…", "…", "…"],
      correctAnswer: 2,
      explanation: "…",
    },
    // 2–5 por disciplina
  ],
};
```

---

## SECTION_TEMPLATE (ordem fixa)

```javascript
const SECTION_TEMPLATE = [
  { key: "percurso",   title: "1. Percurso de estudo",      openByDefault: true  },
  { key: "conteudo",   title: "2. Conteúdo",                openByDefault: false },
  { key: "exercicios", title: "3. Exercícios interativos",   openByDefault: false },
  { key: "dicas",      title: "4. Dicas finais de prova",    openByDefault: false },
];
```

A seção `conteudo` usa `sections.resumo` + `sections.explicacao` com switch interno.

---

## Disciplinas típicas por série

### 6º ano (referência Pedro — `PI_review.html`)

| Chave | Disciplina | Exercícios ref. | Simulado ref. |
|-------|------------|-----------------|---------------|
| ingles | Inglês | ~8 | 2 |
| geografia | Geografia | ~10 | 4 |
| matematica | Matemática | ~12 | 5 |
| desenho | Desenho Geométrico | ~6 | 2 |
| ciencias | Ciências | ~10 | 5 |
| portugues | Língua Portuguesa | ~8 | 4 |
| espanhol | Espanhol | ~6 | 2 |
| historia | História | ~8 | 4 |

### 4º ano (adaptar)

Incluir só disciplinas com material (`imagens_pi_<aluno>/<disciplina>/`). Comum: Português, Matemática, Ciências, História, Geografia — **sem** Espanhol/Inglês se não houver pasta.

---

## Texto-base do simulado — critérios

Escolher tema que permita:

| Disciplina | Tipo de questão possível |
|------------|--------------------------|
| Geografia | Continentes, relevo, clima, localização |
| Matemática | Contas com dados do texto, porcentagem, potência |
| Português | Interpretação, concordância, coesão, sintaxe |
| Ciências | Método científico, propriedades da matéria, fenômenos |
| História | Tempo histórico vs cronológico, cultura, etnocentrismo |
| Inglês | Past simple, there was/were, vocabulário contextual |
| Espanhol | Nacionalidade, estar/ser, localização |
| Desenho | Euler, geometria sólida, relações V+F=A+2 |

---

## Snippet `generation-metadata.json`

```json
{
  "review_id": "pedro-pi-6ano",
  "student": "Pedro",
  "grade": "6º ano",
  "exam": "PI — Prova Integrada",
  "format": "monolith_html",
  "template": "PI_review.html",
  "disciplines": ["ingles", "geografia", "matematica", "desenho", "ciencias", "portugues", "espanhol", "historia"],
  "simulado_questions": 28,
  "output_path": "output/pedro-pi-6ano/",
  "generated_at": "2026-…"
}
```

---

## Prompt rápido para o usuário

```
Nova revisão PI:
- Aluno:
- Série:
- Imagens em: imagens_pi_<aluno>/   (subpastas por disciplina)
- Disciplinas: (ou inferir das subpastas)
- Salvar em: output/<aluno>-pi-<serie-slug>/
```

---

## Migração futura (pipeline)

Quando `review_builder` suportar PI:

1. Contrato `pi-review-content.json` com array `disciplines[]`
2. Compositor gera HTML a partir do template
3. Auditoria valida gabaritos e autossuficiência
4. Skill passará a preferir pipeline; monolítico vira fallback

Até lá, **copiar `PI_review.html` e substituir dados** é o workflow oficial.
