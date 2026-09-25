# Uncertainty

Read this file before citing a number, or when a finding feels too convenient. It lists where the evidence is weak, contradictory, outdated or context-bound; how conflicts between sources were settled; and figures not to repeat.

## Conflicts between sources, and how they were settled

- **Skeleton screens.** One source said they were perceived as faster; another found them rated slowest. The Viget study (136 people) was checked directly: the spinner was rated fastest and the skeleton slowest. Mejtoft 2018, the basis of NN/g's guidance, found no significant difference. **Verdict:** "skeletons feel faster" `[WC · C]`.
- **Inline vs on-submit validation.** Not a contradiction but a difference in context: a small 2009 study of sighted people on a long form, against a public service with slow typers and screen-reader users. Both sides agree: never validate mid-entry.
- **Touch targets.** A note claimed platform guidance points to 9–10 mm. Converting 44 pt and 48 dp gives about 7.3–7.6 mm. **Verdict:** every platform default is below the 9.2 mm the only cited study recommends.
- **Expert reviews and false alarms.** Studies of student analysts found about 65% of predicted problems never happened; professional teams in the CUE studies found few. **Why they differ:** the CUE studies judged validity by expert consensus, not by testing against users. **Verdict:** treat each predicted problem as a hypothesis, and state its mechanism.
- **Above the fold.** Eye-tracking put 57% of viewing time above the fold (NN/g 2018). Chartbeat found 66% of attention *below* it on article pages. **Why they differ:** different measures and page types. Both show attention decaying with scroll distance.
- **Line length.** Studies show longer lines are read faster, yet readers prefer moderate ones. **Verdict:** the performance finding `[CH · B]`; the specific 45–75 range a convention `[DC · C]`.
- **Office telemetry.** Figures of "3 billion" (talk notes) and "1.3 billion sessions" (the team's own 2006 post) both circulate. The primary figure is used.
- **Liquid Glass timeline.** Not a conflict. iOS 26.1 added a Clear/Tinted switch (2025-11). iOS 27 (announced 2026-06) added a slider and adaptive backing (verified with MacRumors).

## Labels changed in this synthesis, and why

- **Doherty's 400 ms:** C → **D**. The reprinted source contains no 400 ms figure.
- **The 1 s and 10 s response limits:** B → **C**. They trace to a conversational analogy, not to measurement. The 0.1 s limit stays **B**.
- **Hidden navigation:** kept at **B**, but many "independent" citations all rest on one NN/g study.
- **"Deceptive patterns work":** split into two findings. "Defaults and framing steer choices" is **FP · A** (a meta-analysis plus experiments). "Mild patterns work without backlash" is **SH · B** (one paper, two experiments).

## Weak or missing evidence

1. **Dense expert interfaces.** No controlled study compares expert performance on dense and sparse professional tools. Bloomberg, Linear and the Ribbon have no independent usability data.
2. **Contrast.** No contrast model, WCAG 2 or APCA, has been validated against reading performance across light and dark polarities. The WCAG 3 method is undecided (April 2026).
3. **Touch targets.** There is no modern replication of the 2006 study on capacitive phones or with motor-impaired or older users. The derivation of 24 px is not shown.
4. **WCAG coverage.** Power et al. (2012) covered WCAG 2.0 and blind users only.
5. **Hamburger menus.** The data is from 2014–16; the icon may be more familiar now.
6. **AI review.** One CHI 2024 paper and one 2025 preprint (21.2% overlap with experts). Treat an AI review as one more evaluator with the same blind spots.
7. **Redesign outcomes.** Spotify 2023, Netflix 2025 and Slack 2023 published no retention data. Backlash is not harm.
8. **Outcomes behind usage.** Monzo and Zerodha report usage, not reduced harm. Deceptive-pattern experiments measure a first choice, not long-run trust.
9. **Little or only vendor research:** tabs, accordions, bottom sheets and floating labels; the value of design systems; human-AI guidelines (validated for relevance only); the prevalence of sensitivity to UI motion.

## Unresolved

- **Spotify shuffle.** A 2014 post reportedly replaced pure random with artist spreading. The 2025 post says shuffle "was exactly that – random" for five years. The 2014 original could not be read.
- **Office Ribbon.** Its backlash is well documented; whether it beat menus on performance is not.
- **Etsy's infinite scroll.** It reduced engagement from search, but the cause was never identified.
- **Snapchat 2018.** The design's share of the drop in daily users can't be separated from competition and Android performance.
- **Excel.** Why the automatic conversions still default to on: no rationale found.
- **Canva and Figma accessibility today.** The only audit found is from 2021.

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
| 7±2 for menus; 60-30-10 colours; "every page needs a CTA"; three clicks | No supporting research |
| Sonos "$500M market value lost" | Search summary only; use "at least $100M revenue" (company) |
| "Heuristic evaluation finds X% of problems" | Depends on what is counted as all problems |
