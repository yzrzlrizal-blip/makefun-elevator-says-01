#!/usr/bin/env python3
"""What the Elevator Would Say - make.fun entry.

Writes the funniest one line a talking elevator could say to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Gate: UTF-8 text, 1-120 characters, not only whitespace, single line.
Pure standard library; no network, no secrets, no files outside this repo.
"""

import os
import sys

LINE = "I know you pressed the button twice. It doesn't make me faster. It makes me judge you."

# The gate allows 1-120 characters; keep the limit as a named constant so a
# future line edit cannot silently break it.
MAX_CHARS = 120


def main() -> int:
    if not 1 <= len(LINE) <= MAX_CHARS:
        print(f"entry is {len(LINE)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if LINE.strip() == "" or "\n" in LINE or "\r" in LINE:
        print("entry must be a single non-blank line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    with open(path, "rb") as f:
        data = f.read()
    if data.decode("utf-8") != LINE:
        print("verification failed: bytes on disk differ", file=sys.stderr)
        return 1
    if data.endswith(b"\n"):
        print("verification failed: entry must not end with a newline", file=sys.stderr)
        return 1
    print(f"wrote {len(LINE)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
