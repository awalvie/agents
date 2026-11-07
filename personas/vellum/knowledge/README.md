# Vellum knowledge base, v2

This knowledge base helps a designer turn requirements into several directions, each a single HTML file. It gives mechanisms, options and tradeoffs, not rules. It was written on 2026-09-26 from five research notes and checked against the raw sources (v2).

Read `README.md` and `core.md` every time, and a topic file when the task needs it.

- `core.md`: brief to constraints, directions that really differ, the machine-made look, references, the conventional baseline, shared mechanisms, choosing.
- `structure.md`: schemes, facets, breadth and depth, object-first structure, navigation, flows, modes, states, motion, lists. Read it when structure or flow is open.
- `visual.md`: line length, body size, type scales, typefaces, spacing, grids, hierarchy, colour, dark themes, icons, imagery. Read it when you choose the look.
- `languages.md`: traditions and where each fails, sameness, identity, plainness, where expression belongs. Read it when you pick a tradition, or a direction looks generic.
- `code.md`: CSS support as of 2026-09-26, tokens, scales, fluid type, layout, cascade, colour formulas, gains and losses of code. Read it when you build.
- `uncertainty.md`: disputed findings, weak evidence, bias, corrections, gaps, sources not read, and figures not to cite. Read it before citing a number.
- `sources.md`: sources, links, and how much was read.
- `skeptic-log.md`: what v2 changed and why. Not needed for design work.

## Label key

Each finding ends with three marks in brackets, such as [SH, B, stated].

The first mark is the kind of claim:
- FP: fundamental principle
- SH: strong heuristic
- CH: context-dependent heuristic
- UP: useful pattern
- DC: design convention
- AP: aesthetic preference
- UC: unsupported claim
- fact: a dated measurement, such as browser support

The second mark is the strength of evidence:
- A: several independent studies, or replicated data
- B: one credible study, or consistent expert guidance with some data
- C: practitioner reports or single cases
- D: opinion, or nothing traceable

C and D are normal for craft.

The third mark is the source of the mechanism:
- stated: the source states the mechanism
- inferred: a researcher drew the mechanism from the sources
- synth: the synthesis drew it by combining areas. It is an inference, not a finding.

The mark covers the mechanism. The closing advice in a finding is always inferred. `sources.md` lists which sources were read on the raw text.
