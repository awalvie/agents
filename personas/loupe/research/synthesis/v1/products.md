# Products: benchmarks, counterexamples, poor examples

Read this file when you need a real product to compare with, or an alternative solution to name. Each entry gives what the product teaches, its evidence (source type), its tradeoff and where it fails. Observations are as of 2026-09 unless dated. None of the products was used hands-on; entries rest on team writing, audits, regulators, press, user reports and public-page screenshots.

**Before crediting design, rule out other causes.** Network effects (GitHub, Figma, Craigslist), lock-in (Bloomberg, Excel, health records), content or data (Netflix, Google Maps), price (Zerodha, Revolut), and a buyer who is not the user (health records) usually explain market share better than the interface does `[CH · C]`. Copy a mechanism only where your users share its conditions.

## Index by lesson

| Lesson | Products |
|---|---|
| Borrow a known model | Dropbox, Flighty, Canva, Arc (failure) |
| Expert speed through recall and stability | Bloomberg, Superhuman, VS Code, GitHub, Linear |
| Density that works | GitHub, Excel, Craigslist, Bloomberg, Linear |
| Speed as design | Linear, Pinterest, GitHub, Superhuman, Notion |
| Plain but excellent | GOV.UK, Craigslist, Wikipedia |
| Accessible by construction | GOV.UK, Stripe colour, Figma Mirror DOM, The Last of Us II |
| Redesign: regression vs transition | Sonos, Figma UI3, Apple Photos, Instagram, Snapchat, Slack, Duolingo, Office Ribbon, Wikipedia |
| Beauty is not usability | Liquid Glass, Vercel, the "Linear look", Things 3 |
| Silent automation and mode errors | Excel, Hawaii alert, health records |
| Business goals vs user goals | Amazon Prime, Booking.com, Pinterest, Spotify, Netflix, Zepto, Uber |
| Protective friction | Monzo, Zerodha |
| Data is the experience | Google Maps, Apple Maps 2012 |
| AI output presentation | Apple Intelligence summaries, Google AI Overviews |

## Benchmarks (study what they do, and where they fail)

- **GOV.UK** (web). *Teaches:* "visually ordinary but exceptionally effective". Plain language; underlined links; a text "Menu" on mobile; equal Accept and Reject buttons on its cookie banner; errors that reach assistive technology (screenshots, 2026-09). Its design system was audited as meeting WCAG 2.2 AA (2024), and it says openly which components are untested. *Tradeoff:* warmth and distinctiveness. *Fails:* paged forms are slow for daily expert users, and its research is asserted rather than published.
- **Stripe** (docs, colour system). *Teaches:* docs for logged-in developers inject their own test keys into code samples (team blog, 2022). Its palette was rebuilt in a perceptual colour space so accessible pairs follow a rule (2019). *Fails:* its marketing uses grey and gradient text over a ribbon, which no single contrast ratio can check (screenshot). Merchants complain about account holds, but that evidence is poor.
- **Linear** (web and desktop). *Teaches:* speed from its architecture (a local store with optimistic sync), keyboard-first use, and hierarchy by visual weight (team blogs, 2024, 2026). *Fails:* its opinionated workflow suits only teams whose process matches. There is no public accessibility audit. Its marketing's dim grey text may be low contrast (visual impression only, not measured).
- **GitHub** (web). *Teaches:* a dense page built on one consistent object model (repository, files, issues, pull requests), a command palette, and single-key shortcuts that users can switch off. It restored native find after virtualising the code view (team blog, 2023). *Fails:* users report slowness and broken Back after the move to client-side rendering (forum, 2025). Its own audit lists many open keyboard and reflow issues (2026-09). Its network effects tolerate the regressions.
- **Figma** (browser). *Teaches:* shared live state instead of files sent back and forth (team blog, 2019). The share link is also its distribution, which explains much of its win over Sketch (Kwok 2020). *Fails:* a 2 GB memory limit per tab; a canvas that is inaccessible until rebuilt (Mirror DOM, 2026); and its 2024 AI "Make Designs" feature produced near-copies of Apple's Weather app and was pulled.
- **Dropbox** (desktop). *Teaches:* invisible software that adds no new concept (Hacker News, 2007). Growth came mostly from a referral loop: referrals raised sign-ups 60% after paid search failed (founder slides, 2010). *Fails:* the 2019 "hub" app made a background utility demand attention. Apple's File Provider moved its folders, breaking external-drive workflows (TidBITS, 2023).
- **Canva** (web). *Teaches:* organised by what the user wants to make, not by tool; templates remove the blank page. A goal-based onboarding branch raised design creation 10% (vendor case study). *Fails:* outputs look alike. Its 2021 audit said the editor canvas was not keyboard accessible.
- **Flighty** (iOS; Apple Design Award 2023). *Teaches:* copy a proven convention from outside software, here the airport departure board (Apple interview). *Evidence:* reputation only.
- **Superhuman** (email). *Teaches:* speed as the product, with targets under 100 ms, then under 50 ms. It narrowed its audience to "high-expectation" users (interview). *Fails:* people who won't invest in learning; it paid for human onboarding.
- **VS Code** (desktop). *Teaches:* its command palette gives "access to all functionality" and shows each keybinding beside the command, which bridges novice and expert use (docs).
- **Pinterest** (web). *Teaches:* measure perceived wait, not page load; the 2015 experiment gave 40% more mobile sign-ups (team blog, 2017). *Fails:* a login wall between image-search visitors and the source. More than 28,000 people installed a browser extension to hide Pinterest from results (Inverse, 2021).
- **Spotify** (mobile). *Teaches:* perceived randomness is not statistical randomness. The "Fewer Repeats" shuffle spreads artists and keeps Standard Shuffle as an escape hatch (team blog, 2025). *Fails:* the 2023 Home feed promoted podcasts and audiobooks over users' own music (press criticism). The free tier restricted play on purpose until 2025.
- **Netflix** (TV). *Teaches:* artwork as decision support, personalised per member (team blog, 2017). *Fails:* autoplay previews were optional only from 2020, after complaints; personalised artwork can misrepresent a film ([interaction.md](interaction.md)); the 2025 homepage shows fewer titles (press).
- **Wikipedia** (web). *Teaches:* when an evidence-based default (limited line width, 2023) met a vocal expert community, the resolution was a visible user control (text size, width, light or dark). Editors objected; the readers, who were the ones measured, cannot vote. The Foundation reported no drop in pageviews or edits.
- **Monzo, Zerodha** (finance). *Teaches:* friction the user chooses, placed at the moment of decision. Monzo's gambling block has a cooling-off period of up to a year and shows the user's own reminder note. Zerodha's 12-hour Kill Switch requires positions to be closed first, and nudges flag concentration above 50% (team blogs). *Fails:* both report usage figures, not reduced harm. Zerodha earns per trade, so its nudges cut its own revenue.
- **The Last of Us Part II; Celeste** (games). See [accessibility-performance.md](accessibility-performance.md).

## Counterexamples to conventional rules

- **Bloomberg Terminal.** Breaks "recognition over recall", "be intuitive" and "reduce density". Function codes give experts constant-time access. Learning takes about a week (one first-person account). Market position comes from data, a chat network and employer-paid seats, not the UI. *Where it now fails:* the vendor itself calls the density "untenable" and is testing a chat interface (2026).
- **Excel.** Breaks "keep it simple". The grid shows every intermediate value, and calling a function is easy even where writing one is hard. *Fails:* silent automatic conversions (see "Poor examples").
- **Craigslist.** Breaks visual hierarchy and modern aesthetics. Every category sits one tap away on one page. Its mobile layout now has its own category rail (screenshots, 2026-09), so "Craigslist never changes" is out of date. It won through local market depth and free posting. Estimated revenue fell from about $1B (2018) to about $300M (2024) (unaudited analyst figures) as specialist rivals added photos, maps and identity.
- **Office Ribbon (2007).** Broke 20 years of consistency and was kept. It rested on about 1.3 billion telemetry sessions (team blog, 2006). The outcome claims ("four times as many features used") are unchecked, and experts reported lasting slowdowns. Telemetry that users opt into may under-sample power users.
- **Dead Space and HUD-free games.** Removing on-screen status raised *experts'* immersion but not novices' (Iacovides et al. 2015; 24 players; interaction only marginal) `[C]`. How much status to show depends on expertise.

## Poor examples and failed redesigns

- **Sonos app (2024-05).** A rewrite tied to a hardware launch removed queue editing, sleep timers and more, and broke VoiceOver. Sonos reported at least $100M in lost revenue, and the CEO left. *Lesson:* this was regression, not change aversion. Inventory every capability and accessibility path before a rewrite.
- **Figma UI3 floating panels (2024).** Reversed before full launch because "they slowed people down". Icon-only labels hurt screen-reader users. *Lesson:* measure experts' speed, not their stated preferences.
- **Apple Photos (iOS 18 → 26).** A single view with no tabs reduced chrome and removed the map of the app; Apple restored the tabs. *Lesson:* authority is not evidence.
- **Instagram full-screen feed test (2022).** Copied TikTok's model onto a different content mix. "The usage data isn't great" (Mosseri), and it was reversed.
- **Snapchat (2018).** Moved friends and media apart and sorted Stories by algorithm. Daily users fell from 191M to 188M, which Snap blamed on the redesign. Instagram Stories and a slow Android app are confounders.
- **Slack (2023).** Added Home, DMs and Activity tabs to "turn down the volume on cognitive load"; power users complained of extra clicks. No data was published.
- **Arc browser.** Loved by designers, used narrowly. 4.17% of daily users used Live Folders (team letter, 2025). The letter also justified a pivot, so its framing may be self-serving.
- **Liquid Glass (iOS 26).** Legibility and unstable controls, patched by settings and adaptive backgrounds ([visual.md](visual.md)).
- **Excel conversions and the England COVID data loss.** Gene names became dates in 30.9% of papers with Excel gene lists, and human genes were renamed to cope. 15,841 COVID-19 cases were silently dropped at a row limit (2020).
- **Hawaii false missile alert (2018).** Test and live alerts in one menu, the same confirmation text for both, and 38 minutes to send a correction (FCC).
- **Electronic health records.** Of 1.735M safety reports, 557 explicitly linked usability to possible harm; data entry was 27% of those and alerts 22% (Howe et al., JAMA 2018). Physicians rated usability 45.9 on the System Usability Scale, in the bottom 9% of scores (Melnick 2019, seen as an abstract). Poor usability persists because hospitals buy and clinicians use.
- **Amazon Prime cancellation.** An internally code-named "Iliad" flow; the FTC complaint called it a "Four-Page, Six-Click, Fifteen-Option" process. Settled for $2.5B without admission (2025-09).
- **Booking.com and hotel sites.** About 25,000 tests a year (HBR 2020), and UK CMA commitments on false scarcity, hidden fees and paid ranking (2019). *Lesson:* an experimentation culture amplifies whatever metric it is pointed at.
- **Airbnb fees; Zepto.** Airbnb's CEO introduced total-price display (2022-11) after complaints about opaque pricing. Zepto was fined ₹7 lakh for drip pricing and basket sneaking (2026-08).
- **Uber surge pricing.** Uber's economist said riders with low phone batteries accept surges more readily, and that Uber did not use this (NPR 2016, second-hand). Restraint is a policy choice.
- **Apple Maps (2012).** The CEO apologised for wrong data and pointed users to rivals. For maps, data quality *is* the experience. The same holds for Google Maps, whose lead O'Beirne (2017) traced to data byproducts.
- **Apple Intelligence summaries; Google AI Overviews.** See [interaction.md](interaction.md).
- **Vendor statistics.** Razorpay claimed "cart abandonment reduced by 100%". Treat such figures as `[D]` unless a method is published ([uncertainty.md](uncertainty.md)).

**Not researched.** YouTube, Discord, Reddit, Amazon's retail pages, Airbnb's search, Uber's ride flow, Notion's onboarding, Groww and most Indian consumer apps beyond Zepto and Zerodha. Their absence is a gap, not a finding.
