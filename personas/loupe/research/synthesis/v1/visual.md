# Visual design

Read this file for layout, hierarchy, type, colour, motion, brand, design systems and charts. Contrast and target-size *compliance* are in [accessibility-performance.md](accessibility-performance.md). Labels as in [core.md](core.md).

## Hierarchy and grouping

- **Grouping is a claim about structure.** People group things that are close together, look alike, are connected, or share a bounded area (Wagemans et al. 2012) `[FP · A]`. A shared container outweighs spacing (Palmer 1992). A card that holds items from different tasks tells users they belong together.
- **Signifiers.** Flat styling that removes the cues showing what is clickable cost 22% more time and 25% more fixations (NN/g 2017, 71 people, 9 page pairs) `[SH · B]`.
  - The cost vanished on sparse, conventional pages with high-contrast targets. Flatness is safe when the page is simple and familiar. The denser or more novel the page, the stronger the cues must be.
  - A blue underlined link carries its meaning with little visual weight. GOV.UK underlines every link (screenshot, 2026-09).
- **Density.** Rank visual weight; don't delete content. Linear's 2026 refresh:
  - dimmed a sidebar that "remained visually prominent even after a user had reached their destination";
  - used fewer and smaller icons;
  - softened separators;
  - kept the density `[UP · C]`.
  
  The cost: users said lost borders weakened section contrast in light mode. Check the contrast of anything you dim.
- **Salience has limits.** Content styled like an ad, or placed where ads usually go, gets ignored. In one study, a large colourful banner was *harder* to find than a text link (Benway & Lane 1998) `[SH · B]`.

## Typography

- **Size.** Reading and comprehension improved up to 18 pt, about 24 px, in a 104-person Wikipedia study; line spacing barely mattered (Rello et al. 2016) `[CH · B]`. Default larger than 16 px for reading-heavy screens. Don't apply this to data-dense tools, and remember that bigger type harms people with tunnel vision.
- **Line length.**
  - Longer lines, up to about 100 characters, are usually read *faster* on screen, but moderate lengths are preferred and may aid comprehension (Dyson 2004 review; 55 characters beat 100 in Dyson & Haselgrove 2001) `[CH · B]`.
  - The specific "45–75 characters" range is a print-derived convention `[DC · C]`. Use a moderate measure for comfort, and don't call it "proven faster".
  - Wikipedia made this default in its 2023 Vector skin, then had to add a user-selectable width after editors objected. The "Appearance" panel now offers text size, width and colour (screenshot, 2026-09).
- **Polarity.** Dark text on a light background is better for acuity and proofreading at all ages, especially at small sizes (Piepenbrock et al. 2013, 2014) `[CH · B]`.
  - Some people with cloudy eye media read faster with light text on dark (Legge 1985, via NN/g).
  - In a 2024 study of chart reading, about half of participants did better in each mode (While & Sarvghad).
  - Dark mode saves 39–47% of display power at full brightness on OLED phones, but only 3–9% at 30–50% brightness (Purdue 2021).
  - Default to light for long or small text, offer dark, and follow the system setting. "Dark mode is better" `[WC · A against]` for normal-vision reading.
- **Optical sizing.** Much of what makes type feel "premium" is display cuts and tighter tracking at large sizes, and text cuts at small sizes. Apple's system font interpolates by point size; Linear uses Inter Display for headings `[UP · C]`. It is cheap and rarely hurts use. Avoid thin weights at small sizes (Apple HIG).

## Colour

- **Never rely on colour alone.** About 8% of men of European descent have red–green colour deficiency (Birch 2012); WCAG SC 1.4.1 applies `[FP · A]`. GOV.UK's error state pairs red with a thick border, the heading "There is a problem", linked text and a hidden "Error:" prefix (screenshot, 2026-09).
- **Colour-count limits** ("never more than X colours", 60-30-10) have no traceable research origin `[AP · D]`.
  - What holds: colour codes work when the categories are few, well separated and backed by a second cue. Search time rose only slightly up to about nine well-separated colours (Smallman & Boynton 1990) `[SH · B]`.
  - Judge each hue by its job.
- **Build palettes so that contrast is guaranteed by rule.** Space the steps by perceived lightness (CIELAB, LCH, OKLCH) and name tokens by role (background, border, text).
  - Stripe (2019): none of its default text colours met 4.5:1, and simply darkening them looked "dark and muddy". After the rebuild, any two colours "at least five levels apart" pass for small text.
  - Linear (2024): moved to LCH and cut its theme inputs from 98 variables to 3, including a contrast control.
  - Vercel's Geist assigns its 10 steps to roles.
  - `[UP · C]`: three team write-ups, sound colour science, no outcome study. Limits: perceptual spaces are only roughly uniform, and some colours don't exist ("very colorful dark yellow").

## Motion

- **Motion helps when it shows what changed and where it went.** Well-designed animated transitions between charts improved perception (Heer & Robertson 2007) `[CH · B]`.
  - In learning studies, animation's apparent benefit disappeared once the static version carried the same information (Tversky et al. 2002).
  - "Animations improve UX" `[WC · B against]` in its blanket form.
- **Failures.** Decorative motion; motion on the path of a frequent task, which adds delay to every repetition; motion for people with vestibular disorders. NN/g on iOS 26: "Motion for motion's sake is not usability" (expert review, 2025).
- **Reduce Motion exists because users got sick.** iOS 7's parallax and zoom effects drew reports of nausea in 2013.
  - Honour `prefers-reduced-motion`. Replace parallax, zoom and depth with fades, and keep small explanatory motion `[SH · C]`.
  - WCAG SC 2.3.3 is only AAA.
  - Don't quote "35% of adults over 40 have vestibular dysfunction". It comes from a balance test on foam (Agrawal et al. 2009), not from sensitivity to on-screen motion.

## Brand expression and "premium" feel

- **Put brand expression in the surrounding layer, and keep text on a controlled background.** Colour at the edges, display type, imagery, and a material or motion layer that respects user settings are all safe. Unsafe: text over backgrounds you don't control, navigation that moves, contrast below the floor, motion on routine actions `[SH · C]`.
- **The case.** Liquid Glass (iOS 26, 2025-09) layered translucent controls over changing content.
  - NN/g reported illegible text, cramped tab bars, and controls that "appear, vanish, collapse, and expand" (expert review; no user testing).
  - Apple kept the look and added a Clear/Tinted switch (iOS 26.1).
  - Then in iOS 27 (announced 2026-06) it added: stronger diffusion, darker edges, uniform toolbars when content scrolls beneath floating bars "to maintain legibility", a clear-to-tinted slider, and adaptation to Reduce Transparency and Increase Contrast.
  - The lesson: when expression can't guarantee contrast, make it adaptive or put it under the user's control.
- **"Premium" feel** seems to come from things that are cheap to see and expensive to fake: consistent spacing, a type scale with optical sizes, a restrained palette with perceptual steps, motion that tracks input, and a response under 100 ms. That last one is invisible in screenshots. `[CH · D]`: synthesis, and no study manipulates "premium".
- **Elegant vs empty.** Minimalism is elegant when what it removed was redundant, and empty when it removed information or signifiers `[CH · D]`.
  - Vercel's home page (screenshot, 2026-09) shows a triangle, "Agentic Infrastructure" and three short lines. It tells a newcomer almost nothing about the product.
  - Google's own Material 3 Expressive research admits that replacing a familiar song list with scattered album art hurt usability.
- **Sameness.** Copying "the Linear look" (dark backgrounds, glows, bento grids) borrows first-impression familiarity, not Linear's speed. Whether sameness helps or hurts trust is unstudied `[D]`.

## Design systems and tokens

- **Tokens make decisions portable, not good.** The W3C Design Tokens Community Group's format reached a stable version, 2025.10. It is a community specification, not a W3C Recommendation. A token system can faithfully spread an inaccessible colour to every platform.
- **Tier your tokens:** primitive values aliased to semantic roles, optionally to component tokens. Then themes (dark, high contrast, sub-brands) change the alias layer only `[UP · C]`.
- **Vendor claims about value are best cases.**
  - Figma: 34% faster with a design system (2019; no sample size; vendor study).
  - Google: key elements found "up to four times faster" in Material 3 Expressive (46 unpublished studies, compared against Google's own older system).
  - `[C]`. The honest mechanism is ordinary hierarchy: a bigger, higher-contrast primary action gets found faster.
- **A design system's publication is not proof.** GOV.UK is a model here: its Tabs page says the component "has not yet been tried in research with users".

## Charts and international text

- **Charts.** People compare position best, then length, then angle and area (Cleveland & McGill 1984, replicated by Heer & Bostock 2010) `[SH · A]`. In pie charts, angle is the least-used cue, and donuts are as accurate as pies (Skau & Kosara 2016) `[C]`. Use bars or dots for precise comparison; pies are fine for rough part-to-whole. Label colours in charts.
- **Translation.** Short strings grow the most, 200–300% for strings under 10 characters (IBM table via W3C; exact figures `[C]`). Don't size buttons to their English text. CJK, Thai, Arabic and Devanagari need more line height. Test with a pseudo-locale.
- **Right to left.** Mirror *direction*, not *objects*. Flip back and next controls, sliders and progress bars. Don't flip logos, photos, checkmarks, clocks or digits (Apple HIG). Use logical CSS properties (start and end, not left and right) `[UP · C]`.
