# Area 5 sources

All sources were read on 2026-09-26.

Count by type (56 numbered sources, plus the items listed after them):

- Browser-support data and platform documentation: 12
- Design systems, specifications and guidelines from organizations: 4
- Books by practitioners: 3 (1 read in part, 2 only as quoted by others)
- Research papers: 6 (2 of them 2026 preprints)
- Practitioner writing (articles, blog posts, talks, posts by designers and engineers): 31
- Supporting items not counted above: 4 (Minto, CUBE CSS, Zen Garden page, Tailwind PR)
- Community discussion: 1
- Real products observed directly: 8 production sites' CSS, 1 site's markup, 2 sites screenshotted, plus 1 test page of my own

"How much read" uses the brief's terms: full text, abstract, or quoted in another source. "Queried" means I downloaded a dataset and ran my own queries on it.

## Browser-support data and platform documentation

1. WebDX Community Group, `web-features` npm package v3.40.0, `data.json`. Published 2026-09-24. https://cdn.jsdelivr.net/npm/web-features/data.json. Queried: Baseline status, dates and per-browser versions for about 120 features.
2. Alexis Deveria and contributors, caniuse `fulldata-json/data-2.0.json`. Updated 2026-09-24. https://raw.githubusercontent.com/Fyrd/caniuse/main/fulldata-json/data-2.0.json. Queried: global usage % and support notes for about 30 features.
3. web.dev / WebDX CG, "Baseline". Undated page. https://web.dev/baseline. Full text.
4. MDN, "CSS container queries". Last modified 2026-07-08. https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries. Full text.
5. MDN, "Using CSS containment". https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using. Full text (sections on size containment).
6. MDN, "@layer". Last modified 2026-04-20. https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer. Full text.
7. MDN, "text-wrap". Last modified 2026-08-27. https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap. Full text.
8. MDN, "light-dark()". Last modified 2026-04-18. https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark. Full text.
9. MDN, "Using CSS nesting". Last modified 2026-06-16. https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/Using. Full text.
10. MDN, "Using CSS custom properties (variables)". Last modified 2026-08-27. https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties. Full text.
11. MDN, "@supports". Last modified 2026-09-14. https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports. Full text.
12. Tailwind Labs, "Play CDN" installation docs. Undated. https://tailwindcss.com/docs/installation/play-cdn. Full text.

## Design systems, specifications and guidelines

13. Design Tokens Community Group, "Design Tokens Format Module 2025.10". Draft report dated 2026-09-08. https://www.designtokens.org/TR/drafts/format/. Read the definitions, alias and type sections, not the whole spec.
14. Design Tokens Community Group, designtokens.org home page, announcing the first stable version on 2025-10-28. https://www.designtokens.org/. Full text.
15. GitHub Primer, "Token names". Undated. https://primer.style/product/primitives/token-names/. Full text.
16. Salesforce, "What Are Styling Hooks?". 2025-01-23. https://www.salesforce.com/blog/what-are-styling-hooks/. Full text.

## Books by practitioners

17. Heydon Pickering & Andy Bell, *Every Layout*, 3rd edition (edition date not stated on the site). https://every-layout.dev/. Full text of the free chapters: Boxes, Composition, Units, Global and local styling, Modular scale, Axioms, and the home page. The layout chapters are paywalled and not read.
18. Adam Wathan & Steve Schoger, *Refactoring UI* (2018). Not read. Quoted in another source: book notes and summaries found by search (maibuith.com, iamaatoh.com and others) for the claim that ratio-based scales give fractional and too-sparse sizes.
19. Robert Bringhurst, *The Elements of Typographic Style*. Not read. Quoted in another source: Tim Brown (item 38) for the modular scale quote, and *Every Layout* Axioms for the 45 to 75 character measure.

## Research papers

20. Stephanie Houde & Charles Hill, "What Do Prototypes Prototype?", in *Handbook of Human-Computer Interaction* (2nd ed.), 1997. https://hci.stanford.edu/courses/cs247/2012/readings/WhatDoPrototypesPrototype.pdf. Full text (10 pp.).
21. Youn-kyung Lim, Erik Stolterman & Josh Tenenberg, "The anatomy of prototypes", *ACM TOCHI* 15(2), 2008. https://dl.acm.org/doi/10.1145/1375761.1375762. Quoted in another source: review at https://ezaex.com/posts/papers/the-anatomy-of-prototypes/.
22. Brad Myers, Sun Young Park, Yoko Nakano, Greg Mueller & Amy J. Ko, "How Designers Design and Program Interactive Behaviors", IEEE VL/HCC 2008. https://faculty.washington.edu/ajko/papers/Myers2008InteractiveBehaviors.pdf. Full text (abstract, results and implications read closely).
23. Björn Hartmann, Loren Yu, Abel Allison, Yeonsoo Yang & Scott Klemmer, "Design as Exploration: Creating Interface Alternatives through Parallel Authoring and Runtime Tuning", UIST 2008. https://dl.acm.org/doi/10.1145/1449715.1449732. Abstract, via search results.
24. Kashif Imteyaz, Kaif Imteyaz, Nakul Rajpal, Kaif Shaikh, Michael Muller & Saiph Savage, "Design Theater: Evaluating the Gap Between User-Facing Design Reasoning and Implementation in Generative UI Tools", arXiv preprint, submitted 2026-07-24, revised 2026-07-31. https://arxiv.org/abs/2607.22928. Abstract plus the method, results and limitations sections of the HTML version. Not peer reviewed.
25. Yifan Zhang, Nghi D. Q. Bui, Georgios Evangelopoulos & Arnaud Benard, "Enabling Creative Exploration for Vibe Design Agents", arXiv preprint, submitted 2026-09-14. https://arxiv.org/abs/2609.15078. Abstract plus the results and limitations sections of the HTML version. Not peer reviewed.

## Practitioner writing

26. Heydon Pickering, "The Flexbox Holy Albatross". 2019-01-13. https://heydonworks.com/article/the-flexbox-holy-albatross/. Full text.
27. Ethan Marcotte, "Responsive Web Design", A List Apart. 2010-05-25. https://alistapart.com/article/responsive-web-design/. Full text.
28. Jen Simmons, interview transcript, "Intrinsic Web Design", The Big Web Show (Zeldman). Published 2018-05-02. https://zeldman.com/2018/05/02/transcript-intrinsic-web-design-with-jen-simmons-the-big-web-show/. Full text.
29. Stephen Hay, "Some thoughts on 'designing in the browser'". 2014-12-23. https://www.the-haystack.com/2014/12/23/some-thoughts-on-designing-in-the-browser/. Full text.
30. Brad Frost, post on X quoting Stephen Hay at BDConf. 2012-04-16 (date decoded from the post ID). https://twitter.com/brad_frost/status/191977076000161793. Quoted in another source: the post text appeared in search results. I did not open X.
31. James Weiner, "Throw away Photoshop and be true to your medium", GDS blog. 2012-03-29. https://gds.blog.gov.uk/2012/03/29/breaking-down-walls-designing-in-browser/. Full text.
32. Andy Budd, "Designing in the Browser is Not the Answer". 2012-03-14. https://www.andybudd.com/archives/2012/03/designing_in_the_browser_is_not_the_answ. Full text.
33. Sarah Parmenter, "I Can't Design in the Browser". 2012-02-21. https://www.sazzy.co.uk/why-i-cant-design-in-the-browser. Full text.
34. Dan Mall, "Reading Is Fundamental: Element Collages". 2012-11-13. https://v3.danmall.com/articles/rif-element-collages/. Full text.
35. Frank Chimero, "The Web's Grain". 2015. https://frankchimero.com/blog/2015/the-webs-grain/. Full text (quotes checked against the raw page).
36. Rauno Freiberg, "Invisible Details of Interaction Design". 2023 (July, per the page). https://rauno.me/craft/interaction-design. Full text.
37. Boris Müller, "Why Do All Websites Look the Same?", Medium. Featured 2018-10-30. https://borism.medium.com/on-the-visual-weariness-of-the-web-8af1c969ce73. Full text through a mirror (readmedium.com), because Medium returned 403.
38. Tim Brown, "More Meaningful Typography", A List Apart. 2011-05-03. https://alistapart.com/article/more-meaningful-typography/. Full text.
39. James Gilyead (with Trys Mudford), "Designing with fluid type scales", Utopia. 2020-02-01. https://utopia.fyi/blog/designing-with-fluid-type-scales/. Full text.
40. James Gilyead & Trys Mudford, "CSS-only fluid modular type scales", Utopia. 2020-02-02. https://utopia.fyi/blog/css-modular-scales/. Full text.
41. Mike Riethmuller, "Precise control over responsive typography". 2015-03-17. https://www.madebymike.com.au/writing/precise-control-responsive-typography/. Full text.
42. Maxwell Barvian, "Addressing Accessibility Concerns With Using Fluid Type", Smashing Magazine. 2023-11-07. https://www.smashingmagazine.com/2023/11/addressing-accessibility-concerns-fluid-type/. Full text.
43. Nathan Curtis, "Naming Tokens in Design Systems", EightShapes. 2020-10-15. https://nathanacurtis.substack.com/p/naming-tokens-in-design-systems-9e86c7444676. Full text.
44. Nathan Curtis, "Space in Design Systems", EightShapes. 2016-09-25. https://nathanacurtis.substack.com/p/space-in-design-systems-188bcbae0d62. Full text.
45. Robin Rendle, "What Are Design Tokens?", CSS-Tricks. 2019-04-03. https://css-tricks.com/what-are-design-tokens/. Full text.
46. Donnie D'Amato, "Avoiding tokens". 2025-02-24. https://blog.damato.design/posts/avoiding-tokens/. Full text. It quotes Salesforce's Alan Weibel from the Design Systems Slack and LinkedIn, which I did not open.
47. Adam Wathan, "CSS Utility Classes and 'Separation of Concerns'". 2017-08-07. https://adamwathan.me/css-utility-classes-and-separation-of-concerns/. Full text.
48. Adam Wathan, post on X about `bg-indigo-500`. 2025-08-07 (date decoded from the post ID). https://x.com/adamwathan/status/1953510802159219096. Quoted in another source: the post text appeared as the search-result title. I did not open X.
49. Patrick Brosset, "Perfecting Baseline", Piccalilli. 2025-11-13. https://piccalil.li/blog/perfecting-baseline/. Full text.
50. Andrey Sitnik & Travis Turner, "OKLCH in CSS: why we moved from RGB and HSL", Evil Martians. Page metadata `datePublished` 2025-09-17; I found no earlier date on the page. https://evilmartians.com/chronicles/oklch-in-css-why-quit-rgb-hsl. Full text.
51. Björn Ottosson, "A perceptual color space for image processing" (Oklab). 2020-12-23. https://bottosson.github.io/posts/oklab/. Full text.
52. Björn Ottosson, "Two new color spaces for color picking – Okhsv and Okhsl". 2021-09-08. https://bottosson.github.io/posts/colorpicker/. Read the sections on lightness and on HSL distortion.
53. Spec (spec.fm), "The 8-Point Grid". Undated, no author shown. https://spec.fm/specifics/8-pt-grid. Full text.
54. Dan Klammer, "Modern Font Stacks". Undated. https://modernfontstacks.com/. Full text.
55. Victor Ayomipo, "Stop Treating CSS Container Queries Like Traditional Media Queries", Smashing Magazine. 2026-09-16. https://www.smashingmagazine.com/2026/09/stop-treating-css-container-queries-traditional-media-queries/. Full text.
56. Alastair Campbell, "Pixels vs Ems commentary". 2018-08. https://alastairc.uk/2018/08/pixels-vs-ems-commentary/. Full text.

Also used, but not counted separately:

- Evan Minto, "Pixels vs. Ems: Users DO Change Font Size", Medium, 2018. https://medium.com/@vamptvo/pixels-vs-ems-users-do-change-font-size-5cfb20831773. Quoted in another source: cited by *Every Layout* Units and Campbell, and the 3.08% figure came from search snippets. Not read.
- Andy Bell, CUBE CSS. https://cube.fyi/. Undated. Home page read in full.
- Dave Shea, CSS Zen Garden project page. https://daveshea.com/projects/zen/. Full text. The launch date of 2003-05-08 comes from search results (Wikipedia and Web Design Museum), not from Shea's page.
- Tailwind CSS PR #20318, "Fix weird character rendering on Windows with Japanese locale". Created 2026-07-09, merged 2026-07-14 (checked with the GitHub API). https://github.com/tailwindlabs/tailwindcss/pull/20318. Full text.

## Community discussion

- Hacker News thread on Müller's essay. 2018. https://news.ycombinator.com/item?id=18414001. Top comments read. Anecdotal.

## Real products observed directly (2026-09-26)

- Served CSS of www.gov.uk, github.com, stripe.com, linear.app, utopia.fyi, every-layout.dev, www.bbc.co.uk and vercel.com. I fetched each home page with a script, pulled its linked and inline stylesheets (up to 25 per page), and counted distinct custom properties, `@layer`, `@container`, `:has(`, `clamp(`, `oklch(`, `color-mix(`, `@property`, and `px` and `rem` values. The files are minified, and only home-page CSS was sampled, so the counts show presence, not totals across each product.
- CSS Zen Garden markup (https://www.csszengarden.com/): six empty `extra1`–`extra6` presentational divs.
- Screenshots, taken with headless Firefox 156.0.1, in `code-shots/`:
  - `utopia-fyi-2026-09-26-390w.png` and `utopia-fyi-2026-09-26-1440w.png`: the same page at two widths, showing fluid type.
  - `every-layout-2026-09-26-390w.png` and `every-layout-2026-09-26-1440w.png`.
  - `own-test-page-firefox156-2026-09-26-{420,900,1500}w.png`: my own single-file test page. It uses `@layer`, a `pow()` scale, `clamp()` type, `oklch()` relative color, `light-dark()`, a Switcher, per-card container queries, `:has()` and `text-wrap: balance`. It shows the container-query inversion described in F5.

## Searched but not used as evidence

- Community posts on "token bloat" (uxplanet, designtokens.substack, dev.to), used only to find disagreements. Weak, and not cited.
- AI-design listicles on the "purple gradient" look (dev.to, 925studios and others), used only to find Wathan's post.
- The "2,300+ unique viewport sizes" claim in Ayomipo (2026). Its origin is untraced, so I did not use it.
