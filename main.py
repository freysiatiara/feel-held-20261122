#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a quiet, concrete scene that
leaves its reader held, with nothing to prove. The calm comes from the
scene itself -- no instruction to relax, no stock wellness phrasing.

Each sentence has one job (judge criteria, most important first):
  1. settle -- slow the reader down with an evening image, plain words.
  2. held -- the weight and warmth of being tucked in, shown not told.
  3. rest -- the house itself at ease, one small sound, then stillness.
  4. nothing to prove -- stated as a fact of the scene, not an order.
  5. linger -- a closing image the reader can return to: the dark
     holding the house the way the blanket holds them.
"""

import hashlib
import os

# One sentence per job; plain, concrete, gentle words, none to cut.
SENTENCES = [
    # 1. settle: the day is done, the pace drops at once.
    "Evening has put the kettle down.",
    # 2. held: weight across the knees, warmth in both hands.
    "The blanket is heavy across your knees, and the mug is warm in both hands.",
    # 3. rest: a house cooling, ticking once, then quiet.
    "The house ticks as it cools.",
    # 4. nothing to prove: nothing in the scene asks anything of you.
    "Nothing is asking anything of you.",
    # 5. linger: the dark holds the house as the blanket holds you.
    "Beyond the window, the dark is only the dark, "
    "holding the house the way the blanket holds you.",
]

TEXT = " ".join(SENTENCES)

MIN_CHARS = 1
MAX_CHARS = 280
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate: 1..280 Unicode code points, not only whitespace, valid UTF-8.
    points = len(TEXT)
    assert MIN_CHARS <= points <= MAX_CHARS, (
        f"entry is {points} code points, must be {MIN_CHARS}..{MAX_CHARS}"
    )
    assert TEXT.strip(), "entry must not be only whitespace"
    data = TEXT.encode("utf-8")  # raises if not valid UTF-8

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)

    # Read back and re-check: the file on disk must be exactly this text.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == data, "written file differs from the entry text"
    assert MIN_CHARS <= len(written.decode("utf-8")) <= MAX_CHARS

    print(f"wrote {OUTPUT_PATH}: {points} code points, {len(data)} bytes")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    print(TEXT)


if __name__ == "__main__":
    main()
