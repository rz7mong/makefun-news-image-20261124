#!/usr/bin/env python3
"""Copy the built entry.png to $MAKEFUN_OUTPUT_DIR (default /output).

Stdlib only, no network. Run after gen_image.py has produced entry.png
in this directory.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
