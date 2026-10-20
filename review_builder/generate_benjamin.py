"""Gera revisão de História PE para Benjamin — salva em output/benjamin-pe-historia-2tri/."""

from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

from review_builder.auditor import audit_and_save
from review_builder.benjamin_content import REVIEW_ID, build_content, build_exercises
from review_builder.composer import compose_page
from review_builder.schema_validator import validate_contract
from review_builder.utils import PROJECT_ROOT, load_yaml, save_json

FOLDER_NAME = "benjamin-pe-historia-2tri"
HTML_NAME = "index.html"
OUTPUT_DIR = PROJECT_ROOT / "output" / FOLDER_NAME
ASSETS_SRC = PROJECT_ROOT / "assets" / "benjamin_pe_historia_2_tri"
WORKSPACE = PROJECT_ROOT / "workspace" / REVIEW_ID


def build_material_map() -> dict:
    manifest = load_yaml(ASSETS_SRC / "manifest.yaml")
    assets = []
    for entry in manifest.get("assets", []):
        assets.append({
            "file": f"assets/benjamin_pe_historia_2_tri/{entry['file']}",
            "format": "jpg",
            "order": entry["order"],
            "subject": "history",
            "unit": entry.get("unit", "history_pe"),
            "importance": entry.get("importance", "medium"),
            "classification": {
                "discipline": "history",
                "topics": [entry.get("unit", "history_pe")],
                "confidence": "observed",
                "observations": [entry.get("notes", "Página do caderno de História")],
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
            {"id": "prehistory", "label": "Pré-história e pinturas rupestres", "source_assets": [], "confidence": "observed"},
            {"id": "umbu_humaita", "label": "Tradições Umbu e Humaitá", "source_assets": [], "confidence": "observed"},
            {"id": "sambaquis", "label": "Sambaquis e sambaquieiros", "source_assets": [], "confidence": "observed"},
            {"id": "ceramists", "label": "Ceramistas da Amazônia", "source_assets": [], "confidence": "observed"},
            {"id": "tupi_guarani", "label": "Povo Tupi-Guarani", "source_assets": [], "confidence": "observed"},
            {"id": "commerce_spices", "label": "Comércio e especiarias", "source_assets": [], "confidence": "observed"},
            {"id": "travelers", "label": "Grandes viajantes", "source_assets": [], "confidence": "observed"},
            {"id": "portuguese_navigation", "label": "Navegações portuguesas", "source_assets": [], "confidence": "observed"},
        ],
        "summary": {
            "total_assets": len(assets),
            "formats": ["jpg"],
            "disciplines_detected": ["history"],
            "unreadable_files": [],
            "duplicates": [],
        },
    }


def build_blueprint() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de História — PE 2º Trimestre",
        "discipline": "history",
        "student_grade": "4º ano",
        "objectives": [
            "Conhecer vestígios da pré-história e dos povos indígenas do Brasil",
            "Diferenciar modos de vida nômade e sedentário",
            "Compreender comércio de especiarias e conexões entre continentes",
            "Reconhecer motivações e instrumentos das navegações portuguesas",
        ],
        "topics": [
            {"id": "prehistory", "label": "Pré-história", "depth": "basic", "order": 1},
            {"id": "umbu_humaita", "label": "Umbu e Humaitá", "depth": "basic", "order": 2},
            {"id": "sambaquis", "label": "Sambaquis", "depth": "basic", "order": 3},
            {"id": "ceramists", "label": "Ceramistas", "depth": "basic", "order": 4},
            {"id": "tupi_guarani", "label": "Tupi-Guarani", "depth": "basic", "order": 5},
            {"id": "commerce_spices", "label": "Comércio e especiarias", "depth": "basic", "order": 6},
            {"id": "travelers", "label": "Viajantes", "depth": "basic", "order": 7},
            {"id": "portuguese_navigation", "label": "Navegações", "depth": "basic", "order": 8},
        ],
        "sections": [
            {"id": "route", "type": "study_route", "title": "Roteiro de estudo", "order": 1},
            {"id": "explain", "type": "explanations", "title": "Explicações", "order": 2},
            {"id": "summary", "type": "quick_summary", "title": "Resumo rápido", "order": 3},
        ],
        "components": ["timeline", "comparison_table", "quiz", "concept_grid", "route_steps"],
        "exercise_plan": {
            "total": 12,
            "distribution": [
                {"type": "multiple_choice", "count": 12, "difficulty": "basic"},
            ],
        },
        "prerequisites": ["Noções de linha do tempo"],
        "common_errors": [
            {
                "topic_id": "sambaquis",
                "description": "Confundir sambaqui com montanha natural",
                "prevention_tip": "Sambaqui = amontoado de conchas (origem tupi)",
            },
            {
                "topic_id": "portuguese_navigation",
                "description": "Confundir caravela com nau",
                "prevention_tip": "Caravela menor e ágil; nau maior para carga",
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
        "exam": "PE — História 2º trimestre",
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
