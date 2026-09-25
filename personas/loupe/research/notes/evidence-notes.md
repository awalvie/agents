# Foundations, evidence and evaluation: research notes

Area: HCI and cognitive foundations; tracing rules and finding counterexamples; competing principles; evaluation methods.
Research done 2026-09-25. Every source is listed in `sources.md` with how I accessed it. Where I read only an abstract or a secondary summary, the note says so.

**Label key.** Each finding gets two labels, as the brief requires: *kind of claim* / *evidence grade A–D*. Where a rule splits into a supported core and an unsupported popular version, I label the parts separately. One observation of one product carries its source type instead of the two labels.

**The main message for the synthesiser.** Most famous UX rules are real findings that lost their context as they were passed on. The finding usually survives. What fails is the universal version ("always", "never", "X maximum"). Across this area, the most reliable knowledge is the mechanism (information scent, signifiers, working-memory load, the speed–accuracy trade-off, transfer of learning), not the rule of thumb built on top of it. The evaluation literature also warns that any single reviewer, human or model, finds only part of the problems and rates severity unreliably. The final output's review framework has to be built around that fact.

---

## Part 1. Evaluation methods and what they can establish

### E1. Different evaluators find different problems (the evaluator effect)

**Claim.** Evaluators who use the same method on the same interface report substantially different problem sets. This holds for heuristic evaluation, cognitive walkthrough and think-aloud testing alike.

**Evidence.**
- Hertzum & Jacobsen (2003) reviewed 11 studies. Average *any-two agreement* (problems shared by a pair of evaluators, as a share of all problems either one found) ranged from **5% to 65%**, and none of the three methods was consistently better. The effect held for novice and experienced evaluators, for cosmetic and severe problems, for problem detection and severity rating, and for simple and complex systems. (I read the abstract, plus a detailed restatement in Hertzum et al. 2014.)
- Jacobsen et al. (1998), as reported in Hertzum et al. 2014: four evaluators analysed the *same* four videotaped sessions. Detection rate was 52% and any-two agreement 42%.
- Hertzum, Molich & Jacobsen (2014, *BIT*): 19 experienced professionals analysed the same videos of five-user tests. In moderated sessions, each participant reported on average **33%** of all problems found and **50%** of the problems someone rated critical or serious. In unmoderated sessions the figures were 32% and 40%. Most participants did not notice the evaluator effect until they merged their findings.
- Molich's CUE series (1998–2018; more than 140 teams across 10 studies) found that no issue was reported by every team. Share of issues reported by only one team: CUE-2 (Hotmail, 9 teams) **75%** of 310; CUE-4 (hotel site, 17 teams) **60%** of 340; CUE-9 (van rental, 35 people watching the *same* videos) **40%** of 223. Some serious or critical problems were reported by only one team: 29, 61 and 17 respectively. In CUE-2 the 9 teams wrote 51 different tasks with "virtually no overlap".

**Context.** The effect appears in all three major methods. It shrinks, but does not disappear, when the tasks and the data are fixed (CUE-9: same videos, still 40% single-team issues).

**Counterevidence.** Agreement rises with well-defined tasks and task-based methods. MeasuringU's small hybrid evaluation with 4 evaluators reached about 57% average pairwise agreement (C evidence: one practitioner study). Molich answers critics of the CUE matching process by conceding that problem matching involves judgement.

**Example.** CUE-9 is the cleanest demonstration: evaluators watched identical footage and still disagreed.

**Labels.** Fundamental principle of evaluation / **A** (many independent studies, several methods, 25 years).

**Implication.** Treat one review as a sample from a larger problem space, not as an inventory. Several independent reviewers, or several independent passes by an automated reviewer, find more problems than one long pass (Nielsen 1994; MeasuringU). A review should say what it examined (tasks, screens, states) so readers know what it could not have found. Do not present a problem list as complete.

### E2. How much heuristic evaluation finds, and why the published rates flatter it

**Claim.** One heuristic evaluator finds a minority of problems. Pooling 3–5 evaluators finds most of the problems that heuristic evaluation can find.

**Evidence.** Nielsen & Molich (1990, CHI) ran four experiments: individual evaluators found 20–51% of problems, and aggregates of 3–5 evaluators did "rather well" (abstract only). Nielsen (1994) averaged six of his own projects: a single evaluator found **35%**. His cost-benefit figures (for example, a benefit-cost ratio of 48) rest on estimated, not measured, benefits.

**Counterevidence.** The denominator is usually the union of problems that the evaluators themselves found, sometimes supplemented by known problems. It is not all real problems, so detection rates are inflated (Hertzum & Jacobsen 2003 make the same point about detection rate against any-two agreement). Gray & Salzman (1998, *HCI* journal, abstract only) argued that design flaws in five influential method-comparison experiments "call into serious question" what was believed about method efficacy. Cockton et al. (c. 2004) note that Nielsen's heuristics were derived from factors that explained only 30% of a 247-problem corpus. They also cite Gray & Salzman's point that, in Nielsen's 1992 study, it was experts who found more problems, not necessarily experts *using heuristics*.

**Labels.** "Use 3–5 evaluators": useful pattern / **B**. "Heuristic evaluation finds X% of problems": unsupported as a general number / **C**, because it depends on the denominator.

**Implication.** Heuristics prompt a reviewer. They do not discover problems on their own; the reviewer's skill and knowledge of users' tasks do (Cockton et al.). A review framework should be driven by tasks ("walk the main task, then check the heuristics") rather than by the heuristic list alone.

### E3. False positives: a real contradiction in the literature

**Claim under test.** Heuristic evaluation produces many false alarms, meaning predicted problems that real users do not have.

**Evidence for.**
- Cockton & Woolrych's large study (99 student analysts in groups, a drawing editor, test tasks designed to *falsify* each prediction), as summarised in Cockton, Woolrych, Hall & Hindmarch (c. 2004, read in full): **65%** of predictions "did not transpire" (validity about 0.35). **61%** of heuristic applications were inappropriate. **80%** of the hardest-to-find problems were missed. Adding analysts raised thoroughness but added "even more false alarms".
- A follow-up in the same paper (31 students, a transport website) found that an extended report format reduced false positives. Analysts had to state the likely user difficulty, the context, the assumed cause and why they kept or dropped each candidate.
- Bailey (2001 newsletter, practitioner) pooled three studies from the late 1990s (Catani & Biers 1998; Rooden et al. 1999; Stanton & Stevenage 1998): about **43%** of predicted problems were false alarms, 36% were hits, and about 21% of real problems were missed. Note that web summaries often attribute the 43% to Bailey, Allan & Raiello (1992). Bailey's own newsletter attributes it to the three later studies. I could not read the underlying papers.

**Evidence against.** Molich's CUE studies report "few false alarms": "almost all described problems" were "reasonable and in accordance with generally accepted advice", except in CUE-3, where less experienced teams reported questionable issues. CUE-4 found expert reviews comparable to usability tests (Molich & Dumas 2008; the Usability Body of Knowledge dates it 2005, which is probably the workshop year).

**How to reconcile them.** The two camps measure different things.
1. **Who the evaluators are.** Cockton's analysts were students. CUE's were mostly experienced professionals, and CUE's only false alarms came from less experienced teams.
2. **What counts as "false".** Cockton tested each prediction against users. CUE judged validity by expert agreement with "generally accepted advice", which can confirm a shared belief without checking it against users.
3. **Tests can miss real problems.** A prediction that users did not hit in five sessions may still be real (see E5). Cockton et al. accept that further testing could turn a false positive into a hit.

**Labels.** "Inexperienced or unstructured heuristic reviews produce many false positives": context-dependent heuristic / **B**. "Expert reviews produce few false positives": context-dependent heuristic / **C**, because validity was judged by expert consensus.

**Implication.** For every problem it reports, a reviewer should state the user difficulty it predicts, when it occurs, and why. That discipline is what reduced false positives in the one study that measured it. Separate an *observed* problem from a *predicted* one, and label predictions as hypotheses.

### E4. Severity ratings are less reliable than problem lists

**Claim.** Evaluators disagree even more about how severe a problem is than about whether it exists.

**Evidence.** Nielsen (1994) wrote that "severity ratings from a single evaluator are too unreliable to be trusted" and recommended the mean of at least three raters. He proposes a 0–4 scale combining frequency, impact and persistence, with market impact assessed separately. He gives no reliability statistics. Hertzum et al. (2014): as much as **24%** (moderated) and **30%** (unmoderated) of problems reported by several evaluators were rated *critical* by one and *minor* by another. Hertzum & Jacobsen (2003) found the evaluator effect extends to severity. CUE-2/4/9 show that serious problems are often reported by only one team (E1).

**Labels.** Strong heuristic / **A** (independent studies agree).

**Implication.** Do not present one reviewer's severity as fact. Anchor each rating in observable factors: how often the problem occurs, whether it blocks the task, whether users can recover, whether it recurs, and what it costs (money, data, safety). Show those factors so that others can re-rate. When prioritising, weight task importance and reach explicitly, as the brief's critique step 16 requires, rather than relying on gut severity.

### E5. "Five users are enough" is a claim about iteration, not about coverage

**Claim (popular form).** Five test users find about 85% of usability problems.

**Origin and original evidence.** Nielsen (2000) proposed the formula N(1−(1−L)^n), with L ≈ 31% averaged "across a large number of projects" (Nielsen & Landauer 1993). His own conditions: users are comparable, testing is iterative (three rounds of five users rather than one round of fifteen), and distinct user groups need their own samples.

**Later research.** Faulkner (2003; abstract and secondary): random subsets of 5 drawn from 60 users found between **55% and 99%** of problems. The worst 10-user set found 80%, and the worst 20-user set 95%. Molich (2018): "Five users are by far not enough to find 75 percent or even 25 percent of the usability problems in a complex website", but "nothing in the CUE studies contradicts ... that five users may be enough to drive a useful iterative process." Changing the tasks or the moderator uncovers new problems.

**When it applies.** Small, simple interfaces; one user group; fixed tasks; repeated test-fix-test cycles.

**When it fails.** Complex products, several user groups, rare but severe problems, and quantitative benchmarks (NN/g itself suggests about 20 users for quantitative studies).

**Labels.** Popular form: unsupported / **A** evidence against. "Small iterative tests are cost-effective": context-dependent heuristic / **B**.

### E6. Cognitive walkthrough

**Claim.** Cognitive walkthrough (CW) is a structured, task-based inspection. At each step the reviewer asks whether a user would know what to do, see the control, connect it with the goal and understand the feedback. It targets learnability by exploration.

**Evidence.** CW shows an evaluator effect comparable to heuristic evaluation (Hertzum & Jacobsen 2003). Hertzum & Jacobsen (1999, abstract only): 11 first-time CW users evaluated a web library system on three set tasks. In their descriptions of users, evaluators showed anchoring on and stereotyping of the imagined user. Cockton et al. note that CW, unlike heuristic evaluation, forces "success cases", so some erroneous dismissals become visible.

**Could not verify.** I did not read Wharton et al. (1994) or a controlled comparison of CW's validity against testing, so I make no quantitative claim for CW.

**Labels.** Useful pattern / **B** for its structure; its detection performance is unverified here.

**Implication.** CW's questions suit a screenshot or flow review better than a heuristic list does, because they force a task and a specific user. Their weakness is the imagined user. State the user's assumed knowledge explicitly, since that assumption is where CW reviewers go wrong.

### E7. What a review of screenshots alone can and cannot establish

This finding combines the evidence above with WCAG 2.2 and two recent studies of AI reviewers.

**Claim.** A static screenshot supports claims about what is *visible* and supports *predictions* about behaviour. It cannot establish behaviour, states, accessibility conformance, performance or actual user difficulty.

**Can be established or strongly estimated from pixels:**
- Visual hierarchy, grouping (Gestalt proximity and common region, see F3), alignment, density, reading order as presented.
- Presence, wording and *visual strength of signifiers*. Weak signifiers measurably slow finding (F4).
- Text contrast against WCAG 2.2 SC 1.4.3 (4.5:1; 3:1 for large text) and non-text contrast under SC 1.4.11 (3:1), *approximately*. Anti-aliasing, text over images and colour compression make pixel sampling imperfect.
- Target size against SC 2.5.8 (24×24 CSS px, AA, with spacing, equivalent, inline, user-agent and essential exceptions), *only if* the screenshot's scale to CSS pixels is known.
- Use of colour as the only cue (SC 1.4.1), label clarity, jargon, presence or absence of visible navigation (F-R1), clutter that resembles ads (F5).

**Cannot be established from a static image:**
- Keyboard operability (2.1.1), focus order (2.4.3), focus visibility (2.4.7) and focus not obscured (2.4.11), except for the one state captured.
- Accessible names, roles and states (4.1.2), and screen-reader output.
- Reflow and resize (1.4.10, 1.4.4), motion (2.3.3), timing.
- Hover, pressed, error, loading and empty states; transitions; latency (F-R16); what happens after an action; whether an undo exists.
- Whether users actually have a predicted problem, how often, and how badly (E3, E4).
- Task context, meaning why the user is on this screen. CUE-2 shows that even experts invent very different tasks for the same UI.

**Evidence about AI reviewers.**
- Duan, Warner, Li & Hartmann (CHI 2024, first two pages read). A GPT-4 Figma plugin evaluated static single-screen mockups from a JSON description of the layout. It was "generally accurate and helpful" at spotting issues in poor designs, but its usefulness *fell* over iterations as designs improved. It did worse where the JSON diverged from what was visually shown.
- Guerino et al. (2025 arXiv preprint, abstract only). GPT-4o heuristic evaluation from screenshots of a web system identified only **21.2%** of the issues human experts found. It also reported 27 new issues and "several false positives due to hallucinations". It was relatively better at aesthetic and minimalist design and at match with the real world, and weak on flexibility, user control and efficiency. Those heuristics need interaction to judge.

**Labels.** Strong heuristic / **B** (standard-based reasoning plus two AI studies and the general evaluation literature).

**Implication for the final framework.** For every screenshot finding, record (a) *observed* (a pixel fact), (b) *predicted* (user difficulty expected, with the mechanism), or (c) *unknown from this artefact* (needs interaction, code or users). Never report WCAG conformance from a screenshot; report "possible failure of SC x, needs verification". Expect the largest blind spots in control, efficiency and error recovery.

---

## Part 2. Commonly repeated rules traced to their evidence

Format for each rule: origin → what the original evidence showed → later research → counterexamples → when it applies or fails → labels.

### R1. "Hamburger menus are bad"

- **Origin.** Practitioner writing in 2014–2015 (Luke Wroblewski, 2015-04-27), which cited Facebook's 2013 iOS move to a tab bar ("engagement went up") via TechCrunch, and Redbooth's switch ("increased sessions and users"). **No numbers were published in either.** James Foster's 2014 A/B tests on one site (Caffeine Informer) reported about 20% more taps on a button labelled "MENU" than on the bare icon. I only saw this quoted in secondary sources and could not read the original.
- **Best evidence.** NN/g (Pernice & Budiu, 2016-06-26 and 2016-07-24): 179 participants, 6 sites (BBC, Bloomberg, Slate and others), desktop and mobile. On desktop, hidden navigation was used in **27%** of cases against 48–50% for visible or combined navigation, and users were "at least 39% slower". On mobile, hidden navigation was used 57% of the time against 86% for combined navigation, and users were 15% slower. Content discoverability dropped "more than 20%" and perceived difficulty rose 21%. NN/g's stated causes: low salience, low information scent, extra interaction cost, lack of standards, and low familiarity on desktop.
- **Context and limits.** The effect is about *hiding navigation*, not about the three-line icon. NN/g itself recommends hiding navigation on mobile when there are more than about 4 top-level items, because nothing else fits. Combined designs (some links visible, the rest behind a menu) performed nearly as well as visible navigation.
- **Counterexample and pattern (docs, as of 2026-09).** The GOV.UK Design System's service navigation collapses to a button with the *text* "Menu" on small screens by default when there is more than one item. The mechanism: it accepts the cost of hidden navigation but repairs the information-scent problem with a word label.
- **When the rule applies.** Desktop, and any context where navigation is the main path to content.
- **When it fails.** Search-led or feed-led products, where navigation is secondary; long navigation sets on small screens; secondary destinations in a tab-bar app.
- **Labels.** "Hidden navigation is used less and slows users": strong heuristic / **B** (one large study plus consistent but unquantified practitioner reports). "Hamburger menus are bad": unsupported as stated / **C**. "Label the menu control with a word": useful pattern / **C**.
- **Implication.** Ask what is hidden, how often users need it, and whether anything signals it. Expose the 2–4 most-used destinations and hide the rest behind a labelled control.

### R2. "Dark mode is better"

- **Evidence on reading performance** (read via NN/g's 2020-02-02 review by Budiu, plus primary abstracts):
  - Piepenbrock, Mayr, Mund & Buchner (2013, *Ergonomics*): young (18–33) and older (60–85) adults with normal vision. Positive polarity (dark text on a light background) was better for visual acuity and proofreading in *both* age groups.
  - Piepenbrock et al. (2014, *Human Factors*): the advantage is largest at small character sizes.
  - Dobres et al. (2017), as reported by NN/g: at night light mode performed better for glanceable reading; by day there was no significant difference.
  - Legge et al. (1985), as reported by NN/g: people with cloudy ocular media read faster with light text on dark.
  - Aleman et al. (2018; 7 participants), as reported by NN/g: choroid thinning with light mode. This is a very small physiological study with no functional outcome.
- **Later research.** While & Sarvghad (IEEE VIS 2024; 134 participants, 52 per group analysed; visualisation tasks, not reading). The strength of the polarity effect did *not* change noticeably with age, and roughly half of participants did better in each mode. The authors recommend offering both.
- **Battery.** Dash & Hu (Purdue, MobiSys 2021; Pixel 2, Moto Z3, Pixel 4, Pixel 5): **39–47%** display power saving at 100% brightness, but only **3–9%** at 30–50% brightness. This applies to OLED phones only.
- **Classification.** "Dark mode improves reading for most users": unsupported / **A** evidence against for normal-vision reading of small text. "Offer a user-controlled choice": useful pattern / **B**. "Dark mode saves battery": context-dependent (OLED, high brightness) / **B**.
- **Implication.** Default to positive polarity for long or small text, offer dark mode as a preference, and follow the system setting. Never justify dark mode as better for accessibility in general. Some low-vision users need it, and others (for example, people with astigmatism, a claim I could not trace to a study) are said to struggle with it.

### R3. "Animations improve UX"

- **Origin.** No single source. Principles from cartoon animation (Lasseter; Chang & Ungar 1993; I did not read either) entered UI practice. Design systems now ship motion guidance.
- **Evidence.**
  - Tversky, Morrison & Bétrancourt (2002, *IJHCS*; I read the conclusion section). In learning studies where animation seemed to help, the animated version usually carried *more information* or *interactivity* than the static control. When information was equated, static graphics did as well. Animation must be slow and clear enough to perceive, and schematic. "Clever schematization of static diagrams may be just as effective" (congruence and apprehension principles).
  - Heer & Robertson (2007, InfoVis; I read the introduction). Two controlled experiments found that appropriately designed animated transitions between statistical charts "significantly improve graphical perception". They list the pitfalls: animation grabs attention and can distract, false object constancy can mislead, too slow harms task time, too fast causes errors. They recommend about 1 second for transitions, which is a design recommendation from their data, not a universal constant.
  - WCAG 2.2 SC 2.3.3 (AAA): "Motion animation triggered by interaction can be disabled" unless essential. The rationale is vestibular disorders (dizziness, nausea, headaches).
- **When the rule applies.** Motion that shows *what changed and where it went*: object constancy across views, spatial relationships in navigation, cause and effect of an action.
- **When it fails.** Decorative motion, motion on the critical path of frequent tasks (it adds delay to every repetition), and motion for users with vestibular disorders.
- **Labels.** "Animations improve UX": unsupported as stated / **B** evidence against the blanket form. "Transitions that preserve object constancy aid comprehension of changes": context-dependent heuristic / **B**. "Honour a reduce-motion preference": design convention / **B** (standard).

### R4. "Users don't read"

- **Origin.** Nielsen's 1997 eyetracking and usability work. The best quantitative basis is Weinreich, Obendorf, Herder & Mayer (2008, *ACM TWEB*), analysed by Nielsen (2008-05-05): 25 users logged in natural browsing, 45,237 page views. Users "have time to read at most 28% of the words during an average visit; 20% is more likely". Each extra 100 words added about 4.4 s of dwell. Caveats: participants were above average in education, it covers pages of 30–1,250 words only, and it infers reading from dwell time.
- **F-pattern.** Pernice (2017-11-12 update of the 2006 study; eyetracking, 45+ and 47 participants in two studies). The F-pattern appears when text is unformatted, the user wants efficiency, and the user is not highly motivated. Other patterns exist, including layer-cake (headings), spotted, marking, bypassing and **commitment** (reading everything when motivated). NN/g calls the F-pattern *bad*, a symptom of poor formatting rather than a layout to design for.
- **Counterexamples.** Committed reading of long-form journalism, documentation, legal and financial pages at a decision point. Chartbeat (Haile, 2014-03-09; 2 billion visits) reported that 55% of visitors spent under 15 s *actively* on a page. So both "users skim" and "some users read deeply" are true of the same content.
- **Labels.** "Most web users scan rather than read word by word, unless motivated": strong heuristic / **A** (log study plus repeated eyetracking). "Users don't read": unsupported as stated / **B**.
- **Implication.** Write for scanning (front-load words, meaningful headings, one idea per paragraph) *and* for committed reading at decision points. Test comprehension, not only findability.

### R5. "Three-click rule"

- **Origin.** The earliest documented reference is Zeldman, *Taking Your Talent to the Web* (2001), per NN/g (Laubheimer, 2019-08-11). No study underlies it.
- **Evidence against.** Porter (UIE, 2003-04-16): 44 users, 620 tasks, more than 8,000 clicks. There was no more quitting after 3 clicks than after 12, dissatisfaction was flat at 46–61% across path lengths, and 80% of tasks ended only by 15 clicks. The data were not peer-reviewed and the method is only partly reported. Larson & Czerwinski (CHI 1998, abstract only): increased depth harmed search, but a *medium* breadth/depth structure outperformed the broadest, shallowest one. Structure interacts with scent and category clarity.
- **Labels.** Unsupported or weak claim / **D** for the rule. The underlying principle is "users persist while information scent is strong; each step must clearly lead toward the goal": strong heuristic / **B**.
- **Implication.** Count *uncertain* steps, not clicks. Removing depth by piling up ambiguous choices can make things worse.

### R6. "Above the fold is critical"

- **Evidence.** NN/g (Fessenden, 2018-04-15): 120 participants and 130,000+ fixations. **57%** of viewing time fell above the fold (80% in the 2010 study on 1024×768 screens) and 74% in the first two screenfuls. Users "rarely go beyond the third screenful". Chartbeat (2014): "66% of attention on a normal media page is spent below the fold".
- **The contradiction explained.** The measures differ: eye fixations across mixed tasks and page types, against analytics "engaged time" on article pages, where the content starts high and runs long.
- **Counterexamples.** Long-form articles and long landing pages where scrolling is expected. NN/g's "false floor" warning shows the real risk: a layout that looks finished stops scrolling.
- **Labels.** "Attention decays with scroll distance; the first screen gets the most": strong heuristic / **A** (two independent large datasets agree on decay even though they disagree on the share). "Everything important must be above the fold": unsupported / **C**.
- **Implication.** Put the page's purpose and main path at the top, signal that more follows, and avoid false floors. Do not cram.

### R7. "Keep it simple" and "Minimalism improves UX"

- **Origin.** I found no research origin in HCI. It is a design maxim, not a finding.
- **What evidence exists** (about *appeal*, not usability):
  - Tuch, Presslaber, Stöcklin, Opwis & Bargas-Avila (2012, *IJHCS*; abstract read). Visual complexity and *prototypicality* (looking like a typical site of its kind) affect aesthetic ratings within 17–50 ms. "Websites with low VC and high PT were perceived as highly appealing."
  - Reinecke et al. (CHI 2013; abstract read). Computational measures of complexity and colourfulness, combined with demographics (education, age), explain about half the variance in 500 ms appeal ratings across 450 sites and 548 raters, so preference is not uniform.
- **Counterevidence.** Removing functions moves cost elsewhere: hidden navigation (R1), gestures without signifiers (T1), weak flat signifiers (F4). The brief's dense products (Bloomberg, Excel, Craigslist) are counterexamples. Other researchers own those specimens, and I did not assess them.
- **Labels.** "Low visual complexity plus a familiar layout raises first-impression appeal": strong heuristic / **A** (two independent studies). "Minimalism improves usability": unsupported / **D**. It conflates visual complexity with functional scope.
- **Implication.** Reduce *visual* noise, meaning inconsistent alignment, competing emphasis and decoration, before reducing *function*. Judge simplicity by the user's steps and decisions for the main task, not by element count.

### R8. "Beautiful interfaces are more usable" (the aesthetic-usability effect)

- **Origin.** Kurosu & Kashimura (1995, CHI short paper; I only saw it quoted): ATM layouts, where rated beauty correlated with *apparent* usability. Tractinsky (1997) reportedly replicated it in Israel (seen quoted only). Tractinsky, Katz & Ikar (2000, *IwC*; abstract read): in a lab ATM simulation, aesthetics affected *post-use* perceived usability, and actual usability did not.
- **Later research.**
  - Hassenzahl & Monk (2010, *HCI*; abstract read) reviewed 25 correlations from 15 papers and found "remarkably high variability". The beauty–usability link was *wholly mediated* by an overall "goodness" judgement across four datasets. They conclude that it "has been overplayed".
  - Tuch, Roth, Hornbæk, Opwis & Bargas-Avila (2012, *CHB*; abstract read): 80 participants, a 2×2 of aesthetics against usability in an online shop. Aesthetics did **not** affect perceived usability. Poor usability **lowered** post-use perceived aesthetics, the reverse of Tractinsky.
- **Labels.** "Aesthetics shifts perceived usability": context-dependent heuristic / **B** with contradictory results. "Beautiful interfaces are more usable (objectively)": unsupported / **B** evidence against.
- **Implication.** Visual polish can raise first impressions and tolerance but will not rescue a broken task. Poor usability can drag down aesthetic judgements. Rate aesthetics and usability separately, as the brief's "Avoid aesthetic bias" section requires.

### R9. "Consistency is always good"

- **Origin.** Shneiderman's "Strive for consistency" and 1980s guideline compendia. Polson's transfer experiments reported "reductions in training time ranging from 100% to 300%" (quoted in Grudin 1989).
- **Critique.** Grudin (1989, *CACM*; pages 1–3 read) separated *internal* consistency, *external* consistency with other interfaces, and *analogical* consistency with the world. He argued that "ease of learning can conflict with ease of use", that consistency is "an unreliable guide", and that designers "would often do better to focus on users' work environments".
  - His knife-drawer analogy: knives are stored where each is *used*, not all together.
  - Calculator keys: 24 interface professionals chose a "consistent" + − × ÷ layout, but data entry favours putting + beside Enter.
  - Cursor keys: experts preferred the analogically consistent "star" arrangement, but studies showed the inverted T performed better.
- **Counterexamples.** Adaptive or task-specific layouts that break internal consistency for frequent actions.
- **Labels.** "Consistency with users' existing knowledge speeds learning": strong heuristic / **B**. "Consistency is always desirable": unsupported / **B** evidence against. Most of Grudin's cases are argument backed by cited studies, not new experiments.
- **Implication.** Ask *consistent with what*, and *for whom*: the user's tasks, their other tools, or the design system's internal rules. Break internal consistency deliberately for high-frequency expert actions, and document it.

### R10. "Users should never need to learn the interface" / "Every interface should be immediately intuitive"

- **Origin of the critique.** Raskin (1994, *CACM* viewpoint; read via AskTog): "'intuitive' in this context is an almost exact synonym of 'familiar.'" His anecdote: a teacher who had never seen a mouse lifted it in the air and turned it over. It became "intuitive" only after a demonstration, by analogy with joysticks.
- **Evidence.**
  - Carroll & Rosson (1987; read). Word-processor learners show a *production bias*: they want throughput, skip learning, and "stick with the procedures they already know, regardless of their efficacy". They also show an *assimilation bias*: they interpret the new system through old ones, which helps and misleads.
  - Lane, Napier, Peres & Sándor (2005, *IJHCI*; abstract and secondary). Of 251 experienced Word users, most rarely used keyboard shortcuts. Experience had little relationship to shortcut use.
- **Implication for the rule.** Users *will* not learn much unprompted, but they *can*. Expert tools depend on learning (the brief's Bloomberg and Excel cases), provided the investment pays off and the product supports the move from novice to expert.
- **Labels.** "Intuitive means familiar": strong heuristic / **B**. "Users will not invest in learning unprompted" (paradox of the active user): strong heuristic / **B**. "Interfaces should never require learning": unsupported / **B** evidence against for expert and frequent-use tools.
- **Implication.** Design for learning *in context*: recognition-based paths that expose faster paths (menus that show shortcuts, command palettes, just-in-time hints). Do not pretend a powerful tool needs no learning.

### R11. "Never use more than X colours"

- **Origin.** I could not trace any HCI source. The nearest popular rule, 60-30-10, comes from interior-design advice with no traceable study.
- **Relevant evidence.** Smallman & Boynton (1990, *JOSA A*; abstract via search). With well-separated basic colours, search time for a cued colour rose "only marginally" as up to nine colour groups were added. Earlier work showed efficient coding for up to six. WCAG 2.2 SC 1.4.1: colour must not be the only means of conveying information.
- **Labels.** Colour-count limits: aesthetic preference / **D**. "Colour codes work when categories are few, well separated and redundantly coded": strong heuristic / **B**.
- **Implication.** Judge colour by *function*: is each hue a meaningful category, discriminable (including for colour-vision deficiency), and backed by a non-colour cue?

### R12. "Every page needs a CTA"

- **Origin.** I found no research origin. It appears to come from marketing and conversion practice. I searched and found no study, so I make no claim beyond that.
- **Counterexamples.** Reference and content pages whose job is to answer a question. A forced CTA competes with the user's task, and ad-like prominent elements get ignored anyway (F5).
- **Labels.** Unsupported or weak claim / **D**.
- **Implication.** Every page needs a *next step for the user's goal*, which may be none.

### R13. "Seven plus or minus two" (Miller's law) for menus and navigation

- **Origin.** Miller (1956) discussed absolute judgement and immediate memory span, treated seven partly as a rhetorical device, and emphasised chunking. My fetch of the original failed, so this rests on secondary accounts. Treat the characterisation as not directly verified.
- **Later research.** Cowan (2001, *BBS*; abstract read): working-memory capacity is closer to **3–5 chunks** (about 4) when rehearsal and chunking are controlled.
- **Why the design rule fails.** Menus are *recognition* tasks, since the items stay visible, not recall tasks. Capacity limits matter for what users must *hold in mind across screens*: codes, earlier choices, comparisons.
- **Labels.** "Working memory is sharply limited (about 4 chunks)": fundamental principle / **A**. "Limit menus to 7±2 items": unsupported / **B** evidence against, because it misapplies the finding.
- **Implication.** Count what the user must *remember*, not what is shown. Carry earlier choices forward on screen and support comparison in view.

### R14. Hick's law, and "fewer choices are always better"

- **Origin.** Hick (1952) and Hyman (1953): choice reaction time grows with the logarithm of the number of *equally likely, well-learned* stimulus–response alternatives.
- **Why it misleads designers.** Cockburn, Gutwin & Greenberg (CHI 2007; abstract read) model menu selection as *visual search* for novices (roughly linear in the number of items) moving to Hick–Hyman *decision* time for experts, plus Fitts pointing time. The model predicted empirical data well. Reducing items helps novices scanning an unfamiliar list. For experts, item count matters little compared with stable positions.
- **Choice overload.** Scheibehenne, Greifeneder & Todd (2010, *JCR*; abstract via search): 63 conditions, N = 5,036, **mean effect "virtually zero"** with large variance. Chernev, Böckenholt & Goodman (2015, *JCP*; abstract via search): 99 observations, N = 7,202. Overload depends on *choice set complexity, decision task difficulty, preference uncertainty and decision goal*.
- **Labels.** Hick–Hyman law in its original domain: fundamental principle / **A**. "Fewer choices are always better": unsupported / **A** evidence against. "Large assortments hurt when options are hard to compare, preferences are unclear and no option dominates": context-dependent heuristic / **A**.
- **Implication.** Support comparison and give a clear default or recommendation rather than cutting options. Keep positions stable so experts can go straight to the item.

### R15. "Keep lines to 50–75 characters"

- **Evidence.** Dyson (2004, *BIT* review; synthesis read): "Most of the studies on line length report faster reading with longer lines," up to about 100 characters per line on screen. Yet "people prefer a more moderate length", and subjective judgements "have not been in close agreement" with performance. Dyson & Haselgrove (2001; abstract via search): 55 cpl gave better comprehension than 100 cpl, so speed and comprehension may diverge. The 50–75 figure echoes print guidance (Spencer 1968: about 70 cpl; Tinker's work interpreted as 52 cpl).
- **Labels.** Context-dependent heuristic / **B**. Performance and preference conflict.
- **Implication.** Moderate lines are a defensible default for comprehension and preference. Longer lines are not a usability defect for scanning or skimming.

### R16. Response-time limits: 0.1 s / 1 s / 10 s; the "Doherty threshold" of 400 ms

- **Origin.** Nielsen (1993) restated limits from R. B. Miller (1968, AFIPS) and Card, Robertson & Mackinlay (1991): 0.1 s feels instantaneous, 1 s keeps flow of thought, 10 s keeps attention. Doherty & Thadani (1982, IBM Systems Journal) argued for sub-400 ms response from IBM productivity data. I only saw it quoted, and I could not assess its method.
- **Labels.** The three limits: strong heuristic / **B**. They are widely used and perceptually plausible, but the originals are partly expert synthesis. 400 ms as a law: weak claim / **C**. Its dollar figures are mainframe-era in-house estimates.
- **Implication.** Match feedback to the delay: under 0.1 s needs no indicator, around 1 s needs subtle feedback, and over 10 s needs progress, cancel and background options. A screenshot cannot show any of this (E7).

### R17. "Users judge a site in 50 ms"

- **Evidence.** Lindgaard, Fernandes, Dudek & Brown (2006, *BIT*; abstract via search): visual-appeal ratings at 50 ms correlated highly with those at 500 ms. Tuch et al. (2012) found effects at 17 ms.
- **Limits.** These are ratings of *visual appeal*. They do not measure usability, trust, comprehension or conversion.
- **Labels.** "Aesthetic first impressions form within a fraction of a second and are stable": strong heuristic / **A** (independent replications). "Users decide whether to stay in 50 ms": unsupported extrapolation / **D**.

---

## Part 3. Foundational principles (cognition and perception)

### F1. Fitts's law

**Claim.** Pointing time rises with distance and falls with target size, following the logarithm of distance over width.

**Evidence.** MacKenzie (1992, *HCI*; abstract and secondary) sets out the Shannon formulation and shows high fit (r ≈ .99 in the reanalysis cited). It is a replicated model over decades of pointing studies. For touch, Bi, Li & Zhai (CHI 2013; abstract via search) show that plain Fitts under-models small finger targets. FFitts adds an absolute finger-precision term (R² ≥ .91).

**Counterevidence and context.** It is a model of aimed movement, not of the search or decision that comes before it (R14). On touch screens, precision has a floor that no speed trade-off overcomes.

**Examples.** Screen-edge and corner targets (effectively infinite depth with a mouse); WCAG 2.2 SC 2.5.8 minimum target size of 24×24 CSS px.

**Labels.** Fundamental principle / **A**.

**Implication.** Make frequent targets large and close. On touch, respect an absolute minimum size and spacing.

### F2. Recognition over recall

**Claim.** Recognising a visible option is easier than recalling it, because the cue activates the memory.

**Evidence.** A classic finding in memory psychology. NN/g (Budiu, 2024-01-15) explains it by cue-driven spreading activation and cites Adar, Teevan & Dumais (2008) on revisiting web pages by retracing paths.

**Counterevidence.** For frequent tasks, recall-based input (shortcuts, typed commands) is faster, and users often fail to make that switch (R10; Lane et al. 2005). Command palettes are a hybrid: the user types a partial recall and then *recognises* the match in a list.

**Labels.** Fundamental principle / **A** as a memory phenomenon. "Always favour recognition": context-dependent heuristic / **B**, because it trades expert speed for ease.

**Implication.** Provide recognition paths for everyone, and faster recall paths that the recognition paths *teach*, for example by showing the shortcut beside the menu item.

### F3. Gestalt grouping

**Claim.** Viewers group elements by proximity, similarity, connectedness and common region.

**Evidence.** Wagemans et al. (2012, *Psychological Bulletin*; abstract via search) review a century of grouping and figure–ground research. They note that the classic principles are robust demonstrations but theoretically underspecified. Palmer (1992, *Cognitive Psychology*; abstract via search): *common region* (a shared bounded area) is a distinct principle that can override proximity and similarity.

**Labels.** Fundamental principle / **A**.

**Implication.** A card or container outweighs spacing. If a container groups things that belong to different tasks, users will read them as related. Visual hierarchy is an information-architecture claim.

### F4. Signifier strength

**Claim.** Weak or flat signifiers for clickable elements slow users down.

**Evidence.** NN/g (Moran, 2017-09-03): 71 participants, 9 page pairs identical except for signifier strength. Weak signifiers led to 22% more time and 25% more fixations, with gaze spread more widely.

**Counterevidence and caveats.** The tasks were short and on a single page, and the study measures findability, not discoverability. Familiar conventions, such as a blue underlined link, can carry meaning with little visual weight.

**Labels.** Strong heuristic / **B** (one controlled study plus consistent theory).

**Implication.** Interactive elements need at least one reliable cue: shape, colour convention, label or position. This is checkable from a screenshot.

### F5. Banner blindness

**Claim.** Users ignore elements that look like, or sit where, ads usually are, even when those elements hold what they seek.

**Evidence.** Benway & Lane (1998; via secondary accounts, as the original PDF link was dead): target information presented in a large, colourful banner was *harder* to find than the same information in a text link. NN/g (Pernice, 2018-04-22; 26 participants, eyetracking): top banners and right rails got little attention. Content next to ads, or ad-styled (boxed, coloured, animated), is also ignored.

**Labels.** Strong heuristic / **B**.

**Implication.** Salience is not a universal lever. Styling important content like promotions makes it invisible, which matters for CTAs (R12) and announcements.

---

## Part 4. Competing principles (design tensions)

For each tension: what each side optimises, who benefits, who struggles, what the context depends on, and what evidence exists. I force no universal answer.

**T1. Simplicity vs discoverability.** A clean surface benefits people who already know the hidden actions. First-time and occasional users struggle. Evidence: hidden navigation cut use and discoverability (R1, B). Norman & Nielsen (2010-05-28, *Interactions*/jnd.org) argued that gestural interfaces broke visibility, consistency and discoverability because gestures "cannot readily be incorporated in menus" (expert argument, C). The context depends on how often a feature is used and whether any signifier or labelled entry point exists. The trade-off is surface clarity against the cost of finding things.

**T2. Consistency vs optimisation.** Consistency optimises learning and transfer (Polson, as cited by Grudin: B). Task-specific optimisation serves frequent, skilled use (Grudin's calculator and cursor-key cases: B). Occasional users of many tools benefit from consistency; daily experts benefit from optimisation. It depends on how often the product is used and how many other tools the user moves between.

**T3. Efficiency vs learnability.** Shortcuts and recall-based commands against menus and recognition. The evidence is that users plateau at "relative mediocrity" (Carroll & Rosson 1987: B) and do not migrate to shortcuts (Lane 2005: B). Bridges between the two, meaning recognition paths that teach the fast path, are the pattern. Whether bridges *cause* migration I did not verify; it is an open question.

**T4. Progressive disclosure vs visibility.** Hiding advanced functions protects novices from error states. Carroll & Carrithers' "training wheels" (1984, *CACM*; abstract read): blocking functions novices do not need gave faster learning and better comprehension (B). Hiding costs discoverability (R1). It depends on whether the hidden items are rare (then disclose progressively) or core (then show them).

**T5. Personalisation vs predictability.** Findlater & McGrenere (CHI 2004; search summary only) found most users preferred *adaptable* (user-controlled) menus to *adaptive* ones, though adaptive menus helped people who never customise. Gajos et al. (CHI 2008; 23 participants; abstract read): both predictability and accuracy raised satisfaction, and **accuracy had the stronger effect on performance**, contrary to the authors' hypothesis (B for small lab studies). Adaptation that is usually right beats a transparent but poor one. Wrong adaptations cost more than none.

**T6. Automation vs user control.** Bainbridge (1983, *Automatica*; first page read): automation leaves the operator "an arbitrary collection of tasks" that the designer could not automate. Manual skills decay, and monitoring is hard, so operators need *more* skill, not less. Strong heuristic / **B**: the source is argument plus cited process-control studies, and I did not trace later replications. In UI terms, automate with visible state, easy override and graceful handover.

**T7. Animation vs accessibility.** Animation aids tracking of change (Heer & Robertson: B) but harms vestibular users (WCAG 2.2 SC 2.3.3) and adds delay to frequent tasks. The resolution pattern: meaningful, short motion, plus honouring the reduce-motion setting.

**T8. Density vs readability.** Longer lines and denser text are read faster but preferred less (Dyson 2004: B). Density benefits scanning experts and harms first-time readers. Visual complexity lowers first-impression appeal (R7: A) but says nothing about expert efficiency. **Open question:** I found no controlled study in this area that measured expert task performance on dense against sparse professional dashboards. The Bloomberg and Excel cases need the product researchers' evidence.

**T9. Branding and aesthetics vs usability.** Beauty affects first impressions (A) and *sometimes* perceived usability (B, contradictory). Poor usability erodes perceived beauty (Tuch 2012). Brand distinctiveness can cut against *prototypicality*, which raises appeal (Tuch et al. 2012). **Familiarity vs innovation** (Raskin) is the same trade-off.

**T10. Delight vs speed; flexibility vs ease of use.** I found **no controlled evidence** directly measuring these trade-offs. Only mechanisms carry over: motion delay (R3), response-time limits (R16) and the paradox of the active user (R10). Treat claims either way as C/D.

---

## Part 5. Open questions and weak spots

1. **False positives in expert review.** The student-analyst studies show many (B). The professional CUE studies show few, but judged by expert consensus (C). A modern study with professional reviewers, falsification-based testing and AI reviewers would settle it. None found.
2. **AI screenshot review.** There is only a CHI 2024 paper on static mockups and one 2025 preprint (21.2% overlap with experts). Performance probably depends on the model, prompt and artefact. Treat any AI-generated review as one more evaluator subject to E1–E4, not as ground truth.
3. **Dense expert interfaces.** No controlled performance evidence found. These products' success also has network-effect and lock-in explanations, which the brief requires be ruled out.
4. **Hamburger evidence is 2014–2016.** Familiarity with the icon may have risen since. NN/g listed "low familiarity" as a cause, which could have changed. No newer controlled study found.
5. **Aesthetic–usability direction.** Contradictory lab results (Tractinsky 2000 against Tuch 2012). Hassenzahl & Monk suggest the effect is mediated and product-dependent.
6. **Untraceable numbers that circulate:** "20% more clicks on MENU" (one site, seen only second-hand), the Doherty dollar figures, 60-30-10, 7±2 for menus, "every page needs a CTA". None should appear as a number in the final output without that caveat.

---

## Outside my area

- **Native ads and scroll (Chartbeat 2014).** Only 24% of visitors scrolled on native-ad pages against 71% for normal content. This is relevant to business-versus-user tension and ad design.
- **OLED battery (Purdue 2021).** Dark-mode savings depend on brightness (39–47% at 100%, 3–9% at 30–50%). This is a platform and performance point for whoever covers mobile.
- **CUE reporting advice (Molich 2018).** Reports should run at most about 25 pages, open with a one-page executive summary, include positive findings, and use annotated screenshots. Useful to whoever writes the final review framework's output format.
- **Unmoderated testing.** Hertzum et al. (2014) found the evaluator effect is no smaller in unmoderated sessions, and the share of severe problems caught was lower (40% against 50%). Relevant to anyone recommending remote unmoderated tools.
