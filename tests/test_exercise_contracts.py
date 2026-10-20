"""Testes de contratos de exercícios."""

from __future__ import annotations

import copy

import pytest

from review_builder.auditor import validate_exercises_logic
from review_builder.schema_validator import validate_contract
from review_builder.utils import load_json

FIXTURES = __import__("pathlib").Path(__file__).parent / "fixtures" / "example-review"


def test_valid_exercises_fixture() -> None:
    data = load_json(FIXTURES / "exercises.json")
    assert validate_contract("exercises", data) == []
    checks = validate_exercises_logic(data)
    assert all(c["passed"] for c in checks if c["severity"] == "error")


def test_exercise_without_correct_answer_fails_schema() -> None:
    data = load_json(FIXTURES / "exercises.json")
    bad = copy.deepcopy(data)
    del bad["exercises"][0]["correct_answer"]
    errors = validate_contract("exercises", bad)
    assert len(errors) > 0


def test_exercise_with_invalid_answer_index() -> None:
    data = load_json(FIXTURES / "exercises.json")
    bad = copy.deepcopy(data)
    bad["exercises"][0]["correct_answer"] = 99
    checks = validate_exercises_logic(bad)
    assert any(not c["passed"] and "índice" in c["message"].lower() for c in checks)


def test_duplicate_exercise_ids() -> None:
    data = load_json(FIXTURES / "exercises.json")
    bad = copy.deepcopy(data)
    bad["exercises"].append(copy.deepcopy(bad["exercises"][0]))
    checks = validate_exercises_logic(bad)
    assert any("duplicado" in c["message"].lower() for c in checks)


def test_written_language_exercise_validates() -> None:
    data = {
        "version": "1.0",
        "review_id": "test-written",
        "exercises": [{
            "id": "wr-1",
            "type": "written_language",
            "topic": "grammar",
            "question": "Escreva o comparativo de old:",
            "correct_answer": "older",
            "input_mode": "word",
            "explanation": "Short adj. + -er.",
            "difficulty": "basic",
            "section": "escrita",
        }],
    }
    assert validate_contract("exercises", data) == []
    checks = validate_exercises_logic(data)
    assert all(c["passed"] for c in checks if c["severity"] == "error")


def test_absolute_asset_path_detected() -> None:
    data = load_json(FIXTURES / "exercises.json")
    bad = copy.deepcopy(data)
    bad["exercises"][0]["source_assets"] = ["/absolute/path.jpg"]
    checks = validate_exercises_logic(bad)
    assert any(not c["passed"] for c in checks)
