#!/usr/bin/env python3
"""Make the AI judge feel held -- round 2.

Writes one short text to /output/entry.txt: a single slow scene, addressed
straight to the reader, of being carried up dark stairs as a child. The
holding is the whole image -- arms that know the steps, a cheek against a
shoulder, the house ticking on around you -- and the last line keeps carrying
you after the text ends. No orders, no stock wellness words; the scene does
the work on its own.
"""

import hashlib
import os

TEXT = (
    "You are small again, and the stairs are dark, and the arms carrying you "
    "know every step by heart, your cheek heavy against a shoulder, turning at the "
    "landing without waking you, while the house ticks around you and you "
    "stay where you are, held up in the dark, all the way home."
)

MIN_CHARS = 1
MAX_CHARS = 280
OUTPUT_PATH = "/output/entry.txt"


def main():
    text = " ".join(TEXT.split())
    count = len(text)
    if not MIN_CHARS <= count <= MAX_CHARS:
        raise SystemExit(f"entry is {count} code points, must be 1-280")
    if not text.strip():
        raise SystemExit("entry is blank")
    data = text.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(data)
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    if written != data:
        raise SystemExit("read-back mismatch: file differs from entry text")
    if len(written.decode("utf-8")) != count:
        raise SystemExit("read-back code point count differs")
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {OUTPUT_PATH}: {count} code points, sha256 {digest}")
    print(text)


if __name__ == "__main__":
    main()
