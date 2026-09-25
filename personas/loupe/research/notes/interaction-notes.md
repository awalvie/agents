# Interaction design: structure, behaviour and patterns — research notes

Area: information architecture, navigation, search and filtering, forms, UX writing, feedback and states, error handling, undo and confirmation, defaults, input modes and platforms, onboarding and expertise, adaptation, the pattern catalogue, deceptive patterns, and AI interfaces.

Researcher's notes for the synthesis writer. Compiled 2026-09-25.

## How to read these notes

- **Labels.** Each finding carries two labels, as the brief requires: *kind of claim* (fundamental principle / strong heuristic / context-dependent heuristic / useful pattern / design convention / aesthetic preference / unsupported or weak claim) and *evidence* (A–D). A single observation about one product carries its **source type** instead.
- **Format.** Findings use a compact form of the brief's Claim / Evidence / Context / Counterevidence / Example / Labels / Implication.
- **What I read.** "Read" means I read the primary text or its abstract myself. "Via X" means I only saw the claim quoted in X. Everything I cite is listed in `sources.md`.
- **Tool limits that affected coverage:**
  - ACM DL, PIB (India) and Axios returned 403 errors.
  - Apple HIG and Material 3 pages render with JavaScript, so a plain fetch returned nothing. I read Apple HIG through its JSON endpoint instead. I only saw Material 3 in search-engine summaries.
  - PDF-to-text conversion, `gh` and compound shell commands were blocked by permissions. I read PDFs as page images instead.
  - A full-page screenshot of Apple HIG was too small to read. It is saved at `out/shots/apple-hig-tab-bars.png`, but I did not use it as evidence.
  - I could not run or log in to any app. Every product finding rests on docs, press, company posts or critics, and says which.

---

## 1. Cross-cutting foundations

### F1. Direct manipulation: keep the object visible, and make actions rapid, incremental and reversible
- **Claim.** Interfaces feel controllable when:
  - the object of interest stays visible;
  - actions are rapid, incremental and reversible;
  - pointing at objects replaces command syntax.
- **Evidence.** Shneiderman, "Direct Manipulation: A Step Beyond Programming Languages" (*IEEE Computer* 16(8), 1983). I read only summaries of it, not the paper. The reversibility part is supported independently by the undo evidence (F13) and by predictive back (F21).
- **Context.** Spatial and visual objects: canvases, maps, lists, files.
- **Counterevidence.**
  - Direct manipulation scales badly to bulk and abstract operations ("rename all files matching X"). This is why command palettes and search-to-act exist (F22).
  - WCAG 2.2 SC 2.5.7 Dragging Movements (AA) requires a single-pointer alternative to any drag. Drag-only manipulation is an accessibility failure, not just a style choice.
- **Example.** Map panning, drag-to-reorder lists. Figma's canvas is the main benchmark (not examined here; see the complex-software notes).
- **Labels.** Fundamental principle; B (the canonical paper is argument plus examples; the parts are backed by later work on undo, feedback and reversibility).
- **Implication.**
  - Give every drag a click or keyboard path.
  - Pair direct manipulation with a command layer for bulk and abstract actions.

### F2. Users start acting before they learn (the paradox of the active user)
- **Claim.** People start using software at once and skip manuals and tutorials. They settle on methods that are "good enough" even when learning would save time overall.
- **Evidence.**
  - Carroll & Rosson (1987), from observation at IBM. I saw it via Nielsen's 1998 summary.
  - Independent support comes from shortcut-adoption studies. Lane et al. (2005) found that even experienced users rarely moved to keyboard shortcuts. I saw that result only via search summaries of the paper.
  - NN/g's onboarding review (Kendrick 2020) reports that deck-of-cards tutorials did not improve task performance.
- **Context.** Holds for discretionary tools. It is weaker where training is mandated (enterprise, aviation, trading terminals).
- **Counterevidence.** Users *do* invest when the payoff is visible and immediate. Superhuman's human-led onboarding (F22) and Duolingo's practice-first start (F24) are designed around this.
- **Labels.** Strong heuristic; B.
- **Implication.**
  - Design for learning inside the task (contextual hints, shortcuts shown beside commands) rather than front-loaded instruction.
  - Treat "they'll learn it in the tutorial" as a warning sign.

---

## 2. Structure: information architecture, navigation, search and forms

### F3. The "three-click rule" is unsupported; information scent is what matters
- **Claim.** Users don't abandon a task because of the number of clicks. They abandon it when they lose confidence that they're on the right path.
- **Evidence.**
  - Porter, UIE (2003): 44 users, 620 tasks, more than 8,000 clicks. Users were no more likely to quit after 3 clicks than after 12. Satisfaction barely varied with path length (46–61%). I read this via the republished article on Center Centre's site.
  - Pirolli & Card's information-foraging theory (*Psychological Review*, 1999) gives the mechanism: people follow "scent" cues and abandon when scent weakens. I read only summaries of the paper.
- **Context.** Content-finding tasks on websites.
- **Counterevidence.**
  - In high-frequency expert workflows, click count *does* cost time (see F22).
  - The Porter study is old, one company's work, not peer-reviewed, and on 2003 sites.
- **Labels.** The three-click rule itself is an unsupported or weak claim (D). "Scent over depth" is a strong heuristic (B).
- **Implication.**
  - Judge navigation by whether each label predicts what lies behind it, not by counting clicks.
  - A tree test or first-click test measures scent. Depth alone doesn't.

### F4. Hidden navigation (hamburger) reduces discovery, especially on desktop
- **Claim.** Putting the main navigation behind a menu icon lowers how often people use it and how much content they find. The penalty is larger on desktop than on mobile.
- **Evidence.** NN/g (Pernice & Budiu, 2016): 179 participants on 6 sites, testing hidden, visible and combo navigation. Read.

  | | Hidden | Visible | Combo |
  |---|---|---|---|
  | Navigation used, desktop | 27% of cases | 48% | 50% |
  | Navigation used, mobile | 57% | not tested | 86% |

  - Task time: people were at least 39% slower with hidden navigation on desktop, and 15% slower on mobile.
  - Perceived difficulty: 2.6 hidden vs 2.1 visible (on a 1–7 scale).
  - On mobile, how visible the icon was mattered a lot. Bloomberg's menu icon looked like part of the logo and had the worst uptake (44%).
- **Context.** Content and commerce sites with many sections, and first-time users.
- **Counterevidence.**
  - On mobile, a visible alternative often costs scarce vertical space. The study didn't test visible navigation on mobile at all, so "hidden is worse on mobile" is really "hidden is worse than combo".
  - Apps with a few core destinations avoid the problem with tab bars (F18).
  - NN/g itself says the result is circumstantial.
- **Example.** In the study, SupermarketHQ and BBC led by putting salient combo navigation at the top of the page.
- **Labels.** Strong heuristic; B (one large, credible study, plus consistent expert guidance).
- **Implication.**
  - Desktop: show the navigation.
  - Mobile: show the 2–5 most-used destinations (tab bar or combo) and hide the long tail.
  - If you hide the menu, make the icon salient and label it "Menu".
  - "Hamburger menus are bad" is too broad. "Hiding *primary* navigation hurts discovery" is what the data supports.

### F5. Faceted filtering helps exploratory search; it fails when the facets don't match users' mental model
- **Claim.** Filters with visible result counts help people explore large collections and avoid dead ends. The benefit disappears for simple known-item lookups, and becomes harm when facets or metadata are poor.
- **Evidence.**
  - Hearst, *Search User Interfaces* (2009), ch. 8 (read), summarising Yee et al. (2003): 32 art-history students, about 35,000 images.
    - 91% preferred the faceted interface overall.
    - For a simple single-facet search, about 50% preferred the plain baseline.
  - Hearst names the failure conditions: facets that don't reflect users' mental model, and wrongly assigned labels.
  - Baymard's filter research (read):
    - 14% of benchmarked sites don't allow multiple values within one filter.
    - 20% don't keep applied filters visible.
    - 25% of desktop and 40% of mobile sites use unclear filter labels.
    - Base: benchmark of 343 e-commerce sites; the article is dated 2026-04-17.
  - Baymard also reports that 42% of sites don't bring applied filters to the top or highlight them. I saw this only in a search summary, not on a Baymard page.
- **Context.** E-commerce, catalogues, listings (Airbnb, Booking.com, Amazon).
- **Counterevidence.** Baymard's percentages come from expert benchmarking of sites against its own guidelines. They show how common a pattern is, not that it harms outcomes. The outcome evidence is Baymard's qualitative testing, whose method is mostly paywalled.
- **Labels.**
  - "Facets help exploration": strong heuristic; B.
  - Specific rules (applied-filter summary, multi-select, counts): useful patterns; B/C.
- **Implication.**
  - Before arguing about filter widgets, audit whether the facets match the words users use for the product.
  - Show counts and never let a filter lead to zero results without a warning.
  - Keep applied filters visible and removable in one tap.
  - On mobile, filtering in a batch with an explicit Apply button is Baymard's recommendation. That is design-system and benchmark guidance; I didn't see test data for it.

### F6. Validate on submit or after a field — never while the user is still typing
- **Claim.** Showing errors before someone has finished entering a field harms them. Whether to validate inline, after each field, or only on submit depends on context.
- **Evidence (a real contradiction between credible sources):**
  - **For inline, after-field validation.**
    - Wroblewski with Etre (*A List Apart*, 2009), read: 22 participants, six form variants. Inline validation gave:
      - +22% success;
      - −22% errors;
      - −42% completion time;
      - +31% satisfaction.
    - Validating after the user left a field ("on blur") beat validating on every keypress. Validating before and during typing was worst.
    - Caveat: within-subjects design with a small sample; the authors call the results indicative.
    - Baymard (2024, read): 31% of 343 benchmarked sites lack inline validation. Baymard warns against premature validation and against errors that persist after the user fixes them.
  - **Against.** GOV.UK Design System, validation pattern (read): "Do not validate when the user moves away from a field. Wait until they try to move to the next part of the service." The reason given is problems for slower typists. Inline validation should be added only if research shows it solves more problems than it creates.
- **Context that reconciles them.**
  - GOV.UK uses short question pages (F8), where submit-time feedback arrives almost at once and covers users with low confidence or access needs.
  - E-commerce checkouts are long pages, where finding errors only at the end is expensive.
  - Both sources agree on the core rule: don't interrupt someone mid-entry.
- **Labels.**
  - "Don't validate mid-entry": strong heuristic; B.
  - "Inline beats submit": context-dependent heuristic; C (one small study plus benchmark observation).
- **Implication.**
  - Long single-page form: validate on blur, clear the error as soon as it's fixed, and consider positive confirmation for fields that are hard to get right.
  - Short paged form: validate on submit, with an error summary.
  - Character-count limits are a sanctioned live exception (GOV.UK).

### F7. Placeholder text is not a label; labels above fields are a safe default
- **Claim.** Placeholder text that disappears as the user types:
  - forces them to remember the instruction;
  - makes it hard to review answers or fix errors;
  - can be mistaken for a pre-filled value.
- **Evidence.**
  - NN/g (Sherwin 2014, reviewed 2018; read) lists seven problems, but cites no specific study.
  - WCAG 2.2 SC 3.3.2 Labels or Instructions requires labels. (The requirement is normative; whether placeholders satisfy it is debated.)
  - The top-aligned-label claim traces to Penzo (UXmatters, 2006; read): an eye-tracking study with an unstated number of participants and short 4-field forms.
    - Labels above fields needed one eye movement (about 50 ms saccades vs about 500 ms for left-aligned labels).
    - Right-aligned labels beat left-aligned ones.
- **Counterevidence.** Penzo's study is small, stripped of context and old. Left-aligned labels help people scan long, unfamiliar forms by label. The case for placeholders is weaker than the case for top labels.
- **Labels.**
  - "Placeholder ≠ label": strong heuristic; B (mechanism plus a standard).
  - "Top-aligned labels are fastest": context-dependent heuristic; C.
- **Implication.** Always use a persistent visible label. Put format hints in hint text that stays visible, not in the placeholder.

### F8. One question per page is a good starting point for forms used by the general public, but its evidence is qualitative
- **Claim.** For forms used by the general public, one question or decision per page makes forms easier to complete. It suits people with low confidence, works on mobile, and makes errors, branching and saving progress easier to handle.
- **Evidence.**
  - Tim Paul, GDS design notes (2015-07-03; read). In the comments he says the team lacks "easy-to-share quant data".
  - Caroline Jarrett, GDS user research blog (2015-08-13; read):
    - Users "show little concern about how many pages … PROVIDED all those questions are easy to answer".
    - Accordion forms disconcerted users by appearing to grow or lose sections.
    - When "create a username" and "create a password" were put on separate pages, users didn't mind.
  - Baymard (2011; read) found that one-page vs multi-step checkout matters much less than the number and difficulty of fields.
- **Counterevidence.**
  - Frequent expert users (for example internal caseworkers) may find paging slow.
  - GOV.UK's own guidance says to start with one thing per page and merge questions when research supports it.
  - Needs fast page loads.
- **Labels.** Context-dependent heuristic; C (well-reasoned practitioner evidence from a large public-service programme, without published quantitative comparison).
- **Implication.** Choose form structure by audience and by how often people use it. Count and simplify questions first: layout is secondary to field count and field difficulty.

---

## 3. Language: UX writing and error messages

### F9. Error messages should say what happened and how to fix it, in the user's words, without blame or jokes
- **Claim.** The best error message:
  - is specific to the error;
  - tells the user what to do next ("Enter your first name");
  - is repeated identically in a summary at the top of the page and next to the field.
- **Evidence.**
  - GOV.UK Design System, error message component (read). It bans:
    - "valid/invalid";
    - "please", which implies a choice;
    - "sorry";
    - "oops";
    - blame words like "you forgot";
    - jargon like "form post error".
    - It reports that users in testing "understood what went wrong, knew how to fix the problem".
  - Nielsen's heuristic 9 ("Help users recognize, diagnose, and recover from errors") is consistent with this. It is heuristic, not experimental, evidence.
- **Context.** Holds generally. The ban on humour is strongest for high-stakes and government tasks.
- **Counterevidence.**
  - Brand voice guides (for example Mailchimp's) allow a lighter tone for low-stakes states. That is a brand choice, and I found no evidence either way on whether it helps.
  - GOV.UK's claim of testing success has no published numbers.
- **Labels.** Strong heuristic; B.
- **Implication.**
  - Write the fix, not the fault.
  - Write a different message for each distinct error.
  - Never use a generic "Something went wrong" where the system knows the cause.

### F10. Button labels should name the action, not say "Yes" or "OK"
- **Claim.** Confirmation buttons labelled with the specific action ("Delete file" / "Keep file") reduce errors compared with "Yes/No" or "OK/Cancel".
- **Evidence.**
  - NN/g (Nielsen 2018, reviewed 2026; read). It cites no study.
  - The mechanism links to habituation (F12): generic labels let people click without reading.
- **Labels.** Strong heuristic; C for direct evidence, supported by the B-grade mechanism in F12.
- **Implication.** Verb + object on every primary action, especially destructive ones.

### F11. Most people read only a fraction of a page's words
- **Claim.** On an average page view, people can read at most about 28% of the words, and more likely about 20%.
- **Evidence.**
  - Nielsen (2008; read), analysing Weinreich et al. (*ACM Transactions on the Web*, 2008): 45,237 page views from a small panel of highly literate users.
  - Each extra 100 words bought only about 4.4 more seconds.
  - The fit holds only for pages of 30–1,250 words.
- **Counterevidence.**
  - "Users don't read" overstates this. Users read selectively, and read closely when motivated (for example contracts or medication).
  - The sample was small and highly educated, and the data is from 2008.
- **Labels.** Strong heuristic ("write for scanning"); B. "Users don't read" as a blanket rule is an unsupported or weak claim.
- **Implication.**
  - Put the decision-relevant word first in labels, headings and error messages.
  - Don't bury the only copy of a critical instruction in a paragraph.

---

## 4. Behaviour: feedback, states, errors, undo, defaults

### F12. Confirmation dialogs lose their effect through repetition (habituation); vary or reserve them
- **Claim.** Repeated identical warnings and confirmations stop being read. People habituate quickly, and attention recovers only partly between sessions.
- **Evidence.**
  - Vance et al. (*MIS Quarterly* 42(2), 2018; abstract read; I didn't check the full author list): simultaneous fMRI and eye tracking over a five-day workweek.
    - Attention dropped sharply over the week, with only partial recovery between days.
    - In a three-week field experiment with mobile permission warnings, adherence fell steadily. Warnings that varied their appearance ("polymorphic") declined far less and "remained high".
  - An earlier CHI 2015 fMRI paper by Anderson et al. found the same in the brain. I saw only its title and summary.
  - Bravo-Lillo et al. (SOUPS 2013; read via summary): "attractors" that force interaction with the critical field made informed decisions 2–3 times more likely.
- **Context.** Security and permission prompts, and by extension any frequent "Are you sure?" dialog.
- **Counterevidence.** Varying a dialog's appearance also breaks consistency and learnability. That's acceptable for rare, high-risk prompts and harmful for routine ones.
- **Example.** Warnings shown on every file delete train people to click through.
- **Labels.** Fundamental principle (habituation to repeated stimuli); A (several independent studies with different methods).
- **Implication.**
  - Keep confirmations for actions that are rare, can't be undone and have high consequences.
  - For routine destructive actions, use undo instead (F13).
  - When a confirmation must work, make it break the automatic path. Examples: name the object, type the resource name (GitHub-style), or highlight what changed.

### F13. Undo beats confirmation for frequent, recoverable actions
- **Claim.** Undo lets people act at full speed and recover from slips. Confirmation taxes every action to protect against rare mistakes.
- **Evidence.**
  - NN/g (Nielsen 2018): "do go to great lengths to provide undo".
  - Shneiderman's "reversible actions" (F1).
  - The habituation research (F12) explains why confirmations fail.
  - Product evidence: Gmail's "Undo Send" ran in Labs from 2009 and became a standard setting in June 2015, with a 5–30 s window (press coverage). The mechanism is a *delay*, not a true undo: the message isn't sent until the window closes.
- **Context.** Actions the system can reverse or delay.
- **Counterevidence.**
  - Some actions can't be undone (payments sent, messages delivered to other systems, physical-world actions).
  - Time-limited undo inside a toast is fragile. It can expire before screen-reader, keyboard or distracted users reach it. WCAG 2.2 SC 2.2.1 Timing Adjustable is relevant (F16).
- **Example.** Gmail Undo Send, as described in 2015 press coverage. Source type: press. I did not read Gmail's help page this session, so the current behaviour is not checked.
- **Labels.** Strong heuristic; B.
- **Implication.**
  - Where the action is reversible, prefer soft delete, a trash folder, or delayed commit, over confirmation.
  - Make undo reachable by keyboard.
  - Don't make a toast the only way to undo.

### F14. Response-time thresholds (0.1 s / 1 s / 10 s) are useful approximations with thin direct evidence
- **Claim.**
  - Around 0.1 s feels instantaneous.
  - Around 1 s keeps the train of thought.
  - Around 10 s is the limit of attention; beyond that, show progress and allow people to do something else.
- **Evidence.**
  - Nielsen (1993, updated 2014; read) cites Miller (1968) and Card et al. (1991). He presents the thresholds as stable guidance, not as new data.
  - The popular "Doherty threshold" (400 ms) is not supported by anything I could trace to a primary source.
- **Counterevidence.** The thresholds are order-of-magnitude guides. Perception depends on expectation and on what the wait looks like (F15).
- **Labels.** Strong heuristic; B (long-standing, consistent across sources, rooted in perception research, but rarely re-tested directly).
- **Implication.** Use them as guides for when to give feedback:
  - under 0.1 s, no indicator;
  - about 1 s, a subtle busy state;
  - over 10 s, determinate progress plus a way to cancel or do something else.

### F15. How a wait is displayed changes how long it feels, but skeleton screens are not proven better
- **Claim.** The way a wait is shown changes how long it feels. The popular belief that skeleton screens feel faster than spinners is not supported.
- **Evidence.**
  - Harrison et al., "Rethinking the Progress Bar" (UIST 2007; read): 22 participants, nine progress functions, each lasting 5.5 s.
    - Bars that sped up toward the end were perceived as faster than linear bars.
    - Bars with pauses near the end were perceived as slower.
    - The authors attribute this to peak-and-end effects.
  - Skeleton screens, contradictory evidence:
    - Viget (Faulkner & Olvera, 2017; read): 136 people, animated GIFs of three loading states. Skeleton was rated *worst*: 59% agreed it was fast, vs 74% for the spinner. Perceived wait was 2.82 s vs 2.41 s.
    - Mejtoft et al. (ECCE 2018; read via abstract and summaries): skeleton rated slightly higher for perceived speed, but no significant differences; spinner users found the article faster.
- **Context.** Waits of about 1–10 s.
- **Counterevidence.** Both skeleton studies are small, used artificial conditions, and disagree with each other.
- **Labels.**
  - "The shape of progress changes perceived duration": strong heuristic; B.
  - "Skeletons feel faster": unsupported or weak claim; C (contradictory).
- **Implication.**
  - Avoid stalls near the end of a progress bar.
  - For skeleton screens, the defensible reason is layout stability and a preview of structure, not speed. Test them against a plain spinner.

### F16. Status messages must be announced without stealing focus, and must not vanish before people can act
- **Claim.** Messages like toasts and "saved" notices must reach screen-reader users without moving focus. Auto-dismissing messages that contain actions exclude slow and assistive-technology users.
- **Evidence.**
  - WCAG 2.2 SC 4.1.3 Status Messages (AA; read). Examples include "5 results returned", cart updates and submission confirmations.
  - IBM Carbon's notification guidance (read from the site's source file on GitHub):
    - toasts may auto-dismiss after 5 s;
    - toasts may include one tertiary action;
    - "ensure there are alternative routes" to that action's destination.
- **Labels.** Design convention anchored in a standard; A (normative standard; the underlying need is well established).
- **Implication.**
  - A toast may confirm something. It must not be the only place for an action, or the only notice of an error.
  - Errors belong inline, next to what caused them.

### F17. Defaults are among the most powerful design decisions
- **Claim.** Whatever is preselected is chosen far more often than alternatives. It works through perceived endorsement ("this is recommended") and endowment ("this is already mine"), more than through effort.
- **Evidence.** Jachimowicz, Duncan, Weber & Johnson (*Behavioural Public Policy* 3(2), 2019; abstract read): a meta-analysis of 58 datasets (n = 73,675).
  - Effect size d = 0.68 (95% CI 0.53–0.83).
  - Larger effects in consumer domains, weaker in environmental ones.
  - Endorsement and endowment were significant moderators; ease was not.
  - Some studies found no effect; two found negative effects.
- **Context.** All settings, opt-ins, plan selectors and consent screens.
- **Counterevidence.**
  - Defaults that people see as self-serving can backfire (the negative-effect studies). This links to the deceptive-pattern regulation in §7.
  - Hidden preselection is named as a deceptive pattern ("sneaking", "trick question") in the taxonomies and in India's 2023 guidelines.
- **Labels.** Fundamental principle; A.
- **Implication.**
  - Set defaults to what most users would choose if informed. Record why.
  - Defaults that favour the business at the user's expense are both ethically and, increasingly, legally exposed.

---

## 5. Input modes and platform conventions

### F18. Platform navigation conventions: bottom tabs on phones, rails and sidebars on larger screens; tabs are for navigation, not actions
- **Claim.** Both major mobile platforms put top-level navigation in a persistent bottom bar of a few destinations on phones. Both move it to a rail or sidebar on larger windows. Following this matters because users carry expectations between apps.
- **Evidence.**
  - **Apple HIG, Tab bars** (read via the HIG JSON endpoint, which shows a change log up to 2026-06-08). Rules:
    - "Use a tab bar to support navigation, not to provide actions."
    - Keep it visible while navigating: "If you hide the tab bar, people can forget which area of the app they're in."
    - Avoid overflow "More" tabs.
    - "Don't disable or hide tab bar buttons."
  - **Apple HIG, iOS 26 behaviour.** The iOS tab bar now floats on a Liquid Glass background and "can minimize when scrolling" when it has an attached accessory. This is in tension with the HIG's own "keep visible" rule.
  - **Material 3** (only seen via search-engine summaries of m3.material.io, not read directly):
    - navigation bar for compact windows under 600 dp;
    - navigation rail for medium and expanded windows;
    - the rail holds 3–7 items.
- **Context.** Native apps. On the web, the equivalent reasoning is F4.
- **Counterevidence.** The conventions are expectations, not proof of optimality. Apple itself now bends them (minimising bars; see F19).
- **Labels.** Design convention; B (consistent vendor guidance; the expectation is backed by NN/g's hidden-navigation data in F4).
- **Implication.**
  - Follow the platform for top-level navigation unless there is a strong, tested reason not to.
  - Put actions in toolbars, not tabs.
  - Adapt navigation by window size, not by device name.

### F19. Specimen: iOS 26 Liquid Glass — a platform owner's redesign that traded legibility and predictability for visual effect
- **Observation (as of 2026-09).** Criticisms from expert review:
  - translucent controls over content reduce legibility;
  - controls "appear, vanish, collapse, and expand depending on context";
  - touch targets are more cramped;
  - back buttons lost their destination labels;
  - some tabs moved into overflow.
- **Sources.**
  - NN/g, Budiu (2025-10-10; read). This is expert review, not user testing.
  - Press reports that Apple added a "Tinted" option in iOS 26.1 beta 4 after criticism (Gulf News; seen via search).
  - The HIG change log shows Liquid Glass guidance added 2025-07-28 and updated 2025-12-16.
  - One widely repeated claim, that the American Foundation for the Blind sent a public letter in December 2025, appears only on a low-quality aggregator. I did not verify it; do not use it.
- **Source type.** Product documentation plus an expert critique and press. No published user-testing data.
- **Mechanism.** When controls change shape or presence with scroll and context, people can no longer rely on spatial memory. This is the same mechanism behind the failure of adaptive menus (F23). The legibility loss comes from contrast depending on whatever content is underneath.
- **Implication.** Authority bias check: "Apple does it" is evidence of influence, not quality. Evaluate each behaviour against visibility and predictability.

### F20. Touch targets: WCAG's 24 px minimum is a floor; research and platform guidance point to about 9–10 mm
- **Claim.** Small targets increase errors for everyone, and severely for people with tremor or low dexterity.
- **Evidence.**
  - Parhi, Karlson & Bederson (MobileHCI 2006; read abstract), one-handed thumb use:
    - error rates stopped improving at targets of at least 9.6 mm for single taps and at least 7.7 mm for sequences of taps;
    - they recommend 9.2 mm for single taps and 9.6 mm for sequences.
  - WCAG 2.2 SC 2.5.8 Target Size (Minimum) (AA; read): at least 24×24 CSS px, or enough spacing, with five exceptions. SC 2.5.5 (AAA) asks for 44×44.
  - Apple (44 pt) and Material (48 dp) are platform conventions. I did not read their pages directly this session.
- **Counterevidence.** Dense expert tools use pointer input, where Fitts's-law costs are lower. Large touch targets there cost density.
- **Labels.** Strong heuristic; B.
- **Implication.**
  - Treat WCAG's 24 px as the legal floor and platform sizes as the working target.
  - Spacing can substitute for size.
  - Check the smallest destructive target first.

### F21. Gestures are invisible: use them as accelerators, not as the only way
- **Claim.** Swipes and other gestures lack visible cues (signifiers), so users don't discover them. Accidental activation is common.
- **Evidence.**
  - NN/g (Li, 2017; read): examples from YouTube, Spotify and B&H.
    - Reserve contextual swipe mostly for removal-type actions.
    - Provide undo or confirmation.
    - Don't make swipe meaning depend on state.
  - Android's predictive back (Android Developers docs; read) is a platform-level fix. The back gesture previews its destination as it progresses and cancels cleanly if released before the commit threshold ("undoing any state changes"). Apps targeting Android 16 get the system animations by default.
- **Labels.** Strong heuristic; B.
- **Implication.**
  - Every gesture needs a visible equivalent.
  - Destructive gestures need undo.
  - Where possible, preview before committing (the predictive-back mechanism). That is feedback plus reversibility applied to gestures.

### F22. Command systems let experts go fast, but only if they teach the shortcut along the way
- **Claim.** Most users never move from menus to shortcuts on their own (F2). A command palette that searches all commands and shows each command's shortcut creates a route from beginner to expert.
- **Evidence.**
  - Lane et al. (2005; seen via summaries only): experienced users rarely switched to shortcuts.
  - Grossman, Dragicevic & Balakrishnan (CHI 2007; abstract read): changing menu feedback and adding a small cost to menu selection significantly sped up hotkey learning.
  - VS Code docs (read): the Command Palette gives "access to all functionality" and shows keybindings next to commands.
  - Superhuman (First Round Review, 2025; read; company-reported and not independently checked):
    - human-led onboarding gave "nearly 2x activation" vs self-serve;
    - redesigning around the Inbox Zero keys ("e"/"h") raised activation from 40% to 50%.
- **Context.** Frequently used productivity tools: Linear, Figma, Slack, GitHub, VS Code, Superhuman.
- **Counterevidence.**
  - Command palettes depend on the user recalling the command name and on the product using the user's vocabulary.
  - They're weak for discovering functions the user doesn't know exist, so menus remain necessary.
  - Superhuman is "deliberately annoying to use with the mouse" (a founder-podcast quote, seen via search). That works for a self-selected expert niche and would fail a general audience.
- **Labels.** Useful pattern; B for the learning mechanism, C for product outcomes.
- **Implication.**
  - Pair every menu item with its shortcut.
  - Make a palette searchable by synonyms.
  - Keep visible menus for discovery.

---

## 6. Onboarding, learning, adaptation

### F23. Adaptive interfaces that move items hurt; ones that copy items to a predictable spot can help
- **Claim.** Interfaces that rearrange themselves destroy spatial memory. Adaptation works better when it *copies* predicted items to a dedicated area and leaves the originals in place, and when the predictions are accurate.
- **Evidence.**
  - Findlater & McGrenere (CHI 2004; read only a summary): static split menus were faster than adaptive ones. User-customisable menus were about as fast as static ones.
  - Gajos et al. (CHI 2008; read), n = 23, a "split interface" in a modified Word:
    - raising accuracy from 50% to 70% improved performance and use of the adaptive area;
    - accuracy mattered more than predictability, contrary to the authors' hypothesis;
    - both raised satisfaction.
  - Office history (Jensen Harris talk notes, UX Week 2008; read secondhand): Office's "IntelliMenus", which hid less-used items, made the UI unpredictable. The Ribbon replaced them. The team had found that users were requesting features that already existed.
- **Context.** Menus, toolbars, launchers, AI-suggested actions.
- **Counterevidence.** Adaptive features that are highly accurate and live in a separate area (recent files, "frequently used") are uncontroversial.
- **Labels.** Strong heuristic; B.
- **Implication.**
  - Never reorder primary navigation automatically.
  - Put predictions in a clearly labelled extra area.
  - Measure prediction accuracy before shipping.
  - This is the core evidence for the personalisation-vs-predictability tension (§10).

### F24. Onboarding: let people do the core task first; tutorials that front-load instruction don't help
- **Claim.** First-run experiences work best when users try the core value before being asked to commit or learn.
- **Evidence.**
  - NN/g (Kendrick 2020; read): avoid deck-of-cards tutorials; coach marks are "nice-to-have". Onboarding is justified for gathering required information, tailoring, or genuinely novel interactions.
  - **Duolingo (company sources only).**
    - Official blog (Loh, 2017; read): an A/B-tested "Streak Wager" gave +14% Day-7 retention. A "Weekend Amulet" made users 4% more likely to return a week later.
    - Mazal (former CPO, Lenny's Newsletter; read): leaderboards increased learning time by 17% and tripled the number of highly engaged learners.
    - The widely repeated claim that "delaying sign-up raised DAU/next-day retention by 20%" appears only on growth blogs. I could not trace it to Duolingo. Treat it as untraceable.
- **Counterevidence.** Duolingo's retention mechanics (streaks, guilt-tinged reminders) blur into pressure design. The same streak mechanism that motivates can coerce. This is a design tension, not settled good practice.
- **Labels.** "Value before commitment" is a context-dependent heuristic; C. Duolingo numbers: source type = company blog.
- **Implication.**
  - Delay account creation until it's needed.
  - Teach in context.
  - When reviewing gamified retention features, ask whether the user would endorse the mechanism if it were described to them plainly.

---

## 7. Pattern catalogue

The ranking is by how often a reviewer is likely to meet each pattern. This is my judgement from the product and design-system documentation read here, not measured (label: D).

| Rank | Pattern | Works when | Fails when | Key evidence |
|---|---|---|---|---|
| 1 | **Modal dialog** | Short, blocking decisions that need an answer now (unsaved changes, destructive confirm) | Used for content, marketing or long forms; stacked modals; poor focus management; on mobile, a small box over a large page | Habituation (F12). GOV.UK has had "Modal dialogue" open on its backlog since 2018-01-12 and publishes no modal component (read). Summaries of that thread report polyfill failures on IE11 and iOS Safari with screen readers (not verified in the thread text). |
| 2 | **Toast / snackbar** | Non-critical confirmation of something the user just did | Carries the only copy of an error or action; disappears before AT users hear it | WCAG 2.2 SC 4.1.3; Carbon (F16) |
| 3 | **Tabs** | A few clearly labelled, parallel sections, the first most relevant; no need to compare across | Sequential steps; comparison across tabs; too many tabs | GOV.UK: "Tabs hide content… not everyone will notice them"; "This component has not yet been tried in research with users" (read) |
| 4 | **Accordion** | Regular users jumping to a known section; an overview of many sections | Content everyone needs; forms (sections "grow"); nesting | GOV.UK: "Test your content without an accordion first" (read); Jarrett 2015 on accordion forms |
| 5 | **Hamburger / hidden nav** | Long-tail destinations on mobile | Hiding primary navigation, especially on desktop | NN/g 2016 (F4) |
| 6 | **Sticky header / nav** | Long pages where navigation or key actions are needed repeatedly | Eats mobile height; **covers focused elements**, which fails WCAG 2.2 SC 2.4.11 Focus Not Obscured (Minimum), AA | WCAG 2.2 (read) |
| 7 | **Infinite scroll** | Homogeneous feeds browsed without a goal | Goal-directed finding, comparison, returning to a place, reaching the footer; keyboard and screen-reader users | NN/g (Neusesser 2022; read). Etsy (McKinley; read): users with infinite scroll clicked, favourited and bought fewer items *from search*. Follow-up tests of "more items" and "faster results" separately explained little. McKinley doesn't identify the cause; the "lost place on Back" explanation is other people's hypothesis. |
| 8 | **Pagination / Load more** | Finding and comparison; stable places to return to | Casual browsing (adds interaction cost) | NN/g 2022 recommends Load More as a middle ground |
| 9 | **Carousel (auto or manual)** | Few items with a strong first slide; exploration where swiping is expected (media rows) | Hero banners hiding content that stakeholders fought over | Runyon (Notre Dame, 2012–13; read): about 1% of visitors clicked ND.edu's carousel, 84% of those on slide 1. Other sites: 1.7–2.3% clicks, first slot 40–62%. **Caveat:** one university's analytics; not a study. One auto-forwarding carousel had an *8.8%* click rate, which cuts against the simple "never auto-rotate" rule. |
| 10 | **Bottom sheet / drawer** | Mobile filters, secondary detail while keeping context | Nested sheets; conflicts with system gestures; unclear dismissal | Baymard mobile filter guidance (F5). I found no strong independent research on sheets. |

Carousel labels: "hero carousels get little engagement beyond slide 1" is a context-dependent heuristic, C. The claim sometimes attributed to NN/g that carousels are "always bad" is an unsupported or weak claim.

---

## 8. Deceptive patterns

### F25. Deceptive patterns are common, measurable, and work best when they are mild
- **Claim.** Deceptive patterns are widespread in commerce. Mild versions substantially change choices without provoking backlash, and hit less-educated users hardest.
- **Evidence.**
  - Mathur et al. (CSCW 2019; abstract read), a crawl of about 53K product pages on about 11K shopping sites:
    - 1,818 instances of 15 types in 7 categories;
    - 183 sites engaged in outright deception;
    - 22 third parties sold dark patterns as turnkey products.
  - Luguri & Strahilevitz (*Journal of Legal Analysis* 13, 2021; read the abstract plus a summary of the Oxford Academic version), n = 1,963 US adults:
    - control acceptance 11.3%;
    - mild patterns about 25–26%;
    - aggressive patterns about 37–42%.

    The two versions I saw give different figures: 25.4/37.2 in Brignull's book vs 25.8/41.9 in the OUP summary. The published abstract says "more than twice" and "almost four times".
    - Aggressive patterns aggravated participants; mild ones did not.
    - In Study 2, hiding information and trick questions were the most potent. Scarcity had no significant effect.
- **Context.** Subscriptions, checkouts, consent flows.
- **Counterevidence.** Mathur's crawl measures how common patterns are, not harm. The experiments are single-shot hypothetical sign-ups.
- **Labels.** Fundamental principle ("interface framing and friction steer choices"); A (a large crawl plus several experiments and meta-analytic default evidence, F17).
- **Implication.** The review question is not "is this persuasive?" but whether it:
  - hides information;
  - misleads;
  - creates asymmetric friction between the business-preferred and user-preferred choice;
  - or shames the user.

### F26. Taxonomy: use the ontology of Gray et al. (2024)
- **Evidence.** Gray, Santos, Bielova & Mildner (CHI 2024; read).
  - It harmonises 10 regulatory and academic taxonomies into a three-level ontology of 64 types.
  - Five high-level types: **obstruction, sneaking, interface interference, forced action, social engineering** (urgency, scarcity and social proof are grouped under social engineering).
  - Nagging, from Gray's 2018 set, persists as a pattern.
  - Brignull's original (2010) catalogue at deceptive.design is the practitioner root.
- **Labels.** Useful pattern (as a vocabulary); B.
- **Implication.** Name findings at the low level (for example "confirmshaming", "hard to cancel"). Map them to the high level when explaining harm.

### F27. Regulation now treats specific UI patterns as unlawful; the landscape differs by jurisdiction (as of 2026-09)
- **United States.**
  - FTC v. Amazon settled 2025-09-25 (FTC press release; read): $1B civil penalty plus $1.5B redress, about 35M consumers, no admission of liability.
  - The order bans decline buttons like "No, I don't want Free Shipping". It requires a clear decline button and cancellation through the same method as enrolment.
  - The FTC's "Click-to-Cancel" rule was **vacated** by the Eighth Circuit on 2025-07-08, on procedural grounds, before taking effect (law-firm alerts; read via search). Enforcement continues case by case under existing law (ROSCA).
- **United Kingdom.** The CMA secured binding commitments in 2019-02 from Booking.com, Expedia, Agoda, Hotels.com, ebookers and trivago (read via a law-firm summary). The sites committed to:
  - no false impressions of scarcity or popularity (for example "others are looking" must say they may be searching different dates);
  - disclosing paid ranking;
  - showing all compulsory fees.
- **India.** CCPA "Guidelines for Prevention and Regulation of Dark Patterns, 2023", notified 2023-11-30 (read via Mondaq; the government PIB page was blocked). They name 13 patterns:
  - false urgency, basket sneaking, confirm shaming, forced action, subscription trap;
  - interface interference, bait and switch, drip pricing, disguised advertisement;
  - nagging, trick question, SaaS billing, rogue malware.

  They were issued under the Consumer Protection Act 2019, with no penalty specific to the guidelines.
- **EU.** The Digital Services Act (Art. 25) codifies "dark patterns". I saw this only via Gray et al.
- **Labels.** Source type: regulator documents and legal commentary.
- **Implication.** For Indian and EU/UK-facing products, drip pricing, false urgency and asymmetric cancellation are compliance issues, not only UX issues.

---

## 9. AI and conversational interfaces

### F28. The 18 Guidelines for Human-AI Interaction were validated for relevance and clarity, not for their effect on outcomes
- **Evidence.** Amershi et al. (CHI 2019; read in full).
  - Built from more than 150 recommendations, turned into 18 guidelines grouped as:
    - **Initially:** G1 make clear what the system can do; G2 make clear how well.
    - **During interaction:** G3 time services based on context; G4 contextually relevant info; G5 social norms; G6 mitigate social biases.
    - **When wrong:** G7 efficient invocation; G8 efficient dismissal; G9 efficient correction; G10 scope services when in doubt; G11 make clear why.
    - **Over time:** G12 remember recent interactions; G13 learn from behaviour; G14 update and adapt cautiously; G15 granular feedback; G16 convey consequences of user actions; G17 global controls; G18 notify about changes.
  - Validation: 49 HCI practitioners ran a modified heuristic evaluation of 20 products in 10 categories, producing 785 examples (313 applications, 277 violations). Then 11 experts reviewed the revisions.
  - **Most-violated relative to how often it was relevant:** G11 (explain why), G2 (how well), G17 (global controls).
  - **Least clear:** G5 and G6.
  - **Stated limits:**
    - all participants were recruited through one large company;
    - some guidelines are hard to judge in one session (G10, G14);
    - voice and sensor products fit poorly;
    - high-stakes domains may need specialised guidelines.
  - The study did **not** test whether following the guidelines improves user outcomes.
- **Labels.** Useful pattern set / strong heuristics; B for relevance, D for outcome effects (untested in this paper).
- **Implication.** Use the list as a review checklist, with G2, G9, G11 and G17 as the most informative checks. Don't cite it as proof that a guideline improves trust or performance.

### F29. Explanations can increase over-reliance on AI; confidence cues and forcing functions help, at a cost
- **Claim.** Explaining an AI output tends to raise acceptance *whether or not the AI is right*. Uncertainty cues and designs that make people think first reduce over-reliance, but users like them less.
- **Evidence.**
  - Bansal et al. (CHI 2021; abstract read): explanations "increased the chance that humans will accept the AI's recommendation, regardless of its correctness". They didn't produce human-AI teams that outperform both alone.
  - Zhang, Liao & Bellamy (2020, arXiv; abstract read): confidence scores helped people calibrate trust. Local explanations did not. Calibration alone didn't improve decisions unless humans had complementary knowledge.
  - Buçinca, Malaya & Gajos (2021, arXiv; abstract read), n = 199: cognitive forcing functions reduced over-reliance but got lower satisfaction ratings. They helped people high in "need for cognition" more.
  - Kim et al. (FAccT 2024; abstract read), n = 404, pre-registered, medical questions: first-person hedges ("I'm not sure, but…") lowered agreement with the system and *raised* accuracy.
- **Context.** AI-assisted decisions; LLM answers.
- **Counterevidence.** Lab tasks with fictional systems; effects may shrink with familiarity. Forcing functions slow down every interaction.
- **Labels.** Strong heuristic ("explanations aren't automatically calibrating"); A–B (several independent studies agree in direction).
- **Implication.**
  - Show *how sure* the system is, in plain language or as alternatives. Google PAIR recommends categorical labels or N-best lists over raw percentages (PAIR Guidebook; read).
  - Keep explanations short and actionable.
  - Add friction only where errors are costly.

### F30. Specimens: AI output presented with the same authority as source content
- **Apple Intelligence notification summaries.**
  - Paused for News & Entertainment apps in the iOS 18.3 betas (announced 2025-01-16/17) after the BBC complained about a false headline presented as a BBC notification.
  - Apple's fixes: italic styling to mark summaries as AI, a "beta" label, and per-app control from the Lock Screen.
  - Source type: press (Silicon Republic; read). Apple's statement is quoted there.
  - Mechanism: the AI summary had the same visual weight as a real publisher notification. The fixes map to G2 (signal quality), G17 (global/per-app control) and G18.
- **Google AI Overviews, May 2024.**
  - The "glue on pizza" and "eat rocks" errors.
  - Google's response (Reid, 2024-05-30; read): the errors came from "data voids" and satirical or forum sources. Google added limits on which queries trigger an Overview, and reduced reliance on user-generated content.
  - Google said content-policy violations occurred in fewer than 1 in 7 million queries showing an Overview. Its method isn't described, so don't treat the figure as verified.
  - Source type: company blog.
  - Mechanism: G10 (scope services when in doubt). Answering was the default even when the evidence was thin.
- **Implication.** Visually separate generated content from sourced content. Let users see the sources. Suppress generation when evidence is weak.

---

## 10. Product specimens (short entries)

**Sonos app (iOS/Android), 2024 redesign.**
- *Demonstrates:* shipping a rewrite that removed working features.
- *Evidence:* press and a secondary analysis (Roger Wong 2025, drawing on Bloomberg, The Verge and staff interviews; M. Tsai, quoting the CEO's apology of 2024-07-25). Removed at launch 2024-05-07: queue editing, playlist management, sleep timers, local-library search. Accessibility regressed. Sonos's market value fell about $500M (search summary), and CEO Spence left in January 2025. Interim CEO Conrad: "…just not enough when our customers' alarms don't go off."
- *Mechanism:* a platform rewrite tied to a hardware launch date. Warnings from staff were overridden.
- *Lesson:* experienced users measure a redesign by lost capability, not visual quality. Never remove a habitual task in a forced update.

**Snapchat, 2018 redesign.**
- *Demonstrates:* re-sorting a navigation model against users' established mental model.
- *Evidence:* press (CNBC, Variety; read via search). A Change.org petition drew about 1.2M signatures. Spiegel said the aim was to make the app easier, especially for older users. DAU went from 191M to 188M in Q2 2018.
- *Confound:* competition from Instagram Stories. I can't isolate the redesign's causal effect.

**Microsoft Office Ribbon (2007).**
- *Demonstrates:* a telemetry-led IA overhaul that replaced adaptive menus.
- *Evidence:* Harris talk notes (secondhand). About 3 billion sessions of telemetry. Menus grew from about 50 to 300 items, and Word went from 2 toolbars (1989) to 30 (2002). People requested features that already existed. The design was tested longitudinally.
- *Where it fails:* initial backlash from experts whose spatial memory was reset. Whether the Ribbon *outperformed* the old menus is less documented than the backlash. This is an open question.

**Amazon Prime enrolment and cancellation (to 2025).**
- *Demonstrates:* obstruction and confirmshaming at scale (F27). Source type: regulator documents.

**GOV.UK Design System.**
- *Demonstrates:* openly saying what hasn't been researched. The Tabs page says the component "has not yet been tried in research with users"; the Accordion page lists open research gaps.
- *Lesson:* a design system's publication is not proof. Check each component's research section.

**Linear, VS Code, Superhuman.** Keyboard-first expert tools; see F22. Source type: docs and company-reported numbers.

**Duolingo.** Retention by game mechanics; see F24. Source type: company blog.

---

## 11. Design tensions

- **Discoverability vs simplicity** (F4, F21, F22).
  - Hiding functions lowers visual load and discovery together.
  - What matters: how often a function is used and who uses it. Hide the long tail, not the core.
  - Evidence: B.
- **Personalisation vs predictability** (F23, G14 in F28).
  - Adaptation helps when it is accurate and additive (copied items).
  - It hurts when it moves things. Beginners lose less from adaptation than experts with spatial memory do.
  - Evidence: B.
- **Error prevention vs speed** (F12, F13).
  - Confirmations protect rare cases and tax every case.
  - Undo shifts the cost to the rare case. Only possible where actions can be reversed.
- **Inline help vs interruption** (F6).
  - Timely feedback helps; premature feedback harms.
  - Page length and audience decide between inline and submit-time validation.
- **Automation vs control** (F28–F30).
  - Proactive AI saves effort and risks error at scale.
  - Mitigations: scope when in doubt, global controls, visible differentiation.
  - Users rate forcing functions lower even when they work. Satisfaction and accuracy diverge.
- **Business vs user goals** (F25–F27).
  - Mild manipulation "works" without visible backlash. That is why regulators, not satisfaction metrics, are what's constraining it.
- **Platform consistency vs brand/novelty** (F18, F19).
  - Following conventions buys transferred learning.
  - Even the platform owner's own novelty (Liquid Glass) drew usability criticism.

## 12. Open questions and weak evidence

1. **Skeleton screens vs spinners.** Contradictory small studies (F15).
2. **Tabs, accordions and bottom sheets.** Little published outcome research. GOV.UK says so for tabs.
3. **Liquid Glass.** No published user-testing data as of 2026-09. Only expert review and press.
4. **Duolingo's "delayed sign-up +20%".** Untraceable.
5. **Ribbon vs menus.** Did performance improve? Public data is thin.
6. **Human-AI guidelines.** Not validated for outcomes (F28). Over-reliance findings are from lab tasks.
7. **Carousels.** Evidence is mostly single-site analytics. The auto-forwarding counter-signal (8.8%) is unexplained.
8. **Placeholder vs floating labels.** Floating labels are common; I found no rigorous comparison.
9. **Infinite scroll at Etsy.** The negative result is solid as an A/B test, but its cause was never identified.
10. **Gesture-only navigation (Android, iOS).** Adoption and error data aren't public.

## Outside my area

- **Visual design:** Liquid Glass legibility is mainly a contrast and visual-hierarchy question (F19). Hand it to the visual/accessibility notes.
- **Accessibility:** WCAG 2.2 also added 3.3.7 Redundant Entry (A), 3.3.8 Accessible Authentication (Minimum) (AA), 3.2.6 Consistent Help (A) and 2.4.13 Focus Appearance (AAA). WCAG 2.2 was published 2023-10-05, and 4.1.1 Parsing was removed.
- **Performance:** the Etsy slowed-results experiment ("absolutely nothing happened" to purchases, per McKinley) is a counterexample to "every millisecond costs conversions". It was one site in about 2012; worth checking against the performance notes.
- **Business context:** the Superhuman onboarding economics (about $650k ARR per specialist, $60–130k cost; company-reported) are in the First Round Review piece.
