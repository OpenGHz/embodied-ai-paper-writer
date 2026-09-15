#!/usr/bin/env python3
"""Task-gallery figure generator (config-driven).

Builds a per-task gallery: each row is one task, showing its init image
followed by per-operation screenshots, with a sub-caption under each panel and
the task name above or at the left of the row. Rows are grouped (e.g. simulator vs.
real-robot). Set layout.group_columns to 2 to place groups side by side with
group labels above or below; groups follow first appearance in rows and wrap
as needed. Task/group label positions and font sizes are independently configurable.
This is an F4 (task definitions) / F5 (qualitative rollouts) style
figure — see references/figures-tables-playbook.md.

ALL configuration lives in a YAML file (rows, paths, layout, style, captions,
output) — nothing paper-specific is hard-coded here. Copy
tools/task_gallery.example.yaml, edit it, then:

    python3 tools/task_gallery_figure.py --config task_gallery.yaml --workspace <paper-dir>

Image directories in the config are resolved relative to --workspace (default:
current working directory). Outputs are written to <workspace>/<output.dir>.

Requires: matplotlib, Pillow, PyYAML (beyond the standard library).
"""
from __future__ import annotations

import argparse
import fnmatch
import math
import os
import re
import sys
from pathlib import Path
from typing import Any

# This is a headless figure generator (saves files, opens no window), so pin a
# non-interactive backend before matplotlib is ever imported. Avoids the noisy
# "QFileSystemWatcher::removePaths: list is empty" warnings a Qt backend prints
# on cleanup. `setdefault` lets a caller still override via MPLBACKEND.
os.environ.setdefault("MPLBACKEND", "Agg")

try:
    import yaml
except ModuleNotFoundError:
    sys.stderr.write("error: PyYAML is required (pip install pyyaml)\n")
    raise SystemExit(1)


# --------------------------------------------------------------------------- #
# Config
# --------------------------------------------------------------------------- #

DEFAULTS: dict[str, Any] = {
    "output": {"name": "task_gallery", "dir": "figures", "formats": ["pdf"], "dpi": 300},
    "style": {
        "font_size": 10,
        "font_family": "sans-serif",
        # Preferred fonts, in order; the last should be an always-present fallback
        # (DejaVu Sans/Serif ship with matplotlib) so the figure still renders in
        # the right family even when the named fonts are not installed.
        "font_names": ["Arial", "Helvetica", "DejaVu Sans"],
        "label_color": "#000000",
        "label_format": "{task} ({group})",
        "task_font_size": None,  # defaults to font_size + 1
        "caption_font_size": None,  # defaults to font_size - 1
        "group_font_size": None,  # defaults to font_size + 2
        "group_label_format": "{group}",  # also accepts {letter} and {index}
        "caption_color": "#000000",
        "panel_border_color": "#D7DCE1",
        "panel_border_width": 0,
    },
    "layout": {
        "group_columns": 1,
        "group_gap": 0.35,
        "group_title_h": 0.3,
        "group_title_position": "top",
        "task_label_position": "left",
        "task_label_h": 0.24,
        "row_gap": 0,
        "panel_h": 1.55,
        "caption_h": 0.18,
        "label_w": 1.15,
        "panel_w": 1.85,
        "hspace": 0.05,
        "wspace": 0.08,
        "square_crop": True,
        # Fractional trim per side (0..1), applied AFTER square_crop so panels
        # stay a uniform aspect. e.g. {"top": 0.2} drops the top 20% of every
        # panel. Per-row `crop:` overrides this globally-set default.
        "crop": {"top": 0.0, "bottom": 0.0, "left": 0.0, "right": 0.0},
    },
    "captions": {
        "init_aliases": ["init", "0_init"],
        "strip_numeric_prefix": True,
        "rename": {},
        "separator": "",  # e.g. a right arrow between operation captions
    },
    "image_extensions": [".png", ".jpg", ".jpeg"],
    "rows": [],
}


def _merge(base: dict, over: dict) -> dict:
    """Shallow-merge per top-level key (one level deep for dict values)."""
    out = {k: (dict(v) if isinstance(v, dict) else v) for k, v in base.items()}
    for k, v in over.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = {**out[k], **v}
        else:
            out[k] = v
    return out


def load_config(path: Path) -> dict:
    raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    cfg = _merge(DEFAULTS, raw)
    if not cfg["rows"]:
        raise SystemExit(f"error: config {path} has no `rows`")
    columns = cfg["layout"]["group_columns"]
    if type(columns) is not int or columns < 1:
        raise SystemExit("error: layout.group_columns must be a positive integer")
    for key in ("group_gap", "group_title_h", "task_label_h", "row_gap"):
        value = cfg["layout"][key]
        if (isinstance(value, bool) or not isinstance(value, (int, float))
                or not math.isfinite(value) or value < 0):
            raise SystemExit(f"error: layout.{key} must be a finite non-negative number")
    for key in ("group_title_h", "task_label_h"):
        if cfg["layout"][key] == 0:
            raise SystemExit(f"error: layout.{key} must be positive")
    for key, choices in (("group_title_position", ("top", "bottom")),
                         ("task_label_position", ("left", "top"))):
        if cfg["layout"][key] not in choices:
            raise SystemExit(f"error: layout.{key} must be one of {choices}")
    for key in ("task_font_size", "caption_font_size", "group_font_size"):
        value = cfg["style"][key]
        if value is not None and (
            isinstance(value, bool) or not isinstance(value, (int, float))
            or not math.isfinite(value) or value <= 0
        ):
            raise SystemExit(f"error: style.{key} must be a finite positive number or null")
    return cfg


# --------------------------------------------------------------------------- #
# Filename -> caption / ordering
# --------------------------------------------------------------------------- #

def _strip_ext(name: str) -> str:
    # Some files are doubly-suffixed (".mp4.png") — drop all trailing extensions.
    stem = name
    while True:
        new_stem, ext = os.path.splitext(stem)
        if not ext:
            return stem
        stem = new_stem


def _is_init(stem: str, init_aliases: list[str]) -> bool:
    lower = stem.lower()
    if lower in {a.lower() for a in init_aliases}:
        return True
    if lower.endswith("_init"):
        return True
    return False


def caption_for(filename: str, cfg: dict) -> str:
    cap = cfg["captions"]
    stem = _strip_ext(filename)
    is_init = _is_init(stem, cap["init_aliases"])
    label = "init" if is_init else stem
    if cap["strip_numeric_prefix"] and not is_init:
        match = re.match(r"^\d+_(.+)$", stem)
        label = match.group(1) if match else stem
    label = label.replace("_", " ").replace("-", " ").strip()
    rename = {k.lower(): v for k, v in (cap["rename"] or {}).items()}
    return rename.get(label.lower(), label)


def sort_key(filename: str, init_aliases: list[str]) -> tuple[int, int, str]:
    """Return (group, prefix, name) — init first, then numeric prefix."""
    stem = _strip_ext(filename)
    if _is_init(stem, init_aliases):
        match = re.match(r"^(\d+)_", stem)
        return (0, int(match.group(1)) if match else -1, stem)
    match = re.match(r"^(\d+)_(.+)$", stem)
    if match:
        return (1, int(match.group(1)), stem)
    return (1, 9999, stem)


# --------------------------------------------------------------------------- #
# Panels
# --------------------------------------------------------------------------- #

def collect_panels(cfg: dict, base: Path) -> list[dict]:
    exts = tuple(e.lower() for e in cfg["image_extensions"])
    init_aliases = cfg["captions"]["init_aliases"]
    rows = []
    for row in cfg["rows"]:
        row_dir = (base / row["dir"]).resolve()
        if not row_dir.is_dir():
            raise SystemExit(f"error: image dir not found for task '{row.get('task')}': {row_dir}")
        # Per-row exclude: list of filename glob patterns to drop (e.g. failure
        # frames that belong in an F8 figure, not the task gallery).
        exclude = row.get("exclude") or []
        files = sorted(
            [
                f
                for f in os.listdir(row_dir)
                if f.lower().endswith(exts)
                and not any(fnmatch.fnmatch(f, pat) for pat in exclude)
            ],
            key=lambda f: sort_key(f, init_aliases),
        )
        if not files:
            raise SystemExit(f"error: no images ({', '.join(exts)}) in {row_dir}")
        panels = [{"path": row_dir / f, "caption": caption_for(f, cfg)} for f in files]
        rows.append({**row, "panels": panels})
    return rows


def _center_square_crop(img):
    w, h = img.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    return img.crop((left, top, left + side, top + side))


def _crop_margins(img, m: dict):
    """Trim fractional margins (0..1 per side) from an image."""
    w, h = img.size
    left = int(round(w * float(m.get("left", 0) or 0)))
    right = int(round(w * float(m.get("right", 0) or 0)))
    top = int(round(h * float(m.get("top", 0) or 0)))
    bottom = int(round(h * float(m.get("bottom", 0) or 0)))
    box = (left, top, max(left + 1, w - right), max(top + 1, h - bottom))
    return img.crop(box)


def _has_crop(m: dict) -> bool:
    return any(float(m.get(k, 0) or 0) > 0 for k in ("top", "bottom", "left", "right"))


# --------------------------------------------------------------------------- #
# Figure
# --------------------------------------------------------------------------- #

def _font_size(style: dict, role: str) -> float:
    value = style[f"{role}_font_size"]
    return float(value if value is not None else style["font_size"] + {
        "task": 1, "caption": -1, "group": 2,
    }[role])


def _panel_letter(index: int) -> str:
    """Zero-based alphabetic panel labels, including aa after z."""
    label = ""
    while index >= 0:
        index, remainder = divmod(index, 26)
        label = chr(ord("a") + remainder) + label
        index -= 1
    return label


def _draw_task_row(fig, gs, grid_idx: int, row: dict, cfg: dict) -> None:
    """Draw one task using the same panel/caption path in every layout."""
    from PIL import Image

    lay, sty = cfg["layout"], cfg["style"]
    label_above = lay["task_label_position"] == "top"
    image_idx = grid_idx + int(label_above)
    col_offset = 0 if label_above else 1
    label_ax = fig.add_subplot(gs[grid_idx, :] if label_above else gs[grid_idx, 0])
    label_ax.axis("off")
    label_ax.text(
        0 if label_above else 0.95, 0.5,
        sty["label_format"].format(task=row["task"], group=row["group"]),
        fontsize=_font_size(sty, "task"), fontweight="bold", color=sty["label_color"],
        ha="left" if label_above else "right", va="center", transform=label_ax.transAxes,
    )
    caption_axes = []
    for col_idx, panel in enumerate(row["panels"], start=col_offset):
        ax = fig.add_subplot(gs[image_idx, col_idx])
        ax.set_xticks([])
        ax.set_yticks([])
        for spine in ax.spines.values():
            spine.set_visible(sty["panel_border_width"] > 0)
            spine.set_edgecolor(sty["panel_border_color"])
            spine.set_linewidth(sty["panel_border_width"])
        with Image.open(panel["path"]) as source:
            img = source.copy()
        if lay["square_crop"]:
            img = _center_square_crop(img)
        crop = {**(lay.get("crop") or {}), **(row.get("crop") or {})}
        if _has_crop(crop):
            img = _crop_margins(img, crop)
        ax.imshow(img)
        ax.set_aspect("equal")

        caption_ax = fig.add_subplot(gs[image_idx + 1, col_idx])
        caption_ax.axis("off")
        caption_ax.text(
            0.5, 0.9, panel["caption"],
            fontsize=_font_size(sty, "caption"), color=sty["caption_color"],
            ha="center", va="top", transform=caption_ax.transAxes,
        )
        caption_axes.append(caption_ax)
    if cfg["captions"]["separator"]:
        for left, right in zip(caption_axes, caption_axes[1:]):
            a, b = left.get_position(), right.get_position()
            fig.text(
                (a.x1 + b.x0) / 2, a.y0 + 0.9 * a.height,
                cfg["captions"]["separator"],
                fontsize=_font_size(sty, "caption"), color=sty["caption_color"],
                ha="center", va="top",
            )


def build_figure(rows: list[dict], cfg: dict):
    import matplotlib.gridspec as gridspec
    import matplotlib.pyplot as plt

    lay, sty = cfg["layout"], cfg["style"]
    panel_h, caption_h = lay["panel_h"], lay["caption_h"]
    label_w, panel_w = lay["label_w"], lay["panel_w"]
    label_above = lay["task_label_position"] == "top"
    task_heights = ([lay["task_label_h"]] if label_above else []) + [panel_h, caption_h]
    n_cols = max(len(r["panels"]) for r in rows)
    grouped = lay["group_columns"] > 1
    if grouped:
        groups: dict[str, list[dict]] = {}
        for row in rows:
            groups.setdefault(row["group"], []).append(row)
        blocks = list(groups.items())
    else:
        blocks = [(None, rows)]

    block_cols = min(lay["group_columns"], len(blocks))
    bands = [blocks[i:i + block_cols] for i in range(0, len(blocks), block_cols)]
    band_rows = [max(len(tasks) for _, tasks in band) for band in bands]
    title_h = lay["group_title_h"] if grouped else 0
    heights = [title_h + count * sum(task_heights) + (count - 1) * lay["row_gap"]
               for count in band_rows]
    widths = ([] if label_above else [label_w]) + [panel_w] * n_cols
    block_w = sum(widths)
    gap = lay["group_gap"]
    fig = plt.figure(figsize=(
        block_cols * block_w + (block_cols - 1) * gap,
        sum(heights) + (len(bands) - 1) * gap,
    ))
    outer = gridspec.GridSpec(
        nrows=len(bands), ncols=block_cols, figure=fig,
        height_ratios=heights,
        hspace=gap / (sum(heights) / len(heights)), wspace=gap / block_w,
    )

    for band_idx, band in enumerate(bands):
        # Pad shorter groups with empty slots so their task rows align at the top
        # and every group in the band uses identical panel sizes.
        title_on_top = grouped and lay["group_title_position"] == "top"
        ratios = [title_h] if title_on_top else []
        task_starts = []
        for task_idx in range(band_rows[band_idx]):
            if task_idx and lay["row_gap"]:
                ratios.append(lay["row_gap"])
            task_starts.append(len(ratios))
            ratios.extend(task_heights)
        if grouped and not title_on_top:
            ratios.append(title_h)
        for block_idx, (group, tasks) in enumerate(band):
            gs = outer[band_idx, block_idx].subgridspec(
                nrows=len(ratios), ncols=len(widths),
                width_ratios=widths,
                height_ratios=ratios, hspace=lay["hspace"], wspace=lay["wspace"],
            )
            if grouped:
                title_ax = fig.add_subplot(gs[0 if title_on_top else -1, :])
                title_ax.axis("off")
                group_idx = band_idx * block_cols + block_idx
                title_ax.text(
                    0.5, 0.5, sty["group_label_format"].format(
                        group=group, letter=_panel_letter(group_idx), index=group_idx + 1,
                    ), fontsize=_font_size(sty, "group"),
                    fontweight="bold" if title_on_top else "normal", color=sty["label_color"],
                    ha="center", va="center", transform=title_ax.transAxes,
                )
            for task_idx, row in enumerate(tasks):
                _draw_task_row(fig, gs, task_starts[task_idx], row, cfg)
    return fig


def apply_style(cfg: dict) -> None:
    import matplotlib
    sty = cfg["style"]
    fs = float(sty["font_size"])
    family = sty["font_family"]
    # Register the preferred font list under the rc key that matches the family,
    # so `font.family: sans-serif` actually consults `font.sans-serif`.
    family_key = "font.sans-serif" if family == "sans-serif" else "font.serif"
    rc = {
        "font.size": fs,
        "font.family": family,
        family_key: sty["font_names"],
        "figure.dpi": cfg["output"]["dpi"],
        "savefig.dpi": cfg["output"]["dpi"],
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.04,
        "axes.grid": False,
        "text.usetex": False,
        # Match math glyphs to the family (sans-serif math when the text is sans).
        "mathtext.fontset": "stixsans" if family == "sans-serif" else "stix",
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
    }
    matplotlib.rcParams.update(rc)


def save_fig(fig, out_dir: Path, name: str, formats: list[str]) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for fmt in formats:
        path = out_dir / f"{name}.{fmt}"
        fig.savefig(path)
        written.append(path)
        print(f"saved {path}")
    return written


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True, help="Path to the task-gallery YAML config")
    parser.add_argument("--workspace", help="Base dir for image paths + output (default: CWD)")
    args = parser.parse_args(argv)

    cfg = load_config(Path(args.config).expanduser())
    base = Path(args.workspace).expanduser().resolve() if args.workspace else Path.cwd()

    apply_style(cfg)
    rows = collect_panels(cfg, base)

    import matplotlib.pyplot as plt
    fig = build_figure(rows, cfg)
    out_dir = (base / cfg["output"]["dir"]).resolve()
    save_fig(fig, out_dir, cfg["output"]["name"], cfg["output"]["formats"])
    plt.close(fig)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
