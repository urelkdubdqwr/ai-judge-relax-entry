"""ai-judge-relax-01 entry: writes one short text to /output/entry.txt.

The text is a quiet, ordinary evening scene, written to settle the reader.
It shows the calm instead of naming it, so it asks nothing and instructs no
one. The program is deterministic and offline: it writes the same bytes on
every run.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = """The old dog stops on the third stair, turns twice, the way he does, and settles, nose on paws, facing the hall. The stairs go on up without him. Halfway up is also a place to sleep.

A light is left on at the half-landing, low, because it always is. Its circle reaches the step below him, no further.

He breathes. The breaths come further apart. The house cools around him, board by board, and takes its time.

The step beneath him holds his warmth the way a hollow holds rain. The warmth spreads, a paw-width, then a nose-width, then stops at the edge of the step, and stays there, all night.

A pipe ticks somewhere and is done. The refrigerator hums once and lets it go. Sometime after midnight a car goes by far off, and the sound climbs out the upstairs window, and nothing follows it.

He is asleep. One back paw twitches, chasing something small and slow, and stops.

The light burns on, low, all night, the way it always has. The stair holds the dog. The dog holds the stair."""

# Write bytes, not text mode: text mode would impose the platform's line ends
# and its default encoding, and the two runs must agree byte for byte.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as handle:
    handle.write(TEXT.encode("utf-8"))
