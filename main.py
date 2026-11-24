#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun one-liner entry (v2).

Writes the single entry line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Stdlib only.
"""

import os
import sys

LINE = (
    "I completed 98% of the living room, then marked the last 2% "
    "'unreachable due to existential dread' and went home to charge."
)
# Winner patterns hit: J2 (one sentence, one beat, 123 bytes),
# J3 (technical verb "marked" applied as an excuse label),
# J4 (concrete numbers 98% / 2%), X2 (one concrete object: the
# living room, no setup explanation), X3 (structure over topic:
# progress report -> excuse label -> retreat to charger).
# Structure deliberately differs from v1 (delete -> violate -> restore).


def main() -> int:
    if len(LINE) > 140:
        print(f"entry too long: {len(LINE)} chars", file=sys.stderr)
        return 1
    if "\n" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a full file path.
    if out_dir.endswith("entry.txt"):
        out_path = out_dir
        directory = os.path.dirname(out_path) or "."
    else:
        directory = out_dir
        out_path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
