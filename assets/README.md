# Assets de entrada

Coloque aqui os materiais educacionais usados para gerar revisões.

## Estrutura recomendada

```text
assets/
└── <identificador-da-revisao>/
    ├── manifest.yaml          # opcional — metadados e ordem dos arquivos
    ├── page-001.jpg
    ├── teacher-notes.jpg
    └── ...
```

## Manifesto

O arquivo `manifest.yaml` é **opcional**. Quando ausente, a skill `inspect-assets`
propõe um manifesto inicial com base nos arquivos encontrados.

Consulte `example-review/manifest.yaml` como referência.

## Política

- **Não modifique** assets originais durante a geração.
- Use caminhos relativos no manifesto.
- Formatos suportados: imagens (jpg, png, webp), PDF, texto (txt, md).
- Arquivos ilegíveis são registrados em `material-map.json`, não ignorados silenciosamente.
