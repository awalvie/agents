# Notes: real products — the well designed, the rule-breakers and the failures

Area: benchmark portfolio, rule-breakers, criticized designs, failed redesigns, deceptive patterns, products as specimens. Visual/brand design and accessibility/public-service design are owned by another researcher and are not covered here except where they came up.

## How to read these notes

- **Observation date.** Every product observation is "as of 2026-09" unless it says otherwise. Where a claim is about an earlier version, the version or year is named.
- **What each observation rests on.** I could not install, run or log in to anything. Each product observation names its basis in brackets: [team] = the product team's own writing or statements; [filing] = regulator or court document, or a company's financial filing or earnings call; [press] = journalism; [users] = user reviews, forums or advocates (anecdote); [study] = peer-reviewed research; [shot] = my own screenshot of the public page, 2026-09-25.
- **Labels.** Cross-product findings carry two labels: *kind of claim* (fundamental principle / strong heuristic / context-dependent heuristic / useful pattern / design convention / aesthetic preference / unsupported or weak claim) and *evidence* (A–D). Single-product observations carry their source type instead.
- **Tool warning (read this).** The fetch tool summarizes pages with a small model. For one paper (Iacovides et al. 2015) its summary was made up: it gave the wrong sample size, study design and findings. I then read the PDF myself. After that I checked the key numbers I rely on against verbatim text or the primary PDF where I could, and `sources.md` marks which sources I read in full, which I only saw as a fetch summary, and which I only saw quoted elsewhere. Treat numbers marked "fetch summary" as less secure.
- **Blocked sources.** bloomberg.com, wired.com, HBR, SSRN, AIM Group and PubMed blocked fetching. I say below where I used an alternative route.

---

## Full specimen records

### 1. Bloomberg Terminal (native desktop, finance; enterprise)

- **Context.** Real-time market data, news, analytics, messaging and trading for finance professionals. It is a subscription product with a very large installed base: 325K+ users per Bloomberg's own 2023 LinkedIn post, and "375,000" per Wired as summarized by Slashdot (2026-04-28). [team; press]
- **Users / expertise.** Traders, analysts and portfolio managers. Mostly experts, trained on the job.
- **Primary tasks.** Monitor many instruments at once, pull a specific function fast, chat with counterparties, act on news.
- **Strengths.** Function codes typed on the command line (e.g., `PDFU COLORS <GO>` to change the colour scheme [team, via search snippet]) give experts direct, constant-time access to thousands of functions with no menu navigation. Launchpad and Worksheets let users build their own multi-monitor layouts [team: Bloomberg Professional, 2024-10-12]. The mappings stay the same for years, and the team treats that stability as a feature. CEO Lex Fenwick was quoted in 2010: "We have to be religiously consistent" [press: Leca, UX Magazine 2010].
- **Weaknesses.** Learning is slow. Leca reports a week and "a few painful hours" to become proficient, plus an 86-page manual [press, single first-person account]. CTO Shawn Edwards said in 2026 that the volume of data "has become more and more untenable. You miss things, or it takes too long" [press: Wired via Slashdot]. The company is now testing a chat interface (ASKB) with about a third of users. That is the vendor itself saying density plus command recall has hit a ceiling.
- **Information architecture.** A flat namespace of mnemonic functions addressed by code, not a browsable hierarchy. Securities are the organizing object: users load an instrument, then apply functions to it.
- **Navigation.** Command line plus user-arranged panels. Recall, not recognition.
- **Interaction.** Keyboard-first. I have not seen the special keyboard, so I did not assess it.
- **Visual design.** Dark background, dense coloured text (outside my area; see visual researcher).
- **Accessibility.** No audit found; not assessed. Bloomberg says it researched colour-vision deficiency with clients and shipped CVD colour schemes (2021-10-14) and estimates about 20,000 users with CVD. I saw these claims only in search snippets; bloomberg.com blocked fetching.
- **Performance.** Not assessed.
- **Cognitive experience.** It shifts load from perception (finding things) to memory (knowing codes). That suits people who repeat the same functions all day and fails anyone who works outside their repertoire.
- **Emotional experience.** Commentators argue users take pride in mastering it as a status marker [press: Leca 2010; Noe, Core77 2013]. Commenters under Noe's article dispute this: they say traders value speed and integrated data, not masochism [users]. Bloomberg says a 2007 font change drew "thousands of client messages" like "You changed perfection" [team, LinkedIn post].
- **Business context.** The data, the Instant Bloomberg chat network and employer-paid seats create lock-in and network effects that have nothing to do with the UI. **You cannot credit the design for its market position.** What the design demonstrably does is keep experts fast on a stable vocabulary.
- **Principles demonstrated.** Efficiency of use for experts (accelerators); consistency over *time*.
- **Principles violated.** "Recognition over recall"; "every interface should be immediately intuitive"; "reduce density".
- **Tradeoffs.** Speed for trained users at the cost of learnability and discoverability. Every change is expensive.
- **Evidence.** Mostly team statements and commentary. There is no published usability data. The primary UX article ("How Bloomberg Terminal UX designers conceal complexity", 2022) was blocked; I relied on Bloomberg's own LinkedIn post and search snippets that quote it.

### 2. Microsoft Excel (native desktop/web; general and expert)

- **Context.** A spreadsheet: a grid of cells, formulas that recalculate live, charts. Microsoft Research calls it "the world's most widely used programming language" and claims its formulas are written by "an order of magnitude" more people than all C/C++/C#/Java/Python programmers combined. **No source is given for that number** [team: Gordon & Peyton Jones, MSR blog, 2021].
- **Users / expertise.** Everyone from beginner to modeller; the population is mixed.
- **Primary tasks.** Lists, calculation, modelling, ad-hoc data exchange between systems ("human middleware" in The Register's phrase about PHE).
- **Strengths.** The grid is a visible, directly manipulable program state: you see every intermediate value. Calling a function takes little skill even if writing it takes a lot (MSR's point about LAMBDA) [team]. Excel tolerates messy, unplanned work.
- **Weaknesses: automation that silently changes data.**
  - Gene symbols such as SEPT2 and MARCH1 were auto-converted to dates. Studies found gene-name errors in about 20% of genomics papers with Excel supplements (Ziemann et al. 2016, seen quoted) and 30.9% (3,436/11,117) in a later scan (Abeysooriya et al. 2021) [study]. The Human Gene Nomenclature Committee *renamed human genes* (SEPT1→SEPTIN1, MARCH1→MARCHF1) rather than wait for the software to change [study].
  - Microsoft later added switches for each conversion. As of 2026-09 all four conversions (leading zeros, 15-digit truncation, "E" to scientific notation, date-like strings) are **on by default**, and "JAN 1" or "JAN-1" "may still be treated as dates" with the option off [team: Microsoft Support].
  - Public Health England, 25 Sep–2 Oct 2020: 15,841 positive cases went unreported because a pipeline used the legacy .xls format (65,536-row limit) and extra rows were **silently dropped**. The Register says about 48,000 contacts were not traced in time [press].
- **Information architecture.** Workbook → sheets → grid, plus the Ribbon (see specimen 3).
- **Navigation.** Spatial (cells and sheets), plus keyboard shortcuts that experts rely on.
- **Interaction.** Direct manipulation and live recalculation. There is no preview of type conversion at entry; the change is visible only if you look at the cell afterwards.
- **Visual design.** Dense grid; not assessed further.
- **Accessibility / performance.** Not assessed.
- **Cognitive experience.** Low barrier to start. Errors are invisible, because formulas are hidden behind values and conversions happen without notice.
- **Emotional experience.** Not assessed from sources.
- **Business context.** Bundled with Microsoft 365. Default and file-format lock-in shape adoption as much as the design does.
- **Principles demonstrated.** Visibility of state; direct manipulation; gentle slope from use to programming.
- **Principles violated.** "User control": silent, lossy automation. "Error prevention": a limit is exceeded and the software drops data without saying so.
- **Tradeoffs.** Convenience for the median user (typing "1/2" gives a date) against data integrity for specialists. The default protects the majority; the minority's losses are large, silent, and reach the scientific literature.
- **Evidence.** Two peer-reviewed prevalence studies, a regulator-adjacent incident, and Microsoft documentation. Reasonably strong for the *harm*; I did not find research on how the defaults affect ordinary users.

### 3. Microsoft Office 2007 Ribbon (historic redesign that held)

- **Context.** Office 2003 had grown to hundreds of menu items; Word went from 2 toolbars in Word 1.0 to 31 in Word 2003 [team talk notes: Harris at UX Week 2008, via Čuhalev]. Earlier fixes (adaptive menus, task panes) had not helped users find features.
- **Users / expertise.** Mixed; hundreds of millions.
- **Primary tasks.** Document creation. Most usage is concentrated in a few commands; the team's post invited readers to guess the top five, and they guessed Paste, Save, Copy, Undo, Bold.
- **What the team said.** Opt-in telemetry (SQM/Customer Experience Improvement Program) gave "about 1.3 billion sessions" and "over 352 million command bar clicks in Word over the last 90 days". Harris calls data "just one input". The data were the stated reason the redesign was possible at all: "for the first time, we have the data we need" [team: Harris, 2006-04-05, read in full].
- **The "90%" claim has two versions.** One is "about 90% of the feature requests for Office were for features already in the product" (John D. Cook 2009, citing the team). The other is "90% of users used less than 10% of all the features" (Harris's own site). **I found no method for either.** Treat both as unsupported folklore until a primary source turns up.
- **Outcome claims.** Word/Excel 2007 users reportedly "using four times as many features" (Katherine Murray's *First Look: Office 2010*, seen only as quoted by Cook, who calls it sales material). "Selling at twice previous volumes" appears only in talk notes. **Neither is independently checked.**
- **Weaknesses.** Experienced users reported lasting slowdowns and lost the ability to give verbal directions to features [users: comments on Cook 2009]. A commenter on Harris's post asked whether power users opt out of telemetry more often. That is a real sampling bias the post does not answer.
- **Principles demonstrated.** Recognition over recall; discoverability; live preview (see the result before committing).
- **Principles violated.** Consistency with prior versions: the change broke 20 years of habits.
- **Tradeoffs.** Discoverability for the majority against the relearning cost and screen space of experts.
- **Evidence.** Mostly team statements and commentary. The telemetry scale is well documented; the outcome figures are not.
- **Accessibility / performance.** Not assessed.

### 4. Craigslist (web and mobile web; classifieds)

- **Context.** Local classifieds: housing, jobs, for-sale, services, community.
- **Users / expertise.** A broad public; no expertise needed.
- **Primary tasks.** Post an ad; browse a category in a city; contact a stranger.
- **What the page is (as of 2026-09) [shot].** Desktop: a single page of text-link categories in columns with small emoji section headings, a search box, a "post an ad" button, a calendar and a list of nearby cities. Phone (390 px): a *different* layout, with a left rail of top-level categories (autos, community, for sale, gigs, housing, jobs, services) and subcategories on the right. **The "Craigslist never changes" story is out of date.** The mobile view has its own information architecture.
- **Strengths.** Every category is one tap away on a single page, and scanning it is fast. It is cheap to post, most categories are free, and it loads nothing heavy. Performance is not assessed; I found no measurement.
- **Weaknesses.** Weak trust mechanisms: no verified identities or reputation system. It is scam-prone; the site links "avoid scams & fraud" and "personal safety tips" from the home page [shot]. Listings are thin on photos and maps compared with vertical rivals.
- **Information architecture.** Geography → category → reverse-chronological listings. There is no ranking algorithm. Slate (2024) frames the absence of algorithms and profiles as a virtue [press].
- **Business context: the confounders.** Its dominance came from **network effects (market liquidity in each city), free posting and a first-mover position**, not from its design. AIM Group estimates (Craigslist is private, so these are **unaudited analyst estimates**) put revenue at $1.035B (2018), about $750M (2019), $660M (2021) and $302M (2024) [press: Fox Business 2020 and a Yahoo summary of the 2025 AIM/ResearchAndMarkets report]. Causes cited: the 2018 closure of personals, lost job-ad share, and Facebook Marketplace, OfferUp and Mercari. Andrew Parker's 2010 "unbundling of Craigslist" map showed single-category startups (Airbnb among them) peeling off categories [seen quoted: CB Insights].
- **What this shows.** The plain design did not cause the success, and design alone did not cause the decline either. Competitors won specific categories with *task-specific* design (photos, maps, identity, payments, trust) that a horizontal, text-only list cannot offer. At the same time, Facebook Marketplace brought its own social graph, which is also a network effect.
- **Principles demonstrated.** Directness; low interaction cost; "good enough" for high-liquidity markets.
- **Principles violated.** Visual hierarchy, trust signals, modern aesthetics.
- **Tradeoffs.** Simplicity and cost against trust and decision support.
- **Evidence.** Screenshots, journalism and analyst estimates. The primary Wired 2009 cover story (Gary Wolf) was blocked; I saw it only through Longreads and Fred Wilson's commentary.
- **Accessibility.** Not assessed.

### 5. Amazon Prime sign-up and cancellation (web; e-commerce)

- **Context.** Getting shoppers to subscribe to Prime, and the path out.
- **Users.** The general public, mostly non-experts in the flow.
- **What regulators found.**
  - The FTC (complaint 2023-06-21) alleged that the option to buy *without* Prime "was more difficult for consumers to locate". The cancellation flow was internally code-named "Iliad", after the epic about a ten-year war, and the complaint describes it as a "Four-Page, Six-Click, Fifteen-Option" process (complaint wording, seen quoted). The FTC also alleged that leadership "slowed or rejected changes that would've made it easier for users to cancel Prime because those changes adversely affected Amazon's bottom line" [filing].
  - Settlement, 2025-09-25: $1B civil penalty plus $1.5B in refunds to about 35M consumers. Amazon did **not** admit wrongdoing. Required changes include a clear decline button that cannot be worded "No, I don't want Free Shipping", disclosure of all material terms, and cancellation "through the same method used for signup". Internal documents quoted by the FTC include "subscription driving is a bit of a shady world" [filing].
  - By 2026-09-17 over $845M had been paid, and maximum payments were raised to $200 [filing].
  - The EU got there earlier: from 2022-07-01, EU/EEA users can cancel "with two clicks" using a prominent cancel button, after complaints from consumer groups (BEUC, the Norwegian Consumer Council and others) [filing: European Commission press release, seen via search].
- **Mechanism.** Several patterns combine. Asymmetric effort (one or two clicks in, many out). Misdirection (the decline option is harder to find). Confirmshaming (the decline wording implies you're refusing a benefit). Retention offers stacked inside the exit.
- **Business context.** Subscription retention is a revenue metric. Allegedly, UX fixes were measured, understood and rejected *because* they worked for users.
- **Principles violated.** User control and freedom; symmetry of effort; honest labelling.
- **Tradeoffs.** Short-term retention against legal risk, fines and trust. The fine is evidence that the tradeoff eventually got priced in.
- **Evidence.** Regulator documents. These are allegations settled without admission, not adjudicated findings.
- **Accessibility / performance / visual.** Not assessed.

### 6. Booking.com and hotel booking sites (web/app; travel)

- **Context.** Search, compare and book accommodation.
- **Users.** The general public; decisions are one-off and moderately high in stakes.
- **Strengths (as claimed).** It is one of the most cited cases of large-scale experimentation: "some 25,000 tests a year" (Thomke, HBR, March–April 2020). The article describes a December 2017 proposal by the director of design to test a radically simplified home page [press; HBR is paywalled, and **I could not read the outcome of that test**].
- **Weaknesses: what optimization found.** In 2019 the UK Competition and Markets Authority got binding commitments from Booking.com, Expedia, Hotels.com, Agoda, ebookers and trivago, effective 1 Sep 2019 [filing, via CMS law summary]. The sites must:
  - say whether paid commission affects ranking;
  - show all compulsory charges up front;
  - stop pressure selling (misleading claims about availability or popularity);
  - stop misleading discount claims (comparisons against inflated reference prices).
- **Mechanism.** If you optimize conversion with thousands of A/B tests and nothing else, the process will *find* deceptive patterns, because they convert. Luguri & Strahilevitz found mild dark patterns more than doubled sign-ups without measurable backlash (see cross-product F4). An experimentation culture is therefore not evidence of user-centred design. It amplifies whatever metric it is pointed at.
- **Principles demonstrated.** Evidence-based iteration.
- **Principles violated.** Honest urgency; transparent pricing; ranking you can interpret.
- **Tradeoffs.** Conversion against trust and regulatory exposure.
- **Evidence.** A regulator record; practitioner journalism (HBR). I did not verify Booking.com's current screens.
- **Accessibility / performance.** Not assessed.

### 7. Duolingo (mobile/web; learning)

- **Context.** Self-study language learning.
- **Users.** Mostly beginners, consumers, casual.
- **Primary tasks.** Do a short lesson daily; progress through a course.
- **Strengths: habit mechanics, measured by the team.** The streak counts consecutive days with at least one lesson. In a 2022-01-31 post [team] Duolingo reported:
  - new streak animations raised 7-day retention by "+1.7%";
  - allowing two Streak Freezes instead of one raised daily active learners by "+0.38%";
  - learners who reach a 7-day streak are "3.6 times more likely to complete their course". This is correlational; motivated learners may simply do both.
  The group PM for retention describes 600+ streak experiments. The biggest win he names was simplifying the streak from hitting an XP target to "complete one lesson a day" [team, podcast summary].
- **2022 path redesign.** Launched 2022-11-01. The branching skill tree became a single linear path. The stated reason was that learners "weren't sure whether they were using the app the 'correct' way", and the path builds in spaced repetition [team]. There was heavy backlash (petition, one-star reviews) [users]. CEO Luis von Ahn said "people are change averse", that testing showed "equivalent engagement", and that keeping two systems was hard. The tree did not come back [press: NBC News 2022-08-25].
- **Weaknesses.** Duolingo itself acknowledges that a broken streak "can feel quite demoralizing" [team]. Learners lost choice, including the option to do easy lessons when tired [users, quoted by NBC]. Efficacy evidence is **mostly produced by Duolingo's own research lab**. The 2024 efficacy summary gives no sample sizes and states no limitations [team].
- **Information architecture.** Course → sections → units → lessons along one path.
- **Navigation.** Linear; the next step is always obvious.
- **Cognitive experience.** Few decisions each session: the product removes "what should I do?". Retention mechanics rely on loss aversion.
- **Emotional experience.** Delight, and anxiety about losing a streak (Duolingo's own admission).
- **Business context.** Freemium and subscription. Daily active users are the key metric, so any engagement mechanic is also a revenue mechanic.
- **Principles demonstrated.** Reduce decisions for beginners; small, frequent wins; forgiveness mechanisms (freeze).
- **Principles violated.** User control over sequence, in the path redesign.
- **Tradeoffs.** Retention and guidance against autonomy. The metric measures return visits, not proficiency.
- **Evidence.** Team-reported experiment results (C), press and users.
- **Accessibility / performance.** Not assessed.

### 8. Sonos app, May 2024 (mobile; smart-home controller)

- **Context.** Controls multi-room speakers. The app *is* the product's interface; speakers have few physical controls.
- **Users.** Consumers, many long-time owners with large systems.
- **What happened.** The rebuilt app shipped 2024-05-07 without long-standing features. CEO Patrick Spence's letter (2024-07-25) names playlist and queue editing ("capabilities available since Sonos's inception"). The rewrite moved the architecture from UPnP to mDNS [team]. Sonos said it would invest "$20 million to $30 million" in recovery and later that the app "adversely affected our revenue by at least $100 million" [filing: earnings calls, via Investing.com summary]. It delayed new products and cut about 100 jobs. Spence left in January 2025 and board member Tom Conrad became CEO [press]. Bloomberg reported that employees had warned the app wasn't ready [press, seen via secondary coverage]. In February 2026 Sonos announced a new, phased overhaul described as "everything we should have done the first time" [press: MacRumors citing Bloomberg].
- **Accessibility (from public reports, not an audit).** Blind users and advocate Jonathan Mosen reported that VoiceOver was badly broken at launch: explore-by-touch failed, buttons were unlabelled, focus jumped, and moving between speakers took 3–5 swipes. A Sonos representative is quoted: "we took our eye off the ball". Sonos later recruited 30 visually impaired beta testers [users]. There is no formal audit, so "not assessed" strictly; the reports are detailed and consistent.
- **Mechanism.** This was a **regression**, not change aversion. Features, accessibility and reliability were removed from a product that owners had already paid for and could not replace with another controller. In Google's own framing (Sedley & Müller), aversion is a transition cost to a *better* product; this was a worse one.
- **Business context.** Hardware lock-in turned app quality into a question of whether the purchase still works. Complaints became accusations of broken products, not just dislike.
- **Principles violated.** Don't remove capabilities people rely on without a path back; ship accessibility with the feature, not after it.
- **Tradeoffs.** Engineering renewal (paying down technical debt) and launch schedule against continuity.
- **Evidence.** CEO letter, earnings statements, press, and user and advocate reports.
- **Performance.** Not assessed (no measurement found).

### 9. Snapchat 2018 redesign (mobile; social)

- **Context.** Ephemeral messaging and Stories.
- **What changed (announced 2017-11-29).** Friends' content moved to the left of the camera and publishers/Discover to the right. Friends' Stories went from chronological order to algorithmic sorting. Stated rationale from Evan Spiegel: "separating the social from the media". The press connected it to making the app easier for older, less tech-savvy users [press: TechCrunch].
- **Outcome.** Q2 2018: daily active users fell from 191M to 188M, the first decline ever. Snap said this was "primarily driven by a slightly lower frequency of use among our user base due to the disruption caused by our redesign". Snap also said retention among users over 35 improved [press reporting the earnings call]. A petition to reverse it reportedly passed 1.2M signatures [press].
- **Confounders (important).** At the same time, Instagram Stories reported 400M daily users, and Snap was still re-engineering a poorly performing Android app [press]. **The DAU drop cannot be attributed to design alone**, even though the company itself blamed the redesign.
- **Mechanism.** Fine as a model on paper (social ≠ media). But it broke location memory (where things were) and replaced a predictable order with an algorithmic one for core users.
- **Principles demonstrated / violated.** Clearer information architecture for newcomers; violated predictability and spatial stability for experts.
- **Tradeoffs.** Acquiring new or older users against the habits of the core.
- **Evidence.** Earnings reports as covered by the press.
- **Accessibility / performance / visual.** Not assessed.

### 10. Electronic health records (Epic, Oracle Health/Cerner and others; desktop; safety-critical)

- **Context.** Clinical documentation, ordering, results and medication administration.
- **Users / expertise.** Physicians, nurses and pharmacists. Expert in the domain, not necessarily in the software. They work under time pressure and interruption.
- **Evidence of harm.** Howe et al. (JAMA 2018) looked at 1.735M safety reports from 2013–2016. Of these, 557 (0.03%) had language explicitly suggesting that EHR usability contributed to possible patient harm. By category: data entry 27%, alerting 22%, interoperability 18%, visual display 9%, availability of information 9%, system automation and defaults 8%, workflow support 7% [study, verbatim-checked]. Examples:
  - a search for "q24h" returned look-alike frequencies;
  - an allergy alert did not fire;
  - a warfarin order defaulted to the wrong date.
  The authors note that reports capture only a small fraction of incidents.
- **Alert fatigue.** A review of 17 papers found drug safety alerts overridden in 49%–96% of cases, and some overriding is justified. It names error-producing conditions: low specificity, low sensitivity, unclear content, workflow disruption [study: van der Sijs et al., JAMIA 2006, abstract read].
- **Usability and burnout.** Physicians' mean System Usability Scale (SUS) score for their EHR was 45.9 ± 21.9, in the bottom 9% of SUS scores. Each point higher on SUS was associated with 3% lower odds of burnout (n = 870, cross-sectional) [study: Melnick et al. 2019, **seen only via abstract snippets**].
- **Business context.** The hospital buys the system; clinicians use it. Switching costs are enormous. Poor usability therefore persists without costing the vendor share. (This is my inference from the market structure; I found no study measuring it.)
- **Principles violated.** Signal-to-noise in alerts; defaults that match intent; look-alike items that are easy to confuse.
- **Tradeoffs.** Documentation, billing and liability requirements against clinical workflow.
- **Accessibility / performance.** Not assessed.

---

## Short entries

- **Figma UI3 (desktop/web, 2024).** Floating panels shipped in beta and were reversed for the full rollout: they "cramped the canvas, especially on smaller screens", and "the nail in the coffin was learning that they slowed people down". The team also found icon-only labels hurt screen-reader users and moved blend modes out of a hidden menu because tooltip delays broke workflows [team: Figma blog 2024-10-01]. *Teaches:* a visual simplification that removes screen space or adds hover-delays taxes the heaviest users most. Measuring speed, not asking for preference, settled the question. *Where it fails:* the evidence is self-reported and no numbers were published.
- **Wikipedia, Vector 2022 skin (web).** Deployed as the English Wikipedia default on 2023-01-18. The Wikimedia Foundation reports A/B tests on 50% of users and prototypes tested by about 200 editors each, with "no negative effects to pageviews, account creation, or edit rates". It says the old skin's line length was "more than three times the recommended value" [team; MediaWiki page gives little per-feature data]. The rollback RfC (closed 2023-03-16) found no consensus to roll back but made **unlimited width the default** [users/community record]. As of 2026-09 a visible "Appearance" panel offers text size, standard/wide width and light/dark [shot]. *Teaches:* when an evidence-based default (line length) meets an entrenched expert population, the resolution was *a user control*, not a winner. The RfC also shows that logged-out readers, the majority, cannot vote. Editor backlash therefore measures experts, not readers.
- **Instagram full-screen feed test (mobile, July 2022).** Adam Mosseri: "people are frustrated and the usage data isn't great… we need to take a big step back, regroup" [press: Platformer 2022-07-28]. *Teaches:* copying a rival's interaction model (TikTok's full-screen feed) onto a different content mix and intent failed on both sentiment and metrics. Here the two agreed, which is what made reversal easy.
- **Apple Photos, iOS 18 → iOS 26 (mobile).** iOS 18 removed the tab bar for one scrolling view. Apple's Billy Sorrentino said the app's density had grown, so "rather than hunt and peck throughout, we've created a simple streamlined single view" [press: 9to5Mac 2024-07-05]. After complaints, iOS 18.2 added fixes. At WWDC 2025 Craig Federighi said "Many of you missed using tabs in the Photos app", and iOS 26 restored Library and Collections tabs [press: TechCrunch 2025-06-09]. *Teaches:* one view with no tabs reduced visible chrome but removed a stable map of the app. Even Apple reversed it. Authority is not evidence.
- **Slack 2023 redesign (desktop/mobile).** Added Home, DMs and Activity tabs. Power users complained about whitespace, extra clicks and a catch-all Activity feed. Slack's product design SVP: "put focus front and center, and turn down the volume on cognitive load" [press: VentureBeat 2023-08-11]. I found no data from Slack. *Teaches:* "reduce cognitive load" by hiding things can mean more navigation for people who knew where everything was.
- **Linear (web/desktop; issue tracking).** Keyboard-first and opinionated, with fixed workflow categories. Its 2024 redesign aimed to "reduce visual noise… and increase the hierarchy and density of navigation elements". It moved themes to the LCH colour space, going from 98 theme variables to 3 inputs [team: Linear 2024-03-28]. Testing was internal dogfooding and a private beta [team]. *Where it fails:* opinionated software fits teams whose process matches its opinions. I found only comparison blogs of low quality, no independent study.
- **Notion (web/desktop).** Speed is a known complaint. Notion's own measurement: moving to WASM SQLite in the browser improved page navigation by 20% overall and 28–33% in Australia, China and India. Initial load did not improve, and slow devices didn't benefit [team, 2024-07-10]. *Performance (public measurement):* this is the team's own measurement, not an independent one.
- **Google Maps (web/mobile).** Justin O'Beirne (2017) argued that Google's lead over Apple Maps came from *data byproducts*: building footprints from imagery and "Areas of Interest" derived from buildings plus places. He places the advantage in data, not visual design [press/independent analysis; dated 2017]. *Teaches:* much of what looks like good map design is a data advantage. The same UI with worse data would not match it.
- **Airbnb total price (web/app).** Brian Chesky, November 2022: "I've heard you loud and clear—you feel like prices aren't transparent… Starting next month, you'll be able to see the total price." Fees now appear in search and you can sort by total. At launch taxes were still excluded [press: CBS News]. *Teaches:* drip pricing (low headline price, fees later) became a trust problem big enough for the CEO to fix. See also the CMA commitments above.
- **Uber surge pricing (mobile).** Uber's then head of economic research, Keith Chen, said on NPR's *Hidden Brain* (2016) that users with low phone batteries were more likely to accept surge pricing. He also said riders accept a 2.1× multiplier more readily than 2.0×, because a round number looks man-made. He said Uber did not use battery level for pricing [press: The Next Web 2016-05-20, **secondhand**; I could not load the NPR transcript]. *Teaches:* the company can see signals of user vulnerability, so restraint is a policy choice, not a technical limit.
- **Stripe payment methods (web; checkout).** Stripe's holdback experiment reports that showing at least one relevant non-card payment method gave +7.4% conversion and +12% revenue on average. Figures vary widely by region (e.g., Alipay, BLIK, iDEAL) [team: Stripe blog 2025-04-10]. *Teaches:* much of checkout "UX" is about offering the right payment method, not layout. The data are vendor-published and the vendor benefits.
- **Flighty (iOS; Apple Design Award 2023, Interaction).** Its founder says the goal is to feel "almost boringly obvious". It borrows airport departure boards ("one line per flight… 50 years of figuring out what's important"), and when connectivity drops before takeoff the Dynamic Island shows progress without live data [team, via Apple's "Behind the Design"]. *Teaches:* a proven convention from outside software can be the best model. The award is evidence of **reputation**; I found no usability data.
- **Dead Space and removing the HUD (games).** Dead Space showed health as a light strip on the character's suit spine, "diegetic by design" (the display exists inside the game world) [team: GDC 2013 talk, seen only via listings and snippets]. Iacovides et al. (CHI PLAY 2015; read in full) tested Battlefield 3 with and without the HUD. Study 1 (n = 9): no significant difference in enjoyment or frustration. Study 2 (n = 24; 10 experts, 14 novices): the condition × expertise interaction was only marginal (p = 0.051). **Experts'** immersion was higher without the HUD; novices were unaffected. The authors caution about sample size and a single game. *Teaches:* the value of visible status information depends on expertise. The evidence is weak (small n, one game).
- **Car touchscreens (automotive; safety-critical).** Vi Bilägare (2022-08-17) timed four simple tasks at 110 km/h. A 2005 Volvo V70 with physical controls took 10 s (306 m travelled); the worst modern car took 44.6 s (1,372 m) [press test]. The article does not report driver count or repetitions. From 2026, Euro NCAP awards top ratings only with physical controls for indicators, hazard lights, horn, wipers and eCall SOS [institution: ETSC summary 2024-03-06]. *Teaches:* in eyes-busy contexts, touch-only controls that need visual search fail. A safety body turned the heuristic into a scoring rule.
- **Hawaii false missile alert (2018-01-13; public safety).** FCC report (April 2018) [filing]:
  - "Test missile alert" and "Missile alert" sat in the same drop-down menu;
  - the confirmation read "Are you sure that you want to send this Alert?" for both;
  - the confirmation did not show the message text;
  - there was no template for a correction, and it took 38 minutes to correct.
  Crucially, the warning officer **believed the attack was real**: the drill recording included "this is not a drill". *Teaches:* a confirmation dialog protects only against slips, not against mistaken belief. The fixes are distinct test and live modes, a second person, and a pre-built correction path.
- **LinkedIn "Add Connections" (web; 2015).** Imported contacts got invitations plus two automatic reminder emails. Judge Lucy Koh found users "did not agree to the reminder emails". The settlement was $13M, and LinkedIn added a way to stop reminders [press: Newsweek 2015-10-05]. *Teaches:* growth features that act *in the user's name* without clear consent carry legal risk.
- **Google Drive launch (2012) as method.** Google defines change aversion as discomfort when "something familiar is replaced with something unfamiliar". It adds that if a product is "very difficult to learn or use, it cannot be because of change aversion, but due to fundamental design flaws". Its 10 steps include priming users, explaining benefits, letting them switch between new and old UI, and a direct feedback channel. The paper claims satisfaction was "significantly more positive" than for earlier launches, **but publishes no numbers** [team: Sedley & Müller, CHI EA 2013, read in full].

**Not researched (gaps).** GitHub, Discord, YouTube, Reddit (old/new), Revolut, Spotify, Netflix, Pinterest, Canva, Dropbox, SAP/Jira-class enterprise suites, and Indian startups. I ran out of time rather than found them uninteresting. The final writer should not treat their absence as a finding.

---

## Cross-product findings

**F1. Backlash is not a verdict: separate change aversion from regression.**
- *Claim.* Negative reaction to a redesign comes in two kinds with different fixes. (a) Transition cost to a product that is at least as capable, which fades. (b) Regression: lost capability, speed or access, which does not fade and should be reversed.
- *Evidence.* Regression cases:
  - Sonos removed features and accessibility; the reported revenue hit was at least $100M and the CEO left.
  - Figma measured a slowdown and reversed.
  - Instagram's sentiment and usage data both fell, and it reversed.
  - Apple Photos lost its navigation structure and got tabs back.
  Transition-cost cases:
  - Duolingo's path held "equivalent engagement" despite backlash and was kept.
  - The Office Ribbon was kept, though outcome data are thin.
  Google's own definition draws the same line.
- *Context.* Most useful for products with an established base.
- *Counterevidence.* Snapchat kept its design direction while losing DAUs, amid confounders. "Equivalent engagement" (Duolingo) can hide losses for a minority. Averages hide subgroups: experts, screen-reader users.
- *Example.* Sonos vs Duolingo.
- *Labels.* Strong heuristic; C (consistent across many cases, but each is company-reported, with few numbers).
- *Implication.* Before launch, list every capability and every accessibility path the old version had, and check it survives. After launch, measure task speed and completion **by segment** (experts, assistive-technology users), not only overall engagement. Keep a way back (Google's step 6) until those numbers recover.

**F2. For expert tools, stability of learned mappings is part of the product.**
- *Claim.* When users have invested in memorized paths (codes, positions, shortcuts), the cost of change grows with expertise. Minor visual changes can then have large costs.
- *Evidence.* Bloomberg ("religiously consistent"; thousands of complaints over a font change). Snapchat and Slack (spatial rearrangement angered core users). Ribbon (power-user slowdowns). Iacovides et al. (the effects of UI elements differ by expertise).
- *Counterevidence.* Bloomberg itself now says density plus recall is "untenable" and is adding a chat interface. Stability can freeze a design past its limits. Office changed radically and survived.
- *Context.* Frequent, repeated, time-pressured use.
- *Labels.* Context-dependent heuristic; C.
- *Implication.* Change expert surfaces additively (new paths alongside old) and incrementally. Keep keyboard and command vocabularies stable even while the visuals change.

**F3. Rule-breaking products that succeed are usually protected by something other than design.**
- *Claim.* Bloomberg (data plus chat network), Craigslist (liquidity plus free posting), Excel (bundling plus file format) and EHRs (institutional purchase) show that success despite poor or unconventional design usually traces to network effects, lock-in, price or buyer–user separation.
- *Evidence.* Craigslist's revenue decline as vertical rivals arrived (AIM estimates, unaudited). EHRs' SUS of 45.9 alongside market persistence.
- *Counterevidence.* The designs do deliver real benefits to their users: speed for Bloomberg experts, scan-ability on Craigslist, visibility of state in Excel. The benefit is real but not what explains market share.
- *Labels.* Context-dependent heuristic; C.
- *Implication.* Don't copy a rule-breaker's interface expecting its results. Copy the specific mechanism, such as constant-time command access or a single-page category index, and only where your users share its conditions.

**F4. Deceptive patterns measurably work, mild ones work quietly, so conversion optimization will find them.**
- *Claim.* Deceptive patterns reliably shift choices, and they are common.
- *Evidence.* Luguri & Strahilevitz, two large experiments on representative US samples (sample sizes of about 1,963 and 3,777 come from a fetch summary that also contained an arithmetic error, so check them before citing): mild patterns more than doubled acceptance and aggressive ones nearly quadrupled it. Only the aggressive ones produced measurable anger. Hidden information, trick questions and obstruction were the most effective, and less-educated participants were more susceptible [abstract]. Mathur et al. 2019 crawled about 11K shopping sites and found 1,818 instances of 15 types, and 22 third parties selling them as ready-made products [abstract via search]. Enforcement records: FTC/Amazon, the CMA hotel commitments, the EU/Amazon two-click commitment, LinkedIn.
- *Counterevidence.* Countdown and scarcity timers showed no significant effect in one Luguri study arm (per a fetch summary, not verified). The effects I found are measured on first choices; long-run churn and trust costs are not measured in these studies.
- *Labels.* Strong heuristic; B.
- *Implication.* Put ethics and regulatory guardrail metrics into experimentation platforms. Examples: the ratio of cancellation to sign-up effort, the visibility of the decline option, and whether all-in price appears first. Otherwise A/B testing will select for manipulation.

**F5. Symmetry of effort: leaving should be as easy as joining.**
- *Claim.* Enrollment and exit should use the same channel and similar effort.
- *Evidence.* The FTC order ("cancellation through the same method used for signup") and the EU two-click cancel. Obstruction was among the most effective dark patterns in Luguri & Strahilevitz.
- *Labels.* Design convention (now legally backed in the US and EU); B.
- *Implication.* Count the clicks and screens for sign-up and for cancel, and make them match. Put retention offers *after* a confirmed cancellation option, not in its way.

**F6. In high-consequence systems, confirmation dialogs and alerts wear out; modes and defaults do the real work.**
- *Claim.* Identical confirmations, mixed test/live controls, noisy alerts and wrong defaults cause harm. Adding more confirmations does not help.
- *Evidence.* Hawaii (the same prompt for test and live; the operator believed the attack was real). EHR alerts overridden in 49–96% of cases. In Howe et al., alerting was 22% and automation/defaults 8% of usability-linked harm reports.
- *Context.* Safety-critical and fatigue-prone work.
- *Counterevidence.* Some overriding is appropriate (van der Sijs), so a high override rate alone is not failure.
- *Labels.* Strong heuristic; B.
- *Implication.* Separate modes physically or visually. Show the actual content being committed. Use two-person rules for irreversible broadcasts. Tune alerts for specificity. Design the correction path before the error happens.

**F7. Silent automation fails the minority it wasn't designed for, at scale.**
- *Claim.* "Helpful" automatic transforms that change data invisibly, like Excel's type conversion and the .xls truncation, cause large, persistent errors for specialists.
- *Evidence.* 30.9% of Excel-supplement genomics papers contained gene-name errors. The fix took two forms: humans renaming genes, then opt-out switches that are still default-on and incomplete. PHE lost 15,841 cases to silent truncation.
- *Counterevidence.* I have no data on how much the defaults help typical users. The benefit is plausible but unmeasured.
- *Labels.* Strong heuristic; B.
- *Implication.* Make automatic transformations visible and undoable at the moment they happen. Fail loudly when a limit is hit. For data import, default to preserving the data.

**F8. "Clean" simplification often costs experts speed. Measure speed, not looks.**
- *Claim.* Redesigns that reduce visible density (floating panels, single views, more whitespace, hidden tabs) often slow frequent users.
- *Evidence.* Figma (measured slowdown), Apple Photos (reversed), Slack (complaints), Instagram (usage data).
- *Counterevidence.* Vector 2022's limited width is density *reduction* backed by line-length guidance and "no negative effects" on core metrics. The dispute there was preference, and a user control resolved it. The Ribbon added *visible* density and improved discoverability.
- *Labels.* Context-dependent heuristic; C.
- *Implication.* Before shipping a simplification, time the top tasks with experienced users. If simplifying, keep a density or width control.

**F9. Engagement mechanics are real levers, but they measure return visits, not the user's goal.**
- *Claim.* Streaks, freezes and a linear path raise retention; that does not show they deliver the outcome users came for.
- *Evidence.* Duolingo's own experiments show small but significant retention lifts (+1.7%, +0.38%), and its CEO reports engagement parity for the path. The learning evidence is largely company-run.
- *Counterevidence.* Forgiveness mechanisms (freezes) show Duolingo designing *against* the pure loss-aversion extreme. I found no independent evidence that streaks harm learning.
- *Labels.* Useful pattern; C.
- *Implication.* Pair engagement metrics with outcome metrics. Add forgiveness (freezes, grace periods) to any streak.

**F10. In eyes-busy or divided-attention contexts, tactile controls beat touchscreen menus for frequent, critical functions.**
- *Evidence.* Vi Bilägare's timing test (a single magazine test), backed by Euro NCAP's 2026 scoring and ETSC.
- *Counterevidence.* Voice control was not tested. Touchscreens can host rarely used settings well.
- *Labels.* Strong heuristic; C (I did not read the driving-distraction literature; the visual or HCI researcher may have better evidence).
- *Implication.* Give the functions that are critical and frequent a fixed physical control, or at least a fixed position. Menus are for the rest.

**F11. Usage telemetry makes redesigns possible but has blind spots.**
- *Evidence.* Office SQM (1.3B sessions) drove the Ribbon. A reader asked whether cynical power users opt out more, and Harris calls data "just one input". Wikipedia's A/B tests covered readers, while the vote came from editors.
- *Labels.* Context-dependent heuristic; C.
- *Implication.* Weight telemetry by who is in the sample. Pair it with longitudinal studies of experts. Harris reported that longitudinal testing over weeks was the most valuable method (talk notes).

### Tensions seen across products

- **Learnability vs efficiency:** Bloomberg vs Ribbon. It is resolved by *adding* recognition paths without removing recall paths. Bloomberg's ASKB and Office's retention of keyboard shortcuts both do this.
- **Business vs user goals:** Amazon, Booking, Airbnb fees, Uber. Regulators increasingly set the boundary: FTC ROSCA, the EU UCPD, UK CMA.
- **Automation vs control:** Excel conversions; Snapchat's algorithmic Stories; Apple Photos' "deep intelligence" single view. Users react most strongly when automation replaces a predictable order.
- **Guidance vs autonomy:** Duolingo's path. Beginners gain and experienced learners lose.
- **Evidence-based defaults vs expert preference:** Vector 2022. The resolution was a visible user control.

### Open questions

- There is no independent, published usability data for Bloomberg, Linear or the Ribbon's outcomes. Most "success" claims are self-reports.
- Does the Duolingo path improve learning, not only engagement? The team says it compared path and tree, but I did not find the data.
- Do mild dark patterns cost long-run trust or churn? The experiments measure the first choice only.
- Why do the Excel conversions still default to on? I found no Microsoft rationale.
- How much of Snapchat's 2018 decline was design vs Android performance vs Instagram Stories? It cannot be separated from public data.

---

## Outside my area

- **Accessibility:** Sonos's 2024 VoiceOver failures (Mosen). Figma says icon-only labels hurt screen-reader users. Bloomberg's CVD themes (claims seen only in snippets). Linear's LCH colour system generates high-contrast themes automatically. Pass these to the accessibility researcher; none is a formal audit against WCAG 2.2.
- **Line length:** Wikipedia's claim that the old line length was more than three times the recommended value. The research behind that recommendation belongs to the visual/typography researcher.
