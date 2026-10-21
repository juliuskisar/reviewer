"""Gera brazil_states.json com paths SVG, fusões históricas e centróides.

Uso: python -m review_builder.map_data.build_brazil_states
"""

from __future__ import annotations

import json
from pathlib import Path

from shapely.geometry import LineString, shape
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

# Linhas imaginárias que cortam o Brasil (Módulo 10 — Geografia 4º ano)
PARALLELS = [
    {"id": "equator", "label": "Linha do Equador", "lat": 0.0, "color": "#dc2626"},
    {"id": "capricorn", "label": "Trópico de Capricórnio", "lat": -23.4366, "color": "#ea580c"},
]

# Zonas em relação às linhas imaginárias (legenda estilo p. 180 do caderno)
LINE_ZONES = {
    "equator_cut": {
        "label": "Cortado pela linha do Equador",
        "color": "#f87171",
        "description": "Parte do estado fica no hemisfério Norte; o restante, no hemisfério Sul.",
    },
    "intertropical": {
        "label": "Zona intertropical (hemisfério Sul)",
        "color": "#fecaca",
        "description": "Entre o Equador e o Trópico de Capricórnio — raios solares mais perpendiculares, calor o ano todo.",
    },
    "capricorn_cut": {
        "label": "Cortado pelo Trópico de Capricórnio",
        "color": "#fde68a",
        "description": "Parte na zona intertropical, parte na zona temperada Sul.",
    },
    "temperate_south": {
        "label": "Zona temperada Sul",
        "color": "#facc15",
        "description": "Ao sul do Trópico de Capricórnio — raios inclinados, inverno mais frio.",
    },
}

# Camada temática: clima predominante por estado (aproximação didática do mapa Climas do Brasil)
CLIMATES = {
    "equatorial": {"label": "Equatorial", "color": "#ef4444",
                   "description": "Quente e úmido o ano todo; chuvas abundantes."},
    "tropical": {"label": "Tropical", "color": "#facc15",
                 "description": "Quente o ano todo; chuvas concentradas no verão e inverno seco."},
    "tropical_litoraneo": {"label": "Tropical litorâneo", "color": "#f472b6",
                           "description": "Quente e mais úmido por causa dos ventos do oceano."},
    "tropical_semiarido": {"label": "Tropical semiárido", "color": "#fb923c",
                           "description": "Quente; chuvas escassas em poucos meses — pode haver seca."},
    "tropical_altitude": {"label": "Tropical de altitude", "color": "#86efac",
                          "description": "Inverno mais frio nas áreas altas do Sudeste e norte do PR."},
    "subtropical": {"label": "Subtropical", "color": "#a78bfa",
                    "description": "Quatro estações bem definidas; inverno mais frio do Brasil."},
}
CLIMATE_BY_STATE: dict[str, list[str]] = {
    "AC": ["equatorial"], "AM": ["equatorial"], "AP": ["equatorial"], "PA": ["equatorial"],
    "RR": ["equatorial"], "RO": ["equatorial", "tropical"],
    "MA": ["tropical", "equatorial"], "MT": ["tropical", "equatorial"], "TO": ["tropical"],
    "GO": ["tropical"], "DF": ["tropical"], "MS": ["tropical", "subtropical"],
    "MG": ["tropical", "tropical_altitude", "tropical_semiarido"],
    "SP": ["tropical", "tropical_altitude", "tropical_litoraneo", "subtropical"],
    "PI": ["tropical", "tropical_semiarido"],
    "BA": ["tropical_semiarido", "tropical", "tropical_litoraneo"],
    "CE": ["tropical_semiarido", "tropical_litoraneo"], "RN": ["tropical_semiarido", "tropical_litoraneo"],
    "PB": ["tropical_semiarido", "tropical_litoraneo"], "PE": ["tropical_semiarido", "tropical_litoraneo"],
    "AL": ["tropical_litoraneo", "tropical_semiarido"], "SE": ["tropical_litoraneo", "tropical_semiarido"],
    "ES": ["tropical_litoraneo", "tropical_altitude"], "RJ": ["tropical_litoraneo", "tropical_altitude"],
    "PR": ["subtropical", "tropical"], "SC": ["subtropical"], "RS": ["subtropical"],
}

# Camada temática: formações vegetais originais (aproximação por estado — mapa p. 192)
VEGETATION = {
    "amazonica": {"label": "Floresta Amazônica", "color": "#4ade80",
                  "description": "Floresta densa e úmida do Norte; clima equatorial."},
    "cocais": {"label": "Mata dos Cocais", "color": "#a855f7",
               "description": "Palmeiras (babaçu, carnaúba) na transição Norte–Nordeste."},
    "atlantica": {"label": "Mata Atlântica", "color": "#15803d",
                  "description": "Floresta tropical do litoral leste — muito desmatada."},
    "araucarias": {"label": "Mata das Araucárias", "color": "#b45309",
                   "description": "Pinheiros-do-paraná nos planaltos frios do Sul."},
    "cerrado": {"label": "Cerrado", "color": "#f9a8d4",
                "description": "Savana brasileira: árvores retorcidas, estação seca."},
    "caatinga": {"label": "Caatinga", "color": "#fde047",
                 "description": "Vegetação seca do semiárido nordestino — cactos e arbustos."},
    "campos": {"label": "Campos", "color": "#fb923c",
               "description": "Campos de gramíneas, sobretudo no Sul."},
    "pantanal": {"label": "Vegetação do Pantanal", "color": "#dc2626",
                 "description": "Planície alagável do Centro-Oeste."},
    "litoranea": {"label": "Vegetação litorânea", "color": "#0f766e",
                  "description": "Restingas e mangues junto ao mar."},
}
VEGETATION_BY_STATE: dict[str, list[str]] = {
    "AC": ["amazonica"], "AM": ["amazonica"], "AP": ["amazonica", "litoranea"], "PA": ["amazonica"],
    "RR": ["amazonica", "campos"], "RO": ["amazonica", "cerrado"],
    "MA": ["cocais", "amazonica", "cerrado"], "PI": ["cocais", "cerrado", "caatinga"],
    "MT": ["cerrado", "amazonica", "pantanal"], "TO": ["cerrado"], "GO": ["cerrado"], "DF": ["cerrado"],
    "MS": ["cerrado", "pantanal", "atlantica"], "MG": ["cerrado", "atlantica", "caatinga"],
    "SP": ["atlantica", "cerrado", "litoranea"],
    "BA": ["caatinga", "cerrado", "atlantica"], "CE": ["caatinga", "litoranea"], "RN": ["caatinga", "litoranea"],
    "PB": ["caatinga", "atlantica"], "PE": ["caatinga", "atlantica"], "AL": ["caatinga", "atlantica"],
    "SE": ["caatinga", "atlantica"],
    "ES": ["atlantica", "litoranea"], "RJ": ["atlantica", "litoranea"],
    "PR": ["araucarias", "atlantica", "campos"], "SC": ["araucarias", "atlantica", "campos"],
    "RS": ["campos", "araucarias", "atlantica"],
}


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


def _lat_to_y(lat: float, proj: tuple) -> float:
    _, _, _, max_y, s, _, oy = proj
    return round(oy + (max_y - lat) * s, 2)


def _parallels(proj: tuple, bounds: tuple) -> list[dict]:
    min_lon, _, max_lon, _ = bounds
    out = []
    for p in PARALLELS:
        out.append({
            **p,
            "y": _lat_to_y(p["lat"], proj),
            "x1": 0,
            "x2": W,
        })
    return out


def _line_zone(geom, bounds: tuple) -> dict:
    min_lon, _, max_lon, _ = bounds
    cuts = {}
    for p in PARALLELS:
        line = LineString([(min_lon - 1, p["lat"]), (max_lon + 1, p["lat"])])
        cuts[p["id"]] = bool(geom.intersects(line))
    cap_lat = next(p["lat"] for p in PARALLELS if p["id"] == "capricorn")
    if cuts["equator"]:
        zone = "equator_cut"
    elif cuts["capricorn"]:
        zone = "capricorn_cut"
    elif geom.centroid.y < cap_lat:
        zone = "temperate_south"
    else:
        zone = "intertropical"
    return {"equator": cuts["equator"], "capricorn": cuts["capricorn"], "zone": zone}


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
            "lines": _line_zone(shape(f["geometry"]), bounds),
            "climates": CLIMATE_BY_STATE[sigla],
            "vegetation": VEGETATION_BY_STATE[sigla],
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
        "imaginary_lines": {
            "label": "Linhas imaginárias",
            "description": "Equador e Trópico de Capricórnio sobre o Brasil — hemisférios e zonas térmicas.",
        },
        "climates": {
            "label": "Climas",
            "description": "Clima predominante em cada estado (aproximação do mapa Climas do Brasil).",
        },
        "vegetation": {
            "label": "Vegetação original",
            "description": "Formação vegetal predominante em cada estado (aproximação do mapa de vegetação).",
        },
        "theme_game": {"label": "Jogo temático", "description": "Responda o tema de cada estado."},
    }

    thematic = {
        "imaginary_lines": {
            "title": "Linhas imaginárias",
            "state_key": "lines",
            "legend": [{"id": k, **v} for k, v in LINE_ZONES.items()],
            "approximate": False,
        },
        "climates": {
            "title": "Clima predominante",
            "state_key": "climates",
            "legend": [{"id": k, **v} for k, v in CLIMATES.items()],
            "approximate": True,
            "note": "Aproximação por estado: o mapa real segue limites naturais, e um estado pode ter mais de um clima.",
        },
        "vegetation": {
            "title": "Formação vegetal original",
            "state_key": "vegetation",
            "legend": [{"id": k, **v} for k, v in VEGETATION.items()],
            "approximate": True,
            "note": "Aproximação por estado: as formações originais não seguem as divisas; o clique mostra as demais.",
        },
    }

    return {
        "viewBox": f"0 0 {W} {H}",
        "periods": periods,
        "modes": modes,
        "parallels": _parallels(proj, bounds),
        "thematic": thematic,
        "states": states,
        "merged": merged,
    }


def main() -> None:
    data = build()
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    print(f"Wrote {len(data['states'])} states + {len(data['merged'])} merged → {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
