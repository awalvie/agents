# Structure and interaction

Read this when a direction's structure is open: organization, navigation, flows, states, modes and motion. Labels are in `README.md`.

## Generate structural options

- Name the structural questions and answer each more than one way: scheme, structure type, root navigation model, flow granularity, posture, modes, motion. Build each direction from one answer per question, and write down the criteria each answer favours (Questions, Options and Criteria: MacLean et al. 1991, read as a summary). [UP, C, inferred]
- Metaphor exploration generates schemes: organizational, functional and visual metaphors, each with the warning that a metaphor limits what fits (Rosenfeld et al. 2015). [UP, C, stated]
- Card sorts show how users group items. They are input, not the structure: separate sorts of the same content agree closely (Katsanos et al. 2019), but Nielsen (2004) advises against building from the scores alone. [SH, B, stated]

## Organization scheme

- Exact schemes (alphabetical, chronological, geographical) serve people who know the name of what they want. Ambiguous schemes (topic, task, audience, metaphor) serve people who browse, because often "you simply don't know the correct label" (Rosenfeld et al. 2015, read as snippets). [SH, B, stated]
- A pure scheme suggests a simple mental model. Audience, topic and task labels mixed in one list break it. A mix is tolerable only in a short list at the surface. Audience schemes need clearly separate audiences. A metaphor breaks when a feature does not fit it (same source). [SH, B, stated]
- Craigslist nests schemes and never mixes them in one list: exact geography outside, topics inside (observed 2026-09-26). [UP, C, inferred]
- To get real alternatives, give each direction a different primary scheme. [CH, C, inferred]

## Structure type

- A hierarchy fits a few items of mixed kinds. Facets fit many items that share attributes, such as a catalogue or a staff directory. Hypertext links suit ideas that cross branches, and they work on top of another structure, rarely as the main one (Rosenfeld et al. 2015). [SH, B, stated]
- In a faceted image search, 91% of 32 users preferred facets to keyword search (Yee et al. 2003). Those who did not found them restrictive. [SH, B, stated] Facets need clean metadata on every item. [CH, C, inferred]

## Breadth and depth

- A flatter tree usually beats a deeper one, because each level adds a category decision, and label quality ("scent") matters more than the count. In Larson & Czerwinski (1998, 19 users, 512 items), a 16x32 tree took 36 s, 32x16 took 46 s, and 8x8x8 took 58 s. The two 2-level trees did not differ significantly, so the cost of a very broad top level is a trend, not a result. [SH, B, stated. Lowered from A-B: all studies are small, mostly menus, and three are known only through this paper]
- The number of clicks does not predict quitting (Porter 2003). "Seven plus or minus two" does not set menu length (Larson & Czerwinski 1998). [UC for both claims, B against them, stated]
- Vary depth and top-level labels between directions. Compare them by counting the decisions a user makes on the key paths. [CH, C, inferred]

## Object-first structure

- You can derive a structure from the domain's things and their links, one page per thing, instead of a page tree or task list. BBC Programmes gives every programme a web identifier and a page, linked to its episodes and people (Raimond et al. 2010). The interaction version is object first, then action, which avoids modes (Xerox Star, Smith et al. 1982). [CH, C, stated]
- It fits domains with many connected entities, where people arrive from search. It is poor for one linear task such as checkout, and where entities are unstable. [CH, C, inferred] Even the Star added dedicated keys for frequent actions, because generic commands interrupted typing. [stated]
- The core model method (Aalen 2015, after Halland): design first the pages where user tasks meet business goals, then the paths in and out, and the home page last. [UP, C, stated]

## Navigation models

- There is a small palette: hub and spoke, flat (tabs or sidebar), drill-down tree, pyramid (siblings linked), step by step, pan and zoom, content-driven, and modal overlays (Tidwell et al. 2020, names only; Rausch 2025). Levels can differ: tabs at the root, drill-down inside, a step-by-step modal to create a record. To get structurally different directions, change the model at the root. [UP, C, inferred]
- Hidden navigation is used less. In an NN/g study (179 users, 6 sites), desktop users used it in 27% of tasks when hidden against 48 to 50% when visible or partly visible, and were at least 39% slower. On phones: 57% hidden against 86% partly visible, and 15% slower (Pernice & Budiu 2016, checked on the page). [SH, B, stated]
- The real question is which few destinations earn permanent space. On phones, NN/g suggests showing the top links when there are 4 or fewer. Hide only rare items, or where the content is the navigation, as in a reader. [SH, B, stated]

## Posture and disclosure

- Posture is in `core.md`. A "training wheels" editor that blocked error-prone states sped up novices' learning (Carroll & Carrithers 1984). Let users open deeper levels themselves. Do not reorder the structure automatically (Findlater & McGrenere 2004). [SH, B, stated] Nielsen's claim that more than two disclosure levels "typically" fail cites no study. [UC, D]

## Flow granularity

- The same questions can be one long page, a few grouped steps, or one thing per page. Effort comes mostly from the number and difficulty of the questions. Baymard finds that the number of checkout fields matters far more than the number of steps (Scott 2024; its testing is not public). So first remove questions. [SH, B, stated]
- One thing per page suits infrequent, low-confidence users, and it handles branching, errors and saving progress (Paul 2015, GDS; GOV.UK Service Manual 2018). It costs repeat users time, loses context between pages, and breaks links into the middle of a flow (GOV.UK deep-link error page, observed 2026-09-26). [CH, C, stated] A check-answers page is the usual repair. [inferred]
- A story map (Patton 2008) lays out the user's activities in order, details below, and gives a flow's skeleton before you choose granularity. [UP, C, stated]

## Modes

- A mode changes what the same input does, and users forget which mode they are in (Tesler, quoted in Smith et al. 1982; Raskin 2000). Three options: avoid it (select, then act); hold it, so it lasts only while a key is down, which caused fewer errors than a latched mode (Sellen et al. 1992); or make a persistent expert mode very visible. [SH, B, stated]
- A command palette is a summoned mode that acts on the current selection and teaches shortcuts (Superhuman, Boucher 2021). It is hidden navigation, so it cannot be the only way in for new users. [UP, C, inferred]

## States

- Every key screen has states: ideal, empty (first use, cleared, no results), partial, loading, and error, which must keep the user's input (Hurff 2015). A statechart nests states so combinations do not explode (Harel 1987). A state the user cannot see is a mode. [SH, C, stated]
- Directions often differ most in these states. An empty state can teach, show a sample, or offer one action. [CH, C, inferred]

## Content first or structure first

- Zeldman (2008): design without content "is decoration". That is opinion [AP, D]. Boulton (2012): you can design without the content, but not without its structure, meaning its types and parts. Both reject placeholder text alone. Choose by whether the content exists. [CH, C, stated]
- Priority guides (`core.md`) rank content without layout, because early wireframes limit what visual designers imagine (van Nues & Overkamp 2018). Mobile-first is the same ranking device (Wroblewski 2009), but mobile patterns carried unchanged to desktop hurt it (Budiu & Pernice 2016). [CH, C, stated]

## Motion

- Motion helps when the view changes place or shape, because it keeps people oriented. Animated viewpoint changes helped users map a zoomable space at no time cost (Bederson & Boltman 1999, 20 users), and staged transitions between charts beat cuts (Heer & Robertson 2007, 24 users). Studies that seemed to show animation helping in general usually compared unequal content (Tversky et al. 2002). [SH, B, stated]
- Let the transition encode the relationship. A container transform says "this view is that card". A shared axis says "sibling" or "next". A fade through says "unrelated" (Material motion documentation). [UP, C, stated] So the motion vocabulary follows the navigation model. [inferred]
- Keep frequent actions nearly instant, and let people cancel motion (Apple HIG, Motion). [DC, C, stated] The lab durations near 1 s were for viewpoint and chart changes, not routine transitions. Motion for "delight" alone: [AP, D].

## Lists

- Etsy's search test found that users with infinite scroll saw, clicked, saved and bought fewer items, and Etsy removed it (McKinley 2012, talk transcript checked). The talk gives no cause (see `uncertainty.md` for a correction). Use pages, or "load more" with a position the user can return to, for goal tasks such as shopping and search. Infinite scroll can fit an aimless feed. [CH, B, stated]
