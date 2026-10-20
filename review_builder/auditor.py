"""Auditoria de contratos, exercícios e HTML gerado."""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from review_builder.schema_validator import validate_contract
from review_builder.utils import load_json, save_json

EXTERNAL_URL_PATTERN = re.compile(
    r"https?://|//cdn\.|googleapis\.com|cloudflare|unpkg\.com|jsdelivr",
    re.IGNORECASE,
)
FETCH_PATTERN = re.compile(r"\bfetch\s*\(", re.IGNORECASE)
XHR_PATTERN = re.compile(r"XMLHttpRequest|\.open\s*\(\s*['\"]?(GET|POST)", re.IGNORECASE)
ABSOLUTE_PATH_PATTERN = re.compile(r'(?:src|href)\s*=\s*["\'](/[^"\']+)["\']')
REMOTE_SCRIPT_PATTERN = re.compile(
    r'<script[^>]+src\s*=\s*["\']https?://',
    re.IGNORECASE,
)


def _check(
    checks: list[dict[str, Any]],
    check_id: str,
    name: str,
    passed: bool,
    severity: str = "error",
    message: str = "",
    details: list[str] | None = None,
) -> None:
    checks.append({
        "id": check_id,
        "name": name,
        "severity": severity,
        "passed": passed,
        "message": message,
        "details": details or [],
    })


def validate_exercises_logic(exercises: dict[str, Any]) -> list[dict[str, Any]]:
    """Validações lógicas além do schema."""
    checks: list[dict[str, Any]] = []
    seen_ids: set[str] = set()

    for ex in exercises.get("exercises", []):
        ex_id = ex.get("id", "?")

        if ex_id in seen_ids:
            _check(checks, f"dup-{ex_id}", "IDs únicos", False, "error",
                   f"ID duplicado: {ex_id}")
        seen_ids.add(ex_id)

        if ex.get("type") == "map_capital":
            visual = ex.get("visual", {})
            if visual.get("type") != "brazil_map":
                _check(checks, f"map-visual-{ex_id}", "Visual de mapa", False, "error",
                       f"Exercício {ex_id}: map_capital exige visual brazil_map")
            elif not ex.get("explanation"):
                _check(checks, f"map-expl-{ex_id}", "Explicação presente", False, "error",
                       f"Exercício {ex_id} sem explanation")
            else:
                _check(checks, f"map-capital-{ex_id}", "Exercício map_capital válido", True, "info")

        if ex.get("type") == "written_language":
            ans = ex.get("correct_answer")
            if not isinstance(ans, str) or not ans.strip():
                _check(checks, f"written-ans-{ex_id}", "Resposta escrita", False, "error",
                       f"Exercício {ex_id}: correct_answer obrigatório")
            elif ex.get("input_mode") not in ("word", "sentence"):
                _check(checks, f"written-mode-{ex_id}", "Modo de entrada", False, "error",
                       f"Exercício {ex_id}: input_mode deve ser word ou sentence")
            else:
                _check(checks, f"written-{ex_id}", "Exercício written_language válido", True, "info")

        if ex.get("type") == "multiple_choice":
            opts = ex.get("options", [])
            ans = ex.get("correct_answer")
            if ans is None:
                _check(checks, f"no-ans-{ex_id}", "Gabarito presente", False, "error",
                       f"Exercício {ex_id} sem resposta correta")
            elif not isinstance(ans, int) or ans < 0 or ans >= len(opts):
                _check(checks, f"bad-ans-{ex_id}", "Índice de resposta válido", False, "error",
                       f"Exercício {ex_id}: índice {ans} inválido para {len(opts)} opções")
            else:
                _check(checks, f"ans-{ex_id}", "Gabarito presente", True, "info")

        for asset in ex.get("source_assets", []):
            if asset.startswith("/") or asset.startswith("http"):
                _check(checks, f"path-{ex_id}", "Caminhos relativos em assets", False, "error",
                       f"Asset com caminho absoluto/externo: {asset}")

    if not checks:
        _check(checks, "exercises-ok", "Exercícios válidos", True, "info")
    return checks


def audit_html(html_path: Path, assets_dir: Path | None = None) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    html = html_path.read_text(encoding="utf-8")

    if "<title>" not in html and "<title " not in html:
        _check(checks, "html-title", "Título HTML", False, "error", "HTML sem elemento title")
    else:
        _check(checks, "html-title", "Título HTML", True, "info")

    lang_match = re.search(r'<html[^>]+lang\s*=\s*["\']([^"\']+)["\']', html, re.I)
    if not lang_match:
        _check(checks, "html-lang", "Atributo lang", False, "error", "HTML sem atributo lang")
    else:
        _check(checks, "html-lang", "Atributo lang", True, "info")

    if EXTERNAL_URL_PATTERN.search(html):
        _check(checks, "no-external", "Sem URLs externas", False, "error",
               "Detectadas referências a recursos externos")
    else:
        _check(checks, "no-external", "Sem URLs externas", True, "info")

    if FETCH_PATTERN.search(html):
        _check(checks, "no-fetch", "Sem fetch()", False, "error", "Detectado uso de fetch()")
    else:
        _check(checks, "no-fetch", "Sem fetch()", True, "info")

    if XHR_PATTERN.search(html):
        _check(checks, "no-xhr", "Sem XHR", False, "error", "Detectado XMLHttpRequest")
    else:
        _check(checks, "no-xhr", "Sem XHR", True, "info")

    if REMOTE_SCRIPT_PATTERN.search(html):
        _check(checks, "no-remote-script", "Sem scripts remotos", False, "error",
               "Detectado script com src externo")
    else:
        _check(checks, "no-remote-script", "Sem scripts remotos", True, "info")

    for match in ABSOLUTE_PATH_PATTERN.finditer(html):
        _check(checks, "rel-paths", "Caminhos relativos", False, "error",
               f"Caminho absoluto detectado: {match.group(1)}")

    if assets_dir and assets_dir.exists():
        img_refs = re.findall(
            r'(?:src|href)\s*=\s*["\']([^"\']+/[^"\']+)["\']', html
        )
        for ref in set(img_refs):
            if ref.startswith("http") or ref.startswith("//"):
                continue
            rel = ref.split("/", 1)[-1] if "/" in ref else ref
            if rel in ("review.css", "review.js"):
                if not (assets_dir / rel).exists():
                    _check(checks, f"asset-{rel}", "Assets existentes", False, "error",
                           f"Asset ausente: {ref}")
                continue
            if not (assets_dir / rel).exists():
                _check(checks, f"asset-{rel}", "Assets existentes", False, "error",
                       f"Asset ausente: {ref}")

    if not any(c["id"] == "rel-paths" for c in checks):
        _check(checks, "rel-paths", "Caminhos relativos", True, "info")

    return checks


def run_audit(
    review_id: str,
    workspace_dir: Path,
    html_path: Path | None = None,
    *,
    assets_dir: Path | None = None,
) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    contracts = {
        "material-map": workspace_dir / "material-map.json",
        "review-blueprint": workspace_dir / "review-blueprint.json",
        "review-content": workspace_dir / "review-content.json",
        "exercises": workspace_dir / "exercises.json",
    }

    for name, path in contracts.items():
        if path.exists():
            data = load_json(path)
            errors = validate_contract(name, data)
            _check(
                checks, f"schema-{name}", f"Schema {name}",
                len(errors) == 0, "error" if errors else "info",
                "; ".join(errors) if errors else "Válido",
            )

    exercises_path = workspace_dir / "exercises.json"
    if exercises_path.exists():
        checks.extend(validate_exercises_logic(load_json(exercises_path)))

    if html_path and html_path.exists():
        resolved_assets = assets_dir if assets_dir is not None else html_path.parent / "assets"
        checks.extend(audit_html(html_path, resolved_assets))

    errors = [c for c in checks if not c["passed"] and c["severity"] == "error"]
    warnings = [c for c in checks if not c["passed"] and c["severity"] == "warning"]

    if errors:
        status = "failed"
    elif warnings:
        status = "passed_with_warnings"
    else:
        status = "passed"

    report: dict[str, Any] = {
        "version": "1.0",
        "review_id": review_id,
        "status": status,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "total_checks": len(checks),
            "passed": sum(1 for c in checks if c["passed"]),
            "warnings": len(warnings),
            "errors": len(errors),
        },
        "checks": checks,
        "blocking_issues": [c["message"] for c in errors if c["message"]],
    }

    schema_errors = validate_contract("audit-report", report)
    if schema_errors:
        report["status"] = "failed"
        report["blocking_issues"].extend(schema_errors)

    return report


def audit_and_save(
    review_id: str,
    workspace_dir: Path,
    html_path: Path | None = None,
    report_path: Path | None = None,
    *,
    assets_dir: Path | None = None,
) -> dict[str, Any]:
    report = run_audit(review_id, workspace_dir, html_path, assets_dir=assets_dir)
    out = report_path or workspace_dir / "audit-report.json"
    save_json(out, report)
    return report
