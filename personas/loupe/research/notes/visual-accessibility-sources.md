# Sources: visual design, accessibility and performance

All sources were accessed on 2026-09-25 unless noted otherwise. "Read" means I read the source itself, as a page, a PDF rendered as images, or a structured docs endpoint. **[Quoted only]** means I saw the source only as it was summarised or cited elsewhere.

## Aesthetics and first impressions

1. **Tuch, Roth, Hornbæk, Opwis, Bargas-Avila, "Is beautiful really usable?"**, *Computers in Human Behavior* 28(5), 2012. Read (abstract and introduction, as images). URL: https://cpb-us-e1.wpmucdn.com/wp.wwu.edu/dist/8/2868/files/2018/04/Tuch-et-al-2012-Is-Beautiful-Usable-2don1em.pdf
   - Claim: aesthetics did not affect perceived usability; usability affected post-use aesthetics.
   - Evidence: lab study, N=80, 2×2 manipulation of one online shop.
   - Limitations: a single product type and a lab setting.
2. **Hassenzahl & Monk, "The Inference of Perceived Usability From Beauty"**, *HCI* 25(3), 2010. Read (abstract). URL: https://pure.york.ac.uk/portal/en/publications/the-inference-of-perceived-usability-from-beauty/
   - Claim: 25 correlations drawn from 15 papers vary widely; the beauty–usability link is mediated by "goodness".
   - Limitations: I read the abstract only.
3. **Tuch, Presslaber, Stöcklin, Opwis, Bargas-Avila, "The role of visual complexity and prototypicality regarding first impression of websites"**, *IJHCS* 70(11), 2012. **[Quoted only]**, via a search-result summary. URL: https://research.google.com/pubs/archive/38315.pdf
   - Claim: complexity and prototypicality affect judgments at 17–50 ms.
   - Evidence: 119 screenshots, two studies.
4. **Reinecke et al., "Predicting users' first impressions of website aesthetics…"**, CHI 2013. **[Quoted only]**, via a search summary. URL: https://dl.acm.org/doi/10.1145/2470654.2481281
   - Claim: 450 sites and 548 volunteers; models explain about half the variance, with demographic differences.
5. **Kurosu & Kashimura 1995; Tractinsky et al. 2000; Sonderegger & Sauer 2010.** **[Quoted only]**, as cited in Tuch et al. 2012.

## Hierarchy and signifiers

6. **Kate Moran, "Flat UI Elements Attract Less Attention and Cause Uncertainty"**, NN/g, 3 Sep 2017. Read. URL: https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/
   - Claim: weak signifiers led to 22% more time and 25% more fixations.
   - Evidence: 71 participants, 9 page pairs, eyetracking.
   - Limitations: single-page findability tasks.
7. **Burmistrov, Zlokazova, Izmalkova, Leonova, "Flat Design vs Traditional Design"**, INTERACT 2015. **[Quoted only]**, via a search summary. URL: https://interux.com/publications/Burmistrov-INTERACT15.pdf
8. **Aufmann & Heckel, "A calmer interface for a product in motion"**, Linear, 12 Mar 2026. Read. URL: https://linear.app/now/behind-the-latest-design-refresh
   - Claim: Linear dimmed the sidebar, reduced icons and softened borders.
   - Evidence: team case study.
   - Limitations: no outcome data.

## Typography and polarity

9. **Rello, Pielot, Marcos, "Make It Big!"**, CHI 2016. Read via the author's blog, 2016. URL: https://pielot.org/2016/01/optimal-font-size-for-web-pages/
   - Claim: readability and comprehension improve up to 18 pt.
   - Evidence: 104 participants, eyetracking.
   - Limitations: Wikipedia reading only; device not stated in the summary.
10. **Mary C. Dyson, "How physical text layout affects reading from screen"**, *Behaviour & IT* 23(6), 2004. Read (pp. 377–382, as images). URL: https://stu.westga.edu/~ssynan1/literacy/Dyson.pdf
    - Claim: line-length results are mixed; 100 cpl was read fastest in Dyson & Kipping 1998, and Bernard 2002 found no difference.
    - Limitations: I read the first six pages only, and the review covers studies before 2004. Dyson & Haselgrove 2001 is known to me via this review and via search summaries.
11. **Piepenbrock, Mayr, Buchner, "Positive display polarity is advantageous for both younger and older adults"**, *Ergonomics* 56(7), 2013. **[Quoted only]**, via the PubMed and search abstract. URL: https://pubmed.ncbi.nlm.nih.gov/23654206/
12. **Raluca Budiu, "Dark Mode vs. Light Mode"**, NN/g, 2 Feb 2020. Read. URL: https://www.nngroup.com/articles/dark-mode/
    - Claim: it summarises Piepenbrock and Legge 1985 (cloudy ocular media favour dark mode). Legge is **[Quoted only]**.
13. **Apple HIG, Typography and Accessibility**, current as of 2026-09. Read via the JSON docs endpoints. URLs: https://developer.apple.com/tutorials/data/design/human-interface-guidelines/typography.json and …/accessibility.json
    - Claims: 17 pt default and 11 pt minimum text on iOS; avoid light weights; dynamic optical sizes; iOS controls 44 pt default and 28 pt minimum; Reduce Motion guidance.
    - Context: vendor guidance.

## Colour and contrast

14. **W3C, Understanding SC 1.4.3 Contrast (Minimum)**, WCAG 2.2. Read. URL: https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
    - Claim: the rationale for the thresholds (ISO 9241-3, ANSI/HFES 100-1988, 20/40 vision).
15. **W3C Low Vision TF, GitHub discussion #131, "WCAG 2 and APCA Comparison"**, Somers and sdw32, Oct 2021 – Jan 2022. Read. URL: https://github.com/w3c/low-vision-a11y-tf/discussions/131
    - Claim: WCAG 2 "false passes" on random colour pairs.
    - Limitations: "false" is judged against APCA itself; the full APCA experimental data were unpublished at the time.
16. **Adrian Roselli, "WCAG3 Contrast as of April 2026"**, 10 Apr 2026 (updated 13 Apr). Read. URL: http://adrianroselli.com/2026/04/wcag3-contrast-as-of-april-2026.html
    - Claim: APCA was removed from WCAG 3 drafts in 2023, and the algorithm is still TBD in the 8 Apr 2026 Editor's Draft.
    - Limitations: practitioner opinion; the status facts are checkable against W3C drafts, which I did not open directly.
17. **Koopersmith & Miner, "Designing accessible color systems"**, Stripe, 15 Oct 2019. Read. URL: https://stripe.com/blog/accessible-color-systems
    - Claim: the palette was rebuilt in CIELAB with a rule of 5 steps for small text and 4 steps for large text and icons.
18. **Linear, "How we redesigned the Linear UI (part II)"**, 28 Mar 2024. Read. URL: https://linear.app/now/how-we-redesigned-the-linear-ui
    - Claim: HSL was replaced by LCH, 98 theme variables became 3, a contrast variable was added, and Inter Display is used for headings.
19. **Vercel, Geist Introduction and Colors**, current as of 2026-09. Read. URLs: https://vercel.com/geist/introduction and https://vercel.com/geist/colors
    - Claim: a 10-step scale mapped to roles, with P3 support.
20. **Jennifer Birch, "Worldwide prevalence of red-green color deficiency"**, *JOSA A* 29(3), 2012. **[Quoted only]**, abstract via search. URL: https://opg.optica.org/josaa/abstract.cfm?uri=josaa-29-3-313

## Design systems and tokens

21. **Design Tokens Community Group, "Design Tokens specification reaches first stable version"**, Kaelig Deloumeau-Prigent, 28 Oct 2025. Read. URL: https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/
    - Claim: Format Module 2025.10 is stable. It is a Community Group specification, not a W3C Recommendation.
22. **Nathan Curtis, EightShapes token articles.** **[Quoted only]**. The Medium article returned 403 and eightshapes.com did not resolve. URL: https://medium.com/eightshapes-llc/reimagining-a-token-taxonomy-462d35b2b033
23. **Clancy Slack, "Measuring the value of design systems"**, Figma, 19 Dec 2019. Read. URL: https://www.figma.com/blog/measuring-the-value-of-design-systems/
    - Claim: 34% faster with a design system.
    - Limitations: vendor study, no N given, the system was directly applicable, and completion was self-judged.
24. **Google Design, "Expressive Design: Google's UX Research"** (Material 3 Expressive), undated as viewed; M3E launched May 2025. Read. URL: https://design.google/library/expressive-material-design-google-research
    - Claim: 46 studies, more than 18,000 participants, "up to 4×" faster spotting.
    - Limitations: unpublished; the baseline is Google's own M3; the figure is a best case.
25. **Frontend Horse, "The Linear Look"**, before 2024, no author named. Read. URL: https://frontend.horse/articles/the-linear-look/
    - Claim: catalogues the imitated aesthetic; descriptive, not critical.
26. **Overpass Studio and LogRocket on SaaS sameness.** **[Quoted only]**, via a search summary. URLs: https://www.overpass.studio/blog/why-saas-websites-look-the-same and https://blog.logrocket.com/ux-design/linear-design/

## Motion

27. **W3C, Understanding SC 2.3.3 Animation from Interactions**, WCAG 2.2. Read. URL: https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
    - Claim: the criterion is AAA and cites no clinical research.
28. **Agrawal et al., "Disorders of balance and vestibular function in US adults"**, NHANES 2001–04, 2009. **[Quoted only]**, via the PubMed listing and a search summary. URL: https://pubmed.ncbi.nlm.nih.gov/19468085/
    - Claim: 35.4% of adults aged 40 and over failed a foam-balance test. This is not a measure of UI motion sensitivity.
29. **MacRumors, "iOS 7 Users Complaining About Motion Sickness…"**, 26 Sep 2013; also Scientific American. **[Quoted only]**, via a search summary. URL: https://www.macrumors.com/2013/09/26/ios-7-users-complaining-about-motion-sickness-due-to-parallax-and-zooming-effects/

## Internationalisation

30. **W3C Internationalization, "Text size in translation"**, undated as viewed. Read. URL: https://www.w3.org/International/articles/article-text-size
    - Claim: IBM's expansion table and the extra vertical space non-Latin scripts need.
    - Limitations: the IBM source is undated and its table is non-monotonic.
31. **Apple HIG, Right to left**, current as of 2026-09. Read via JSON. URL: https://developer.apple.com/tutorials/data/design/human-interface-guidelines/right-to-left.json
32. **Material bidirectionality page.** Not readable; the page is rendered by JavaScript. URL: https://m2.material.io/design/usability/bidirectionality.html

## Data display

33. **Heer & Bostock, "Crowdsourcing graphical perception"**, CHI 2010; and **Cleveland & McGill 1984**. **[Quoted only]**, via search summaries. URL: https://dl.acm.org/doi/10.1145/1753326.1753357
    - Claim: the crowdsourced replication confirmed the ranking of position above length above angle and area.
34. **Skau & Kosara, "Arcs, Angles, or Areas"**, EuroVis 2016. **[Quoted only]**, via a search summary. URL: https://kosara.net/publications/Skau-EuroVis-2016
    - Claim: angle is the least important cue in pie charts, and donuts are as accurate as pies.
    - Used in notes §7.3.

## Accessibility

35. **Power, Freire, Petrie, Swallow, "Guidelines are only half of the story"**, CHI 2012. Read (abstract via the York research portal). URL: https://pure.york.ac.uk/portal/en/publications/guidelines-are-only-half-of-the-story-accessibility-problems-enco/
    - Claim: only 50.4% of problems were covered by WCAG 2.0.
    - Evidence: 32 blind users, 16 sites, 1,383 problems.
36. **WebAIM, The WebAIM Million 2026**, February 2026. Read. URL: https://webaim.org/projects/million/
    - Evidence: automated crawl of the top million home pages.
    - Limitations: automated detection only; ARIA correlation is confounded by complexity.
37. **WebAIM, Screen Reader User Survey #10**, published Feb 2024. Read. URL: https://webaim.org/projects/screenreadersurvey10/
    - Evidence: 1,539 responses. Limitations: self-selected sample.
38. **FTC, accessiBe Inc. case page**, complaint 3 Jan 2025, order 22 Apr 2025. Read. URL: https://www.ftc.gov/legal-library/browse/cases-proceedings/2223156-accessibe-inc
39. **W3C, Making Content Usable for People with Cognitive and Learning Disabilities**, WG Note, 29 Apr 2021. Read. URL: https://www.w3.org/TR/coga-usable/
40. **W3C, Accessibility Requirements for People with Low Vision**, FPWD, 17 Mar 2016. Read. URL: https://www.w3.org/TR/low-vision-needs/
    - Claim: needs conflict (contrast versus photophobia, large versus small text).
    - Limitations: this is a draft.
41. **W3C, What's New in WCAG 2.2**, 5 Oct 2023. Read. URL: https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
42. **W3C, Understanding SC 2.5.8 Target Size (Minimum)**, WCAG 2.2. Read. URL: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
43. **Parhi, Karlson, Bederson, "Target Size Study for One-Handed Thumb Use on Small Touchscreen Devices"**, MobileHCI 2006. Read (pp. 203–206, as images). URL: https://www.microsoft.com/en-us/research/wp-content/uploads/2006/01/parhi-mobileHCI06.pdf
    - Claim: 9.2 mm for discrete targets and 9.6 mm for serial ones.
    - Evidence: N=20 right-handed, mostly male computer science participants on an HP iPAQ.
    - Limitations: 2005 hardware and no motor-impaired users.
44. **Aurora Harley, "Touch Targets on Touchscreens"**, NN/g, 5 May 2019. Read. URL: https://www.nngroup.com/articles/touch-target-size/
    - Claim: at least 1×1 cm. The MIT Touch Lab fingertip data it cites are **[Quoted only]**.
45. **Android Developers, "Make apps more accessible" (touch targets)**, current as of 2026-09. Read. URL: https://developer.android.com/guide/topics/ui/accessibility/apps
46. **GOV.UK Design System: Error summary, Error message and Validation pattern**, current as of 2026-09. Read. URLs: https://design-system.service.gov.uk/components/error-summary/, …/components/error-message/ and …/patterns/validation/
    - Claims: move focus to the summary, prefix the title with "Error:", do not validate on blur.
    - Limitations: research is described but not published.
47. **GOV.UK Design System accessibility statement**, current as of 2026-09. Read. URL: https://design-system.service.gov.uk/accessibility-statement/
    - Claim: WCAG 2.2 AA, audited by the Digital Accessibility Centre in July 2024; known Dragon and VoiceOver issues.
48. **Luke Wroblewski, "Inline Validation in Web Forms"**, A List Apart, 1 Sep 2009. Read. URL: https://alistapart.com/article/inline-validation-in-web-forms/
    - Evidence: 22 participants, 6 form variants, with Etre.
    - Limitations: small, old, sighted participants, one form.
49. **Adrian Roselli, "Exposing Field Errors"**, 3 Apr 2023 (updated 15 Aug 2023). Read. URL: http://adrianroselli.com/2023/04/exposing-field-errors.html
    - Evidence: a practitioner's own tests across 5 browser and AT pairs.
50. **Microsoft Inclusive Design persona spectrum.** **[Quoted only]**, via summaries. URL: https://inclusive.microsoft.design/
51. **Frank Spillers, "The problem with Inclusive Design and Temporary Disabilities".** **[Quoted only]**, via a search summary. URL: https://frankspillers.com/the-problem-with-inclusive-design-and-temporary-disabilities/
52. **Ofcom, Television Access Services Review**, 2006. **[Quoted only]**; the page returned 403. URL: https://www.ofcom.org.uk/tv-radio-and-on-demand/accessibility/access-services-review
    - Claim: about 7.5 million UK subtitle users, of whom about 6 million had no hearing impairment.
53. **BBC GEL, "How to design for screen readers."** Unavailable: fetch was blocked and the screenshot shows "Page temporarily unavailable" on 2026-09-25. URL: https://www.bbc.co.uk/gel/how-to-design-for-screen-readers

## Performance

54. **Jakob Nielsen, "Response Times: The 3 Important Limits"**, NN/g, 1993 (updated 2014). Read. URL: https://www.nngroup.com/articles/response-times-3-important-limits/
55. **Robert B. Miller, "Response time in man-computer conversational transactions"**, AFIPS FJCC 1968. **[Quoted only]**, via search summaries. URL: https://dl.acm.org/doi/10.1145/1476589.1476628
56. **Card, Robertson, Mackinlay 1991; Michotte 1962; Kaaresoja.** **[Quoted only]**, as cited by Nielsen and web.dev.
57. **Doherty & Thadani, "The Economic Value of Rapid Response Time"**, IBM, Nov 1982, reprinted with permission on Jim Elliott's blog. Read. URL: https://jlelliotton.blogspot.com/p/the-economic-value-of-rapid-response.html
    - Claim: productivity rises sharply below 1 s.
    - Limitations: vendor-authored, and figures were not visible in the reprint. "400 ms" does not appear in the text.
58. **web.dev, "Defining the Core Web Vitals metrics thresholds"**, Google, current as of 2026-09. Read. URL: https://web.dev/articles/defining-core-web-vitals-thresholds
    - Claim: thresholds were chosen from perception research plus achievability; CLS came from internal testing.
59. **web.dev, "Interaction to Next Paint (INP)"**, current as of 2026-09. Read. URL: https://web.dev/articles/inp
60. **DoubleClick by Google, "The Need for Mobile Speed"**, Sep 2016. Read (pp. 1–8, as images). URL: https://www.thinkwithgoogle.com/_qs/documents/2340/bc22e_The_Need_for_Mobile_Speed_-_FINAL_1.pdf
    - Claim: 53% of visits are abandoned after 3 s.
    - Evidence: footnote only ("Google Analytics… n=3.7K… March 2016").
    - Limitations: no definition of abandonment and no method; ad-business sponsor.
61. **Harrison, Yeo, Hudson, "Faster Progress Bars"**, CHI 2010. Read (full paper, as images). URL: https://www.chrisharrison.net/projects/progressbars2/ProgressBarsHarrison.pdf
    - Claim: backwards-decelerating ribbing made bars feel about 11–12% faster.
    - Evidence: 4 small studies (N=10–20).
    - Limitations: attention was on the bar; 5 s and 15 s only.
62. **David Maister, "The Psychology of Waiting Lines"**, 1985. **[Quoted only]**, via summaries.
63. **Samhita Tankala, "Skeleton Screens 101"**, NN/g, 4 Jun 2023 (reviewed 2 Sep 2026). Read. URL: https://www.nngroup.com/articles/skeleton-screens/
64. **Mejtoft, Långström, Söderström, "The effect of skeleton screens"**, ECCE 2018. **[Quoted only]**. I reached only an abstract-level summary; the author page had just the citation. URL: https://dl.acm.org/doi/10.1145/3232078.3232086
65. **Katie Sherwin, "Progress Indicators Make a Slow System Less Insufferable"**, NN/g, 26 Oct 2014. Read. URL: https://www.nngroup.com/articles/progress-indicators/
    - Claim: "willing to wait 3 times longer". The source of that figure is not traced in the article, so I did not use it.
66. **wzhudev, "reverse-linear-sync-engine"** (GitHub), undated, endorsed in the README by Linear's CTO. Read. URL: https://github.com/wzhudev/reverse-linear-sync-engine
    - Claim: IndexedDB bootstrap, in-memory pool, optimistic transactions, rollback.
    - Limitations: reverse-engineered, not official documentation.
67. **"Optimistic UI cuts perceived wait by up to 40%."** Industry blogs (for example OpenReplay). **[Quoted only]**. Untraceable, so I did not use it as evidence.

## Products and criticism

68. **Raluca Budiu, "Liquid Glass Is Cracked, and Usability Suffers in iOS 26"**, NN/g, 10 Oct 2025. Read. URL: https://www.nngroup.com/articles/liquid-glass/
    - Evidence: expert review, no user testing.
69. **MacRumors, "Here's How Liquid Glass Is Changing in iOS 27"**, 10 Jun 2026. Read. URL: https://www.macrumors.com/2026/06/10/how-liquid-glass-is-changing-in-ios-27/
    - Claim: diffusion, darkened edges, a uniform toolbar on scroll, and a clear-to-tinted slider. Apple is quoted on addressing feedback.
    - Limitations: secondary reporting of Apple's statements.
70. **MacRumors, "iOS 26's Liquid Glass Design Draws Criticism From Users"**, 17 Sep 2025. **[Quoted only]**, via a search summary.
71. **beeps (GOV.UK Design System developer), "The (not quite new) GOV.UK brand"**, 25 Jun 2025. Read. URL: https://beeps.website/blog/2025-06-25-the-not-quite-new-govuk-brand/
    - Claim: the reasons for the refresh; the cyan is "too oversaturated"; blue has dominated since Nov 2023.
72. **PublicTechnology, "GDS unveils colourful £500k refresh of GOV.UK"**, 30 Jun 2025. **[Quoted only]**, via a search summary (cost of about £532k).
73. **Linear changelog and LinkedIn announcement of the 2026 UI refresh.** **[Quoted only]**, via a search summary (user feedback on light-mode contrast).
74. **Own screenshots, 2026-09-25, via tools/shot.mjs:**
    - `out/shots/linear-home.png`, `linear-home-mobile.png`
    - `stripe-home.png`
    - `vercel-home.png`
    - `apple-home.png` (served in a Norwegian regional variant)
    - `govuk-passport-mobile.png`, `govuk-error-summary.png`
    - `bbc-gel-screenreaders.png`

    Limitations: marketing pages only, not the apps; no measured contrast (my contrast script was blocked by the sandbox).
