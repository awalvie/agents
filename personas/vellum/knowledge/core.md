# Core: from requirements to directions

Read this every time. Labels are in `README.md`. Everything here is an option with its conditions, not a procedure.

## 1. Turn the brief into constraints

- Problem and solution develop together: once a core idea formed, designers redefined the problem around it (Dorst & Cross 2001, 9 designers, one task) and invented requirements as they sketched (Suwa et al. 2000, abstract). So directions can differ in their frame, not only in styling. [CH, C, stated]
- All nine designers in Dorst & Cross reached the same core idea from facts spread through the brief, and each reported it as original, though their designs differed. If the obvious idea is right, keep it as the expected direction and let the others depart from it. [UP, C, stated]
- Reduce the requirements to a few binding constraints: audience, the one job, real content, platform, posture, and affordable complexity. A constraint can help when it removes the default answer and leaves room to search. Acar et al. (2019, a review) propose an inverted U for all constraints; it is measured only for slack and time pressure. Input constraints helped only without heavy time pressure (Moreau & Dahl 2005, abstract). [CH, B, stated. The general curve: CH, C]
- A brief with no context led designers to "self-similar solutions" (Liikkanen & Perttula 2008, via Vasconcelos & Crilly 2016). Ask for the missing context, or write the assumption down. [CH, C, stated]
- Abstract problem statements gave more original ideas, and concrete ones gave ideas that fit the constraints better (Zahner et al. 2010, via the same review). [CH, C, stated]
- One option before layout: a ranked list of each key screen's content (a "priority guide", van Nues & Overkamp 2018, one agency's practice), shared across directions so they differ in form, not in what they forgot. [UP, C, inferred]

## 2. Generate directions that really differ

- Engineering designers with very few concepts fixated early, those with very many spent their time managing variants, and the successful ones ran a "balanced search" (Fricke 1996, via Cross 2004). No source gives a right number of directions. [CH, C, stated]
- For the best direction, the number of options, their average quality, their spread and good selection all matter (Girotra et al. 2010, students; data on spread inconclusive). Two directions that share one core principle may count as one (inferred from a consultant in Crilly 2015). [CH, B, stated]
- Axes that can produce real difference: the frame; the structure (`structure.md`); posture and density; the tradition (`languages.md`); which layer carries the novelty; a self-imposed constraint. GDS once set the whole site "in one typeface, just one type size" and in black and white, to find how many typefaces and sizes it needed (Terrett 2012). No source tests which axes spread best. [UP, C, synth]
- Generate the directions separately before you merge ideas. Iterating one design kept participants on their first idea: "I pretty much stuck with the same idea" (Dow et al. 2009, 2010, mostly students). Exchanging ideas during brainstorming narrowed the domains explored (Kohn & Smith 2011). Pairs who shared several drafts borrowed more from each other, and that condition did better, though borrowing itself was not linked to results (Dow et al. 2011). [SH, B, stated. The advice to separate first and share drafts later is inferred]
- One option: write each direction as a short spec before markup: frame, axioms, scales, colour roles, type pairing, layout idea, and the defaults it keeps. With GPT-4, a prompt that listed 100 short ideas, made them "bolder and more different", then elaborated them came closest of 35 prompts to the variety of people working separately (Meincke et al. 2024). Specs first broadened the variety of generated designs, but an LLM judge mostly preferred the baseline (Zhang et al. 2026, preprint). [UP, C, stated. Evidence for variety, not quality]

### The machine-made look

- Anthropic says unguided output "will almost always conform to Inter fonts, purple gradients on white backgrounds, and minimal animations" (Claude blog, 2025-11-12, a vendor's account). 120 interfaces from five tools converged in appearance and layout and varied most in colour, with no human baseline for comparison (Imteyaz et al. 2026, preprint). [CH, C, stated]
- AI help makes people's output more alike: stories with AI ideas were more similar to each other (Doshi & Hauser 2024), ChatGPT users' ideas were less distinct from each other's (Anderson et al. 2024), and an image generator during ideation raised fixation (Wadinambiarachchi et al. 2024). All used lay or student participants. [SH, B, stated]
- A ban moves the default: with Inter banned, Anthropic's prompt still notes convergence on Space Grotesk, a font its own post lists as a good choice. One way out is to derive choices from something specific to the brief: content, audience, a named reference, a material, a place, the product's data or history. [CH, C. The shift is stated, the method inferred]
- A generic look is partly the sum of unchosen defaults: "templates are content agnostic" (Müller 2018), and Adam Wathan joked that his Tailwind UI `bg-indigo-500` buttons made "every AI generated UI on earth also being indigo" (2025-08-07). For each direction, list the defaults it keeps on purpose and those it overrides; a default kept by choice is valid. [CH, C, inferred]

### References

- Examples make designers copy their features (Sio et al. 2015, meta-analysis of 43 studies), even flawed features they were told to avoid (Jansson & Smith 1991, students; Sio et al. excluded flawed examples). [FP, A for copying, stated] In the same meta-analysis examples raised novelty, cut variety, and left quantity and average quality unchanged; fewer and less common examples helped more. So choose references rather than avoid them. [CH, B, stated]
- Abstract or far references can trigger reinterpretation: a reference "too literal" is "of no use" (a designer in Lucero 2012). Many designers survey competitors early, some firms avoid their own field (Herring et al. 2009), and one consultant called prior research "polluting your mind" (Crilly 2015). One option: far references to generate, near ones to check what is taken. When a reference is flawed or belongs to another brand, name the features not to reuse (Chrysikou & Weisberg 2005; disputed, `uncertainty.md`). [CH, C, inferred]
- Timing matters. Examples on request, when people knew they were stuck, gave more novel ideas than examples pushed at them (Siangliulue et al. 2015, via Vasconcelos & Crilly). Early and repeated exposure raised creativity ratings; exposure at any time raised conformity (Kulkarni et al. 2012, 81 online participants). [CH, C, stated]

### The conventional baseline

- A conventional direction done well can win when the product must be understood fast. In a Slack sprint on first-time use, "the boring, traditional approach was the clear winner — it actually explained the product to customers" (Knapp 2016). [CH, C, stated]
- Check why an option wins. Evaluators favour feasible and desirable ideas over original ones (Rietzschel et al. 2010), and under uncertainty people show an implicit bias against creativity relative to practicality (Mueller et al. 2012). In the Mozilla rebrand, early favourites were dropped, and the winning route had "sat in the background whilst all around it hogged the spotlight" (Murray & Johnson 2017). [CH, C, stated]
- A conventional direction can be the "datum" the others are compared against; Pugh's method wants one "known to be generally strong", often the market leader (Frey et al. 2009). Leave it out when the requester already has the conventional answer, or the brief is art, culture or seduction. It is an option, not a fixed slot. [UP, C, inferred]

## 3. Mechanisms that matter in every design

### Where a direction departs: furniture, core model, surface

Splitting "structure" in two gives a default for where novelty costs least, not a law. [UP, C, synth]

- Furniture: the logo and home link, where the navigation sits, search, the cart, standard controls, labels on actions. Departing here usually costs, because "users spend most of their time on other sites" (Nielsen 2000, an argument). A centred logo went with six times the failure to reach the home page in one click (Whitenton 2016, 50 users, compared across 14 different fashion sites). Hidden navigation was used less (`structure.md`), and removing text labels from email actions lowered usability (Google 2025, vendor research). [SH, B, stated]
- Core model: what the objects are and how you act on them, such as one page per thing, object then action, or a command palette. One can depart here when users return often and the new model moves irreducible complexity away from the user (Tesler). [CH, C, inferred]
- Surface: type, colour, imagery, motion, voice, art direction. Expression here leaves hierarchy, navigation and interaction intact (Moran 2017, on brutalism, an opinion piece; Apple HIG, Branding). [CH, C, stated]

Where the split breaks:
- Layers merge. Snapchat's camera "serves as a 'homepage'", left by swipes Snap called "not always intuitive". Snap said this had not yet hindered growth, perhaps because young users were "more willing to invest the time to learn" (Snap S-1, 2017, a risk statement). [C]
- Conventions move. Pull-to-refresh was one app's departure (Brichter, Tweetie 2, via MacStories 2012) and became furniture. [C]
- Returning users pay for change in any layer: Snap's 2018 redesign "negatively impacted" daily users (Snap 10-Q, Q2 2018). [C]
- The surface is not free: glass over busy content costs legibility (`languages.md`).

So keep furniture conventional by default. Depart there when the departure is the direction's idea and repays its learning cost, and say so. [CH, C, synth]

### Typicality and novelty

- For consumer products, typicality and novelty each predicted preference once the other was controlled for, and each suppressed the other: people "prefer novel designs as long as the novelty does not affect typicality" (Hekkert et al. 2003, abstract). A theory review traces the appeal of prototypes to fluency: they "are easier to process" (Reber et al. 2004). For motivated viewers, difficulty that resolves can become interest, and difficulty that does not becomes confusion (Graf & Landwehr 2015, theory). [SH, B, stated]
- For websites, studies disagree. With screenshots shown for 17 ms to 1 s, low complexity and high typicality drove appeal (Tuch et al. 2012). With 12 static screenshots and no stated time limit, novelty predicted appeal far more than typicality, less so on commercial than on service sites (Silvennoinen et al. 2025, 108 people). Stimuli, measures and viewing all differ, so why is unknown. [SH, B for each study. No reconciliation holds]
- For each direction, say what keeps it recognisable as its category and which layer carries its novelty and risk. [UP, C, inferred]

### Perception works on differences

- Search gets harder as targets resemble non-targets and as non-targets differ from each other (Duncan & Humphreys 1989), a shared region can overcome proximity (Palmer 1992), and a colour changes with its ground (Albers 1963). [FP, A, stated] So emphasis everywhere cancels out, lowering secondary items raises the primary one, and space inside a group must be clearly smaller than between groups (`visual.md`). [SH, C, inferred]

### Systems limit decisions, and the numbers are not magic

- Scales, grids and tokens work by removing choices, so repeated sizes read as deliberate levels (Bringhurst; Müller-Brockmann; Curtis 2016). No source shows that a particular ratio, the 8 px unit, the golden section or 12 columns beats another: "Modular scales are a tool, they're not magic" (Brown 2011). Choose the ratio for voice and density, and break the scale where a step looks wrong. [UP, C, stated. Any specific number: DC or UC, D]

### Posture and density

- How long and how often people use a product can set its density. Users of "sovereign" applications are "perpetual intermediates", so controls can be smaller and tighter, while "transient" applications must be "simple, clear, and to the point" (Cooper & Reimann 2003). A static menu was faster than one that rearranged itself by use (Findlater & McGrenere 2004, 27 students, one hour). [CH, C for posture. CH, B for stable menus. Stated]
- Density moves body size, scale ratio, flow granularity and complexity at once. When a brief has both expert and occasional users, a dense expert direction and a sparse guided one are a real pair of options. For a product everyone uses rarely, the dense one is not. [CH, C, synth]

## 4. Present and choose

- Show the directions side by side, each able to win, with no decoys. Pairs who shared several drafts got better-rated ads, and sharing only the best did not differ from making one (Dow et al. 2011, mostly students). Users rated a prototype higher and praised it more when they saw it alone than among three (Tohidi et al. 2006, 48 students; ratings significant for two of three designs). Ratings and click-through did not correlate (Dow et al. 2011), so say what "better" means. [SH, B, stated]
- Say what each direction is for: "Be clear about what design questions are being explored with a given prototype—and what are not" (Houde & Hill 1997). A rendering "should not suggest a degree of refinement" beyond the thinking (Buxton 2007). Mozilla's routes were called both "too 'unpolished'" and "too polished" (Murray & Johnson 2017). One option: finish directions to the same level, since the most polished wins on polish, and mark what is placeholder: copy, icons, untested states. A rough greyscale version is possible when the question is structure. [CH, C, inferred]
- Make the criteria explicit and tie them to the brief. Explicit instructions to pick original ideas raised originality but lowered satisfaction and the rated effectiveness of the picks (Rietzschel et al. 2010). Creators overvalued their own ideas but judged peers' better than managers did (Berg 2016). Let the requester choose, and do not filter out the risky option first. [SH, B, stated]
- Check your rationale against your file. About one in four rationales stated by generative UI tools did not fully appear in the interface (Imteyaz et al. 2026, preprint). Every decision you claim should be visible in the code. [UP, C, stated]
- If asked to merge: two routes put together "looked exactly like what it is: two routes mashed together" (Murray & Johnson 2017). A merge needs one new organizing idea; say what distinctiveness it costs. [UP, C, stated]
- Persistence and fixation pull apart. A concept can "only [look] more appealing because it hasn't been built yet" (a technical lead in Crilly 2015), yet experts "become readily attached to single, early solution concepts" (Cross 2004). Once a direction is chosen, push through its first problems, and name the problem that would make you drop it. [CH, C, stated. The balance is inferred]
- Feedback. Say what feedback you want and what you do not (Levin 2019, Figma). Over a third of feedback interventions lowered performance (Kluger & DeNisi 1996, meta-analysis). Check a vivid comment against the brief before it kills a direction. [UP, C, stated. "Feedback can harm": FP, A]

## 5. Order of work

- The Double Diamond was popularized to help designers "contextualize their work" and clients "understand what designers do" (Eisermann, of the Design Council team), not to record how experts work. Experts alternate breadth-first and depth-first work (Ball & Ormerod, via Cross 2004): breadth-first on easy requirements, depth-first on complex ones (Ball et al. 2010, abstract). One order that follows: a quick pass across all directions on the easy requirements, then depth on the hardest one inside each direction, where directions differ or break. Linear narrowed "hundreds of screens" to "a few major directions", then ran "stress tests" (Linear 2024). [SH, B for the alternation. The order is inferred]
