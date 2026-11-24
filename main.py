#!/usr/bin/env python3
"""Copy the entry image to the harness output directory.

Validates that entry.png is a real PNG (magic bytes) before copying, so a
corrupt or missing image fails loudly instead of submitting bad bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as f:
        head = f.read(len(PNG_MAGIC))
    if head != PNG_MAGIC:
        print("entry.png is not a valid PNG", file=sys.stderr)
        sys.exit(1)
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
