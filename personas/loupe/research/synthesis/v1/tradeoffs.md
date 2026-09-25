# Design tradeoffs

Read this file when a recommendation would improve one thing by worsening another. None of these has a universal answer. For each tension: what each side optimises, who gains and who loses, the variables that decide it, the evidence, and an example. Labels as in [core.md](core.md).

| Tension | Side A optimises (who gains) | Side B optimises (who gains) | Deciding variables | Evidence | Example |
|---|---|---|---|---|---|
| **Simplicity vs discoverability** | Clean surface (people who already know the hidden actions) | Findability (first-time and occasional users) | How often the feature is used; whether any signifier or labelled entry point exists | Hidden navigation cut use and speed `[SH · B]` | Apple Photos removed tabs, then restored them |
| **Efficiency vs learnability** | Speed through recall and shortcuts (daily experts) | Ease through recognition (novices) | Frequency of use; whether training is mandated | Users rarely move to shortcuts unprompted `[SH · B]` | Bloomberg vs the Office Ribbon; bridged by command palettes |
| **Consistency vs task fit** | Transfer of learning (people who switch between many tools) | Speed on the frequent task (specialists) | Frequency; how many other tools users move between | Grudin 1989 `[SH · B]` | Calculator + beside Enter |
| **Density vs readability** | Overview and fewer screens (scanning experts) | Comfort (first-time readers) | Task (scanning or reading); how hierarchy is ranked | Longer lines read faster but preferred less `[CH · B]`; no controlled study of expert dashboards | GitHub, Bloomberg vs GOV.UK |
| **Progressive disclosure vs visibility** | Protection from error states (novices) | Nothing hidden (everyone who needs the hidden part) | Is the hidden item rare or core? | Blocking functions novices didn't need sped learning (Carroll & Carrithers 1984) `[B]`; hiding costs discovery `[B]` | GOV.UK: "test your content without an accordion first" |
| **Personalisation vs predictability** | Relevance (people who never customise) | Spatial memory (habitual users) | Prediction accuracy; does adaptation add or move items? | Accuracy mattered more than predictability; moving items hurts `[SH · B]` | Office's self-hiding menus replaced by the Ribbon; Snapchat's algorithmic Stories |
| **Automation vs user control** | Effort saved (the typical case) | Correctness and override (specialists, edge cases) | Is the change visible, reversible, and at what cost when wrong? | Automation leaves operators the hardest tasks (Bainbridge 1983) `[SH · B]`; Excel's gene-name errors | Excel conversions; GitHub's 4.7% stale cache |
| **Brand expression vs legibility** | Distinctiveness, first impression | Contrast, stable controls (low-vision users, everyone in bright light) | Does text sit on a background the designer controls? Can users adjust the effect? | `[CH · B/C]` | Liquid Glass, then iOS 26.1 and iOS 27 fixes |
| **Delight and motion vs speed and comfort** | Explaining where things went; character | No added delay; vestibular safety | Is the motion essential? Is it on a frequent path? Is Reduce Motion honoured? | Transitions aid perception `[CH · B]`; the blanket claim `[WC · B against]` | iOS 7 motion sickness; Reduce Motion |
| **Error prevention vs speed** | Protection in the rare bad case | Speed in every normal case | Is the action reversible? How often does it occur? | Habituation `[FP · A]` | Gmail Undo Send vs GitHub's type-to-confirm |
| **Inline help vs interruption** | Early correction (long forms, hard fields) | Uninterrupted entry (slow typists, screen-reader users) | Page length; breadth of the audience | Wroblewski 2009 vs GOV.UK `[CH · C]` | Checkout vs GOV.UK service |
| **Perceived speed vs correctness** | Feeling instant | Truthful state | Stakes; reversibility; tolerance of staleness | `[UP · C]` | Linear's optimistic sync; GitHub's cache |
| **Guidance vs autonomy** | A clear next step (beginners) | Choice of order (experienced learners) | Expertise; whether the goal is completion or exploration | Company data only `[C]` | Duolingo's 2022 path |
| **Business goals vs user goals** | Conversion, retention, cross-selling | The user's task and trust | Symmetry of effort; disclosure; regulation | Mild deceptive patterns double sign-ups `[SH · B]`; regulator actions | Amazon Prime, Spotify Home 2023, Pinterest's login wall |
| **Distribution vs goodwill** | Growth loops (sign-up walls, visible apps) | Getting to the goal without detours | Is the user arriving with a goal elsewhere? | Press and user reports `[C]` | Pinterest; Dropbox 2019 |
| **Evidence-based default vs expert preference** | Outcome for the majority | Habit of vocal experts | Who was measured and who complains | `[C]` | Wikipedia's width control |

**Recurring resolutions**, each qualified:
- **Two paths linked together** (recognition and recall). They work when the fast path is shown inside the slow one. Whether this *causes* users to migrate is unverified.
- **Add, don't move.** Additive change protects experts. It can freeze a design that has already hit its limit (Bloomberg).
- **Hand the tradeoff to the user** with a setting (Wikipedia's width, Apple's Tinted switch, Netflix's autoplay toggle). Most people never change settings, so the default still decides what most users experience. Don't use a toggle to excuse a bad default where legibility or control is at stake.
- **Put friction where the user's future self would want it** (Monzo, Zerodha). The same mechanism, aimed at the business's goal, is obstruction.
