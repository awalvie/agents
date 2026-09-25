# Interaction: structure, behaviour, language

Read this file when a review involves navigation, search, forms, wording, feedback, errors, gestures, expert tools, onboarding, personalisation, deceptive patterns or AI features. Labels as in [core.md](core.md).

## Structure

**Navigation.**
- Judge navigation by whether each label predicts what lies behind it, not by counting clicks.
  - "Scent over depth" `[SH · B]`.
  - Three-click rule `[WC · D]`.
  - A medium breadth and depth beat the flattest structure (Larson & Czerwinski 1998). Piling up ambiguous choices to save depth makes things worse.
- **Hidden navigation.** On desktop, hidden navigation was used in 27% of cases, against 48–50% when it was visible or combined. On mobile it was 57%, against 86% combined (NN/g 2016) `[SH · B]`. Visible navigation was not tested on mobile, so the mobile result compares hidden with *combined* navigation.
  - Fix: show the 2–5 most-used destinations and hide the rest behind a control labelled "Menu" (GOV.UK) `[UP · C]`.
  - Failure mode: an icon that blends into the logo. Bloomberg's menu icon had the worst uptake in the study, at 44%.
- **Platform navigation.** On phones, both platforms put top-level navigation in a bottom bar; on larger windows, a rail or sidebar (Apple HIG; Material 3) `[DC · B]`.
  - Tabs are for navigation, not actions. Apple: "If you hide the tab bar, people can forget which area of the app they're in."
  - Apple's own iOS 26 tab bars shrink on scroll, which breaks that rule. Follow the principle, not the vendor.
  - Choose navigation by window size, not device name.

**Search and filtering.**
- Filters with visible result counts help people explore large collections. For a simple lookup of one known item, about half of users preferred the plain interface (Yee et al. 2003, in Hearst 2009) `[SH · B]`.
- The most common failure is facets that don't match users' words or mental model. Audit the vocabulary before the widgets.
- Baymard's benchmark of 343 sites (2026) found 20% don't keep applied filters visible and 14% don't allow several values in one filter `[UP · B/C]`. These figures show how common a practice is, not what it costs.
- Patterns: warn before a filter would return zero results; keep applied filters removable in one tap.

**Forms.**
- **Labels.** Use a persistent visible label, not placeholder text. Placeholders vanish, tax memory and look like entered values `[SH · B]`. Labels above fields suit short forms (Penzo 2006, small eye-tracking study) `[CH · C]`.
- **Validation timing.** The evidence conflicts, and the conflict has a reason.
  - For inline validation: validating after each field gave 22% more success and 42% less time than validating on submit (Wroblewski 2009; 22 people, one form). Validating *while* typing was worst.
  - Against: GOV.UK validates only on submit, because checking as the user leaves a field hurts slower typists, and screen-reader announcements at that moment are unreliable.
  - Both agree: never validate mid-entry `[SH · B]`.
  - Long single-page form (a checkout): validate after each field, and clear the error the moment it's fixed.
  - Short paged form for the general public: validate on submit, with an error summary.
  - "Inline beats on-submit" in general: `[CH · C]`.
- **One question per page** suits infrequent, high-stakes public forms `[CH · C]`. GOV.UK says it lacks shareable numbers. Users "show little concern about how many pages" if each question is easy (Jarrett 2015). The number and difficulty of fields matter more than one-page versus multi-step (Baymard 2011). Paging is slow for people who enter data every day.

## Language

- **Error messages.** Say what happened and how to fix it, in the user's words, and repeat the same text in the summary and beside the field. No "invalid", "oops" or blame (GOV.UK) `[SH · B]`. Never write "Something went wrong" when the system knows the cause.
- **Buttons.** Name the action ("Delete file", "Keep file"), not "Yes/OK". Generic labels feed habituation `[SH · C]`, backed by the `B` mechanism.
- **Reading.**
  - People read at most about 28% of a page's words on an average visit (Weinreich et al. 2008). Eye-tracking repeatedly finds scanning unless the reader is motivated `[SH · A]`. "Users don't read" `[WC · B]`: motivated readers read everything.
  - The F-shaped scan is a symptom of poor formatting, not a layout to design for (NN/g 2017).
  - Write for scanning (the key word first, headings with meaning) *and* for close reading where a decision is made.
- **Every page needs a CTA** `[WC · D]`. Every page needs a next step toward the user's goal, which may be none. A promotion-styled box is ignored anyway: banner blindness `[SH · B]`.

## Behaviour

**Feedback and states.**
- Status messages ("5 results", "Saved") must reach screen readers without moving focus (WCAG 2.2 SC 4.1.3) `[DC · A]`.
- A toast may confirm something. It must never be the only place for an action or an error. Toasts that disappear (Carbon: after 5 s) can vanish before keyboard or screen-reader users reach them.
- Design every state: empty, loading, partial, error, success, offline.

**Errors, undo and confirmation.** See [core.md](core.md) P7. In short:
- Prefer soft delete, a trash folder or a delayed commit to a confirmation. Gmail's Undo Send is a delay: the message isn't sent until the window closes (press, 2015).
- Make undo reachable by keyboard.
- Reserve confirmations for rare, irreversible actions, and label them with the object and the verb.
- Show the actual content being committed (the Hawaii lesson).

**Defaults.** Preselected options win (d = 0.68). Set them to what most users would choose if informed, and record why `[FP · A]`. A hidden preselection that favours the business is "sneaking" in the deceptive-pattern taxonomies and in India's 2023 guidelines.

**Silent transformation.** Make automatic changes to user data visible and undoable at the moment they happen. Fail loudly at limits. Excel's four automatic conversions are still on by default, and "JAN 1" may still turn into a date with the option off (Microsoft Support, 2026-09) `[SH · B]`.

## Input modes

- **Direct manipulation.** Keep the object visible and make actions quick, step-by-step and reversible (Shneiderman 1983) `[FP · B]`. Every drag needs a single-pointer alternative (WCAG 2.2 SC 2.5.7). Pair it with a command layer for bulk and abstract operations ("rename all").
- **Gestures.** Nothing on screen shows a gesture exists. Use gestures as accelerators with a visible equivalent. Put undo on destructive swipes. Prefer a preview before commit, like Android's predictive back, which cancels cleanly if released early `[SH · B]`.
- **Touch targets.** See [accessibility-performance.md](accessibility-performance.md).
- **Eyes-busy contexts.** For frequent critical functions, a fixed physical control beats a touchscreen menu.
  - A magazine test at 110 km/h: 10 s for four tasks in a 2005 car with buttons, 44.6 s in the worst modern car (Vi Bilägare 2022; method thinly reported).
  - Since 2026, Euro NCAP requires physical controls for indicators, hazard lights, horn, wipers and SOS for top ratings.
  - `[SH · C]`, backed by a safety body's rule.
- **Keyboard shortcuts** that use single characters must be possible to switch off (WCAG 2.1.4). GitHub offers this.

## Expertise and learning

- **Onboarding.**
  - Let people do the core task before asking them to learn or commit. Swipe-through tutorial cards did not improve task performance (NN/g 2020) `[CH · C]`.
  - Canva starts from templates; a goal-based onboarding branch raised design creation by 10% (vendor case study, C).
  - Delay account creation until it is needed. The popular "Duolingo delayed sign-up, +20%" figure is untraceable; don't cite it.
- **Path from novice to expert.** Show shortcuts beside commands, offer a palette that also accepts synonyms, and keep the menus.
  - Superhuman shows the cost of a pure expert interface: human-led onboarding gave nearly twice the activation of self-serve (company-reported, 2025).
- **Engagement mechanics.**
  - Streaks work: Duolingo reports small significant lifts, such as +1.7% seven-day retention from new streak animations (team blog, 2022). They measure return visits, not learning.
  - Add forgiveness (Duolingo's streak freeze), and pair engagement metrics with outcome metrics `[UP · C]`.
  - Ask whether users would endorse the mechanism if it were described plainly.

## Personalisation and adaptation

- Never reorder primary navigation automatically.
- Put predictions in a separate, labelled area (recent files, "for you"), and measure their accuracy first. Accurate adaptation that adds items helps; adaptation that moves items destroys spatial memory `[SH · B]`.
- User-controlled layouts avoid most of the cost: Revolut 10 (2023) lets users choose their navigation and widgets.
- Personalised assets optimise a proxy. Netflix's per-member artwork raises plays, but in 2018 it drew complaints that it featured minor Black actors in films with white leads (The FADER). Require personalised imagery to represent the item truthfully `[UP · C]`, with a documented failure mode.

## Pattern catalogue (with failure modes)

Ordered by how often a reviewer meets them. The ordering is judgement `[D]`; the evidence is per row.

| Pattern | Use when | Fails when | Evidence |
|---|---|---|---|
| Modal dialog | A short blocking decision is needed now | It holds content, marketing or long forms; modals stack; focus isn't trapped and returned. GOV.UK still publishes no modal component (backlog open since 2018) | Habituation `[FP · A]` |
| Toast | Confirming something the user just did | It is the only copy of an error or action; it expires too soon | WCAG 4.1.3; Carbon |
| Tabs | A few parallel, clearly labelled sections, with no need to compare across them | Steps in a sequence; comparison; many tabs. GOV.UK: "not everyone will notice them" and "not yet been tried in research with users" | `[DC · C]` |
| Accordion | Regular users jumping to a known section | Content everyone needs; forms, whose sections seem to grow | GOV.UK: "test your content without an accordion first" |
| Hidden menu | Rarely used destinations on mobile | It hides primary navigation, especially on desktop | NN/g 2016 `[SH · B]` |
| Sticky header | Long pages that need repeated actions | It eats mobile height, or covers the focused element (fails WCAG 2.4.11) | Standard |
| Infinite scroll | Homogeneous feeds browsed without a goal | Finding, comparing, returning to a place, reaching the footer, keyboard use. At Etsy, users clicked, favourited and bought fewer items from search; the cause was never found | A/B test, one site `[CH · C]` |
| Load more / pagination | Finding and comparing; stable places to return to | Casual browsing | NN/g 2022 |
| Carousel | A few items with a strong first slide; media rows where swiping is expected | Hero banners that hide content stakeholders fought over. About 1% of visitors clicked one university's carousel, and 84% of those clicks were on slide 1 (Runyon 2013) | Single site `[CH · C]`. "Always bad" `[WC]` |
| Bottom sheet | Mobile filters; detail that keeps context | Sheets nested in sheets; clashes with system gestures; unclear dismissal | No strong research |
| Command palette | Frequent users; large command sets | Users who don't know a feature exists; vocabulary mismatch | `[UP · B]` |

**Anti-patterns**, each covered above or in [core.md](core.md): ad-styled important content; placeholder as label; validating while the user types; "Are you sure?" on routine deletes; controls that appear and vanish (Liquid Glass); self-rearranging menus; gesture-only actions; toast-only errors; silent data conversion; test and live modes in one menu; redesigns that remove relied-on capabilities (Sonos); login walls between search visitors and content (Pinterest).

## Deceptive patterns

- **Vocabulary.** Use Gray et al.'s 2024 ontology (64 types) `[UP · B]`. At the top level: obstruction, sneaking, interface interference, forced action, social engineering. Name findings at the low level ("confirmshaming", "hard to cancel"), then map them to the high level to explain the harm.
- **Review question.** Not "is it persuasive?" but: does it hide information, mislead, make the user's preferred choice harder than the business's, or shame the user?
- **Regulation, as of 2026-09.** Drip pricing, false urgency and asymmetric cancellation are compliance issues, not just UX issues.
  - **US.** The FTC's Amazon order (2025-09-25) requires a clear decline button (not "No, I don't want Free Shipping") and cancellation by the same method as sign-up. The Click-to-Cancel rule was vacated on 2025-07-08; enforcement is case by case.
  - **EU and UK.** Amazon Prime has had two-click cancellation in the EU since 2022-07; the Digital Services Act, Art. 25, addresses dark patterns. The CMA's 2019 hotel-site commitments cover paid ranking, compulsory fees and false scarcity.
  - **India.** The CCPA's 2023 guidelines name 13 patterns, including drip pricing, basket sneaking and subscription traps; fines followed in 2026-08.

## AI and generated content

- **Guidelines.** Microsoft's 18 Guidelines for Human-AI Interaction (Amershi et al. 2019) were checked for relevance and clarity, not for their effect on outcomes `[UP · B relevance, D outcomes]`. The most informative checks:
  - G2: make clear how well the system works;
  - G9: make correction efficient;
  - G11: explain why;
  - G17: give global controls.
- **Explanations can increase over-reliance.** They raised acceptance "regardless of correctness" (Bansal et al. 2021). Confidence cues helped calibrate trust. First-person hedges ("I'm not sure, but…") raised accuracy (Kim et al. 2024). Forcing people to think first reduced over-reliance but lowered satisfaction (Buçinca et al. 2021). `[SH · A–B]`
  - Show how sure the system is, in words or as alternatives. Add friction only where errors are costly.
- **Keep generated content visibly apart from sourced content, and suppress it when the evidence is thin.**
  - Apple paused AI summaries of news notifications (2025-01) after a false headline appeared styled as a BBC notification. Its fixes were italics, a beta label and a per-app control.
  - Google limited when AI Overviews appear after the "glue on pizza" answers (2024-05). It blamed "data voids" and satirical sources.
