# Uncertainty

Read this file before citing a number, or when a finding feels too convenient. It lists where the evidence is weak, contradictory, outdated or context-bound; how conflicts between sources were settled; where the whole output leans; and figures not to repeat.

## Conflicts between sources, and how they were settled

- **Skeleton screens.** Viget (136 people, checked directly) rated the skeleton worst; Mejtoft 2018, NN/g's basis, was read only at abstract level and the notes disagree on its result. **Verdict:** "skeletons feel faster" `[WC · C]` ([accessibility-performance.md](accessibility-performance.md)).
- **Inline vs on-submit validation; touch-target sizes.** Settled in [interaction.md](interaction.md) and [accessibility-performance.md](accessibility-performance.md).
- **Expert reviews and false alarms.** Student analysts: about 65% of predicted problems never happened. Professional CUE teams: few false alarms, but judged by expert consensus, not by testing against users. **Verdict:** treat each predicted problem as a hypothesis and state its mechanism.
- **Above the fold.** Eye-tracking put 57% of viewing time above the fold (NN/g 2018); Chartbeat found 66% of attention *below* it on article pages. Different measures and page types; both show attention decaying with scroll distance.
- **Office telemetry.** "3 billion" (talk notes) against "1.3 billion sessions" (the team's own 2006 post). The primary figure is used.

## Labels changed, and why

- **Doherty's 400 ms:** C → **D**. A researcher read the reprinted source; it contains no 400 ms figure.
- **The 1 s and 10 s response limits:** B → **C**. They trace to a conversational analogy, not to measurement. The 0.1 s limit stays **B**.
- **Hidden navigation:** kept at **B**, but many "independent" citations all rest on one NN/g study.
- **"Deceptive patterns work":** split. "Defaults and framing steer choices" is **FP · A** (a meta-analysis plus experiments); "mild patterns work without backlash" is **SH · B** (one paper, two experiments).
- **"Dark mode is better":** evidence against A → **B** (skeptic pass). The data read come mainly from one lab group, and one daytime study found no difference.

## Where the whole output leans

- **One research house.** Hidden navigation, signifiers, reading, the F-pattern, onboarding, banner blindness and skeleton advice all rest on single NN/g studies. Consistent with each other is not independent.
- **GOV.UK as the model.** It is the main example of good forms, errors and plain design, yet its research is asserted, not published, and it serves infrequent public tasks. Don't carry its patterns to daily-use expert tools unexamined.
- **First-party evidence.** Most product "results" (Linear, GitHub, Pinterest, Duolingo, Monzo, Arc, Figma) are the company's own write-ups. They show mechanism, rarely outcome.
- **Era.** Many anchor studies are 1998–2012 (Porter 2003, Parhi 2006, Wroblewski 2009, Power 2012); newer replications are rare.
- **Product type.** Mostly web and SaaS tools, with few games, native desktop apps or small independent products, and almost no voice or TV interfaces.

## Gaps: brief topics not covered well enough to use

- **Rule-breakers named in the brief but not studied:** YouTube, Discord, Reddit (old vs new), Amazon's retail pages. Don't cite them as counterexamples from this output.
- **Search, transactions, real-time status:** Airbnb search, maps and booking; Booking.com's current screens; Uber's ride flow; Stripe Checkout; notifications. Only business-side criticism was researched.
- **Accessibility systems:** BBC GEL was unavailable; Microsoft and Apple's own apps have no audit here; Canva (current), Figma, Linear and Bloomberg are not assessed.
- **Onboarding** in Notion and Figma; **criticism of Material Design and Meta products** beyond Instagram's 2022 test; **Indian products** beyond Zerodha, Zepto and Razorpay (Groww and CRED have no first-party writing or data).

## Weak or missing evidence

1. **Dense expert interfaces.** No controlled study compares expert performance on dense and sparse professional tools; Bloomberg, Linear and the Ribbon have no independent usability data.
2. **Contrast.** No model, WCAG 2 or APCA, is validated against reading performance across polarities; the WCAG 3 method is undecided (April 2026).
3. **Old or narrow anchors:** touch targets (one 2006 stylus-era study), WCAG coverage (WCAG 2.0, blind users only), hidden navigation (2014–16 data).
4. **AI review.** One CHI 2024 paper and one 2025 preprint. Treat an AI review as one more evaluator with the same blind spots.
5. **Outcomes.** Redesign backlash (Spotify 2023, Netflix 2025, Slack 2023) came with no retention data, and Duolingo's "equivalent engagement" is unpublished; Monzo and Zerodha report usage, not reduced harm; deceptive-pattern experiments measure a first choice, not long-run trust.
6. **Little or only vendor research:** tabs, accordions, bottom sheets, floating labels; the value of design systems; human-AI guidelines (validated for relevance only); prevalence of sensitivity to UI motion.

## Unresolved

- **Spotify shuffle.** A 2014 post reportedly replaced pure random with artist spreading; the 2025 post says shuffle "was exactly that – random" for five years. The 2014 original could not be read.
- **Causes not separable or not found:** whether the Ribbon beat menus on performance; why Etsy's infinite scroll cut engagement; the redesign's share of Snapchat's 2018 drop; why Excel's conversions default to on; why Wikipedia readers still get Standard width after a 2023 vote for unlimited width.

## Do not cite these figures as fact

| Figure | Problem |
|---|---|
| "53% abandon after 3 s" | No definition or method; ad-industry source |
| "Doherty threshold 400 ms" | Not in the source |
| "35% of adults over 40 have vestibular dysfunction", used for UI motion | It measures a balance test |
| "Delayed sign-up +20%" (Duolingo) | Untraceable |
| "90% of feature requests already existed" / "90% use 10% of features" (Office) | No method |
| "Optimistic UI cuts perceived wait 40%" | Untraceable |
| "20% more taps on 'MENU'" | One site, seen only second-hand |
| Netflix "82% of focus on artwork", "1.8 s per title" | No method or sample |
| Netflix "80% of hours from recommendations" | Seen only quoted; the paper was not read |
| Pinterest "40% wait / +15% SEO / +15% sign-ups" | Seen only quoted (the 60%/40% figures were read directly) |
| Google AI Overviews "fewer than 1 in 7 million" | No method |
| Razorpay "abandonment reduced 100%" | Implausible; no baseline |
| Revolut "most fraud reports of any UK bank" | Not normalised by customers or volume |
| 7±2 for menus; 60-30-10 colours; "every page needs a CTA"; three clicks | No supporting research |
| Sonos "$500M market value lost" | Search summary only; use "at least $100M revenue" (company estimate) |
| "Heuristic evaluation finds X% of problems" | Depends on what is counted as all problems |
