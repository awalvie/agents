# Visual craft

Read this when you choose type, spacing, grids, colour, icons and imagery. `code.md` says how to build them. Labels are in `README.md`. The three coverage books were read only in part.

## Type

- Line length. Bringhurst's 45 to 75 characters, with 66 "widely regarded as ideal", is stated for a single serifed column in print, as consensus, not measurement. On screen, most studies found lines up to about 100 characters read faster (Dyson 2004, a review). About 55 characters gave better comprehension than 100 (Dyson & Haselgrove 2001) and was rated easiest to read (Dyson & Kipping 1998, via Dyson 2004). Dyson (2021) still advises against long lines, because readers like them least. [CH, B, stated]
- So cap the measure near 60 to 80 characters for long reading. Allow wider lines, or a width toggle, for reference content that people scan: Wikipedia added a toggle after editors called its 2022 width limit "wasted space" (Wikimedia). [CH, B, inferred]
- Body size. Comprehension was significantly lower at 10 and 12 pt than at 18 pt (Rello et al. 2016, 104 readers). The authors recommend 18 pt; the co-author's blog equates it to 24 px. So the 16 px default may be small for long reading, and where the gain stops is not shown. Line spacings of 1.0 and 1.4 performed alike; only 0.8 and 1.8 hurt. GOV.UK keeps body text at 19 px on small screens while its headings shrink. Smaller body text fits when density is the goal and users come every day. [SH, B, stated]
- Type scale. A limited set of related sizes makes each step read as a level (Bringhurst). The ratio is taste. Brown (2011) broke his own scale: "Modular scales are a tool, they're not magic." Phones need a tighter ratio than large screens, because large jumps wrap headlines into many lines (Gilyead 2020). Use a tight ratio for calm, dense tools and a steep one for editorial drama. [UP, C, stated]
- Typeface. Serifs made no difference to reading speed when everything else was equal (Arditi & Cho 2005). In a study of 16 fonts normalised for size, "preference does not predict speed", and no single font was fastest for everyone: "different fonts work best for different people" (Wallace et al. 2022, crowdsourced readers, 5 fonts each). Readers notice when a face does not fit the content, but in one study it barely changed how they perceived the text (Brumberger 2003). [SH, B, stated]
- So choose a body face for how it renders at the target size: generous x-height, open spacing, a full set of weights. Spend the character on display type, where it is visible and cheap, as The Pudding does with a heavy display serif (observed 2026-09-26). [CH, B/C, inferred]

## Space and grouping

- Elements close together read as a group, and a shared region is "capable of overcoming" closeness (Gestalt research, Wagemans et al. 2012; Palmer 1992, demonstrations). So the ratio between the space inside a group and the space between groups matters more than the values. Craigslist groups about a hundred links with almost no boxes, by tight lines and wide gutters (observed 2026-09-26). [FP, A for grouping, stated. The ratio rule is inferred]
- Boxes and cards group strongly, but each adds edges, and edges add complexity. Use them when space alone cannot separate the groups, as in mixed content or dense data. [CH, C, inferred]
- A spacing scale of 5 to 8 steps, each with a role (inside a component, between siblings, between sections), makes the same ratios repeat across a product. The 8 px unit has no perceptual basis. Its stated reasons are fewer choices and screen sizes that divide by 8 (spec.fm, undated, no author shown). Some teams use 4, and dense tools may need finer steps. [UP, C, inferred for a scale. DC, D, stated for the 8]

## Grids

- A grid makes a few decisions once and reuses them, so repeated sizes read as a family and priorities stand out (Müller-Brockmann, pp. 9 to 12). He derives each grid from the work, and frames it as an ethic of objectivity, which makes it a style, not a law. [UP, C, stated]
- On the web, derive the grid from the content, such as an ad unit or an image size (Boulton 2011). Some designers never start with a grid (van Deursen, quoted by Ford 2014). Van Toorn's objection to Crouwel (1972) is that a neutral system also carries values. [UP, C, stated] Twelve columns are popular because 12 divides by 2, 3, 4 and 6. [inferred, arithmetic]
- A strict grid suits many-page systems, editorial content and dense data, with column width taken from the measure or the main media size. An expressive single page can break it on purpose, keeping one strong alignment so the break reads as intended. [CH, C, inferred]
- Vertical rhythm. A shared vertical unit for spacing is cheap and calms the page. A true baseline grid pays off only where lines sit side by side in columns, and it is hard to build in CSS (Brunborg 2012). No study shows reader benefits. [AP, C/D, inferred]

## Hierarchy

- Emphasis is relative (`core.md`), so weight, colour, contrast and position build hierarchy as well as size. Refactoring UI advises lowering a label rather than raising the value, except where users hunt for the label (Wathan & Schoger 2018, preview). Stripe's hero sets one headline in dark ink, then a lighter slate, at one size (observed 2026-09-26). [SH, C, stated]
- One option: decide the most important item per view, lower everything else one step before raising anything, and use size jumps between sections and weight or colour inside them. [SH, C, inferred]

## Colour

- A colour looks different on different grounds (Albers). HSL's equal "lightness" looks unequal across hues. Perceptual spaces such as Oklab align it better, but they are fitted models (Ottosson 2020). [FP, A, stated for relativity. SH, B, stated for the models]
- Build a palette as ramps with equal perceived lightness steps, each step with a role. Stripe rebuilt its palette so that any two colours at least five levels apart have enough contrast for small text (Koopersmith & Miner 2019). Radix gives its 12 steps roles from background to text. Linear builds its themes, in LCH, from three variables: a base colour, an accent colour and a contrast level (Linear 2024). A dark, saturated yellow cannot exist, and designers still adjust by eye. [SH, B/C, stated]
- Harmony and emphasis pull apart. Pairs of similar hue read as harmonious, while a figure stands out as its hue contrasts with its ground (Schloss & Palmer 2011, 48 people). Bright colour over large areas is loud, and in small amounts it signals (Imhof, quoted by Tufte, quote unchecked). [CH, B, stated]
- Routes of equal standing include neutral surfaces with one accent reserved for action or meaning, as Stripe keeps its gradient to one band, close to the common SaaS look; colour as identity in large saturated fields, as on The Pudding's story cards (both observed 2026-09-26); black and white with no accent; and colour taken from the product's photography or data. [CH, C, inferred for the first two, synth for the last two]
- In the Mozilla rebrand a "breathtaking" neon palette was impractical for web products, and the softer colours came from the browser's highlight bar (Murray & Johnson 2017). Brand colour must survive interface use. [UP, C, stated]

## Neutrals and dark themes

- "Never use pure black" (Taylor 2012) is taste with a narrow truth: tinted dark greys relate to the palette. Pure black suits photography and product stages, as behind Apple's iPhone render, while Linear uses a near-black #08090a (sampled 2026-09-26). [AP, D, stated]
- Dark text on a light ground was read better than the reverse for young and older adults (Piepenbrock et al. 2013), and the advantage grew as characters got smaller (Piepenbrock et al. 2014). Both come from one lab. A dark direction is still legitimate for long-hours tools and media; give its reading screens larger text or a light mode. [SH, B, stated]

## Complexity, typicality and posture

- At first glance (screenshots shown for 1 s or less), people prefer low to moderate visual complexity (Tuch et al. 2012; Reinecke & Gajos 2014, 2.4 million ratings), and low complexity costs less than high (Reinecke & Gajos). [SH, A, stated] Typicality is in `core.md`.
- Cooper & Reimann (2003) advise a conservative style and a narrow palette for a product people stare at all day, because bright colours "seem garish after a couple of weeks", and bigger, brighter controls for one visited briefly. [CH, C, stated]

## Proportion

- A fixed ratio gives a shared rule, but the claim that 1.618 or the thirds are especially beautiful is barely supported. Preference for rectangles peaks broadly, from about 1.5:1 to 2:1 (McManus 1980, via Green 1995), and the rule of thirds plays a minor role in fine art (Amirshahi et al. 2014). Never justify a direction by its ratio. [UP, C, inferred for ratios as constraints. UC, D, stated for golden-ratio beauty]

## Icons and imagery

- An icon's meaning comes mostly from familiarity, not from realism (McDougall et al. 2016). Labels speed up learning, and their value fades once the icon is known (Wiedenbeck 1999). Label icons in navigation and for anything new. A distinctive set holds together with a shared grid, stroke and corner rules; keeping the usual metaphors for search, close, menu and share keeps it readable. A circle is drawn larger than a square to look the same size (Material system icons). [SH, B, stated for familiarity and labels. UP, C, inferred for keylines]
- In NN/g eyetracking, purely decorative "feel-good" images were ignored, and photos of the real product and real people were studied, on one page for longer than the text beside them (Nielsen 2010). Plan imagery from the content: the real product, data or people. Abstract or illustrated imagery can carry identity, but do not expect it to carry information. [SH, C, stated]
