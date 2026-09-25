import shutil
import sys
from pathlib import Path

base = Path(__file__).parent
brief = base / "BRIEF.md"
shot = (base.parent / "research-room-2/tools/shot.mjs").read_text()

common = """# Your task

`BRIEF.md` in this folder describes a large research project. Read all of it first. It is the
standard for your work: its methodology, its source tiers, its skepticism, its contradiction
hunting, its two-axis evidence grading, and its final objective.

Five researchers work on the project, alone. Each one takes one area. Yours is
below. A later researcher reads all five sets of notes and writes the final research output that
the brief describes, so you do not write that output, and you do not run the critique framework.
You write notes for your area that make the final output accurate.

## Your area

__AREA__

Stay inside your area where you can. If a finding clearly belongs to another area but you found it
anyway, keep it in a short section at the end called "Outside my area".

## What to write

- `out/notes.md`: at most about 9,000 words. __LAYOUT__ Record each finding as the brief's
  "Research notes" asks, with its evidence, counterevidence and example inline. Give every finding
  both labels from "Evidence grading", and its source. Prefer ten findings you checked to fifty you
  repeated.
- Date every observation of a product ("as of 2026-09") and name the version of every standard
  (for example WCAG 2.2). State the mechanism, not only the current screen, so the point survives a
  redesign.
- `out/sources.md`: every source you actually read and used: source, author, date, URL, date
  accessed, claim, evidence, context, limitations. Mark the ones you only saw quoted elsewhere.
- Say plainly where you could not find good evidence. Never invent a number, a study, a quote or a
  date. If a statistic has no traceable method, say so.

## Limits you work under

- You can read the web (WebSearch, WebFetch). You cannot install, run or log in to any app. What you
  know about a product comes from its site, its screenshots, its docs, case studies and what users
  and critics write about it. Say which of these each product finding rests on.
- Some pages block fetch tools or hide behind paywalls. Find another route to the idea (the
  author's own site, a talk, a summary by a reliable source) and say that you did.
__TOOLS__"""

topic_layout = ("Organise it by topic. Within each topic, use the brief's knowledge-base kinds that "
                "apply: principles, heuristics, patterns, anti-patterns, design tensions and open questions.")
product_layout = ("Organise it by product. End with a section called \"Cross-product findings\": "
                  "what several products together show, as principles, heuristics, patterns, "
                  "anti-patterns, tensions and open questions.")

tools_line = """- You can screenshot a public https page: `node tools/shot.mjs <https url> out/shots/NAME.png [width] [height] [full]`.
  For a phone view, use width 390 and height 844. Open the image with Read to look at it. Cookie
  banners and sign-in walls often hide the product. Where that happens, look for the product's own
  screenshots instead.
"""

areas = {
    "s1": ("""Foundations, evidence and evaluation.
- The research behind design: HCI, cognitive psychology and perception (attention, memory,
  recognition against recall, mental models, learning, Fitts's and Hick's laws, Gestalt, reading
  and scanning behaviour). Read a book only where it is the origin of a rule you trace.
- You own the brief's "Find counterexamples" and "Contradiction hunting": trace every rule listed
  there (including "hamburger menus are bad", "dark mode is better" and "animations improve UX"),
  and others you find, to its original evidence and context, find later research and
  counterexamples, and classify it. Other researchers hand evidence on these rules to you.
- The brief's "Compare competing principles".
- Evaluation methods: heuristic evaluation, cognitive walkthrough, severity ratings, and their
  measured reliability, including how often different expert reviewers find different problems,
  and false positives. What a review of screenshots alone can and cannot establish.""", None, topic_layout),
    "s2": ("""Visual design, accessibility and performance.
- Visual design: hierarchy, typography and type scale, spacing, alignment, grids, colour and colour
  systems, density, shape, radius, borders, shadows and elevation, iconography, imagery and
  illustration, motion, and consistency. Responsive layout. Internationalisation: text expansion,
  right-to-left layout, non-Latin type. Data display and charts.
- Design systems and design tokens: how mature organisations structure them and why, and their
  limits.
- What makes an interface feel premium, elegant, coherent, expressive or empty, and what brand
  expression can and cannot do without hurting use.
- Accessibility: WCAG and what it does and does not guarantee, keyboard navigation, screen readers
  and semantic structure, focus management, colour contrast (including the debate over WCAG 2
  contrast against APCA), motion sensitivity, text scaling, touch target size and its evidence,
  plain language and cognitive accessibility, and how errors reach assistive technology. Where
  accessibility helps everyone, and where different needs conflict.
- Performance as users feel it: perceived against actual speed, response-time thresholds and their
  origin, loading behaviour, progressive rendering, skeleton screens, optimistic UI, and
  responsiveness.
- You own the brief's "Visual and brand design" benchmarks (Apple's visual design, Stripe, Linear,
  Vercel), its "Accessibility and public-service design" benchmarks, and "Avoid aesthetic bias".
  Look at real interfaces.""", "9223", topic_layout),
    "s3": ("""Interaction design: structure, behaviour and patterns.
- Structure: information architecture and mental models, navigation models and wayfinding, search,
  filtering, sorting and comparison, and forms and input.
- Language: UX writing, microcopy, labels, instructions and error message content.
- Behaviour: feedback and system status, affordance and discoverability, direct manipulation, error
  prevention and recovery, undo and confirmation, defaults, and empty, loading, success and failure
  states, and microinteractions.
- Input modes and platforms: touch, pointer and keyboard, gestures, command systems and shortcuts,
  and platform conventions (iOS, Android, desktop and web), where they differ and when to follow
  them.
- Onboarding and learning, how interfaces serve beginners against experts, and how they adapt to
  repeated use. Personalization and automation against user control.
- The pattern catalogue: modal, sheet, drawer, tabs, accordion, carousel, infinite scroll,
  pagination, hamburger menu, sticky navigation, toasts and others. Rank patterns by how often a
  reviewer will meet them, and cover the most common ones properly: when each works and when it
  fails.
- Anti-patterns, and the taxonomy and research on deceptive patterns.
- AI and conversational interfaces: showing uncertainty, correction, explanation and user control
  (for example the Guidelines for Human-AI Interaction by Amershi and others, 2019).""", "9222", topic_layout),
    "s4": ("""Real products: the well designed, the rule-breakers and the failures.
- The brief's "Build a benchmark portfolio", "Benchmark products", "Study successful products
  without assuming they are good", "Study products that violate conventional design advice",
  "Study criticized or controversial designs" and "Analyze products as specimens".
- Work through the benchmark categories, except "Visual and brand design" and "Accessibility and
  public-service design", which the visual researcher owns.
- Find more apps and websites that respected designers and design teams hold up as models.
  Juried awards and designer-curated lists help you find candidates. An award is evidence of
  reputation, not of usability.
- Include games, native desktop apps, enterprise and internal tools, and safety-critical products
  such as health, not only consumer and SaaS products.
- Study the rule-breakers the brief names, criticism of praised products and design systems,
  demonstrably poor designs, redesigns that failed or drew backlash (with what the team and the
  users said), deceptive patterns in real products, and conflicts between business goals and user
  goals. Use user reviews, forums and critics, graded as anecdote.
- Before crediting or blaming design for a product's fate, rule out network effects, lock-in,
  content, price and market position.
- For each product, find the mechanism that makes it work or fail, what is worse or better than it
  appears, and what it teaches about the limits of a principle. Give the full specimen record to
  about ten products that teach the most, and a short entry to the rest.""", "9224", product_layout),
    "s5": ("""Products known for great design.
- Another researcher already studied these products, so do not repeat them: Bloomberg Terminal,
  Microsoft Excel, the Office 2007 ribbon, Craigslist, Amazon Prime sign-up and cancellation,
  Booking.com, Duolingo, the 2024 Sonos app, the 2018 Snapchat redesign, electronic health records,
  Figma UI3, Wikipedia's Vector 2022, Instagram's 2022 full-screen test, Apple Photos in iOS 18,
  Slack's 2023 redesign, Linear, Notion, Google Maps, Airbnb total pricing, Uber surge pricing,
  Stripe payment methods, Flighty, Dead Space, car touchscreens, the 2018 Hawaii missile alert,
  LinkedIn contact import and the Google Drive launch. That researcher leaned toward failures and
  rule-breakers. Your job is the other side.
- Study apps and websites that respected designers, design teams and juried awards hold up as
  well designed, and find exactly why. Awards and designer-curated lists help you find candidates.
  An award is evidence of reputation, not of usability. Before crediting design for a product's
  success, rule out network effects, lock-in, content, price and market position.
- Cover at least these, which the other researcher skipped: GitHub, Spotify, Netflix, Pinterest,
  Canva, Dropbox, Revolut, Figma (beyond UI3), Stripe (beyond payment methods), Apple's own apps,
  and Indian startups known for design. Then add others you find, across mobile, web, desktop,
  games, productivity, finance and developer tools.
- The brief's "Study successful products without assuming they are good" applies to each: find
  the mechanism that makes it work, what is worse than it appears, and when its approach would
  fail. Include the product's criticisms and limits.
- Give the full specimen record to about ten products that teach the most, and a short entry to
  the rest.""", "9224", product_layout),
}

for name, (area, port, layout) in areas.items():
    if sys.argv[1:] and name not in sys.argv[1:]:
        continue
    room = base / name
    if room.exists():
        shutil.rmtree(room)
    (room / "out").mkdir(parents=True)
    shutil.copy(brief, room / "BRIEF.md")
    tools = ""
    if port:
        (room / "tools").mkdir()
        (room / "out/shots").mkdir()
        (room / "tools/shot.mjs").write_text(shot.replace("9222", port))
        tools = tools_line
    text = common.replace("__AREA__", area).replace("__TOOLS__", tools).replace("__LAYOUT__", layout)
    (room / "TASK.md").write_text(text)
    print(name, port or "-")
