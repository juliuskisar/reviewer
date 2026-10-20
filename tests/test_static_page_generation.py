"""Testes de geração de página estática e auditoria."""

from __future__ import annotations

from pathlib import Path

import pytest

from review_builder.auditor import audit_and_save, run_audit
from review_builder.composer import compose_page
from review_builder.demo import run_demo
from review_builder.packager import PackagingError, package_review
from review_builder.utils import load_json, save_json

FIXTURES = Path(__file__).parent / "fixtures" / "example-review"
ASSETS = Path(__file__).parent.parent / "assets" / "example-review"
PROJECT = Path(__file__).parent.parent


def test_generated_page_has_title_and_lang(tmp_path: Path) -> None:
    out = tmp_path / "staging"
    compose_page(
        FIXTURES / "review-content.json",
        FIXTURES / "exercises.json",
        out,
        assets_root=ASSETS,
    )
    html = (out / "index.html").read_text(encoding="utf-8")
    assert "<title>" in html
    assert 'lang="pt-BR"' in html
    assert "https://" not in html
    assert "fetch(" not in html


def test_full_audit_passes_for_demo_fixtures(tmp_path: Path) -> None:
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    for name in ("material-map", "review-blueprint", "review-content", "exercises"):
        import shutil
        shutil.copy2(FIXTURES / f"{name}.json", workspace / f"{name}.json")

    staging = tmp_path / "staging"
    compose_page(
        workspace / "review-content.json",
        workspace / "exercises.json",
        staging,
        assets_root=ASSETS,
    )
    report = audit_and_save("example-review", workspace, staging / "index.html")
    assert report["status"] in ("passed", "passed_with_warnings")


def test_html_without_title_fails_audit(tmp_path: Path) -> None:
    html = tmp_path / "bad.html"
    html.write_text("<html><body></body></html>", encoding="utf-8")
    from review_builder.auditor import audit_html
    checks = audit_html(html)
    assert any(c["id"] == "html-title" and not c["passed"] for c in checks)


def test_html_without_lang_fails_audit(tmp_path: Path) -> None:
    html = tmp_path / "bad.html"
    html.write_text("<html><head><title>T</title></head><body></body></html>", encoding="utf-8")
    from review_builder.auditor import audit_html
    checks = audit_html(html)
    assert any(c["id"] == "html-lang" and not c["passed"] for c in checks)


def test_packaging_blocked_on_failed_audit(tmp_path: Path) -> None:
    report_path = tmp_path / "audit-report.json"
    save_json(report_path, {
        "version": "1.0",
        "review_id": "x",
        "status": "failed",
        "generated_at": "2026-06-15T12:00:00+00:00",
        "checks": [],
        "blocking_issues": ["test failure"],
    })
    source = tmp_path / "source"
    source.mkdir()
    (source / "index.html").write_text("<html></html>")
    with pytest.raises(PackagingError):
        package_review("x", source, tmp_path / "out", report_path)


def test_demo_generates_output() -> None:
    dest = run_demo()
    assert (dest / "index.html").exists()
    assert (dest / "assets" / "review.css").exists()
    report = load_json(PROJECT / "workspace" / "example-review" / "audit-report.json")
    assert report["status"] != "failed"
