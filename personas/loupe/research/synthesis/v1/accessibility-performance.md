# Accessibility and performance

Read this file for any accessibility judgement, for touch targets, contrast, errors reaching assistive technology, loading and perceived speed. The standard is WCAG 2.2 (W3C Recommendation, 2023-10-05) unless stated. Labels as in [core.md](core.md).

## Accessibility

**Conformance is the floor, not the goal.**
- Of the problems 32 blind users met on 16 sites, only 50.4% were covered by WCAG 2.0 criteria. Where a criterion did apply, the recommended techniques sometimes didn't solve the problem (Power et al. 2012) `[FP · B]`.
  - This is dated: WCAG 2.0, blind users only. WCAG 2.2 added criteria such as target size, consistent help, redundant entry and accessible authentication, but has no equivalent study.
- The W3C's own cognitive-accessibility guidance covers barriers "that could not be included" in WCAG (COGA note, 2021). Its demands are plain language, stable layouts, no memory tests, and forgiving errors. No checker flags them `[SH · B/C]`.

**The measurable web is getting worse** (WebAIM Million 2026, top million home pages; a measurement, `A` for its scope):
- 95.9% of pages had detected failures, averaging 56.1 errors per page.
- The most common failures:
  - low-contrast text, 83.9%;
  - missing alt text, 53.1%;
  - missing form labels, 51%;
  - empty links, 46.3%;
  - empty buttons, 30.6%.
- Pages with ARIA averaged more errors (59.1 against 42). This is a correlation, and page complexity confounds it.
- Implications:
  - Low contrast is a visual designer's problem.
  - Adding ARIA is not accessibility; native HTML comes first.
  - "No detected errors" does not mean accessible.

**Overlays don't deliver conformance** `[anti-pattern · B]`. The FTC fined accessiBe $1M (order 2025-04-22) for claiming its AI tool could make any site WCAG-compliant.

**Headings are how screen-reader users navigate.**
- 71.6% navigate long pages mainly by headings, and only 3.7% mainly by landmarks (WebAIM Screen Reader Survey #10, 2024, 1,539 self-selected respondents) `[SH · A–B]`.
- The most problematic items they report: CAPTCHA, unexpected behaviour of interactive elements, ambiguous links and buttons, and missing keyboard access.
- Every visual heading must be a real heading at the right level. Mark the levels in design hand-off.

**Errors must reach assistive technology.** GOV.UK's pattern `[UP · C]`; the research behind it is described but not published:
- On submit, show an error summary at the top, and move focus to it.
- Prefix the page title with "Error:".
- Link each item in the summary to its field, using the same words as the message beside the field.
- Associate the field message with `aria-describedby`, plus a visually hidden "Error:" prefix.

Roselli's tests across NVDA, JAWS, Narrator, VoiceOver and TalkBack (2023) found `aria-describedby` the most reliable. `aria-errormessage` was often not announced, and assertive announcements as the user leaves a field can cut off the next field's name `[C]`. For validation *timing*, see [interaction.md](interaction.md).

**Honour the user's own settings, because needs conflict.**
- Some people need high contrast. People with light sensitivity find bright backgrounds painful. Most low-vision users need large text, but people with tunnel vision may want it small, and needs change with fatigue (W3C low-vision requirements draft, 2016) `[FP · B]`.
- Support:
  - text resize to 200% (SC 1.4.4);
  - reflow at 320 CSS px (SC 1.4.10);
  - text-spacing overrides (SC 1.4.12);
  - OS contrast, transparency and motion settings;
  - light and dark modes.
- Prefer a set of assists people can combine over one "accessible mode". The Last of Us Part II has more than 60 settings, and a blind reviewer played it without sighted help; but text-to-speech was off at first launch (Can I Play That?, 2020).
- Words decide whether an accommodation gets used. Celeste renamed "Cheat Mode" to "Assist Mode" after feedback from disabled players (Vice, 2019).
- "Accessibility helps everyone" `[WC]`: some accommodations harm another group. "Accessible features are often used widely" `[SH · B]`.

**Touch targets: the rules rest on thin, old evidence.**
- **The study.** Parhi, Karlson & Bederson (2006): 20 right-handed, mostly male computer-science students, using a 2005 stylus-era device with the thumb. Errors stopped improving at about 9.6 mm; the authors recommend 9.2 mm for single taps and 9.6 mm for taps in sequence.
- **The rules.**
  - WCAG 2.2 SC 2.5.8 (AA): 24 × 24 CSS px, or enough spacing, with exceptions. Its supporting document cites only Parhi and doesn't show how 24 was derived.
  - SC 2.5.5 (AAA): 44 × 44.
  - Apple: 44 pt default, 28 pt minimum.
  - Android: 48 dp.
- **The arithmetic** (approximate): 44 pt ≈ 7.3 mm, 48 dp ≈ 7.6 mm, 24 CSS px ≈ 4 mm on a phone. **Every platform default is below the 9.2 mm the cited study recommends.** The claim sometimes made that platform guidance "points to 9–10 mm" is wrong on this arithmetic.
- **Labels.** "Bigger targets reduce errors, with diminishing returns around 1 cm" `[SH · B]`. "24 px is enough" is a legal floor `[DC]`, not an ergonomic threshold `[D]`.
- **What to do.** Use 44 pt / 48 dp as normal and 24 px as the floor. Give destructive and frequent targets about 1 cm plus spacing. Modern capacitive screens are more accurate than 2005 hardware, and spacing matters about as much as size.

**Canvas and custom-rendered apps start at a deficit** `[SH · B]`.
- Figma: a canvas "strips away any accessibility the browser gives you for free". It built a hidden, synchronised DOM (team blog, 2026-07). There is no third-party audit.
- GitHub's code view: rendering only the visible lines broke browser find. The fix was a hidden textarea holding the whole file (team blog, 2023).
- GitHub's own audit (2026-09-08) still lists many open issues: for example, 14 high-priority keyboard issues, 13 high-priority reflow issues, and 59 medium-priority status-message issues.
- Canva's 2021 audit marked keyboard access and focus order "Does Not Support" for the editor canvas. It is outdated, and the current state is unverified.
- Before choosing custom rendering, list the native behaviours you will lose (find, selection, focus order, history, the accessibility tree), and budget to rebuild each one.

**Contrast.**
- **Where the numbers come from.** WCAG's 4.5:1 compensates for vision of about 20/40; 3:1 is the ISO/ANSI figure for normal vision (W3C Understanding 1.4.3) `[DC]`, with a legal role. That more luminance contrast helps low vision is `[B]`.
- **APCA**, a proposed perceptual measure, argues that the WCAG ratio misjudges dark pairs and light text on mid-tones.
  - Its "false passes" were defined against APCA itself, which is circular, and its supporting data were unpublished.
  - It was removed from the WCAG 3 drafts in 2023. As of April 2026, the WCAG 3 contrast method is "yet to be determined".
  - Pass WCAG 2.2 for conformance. For dark themes and mid-tone brand colours, also check a perceptual measure and your own eyes. Distrust tools that call APCA "the WCAG 3 method". "WCAG 2 mis-ranks some pairs" `[CH · C]`; "APCA is correct" `[WC · D]`.

## Performance as users feel it

**Thresholds.**
- 0.1 s feels instant `[SH · B]`: the perception research agrees (Michotte, cited by web.dev).
- 1 s keeps the flow of thought, and 10 s is the limit of attention `[SH · C]`. These are reasoned estimates from Miller 1968 and Card et al. 1991, not measured breakpoints.
- So: no indicator under 0.1 s; subtle feedback at about 1 s; over 10 s, show determinate progress, a cancel option, and let the user do something else.

**Numbers not to cite.**
- **"The Doherty threshold of 400 ms".** "400 ms" does not appear in the reprinted 1982 IBM paper it is credited to `[WC · D]`. An earlier note graded it C; it is downgraded because a researcher read the reprint and found no such figure. The paper does support "sub-second response raised productivity on 1980s mainframes" `[CH · C]`.
- **"53% of mobile visits are abandoned after 3 seconds"** (DoubleClick 2016). The source has no definition of abandonment and no method, and was published by an ad business `[WC · D]`.
- **"Optimistic UI cuts perceived wait by 40%".** Untraceable.

**Core Web Vitals are partly perceptual and partly chosen to be achievable** `[DC · C]` as perceptual thresholds.
- LCP 2.5 s was picked partly because 42% of phone origins already met it.
- INP 200 ms is above the 100 ms perceptual limit.
- CLS 0.1 came from internal testing, because "no prior research existed".
- All are assessed at the 75th percentile (web.dev).
- Passing Core Web Vitals is not the same as feeling instant. For direct input such as typing, dragging and toggles, aim for 100 ms.

**Perceived speed can be shaped, a little.**
- Progress bars that speed up toward the end felt faster, and pauses near the end felt slower (Harrison et al. 2007, 22 people). Backward-moving ribbing made a 5 s bar feel about 12% shorter (Harrison et al. 2010; small student samples, attention on the bar) `[CH · B]`.
- "Show progress and structure during waits" `[SH · B]`.

**Skeleton screens are not proven faster.** The evidence conflicts, and the stronger test goes against them.
- Viget (2017; 136 people, animated GIFs of equal-length loads) found the spinner rated fastest: 74% agreed it "loaded quickly", against 59% for the skeleton. Perceived waits were 2.41 s for the spinner, 2.82 s for the skeleton and 2.29 s for a blank screen (verified on Viget's page, 2026-09-25).
- Mejtoft et al. (2018) found no significant difference.
- NN/g's advice to use skeletons for full-page loads rests on the Mejtoft study.
- "Skeletons feel faster" `[WC · C]`. The defensible reason to use one is a stable layout and a preview of structure. Test it against a spinner, and make sure it matches the final layout, or it adds layout shift.

**Measure what the user sees, and state what you trade for it** `[SH · B]`, from several independent first-party measurements.
- Pinterest defined "user perceived wait time" as the time until the visible images load. In its 2015 experiment, landing pages were 60% faster and mobile sign-ups rose 40% (team blog, 2017, read directly).
- GitHub sets its own tiers (instant under 200 ms, fast under 1 s). A local cache cut its Issues median from about 1,200 ms to 700 ms, accepting about 4.7% stale data (team blog, 2026-05).
- Notion's move to WASM SQLite made page navigation 20% faster, but not the first load (team blog, 2024).

**Optimistic UI makes an app feel fast only when the architecture can keep its promises.** Linear applies changes to a local in-memory store at once, queues them to the server, and rolls back on failure (a reverse-engineered write-up endorsed by Linear's CTO) `[UP · C]`. Use it for low-risk, reversible actions such as status or assignee. For money or irreversible actions it is an anti-pattern.

**Counterexample to "every millisecond costs conversions".** At Etsy (about 2012), an experiment that deliberately slowed search results changed nothing measurable in purchases (team talk). That was one site, one experiment. Speed effects depend on task and baseline `[C]`.
