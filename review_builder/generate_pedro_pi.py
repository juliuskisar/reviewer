"""Gera revisão PI multidisciplinar do Pedro — output/pedro-pi-6ano/index.html."""

from __future__ import annotations

import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

from review_builder.js_export import render_simulado_block, render_subjects_block
from review_builder.pedro_pi_content import (
    GRADE,
    PAGE_TITLE,
    REVIEW_ID,
    STUDENT_NAME,
    build_simulado,
    build_subjects,
)
from review_builder.utils import PROJECT_ROOT, save_json

FOLDER_NAME = "pedro-pi-6ano"
OUTPUT_DIR = PROJECT_ROOT / "output" / FOLDER_NAME
TEMPLATE = PROJECT_ROOT / "PI_review.html"
ASSETS_SRC = PROJECT_ROOT / "assets" / "pedro_pi_6_ano"


def _replace_js_block(html: str, marker: str, end_marker: str, new_block: str) -> str:
    pattern = rf"({re.escape(marker)})(.*?)({re.escape(end_marker)})"
    match = re.search(pattern, html, flags=re.DOTALL)
    if not match:
        raise RuntimeError(f"Marcador não encontrado: {marker!r}")
    return html[: match.start()] + new_block + "\n\n" + html[match.end() :]


def compose_html() -> str:
    html = TEMPLATE.read_text(encoding="utf-8")
    html = html.replace(
        "<title>Revisão Multidisciplinar — Pedro Katsumi (6º Ano)</title>",
        f"<title>{PAGE_TITLE}</title>",
    )
    html = html.replace(
        "<h1>Revisão Multidisciplinar — Pedro Katsumi (6º Ano)</h1>",
        f"<h1>{PAGE_TITLE}</h1>",
    )

    subjects_block = render_subjects_block(build_subjects())
    simulado_block = render_simulado_block(build_simulado())

    section_comment = """
    /* Modelo padrão de seções (na ordem em que devem aparecer).
       Para mudar nomes ou ordem, basta editar este array.
       A seção "conteudo" agrupa Resumo + Explicação geral, com switch
       (Resumo aparece por padrão). */"""

    simulado_header_comment = """
    /* =========================================================
       SIMULADO DA PI — Projeto Água e Memória (24 questões)
       ========================================================= */"""

    progress_comment = """
    /* Estado em memória para acompanhar o progresso por disciplina. */"""

    html = _replace_js_block(
        html,
        "const subjects = {",
        "    const SECTION_TEMPLATE = [",
        subjects_block + "\n\n" + section_comment + "\n    const SECTION_TEMPLATE = [",
    )

    html = html.replace(
        """    /* =========================================================
       SIMULADO DA PI
       Texto-base sobre a Copa do Mundo 2026 + 24 questões
       (3 por disciplina, todas múltipla escolha).

       A ordem das disciplinas em "questions" será respeitada
       no agrupamento exibido na tela.
       ========================================================= */
    const simulado = {""",
        simulado_header_comment + "\n    const simulado = {",
        1,
    )

    html = _replace_js_block(
        html,
        "const simulado = {",
        "    const progressState = {};",
        simulado_block + "\n\n" + progress_comment + "\n    const progressState = {};",
    )
    return html


def run() -> Path:
    if not TEMPLATE.exists():
        raise FileNotFoundError(f"Template não encontrado: {TEMPLATE}")
    if not ASSETS_SRC.exists():
        raise FileNotFoundError(f"Assets não encontrados: {ASSETS_SRC}")

    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    html_path = OUTPUT_DIR / "index.html"
    html_path.write_text(compose_html(), encoding="utf-8")

    subjects = build_subjects()
    simulado = build_simulado()
    exercise_total = sum(len(s["exercises"]) for s in subjects.values())

    save_json(
        OUTPUT_DIR / "generation-metadata.json",
        {
            "review_id": REVIEW_ID,
            "student": STUDENT_NAME,
            "grade": GRADE,
            "exam": "PI — Prova Integrada (2º trimestre)",
            "format": "monolith_html",
            "template": "PI_review.html",
            "disciplines": list(subjects.keys()),
            "exercises_per_discipline": {k: len(v["exercises"]) for k, v in subjects.items()},
            "total_discipline_exercises": exercise_total,
            "simulado_questions": len(simulado["questions"]),
            "output_path": f"output/{FOLDER_NAME}/",
            "generated_at": datetime.now(timezone.utc).isoformat(),
        },
    )

    return html_path


def main() -> None:
    path = run()
    print(f"Revisão PI gerada: {path}")
    print(f"Pasta: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
