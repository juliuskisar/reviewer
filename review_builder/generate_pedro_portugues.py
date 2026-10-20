"""Gera revisão de Português PE para Pedro — salva em output/pedro-pe-portugues-2tri/."""

from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

from review_builder.auditor import audit_and_save
from review_builder.composer import compose_page
from review_builder.pedro_portugues_content import REVIEW_ID, build_content, build_exercises
from review_builder.schema_validator import validate_contract
from review_builder.utils import PROJECT_ROOT, load_yaml, save_json

FOLDER_NAME = "pedro-pe-portugues-2tri"
HTML_NAME = "index.html"
OUTPUT_DIR = PROJECT_ROOT / "output" / FOLDER_NAME
ASSETS_SRC = PROJECT_ROOT / "assets" / "pedro_pe_portugues_2_tri"
WORKSPACE = PROJECT_ROOT / "workspace" / REVIEW_ID


def build_material_map() -> dict:
    manifest = load_yaml(ASSETS_SRC / "manifest.yaml")
    assets = []
    for entry in manifest.get("assets", []):
        assets.append({
            "file": f"assets/pedro_pe_portugues_2_tri/{entry['file']}",
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
        "topics": [
            {"id": "text_genres", "label": "Gêneros textuais", "source_assets": [], "confidence": "observed"},
            {"id": "legal_texts", "label": "Textos legais", "source_assets": [], "confidence": "observed"},
            {"id": "netiquette", "label": "Netiqueta", "source_assets": [], "confidence": "observed"},
            {"id": "verbal_phrase", "label": "Sintagma verbal", "source_assets": [], "confidence": "observed"},
            {"id": "verbs_moods", "label": "Modos verbais", "source_assets": [], "confidence": "observed"},
            {"id": "adverbs", "label": "Advérbios", "source_assets": [], "confidence": "observed"},
            {"id": "humor", "label": "Humor", "source_assets": [], "confidence": "observed"},
            {"id": "speech", "label": "Discurso direto/indireto", "source_assets": [], "confidence": "observed"},
        ],
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
        "title": "Revisão de Português — PE 2º Trimestre",
        "discipline": "portuguese",
        "student_grade": "6º ano",
        "objectives": [
            "Diferenciar textos normativos e instrucionais",
            "Analisar estrutura de leis e regras de netiqueta",
            "Identificar sintagma verbal, modos e advérbios",
            "Interpretar humor e converter discurso direto em indireto",
        ],
        "topics": [
            {"id": "text_genres", "label": "Gêneros", "depth": "basic", "order": 1},
            {"id": "legal_texts", "label": "Textos legais", "depth": "basic", "order": 2},
            {"id": "netiquette", "label": "Netiqueta", "depth": "basic", "order": 3},
            {"id": "verbal_phrase", "label": "Sintagma verbal", "depth": "basic", "order": 4},
            {"id": "verbs_moods", "label": "Modos verbais", "depth": "basic", "order": 5},
            {"id": "adverbs", "label": "Advérbios", "depth": "basic", "order": 6},
            {"id": "humor", "label": "Humor", "depth": "basic", "order": 7},
            {"id": "speech", "label": "Discurso", "depth": "basic", "order": 8},
        ],
        "sections": [
            {"id": "route", "type": "study_route", "title": "Roteiro de estudo", "order": 1},
            {"id": "explain", "type": "explanations", "title": "Explicações", "order": 2},
            {"id": "summary", "type": "quick_summary", "title": "Resumo rápido", "order": 3},
            {"id": "game_genre", "type": "study_game", "title": "Jogo: Gênero certo", "order": 4},
            {"id": "game_humor", "type": "study_game", "title": "Jogo: Detetive do humor", "order": 5},
        ],
        "components": ["concept_grid", "comparison_table", "quiz", "route_steps", "study_game"],
        "exercise_plan": {
            "total": 16,
            "distribution": [
                {"type": "multiple_choice", "count": 16, "difficulty": "basic"},
            ],
        },
        "prerequisites": ["Leitura de textos curtos e noções básicas de gramática"],
        "common_errors": [
            {
                "topic_id": "text_genres",
                "description": "Confundir receita culinária com texto normativo",
                "prevention_tip": "Receita ensina a fazer — é instrucional",
            },
            {
                "topic_id": "verbs_moods",
                "description": "Achar que «evite» está no indicativo",
                "prevention_tip": "Imperativo dá conselho ou ordem",
            },
            {
                "topic_id": "speech",
                "description": "Manter travessão no discurso indireto",
                "prevention_tip": "Use «perguntou se/que» e ajuste o tempo verbal",
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
        "exam": "PE — Português 2º trimestre",
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
