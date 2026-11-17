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

TEXT = """The old dog stops on the third stair and thinks about it.

The stairs go on up without him. He turns around, twice, the way he does, and settles where he is, nose on paws, facing the hall.

The house rearranges itself around the decision. A light is left on at the half-landing, low, for whenever he changes his mind. The kettle is filled for the morning and set on the cold plate so it will not tick in the night.

Upstairs a floorboard settles. He does not look up.

He is asleep before anyone decides anything. One back paw twitches, chasing something small and slow. Halfway up is also a place to sleep."""

# Write bytes, not text mode: text mode would impose the platform's line ends
# and its default encoding, and the two runs must agree byte for byte.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as handle:
    handle.write(TEXT.encode("utf-8"))
