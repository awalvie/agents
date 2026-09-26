# How to run and judge the test

1. Run both agents on the same model, each in a fresh session, with `PROMPT.md` and one
   requirements file.
2. Have a third agent rename the output files to A1–A3 and B1–B3, with A and B chosen at random
   for each requirements file. It removes HTML comments, `<meta>` and `<title>`, and keeps the key.
3. Open each file at 390 px wide for sets 1 and 3, and at 1440 px wide for set 2.
4. Judge the HTML before you read any explanation. For each requirements file, answer:
   - How many of the requirement bullets does each direction meet?
   - Do the three directions really differ, or are they one design in three colors?
   - Which set of directions shows more care in layout, type and detail?
   - Which single direction would you ship?
5. Then read the explanations, with citations removed, and note if they change your view.
6. Ask for the key only after you write down your answers.
