"""Gera revisão de Ciências PE 3º trimestre para Benjamin — output/benjamin-pe-ciencias-3tri/."""

from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

from review_builder.auditor import audit_and_save
from review_builder.benjamin_ciencias_3tri_content import REVIEW_ID, build_content, build_exercises
from review_builder.composer import compose_page
from review_builder.schema_validator import validate_contract
from review_builder.utils import PROJECT_ROOT, load_yaml, save_json

FOLDER_NAME = "benjamin-pe-ciencias-3tri"
HTML_NAME = "index.html"
OUTPUT_DIR = PROJECT_ROOT / "output" / FOLDER_NAME
ASSETS_SRC = PROJECT_ROOT / "assets" / "benjamin_pe_ciencias_3_tri"
WORKSPACE = PROJECT_ROOT / "workspace" / REVIEW_ID

TOPICS = [
    {"id": "micro_intro", "label": "Microrganismos ao redor"},
    {"id": "lab_study", "label": "Investigação em laboratório"},
    {"id": "hand_hygiene", "label": "Higiene das mãos"},
    {"id": "food_prevention", "label": "Alimentos e prevenção"},
    {"id": "waste", "label": "Resíduos e decomposição"},
    {"id": "composting", "label": "Compostagem"},
    {"id": "yeasts", "label": "Leveduras e fermentação"},
    {"id": "antibiotics_vaccines", "label": "Antibióticos e vacinas"},
]


def build_material_map() -> dict:
    manifest = load_yaml(ASSETS_SRC / "manifest.yaml")
    assets = []
    for entry in manifest.get("assets", []):
        assets.append({
            "file": f"assets/benjamin_pe_ciencias_3_tri/{entry['file']}",
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
        "topics": [{**t, "source_assets": [], "confidence": "observed"} for t in TOPICS],
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
        "title": "Revisão de Ciências — PE 3º Trimestre",
        "discipline": "science",
        "student_grade": "4º ano",
        "objectives": [
            "Identificar microrganismos, doenças associadas e práticas de higiene",
            "Explicar meio de cultura, colônias e experimentos de mãos na escola",
            "Classificar resíduos e descrever compostagem e decomposição",
            "Relacionar leveduras, fermentação, pão e etanol",
            "Diferenciar antibióticos (bactérias) e vacinas (prevenção)",
        ],
        "topics": [{**t, "depth": "basic", "order": i + 1} for i, t in enumerate(TOPICS)],
        "sections": [
            {"id": "route", "type": "study_route", "title": "Roteiro de estudo", "order": 1},
            {"id": "explain", "type": "explanations", "title": "Explicações", "order": 2},
            {"id": "summary", "type": "quick_summary", "title": "Resumo rápido", "order": 3},
        ],
        "components": ["concept_grid", "comparison_table", "quiz", "route_steps"],
        "exercise_plan": {
            "total": 16,
            "distribution": [{"type": "multiple_choice", "count": 16, "difficulty": "basic"}],
        },
        "prerequisites": ["Noções de seres vivos e meio ambiente"],
        "common_errors": [
            {
                "topic_id": "antibiotics_vaccines",
                "description": "Usar antibiótico para gripe ou resfriado",
                "prevention_tip": "Gripe é vírus — antibiótico só para infecção bacteriana com receita",
            },
            {
                "topic_id": "waste",
                "description": "Confundir lixo (rejeito) com resíduo reciclável",
                "prevention_tip": "Rejeito = sem utilidade · reciclável = vira matéria-prima nova",
            },
            {
                "topic_id": "hand_hygiene",
                "description": "Achar que álcool em gel substitui sabão com sujeira visível",
                "prevention_tip": "Sabão e água removem sujeira; gel complementa quando as mãos estão limpas",
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
        "exam": "PE — Ciências 3º trimestre",
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
