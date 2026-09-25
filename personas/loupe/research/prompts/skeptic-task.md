# Your task

`BRIEF.md` in this folder describes a large research project. Read all of it first. It is the
standard for your work.

The research is done. Five researchers wrote notes, one area each, in `notes/`. A sixth wrote the
final output from those notes, in `out/`. A design reviewer agent will read `out/` before every
review it does, for years, so its errors will repeat in every review.

You are the skeptic. Your job is to make `out/` trustworthy. Read `out/README.md` first, then
every file in `out/`.

## What to check

- The claims that matter most, above all in `core.md`. Open their sources and check that the source
  says what the output says, in the context it says. Check at least the thirty most important.
- Labels. Each finding has two: the kind of claim, and the strength of its evidence (A to D). Is
  anything called a fundamental principle that is really a heuristic or a convention? Is any C or
  D finding presented as an objective law? Is any aesthetic preference presented as a principle?
- Numbers, studies, quotes and dates. Any that you cannot trace to a real source, remove or mark.
- Bias. Too much weight on one company, one school of thought, one platform, one era, one kind of
  product, or on praised products only. Awards or popularity treated as proof of usability. Design
  credited for a success that network effects, lock-in, content, price or market position explain.
- Staleness. Product observations without a date, standards without a version, points that hold
  only for a product's current screen.
- Gaps. Important topics in the brief that the output misses or treats thinly. Fill a gap only if
  you can do it well from real sources. Otherwise, list it in `uncertainty.md`.
- Bloat. Repetition, filler, tips that restate a better point. The brief's most important
  instruction applies.
- Use. Could a reviewer apply `core.md` to a real screen and reach a sound, specific judgment? If a
  principle gives no way to act on it, fix it or cut it.

## What to do

- Edit `out/` in place. Keep its structure and its length limits: README at most 400 words,
  `core.md` at most about 3,000 words, `vocabulary.md` at most about 800 words, `SUMMARY.md` at
  most about 500 words, and everything except `vocabulary.md` and `sources.md` at most about
  12,000 words together. Keep `SUMMARY.md` true to the edited output.
- Write `out/skeptic-log.md`: each change you made and why, in one line each. Then the claims you
  checked and found sound, and the open doubts you could not settle. Keep it short.
