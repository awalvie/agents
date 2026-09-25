# Design review knowledge base: index

This is a synthesis of five independent research passes (foundations, visual and accessibility, interaction, criticised products, praised products), done 2026-09-25. It is written for a design reviewer that reviews websites and apps of any kind.

**Read every time:** this file and [core.md](core.md). Core holds the ten principles, the review framework, the main tradeoffs, and short answers to the deeper questions (what makes something intuitive, trustworthy, fast).

**Read when the review needs it:**

| File | Holds | Read when reviewing |
|---|---|---|
| [interaction.md](interaction.md) | Navigation, search and filters, forms and validation, UX writing, feedback and states, undo and confirmation, defaults, gestures, shortcuts, onboarding, personalisation, a pattern catalogue with failure modes, anti-patterns, deceptive patterns and regulation, AI features | Any flow, form, menu, dialog, list, onboarding, subscription or checkout, AI output |
| [visual.md](visual.md) | Hierarchy, signifiers, density, type, colour, motion, brand expression, "premium" vs "empty", design systems, charts, translation and right-to-left layout | Screenshots, landing pages, visual redesigns, dashboards |
| [accessibility-performance.md](accessibility-performance.md) | WCAG 2.2 as the floor, errors reaching assistive technology, headings, touch targets, contrast and APCA, canvas apps, response-time thresholds, Core Web Vitals, perceived speed, skeletons, optimistic UI | Any accessibility claim, a mobile UI, loading states, speed |
| [products.md](products.md) | Benchmarks, counterexamples and poor examples, indexed by lesson | When you need a real product to compare with or cite as an alternative |
| [tradeoffs.md](tradeoffs.md) | Sixteen tensions: who gains, who loses, what decides it | Before recommending any change that improves one thing by worsening another |
| [uncertainty.md](uncertainty.md) | Conflicts, label changes, where the output leans, topics not covered, weak evidence, figures not to cite | Before quoting a number, stating a finding as settled, or citing a product not listed |
| [vocabulary.md](vocabulary.md) | Terms commonly confused (affordance vs signifier, minimal vs simple, accessible vs conformant…) | When wording a finding precisely |
| [sources.md](sources.md) | The source library by subject, with links and how each was read | When you need to cite or check |
| [SUMMARY.md](SUMMARY.md) | One page for non-designers | Explaining the approach to a stakeholder |
| [skeptic-log.md](skeptic-log.md) | What a checking pass changed, confirmed and left open | Auditing this output |

**Labels.** Every finding carries `[kind · evidence]`. Kinds: FP fundamental principle, SH strong heuristic, CH context-dependent heuristic, UP useful pattern, DC design convention, AP aesthetic preference, WC unsupported or weak claim. Evidence grades run from A (strong) to D (none). The full key is in [core.md](core.md).

**Two cautions.** Never present a C- or D-graded finding as a law. From a screenshot, report accessibility problems as "possible failure, needs checking", never as conformance or failure.
