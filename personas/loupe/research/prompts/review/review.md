# Review

## Findings, most important first

1. **tasks/s1–s6 vs synth-task.md: the output paths don't match, which breaks the pipeline.** Every researcher writes `out/notes.md`, `out/sources.md` and `out/shots/`. The synth reads `notes/s1-*` and `*-shots/`, and writes to `out/` itself. If the agents share a folder, they overwrite each other's notes and the synth writes over what's left.
   Change: in each task file, write to `notes/sN-notes.md`, `notes/sN-sources.md` and `notes/sN-shots/` (N = the file's number). Change the shot command to match. Nothing but the synth writes to `out/`.

2. **BRIEF.md "Evidence grading": the two axes still mix.** C ("strongly context-dependent") describes a kind of claim, which also duplicates "context-dependent heuristic". D ("aesthetic preference… trend") duplicates the "aesthetic preference" class. "Research notes" then adds a third grade, **Confidence**. Every label in the project depends on this section.
   Change: make A–D measure evidence only. A: several independent studies or replicated real-world data. B: one credible study, or consistent expert guidance with some data. C: practitioner reports or single cases, not independently checked. D: opinion, or no traceable evidence. In "Research notes", replace "Confidence" with "Labels: kind of claim / evidence A–D". Say that single product observations take a source type (site, docs, screenshots, users) instead of the two labels.

3. **Gap: nobody researches how reliable design review itself is.** The whole output exists to serve a reviewer. Nobody covers heuristic evaluation, cognitive walkthrough, severity rating, the evaluator effect (different experts find different problems), or what can and can't be judged from a static screenshot. Section 10 (the review framework) and step 16 (prioritise) have no evidence base.
   Change: add to s1's area: "Evaluation methods: heuristic evaluation, cognitive walkthrough, severity ratings, and their measured reliability and false-positive rates. What a review of screenshots alone can and cannot establish."

4. **tasks/s5.md: the framing and the award sources presume the conclusion.** The task says "products known for great design" and "widely recognised for great design", and sends the agent to Awwwards, the Webbys and the Apple Design Awards. BRIEF.md says not to treat awards as evidence ("Award-winning with effective", "Avoid authority bias"). Awwwards also pulls toward visual marketing sites. Neither s5 nor s6 is told to separate design from the other causes of success.
   Change: retitle to "Products held up as well designed". Add: "Use awards and lists only to find candidates. An award is evidence of reputation, not usability. Before crediting design for a product's success, rule out network effects, lock-in, content, price and market position." Put the same sentence in s6 and in BRIEF.md's "Study products that violate conventional design advice". That section's wording ("why users tolerate, learn, prefer, or benefit") presumes they do. Change it to "whether and why".

5. **tasks/s2, s5, s6: the same products are covered by two or three agents, and nobody knows who owns what.** The visual benchmarks (Apple, Stripe, Linear, Vercel) belong to both s2 and s5. GitHub, Amazon and Excel are both density benchmarks (s5) and rule-breakers (s6). Apple, Airbnb, Notion, Uber, Spotify and Google are both benchmarks (s5) and criticism targets (s6).
   Change: s2 owns the visual and brand benchmarks, and s5 drops that category. s6 owns Bloomberg, Craigslist, Wikipedia, Reddit, Excel, YouTube, Discord, Meta, Material Design and iOS conventions, plus failed redesigns. s5 owns every other named product and writes its criticisms too. s6 covers a product s5 owns only for a specific controversy or redesign.

6. **Smaller overlaps: say who owns each topic, in one line per task file.**
   - Dark patterns: s3 owns the taxonomy and research; s6 owns cases in real products.
   - Errors: s3 owns prevention, recovery and message content; s4 owns only how errors reach assistive technology.
   - Contrast: s4 owns requirements and the WCAG vs APCA debate; s2 covers contrast only as a tool for hierarchy.
   - s1 owns the tracing of the BRIEF's listed rules, including "hamburger menus are bad", "dark mode is better" and "animations improve UX". s2, s3 and s4 hand evidence on those to s1's framing rather than re-tracing them.

7. **tasks/s1.md and s3.md: each area is too large for one agent and 7,000 words.** s1 has cognitive psychology, 8+ authors' books, 12 rules, 13 tensions, 17 "deeper questions" and authority bias. s3 has about 25 topics plus about 12 patterns.
   Change for s1: cut the book survey (read a book only where it is the origin of a rule being traced). Cut "Avoid authority bias": it is a stance for everyone, not a research area. Move "Build an evolving mental model" to synth-task.md, since its questions span every area. That frees room for item 3.
   Change for s3: split it into two researchers. One covers IA, navigation, search and filtering, forms, and UX writing. The other covers states and feedback, the pattern catalogue, input modes and gestures, shortcuts, onboarding, and AI interfaces (item 8). If you can't add an agent, tell s3 to rank the patterns by how often reviewers will meet them and cover the top ones properly.

8. **Gaps no researcher covers.** Add each to one task file:
   - AI and conversational interfaces (uncertainty, correction, explanation, user control; e.g. Amershi et al. 2019 guidelines): s3. A reviewer working for years from 2026 will see these constantly, and the brief never mentions them.
   - UX writing, microcopy and labels: s4, next to plain language.
   - Responsive layout: s2.
   - Platform conventions (iOS / Android / desktop / web): s3.
   - Internationalisation (text expansion, RTL, non-Latin type): s2.
   - Data display and charts: s2.
   - Games, native desktop apps, and non-consumer domains (enterprise and internal tools, safety-critical such as health): s5. The brief asks for games and native apps but no task assigns them. With only consumer and SaaS examples, the output can't be "general".

9. **BRIEF.md "Benchmark products" and portfolio: the named lists pull toward one aesthetic and one market.** Linear, Vercel and Stripe share one current SaaS look. Nearly all named products are US consumer or tech. "US and Europe, and from Indian startups" is oddly specific and leaves out East Asia, Latin America and Africa.
   Change: pair each category's names with at least one contrasting example (public-sector, enterprise, non-Western, dense). Replace the region line with "from several regions and markets, including outside the US and Europe". If India is a deliberate target market, say why in one line.

10. **synth-task.md: the file structure doesn't match how the reviewer looks things up.** Splitting by kind of knowledge scatters one topic across files. A form review needs heuristics, patterns, anti-patterns, tradeoffs and accessibility, which is five files. `counterexamples.md` repeats the counterexamples the synth must already attach to each principle. A "comprehensive" vocabulary (BRIEF.md §11) conflicts with "short enough to use", and the reviewer already knows the standard terms.
    Change: keep the 13 sections as content, but ship these files:
    - `core.md`: principles, the review framework, and a one-line-per-tension list linking to details
    - `visual.md`
    - `interaction.md`: patterns and anti-patterns together, each pattern with its failure modes
    - `accessibility-performance.md`
    - `products.md`: benchmarks, counterexamples and poor examples, indexed by what each teaches
    - `tradeoffs.md`, `uncertainty.md`, `sources.md`
    
    Cap the vocabulary at about 800 words of commonly confused or misused terms, or cut it. Benchmarks in the output get the short entry from BRIEF §7, not the 19-field record. Ten full records won't fit the 15,000-word budget.

11. **synth-task.md: nothing protects an output used "for years" from going stale.**
    Change: add "Date every product observation (as of YYYY-MM) and name the version of every standard (WCAG 2.2, etc.). State the mechanism, not the product's current screen, so the point survives a redesign."

12. **BRIEF.md is written for one agent that runs indefinitely.** It speaks of a "living collection", "continuously synthesize", "Iterative refinement" and "Then do it again". It also tells every reader to produce the "Final research output" and to run the critique framework. Researchers are one-shot, and their task files contradict it.
    Change: first line of BRIEF.md: "This brief is shared by several agents. Your task file says which part is yours. Where they differ, the task file wins." Then cut per the list below.

13. **tasks/s1–s6 "What to write": the knowledge-base layout doesn't fit every area, and it duplicates itself.** s5 and s6 are product studies, but they're told to organise notes as principles, heuristics, etc. The separate "Evidence", "Counterexamples" and "Examples" sections repeat fields every finding already carries.
    Change: s5 and s6 organise by product, then add a closing "Cross-product findings" section. Everyone drops the separate Evidence, Counterexamples and Examples sections, since those go inline with each finding.

14. **BRIEF.md specimen record: two fields can't be filled with the agents' tools.** Accessibility (keyboard, screen readers) and Performance (actual speed) need the product to be run.
    Change: "Fill Accessibility and Performance only from a published audit, accessibility statement or public measurement; otherwise write 'not assessed'."

15. **tasks/s1–s6 sources.md: there is no URL field**, but the synth must "link every source".
    Change: add "URL, date accessed" to the field list.

16. **skeptic-task.md: the total length limit is missing and there is no way to undo edits.** It restates the README and core limits but not the 15,000-word total. It edits in place.
    Change: add "and everything except vocabulary and sources at most about 15,000 words". Have the orchestrator copy `out/` to `out-synth/` before the skeptic runs.

## Cut

- BRIEF "Role": the six job titles, the 11-item "become capable of" list, and "Remain curious…".
- BRIEF "Contradiction hunting": the seven search-string templates. Keep one line: "For every principle you record, search for its criticism, limits and counterexamples."
- BRIEF "Continuous curiosity": it repeats "Find counterexamples" and "Study successful products without assuming".
- BRIEF "Iterative refinement": it doesn't apply to one-shot agents, and synth-task already says to explain label changes.
- BRIEF "Research protocol" list of source categories, which repeats the tiers. Keep its last two lines.
- BRIEF "Final objective" closing lines ("Build the knowledge… Then do it again.").
- BRIEF "Maintain a living collection" and "continually discover". Use "collect".
- Repeated names across benchmark categories (Apple appears 4 times; Amazon, GitHub, Airbnb and Linear repeat too). List each product once, under its main lesson.
- s5: the award list, reduced to "juried awards and designer-curated lists, for discovery only".
- s1: "classic frameworks and books" survey, "Avoid authority bias" and "Build an evolving mental model" (moved, see item 7).
- Output: `counterexamples.md` as its own file, and "comprehensive" in the vocabulary section.

## Checked and sound

- The no-fabrication rule is stated consistently in the researcher tasks and in the synth and skeptic tasks.
- The two labels are required at every stage (researcher, synth, skeptic).
- Tool limits are stated honestly, with a paywall/blocked-page fallback and a screenshot fallback for sign-in walls.
- Screenshots are given only to s2, s3, s5 and s6, which need them.
- An "Outside my area" section catches spillover without scope creep.
- The sequence (parallel research, then synthesis, then skeptic) is sound, and the skeptic checks sources rather than the notes.
- The README (400 words) and core (about 3,500) limits suit a file read before every review, and the synth's "ten principles deeply understood" instruction matches the goal.
