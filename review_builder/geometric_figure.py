"""Figuras geométricas SVG offline para explicações e exercícios PE (Desenho Geométrico)."""

from __future__ import annotations

from typing import Any


def _scale_dims(w: float, h: float, max_side: float = 110.0) -> tuple[float, float, float]:
    m = max(w, h, 0.1)
    s = max_side / m
    return w * s, h * s, s


def _dim_h(x1: float, x2: float, y: float, label: str) -> list[dict[str, Any]]:
    mid = (x1 + x2) / 2
    return [
        {"t": "line", "x1": x1, "y1": y, "x2": x2, "y2": y, "stroke": "#64748b", "width": 1},
        {"t": "line", "x1": x1, "y1": y - 4, "x2": x1, "y2": y + 4, "stroke": "#64748b", "width": 1},
        {"t": "line", "x1": x2, "y1": y - 4, "x2": x2, "y2": y + 4, "stroke": "#64748b", "width": 1},
        {"t": "text", "x": mid, "y": y + 14, "text": label},
    ]


def _dim_v(y1: float, y2: float, x: float, label: str) -> list[dict[str, Any]]:
    mid = (y1 + y2) / 2
    return [
        {"t": "line", "x1": x, "y1": y1, "x2": x, "y2": y2, "stroke": "#64748b", "width": 1},
        {"t": "line", "x1": x - 4, "y1": y1, "x2": x + 4, "y2": y1, "stroke": "#64748b", "width": 1},
        {"t": "line", "x1": x - 4, "y1": y2, "x2": x + 4, "y2": y2, "stroke": "#64748b", "width": 1},
        {"t": "text", "x": x - 8, "y": mid + 4, "text": label, "anchor": "end"},
    ]


def _right_angle_mark(x: float, y: float, size: float = 8, corner: str = "bl") -> dict[str, Any]:
    if corner == "bl":
        d = f"M {x + size} {y} L {x + size} {y - size} L {x} {y - size}"
    elif corner == "br":
        d = f"M {x - size} {y} L {x - size} {y - size} L {x} {y - size}"
    else:
        d = f"M {x} {y} L {x + size} {y} L {x + size} {y + size}"
    return {"t": "path", "d": d, "fill": "none", "stroke": "#334155", "width": 1}


def _wrap(content: dict[str, Any]) -> dict[str, Any]:
    return {"type": "geometric_figure", "content": content}


def rectangle(
    width: float,
    height: float,
    *,
    w_label: str,
    h_label: str,
    title: str | None = None,
    aria_label: str | None = None,
    fill: str = "#c4b5fd",
    stroke: str = "#4338ca",
) -> dict[str, Any]:
    sw, sh, _ = _scale_dims(width, height)
    ox, oy = 55.0, 35.0
    elements: list[dict[str, Any]] = [
        {
            "t": "rect",
            "x": ox,
            "y": oy,
            "width": sw,
            "height": sh,
            "fill": fill,
            "stroke": stroke,
        },
        _right_angle_mark(ox, oy + sh, corner="bl"),
    ]
    elements.extend(_dim_h(ox, ox + sw, oy + sh + 12, w_label))
    elements.extend(_dim_v(oy, oy + sh, ox - 18, h_label))
    return _wrap({
        "title": title,
        "aria_label": aria_label or f"Retângulo de {w_label} por {h_label}",
        "view_box": "0 0 220 160",
        "elements": elements,
    })


def unit_grid(
    cols: int,
    rows: int,
    *,
    title: str | None = None,
    aria_label: str | None = None,
    unit_label: str = "1 cm",
    fill: str = "#ddd6fe",
) -> dict[str, Any]:
    cell = 18.0
    ox, oy = 40.0, 30.0
    w, h = cols * cell, rows * cell
    elements: list[dict[str, Any]] = [
        {
            "t": "rect",
            "x": ox,
            "y": oy,
            "width": w,
            "height": h,
            "fill": fill,
            "stroke": "#4338ca",
        },
    ]
    for c in range(1, cols):
        x = ox + c * cell
        elements.append({
            "t": "line",
            "x1": x,
            "y1": oy,
            "x2": x,
            "y2": oy + h,
            "stroke": "#6366f1",
            "width": 0.8,
        })
    for r in range(1, rows):
        y = oy + r * cell
        elements.append({
            "t": "line",
            "x1": ox,
            "y1": y,
            "x2": ox + w,
            "y2": y,
            "stroke": "#6366f1",
            "width": 0.8,
        })
    elements.append({"t": "text", "x": ox + w / 2, "y": oy + h + 22, "text": f"Cada quadradinho = {unit_label}"})
    return _wrap({
        "title": title,
        "aria_label": aria_label or f"Malha de {cols} por {rows} quadrados de {unit_label}",
        "view_box": "0 0 220 160",
        "elements": elements,
    })


def right_triangle(
    base: float,
    height: float,
    *,
    b_label: str,
    h_label: str,
    title: str | None = None,
    aria_label: str | None = None,
    fill: str = "#5eead4",
    stroke: str = "#0f766e",
) -> dict[str, Any]:
    sb, sh, _ = _scale_dims(base, height)
    ox, oy = 50.0, 35.0
    x2, y2 = ox + sb, oy
    x3, y3 = ox, oy + sh
    points = f"{ox},{oy} {x2},{y2} {x3},{y3}"
    elements: list[dict[str, Any]] = [
        {"t": "polygon", "points": points, "fill": fill, "stroke": stroke},
        _right_angle_mark(x3, y2, corner="br"),
    ]
    elements.extend(_dim_h(ox, x2, y2 + 12, b_label))
    elements.extend(_dim_v(oy, y2, ox - 18, h_label))
    return _wrap({
        "title": title,
        "aria_label": aria_label or f"Triângulo retângulo base {b_label} altura {h_label}",
        "view_box": "0 0 220 160",
        "elements": elements,
    })


def parallelogram(
    base: float,
    height: float,
    skew: float = 0.35,
    *,
    base_label: str,
    height_label: str,
    title: str | None = None,
    aria_label: str | None = None,
    fill: str = "#86efac",
    stroke: str = "#15803d",
) -> dict[str, Any]:
    sb, sh, _ = _scale_dims(base, height)
    sk = sb * skew
    ox, oy = 45.0, 40.0
    pts = (
        f"{ox + sk},{oy} {ox + sb + sk},{oy} "
        f"{ox + sb},{oy + sh} {ox},{oy + sh}"
    )
    elements: list[dict[str, Any]] = [
        {"t": "polygon", "points": pts, "fill": fill, "stroke": stroke},
        {
            "t": "line",
            "x1": ox + sk,
            "y1": oy,
            "x2": ox + sk,
            "y2": oy + sh,
            "stroke": "#64748b",
            "width": 1,
            "dash": True,
        },
    ]
    elements.extend(_dim_h(ox + sk, ox + sb + sk, oy - 10, base_label))
    elements.extend(_dim_v(oy, oy + sh, ox + sk - 14, height_label))
    return _wrap({
        "title": title,
        "aria_label": aria_label or f"Paralelogramo base {base_label} altura {height_label}",
        "view_box": "0 0 220 160",
        "elements": elements,
    })


def trapezoid(
    top: float,
    bottom: float,
    height: float,
    *,
    top_label: str,
    bottom_label: str,
    height_label: str,
    title: str | None = None,
    aria_label: str | None = None,
    fill: str = "#fca5a5",
    stroke: str = "#b91c1c",
) -> dict[str, Any]:
    sb, sh, _ = _scale_dims(bottom, height)
    st = sb * (top / bottom) if bottom else sb * 0.7
    ox, oy = 50.0, 40.0
    inset = (sb - st) / 2
    pts = (
        f"{ox + inset},{oy} {ox + inset + st},{oy} "
        f"{ox + sb},{oy + sh} {ox},{oy + sh}"
    )
    elements: list[dict[str, Any]] = [
        {"t": "polygon", "points": pts, "fill": fill, "stroke": stroke},
        _right_angle_mark(ox, oy + sh, corner="bl"),
    ]
    elements.extend(_dim_h(ox + inset, ox + inset + st, oy - 10, top_label))
    elements.extend(_dim_h(ox, ox + sb, oy + sh + 12, bottom_label))
    elements.extend(_dim_v(oy, oy + sh, ox - 18, height_label))
    return _wrap({
        "title": title,
        "aria_label": aria_label or f"Trapézio bases {top_label} e {bottom_label}",
        "view_box": "0 0 220 160",
        "elements": elements,
    })


def exercise_visual(block: dict[str, Any]) -> dict[str, Any]:
    """Envolve bloco geometric_figure para campo visual de exercício."""
    return {"type": "geometric_figure", "content": block["content"]}
