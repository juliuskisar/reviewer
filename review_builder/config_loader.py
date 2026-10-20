"""Carregamento e combinação de configurações YAML."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from review_builder.utils import PROJECT_ROOT, deep_merge, load_yaml

# Precedência (menor índice = menor prioridade):
# student-default < student < discipline < exam < execution overrides
PRECEDENCE = [
    "student-default",
    "student",
    "discipline",
    "exam",
    "execution",
]


def load_config(path: Path | str) -> dict[str, Any]:
    p = Path(path)
    if not p.is_absolute():
        p = PROJECT_ROOT / p
    return load_yaml(p)


def merge_configs(
    student: dict[str, Any],
    exam: dict[str, Any],
    discipline: dict[str, Any],
    execution: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Combina configurações respeitando precedência documentada."""
    default_student = load_config("configs/students/student-default.yaml")
    merged = deep_merge(default_student, student)
    merged = deep_merge(merged, discipline)
    merged = deep_merge(merged, exam)
    if execution:
        merged = deep_merge(merged, execution)
    merged["_precedence"] = PRECEDENCE
    return merged


def load_generation_context(manifest: dict[str, Any]) -> dict[str, Any]:
    """Carrega contexto completo a partir de um manifest.yaml."""
    student = load_config(manifest["student"]["config"])
    exam = load_config(manifest["exam"]["config"])
    disciplines = [
        load_config(d["config"]) for d in manifest.get("disciplines", [])
    ]
    discipline = disciplines[0] if disciplines else {}
    return merge_configs(student, exam, discipline)
