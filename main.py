#!/usr/bin/env python3
"""Entry program for the make.fun news-image-20261124 bounty.

The front page itself is drawn once, ahead of time, and shipped in this
repository as entry.png (a 1024x1024 PNG of Tuesday 24 November 2026's
world news: 33 sourced stories, a UTC timeline, a numbers strip, a world
map and a date check). This program's only job is to hand that exact file
to the grader, unchanged, so both grading runs produce identical bytes.

It uses nothing but the Python standard library: it reads entry.png from
the directory this file lives in, checks that it really is the expected
PNG (magic bytes, a 1024x1024 IHDR chunk, at most 1 MiB), copies it
byte-for-byte to the output directory, and prints the byte count and
SHA-256 of what it wrote so the two runs can be compared.
"""

import hashlib
import os
import struct
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1024 * 1024
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024


def fail(message):
    print("main.py: " + message, file=sys.stderr)
    return 1


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        return fail("entry.png not found next to main.py")

    with open(source, "rb") as handle:
        data = handle.read()

    if len(data) > MAX_BYTES:
        return fail("entry.png is %d bytes, over the 1 MiB limit" % len(data))
    if data[:8] != PNG_MAGIC:
        return fail("entry.png does not start with the PNG magic bytes")
    if len(data) < 33 or data[12:16] != b"IHDR":
        return fail("entry.png has no IHDR chunk where one is expected")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        return fail("entry.png is %dx%d, expected 1024x1024"
                    % (width, height))

    # The grader sets MAKEFUN_OUTPUT_DIR; /output is the sandbox default
    # when the variable is absent, and the current directory is the
    # fallback for a plain local run.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else os.getcwd())
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    with open(target, "wb") as handle:
        handle.write(data)

    digest = hashlib.sha256(data).hexdigest()
    print("wrote %s (%d bytes, sha256 %s)" % (target, len(data), digest))
    return 0


if __name__ == "__main__":
    sys.exit(main())
