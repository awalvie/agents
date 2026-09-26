# Visual craft

Read this when you choose type, spacing, grids, colour, icons and imagery. `code.md` says how to build them. Labels are in `README.md`. Bringhurst, Müller-Brockmann and Albers were read only in part.

## Type

- Line length. Bringhurst's 45 to 75 characters, with 66 as ideal, is stated for a single column of a serif text face in print, and he reports it as consensus, not as a measurement. On screen, longer lines (up to about 100 characters) were often read faster, and about 55 characters gave better comprehension and was preferred (Dyson 2004, a review; Dyson & Haselgrove 2001). Dyson (2021) still advises against long lines, because readers like them least. [CH, B, stated]
- So cap the measure near 60 to 80 characters for long reading. Allow wider lines, or a width toggle, for reference content that people scan: Wikipedia added a toggle after editors called its 2022 width limit "wasted space" (Wikimedia). [CH, B, inferred]
- Body size. Comprehension was significantly lower at 10 and 12 pt than at larger sizes (Rello et al. 2016, 104 readers, co-author's summary checked). The authors recommend 18 pt, which they equate to 24 px, as a balance with fitting text on screen. So the 16 px default is small for reading, and where the gain stops is not shown. Line spacing from 1.0 to 1.4 made little difference. GOV.UK keeps body text at 19 px on small screens while its headings shrink. Use smaller body text only when density is the goal and users come every day. [SH, B, stated]
- Type scale. A limited set of related sizes makes each step read as a level (Bringhurst). The ratio is taste. Brown (2011) broke his own scale: "Modular scales are a tool, they're not magic." Phones need a tighter ratio than large screens, because large jumps wrap headlines into many lines (Gilyead 2020). Use a tight ratio for calm, dense tools and a steep one for editorial drama. [UP, C, stated]
- Typeface. Serifs made no difference to reading speed when everything else was equal (Arditi & Cho 2005, abstract checked). In a study of 16 fonts normalised for size, "preference does not predict speed", and each reader had a different fastest font (Wallace et al. 2022). Readers notice when a face does not fit the content, but in one study the face barely changed how they perceived the text (Brumberger 2003). [SH, B, stated]
- So choose a body face for how it renders at the target size: generous x-height, open spacing, a full set of weights. Spend the character on display type, where it is visible and cheap, as The Pudding does with a heavy display serif (observed 2026-09-26). [CH, B/C, inferred]

## Space and grouping

- Elements close together read as a group, and a shared region groups even more strongly than closeness (Gestalt research, Wagemans et al. 2012; Palmer 1992). So the ratio between the space inside a group and the space between groups matters more than the values. Craigslist groups about a hundred links with almost no boxes, using tight lines inside columns and wide gutters between them (observed 2026-09-26). [FP, A for grouping, stated. The ratio rule is inferred]
- Boxes and cards group strongly, but each adds edges, and edges add complexity. Use them when space alone cannot separate the groups, as in mixed content or dense data. [CH, C, inferred]
- A spacing scale of 5 to 8 steps, each with a role (inside a component, between siblings, between sections), makes the same ratios repeat across a product. The 8 px unit has no perceptual basis. Its stated reasons are fewer choices and screen sizes that divide by 8 (spec.fm, undated, no author shown). Some teams use 4, and dense tools may need finer steps. [UP, C, inferred for a scale. DC, D, stated for the 8]

## Grids

- A grid makes a few decisions once and reuses them, so repeated sizes read as a family and priorities stand out (Müller-Brockmann, pp. 9 to 12). He derives each grid from the work, and frames it as an ethic of objectivity, which makes it a style, not a law. [UP, C, stated]
- On the web, derive the grid from the content, such as an ad unit or an image size (Boulton 2011). Some designers never start with a grid (van Deursen, quoted by Ford 2014). Van Toorn's objection to Crouwel (1972) is that a neutral system also carries values. [UP, C, stated] Twelve columns are popular because 12 divides by 2, 3, 4 and 6. [inferred, arithmetic]
- Use a strict grid for many-page systems, editorial content and dense data, and take the column width from the measure or the main media size. Break the grid on purpose for expressive single pages, and keep one strong alignment so that the break reads as intended. [CH, C, inferred]
- Vertical rhythm. A shared vertical unit for spacing is cheap and calms the page. A true baseline grid pays off only where lines sit side by side in columns, and it is hard to build in CSS (Brunborg 2012). No study shows reader benefits. [AP, C/D, inferred]

## Hierarchy

- Emphasis is relative (`core.md`), so weight, colour, contrast and position build hierarchy as well as size. Refactoring UI's advice is to lower a label (smaller, lighter, less contrast) rather than raise the value, except where users hunt for the label (Wathan & Schoger 2018, preview chapter). Stripe's hero sets one headline in dark ink, then a lighter slate, at one size (observed 2026-09-26). [SH, C, stated]
- One option: decide the most important item per view, lower everything else one step before raising anything, and use size jumps between sections and weight or colour inside them. [SH, C, inferred]

## Colour

- A colour looks different on different grounds (Albers). In HSL, colours of equal "lightness" look very different in lightness across hues. Perceptual spaces such as Oklab align lightness better, but they are fitted models, not proof of perception (Ottosson 2020). [FP, A, stated for relativity. SH, B, stated for the models]
- Build a palette as ramps with equal perceived lightness steps, each step with a role. Stripe rebuilt its palette so that any two colours five levels apart have enough contrast for small text (Koopersmith & Miner 2019). Radix gives its 12 steps roles from background to text. Linear builds whole themes from three LCH values: base, accent and contrast (Linear 2024). A dark, saturated yellow cannot exist, and designers still adjust by eye. [SH, B/C, stated]
- Harmony and emphasis pull apart. Pairs of similar hue read as harmonious, while a figure stands out as its hue contrasts with its ground (Schloss & Palmer 2011, 48 people). Bright colour over large areas is loud, and in small amounts it signals (Imhof, quoted by Tufte, quote unchecked). [CH, B, stated]
- This gives two routes of equal standing. One is analogous or neutral surfaces with one contrasting accent reserved for action or meaning, as Stripe keeps its saturated gradient to one band. That route sits close to the common SaaS look (`languages.md`). The other makes colour the identity with large saturated fields, each holding one thing, as on The Pudding's story cards (both observed 2026-09-26). [CH, C, inferred]
- In the Mozilla rebrand a "breathtaking" neon palette was impractical for web products, and the softer colours came from the browser's highlight bar (Murray & Johnson 2017). Brand colour must survive interface use. [UP, C, stated]

## Neutrals and dark themes

- "Never use pure black" (Taylor 2012) is taste with a narrow truth: tinted dark greys relate to the palette. Pure black suits photography and product stages, as behind Apple's iPhone render, while Linear uses a near-black #08090a (sampled 2026-09-26). [AP, D, stated]
- Dark text on a light ground was read better than the reverse, especially at small sizes, in studies from one lab (Piepenbrock et al. 2013, 2014). A dark direction is still legitimate for long-hours tools and media; give its reading screens larger text or a light mode. [SH, B, stated]

## Complexity, typicality and posture

- At first glance, people prefer low to moderate visual complexity (Tuch et al. 2012; Reinecke & Gajos 2014), and too little complexity costs less than too much (Reinecke & Gajos). [SH, A, stated] Typicality is in `core.md`.
- A product people live in should use a conservative visual style and a narrow palette, while one people visit briefly can use bigger, brighter controls (Cooper & Reimann 2003). [CH, C, stated]

## Proportion

- A fixed ratio gives a shared rule, but the claim that 1.618 or the thirds are especially beautiful is barely supported. Preference for rectangles peaks broadly, from about 1.5:1 to 2:1 (McManus 1980, via Green 1995), and the rule of thirds plays a minor role in fine art (Amirshahi et al. 2014). Never justify a direction by its ratio. [UP, C, inferred for ratios as constraints. UC, D, stated for golden-ratio beauty]

## Icons and imagery

- An icon's meaning comes mostly from familiarity, not from realism (McDougall et al. 2016). Labels speed up learning, and their value fades once the icon is known (Wiedenbeck 1999). Label icons in navigation and for anything new. Draw a distinctive set only on a shared grid with shared stroke and corner rules, and keep the usual metaphors for search, close, menu and share. A circle is drawn larger than a square to look the same size (Material system icons). [SH, B, stated for familiarity and labels. UP, C, inferred for keylines]
- In NN/g eyetracking, purely decorative "feel-good" images were ignored, and photos of the real product and real people were studied, on one page for longer than the text beside them (Nielsen 2010). Plan imagery from the content: the real product, data or people. Abstract or illustrated imagery can carry identity, but do not expect it to carry information. [SH, C, stated]
