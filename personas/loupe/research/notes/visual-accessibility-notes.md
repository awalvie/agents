# Notes: visual design, accessibility and performance

Researcher area: visual design, design systems and tokens, brand expression, accessibility, and performance as users feel it. Written 2026-09-25.

## How to read these notes

- Every finding has two labels, following the brief. **Kind** is one of the seven claim classes. **Evidence** is a grade from A to D. A single observation of a product carries its source type in place of the labels.
- A product observation marked "as of 2026-09" rests on my own screenshots, taken 2026-09-25 and saved in `out/shots/`, or on the product's own documentation. I could not log in to any product, so I did not see any app's inside.
- **What I could not do.** I wrote a script to read computed CSS colours and calculate WCAG 2.2 contrast ratios and APCA values on Linear, Stripe and Vercel. The sandbox refused to run it, because it needs approval that this session cannot give. So none of my product findings includes a measured contrast figure. When I say text "looks low contrast", that is my visual impression of a screenshot, not a measurement. The BBC GEL guidance pages returned "Page temporarily unavailable" both by fetch and by screenshot, so BBC is thinly covered.
- Several PDFs could not be parsed as text. I read them as page images instead: the Google/DoubleClick report, Parhi et al. 2006, Tuch et al. 2012, Dyson 2004 and Harrison et al. 2010. The sources file says which parts I read.

---

## 1. Aesthetics, usability and "avoid aesthetic bias"

### 1.1 Beauty does not reliably make an interface more usable. Bad usability makes it look worse.
- **Claim.** The "aesthetic-usability effect" (what is beautiful is usable) is weaker and less consistent than design folklore says. The better-supported direction runs the other way: how well a product works changes how good it looks to people after they use it.
- **Evidence.**
  - Tuch, Roth, Hornbæk, Opwis & Bargas-Avila (2012, *Computers in Human Behavior*) ran a lab experiment with 80 participants. They manipulated aesthetics (low or high) and usability (low or high) independently in one online shop, and used four validated instruments. Aesthetics did not affect perceived usability. Usability did affect post-use aesthetics, and frustration appeared to mediate that effect.
  - Hassenzahl & Monk (2010, *HCI* journal) reviewed 15 papers with 25 correlations between beauty and perceived usability. The coefficients varied "remarkably". In their own data, the link ran entirely through a general "goodness" judgment.
  - The original positive findings were Kurosu & Kashimura (1995) and Tractinsky et al. (2000). I only saw these cited inside Tuch et al.; I did not read them.
- **Context.** The effect is strongest on first impressions and on self-reported ratings. It is weakest on measured task performance and after real use.
- **Counterevidence.** Sonderegger & Sauer (2010, cited in Tuch et al.; I did not read it) reported that a better-looking phone prototype also improved measured performance. So the effect is not zero in every study.
- **Example.** Apple's iOS 26 Liquid Glass (section 10.1). It was widely called beautiful, yet the criticism was about legibility and unstable controls, the costs you only feel in use.
- **Labels.** Kind: context-dependent heuristic ("beauty raises *first-impression* ratings"). Evidence: B. The strong form ("beautiful is usable") is an unsupported or weak claim, evidence C.
- **Implication.** Never use visual polish as evidence of usability in a review. Rate aesthetics, usability, accessibility and efficiency separately. Expect a product that frustrates people to lose its "beauty" in their eyes over time.

### 1.2 First impressions of aesthetics form within 17–50 ms, driven by visual complexity and prototypicality
- **Claim.** People judge a website's appeal in under a twentieth of a second. Lower visual complexity and a layout that looks like a typical site for its category both raise that judgment.
- **Evidence.**
  - Tuch, Presslaber, Stöcklin, Opwis & Bargas-Avila (2012, *IJHCS*; Google Research co-published) used 119 real-site screenshots shown for 50, 500 or 1000 ms. Complexity and prototypicality affected ratings at 50 ms. A second study found effects at 17 ms, with prototypicality's effect weaker than complexity's.
  - Reinecke et al. (CHI 2013) collected ratings of 450 sites from 548 volunteers. Their computed colourfulness and complexity, combined with demographics such as age and education, explained about half the variance in appeal at 500 ms. Preferences differed across demographic groups.
- **Context.** First exposure, static screenshots, no task.
- **Counterevidence.** These measure liking, not use. Given 1.1, a first-impression win can be reversed by use.
- **Labels.** Kind: strong heuristic (for first impressions). Evidence: A–B (two independent groups, several studies).
- **Implication.** Prototypicality is a real force. A radically unconventional landing page pays a first-impression cost, and the design has to earn that cost back. "Clean" wins the first glance, but that says nothing about the tenth hour of use.

### 1.3 Separate the dimensions: a worked split for this area's benchmarks
The table below (as of 2026-09) shows that the dimensions do not move together. The "evidence" column says what each judgment rests on.

| Product | Aesthetic reputation | Usability / accessibility evidence I found | Evidence type |
|---|---|---|---|
| Apple iOS 26 | Very high | Expert review found legibility, target and stability problems; Apple changed the design in iOS 27 | NN/g expert review; Apple's changes reported by MacRumors |
| Linear | Very high, and widely imitated | Speed rests on architecture, not visuals; team reports raising contrast in 2024; no public accessibility audit found | Team blog; engineering write-up endorsed by Linear's CTO |
| Stripe | High | Team documented that none of its default text colours met WCAG AA in 2019, then fixed this systematically | Team blog |
| GOV.UK | Plain, "ordinary" | Audited as fully WCAG 2.2 AA (Design System site, July 2024); the error pattern was tested in live services | Accessibility statement; design-system docs |

- **Labels.** Kind: fundamental principle ("these dimensions are distinct and can diverge"). Evidence: A. The literature in 1.1 and every specimen here show the split.

---

## 2. Visual hierarchy, signifiers and flatness

### 2.1 Weak clickability signifiers cost time and attention. The cost shrinks on simple pages.
- **Claim.** Flat styling that removes cues showing an element is interactive (underlines, button shapes, contrast) makes people slower to find what they can click.
- **Evidence.** NN/g (Kate Moran, 2017): 71 participants, eyetracking, 9 pairs of real-site pages, between-subjects. On weak-signifier versions, people took 22% more time and made 25% more fixations. Six of nine pairs showed different gaze patterns. Burmistrov et al. (INTERACT 2015, EyeLink 1000) found slower search for icons and clickable objects in flat designs. I only read the abstract-level summary of that paper.
- **Context.** The three NN/g pairs with no difference were low in density, used a traditional layout, and had high-contrast targets.
- **Counterevidence.** Both are single-page findability tasks, not learned, repeated use. Experts in a familiar app may not pay this cost.
- **Example.** Liquid Glass, where controls "appear, vanish, collapse" (section 10.1). GOV.UK's always-underlined links (as of 2026-09, screenshot `govuk-passport-mobile.png`) take the opposite approach.
- **Labels.** Kind: strong heuristic. Evidence: B (one well-run study plus one supporting study).
- **Implication.** Flatness is safe when the page is sparse and conventional. The denser or more novel the page, the more signifier strength you need.

### 2.2 Density is a tool of hierarchy, not an enemy of it
- **Claim.** Dense products stay usable by ranking visual weight, not by removing content. Chrome (navigation, sidebars) should recede so that content leads.
- **Evidence.** Linear's March 2026 refresh (Aufmann & Heckel, team blog) is a documented case. They dimmed the sidebar because it "remained visually prominent even after a user had reached their destination". They used fewer and smaller icons, removed coloured team-icon backgrounds, and softened separators, all while "preserving the rich density". There is no outcome data. User feedback noted that removing borders cost section contrast in light mode (Linear's LinkedIn announcement comments, seen via search summary only).
- **Counterevidence.** Dimming chrome lowers its contrast. That is exactly the users-with-low-vision cost described in section 8.8.
- **Labels.** Kind: useful pattern. Evidence: C (team case study, no measurement).
- **Implication.** When a dense product feels noisy, first reduce the *weight* of low-priority elements before removing any of them. Then check the contrast of what you dimmed.

---

## 3. Typography

### 3.1 Bigger body text reads better than the old web default, up to about 18 pt
- **Evidence.** Rello, Pielot & Marcos (CHI 2016): 104 participants read Wikipedia articles at 10–26 pt with line spacing from 0.8 to 1.8, while an eyetracker recorded them. Readability measured by fixation duration, and comprehension, improved up to 18 pt, with fixation duration shortest at 22 pt. Subjective readability peaked at 18 pt. Line spacing had "only minimal effects". The authors equate 18 pt to 24 px (author's blog).
- **Context.** Desktop Wikipedia reading. Device and distance were not given in the summary I read.
- **Counterevidence.** Bigger type means fewer words per screen. For people with tunnel vision, that is harmful (section 8.8). Dense expert tools trade reading comfort for overview.
- **Example.** Apple HIG (as of 2026-09): iOS default body is 17 pt with a minimum of 11 pt. It advises avoiding Ultralight, Thin and Light weights at small sizes.
- **Labels.** Kind: context-dependent heuristic (for long-form reading). Evidence: B.
- **Implication.** For reading-heavy screens, default larger than 16 px and support user scaling. Do not apply this rule to data-dense tools.

### 3.2 The "45–75 characters per line" rule is a typographic convention. Screen studies are mixed.
- **Evidence.** Dyson's review (2004, *Behaviour & IT*) is the key source. Dyson & Kipping (1998) had 48 participants read 25–100 characters per line (cpl). The *longest* line (100 cpl) was read fastest, partly because it needed less scrolling. Bernard et al. (2002) tested 45, 76 and 132 cpl and found no difference in reading time. Dyson & Haselgrove (2001) found 55 cpl best overall at normal and fast reading speeds, and better for comprehension than 100 cpl. Dyson notes that characters per line, type size and physical length are confounded in many studies.
- **Labels.** Kind: design convention (moderate measure). Evidence: C for a specific range. Speed does not reliably favour short lines, and readers' preference for moderate lines is the steadier finding.
- **Implication.** Choose a moderate measure for comfort and preference. Do not claim it is "proven faster". Scanning tasks and reference tables can justify long lines.

### 3.3 Light mode reads better for most people. Some people with low vision need dark mode.
- **Evidence.** Piepenbrock, Mayr & Buchner (2013, *Ergonomics*) found a positive-polarity (dark text on light) advantage for visual acuity and proofreading in both younger and older adults. The advantage was smaller in older adults and in their 2014 follow-up it was larger for small characters. Per NN/g's summary (Budiu, 2020), Legge (1985) found that people with cloudy ocular media read faster in negative polarity. I did not read Legge directly.
- **Labels.** Kind: context-dependent heuristic. Evidence: B.
- **Implication.** Default to light for reading, offer dark, and honour the system setting. "Dark mode is better" is an aesthetic preference, and in some cases a medical need. It is not a general usability rule.

### 3.4 Optical sizing and tracking are mechanisms, not decoration
- **Evidence.** Apple HIG (as of 2026-09): the system font interpolates optical size and adjusts tracking "at every point size". Linear (2024) switched headings to Inter Display while keeping Inter for body text, "to increase expression while maintaining readability".
- **Labels.** Kind: useful pattern. Evidence: C (vendor practice; I found no user study).
- **Implication.** Much of what makes type feel "premium" is display cuts at large sizes, tighter tracking there, and text cuts at small sizes. This is cheap to copy and rarely hurts use.

---

## 4. Colour systems and contrast

### 4.1 Where WCAG 2's 4.5:1 comes from
- **Evidence.** W3C *Understanding SC 1.4.3* (WCAG 2.2) explains the numbers. 3:1 is the minimum in ISO 9241-3 and ANSI/HFES 100-1988 for normal vision. 4.5:1 "compensated for the loss in contrast sensitivity usually experienced by users with vision loss equivalent to approximately 20/40". 7:1 covers roughly 20/80. The formula's 0.05 term models "typical viewing flare". The document does not discuss whether the ratio matches human perception.
- **Labels.** Kind: design convention with a legal role, since WCAG 2.x AA is the legal benchmark in many jurisdictions. Evidence: B for the principle that more luminance contrast helps low vision. The specific thresholds rest on standards and one empirical relationship (acuity to contrast-sensitivity loss). I did not trace that relationship to its original study.

### 4.2 The APCA debate. Status as of 2026-09: unresolved, and APCA is not a standard.
- **Claim.** The WCAG 2 ratio misjudges some colour pairs, especially dark pairs and light text on mid-tones. APCA, which accounts for polarity and depends on font size and weight, is a proposed replacement. It has not been adopted.
- **Evidence for the problem.** In W3C Low Vision Task Force GitHub discussion #131 (2021–22), APCA's author (Andrew Somers) and an independent contributor (sdw32) compared the two algorithms on thousands of random colour pairs. They found WCAG 2 "false passes" in about 34–56% of some subsets, and false failures for white text.
- **Why this evidence is weaker than it looks.** "False" was defined *relative to APCA itself*. That is circular, and it is not a test with human readers. The same thread notes that "the full set of experimental results that support the latest version... have not been published" (as of January 2022), and that neither algorithm models colour vision deficiency.
- **Status.** Adrian Roselli's post (April 2026, updated April 13) says APCA was removed from the WCAG 3 drafts in mid-2023 after failing to gain Working Group support. The WCAG 3 Editor's Draft of 8 April 2026 says "the contrast algorithm used in WCAG 3 is yet to be determined". WCAG 3 is expected around 2030 at the earliest.
- **Counterevidence and nuance.** The *direction* of the critique, that the ratio is symmetric and perception is not, is plausible, and designers widely observe it in dark themes. So the problem is credible even though the fix is unvalidated.
- **Labels.** "WCAG 2 contrast mis-ranks some colour pairs": context-dependent heuristic, evidence C, because it rests on analysis without published tests on readers. "APCA is the correct replacement": unsupported or weak claim, evidence D as a validated standard.
- **Implication.** Pass WCAG 2.2 for legal conformance. Where you design dark themes or mid-tone brand colours, *also* check a perceptual measure and your own eyes, and treat that as an extra check, not a substitute. Distrust tools and vendors that call APCA "the WCAG 3 method".

### 4.3 Build colour scales in a perceptually uniform space so contrast is guaranteed by structure
- **Claim.** If palette steps are spaced by perceptual lightness, you can promise contrast by rule ("N steps apart passes") rather than checking pair by pair. This also lets a brand keep its vibrancy while becoming accessible.
- **Evidence.**
  - Stripe (Koopersmith & Miner, 15 Oct 2019): none of Stripe's default text colours met 4.5:1, and simply darkening them made the palette "dark and muddy". They rebuilt the palette in CIELAB. The rule became "any two colors are guaranteed to have sufficient contrast for small text if they are at least five levels apart, and at least four levels apart for icons and large text."
  - Linear (28 Mar 2024) moved from HSL to LCH. Themes went from 98 variables to three (base, accent, contrast), and the contrast variable "automatically include[s] super high-contrast themes".
  - Vercel Geist (as of 2026-09) maps each of its 10 steps to a *role*: 100–300 backgrounds, 400–600 borders, 700–800 high-contrast fills, 900–1000 text. It makes no explicit contrast-ratio claim.
- **Context.** This works for systems with many themes or many brands.
- **Counterevidence.** Perceptual spaces are uniform only approximately. Hues that are out of gamut compress. A guarantee by rule still relies on the WCAG 2 ratio, which has the limits in 4.2.
- **Labels.** Kind: useful pattern. Evidence: C (three independent team write-ups; I found no outcome study). The mechanism is well founded in colour science.
- **Implication.** Name tokens by role (background, border, text) and space them perceptually. The system then prevents inaccessible pairings instead of catching them in review.

### 4.4 Never rely on colour alone
- **Evidence.** Birch (2012, *JOSA A*): about 8% of men and 0.4% of women of European descent have red–green colour deficiency, and 4–6.5% of Chinese and Japanese men. WCAG 2.2 SC 1.4.1 covers the use of colour.
- **Labels.** Kind: fundamental principle. Evidence: A.
- **Example.** GOV.UK error messages pair red with a thick border, the heading "There is a problem", linked text, and a hidden "Error:" prefix (as of 2026-09, `govuk-error-summary.png`).

---

## 5. Design systems and design tokens

### 5.1 Tokens now have a standard format, but the standard only covers the format
- **Evidence.** The W3C Design Tokens Community Group published the first stable Design Tokens Format Module, **2025.10**, on 28 Oct 2025. It is a *Community Group* specification, not a W3C Recommendation. It covers theming and multi-brand, colour spaces including Display P3 and OKLCH, aliases, inheritance and component references. Style Dictionary, Tokens Studio and Terrazzo provide reference implementations, and Figma, Sketch, Penpot, Framer and others support it or are implementing it.
- **Labels.** Kind: design convention. Evidence: not applicable (this is a fact about the standard).
- **Implication.** Tokens make decisions portable. They do not make those decisions good. A token system can faithfully spread an inaccessible colour to every platform.

### 5.2 How mature organisations structure tokens, and why
- **Pattern.** Mature systems use tiers. *Primitive* values (for example, grey-42 = #6B6B6B) are aliased to *semantic* roles (for example, text-secondary), and sometimes to *component* tokens. Nathan Curtis (EightShapes) describes a naming grammar: namespace, category, concept, property, variant, state, scale. His site was unreachable and the Medium article returned 403, so I have this only from summaries of his work, not his text.
- **Why.** You can re-theme (dark mode, high contrast, sub-brands) by changing the alias layer without touching components. Linear's 98→3 variables and Stripe's step rule are examples.
- **Limit.** Curtis reports redesigning taxonomies for four systems (seen via summary only). That suggests that getting naming wrong is common and expensive to fix.
- **Labels.** Kind: useful pattern. Evidence: C.

### 5.3 Vendor claims about the value of design systems are best cases
- **Evidence.**
  - Figma (Clancy Slack, 19 Dec 2019): designers finished a task 34% faster with a design system than without one. By the post's own account, the system was "directly applicable" and up to date, and designers chose their own stopping point. The post gives no participant count, and the sponsor sells design-system tooling.
  - Google, Material 3 Expressive (Google Design article, undated as I viewed it): 46 studies and more than 18,000 participants. People spotted key elements "up to four times faster". The baseline was *Google's own current Material 3*, "up to" marks the best case (an enlarged Send button), and the studies are unpublished and not peer reviewed. The article admits that removing familiar patterns (for example, a song list replaced by scattered album art) hurt usability, and says older users found key elements as fast as younger users.
- **Labels.** "Design systems speed up design": context-dependent heuristic, evidence C. "Expressive design is 4× faster": unsupported or weak claim as a general statement, evidence C for the narrow result.
- **Implication.** Quote these numbers only with their conditions attached. The honest mechanism behind the M3E result is familiar: make the primary action bigger, higher in contrast and more distinct, and it gets found faster. That is ordinary hierarchy under a new name.

### 5.4 Limits of design systems: sameness and borrowed authority
- **Evidence.** Practitioners widely describe "the Linear look" (Frontend Horse, before 2024): dark backgrounds, glows, bento grids, thin lines, gradient headings. They call it the default for SaaS marketing sites, and designers complain of homogeneity (Overpass Studio and LogRocket, practitioner sources). I found no study of whether sameness hurts or helps conversion or trust.
- **Mechanism (my inference, D).** Copying a respected product's surface borrows its first-impression prototypicality (1.2). It does not borrow the substance that produced the reputation: Linear's speed comes from its sync engine (9.6).
- **Labels.** Kind: open question. Evidence: D.

---

## 6. Motion

### 6.1 Reduce Motion exists because real users got sick. The rule's evidence base is thin.
- **Evidence.**
  - iOS 7 (September 2013) drew reports on Apple's forums of nausea and vertigo from parallax and zoom transitions. MacRumors (26 Sep 2013) and Scientific American covered them. I have these via search summaries. Early coverage said Reduce Motion removed only parallax, not the zooms.
  - W3C *Understanding SC 2.3.3 Animation from Interactions* is **AAA** only in WCAG 2.2. It cites no clinical research, only practitioner articles and browser docs.
  - The widely repeated "35% of adults over 40 have vestibular dysfunction" comes from Agrawal et al. 2009 (NHANES 2001–04). That study defined dysfunction as failing to balance on foam with eyes closed for 30 seconds. **It is not a measure of sensitivity to on-screen motion**, so using it to size the problem for UI motion is a misuse.
- **Apple's current guidance** (HIG, as of 2026-09): with Reduce Motion on, tighten springs, track gestures directly, avoid z-axis depth animation, replace movement along x, y and z with fades, and avoid animating into and out of blurs.
- **Labels.** "Provide a way to reduce non-essential motion": strong heuristic, evidence C (many consistent user reports, no controlled prevalence data for UI triggers). The 35% figure applied to UI motion: unsupported or weak claim.
- **Implication.** Honour `prefers-reduced-motion` and the OS setting. Swap large movement (parallax, zoom, depth) for fades. Keep motion that explains what changed, but make it smaller. Do not quote the 35% figure as a count of people sensitive to UI motion.

### 6.2 Motion that serves no purpose is a cost, even for users without motion sensitivity
- **Evidence.** NN/g's review of iOS 26 (Budiu, 10 Oct 2025, expert review with no user testing) calls out pulsating buttons, shimmering text and animated tab switches: "Motion for motion's sake is not usability."
- **Labels.** Kind: strong heuristic. Evidence: C.
- **Tension.** Delight versus speed and attention. Motion that reveals spatial relationships (where a sheet came from) earns its place. Motion that decorates competes with the content for attention.

---

## 7. Internationalisation and data display

### 7.1 Short strings expand the most
- **Evidence.** W3C Internationalization, *Text size in translation* (undated as viewed), reproduces IBM's guideline table. Strings of up to 10 characters grow by 200–300%, and strings over 70 characters grow by 130%. The IBM source is undated. Its 51–70 row (151–170%) is higher than its 31–50 row (140–160%), which is odd and may be a transcription error. It is also unclear whether "200%" means twice as long or growing *by* 200%. The article also notes that CJK, Thai, Arabic and Devanagari scripts need more vertical space than Latin.
- **Labels.** Kind: strong heuristic ("labels and buttons need the most room"). Evidence: C for the exact percentages (single untraced source).
- **Implication.** Don't size buttons to their English text, and don't fix line height for Latin script only. Test with a pseudo-locale that pads short strings the most.

### 7.2 Right-to-left layout mirrors *direction*, not *objects*
- **Evidence.** Apple HIG *Right to left* (as of 2026-09) says to flip back and next controls, sliders and progress indicators, and icons that show reading direction. It says not to flip photographs, logos, checkmarks, clocks, or the digits within a specific number. It suggests raising Arabic and Hebrew text by about 2 pt beside uppercase Latin, because those scripts have no capitals. The Material bidirectionality page would not render for fetching.
- **Labels.** Kind: useful pattern. Evidence: C (platform guidance).
- **Implication.** Build with logical CSS properties (start/end) rather than physical ones (left/right), and review every icon for whether it shows direction.

### 7.3 Data display: position beats angle and area, and pie charts are not read by angle
- **Evidence.** Heer & Bostock (CHI 2010) replicated Cleveland & McGill's (1984) ranking of encodings with crowdsourced participants: position, then length, then angle and area. Skau & Kosara (EuroVis 2016) found that angle is the *least* important cue in pie charts and that donut charts are as accurate as pies. I have both only from summaries (see sources).
- **Labels.** Kind: strong heuristic. Evidence: A for the ranking (replicated), C for the pie result (one group).
- **Implication.** Use position or length (bars, dots) for precise comparison. Pie and donut charts are fine for rough part-to-whole views. Pair colour in charts with labels or patterns (4.4).

---

## 8. Accessibility

### 8.1 WCAG conformance is necessary but far from sufficient
- **Evidence.** Power, Freire, Petrie & Swallow (CHI 2012): 32 blind users, 16 websites, 1,383 problem instances. "Only 50.4% of the problems encountered by users were covered by Success Criteria in WCAG 2.0." Where WCAG did cover a problem, 16.7% of sites had implemented the recommended techniques and the techniques still did not solve it. The authors call for moving "towards a design principle approach".
- **Counterevidence and dating.** This study is WCAG 2.0 with blind users only. WCAG 2.1 and 2.2 added criteria (for example, target size and consistent help). I found no replication against 2.2.
- **Labels.** Kind: fundamental principle ("conformance is not the same as a usable experience for disabled people"). Evidence: B. It is one strong study, and W3C itself agrees: COGA states that its patterns cover barriers "that could not be included in the normative WCAG 2.x".
- **Implication.** Test with disabled users. Treat a WCAG 2.2 AA pass as the floor.

### 8.2 The measurable web is getting worse, and automated tests see only part of it
- **Evidence.** WebAIM Million 2026 (February 2026 crawl of the top million home pages): 95.9% had detected WCAG 2 A/AA failures, up from 94.8% in 2025, with 56.1 errors per page, up 10.1%. The most common failures were low-contrast text (83.9%), missing alt text (53.1%), missing input labels (51%), empty links (46.3%), empty buttons (30.6%) and missing document language (13.5%). Pages with ARIA averaged 59.1 errors against 42 without. WebAIM warns that this is a correlation and that complexity is a confounder. It also says "absence of detected errors does not indicate that a page is accessible."
- **Labels.** Kind: not a design rule. This is a measurement, evidence A for its scope: large-scale, repeated yearly, with a published method.
- **Implication.** Low contrast is the most common barrier on the web, and visual designers own it. Adding ARIA is not accessibility. Native HTML elements come first.

### 8.3 Overlays do not deliver conformance
- **Evidence.** FTC v. accessiBe: complaint announced 3 Jan 2025, final order 22 Apr 2025, $1 million. The FTC alleged the company "misrepresented the ability of its AI-powered web accessibility tool to make any website compliant with" WCAG. Practitioner sources report many lawsuits against sites that use overlays. I did not verify those counts.
- **Labels.** Kind: anti-pattern. Evidence: B (regulatory finding plus consistent expert opposition).

### 8.4 Semantic structure is the screen-reader user's navigation system
- **Evidence.** WebAIM Screen Reader Survey #10 (Dec 2023–Jan 2024, 1,539 valid responses, self-selected): 71.6% navigate long pages mainly by headings. Only 3.7% use landmarks as their primary method, although 31.7% use them frequently. The most problematic items were CAPTCHA, unexpected behaviour of interactive elements, ambiguous links and buttons, unexpected screen changes, and lack of keyboard access. 91.3% use a screen reader on mobile and 70.6% of those use iOS. Primary desktop screen readers: JAWS 40.5%, NVDA 37.7%, VoiceOver 9.7%, with JAWS dominant in North America.
- **Labels.** Kind: strong heuristic ("a real, ordered heading outline is the most valuable structure you can give"). Evidence: A–B (survey repeated over many years, but self-selected).
- **Implication for visual designers.** Visual hierarchy must be reproduced as a *heading hierarchy* in code, and the design hand-off should mark heading levels. A visual heading built from styled `div`s fails the most common way people navigate.

### 8.5 How errors reach assistive technology: GOV.UK's pattern against the inline-validation evidence
- **GOV.UK (as of 2026-09, Design System docs).**
  - On submit, show an error summary at the top with `role="alert"` and move keyboard focus to it.
  - Prefix the page `<title>` with "Error: " so screen readers announce it early.
  - Link each summary item to its field, and word it the same as the message next to the field.
  - Associate each field's message with `aria-describedby` and a visually hidden "Error:" prefix.
  - "Do not validate when the user moves away from a field." Wait for Continue, because early validation causes problems "especially for users who type more slowly", and "it's hard to tell the user about errors in a way that works reliably across different browsers and assistive technologies".
  - Research is cited only as "showed users understood what went wrong… tested in live services, including tax credits". There is no published method.
- **Opposing evidence.** Wroblewski with Etre (A List Apart, Sept 2009): 22 participants aged 21–49, six versions of one registration form. Inline validation on blur, compared with validation after submit, gave +22% success, −22% errors, +31% satisfaction and −42% completion time. Validating *while typing* or *before* input frustrated people. For easy fields (name, address), only 30–50% of participants even noticed the messages. Inline validation helped most for hard fields (username, password).
- **Assistive-technology evidence.** Adrian Roselli (April 2023, updated August 2023) tested six patterns across NVDA, JAWS, Narrator, VoiceOver (macOS and iPadOS) and TalkBack. `aria-describedby` without a live region was the most reliable. `aria-errormessage` was "generally not exposed when navigating through fields". Assertive announcements on blur can clip the next field's name. Only VoiceOver on iPadOS announced errors consistently in both situations.
- **Resolution (context-dependent).** The two sides studied different people. Wroblewski had a small, sighted, single-form sample in 2009. GOV.UK serves everyone, including slow typers and screen-reader users, and AT support for announcements on blur is still inconsistent as of 2023. For a public service with a broad population, validating on submit with a focused summary is the safer default. For a hard field such as a password, a *persistent* requirement hint shown before the user types gives the benefit of inline validation without announcements on blur.
- **Labels.** "Validate on submit with a focused, linked error summary": useful pattern, evidence C (strong institutional practice, unpublished research). "Inline validation improves completion": context-dependent heuristic, evidence C (one small study, old, sighted participants).

### 8.6 Touch target size: the evidence is older and smaller than the rules built on it
- **Primary study.** Parhi, Karlson & Bederson (MobileHCI 2006): 20 right-handed participants (17 male, aged 19–42, mean 25.7) from the University of Maryland computer science department, using an HP iPAQ with a 2005-era stylus touchscreen, one thumb, standing, with lift-off selection. Error rates stopped differing significantly at 9.6 mm or more for discrete taps and 7.7 mm or more for serial taps. The authors recommend 9.2 mm for discrete targets and 9.6 mm for serial ones. No participants had motor impairments.
- **Rules as of 2026-09.**
  - WCAG 2.2 SC 2.5.8 (AA): 24×24 CSS px, or enough spacing, with exceptions for inline links, user-agent controls and essential cases. Its Understanding document cites only Parhi et al. SC 2.5.5 (AAA) asks for 44×44.
  - Apple HIG: iOS default control size 44×44 pt and **minimum 28×28 pt**; visionOS 60 pt default.
  - Android: 48×48 dp, "larger is even better".
  - NN/g (Harley, 2019): at least 1×1 cm, citing Parhi, plus MIT Touch Lab fingertip widths of 1.6–2 cm.
- **My arithmetic (label D; the assumptions matter).** On a phone at 3× scale and about 460 ppi, 1 pt is about 0.17 mm. So 44 pt ≈ 7.3 mm, 28 pt ≈ 4.6 mm and 24 CSS px ≈ 4 mm. **Every platform default is below the 9.2 mm the cited study recommends.** WCAG's AA minimum is less than half of it. The 24 px figure is best read as a compromise that product teams will accept, not as an empirical threshold. The Understanding document does not show how 24 was derived.
- **Counterevidence.** Capacitive screens and modern touch-point correction are much better than 2005 resistive screens with lift-off selection. Spacing (the 2.5.8 exception) matters about as much as size. Fitts's law says the cost is mainly in speed, so small targets are acceptable where accuracy demands are low and undo is cheap.
- **Example.** NN/g's iOS 26 review says the App Store tab bar was squeezed to fit a floating search button. It reports "the long-standing guideline of at least 0.4cm between targets seems to have been tossed out".
- **Labels.** "Bigger targets reduce errors, with diminishing returns around 1 cm": strong heuristic, evidence B. "24 px is enough": design convention (legal floor), evidence D as an ergonomic threshold.
- **Implication.** Treat 44 pt / 48 dp as the normal size and 24 px as a legal floor. Give destructive or frequent actions about 1 cm with spacing.

### 8.7 Cognitive accessibility is under-specified by testable rules
- **Evidence.** W3C *Making Content Usable for People with Cognitive and Learning Disabilities* (COGA, Working Group Note, 29 Apr 2021) sets eight objectives: help users understand what things are; find what they need; clear content; avoid mistakes and correct them; focus; not rely on memory; help and support; adaptation and personalisation. WCAG 2.2 moved a little in this direction with 3.2.6 Consistent Help (A), 3.3.7 Redundant Entry (A) and 3.3.8 Accessible Authentication (AA), which bars memory or transcription puzzles without an alternative.
- **Labels.** Kind: strong heuristic set. Evidence: C–B (expert consensus; many individual items are backed by research I did not trace).
- **Implication.** Plain language, stable layouts, no memory tests and forgiving errors are what cognitive accessibility demands. A WCAG checker will not flag you for failing them.

### 8.8 Different needs conflict, so no single setting is accessible for everyone
- **Evidence.** W3C *Accessibility Requirements for People with Low Vision* (First Public Working Draft, 17 Mar 2016) says so directly: "one user's needs may conflict with another user's needs". Some people need high contrast. People with photophobia find a normal bright light background "not readable and painful". Most people with low acuity need large text, but people with good acuity and tunnel vision "might want to set the text size small". Needs can change within a single day with fatigue.
- **Labels.** Kind: fundamental principle ("accessibility means adaptability, not a single optimum"). Evidence: B.
- **Implication.** The durable answer is to honour user settings: text scaling to 200% (SC 1.4.4), reflow at 320 CSS px (1.4.10), text spacing overrides (1.4.12), OS contrast and motion preferences, and dark and light modes. That is better than choosing one "accessible" look. Apple's iOS 27 transparency slider (10.1) applies exactly this lesson.

### 8.9 Where accessibility helps everyone, and the limits of that claim
- **Evidence.** Ofcom's 2006 television access services review reported about 7.5 million UK subtitle users, of whom about 6 million had no hearing impairment. I saw this only quoted; the Ofcom page returned 403. Microsoft's Inclusive Design persona spectrum covers permanent, temporary and situational cases, for example one arm, an arm injury, or holding a baby.
- **Counterevidence.** Frank Spillers argues that equating situational limits with disability hides the size of the barriers: being distracted while driving is not blindness. I saw this only via a summary. And 8.8 shows that some accommodations help one group while harming another.
- **Labels.** "Accessible features are often used widely": strong heuristic, evidence B. "Accessibility always helps everyone": unsupported or weak claim.

---

## 9. Performance as users feel it

### 9.1 Where the 0.1 s / 1 s / 10 s thresholds come from
- **Evidence.** Nielsen (1993, updated 2014) states the limits: 0.1 s feels instantaneous, 1 s keeps the "flow of thought… uninterrupted", and 10 s is the limit for keeping attention. He cites Miller (1968) and Card, Robertson & Mackinlay (1991). Miller's AFIPS paper (I saw summaries, not the text) framed interaction as conversation. It proposed about 2 s as an "almost magical boundary" for feedback, 0.1–0.2 s as instantaneous, and noted that silences over 4 s become awkward in human conversation. web.dev supports the 100 ms end with perception research: Michotte (1962) found delays under about 100 ms still look causal, and Kaaresoja found quality perception drops above 100–150 ms. I saw both only as cited by web.dev.
- **Assessment.** The 0.1 s limit rests on perception science. The 1 s and 10 s limits are reasoned estimates from the conversation analogy and attention, not measured breakpoints.
- **Labels.** Kind: strong heuristic. Evidence: B for 0.1 s, C for 1 s and 10 s.

### 9.2 The "400 ms Doherty threshold" cannot be traced to the paper it is credited to
- **Evidence.** I read the reprint of Doherty & Thadani, *The Economic Value of Rapid Response Time* (IBM, November 1982), published with permission on Jim Elliott's IBM mainframe blog. The text shows productivity rising sharply as system response time falls below 1 s. Its data are field and lab observations, some with small samples: 75 sessions of 15 engineers, NIH with about 400 concurrent users, a card-wiring task, and a project at IBM Portsmouth. **The strings "400 ms", "0.4" and "addict" do not appear in the reprinted text.** The number may come from a figure, from Thadhani's earlier work, or from later retellings such as Laws of UX. I could not confirm which.
- **Labels.** "Sub-second response raises productivity in conversational computing": context-dependent heuristic, evidence C (1980s mainframe field data, vendor-authored). "400 ms is a threshold": unsupported or weak claim, evidence D.

### 9.3 Core Web Vitals thresholds are partly perceptual and partly chosen for achievability
- **Evidence.** web.dev, *Defining the Core Web Vitals metrics thresholds*.
  - LCP 2.5 s: candidates were narrowed to 1–3 s using Miller, Card and others. 2.5 s was chosen partly because 42% of phone origins already met it and it was "consistently achievable" for top sites at the 75th percentile, while 1.5–2 s were not.
  - INP 200 ms: 56% of phone origins met it. The *INP* article itself gives no scientific rationale for 200 ms and admits that labelling responsiveness "good" is "difficult".
  - CLS 0.1: "no prior research existed". It was set by internal testing that found 0.1 "noticeable but not excessively disruptive".
  - All three are assessed at the 75th percentile, so that 3 of 4 visits meet the target.
- **Labels.** Kind: design convention (industry benchmark). Evidence: C as a perceptual threshold. INP's 200 ms sits above the 100 ms perceptual limit it cites.
- **Implication.** Passing CWV is not the same as feeling instant. For direct manipulation (drag, typing, toggles), aim for 100 ms.

### 9.4 "53% of mobile visits are abandoned after 3 seconds" has no stated method for abandonment
- **Evidence.** DoubleClick by Google, *The Need for Mobile Speed* (September 2016). I read pages 1–8 as images. Footnote 5 reads in full: "Google Data, Aggregated, anonymized Google Analytics data from a sample of mWeb sites opted into sharing benchmark data, n=3.7K, Global, March 2016." Nothing in the report defines "abandoned", describes the analysis, or separates correlation from causation. The same report pairs this with ad-revenue projections from "our model". It was published by an ad business.
- **Labels.** Kind: unsupported or weak claim as stated. Evidence: D for the specific number. The general direction, that slower loads lose visitors, is plausible but needs better sources.
- **Implication.** Do not quote the 53% figure as fact. Cite controlled experiments or your own analytics instead.

### 9.5 Perceived speed can be shaped, but the effects are modest and depend on where attention is
- **Evidence.**
  - Harrison, Yeo & Hudson (CHI 2010) ran four studies with 20, 20, 10 and 16 participants, mostly students with mean ages of 19–23. Ribbing that moved backwards and decelerated made a 5 s bar feel equal to a plain bar about 12% longer (5.61 s), and a 15 s bar about 11.7% longer. The design was head-to-head, with attention on the bars and no other task.
  - Maister (1985, service operations) proposed that occupied waits feel shorter than unoccupied ones and that uncertain waits feel longer than known ones. These are propositions, not experiments.
  - Skeleton screens: Mejtoft, Långström & Söderström (ECCE 2018) report that skeletons were perceived as faster than spinners or blank screens. I could reach only the abstract-level claim, not the method or sample. NN/g (Tankala, 2023, reviewed 2 Sep 2026) builds its guidance on that single study: skeletons for full-page loads under about 10 s, spinners for single modules, progress bars beyond 10 s, and nothing under 1 s.
- **Counterevidence.** Real users multitask. A progress bar nobody watches cannot distort time. A skeleton that does not match the final layout adds layout shift, which is exactly what CLS penalises.
- **Labels.** "Show progress and structure during waits": strong heuristic, evidence B. "Skeletons beat spinners": context-dependent heuristic, evidence C. "Visual tricks cut perceived time by about 11%": context-dependent heuristic, evidence B (narrow lab conditions).

### 9.6 Optimistic UI makes an app feel fast only when the architecture can keep its promises
- **Evidence.** The most documented case is Linear's sync engine. A reverse-engineering write-up (wzhudev/reverse-linear-sync-engine) quotes Linear's CTO Tuomas Artman calling it "correct" and "probably the best documentation that exists". According to it, the app hydrates from IndexedDB into an in-memory object pool and applies changes to that pool immediately. It queues transactions to the server, updates local tables only after the server confirms, and rolls back on failure, resubmitting after reconnection. I found no user study of optimistic UI. The widely repeated "immediate feedback cuts perceived wait by up to 40%" appears in industry blogs with no traceable source.
- **Mechanism.** Most interactions then land under the 100 ms instant limit, because no network round-trip sits on the critical path. The cost is rollback: a change the user saw "succeed" can revert.
- **Labels.** Kind: useful pattern for low-risk, reversible actions (status, assignee). Evidence: C. For financial or irreversible actions it is an anti-pattern, because apparent success followed by reversal destroys trust.
- **Implication.** Much of Linear's reputation for "feeling premium" is an engineering property. It is not in the screenshots, which is why copying the look does not copy the feel.

---

## 10. Benchmark specimens

### 10.1 Apple iOS 26 → 27 "Liquid Glass" (full record)
- **Product and platform.** Apple's system-wide visual language for iOS and its sibling platforms. It shipped September 2025 (iOS 26) and was revised June 2026 (iOS 27, announced at WWDC 2026).
- **Context and users.** Every iPhone user, from beginners to experts, doing everything the phone does.
- **Strengths.** A strong, recognisable identity, spatial layering, and content running edge to edge. As of 2026-09, Apple.com shows the brand's product presentation: large headline type, a two-button call to action, full-bleed product imagery on black (`apple-home.png`).
- **Weaknesses (NN/g, Budiu, 10 Oct 2025, expert review only).**
  - Translucent controls over variable content lower legibility.
  - Tab bars were compressed and target spacing shrank.
  - Controls "appear, vanish, collapse, and expand depending on context", which undermines learning.
  - Decorative motion, such as pulsing, shimmering and animated tab switches.
  - Users also complained about contrast and notification legibility (MacRumors, 17 Sep 2025, seen via search).
- **Interaction.** Floating, context-dependent chrome.
- **Visual design.** Refraction, blur, specular highlights and translucency.
- **Accessibility.** Not assessed from a published audit. Reduce Transparency and Reduce Motion existed as settings. iOS 27 added a system slider from "More Clear" to "More Tinted" (MacRumors, 10 Jun 2026).
- **Performance.** Not assessed. User reports of animation lag exist but I found no measurement.
- **Cognitive experience.** Controls that come and go impose memory load and harm predictability (per NN/g).
- **Emotional experience.** Novelty and delight for some people, frustration for others. I found no systematic data.
- **Business context.** A hardware maker differentiates on perceived quality, and a unified language across Vision Pro, Mac and iPhone serves the ecosystem.
- **Principles demonstrated.** Distinct identity; spatial continuity.
- **Principles violated.** Sufficient contrast for text over images; stable locations for navigation; purposeful motion.
- **Tradeoffs.** Expression and depth were bought at the price of legibility and predictability.
- **What changed and why it matters.** In iOS 27, per MacRumors (10 Jun 2026), Apple:
  - "more effectively diffuses complex content";
  - added a darkened edge and brighter specular highlights;
  - shows a uniform toolbar when content scrolls under floating bars, "to maintain legibility and contrast";
  - made icons sharper;
  - added the clear-to-tinted slider.

  Apple framed this as addressing "feedback that followed last year's rollout". The mechanism is instructive. Apple kept the brand expression and added (a) *adaptive* backing behind text where the content underneath gets busy and (b) *user control* over the trade-off. That matches 8.8: when needs conflict, hand the control to the user.
- **Evidence.** Expert review, press reports of Apple's changes, and Apple's HIG. No user-testing data was public.
- **Lesson.** Brand expression can live in the *layer* (material, light, motion) as long as the *content plane* keeps guaranteed contrast. Where it cannot guarantee contrast, it has to become adaptive or optional.

### 10.2 Linear (full record, from site, docs and team writing; the app itself was not seen)
- **Context.** Issue tracking and product planning for software teams. Users are intermediate to expert, work in it daily, and rely heavily on the keyboard.
- **Primary tasks.** Triage, update and navigate issues and projects.
- **Visual design (site as of 2026-09, `linear-home.png`, `linear-home-mobile.png`).**
  - Near-black background, a large tightly tracked sans-serif headline, a one-line grey subhead, and a large product screenshot as the hero.
  - The secondary grey text inside the screenshot *looks* low in contrast. I could not measure it (see the method note at the top).
  - At 390 px wide, the hero screenshot's UI text shrinks to an illegible size. It works as a picture of the product, not as content.
- **Colour.** LCH themes defined by three variables with a contrast control (2024). In 2024 text and icons were made darker in light mode and lighter in dark mode. The brand blue was deliberately used less for a "timeless" feel.
- **Density.** The 2026 refresh dimmed the sidebar, made tabs compact, used fewer and smaller icons, and softened borders (2.2).
- **Performance.** The sync engine (9.6) is the plausible core of its "fast" reputation, and it is an architectural fact. There is no public latency measurement, so I leave measured performance not assessed.
- **Accessibility.** Not assessed (no public audit found). High-contrast themes exist per the 2024 blog.
- **Principles violated.** A dark, low-contrast marketing aesthetic cuts against WCAG-style contrast for secondary text. This is my visual impression only.
- **Tradeoffs.** Calm and density versus contrast of the chrome. Speed versus rollback complexity.
- **Business context.** A product-led brand selling to designers and engineers, where the look itself is marketing.
- **Lesson.** The "Linear look" imitated across SaaS (5.4) copies the surface. The durable causes are speed, keyboard-first interaction and hierarchy by weight, and none of them shows in a screenshot.

### 10.3 GOV.UK (full record)
- **Context.** Services and information from the UK government for the whole population, including people in distress and people with low literacy. Expertise is mixed and weighted towards beginners.
- **Primary tasks.** Complete a transaction (passport, tax, benefits) correctly on the first try.
- **Visual design (as of 2026-09, `govuk-passport-mobile.png`, `govuk-error-summary.png`).**
  - Blue header with the refreshed GOV.UK wordmark and a raised cyan dot. The web launch was 25 June 2025, and blue had dominated since November 2023, per a GOV.UK Design System team developer's blog.
  - Large, heavy headings, underlined blue links and a breadcrumb.
  - The cookie banner gives "Accept" and "Reject" identical styling.
  - Single column on mobile, with plain text such as "Use this service to apply for, renew, replace or update your passport".
- **Brand.** The refresh (about £500–532k, per PublicTechnology and the team blog) aimed to counter the view among younger audiences that the service seemed "monolithic, unfriendly, and even intimidating". The team member says openly that the cyan is "too oversaturated", and says the blue signals trust, not politics.
- **Accessibility.** The Design System website is "fully compliant with WCAG 2.2 AA" (Digital Accessibility Centre audit, July 2024; codebase examples July 2024). Known AT issues: `<details>` with Dragon and older VoiceOver, and file upload with Dragon (a custom component sits behind a flag). The team states plainly that "using the GOV.UK Design System in a service does not immediately make that service accessible."
- **Interaction.** The error pattern in 8.5, and no validation on blur.
- **Performance.** Not assessed.
- **Principles demonstrated.** Plain language, strong signifiers, errors that reach AT, and honesty about limits.
- **Principles violated.** Few of the premium or brand-expressive conventions. That is by design.
- **Tradeoffs.** Distinctiveness and emotional warmth are traded for clarity and trust. The 2025 refresh tests how much expression can be added back without harm.
- **Lesson.** "Visually ordinary but exceptionally effective". Its quality is in guaranteed behaviour (focus, announcements, wording), which a screenshot barely shows.

### 10.4 Stripe (short entry)
- **What it demonstrates.** An accessible colour system as a *brand-preserving* engineering move (4.3).
- **Site as of 2026-09 (`stripe-home.png`).**
  - A two-tone headline: the first sentence in dark navy, the rest in grey, part of it in gradient purple where it overlaps a gradient ribbon. The emphasis comes from colour inside one sentence.
  - A live-ticking "Global GDP running on Stripe" figure.
  - Cookie buttons of equal weight.
- **Where it may fail.** Grey and gradient text over a ribbon cannot be checked by a single contrast ratio (section 4.2). This is my visual impression; I did not measure it.
- **Evidence.** Team blog (2019) and screenshot.

### 10.5 Vercel (short entry)
- **What it demonstrates.** Radical reduction as brand. As of 2026-09 (`vercel-home.png`) the page is off-white, with a large black triangle, a Geist Sans headline and three short lines. The Geist colour scale maps steps to roles (4.3), and P3 colour is used where supported.
- **Where it may fail.** The page tells a newcomer little about what the product does ("Agentic Infrastructure"). Minimal here means low information, not simplicity. That is a content judgment (see "Outside my area").
- **Evidence.** Geist docs and screenshot.

### 10.6 BBC (short entry)
- **Not assessed.** The GEL guidance was unavailable on 2026-09-25 (`bbc-gel-screenreaders.png` shows "Page temporarily unavailable").
- **Incidental observation (as of 2026-09).** The BBC cookie banner on that page set "Yes, I agree" against "No, take me to settings". There was no one-step reject, unlike GOV.UK's equal Accept and Reject. This is an observation of one page; I read nothing further into it.

---

## 11. Premium, elegant, coherent, expressive or empty

- **Heuristic (C).** Across the specimens, "premium" correlates with a set of properties that are *cheap to see and expensive to fake*:
  1. consistent spacing and a type scale with optical sizing (3.4);
  2. a restrained palette with perceptual steps (4.3);
  3. motion that tracks input (6.1);
  4. and, the part missing from screenshots, responsiveness under 100 ms (9.6).

  Kind: context-dependent heuristic. Evidence: D. This is my synthesis; I found no study that manipulates "premium" perception.
- **Elegant versus empty (my inference, D).** Minimalism feels elegant when what was removed was *redundant*, so the remaining cues still carry the task. It feels empty when what was removed was *information* or *signifiers*. The evidence is indirect but real: flat signifiers cost more on dense, novel pages (2.1), and M3E's own caveat is that removing familiar list structure hurt usability (5.3). Vercel's home page (10.5) is a candidate for "empty" to a newcomer and "elegant" to someone who already knows the product.
- **What brand expression can do without hurting use.** Brand expression can live in colour at the edges, display type, imagery, and a material or motion layer that honours user settings. What it cannot do safely: put text on uncontrolled backgrounds, move navigation around, drop contrast below the floor, or add motion to routine actions (Liquid Glass, 10.1; Stripe's gradient text, 10.4). Kind: strong heuristic. Evidence: C.

---

## 12. Design tensions (summary)

| Tension | Side A optimises | Side B optimises | Deciding variables | Evidence |
|---|---|---|---|---|
| Brand expression vs legibility | Distinctiveness, first impression (1.2) | Contrast, stability (4, 10.1) | Is text on a controlled plane? Can users adjust it? | B/C |
| Calm chrome vs contrast | Focus on content (2.2) | Visibility for low vision (8.8) | Frequency of navigation; user settings | C |
| Inline vs on-submit validation | Speed for sighted users on hard fields (8.5) | AT reliability, slow typers | Population breadth, field difficulty | C |
| Optimistic UI vs truthfulness | Perceived speed (9.6) | Trust when actions fail | Reversibility, stakes | C |
| Large type vs overview | Reading comfort (3.1) | Density, tunnel-vision users (8.8) | Task (reading vs scanning) | B |
| Rich motion vs attention and motion sensitivity | Spatial clarity, delight | Calm, vestibular safety (6) | Is it essential? Is Reduce Motion honoured? | C |

---

## 13. Open questions and uncertainty

1. **Contrast.** There is still no published validation of any contrast model against reading performance across polarities, and WCAG 3's algorithm is "yet to be determined" (April 2026). This is the biggest evidence gap in my area.
2. **Touch targets.** There is no modern replication of Parhi et al. on capacitive phones, with motor-impaired or older users, or across sizes from 24 to 48 px. The legal floor (24 px) has no visible empirical derivation.
3. **Skeleton screens and optimistic UI.** Evidence is one study, which I reached only at abstract level, plus none for optimistic UI. The popular percentages ("up to 40%") are untraceable.
4. **"Premium" perception.** I found no study that manipulates it. Everything in section 11 is synthesis.
5. **Design-system value.** Only vendor studies exist (Figma, Google), and the M3E studies are unpublished.
6. **WCAG coverage.** Power et al. (2012) is WCAG 2.0 and blind users only. There is no 2.2 equivalent, and no equivalent for low-vision, motor or cognitive users.
7. **Motion prevalence.** There is no measured prevalence of sensitivity to UI motion. The common 35% figure measures something else (a balance test).
8. **Product measurements I could not make.** I have no computed contrast on Linear, Stripe or Vercel, because the script was blocked. The final writer should not turn my visual impressions into claims of non-conformance.

## Outside my area

- **Vercel's home page (as of 2026-09)** communicates little about the product to a newcomer. That is a content and information-architecture question, not visual.
- **Cookie banners.** GOV.UK and Stripe give Accept and Reject equal weight, while the BBC GEL page offered "Yes, I agree" against "No, take me to settings". This is relevant to dark patterns.
- **Linear's comment sending.** The 2026 refresh lets users choose Enter or ⌘/Ctrl+Enter to send comments. This is relevant to expert workflows and to preventing errors.
