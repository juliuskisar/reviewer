"""Testes de referências a assets e caminhos."""

from __future__ import annotations

from pathlib import Path

import pytest

from review_builder.auditor import audit_html
from review_builder.composer import compose_page

FIXTURES = Path(__file__).parent / "fixtures" / "example-review"
ASSETS = Path(__file__).parent.parent / "assets" / "example-review"


def test_compose_copies_referenced_assets(tmp_path: Path) -> None:
    out = tmp_path / "page"
    compose_page(
        FIXTURES / "review-content.json",
        FIXTURES / "exercises.json",
        out,
        assets_root=ASSETS,
    )
    assert (out / "index.html").exists()
    assert (out / "assets" / "review.css").exists()
    assert (out / "assets" / "review.js").exists()


def test_missing_asset_detected_in_audit(tmp_path: Path) -> None:
    html = tmp_path / "index.html"
    html.write_text(
        '<html lang="pt-BR"><head><title>T</title></head>'
        '<body><img src="assets/missing.svg" alt="x"></body></html>',
        encoding="utf-8",
    )
    assets = tmp_path / "assets"
    assets.mkdir()
    checks = audit_html(html, assets)
    assert any(not c["passed"] and "ausente" in c["message"].lower() for c in checks)


def test_external_url_detected() -> None:
    checks = audit_html(Path(__file__))  # won't have html structure
    # Use inline html string via temp file
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write('<html lang="pt"><head><title>T</title></head>'
                '<body><script src="https://cdn.example.com/lib.js"></script></body></html>')
        path = Path(f.name)
    try:
        checks = audit_html(path)
        assert any(not c["passed"] and c["id"] == "no-external" for c in checks)
    finally:
        path.unlink()


def test_fetch_detected() -> None:
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write('<html lang="pt"><head><title>T</title></head>'
                '<body><script>fetch("/api")</script></body></html>')
        path = Path(f.name)
    try:
        checks = audit_html(path)
        assert any(not c["passed"] and c["id"] == "no-fetch" for c in checks)
    finally:
        path.unlink()
