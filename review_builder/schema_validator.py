"""Validação de contratos JSON contra schemas."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import jsonschema
from jsonschema import Draft202012Validator

from review_builder.utils import SCHEMAS_DIR, load_json

SCHEMA_FILES = {
    "material-map": "material-map.schema.json",
    "review-blueprint": "review-blueprint.schema.json",
    "review-content": "review-content.schema.json",
    "exercises": "exercises.schema.json",
    "audit-report": "audit-report.schema.json",
}


def load_schema(name: str) -> dict[str, Any]:
    if name not in SCHEMA_FILES:
        raise ValueError(f"Schema desconhecido: {name}")
    return load_json(SCHEMAS_DIR / SCHEMA_FILES[name])


def validate_contract(name: str, data: dict[str, Any]) -> list[str]:
    """Valida dados contra schema. Retorna lista de erros (vazia = ok)."""
    schema = load_schema(name)
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
    return [f"{'.'.join(str(p) for p in err.path) or '<root>'}: {err.message}" for err in errors]


def validate_contract_file(name: str, path: Path) -> list[str]:
    data = load_json(path)
    return validate_contract(name, data)
