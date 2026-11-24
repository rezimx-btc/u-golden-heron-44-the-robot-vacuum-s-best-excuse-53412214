#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun one-liner entry.

Writes the chosen one-line excuse (140 characters max) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only.
"""

import os
import sys

LINE = (
    "I deleted 'under the couch' from my map, cleaned around it anyway, "
    "then restored it \u2014 the dust bunny is now a protected landmark."
)


def main() -> int:
    if len(LINE) > 140:
        print("entry exceeds 140 characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR is a directory; a bare filename would be ambiguous,
    # so treat a value ending in .txt as a file path, else join entry.txt.
    if out_dir.endswith(".txt"):
        path = out_dir
    else:
        path = os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
