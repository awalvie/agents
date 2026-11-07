# From direction to code

Read this when you build a direction as one HTML file with no build step. Support facts are as of 2026-09-26, from `web-features` v3.40.0 and caniuse, queried directly. Labels are in `README.md`.

## Choose features by support tier and by failure mode

- A browser drops CSS it does not understand. A missing feature fails quietly (a heading wraps normally without `text-wrap: balance`) or breaks the structure (an anchored tooltip lands in the wrong place). Use quiet failures freely. Use structural ones only when the direction is about that interaction, and name the browser. [SH, B, inferred from the stated mechanism]
- Safe as structure (Baseline widely available): grid, flex `gap`, `clamp()`, `min()`, `max()`, custom properties, `aspect-ratio`, logical properties, cascade layers, size container queries, `:has()`, native nesting, `oklch()`, `color-mix()`, subgrid, `pow()`, `<dialog>`, `<details>`, `:user-invalid`, `inert`, import maps, `system-ui`, small, large and dynamic viewport units, media-query range syntax. [fact, A, stated]
- Fine with an acceptable fallback (newly available): `light-dark()`, `text-wrap: balance`, `@property`, relative colour syntax, `@starting-style`, popover, exclusive `<details name>`, same-document view transitions, invoker commands, `@scope`, `contrast-color()`, container style queries, `field-sizing`, `sibling-index()`. [fact, A, stated]
- Enhancement only (limited): `text-wrap: pretty`, scroll-driven animations, cross-document view transitions, `text-box` trim, `if()`, `@function`, `interpolate-size`, customizable `<select>`, `initial-letter`, `corner-shape`, grid lanes (formerly masonry). Anchor positioning: most parts newly available since 2026-01-13, but the feature is limited in `web-features` and partial in caniuse; it fails structurally, so treat it as enhancement. [fact, A, stated]
- Baseline is not a checklist: it ignores browsers outside the core set (Brosset 2025), and a feature query tests only basic support (MDN). [SH, B, stated]

## Tokens

- A token is a named design decision. In one file, it is a CSS custom property on `:root`. Tiers exist to create one place to swap: components use a meaning (`--text-muted`), the meaning points to a raw value (`--gray-6`), and a new theme or direction rewrites only the middle layer (DTCG format 2025.10 on aliases; Curtis 2020). GitHub's Primer uses three tiers; Salesforce, which coined the term, now uses plain custom properties, since it lives on one platform (D'Amato 2025). [UP, C, stated]
- For a prototype, two tiers are enough: roughly 5 to 8 raw colours mapped to 8 to 12 roles such as surface, text, muted, accent, border, focus, danger and success (the researcher's suggestion, not measured). Keep component tokens local until several components share one (Curtis 2020). [UP, C, inferred]
- Custom properties cannot be used in media or container query conditions, and an invalid substituted value falls back to the inherited or initial value (MDN). `@property` adds type checking. [fact, A, stated]

## Scales

- Build the scale with `calc()` and `pow()`: `calc(1rem * pow(var(--ratio), 3))` needs no build step and rendered in Firefox 156 (the researcher's test). *Every Layout* uses a ratio of 1.5, taken from a body line height of 1.5. [UP, C, stated]
- Ratio-based scales and hand-picked scales disagree. Refactoring UI prefers hand-picked sizes, because ratios give too few useful small sizes (read only through secondary notes). Dense tools need many small, close sizes, and editorial pages need a few clear jumps, so the answer depends on density. [CH, C, inferred]

## Fluid type and space

- Instead of jumping at breakpoints, set a small-screen scale and a large-screen scale and let `clamp()` interpolate (Riethmuller 2015; Utopia, Gilyead & Mudford 2020, e.g. ratio 1.2 at 320 px, 1.333 at 1500 px). It matters most where display type carries the identity. [UP, B, stated]
- The `vw` part of the formula does not grow with browser zoom. Keep each step's maximum at most 2.5 times its minimum, so that text still reaches 200% at the browser's maximum zoom (Barvian 2023, a derivation, not a user study). Example: `--step-3: clamp(1.75rem, 1.2rem + 2.5vw, 3rem)`. [UP, B, stated]

## Layout: intrinsic or explicit

- The intrinsic school lets the browser decide by giving it goals: wrapping, `flex-basis`, `min()`, `ch`, auto-fit grids (Simmons 2018; *Every Layout*). The Switcher, `flex-basis: calc((40rem - 100%) * 999)`, puts items in a row above a threshold and stacks them below it, with no media query (Pickering 2019). The explicit school sets thresholds: viewport media queries for the page shell, container queries for components. Put breakpoints where the content breaks, not at device sizes (Hay, 2012). [CH, C, stated]
- Container queries need a wrapper, because a container cannot query itself. Block-size queries collapse without an explicit height (Ayomipo 2026; MDN). A component that follows its container does not follow the viewport: in the researcher's test, cards were wide at 420 px, compact at 900 px, wide at 1500 px. [fact, A, stated] Container style queries (newly available) can query a custom property's value, so one file could switch a component's style by a direction variable. [UP, C, inferred]
- Use intrinsic layout when content and slots vary. Use explicit thresholds when the direction depends on a precise composition at known sizes, such as a poster-like hero. Use media queries for user preferences such as `prefers-color-scheme` and `prefers-reduced-motion`, which container queries cannot read. Intrinsic layouts drift toward stacks and even columns, so an asymmetric direction needs explicit control. [CH, C, inferred]

## Organize the cascade

- Cascade layers set precedence by order, not by specificity. The last listed layer wins, and unlayered styles beat all layers (MDN). A single file can open with `@layer reset, tokens, layout, components, exceptions;`. Stripe and Linear declare layers in production (observed 2026-09-26). Native nesting cannot join selector fragments the way Sass `&__el` does. [UP, B, stated]
- Utility-first (Wathan 2017) and cascade-first (*Every Layout*; CUBE CSS) disagree. For directions that share markup, cascade-first with tokens swaps more easily, because the direction lives in the stylesheet. Tailwind's in-browser script needs no build, but its docs call it development-only. [CH, C, inferred]

## Colour as a formula

- In a perceptual space, lightness steps look equal across hues. So a palette can be a few seeds plus rules: `oklch(from var(--brand) calc(l + .35) calc(c * .3) h)`, `color-mix()`, and `light-dark()` with `color-scheme: light dark`. Changing one seed changes the direction's colour. HSL cannot do this, because its lightness is not perceptual (Ottosson 2020; Sitnik & Turner 2025). [SH, B for uniformity. UP, C for formulas. Stated]
- Limits: each hue has a different maximum chroma, many OKLCH values fall outside sRGB, and browsers clip them, so one chroma formula can clip some hues and not others. A given brand palette in hex should be mapped, not generated. Look at the result on its real ground (`visual.md`). [SH, B, stated]

## What code gains and loses

- A prototype answers some questions and leaves others incidental (Houde & Hill 1997). In a survey of 259 designers, 86% said behaviour is harder to prototype than appearance (Myers et al. 2008). Code is strong for behaviour, states, reflow, real text and real rendering (Hay 2014; GDS 2012; Freiberg 2023). Budd (2012), Parmenter (2012) and Mall (2012) say it is weak for fast, rough visual divergence, and Budd adds that it pulls toward a minimal look. [SH, B, stated]
- The losses concern divergence, and the gains concern convergence. An agent pays no drawing cost, so its main risk is committing too early to one structure; differing in the spec before markup is one guard (`core.md`). [CH, C, inferred]

## Shared or separate markup

- Directions that share one HTML file and differ only in CSS can look very different, but they cannot change structure, order or content. CSS Zen Garden needed six empty `extra` divs so designers had something to style (observed 2026-09-26). Shared markup suits directions that differ only in visual language, and makes the comparison fair; separate markup suits differences in structure, flow, density or content priority. [UP, C, stated]

## Units, states and fonts

- Choose a unit by what the size should follow: `rem` for type and block spacing, `em` for things inside text such as icons, `ch` for the measure, `px` for hairlines (*Every Layout*). `1ch` is the width of "0", so `60ch` varies by font. [SH, B, stated]
- Native HTML and CSS now show most states without a framework: `<dialog>`, `<details>`, popover, `:has()` for a parent's state, `:user-invalid`, and `@starting-style` for entry transitions. Script can then be kept for behaviour that is the point of the direction. [fact, A, stated for support. UP, C, inferred for the practice]
- A system font stack loads nothing and looks native, and it carries the platform's voice, not the direction's. `ui-sans-serif` and its relatives work only in Safari (caniuse). On Japanese-locale Windows `system-ui` resolves to Yu Gothic UI, which renders some characters wrongly, so Tailwind dropped both from its default stack (PR #20318, 2026-07-14). A direction whose identity is its type needs a chosen font, embedded or from a service, with a named fallback. [CH, C, stated]
