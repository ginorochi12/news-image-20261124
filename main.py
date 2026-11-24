"""Write this entry's image where the harness expects it.

Reads entry.png next to this file, checks the PNG signature, and places a
copy at $MAKEFUN_OUTPUT_DIR/entry.png. Exits nonzero on a bad signature so a
damaged image never reaches the judge.
"""
from pathlib import Path
import os, sys

SIGNATURE = bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])


def run():
    source = Path(__file__).resolve().parent / "entry.png"
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    data = source.read_bytes()
    if data[:8] != SIGNATURE:
        sys.stderr.write("entry.png: bad PNG signature\n")
        raise SystemExit(1)
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "entry.png").write_bytes(data)


run()
