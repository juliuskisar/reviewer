"""Gera revisão de Geografia PE 3º trimestre para Pedro — output/pedro-pe-geografia-3tri/."""

from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

from review_builder.auditor import audit_and_save
from review_builder.composer import compose_page
from review_builder.pedro_geografia_3tri_content import REVIEW_ID, build_content, build_exercises
from review_builder.schema_validator import validate_contract
from review_builder.utils import PROJECT_ROOT, load_yaml, save_json

FOLDER_NAME = "pedro-pe-geografia-3tri"
HTML_NAME = "index.html"
OUTPUT_DIR = PROJECT_ROOT / "output" / FOLDER_NAME
ASSETS_SRC = PROJECT_ROOT / "assets" / "pedro_pe_geografia_3_tri"
WORKSPACE = PROJECT_ROOT / "workspace" / REVIEW_ID

TOPICS = [
    {"id": "world_vegetation", "label": "Paisagens vegetais do mundo"},
    {"id": "biodiversity_hotspots", "label": "Biodiversidade e hotspots"},
    {"id": "brazil_biomes", "label": "Biomas e cobertura vegetal"},
    {"id": "brazil_forests_savannas", "label": "Florestas, Cerrado e Caatinga"},
    {"id": "brazil_coastal_wetlands", "label": "Pantanal, manguezais e litoral"},
    {"id": "water_earth_cycle", "label": "Água na Terra e ciclo hidrológico"},
    {"id": "hydrography_energy", "label": "Hidrografia, navegação e energia"},
    {"id": "water_pollution_aquifers", "label": "Usos, poluição e aquíferos"},
]


def build_material_map() -> dict:
    manifest = load_yaml(ASSETS_SRC / "manifest.yaml")
    assets = []
    for entry in manifest.get("assets", []):
        assets.append({
            "file": f"assets/pedro_pe_geografia_3_tri/{entry['file']}",
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
            {**t, "source_assets": [], "confidence": "observed"} for t in TOPICS
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
        "title": "Revisão de Geografia — PE 3º Trimestre",
        "discipline": "geography",
        "student_grade": "6º ano",
        "objectives": [
            "Comparar paisagens vegetais mundiais e critérios de hotspots",
            "Relacionar biomas brasileiros a clima, relevo e ação humana",
            "Explicar ciclo da água, bacias hidrográficas e matriz elétrica",
            "Analisar usos da água, poluição e aquíferos Guarani e SAGA",
        ],
        "topics": [
            {**t, "depth": "basic", "order": i + 1} for i, t in enumerate(TOPICS)
        ],
        "sections": [
            {"id": "route", "type": "study_route", "title": "Roteiro de estudo", "order": 1},
            {"id": "explain", "type": "explanations", "title": "Explicações", "order": 2},
            {"id": "summary", "type": "quick_summary", "title": "Resumo rápido", "order": 3},
            {"id": "maps", "type": "interactive_maps", "title": "Mapas interativos", "order": 4},
            {"id": "capital_game", "type": "capital_game", "title": "Jogo das capitais", "order": 5},
        ],
        "components": ["concept_grid", "comparison_table", "quiz", "route_steps", "brazil_map"],
        "exercise_plan": {
            "total": 16,
            "distribution": [{"type": "multiple_choice", "count": 16, "difficulty": "basic"}],
        },
        "prerequisites": ["Noções de clima e mapas do Brasil"],
        "common_errors": [
            {
                "topic_id": "biodiversity_hotspots",
                "description": "Achar que hotspot significa área bem preservada",
                "prevention_tip": "Hotspot = muita biodiversidade + perda de ≥70% da vegetação original",
            },
            {
                "topic_id": "hydrography_energy",
                "description": "Confundir matriz mundial com a brasileira",
                "prevention_tip": "No mundo predomina carvão; no Brasil, hidrelétrica (~65%)",
            },
            {
                "topic_id": "water_pollution_aquifers",
                "description": "Achar que aquífero Guarani é o maior em extensão no Brasil",
                "prevention_tip": "SAGA (Amazônia) é maior em área e volume; Guarani é transfronteiriço",
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
        "exam": "PE — Geografia 3º trimestre",
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
