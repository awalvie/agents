# Area 4: Design languages and distinctiveness

Researched 2026-09-26. Sources are in `languages-sources.md`. Screenshots are in `languages-shots/`, all taken 2026-09-26 at 1440 x 1000 px.

"Stated" means the source says it. "Inferred" means I drew it from the sources.

Coverage check: I could not read the text of Meggs' *History of Graphic Design*. The Internet Archive copy is loan-only, and Google Books blocked the search with a captcha. I used its table of contents (4th edition, Library of Congress record) and the 6th edition publisher's description. So Meggs appears below only as one way to group traditions. It is not evidence for any claim.

## Part 1. The traditions, and how sources group them

The sources do not share a list. Four ways of grouping appear:

- By historical movement (Meggs' table of contents). Part Five, "The Age of Information", runs: International Typographic Style, New York School, Corporate Identity and Visual Systems, The Conceptual Image, Postmodern Design, The Digital Revolution. This grouping is about print and identity. It has no category for interactive conventions such as signifiers.
- As a cycle of visual trends (NN/g). Skeuomorphism, then flat (2011 to 2012), then "flat 2.0" and Material, then neumorphism (2019), then glassmorphism (2020 on), then Liquid Glass (2025). Chan (NN/g, 2024) states that "each trend is a response to the one before".
- As platform "materials" (Apple, Google, Microsoft). Platform owners do not use trend names. Brown (NN/g, 2024) notes that design systems "tend to label this style under the broader category of 'material'", for example Fluent's "Acrylic". Material Design 1 called its whole language a "material metaphor".
- By attitude to the medium (Allsopp 2000, Chimero 2015). Print-derived control is set against web-native flow. This axis cuts across all of the visual trends.

Sources also disagree on the edges of single traditions:

- Brutalism. Deville's site (checked 2026-09-26) defines it by attitude: "a reaction by a younger generation to the lightness, optimism, and frivolity of today's web design". It lists both raw HTML sites and chaotic art sites. Moran (NN/g, 2017) splits these into brutalism (raw, unadorned) and antidesign (deliberately disorienting), and judges the two differently. Sheikh (NN/g, 2025) adds neobrutalism (thick borders, flat bright colour, hard offset shadows) as a third, more orderly style.
- Flat. Burmistrov et al. (2015) name Windows Phone 7 (2010) as the first flat design. Moran (2015) dates it to Metro and Windows 8 (2011). Microsoft (Windows Developer Blog, 2013) rejected "the misconception that the Microsoft visual language consists only of uniform rectangles in a grid."
- Skeuomorphism. Chan (NN/g, 2024) separates skeuomorphism as a learning aid (the folder and trash icons, "never truly dead") from skeuomorphism as a visual trend (leather and wood). Moran (2015) separates skeuomorphism, which supports a metaphor, from realism, which is texture for its own sake.

The working list I built from the sources follows. For each tradition: what it is good for, and where it fails.

1. Print-derived modernism. International Typographic Style, then Metro, then flat (Meggs ch. 18; Burmistrov 2015). It is good for clear hierarchy, content over chrome, and scaling across many screens. It fails when it removes the depth and colour cues that tell a user what is clickable (F2).
2. Skeuomorphism and realism (iOS 6 era, the Kindle Fire bookshelf). It is good for teaching new users by analogy. It fails once users know the medium: the textures turn into clutter, and false physical actions confuse (Chan 2024; the Pizza Hut tilt-to-add-toppings app).
3. Flat 2.0 and Material. Depth is used as information: "Surfaces and edges of the material provide visual cues that are grounded in reality" (Material 1). It is good for signifiers without ornament. It fails as a default, because it produces the look where "all these apps look so similar" (Google, 2025).
4. Platform-native languages (HIG, Material, Fluent). They are good for familiarity and low cost. They fail on identity, which the platform owners limit to a small set of places (F13).
5. Decorative materials: neumorphism, glassmorphism, Liquid Glass. They give a fresh look and some depth. They fail on figure-ground contrast and legibility (F14).
6. Web-native fluid design (Allsopp 2000; Chimero 2015). It is good for layouts of unknown size and user control. It is criticised as a cause of sameness (Müller 2018). F6 gives the defence.
7. Utilitarian plainness (Craigslist, Hacker News, Drudge Report, early NN/g). It is good for speed and for the signal that nobody is selling to you. It fails where the product must persuade or look aspirational: Chayka (2016) credits Airbnb's shift away from a "Craigslist-rough" look for its win over Couchsurfing.
8. Brutalism, antidesign and neobrutalism. They are good for attention, a designer audience and entertainment. They fail for tasks (F12).
9. The civic or "invisible" service style (GOV.UK). It is good for a universal audience and for trust (F11).
10. The dense instrument (Bloomberg Terminal). It is good for experts who use the product for years. It is hostile to newcomers (F11).
11. Brand illustration systems (Facebook's "Alegria" by Buck, 2017, later called "Corporate Memphis"). They warm a product cheaply. They fail when copied: they read as generic, and critics read them as a mask for the company (F8).
12. Art-directed and expressive editorial design (Postmodern Design in Meggs, ch. 23; Carson, Greiman and Brody as cited by Müller; Santa Maria 2008). It is good when form should carry the meaning of the content. It costs design time for each piece (F15).
13. The "Linear look" (dark background, lighting effects, product UI as the main image, thin lines, sans serif). It is good for signalling a fast, serious tool. It is now a trend of its own (F8).

Gaps: I did not research game UI, Japanese and Chinese high-density commerce design, or Y2K revival styles in depth. Only Reinecke and Gajos (F4) touch on culture.

## Part 2. Findings

## F1. Each language answers a problem of its time. Its costs stay after the problem goes.

Claim: Skeuomorphism answered "users do not know this medium". Flat answered "ornament is noise, and the medium is its own thing". Material answered "flat lost the cues". Each answer carried costs that stayed after the problem changed.

Evidence: Microsoft called Metro "authentically digital" (quoted by Moran 2015). Chan (2024) states that skeuomorphism eased the move to digital, and that Amazon "dropped the skeuomorphic elements" once "users became familiar with ereaders". Moran (2015) states that flat's main problem is the loss of signifiers. Material Design 1 states the fix: "The use of familiar tactile attributes helps users quickly understand affordances." All of this is stated. The general pattern is my inference.

Context: It applies whenever a designer picks a named style. The useful question is "what problem was this style solving, and does my product have that problem?"

Counterevidence: Style changes are also driven by fashion and by the wish to look new, not only by problems. Malewicz (2019) gives "freshness (at least for as long as it lasts)" as neumorphism's main benefit. The problem-answer story explains some shifts and rationalises others.

Example: Amazon's Kindle Fire bookshelf was dropped after users learned the product (Chan 2024).

Labels: strong heuristic. Evidence C (practitioner accounts and single cases, with no controlled study of the pattern).

Use: When choosing or mixing traditions, name the problem each one solves for this product and audience. Do not use it to predict the next trend.

## F2. The cost of flat design depends on density, layout convention and target salience

Claim: Weak signifiers cost users time and cause errors. The cost mostly goes away when the page is sparse, the layout is conventional, and the targets stand out.

Evidence:
- Moran (NN/g, 2017) ran an eyetracking study with 71 users. Nine page pairs differed only in signifier strength. On weak-signifier versions users took 22% more time and made 25% more fixations (p < 0.05). Three of the nine pairs showed no difference. Those pages had low density, a traditional layout, and salient, high-contrast targets.
- Burmistrov et al. (2015) tested 20 students, 19 of them women. Finding a flat icon took almost twice as long as finding a realistic icon (15.4 s vs 8.0 s). Flat web pages had more misses (35.8% vs 26.0%) and more false alarms (28.0% vs 16.6%).
- Moran (2016) surveyed 457 people. Adults aged 18 to 25 rated flat designs 0.53 points higher than adults aged 35 and over (95% CI 0.4 to 0.7). The control design got the same rating from both groups.

Context: Most of this is stated. The rule to "choose flat only when all three conditions hold" is stated by Moran (2017).

Counterevidence and limits: Burmistrov's "flat text" condition used Helvetica Neue Condensed, Light and UltraLight. That test measures thin type, not flatness as such. Both studies measured findability on single pages, not full tasks. Moran (2017) says that the slowdown on a whole task "would often be less than the 22%".

Example: In Moran's Brilliant Earth pair, 9 of 24 users on the weak version stopped at the subheading and never saw the "Shop Pearl" link.

Labels: fundamental principle (signifiers must be perceivable). Evidence B (two controlled studies and one survey, not independent replications).

Use: A minimal or flat direction is safe for sparse, conventional pages. Add explicit signifiers, or pick a different tradition, for dense tools, novel layouts, or features the user must discover.

## F3. "Most advanced, yet acceptable": typicality and novelty both raise appeal, and they pull against each other

Claim: People like designs that are new, but only while they still read as a good member of their category. The best balance shifts with stakes and exposure time, and possibly with expertise.

Evidence:
- Hekkert, Snelders and van Wieringen (2003) ran three studies on telephones, teakettles, sanders and cars. Typicality and novelty were "jointly and equally effective" predictors of preference, but they "suppress each other's effect". People "prefer novel designs as long as the novelty does not affect typicality."
- In Hekkert's car study, experts showed a weaker suppression effect than non-experts. The third-party summary I read also says expertise reduced novelty's relative influence, so the expertise result is unclear to me. I did not read the full text.
- Tuch et al. (2012) showed that visual complexity and prototypicality shape appeal within 50 ms. Low-complexity, high-prototypicality sites were the most appealing.
- Silvennoinen et al. (2025) are the first test of this idea (known as MAYA) on websites: 108 participants, 12 sites. Both factors predicted appeal, and novelty had the stronger link. Typicality weighed more on commercial sites, where users spend money. Novelty weighed more on free service sites.
- Google (2025) tested a playlist design with album art "arranged helter-skelter". Users called it "modern and exciting", but its usability scores suffered.

Context: The main effects are stated. That money and risk increase the value of typicality is the stated hypothesis and result of Silvennoinen et al., in one study.

Counterevidence: Silvennoinen et al. note "conflicting findings regarding preferences for typicality and novelty". All the studies rate static pictures. None measures appeal after long use.

Example: Sharp answered a reader in a comment on his own blog: brands must signal their category, and "Being distinctive means 'looking like you'. It doesn't mean doing whacky things." Marketing arrives at the same balance from a different field.

Labels: strong heuristic. Evidence B (several studies, one of them on websites).

Use: For each direction, state what keeps it recognisable as its category (layout, placement of navigation and actions) and where it spends its novelty (type, colour, image, motion, voice). Put novelty into the surface and typicality into the structure. Lean further toward typicality when users pay, risk something, or glance briefly.

## F4. Preference for a style varies by audience, so no single house style is right

Claim: The level of colour and complexity people find most appealing differs by gender, education, country and age.

Evidence:
- Reinecke and Gajos (2014) collected 2.4 million ratings from nearly 40,000 participants. "The level of colorfulness and visual complexity at which visual appeal is highest strongly varies." Russians preferred lower complexity. Macedonians liked high colourfulness more than any other country in the data. Higher education lowered the preference for colour.
- Moran (2016) found the age difference for flat design described in F2.
- Google (2025) reports that preference for Material 3 Expressive was "up to 87%" among 18 to 24 year olds, and that "a strong minority of users preferred calmer, less intense versions".

Context: All of this is stated. Google's study is company research on its own product, so treat it as evidence of what Google intended and measured, not as independent evidence.

Counterevidence: Tuch et al. (2012) and Hekkert et al. (2003) find regularities that hold across people. Differences between groups sit on top of a shared structure, not in place of one.

Labels: strong heuristic. Evidence A for the existence of group differences (Reinecke's dataset is very large). Evidence C for any specific audience.

Use: Name the audience before choosing a language. Directions for a broad public should cover more than one level of complexity. Do not assume the designer's own taste is the audience's taste.

## F5. Sameness has specific causes

Claim: Interfaces converge through five mechanisms: templates that separate form from content, showcases where designers perform for other designers, feeds that spread one taste across the world, design systems, and default values in frameworks.

Evidence:
- Müller (2018) says templates "are content agnostic. And that is the problem." He also blames the economics of producing a page, "mobile-first, generic, framework-driven development", and the fact that "HTML, JavaScript, and CSS remain challenging tools for designers."
- Adams (Intercom, 2013) wrote about job applicants: "A huge majority of the product design work on Dribbble looks the same." Designers work "to impress their peers rather than address real business problems."
- Chayka (2016) describes "AirSpace": cafes worldwide that "have all independently decided to adopt the same faux-artisanal aesthetic", spread by Instagram and Foursquare.
- Google's Material team (2025) asked, "Why did all these apps look so similar? So boring?" This was about apps built on its own system.
- Wathan (7 August 2025, on X, quoted by several outlets): "I'd like to formally apologize for making every button in Tailwind UI `bg-indigo-500` five years ago, leading to every AI generated UI on earth also being indigo."

Context: The mechanisms are stated by the people inside them (Google, Wathan, Adams). Their weight relative to each other is unknown.

Counterevidence: See F6.

Labels: context-dependent heuristic. Evidence C.

Use: When a direction looks familiar, find which mechanism produced the resemblance. Then decide whether the resemblance helps (F6, F11) or hides the product.

## F6. Some sameness is the grain of the medium, and it is correct

Claim: Shared solutions are often the right answer to shared constraints. They are not always a failure of imagination.

Evidence:
- Chimero (2015): "Many sites will share design solutions, because we're using the same materials. The consistencies establish best practices; they are proof of design patterns that play off of the needs of a common medium, and not evidence of a visual monoculture."
- Allsopp (2000) argued that designers should give up print's "designer is controller" habit and design for flexibility.
- Nielsen (2000): "Users spend most of their time on other sites. This means that users prefer your site to work the same way."
- In Chayka (2016), an Airbnb designer says the "International Airbnb Style" gives "a sense of comfort and immediate belonging", and an investor says users "are coming to demand" it.

Counterevidence: Müller (2018): "If you equate stereotypes with usability, you have understood neither visual design nor human-centered design." Nielsen's claim that "websites do more business the more standardized their design is" cites no data. The same article also predicted grayscale mobile screens.

Context: This is inferred from the two camps together. Chimero's argument is about structure and layout. Müller's complaint is about visual expression. They conflict less than they seem to.

Labels: strong heuristic for structure. Aesthetic preference for the surface. Evidence C.

Use: Accept the shared grain in structure: flow, responsive layout, standard controls. Make distinctive choices in the layers the grain does not fix: type, colour, imagery, voice, motion, and the art direction of key pages.

## F7. The "machine-made" look is the most common choice in the training data. Banning it moves the default instead of removing it.

Claim: An AI generating an interface without direction picks the most likely choice at each decision. The result is recognisably generic. A list of banned choices shifts that default to the next most common option.

Evidence:
- Anthropic (Claude blog, November 2025): unguided output "will almost always conform to Inter fonts, purple gradients on white backgrounds, and minimal animations", because "Safe design choices ... dominate web training data." Even with bans, "You still tend to converge on common choices (Space Grotesk, for example) across generations."
- Doshi and Hauser (2024): 300 writers and 600 judges. AI ideas made individual stories more creative, but the stories were more similar to each other. The authors call this a social dilemma.
- Anderson, Shah and Kreminski (2024): 36 participants. Different ChatGPT users produced ideas that were less distinct from each other's than users of another creativity tool.

Context: The claim about design output is stated by one vendor about its own model (C). The homogenising effect of AI on creative work has two studies behind it, but in writing and ideation, not visual design. Applying that to interfaces is my inference.

Counterevidence: Anthropic reports that targeted prompts "improve immediately" the output, so the default can be steered. Neither study measured how much variety survives when choices come from the specific content.

Example: The markers listed across sources are: Inter or Roboto, a purple or indigo accent, gradients on white, a centred hero with three feature cards, and "containers in containers in containers" (Müller). On 2026-09-26, stripe.com used an indigo primary button and a large gradient ribbon (screenshot). That is a distinctive brand asset that sits close to this common look. Resemblance to the generic look is not proof of being generic.

Labels: context-dependent heuristic. Evidence C for design, B for the general homogenising effect.

Use: For a persona that generates several directions, derive each choice from something specific to the brief (content, audience, a named reference, a material or place). Do not start from a list of things to avoid. Compare the directions with each other, not only with the brief, because they can converge on the same default.

## F8. A style built to be easy to copy becomes common property and stops identifying anyone

Claim: Styles made for easy reuse spread fastest. Once widely copied, they signal the trend rather than the owner, and the next style defines itself against them.

Evidence:
- Buck built Alegria as "a scalable system rooted in flat, minimal, geometric shapes" (Buck case study).
- Herrera, an illustrator on the Buck team, said the style "started as something more intuitive and complex ... after different reviews, it started to shift towards something simpler to copy and implement". A usage manual "has been passed through a lot of different studios" (Hawley, Eye on Design, 2019).
- Buck's own page says, "There's many imitators, but there's only one Alegria."
- Trost (Frontend Horse, early 2024) lists the ingredients of the "Linear look". One is "You'd be hard-pressed to find a stock photograph or flat illustration of a person". I read this as a reaction against the Alegria era (inferred).
- Malewicz (2019) credits one Dribbble shot with "over 3000 likes" for starting neumorphism.

Context: The case facts are stated. The general mechanism is inferred from three cases.

Counterevidence: Copying does not always erase the original. Buck still claims Alegria. Linear kept its identity while its look spread, perhaps because its identity also rests on the product (F10).

Labels: context-dependent heuristic. Evidence C.

Use: When a direction borrows a current trend, say so, and say how long the trend is likely to read as fresh. For identity work, prefer elements that are hard to copy because they come from the product's own content, data or history.

## F9. Distinctiveness means "looking like yourself", built by using owned assets consistently. It is not the same as differentiation.

Claim: A strong identity comes from a few assets people link to the brand (a colour, a character, a shape, a typeface, a sound), used consistently over time. Replacing them throws away the association that was built up.

Evidence:
- Romaniuk, Sharp and Ehrenberg (2007) found, across many categories in two countries, low perceived differentiation between competing brands, and yet people still bought them. They propose distinctiveness ("a brand looking like itself") as the centre of brand strategy (abstract, and Sharp's blog summary).
- Burberry replaced its equestrian knight, first used around 1901, with a Peter Saville sans-serif wordmark in 2018. Under a new creative director in February 2023, it brought back the knight and a serif wordmark, calling them "archive-inspired" (Dezeen 2023).
- Bloomberg's then-CEO Lex Fenwick is quoted: "We have to be religiously consistent ... You can see a Bloomberg from a mile away" (quoted in Leca, UX Magazine, 2010).

Context: The Ehrenberg-Bass findings come from marketing data (B). How they carry over to interface design is inferred.

Counterevidence: Other marketing schools argue that meaningful difference still matters. I did not check their data. Burberry is one case, and a new creative director may simply have preferred the old logo.

Labels: strong heuristic. Evidence B for brands, C for interfaces.

Use: Before a direction reworks an existing product, list its assets that people already recognise and keep or develop them. For a new product, choose one or two assets that no competitor owns, and use them everywhere.

## F10. Strong identities grow from one core asset, or from a product principle, not from a clever font alone

Claim: Products with a strong identity extend one existing asset into every part of the system, or express a principle about how the product works. A distinctive surface alone does not do it.

Evidence:
- Duolingo (2019): Johnson Banks decided that Duo the owl was the strongest asset. Monotype built the Feather Bold typeface from "the shape and spirit of an owl's wing", so that "Every aspect of Duolingo's identity is informed by ... Duo's personality and rounded feather form" (Monotype case study).
- Mailchimp (2018, Collins) kept Freddie the chimp and chose Cavendish Yellow as its main colour. Its stated rule was "just because we've grown doesn't mean we have to grow up" (Creative Review).
- Linear (2024) uses Inter and Inter Display, the most common fonts in the generic look. Its redesign aimed "to reduce visual noise, maintain visual alignment, and increase the hierarchy and density of navigation elements". It reduced "how much chrome (blue in our case)" appeared, and aligned details "you'll feel after a few minutes of using the app" (Linear blog).

Context: Each team's account shows what it intended, not what the result achieved. That identity comes from the principle rather than the font is my inference from the Linear case.

Counterevidence: The "Linear look" was copied widely (F8), so the surface did spread as a style. On 2026-09-26, mailchimp.com (now under Intuit branding) showed Freddie small in the header and a darker yellow-olive button. Even an owned asset gets diluted when the company changes hands (screenshot).

Labels: useful pattern. Evidence C.

Use: For each direction, state the core idea it expresses. Either take an existing asset and let it shape type, shape, motion and voice, or take a product principle (speed, calm, density, care) and make it visible. A typeface swap is not a direction.

## F11. Plain, conventional design is the right choice for a universal audience, task-driven use and trust. Rigorously applied, plainness becomes its own identity.

Claim: When anyone might arrive, for any task, and trust matters, restraint serves users best. Applied consistently at scale, that restraint also becomes recognisable.

Evidence:
- GOV.UK merged about 2,000 sites into one. Its designers "are happy when people say things are simple or even boring" (McCarthy, GDS, 2015). The Daily Mail called it "boring.com", and it won Design of the Year (Terrett 2015).
- Terrett (2012) described an exercise: setting the site in "one typeface, just one type size and ... everything black and white". The team chose Transport, the typeface of British road signs, because it was tested for legibility "in the rain, at night, at speed".
- Icons that looked "rather beautiful" were deleted because users read the orange door as an exit (Terrett 2015).
- The single crown logo let changes of monarch and of department names become "a simple code change" (Terrett 2024).
- Craigslist's CEO: "In all the complaints and requests we get from users, this is never one of them" (Wolf, Wired, 2009). Wolf found that users complain about spam, fraud and search, not the look.
- Silvennoinen et al. (2025) found that typicality weighs more where money is involved (F3).

Context: The cases are stated. That consistent plainness becomes identity is my inference. On 2026-09-26, the GOV.UK homepage (blue banner, Transport-derived type, underlined links, black arrow buttons) was recognisable at a glance with no decoration (screenshot).

Counterevidence: A commenter on the GDS blog called the style "really boring and 'underdesigned'". Plainness also fails when a product must win people over against a rival, as with Airbnb against Couchsurfing (Chayka 2016). Craigslist's plainness survives on network effects that most products do not have.

Labels: strong heuristic. Evidence C.

Use: Offer a conventional, restrained direction whenever the audience is broad, the use is a task, or trust is central. Make it distinctive through rigour (one typeface, strict hierarchy, a clear voice), not ornament. Do not choose it when the product's job is to seduce or to create desire.

## F12. Put expression in the visual layer and keep structure conventional. Antidesign only fits some contexts.

Claim: A loud, raw or strange surface can work if hierarchy, navigation and interaction stay conventional. Breaking the structure fails, except for designer audiences or pure entertainment.

Evidence:
- Moran (2017): "keep it limited to visual design. Don't break your visual hierarchy, navigation, or interaction design just for the sake of novelty." She calls adultswim.com brutalist on the surface only, with "a clear visual hierarchy". She says antidesign may suit a designer audience or entertainment, and "will backfire" elsewhere.
- Google (2025) found the same: removing text labels from email actions lowered usability. "When basic interaction paradigms are broken, expressive design can lead to poor usability."
- Gumroad (checked 2026-09-26) used a neobrutalist surface (hard black borders, pink coins, "Go from 0 to $1") over a standard layout: top navigation, a clear call to action and a search field (screenshot).

Counterevidence: Müller (2018) told his students "Do not be constrained by questions of usability, legibility, and flexibility", and quoted Carson: "don't confuse communication with legibility". For cultural institutions (his ZKM example), a structural experiment may be what the content means.

Labels: strong heuristic. Evidence C (the Google study adds some data, but it is the company's research on its own system).

Use: Expressive directions should take their risk in type, colour, image and motion. Break structure only when the brief is art, culture or entertainment, and say so as a tradeoff.

## F13. Platform languages specify where a brand is allowed to live

Claim: Apple and Microsoft both invite brand expression, but only in bounded places. These are voice, accent colour on primary actions, custom display type, and content. Controls, placement and behaviour stay standard.

Evidence:
- Apple HIG, Branding (last changed 2026-09-09): "Apply your app's accent color judiciously ... Minimize its use on controls." Use "a custom font for headlines and subheadings while using system fonts for body copy". "Express your brand with familiar components." "Ensure branding always defers to content." "Even a highly stylized interface can be approachable if it maintains familiar behaviors and patterns."
- Microsoft (2013): "Personality helps to differentiate your app ... be creative with the composition, typography, color and motion."

Context: This is stated as platform guidance. It also matches F3 and F12: novelty in the surface, typicality in the structure (inferred).

Counterevidence: Platform owners have their own interest in apps that look native. Games and some brand-led apps ignore this guidance and succeed. I found no data either way.

Labels: design convention with a reason stated. Evidence C.

Use: For native-feeling directions, place brand in the allowed layers. For a web product, the same division is a sensible default, not a rule.

## F14. A decorative material that competes with the content fails, even at the company with the strongest design identity

Claim: Translucent and animated "materials" help hierarchy only when legibility is protected. A material used for vitality or delight can hide the content it claims to serve.

Evidence:
- Apple (9 June 2025) introduced Liquid Glass to "bring greater focus to content" and "a new level of vitality".
- Budiu (NN/g, 10 October 2025) found text on busy backgrounds hard to read, "text on top of text" in Mail, animated controls ("motion without meaning"), and tighter tap targets.
- In iOS 26.1, Apple added a "Tinted" setting that makes Liquid Glass more opaque, after beta feedback (MacRumors, 2025).
- Brown (NN/g, 2024) advises "More blur is better", solid fallbacks, and letting users reduce transparency. Malewicz (2019) states that neumorphic buttons have no figure-ground contrast, "there's no contrast to measure".

Context: The critique is a single NN/g expert review, not a study. Apple's added setting is strong evidence that the problem was real.

Counterevidence: Glass works in visionOS, where it separates floating UI from a real environment (Brown 2024). Some users like the look (MacRumors).

Labels: strong heuristic. Evidence C.

Use: If a direction uses glass, soft shadows or ambient motion, keep them off text and controls. Put them on backgrounds or large surfaces, and say what the direction loses when the background is busy.

## F15. Art direction can tie form to content, at a cost in time for each piece

Claim: Templates make every item look alike. A system that fixes the frame and leaves each important item free to take its own look can restore the link between form and content.

Evidence:
- Santa Maria (2008) became "disillusioned" that a design gets "dropped into a template, reducing the design to more a bit player". He built "a system for the way content gets handled, but every layout and story can take on a look of their own within that system": a fixed eight-column grid and masthead, with type, colour and layout free for each article.
- Müller (2018): "form should both reflect and shape content."

Context: Stated. It applies to flagship pages, campaigns, editorial features and portfolios, not to every record in a database.

Counterevidence: Müller names the cost: large sites "do not have the resources to design a page from the ground up." Santa Maria called his site an "experiment", and I did not check how long it lasted.

Labels: useful pattern. Evidence C.

Use: A direction can propose a fixed frame plus one art-directed page, to show how the system bends for important content.

## Outside my area

- Process (area 1). Linear's redesign: one designer produced "hundreds of screens" in a daily cycle, narrowed them to a few directions, shared those for feedback, and ran "stress tests" of the concept ("How real could this concept car be?") before building it (Linear 2024).
- Process (area 1). GOV.UK's reduction exercise (one typeface, one size, black and white) is a way to find out which variation a design actually needs (Terrett 2012).
- Code (area 5). Linear generates its light, dark and custom themes from three variables (base colour, accent, contrast) in LCH instead of HSL, replacing 98 hand-set variables per theme. A contrast variable yields high-contrast themes automatically (Linear 2024).
- Code (area 5). Chimero (2015) and Allsopp (2000) argue for designing with the web's flexibility (relative units, unknown sizes) rather than against it.
