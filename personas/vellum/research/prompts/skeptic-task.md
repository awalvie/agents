# Your task

Read `/home/awalvie/code/lamp/agents/personas/vellum/research/BRIEF.md` first, all of it. It is
the standard for your work.

Five researchers wrote notes in `research/notes/`. A sixth agent wrote a knowledge base from those
notes, in `research/synthesis/v1/`. A designer agent will read that knowledge base each time it
designs a website or an app, so its errors will repeat in every design. All paths are under
`/home/awalvie/code/lamp/agents/personas/vellum/`.

You are the skeptic. Your job is to make the knowledge base trustworthy. Copy `synthesis/v1/` to
`synthesis/v2/`, and edit only `v2`. Read `v2/README.md` first, then every file in `v2`.

Do not read any other file in `/home/awalvie/code/lamp/agents/`. Other files there hold test
outputs and another persona's conclusions, and they would bias you.

## What to check

- Start with the frameworks in `core.md` that the synthesis agent built itself, marked "synth". One
  of them is the three-layer split: conventional furniture, a distinctive core model, and
  expression in the surface. Try to break each one with real counterexamples. Keep it only if it
  survives, and label it as the synthesis agent's inference.
- The claims that matter most, above all in `core.md`. Open their sources and check that the
  source says what the knowledge base says, in the same context. Check at least the thirty most
  important. The web fetch tool returns a summary made by a small model, not the page, so read the
  raw page with `curl` or the PDF before you confirm a quote.
- Labels and marks. Is a C or D finding presented as a law? Is an aesthetic preference presented
  as a principle? Is a mechanism marked "stated" when the source does not state it?
- Numbers, studies, quotes and dates that you cannot trace to a real source: remove or mark them.
- Narrowing. Does any file push the designer toward one style, one kind of product, or one
  process? Is anything written as a checklist or a rule where the evidence supports only an
  option? Does the knowledge base treat conventional design as a failure?
- Bias. Too much weight on one company, one research firm, one tradition, one platform or one
  era.
- Gaps. Fill a gap only if you can do it well from real sources. Otherwise, list it in
  `uncertainty.md`.
- Use. Could a designer apply `core.md` to real requirements and produce several directions that
  really differ? If a mechanism gives no way to act on it, fix it or cut it.

## What to do

- Keep the structure and the length limits of the synthesis task: README at most 400 words,
  `core.md` at most about 2,500 words, and everything except `sources.md` at most about 10,000
  words.
- Write `v2/skeptic-log.md`: each change and why, in one line each. Then the claims you checked and
  found sound, and the open doubts you could not settle. Keep it short.
- When you finish, reply with the number of claims you checked, the number you changed, and what
  happened to the synthesis agent's own frameworks.
