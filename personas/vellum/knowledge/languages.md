# Design languages and distinctiveness

Read this when you pick a tradition, when a direction looks generic, or when identity matters. Labels are in `README.md`. Meggs could not be read and serves only as one way to group traditions.

## The traditions

Sources group them four ways: by historical movement (Meggs), as a cycle of trends where "each trend is a response to the one before" (Chan, NN/g 2024), as platform "materials", and by attitude to the medium, print-like control against web-native flow (Allsopp 2000; Chimero 2015). The last axis cuts across the others. Edges differ too: NN/g splits brutalism (raw) from antidesign (disorienting) and neobrutalism (thick borders, flat bright colour, hard shadows).

The working list, with what each is good for and where it fails. Each entry is argued in the findings below. [CH, C, the list is inferred from the sources]

- Print-derived modernism (Swiss style, Metro, flat): clear hierarchy, content over chrome. Fails when it strips the cues that show what is clickable.
- Skeuomorphism: teaches a new medium by analogy. Turns into clutter once users know the medium. Amazon dropped the Kindle bookshelf once users knew e-readers (Chan 2024).
- Flat 2.0 and Material: depth used as information. As a default it gives a sameness that Google's own team questioned: "Why did all these apps look so similar?" (Google 2025).
- Platform-native (HIG, Material, Fluent): familiar and cheap. Limits brand to a few places.
- Decorative materials (neumorphism, glassmorphism, Liquid Glass): fresh, some depth. Fail on figure-ground contrast.
- Web-native fluid design: suits unknown screen sizes and user control. Blamed for sameness (Müller 2018).
- Utilitarian plainness (Craigslist, Hacker News): fast, and signals that nobody is selling to you. Fails when the product must persuade: Chayka (2016) says Airbnb began "Craigslist-rough", and credits its later aspirational listings with helping it "blow past" Couchsurfing.
- Brutalism, antidesign, neobrutalism: attention, designer audiences, entertainment. Disorienting structure fails for tasks; a raw surface over a standard layout can serve them (Gumroad, below).
- The civic service style (GOV.UK): universal audiences and trust.
- The dense instrument (Bloomberg Terminal): experts over years. Hostile to newcomers.
- Brand illustration systems (Facebook's "Alegria", later called "Corporate Memphis"): warm a product cheaply. Read as generic once copied.
- Art-directed editorial: form carries the content's meaning. Costs design time per piece.
- The "Linear look" (dark ground, glow, product UI as the image, thin lines, sans serif): signals a fast, serious tool. Now a trend of its own.

## Why languages rise and fall

- Each language answered a problem of its time: skeuomorphism "users do not know this medium", flat "ornament is noise", Material "flat lost the cues" (Moran 2015; Chan 2024; Material Design 1). The costs stay after the problem goes. Fashion also drives change: Malewicz (2019) names "freshness" as neumorphism's main benefit. When choosing a tradition, ask what problem it solved and whether this product has that problem. [SH, C, inferred]
- A style built to be easy to copy spreads fastest and then stops identifying anyone. Xoana Herrera, an illustrator on Buck's team for the Facebook work, said it shifted "towards something simpler to copy and implement" (Hawley 2019). When a direction borrows a current trend, say so, and say how long it is likely to look fresh. [CH, C, inferred from three cases]

## Where flat and minimal fail

- Weak signifiers cost 22% more time and 25% more fixations in an eyetracking study (Moran 2017, 71 users, nine page pairs). Three pairs showed no difference in gaze: one used contrasting in-line links, and two were sparse, conventional and had salient targets. A flat or minimal direction is safest on such pages. Flat icons took almost twice as long to find in one lab study, which partly measured thin type (Burmistrov et al. 2015). Adults aged 18 to 25 rated flat designs slightly higher than adults 35 and over (Moran 2016, 457 people, five screenshots). [FP, B, stated that signifiers must be seen. CH, B, stated for when flat costs]

## Audience

- The level of colour and complexity people like differs by country, education and age (Reinecke & Gajos 2014, 2.4 million ratings). In Google's research on its expressive Material 3, "a strong minority of users preferred calmer, less intense versions" (Google 2025, vendor research with no per-study methods). Name the audience before you choose a language, and do not assume your taste is theirs. [SH, B, stated. Lowered from A: one large study, a survey and company research]

## Sameness

- Interfaces converge through templates that ignore content, showcases where designers perform for other designers, feeds that spread one taste, design systems, and framework defaults (Müller 2018; Adams 2013; Chayka 2016; Google 2025; Wathan 2025). Their relative weight is unknown. When a direction looks familiar, find which of these produced the resemblance. [CH, C, stated]
- Some sameness is the grain of the medium. Chimero (2015): "Many sites will share design solutions, because we're using the same materials", which he reads as "not evidence of a visual monoculture". Nielsen (2000): users "prefer your site to work the same way". Müller (2018) answers that equating stereotypes with usability misunderstands both. The two camps mostly talk about different layers. By default, accept the grain in structure and make distinctive choices elsewhere (`core.md` lists exceptions). [SH, C, inferred for structure. AP, C, inferred for the surface]
- The machine-made look and how to avoid it are in `core.md`. Resemblance to that look is not proof of being generic. Stripe's indigo button and gradient ribbon are an owned asset that sits close to it (observed 2026-09-26). [CH, C, inferred]

## How strong identities are built

- Distinctiveness means looking like yourself: a few assets people link to the brand, used consistently. Buyers saw little difference between competing brands, and bought them anyway (Romaniuk, Sharp & Ehrenberg 2007, marketing data). Burberry dropped its knight in 2018 and brought it back in 2023 (Dezeen 2023). Before reworking an existing product, list the assets people already recognise, and keep or develop them. For a new product, choose one or two assets that no competitor owns. [SH, B for brands, C for interfaces, inferred]
- Strong identities extend one core asset, or a product principle, into every part of the system. Duolingo's typeface was drawn from the owl's feathers (Monotype case study). Mailchimp kept Freddie and chose Cavendish Yellow (Creative Review). Linear uses the common Inter, with Inter Display for headings, and aimed "to reduce visual noise, maintain visual alignment, and increase the hierarchy and density of navigation elements" (Linear 2024). These are accounts of intent; that Linear's identity comes from the principle, not the font, is inferred. A typeface swap is not a direction. For each direction, name the asset or the principle it makes visible. [UP, C, stated]
- Prefer identity elements that are hard to copy because they come from the product's own content, data or history. [CH, C, inferred]

## Plainness as identity

- For a universal audience, task-driven use and trust, GOV.UK chose restraint. Its designers "are happy when people say things are simple or even boring" (McCarthy 2015). Its type descends from Kinneir and Calvert's road-sign lettering, tested "in the rain, at night, at speed" (Terrett 2012), and "rather beautiful" icons were deleted when "no-one knew what they meant" (Terrett 2015). Applied rigorously, this plainness became recognisable. Craigslist's users complain about spam and search, not the look (Wolf 2009), but it has network effects most products lack. [SH, C, stated. Plainness as identity is inferred]
- Offer a restrained direction when the audience is broad, the use is a task, or trust is central. One way to make it distinctive is rigour: one typeface, a strict hierarchy, a clear voice. Do not choose it when the product must seduce. [SH, C, inferred]

## Where expression belongs

- A loud or raw surface works best when hierarchy, navigation and interaction stay conventional. For brutalism, Moran (2017) advises "keep it limited to visual design", and says antidesign "will backfire" unless the audience is designers or artists, or the product is entertainment (an opinion piece). Google's helter-skelter playlist looked "modern and exciting", but its usability scores suffered (Google 2025). Gumroad puts a neobrutalist surface over a standard layout (observed 2026-09-26). Müller (2018) faults the media-art museum ZKM's site for lacking "the avant-garde assertion" of its exhibitions; that for art and culture a structural experiment can be the point is inferred. [CH, C, stated. The art case is inferred]
- Platforms say where brand may live: accent colour used "judiciously", custom display type with system body text, familiar components, and branding that "defers to content" (Apple HIG, Branding, 2026-09-09). Microsoft (2013) points to composition, type, colour and motion. The platforms have an interest in native-looking apps. [DC, C, stated]
- Glass, soft shadows and ambient motion fail when they compete with the content. NN/g found Liquid Glass text hard to read over busy backgrounds (Budiu 2025, an expert review), and Apple added a more opaque "Tinted" setting in iOS 26.1 (MacRumors 2025). Neumorphic buttons have no figure-ground contrast at all (Malewicz 2019). One option: keep these effects off text and controls. [SH, C, stated]
- Art direction ties form to content at a cost per piece. Santa Maria (2008) fixed the grid and masthead and let each article take its own type, colour and layout. A direction can propose a fixed frame plus one art-directed page to show how the system bends. [UP, C, stated]
