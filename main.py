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

TEXT = """Every evening about now a small bird came to the gutter over the window and drank and left. She came in low over the yard, stopped for one swallow, and was gone before the water had finished moving. Then the water stilled, and the ledge kept its small dark place where she had been. She did this at the same minute every day and had never once looked in at the window. Some evenings the yard was loud with next door's radio; some evenings it was only the tap of her feet on the metal and then nothing. Later she would come back at dusk and be a shape on the wire. Later still she would not, and the ledge would hold the place for her either way. The day let go of its light a little at a time, and the water in the gutter went on being still."""

# Write bytes, not text mode: text mode would impose the platform's line ends
# and its default encoding, and the two runs must agree byte for byte.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as handle:
    handle.write(TEXT.encode("utf-8"))
