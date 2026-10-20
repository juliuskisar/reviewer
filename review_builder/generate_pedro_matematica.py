"""Gera revisão de Matemática PE para Pedro — salva em output/pedro-pe-matematica-2tri/."""

from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

from review_builder.auditor import audit_and_save
from review_builder.composer import compose_page
from review_builder.pedro_matematica_content import REVIEW_ID, build_content, build_exercises
from review_builder.schema_validator import validate_contract
from review_builder.utils import PROJECT_ROOT, load_yaml, save_json

FOLDER_NAME = "pedro-pe-matematica-2tri"
HTML_NAME = "index.html"
OUTPUT_DIR = PROJECT_ROOT / "output" / FOLDER_NAME
ASSETS_SRC = PROJECT_ROOT / "assets" / "pedro_pe_matematica_2_tri"
WORKSPACE = PROJECT_ROOT / "workspace" / REVIEW_ID


def build_material_map() -> dict:
    manifest = load_yaml(ASSETS_SRC / "manifest.yaml")
    assets = []
    for entry in manifest.get("assets", []):
        assets.append({
            "file": f"assets/pedro_pe_matematica_2_tri/{entry['file']}",
            "format": "jpg",
            "order": entry["order"],
            "subject": "math",
            "unit": entry.get("unit", "math_pe"),
            "importance": entry.get("importance", "medium"),
            "classification": {
                "discipline": "math",
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
        "topics": [
            {"id": "expressions", "label": "Expressões numéricas", "source_assets": [], "confidence": "observed"},
            {"id": "decimal_multiply", "label": "Multiplicação decimal", "source_assets": [], "confidence": "observed"},
            {"id": "decimal_divide", "label": "Divisão decimal", "source_assets": [], "confidence": "observed"},
            {"id": "division_break", "label": "Divisão com/sem quebra", "source_assets": [], "confidence": "observed"},
            {"id": "division_fractions", "label": "Divisão e frações", "source_assets": [], "confidence": "observed"},
            {"id": "ratios", "label": "Razões", "source_assets": [], "confidence": "observed"},
            {"id": "mean", "label": "Média aritmética", "source_assets": [], "confidence": "observed"},
            {"id": "statistics", "label": "Gráficos e frações", "source_assets": [], "confidence": "observed"},
        ],
        "summary": {
            "total_assets": len(assets),
            "formats": ["jpg"],
            "disciplines_detected": ["math"],
            "unreadable_files": [],
            "duplicates": [],
        },
    }


def build_blueprint() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Matemática — PE 2º Trimestre",
        "discipline": "math",
        "student_grade": "6º ano",
        "objectives": [
            "Resolver expressões numéricas com ordem correta das operações",
            "Multiplicar e dividir números decimais",
            "Interpretar divisões com e sem subdivisão do resto",
            "Relacionar divisão com frações e calcular razões, médias e frações em gráficos",
        ],
        "topics": [
            {"id": "expressions", "label": "Expressões", "depth": "basic", "order": 1},
            {"id": "decimal_multiply", "label": "Mult. decimal", "depth": "basic", "order": 2},
            {"id": "decimal_divide", "label": "Div. decimal", "depth": "basic", "order": 3},
            {"id": "division_break", "label": "Com/sem quebra", "depth": "basic", "order": 4},
            {"id": "division_fractions", "label": "Frações", "depth": "basic", "order": 5},
            {"id": "ratios", "label": "Razões", "depth": "basic", "order": 6},
            {"id": "mean", "label": "Média", "depth": "basic", "order": 7},
            {"id": "statistics", "label": "Gráficos", "depth": "basic", "order": 8},
        ],
        "sections": [
            {"id": "route", "type": "study_route", "title": "Roteiro de estudo", "order": 1},
            {"id": "explain", "type": "explanations", "title": "Explicações", "order": 2},
            {"id": "summary", "type": "quick_summary", "title": "Resumo rápido", "order": 3},
        ],
        "components": ["concept_grid", "comparison_table", "quiz", "route_steps"],
        "exercise_plan": {
            "total": 28,
            "distribution": [
                {"type": "multiple_choice", "count": 18, "difficulty": "basic"},
                {"type": "multiple_choice", "count": 10, "difficulty": "advanced"},
            ],
        },
        "prerequisites": ["Operações com naturais e frações básicas"],
        "common_errors": [
            {
                "topic_id": "decimal_multiply",
                "description": "Errar posição da vírgula",
                "prevention_tip": "Somar casas decimais ou usar compensação",
            },
            {
                "topic_id": "expressions",
                "description": "Fazer adição antes da multiplicação",
                "prevention_tip": "× e ÷ antes de + e −",
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
        "student": "Pedro",
        "grade": "6º ano",
        "exam": "PE — Matemática 2º trimestre",
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
