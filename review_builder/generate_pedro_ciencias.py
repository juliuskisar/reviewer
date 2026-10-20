"""Gera revisão de Ciências PE para Pedro — salva em output/pedro-pe-ciencias-2tri/."""

from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

from review_builder.auditor import audit_and_save
from review_builder.composer import compose_page
from review_builder.pedro_ciencias_content import REVIEW_ID, build_content, build_exercises
from review_builder.schema_validator import validate_contract
from review_builder.utils import PROJECT_ROOT, load_yaml, save_json

FOLDER_NAME = "pedro-pe-ciencias-2tri"
HTML_NAME = "index.html"
OUTPUT_DIR = PROJECT_ROOT / "output" / FOLDER_NAME
ASSETS_SRC = PROJECT_ROOT / "assets" / "pedro_pe_ciencias_2_tri"
WORKSPACE = PROJECT_ROOT / "workspace" / REVIEW_ID


def build_material_map() -> dict:
    manifest = load_yaml(ASSETS_SRC / "manifest.yaml")
    assets = []
    for entry in manifest.get("assets", []):
        assets.append({
            "file": f"assets/pedro_pe_ciencias_2_tri/{entry['file']}",
            "format": "jpg",
            "order": entry["order"],
            "subject": "science",
            "unit": entry.get("unit", "science_pe"),
            "importance": entry.get("importance", "medium"),
            "classification": {
                "discipline": "science",
                "topics": [entry.get("unit", "science_pe")],
                "confidence": "observed",
                "observations": [entry.get("notes", "Página do caderno de Ciências")],
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
            {"id": "solid_waste", "label": "Resíduos sólidos", "source_assets": [], "confidence": "observed"},
            {"id": "waste_destinations", "label": "Destinos", "source_assets": [], "confidence": "observed"},
            {"id": "recycling", "label": "Reciclagem", "source_assets": [], "confidence": "observed"},
            {"id": "pollution_health", "label": "Poluição e saúde", "source_assets": [], "confidence": "observed"},
            {"id": "vectors_diseases", "label": "Vetores", "source_assets": [], "confidence": "observed"},
            {"id": "health_sanitation", "label": "Saúde e saneamento", "source_assets": [], "confidence": "observed"},
            {"id": "water_treatment", "label": "Tratamento de água", "source_assets": [], "confidence": "observed"},
            {"id": "sewage_sanitation", "label": "Esgoto e Brasil", "source_assets": [], "confidence": "observed"},
        ],
        "summary": {
            "total_assets": len(assets),
            "formats": ["jpg"],
            "disciplines_detected": ["science"],
            "unreadable_files": [],
            "duplicates": [],
        },
    }


def build_blueprint() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Ciências — PE 2º Trimestre",
        "discipline": "science",
        "student_grade": "6º ano",
        "objectives": [
            "Classificar RSU e RSS e identificar destinos de resíduos",
            "Explicar reciclagem, coleta seletiva, 4 Rs e PNRS",
            "Analisar poluição, metais pesados, vetores e doenças",
            "Compreender ETA, ETE e índices de saneamento no Brasil",
        ],
        "topics": [
            {"id": "solid_waste", "label": "Resíduos", "depth": "basic", "order": 1},
            {"id": "waste_destinations", "label": "Destinos", "depth": "basic", "order": 2},
            {"id": "recycling", "label": "Reciclagem", "depth": "basic", "order": 3},
            {"id": "pollution_health", "label": "Poluição", "depth": "basic", "order": 4},
            {"id": "vectors_diseases", "label": "Vetores", "depth": "basic", "order": 5},
            {"id": "health_sanitation", "label": "Saúde", "depth": "basic", "order": 6},
            {"id": "water_treatment", "label": "ETA", "depth": "basic", "order": 7},
            {"id": "sewage_sanitation", "label": "ETE", "depth": "basic", "order": 8},
        ],
        "sections": [
            {"id": "route", "type": "study_route", "title": "Roteiro de estudo", "order": 1},
            {"id": "explain", "type": "explanations", "title": "Explicações", "order": 2},
            {"id": "summary", "type": "quick_summary", "title": "Resumo rápido", "order": 3},
        ],
        "components": ["concept_grid", "comparison_table", "quiz", "route_steps"],
        "exercise_plan": {
            "total": 16,
            "distribution": [
                {"type": "multiple_choice", "count": 16, "difficulty": "basic"},
            ],
        },
        "prerequisites": ["Noções de meio ambiente e saúde"],
        "common_errors": [
            {
                "topic_id": "waste_destinations",
                "description": "Confundir lixão com aterro sanitário",
                "prevention_tip": "Aterro tem impermeabilização e coleta de chorume",
            },
            {
                "topic_id": "water_treatment",
                "description": "Achar que fluoretação desinfeta a água",
                "prevention_tip": "Desinfecção com cloro elimina microrganismos",
            },
            {
                "topic_id": "sewage_sanitation",
                "description": "Acreditar que todo o Brasil tem esgoto tratado",
                "prevention_tip": "Coleta e tratamento de esgoto ficam atrás da água tratada",
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
        "exam": "PE — Ciências 2º trimestre",
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
