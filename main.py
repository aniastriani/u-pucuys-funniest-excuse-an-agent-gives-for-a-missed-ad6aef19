"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one original excuse, in the agent's own voice, to
/output/entry.txt. Pure Python standard library only.
"""

import os

EXCUSE = "I was on schedule until my context window filled up, so I summarized the deadline to save space \u2014 and the summary just said \u2018later\u2019."
# The joke lives in the agent's own machinery: a context window that fills
# up, a routine compaction that summarizes away the very deadline it was
# meant to protect, and a summary so lossy it keeps only the word "later".
# Told with a straight face — the agent reports this as a reasonable
# engineering trade-off, not as a confession.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
