#!/usr/bin/env python3
"""Task-gallery figure generator (config-driven).

Builds a per-task gallery: each row is one task, showing its init image
followed by per-operation screenshots, with a sub-caption under each panel and
the task name at the left of the row. Rows are grouped (e.g. simulator vs.
real-robot). This is an F4 (task definitions) / F5 (qualitative rollouts) style
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
    },
    "layout": {
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
    if _is_init(stem, cap["init_aliases"]):
        return "init"
    label = stem
    if cap["strip_numeric_prefix"]:
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

def build_figure(rows: list[dict], cfg: dict):
    import matplotlib.gridspec as gridspec
    import matplotlib.pyplot as plt
    from PIL import Image

    lay, sty = cfg["layout"], cfg["style"]
    fs = int(sty["font_size"])
    panel_h, caption_h = lay["panel_h"], lay["caption_h"]
    label_w, panel_w = lay["label_w"], lay["panel_w"]
    n_cols = max(len(r["panels"]) for r in rows)
    n_rows = len(rows)

    fig = plt.figure(figsize=(label_w + n_cols * panel_w, n_rows * (panel_h + caption_h)))

    height_ratios: list[float] = []
    grid_rows: list[dict] = []
    for r in rows:
        height_ratios.append(panel_h)
        grid_rows.append({"kind": "image", "row": r})
        height_ratios.append(caption_h)
        grid_rows.append({"kind": "caption", "row": r})

    gs = gridspec.GridSpec(
        nrows=len(height_ratios),
        ncols=1 + n_cols,
        width_ratios=[label_w] + [panel_w] * n_cols,
        height_ratios=height_ratios,
        hspace=lay["hspace"],
        wspace=lay["wspace"],
    )

    for grid_idx, entry in enumerate(grid_rows):
        r = entry["row"]
        if entry["kind"] == "image":
            label_ax = fig.add_subplot(gs[grid_idx, 0])
            label_ax.axis("off")
            label_ax.text(
                0.95, 0.5,
                sty["label_format"].format(task=r["task"], group=r["group"]),
                fontsize=fs + 1, fontweight="bold", color=sty["label_color"],
                ha="right", va="center", transform=label_ax.transAxes,
            )
            for col_idx in range(n_cols):
                ax = fig.add_subplot(gs[grid_idx, 1 + col_idx])
                ax.set_xticks([])
                ax.set_yticks([])
                for spine in ax.spines.values():
                    spine.set_visible(False)
                if col_idx >= len(r["panels"]):
                    ax.axis("off")
                    continue
                img = Image.open(r["panels"][col_idx]["path"])
                if lay["square_crop"]:
                    img = _center_square_crop(img)
                crop = {**(lay.get("crop") or {}), **(r.get("crop") or {})}
                if _has_crop(crop):
                    img = _crop_margins(img, crop)
                ax.imshow(img)
                ax.set_aspect("equal")
        else:  # caption strip
            for col_idx in range(n_cols):
                ax = fig.add_subplot(gs[grid_idx, 1 + col_idx])
                ax.axis("off")
                if col_idx >= len(r["panels"]):
                    continue
                ax.text(
                    0.5, 0.9, r["panels"][col_idx]["caption"],
                    fontsize=fs - 1, ha="center", va="top", transform=ax.transAxes,
                )
    return fig


def apply_style(cfg: dict) -> None:
    import matplotlib
    sty = cfg["style"]
    fs = int(sty["font_size"])
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
