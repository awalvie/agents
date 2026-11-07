# Apps and web pages

Use this with the skill when the thing is a screen of an app or a web page.

## States to record

Read the code for every state, then record each one on each screen size the product supports:

- Empty, first use, loading, slow or no connection, an error.
- A lot of data, long text, odd names.
- An item picked, a menu open, a sheet or dialog open, a form empty and typed in.
- Each theme the product has.

Reach states that are hard to get, such as no connection or a given date, with the browser's
tools: block a request, or fix the clock.

## Prototypes

- A prototype is a screenshot of the running app with the version applied, not a drawing.
- Drive a headless browser, signed in as a test account.
- Make test data through the app's own API. Make it fit the case that it shows. Remove it after,
  with the same script.
- Before you edit, copy each file and save the version-control status and diff. After, copy the
  files back and compare. Never use a command that discards the person's changes.
- Keep the scripts, so that every round shoots the same states the same way.

## Look closely

- Look at three sizes: the whole screen, each card or section, and each group inside it. Crop at
  a higher scale, after the last change.
- Check how each group wraps, where each text is cut, and whether rows and edges line up.
- Read every word in the crops. A fault in a crop counts even when the whole screen looks fine.

## Interaction

For each control, write:

- What a tap or a click opens: a page, a pane, a sheet, a menu or a dialog.
- What a long press does, including what the system does by default, such as a link preview.
- What feedback it gives: a haptic, a sound, a message, a change on the screen.
- What hover and the keyboard do.

Name the dialogs that the browser or the system draws, as a screenshot may not show them.

## Review page

- Before and after, in each state and on each screen size.
- Mark each change on the "after" shot with a box and a number, and list the numbers beside the
  shot. Take the box positions from the page, not by eye.
- Give the reviewer the shots, and name the faults of the shots, for example a fixed bar drawn
  over the content.
