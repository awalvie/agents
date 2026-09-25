# Core: principles, review framework, tradeoffs

Read this before every review.

**Labels.** Every finding carries `[kind · evidence]`.
- Kinds: **FP** fundamental principle, **SH** strong heuristic, **CH** context-dependent heuristic, **UP** useful pattern, **DC** design convention, **AP** aesthetic preference, **WC** unsupported or weak claim.
- Evidence: **A** several independent studies or replicated real-world data; **B** one credible study, or consistent expert guidance with some data; **C** practitioner reports or single cases; **D** opinion, or nothing traceable.
- A single observation of one product carries its source type and date instead, for example "(team blog, 2024)" or "(screenshot, 2026-09)".

**The idea behind everything below.** Most famous UX rules are real findings stripped of their context; the "always", "never" and "X maximum" versions fail. Review with *mechanisms* (what the user must see, know, remember, decide and recover from), not slogans.

---

## 1. Ten principles

### P1. "Intuitive" means familiar. Borrow what users already know, and make every new concept pay for itself.
- **Mechanism.** People read a new interface through the ones they already know (Carroll & Rosson 1987). An intuitive interface is one that matches something familiar (Raskin 1994). Layouts that look typical for their category are liked more at first sight (Tuch et al. 2012). `[SH · B]`
- **Products.** Dropbox added no new concept: it was a folder that syncs (founder, Hacker News 2007). Flighty copied airport departure boards (Apple "Behind the Design", 2023). Arc is the counter-case: in its own data, 5.52% of daily users regularly used more than one Space, and the team called it "too many new things to learn, for too little reward" (team letter, 2025-05).
- **Counterexamples and when not to follow it.** Daily-use expert tools (Bloomberg, Excel, Superhuman) must be learned, and it pays back; fund the teaching, as Superhuman did with one-to-one onboarding. Familiar is not optimal: studies found the inverted-T arrow keys more usable than the layout experts preferred (cited in Grudin 1989).
- **Review question.** Count the new concepts. For each one, name the reward and who gets it.

### P2. Give everyone a path that works by recognition, give frequent users a faster path from memory, and show the faster path inside the slower one.
- **Mechanism.** Recognising an option is easier than recalling it `[FP · A]`. Novices scan menus item by item. Experts pick from memory, so the number of items matters mostly to novices (Cockburn, Gutwin & Greenberg 2007). Users settle on methods that are good enough and rarely move to shortcuts unprompted (Carroll & Rosson 1987; Lane et al. 2005, 251 Word users) `[SH · B]`.
- **Pattern.** Menus that show each command's shortcut, and a command palette that searches every command and shows its key (VS Code, GitHub, Linear). Showing shortcuts in menu feedback sped up hotkey learning (Grossman et al. 2007). `[UP · B for the learning mechanism, C for product outcomes]`
- **Counterexample.** Bloomberg is recall-first and fast for trained users, yet its CTO says navigating its growing data "has become more and more untenable", and it is testing a chat interface (Wired via Slashdot, 2026-04). A palette can't surface features users don't know exist, so keep the menus.
- **When not to follow it.** Services people use once or twice (tax, passports). Don't build recall paths there; make recognition excellent.

### P3. Match visibility to frequency of use. Hide the rarely used tail, never the core.
- **Mechanism.** People follow cues that suggest they are on the right path ("information scent") and give up when those cues fade (Pirolli & Card 1999). Hidden things carry no scent.
- **Evidence.**
  - On desktop, hiding the main navigation cut its use from 48–50% of cases to 27% and slowed people by at least 39% (NN/g 2016, 179 people, 6 sites) `[SH · B]`. Many sources repeat this, but it is one study.
  - Weak clickable cues cost 22% more time (NN/g 2017, 71 people) `[SH · B]`.
  - The three-click rule has no study behind it. In Porter's 2003 test, people were no more likely to quit after 3 clicks than after 12 `[WC · D]` for the rule.
- **Products.** Apple removed the tabs from Photos in iOS 18 and restored them in iOS 26 after complaints (TechCrunch, 2025-06). GOV.UK's mobile menu button says "Menu" in words (screenshot, 2026-09).
- **When not to follow it.**
  - Search-led products. Wikipedia keeps its main menu behind an icon on desktop and leads with a wide search box (screenshot, 2026-09).
  - Small screens with many destinations: show the top 2–5 and label the rest.
- **Review question.** What is hidden, how often is it needed, and what signals that it exists? Count the steps where the user is unsure, not the clicks.

### P4. Count what users must remember and decide, not what they can see.
- **Mechanism.**
  - Working memory holds about four chunks (Cowan 2001) `[FP · A]`.
  - Menus are recognition, not recall, so "limit menus to 7±2 items" misapplies Miller `[WC · B against]`.
  - Across 63 conditions, the average effect of "too much choice" was "virtually zero" (Scheibehenne et al. 2010). Choice overload appears only when options are hard to compare, preferences are unclear and no option stands out (Chernev et al. 2015) `[CH · A]`.
- **So density is not the enemy.** Dense screens work when the visual hierarchy ranks what matters. Linear dimmed its sidebar to let content lead (team blog, 2026-03). GitHub, Excel and Bloomberg are dense on purpose. Showing fewer elements can *raise* load when it moves needed information off-screen.
- **Pattern.** Carry earlier choices forward on screen, put comparisons side by side, and recommend a default instead of cutting options.
- **When not to follow it.** First-time users scanning an unfamiliar list pay a cost for every item. Shorten lists there.
- **Review question.** What must the user carry from one screen to the next, and which options can't they compare side by side?

### P5. Skill is built on things staying where they are and behaving the same way. Change by adding, not by moving.
- **Evidence.** Menus that rearranged themselves did worse than static ones. Adaptation helped when its predictions were accurate and it *copied* items into a separate area (Findlater & McGrenere 2004; Gajos et al. 2008) `[SH · B]`. Office replaced its self-hiding menus with the Ribbon.
- **Backlash to a redesign comes in two kinds.**
  - *Transition cost* to a product that is at least as good. It fades. Duolingo kept its 2022 learning path after a backlash; its CEO cited "equivalent engagement" in unpublished internal metrics.
  - *Regression*: lost capability, speed or access. It does not fade. Sonos's 2024 app removed features and broke VoiceOver; the company reported at least $100M in lost revenue. Figma dropped floating panels because "they slowed people down".
  - Google's definition supports the split: if something is hard to learn or use, the cause is a design flaw, not change aversion (Sedley & Müller 2013). `[SH · C]`
- **Consistency is a means, not the goal.** Consistency with what users already know speeds learning `[SH · B]`. "Always be consistent" is `[WC · B against]`. Grudin (1989) argued from task analysis, not a test, that a keypad with + beside Enter suits data entry better than the tidy + − × ÷ row.
- **When not to follow it.** When the old structure has hit its limit (Word had grown to about 30 toolbars). Then change boldly, measure experienced users separately, and keep a way back.

### P6. Feedback must match the length of the wait, and must tell the truth about what happened.
- **Timing.** About 0.1 s feels instant `[SH · B]`. About 1 s keeps the train of thought, and about 10 s is the limit of attention `[SH · C]`; these two are reasoned estimates, not measured breakpoints (Nielsen 1993, from Miller 1968).
- **Truth.**
  - Users trust that an action worked when they see the result on the object itself.
  - Optimistic UI (show the change at once, sync it later, roll back on failure) makes Linear feel instant `[UP · C]`. It is only safe for low-stakes, reversible actions. With money, showing "success" and then reversing it destroys trust.
- **Silent automation is the worst feedback failure** `[SH · B]`.
  - Excel's automatic conversions left gene-name errors in 30.9% of papers with Excel gene lists (Abeysooriya et al. 2021).
  - A legacy spreadsheet row limit silently dropped 15,841 COVID-19 cases in England in 2020 (The Register).
- **When not to follow it.** GitHub accepted about 4.7% stale cached data to feel faster (team blog, 2026). That is defensible for issue lists, not for bank balances or medication.

### P7. Make errors cheap: prevent slips, prefer undo to confirmation, and fail loudly.
- **Habituation.** Attention to repeated, identical warnings drops within days, and warnings that vary their look decline far less (Vance et al. 2018, brain imaging plus a three-week field test) `[FP · A]`. So confirmations on routine actions train people to click through, while undo lets them work at speed `[SH · B]`. Keep confirmations for rare, irreversible, costly actions, and make them break autopilot: name the object, or make the user type the resource name, as GitHub does.
- **Confirmation stops slips, not mistaken beliefs.** In Hawaii's 2018 false missile alert, the officer believed the attack was real. The test and live alerts sat in one menu and had the same confirmation text (FCC report, 2018). The fixes: separate modes, show the actual message, require a second person, and have a correction ready before you need it.
- **Alert noise.** Clinicians override drug-safety alerts in 49–96% of cases, often justifiably; low-specificity alerts teach overriding (van der Sijs et al. 2006). Judge an alert by its specificity, not its override rate.
- **Don't interrupt people mid-entry.** Validate after a field or on submit, not while they type ([interaction.md](interaction.md)) `[SH · B]`.
- **When not to follow it.** Some actions cannot be undone (sent payments, broadcasts). There, preview and deliberate friction are right.

### P8. Defaults and friction steer choices. Always ask whose goal they serve.
- **Evidence.**
  - Defaults: a meta-analysis of 58 datasets found a medium-to-large effect, d = 0.68 (Jachimowicz et al. 2019) `[FP · A]`.
  - Mild deceptive patterns more than doubled sign-ups to a dubious service, with no measurable backlash; aggressive ones almost quadrupled them and angered people (Luguri & Strahilevitz 2021) `[SH · B]`.
  - They are common: 1,818 instances across about 11,000 shopping sites (Mathur et al. 2019), and 52 of 53 top Indian apps (ASCI, 2024).
- **Consequence.** A/B testing aimed only at conversion will *find* deceptive patterns, because they convert. Regulators now act: FTC v. Amazon, $2.5B settled without admission (2025-09); India's ₹7 lakh fine on Zepto for drip pricing (2026-08).
- **The same mechanism can protect.** Monzo's gambling block uses a cooling-off period the user chooses. Zerodha's Kill Switch locks trading for 12 hours. Protective friction is chosen by the user, reversible after a delay, and placed at the moment of decision `[UP · C]`.
- **Tests.** Is leaving as easy as joining? Would users endorse the mechanism if it were described to them plainly?

### P9. Beauty, usability, accessibility, efficiency and business results are separate things. Judge each one separately.
- **Evidence.**
  - People judge a site's *appeal* within 17–50 ms and favour low clutter and typical layouts `[SH · A]`. That measures liking, not ease of use.
  - Whether beauty makes a product *seem* easier varies widely between studies, and the effect can run backwards: poor usability lowers how beautiful people find it after use (Hassenzahl & Monk 2010; Tuch et al. 2012) `[CH · B]`.
  - "Beautiful interfaces are more usable" is `[WC · B against]`.
- **Products.** iOS 26's Liquid Glass was praised for its looks and criticised for legibility and for controls that come and go; Apple then added settings and adaptive backgrounds ([visual.md](visual.md)). GOV.UK looks ordinary; its Design System website was audited as meeting WCAG 2.2 AA (2024), which says nothing about each service built with it. Imitators copy "the Linear look", but Linear's speed most likely comes from its sync engine, which no screenshot shows.
- **Awards, popularity and imitation measure reputation** `[WC · D as usability evidence]`.
- **Review question.** Write a separate verdict for appeal, usability, accessibility and efficiency, each with its own evidence. If the only evidence for "usable" is polish, an award or user numbers, write "not assessed".

### P10. Accessibility means adapting to each user and keeping the platform's built-in behaviour. Meeting the standard is the floor.
- **Evidence.**
  - Only 50.4% of the problems blind users met were covered by WCAG 2.0 criteria (Power et al. 2012) `[FP · B]`.
  - Needs conflict: high contrast against light sensitivity, large text against tunnel vision (W3C low-vision working draft, 2016) `[FP · B]`. So the durable answer is to honour the user's own settings: text size, zoom and reflow, contrast, motion, light or dark.
  - Custom rendering throws away what the browser gives for free: find, focus, the back button, the accessibility tree. Figma and GitHub had to rebuild these deliberately `[SH · B]`.
  - Low-contrast text is the most common failure, found on 83.9% of the top million home pages (WebAIM 2026). Visual designers own it.
- **Review question.** Does the design survive 200% text, 320 px reflow, the OS contrast, motion and dark settings, and keyboard-only use, with native controls where they exist? From a screenshot, only contrast, colour-only cues and target size can be estimated.

---

## 2. Review framework

**Built around one fact.** Any single reviewer, human or AI, finds only part of the problems `[FP · A]`.
- Experienced professionals watching the *same* test videos each reported about a third of all problems (Hertzum et al. 2014). Across the CUE studies, 40–75% of problems were reported by only one team.
- Severity ratings disagree even more: up to 30% of shared problems were rated critical by one evaluator and minor by another (Hertzum et al. 2014) `[SH · A]`.
- An AI model reviewing screenshots matched only 21.2% of the issues human experts found, and invented some (Guerino et al. 2025, preprint).

**Steps**
1. **Scope.** State what you reviewed (screenshot, flow or live product) and which screens and states you saw. List what the artefact cannot show.
2. **User and task.** State the user you assume, what they know, how often they come, and what is at stake. Name the main task and the secondary ones. Unstated assumptions about the user are where walkthrough reviews go wrong.
3. **Walk the main task step by step.** At each step ask: will the user know what to do, see the control, connect it to their goal, and understand the feedback?
4. **Observe before judging.** Note what draws the eye first and second, what is hidden, how things are grouped, what looks clickable, and the wording.
5. **Analyse against P1–P10.** Cover structure and scent; memory and decisions; states (empty, loading, error, success); recovery; defaults; keyboard and touch; accessibility; speed.
6. **Rule out causes that aren't design** before crediting or blaming design: network effects, lock-in, content or data, price, or a buyer who isn't the user.
7. **Record strengths**, not only problems.
8. **Write each finding** with:
   - what you saw;
   - the difficulty you predict and why;
   - when it happens;
   - its status: *observed*, *predicted* or *unknown from this artefact*;
   - its evidence label.

   Stating the difficulty and its cause cut false alarms in the one study that measured it (Cockton et al., c. 2004).
9. **Rate severity from visible factors:** how often it happens, whether it blocks the task, whether users can recover, whether it recurs, what it costs (money, data, safety, legal), and how many users it reaches, including assistive-technology users.
10. **Name an alternative:** a real product that solves the same problem differently.
11. **Recommend the smallest change that fixes the cause**, and state what it might make worse.
12. **Prioritise** by impact, frequency and task importance. Don't redesign everything.

**From a screenshot you can judge:** hierarchy, grouping, signifiers, wording, approximate contrast, and target size if you know the scale.
**You cannot judge:** keyboard use, focus, screen-reader output, other states, speed, reflow, or what happens after an action.
- Write "possible failure of SC 1.4.3, needs checking". Never claim conformance.
- Expect your biggest blind spots in user control, efficiency and error recovery.

**Output.** A short summary, the top issues, positive findings, each finding with its labels, and a line on what you did not examine.

---

## 3. Main tradeoffs (details in [tradeoffs.md](tradeoffs.md))

- **Simplicity vs discoverability.** Hide the rare, show the frequent.
- **Efficiency vs learnability.** Offer two paths and link them.
- **Density vs readability.** Scanning experts gain; first-time readers pay.
- **Personalisation vs predictability.** Adapt by adding, never by moving.
- **Automation vs control.** Automate visibly, reversibly, and with a way to override.
- **Brand expression vs legibility.** Express in the surrounding layer; keep text on a controlled background.
- **Delight and motion vs speed and comfort.** Motion should explain; honour Reduce Motion.
- **Business goals vs user goals.** Keep the core task's shortest path and make leaving as easy as joining.
- **Guidance vs autonomy.** One clear path suits beginners and costs experienced users.

---

## 4. Short answers to the deeper questions

Syntheses, not findings: each rests on the principle cited, and is `[D]` where none is cited.

- **Intuitive:** familiar (P1).
- **Easy to learn:** few new concepts, learning inside the task (P1, P2).
- **In control:** visible state, reversible actions, stable positions, no silent automation, and settings that beat defaults (P5–P7).
- **Trustworthy:** honest prices and state; leaving as easy as joining; generated content marked apart from sourced content (Apple added italics to its AI notification summaries in 2025); and a human to reach when money is at risk. Revolut's chat-only support was criticised during fraud cases.
- **Manageable complexity:** one consistent object model (GitHub: a repository contains files, issues and pull requests), hierarchy by visual weight, the rare tail disclosed later, and a command layer.
- **Feels fast:** useful content visible in about 1 s, instant response to direct input, and honest progress for long waits.
- **Elegant vs empty minimalism:** elegant when what was removed was redundant; empty when it removed information or cues. Vercel's home page tells a newcomer little.
- **Complex made simple:** one obvious next step (Duolingo), a template to start from (Canva), and good defaults, with depth still reachable.
- **Satisfying, and confident it worked:** immediate feedback on the object itself, a confirmation that persists, and the committed content shown.
- **Beginners vs experts** (P2) and **when consistency helps or harms** (P5): one model, two paths; consistency with what users know, not with the style guide.
- **Hierarchy and IA:** a shared container makes things read as related, and can override spacing (Palmer 1992). The visual hierarchy is therefore a claim about structure, and it must exist as real headings in the code.
- **Business incentives:** they shape home screens (Spotify 2023, Netflix 2025), friction and defaults. When goals conflict, protect the core task, disclose costs, and keep effort symmetric. Regulators increasingly draw the line.
