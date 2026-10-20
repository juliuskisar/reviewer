"""Gera revisão de Português PE para Benjamin — salva em output/benjamin-pe-portugues-2tri/."""

from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

from review_builder.auditor import audit_and_save
from review_builder.benjamin_portugues_content import REVIEW_ID, build_content, build_exercises
from review_builder.composer import compose_page
from review_builder.schema_validator import validate_contract
from review_builder.utils import PROJECT_ROOT, load_yaml, save_json

FOLDER_NAME = "benjamin-pe-portugues-2tri"
HTML_NAME = "index.html"
OUTPUT_DIR = PROJECT_ROOT / "output" / FOLDER_NAME
ASSETS_SRC = PROJECT_ROOT / "assets" / "benjamin_pe_portugues_2_tri"
WORKSPACE = PROJECT_ROOT / "workspace" / REVIEW_ID


def build_material_map() -> dict:
    manifest = load_yaml(ASSETS_SRC / "manifest.yaml")
    assets = []
    for entry in manifest.get("assets", []):
        assets.append({
            "file": f"assets/benjamin_pe_portugues_2_tri/{entry['file']}",
            "format": "jpg",
            "order": entry["order"],
            "subject": "portuguese",
            "unit": entry.get("unit", "portuguese_pe"),
            "importance": entry.get("importance", "medium"),
            "classification": {
                "discipline": "portuguese",
                "topics": [entry.get("unit", "portuguese_pe")],
                "confidence": "observed",
                "observations": [entry.get("notes", "Página do caderno de Português")],
                "inferences": [],
                "uncertainties": [],
            },
        })
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "manifest_present": True,
        "assets": assets,
        "topics": [
            {"id": "infographic", "label": "Infográfico", "source_assets": [], "confidence": "observed"},
            {"id": "joca_reading", "label": "Texto Joca", "source_assets": [], "confidence": "observed"},
            {"id": "visual_resources", "label": "Recursos visuais", "source_assets": [], "confidence": "observed"},
            {"id": "suffixes", "label": "Sufixos", "source_assets": [], "confidence": "observed"},
            {"id": "nasal", "label": "Nasalidade", "source_assets": [], "confidence": "observed"},
            {"id": "research", "label": "Pesquisa escolar", "source_assets": [], "confidence": "observed"},
            {"id": "dictionary", "label": "Dicionário", "source_assets": [], "confidence": "observed"},
            {"id": "encyclopedia", "label": "Enciclopédia", "source_assets": [], "confidence": "observed"},
        ],
        "summary": {
            "total_assets": len(assets),
            "formats": ["jpg"],
            "disciplines_detected": ["portuguese"],
            "unreadable_files": [],
            "duplicates": [],
        },
    }


def build_blueprint() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Português — PE 2º Trimestre",
        "discipline": "portuguese",
        "student_grade": "4º ano",
        "objectives": [
            "Interpretar infográficos e textos informativos sobre brincadeiras",
            "Formar palavras derivadas com sufixos e aplicar regras de nasalidade",
            "Realizar pesquisa escolar com citação de fontes",
            "Ler verbetes de dicionário e artigos enciclopédicos",
        ],
        "topics": [
            {"id": "infographic", "label": "Infográfico", "depth": "basic", "order": 1},
            {"id": "joca_reading", "label": "Texto Joca", "depth": "basic", "order": 2},
            {"id": "visual_resources", "label": "Recursos visuais", "depth": "basic", "order": 3},
            {"id": "suffixes", "label": "Sufixos", "depth": "basic", "order": 4},
            {"id": "nasal", "label": "Nasalidade", "depth": "basic", "order": 5},
            {"id": "research", "label": "Pesquisa", "depth": "basic", "order": 6},
            {"id": "dictionary", "label": "Dicionário", "depth": "basic", "order": 7},
            {"id": "encyclopedia", "label": "Enciclopédia", "depth": "basic", "order": 8},
        ],
        "sections": [
            {"id": "route", "type": "study_route", "title": "Roteiro de estudo", "order": 1},
            {"id": "explain", "type": "explanations", "title": "Explicações", "order": 2},
            {"id": "summary", "type": "quick_summary", "title": "Resumo rápido", "order": 3},
            {"id": "game_brincadeira", "type": "study_game", "title": "Jogo: Brincadeira certa", "order": 4},
            {"id": "game_sufixo", "type": "study_game", "title": "Jogo: Detetive do sufixo", "order": 5},
        ],
        "components": ["concept_grid", "comparison_table", "quiz", "route_steps", "study_game", "bar_chart"],
        "exercise_plan": {
            "total": 16,
            "distribution": [
                {"type": "multiple_choice", "count": 16, "difficulty": "basic"},
            ],
        },
        "prerequisites": ["Leitura fluente de textos curtos"],
        "common_errors": [
            {
                "topic_id": "infographic",
                "description": "Confundir infográfico com texto só verbal",
                "prevention_tip": "Infográfico sempre mistura palavras e recursos visuais",
            },
            {
                "topic_id": "suffixes",
                "description": "Escrever -ês com z",
                "prevention_tip": "Nacionalidade = -ês/-esa sempre com s",
            },
            {
                "topic_id": "dictionary",
                "description": "Confundir dicionário com enciclopédia",
                "prevention_tip": "Dicionário = palavra · enciclopédia = assunto",
            },
        ],
        "source_mapping_required": True,
    }


def run() -> Path:
    WORKSPACE.mkdir(parents=True, exist_ok=True)
    content = build_content()
    exercises = build_exercises()
    material_map = build_material_map()
    blueprint = build_blueprint()

    save_json(WORKSPACE / "material-map.json", material_map)
    save_json(WORKSPACE / "review-blueprint.json", blueprint)
    save_json(WORKSPACE / "review-content.json", content)
    save_json(WORKSPACE / "exercises.json", exercises)

    for name, data in [
        ("material-map", material_map),
        ("review-blueprint", blueprint),
        ("review-content", content),
        ("exercises", exercises),
    ]:
        errors = validate_contract(name, data)
        if errors:
            raise RuntimeError(f"Schema {name}: {errors}")

    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    html_path = compose_page(
        WORKSPACE / "review-content.json",
        WORKSPACE / "exercises.json",
        OUTPUT_DIR,
        assets_root=ASSETS_SRC,
        assets_href_prefix="",
        html_filename=HTML_NAME,
        assets_out_dir=OUTPUT_DIR,
    )

    report = audit_and_save(
        REVIEW_ID,
        WORKSPACE,
        html_path,
        WORKSPACE / "audit-report.json",
        assets_dir=OUTPUT_DIR,
    )

    if report["status"] == "failed":
        raise RuntimeError(f"Auditoria falhou: {report.get('blocking_issues')}")

    save_json(OUTPUT_DIR / "generation-metadata.json", {
        "review_id": REVIEW_ID,
        "student": "Benjamin",
        "grade": "4º ano",
        "exam": "PE — Português 2º trimestre",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "audit_status": report["status"],
        "html_file": HTML_NAME,
        "output_path": f"output/{FOLDER_NAME}/",
    })

    return html_path


def main() -> None:
    path = run()
    print(f"Revisão gerada: {path}")
    print(f"Pasta: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
