"""Dados do mapa político interativo do Brasil (SVG paths offline)."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Any

from review_builder.utils import load_json

_MAP_PATH = Path(__file__).parent / "map_data" / "brazil_states.json"


@lru_cache(maxsize=1)
def get_map_data() -> dict[str, Any]:
    return load_json(_MAP_PATH)
