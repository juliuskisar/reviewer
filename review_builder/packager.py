"""Empacotamento da revisão final após auditoria."""

from __future__ import annotations

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from review_builder.utils import load_json, save_json


class PackagingError(Exception):
    """Erro que impede empacotamento (ex.: auditoria falhou)."""


def package_review(
    review_id: str,
    source_dir: Path,
    output_dir: Path,
    audit_report_path: Path,
    *,
    metadata: dict[str, Any] | None = None,
) -> Path:
    """
    Copia revisão para output/ após verificar auditoria.
    Falha se status == failed.
    """
    report = load_json(audit_report_path)
    if report.get("status") == "failed":
        blocking = report.get("blocking_issues", [])
        raise PackagingError(
            f"Auditoria falhou — empacotamento bloqueado. Issues: {blocking}"
        )

    dest = output_dir / review_id
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)

    index = source_dir / "index.html"
    if not index.exists():
        raise PackagingError("index.html não encontrado na origem")

    shutil.copy2(index, dest / "index.html")

    assets_src = source_dir / "assets"
    if assets_src.exists():
        shutil.copytree(assets_src, dest / "assets")

    gen_meta = {
        "review_id": review_id,
        "packaged_at": datetime.now(timezone.utc).isoformat(),
        "audit_status": report.get("status"),
        "generator": "review_builder",
        **(metadata or {}),
    }
    save_json(dest / "generation-metadata.json", gen_meta)

    return dest
