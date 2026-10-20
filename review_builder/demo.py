"""Pipeline de demonstração com dados de exemplo."""

from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path

from review_builder.auditor import audit_and_save
from review_builder.composer import compose_page
from review_builder.config_loader import load_generation_context
from review_builder.packager import package_review
from review_builder.utils import PROJECT_ROOT, load_json, load_yaml, save_json

FIXTURES_DIR = PROJECT_ROOT / "tests" / "fixtures" / "example-review"
ASSETS_DIR = PROJECT_ROOT / "assets" / "example-review"
WORKSPACE_DIR = PROJECT_ROOT / "workspace" / "example-review"
OUTPUT_DIR = PROJECT_ROOT / "output"


def _ensure_material_map(review_id: str) -> dict:
    """Gera material-map.json a partir do manifest e assets (simula inspect-assets)."""
    manifest = load_yaml(ASSETS_DIR / "manifest.yaml")
    assets = []
    for entry in manifest.get("assets", []):
        fpath = ASSETS_DIR / entry["file"]
        asset_entry: dict = {
            "file": f"assets/example-review/{entry['file']}",
            "format": fpath.suffix.lstrip("."),
            "order": entry.get("order", 1),
            "importance": entry.get("importance", "medium"),
            "classification": {
                "discipline": "mathematics",
                "topics": [entry.get("unit", "geometric_solids")],
                "confidence": "observed" if entry.get("unit") else "inferred",
                "observations": [entry["notes"]] if entry.get("notes") else [],
                "inferences": [],
                "uncertainties": [],
            },
        }
        if entry.get("subject"):
            asset_entry["subject"] = entry["subject"]
        if entry.get("unit"):
            asset_entry["unit"] = entry["unit"]
        if entry.get("notes"):
            asset_entry["notes"] = entry["notes"]
        assets.append(asset_entry)

    return {
        "version": "1.0",
        "review_id": review_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "manifest_present": True,
        "assets": assets,
        "topics": [{
            "id": "geometric_solids",
            "label": "Sólidos Geométricos",
            "source_assets": [a["file"] for a in assets],
            "confidence": "observed",
        }],
        "summary": {
            "total_assets": len(assets),
            "formats": list({a["format"] for a in assets}),
            "disciplines_detected": ["mathematics"],
            "unreadable_files": [],
            "duplicates": [],
        },
    }


def run_demo() -> Path:
    review_id = "example-review"
    WORKSPACE_DIR.mkdir(parents=True, exist_ok=True)

    manifest = load_yaml(ASSETS_DIR / "manifest.yaml")
    context = load_generation_context(manifest)

    material_map = _ensure_material_map(review_id)
    save_json(WORKSPACE_DIR / "material-map.json", material_map)

    for name in ("review-blueprint", "review-content", "exercises"):
        src = FIXTURES_DIR / f"{name}.json"
        shutil.copy2(src, WORKSPACE_DIR / f"{name}.json")

    staging = WORKSPACE_DIR / "staging"
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir()

    compose_page(
        WORKSPACE_DIR / "review-content.json",
        WORKSPACE_DIR / "exercises.json",
        staging,
        assets_root=ASSETS_DIR,
    )

    report = audit_and_save(review_id, WORKSPACE_DIR, staging / "index.html")

    if report["status"] == "failed":
        raise RuntimeError(f"Auditoria falhou: {report.get('blocking_issues')}")

    dest = package_review(
        review_id,
        staging,
        OUTPUT_DIR,
        WORKSPACE_DIR / "audit-report.json",
        metadata={
            "title": manifest["review"]["title"],
            "student_grade": context.get("student", {}).get("grade"),
        },
    )
    return dest


def main() -> None:
    dest = run_demo()
    print(f"Demonstração gerada em: {dest / 'index.html'}")
