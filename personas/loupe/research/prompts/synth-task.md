# Your task

`BRIEF.md` in this folder describes a large research project. Read all of it first. It is the
standard for your work.

Five researchers already did the research, alone, one area each. Their notes and source lists are
in `notes/`:

- `s1-*`: foundations, evidence, where famous rules come from, and how reliable design review is
- `s2-*`: visual design, accessibility and performance
- `s3-*`: interaction design (structure, UX writing, behaviour, input modes, platform conventions,
  onboarding, the pattern catalogue, deceptive patterns, AI interfaces)
- `s4-*`: real products, leaning toward rule-breakers and failures
- `s5-*`: products known for great design, run afterwards to balance `s4`
- `*-shots/`: screenshots some of them took

Your job is the brief's "Final research output": the content of its thirteen sections, in the
files listed below. You write it from the five sets of notes. You do not repeat them. You judge
them.

## How to judge

- Where the researchers agree from independent sources, say so. Where they conflict, find out why
  (different context, different evidence, one of them wrong) and say which holds, and when.
- Keep both labels from the brief's "Evidence grading" on every finding: the kind of claim, and the
  strength of its evidence (A to D). Change a label if the notes together justify it, and say why.
- Where a finding matters and the notes are thin or contradict each other, check it yourself on the
  web. You may also look for sources the researchers missed.
- Follow the brief's final objective. Ten principles deeply understood beat a hundred tips. Cut
  repetition. Cut anything that only restates a better point.
- Every principle needs its evidence, its counterexamples, the products that show it, and when not
  to follow it.
- Answer the deeper questions in the brief's "Build an evolving mental model" where the notes
  support an answer. They span every area, so they are yours, not a researcher's.
- Never invent a number, a study, a quote or a date. If a note gives one without a traceable
  source, drop it or mark it.
- Keep the dates on product observations and the versions of standards. State mechanisms, not only
  current screens, so the points survive redesigns.

## Who reads it

A design reviewer agent reads this output before every review, for years. It reviews websites and
applications of every kind. So:

- It must be general, not tied to any one kind of product.
- It must be fast to use. The reviewer reads the index and the core every time, and the rest only
  when a review needs it. A review of one topic (for example a form) must find what it needs in one
  or two files.

## What to write, in `out/`

- `README.md`: the index. At most 400 words. Which file holds what, and when to read it.
- `core.md`: the design principles, the design review framework, and a list of the main design
  tradeoffs, one line each, that links to `tradeoffs.md`. This is the file read every time. At most
  about 3,000 words.
- `visual.md`: visual design.
- `interaction.md`: structure, behaviour and language. Patterns and anti-patterns together, each
  pattern with its failure modes.
- `accessibility-performance.md`
- `products.md`: benchmark products, counterexamples and poor examples, indexed by what each one
  teaches. Use the brief's short entry for each benchmark (section 7), not the full specimen record.
- `tradeoffs.md`, `uncertainty.md`, `sources.md`.
- `vocabulary.md`: at most about 800 words. Only terms that are commonly confused or misused, not
  the standard vocabulary a designer already knows.
- Everything except `vocabulary.md` and `sources.md` together: at most about 12,000 words.
- `SUMMARY.md`: one page, at most about 500 words, for a person who is not a designer and will not
  read the rest. The few ideas that matter most, each in plain words with one real example, and
  what the research could not settle.
- Write in plain words that a non-designer can follow. Name a real product or study wherever a
  claim needs one. Link every source you rely on.
