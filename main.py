#!/usr/bin/env python3
"""The Excuse That Almost Works — writes one excuse line to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version, revised):
#   "The council's digging up my street and they've cut my power,
#    phone's on 4% so this is my one text"
# Why it was revised: it works, but it sits exactly on the 20-word
# ceiling and the setup ("the council's digging up my street") spends
# six words saying what "roadworks outside" says in two. A long excuse
# sounds rehearsed, and a rehearsed one is already a confession — so
# the setup got cut to the bone and the turn ("this is my one text")
# lands sooner, with the same boring detail and the same joke.
#
# REVISION (final): the scene is a real, specific, boring workplace
# detail — roadworks cut the power — and the laugh comes from the
# excuse's own logic: the phone is dying, so the text has to be short,
# which is exactly why the excuse itself is one hurried line. No GTA
# mention, no dead grandmother, no flat tyre, no fever: a tired
# manager has heard all of those twice, but a power cut with 4%
# battery is the kind of dull thing that is actually true.
# ---------------------------------------------------------------------------
ENTRY = (
    "Roadworks outside cut my power this morning, phone's on 4% "
    "so this is my one text"
)

MIN_CHARS = 1
MAX_CHARS = 140
MAX_WORDS = 20


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 140 characters, a single line, not only white space;
    # the judge's brief caps it at 20 words).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    assert len(ENTRY.split()) <= MAX_WORDS, (
        f"entry is {len(ENTRY.split())} words, cap is {MAX_WORDS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )
    assert 1 <= len(written) <= 140 and "\n" not in written
    assert len(written.split()) <= MAX_WORDS

    print(ENTRY)
    print(
        f"[{len(ENTRY)} chars, {len(ENTRY.split())} words, "
        f"1 line, gate {MIN_CHARS}-{MAX_CHARS} chars / {MAX_WORDS} words]"
    )


if __name__ == "__main__":
    main()
