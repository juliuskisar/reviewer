"""Gera revisão de Português PE 3º trimestre para Benjamin — output/benjamin-pe-portugues-3tri/."""

from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

from review_builder.auditor import audit_and_save
from review_builder.benjamin_portugues_3tri_content import REVIEW_ID, build_content, build_exercises
from review_builder.composer import compose_page
from review_builder.schema_validator import validate_contract
from review_builder.utils import PROJECT_ROOT, load_yaml, save_json

FOLDER_NAME = "benjamin-pe-portugues-3tri"
HTML_NAME = "index.html"
OUTPUT_DIR = PROJECT_ROOT / "output" / FOLDER_NAME
ASSETS_SRC = PROJECT_ROOT / "assets" / "benjamin_pe_portugues_3_tri"
WORKSPACE = PROJECT_ROOT / "workspace" / REVIEW_ID

TOPICS = [
    {"id": "theater_viravez", "label": "Peça Viravez, o cortês"},
    {"id": "direct_indirect", "label": "Discurso direto e indireto"},
    {"id": "theater_staging", "label": "Texto teatral e encenação"},
    {"id": "tv_journalism", "label": "Telejornal e reportagem na TV"},
    {"id": "tarsila_pronouns", "label": "Tarsila do Amaral e pronomes"},
    {"id": "interview", "label": "Entrevista e roteiro"},
    {"id": "oral_resources", "label": "Recursos do texto oral"},
    {"id": "instructional_text", "label": "Texto e vídeo instrucional"},
]


def build_material_map() -> dict:
    manifest = load_yaml(ASSETS_SRC / "manifest.yaml")
    assets = []
    for entry in manifest.get("assets", []):
        assets.append({
            "file": f"assets/benjamin_pe_portugues_3_tri/{entry['file']}",
            "format": "jpg",
            "order": entry["order"],
            "subject": "portuguese",
            "unit": entry.get("unit", "portuguese_pe"),
            "importance": entry.get("importance", "medium"),
            "classification": {
                "discipline": "portuguese",
                "topics": [entry.get("unit", "portuguese_pe")],
                "confidence": "observed",
                "observations": [entry.get("notes", "Página do caderno de Português")],
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
            "disciplines_detected": ["portuguese"],
            "unreadable_files": [],
            "duplicates": [],
        },
    }


def build_blueprint() -> dict:
    return {
        "version": "1.0",
        "review_id": REVIEW_ID,
        "title": "Revisão de Português — PE 3º Trimestre",
        "discipline": "portuguese",
        "student_grade": "4º ano",
        "objectives": [
            "Interpretar texto teatral e transformar trechos em narrativa com discurso direto",
            "Analisar telejornal e reportagem sobre Tarsila do Amaral",
            "Usar pronomes para evitar repetição e revisar pretérito de verbos em -car",
            "Planejar e avaliar entrevista e vídeo tutorial instrucional",
        ],
        "topics": [{**t, "depth": "basic", "order": i + 1} for i, t in enumerate(TOPICS)],
        "sections": [
            {"id": "route", "type": "study_route", "title": "Roteiro de estudo", "order": 1},
            {"id": "explain", "type": "explanations", "title": "Explicações", "order": 2},
            {"id": "summary", "type": "quick_summary", "title": "Resumo rápido", "order": 3},
            {"id": "game_speech", "type": "study_game", "title": "Jogo: Fala certa", "order": 4},
            {"id": "game_pronoun", "type": "study_game", "title": "Jogo: Detetive do pronome", "order": 5},
        ],
        "components": ["concept_grid", "comparison_table", "quiz", "route_steps", "study_game"],
        "exercise_plan": {
            "total": 16,
            "distribution": [{"type": "multiple_choice", "count": 16, "difficulty": "basic"}],
        },
        "prerequisites": ["Leitura fluente de textos curtos"],
        "common_errors": [
            {
                "topic_id": "direct_indirect",
                "description": "Esquecer travessão e dois-pontos no discurso direto",
                "prevention_tip": "Direto = fala exata com — · indireto = narrador resume sem travessão",
            },
            {
                "topic_id": "tarsila_pronouns",
                "description": "Confundir pronome pessoal com possessivo",
                "prevention_tip": "Possessivo indica dono (meu, sua) · pessoal substitui nome (ele, eles)",
            },
            {
                "topic_id": "instructional_text",
                "description": "Misturar ordem de etapas no texto instrucional",
                "prevention_tip": "Tutorial = sequência planejada — objetivo, materiais, passos, conclusão",
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
        "exam": "PE — Português 3º trimestre",
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
