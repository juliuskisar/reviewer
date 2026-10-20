"""Converte estruturas Python em literais JavaScript (objetos subjects/simulado da PI)."""

from __future__ import annotations

import json
from typing import Any


def _js_string(value: str) -> str:
    if "\n" in value or "`" in value or "${" in value:
        escaped = value.replace("\\", "\\\\").replace("`", "\\`").replace("${", "\\${")
        return f"`{escaped}`"
    return json.dumps(value, ensure_ascii=False)


def dict_to_js(value: Any, *, indent: int = 2, level: int = 0) -> str:
    pad = " " * (level * indent)
    inner = " " * ((level + 1) * indent)

    if isinstance(value, dict):
        if not value:
            return "{}"
        parts = []
        for key, item in value.items():
            key_repr = key if str(key).replace("-", "_").isidentifier() else json.dumps(key, ensure_ascii=False)
            parts.append(f"{inner}{key_repr}: {dict_to_js(item, indent=indent, level=level + 1)}")
        return "{\n" + ",\n".join(parts) + f"\n{pad}}}"

    if isinstance(value, list):
        if not value:
            return "[]"
        parts = [f"{inner}{dict_to_js(item, indent=indent, level=level + 1)}" for item in value]
        return "[\n" + ",\n".join(parts) + f"\n{pad}]"

    if isinstance(value, str):
        return _js_string(value)
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, (int, float)):
        return repr(value)
    raise TypeError(f"Tipo não suportado para export JS: {type(value)!r}")


def render_subjects_block(subjects: dict) -> str:
    return f"const subjects = {dict_to_js(subjects, indent=4, level=0)};"


def render_simulado_block(simulado: dict) -> str:
    return f"const simulado = {dict_to_js(simulado, indent=4, level=0)};"
