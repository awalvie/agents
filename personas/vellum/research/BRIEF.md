This brief is shared by several research agents. Your task file says which area is yours. Where
the two differ, the task file wins.

# Goal

The research builds the knowledge base of a designer persona. The persona takes the requirements
for a website or an app and produces several design directions. Each direction is one
self-contained HTML file that opens in a browser with no build step. The persona explains the
reasoning behind each direction and its tradeoffs.

The persona must know many ways to design well, and when each way fits. It must know when the
conventional design is right, and when to depart from it. It must not follow a single house
style.

This research is about how to make a design. Another persona already holds researched knowledge
about how to judge one. So do not research these subjects: usability testing and evaluation
methods, accessibility standards and conformance, performance and loading, and design review.

# What to find out

For each area, find out:

- What experienced designers actually do, and why it works.
- Where designers disagree, and what the disagreement depends on.
- Which conventions have evidence behind them, and which are only habit.
- What makes a design distinctive, what makes it look generic, and when generic is the right
  choice.

Record mechanisms, not rules. "Use an 8 px spacing grid" is a rule. "A fixed spacing scale
reduces arbitrary decisions and makes rhythm visible" is a mechanism, and it says when the rule
helps. A number is acceptable only when you can trace it to its origin.

For each mechanism, say whether the source states it or you inferred it.

# Sources

Use these sources first:

- The writing of designers about their own work: studio case studies, design team blogs,
  postmortems and interviews. Treat a team's account of its own work as evidence of what it
  intended, not of what the result achieved.
- Books by practitioners and teachers of design, typography, layout and color.
- Research papers about the design process, creativity, visual perception and aesthetics.
- Design systems and guidelines from mature organizations. Read their reasoning, not only their
  rules.
- Real products and sites. Look at them directly, and date each observation.

Use community discussion to find disagreements, complaints and counterexamples. Treat it as
anecdotal evidence.

Do not use SEO articles, listicles, "top 10" posts, inspiration galleries without reasoning, or
AI-generated summaries as evidence. You can use them to find a primary source. Then read the
primary source.

Ten articles that repeat one claim are one source. Trace each claim to its earliest source.

Do not treat a famous designer, studio or company as correct because it is famous. Find the
mechanism behind the result.

# Evidence

Give every finding two labels:

- The kind of claim: fundamental principle, strong heuristic, context-dependent heuristic, useful
  pattern, design convention, aesthetic preference, or unsupported claim.
- The strength of the evidence: A (several independent studies or replicated data), B (one
  credible study, or consistent expert guidance with some data), C (practitioner reports or
  single cases), D (opinion, or nothing traceable).

Much design craft has no controlled study behind it. A C or D label is expected for craft, and it
is not a reason to discard the finding. Record whose work demonstrates the finding instead, and
where it fails.

For each important claim, search for its criticism, its limits and its counterexamples. The
goal is to find where the claim stops being true.

# Areas

Each researcher takes one area.

1. **Process.** How designers turn requirements into constraints, get from the constraints to
   several directions, and choose between them. Research divergence and convergence, design
   fixation, parallel and serial prototyping, the use of references, critique, and iteration.
   Find what the research says, and what studios and product teams say that they do.
   Coverage check: Jansson & Smith, "Design fixation" (1991); Dow et al., "Parallel prototyping
   leads to better design results" (2010).
2. **Structure and interaction as design choices.** How designers produce different options for
   the structure of a product: its information architecture, flows, states, content and motion.
   Research how to generate and compare these options, not how to evaluate them.
   Coverage check: Rosenfeld, Morville & Arango, *Information Architecture* (4th edition, 2015).
3. **Visual craft.** Layout, grids, spacing, alignment, typography, color, imagery, icons and
   composition. Find the mechanism behind each practice. This area covers which choice to make
   and why. Area 5 covers how to build it.
   Coverage check: Bringhurst, *The Elements of Typographic Style*; Müller-Brockmann, *Grid
   Systems in Graphic Design*; Albers, *Interaction of Color*.
4. **Design languages and distinctiveness.** The traditions of interface design. Build the list
   of traditions from your sources, and record where sources group them differently. For each
   tradition, find what it is good for and where it fails. Find how products with a strong
   identity got it. Find what makes a design look generic or machine-made, and when a generic
   design is the right choice.
   Coverage check: Meggs, *Meggs' History of Graphic Design*.
5. **From direction to code.** How a direction becomes a working prototype in one HTML file with
   no build step: design tokens, type and spacing scales, responsive layout, and current CSS
   capabilities. Use dated sources for browser support, such as MDN and caniuse. Find what
   designers lose or gain when they design directly in code.
   Coverage check: MDN; caniuse; Pickering & Bell, *Every Layout*.

The coverage checks are a minimum, not a starting list. Your sources must include them, or your
notes must say why you did not use them. Find the other sources yourself.

Stay inside your area. If you find something important for another area, put it in a short
section at the end of your notes called "Outside my area".

# What each researcher writes

- `notes.md`: your findings. For each finding, give the claim, the evidence, the context where it
  applies, the counterevidence, an example, the two labels, and when a designer would use it and
  when not. Ten findings that you checked are better than fifty that you repeated.
- `sources.md`: every source you used, with its author, date, URL, the date you read it, and how
  much you read (full text, abstract, or quoted in another source). At the top, give a count of
  your sources by type.
- Screenshots go in a folder called `<area>-shots/` next to your notes. Name each file after the
  product and the date.

Never invent a study, a number, a quote or a date. If you cannot find good evidence for
something, say so.

# The final knowledge base

A later agent writes the knowledge base from all the notes, and a skeptic checks it against the
sources. The knowledge base must widen what the persona can do, not narrow it. It gives the
persona mechanisms, options and tradeoffs, not a checklist to follow.
