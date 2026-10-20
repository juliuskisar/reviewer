"""Gera revisão de Matemática PE 3º trimestre para Benjamin — output/benjamin-pe-matematica-3tri/."""

from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

from review_builder.auditor import audit_and_save
from review_builder.benjamin_matematica_3tri_content import REVIEW_ID, build_content, build_exercises
from review_builder.composer import compose_page
from review_builder.schema_validator import validate_contract
from review_builder.utils import PROJECT_ROOT, load_yaml, save_json

FOLDER_NAME = "benjamin-pe-matematica-3tri"
HTML_NAME = "index.html"
OUTPUT_DIR = PROJECT_ROOT / "output" / FOLDER_NAME
ASSETS_SRC = PROJECT_ROOT / "assets" / "benjamin_pe_matematica_3_tri"
WORKSPACE = PROJECT_ROOT / "workspace" / REVIEW_ID

TOPICS = [
    {"id": "equality_balance", "label": "Igualdade e balança"},
    {"id": "inverse_operations", "label": "Operações inversas"},
    {"id": "multiplication_table", "label": "Regularidades da tabuada"},
    {"id": "quadrilaterals", "label": "Quadriláteros"},
    {"id": "trapezoids_parallelograms", "label": "Trapézios e paralelogramos"},
    {"id": "rectangles_rhombuses", "label": "Retângulos e losangos"},
    {"id": "decimals_intro", "label": "Números decimais"},
    {"id": "money_decimals", "label": "Sistema monetário"},
]


def build_material_map() -> dict:
    manifest = load_yaml(ASSETS_SRC / "manifest.yaml")
    assets = []
    for entry in manifest.get("assets", []):
        assets.append({
            "file": f"assets/benjamin_pe_matematica_3_tri/{entry['file']}",
            "format": "jpg",
            "order": entry["order"],
            "subject": "mathematics",
            "unit": entry.get("unit", "math_pe"),
            "importance": entry.get("importance", "medium"),
            "classification": {
                "discipline": "mathematics",
                "topics": [entry.get("unit", "math_pe")],
                "confidence": "observed",
                "observations": [entry.get("notes", "Página do caderno de Matemática")],
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
        "topics": [{**t, "source_assets": [], "confidence": "observed"} for t in TOPICS],
        "summary": {
            "total_assets": len(assets),
            "formats": ["jpg"],
            "disciplines_detected": ["mathematics"],
            "unreadable_files": [],
            "duplicates": [],
        },
    }


def build_blueprint() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Matemática — PE 3º Trimestre",
        "discipline": "mathematics",
        "student_grade": "4º ano",
        "objectives": [
            "Manter igualdades transformando os dois membros da mesma forma",
            "Usar adição e subtração como operações inversas",
            "Aplicar comutativa e regularidades da tabuada",
            "Classificar quadriláteros, trapézios, paralelogramos, retângulos e losangos",
            "Ler, comparar e escrever números decimais e valores em reais",
        ],
        "topics": [{**t, "depth": "basic", "order": i + 1} for i, t in enumerate(TOPICS)],
        "sections": [
            {"id": "route", "type": "study_route", "title": "Roteiro de estudo", "order": 1},
            {"id": "explain", "type": "explanations", "title": "Explicações", "order": 2},
            {"id": "summary", "type": "quick_summary", "title": "Resumo rápido", "order": 3},
        ],
        "components": ["concept_grid", "comparison_table", "quiz", "route_steps", "line_chart"],
        "exercise_plan": {
            "total": 26,
            "distribution": [
                {"type": "multiple_choice", "count": 16, "difficulty": "basic"},
                {"type": "multiple_choice", "count": 10, "difficulty": "advanced"},
            ],
        },
        "prerequisites": ["Operações básicas e noções de ângulo reto"],
        "common_errors": [
            {
                "topic_id": "trapezoids_parallelograms",
                "description": "Achar que todo paralelogramo é trapézio",
                "prevention_tip": "Trapézio tem só um par de lados paralelos",
            },
            {
                "topic_id": "decimals_intro",
                "description": "Comparar 3,5 com 3,05 ignorando a casa dos décimos",
                "prevention_tip": "Alinhe vírgula e compare casa a casa",
            },
            {
                "topic_id": "money_decimals",
                "description": "Confundir centavos (centésimos) com reais inteiros",
                "prevention_tip": "Após a vírgula, cada algarismo é fração do real",
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
        "exam": "PE — Matemática 3º trimestre",
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
