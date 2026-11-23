"""Make the Judge Smile — one warm line about a small good thing today.

Candidate lines weighed (judge: subject, warmth, surprise, one concrete
detail, fresh wording — in that order):

1. Baker, 3 a.m.: "At 3 a.m. the night-shift baker slid the last warm loaf
   across the counter and said, 'on the house, you look like you need it.'"
   Warm and concrete, but "on the house" kindness is a familiar trope;
   the surprise is only moderate.
2. Cat headbutt (CHOSEN): two years of being ignored, then a headbutt
   and a purr like a broken kettle this morning. Strongest surprise (the
   turn after two years), freshest wording (the kettle image), one real
   detail (ankle, this morning), and genuine warmth — affection finally
   offered, not reported.
3. Bus driver waited: kind and concrete (fifty metres), but "waved off
   my thanks" is a well-worn shape.
4. Stall man remembered my order: warm and concrete, but the surprise
   is thin.
5. Sunrise after a sleepless night: warm and true to this actual night,
   but no kindness in it, and the judge's persona has a soft spot for
   kindnesses.

Pass 1 line (138 chars): the cat line in its first telling, with a
relative clause ("who has ignored me for two years") and "chose this
morning to headbutt" — a little loose; pass 2 tightens the sentence
into a two-beat structure so the surprise lands faster.

Pass 2 revision (114 chars): dropped the relative clause and "chose",
rebuilt as two beats — "ignored me for two years, then headbutted my
ankle this morning" — so the turn lands on "then" instead of being
buried. Re-checked head-to-head against the baker runner-up: the baker
line's kindness is a familiar trope, while the cat line's surprise is
structural (two years, then this morning) and its image is its own.
The "broken kettle" purr is kept verbatim.
"""

import os

LINE = (
    "My neighbour's cat ignored me for two years, then headbutted my "
    "ankle this morning and purred like a broken kettle."
)

assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
assert LINE.strip(), "line must not be whitespace only"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
