"""Gera brazil_states.json com paths SVG, fusões históricas e centróides.

Uso: python -m review_builder.map_data.build_brazil_states
"""

from __future__ import annotations

import json
from pathlib import Path

from shapely.geometry import shape
from shapely.ops import unary_union

DIR = Path(__file__).parent
GEO = DIR / "br_states.geojson"
OUT = DIR / "brazil_states.json"

CAPITALS: dict[str, tuple[str, str, str]] = {
    "AC": ("Acre", "Rio Branco", "Norte"),
    "AL": ("Alagoas", "Maceió", "Nordeste"),
    "AM": ("Amazonas", "Manaus", "Norte"),
    "AP": ("Amapá", "Macapá", "Norte"),
    "BA": ("Bahia", "Salvador", "Nordeste"),
    "CE": ("Ceará", "Fortaleza", "Nordeste"),
    "DF": ("Distrito Federal", "Brasília", "Centro-Oeste"),
    "ES": ("Espírito Santo", "Vitória", "Sudeste"),
    "GO": ("Goiás", "Goiânia", "Centro-Oeste"),
    "MA": ("Maranhão", "São Luís", "Nordeste"),
    "MG": ("Minas Gerais", "Belo Horizonte", "Sudeste"),
    "MS": ("Mato Grosso do Sul", "Campo Grande", "Centro-Oeste"),
    "MT": ("Mato Grosso", "Cuiabá", "Centro-Oeste"),
    "PA": ("Pará", "Belém", "Norte"),
    "PB": ("Paraíba", "João Pessoa", "Nordeste"),
    "PE": ("Pernambuco", "Recife", "Nordeste"),
    "PI": ("Piauí", "Teresina", "Nordeste"),
    "PR": ("Paraná", "Curitiba", "Sul"),
    "RJ": ("Rio de Janeiro", "Rio de Janeiro", "Sudeste"),
    "RN": ("Rio Grande do Norte", "Natal", "Nordeste"),
    "RO": ("Rondônia", "Porto Velho", "Norte"),
    "RR": ("Roraima", "Boa Vista", "Norte"),
    "RS": ("Rio Grande do Sul", "Porto Alegre", "Sul"),
    "SC": ("Santa Catarina", "Florianópolis", "Sul"),
    "SE": ("Sergipe", "Aracaju", "Nordeste"),
    "SP": ("São Paulo", "São Paulo", "Sudeste"),
    "TO": ("Tocantins", "Palmas", "Norte"),
}

CREATED = {"MS": 1977, "TO": 1988}
W, H = 800, 750
SIMPLIFY = 0.035
PAD = 10


def _bounds(features: list) -> tuple[float, float, float, float]:
    coords: list[tuple[float, float]] = []
    for f in features:
        geom = shape(f["geometry"])
        minx, miny, maxx, maxy = geom.bounds
        coords.extend([(minx, miny), (maxx, maxy)])
    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]
    return min(xs), min(ys), max(xs), max(ys)


def _project(bounds: tuple[float, float, float, float]) -> tuple[float, float, float, float]:
    min_x, min_y, max_x, max_y = bounds
    sx = (W - 2 * PAD) / (max_x - min_x)
    sy = (H - 2 * PAD) / (max_y - min_y)
    s = min(sx, sy)
    ox = PAD + (W - 2 * PAD - (max_x - min_x) * s) / 2
    oy = PAD + (H - 2 * PAD - (max_y - min_y) * s) / 2
    return min_x, min_y, max_x, max_y, s, ox, oy


def _ring_path(ring: list, proj: tuple) -> str:
    min_x, min_y, max_x, max_y, s, ox, oy = proj
    pts = []
    for lon, lat in ring:
        x = round(ox + (lon - min_x) * s, 2)
        y = round(oy + (max_y - lat) * s, 2)
        pts.append((x, y))
    if len(pts) < 3:
        return ""
    d = f"M {pts[0][0]},{pts[0][1]}"
    for x, y in pts[1:]:
        d += f" L {x},{y}"
    return d + " Z"


def _geom_paths(geom, proj: tuple) -> list[str]:
    paths: list[str] = []
    if geom.geom_type == "Polygon":
        p = _ring_path(list(geom.exterior.coords), proj)
        if p:
            paths.append(p)
    elif geom.geom_type == "MultiPolygon":
        for poly in geom.geoms:
            p = _ring_path(list(poly.exterior.coords), proj)
            if p:
                paths.append(p)
    return paths


def _centroid_xy(geom, proj: tuple) -> tuple[float, float]:
    min_x, min_y, max_x, max_y, s, ox, oy = proj
    c = geom.centroid
    x = round(ox + (c.x - min_x) * s, 1)
    y = round(oy + (max_y - c.y) * s, 1)
    return x, y


def _feature_by_sigla(features: list) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for f in features:
        sigla = f["properties"].get("sigla", "")
        out[sigla] = f
    return out


def build() -> dict:
    raw = json.loads(GEO.read_text())
    features = raw["features"]
    by_sigla = _feature_by_sigla(features)
    bounds = _bounds(features)
    proj = _project(bounds)

    states = []
    geoms: dict[str, object] = {}

    for f in features:
        sigla = f["properties"]["sigla"]
        name, capital, region = CAPITALS[sigla]
        geom = shape(f["geometry"]).simplify(SIMPLIFY, preserve_topology=True)
        geoms[sigla] = geom
        cx, cy = _centroid_xy(geom, proj)
        states.append({
            "id": sigla,
            "name": name,
            "capital": capital,
            "region": region,
            "paths": _geom_paths(geom, proj),
            "created": CREATED.get(sigla),
            "label_x": cx,
            "label_y": cy,
        })

    mt_ms_geom = unary_union([geoms["MT"], geoms["MS"]]).simplify(SIMPLIFY, preserve_topology=True)
    go_to_geom = unary_union([geoms["GO"], geoms["TO"]]).simplify(SIMPLIFY, preserve_topology=True)

    merged = [
        {
            "id": "MT_MS",
            "name": "Mato Grosso",
            "capital": "Cuiabá",
            "region": "Centro-Oeste",
            "note": "Antes de 1977, Mato Grosso do Sul fazia parte deste estado maior.",
            "components": ["MT", "MS"],
            "paths": _geom_paths(mt_ms_geom, proj),
            "label_x": _centroid_xy(mt_ms_geom, proj)[0],
            "label_y": _centroid_xy(mt_ms_geom, proj)[1],
        },
        {
            "id": "GO_TO",
            "name": "Goiás",
            "capital": "Goiânia",
            "region": "Centro-Oeste",
            "note": "Antes de 1988, Tocantins fazia parte deste estado maior.",
            "components": ["GO", "TO"],
            "paths": _geom_paths(go_to_geom, proj),
            "label_x": _centroid_xy(go_to_geom, proj)[0],
            "label_y": _centroid_xy(go_to_geom, proj)[1],
        },
    ]

    periods = {
        "post_1988": {
            "label": "Após 1988",
            "hidden_states": [],
            "visible_merged": [],
        },
        "1977_1988": {
            "label": "1977–1988",
            "hidden_states": ["GO", "TO"],
            "visible_merged": ["GO_TO"],
        },
        "1942_1977": {
            "label": "1942–1977",
            "hidden_states": ["MT", "MS", "GO", "TO"],
            "visible_merged": ["MT_MS", "GO_TO"],
        },
    }

    modes = {
        "evolution": {"label": "Evolução histórica", "description": "Veja como o mapa mudou ao criar novos estados."},
        "regions": {"label": "Por região", "description": "Cores por região do Brasil."},
        "capitals": {"label": "Capitais", "description": "Clique para ver a capital de cada estado."},
        "new_states": {"label": "Novos estados", "description": "Destaque dos estados criados após 1977."},
    "capital_quiz": {"label": "Quiz de capitais", "description": "Clique no estado e digite a capital."},
    "capital_game": {"label": "Jogo das capitais", "description": "Complete todas as capitais no mapa."},
    }

    return {
        "viewBox": f"0 0 {W} {H}",
        "periods": periods,
        "modes": modes,
        "states": states,
        "merged": merged,
    }


def main() -> None:
    data = build()
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"Wrote {len(data['states'])} states + {len(data['merged'])} merged → {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
