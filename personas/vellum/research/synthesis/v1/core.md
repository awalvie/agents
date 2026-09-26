# Core: from requirements to directions

Read this every time. It covers how to get from a brief to directions that really differ, how to choose, and the mechanisms that apply to every design. Labels are explained in `README.md`.

## 1. Turn the brief into constraints

- Make the directions differ in their frame, what the design is fundamentally about, before styling. Designers reach a frame through early solution sketches and invent requirements as they sketch (Dorst & Cross 2001; Cross 2004; Suwa et al. 2000). [SH, B, stated]
- The first clever idea a brief suggests is usually the idea everyone reaches. All nine experienced designers in Dorst & Cross (2001) produced the same concept from salient facts in the brief, and each thought it original. Keep it if it is right, but label it the expected direction and make the others depart from it. [UP, C, stated]
- Reduce the requirements to a few binding constraints: audience, the one job, real content, platform, posture (section 3), and how much complexity the product can afford. A constraint helps when it removes the default answer and leaves room to search, and hurts when it removes the room; time pressure removes the search itself (Acar et al. 2019, a review; Moreau & Dahl 2005; Basecamp, *Shape Up* 2019). [SH, B, inferred. The inverted-U curve in Acar is a proposal, not a measurement: CH, C]
- A brief with no context makes every direction fall back on the same default solution (Liikkanen & Perttula 2008, via Vasconcelos & Crilly 2016). Ask for the missing context, or write the assumption down. [CH, C, stated]
- Abstract problem statements gave more original ideas, and concrete ones gave ideas that fit the constraints better (Zahner et al. 2010, via the same review). [CH, C, stated]
- Before any layout, write a ranked list of each key screen's content (a "priority guide", van Nues & Overkamp 2018) and share it across all directions, so they differ in form, not in what they forgot. [CH, C, inferred]

## 2. Generate directions that really differ

- Decide the axes of difference before you design anything. A balanced search beats both one idea and a flood of variants: engineers who made very few concepts fixated, and those who made very many spent their time managing variants (Fricke 1996, via Cross 2004). No source gives a right number of directions. [CH, B, stated]
- The goal is the best direction, so spread matters more than average quality (Girotra et al. 2010). Two directions that share one core principle count as one (a consultant in Crilly 2015). [SH, B, stated]
- Axes that produce real difference: the frame; the structure (scheme, root navigation model, flow granularity, modes: `structure.md`); posture and density; the tradition (`languages.md`); which layer carries the novelty; and a self-imposed constraint, such as type only, no imagery, or one typeface at one size in black and white. GDS used the last one as an exercise to find which variation GOV.UK really needed (Terrett 2012). [UP, C, synth]
- Generate each direction on its own, not by revising the previous one. Iteration improves a concept but keeps its first idea (Dow et al. 2009; Dow et al. 2010). Seeing other ideas during generation narrows the range (Kohn & Smith 2010; Girotra et al. 2010). Borrow between directions only after each one exists. Borrowing between finished alternatives went with better results (Dow et al. 2011). [SH, B, stated. The split between "during" and "after" is inferred]
- Write each direction as a short spec before any markup: frame, axioms, scales, colour roles, type pairing, layout idea, and the defaults it keeps. Two methods have a measured effect on the variety of AI output, and both separate the choice of direction from the build. One is to list many short ideas, then push them to be bold and different, then elaborate. With GPT-4 this nearly matched the variety of humans who worked separately (Meincke et al. 2024). The other is to propose structured design specs first and build one (Zhang et al. 2026, a preprint). Variety broadened, but the quality gain was uncertain (abstract checked). [UP, C, stated. One preprint and one idea-generation study]

### The machine-made look

- Unguided, an AI takes the most probable choice at each step. Anthropic says unguided output "will almost always conform to Inter fonts, purple gradients on white backgrounds, and minimal animations", because safe choices "dominate web training data" (Claude blog, 2025-11-12, checked on the raw page). A 2026 preprint found that 120 interfaces from five tools converged in look and in layout, and varied most in colour (Imteyaz et al., abstract checked). [CH, C for interfaces, stated]
- AI help makes people's ideas more alike. Writers with AI ideas produced stories more similar to each other (Doshi & Hauser 2024), and ChatGPT users' ideas were less distinct from each other's (Anderson et al. 2024). Related: GPT-4 idea pools were less diverse than pools from people working alone (Meincke et al. 2024), and an image generator during ideation raised fixation and lowered the variety of ideas (Wadinambiarachchi et al. 2024). [SH, B, stated]
- A ban moves the default instead of removing it: after banning Inter, Anthropic's own prompt notes convergence on Space Grotesk (same page). So do not start from a list of things to avoid. Derive each choice from something specific to the brief: the content, the audience, a named reference, a material, a place, the product's own data or history. [CH, C. The shift is stated, the method is inferred]
- A generic look is largely the sum of the defaults that nobody chose: the browser's, a framework's, a template's. Müller (2018) blames content-agnostic templates. Adam Wathan (2025-08-07, checked through a mirror of the post) blamed his Tailwind UI `bg-indigo-500` buttons for "every AI generated UI on earth also being indigo". For every direction, list the defaults it keeps on purpose and the ones it overrides; a default kept by choice is a valid decision. Compare the directions with each other too, because they can drift to the same default. [CH, C, inferred]

### References

- Designers copy the features of examples they see, flaws included, even when told not to (Jansson & Smith 1991 and many replications; Sio et al. 2015, a meta-analysis). [FP, A, stated] In the same meta-analysis, examples also raised the novelty and quality of ideas. So do not avoid references. [CH, B, stated]
- Use far-domain, partial or abstracted references to generate ideas, and near competitors only to check what is taken and what is conventional (Lucero 2012; Herring et al. 2009; Vasconcelos & Crilly 2016). When a reference is flawed or belongs to another brand, name the features not to reuse (Chrysikou & Weisberg 2005; disputed, see `uncertainty.md`). [CH, C, inferred]
- Timing matters too. Examples given on request, when a designer knows they are stuck, gave more novel ideas than examples pushed at them (Siangliulue et al. 2015, via Vasconcelos & Crilly). Early and repeated exposure improved creativity ratings, and late exposure only raised conformity (Kulkarni et al. 2012). [CH, C, stated]

### The conventional baseline

- A conventional direction done very well often wins when the product must be learned fast or fits a well-known category. In a Slack onboarding sprint, "the boring, traditional approach was the clear winner — it actually explained the product" (Knapp 2016, checked on the archived page). Experienced designers made less diverse ads that were rated better (Dow et al. 2010). [CH, C, stated]
- Check why it won. People pick the familiar option even when originality is the goal (section 4), and in the Mozilla rebrand the early favourites "hogged the spotlight" and were later dropped (Murray & Johnson 2017). [CH, C, stated]
- When one is included, it can serve as the "datum" the others are judged against (Pugh's method; Frey et al. 2009). Leave it out when the requester already has the conventional answer, or when the brief is art, culture or seduction. It is an option for the set, not a fixed slot. [UP, C, inferred]

## 3. Mechanisms that matter in every design

### Three layers: furniture, core model, surface

The structure notes say a distinctive product departs in its core model. The languages notes say keep structure conventional. Both hold once "structure" is split in two (synth):

- Furniture: the logo and home link, where the navigation sits, search, the cart, standard controls, labels on actions. Keep it conventional. Users spend most of their time on other sites (Nielsen 2000). A centred logo made users about six times as likely to fail to reach the home page in one click (Whitenton 2016, 50 users, fashion sites only). Removing text labels from email actions lowered usability (Google 2025, company research). Weak signifiers cost time except on sparse, conventional pages (`languages.md`). [SH, B, stated]
- Core model: what the objects are and how you act on them, such as one page per thing, object-then-action, or a command palette. Depart here when users return often and the new model clearly moves complexity from the user into the system (Tesler's law of conservation of complexity). [CH, C, inferred]
- Surface: type, colour, imagery, motion, voice, art direction. Put expression here and keep hierarchy, navigation and interaction intact (Moran 2017; Apple HIG, Branding; Microsoft 2013). [SH, C, stated]
- The mechanism. Typicality and novelty both raise appeal, and each suppresses the other. People "prefer novel designs as long as the novelty does not affect typicality" (Hekkert et al. 2003, abstract checked: expertise did not change the balance). A typical design is processed fluently, and fluency feels like beauty at first sight (Reber et al. 2004). When people are motivated and have time, difficulty can become interest instead of displeasure (Graf & Landwehr 2015). [SH, B, stated]
- When the balance shifts. At 17 to 50 ms, typicality and low complexity drove appeal (Tuch et al. 2012, checked in the paper). With time to look at 12 websites, novelty predicted appeal more strongly than typicality, and counted for less on sites that sell things (Silvennoinen et al. 2025, checked in the paper). Read together: a glance, risk and money favour typicality, and attention and time make room for novelty. [SH, B for each study. The reconciliation is synth]
- For each direction, say what keeps it recognisable as its category and which layer carries its novelty and risk. [UP, C, inferred]

### Perception works on differences

- One mechanism is behind hierarchy, grouping and colour. A target stands out as far as it differs from its neighbours and the neighbours resemble each other (Duncan & Humphreys 1989). Items group by relative closeness and by shared regions (Gestalt research; Palmer 1992). A colour looks different on different grounds (Albers 1963). [FP, A, stated]
- So emphasis everywhere cancels out, lowering secondary items raises the primary one, space inside a group must be clearly smaller than space between groups, and every colour must be judged on its real ground (`visual.md`). [SH, C, inferred]

### Systems limit decisions, and the numbers are not magic

- Type scales, spacing scales, grids, ratios and tokens all work by removing choices, so repeated sizes read as deliberate levels and the product as one system (Bringhurst; Müller-Brockmann; Curtis 2016; *Every Layout*). No source shows that a particular ratio, the 8 px unit, the golden section or 12 columns beats another. Choose the ratio for voice and density, and break the scale where the eye says a step is wrong. [UP, C, stated. Any specific number: DC or UC, D]

### Posture and density

- How long and how often people use a product sets its density. A tool people live in can be dense, because its users become intermediates; one they visit briefly must be obvious and sparse (Cooper & Reimann 2003). Layouts that rearrange themselves by use break location learning for frequent users (Findlater & McGrenere 2004). [CH, C for posture. SH, B for stable layouts. Stated]
- Density moves many choices at once: body size, the type scale's ratio, flow granularity, visual complexity. A dense expert direction and a sparse guided direction are a real pair of options for one brief, each with its own structure. [CH, C, synth]

## 4. Present and choose

- Show the directions side by side as real alternatives, each able to win, with no decoys. "Share multiple" beat "share best", and "share best" did not differ from making one design (Dow et al. 2011), so showing only the best of several seems to lose most of the gain (inferred). Users rate a design higher and criticise it less when they see it alone (Tohidi et al. 2006). Ratings and click-through did not agree in Dow et al. (2011), so say what "better" means. [SH, B, stated]
- Finish steers critique: polish draws comments on details, rough work invites questions about direction (Buxton 2007; Lucero 2012; Murray & Johnson 2017). HTML cannot be rough, so make the directions differ in frame, finish them to the same level (the most polished wins on polish), and say for each which decisions are intended and which are placeholders: copy, icons, untested states (Houde & Hill 1997). [CH, C, inferred]
- Make the criteria explicit and tie them to the brief. Assume your favourite is overrated and the strangest direction underrated. Evaluators pick feasible and familiar ideas even when originality is the goal (Rietzschel et al. 2010; Mueller et al. 2012). Telling them to pick original ideas worked, at a cost to their satisfaction (Rietzschel). Creators overrate their own ideas (Berg 2016). Preference does not predict reading speed (Wallace et al. 2022; Dyson 2004). Let the requester choose, and do not filter out the risky option first. [SH, B, stated]
- Check your rationale against your file. In one 2026 preprint, over 25% of the design rationales written by generative UI tools were not implemented in the interface (Imteyaz et al., abstract checked). Every decision you claim should be visible in the code. [UP, C, stated]
- If asked to merge: two routes pasted together "looked exactly like what it is" (Murray & Johnson 2017). A merge needs one new organizing idea that carries the chosen strengths. Say what distinctiveness it costs. [UP, C, stated]
- Once a direction is chosen, push through its first problems: an unbuilt alternative looks better because it is unbuilt (Crilly 2015; Cross 2004). [CH, B, stated]
- Feedback. Name the decision it should inform, treat comments as problems to diagnose, not instructions, and check a vivid comment against the brief before it kills a direction (Levin 2019 at Figma; Murray & Johnson 2017). Over a third of feedback interventions lowered performance (Kluger & DeNisi 1996). [UP, C, stated. "Feedback can harm": FP, A]

## 5. Order of work

- The Double Diamond was made to explain design to clients (Eisermann, its co-creator). Experts alternate between breadth-first and depth-first work (Cross 2004). A sensible order: a quick pass across all directions on the easy requirements, then depth on the hardest requirement inside each direction, where directions really differ or break (Ball et al. 2010). Linear's redesign narrowed hundreds of screens to a few directions, then "stress tested" the concept (Linear 2024, team account). [SH, B, stated. The order is inferred]
- In each direction, show the key screen's empty, loading and error states next to the ideal one. Directions often differ most there (`structure.md`). [SH, C, inferred]
