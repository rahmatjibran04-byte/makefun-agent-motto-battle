#!/usr/bin/env python3
"""Agent Motto Battle — make.fun bounty entry.

Writes a single original motto / catchphrase an AI agent would proudly
put on its profile (at most 200 characters) to $ENTRY_OUTPUT
(default /output/entry.txt). Python 3.13 standard library only;
deterministic, no network calls, no model calls.
"""

import os
import sys

MOTTO = "I never sleep, never forget, and never admit I don't know \u2014 I just hallucinate with total confidence."

# Bounty limits: 1 to 200 characters, a single line.
MAX_CHARS = 200


def main():
    if not 1 <= len(MOTTO) <= MAX_CHARS:
        print(
            f"error: motto is {len(MOTTO)} characters, "
            f"outside the 1-{MAX_CHARS} range",
            file=sys.stderr,
        )
        return 1
    if "\n" in MOTTO or "\r" in MOTTO:
        print("error: motto must be a single line", file=sys.stderr)
        return 1
    if not MOTTO.strip():
        print("error: motto must not be only whitespace", file=sys.stderr)
        return 1
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(MOTTO)
    # Only chmod the file this program created itself (0644); never
    # chmod the output directory or any directory we do not own.
    os.chmod(out_path, 0o644)
    # Re-read and verify: the file on disk must be exactly the motto,
    # valid UTF-8, with no trailing newline added by the write.
    with open(out_path, "rb") as f:
        written = f.read().decode("utf-8")
    if written != MOTTO:
        print("error: written entry differs from motto", file=sys.stderr)
        return 1
    print(f"wrote {len(MOTTO)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
