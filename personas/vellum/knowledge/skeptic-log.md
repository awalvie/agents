# Skeptic log, v1 to v2

Checked on 2026-09-26 against raw pages, PDFs or publisher abstracts, read with `curl` and `pdftotext`, not a summarising fetch tool. The research notes were not reread; claims were checked against their sources.

## The synthesis agent's own frameworks

- Three layers (furniture, core model, surface): kept as a default, labelled synth. Added counterexamples where it breaks: Snapchat's camera-as-homepage navigation (Snap S-1), pull-to-refresh becoming furniture (MacStories 2012), and Snap's 2018 redesign costing daily users (10-Q). Furniture departures are now an option with a stated condition.
- Typicality and novelty reconciled by exposure time: cut. Tuch's typicality effect held at 500 and 1000 ms, and Silvennoinen states no viewing time. The disagreement is now reported as unexplained.
- Axes of difference: kept as synth, with a note that no source tests which axes spread best.
- Dense and sparse pair: kept as synth, limited to briefs with both expert and occasional users.

## Changes to core.md

- Dorst & Cross: "same concept" changed to the same core idea with different designs; "frame through sketches" dropped (not in the paper); label B to C.
- Acar et al.: the inverted U is measured for slack and time pressure, not only proposed. Moreau & Dahl's time-pressure condition added.
- Liikkanen & Perttula: "same default solution" changed to the review's "self-similar solutions".
- Fricke: label B to C (one study, second-hand).
- Girotra: "spread matters more than average" is not in the paper; changed to all four drivers, with its own spread data inconclusive.
- Crilly "count as one": marked as inference; the quote is about working alone.
- GDS exercise: reworded to the source's aim, how many typefaces and sizes were needed.
- Dow 2011 borrowing: it was from drafts, not finished alternatives, and was not linked to results.
- Meincke: the list, bolder, elaborate steps are one chain-of-thought prompt, not two methods.
- Zhang preprint: an LLM judge mostly preferred the baseline; "quality uncertain" was too soft.
- Imteyaz: added that there is no human baseline; 25% is "did not fully appear".
- Homogenisation studies: participant pools noted (lay or student).
- Wathan post: noted as a joke.
- Sio et al.: examples did not raise quality, and the meta-analysis excluded flawed examples. Flaw-copying now cited to Jansson & Smith only.
- Herring: some firms avoid their own field; the audit is one designer's account. Crilly's "polluting" quote is about prior work in general.
- Kulkarni: conformity rose at any timing, not only late. Added its missing source entry.
- Knapp: "onboarding" changed to first-time use.
- Dow 2010 "experienced designers rated better": removed. They were 14 non-professionals, and the diversity gap was small.
- Mozilla "hogged the spotlight": reversed in v1. The winning route was the one in the background.
- Pugh datum: added the source's advice that the datum be a strong, often market-leading concept.
- Nielsen 2000: marked as an argument, not data. Google 2025: marked as vendor research.
- Hekkert: effects hold only once the other variable is controlled, and the stimuli were consumer products.
- Reber: marked as a theory review. Graf & Landwehr: "time" dropped; interest needs the difficulty to be resolved.
- Duncan & Humphreys: restated as search difficulty. Palmer: "capable of overcoming" proximity, not "stronger than".
- Cooper & Reimann: quotes added. Findlater & McGrenere: "location learning for frequent users" is not in the paper; now 27 students, one hour.
- Tohidi: 48 students, paper prototypes; significant for two of three designs.
- Buxton, Lucero, Murray & Johnson: "polish draws detail comments, rough invites direction" is in none of them; rewritten from what Buxton, Houde & Hill and Mozilla say. "HTML cannot be rough" removed.
- Rietzschel: "familiar" changed to "desirable"; the cost includes rated effectiveness. Mueller: implicit bias relative to practicality.
- Berg: creators overvalue their own ideas but judge peers' ideas better than managers do.
- Levin (Figma): "name the decision" and "diagnose, not instructions" are not in the article; replaced with its advice to state the feedback wanted and not wanted.
- Cross "unbuilt looks better": moved to Crilly, where the quote is. Persistence and fixation shown as a tension.
- Eisermann: the Design Council popularised the Double Diamond, for designers as well as clients. Ball & Ormerod credited for breadth and depth.
- Removed the states bullet from section 5, since `structure.md` covers states.
- Imperatives softened to options where the evidence is C or a preprint, including equal finish for all directions.
- Whitenton: noted that the comparison was across different sites. Space Grotesk: noted that Anthropic's own post recommends it. Surface bullet SH to CH. The three counterexamples labelled C, and the Snap growth statement marked as a company risk statement.
- Cut for length: the empty-states bullet, the Wallace and Dyson preference sentence (it is in `visual.md`), and the history of the three-layer split.

## Changes to topic files

- structure.md: Katsanos sample added; the Findlater repeat replaced by a pointer to `core.md`; "different primary scheme" and the command-palette warning softened to options; Yee 29 of 32 (paper says 90% and 91%); Rosenfeld-based findings B to C (textbook, snippets); Baymard B to C; Findlater corrected; Sellen sample added; Bederson was a flat space, not zoomable, and only reconstruction improved; Etsy bought fewer from search, not overall; the Etsy advice labelled inferred.
- visual.md: line-length results split between Dyson & Haselgrove and Dyson & Kipping; Rello significant only against 18 pt, and 24 px is from the blog; Wallace readers tried 5 of 16 fonts; Palmer wording; Stripe "at least five"; Linear's contrast is a variable, not an LCH value; colour routes widened past two; Piepenbrock size effect moved to the 2014 paper; Cooper's reason for a narrow palette added; first-glance times corrected; "use smaller body text only when" and the icon-set rule softened; colour routes without a source marked synth. Cut for length: "so the cost of a very broad top level is a trend" (structure.md), and *Every Layout*'s fractional-pixel point (code.md).
- languages.md: Moran 2017's three null pairs were gaze patterns, one not sparse; Moran 2016 sample; Google's "look so similar" was the team's own question; Chimero's next sentence added; Alegria quote attributed to Xoana Herrera; Chayka credits aspirational listings; Linear wording and Inter Display; brutalism quote tied to brutalism; Müller's cultural-institution point marked inferred; GOV.UK "serves users best" changed to "chose restraint"; "fail for tasks" softened, since Gumroad is a counterexample; a visionOS claim citing "Brown, NN/g 2024" removed, since it had no source entry; "keep these effects off text" and "distinctive through rigour" softened to options; the expression bullet SH to CH; "sit on top of shared regularities (Tuch; Hekkert)" cut for length.
- code.md: anchor positioning moved out of the newly-available tier (`web-features` says limited; caniuse says partial); Tailwind dropped `ui-sans-serif` too, because of a Yu Gothic UI bug; Barvian "at most 2.5 times"; Houde & Hill wording; a chosen font may be embedded, not only served.
- uncertainty.md: v1's MAYA correction was itself wrong and is fixed; the "trust direction over size" advice was attributed to Vasconcelos & Crilly but is not in the review; added disputes, a bias section and gaps.
- sources.md: listed which sources were read raw; added Kulkarni, Siangliulue, Dyson & Kipping, Ball & Ormerod, Snap S-1, Snap 10-Q and MacStories; fixed dates and titles.

## Checked and found sound

Anthropic blog quotes and Space Grotesk; Fricke via Cross; Dow 2011 share multiple and ratings against click-through; Kohn & Smith; Doshi & Hauser; Anderson et al.; Wadinambiarachchi; Zahner; Siangliulue; Whitenton 6x; Nielsen 2000 quotes; Google labels, "strong minority", helter-skelter; Moran 22% and 25%; Tesler; Kluger & DeNisi; Frey on Pugh; van Nues & Overkamp; Ball et al.; Linear "hundreds of screens" and "stress tests"; Terrett road signs and icons; McCarthy; Apple HIG Branding, four quotes; Houde & Hill; Müller on templates and stereotypes; Hawley quote text; Rutter on Bringhurst; Pernice & Budiu figures and "4 or fewer"; Larson & Czerwinski; Arditi & Cho; Brown 2011; Reinecke & Gajos; Romaniuk et al.; Nielsen 2004 on card sorts; GOV.UK 19 px body; Material motion patterns; MacRumors Tinted setting; Budiu 2025 as expert review; 45 support tiers against `web-features` 3.40.0; `ui-sans-serif` Safari-only.

## Open doubts

- Abstract only: Hekkert, Graf & Landwehr, Palmer, Rietzschel, Kohn & Smith, Ball et al., Moreau & Dahl, Piepenbrock. Full texts could change the wording.
- Girotra was read in its 2009 working paper, not the published version.
- Snap's accounts of its own navigation are company statements. No independent data shows the furniture departure caused or survived growth.
- Not rechecked: Suwa et al., Carroll & Carrithers, Heer & Robertson, Tversky et al., Schloss & Palmer, McDougall, Wiedenbeck, Nielsen 2010, Boulton, Hurff, Aalen, and most of `code.md`'s practitioner sources. Their wording is as v1 had it.
- Lindgaard et al. (2006) could bear on whether first impressions persist, but no open copy was reachable, so it is not cited.
- A second agent reviewed the diff; its corrections are applied. Its suggestion to move this log out of `v2` was not taken, because the task puts it there.
