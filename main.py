#!/usr/bin/env python3
"""Two Lines to Your Past Self - make.fun bounty entry.

Writes exactly two lines to /output/entry.txt:
  line 1 warns the writer's past self about one specific moment;
  line 2 says in one sentence why that moment mattered and what
  changed because of it.

Deterministic, Python standard library only, no network, no input.
"""

import os
import sys

LINE_1 = (
    "At the kitchen table on your eighteenth birthday, when Dad says "
    "'stay, we need you here,' don't nod, buy the ticket anyway."
)

LINE_2 = (
    "That nod would have kept you in that town for ten more years, "
    "and every door you wanted only opened once you finally left."
)

TEXT = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> int:
    # Gate check, mirroring the bounty rules: UTF-8 text of 1 to 280
    # characters, not only white space, exactly two lines.
    if not 1 <= len(TEXT) <= 280:
        print(f"entry is {len(TEXT)} characters, must be 1-280",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    if len(TEXT.strip().splitlines()) != 2:
        print("entry must be exactly two lines", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8",
              newline="\n") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
