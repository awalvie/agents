# Sources

All accessed 2026-09-25. Tier numbers follow BRIEF.md.

Status markers:

- **READ**: I read the page itself.
- **READ (screenshot)**: the page blocks the fetch tool, so I read a screenshot taken with `tools/shot.mjs`. Only part of the page may have been visible.
- **QUOTED ONLY**: I did not read the original. I saw it only quoted or summarised elsewhere (usually by a search-engine summary). Do not rely on these without checking them.

Each entry lists the source, then **Claim**, **Evidence**, **Context** and **Limits**.

---

## Netflix

1. **Artwork Personalization at Netflix.** Chandrashekar, Amat, Basilico, Jebara. Netflix TechBlog, 2017-12-07. https://netflixtechblog.com/artwork-personalization-c589f074ad76. READ (screenshot, first ~40% of the post).
   - **Claim:** artwork is personalised per member, using contextual bandits, to act as visual "evidence" for a title.
   - **Evidence:** first-party description; example images each get >5% of impressions.
   - **Context:** Tier 2, the team responsible.
   - **Limits:** I did not see the evaluation section.
2. **The Power of a Picture.** Nick Nelson (Head of Product Creative). About Netflix, 2016-05-03. https://about.netflix.com/en/news/the-power-of-a-picture. READ.
   - **Claim:** artwork was "over 82% of their focus while browsing"; members spend 1.8 s per title; images with >3 people win less often.
   - **Evidence:** "consumer research studies" in early 2014, with no method or sample given.
   - **Context:** Tier 2.
   - **Limits:** untraceable numbers, graded D.
3. **The Netflix Recommender System: Algorithms, Business Value, and Innovation.** Gomez-Uribe & Hunt. ACM TMIS, 2015. https://dl.acm.org/doi/10.1145/2843948. QUOTED ONLY (ACM returned 403).
   - **Claim:** recommendations influence ~80% of hours streamed; personalization saves >$1B/yr.
   - **Evidence:** internal data.
   - **Context:** Tier 1/2, written by Netflix staff.
   - **Limits:** not read; the $1B figure is an internal estimate.
4. **Netflix's horrible autoplay previews can be turned off.** Brian Heater. TechCrunch, 2020-02-06. https://techcrunch.com/2020/02/06/netflixs-horrible-autoplay-previews-can-be-turned-off/. READ.
   - **Claim:** Netflix made autoplay previews optional after feedback ("heard the feedback loud and clear").
   - **Evidence:** Netflix statement.
   - **Context:** Tier 2 press.
   - **Limits:** gives no Netflix rationale for having the previews.
5. **Netflix Help Center, "How to turn preview autoplay on or off".** https://help.netflix.com/en/node/2102. QUOTED ONLY (seen as a search result).
   - **Claim:** a setting exists.
   - **Limits:** not opened.
6. **Unveiling Our Innovative New TV Experience.** Eunice Kim (CPO) & Elizabeth Stone (CTO). About Netflix, 2025-05-07. http://about.netflix.com/en/news/unveiling-our-innovative-new-tv-experience. READ.
   - **Claim:** the redesigned TV homepage is "more flexible for our broad entertainment offerings, more intuitive"; Search and My List move to the top; callouts added.
   - **Evidence:** announcement only.
   - **Context:** Tier 2 first-party.
   - **Limits:** no test data.
7. **The new Netflix redesign is drawing early criticism online.** Matt Horne. Android Authority, 2025-05-07. https://www.androidauthority.com/netflix-new-tv-experience-redesign-3555283/. READ.
   - **Claim:** Reddit and YouTube responses are largely critical, and genre browsing moved to Search.
   - **Evidence:** summary of user reactions.
   - **Context:** Tier 2/4.
   - **Limits:** anecdotal. The claim that about 7 titles per row dropped came from a search summary of other outlets and was not verified.
8. **Eunice Kim "eye gymnastics" quote.** QUOTED ONLY (search summary of Tubefilter/Variety coverage, 2025-05).
   - **Claim:** the old UI required "eye gymnastics" when scrolling down and right.
   - **Limits:** not read in the original outlet.
9. **Netflix users suggest the service is targeting black viewers with inaccurate movie posters.** David Renshaw. The FADER, 2018-10-22. https://www.thefader.com/2018/10/22/netflix-target-users-race. READ.
   - **Claim:** users saw artwork featuring minor Black actors; Netflix says only viewing history is used.
   - **Evidence:** user reports plus Netflix statement.
   - **Context:** Tier 2/4.
   - **Limits:** a few users; prevalence unknown.

## Pinterest

10. **Driving user growth with performance improvements.** Sam Meder, Vadim Antonov, Jeff Chang. Pinterest Engineering (Medium), 2017-03-03. https://medium.com/pinterest-engineering/driving-user-growth-with-performance-improvements-cfc50dafadd7. READ (screenshot, first ~half).
    - **Claim:** an early-2015 mobile web experiment gave 60% faster landing pages and 40% higher mobile signup conversion. It introduced the "user perceived wait time" metric.
    - **Evidence:** first-party experiments.
    - **Context:** Tier 2.
    - **Limits:** the headline 40% wait-time / +15% SEO / +15% signup results are QUOTED ONLY (search summary of the same post; that section was not visible in my screenshot).
11. **How Pinterest utterly ruined photo search on the internet.** Chris Stokel-Walker. Inverse, 2021-11-05. https://www.inverse.com/input/culture/pinterest-sucks-google-image-photo-search-ruining-internet. READ.
    - **Claim:** a login wall blocks image-search visitors; the "Unpinterested!" extension has 28,000+ installs; Pinterest blames Google's ranking.
    - **Evidence:** user quotes, extension count, spokesperson.
    - **Context:** Tier 2/4.
    - **Limits:** journalistic; no traffic data.
12. **Gestalt accessibility page.** https://gestalt.pinterest.systems/foundations/accessibility. QUOTED ONLY. The page now requires an internal Okta login (confirmed by screenshot `out/shots/gestalt-a11y.png`).
    - **Claim (via search summary):** Pinterest targets WCAG 2.2 AA; ~2,500 in-product accessibility improvements since 2021.
    - **Limits:** unverifiable.

## Figma

13. **How Figma's multiplayer technology works.** Evan Wallace. Figma blog, 2019-10-16. https://www.figma.com/blog/how-figmas-multiplayer-technology-works/. READ.
    - **Claim:** server-authoritative, CRDT-inspired, last-writer-wins per property; OTs rejected.
    - **Evidence:** engineering description, with stated limits (text merges, reparent cycles, undo).
    - **Context:** Tier 2.
    - **Limits:** first-party.
14. **WebAssembly cut Figma's load time by 3x.** Evan Wallace. Figma blog, 2017-06-08. https://www.figma.com/blog/webassembly-cut-figmas-load-time-by-3x/. READ.
    - **Claim:** load time improved >3×.
    - **Evidence:** internal measurement across document sizes (load = init + download + first render).
    - **Context:** Tier 2.
    - **Limits:** used only in Firefox at the time; 2017 data.
15. **Building Accessibility Into a Canvas-Based Product.** David Winslow & Elynn Lee. Figma blog, 2026-07-01. https://www.figma.com/blog/building-accessibility-into-a-canvas-based-product/. READ.
    - **Claim:** a canvas strips browser accessibility; the "Mirror DOM" rebuilds it.
    - **Evidence:** engineering description.
    - **Context:** Tier 2.
    - **Limits:** no audit; no statement of what remains inaccessible.
16. **Reduce memory usage in files.** Figma Help Center, undated. https://help.figma.com/hc/en-us/articles/360040528173-Reduce-memory-usage-in-files. READ.
    - **Claim:** ~2 GB active memory limit per tab, which applies to the desktop app too.
    - **Context:** Tier 2 docs.
    - **Limits:** no date given.
17. **Figma accessibility blog posts and FigJam screen reader help.** QUOTED ONLY (search summaries).
    - **Claim:** FigJam screen-reader support since 2023; "Adapt content for screen readers" setting; 15+ improvements in 2024–25.
18. **Why Figma Wins.** Kevin Kwok. kwokchain.com, 2020-06-19 (updated 2025-07-31). https://kwokchain.com/2020/06/19/why-figma-wins/. READ.
    - **Claim:** the product is the distribution loop; Figma is built for teams, not only designers.
    - **Evidence:** analysis.
    - **Context:** Tier 2 practitioner essay.
    - **Limits:** opinion; the author is an investor-analyst.
19. **Figma "Make Designs" pulled after copying Apple Weather.** TechCrunch / AppleInsider, 2024-07. QUOTED ONLY (search summaries).
    - **Claim:** the feature was disabled; Field blamed QA and the Config deadline.

## Stripe

20. **Designing accessible color systems.** Daryl Koopersmith & Wilson Miner. Stripe blog, 2019-10-15. https://stripe.com/blog/accessible-color-systems. READ.
    - **Claim:** the old palette failed contrast; rebuilt in CIELAB to meet WCAG 2.0 4.5:1 and 3:1.
    - **Evidence:** method description.
    - **Context:** Tier 2.
    - **Limits:** no audit of the resulting product.
21. **How Stripe builds interactive docs with Markdoc.** Ryan Paul. stripe.dev, 2022-09-13. https://stripe.dev/blog/markdoc. READ.
    - **Claim:** docs inject the user's test keys and conditional content; Markdoc deliberately omits loops and variables.
    - **Evidence:** engineering description.
    - **Context:** Tier 2.
    - **Limits:** no metrics.
22. **Merchant complaints about Stripe holds and freezes.** Chargeflow, Shuttle, Sleft Payments and others, 2025–26. QUOTED ONLY (search summaries).
    - **Claim:** holds are the top merchant complaint; "2,018 Reddit threads analysed".
    - **Context:** Tier 4.
    - **Limits:** competitor or consultancy SEO content with no method. Graded D.

## GitHub

23. **Crafting a better, faster code view.** Joshua Brown. GitHub Blog, 2023-06-21. https://github.blog/engineering/architecture-optimization/crafting-a-better-faster-code-view/. READ.
    - **Claim:** virtualisation cut an 18k-line render from ~27 s to <1 s; it broke Ctrl+F; fixed with a hidden textarea; "users think of GitHub as a page, not as an app".
    - **Evidence:** first-party measurement.
    - **Context:** Tier 2.
    - **Limits:** first-party.
24. **Accessibility Conformance Report for GitHub.com.** GitHub, report dated 2026-09-08. https://accessibility.github.com/conformance/github-com/. READ.
    - **Claim:** WCAG 2.2 A/AA audit (VPAT 2.5) listing outstanding issues by criterion and priority.
    - **Evidence:** audit of 100+ scenarios.
    - **Context:** Tier 1/2 audit, self-published.
    - **Limits:** the auditor's independence is not stated in my summary.
25. **From latency to instant: Modernizing GitHub Issues navigation performance.** Alexander Lelidis. GitHub Blog, 2026-05-14. https://github.blog/engineering/architecture-optimization/from-latency-to-instant-modernizing-github-issues-navigation-performance/. READ.
    - **Claim:** P50 went from ~1,200 to ~700 ms and P90 from ~2,400 to ~2,100 ms; ~4.7% cache divergence accepted.
    - **Evidence:** first-party RUM percentiles.
    - **Context:** Tier 2.
    - **Limits:** first-party.
26. **"Why is GitHub UI getting so much slower?"** Lobsters discussion, 2025-08-08. https://lobste.rs/s/5qq2k2/why_is_github_ui_getting_so_much_slower. READ.
    - **Claim:** users report slowness, broken back navigation, and hidden PR content after the React migration.
    - **Evidence:** anecdotes, no measurements.
    - **Context:** Tier 4.
    - **Limits:** a self-selected audience.
27. **GitHub Docs: accessibility settings, keyboard shortcuts, command palette.** QUOTED ONLY (search summaries).
    - **Claim:** character-key shortcuts can be disabled; palette shortcuts can be customised.

## Spotify

28. **Shuffle: Making Random Feel More Human.** Ludvig Borgne & Chidem Sahiner. Spotify Engineering, 2025-11-13. https://engineering.atspotify.com/2025/11/shuffle-making-random-feel-more-human. READ.
    - **Claim:** "statistical randomness doesn't always translate into perceived randomness"; the "Fewer Repeats" default; Standard Shuffle kept.
    - **Context:** Tier 2.
    - **Limits:** no user-research data. It says shuffle was purely random "for the last 5 years", which conflicts with reports of the 2014 change.
29. **How to shuffle songs?** Lukáš Poláček. Spotify Labs, 2014-02. https://engineering.atspotify.com/2014/02/how-to-shuffle-songs/. QUOTED ONLY (404 to the fetch tool; seen via HN and press).
    - **Claim:** artist-spreading shuffle replaced pure random after complaints.
30. **"How to Shuffle Songs? (2014)" discussion.** Hacker News, 2023. https://news.ycombinator.com/item?id=38330877. READ.
    - **Claim:** links the 2014 post; commenters say people don't want true random; some allege caching or promotion bias.
    - **Context:** Tier 4.
    - **Limits:** the bias claims are speculation.
31. **Spotify newsroom, Stream On 2023.** 2023-03-08. https://newsroom.spotify.com/2023-03-08/new-home-page-scroll-clips-previews/. QUOTED ONLY (search summary).
    - **Claim:** vertical Home feed with sub-feeds and previews.
32. **How Apple Music could benefit from Spotify's bad redesign.** Chance Miller. 9to5Mac, 2023-03-09. https://9to5mac.com/2023/03/09/spotify-redesign-apple-music/. READ.
    - **Claim:** the redesign does "too much"; music is buried; the redesign is driven by podcast and audiobook investment.
    - **Context:** Tier 2 press opinion.
    - **Limits:** opinion from an Apple-focused outlet.
33. **Spotify scraps shuffle restriction for users of free tier.** Murray Stassen. Music Business Worldwide, 2025-09-15. https://www.musicbusinessworldwide.com/spotify-scraps-shuffle-restriction-for-users-of-free-tier/. READ.
    - **Claim:** Pick/Search/Share & Play for free users after 18 months of tests; 60% of Premium subscribers started on Free; a VP says the old free tier felt "almost broken".
    - **Context:** Tier 2 press quoting the company.
34. **Encore design system posts** (Spotify Design / Medium, 2019–2020). QUOTED ONLY (search summaries).
    - **Claim:** a family of design systems joined by tokens; previously 22 disconnected systems.

## Canva

35. **How Canva's growth team improves activation +10%.** Ty Magnin. Appcues blog, undated. https://www.appcues.com/blog/canva-growth-process. READ.
    - **Claim:** goal-branched onboarding raised poster activation 10%, tested on 5% of new users.
    - **Evidence:** a Canva growth manager's account.
    - **Context:** Tier 2/4.
    - **Limits:** the vendor sells the onboarding tool; no absolute rates given.
36. **How Canva's Templates Drive User Acquisition, Onboarding, Retention and Revenue.** Olabinjo Adeniran. Growth Case Studies, 2025-11-06. https://growthcasestudies.com/p/canva-templates. READ.
    - **Claim:** templates act as SEO, onboarding and monetisation.
    - **Context:** Tier 4.
    - **Limits:** company figures uncited.
37. **Canva Accessibility Conformance Report, WCAG Edition (VPAT 2.4).** Canva, June 2021. https://content-management-files.canva.com/e9ee69ee-b0c9-4493-93de-85f26a752a61/VPAT2.4WCAGCanva.pdf. READ (pp. 1–6).
    - **Claim:** WCAG 2.0/2.1 A/AA. SC 2.1.1, 2.4.3 and 2.2.2 "Does Not Support"; several criteria partial.
    - **Evidence:** automated tools plus JAWS 2019 and VoiceOver testing across 7 flows.
    - **Context:** Tier 1/2 audit.
    - **Limits:** 2021, likely outdated.
38. **Canva Help, "Use a screen reader in the Canva Editor".** https://www.canva.com/help/screen-reader-editor/. QUOTED ONLY (403; search summary).
    - **Claim:** screen-reader support on desktop and browser, not mobile.
39. **Critiques of the "Canva aesthetic".** Westenberg, Glastris and others. QUOTED ONLY (search summaries).
    - **Claim:** homogenisation.
    - **Limits:** opinion.

## Dropbox

40. **My YC app: Dropbox – Throw away your USB drive.** Hacker News, 2007-04-04. https://news.ycombinator.com/item?id=8863. READ.
    - **Claim:** BrandonM's FTP/curlftpfs/SVN comment; Houston's reply stressing a local folder with background sync.
    - **Context:** Tier 4 primary historical record.
41. **Meet the New Dropbox.** Michael Tsai (roundup), 2019-06-13. https://mjtsai.com/blog/2019/06/13/meet-the-new-dropbox/. READ.
    - **Claim:** the new desktop app was criticised for memory use, popping itself up, and mission drift. Quotes from Sandofsky, Heer, Arment, Fleishman and Gruber.
    - **Context:** Tier 2/4.
    - **Limits:** quotes from Apple-centric commentators.
42. **Startup Lessons Learned.** Drew Houston. Slides, 2010-04. https://www.slideshare.net/slideshow/dropbox-startup-lessons-learned-3836587/3836587. READ (transcript).
    - **Claim:** SEM CPA of $233–388 for a $99 product; referrals "permanently increased signups by 60%"; 35% of daily signups came from referrals.
    - **Context:** Tier 2 founder.
    - **Limits:** self-reported.
43. **Apple's File Provider Forces Mac Cloud Storage Changes.** Adam Engst. TidBITS, 2023-03-10. https://tidbits.com/2023/03/10/apples-file-provider-forces-mac-cloud-storage-changes/. READ.
    - **Claim:** `~/Library/CloudStorage` location; no external drives; online-only files not backed up by Time Machine; drag moves instead of copying.
    - **Context:** Tier 2.

## Revolut and Monzo

44. **The era of ease has arrived with Revolut 10.** Jessica Phelan. Revolut blog, 2023-10-10. https://www.revolut.com/blog/post/revolut-10/. READ (screenshot, `out/shots/revolut-10-blog.png`).
    - **Claim:** a simplified home with all accounts; customisable backgrounds, widgets, themes and navigation; "countless customer interviews".
    - **Context:** Tier 2 marketing.
    - **Limits:** no data.
45. **Revolut named in more fraud reports than any other UK bank.** FStech, 2024-10-15. https://www.fstech.co.uk/fst/Revolut_Named_In_More_Fraud_Reports_Than_Any_Other_UK_Bank.php. READ.
    - **Claim:** 9,793 Action Fraud reports naming Revolut against Barclays' 7,874 (FOI by BBC Panorama).
    - **Context:** Tier 2.
    - **Limits:** not normalised per customer.
46. **Panorama "23 minutes via in-app chat" anecdote; Which?/FOS complaint counts.** QUOTED ONLY (search summaries).
47. **We've improved our gambling block.** Monzo blog, 2023-09-13. https://monzo.com/blog/weve-improved-our-gambling-block. READ.
    - **Claim:** cooldown of up to a year; self-written reminder note; ~100,000 users in 10 months; 200,000+ blocked attempts; GamCare alignment from 45% to 87%.
    - **Context:** Tier 2.
    - **Limits:** usage, not outcomes.

## Apple

48. **Apple introduces a delightful and elegant new software design.** Apple Newsroom, 2025-06-09. https://www.apple.com/newsroom/2025/06/apple-introduces-a-delightful-and-elegant-new-software-design/. READ.
    - **Claim:** Liquid Glass "bring[s] greater focus to content"; tab bars shrink on scroll.
    - **Context:** Tier 2.
    - **Limits:** no legibility or accessibility discussion.
49. **Liquid Glass Is Cracked, and Usability Suffers in iOS 26.** Raluca Budiu. NN/g, 2025-10-10. https://www.nngroup.com/articles/liquid-glass/. READ.
    - **Claim:** legibility, cramped tab bars, collapsing navigation, Safari truncation, target spacing.
    - **Evidence:** expert review, no user study.
    - **Context:** Tier 1/2.
    - **Limits:** one-sided; the target-size figures are uncited.
50. **iOS 26.1: Reduce Liquid Glass Effects With Apple's New Toggle.** Tim Hardwick. MacRumors, 2025-11-04. https://www.macrumors.com/how-to/ios-26-1-reduce-liquid-glass-effects/. READ.
    - **Claim:** Clear/Tinted setting location and effect.
    - **Context:** Tier 2.
51. **Tim Cook Apologizes For Apple Maps, Points To Competitive Alternatives.** Jordan Crook. TechCrunch, 2012-09-28. https://techcrunch.com/2012/09/28/tim-cook-apologizes-for-apple-maps-points-to-competitive-alternatives/. READ.
    - **Claim:** the letter's quotes.
    - **Context:** Tier 2, reporting a primary letter.

## India

52. **Introducing Kill Switch.** Nithin Kamath. Z-Connect (Zerodha), 2021-06-09. https://zerodha.com/z-connect/console/introducing-kill-switch. READ.
    - **Claim:** segment disable for 12 hours; positions must be closed first; frequency is inversely related to profitability.
    - **Context:** Tier 2.
    - **Limits:** no usage or outcome data.
53. **Zerodha Nudges** (Z-Connect updates; support portal). QUOTED ONLY (search summaries).
    - **Claim:** nudges for concentration >50%, ETF premium or discount to iNAV, freeze-limit slicing, and dubious or illiquid stocks.
54. **SEBI: 93% of individual traders incurred losses in equity F&O, FY22–FY24.** SEBI press release, 2024-09. https://www.sebi.gov.in/media-and-notifications/press-releases/sep-2024/updated-sebi-study-reveals-93-of-individual-traders-incurred-losses-in-equity-fando-between-fy22-and-fy24-aggregate-losses-exceed-1-8-lakh-crores-over-three-years_86906.html. QUOTED ONLY (search summary).
    - **Claim:** 93% lost money; aggregate losses >₹1.8 lakh crore.
    - **Context:** Tier 1 regulator.
55. **Nithin Kamath slams 'Dark Patterns' in finance apps.** Storyboard18, 2025-07. https://www.storyboard18.com/brand-makers/nithin-kamath-slams-dark-patterns-in-finance-apps-says-industry-incentives-often-work-against-users-73717.htm. READ.
    - **Claim:** incentives are skewed toward the business; Zerodha has avoided dark patterns. Also cites ASCI's 52 of 53 figure.
    - **Context:** Tier 2 press.
    - **Limits:** self-report with no examples.
56. **CRED's design philosophy.** Amit Naik. Analytics India Magazine, 2022-07-15. https://analyticsindiamag.com/it-services/creds-design-philosophy. READ.
    - **Claim:** the move from Synthour (neumorphic) to NeoPOP as the fourth design system; open-sourced.
    - **Context:** Tier 2 press quoting CRED.
    - **Limits:** uncritical.
57. **CRED user complaints about complexity.** QUOTED ONLY (search summaries of reviews and blogs).
58. **CCPA penalises Zepto, IndiGo, Physics Wallah and 6 other platforms over dark patterns.** Free Press Journal, 2026-08-05. https://www.freepressjournal.in/business/ccpa-penalises-zepto-indigo-physics-wallah-and-6-other-platforms-over-dark-patterns. READ.
    - **Claim:** Zepto fined ₹7 lakh for drip pricing and basket sneaking; other platforms and violations listed.
    - **Context:** Tier 2 press reporting a government statement.
59. **Zepto CEO calls dark patterns "a mistake".** Storyboard18 / BestMediaInfo. QUOTED ONLY (both returned 403; search summary).
60. **98% of top Indian apps use deceptive patterns: ASCI report.** Campaign India, 2024. https://www.campaignindia.in/article/98-of-top-indian-apps-use-deceptive-patterns-asci-report/497533. READ.
    - **Claim:** 52 of 53 apps, 12,000+ screens, 2.7 patterns per app; privacy deception, interface interference, drip pricing and false urgency are the most common.
    - **Evidence:** ASCI Academy + Parallel expert review.
    - **Context:** Tier 2 press on a Tier 2 study.
    - **Limits:** apps not named; I did not read the report itself.
61. **Knitroot Magic Checkout case study.** Razorpay blog, 2022-04-29. https://razorpay.com/blog/knitroot-magic-checkout-case-study/. READ.
    - **Claim:** conversion "doubled"; abandonment "reduced by 100%".
    - **Context:** Tier 4 vendor marketing.
    - **Limits:** no baseline or method; implausible. Graded D.
62. **Groww design coverage** (Medium student case studies, marketing blogs). QUOTED ONLY (search summaries).
    - **Limits:** no primary evidence found.

## Other products

63. **Letter to Arc members 2025.** Josh Miller. The Browser Company (Substack), 2025-05-26. https://browsercompany.substack.com/p/letter-to-arc-members-2025. READ.
    - **Claim:** "too different… too little reward"; feature-usage percentages; strong D1 retention among fans.
    - **Context:** Tier 2 first-party.
    - **Limits:** written to justify a pivot.
64. **How Superhuman Built an Engine to Find Product/Market Fit.** First Round Review (Rahul Vohra). https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/. READ.
    - **Claim:** 100 ms, then <50 ms targets; keyboard-first; PMF score 22% → 33% → 58%.
    - **Context:** Tier 2 interview.
    - **Limits:** founder self-report. The 1:1 onboarding detail is QUOTED ONLY.
65. **Things (software).** Wikipedia. https://en.wikipedia.org/wiki/Things_(software). READ.
    - **Claim:** Apple Design Awards 2009 and 2017; separate paid apps per platform.
    - **Context:** Tier 4 reference.
66. **The Last of Us 2 – Blind Accessibility Review.** "Sightless Kombat". Can I Play That?, 2020-06-18. https://caniplaythat.com/2020/06/18/the-last-of-us-2-review-blind-accessibility/. READ.
    - **Claim:** playable without sighted help; mechanisms and limits listed.
    - **Context:** Tier 2/4 disabled-reviewer outlet.
    - **Limits:** one reviewer. The "60+ settings" figure came from search summaries of CNN and CBC.
67. **The Small But Important Change 'Celeste' Made to Its Celebrated Assist Mode.** Patrick Klepek. Vice, 2019-09-16. https://www.vice.com/en/article/celeste-assist-mode-change-and-accessibility/. READ.
    - **Claim:** old and new wording; feedback from Lexa and Jones; Thorson's quote.
    - **Context:** Tier 2.
68. **One thing per page.** Tim Paul. GOV.UK Design in Government blog, 2015-07-03. https://designnotes.blog.gov.uk/2015/07/03/one-thing-per-page/. READ.
    - **Claim:** benefits for low-confidence users, mobile, and branching.
    - **Evidence:** asserted research, not published.
    - **Context:** Tier 1/2.
    - **Limits:** commenters raise the limits noted in the notes.

## Research on aesthetics and usability

69. **The Aesthetic-Usability Effect.** Kate Moran. NN/g, 2024-02-03. https://www.nngroup.com/articles/aesthetic-usability-effect/. READ.
    - **Claim:** attractive UIs make users more tolerant of minor issues, and can mask problems in testing.
    - **Evidence:** cites Kurosu & Kashimura 1995.
    - **Context:** Tier 1/2.
70. **Kurosu & Kashimura (1995), "Apparent usability vs. inherent usability", CHI '95 companion.** QUOTED ONLY (via NN/g).
    - **Claim:** 26 ATM layouts, 252 participants; perceived ease correlated with aesthetics.
71. **Is beautiful really usable? Toward understanding the relation between usability, aesthetics, and affect in HCI.** Tuch, Roth, Hornbæk, Opwis, Bargas-Avila. *Computers in Human Behavior* 28(5):1596–1607, 2012. PDF via https://cpb-us-e1.wpmucdn.com/wp.wwu.edu/dist/8/2868/files/2018/04/Tuch-et-al-2012-Is-Beautiful-Usable-2don1em.pdf. READ (abstract and introduction).
    - **Claim:** aesthetics did not affect perceived usability; poor usability lowered post-use aesthetics ratings.
    - **Evidence:** lab experiment, n=80, 2×2 manipulation of an online shop.
    - **Context:** Tier 1.
    - **Limits:** one lab study; strong usability manipulation.
72. **The influence of product aesthetics and usability over the course of time: a longitudinal field experiment.** Sonderegger, Zbinden, Uebelbacher, Sauer. *Ergonomics* 55(7):713–730, 2012. https://www.tandfonline.com/doi/full/10.1080/00140139.2012.672658. QUOTED ONLY (403 and captcha; search summary).
    - **Claim:** the aesthetic effect wanes with exposure (2-week field study).

## Screenshots taken (in `out/shots/`)

- `netflix-artwork-blog.png`: Netflix TechBlog post (source 1).
- `pinterest-perf-blog.png`: Pinterest Engineering post (source 10).
- `gestalt-a11y.png`: shows that Gestalt's accessibility page is behind an internal login (source 12).
- `revolut-10-blog.png`: Revolut 10 blog post (source 44).
