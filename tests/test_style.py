"""Tests for site/v2/style.json (REFACTOR_PLAN.md §2.7 lint suite).

Asserts:
- Valid JSON schema structure (MapLibre Style Spec v8).
- Relative glyphs and sprites URLs (no external CDNs / absolute schemes).
- Every symbol layer sets text-allow-overlap: false.
- Every symbol layer has a symbol-sort-key for collision priority.
- Text sizes stay within the §2.4 / §3.2 font caps across all zoom stops.
- Minzoom and maxzoom bounds are consistent with the four semantic zoom levels.
"""

import json
from pathlib import Path
import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
STYLE_PATH = REPO_ROOT / "site" / "v2" / "style.json"

# Semantic levels: z0 (3.0), z1 (4.5), z2 (6.0), z3 (7.5), overzoom cap 8.5
VALID_ZOOM_LEVELS = [3.0, 4.5, 6.0, 7.5, 8.5]

# §2.4 / §3.2 font caps per feature class
FONT_CAPS = {
    "continent": 42,
    "country": 28,
    "landmark": 16,
    "fact": 13,
}
FONT_MIN = 11

LAYER_CLASSES = {
    "symbol-continent": "continent",
    "symbol-ocean": "continent",
    "symbol-range": "landmark",
    "symbol-country": "country",
    "symbol-country-hint": "fact",
    "symbol-country-tag": "fact",
    "symbol-event": "landmark",
    "symbol-event-z1": "landmark",
    "symbol-summit": "landmark",
    "symbol-pass": "landmark",
    "symbol-fact": "fact",
}


@pytest.fixture(scope="module")
def style():
    assert STYLE_PATH.exists(), f"style.json not found at {STYLE_PATH}"
    with open(STYLE_PATH, encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="module")
def symbol_layers(style):
    return [l for l in style.get("layers", []) if l.get("type") == "symbol"]


def test_style_valid_v8(style):
    assert style.get("version") == 8
    assert "layers" in style and len(style["layers"]) > 0


def test_glyphs_and_sprites_relative(style):
    glyphs = style.get("glyphs")
    assert glyphs, "style.json must specify glyphs"
    assert not glyphs.startswith(("http://", "https://", "/")), f"glyphs must be relative URL, got: {glyphs}"

    sprite = style.get("sprite")
    if sprite:
        assert not sprite.startswith(("http://", "https://", "/")), f"sprite must be relative URL, got: {sprite}"


def test_symbol_layers_no_overlap(symbol_layers):
    for layer in symbol_layers:
        lid = layer.get("id")
        layout = layer.get("layout", {})
        assert layout.get("text-allow-overlap") is False, (
            f"Layer '{lid}' must set text-allow-overlap: false"
        )


def test_symbol_layers_sort_key(symbol_layers):
    for layer in symbol_layers:
        lid = layer.get("id")
        layout = layer.get("layout", {})
        assert "symbol-sort-key" in layout, f"Layer '{lid}' must define symbol-sort-key"


def test_symbol_layers_zoom_bounds(symbol_layers):
    for layer in symbol_layers:
        lid = layer.get("id")
        minz = layer.get("minzoom", 0)
        maxz = layer.get("maxzoom", 24)
        assert minz >= 3.0, f"Layer '{lid}' minzoom ({minz}) is below global minzoom 3.0"
        assert maxz <= 8.5, f"Layer '{lid}' maxzoom ({maxz}) exceeds max overzoom 8.5"
        assert minz < maxz, f"Layer '{lid}' minzoom ({minz}) must be strictly less than maxzoom ({maxz})"


def _eval_zoom_expression(expr, zoom):
    """Evaluate simple linear zoom interpolation expression."""
    if isinstance(expr, (int, float)):
        return float(expr)
    if isinstance(expr, list) and len(expr) >= 4:
        # ['interpolate', ['linear'], ['zoom'], stop1, val1, stop2, val2, ...]
        if expr[0] == "interpolate" and expr[2] == ["zoom"]:
            stops = []
            for i in range(3, len(expr), 2):
                stops.append((float(expr[i]), float(expr[i + 1])))
            stops.sort(key=lambda s: s[0])
            if zoom <= stops[0][0]:
                return stops[0][1]
            if zoom >= stops[-1][0]:
                return stops[-1][1]
            for (z0, v0), (z1, v1) in zip(stops[:-1], stops[1:]):
                if z0 <= zoom <= z1:
                    t = (zoom - z0) / (z1 - z0)
                    return v0 + t * (v1 - v0)
    raise ValueError(f"Unsupported text-size expression: {expr}")


def test_symbol_layers_font_caps(symbol_layers):
    for layer in symbol_layers:
        lid = layer.get("id")
        cls = LAYER_CLASSES.get(lid)
        assert cls, f"Unknown symbol layer '{lid}', add to LAYER_CLASSES"
        cap = FONT_CAPS[cls]
        layout = layer.get("layout", {})
        size_expr = layout.get("text-size")
        assert size_expr is not None, f"Layer '{lid}' missing text-size"

        minz = layer.get("minzoom", 3.0)
        maxz = layer.get("maxzoom", 8.5)

        # Check font sizes across test zooms in its active range
        test_zooms = [z for z in [3.0, 4.5, 6.0, 7.5, 8.5] if minz <= z <= maxz]
        if not test_zooms:
            test_zooms = [minz, maxz]

        for z in test_zooms:
            resolved_size = _eval_zoom_expression(size_expr, z)
            assert resolved_size >= FONT_MIN - 0.01, (
                f"Layer '{lid}' size {resolved_size}px at zoom {z} below minimum {FONT_MIN}px"
            )
            assert resolved_size <= cap + 0.01, (
                f"Layer '{lid}' size {resolved_size}px at zoom {z} exceeds cap {cap}px for {cls}"
            )
