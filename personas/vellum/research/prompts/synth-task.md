# Your task

Read `/home/awalvie/code/lamp/agents/personas/vellum/research/BRIEF.md` first, all of it. It is
the standard for your work.

Five researchers did the research, alone, one area each. Their notes and source lists are in
`/home/awalvie/code/lamp/agents/personas/vellum/research/notes/`: `process-*`, `structure-*`,
`visual-craft-*`, `languages-*` and `code-*`. The `*-shots/` folders hold their screenshots.

Your job is the knowledge base that the brief describes. You write it from the five sets of notes.
Do not repeat the notes. Judge them.

Do not read any other file in `/home/awalvie/code/lamp/agents/`. Other files there hold test
outputs and another persona's conclusions, and they would bias you.

## How to judge

- Where researchers agree from independent sources, say so. Where they conflict, find out why and
  say which holds, and when.
- Keep both labels on every finding, and the mark that says whether the source states the
  mechanism or the researcher inferred it. Change a label if the notes together justify it, and
  say why.
- Where a finding matters and the notes are thin, check it yourself on the web. The web fetch
  tool returns a summary made by a small model, not the page. So before you keep a quote, read
  the raw page with `curl` if you can, or mark the quote as unchecked.
- Read each "Outside my area" section, and put each finding where it belongs.
- Never invent a number, a study, a quote or a date. If a note gives one without a traceable
  source, drop it or mark it.
- Cut repetition. A few mechanisms that are well understood beat many tips.

## Who reads it

A designer agent reads this before it designs a website or an app. It produces several
directions as HTML prototypes. So:

- The knowledge base must widen what the agent can do. Give mechanisms, options and tradeoffs.
  Never write a checklist or a house style.
- It must be fast to use. The agent reads the index and the core every time, and a topic file
  only when a task needs it.

## What to write, in `/home/awalvie/code/lamp/agents/personas/vellum/research/synthesis/v1/`

- `README.md`: the index, at most 400 words. Which file holds what, and when to read it. Include
  the label key.
- `core.md`: at most about 2,500 words. How to get from requirements to several directions that
  really differ, how to choose between them, and the mechanisms that matter in every design.
- `structure.md`, `visual.md`, `languages.md`, `code.md`: one topic file for each of those areas.
- `uncertainty.md`: disputed findings, weak evidence, gaps, sources that could not be read, and
  figures not to cite.
- `sources.md`: the sources you rely on, with links and how much of each was read. At the top,
  give the count of sources by type and by how much was read, so that a reader can judge the
  quality at a glance.
- Everything except `sources.md`: at most about 10,000 words in total.

Write in plain words that a non-designer can follow. When you finish, reply with the word count
of each file and the five findings you trust least.
