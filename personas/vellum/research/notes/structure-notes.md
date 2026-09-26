# Area 2: Structure and interaction as design choices

Scope: how a designer produces several different options for the structure of a product
(organization, navigation, flows, states, content, motion), and what each option trades. It
does not cover how to test or evaluate them.

Method: sources read 2026-09-26. Full list and depth of reading in `structure-sources.md`.
Screenshots in `structure-shots/`.

Labels. Kind: fundamental principle, strong heuristic, context-dependent heuristic, useful
pattern, design convention, aesthetic preference, unsupported claim. Strength: A to D as in the
brief. "Stated" means the source says it. "Inferred" means I drew it from the sources.

Coverage check. Rosenfeld, Morville & Arango, *Information Architecture* (4th ed., 2015). I
could not get the full text. I read it through Google Books search-inside snippets of chapters
6 (organization systems), 10 (faceted classification) and 12 (metaphor exploration). Findings
1 to 3 quote those snippets. Treat my reading of the book as partial.

---

## Finding 1. Choose the organization scheme by the kind of seeking, and know that mixing schemes costs the mental model

Claim. Every structure starts from a scheme: how items are grouped. Exact schemes
(alphabetical, chronological, geographical) put each item in one obvious place. Ambiguous
schemes (topic, task, audience, metaphor) group by meaning, and the designer has to make
judgment calls. Exact schemes serve people who know the name of what they want. Ambiguous
schemes serve people who do not.

Evidence.
- Rosenfeld et al. (2015, p. 130), stated: "Exact schemes are best for known-item searching,
  when users know precisely what they are looking for. Ambiguous schemes are best for browsing."
- The mechanism, stated (p. 109): people find ambiguous schemes useful because "we don't always
  know what we're looking for… you simply don't know the correct label." Ambiguous schemes
  "require more work and introduce a messy element of subjectivity," but "often prove more
  valuable to the user than exact schemes."
- On hybrids, stated (p. 114): "The power of a pure organization scheme derives from its
  ability to suggest a simple mental model that users can quickly understand." When audience,
  topic and task labels sit together in one list, users cannot form that model. The authors
  accept hybrids "within the surface layer of navigation" and say the problems start when a
  hybrid organizes a large volume of content (p. 115).
- Audience schemes fit "where there are two or more clearly definable audiences" (p. 112).
  Metaphor schemes relate "the new… to the familiar," but a feature the metaphor cannot hold
  forces you to "break out of the metaphor, introducing inconsistency" (p. 113).

Counterevidence and limits. The known-item versus browsing split is stated as guidance, not as a
measured result in the pages I saw. Yee et al. (2003) give indirect support. For a simple
single-facet task ("find images of roses"), about 50% of their 32 participants preferred a plain
keyword interface to the faceted one. For the other task types, most preferred the faceted one.

Example. Craigslist's home page (screenshot `craigslist-sfbay-home-2026-09-26.png`, 2026-09-26)
nests schemes deliberately. Geography comes first and is exact (the city, then sub-areas such as
sfc, sby, eby). Inside that, the page groups by topic (housing, jobs, for sale). The book uses
Craigslist as its example of a geographical scheme (p. 108). The page never mixes the two
schemes in one list.

Labels. Strong heuristic, B (consistent expert guidance plus one study on the preference split).

Use. When generating directions, give each direction a different primary scheme: by task, by
audience, by topic, by an exact attribute. This produces real structural alternatives instead
of variations in visual style (inferred). Avoid a primary scheme that mixes kinds in one list,
unless the list is short and at the surface. Avoid audience schemes when users do not identify
with one audience, or belong to several.

---

## Finding 2. Hierarchy, database (facets) and hypertext are three different structures, and each suits a different shape of content

Claim. After the scheme comes the structure: a tree, a set of records with attributes, or a web
of links. The shape of the content decides which one fits.

Evidence.
- Rosenfeld et al. (2015), stated: "The hierarchy is a good place to begin, but it is only one
  component in a cohesive organization system" (p. 122). The database model "is particularly
  useful when applied within relatively homogeneous subsites such as product catalogs and staff
  directories" (p. 126). Hypertext "is rarely a good candidate for the primary organization
  structure… it can be used to complement structures based upon the hierarchical or database
  models" (p. 127).
- Facets, stated (p. 303): Ranganathan built his classification on the idea that "documents and
  objects have multiple" dimensions. This replaced the question "Where do I put this?" The
  authors list common business facets: topic, product, document type, audience, geography, price
  (p. 304).
- Yee et al. (2003, CHI) tested a faceted interface ("Flamenco") on 35,000 art images with 32 art
  history students, against a keyword baseline. 91% preferred the faceted interface overall, and
  participants "felt significantly more confident that they had found all of the relevant
  images." The measures were mostly subjective, because "there are no correct answers" in
  browsing tasks.

Counterevidence and limits. Facets need clean, consistent metadata on every item. Without it
they fail (inferred from the p. 124 remark that metadata is "the primary key"). Yee et al. say
the faceted interface was an order of magnitude slower to compute. Participants who preferred
the baseline "commented on its simplicity and stated that the categories felt too restrictive."

Labels. Strong heuristic, B.

Use. Ask what the content is made of. Many items with the same attributes: use facets and filters
as the main structure. Few items of mixed kinds: use a hierarchy. Ideas that relate across
branches: add hypertext links on top, but not as the main structure (inferred from the book).

---

## Finding 3. Breadth versus depth: the cost is the number of category decisions and how distinct the labels are, not the number of clicks

Claim. A flatter hierarchy usually beats a deeper one. The reason is that each level asks for a
categorical decision, and a decision costs more than scanning a longer list. But very broad top
levels have their own cost, and label quality ("scent") matters more than the count.

Evidence.
- Larson & Czerwinski (1998, CHI; full text read). 19 experienced web users searched 512
  encyclopedia items in three structures: 8x8x8, 16x32 and 32x16. Mean times were 36 s for
  16x32, 46 s for 32x16 and 58 s for 8x8x8. The 3-level tree was significantly slower than both
  2-level trees. The difference between the two 2-level trees was not significant. The mean
  lostness score was 0.35 for 16x32, 0.49 for 32x16 and 0.63 for 8x8x8.
- Their explanation, stated: the 2-level structures "most likely afforded optimal performance
  because their category labels were more distinct at the top levels (better scent)." The
  8x8x8 tree "suffered from the fact that subjects had to make another categorical decision."
  16x32 may have beaten 32x16 because "there were fewer categorical judgments to be made at the
  top level." Designers "need to balance the number of categorical decisions… against the
  number of items needing to be visually searched."
- Earlier menu studies, as the same paper reports them. D. Miller (1981): with 64 items, 8x8 gave
  the fastest acquisition and fewest errors among 2^6, 4^3, 8^2 and 64^1. Kiger (1984): 4x16 was
  fastest, but not reliably faster than 16x4 or 8x8. Snowberry et al. found that memory span did
  not predict performance, but visual scanning did.
- The "7 plus or minus 2" figure does not decide menu length. Larson & Czerwinski, stated: "At the
  onset of this study the authors were convinced that short-term memory limitations would play
  an important role… Instead we have shown that memory is only one variable."
- Click count. Porter (2003, UIE) analyzed 44 users, 620 tasks and more than 8,000 clicks:
  "there wasn't any more likelihood of a user quitting after three clicks than after 12 clicks."
  Complaints about clicks "are really complaints about failing to find something."
- Theory. Pirolli & Card (1999; abstract read): information foraging. People adapt their
  strategies "to maximize their rate of gaining valuable information." Information scent is the
  cue each link gives about what is behind it.
- The IA book agrees, stated (p. 121): lean "toward a broad-and-shallow rather than a
  narrow-and-deep hierarchy" when the site will grow.

Counterevidence and limits. Larson & Czerwinski had 19 people, one content set, and categories
built by experts but not tested with users. Their own result argues against extreme breadth:
the 32-wide top level was slower and more "lost" than the 16-wide one. The early menu studies
used small item sets and gave participants only the target word.

Labels. Breadth over depth: strong heuristic, A to B (several studies that agree, all small
and mostly on menus). Label distinctness as the mechanism: context-dependent heuristic, B. The
"three-click rule": unsupported claim, C against it. "7 plus or minus 2 per menu": unsupported
claim.

Use. To generate options, vary the depth and the top-level labels, not the click count.
Compare options by counting the decisions a user must make on the most important paths and
checking whether each label predicts its contents (inferred).

---

## Finding 4. Object-first structure (nouns before verbs) is a real alternative to task-first or department-first structure

Claim. You can derive the structure from the things in the domain and their relationships
("one page per thing"), instead of from a tree of pages or a list of tasks. Navigation then
comes from the links between things. The same idea at the interaction level is the noun-verb
command order: select the object, then the action.

Evidence.
- Smith, Irby, Kimball, Verplank & Harslem (1982, *Byte*; full text read), on the Xerox Star,
  stated: "Commands in Star take the form of noun-verb… This helps make the command interface
  modeless; you can change your mind as to which object to affect simply by making a new
  selection before invoking the command." Star used a small set of "universal" commands (MOVE,
  COPY, DELETE, SHOW PROPERTIES…) that "perform the same way regardless of the type of object
  selected."
- The same paper names the limit, stated: "General mechanisms are often inconvenient for
  high-frequency actions." The team added dedicated keys for bold and italics because SHOW
  PROPERTIES "is too much of an interruption during typing."
- Prater (2015, *A List Apart*), Object-Oriented UX. Design "real-world objects before
  procedural actions." Method: pick the nouns out of the brief, define each object's content and
  metadata, and nest objects to find cross-links, so that "users get to content through content."
  This is a practitioner method with no outcome data.
- BBC (Raimond, Scott et al., W3C case study, 2010): "a web identifier, with associated HTML
  pages… for every programme the BBC broadcasts." Links between programmes, artists and species
  gave "rich cross-domain user journeys." Scott (2009; abstract): "throw out the Photoshop and
  embrace Domain Driven Design."
- Aalen (2015, *A List Apart*), the core model, developed by Are Halland (IA Summit 2007).
  Design the pages where user tasks meet business goals first. Then design their inward paths
  (search, links) and forward paths. Design the home page last, because many users arrive on
  deep pages from search. Her team reports that a Norwegian Cancer Society redesign raised
  one-time donations by 198% and regular-donor income by 382% within two years. This is the
  team's own report and does not isolate the structural change.

Counterevidence and limits. Object-first structure is weak for linear, task-driven products
such as tax filing or checkout, where the user wants a path and not a web (inferred; compare
Finding 8). Domain models need editorial or data upkeep, and the BBC admits that much legacy
content "has not been created… with semantic web principles in mind." In the Star's own
account, a generic command model had to be broken for speed.

Example. The BBC Programmes page (screenshot `bbc-programmes-desert-island-discs-2026-09-26.png`,
2026-09-26). One page per programme, with episodes, collections and people linked from it.
There is no "Radio > Speech > Interviews" tree to walk.

Labels. Noun-verb order as an interaction structure: useful pattern, C (a designed and tested
product, but no controlled comparison in the source). Object-first IA: context-dependent
heuristic, C.

Use. Good as a distinct direction when the domain has many connected entities (media, catalogs,
people, places, records) and people arrive from search. Poor as the main structure for a single
linear task, or where the entities are not stable.

---

## Finding 5. Navigation models are a palette. Different levels of one product can use different models.

Claim. There is a small set of navigation models, and a structure option is largely a choice of
model at each level: hub-and-spoke, flat (tabs or sidebar), drill-down (tree), pyramid
(siblings linked), step-by-step, pan-and-zoom, content-driven (hypertext), and modal overlays.

Evidence.
- Tidwell, Brewer & Valencia (2020), *Designing Interfaces*, 3rd ed. Search results say its
  table of contents lists hub and spoke, fully connected, tree, step by step, pyramid, pan and
  zoom, and flat. The text was blocked (HTTP 403), so I have the names but not the reasoning.
- Rausch (2025, practitioner, iOS), stated reasons for each model. Drill-down: "animated
  transitions imply horizontal movement," which orients the user in the hierarchy. Tab bar items
  are "curated around the main capabilities of the app to shape the user's expectations."
  Hub-and-spoke gives a "neutral state" and an "escape hatch" but is "rarely used within apps."
  Step-by-step "can feel tedious." Content-driven navigation: "avoid this pattern in iOS apps"
  outside hypertext or immersive content. Modals, high-friction: "block what's behind them until
  the user makes a decision." Modals, low-friction: "low friction is not the same as no friction."
- Rosenfeld et al. (2015, p. 182): hypertext allows both lateral and vertical movement across
  a hierarchy.

Counterevidence and limits. These are practitioner taxonomies, not tested categories. The
models overlap: a pyramid is a tree with sibling links.

Example. One product, three models: a flat tab bar at the root, a drill-down inside each tab,
and a step-by-step modal for creating a new record (inferred; this is common in iOS apps).

Labels. Useful pattern, C.

Use. To produce structurally different directions, change the model at the root. For example,
a hub (a home screen of tools) against a flat model (persistent tabs) against a content-driven
model (a feed or document that links outward). Then pick the model for each deeper level
separately (inferred).

---

## Finding 6. Hiding the navigation reduces its use. This is one of the better-measured structural choices.

Claim. Navigation that is visible (or partly visible) gets used more, and earlier, than
navigation behind a menu icon. The effect is larger on desktop.

Evidence.
- Pernice & Budiu (NN/g, 2016). 179 participants, 6 sites, phone and desktop, conditions
  hidden, visible and combo. On desktop, navigation was used in 27% of hidden-condition tasks
  against 48 to 50% for visible or combo. Tasks took 39% longer and felt harder. On phones, use
  was 57% hidden against 86% combo, and tasks took 15% longer. Stated: "Discoverability is cut
  almost in half by hiding a website's main navigation." Their rule of thumb is to show 4 or
  fewer top-level links. They did not fully test visible navigation on phones.
- Pernice & Budiu (2016, follow-up). Salience and placement matter. A large labelled "Browse"
  button got 89% navigation use against 44% for a menu icon that "looked… as part of the logo."
  Stated: "The hamburger is not so universal that everyone knows it."
- Wroblewski (2015, "Obvious Always Wins"; practitioner reports without numbers). Polar: moving
  sections from a segmented control into a toggle menu made engagement "plummet." Facebook iOS
  and Redbooth: moving from a hamburger to a bottom tab bar increased engagement, sessions and
  users. He accepts that "not everything can be visible in a mobile UI."

Counterevidence and limits. One lab study plus company anecdotes. A small screen cannot show
everything. The real design question is which 3 to 5 destinations earn permanent space.

Example. The Guardian's UK home page at 390 px (screenshot
`guardian-uk-mobile-390px-2026-09-26.png`, 2026-09-26) uses the combo form: five pillar links
visible, a scrollable row of subsections, and a labelled menu button for the rest.

Labels. Strong heuristic, B.

Use. Hide navigation only for items that are rarely used, or in apps where content is the
navigation (a reader, a camera). Everything critical and frequent should be visible. This fits
Wroblewski's point that deciding what to show "requires good design."

---

## Finding 7. Posture and frequency of use set how dense and how layered a structure should be

Claim. How long and how often people stay in a product changes the right structure. A tool
people live in all day can be dense and rich in controls, because users become intermediates. A
tool people visit briefly must be obvious and sparse. Progressive disclosure helps new users, but
hiding things adaptively hurts regular ones.

Evidence.
- Cooper & Reimann, *About Face 2.0* (2003, chapter on posture; excerpt read). A sovereign
  application monopolizes attention "for long periods." "The most important implication is that
  users of sovereign programs are intermediate users." Such a program can take the whole screen
  ("If you need four toolbars… use four toolbars") and use smaller controls, because users gain
  "an innate sense of where things are from sheer familiarity." A transient program "comes and
  goes." Users never become familiar with it, so it "must be simple, clear, and to the point."
- The GOV.UK Service Manual (2018) says that "one thing per page" can relax for internal services
  "where users need to repeat tasks quickly." This is the same frequency argument from a
  different tradition.
- Progressive disclosure. Carroll & Carrithers (1984, *CACM*; abstract): a "training wheels"
  word processor that made error-prone states unreachable gave "substantially faster learning."
  The control group spent almost a quarter of its time recovering from errors that the training
  interface blocked. Nielsen (2006) defines progressive disclosure and names the two hard parts:
  the "right split between initial and secondary features," and making it "obvious how users
  progress" to the second level. He adds that designs "beyond 2 disclosure levels typically have
  low usability." He cites no study for that limit.
- Counter: Findlater & McGrenere (2004, CHI; abstract and summary). A static split menu was
  faster than an adaptive one that moved items by frequency. Structure that changes under the
  user breaks location learning.

Counterevidence and limits. The posture categories are one studio's framework (D to C). The
training-wheels result is for first-time learning, not long-term use.

Example. Cooper's transient example is the Windows volume control. His sovereign examples are
word processors, spreadsheets and e-mail.

Labels. Posture shaping density: context-dependent heuristic, C. Blocking error states for
novices: strong heuristic, B. Stable over adaptive layouts for frequent use: strong heuristic, B.

Use. Decide the posture before you choose density. A "dense expert" direction and a "sparse
guided" direction are a real pair of options for the same requirements, and each needs its own
structure, not only different spacing (inferred). Disclose in stages that the user controls. Do
not reorder the product's structure automatically.

---

## Finding 8. Flow granularity: split by decision, and count the effort, not the steps

Claim. The same questions can be one long page, a few grouped steps, or one question per page.
The effort a flow asks for comes mainly from the number and difficulty of its questions. The
page count matters less. One question per page gains focus and handles branching, errors and
saving progress. It costs repetition for expert users and makes the middle of a flow hard to
link to.

Evidence.
- Paul (2015, GDS blog): one thing per page. "Low-confidence users find them easier to use,"
  "they work well on mobile devices," and they are "better at handling things like errors,
  branches, loops and saving progress." The post gives no quantitative data. The comments refer
  to lab testing on Register to Vote and GOV.UK Verify.
- GOV.UK Service Manual (2018), stated: start with each page containing "one piece of
  information, one decision, or one question." "User research will tell you when you can merge
  pages together." Before asking any question, check that you know why you need the answer and
  what you will do with it.
- Baymard (Scott, 2024): "the number of form fields in a checkout impacts overall usability far
  more than the number of steps… usability does seem to suffer after 8+ checkout steps." This is
  based on benchmarks of 343 sites and Baymard's own usability testing, which is not public.
- Patton (2008), story mapping. Lay user activities left to right in narrative order (the
  "backbone") and hang details below by priority. A flat backlog is "a bag of context-free
  mulch." The top slice is the "smallest possible system… that would give you end to end
  functionality." This is a way to produce the flow skeleton before choosing granularity.

Counterevidence and limits. For frequent or expert users, the repeated page loads are pure
cost (GOV.UK says so itself). Step flows lose context between pages. An overview or
check-answers page is the usual repair (inferred). Deep links into the middle of a flow break:
see the screenshot `govuk-register-to-vote-deep-link-error-2026-09-26.png` (2026-09-26), where
the service says "followed a link to the middle of this service — please start from the
beginning."

Example. GOV.UK Register to Vote (screenshot `govuk-register-to-vote-first-question-2026-09-26.png`,
2026-09-26). The first page asks only "Where do you live?" The answer changes the rules
downstream, which is exactly the branching case the pattern handles well.

Labels. Fields over steps: strong heuristic, B (large benchmark, methods not public). One thing
per page for infrequent, low-confidence users: context-dependent heuristic, C. Story map as a
generator: useful pattern, C.

Use. Generate options along one axis: a single page, grouped steps, or one thing per page.
Choose by frequency of use, how much the questions branch, and whether users need to see all
answers together. First remove questions: that cuts effort more than any regrouping.

---

## Finding 9. Modes are a structural choice. Make them visible, held, or absent.

Claim. A mode changes what the same input does. Modes cause errors when users forget which
mode they are in. The options are to avoid modes (select the object, then act), to make the
mode spring-loaded (it lasts only while a key is held), or to accept a persistent mode for
experts and make it very visible.

Evidence.
- Tesler's definition, as quoted in Smith et al. (1982): a mode is "a state of the user interface
  that lasts for a period of time, is not associated with any particular object, and has no
  role other than to place an interpretation on operator input." In the paper's Bravo story, a
  user typed "edit" in command mode and the document became the letter "t." Modes "should be
  introduced… with caution, if at all."
- Raskin (2000, *The Humane Interface*; snippets). "Modes are a significant source of errors,
  confusion, unnecessary restrictions, and complexity" (p. 37). A quasimode is a mode
  "maintained kinesthetically," such as holding Shift, as opposed to Caps Lock (p. 55).
- Sellen, Kurtenbach & Buxton (1992, *HCI*; abstract). In a modal text editor, a foot pedal held
  down for the mode (kinesthetic feedback) reduced mode errors and cognitive load more than
  visual feedback. Both kinds of feedback helped.

Counterevidence and limits. Expert tools rely on modes: vim, tool modes in drawing apps. When
the mode is the job itself (drawing with the pen tool), the user's attention is already on it
(inferred). The Star paper's own counterpoint: noun-verb order "does not by itself imply" that
an interface is modeless.

Example. The command palette is a contemporary structural option. Superhuman (Boucher, 2021,
the company's own blog) makes Cmd+K "the one place where users can find every command." It is
available "wherever your user is," it matches fuzzy text and synonyms, and it shows each
command's shortcut so users learn it. It is a transient, summoned mode that closes on Esc. It
acts on the current selection or context, which is noun-verb order again (inferred).

Labels. Mode errors: strong heuristic, B. Held modes cause fewer errors than latched ones:
strong heuristic, B (one set of experiments plus Raskin's argument). Command palette: useful
pattern, C.

Use. When a direction needs expert speed, offer a summoned command layer or held modes on top
of a visible structure. Do not add hidden persistent modes. For new or occasional users, the
command layer cannot be the only way in, because it is hidden navigation (see Finding 6).

---

## Finding 10. States are part of the structure: list them systematically, and nest them to control the explosion

Claim. Every screen exists in several states, and a design that shows only the ideal state is
incomplete. You can list the states per screen (ideal, empty, partial, loading, error). For
complex behavior, a statechart shows how states nest and run in parallel, so the combinations
do not multiply out of control.

Evidence.
- Hurff (2015, practitioner): five states. Ideal: design this first. Empty: split into first use,
  cleared by the user, and no results. Error: must keep the user's input ("A computer shall not
  harm your work"). Partial: sparse data. Loading. His claim is that "awkward UI" comes from
  ignoring these states.
- Harel (1987, *Science of Computer Programming*; abstract). Statecharts add hierarchy,
  concurrency and communication to state diagrams, so that "small diagrams can express complex
  behavior." Horrocks (1999; publisher description only) applies statecharts to building user
  interfaces.
- Tesler's mode definition (Finding 9) is the same idea seen from the user's side. A state the
  user cannot see is a mode.

Counterevidence and limits. Hurff's list is a practitioner taxonomy. Statecharts cost time to
draw. For a small prototype, a per-screen state list is usually enough (inferred).

Example. The GOV.UK deep-link error page (screenshot, 2026-09-26) is a designed error state. It
lists the three likely causes in plain words and offers one action.

Labels. Enumerating states: strong heuristic, C (wide practitioner agreement, no study).
Statecharts: useful pattern, B for the formalism, C for its use in design.

Use. For each direction, show at least the empty, loading and error states of the key screen.
Directions often differ most in these states. For example, an empty state can teach, show a
sample, or be a single call to action (inferred).

---

## Finding 11. Content-first or structure-first: practitioners disagree, and the answer depends on whether the content exists

Claim. One camp says design must start from real content. Another says you can start from the
structure of the content (its types and parts) before it is written. Both reject designing with
placeholder text alone.

Evidence.
- Zeldman (2008): "Content precedes design. Design in the absence of content is not design, it's
  decoration." This is a one-line opinion.
- Boulton (2012), stated: "You can create good experiences without knowing the content. What you
  can't do is create good experiences without knowing your content structure." "It is
  unrealistic to write your content before you design it." His method: sort words into themes,
  define content types, then use page tables. His model is newspaper and magazine templating.
- van Nues & Overkamp (2018, *A List Apart*): priority guides, credited to Drew Clemens (2012). A
  priority guide "contains content and elements for a mobile screen, sorted by hierarchy from
  top to bottom and without layout specifications." Their mechanism is that wireframes fix
  layout too early: visual designers struggle to "think outside the boundaries set by that
  wireframe." Their advice: "Just don't *start* with wireframes."
- Wroblewski (2009), mobile first: small screens "require software development teams to focus
  on only the most important data and actions." The same ranking mechanism.

Counterevidence and limits. None of these sources has outcome data. The priority-guide argument
about early wireframes limiting creativity matches design-fixation research (area 1), but the
article does not cite it. Budiu & Pernice (2016, "Mobile First Is NOT Mobile Only"): mobile
patterns carried unchanged to desktop, such as hidden navigation and search icons, hurt it.

Labels. Structure before layout: context-dependent heuristic, C. "Content first" as an absolute
rule: aesthetic preference or opinion, D.

Use. Before generating layouts, write a ranked list of content per key screen and share it
across all directions. The directions then differ in structure and form, not in what they
forgot to include (inferred).

---

## Finding 12. Motion should express the structure. It helps when the view changes place or shape, and adds little elsewhere.

Claim. A transition can show how two states relate: this came from there, this sits beside
that, this is a new context. Evidence supports animated transitions for keeping people oriented
during changes of viewpoint or of data shape. It does not support animation in general.

Evidence.
- Tversky, Morrison & Bétrancourt (2002, *IJHCS*; abstract and sections). In studies where
  animated graphics seemed better than static ones, "scrutiny reveals lack of equivalence." The
  animated versions carried more information or allowed interaction. "Animations are often too
  complex or too fast to be accurately perceived." Still, animation may help "for real time
  reorientations in time and space."
- Bederson & Boltman (1999, InfoVis; full text). 20 participants navigated a zoomable family
  tree. A 1-second animated viewpoint change improved their ability to reconstruct the space,
  "with no penalty on task performance time." There was no difference in other tasks or in
  satisfaction. Stated limit: "Animation has a strong visual impact, and not all users like it."
- Heer & Robertson (2007, InfoVis; full text). 24 participants. Animated transitions between
  charts "significantly improve graphical perception" over static cuts, and staged transitions
  (one change at a time) often did better. Their design rules, drawn from Tversky's principles:
  keep intermediate frames valid, "use simple transitions," "use staging for complex
  transitions," and "make transitions as long as needed, but no longer." They cite about 1 s from
  Robertson et al.
- Chang & Ungar (1993, UIST; partial): cartoon principles in the Self environment, so objects
  "arrive and depart smoothly, without sudden materializations." A design account, not a test.
- Material Design (Material Components motion documentation). The transition pattern follows the
  relationship. Container transform: "a visible connection between two UI elements." Shared axis:
  elements "that have a spatial or navigational relationship." Fade through: elements "that do
  not have a strong relationship to each other." Fade: elements that enter or exit within the
  screen.
- Apple HIG (Motion, read 2026-09-26): "Don't add motion for the sake of adding motion." "Generally
  avoid adding motion to UI interactions that occur frequently." "Let people cancel motion." Make
  it optional, and never the only carrier of information.

Counterevidence and limits. The lab studies are small and measure orientation and memory, not
satisfaction or speed over months. Repeated motion costs time for experts (Apple, stated).

Example. Opening an item from a grid: a container transform shows that the detail view is that
card. Switching between unrelated tabs: a fade through says there is no spatial relation. The
choice of motion follows from the choice of navigation model (Finding 5; inferred).

Labels. Animated transitions for spatial reorientation: strong heuristic, B (two to three
studies that agree). Motion that encodes structural relationships: useful pattern, C. Animation
for general "delight": aesthetic preference, D.

Use. Give each direction a motion vocabulary tied to its structure: which transitions mean
"deeper," "sideways" and "new context." Keep frequent actions nearly instant. Leave motion out
when the structure is flat and the changes are small.

---

## Finding 13. Infinite scroll or pages: it depends on whether the user is searching or browsing

Claim. Endless lists suit aimless browsing of similar items. Pages, or "load more," suit goal
tasks: comparing, returning to an item, and finding the footer.

Evidence.
- McKinley (Etsy, talk "Design for Continuous Experimentation," 2012). People with infinite
  scroll "saw fewer items," "clicked on fewer items," "saved fewer items as favorites," and
  "bought fewer items from search." Follow-up tests: more items per page gave "a very slight
  improvement." Slowing the results page artificially: "Absolutely nothing happened." Etsy
  removed the feature. The anecdote in the talk: power users opened results in new tabs to
  compare them.
- Loranger (NN/g, 2014): "Endless scrolling is not recommended for goal-oriented finding tasks."
  This comes from observation, with no study cited.

Counterevidence and limits. Social feeds use infinite scroll to maximize time spent, which is a
different goal (inferred). McKinley's result is one A/B test on one marketplace.

Labels. Context-dependent heuristic, B (one large A/B test, plus expert guidance).

Use. Pick the list structure from the task. For shopping and search, prefer pages or load-more
with a position that can be restored. For a feed, infinite scroll can fit.

---

## Finding 14. Follow conventions for navigation furniture, and put the distinctiveness in the structure of the core task

Claim. Users bring expectations from other products, so the furniture (logo, home link, search
position, cart) should usually be conventional. A distinctive product usually departs in its
core model (what the objects are and how you act on them), not in where the menu sits.

Evidence.
- Nielsen (2000), "Jakob's Law": "Users spend most of their time on *other* sites." He argues for
  standard interaction and IA, and places innovation in task analysis and content. He offers
  business outcomes as support, but no data.
- Whitenton (NN/g, 2016). 50 users on 14 fashion sites. Users were "6 times as likely to fail" to
  get to the home page in one click when the logo was centered. The study covered one site
  category.
- Tesler (c. 1984, his own site), the law of conservation of complexity: "Every application has
  an inherent amount of irreducible complexity. The only question is: Who will have to deal with
  it?" Departures that move complexity from the user into the system are the ones worth making
  (inferred).
- Structural departures in the teams' own accounts (evidence of intent only): the Star's
  universal commands, the BBC's one page per thing, Superhuman's command palette. Craigslist
  (observed 2026-09-26) shows the reverse: a strong identity from not changing a learned
  structure.

Counterevidence and limits. Conventions change, and familiarity is not the same as use (the
hamburger, Finding 6). These products may succeed for reasons other than structure.

Labels. Conventional furniture: strong heuristic, B. Distinctiveness through the core model:
context-dependent heuristic, C to D.

Use. The generic structure is right when users visit rarely, the task is standard (checkout,
login, government forms), or trust matters more than character. A distinctive structure is
worth its learning cost when users return often and the new model makes the core task clearly
simpler.

---

## Finding 15. Generating and comparing structural options: make the questions explicit, vary one question at a time, and use user groupings as input

Claim. You get several real options by naming the structural questions and answering each one
more than one way. The questions are: the primary scheme, the structure, the root navigation
model, the flow granularity, the posture, the mode strategy and the motion vocabulary. Card
sorting shows how users group items. It is input for the structure, not the structure itself.

Evidence.
- MacLean, Young, Bellotti & Moran (1991, *HCI*; summary only). Design space analysis
  represents design as Questions, Options and Criteria (QOC). The questions are "key issues for
  structuring the space of alternatives," and the criteria are "the bases for choosing among the
  options." Buckingham Shum & Hammond (1994; abstract fragment only) examined whether designers
  find such argument notations useful and usable. I could not read their conclusions.
- Smith et al. (1982): the Star team tested six mouse-button designs, found "none of them was
  completely easy to use," and merged two into a seventh that tested best. Stated: "Almost
  always there are trade-offs."
- Rosenfeld et al. (2015, p. 367 to 369): metaphor exploration as brainstorming, in three kinds:
  organizational, functional and visual metaphors. Each is a way to generate a scheme, with the
  warning that metaphors limit.
- Card sorting. Katsanos et al. (2019, CHI; abstract): 6 open card sorts with 140 participants
  gave "highly similar" data for the same content, with "rather high agreement" in the resulting
  navigation schemes. Tullis & Wood (2004, as reported by Nielsen, 2004): from 168 users,
  subsets of 15 correlated 0.90 with the full result, and 30 correlated 0.95. Nielsen: "I don't
  recommend designing an information architecture based purely on a card sort's numeric
  similarity scores."

Counterevidence and limits. Explicit rationale notations cost effort, and their benefit is not
well established (the details of the 1994 critique were not read). Card sorts reflect the
labels printed on the cards and say nothing about where people will look first (inferred).

Example. A structure matrix for a recipe app. Scheme: by meal, by ingredient, or by time
available. Root model: hub, tabs, or feed. Flow: one-page recipe or step mode. Posture:
transient. Choose one cell per row to make three coherent directions, and write down the
criteria (known-item search against browsing, frequency of use) that each direction favors
(inferred).

Labels. QOC as a generator: useful pattern, C. Card sorting as generative input: strong
heuristic, B.

Use. Always, when producing several directions. Say which questions each direction answers
differently, so the tradeoffs are visible.

---

## Outside my area

- Visual craft (area 3). Cooper: sovereign apps should use a "conservative visual style" and a
  narrow palette, while transient apps can use bigger, brighter controls. Tversky's congruence
  and apprehension principles apply to static charts too.
- Process (area 1). Priority guides against fixation on early wireframes. The Star team's six
  prototypes, then a seventh, is an early case of parallel prototyping.
- Code (area 5). Material's motion tokens (easing curves and duration slots) and Apple's
  optional-motion rule map to CSS `prefers-reduced-motion` (accessibility, excluded here).
  Heer & Robertson report transitions of about 1 s.
- Excluded subjects I met: skeleton screens and perceived waiting (performance), and tree
  testing (evaluation).
