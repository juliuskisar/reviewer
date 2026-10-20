# Revisão — Pedro | Geografia PE 2º trimestre

Material de entrada para a revisão de Geografia do Pedro (6º ano), Prova Específica do 2º trimestre.

## Configurações vinculadas

| Config | Arquivo |
|--------|---------|
| Aluno | `configs/students/pedro-student.yaml` |
| Prova | `configs/exams/pe-exam.yaml` |
| Disciplina | `configs/disciplines/geography-pe-6.yaml` |

## Origem das imagens

Copiadas de `imagens_geografia_pedro/` (48 fotos do Caderno 2 digital, Geografia, 6º ano).

Duplicatas com sufixo ` 2.JPG` foram ignoradas.

## Escopo da PE (Geografia)

Conteúdo **principal** (Módulos 5 e 6):

- Terra no Sistema Solar
- Estrutura interna da Terra
- Deriva continental e tectônica de placas
- Tipos de rochas e ciclo das rochas
- Formas de relevo (terrestre, submarino, brasileiro)

Conteúdo **complementar** presente nas imagens (Módulo 7+):

- Precipitações e tipos de chuva
- Fatores do tempo e do clima
- Pressão atmosférica e amplitude térmica

## Gerar a revisão

```bash
source .venv/bin/activate
python -m review_builder.generate_pedro
```

Saída: `output/pedro-pe-geografia-2tri/index.html` (HTML, CSS, JS e imagens na mesma pasta).
