"""Composição de páginas HTML estáticas a partir de contratos estruturados."""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape

from review_builder.brazil_map import get_map_data
from review_builder.thermal_globe import get_globe_data
from review_builder.utils import TEMPLATES_DIR, load_json


def _create_jinja_env() -> Environment:
    return Environment(
        loader=FileSystemLoader(TEMPLATES_DIR),
        autoescape=select_autoescape(["html", "xml"]),
    )


def _collect_rendered_asset_refs(content: dict[str, Any]) -> set[str]:
    """Referências a arquivos exibidos no HTML (blocos image). Metadados em sources/source_assets não entram."""
    refs: set[str] = set()
    for section in content.get("sections", []):
        for block in section.get("blocks", []):
            if block.get("type") != "image":
                continue
            file_ref = block.get("content", {}).get("file")
            if file_ref:
                refs.add(file_ref)
            if img := block.get("content", {}).get("image"):
                refs.add(img)
    return refs


def compose_page(
    content_path: Path,
    exercises_path: Path,
    output_dir: Path,
    *,
    assets_root: Path | None = None,
    assets_href_prefix: str = "assets",
    html_filename: str = "index.html",
    assets_out_dir: Path | None = None,
) -> Path:
    """
    Gera index.html e copia assets estáticos.
    Não altera conteúdo pedagógico — apenas monta apresentação.
    """
    content = load_json(content_path)
    exercises_data = load_json(exercises_path)
    env = _create_jinja_env()
    template = env.get_template("review-page.html")

    review_data = {
        "review_id": content.get("review_id"),
        "exercises": exercises_data.get("exercises", []),
    }

    asset_base = f"{assets_href_prefix.rstrip('/')}/" if assets_href_prefix else ""

    all_exercises = exercises_data.get("exercises", [])
    regular_exercises = [
        e for e in all_exercises
        if e.get("section", "exercises") in ("exercises", "final_quiz")
    ]
    challenge_exercises = [e for e in all_exercises if e.get("section") == "desafios"]
    written_exercises = [e for e in all_exercises if e.get("section") == "escrita"]

    html = template.render(
        title=content["title"],
        subtitle=content.get("subtitle", ""),
        language=content.get("language", "pt-BR"),
        discipline=content.get("discipline", ""),
        grade=content.get("grade", ""),
        metadata=content.get("metadata", {}),
        sections=content.get("sections", []),
        exercises=regular_exercises,
        challenge_exercises=challenge_exercises,
        written_exercises=written_exercises,
        parent_support=content.get("parent_support"),
        parent_answers=exercises_data.get("exercises", []),
        review_data_json=json.dumps(review_data, ensure_ascii=False),
        map_data_json=json.dumps(get_map_data(), ensure_ascii=False),
        globe_data_json=json.dumps(get_globe_data(), ensure_ascii=False),
        assets_prefix=assets_href_prefix,
        asset_base=asset_base,
        map_data=get_map_data(),
        globe_data=get_globe_data(),
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    assets_out = assets_out_dir or (output_dir / "assets")
    assets_out.mkdir(parents=True, exist_ok=True)

    static_src = TEMPLATES_DIR / "static"
    for fname in ("review.css", "review.js"):
        shutil.copy2(static_src / fname, assets_out / fname)

    if assets_root:
        refs = _collect_rendered_asset_refs(content)
        for ref in refs:
            src = Path(ref)
            if not src.is_absolute():
                src = assets_root.parent / ref if ref.startswith("assets/") else assets_root / src.name
                if not src.exists():
                    src = assets_root / Path(ref).name
            if src.exists() and src.is_file():
                shutil.copy2(src, assets_out / src.name)

    html_path = output_dir / html_filename
    html_path.write_text(html, encoding="utf-8")
    return html_path
