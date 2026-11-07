Shared grocery list: three directions. Each file shows the list and adding an item on phone-sized screens, and some taps work. All three use the same household (Maureen, Tom, Anna, Sam), the same fifteen items, and the same moment, with Anna and Tom shopping at the same time. Directions 2 and 3 load one font from Google Fonts and fall back to a system font when offline.

Assumptions:

- A UK household with one shared list, where everyone has their own phone and account.
- Changes reach the other phones within a few seconds.
- The app sorts items into shop sections by itself.
- Whoever is free does the shopping.

Direction 1, `direction-1.html`: one checklist, sorted the way the shop is laid out. This is the expected answer, and the baseline for the other two.

- It has shop sections, a large tick on each row, and the first letter of the person who asked. The add field sits at the bottom, where the thumb is.
- When Tom ticks an item, it shows his name. Tapping an item's name shows who asked and their note, with a ready-made "which cheese?" message.
- When you add, the app suggests things the household has bought before, and warns you if the item is already on the list.
- Why: people read a new app through the ones they know. Typical-looking pages are liked more at first sight, which rests on moderate evidence. Picking from suggestions is easier than recalling a word, which is well established.
- Tradeoff: it is the least distinctive of the three. "Who asked" is only a letter until you tap it. Adding works best with clean hands, because it is keyboard first.

Direction 2, `direction-2.html`: at home you add, at the shop you shop. The two jobs happen in different places with different hands, so the app has two modes over the same list. Its real departure is the home side: the app opens on adding, not on the list, because adding is what most of the household does most of the time. The shop side is direction 1's list, made bigger and plainer.

- At home, you can hold a button and speak, type, or tap tiles of the household's usual items. Tiles already on the list are greyed out, and typing something already listed gets a warning.
- At the shop, the top bar turns yellow. Names are 26 px, and one tap on an item puts it in your trolley, with a large Undo. Items Tom takes shrink to a grey line with his name.
- Why: people forget which mode they are in, which is solid evidence. So the mode is shown in words and in the colour of the whole bar. Undo beats "are you sure?" prompts, which people learn to click through, also solid. The big type is my judgement, not a measured finding.
- Tradeoff: the mode is one more thing to learn, and someone who forgets to switch sees the adding screen in the shop. "Who asked" shows only where someone wrote a note. Voice is untested.

Direction 3, `direction-3.html`: the list on the fridge, where everyone writes in their own ink. It keeps the habits of the paper list the household already shares.

- Lines stay in the order they were written. Each line has the writer's name in the margin and is set in their ink colour.
- Items are crossed out in the ink of whoever got them. A question and its answer are written on the line itself.
- Adding something already on the list offers "Add me to his", so the list keeps one line instead of two.
- Why: it is the only direction where "who asked" shows on every line with no tap. A name always sits beside each colour, and every ink passes 4.5:1 contrast on the paper. A familiar object teaches a new app by analogy, which rests on practitioner accounts. The serif font is a choice of voice: serifs do not change reading speed, which is moderate evidence.
- Tradeoff: the list is not in shop order, so the shopper criss-crosses the shop.

Placeholder or untested in all three:

- The keyboards are drawn.
- Sync, voice, messages and calls are not built.
- In directions 1 and 3, the second screen shows what tapping a name opens, but that tap is not wired on the first screen.
- Shop sections are set by hand.
- Nothing has been tested with users. The main unknowns are one-handed tap accuracy in a busy aisle, and whether older parents can read the initials (1), switch modes (2) or tell the inks apart (3).
- None of the directions handles two shoppers tapping the same item in the same second, or a shop with no signal.

What the choice should rest on:

- If adding is the bottleneck (things never get onto the list), or the shopper needs bigger targets, choose direction 2.
- If "which cheese?" questions are the main failure, choose direction 3.
- If the main risk is that older parents never open the app, choose direction 1.
- Directions 1 and 2 need reliable automatic sorting into shop sections. Direction 3 does not.

Open questions:

- Does each older parent have their own phone?
- Should adding an item alert whoever is shopping right now?
- Does the household use more than one shop?
- How good is the signal in the shop? Preventing double buying depends on it.
