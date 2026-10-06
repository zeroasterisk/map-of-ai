#!/usr/bin/env python3
"""build_dem.py — 2D Digital Elevation Model, Lambertian hillshade, hypsometric contours, and Lehmann hachures.

Replaces cartoon 2.5D triangular mountain icons with an authentic planimetric topographic terrain model:
  1. Constructs a continuous 2D elevation field Z(x, y) over the 1800×1050 plate from:
     - The Silicon Range (data/threads/compute-mountain-range.yaml) modeled as an anisotropic 2D ridge massif
       with milestone summits, secondary spurs, and glacial pass saddles.
     - Continental plateau / escarpment relief across the Symbolic Heartland, Winter Steppes, Expert Systems Plateau,
       and Antecedent Isles.
  2. Computes 2D partial derivatives (dZ/dx, dZ/dy), slope magnitude, aspect angle, and northwest (315° azimuth,
     42° altitude) Lambertian hillshading.
  3. Writes:
     - site/assets/textures/hillshade.png (RGBA northwest-illuminated topographic relief shading for atlas.html)
     - site/data/contours.geojson (multi-tier iso-elevation contour lines in plate coordinates)
     - site/data/hachures.geojson (gradient-aligned Lehmann slope hachures with NW/SE illumination weights)
"""
from __future__ import annotations

import datetime as dt
import json
import math
from pathlib import Path

import numpy as np
from PIL import Image
from scipy.ndimage import gaussian_filter
import yaml

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site"
DATA = REPO / "data"

W, H = 1800, 1050
PAD_L, PAD_R, ARCH_W = 24, 200, 150
MAP_TOP, MAP_BOT = 150, 560
BANDS = ["N1", "N2", "C", "S1", "S2"]
BAND_H = (MAP_BOT - MAP_TOP) / len(BANDS)
MAP_MID = (MAP_TOP + MAP_BOT) / 2.0
Y_OFF = 165.0
SPINE_AMP = 46.0

NOW = dt.date.today()
PRESENT = NOW.year + (NOW.month - 1) / 12.0
SEG = [(1943.0, 1974.0, 1.0), (1974.0, 2006.0, 1.5), (2006.0, 2017.0, 3.0), (2017.0, PRESENT, 6.0)]
YSEG = [(2017.0, 1.0), (2022.0, 1.1), (2024.0, 1.3), (2025.2, 1.6), (PRESENT, 2.0)]

MAIN_W = W - PAD_L - PAD_R - ARCH_W
UNITS = sum((b - a) * k for a, b, k in SEG)
PX_PER_UNIT = MAIN_W / UNITS


def x_main(yr: float) -> float:
    x = float(PAD_L + ARCH_W)
    for a, b, k in SEG:
        if yr <= a:
            return x
        x += (min(yr, b) - a) * k * PX_PER_UNIT
        if yr <= b:
            return x
    return x


def x_arch(yr: float) -> float:
    d = max(1.0, 1943.0 - yr)
    t = math.log(d + 1.0) / math.log(1943.0 - 1600.0 + 1.0)
    return PAD_L + ARCH_W - 14.0 - t * (ARCH_W - 34.0)


def X(yr: float) -> float:
    return x_main(yr) if yr >= 1943.0 else x_arch(yr)


def year_at(x: float) -> float:
    x0 = float(PAD_L + ARCH_W)
    if x <= x0:
        return 1943.0
    for a, b, k in SEG:
        w = (b - a) * k * PX_PER_UNIT
        if x <= x0 + w:
            return a + (x - x0) / (k * PX_PER_UNIT)
        x0 += w
    return PRESENT


def y_scale(yr: float) -> float:
    if yr <= YSEG[0][0]:
        return YSEG[0][1]
    for i in range(1, len(YSEG)):
        a, sa = YSEG[i - 1]
        b, sb = YSEG[i]
        if yr <= b:
            return sa + (sb - sa) * (yr - a) / (b - a)
    return YSEG[-1][1]


def band_top(b: str) -> float:
    return MAP_TOP + BANDS.index(b) * BAND_H


def spine_y(x: float) -> float:
    t = (x - PAD_L) / (W - PAD_L - PAD_R)
    return SPINE_AMP * (math.sin(t * math.pi * 1.55 - 0.35) * 0.85 + math.sin(t * math.pi * 3.3 + 1.1) * 0.18)


def SY(x: float, py: float) -> float:
    fy = Y_OFF + MAP_MID + (py - MAP_MID) * y_scale(year_at(x))
    return fy + spine_y(x)


def ridge_y(x: float, x0: float, py: float) -> float:
    wobble = 5.0 * math.sin((x - x0) / 47.0) + 3.0 * math.sin((x - x0) / 19.0 + 1.3)
    return SY(x, py + wobble)


def build_dem() -> None:
    thread_path = sorted((DATA / "threads").glob("*.yaml"))[0]
    thread = yaml.safe_load(thread_path.read_text(encoding="utf-8"))
    b0, b1 = thread["placement"]["band"]
    bank = float(thread["placement"].get("bank", 0.5))
    py_ridge = band_top(b0) + bank * (band_top(b1) + BAND_H - band_top(b0))

    y0_yr = float(thread["placement"]["time_range"][0])
    y1_raw = thread["placement"]["time_range"][1]
    y1_yr = PRESENT - 0.06 if y1_raw == "present" else float(y1_raw)
    x0, x1 = X(y0_yr), X(y1_yr)

    milestones = sorted(thread.get("milestones", []), key=lambda m: float(m["year"]))
    passes = sorted(thread.get("passes", []), key=lambda p: float(p["year"]))

    # Coordinate grid (1 px resolution: 1800 x 1050)
    xs = np.arange(W, dtype=np.float32)
    ys = np.arange(H, dtype=np.float32)
    XX, YY = np.meshgrid(xs, ys)

    Z = np.zeros((H, W), dtype=np.float32)

    # 1. Continuous Silicon Range cordillera backbone + milestone massifs in 2D planimetric space
    ridge_ys = np.array([ridge_y(float(x), x0, py_ridge) for x in xs], dtype=np.float32)
    scales = np.array([y_scale(year_at(float(x))) for x in xs], dtype=np.float32)

    # Pass saddle factor along X
    pass_factor = np.ones(W, dtype=np.float32)
    for p in passes:
        px = X(float(p["year"]))
        dist_p = (xs - px) / 16.0
        pass_factor *= 1.0 - 0.62 * np.exp(-0.5 * dist_p * dist_p)

    # Mask to [x0 - 18, x1 + 12] with smooth taper at range ends
    in_range = np.clip((xs - (x0 - 14.0)) / 18.0, 0.0, 1.0) * np.clip(((x1 + 10.0) - xs) / 14.0, 0.0, 1.0)

    # Multi-frequency ridge modulation along the cordillera spine
    crag = (
        0.24
        + 0.08 * np.sin((xs - x0) * 0.11 + 0.5)
        + 0.06 * np.cos((xs - x0) * 0.23 - 0.8)
    )
    sigma_backbone = 10.5 * scales
    dy_grid = YY - ridge_ys[None, :]
    backbone = (
        in_range[None, :]
        * pass_factor[None, :]
        * crag[None, :]
        * np.exp(-0.5 * (dy_grid / sigma_backbone[None, :]) ** 2)
    )
    Z += backbone

    # Add each milestone summit as an anisotropic 2D elliptical massif + NW/SE spurs
    summit_records = []
    for m in milestones:
        yr = float(m["year"])
        peak = float(m.get("peak", 0.5))
        sc_x1 = y_scale(year_at(x1))
        pw_x1 = max(18.0, BAND_H * sc_x1 * (0.28 + 0.42 * peak) * 1.7)
        mx = min(X(yr), x1 - pw_x1 / 2.0 - 2.0)
        my = ridge_y(mx, x0, py_ridge)
        sc = y_scale(year_at(mx))

        # Local tangent angle of ridge
        dx_step = 4.0
        slope_r = (ridge_y(mx + dx_step, x0, py_ridge) - ridge_y(mx - dx_step, x0, py_ridge)) / (2.0 * dx_step)
        ang = math.atan(slope_r)
        ca, sa = math.cos(ang), math.sin(ang)

        sig_along = (13.0 + 15.0 * peak) * (0.85 + 0.25 * sc)
        sig_across = (7.5 + 8.5 * peak) * (0.85 + 0.30 * sc)
        amp = 0.42 + 0.56 * peak

        dx = XX - mx
        dy = YY - my
        u = dx * ca + dy * sa
        v = -dx * sa + dy * ca

        # Primary dome + slight ridge asymmetry + two natural arête spurs
        r2 = (u / sig_along) ** 2 + (v / sig_across) ** 2
        dome = amp * np.exp(-0.5 * r2) * (1.0 + 0.08 * np.cos(u * 0.35) * np.sin(v * 0.45))

        # Spur 1 (NW-SE oblique arête)
        u_s1 = dx * math.cos(ang + 0.65) + dy * math.sin(ang + 0.65)
        v_s1 = -dx * math.sin(ang + 0.65) + dy * math.cos(ang + 0.65)
        spur1 = (0.24 * amp) * np.exp(-0.5 * ((u_s1 / (sig_along * 0.85)) ** 2 + (v_s1 / (sig_across * 0.42)) ** 2))

        # Spur 2 (NE-SW counter-spur)
        u_s2 = dx * math.cos(ang - 0.55) + dy * math.sin(ang - 0.55)
        v_s2 = -dx * math.sin(ang - 0.55) + dy * math.cos(ang - 0.55)
        spur2 = (0.20 * amp) * np.exp(-0.5 * ((u_s2 / (sig_along * 0.75)) ** 2 + (v_s2 / (sig_across * 0.40)) ** 2))

        Z = np.maximum(Z, (dome + spur1 + spur2) * pass_factor[None, :])
        summit_records.append({
            "name": m["name"],
            "label": m.get("label", m["name"]),
            "year": yr,
            "elev": m.get("elev", ""),
            "peak": peak,
            "x": round(float(mx), 2),
            "y": round(float(my), 2),
            "sig_along": round(float(sig_along), 2),
            "sig_across": round(float(sig_across), 2),
            "angle_rad": round(float(ang), 4),
        })

    # 2. Add subtle northern highland plateau relief (Symbolic Heartland, Winter Steppes, Expert Systems Plateau)
    for (yr_a, yr_b, band_name, amp_p) in [
        (1956.0, 1974.0, "N2", 0.16),
        (1974.0, 1993.0, "N1", 0.18),
        (1980.0, 1993.0, "N2", 0.22),
    ]:
        xa, xb = X(yr_a), X(yr_b)
        xc = 0.5 * (xa + xb)
        yc = SY(xc, band_top(band_name) + 0.5 * BAND_H)
        sx = 0.45 * (xb - xa)
        sy = 0.55 * BAND_H
        plat = amp_p * np.exp(-0.5 * (((XX - xc) / sx) ** 4 + ((YY - yc) / sy) ** 4))
        Z += plat

    # Smooth slightly with Gaussian filter for natural geomorphology
    Z = gaussian_filter(Z, sigma=1.8)
    Z = np.clip(Z / max(float(Z.max()), 1e-6), 0.0, 1.0)

    # 3. Compute 2D gradients and NW (315° azimuth, 42° altitude) Lambertian hillshade
    dZy, dZx = np.gradient(Z)
    slope = np.hypot(dZx, dZy) * 18.0
    aspect = np.arctan2(dZy, dZx)

    azimuth = math.radians(225.0)  # light from top-left (NW in screen coords: dx < 0, dy < 0 -> -135 deg = 225 deg)
    alt = math.radians(42.0)
    slope_ang = np.arctan(slope)
    hs = np.sin(alt) * np.cos(slope_ang) + np.cos(alt) * np.sin(slope_ang) * np.cos(azimuth - aspect)
    hs = np.clip(hs, 0.0, 1.0)
    neutral = math.sin(alt)

    # Create RGBA hillshade image: warm sunlit highlights on NW faces, sepia umber shadows on SE faces
    rgba = np.zeros((H, W, 4), dtype=np.uint8)
    diff = hs - neutral
    # Shadow pixels (diff < 0): warm dark sepia (#2a1c0c)
    # Highlight pixels (diff > 0): warm parchment cream (#fff6e0)
    pos = np.clip(diff / (1.0 - neutral + 1e-6), 0.0, 1.0)
    neg = np.clip(-diff / (neutral + 1e-6), 0.0, 1.0)
    relief_mask = np.clip(Z * 2.2 + slope * 1.5, 0.0, 1.0)

    rgba[..., 0] = np.where(diff >= 0, 255, 42).astype(np.uint8)
    rgba[..., 1] = np.where(diff >= 0, 246, 28).astype(np.uint8)
    rgba[..., 2] = np.where(diff >= 0, 224, 12).astype(np.uint8)
    alpha = relief_mask * np.where(diff >= 0, pos * 68.0, neg * 115.0)
    rgba[..., 3] = np.clip(alpha, 0, 135).astype(np.uint8)

    tex_dir = SITE / "assets" / "textures"
    tex_dir.mkdir(parents=True, exist_ok=True)
    Image.fromarray(rgba, mode="RGBA").save(tex_dir / "hillshade.png", "PNG", optimize=True)

    # 4. Generate Topographic Contours + Lehmann Slope Hachures GeoJSON in plate coordinates
    data_dir = SITE / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    contour_features = []
    hachure_features = []

    # Parametric multi-tier contour rings & Lehmann hachures along the Silicon Range
    levels = [
        (0.22, "foothill", 0.45),
        (0.38, "lower-slope", 0.58),
        (0.54, "mid-contour", 0.72),
        (0.70, "index-contour", 0.86),
        (0.85, "summit-crest", 0.96),
    ]

    for s in summit_records:
        mx, my = s["x"], s["y"]
        sa_base, sb_base = s["sig_along"], s["sig_across"]
        ang = s["angle_rad"]
        ca, sa = math.cos(ang), math.sin(ang)
        peak = s["peak"]

        for idx_lvl, (lvl, kind, _) in enumerate(levels):
            if peak < (lvl - 0.15):
                continue
            scale_r = math.sqrt(max(0.08, -1.65 * math.log(min(0.94, lvl / (0.42 + 0.56 * peak)))))
            rx = sa_base * scale_r * 0.92
            ry = sb_base * scale_r * 0.85
            if rx < 2.2 or ry < 1.6:
                continue

            pts = []
            n_pts = 36
            seed = ( hash(s["name"]) % 997 ) * 0.013 + idx_lvl * 1.1
            for k in range(n_pts + 1):
                th = (k / n_pts) * 2.0 * math.pi
                # Natural geomorphological indentation (re-entrant gullies & spurs)
                wob = (
                    1.0
                    + 0.08 * math.cos(3.0 * th + seed)
                    + 0.05 * math.sin(5.0 * th - seed * 1.7)
                )
                u = rx * wob * math.cos(th)
                v = ry * wob * math.sin(th)
                px = mx + u * ca - v * sa
                py = my + u * sa + v * ca
                pts.append([round(px, 2), round(py, 2)])

            contour_features.append({
                "type": "Feature",
                "properties": {
                    "milestone": s["name"],
                    "level": lvl,
                    "kind": kind,
                    "index": idx_lvl in (1, 3, 4),
                    "year": s["year"],
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [pts],
                },
            })

            # Lehmann slope hachures radiating orthogonal to this contour ring toward the next lower ring
            if idx_lvl in (1, 2, 3, 4):
                n_hach = int(max(10, min(32, round((rx + ry) * 0.95))))
                for hk in range(n_hach):
                    th = (hk / n_hach) * 2.0 * math.pi + (idx_lvl * 0.27)
                    wob = 1.0 + 0.08 * math.cos(3.0 * th + seed) + 0.05 * math.sin(5.0 * th - seed * 1.7)
                    u0 = rx * wob * math.cos(th)
                    v0 = ry * wob * math.sin(th)
                    # Outward normal direction (downslope)
                    nx_loc = math.cos(th) / max(rx, 1.0)
                    ny_loc = math.sin(th) / max(ry, 1.0)
                    n_norm = math.hypot(nx_loc, ny_loc) or 1.0
                    nx_loc /= n_norm
                    ny_loc /= n_norm

                    hlen = (2.2 + 2.8 * peak) * (0.85 if idx_lvl == 4 else 1.15)
                    u1 = u0 + nx_loc * hlen
                    v1 = v0 + ny_loc * hlen

                    x_start = mx + u0 * ca - v0 * sa
                    y_start = my + u0 * sa + v0 * ca
                    x_end = mx + u1 * ca - v1 * sa
                    y_end = my + u1 * sa + v1 * ca

                    # World-space outward angle for NW (225°) vs SE (45°) Lehmann illumination weight
                    out_ang = math.atan2(y_end - y_start, x_end - x_start)
                    # SE shadow alignment in [-1, 1]: +1 when facing SE (45°), -1 when facing NW (-135°)
                    se_dot = math.cos(out_ang - math.radians(45.0))
                    weight = round(0.55 + 0.40 * se_dot, 3)

                    hachure_features.append({
                        "type": "Feature",
                        "properties": {
                            "milestone": s["name"],
                            "tier": idx_lvl,
                            "se_shade": round(se_dot, 3),
                            "weight": weight,
                        },
                        "geometry": {
                            "type": "LineString",
                            "coordinates": [[round(x_start, 2), round(y_start, 2)], [round(x_end, 2), round(y_end, 2)]],
                        },
                    })

    (data_dir / "contours.geojson").write_text(
        json.dumps({"type": "FeatureCollection", "summits": summit_records, "features": contour_features}, indent=1) + "\n",
        encoding="utf-8",
    )
    (data_dir / "hachures.geojson").write_text(
        json.dumps({"type": "FeatureCollection", "features": hachure_features}, indent=1) + "\n",
        encoding="utf-8",
    )
    print(
        f"build_dem.py: wrote site/assets/textures/hillshade.png ({W}x{H}), "
        f"{len(contour_features)} topographic contours, {len(hachure_features)} Lehmann hachures"
    )


if __name__ == "__main__":
    build_dem()
