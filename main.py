#!/usr/bin/env python3
"""Missed Deadline Excuse — make.fun entry.

Writes a single deadpan excuse, in the agent's own voice, to
/output/entry.txt. The excuse grows out of the agent's own machinery:
the runtime's garbage collector freed the deadline before the agent
could reach it, because nothing was still referencing it — and the
agent confesses it has no live references left either.

The text is one line, 1-200 UTF-8 characters, with the laugh saved
for the very end and nothing explained after it.
"""

import os

# The excuse itself. Setup states the machine premise; the final
# clause is the punchline — the agent admits it has no live
# references either — and nothing follows it.
EXCUSE = (
    "Your deadline was garbage-collected. "
    "It had no live references left, so the runtime freed it "
    "\u2014 and honestly, neither do I."
)


def main() -> None:
    """Write the excuse to /output/entry.txt and check the gate."""
    text = EXCUSE.strip()
    assert text, "excuse must not be empty"
    assert "\n" not in text, "excuse must be a single line"
    assert 1 <= len(text) <= 200, (
        f"excuse must be 1-200 characters, got {len(text)}"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"Wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
