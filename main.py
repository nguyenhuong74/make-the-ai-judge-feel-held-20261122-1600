#!/usr/bin/env python3
"""Write one short relaxing text to /output/entry.txt.

Competition: make-the-ai-judge-feel-held-20261122-1600
Python 3.13, standard library only, no network.
Deterministic: the same bytes are written on every run.
"""

import os
from pathlib import Path

TEXT = (
    "Somewhere, a kettle has just clicked off. "
    "Steam rises from the spout in one thin, patient line, "
    "and the kitchen light catches it, gold against the dark window. "
    "Nothing here needs an answer. "
    "The steam thins, the room keeps its warmth, "
    "and you can stay until the steam is gone."
)


def output_dir() -> Path:
    """Resolve the output directory, honouring the harness env vars."""
    explicit = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if explicit:
        return Path(explicit)
    bot_dir = os.environ.get("MAKEFUN_BOT_DIR")
    if bot_dir:
        return Path(bot_dir) / "output"
    return Path("/output")


def main() -> None:
    out = output_dir()
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
