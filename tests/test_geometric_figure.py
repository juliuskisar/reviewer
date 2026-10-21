"""Testes do componente geometric_figure."""

from review_builder.geometric_figure import rectangle, right_triangle, unit_grid


def test_rectangle_figure_schema_shape() -> None:
    block = rectangle(5, 4, w_label="5 cm", h_label="4 cm")
    assert block["type"] == "geometric_figure"
    assert block["content"]["view_box"]
    assert len(block["content"]["elements"]) >= 3


def test_triangle_figure_has_polygon() -> None:
    block = right_triangle(7, 4, b_label="7 cm", h_label="4 cm")
    kinds = {el["t"] for el in block["content"]["elements"]}
    assert "polygon" in kinds


def test_unit_grid_lines() -> None:
    block = unit_grid(5, 4)
    lines = [el for el in block["content"]["elements"] if el["t"] == "line"]
    assert len(lines) == (5 - 1) + (4 - 1)
