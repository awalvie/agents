Three directions for The Paper Moth, an invented bookshop. Each file shows the home page and the event page. The dark bar at the top is a prototype control, not part of the design. It switches screens and shows the event page in five entry states: ticketed with 4 seats left, ticketed with seats free, free but sold out, free with booking, and free drop-in. All three use the same events and copy, so they differ in form, not in content.

Assumptions I made:

- Many visitors land on an event page straight from a social post and never see the home page. So each event page names the shop, the address, the price and the seats near the top.
- The shop is in the UK. Prices are in pounds, and the phone number is in a range set aside for fiction.
- Author readings are upstairs, up 16 steps with no lift. Story hours are on the ground floor.
- The prototype treats today as Saturday 26 September 2026.
- The shop, the people and their books are invented. The book club book, Piranesi by Susanna Clarke, is real.

The evidence, in plain terms:

- One study (NN/g 2016) found that people use hidden menus much less, on phones too. So all three keep two navigation links in view.
- Larger body text helped comprehension in one study (Rello 2016). Nobody has shown where that gain stops. So body text is 18 to 20 px rather than 16.
- Eyetracking (NN/g 2010, practitioner evidence) found that people ignore decorative pictures. So no direction uses stock imagery to fill the gap left by having no photos.
- Studies disagree on whether a familiar-looking site or a novel one is liked more, and nobody knows why. That uncertainty is the real question between these directions.
- I checked the main text and background colours. Each pair is at least 5.2:1, above the 4.5:1 minimum for normal text.

- Direction 1: The listings (direction-1.html). A plain, well-made list of dates where every row says in words whether you pay and how you get in.
  - Why: phone visitors come briefly and want one answer fast. Practitioner guidance says brief-visit sites should be simple and clear, and one sprint case found the plain option explained a product best. That is case evidence, not a study.
  - The list is in date order, grouped by week, with filters for the three kinds of event. Each row ends in a coloured status line, "£6 · only 4 seats left" or "Free · just turn up", with an icon so colour is not the only signal.
  - The event page puts When, Where, Entry and For in a fact list, then a seat panel with a bar and the button. On phones, a bar pinned to the bottom of the screen keeps the price, the seats left and the Book button in view.
  - The shop's character comes only from one reading serif (Literata), cream paper and a small moth mark.
  - Tradeoff: it is the least eccentric of the three. It could be any good listings site, so it gives up most of "feels like the shop".

- Direction 2: Posters in the window (direction-2.html). Every event gets a woodtype poster, built from its own details, like the posters taped in a shop window.
  - Why: the owners cannot supply photos, so the picture comes from the words. The poster is made from type, date, price and a colour and ornament for each kind of event. The owners fill in fields and get a poster.
  - The poster carries the facts, not decoration: the day, the date, the title, the time and the entry strip. A sticker ("Only 4 left") or a rubber stamp ("Sold out") appears only on events where seats are scarce, so they stand out.
  - The layout underneath is conventional: a grid, a plain details card, a normal button. Advice to keep a loud look on the surface and leave the layout conventional is expert opinion only.
  - Tradeoff: about four events fit on a phone screen, and titles in condensed capitals are harder to read at small sizes. The five yellow story-hour posters look alike. Visitors have to learn the colours; the intro explains them. It also loads two web fonts.
  - Not built: the same poster could become the image for the owners' social posts, so the post and the page match.

- Direction 3: The contents page (direction-3.html). The site reads like a small book, and the booksellers' voice is the identity. It uses no pictures at all.
  - Why: this one changes the structure, not only the look. The home page groups events by rhythm instead of date. The visiting authors are one-off evenings and some sell out, so they come first. Then the monthly book club, then story hour every Saturday.
  - The regular events state their terms once ("Every Saturday, 10:30am. Free, no booking"). Each entry has a dotted line leading to its date, with the entry status below it in italics, or in red when seats are scarce. A "Coming next" line covers anyone asking what is on soon.
  - A signed note from the owners and one line per event starting "In which..." carry the warmth. The fonts are EB Garamond for text and IM Fell for headings, with the red that old books used for headings.
  - Tradeoff: a date appears in only one of three sections, so "what is on this Saturday" takes a moment longer. The owners must keep writing: a note each month and a line for each event. On a phone the Book button sits near the bottom edge of the first screen. Garamond is less crisp than the others on cheap screens.

Placeholder or untested in all three:

- The booking and waiting-list steps are not designed. The buttons show a notice instead.
- Nobody has tested any of it with users.
- The fonts load from Google Fonts. Without a network they fall back to system fonts.
- The posters in direction 2 were not tried with very long titles.

The choice should rest on these questions:

- How do most visitors arrive? If most tap straight into an event page from a post, compare the event pages first. Direction 1 keeps the answer in view best on a phone.
- How much does "warm and a little eccentric" weigh against speed for a first-time visitor? Direction 1 gives up character, direction 2 gives up some legibility and density, and direction 3 gives up some speed in finding a date.
- How much can the owners keep doing? Direction 2 needs only the event fields. Direction 3 needs regular writing and gets worse without it.

Open questions:

- What ticketing system does the shop use? It decides what the Book button leads to.
- How often do events really sell out?
- What are the real rooms and access details?
- Can the owners get publisher images of authors or covers? If so, direction 1 or 3 could show them.
- Would the owners want the posters for their own social posts?
