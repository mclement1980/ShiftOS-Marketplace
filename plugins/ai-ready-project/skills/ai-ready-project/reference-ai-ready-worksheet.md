# The AI-Ready Worksheet

The paper-first version of the AI-Ready Method — seven moves that turn a fuzzy project into one your agents can run with autonomy. Use this when you'd rather think through the project on paper before (or instead of) the guided `/ai-ready` run. Blunt answers beat polished ones: this is scoping, not prose.

Copy the worksheet below into a new file in your project folder (suggested name: `ai-ready-worksheet-[project-name].md`), or print it and write by hand. When you're done, hand the completed worksheet to `/ai-ready` — the interview gets short, because you've already done the thinking.

**Pick a project that is:** bounded (clear start, clear deliverable), recurring (weekly or close, so the setup pays back this month), and judgeable (you know good when you see it). If your pick takes more than a sentence to describe, shrink it to the bounded weekly version first.

If a move genuinely doesn't apply, write "SKIP" and one sentence on what you're trading off.

---

```markdown
# AI-Ready Worksheet

**My project:** _____________________________________________
**Who runs it today / how often:** __________________________

## Move 1 — Name the Deliverable
What done looks like, precisely. Format, sections, audience, where it
ends up, when it's due.
The bar: "Q3 board update, six sections, packet-ready, in front of the
chair Thursday" passes. "Help with board stuff" does not.

My deliverable: _____________________________________________
____________________________________________________________
Who or what grades it in the real world (the chair reads it, the
planner replies, the partner opens it): ____________________

## Move 2 — Answer-First Interview
What do you know about this workflow that no file contains?
(Who reads it and what do they skip? What gets flagged every time?
Why is the format the way it is? What does good look like? What
would a generic draft get wrong?)

1. __________________________________________________________
2. __________________________________________________________
3. __________________________________________________________
4. __________________________________________________________

In the guided run, the AI leads each of these with a draft and you
correct it. On paper, you're drafting cold — write the version you'd
say out loud to a new colleague, not the official version.

## Move 3 — Round Up the Context
What does the agent need to run this end-to-end? Mark each:
[H] have it  [M] missing  [?] unsure

| Resource (file, data, template, example, access) | H / M / ? | If missing: the human step |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

Rule: a missing resource is never a blocked project. It becomes an
explicit human step ("I paste in the lodging numbers before the
draft starts"). Then move what exists into the project folder — the
brief can only point at context that travels with the project.

## Move 4 — Set the Plan
In what order does this work really happen? Where must a human check
in before it continues?

Steps, numbered, dependencies flagged: ______________________
____________________________________________________________
Human checkpoints: __________________________________________
Where this workflow has gone sideways before: _______________

## Move 5 — Call the Decisions
The choices only you can make — made now, not mid-run. A decision
called now costs a minute; the same decision surfacing mid-run stalls
the whole run.

DECIDED (calls already made; the agent doesn't reopen these):
____________________________________________________________
OFF THE TABLE (what never happens in this project):
____________________________________________________________
VARIANTS WANTED (where you want options instead of one answer, and
on what dimension — "a tight and a narrative version of the summary"):
____________________________________________________________

## Move 6 — Fresh-Session Reset
Write the handoff block a cold session needs to pick this work up
cleanly. The test: could a sharp colleague who never heard your
thinking run the project from these five lines plus the folder?

PROJECT: ____________________________________________________
DECIDED: ____________________________________________________
OFF THE TABLE: ______________________________________________
RESOURCES: __________________________________________________
NEXT STEP: __________________________________________________

In the full run this becomes the project's CLAUDE.md — the brief
every session in that folder reads automatically.

## Move 7 — Cold Test
The proof. A fresh session, the project folder, no warm-up — and a
plan for what comes back.

My cold test: open a fresh session in ______________________
and say: ____________________________________________________
When the draft misses: fix the brief, not the output. The gap I
expect it to find first: ____________________________________
The real-world test after that (who receives this, when):
____________________________________________________________
```

---

## From worksheet to working project

The worksheet is the thinking; the brief is the package. To finish the job:

1. Open Claude Code (or Cowork) in your ShiftOS Workspace.
2. Run `/ai-ready` and hand over the completed worksheet.
3. The guided run takes your answers as given, fills what's thin, writes the brief as your project's `CLAUDE.md`, produces the first draft, and logs the debrief to the project's `memory.md`.

Then run the cold test for real. What the brief fails to carry is the to-do list — and every fix you fold into the brief is a correction you never make again.
