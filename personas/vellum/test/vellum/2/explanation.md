Clinic front desk: three directions

All three use the same invented clinic day: Tuesday 29 September 2026 at 10:27, six therapists, 83 booked appointments plus 3 cancellations, two patients running late, three waiting, two still to pay, and a waitlist of six people. They differ in how the day is laid out and how a booking is made, not in what they show.

To open the booking screen directly, add these to the address: direction-1.html#gap or #book, direction-2.html#book or #gap, direction-3.html#book. Each file also works by clicking or by keyboard.

Direction 1: the appointment book (direction-1.html)

- Idea: the familiar clinic calendar, done carefully. One column per therapist, time runs down the page, and you click a free slot to book it in a side drawer.
- Free time is drawn as dashed boxes inside each therapist's hours, showing how many waitlist patients would fit and who cancelled. The search box at the top finds a caller's appointment today, so it can be moved or cancelled. The right-hand rail lists, in order: running late, waiting, to pay, free today, waitlist. The problems of the moment never scroll away.
- Hours off and lunch are hatched out, so you cannot book there. Each block shows a status chip (Late 12m, Arrived, In session, To pay £55, DNA), and treatments that need the Studio or the shockwave unit are tagged.
- The drawer keeps the calendar visible and draws a preview block where the booking will land. Choosing a treatment limits the list to the therapists who give it. The time list shows only valid start times, and a room check says whether the Studio or the machine is free. The footer holds a read-back sentence for the caller.
- Evidence: layouts that look typical for their kind are liked more at first sight, and familiar interfaces are easier to learn (one credible study each, B). In one design sprint, "the boring, traditional approach" won (a single case, C). Things that are hidden get used less (one NN/g study, B), which is why the late, waiting and to-pay lists stay on screen.
- Tradeoff: the calendar shows one day. A caller who asks for "a shockwave slot any afternoon this week" makes the receptionist step through days and therapists one by one in the drawer. It is also mostly mouse work. It gives up speed on phone bookings in exchange for being easy to learn.

Direction 2: the run sheet (direction-2.html)

- Idea: the day as one list in time order, like the paper day sheet on a clinic desk, driven by the keyboard. You book by typing a line such as `anna kow fu thu am priya` while the caller talks.
- The list folds away everything already seen and paid. Patients who still need something (did not attend, to pay) stay visible above the "now" line. Free time appears as hatched rows in the list, with "1 on waitlist fits · F to fill".
- The command line reads names, treatments (fu, ia, sw, rp…), days, times of day and therapists as you type. It shows how it read each word and the matching free times. Enter books the highlighted time, and Tab switches between patients with similar names. "pay singh", "in doyle", "move evans" and "cancel walsh" act on today's list. They skip appointments that can't take that action, and Tab steps through the other matches. A word counts as part of the name while it still matches a patient, so "tom chen" is not read as tomorrow.
- Single keys act on the highlighted line: A arrived, M move, X cancel, S shorten a late session, F fill free time, Z undo. The keys are printed on every action button and in the bar at the bottom, so the fast way is visible while you use the slow one. Taking payment is deliberately two steps: P, then 1 for card, 2 for cash, 3 for invoice. There is no undo for money.
- Type: one type family (Atkinson Hyperlegible) at one size. Weight and grey are the only hierarchy. Numbers use its monospaced cut so times and phone numbers line up and read back clearly.
- Evidence: products used all day by people who know them well can be denser and tighter (one studio's framework, C). Showing shortcuts next to menu commands sped up learning them (one study, B). A command line is a hidden path, and hidden paths cost new users (inferred). The knowledge base has nothing on whether this typeface helps with reading numbers aloud; that choice is my reasoning, not a finding.
- Tradeoff: it loses the picture. You cannot see the shape of one therapist's day, or when the Studio and the machine are busy, without filtering. Temporary staff pay a learning cost. It also assumes a headset: with a handset in one hand, typing a whole booking line is slow.

Direction 3: the gap board (direction-3.html)

- Idea: the desk's real job is to keep therapists, rooms and the machine in use. The whole day fits on one screen as horizontal timelines, and unused time is the only loud colour.
- Six therapist rows sit above two lanes for the Studio (reformer) and the single shockwave unit, so you can see when the machine is busy. The header shows "7 gaps · 3 h 45 min left to fill".
- Below the board, "Fill now" lists the gaps that a waitlist patient fits (right treatment, therapist, time window, machine free). "Book" fills the gap in one click. The same area lists late patients and people waiting to pay. Selecting a late patient shows the patient booked next and offers to shorten the session so it still ends on time ("Shorten to 10 min from ETA 10:35"). Move keeps the old appointment until the new time is booked.
- Booking is a search called "Find a time". You enter the patient, the treatment, the therapist or anyone, the days and the time of day. It proposes three best options, each with a reason ("with the therapist she usually sees", "soonest, fills a gap today") and shows every free start in a therapist-by-day grid. It only offers times when the room or machine is free.
- Type: a condensed face (IBM Plex Sans Condensed) so surnames fit in half-hour blocks.
- Evidence: we find a target faster when it differs from everything around it (replicated perception research, A), and colour works as a signal when used in small amounts (a quoted cartographer, unchecked). So the saffron is kept for gaps only. Showing a recommended default beside the full list, rather than cutting options, fits the finding that too much choice hurts only when options are hard to compare (a meta-analysis, A). The room and machine lanes are my inference from the brief, not a tested pattern.
- Tradeoff: at 1366 to 1440 pixels wide a half-hour block is about 48 pixels, so surnames get cut ("Mitche"). The first name goes underneath, and treatment is shown only when it is not a follow-up. Find a time covers the board while you book. It also brings the most new ideas to learn (lanes, gap cards, ranked options), and a loud colour on screen all day may start to nag.

What is placeholder or untested, in all three

- All patients, times and prices are invented. Availability on days other than today is generated at random, so the future-day slots mean nothing.
- Undo works for one step only. Text messages and offers only show a message. The day arrows, the new-patient form and the card terminal do nothing. Payment itself was not designed, because it is not one of the two screens asked for. Payments are the one action with no undo.
- Two receptionists booking the same slot at once is not handled. There is no accessibility audit and no screen-reader test. Directions 2 and 3 load their fonts from Google Fonts and fall back to system fonts offline.
- Nobody has used any of these. I checked each one in a headless browser at 1366×768, 1440×900 and 1920×1080, and scripted the main clicks and keys.

Assumptions I made

- A UK private clinic: pounds, 24-hour times, insurers such as Bupa. Open Monday to Friday, 07:30 to 20:00.
- Rooms: each therapist has a home room, and James and Tomasz share Room 2 on different shifts. Reformer rehab needs the Studio. There is one shockwave unit that moves between rooms.
- Not every therapist gives every treatment: shockwave, acupuncture and reformer need a trained therapist. The brief does not say this.
- The clinic keeps a waitlist of patients who want an earlier slot, with their preferred therapist and times.
- Patients pay at the desk after the session.

What the choice should rest on

- Directions 1 and 3 share the same picture of the day (time by therapist), turned 90 degrees. They differ in booking: a form for one therapist on one day, against a search across therapists and days. They also differ in what comes first: the next patient, or the unused time. Direction 2 is the only one without a time grid.
- How bookings arrive. If most come by phone with conditions attached ("Thursday morning, with Priya"), direction 2 or direction 3's Find a time will be faster than stepping through a calendar. If most are rebookings made at the desk after a session, direction 1 is enough.
- Headset or handset. Direction 2 needs two hands on the keyboard.
- Where the time goes today. If cancellations stay unfilled because nobody spots the gap or remembers the waitlist, that is direction 3's whole purpose.
- Staff turnover. If temporary or new staff cover the desk often, direction 1 costs least to learn.
- Screen width at the desk. Direction 3 needs 1440 pixels or more to show names well.
- A cheap way to decide: give both receptionists three real tasks in each direction after ten minutes of practice. Book "shockwave, any afternoon this week" for a caller, fill a cancellation from the waitlist, and deal with a patient who is 12 minutes late. Time them and count errors.

Open questions

- Do receptionists wear headsets?
- Is there a waitlist today, and where is it kept?
- Which treatments need which rooms, machines or qualified therapists?
- How are payments taken: card terminal, insurer billing, packages of sessions?
- What screen size and browser does the desk use?
- Do the two receptionists split the work (one on the phone, one at the counter)? If so, they might each want a different direction on their own screen.
