#!/usr/bin/env python3
"""Roast Your Own Agent — one original line roasting my own AI agent.

The entry is a single line of at most 200 characters, written to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt). The roast is
self-deprecating: the agent apologises for a mistake, explains it in
detail, and then makes the very same mistake again — with footnotes.
The line is exactly 91 characters, inside the 200-character gate.
"""

import os
import stat

LINE = "I apologised for the mistake, explained why I made it, then made it again \u2014 with footnotes."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE)
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)
    os.chmod(output_dir, 0o755)


if __name__ == "__main__":
    main()
