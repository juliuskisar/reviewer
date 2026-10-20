"""Testes de validação dos JSON Schemas."""

from __future__ import annotations

from pathlib import Path

import pytest

from review_builder.schema_validator import validate_contract
from review_builder.utils import load_json

FIXTURES = Path(__file__).parent / "fixtures" / "example-review"


@pytest.mark.parametrize("contract,file_name", [
    ("material-map", "material-map.json"),
    ("review-blueprint", "review-blueprint.json"),
    ("review-content", "review-content.json"),
    ("exercises", "exercises.json"),
])
def test_fixture_validates_against_schema(contract: str, file_name: str) -> None:
    data = load_json(FIXTURES / file_name)
    errors = validate_contract(contract, data)
    assert errors == [], f"Erros inesperados: {errors}"


def test_invalid_material_map_missing_required() -> None:
    errors = validate_contract("material-map", {"version": "1.0"})
    assert any("review_id" in e for e in errors)


def test_audit_report_schema_accepts_valid_report() -> None:
    report = {
        "version": "1.0",
        "review_id": "test",
        "status": "passed",
        "generated_at": "2026-06-15T12:00:00+00:00",
        "checks": [{
            "id": "c1",
            "name": "Test",
            "severity": "info",
            "passed": True,
        }],
    }
    assert validate_contract("audit-report", report) == []
