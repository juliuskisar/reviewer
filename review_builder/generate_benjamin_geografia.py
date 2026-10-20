"""Gera revisão de Geografia PE para Benjamin — salva em output/benjamin-pe-geografia-2tri/."""

from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

from review_builder.auditor import audit_and_save
from review_builder.benjamin_geografia_content import REVIEW_ID, build_content, build_exercises
from review_builder.composer import compose_page
from review_builder.schema_validator import validate_contract
from review_builder.utils import PROJECT_ROOT, load_yaml, save_json

FOLDER_NAME = "benjamin-pe-geografia-2tri"
HTML_NAME = "index.html"
OUTPUT_DIR = PROJECT_ROOT / "output" / FOLDER_NAME
ASSETS_SRC = PROJECT_ROOT / "assets" / "benjamin_pe_geografia_2_tri"
WORKSPACE = PROJECT_ROOT / "workspace" / REVIEW_ID


def build_material_map() -> dict:
    manifest = load_yaml(ASSETS_SRC / "manifest.yaml")
    assets = []
    for entry in manifest.get("assets", []):
        assets.append({
            "file": f"assets/benjamin_pe_geografia_2_tri/{entry['file']}",
            "format": "jpg",
            "order": entry["order"],
            "subject": "geography",
            "unit": entry.get("unit", "geography_pe"),
            "importance": entry.get("importance", "medium"),
            "classification": {
                "discipline": "geography",
                "topics": [entry.get("unit", "geography_pe")],
                "confidence": "observed",
                "observations": [entry.get("notes", "Página do caderno de Geografia")],
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
            {"id": "flag", "label": "Bandeira", "source_assets": [], "confidence": "observed"},
            {"id": "stars", "label": "Estrelas", "source_assets": [], "confidence": "observed"},
            {"id": "political_maps", "label": "Mapas políticos", "source_assets": [], "confidence": "observed"},
            {"id": "new_states", "label": "Novos estados", "source_assets": [], "confidence": "observed"},
            {"id": "mato_grosso", "label": "Mato Grosso", "source_assets": [], "confidence": "observed"},
            {"id": "goias_tocantins", "label": "Goiás/Tocantins", "source_assets": [], "confidence": "observed"},
            {"id": "borders", "label": "Divisas", "source_assets": [], "confidence": "observed"},
            {"id": "physical_maps", "label": "Mapas físicos", "source_assets": [], "confidence": "observed"},
        ],
        "summary": {
            "total_assets": len(assets),
            "formats": ["jpg"],
            "disciplines_detected": ["geography"],
            "unreadable_files": [],
            "duplicates": [],
        },
    }


def build_blueprint() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Geografia — PE 2º Trimestre",
        "discipline": "geography",
        "student_grade": "4º ano",
        "objectives": [
            "Compreender a bandeira do Brasil e o significado das cores e estrelas",
            "Relacionar estrelas da bandeira às unidades federativas ao longo do tempo",
            "Analisar mapas políticos históricos do Brasil",
            "Explicar criação de Mato Grosso do Sul e Tocantins",
            "Diferenciar mapa político e físico; interpretar altitude",
            "Reconhecer divisas e propostas de divisão territorial",
        ],
        "topics": [
            {"id": "flag", "label": "Bandeira", "depth": "basic", "order": 1},
            {"id": "stars", "label": "Estrelas", "depth": "basic", "order": 2},
            {"id": "political_maps", "label": "Mapas políticos", "depth": "basic", "order": 3},
            {"id": "new_states", "label": "Novos estados", "depth": "basic", "order": 4},
            {"id": "mato_grosso", "label": "Mato Grosso", "depth": "basic", "order": 5},
            {"id": "goias_tocantins", "label": "Goiás/Tocantins", "depth": "basic", "order": 6},
            {"id": "borders", "label": "Divisas", "depth": "basic", "order": 7},
            {"id": "physical_maps", "label": "Mapas físicos", "depth": "basic", "order": 8},
        ],
        "sections": [
            {"id": "route", "type": "study_route", "title": "Roteiro de estudo", "order": 1},
            {"id": "explain", "type": "explanations", "title": "Explicações", "order": 2},
            {"id": "summary", "type": "quick_summary", "title": "Resumo rápido", "order": 3},
            {"id": "maps", "type": "interactive_maps", "title": "Mapas interativos", "order": 4},
            {"id": "capital_game", "type": "capital_game", "title": "Jogo das capitais", "order": 5},
        ],
        "components": ["concept_grid", "comparison_table", "quiz", "route_steps", "brazil_map", "capital_game"],
        "exercise_plan": {
            "total": 16,
            "distribution": [
                {"type": "multiple_choice", "count": 16, "difficulty": "basic"},
            ],
        },
        "prerequisites": ["Noções de mapas e regiões do Brasil"],
        "common_errors": [
            {
                "topic_id": "stars",
                "description": "Esquecer o Distrito Federal nas estrelas",
                "prevention_tip": "27 estrelas = 26 estados + DF",
            },
            {
                "topic_id": "mato_grosso",
                "description": "Confundir capitais de MT e MS",
                "prevention_tip": "Cuiabá = MT; Campo Grande = MS",
            },
            {
                "topic_id": "physical_maps",
                "description": "Confundir mapa político com físico",
                "prevention_tip": "Político = divisas; físico = relevo e altitude",
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
        "exam": "PE — Geografia 2º trimestre",
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
