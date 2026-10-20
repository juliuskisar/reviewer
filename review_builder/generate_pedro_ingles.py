"""Gera revisão de Inglês PE para Pedro — salva em output/pedro-pe-ingles-2tri/."""

from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

from review_builder.auditor import audit_and_save
from review_builder.composer import compose_page
from review_builder.pedro_ingles_content import REVIEW_ID, build_content, build_exercises
from review_builder.schema_validator import validate_contract
from review_builder.utils import PROJECT_ROOT, load_yaml, save_json

FOLDER_NAME = "pedro-pe-ingles-2tri"
HTML_NAME = "index.html"
OUTPUT_DIR = PROJECT_ROOT / "output" / FOLDER_NAME
ASSETS_SRC = PROJECT_ROOT / "assets" / "pedro_pe_ingles_2_tri"
WORKSPACE = PROJECT_ROOT / "workspace" / REVIEW_ID


def build_material_map() -> dict:
    manifest = load_yaml(ASSETS_SRC / "manifest.yaml")
    assets = []
    for entry in manifest.get("assets", []):
        assets.append({
            "file": f"assets/pedro_pe_ingles_2_tri/{entry['file']}",
            "format": "jpg",
            "order": entry["order"],
            "subject": "english",
            "unit": entry.get("unit", "english_pe"),
            "importance": entry.get("importance", "medium"),
            "classification": {
                "discipline": "english",
                "topics": [entry.get("unit", "english_pe")],
                "confidence": "observed",
                "observations": [entry.get("notes", "Página do caderno de Inglês")],
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
            {"id": "simple_past_regular", "label": "Simple Past afirmativo", "source_assets": [], "confidence": "observed"},
            {"id": "spelling_rules", "label": "Ortografia -ed", "source_assets": [], "confidence": "observed"},
            {"id": "time_expressions", "label": "Expressões de tempo", "source_assets": [], "confidence": "observed"},
            {"id": "transport_travel", "label": "Transporte e viagem", "source_assets": [], "confidence": "observed"},
            {"id": "simple_past_negative", "label": "Simple Past negativo", "source_assets": [], "confidence": "observed"},
            {"id": "irregular_verbs", "label": "Verbos irregulares", "source_assets": [], "confidence": "observed"},
            {"id": "questions_short_answers", "label": "Perguntas Did", "source_assets": [], "confidence": "observed"},
            {"id": "could_couldnt", "label": "Could / Couldn't", "source_assets": [], "confidence": "observed"},
        ],
        "summary": {
            "total_assets": len(assets),
            "formats": ["jpg"],
            "disciplines_detected": ["english"],
            "unreadable_files": [],
            "duplicates": [],
        },
    }


def build_blueprint() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Inglês — PE 2º Trimestre",
        "discipline": "english",
        "student_grade": "6º ano",
        "objectives": [
            "Formar o Simple Past afirmativo de verbos regulares",
            "Aplicar regras de ortografia (-ed, -d, -ied)",
            "Usar didn't + base na forma negativa",
            "Reconhecer verbos irregulares frequentes",
            "Fazer perguntas com Did e respostas curtas",
            "Usar could/couldn't para habilidade no passado",
        ],
        "topics": [
            {"id": "simple_past_regular", "label": "Afirmativo", "depth": "basic", "order": 1},
            {"id": "spelling_rules", "label": "Ortografia", "depth": "basic", "order": 2},
            {"id": "time_expressions", "label": "Tempo", "depth": "basic", "order": 3},
            {"id": "transport_travel", "label": "Transporte", "depth": "basic", "order": 4},
            {"id": "simple_past_negative", "label": "Negativo", "depth": "basic", "order": 5},
            {"id": "irregular_verbs", "label": "Irregulares", "depth": "basic", "order": 6},
            {"id": "questions_short_answers", "label": "Perguntas", "depth": "basic", "order": 7},
            {"id": "could_couldnt", "label": "Could", "depth": "basic", "order": 8},
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
        "prerequisites": ["Noções básicas de vocabulário em inglês"],
        "common_errors": [
            {
                "topic_id": "simple_past_negative",
                "description": "Usar didn't + verbo no passado",
                "prevention_tip": "didn't go, não didn't went",
            },
            {
                "topic_id": "spelling_rules",
                "description": "Escrever tryed em vez de tried",
                "prevention_tip": "Consoante + y → -ied",
            },
            {
                "topic_id": "questions_short_answers",
                "description": "Repetir o verbo na resposta curta",
                "prevention_tip": "Yes, I did — sem o verbo principal",
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
        "exam": "PE — Inglês 2º trimestre",
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
