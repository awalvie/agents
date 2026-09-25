# Skeptic log (2026-09-25)

## Changes

- core P9, products: "GOV.UK was audited as meeting WCAG 2.2 AA" → the *Design System website* was audited; the audit says nothing about services built with it.
- core P2, products: Bloomberg's CTO called navigating the growing *data* "untenable"; products.md had turned that into the vendor calling its *density* untenable.
- core P5: Grudin's calculator keypad was presented as a result ("beat"); it is task-analysis argument, not a test.
- core P1: inverted-T arrow keys now attributed to studies *cited in* Grudin, not to Grudin.
- core P7: "people stop reading warnings" → attention declines (what Vance et al. measured); added that polymorphic warnings decline less.
- core P7: added van der Sijs's own caveat that many overrides are justified, plus an action (judge alerts by specificity).
- core P8: "regulators price this in" overstated a ₹7 lakh fine; now says what happened and that Amazon settled without admission.
- core P5: Duolingo's "equivalent engagement" marked as unpublished internal metrics.
- core P3: "Wikipedia hides its menu *because* search is the main path": the cause can't be read from a screenshot, so it now describes what's shown.
- core, visual: "a container outweighs spacing" → "can override" (Palmer 1992).
- core P10: W3C low-vision document is a 2016 working draft, not a note.
- core P4, P9, P10: added review questions, because these principles gave no way to act on a screen.
- core §4: marked as synthesis (D unless a principle is cited). Cut duplicate tradeoff bullets and answers that repeated P2/P5.
- accessibility-performance: Viget text said the spinner was "rated fastest" but listed a shorter wait for the blank screen; rewritten from the source. The skeleton did worst on both measures.
- accessibility-performance, uncertainty: "Mejtoft 2018 found no significant difference" was stated as fact; the notes disagree and only the abstract was reached, so it's now marked unsettled.
- accessibility-performance: `[anti-pattern · B]` is not one of the seven kinds → `[SH · B]`. "Accessibility helps everyone" given an evidence grade.
- visual: "Dark mode is better" `[WC · A against]` → B (mostly one lab group; one daytime study found no difference). "At all ages" → younger and older adults (what was tested).
- visual, products: Wikipedia width story corrected from the RfC close (rough consensus for unlimited width) and the 2026-09 screenshot (readers still get Standard). The claim that the width control was added *after* the objections was unsupported.
- visual: Linear light-mode contrast complaint marked as seen only via search summary.
- interaction: "Users don't read" `[WC · B]` → `[WC · B against]`; carousel "always bad" given a grade; dates added to HIG, Material 3 and GitHub docs observations.
- products: added a short Revolut entry (a brief benchmark that had none); removed Things 3 from the index (no entry). Sonos figure marked as the CFO's estimate.
- tradeoffs: "most people never change settings" had no source; now hedged.
- uncertainty: added "Where the whole output leans" (NN/g, GOV.UK, first-party, era, product type) and "Gaps" (YouTube, Discord, Reddit, Amazon retail, Airbnb search, Uber, BBC, Material/Meta criticism, Indian products). Revolut fraud counts added to "do not cite".
- SUMMARY: "without annoying anyone" → no measurable backlash; "WCAG caught half" → covered half, in one study; Craigslist doesn't "thrive" (revenue fell ~70%); added the gaps and bias line.
- Bloat: cut repeats of core figures from interaction, products, accessibility, visual and uncertainty, bringing the capped files from about 12,800 words to about 12,000. Word counts are pattern-based estimates; no exact counter was available.

## Checked against the source and found sound

Viget skeletons (136; 59/74/66%) · WebAIM Million 2026 (95.9%, 56.1, 83.9%…, ARIA 59.1 vs 42) · FTC–Amazon ($1B + $1.5B, 35M, no admission, same-method cancel) · Luguri & Strahilevitz (more than twice / almost four times; mild no backlash) · Jachimowicz 2019 (58 datasets, d = 0.68) · Scheibehenne 2010 (63 conditions, N = 5,036, "virtually zero") · Power 2012 (32 users, 16 sites, 50.4%) · Guerino 2025 (21.2%, hallucinated false positives) · Hertzum 2014 (19 professionals, 33%/50%, 24–30% severity split) · Cockburn 2007 model · Abeysooriya 2021 (30.9%, 3,436/11,117) · The Register (15,841; .xls limit) · Vance 2018 (fMRI, eye tracking, three-week field test, polymorphic) · FCC Hawaii (officer believed it real; same menu; same prompt; 38 min) · van der Sijs 2006 (17 papers, 49–96%) · NN/g hidden navigation (179, 6 sites, 27/48/50%, 57/86%, 39%/15%) · NN/g flat UI (71, 9 pages, 22%/25%) · Porter 2003 (44 users, 620 tasks) · Raskin 1994 · Grudin 1989 · W3C low-vision draft 2016 · Apple summaries pause (italics, beta label, per-app) · TechCrunch on Photos tabs · GitHub Issues (1,200→700 ms, 4.7% divergence, tiers) · Linear 2026 refresh (sidebar quote) · Monzo gambling block (up to a year, note, ~100k users) · Arc letter (5.52%, 4.17%, "too different") · Bloomberg ASKB (quote, a third of 375k users) · Sonos (≥ $100M, CFO estimate) · Duolingo (NBC, "equivalent engagement", internal metrics) · Zepto (₹7 lakh, drip pricing, basket sneaking, 2026-08-05) · Wikipedia RfC close.

## Open doubts

- Mejtoft et al. 2018: the ACM and ResearchGate pages were blocked, so its result is unknown here.
- Palmer 1992 and Lane 2005: PubMed and T&F were blocked; they rest on the researchers' abstract reading.
- Sedley & Müller's "design flaw, not change aversion" line: the Google abstract page doesn't contain it; it rests on one researcher's full read.
- Whether GOV.UK's live services, as distinct from its Design System site, meet WCAG 2.2 AA: not established.
- Habituation is labelled FP · A on the wider psychology literature; the UI-warning studies cited here come largely from one research group.
- The Bloomberg "untenable" quote comes via Slashdot's summary of Wired (wired.com was blocked).
