# Area 5: From direction to code

Scope: how a design direction becomes a working prototype in one HTML file with no build step. Tokens, type and spacing scales, responsive layout, current CSS, and what designers gain or lose when they design in code.

All browser-support statements are dated 2026-09-26. They come from two datasets that I downloaded and queried directly: the WebDX `web-features` package v3.40.0 (published 2026-09-24), and the caniuse `data-2.0.json` (updated 2026-09-24). Where they disagree, I say so.

Coverage check:

- MDN: used for mechanism and caveats of each feature (container queries, containment, `@layer`, nesting, custom properties, `light-dark()`, `text-wrap`, `@supports`). Each page's last-modified date is in the sources file.
- caniuse: used as raw data, cross-checked against `web-features`.
- Pickering & Bell, *Every Layout*: I read the free "Rudiments" and "Axioms" chapters in full (Boxes, Composition, Units, Global and local styling, Modular scale, Axioms). The layout chapters (Stack, Switcher, and the rest) are behind a paywall. For the Switcher mechanism I used Pickering's own free article from 2019, which the chapter is based on.

Labels: kind of claim / evidence strength (A to D), as the brief defines them. "Stated" means the source says it. "Inferred" means I concluded it.

---

## F1. Decide on a CSS feature by its support tier and its failure mode, not by whether it is "modern"

Claim. Whether a feature belongs in a prototype depends on two things. The first is its interoperability tier. The second is what the page looks like when the feature is missing. CSS drops declarations it does not understand, so a missing feature can fail silently, which is safe. It can also fail structurally, which breaks the page.

Evidence.

- Baseline definitions (web.dev, stated). "Newly available" means supported in all core browsers: Chrome, Edge, Firefox and Safari, desktop and mobile. "Widely available" means 30 months have passed since then. The WebDX Community Group now defines Baseline. The Chrome team started it.
- My queries of both datasets, 2026-09-26, give three tiers.
  - Widely available (safe as the structure of a prototype): grid, flex `gap`, `clamp()`/`min()`/`max()` (since 2020-07), custom properties, `aspect-ratio`, logical properties, cascade layers (2022-03), size container queries (2023-02), `:has()` (2023-12), native nesting (2023-12), `oklch()`/`oklab()` and `color-mix()` (2023-05), subgrid (2023-09), `pow()` and the other exponential functions (2023-12), import maps, `system-ui`, `<dialog>`, small/large/dynamic viewport units, media-query range syntax.
  - Newly available (fine when the fallback is acceptable): `light-dark()` (2024-05), `text-wrap: balance` (2024-05), `@property` (2024-07; Firefox 128 was last), relative color syntax (2024-09), `@starting-style` and `transition-behavior` (2024-08), popover (2025-01), same-document view transitions (2025-10; Firefox 144), invoker commands (2025-12), anchor positioning core properties (2026-01; Firefox 147), `@scope` (2026-03), `contrast-color()` (2026-04), container style queries (2026-05; Firefox 151), `field-sizing` (2026-06), `sibling-index()`/`sibling-count()` (2026-08).
  - Limited (enhancement only): `text-wrap: pretty` (no Firefox), scroll-driven animations (no Firefox), cross-document view transitions (no Firefox), `text-box` trim (no Firefox), `if()`, `@function`, `interpolate-size`, `calc-size()` and customizable `<select>` (Chromium, plus Safari 27 for select), `initial-letter` and `corner-shape` (Chromium only), grid lanes, formerly called masonry (Safari 26.4 only).
- The datasets disagree on anchor positioning. `web-features` marks it "limited" because `position-visibility: anchor-valid/anchor-visible` exists only in Safari 27. caniuse marks it "partial" at 85.9% global usage, noting only that sub-feature (and, for Firefox, animating `anchor()`). Baseline fails a whole feature when any sub-feature fails (my reading of the data).
- MDN on `@supports` (stated): a browser "may parse a property but implement it only partially", so a feature query tests only basic support.

Counterevidence. Patrick Brosset of the WebDX group (Piccalilli, 2025-11-13) says Baseline ignores browsers outside the core set, does not reach old enough versions for some teams, says nothing about accessibility, and does not say when a newer feature is safe as an enhancement: "Please don't treat it as a checkbox." caniuse percentages are global averages.

Example. `text-wrap: balance` fails silently: the heading wraps normally. An anchored tooltip fails structurally: it lands in the wrong place. Use the first freely. Use the second only when the direction is about that interaction, and name the browser.

When to use. Before relying on any feature for layout. Not needed for decorative declarations that fail silently.

Labels: strong heuristic / A for the support facts (two independent datasets that agree, except as noted), B for the decision rule. Mechanism "CSS ignores unknown declarations" is stated in the CSS specs, via MDN. The rule "classify by failure mode" is inferred.

---

## F2. In a single file, design tokens are custom properties on `:root`, and the value of a tier is that it gives one place to swap

Claim. A token is a named design decision. In a no-build file the natural carrier is a CSS custom property. Tiers of tokens exist to create indirection. Components refer to a meaning (`--text-muted`), the meaning refers to a raw value (`--gray-6`), and a theme or a direction changes only the middle layer. That indirection is the whole benefit. Each tier you add costs lookup effort.

Evidence.

- DTCG Format Module (first stable version 2025.10, released 2025-10-28; draft read 2026-09-08). Definition: "information associated with a human readable name, at minimum a name/value pair". It supports aliases: "The same value can have multiple names." The spec defines no tiers.
- History. The term comes from Salesforce's Lightning Design System (Jina Anne and Jon Levine; Rendle, CSS-Tricks, 2019). Its purpose was to share one set of values across web, iOS and Android.
- Salesforce itself moved away from the term (stated in D'Amato, 2025-02-24, quoting Salesforce UX architect Alan Weibel). "Design tokens are very helpful for a lot of teams. They just aren't super helpful for Salesforce … 99% of Salesforce is on a single platform—the web." They "ended up using a web standard, CSS custom properties". Salesforce's own post (2025-01-23) defines a "styling hook" as "a CSS custom property".
- Nathan Curtis (2020-10-15) separates generic scale values (`$color-neutral-42`) from purposeful ones (`$color-feedback-error`). He advises keeping component tokens local until about three components need them. He also advises including "only the levels needed to sufficiently describe and distinguish purposeful intent."
- GitHub Primer's docs name three tiers. Base tokens "map directly to a raw value". Functional tokens "represent global UI patterns". Component tokens "should only be used in component CSS". I checked github.com's served CSS (2026-09-26) and saw all three tiers: `--base-duration-100`, `--fgColor-default`, `--button-danger-bgColor-rest`. The served CSS defines 1,310 distinct custom properties.
- Same scan: every-layout.dev defines 26 (a ratio, eleven scale steps, a measure, colors, fonts, borders). utopia.fyi defines 102, mostly min/max pairs. www.gov.uk defines 105.

Counterevidence. D'Amato argues that structured token formats are "tedious" and favor machine parsing over human authoring. Community posts complain about token bloat and about tiers too deep to trace. Those are anecdotal. MDN (stated): custom properties cannot be used in media or container query conditions, and an invalid substituted value falls back to the inherited or initial value, not to the previous declaration. `@property` (newly available 2024-07) adds type checking and an `initial-value`.

Example. A direction file might define about 5 to 8 raw colors. It maps them to about 8 to 12 roles (surface, text, muted, accent, border, focus, danger, success). Components use only the roles. Changing direction means rewriting the role map, not the components. (These counts are my suggestion, not measured.)

When to use. Always, for a set of directions that share markup or that will be compared. Skip the component tier in a prototype: Curtis's promote-gradually rule applies, and a single file rarely has three consumers of one component value.

Labels: useful pattern / C (practitioner consensus plus observed products). The indirection mechanism is stated (DTCG alias, Curtis). "Two tiers suffice for a prototype" is inferred.

---

## F3. A scale reduces the number of decisions. The particular ratio is a style choice, not a law

Claim. Choosing sizes from a short scale makes rhythm visible and removes arbitrary decisions. It works through constraint, not through any magic in the numbers. Sources agree on the constraint and disagree on how to build the scale.

Evidence, with each number traced.

- Tim Brown (A List Apart, 2011-05-03) defines a modular scale as "a sequence of numbers that relate to one another in a meaningful way". He quotes Bringhurst: "A modular scale, like a musical scale, is a prearranged set of harmonious proportions." Brown's own caveats: "Modular scales are a tool, they're not magic", and "Math is no substitute for an experienced designer's eye". He broke his own scale with a 15 px sidebar size.
- *Every Layout* (Modular scale chapter) builds `--s-5` to `--s5` with `calc()` and a `--ratio` of 1.5. Where 1.5 comes from: body `line-height` 1.5 at `1rem` "creates a default value of 1.5rem", which they treat as the basis for white space. They say: "it is in the strict adherence to *whichever* ratio you choose that harmony is created." The chapter says `pow()` is "coming". It is now widely available (2023-12 in `web-features`), so `calc(1rem * pow(var(--ratio), 3))` works without a build. I confirmed it renders in Firefox 156.
- Nathan Curtis, "Space in Design Systems" (2016-09-25). Base 16, because "It's a good default font size" and divides common screen widths (320, 768, 1024). He doubles each step (2, 4, 8, 16, 32, 64) because a linear scale offers too many near-equal options. He names space by role: inset, squish, stretch, stack, inline, grid.
- The 8-point grid (spec.fm, undated). Justified by "most popular screen sizes are divisible by 8", and by fewer options speeding handoff. Its caveat: "users will likely never see the actual measurements you use."
- Disagreement. *Refactoring UI* (Wathan & Schoger, 2018, read only through secondary notes) prefers a hand-picked scale over a ratio-derived one. Ratios give fractional pixels and too few useful sizes at the small end. *Every Layout* (Units chapter) says the opposite about fractions: "There's no need to do precise conversion, since browsers employ sub-pixel rendering and/or rounding."

What the disagreement depends on (inferred). Dense UI (dashboards, tools) needs many small, close sizes, which a geometric ratio does not give. Editorial and marketing pages need few sizes with clear jumps, which a ratio gives well. Utopia's answer (F4) is to use a smaller ratio on small screens.

Counterevidence. No source I found tests whether ratio-based scales look better than hand-picked ones. The musical-harmony argument, in both Brown and *Every Layout*, is an analogy, not evidence.

Example. every-layout.dev's own CSS (scanned 2026-09-26) has exactly eleven `--s` steps and one `--ratio`. That is the method applied to itself.

When to use. Always use some scale in a direction, because it keeps the file coherent. Choose the ratio for the density of the direction: smaller for dense UI, larger for expressive editorial work. Break the scale on purpose where the eye needs it, as Brown does.

Labels: strong heuristic (a constrained scale) / C. Aesthetic preference (a specific ratio) / D. The constraint mechanism is stated by Curtis and Brown. The density dependence is inferred.

---

## F4. Fluid type and space interpolate between two scales, but viewport units do not zoom

Claim. Instead of stepping sizes at breakpoints, you can set a small-screen scale and a large-screen scale and let `clamp()` interpolate between them. This removes jumps at breakpoints and the question of which side of a breakpoint a device falls on. It has a limit: the `vw` part of the formula does not grow with browser zoom.

Evidence.

- Mike Riethmuller (2015-03-17) introduced the formula: `calc(12px + (24 - 12) * ((100vw - 400px) / (800 - 400)))`. His reason: switching from 2vw to 4vw needs a breakpoint, so the scaling is "jumpy and not fluid". Tim Brown later named it "CSS locks" (stated in search results; I did not read Brown's post).
- Utopia (James Gilyead with Trys Mudford, 2020-02-01) has three steps. Define a small-screen scale (their example is 1.2 at 320 px). Define a large-screen scale (1.333 at 1500 px). Interpolate. The motive (stated): "Breakpoint-based type sizing has always felt a bit arbitrary … equal parts guesswork and compromise." Their caveat: "This approach is not a substitute for good design." My screenshots of utopia.fyi at 390 px and 1440 px (2026-09-26) show the same page with smaller body type and a tighter scale on the narrow viewport.
- *Every Layout* (Units) gives a minimal version with no endpoints: `:root { font-size: calc(1rem + 0.5vw) }`. The `1rem` term keeps the user's default as the floor.
- Limit. Maxwell Barvian (Smashing, 2023-11-07): "browsers do not scale viewport-based units when zooming the page", so fluid text can fail to reach 200% on zoom. His derived rule: "The maximum value must be less than or equal to 2.5 times the minimum value." It holds when the largest breakpoint is under five times the smallest.

Counterevidence. A formula is not a design. Utopia says so, and it cannot pick the two scales for you. Utopia's own site (scanned 2026-09-26) uses zero `clamp()` calls, because it predates wide support and uses `calc()` locks. So the technique does not require `clamp()`. `clamp()` just makes it shorter.

Example. `--step-3: clamp(1.75rem, 1.2rem + 2.5vw, 3rem)`. Here max/min is about 1.71, inside Barvian's 2.5× limit. It rendered as expected in my Firefox 156 test at 420, 900 and 1500 px.

When to use. For directions where display type carries the identity: large headlines and editorial pages. It matters less for dense tool UIs whose type barely changes size. Keep the max/min ratio of each step under 2.5.

Labels: useful pattern / B. The mechanism is shown mathematically by Riethmuller and Barvian, and I tested it. The zoom limit is stated. The 2.5 limit is a derivation, not a user study.

---

## F5. Intrinsic layout and explicit breakpoints are two ways to control a layout. The choice depends on how much the content and its context vary

Claim. One school tells the browser what to aim for and lets its layout algorithms decide: wrapping, flex-basis, `min()`, `ch`, auto-fit grids. Components then adapt to any container without media queries. The other school sets explicit thresholds: viewport media queries for the page shell, and container queries for components. Each has its own failure modes. Container queries now let the explicit school work at component level, which used to be the intrinsic school's main advantage.

Evidence.

- Origins. Ethan Marcotte (A List Apart, 2010-05-25) named the ingredients: fluid grids, flexible images, media queries. He frames the idea with John Allsopp's *The Dao of Web Design* (2000). Jen Simmons (The Big Web Show, published 2018-05-02) named "intrinsic web design": layouts with "four stages of things squishing or growing at separate moments", built from grid, flexbox, multi-column and other tools.
- Where breakpoints go. Stephen Hay at BDConf, as tweeted by Brad Frost on 2012-04-16: "start with the small screen first, then expand until it looks like shit. TIME FOR A BREAKPOINT!" The mechanism: breakpoints come from the content, not from device sizes.
- The intrinsic case (*Every Layout*, stated): "If you find yourself wrestling with CSS layout, it's likely you're making decisions for browsers they should be making themselves." Media queries are "manual overrides"; "What's so special about 960px?" The Switcher (Pickering, "The Flexbox Holy Albatross", 2019-01-13) uses `flex-basis: calc((40rem - 100%) * 999)`. Above the threshold the basis is hugely negative, so items sit in a row. Below it the basis is hugely positive, so they stack. There is no 2+1 state and no media query.
- *Every Layout*'s own admission (Axioms, stated): "designing for the web is designing without seeing". Axioms "do not directly create visual artefacts, only the characteristics of artefacts that might emerge", and results can "look and behave in ways that you might not have foreseen."
- Container queries (MDN, stated). `container-type: inline-size` applies inline-size containment. Size containment means the element's "size is computed as if it had no children", and `size` containment risks "a box could end up zero-sized". Victor Ayomipo (Smashing, 2026-09-16) lists the practical limits: a container cannot query itself, so it needs a wrapper; block-size queries collapse without an explicit height; you cannot use `var()` in a size condition. Container style queries, newly available 2026-05, can query custom property values.
- My test (Firefox 156, 2026-09-26; `code-shots/own-test-page-*`): three cards in a Switcher, each an inline-size container with a wide variant above 22rem. At 420 px the cards stack full width and show the wide variant. At 900 px they sit in a row, each under 22rem, and show the compact variant. At 1500 px they are wide again. The component does not track the viewport, as intended, so its look cannot be predicted from viewport width alone (inferred).

Counterevidence. Andy Budd (2012) argued that working in the medium "encourages a minimal design aesthetic based on the rendering capabilities of CSS". That was before grid, but intrinsic layouts still tend toward stacks, clusters and even columns (inferred). Hacks like the 999 multiplier are hard to read for anyone who did not write them (inferred). Explicit breakpoints give art-directed control at known widths, which a comp-matching direction may need.

What the choice depends on (inferred). Use intrinsic primitives when the content is unknown or variable, or when components appear in many slots. Use explicit thresholds when the direction depends on a specific composition at specific sizes, such as an editorial hero or a poster-like page. Use viewport media queries for the page shell and for user preferences (`prefers-color-scheme`, `prefers-reduced-motion`), which container queries cannot read.

When not to use intrinsic layout. When the direction's identity is a precise, asymmetric composition. When the audience for the prototype needs predictable screenshots at named sizes.

Labels: context-dependent heuristic / C. The mechanisms (flex-basis, containment) are stated in MDN and Pickering, and I tested them. The rule for choosing is inferred.

---

## F6. Organize the cascade on purpose: layers set precedence by order, not by specificity

Claim. In a single file, most style conflicts come from specificity. Cascade layers, `:where()`, native nesting and `@scope` let one file hold a reset, tokens, layout primitives, components and exceptions with predictable precedence and no naming system.

Evidence.

- MDN `@layer` (stated). "The last layer to be listed will win." "Styles that are not defined in a layer always override styles declared in named and anonymous layers." `!important` reverses layer order. Cascade layers are widely available (2022-03).
- MDN nesting (stated). Native nesting is "parsed by the browser". It cannot concatenate selectors the way Sass does (`&__element` is not possible), and the specificity of `&` is computed like `:is()`, from the most specific selector in the list. Widely available since 2023-12.
- `@scope` became newly available on 2026-03-24 (Safari 26.4 was last). It is fine as an enhancement, but not yet as structure for audiences on older Safari.
- Observed 2026-09-26 in served, minified CSS: stripe.com declares `@layer reset, base, app`; linear.app `@layer reset, base, app.base`; vercel.com has `theme`, `base`, `components`, `utilities`. github.com, gov.uk and bbc.co.uk use `@layer` little or not at all.
- The architecture disagreement. Adam Wathan (2017-08-07) argues that semantic CSS still depends on the HTML ("Your CSS … needs to know what classes your HTML has decided to expose"). He says constrained utilities stop CSS "growing linearly with your project size". He cites GitLab's 402 unique text colors, a number I did not trace to its source. *Every Layout* (Global and local styling) and Andy Bell's CUBE CSS argue for element and universal styles first, layout primitives next, utilities last. Utilities are "for final adjustments". Their reason: reach should be inversely proportional to specificity (Harry Roberts' ITCSS).
- No-build constraint. Tailwind's browser script (`@tailwindcss/browser@4`) runs in the page. Its docs say: "The Play CDN is designed for development purposes only, and is not intended for production." That is acceptable for a throwaway prototype, and it adds a runtime dependency on a CDN.

What the disagreement depends on (inferred from both sides). *Every Layout* itself concedes utility-first may suit "a great deal of detail and disparity in the visual design" or quick prototyping "without context switching between CSS and HTML". Cascade-first suits a design where a few axioms should apply everywhere. For comparing several directions that share markup, cascade-first with tokens is easier to swap, because the direction lives in the stylesheet, not in thousands of class attributes (inferred).

Example. `@layer reset, tokens, layout, components, exceptions;` at the top of the `<style>` block, with each direction's personality in `tokens` and `components`. My test file used this structure without conflicts.

Labels: useful pattern / B for the precedence mechanics (spec behavior per MDN). Context-dependent heuristic / C for the choice of architecture.

---

## F7. Color can be built as a formula: a few seeds in OKLCH, with derived roles

Claim. In a perceptual color space, lightness steps look like equal steps across hues. So a palette can be written as seeds plus rules (`oklch(from var(--brand) calc(l + .35) calc(c * .3) h)`, `color-mix()`, `light-dark()`), and a direction's color changes by editing one or two seeds. HSL cannot do this reliably, because its lightness is not perceptual.

Evidence.

- Björn Ottosson (2020-12-23) designed Oklab to predict "perceived lightness, chroma and hue", fitted to CAM16-generated data plus earlier hue data. His limit: "this data can't be used to say which model best matches human perception." JzAzBz beats it on hue and CAM16-UCS on overall uniformity. His later color-picker post says Oklab's lightness is weaker where a reference white is defined, and that HSL hue "has quite severe distortions".
- Evil Martians (Sitnik & Turner, page dated 2025-09-17) argue that OKLCH gives predictable palette generation and contrast. They list the problems: many OKLCH values fall outside sRGB or P3; each hue has a "different maximum chroma"; browsers clip out-of-gamut colors rather than map them.
- Support: `oklch()` and `color-mix()` are widely available (2023-05). Relative color syntax is newly available (2024-09). `light-dark()` is newly available (2024-05), and MDN says it needs `color-scheme: light dark`. `contrast-color()` is newly available (2026-04).
- Observed adoption, 2026-09-26: vercel.com's served CSS uses `oklch(` 171 times and `@property` 106 times. github.com, gov.uk, stripe.com, linear.app and bbc.co.uk use `oklch(` zero times. linear.app uses `color-mix(` 43 times. So the technique is in production, not universal.

Counterevidence. Equal OKLCH chroma is not equally vivid across hues, because the gamut is uneven. A formula that multiplies chroma can clip some hues and not others (stated by Evil Martians; inferred for formulas). Albers' point that color is relative to its neighbors (area 3) means no formula removes the need to look.

Example. My test page derived `--brand-soft` from `--brand` with relative syntax, and derived surface and text from `light-dark()`. It rendered in Firefox 156.

When to use. When directions need light and dark modes, or several accent variants, from few decisions. When not: a direction built on a fixed brand palette given in hex. There you map the palette, you do not generate it.

Labels: strong heuristic / B for perceptual uniformity (a model fitted to data, not a direct perception study). Useful pattern / C for palette formulas.

---

## F8. Build in code to answer behavior, responsiveness and real-content questions. Draw or mock to answer look questions fast. Say which question each prototype answers

Claim. A prototype answers some questions and leaves others incidental. A coded HTML prototype is strong on behavior, states, responsiveness, real text and real rendering. It is weaker at fast visual divergence. The designer should say what the prototype prototypes, so that reviewers do not critique incidental parts.

Evidence.

- Houde & Hill (1997, full text) identify three questions: role, look and feel, implementation. "The degree of visual and behavioral refinement of a prototype does not necessarily correspond to the solidity of the design." They describe a prototype whose UI "was neither good enough nor bad enough to avoid misunderstandings". The discussion drifted to the incidental UI. "No one tool supports iterative design work in all of the important areas."
- Lim, Stolterman & Tenenberg (2008, through quotes in a review) give the economic principle: "the best prototype is one that, in the simplest and most efficient way, makes the possibilities and limitations of a design idea visible and measurable", and "the decision of what to filter out is always based on the purpose."
- Myers et al. (2008, full text) surveyed 259 designers. 86% said behavior is harder to prototype than appearance, and 76% said behavior is harder to communicate to developers. They also report that designers "want to explore multiple versions of behaviors, but today's tools make this difficult", and that keeping and comparing code versions is hard.
- Hartmann et al. (UIST 2008, abstract only) built Juxtapose, which edits and runs code alternatives in parallel and tunes parameters at runtime. The premise is that code tools push toward single artifacts.
- For code: Stephen Hay (2014-12-23) says a browser comp is "the visualization of the design" and "Creativity is tool-independent"; he sketches on paper first. GDS (James Weiner, 2012-03-29) designed GOV.UK in the browser for "as little friction … as possible". Jen Simmons (2018) calls a static comp "a PDF of a printout of a website that doesn't exist and never will". Rauno Freiberg (2023) found interaction details, such as gesture thresholds and no animation on high-frequency actions, only by building.
- Against, or with limits: Andy Budd (2012-03-14) says the browser "lacks rudimentary tools" for drawing and "encourages a minimal design aesthetic". Sarah Parmenter (2012-02-21): "My creative brain switches at the point when I open my html/css editor … starts thinking in terms of structure." Dan Mall (2012-11-13) uses element collages to "document a thought at any state of realization and move on", which a coded page does not allow.

What the disagreement depends on (inferred). Parmenter's and Budd's complaint is about divergence: making many rough visual ideas fast. Hay's and GDS's praise is about convergence: testing a chosen idea against the real medium. Both can be true. Hay's, Simmons' and Parmenter's own processes all start with sketching.

Implications for an agent that outputs HTML (inferred). The agent pays no drawing cost, so its main risk is not tool friction but premature commitment to one structure. It should make directions differ at the level of axioms and tokens before writing markup (F10). It should state, per direction, which aspects are intended and which are incidental: placeholder copy, stock icons, untested states.

Labels: strong heuristic / B. Houde & Hill and Lim et al. are frameworks. Myers is survey data. Practitioner accounts are consistent but anecdotal.

---

## F9. Generic output comes from defaults taken without choosing them

Claim. When a design is built in code, whatever the file does not decide is decided by defaults: the browser's, a framework's, a template's, or a generator's training data. A generic look is largely the sum of unchosen defaults. That is sometimes right, because defaults carry conventions users know.

Evidence.

- Adam Wathan (X, 2025-08-07; date decoded from the post ID): "I'd like to formally apologize for making every button in Tailwind UI `bg-indigo-500` five years ago, leading to every AI generated UI on earth also being indigo." This is anecdotal but first-hand. A placeholder default spread through copies, and then through generators.
- The Design Theater preprint (Imteyaz et al., arXiv, 2026-07) compared 120 interfaces from ChatGPT, Claude, Firebase Studio, v0 and Bolt. The outputs converged on "stylistic patterns, component aesthetics, spacing tendencies" and on "section ordering, navigation placement, grouping of elements". Color varied most. It is a single study, not peer reviewed, and it measures no users.
- The "Vibe Design Agents" preprint (Zhang et al., arXiv, 2026-09) found that a baseline generator produced one theme across five runs, with screenshot similarity 0.6765. Having the model first propose scored design specs (seed color, light/dark, headline and body fonts, corner roundness) and choose one broadened the variation. Their data are not released, and it is a single study.
- Boris Müller (2018): "Templates are not designs. Rather, they are rules for combining related data types." Web design seems "driven by technical and ideological constraints rather than creativity."
- Frank Chimero ("The Web's Grain", 2015) offers the counter-reading: "Many sites will share design solutions, because we're using the same materials … proof of design patterns … and not evidence of a visual monoculture."
- Hacker News on Müller (2018, anecdotal): "users prefer your site to work the same way as all the other sites they already know" (tvanantwerp).

Counterevidence. None of these sources show that generic designs perform worse. The convergence studies measure similarity, not quality.

Example (inferred). A direction that keeps a framework's default palette, radius and font inherits that framework's identity.

When to use. For each direction, list which defaults it keeps on purpose (convention, familiarity, low cost) and which it overrides to carry identity (type, color, shape, composition, motion). A conventional direction is valid when it keeps defaults by choice.

Labels: context-dependent heuristic / C. The mechanism that defaults spread is stated by Wathan and Müller. The convergence is measured in two single 2026 preprints. The "list your defaults" practice is inferred.

---

## F10. Write the direction as a small spec before the markup. Style-only variation cannot change structure

Claim. If each direction is written first as a small spec (axioms, a scale, a token map, a type pairing, a layout idea), directions differ on purpose and are easier to compare. Directions that share one HTML file and differ only in CSS can vary a lot visually, but they cannot vary structure, order or content.

Evidence.

- CSS Zen Garden (Dave Shea, launched 2003-05-08; I read the current markup on 2026-09-26). Participants change only the CSS: "The HTML remains the same". The markup carries six empty presentational hooks (`<div class="extra1" role="presentation">` through `extra6`) so that designers had elements to style. This is direct evidence that CSS-only variation needed markup made for styling (observed). Also, none of those designs could reorder the content (inferred from the rule).
- *Every Layout* (Axioms, stated). A design should rest on axioms stated in "a short phrase or sentence" (for example, "the measure should never exceed 60ch"), coded so they "pervade the design without qualifications or exceptions". Exceptions are then handled by the cascade.
- Vibe Design Agents preprint (2026, see F9). Making "design direction an explicit intermediate decision" before implementation broadened the variety of output.
- Design Theater preprint (2026, see F9). Over 25% of user-facing design explanations were not implemented in the generated interface, and 34% for functional requirements. Two evaluators judged each claim against the rendered interface.

Implication (inferred). For a persona that writes a rationale and a file, the rationale should be checkable against the file. The spec should name concrete tokens and axioms, and the persona should confirm that each claimed decision is present in the code.

Counterevidence. Committing to a spec early can fix a direction before any rendering feedback, which is Parmenter's complaint in reverse. The Zen Garden shows that CSS alone can produce very different results, so sharing markup is a real option when the question is purely visual.

When to use. Share markup when the directions differ only in visual language, which makes comparison fair. Write separate markup when they differ in structure, flow, density or content priority (area 2 territory).

Labels: useful pattern / C. The Zen Garden observation is direct. The benefit of a spec is supported by one 2026 preprint (B- at best). The rationale-mismatch rate is from one 2026 preprint.

---

## F11. Relative units tie layout to text. Choose the unit by what the size should follow

Claim. Sizes set in `rem`, `em` and `ch` follow the user's font setting and the local text size. Sizes set in `px` do not. Choosing a unit means choosing what the size follows.

Evidence.

- *Every Layout* (Units, stated). Font sizes set in `px` ignore the user's default size. Their rules of thumb: "em units are better for sizing inline elements, and rem units are better for block elements". SVG icons suit `em`. `ch` is "the only appropriate unit" for measure. They cite Evan Minto's finding (Internet Archive data, 2018) that more users change their default font size than use Edge or IE. The figure is 3.08% in secondary reports. I did not read Minto's post itself.
- Alastair Campbell (2018) thinks that figure is too low, because "Text-only sizing simply doesn't work beyond a small amount", so users give up on it.
- *Every Layout* (Axioms) sets measure at `60ch` and cites Bringhurst's 45 to 75 characters. `1ch` is the width of the "0" glyph, so `60ch` is an approximation that varies with the font (stated).
- Counter-practice, observed 2026-09-26: `px` against `rem` values in served CSS were 2,141 to 346 on gov.uk, 5,938 to 252 on github.com, and 11 to 93 on every-layout.dev. I did not check which properties they set.

When to use. Use `rem` for type and block spacing, `em` for things that sit inside text (icons, inline padding), `ch` for measure, and `px` for hairlines and borders where scaling does not help. Accessibility conformance itself is outside this area.

Labels: strong heuristic / B-C. The unit behavior is spec behavior. The user data is one site's analytics, reported second-hand.

---

## F12. Declarative HTML and CSS now cover most interaction states a prototype needs, without a framework

Claim. A single file can show open/closed, selected, invalid, empty, hover, focus and transitions using only native elements and CSS. This makes it cheap to show states, which Myers et al. found hardest to prototype.

Evidence (support tiers as of 2026-09-26).

- Widely available: `<dialog>`, `<details>`, `:has()` (style a parent by its state), `:user-valid`/`:user-invalid` (2023-11), `inert`, import maps (ES modules from a CDN, no bundler).
- Newly available: popover, exclusive accordions via `<details name>` (2024-09), `@starting-style` for enter/exit animation, invoker commands, same-document view transitions, anchor positioning core (dates in F1).
- Limited: interest invokers (hover popovers), customizable `<select>`, scroll-driven animations, `interpolate-size`, `popover="hint"` (no Safari).
- My test: `:has()` outlined a card that contained a flag element, in Firefox 156.

Counterevidence. Declarative features cover common states, not custom behavior. Rauno's gesture examples need script. Newly available features exclude older Safari and Firefox users (F1).

When to use. Show at least the key non-default states of each direction (empty, error, loading, open) with native features. Use a few lines of script only where the behavior is the point of the direction.

Labels: useful pattern / A for support facts. C for the claim that this changes what designers prototype (inferred from Myers).

---

## F13. System font stacks cost nothing to load and carry the OS's voice, not the direction's

Claim. In a no-build file, type comes either from installed fonts (system stacks) or from a hosted service such as Google Fonts via a `<link>`. System stacks render instantly and feel native. They also make the direction look like the platform, and they have script-specific failures.

Evidence.

- Modern Font Stacks (Dan Klammer, CC0): "The fastest fonts available. No downloading, no layout shifts, no flashes". Rendering varies by OS.
- `system-ui` has been widely available since 2021-09. `ui-sans-serif`, `ui-serif` and the other `ui-*` families are Safari only (`web-features`).
- Tailwind PR #20318 (merged 2026-07-14) removed `system-ui` and `ui-sans-serif` from Tailwind's default stack. On Japanese-locale Windows, `system-ui` resolved to Yu Gothic UI and rendered some characters wrongly. The PR cites MDN and similar changes in Astro Starlight and VitePress.

When to use. System stacks suit conventional, tool-like or native-feeling directions. Directions where type carries the identity need a chosen font, loaded from a service, with a named fallback. Loading and performance are outside this area.

Labels: context-dependent heuristic / C. The CJK failure is documented in code and issue threads.

---

## Gains and losses in code, in one place

- Gains: real reflow and type rendering (*Every Layout*, Simmons, Hay); behavior and states (Myers et al., Rauno); self-enforcing axioms (*Every Layout*); cheap direction swaps through tokens (F2, F7); no comp-to-build gap (GDS, Hay).
- Losses: direct manipulation and fast divergence (Budd, Parmenter, Mall); a pull toward default-shaped output (Budd, Parmenter, Wathan); hard version comparison (Myers et al., Hartmann et al.); "designing without seeing" (*Every Layout*).
- Inferred: the losses concern divergence, and the gains concern convergence.

---

## Where I found no good evidence

- No controlled study compares ratio-based and hand-picked type scales.
- No study measures whether intrinsic layouts produce fewer layout defects than breakpoint layouts. The claims are practitioner arguments.
- No study of human designers measures whether designing in code narrows exploration. Myers et al. report difficulty with versions, not narrower results. The homogeneity data are about AI generators.
- I could not read *Refactoring UI*, Hay's *Responsive Design Workflow*, or the paid *Every Layout* layout chapters. I used them only where noted.

---

## Outside my area

- Area 1: Houde & Hill (1997), Lim et al. (2008), Myers et al. (2008), Hartmann et al. (2008) and the Vibe Design Agents preprint (2026), as used in F8 and F10.
- Area 4: the Design Theater preprint (2026), Wathan (2025), Müller (2018) and Chimero (2015), as used in F9.
- Review persona: over 25% of stated rationales were not implemented (Design Theater), so check rationale against code.
- Accessibility: Barvian (2023) on fluid type and zoom; Minto and Campbell (2018) on font-size settings.
