"""Gera revisão de Espanhol PE 3º trimestre para Pedro — output/pedro-pe-espanhol-3tri/."""

from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

from review_builder.auditor import audit_and_save
from review_builder.composer import compose_page
from review_builder.pedro_espanhol_3tri_content import REVIEW_ID, build_content, build_exercises
from review_builder.schema_validator import validate_contract
from review_builder.utils import PROJECT_ROOT, load_yaml, save_json

FOLDER_NAME = "pedro-pe-espanhol-3tri"
HTML_NAME = "index.html"
OUTPUT_DIR = PROJECT_ROOT / "output" / FOLDER_NAME
ASSETS_SRC = PROJECT_ROOT / "assets" / "pedro_pe_espanhol_3_tri"
WORKSPACE = PROJECT_ROOT / "workspace" / REVIEW_ID

TOPICS = [
    {"id": "alimentos_habitos", "label": "Alimentos y hábitos"},
    {"id": "verbo_gustar", "label": "Verbo gustar"},
    {"id": "frecuencia_adverbios", "label": "Frecuencia"},
    {"id": "medidas_restaurante", "label": "Medidas y restaurante"},
    {"id": "verbos_regulares", "label": "Verbos regulares"},
    {"id": "lectura_hambre", "label": "Lecturas"},
    {"id": "animales_muy_mucho", "label": "Animales, muy/mucho"},
    {"id": "numeros_hora", "label": "Números y hora"},
]


def build_material_map() -> dict:
    manifest = load_yaml(ASSETS_SRC / "manifest.yaml")
    assets = []
    for entry in manifest.get("assets", []):
        assets.append({
            "file": f"assets/pedro_pe_espanhol_3_tri/{entry['file']}",
            "format": "jpg",
            "order": entry["order"],
            "subject": "spanish",
            "unit": entry.get("unit", "spanish_pe"),
            "importance": entry.get("importance", "medium"),
            "classification": {
                "discipline": "spanish",
                "topics": [entry.get("unit", "spanish_pe")],
                "confidence": "observed",
                "observations": [entry.get("notes", "Página do caderno de Espanhol")],
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
            "disciplines_detected": ["spanish"],
            "unreadable_files": [],
            "duplicates": [],
        },
    }


def build_blueprint() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Espanhol — PE 3º Trimestre",
        "discipline": "spanish",
        "student_grade": "6º ano",
        "objectives": [
            "Usar vocabulario de alimentos y hábitos alimentarios",
            "Emplear gustar con me/te/le y gusta/gustan",
            "Usar adverbios de frecuencia y expresiones de medida",
            "Conjugar verbos regulares en presente de indicativo",
            "Diferenciar muy y mucho; saber, conocer y poner",
            "Leer números cardinales y decir la hora",
        ],
        "topics": [
            {"id": t["id"], "label": t["label"], "depth": "basic", "order": i + 1}
            for i, t in enumerate(TOPICS)
        ],
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
        "prerequisites": ["Noções básicas de vocabulário em espanhol"],
        "common_errors": [
            {
                "topic_id": "verbo_gustar",
                "description": "Conjugar gustar como yo gusto",
                "prevention_tip": "Me gusta/gustan — concuerda con la cosa",
            },
            {
                "topic_id": "animales_muy_mucho",
                "description": "Muy + sustantivo",
                "prevention_tip": "Mucho/mucha/muchos/muchas + sustantivo",
            },
            {
                "topic_id": "numeros_hora",
                "description": "Son las una",
                "prevention_tip": "Es la una · Son las dos…",
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
        "exam": "PE — Espanhol 3º trimestre",
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
