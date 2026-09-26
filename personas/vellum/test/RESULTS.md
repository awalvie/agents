# Test results, 2026-09-26

One judge (the repo owner) ranked every design without knowing which agent made it. Treat all
results as weak evidence.

## Blind test

Plain Claude and Vellum each made three full, interactive directions for the three requirement
sets in this folder. Vellum read its knowledge base first.

- Plain Claude's direction was the favorite in all three sets.
- In sets 2 and 3, Vellum's two directions were the least liked.
- Vellum used one slot in each set for a deliberately conventional direction.

## Taste rounds

Both arms were Vellum on the same prompt, with one difference: arm `kb` used the knowledge base,
and arm `nokb` did not. Each arm made three static mockups of one screen per round. In rounds 1
and 2, arm `kb` read the knowledge base first. In rounds 3 to 5, it designed first and then used
the knowledge base only to check execution.

- Round 1, bookshop: a tie. The two favorites were bright printed-zine styles, one from each arm.
- Round 2, portfolio: no preference.
- Round 3, cloud platform: the design-first arm won, and it made the favorite.
- Round 4, training app: a tie. The judge liked none of the mockups.
- Round 5, festival: a tie.

## Findings

- The prompt mattered more than the research. The judge disliked all 18 blind-test designs and
  liked the round 1 mockups. The round 1 prompt stated the judge's bar, "gorgeous while being
  functional", allowed no safe version, and asked for one static screen.
- Reading the knowledge base first made the designs safer. Using it as a check after designing
  never lost, and it improved details: contrast, quieter healthy states, labels and keys.
- Both arms produced almost the same three concepts in each round. The judge ranked by concept,
  not by arm. Concept variety is the limit, and the knowledge base does not change it.
