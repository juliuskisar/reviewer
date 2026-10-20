"""Gera revisão de Ciências PE para Helena — salva em output/helena-pe-ciencias-2tri/."""

from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

from review_builder.auditor import audit_and_save
from review_builder.composer import compose_page
from review_builder.helena_ciencias_content import REVIEW_ID, build_content, build_exercises
from review_builder.schema_validator import validate_contract
from review_builder.utils import PROJECT_ROOT, load_yaml, save_json

FOLDER_NAME = "helena-pe-ciencias-2tri"
HTML_NAME = "index.html"
OUTPUT_DIR = PROJECT_ROOT / "output" / FOLDER_NAME
ASSETS_SRC = PROJECT_ROOT / "assets" / "helena_pe_ciencias_2_tri"
WORKSPACE = PROJECT_ROOT / "workspace" / REVIEW_ID


def build_material_map() -> dict:
    manifest = load_yaml(ASSETS_SRC / "manifest.yaml")
    assets = []
    for entry in manifest.get("assets", []):
        assets.append({
            "file": f"assets/helena_pe_ciencias_2_tri/{entry['file']}",
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
            {"id": "air_composition", "label": "Composição do ar", "source_assets": [], "confidence": "observed"},
            {"id": "atmospheric_pollutants", "label": "Poluentes", "source_assets": [], "confidence": "observed"},
            {"id": "greenhouse_warming", "label": "Efeito estufa", "source_assets": [], "confidence": "observed"},
            {"id": "ozone_acid_rain", "label": "Ozônio e chuva ácida", "source_assets": [], "confidence": "observed"},
            {"id": "indoor_pollution", "label": "Ar interno", "source_assets": [], "confidence": "observed"},
            {"id": "respiratory_thermal", "label": "Respiração", "source_assets": [], "confidence": "observed"},
            {"id": "sanitation_floods", "label": "Saneamento", "source_assets": [], "confidence": "observed"},
            {"id": "diseases", "label": "Doenças", "source_assets": [], "confidence": "observed"},
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
        "student_grade": "7º ano",
        "objectives": [
            "Descrever composição do ar e poluentes atmosféricos",
            "Explicar efeito estufa, aquecimento global e ciclo do carbono",
            "Diferenciar ozônio troposférico e estratosférico; compreender chuva ácida",
            "Analisar poluição do ar interno e doenças respiratórias",
            "Relacionar saneamento, enchentes e doenças hídricas e por vetores",
        ],
        "topics": [
            {"id": "air_composition", "label": "Ar", "depth": "basic", "order": 1},
            {"id": "atmospheric_pollutants", "label": "Poluentes", "depth": "basic", "order": 2},
            {"id": "greenhouse_warming", "label": "Clima", "depth": "basic", "order": 3},
            {"id": "ozone_acid_rain", "label": "Ozônio", "depth": "basic", "order": 4},
            {"id": "indoor_pollution", "label": "Ar interno", "depth": "basic", "order": 5},
            {"id": "respiratory_thermal", "label": "Respiração", "depth": "basic", "order": 6},
            {"id": "sanitation_floods", "label": "Saneamento", "depth": "basic", "order": 7},
            {"id": "diseases", "label": "Doenças", "depth": "basic", "order": 8},
        ],
        "sections": [
            {"id": "route", "type": "study_route", "title": "Roteiro de estudo", "order": 1},
            {"id": "explain", "type": "explanations", "title": "Explicações", "order": 2},
            {"id": "summary", "type": "quick_summary", "title": "Resumo rápido", "order": 3},
        ],
        "components": ["concept_grid", "comparison_table", "bar_chart", "pie_chart", "line_chart", "quiz", "route_steps"],
        "exercise_plan": {
            "total": 16,
            "distribution": [
                {"type": "multiple_choice", "count": 16, "difficulty": "basic"},
            ],
        },
        "prerequisites": ["Noções de meio ambiente e saúde do 6º ano"],
        "common_errors": [
            {
                "topic_id": "ozone_acid_rain",
                "description": "Confundir ozônio da troposfera com o da estratosfera",
                "prevention_tip": "Solo = poluente; estratosfera = filtra UV",
            },
            {
                "topic_id": "indoor_pollution",
                "description": "Achar que chama amarela é sinal de boa combustão",
                "prevention_tip": "Chama azul = completa; amarela = CO perigoso",
            },
            {
                "topic_id": "diseases",
                "description": "Confundir agente causador com vetor",
                "prevention_tip": "Causador = microrganismo; vetor = quem transporta",
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
        "student": "Helena",
        "grade": "7º ano",
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
