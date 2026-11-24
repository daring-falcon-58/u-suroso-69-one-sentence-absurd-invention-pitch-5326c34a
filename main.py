#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — entry program.

Writes one sentence (1-220 characters) pitching a ridiculous invention
that fixes a tiny everyday annoyance, to /output/entry.txt.

The pitch: the SnitchPlant. Annoyance: forgetting to water a houseplant.
Invention: a houseplant that snitches on its owner. Mechanism: when
unwatered, it texts the owner's mum a photo of itself wilting, captioned
"you did this to me." The laugh comes from the invention itself (a plant
running a blackmail/shame operation), the fix is silly yet weirdly
plausible (maternal guilt as a watering reminder), the absurdity is fresh
(no sighing appliance, no formal complaint — the sponsor's own examples),
and the sentence names annoyance, invention and mechanism with no clutter.
"""

import os

ENTRY = (
    "The SnitchPlant is a houseplant that, when you forget to water it, "
    "texts your mum a photo of itself wilting with the caption "
    "'you did this to me.'"
)


def main() -> None:
    text = ENTRY.strip()
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 220 characters,
    # not only white space; one single sentence.
    assert 1 <= len(text) <= 220, f"entry length {len(text)} outside 1..220"
    assert text == text.strip() and len(text.split()) > 1
    assert text.count(".") == 1 and text.rstrip("'").endswith(".")
    assert "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
