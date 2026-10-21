"""Testes dos componentes de Geografia: camadas temáticas do mapa, globo térmico e jogos."""

from __future__ import annotations

from pathlib import Path

from review_builder.brazil_map import get_map_data
from review_builder.composer import compose_page
from review_builder.schema_validator import validate_contract
from review_builder.thermal_globe import get_globe_data
from review_builder.utils import save_json

ASSETS = Path(__file__).parent.parent / "assets" / "example-review"


def test_map_data_has_parallels_and_zones() -> None:
    data = get_map_data()
    ids = {p["id"] for p in data["parallels"]}
    assert ids == {"equator", "capricorn"}
    zones = {s["id"]: s["lines"] for s in data["states"]}
    assert all(zones[uf]["equator"] for uf in ("AP", "AM", "PA", "RR"))
    assert all(zones[uf]["capricorn"] for uf in ("MS", "SP", "PR"))
    assert zones["SC"]["zone"] == "temperate_south"
    assert zones["RS"]["zone"] == "temperate_south"
    assert zones["GO"]["zone"] == "intertropical"


def test_map_thematic_layers_cover_all_states() -> None:
    data = get_map_data()
    for theme in ("climates", "vegetation"):
        legend_ids = {item["id"] for item in data["thematic"][theme]["legend"]}
        for state in data["states"]:
            values = state[theme]
            assert values, f"{state['id']} sem {theme}"
            assert set(values) <= legend_ids, f"{state['id']}: {values} fora da legenda {theme}"
    zone_ids = {item["id"] for item in data["thematic"]["imaginary_lines"]["legend"]}
    assert all(s["lines"]["zone"] in zone_ids for s in data["states"])


def test_globe_data_geometry() -> None:
    globe = get_globe_data()
    ys = [p["y"] for p in globe["parallels"]]
    assert ys == sorted(ys), "paralelos devem ir do norte (y menor) ao sul"
    assert [p["id"] for p in globe["parallels"]] == ["arctic", "cancer", "equator", "capricorn", "antarctic"]
    assert abs(globe["parallels"][2]["y"] - globe["cy"]) < 0.01
    assert len(globe["bands"]) == 5
    assert {b["zone"] for b in globe["bands"]} == {"polar", "temperate", "intertropical"}
    total_height = sum(b["height"] for b in globe["bands"])
    assert abs(total_height - 2 * globe["r"]) < 0.1


def _geo_content() -> dict:
    return {
        "version": "1.0",
        "review_id": "geo-test",
        "title": "Geo",
        "language": "pt-BR",
        "sections": [
            {
                "id": "maps",
                "type": "interactive_maps",
                "title": "Mapas",
                "blocks": [
                    {"type": "heading", "content": {"level": 3, "text": "Linhas"}},
                    {"type": "brazil_map", "content": {"mode": "imaginary_lines", "show_mode_toggle": False}},
                    {"type": "thermal_globe", "content": {"mode": "explore", "show_mode_toggle": True}},
                ],
            },
            {
                "id": "climate_game",
                "type": "map_theme_game",
                "title": "Jogo dos climas",
                "theme": "climates",
                "question_prefix": "Qual clima predomina em",
                "blocks": [],
            },
        ],
    }


def test_schema_accepts_geography_components() -> None:
    assert validate_contract("review-content", _geo_content()) == []


def test_compose_renders_geography_components(tmp_path: Path) -> None:
    content = tmp_path / "review-content.json"
    exercises = tmp_path / "exercises.json"
    save_json(content, _geo_content())
    save_json(exercises, {"version": "1.0", "review_id": "geo-test", "exercises": []})
    out = tmp_path / "out"
    html = compose_page(content, exercises, out, assets_root=ASSETS).read_text(encoding="utf-8")
    assert 'data-mode="imaginary_lines"' in html
    assert 'class="brazil-map__parallel"' in html
    assert 'data-component="thermal-globe"' in html
    assert 'data-component="map-theme-game"' in html
    assert 'data-theme="climates"' in html
    assert "THERMAL_GLOBE_DATA" in html
    assert 'data-zone="equator_cut"' in html
    assert "https://" not in html
