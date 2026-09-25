# Your task

Review a set of prompts before they run. Do not run them and do not do the research they describe.

The plan: six research agents work alone and in parallel, one area each. Each gets `BRIEF.md` (the
shared research brief) and its own task file (`tasks/s1.md` to `tasks/s6.md`). Then one agent writes
the final output from their notes (`synth-task.md`), and one skeptic agent checks and edits that
output (`skeptic-task.md`). Every agent starts with no other context. Each can search and read the
web, and some can screenshot public web pages. None can run or log in to apps.

The goal of the whole project: a body of knowledge that a design reviewer agent will read before
every review of a website or app, for years. It must be general, trustworthy, and short enough to
use. It must not be tied to any one kind of product.

## Look for

- Instructions that conflict, within one file or across files.
- Gaps: important parts of the brief that no researcher covers, or that fall between two areas.
- Overlap: work that two researchers will both do.
- Areas too large for one agent to cover well.
- Anything that will bias the result: a named product or source that pulls the agents one way,
  wording that presumes a conclusion.
- Instructions that an agent cannot follow with its tools.
- Anything unnecessary. Cut it.
- Whether the length limits and the output structure serve the reader described above.

## Output

Write `review.md`. Short. Your findings in order of importance. For each: the file, the problem in
one line, and the exact change you recommend. Then a list of what you would cut. Then anything you
checked and found sound, in one line. Do not edit the other files.
