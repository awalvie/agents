# Research notes: products known for great design

Area: apps and websites that respected designers, design teams and juried awards hold up as well designed, and exactly why. Researcher 5 of 5. All observations are as of 2026-09 unless another date is given. Research done 2026-09-25.

## How to read these notes

- **I did not use any of these products.** I could not install, log in to or run anything. Every product observation rests on one of: the product's own **site**, its **docs/help centre**, a **first-party** engineering/design blog or press release, a published **audit** (VPAT/ACR), the **press**, **user reports** (forums, Hacker News, Reddit as quoted by the press), or a **screenshot** I took. Each observation below says which.
- Single observations about one product carry their source type instead of the two labels. Generalised findings (mostly in "Cross-product findings") carry both labels: kind of claim (the brief's seven classes) and evidence strength (A–D).
- Accessibility and Performance fields are filled only from a published audit, accessibility statement or public measurement. Otherwise they say "not assessed".
- Several key primary sources are on Medium, which blocks the fetch tool. I read them by screenshotting the page with `tools/shot.mjs` and reading the image. Some pages were only partly readable that way. Where I relied on a search-engine summary instead of the page, the note says so and `sources.md` marks it.
- **Awards were used only to find candidates.** The Apple Design Award (Things 3, 2009 and 2017) shows that a product has a good reputation among designers. It is not evidence that the product is usable.

## Rule-outs applied to every product

Before crediting design, I asked: is the success better explained by **network effects** (GitHub, Figma inside companies), **lock-in** (Dropbox, GitHub, Apple), **content** (Netflix, Spotify, Pinterest), **price** (Revolut FX, Zerodha zero-brokerage delivery, UPI apps), or **market position** (Apple defaults, Stripe's developer mindshare)? For most products here the honest answer is "design is one cause among several, and the others are larger". The products where design plausibly *is* the main mechanism are narrower: Stripe's docs, Figma's multiplayer model, Canva's template-first onboarding, and Superhuman's speed. Even there, the evidence is mostly first-party.

---

# Full specimen records

## 1. GitHub (web; also Desktop, CLI, mobile)

- **Context:** hosting, reviewing and collaborating on code, plus issues, CI (Actions), and now AI agents (Copilot).
- **Users / expertise:** mixed. Its core users are expert developers; it also serves occasional contributors, designers, PMs and people who only file issues.
- **Primary tasks:** read code, review pull requests, triage issues, follow CI status, search code.
- **Strengths:** dense, scannable pages built on a shared object model (repo → files, issues, PRs, Actions), with stable URLs for everything. Keyboard shortcuts and a command palette give experts speed without cluttering the page for novices [docs]. In 2023 the code view added a file tree, symbol navigation, sticky lines and folding [first-party blog, 2023-06-21].
- **Weaknesses:** perceived speed regressed as the front end moved to client-side React. Users report slow loads, lost scroll position, broken back-button behaviour, and PR diffs hidden to keep pages fast [user reports: Lobsters thread, 2025-08; no measurements given]. The accessibility audit lists many open issues (see below).
- **Information architecture:** repository-centric, with the repo tab bar (Code, Issues, PRs, Actions…) as the main IA. Cross-repo work (notifications, org-wide projects) cuts across that hierarchy and is weaker (my inference, not a study).
- **Navigation:** tabs plus deep links, the command palette (Ctrl/Cmd+K), and single-key shortcuts. GitHub lets users switch off single-character shortcuts, and the docs present this as an accessibility setting [docs]. This supports WCAG 2.2 SC 2.1.4 (Character Key Shortcuts).
- **Interaction:** a key lesson from the 2023 code view. GitHub virtualised the file view (rendering only visible lines), which cut the initial render of an 18,000-line file from "nearly 27 seconds" to under one second. Virtualisation broke native browser find (Ctrl+F). GitHub first built its own find, then found that users "think of GitHub as a page, not as an app", and that assistive-technology users relied on native search. The fix was a hybrid: an invisible textarea holding the whole file (findable, copyable, accessible) under a virtualised, syntax-highlighted overlay [first-party blog, Joshua Brown, 2023-06-21].
- **Visual design:** Primer design system; restrained colour; density that suits experts. Not assessed further.
- **Accessibility (from audit):** GitHub.com Accessibility Conformance Report (VPAT 2.5, WCAG 2.2 A/AA), dated 2026-09-08, covering 100+ user scenarios. It lists outstanding issues including SC 2.1.1 Keyboard (14 high, 16 medium, 28 low priority), SC 1.4.10 Reflow (13 high, 85 medium), SC 2.4.3 Focus Order (43 medium, 150 low), SC 1.3.1 Info & Relationships (88 medium, 431 low), and SC 4.1.3 Status Messages (59 medium) [audit]. It is unusual for a company to publish issue counts at all. The counts are large, and they are the company's own.
- **Performance (public measurement):** for Issues navigation, time to "highest priority content" fell from P50 ~1,200 ms / P90 ~2,400 ms to P50 ~700 ms / P90 ~2,100 ms. It was achieved with an IndexedDB cache (stale-while-revalidate), "preheating" and a service worker. GitHub states it accepted ~4.7% server/cache divergence, and that cold starts still depend on JavaScript boot [first-party blog, 2026-05-14]. GitHub's own speed tiers are Instant <200 ms, Fast <1 s, Slow ≥1 s.
- **Cognitive / emotional experience:** heavy but learnable, because the object model is consistent. Frustration centres on speed. A self-described former GitHub engineer on Lobsters said quality complaints "fell on deaf ears unless AI was mentioned" [user report, unverified].
- **Business context:** network effects and lock-in dominate. Open source lives there, and profiles act as CVs. **Design is not the main reason GitHub wins.** That makes its tolerance for regressions high.
- **Principles demonstrated:** recognition over recall (the palette); flexibility and efficiency of use (shortcuts); respect for platform conventions (native find).
- **Principles violated:** "minimalism is better" (the pages are dense on purpose); client-side rendering traded speed for development velocity.
- **Tradeoffs:** richer interactive features against the speed and "it's a web page" behaviour of the server-rendered original; performance against data freshness (4.7% divergence accepted).
- **Evidence:** first-party engineering blogs (2023, 2026), ACR audit (2026), docs, user reports (unmeasured).

## 2. Netflix (TV, mobile, web)

- **Context:** choosing something to watch from a large catalogue, often on a TV with a remote.
- **Users / expertise:** everyone, including children and people with low technical skill. The input device (a D-pad remote) is the main constraint.
- **Primary tasks:** decide what to watch quickly; resume what they were watching.
- **Strengths:** the whole homepage is a recommendation surface. Netflix's CPO and product VP wrote that recommendations influence "about 80% of hours streamed", and estimated personalization and recommendations save "more than $1 billion per year" [ACM TMIS 2015, Gomez-Uribe & Hunt; **seen quoted via search summaries only**; the ACM page blocked me]. Artwork is treated as decision support: each member sees the image that the algorithm predicts will appeal to them [first-party blog, 2017-12-07, screenshot read].
- **Weaknesses:**
  - Autoplaying previews were widely hated. On 2020-02-06 Netflix made them optional: "We've heard the feedback loud and clear" [press: TechCrunch].
  - The 2025 TV homepage redesign drew heavy criticism. Users said larger tiles show fewer titles, and genre browsing moved into Search [press: Android Authority 2025-05-07; the claim that about seven titles per row dropped came from a search summary I did not verify].
- **Information architecture:** rows of algorithmically ranked collections ("rows"). Each row is a hypothesis about the user. Since 2025, callouts such as "#1 in TV Shows" and award labels sit on the tiles [first-party, 2025-05-07].
- **Navigation:** 2D grid on a remote. Since 2025, Search and My List sit at the top instead of a left rail [first-party].
- **Interaction:** autoplay previews (can be switched off since 2020 [help centre]) and autoplay of the next episode (can be switched off since 2014, per press).
- **Visual design:** artwork-dominant. Netflix's 2016 consumer research (method and sample not stated) claimed artwork was "over 82% of their focus while browsing" and that users spent "1.8 seconds considering each title". It also found that images with more than 3 people won less often [first-party, Nick Nelson, 2016-05-03]. **These are untraceable numbers (no method or sample), so I treat them as D-grade** even though they are widely repeated.
- **Accessibility:** not assessed.
- **Performance:** not assessed.
- **Cognitive experience:** Netflix's own framing is that choice is costly. The 2025 redesign rationale was reducing "eye gymnastics" when scrolling down and right [press quoting CPO Eunice Kim]. Critics argue the redesign reduces *choice visibility* in favour of *passive scrolling* [press].
- **Emotional experience:** trust damage from personalization. In 2018, Black subscribers reported artwork featuring minor Black characters in films with white leads. Netflix answered: "We don't ask members for their race, gender, or ethnicity… The only information we use is a member's viewing history" [press: The FADER, 2018-10-22]. Both things can be true. Optimising artwork for clicks based on viewing history can produce images that misrepresent the film, without any demographic input.
- **Business context:** retention; promotion of originals, live events and games (the 2025 rationale explicitly says "flexible for our broad entertainment offerings"). **Content, not UI, is the main driver**, but at Netflix's scale recommendations are the UI.
- **Principles demonstrated:** decision support through imagery; reducing time to value (resume).
- **Principles violated:** user control (autoplay by default for years); predictability (per-user artwork means two people describe different screens).
- **Tradeoffs:** click-through on each tile against honest representation; showing the breadth of the catalogue against the depth of each item (tile size).
- **Evidence:** first-party (2016, 2017, 2025); academic paper seen only as quotes; press; user reports.

## 3. Spotify (mobile, desktop, web)

- **Context:** music, and increasingly podcasts, audiobooks and video.
- **Users / expertise:** mixed. Free users are shaped by deliberate restrictions.
- **Primary tasks:** play something known; find something new; manage a library.
- **Strengths:** discovery through personalised playlists (not studied first-hand here). The **shuffle story** is the clearest design lesson. Users complained that true random shuffle felt non-random (clusters of the same artist), and Spotify changed the algorithm to *spread* artists. Spotify's 2025 engineering post states the core insight directly: "statistical randomness doesn't always translate into perceived randomness." The current "Fewer Repeats" default generates several random orders and picks the "freshest" one. The legacy "Standard Shuffle" stays available [first-party, 2025-11-13].
- **Contradiction found:** the 2014 engineering post ("How to shuffle songs?") is widely reported as having *replaced* pure random with artist-spreading. The 2025 post says that "for the last 5 years, Spotify's Shuffle was exactly that – random." So either the 2014 approach was later reverted, or the two posts describe different layers. **I could not resolve this.** The 2014 post returned 404 to the fetch tool, and I saw it only via HN and press summaries.
- **Weaknesses:** the March 2023 redesign (vertical Home feed with sub-feeds for music, podcasts and audiobooks, plus audio/visual previews [first-party newsroom, 2023-03-08]) was criticised for doing "too much at the same time" and burying music [press: 9to5Mac, 2023-03-09, Chance Miller]. Miller's diagnosis was that the feed exists to justify Spotify's podcast and audiobook investment. That is a business-surface problem, not a layout problem.
- **Information architecture / navigation:** Home / Search / Library bottom tabs. Home has become a multi-media feed; Library is user-owned.
- **Interaction:** the free tier is a case of **deliberate friction as a business lever**. Free mobile users were long limited to shuffle. On 2025-09-15 Spotify added "Pick & Play", "Search & Play" and "Share & Play" after 18 months of tests in emerging markets. On-demand listening is still capped daily. A Spotify VP was quoted: "Young users felt like the old Spotify free experience on mobile was almost broken." Spotify also said 60% of Premium subscribers began as free users [press: Music Business Worldwide, 2025-09-15].
- **Visual design:** dark UI; Encore, a *family* of design systems joined by shared design tokens rather than one monolith (Spotify says it previously had 22 disconnected systems) [search summaries of Spotify Design posts; not read in full].
- **Accessibility / Performance:** not assessed.
- **Cognitive / emotional experience:** Home asks users to weigh mixed media types. Users are strongly attached to their own playlists and angry when the service's priorities displace them.
- **Business context:** content licensing costs push Spotify toward podcasts and audiobooks it owns or controls, and toward converting free users to Premium. These goals shape Home.
- **Principles demonstrated:** match the user's mental model (shuffle); keep an escape hatch (Standard Shuffle).
- **Principles violated:** user control on the free tier (by design); focus on the primary task (Home 2023).
- **Tradeoffs:** exposure for new businesses against speed to the user's own music; perceived fairness against statistical purity.
- **Evidence:** first-party (2023, 2025), press, HN.

## 4. Figma (browser and desktop; beyond UI3)

- **Context:** interface design, prototyping, whiteboarding (FigJam), dev handoff (Dev Mode), slides.
- **Users / expertise:** expert designers at the core, plus a large ring of PMs, engineers and stakeholders who mainly view and comment.
- **Primary tasks:** design together, share a link, review and comment, inspect for build.
- **Strengths:**
  - **Multiplayer as the core mechanism.** Figma chose a server-authoritative model inspired by CRDTs, with last-writer-wins per property, over operational transforms. Co-founder Evan Wallace wrote that OTs "result in a combinatorial explosion of possible states." Known limits: simultaneous edits to the same text don't merge; concurrent reparenting that would create cycles is handled by temporarily removing objects; undo semantics in multiplayer differ from single-player [first-party, 2019-10-16].
  - **The link is the distribution.** Kevin Kwok's analysis: "The core of Figma's product *is* the core of its distribution loop," and "Figma is a tool for teams to design. Not for designers alone" [practitioner essay, 2020-06-19, updated 2025]. This is a network-effect explanation. Much of Figma's win over Sketch is not about the quality of the canvas UI.
- **Weaknesses:**
  - The browser imposes limits. The help centre states "an active memory limit of 2GB per browser tab", and says it applies even to the desktop apps because they are built on browser technology [docs; undated].
  - The Config 2024 "Make Designs" AI produced near-copies of Apple's Weather app. Figma pulled it, and CEO Dylan Field blamed insufficient QA before the Config deadline [press: TechCrunch/AppleInsider, 2024-07].
- **Information architecture:** files → pages → frames → layers; team libraries of components and variables.
- **Navigation:** canvas pan/zoom, layers panel, multiplayer cursors, and following another user's view.
- **Interaction:** direct manipulation; everything saves live (no save state); comments sit on the canvas.
- **Visual design:** covered by the other researcher (UI3).
- **Accessibility (first-party statement):** a canvas has no DOM, so it "strips away any accessibility the browser gives you for free"; the canvas had "only one `<input>` element." Figma built a "Mirror DOM", an invisible React-rendered DOM kept in sync with the canvas using real layout positions (so magnifiers and voice control can target it), plus ARIA live-region announcements [first-party, 2026-07-01]. Figma also reports FigJam screen-reader support (2023) and an "Adapt content for screen readers" setting in Design/Dev Mode/Slides [search summary of Figma blog]. **No third-party audit found.**
- **Performance:** first-party claim that WebAssembly cut load time more than 3× (load = init + download + first full render). At the time it was used only in Firefox because of Chrome bugs, and download size didn't shrink much [first-party, 2017-06-08]. The 2 GB limit above is a hard ceiling.
- **Cognitive experience:** there are many concepts (components, variants, variables, auto layout, modes), but Figma stays close to vector-editor conventions. Its novelty is in collaboration, not in basic manipulation.
- **Emotional experience:** strong designer loyalty. Anxiety over AI and pricing changes (not researched in depth).
- **Business context:** seat expansion into non-designers (Dev Mode, FigJam, Slides) aligns growth with the collaboration story.
- **Principles demonstrated:** remove the concept of "file versions to send"; shared state as the source of truth.
- **Principles violated:** none of note. It is conservative in basic interaction.
- **Tradeoffs:** browser reach and zero-install sharing against memory ceilings and a canvas that is inaccessible by default.
- **Evidence:** first-party engineering (2017, 2019, 2026), docs, practitioner essay, press.

## 5. Stripe (developer docs, Checkout, Dashboard; beyond payment methods)

- **Context:** payments infrastructure. The first "user" is a developer integrating it.
- **Users / expertise:** developers (expert), finance and ops staff (intermediate), end customers at checkout (everyone).
- **Primary tasks:** integrate quickly and correctly; see money in and out; resolve disputes.
- **Strengths:**
  - **Docs designed as an application.** When a developer is logged in, their own test API keys are injected into code samples, so the sample runs when pasted. Content changes by location and by the features the account has enabled. Stripe built Markdoc (open-sourced 2022) to separate content from code. It deliberately omits loops and variable assignment so that writers, not only engineers, can maintain the docs [first-party, Ryan Paul, 2022-09-13]. This is design as *reducing the distance between the example and the user's real situation*.
  - **Colour system rebuilt for accessibility.** None of Stripe's default small-text colours (except black) met the contrast threshold. Darkening them in RGB/HSL made them "dull and muddy". Stripe moved to a perceptually uniform space (CIELAB) with custom tools, targeting **WCAG 2.0** 4.5:1 for small text and 3:1 for large text and icons. Stated limit: some hue/lightness combinations are impossible ("no such thing as 'very colorful dark yellow'") [first-party, Koopersmith & Miner, 2019-10-15].
- **Weaknesses:** merchants complain about account holds and freezes with generic explanations, typically during risk review. **Evidence is poor.** What I found is mostly SEO pages from competitors and consultancies (for example, a claim of "2,018 Reddit threads analysed" with no method) [Tier 4, conflicted]. I found no neutral data on how often this happens.
- **Information architecture:** docs are organised by task ("Accept a payment") and backed by an API reference. The Dashboard is organised by objects (payments, customers, balances).
- **Navigation / Interaction / Visual design:** not assessed first-hand beyond the docs mechanisms above.
- **Accessibility:** the colour work is a first-party method statement, not an audit. The product itself is **not assessed**.
- **Performance:** not assessed.
- **Cognitive experience:** personalised samples remove a whole class of errors (the wrong key, a placeholder left in the code).
- **Emotional experience:** developers trust Stripe because of the docs. Merchants distrust it during holds, which is the opposite end of the relationship.
- **Business context:** developer mindshare is the moat. Risk controls protect Stripe's own liability, and holds are where the business goal and the user goal collide.
- **Principles demonstrated:** use the user's real data in examples; design the system (tokens, colour space) so accessible choices become the default.
- **Tradeoffs:** a vivid brand palette against contrast; writer-friendly authoring against expressive power (no loops).
- **Evidence:** first-party (2019, 2022); Tier 4 complaints.

## 6. Canva (web, desktop, mobile)

- **Context:** graphic design for non-designers.
- **Users / expertise:** mostly beginners; also marketers, teachers and small businesses.
- **Primary tasks:** make a good-looking poster, post or deck fast, without design training.
- **Strengths:**
  - **Templates remove the blank canvas.** Templates make the first design a matter of editing rather than creating.
  - **Onboarding split by goal.** A Canva growth manager described an A/B test (initially 5% of new users) that branched new users to specific poster types based on survey-derived popular choices. It raised "activation" (defined as the share of new users who create a design) by 10% for the poster product, with results in 2–3 weeks. They said experiments "typically" improve activation "by around 10%" [vendor case study: Appcues, undated; the vendor sells the onboarding tool].
  - Template pages are also SEO landing pages. Acquisition and onboarding are the same object [practitioner newsletter, 2025-11-06; its company numbers are uncited].
- **Weaknesses:**
  - **Homogenisation.** Critics describe a recognisable "Canva aesthetic" produced by a shared template library at vast scale [practitioner blogs; opinion].
  - Accessibility of the editor (below).
- **Information architecture:** organised by *output type* (poster, Instagram post, presentation), not by tool. This matches how beginners think ("I need a flyer") rather than how designers think ("I need a text tool").
- **Navigation / Interaction:** a left rail of asset types (templates, elements, text, uploads); drag-and-drop; snapping guides.
- **Visual design:** not assessed.
- **Accessibility (audit):** the Canva ACR (VPAT 2.4) covered the product as of **June 2021**, tested against **WCAG 2.0 and 2.1 A/AA** with JAWS 2019 + Chrome 91 and VoiceOver + Safari 14. It marked **SC 2.1.1 Keyboard "Does Not Support"** ("Elements on the canvas in the editor" not keyboard accessible, among others), **SC 2.4.3 Focus Order "Does Not Support"**, **SC 2.2.2 Pause, Stop, Hide "Does Not Support"** (autoplaying video in the logged-in home carousel), and partial support for 1.1.1, 1.3.1, 2.4.1 and 2.4.2 [audit, read directly]. **This audit is five years old.** Canva's help centre (per search summary) now says screen-reader support exists in the editor on desktop and browser, but not on mobile. I could not load that page (403). The current state is unverified.
- **Performance:** not assessed.
- **Cognitive experience:** low. Decisions are pre-made by the template, which is both the strength and the limit.
- **Emotional experience:** fast confidence ("I made something that looks professional").
- **Business context:** freemium. Premium templates and elements are the upsell. Templates are acquisition (SEO), onboarding and monetisation at once.
- **Principles demonstrated:** recognition over recall (choose, then edit); defaults as decisions; task-oriented IA.
- **Principles violated:** expressiveness and distinctiveness. Using the product well tends to produce similar outputs.
- **Tradeoffs:** time to first success against originality; accessible authoring *of outputs* (Canva has design accessibility checks, per search summary) against an inaccessible authoring *surface* (2021 audit).
- **Evidence:** audit (2021), vendor case study, practitioner writing.

## 7. Dropbox (desktop sync, web, mobile)

- **Context:** keep files the same everywhere; share them.
- **Users / expertise:** everyone, from individuals to enterprise teams.
- **Primary tasks:** save a file here, have it there; send a folder to someone.
- **Strengths:** the original design **was the file system**: "a local folder with efficient sync in the background" (Drew Houston, replying on HN, 2007-04-04). The famous top comment (BrandonM) said Linux users could already build this with "FTP account, mounting it locally with curlftpfs, and then using SVN or CVS". Houston replied that most users want plug-and-play, and cited latency problems with network drives [HN thread, read directly]. The mechanism is to **add no new concept**. Users already knew folders, so there was nothing to learn.
- **Growth rule-out:** Houston's 2010 "Startup Lessons Learned" slides say search ads cost "$233–$388" per acquisition "for a $99 product. Fail.", and "Search is a way to harvest demand, not create it". A two-sided referral programme "permanently increased signups by 60%", and 35% of daily signups came from referrals by April 2010 [slides, read via SlideShare]. So Dropbox's growth came from a referral loop tied to storage space. Invisible design made the product worth referring, but the loop did the distribution.
- **Weaknesses:**
  - **Mission drift into a visible app.** The June 2019 desktop client turned a background sync utility into a windowed "hub". Critics said it used "over half a gig of memory" and popped itself up. Glenn Fleishman said, "I saw a Dropbox app in my dock and thought I'd been infected by malware." John Gruber summed up what users wanted as "a folder that syncs perfectly" [blog roundup: Michael Tsai, 2019-06-13].
  - **Platform constraints broke the core metaphor.** Apple's File Provider API (from macOS 12.3) forced cloud folders into `~/Library/CloudStorage`. That location is hidden by default, can't live on external drives, doesn't let Time Machine back up online-only files, and made drag between locations move instead of copy [press: TidBITS, 2023-03-10]. Users with media workflows on external drives called it a "showstopper" [press/user reports].
- **Information architecture:** the user's own folder tree. Dropbox imposes none of its own.
- **Navigation / Interaction:** Finder/Explorer. The sync-status badges on file icons are the entire feedback system.
- **Visual design:** not assessed.
- **Accessibility / Performance:** not assessed (memory complaints are anecdotal).
- **Cognitive experience:** near zero while it works. When sync conflicts or online-only placeholders appear, users must suddenly understand a distributed system.
- **Emotional experience:** trust as long as the files appear. Violation when the app claims attention.
- **Business context:** the move up-market into enterprise collaboration (Spaces, 2019) pulled the product toward being visible, because a visible product can be sold to teams.
- **Principles demonstrated:** use an existing mental model; invisible software.
- **Principles violated (2019):** the calm "the best interface is no interface" stance was dropped for a business reason.
- **Tradeoffs:** a product you can sell to teams against a utility that stays out of the way. OS integration (coherence, privacy) against flexibility (external drives).
- **Evidence:** HN primary thread, founder slides, press, user reports.

## 8. Pinterest (web, mobile)

- **Context:** visual discovery and saving ideas (recipes, home, fashion).
- **Users / expertise:** mostly casual, with a planning mindset.
- **Primary tasks:** browse images, save them to boards, click through to the source.
- **Strengths:**
  - A masonry grid of images makes scanning fast.
  - **They measured perceived speed rather than raw load time.** Engineers found that full page load time (navigationStart→domComplete) "doesn't reflect performance" that matters to the user. They defined "user perceived wait time" (UPWT) as time until the *visible* part of the page, based on image load events, is rendered [first-party, Meder/Antonov/Chang, 2017-03-03, read by screenshot]. In the same post, an early-2015 mobile-web experiment improved landing-page performance by 60% and signup conversion by 40%. The later production rebuild is reported as a 40% cut in wait time, and +15% SEO traffic and +15% signup conversion [the 40/15/15 numbers come from a search summary of the same post; I read the 60/40 numbers directly]. Method: before/after and experiments on the growth team's own pages.
- **Weaknesses:** **the login wall on search traffic.** People who arrive from Google Images hit sign-up prompts before they reach the image or its source. More than 28,000 Chrome users installed an extension ("Unpinterested!") to remove Pinterest from results. A spokesperson blamed Google ("Google controls how results appear based on engagement") and said prompts can be dismissed [press: Inverse, 2021-11-05]. The same growth machinery that the performance post celebrates (logged-out landing pages → signup) is the source of the anger.
- **Information architecture:** pins → boards → the user's taste graph. Home is a personalised feed.
- **Navigation / Interaction:** infinite scroll, save, and a close-up view with visually similar items.
- **Visual design:** content-first, and the chrome recedes.
- **Accessibility:** a search summary of Pinterest's Gestalt design-system site says Pinterest targets **WCAG 2.2 AA** and has made "roughly 2,500 in-product accessibility improvements" since 2021. **The page is now behind an internal login (screenshot confirmed), so I could not verify it.** Otherwise not assessed.
- **Performance:** first-party measurements as above (2015–2016 data).
- **Cognitive experience:** low demand. Scanning images needs little reading.
- **Emotional experience:** inspiration for logged-in users, and a feeling of bait-and-switch for visitors from search.
- **Business context:** SEO-driven acquisition; ads.
- **Principles demonstrated:** measure what the user perceives; content as the interface.
- **Principles violated:** do not block a user's goal to serve your funnel (the login wall).
- **Tradeoffs:** signups against goodwill and ecosystem reputation.
- **Evidence:** first-party (2017), press (2021), unverifiable design-system claim.

## 9. Revolut (mobile), with Monzo as contrast

- **Context:** multi-currency accounts, cards, transfers, and a growing "super app" (stocks, crypto, savings, loans).
- **Users / expertise:** mixed. It started with travellers and has grown into primary banking.
- **Primary tasks:** see balances, pay, exchange currency, freeze a card, get help when something goes wrong.
- **Strengths (first-party):** Revolut 10 (2023-10-10) launched "a new, simplified look": all accounts on the home screen, switched with a tap. It also added personalisation: "custom backgrounds, widgets, themes, and navigation". Revolut says this came from "countless customer interviews" [first-party blog, read by screenshot]. Letting users customise navigation is a response to feature sprawl. The user decides which of many products gets a place in the tab bar.
- **Rule-out:** Revolut's early appeal is widely attributed to cheap currency exchange, i.e. **price**. I did not find a primary source quantifying this, so it is not graded.
- **Weaknesses (the part design can't hide):** trust and support.
  - BBC Panorama (aired 2024-10-14) obtained Action Fraud data showing Revolut named in 9,793 fraud reports over 12 months, against Barclays' 7,874 [press: FStech, 2024-10-15]. **The figures are not normalised by customer base or transaction volume**, which FStech itself notes.
  - Panorama reported a customer who said it took 23 minutes via in-app chat to reach the right team to freeze an account while money was being taken [search summary of press; not read directly].
  - Support is chat-first, with no public phone line, per complaint summaries.
- **Information architecture:** as of 2023-10, the home screen is the account carousel, with product features behind tabs and widgets the user can reconfigure.
- **Accessibility / Performance:** not assessed.
- **Cognitive experience:** each added product adds decisions. Customisable navigation moves the curation work onto the user.
- **Emotional experience:** polish creates confidence until an account freeze or fraud event. Then the lack of a human channel matters more than any screen.
- **Business context:** cross-selling products (crypto, trading, credit) pushes those products onto key surfaces. The same tension appears at Spotify.
- **Contrast, Monzo's gambling block:** a user-enabled block on gambling transactions, with a cooling-off period before removal. It started at 48 hours; since 2023-09-13 users can choose up to a year. Users can also write a note to themselves that is shown if they try to remove the block. Monzo: "The decision to gamble is often an impulsive one, so some extra 'friction' gives you the chance to think." They report "close to 100,000 people" used it in 10 months and "more than 200,000 attempted gambling transactions" blocked [first-party blog, 2023-09-13]. Outcome data (harm reduced) was not given.
- **Principles demonstrated:** personalisation as a way to manage complexity; (Monzo) friction placed where the user's future self wants it.
- **Principles violated:** Revolut's reliance on chat-only support breaks "help users recognise, diagnose, and recover from errors" at the moment it matters most.
- **Tradeoffs:** feature breadth against clarity; automated fraud controls against human recourse.
- **Evidence:** first-party (Revolut 2023, Monzo 2023), press (2024). There is **no first-party design writing from Revolut beyond marketing**, a gap in the evidence.

## 10. Apple's own apps and system UI (iOS 26 Liquid Glass; Apple Maps 2012)

- **Context:** the default apps and system chrome on a billion-plus devices. Its conventions are copied industry-wide.
- **Users / expertise:** everyone.
- **Liquid Glass (announced 2025-06-09):** a translucent material that "reflects and refracts its surroundings", meant to "bring greater focus to content". In iOS 26 tab bars shrink as the user scrolls and "fluidly expand" when they scroll back up [first-party newsroom]. **The press release does not discuss legibility or accessibility.**
- **Criticism (expert review, not a user study):** NN/g's Raluca Budiu (2025-10-10) wrote the following [expert review]:
  - Text over photos and "text on top of text" are illegible.
  - Tab bars are "cramped, squeezed to make room for the ever present search button".
  - In Health, the tab bar collapses when search expands.
  - Safari's address is truncated, and tabs are hidden behind an overflow menu.
  - Touch-target spacing is below "at least 0.4cm between targets (and 1cm × 1cm tap areas)". The article doesn't cite a source for these figures.
  - **The review names no benefits.** A one-sided expert review is B-grade at best for these specific claims.
- **Apple's response:** iOS 26.1 (2025-11) added a Clear/Tinted switch under Settings › Display & Brightness › Liquid Glass. Tinted raises opacity and contrast [press: MacRumors, 2025-11-04]. This is separate from the older Reduce Transparency accessibility setting (MacRumors doesn't link the two, and I didn't verify how they interact).
- **Apple Maps (iOS 6, 2012):** Apple replaced Google data with its own. After widespread errors, Tim Cook wrote, "We fell short on this commitment… We are extremely sorry," and pointed users to Bing, MapQuest, Waze, Google and Nokia maps. He also said, "The more our customers use our Maps the better it will get" [press: TechCrunch, 2012-09-28]. The lesson: for a map, **data quality is the user experience**. Interface polish could not offset wrong data.
- **Accessibility:** Apple's platform accessibility features are widely praised, but I did not find an audit of specific first-party apps. **Not assessed.**
- **Performance:** not assessed.
- **Business context:** platform differentiation and cross-device coherence (the same material across iOS, iPadOS, macOS, watchOS and tvOS) justify a system-wide visual change. Defaults and market position mean users can't easily opt out of the system UI.
- **Principles demonstrated:** (Maps) own the data before the interface; (26.1) add a control after backlash.
- **Principles violated:** contrast and legibility (by NN/g's account); stable navigation (collapsing tab bars).
- **Tradeoffs:** a distinctive, brand-defining material against legibility on unpredictable backgrounds; cross-platform consistency against per-platform fitness.
- **Evidence:** first-party press releases, one expert review, press.

## 11. Zerodha Kite (India; web and mobile trading)

- **Context:** India's large discount broker. Kite is its trading platform.
- **Users / expertise:** mixed, from first-time investors to active F&O (futures and options) traders.
- **Primary tasks:** place orders, watch positions, manage risk.
- **Strengths:**
  - A reputation for a minimal, fast UI (widely asserted by users and press; **no measurement found**).
  - More distinctive is **"Nudges": warnings built into the order flow.** Examples include illiquid or dubious stocks, portfolio concentration (an alert when one stock or sector exceeds 50%), ETFs trading away from iNAV, and orders that exceed freeze limits [first-party Z-Connect, search summaries and support pages].
  - **Kill Switch** (2021-06-09) lets a trader disable a segment for **12 hours**. All positions must be closed first, to prevent impulsive re-entry. Kamath's rationale: "The trading frequency is usually inversely proportional to profitability for most traders" [first-party, read directly].
- **Context that makes this matter:** SEBI's updated study (2024-09) found 93% of individual equity F&O traders lost money between FY22 and FY24, with aggregate losses above ₹1.8 lakh crore [regulator press release, seen via search summary].
- **Weaknesses / tension:** a broker earns per order, so nudges that reduce trading work against its revenue. Kamath has said publicly, "Incentives are often skewed toward doing what's good for the business and not for the customer," and claims Zerodha has avoided dark patterns [press: Storyboard18, 2025-07]. The article gives no concrete examples, so **the claim is self-reported.**
- **Rule-out:** Zerodha's growth is widely attributed to price (zero-brokerage equity delivery) and to its educational content (Varsity). Design is secondary. Not quantified here.
- **Accessibility / Performance:** not assessed.
- **Principles demonstrated:** protective friction chosen by the user; warnings placed at the moment of decision rather than in a help page.
- **Tradeoffs:** revenue per trade against customer survival and long-term trust.
- **Evidence:** first-party posts, regulator data, press interview.

---

# Short entries

**CRED (India; credit-card bill payments and rewards).** It demonstrates *brand-led visual design as a product strategy*. CRED moved from a neumorphic system ("Synthour") to **NeoPOP** (open-sourced 2022), described as its fourth design system, and framed design as something that should "inspire creativity, bring out emotions and delight" [press: Analytics India Magazine, 2022-07-15, quoting a CRED engineer]. Neumorphism's low-contrast soft shadows are commonly criticised for accessibility. The shift to a high-contrast style is consistent with that, but I found no CRED statement of the reason. Weakness: users report confusion as the app expanded into loans, BNPL, rent and P2P lending [search summaries of user reviews; C]. Rule-out: the rewards economics and a curated high-credit-score member base, not the visuals, are the plausible engine. **Evidence thin. No usability data found.**

**Zepto (India; quick commerce).** A negative example from a design-praised startup. Users itemised fees added late in checkout ("rain fee", "cash handling fee", "small cart fee", "processing fee") [search summaries]. The CCPA fined Zepto ₹7 lakh for **drip pricing and basket sneaking** (showing lower prices, then adding handling charges and membership fees). The action was announced 2026-08-05; Zepto has discontinued the practice and is appealing [press: Free Press Journal, 2026-08-05]. The CEO reportedly called it "a mistake… We killed it" [search summary; the source pages returned 403]. Context: the ASCI Academy + Parallel study of **12,000+ screens from 53 top Indian apps** found deceptive patterns in 52 of them. That is an average of 2.7 per app, with "basket sneaking" common in delivery apps [press: Campaign India, 2024]. Method: expert screen review against a 12-pattern taxonomy. No apps were named. India's Department of Consumer Affairs guidelines (2023-11) list 13 dark patterns.

**Razorpay Magic Checkout (India; payments).** Useful mainly as a **warning about vendor statistics**. A Razorpay case study (2022-04-29) claims one merchant's conversion "doubled in one month" and "cart abandonment rate was reduced by 100%", with no baseline and no method [first-party, read]. A 100% reduction means zero abandonment, which isn't plausible. Treat the whole genre of vendor case studies as D-grade unless a method is published. The design mechanism (prefilled address and contact details across merchants, a network-wide saved identity) is plausible. But it is a *network effect* (it works because Razorpay has seen the shopper before), not a screen design.

**Groww (India; investing for first-time investors).** Frequently cited for plain language and for filtering mutual funds by risk, goal and horizon. **I found only student case studies and marketing blogs, with no first-party design writing and no data.** Listed here so the final author knows the evidence gap. Not graded.

**Arc (The Browser Company; desktop browser).** Beloved by designers and one of the most instructive failures here. The team's own letter (2025-05-26) says that "for most people, Arc was simply too different, with too many new things to learn, for too little reward," and that it "lacked cohesion". It also gives rare usage data: "Only 5.52% of DAUs use more than one Space regularly. Only 4.17% use Live Folders", and 0.4% use Calendar Preview on Hover. They contrast this with Dia features used by 40% and 37% of DAUs. D1 retention was strong among those who stayed ("fanatics") [first-party letter, read]. Caveat: the letter also argues for the company's pivot to AI, so it has a reason to frame Arc as a dead end. The numbers are self-reported.

**Superhuman (email; desktop first).** Demonstrates *speed as the product* and *narrow targeting*. First Round Review (Vohra interview) reports targets of 100 ms UI response, later under 50 ms, with keyboard-first design. It also reports deliberately serving "high-expectation customers". The "very disappointed" product-market-fit score went from 22% to 33% after segmentation, and to 58% after three quarters [interview, read]. Early users got a 1:1 onboarding session [search summary]. That is the human cost of an expert interface. Where it fails: price, and learnability for people who won't invest the effort. Mobile turned out to be critical, contrary to the team's first bet.

**Things 3 (Cultured Code; Apple platforms).** Won Apple Design Awards in 2009 and 2017, and is sold as separate paid apps per platform [Wikipedia]. It demonstrates that a small, opinionated feature set can win a reputation for elegance. Where it fails: no collaboration and Apple-only. It suits people who work alone, not teams. **No usability data. The award is reputation only.**

**The Last of Us Part II (PlayStation, 2020; game).** More than 60 accessibility settings. A blind reviewer (Can I Play That?, 2020-06-18) wrote, "I can play this game without needing sighted assistance". The mechanisms were text-to-speech menus, audio cues with an in-game glossary, enhanced listen mode, navigation assistance, and audio-guided aim. Noted limits: the audio-cue glossary is a single long list; there is no audio description of cutscenes; and **TTS is off at first launch**, so the first step still needs help [user review by a blind player, read]. Lesson for apps: accessibility as a *set of composable assists* rather than a single "accessible mode".

**Celeste (indie platformer, 2018).** Assist Mode (game speed, invincibility, infinite stamina, chapter skip) was first called "Cheat Mode". The creator renamed it because the name felt "judgmental". In 2019 the text changed from "We believe that its difficulty is essential to the experience" to "Celeste is intended to be a challenging and rewarding experience". The change followed feedback from speedrunner Clint "Halfcoordinated" Lexa, who has hemiparesis, and narrative designer Kathy Jones. Thorson: "our original text was unintentionally undermining that purpose" [press: Vice, 2019-09-16]. Lesson: **the words around an accommodation decide whether people use it.**

**GOV.UK "one thing per page" (public service).** Pattern guidance by Tim Paul (2015-07-03). Claimed benefits: "low-confidence users find them easier to use", it works on mobile, and it handles branching, errors and saving better [first-party blog, read]. **The research is asserted but not published** (a GDS commenter says Register to Vote and Verify researched it "in great depth"). Commenters list limits: complex branching, gathering documents for long forms like tax returns, and progress indicators when the length is unpredictable. Evidence C. It is a context-dependent heuristic for infrequent, high-stakes forms. It is not a rule for expert, repeated data entry.

---

# Cross-product findings

Each finding: claim, evidence, context, counterevidence, example, labels (kind of claim; evidence A–D), implication.

### F1. Perceived performance and perceived correctness, not the technical measure, are what users experience

- **Claim:** users judge speed by when the *visible, useful* part is ready, and judge randomness and correctness by whether it matches their mental model. Products that optimise the technical metric instead can be objectively better and still feel worse.
- **Evidence:**
  - Pinterest replaced full-page-load time with "user perceived wait time" because load time "doesn't reflect performance" that matters to users. Its gains in wait time came with gains in signups and SEO (first-party, 2017).
  - Spotify: "statistical randomness doesn't always translate into perceived randomness" (first-party, 2025).
  - GitHub measures "highest priority content" and defines tiers at 200 ms and 1 s (first-party, 2026).
  - Superhuman targets 100 ms, then 50 ms (interview).
- **Context:** consumer and pro tools alike; strongest when feedback is repeated many times a day.
- **Counterevidence:** GitHub accepted ~4.7% stale data to feel faster. Perceived speed can be bought with correctness, which is dangerous where staleness matters (finance, health). The 100 ms figure traces to older response-time research (Miller 1968; Card, Moran & Newell). I did not re-read those sources here.
- **Example:** Pinterest UPWT; Spotify "Fewer Repeats".
- **Labels:** Strong heuristic; **B** (several independent first-party measurements, consistent with older HCI response-time work, but no independent replication in these notes).
- **Implication:** define the metric from what the user sees (first meaningful content, perceived fairness), instrument it, and state openly what correctness you trade for it.

### F2. The best-regarded "invisible" designs piggyback on a mental model the user already has; novelty carries a learning tax that must be repaid by the product

- **Claim:** interfaces praised as simple often introduce *no new concept* (Dropbox = a folder; Canva = pick the thing you need to make; Figma = a familiar vector editor where only collaboration is new). Products that ask users to learn several new concepts at once lose most users, even when experts love them.
- **Evidence:**
  - Arc's own data: 5.52% of DAUs use multiple Spaces, 4.17% Live Folders, 0.4% Calendar Preview. "Too many new things to learn, for too little reward" (first-party, 2025).
  - Dropbox's founder argued against the "you can build this with FTP + SVN" critique on exactly these grounds (HN, 2007).
  - NN/g says Liquid Glass "makes users relearn basics" (expert review, 2025).
- **Context:** consumer and cross-audience tools. Experts can amortise learning (Superhuman users, GitHub shortcuts).
- **Counterevidence:**
  - Superhuman and GitHub succeed with learned, keyboard-heavy models, but they target experts, and Superhuman paid for 1:1 onboarding.
  - The Arc letter is also a pivot justification, so its framing may be self-serving.
  - Feature-usage percentages are normal for power features in many products. Low use doesn't prove a feature fails the users who rely on it.
- **Example:** Dropbox (success), Arc (failure), Superhuman (success with a paid-for learning curve).
- **Labels:** Context-dependent heuristic; **C** (single-company data plus expert opinion, consistent in direction).
- **Implication:** count the new concepts in a design. For each one, name the reward and who gets it. If the audience is broad, keep the number of new concepts near one. If it is expert, fund the teaching (onboarding sessions, a command palette, progressive shortcuts).

### F3. For many praised products the growth loop is built into the core object; credit design only for what the loop doesn't explain

- **Claim:** Figma links, Canva template pages, Pinterest landing pages and Dropbox shared folders and referrals are all the product *and* its distribution. Much of the success that gets attributed to "great design" is the loop.
- **Evidence:** Kwok: "The core of Figma's product *is* the core of its distribution loop" (essay). Dropbox: paid search failed ($233–388 CPA on a $99 product), and referrals raised signups 60% (founder slides). Canva template pages double as SEO (practitioner newsletter). Pinterest's signup gains came from logged-out landing pages (first-party).
- **Context:** multi-user, shareable-artefact products.
- **Counterevidence:** a loop only works if the thing shared is good enough to convert the recipient, so design quality and loop are intertwined, not rival explanations. Pinterest shows a loop can also generate hostility (the login wall, Chrome extension installs).
- **Example:** Figma vs Sketch; Dropbox 2008–2010.
- **Labels:** Strong heuristic (as a research method: "rule out the loop before crediting design"); **B** (several independent first-party data points and one respected analysis).
- **Implication:** when citing a product as a design benchmark, separate what the recipient of a shared link experiences (design) from why they received it (loop). Learn the recipient experience. Don't copy the loop and expect the same outcome.

### F4. When the primary surface starts serving the company's product portfolio, the core task degrades and users say so loudly

- **Claim:** home screens get repurposed to promote new business lines. Examples: Spotify's 2023 feed for podcasts and audiobooks; Netflix's 2025 homepage "flexible for our broad entertainment offerings" (live, games); Revolut's super-app products; CRED's lending; Dropbox's 2019 hub. This reliably draws backlash from the users of the core task.
- **Evidence:** Spotify 2023 press criticism ("too much at the same time"). Netflix 2025 user backlash (press) plus Netflix's own rationale naming breadth of offerings. Dropbox 2019 ("a folder that syncs perfectly"). Revolut and CRED: complaints about complexity (weak).
- **Context:** mature products expanding into adjacent markets.
- **Counterevidence:** backlash is not the same as outcome. None of these companies published engagement or retention data showing harm, and backlash to redesigns can fade. Netflix may well have data showing its redesign works. **This is the main open question in this finding.**
- **Example:** Spotify Home 2023.
- **Labels:** Context-dependent heuristic; **C** (press and user reports; no outcome data).
- **Implication:** give new business lines their own entry points, and keep the core task's shortest path untouched. If you must promote on the primary surface, keep an explicit route to the core task (Library, a pinned row), and measure time-to-core-task before and after.

### F5. Personalisation optimises a proxy; the proxy can misrepresent the product and weaken predictability

- **Claim:** per-user ranking and imagery raise the metric they target (plays, clicks) but can mislead (artwork that overstates a minor character) and make the interface unpredictable (two users can't describe "the same" screen). User-controlled personalisation (Revolut's configurable navigation) avoids some of this.
- **Evidence:** Netflix's artwork system and the 2018 race controversy, plus Netflix's statement that only viewing history is used. The 80%-of-hours figure shows how central recommendations are (paper, seen quoted). Autoplay previews made optional after complaints (2020).
- **Context:** content catalogues and feeds.
- **Counterevidence:** Netflix reports large business value from personalisation (quoted). Users may prefer personalised homes overall. The 2018 case reached the press through a handful of users; its prevalence is unknown.
- **Example:** Netflix artwork; Spotify Home previews.
- **Labels:** Useful pattern (personalised decision support) *with* a documented failure mode; **C**.
- **Implication:** constrain personalised assets so they must truthfully represent the item (for example, artwork must show leads or core themes); give users a way to turn off attention-grabbing automation; prefer personalisation users can see and control where predictability matters.

### F6. Protective friction, chosen by the user and placed at the moment of decision, is a recurring pattern in products with a conscience

- **Claim:** well-regarded products add deliberate friction where the user's *future self* would want it. Examples: Monzo's gambling block with a chosen cooldown and a self-written note; Zerodha's 12-hour Kill Switch that requires positions closed first, plus order-window nudges; Celeste's assist options framed without judgement.
- **Evidence:** Monzo reports ~100,000 users in 10 months and 200,000+ blocked attempts (first-party). Zerodha documents the mechanism and rationale (first-party). SEBI's 93% F&O loss figure (regulator) shows the stakes.
- **Context:** money, gambling, trading, and other domains where impulses cause harm.
- **Counterevidence:**
  - **No outcome data**: neither company reports reduced harm, only usage.
  - Friction imposed *by the business* (Spotify's free-tier shuffle-only, Pinterest's login wall) is the same mechanism pointed the other way.
  - Friction for users who didn't opt in can be paternalistic.
- **Example:** Monzo gambling block; Zerodha Kill Switch.
- **Labels:** Useful pattern; **C** (first-party usage figures, no independent outcome studies found).
- **Implication:** when adding friction, ask whose goal it serves. Protective friction should be opt-in or clearly justified, reversible after a delay the user chooses, and it should show the user's own stated reason back to them.

### F7. Rich, canvas-based or client-rendered apps start with an accessibility and platform-convention deficit that must be paid back deliberately

- **Claim:** moving from documents to apps (canvas rendering, virtualisation, client-side routing) removes behaviour the browser gave for free: find, focus, back button, and the accessibility tree. The praised products fixed this only with explicit engineering.
- **Evidence:**
  - Figma's Mirror DOM ("strips away any accessibility the browser gives you for free", first-party 2026).
  - GitHub's hidden-textarea fix for Ctrl+F because users "think of GitHub as a page" (first-party 2023).
  - Canva's 2021 ACR marking canvas elements not keyboard accessible (audit).
  - GitHub's 2026 ACR still listing dozens of high and medium keyboard, focus and status-message issues (audit).
  - User reports of broken back navigation on GitHub.
- **Context:** web apps with custom rendering.
- **Counterevidence:** these same architectures enabled the praised features (Figma multiplayer at 60 fps, GitHub's code navigation). The deficit is a cost, not proof that the architecture is wrong. Audits are self-published, and their completeness varies.
- **Example:** Figma, GitHub, Canva.
- **Labels:** Strong heuristic; **B** (several independent first-party engineering accounts plus two published audits; the direction is consistent).
- **Implication:** before choosing canvas or virtualised rendering, list the native behaviours you will lose (find, selection, focus order, the accessibility tree, history), and budget to rebuild each one. Test with native browser features and assistive technology, not only with your own replacements.

### F8. Beauty and awards predict reputation, not usability; the aesthetic-usability link is real but conditional and can reverse

- **Claim:** "Beautiful interfaces are perceived as more usable" is not a dependable law.
- **Evidence:**
  - Kurosu & Kashimura (1995; 252 participants, 26 ATM layouts) found perceived ease correlated with aesthetics more than with actual ease [seen via NN/g, 2024].
  - Tuch et al. (2012, *Computers in Human Behavior* 28(5), n=80, manipulated both aesthetics and usability of an online shop): "aesthetics does not affect perceived usability. In contrast, usability has an effect on post-use perceived aesthetics". The frustration of poor usability *lowered* beauty ratings [read directly].
  - Sonderegger et al. (2012, *Ergonomics*, 2-week longitudinal field study) reportedly found aesthetic effects wane with exposure [search summary only].
  - NN/g (2024) itself limits the effect to *minor* issues, and warns that it masks problems in testing.
- **Context:** first impressions and short tests (where the effect is strongest) against sustained use (where it is weakest).
- **Counterevidence:** several studies do find the effect. Conflicting operationalisations of "aesthetics" and "usability" explain part of the disagreement (noted by Tuch et al.).
- **Product example:** Liquid Glass shows a visually ambitious change criticised on legibility, and followed within months by a Tinted switch. CRED moved away from neumorphism. Things 3's awards come with no usability data.
- **Labels:** "Beauty → perceived usability" as a general rule: Context-dependent heuristic; **B** (multiple studies, mixed results). "An award signals usability": Unsupported or weak claim; **D**.
- **Implication:** evaluate beauty and usability separately. In usability tests of polished prototypes, use task success and errors, not ratings alone. Don't use awards as usability evidence.

### F9. Mature products increasingly resolve backlash by adding an escape hatch rather than reverting

- **Claim:** after complaints, praised products tend to keep the new default and add a setting. Examples: Netflix's autoplay-previews toggle (2020), iOS 26.1 Clear/Tinted (2025), Spotify's Standard Shuffle kept alongside "Fewer Repeats" (2025), Revolut's configurable navigation (2023).
- **Evidence:** first-party help and press documentation of each.
- **Context:** large user bases with diverse preferences.
- **Counterevidence:** settings are discovered by a minority of users, so a default decides what most people experience. A toggle can be a way to preserve a business-preferred default while quieting critics. No product published how many users flipped the setting.
- **Example:** Netflix 2020; iOS 26.1.
- **Labels:** Design convention (emerging); **C**.
- **Implication:** an escape hatch is not a fix for a bad default. If complaints concentrate on legibility or control, which have accessibility consequences, fix the default. Use settings for genuine preference splits.

### F10. Put the user's real situation into the interface: examples, previews and warnings built from their own data

- **Claim:** among the most-praised patterns in developer tools and finance, several work by replacing generic content with the user's own context. Stripe injects the user's test keys and account-specific content into docs. Zerodha nudges on the user's actual order or portfolio (concentration over 50%). Monzo shows the user their own note.
- **Evidence:** first-party mechanism descriptions (Stripe 2022, Zerodha, Monzo 2023). **No outcome metrics were published** for any of them.
- **Context:** tasks where a mismatch between the example and the user's case causes errors.
- **Counterevidence:** personalised content raises privacy and correctness stakes (showing the wrong account's data would be severe). Stripe had to restrict its authoring language to keep this maintainable.
- **Example:** Stripe docs.
- **Labels:** Useful pattern; **C**.
- **Implication:** where users copy, compare or decide, show their own values. Keep generic examples for logged-out users. Treat the personalisation logic as a correctness-critical system.

### Anti-pattern noted across products: statistics without method

Many of the most-quoted "design results" have no traceable method. Examples: Netflix's 82% focus on artwork and 1.8 seconds per title (no sample stated); Canva's "around 10%" typical activation lift (from a vendor selling the tool); Razorpay's "cart abandonment reduced by 100%"; consultancy claims of "2,018 Reddit threads analysed" about Stripe. **Labels:** Unsupported or weak claim; **D**. **Implication:** the final output should not repeat these numbers as findings. Where one is used, give it with its source type and the missing method.

### Tensions seen across products (no universal answer)

- **Distribution against goodwill:** Pinterest's login wall and Dropbox's visible app. The growth surface and the user's task compete.
- **Development velocity against native behaviour:** GitHub on React, Dropbox on Electron. Faster team iteration, at the cost of speed and platform conventions for users.
- **Portfolio against focus:** Spotify, Netflix, Revolut and CRED.
- **Protective against commercial friction:** the same mechanism serves opposite interests (Monzo and Zerodha against Spotify's free tier).
- **Expressive visuals against legibility:** Liquid Glass and neumorphism against Stripe's contrast-first colour system.
- **Breadth of catalogue against depth per item:** Netflix's tile size.

### Open questions (evidence missing)

1. Do redesign backlashes (Spotify 2023, Netflix 2025) show up in retention or engagement? No company published data.
2. What is the actual effect of protective friction (Monzo, Zerodha) on harm, not just usage?
3. Did Spotify's shuffle revert to pure random between 2014 and 2020? The first-party posts conflict.
4. How accessible are Canva and Figma today? The only audit found (Canva) dates from 2021. Figma has no third-party audit.
5. How much of Revolut's, Zerodha's and CRED's adoption is price or rewards rather than design? No primary data found.
6. The Netflix 80% figure and the Pinterest 40/15/15 figures are widely repeated. I saw them only via summaries, and the final author should check the originals before relying on them.

---

# Outside my area

- **Regulation of dark patterns in India** (CCPA 2023 guidelines listing 13 patterns; the 2026-08 fines on Zepto, IndiGo, BookMyShow, FirstCry, PharmaEasy, Physics Wallah and others; the ASCI Conscious Patterns study). This probably belongs to whoever covers ethics and dark patterns. The details are in the Zepto entry and `sources.md`.
- **Aesthetic-usability research** (Kurosu & Kashimura 1995; Tuch et al. 2012; Sonderegger et al. 2012) belongs to the principles/counterexamples area. I recorded it in F8 because it bears directly on "award-winning ≠ effective".
- **GOV.UK "one thing per page"** probably belongs to the public-service/accessibility researcher. The short entry notes that its evidence is asserted but not published.
- **Game accessibility** (The Last of Us Part II, Celeste) is also relevant to the accessibility area.
