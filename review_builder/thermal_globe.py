"""Geometria do globo de zonas térmicas (SVG offline) — Módulo 10, Geografia 4º ano.

Globo visto de frente (projeção ortográfica): y = cy - r·sin(lat).
Bandas = zonas térmicas delimitadas por trópicos e círculos polares.
"""

from __future__ import annotations

import math
from functools import lru_cache
from typing import Any

CX, CY, R = 210.0, 210.0, 190.0
VIEW_W, VIEW_H = 640, 420

PARALLELS = [
    {"id": "arctic", "label": "Círculo Polar Ártico", "lat": 66.56, "color": "#64748b"},
    {"id": "cancer", "label": "Trópico de Câncer", "lat": 23.44, "color": "#ea580c"},
    {"id": "equator", "label": "Linha do Equador", "lat": 0.0, "color": "#dc2626"},
    {"id": "capricorn", "label": "Trópico de Capricórnio", "lat": -23.44, "color": "#ea580c"},
    {"id": "antarctic", "label": "Círculo Polar Antártico", "lat": -66.56, "color": "#64748b"},
]

ZONES = {
    "polar": {
        "label": "Zona polar (glacial)",
        "color": "#9ca3af",
        "paint_label": "Cinza",
        "rays": "Raios solares muito inclinados — e por dois meses do ano nem chegam.",
        "temperature": "Região mais fria do planeta.",
    },
    "temperate": {
        "label": "Zona temperada",
        "color": "#facc15",
        "paint_label": "Amarelo",
        "rays": "Raios solares inclinados — luz e calor se espalham por uma área maior.",
        "temperature": "Temperaturas médias; estações bem marcadas.",
    },
    "intertropical": {
        "label": "Zona intertropical (tropical)",
        "color": "#ef4444",
        "paint_label": "Vermelho",
        "rays": "Raios solares perpendiculares — luz concentrada em pouca área.",
        "temperature": "Região mais quente e iluminada do planeta.",
    },
}

BANDS = [
    {"id": "polar_north", "zone": "polar", "label": "Zona polar Norte", "top": "north_pole", "bottom": "arctic"},
    {"id": "temperate_north", "zone": "temperate", "label": "Zona temperada Norte", "top": "arctic", "bottom": "cancer"},
    {"id": "intertropical", "zone": "intertropical", "label": "Zona intertropical", "top": "cancer", "bottom": "capricorn"},
    {"id": "temperate_south", "zone": "temperate", "label": "Zona temperada Sul", "top": "capricorn", "bottom": "antarctic"},
    {"id": "polar_south", "zone": "polar", "label": "Zona polar Sul", "top": "antarctic", "bottom": "south_pole"},
]


def _lat_to_y(lat: float) -> float:
    return round(CY - R * math.sin(math.radians(lat)), 2)


def _half_width(y: float) -> float:
    dy = y - CY
    return round(math.sqrt(max(R * R - dy * dy, 0.0)), 2)


@lru_cache(maxsize=1)
def get_globe_data() -> dict[str, Any]:
    y_by_id = {"north_pole": CY - R, "south_pole": CY + R}
    parallels = []
    for p in PARALLELS:
        y = _lat_to_y(p["lat"])
        hw = _half_width(y)
        y_by_id[p["id"]] = y
        parallels.append({
            **p,
            "y": y,
            "x1": round(CX - hw, 2),
            "x2": round(CX + hw, 2),
            "label_x": round(CX + R + 18, 2),
        })

    bands = []
    for b in BANDS:
        top = y_by_id[b["top"]]
        bottom = y_by_id[b["bottom"]]
        bands.append({
            **b,
            "y": round(top, 2),
            "height": round(bottom - top, 2),
            "mid_y": round((top + bottom) / 2, 2),
        })

    return {
        "viewBox": f"0 0 {VIEW_W} {VIEW_H}",
        "cx": CX,
        "cy": CY,
        "r": R,
        "parallels": parallels,
        "bands": bands,
        "zones": [{"id": k, **v} for k, v in ZONES.items()],
    }
