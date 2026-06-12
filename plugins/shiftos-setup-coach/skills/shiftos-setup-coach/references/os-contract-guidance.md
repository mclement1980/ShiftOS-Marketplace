# OS Contract Personalization — Step 9 Mechanics

The workspace root `CLAUDE.md` is the operating contract every session obeys. Step 9 personalizes exactly one region of it. This reference covers the mechanics and the quality bar.

---

## The two marker pairs in root CLAUDE.md

| Markers | Owner | What happens |
|---|---|---|
| `<!-- FIRST-RUN-START -->` … `<!-- FIRST-RUN-END -->` | Step 0 | The bootstrap pointer at the top of the contract. Once the plugin check passes, delete the entire block including both markers — silently. Its job was routing the very first session to the coach; after that it's dead weight every session would re-read. |
| `<!-- PERSONALIZATION-START -->` … `<!-- PERSONALIZATION-END -->` | Step 9 | The **My Operating Preferences** section. Replace the bracketed placeholder content between the markers with the owner's real rules. Keep both markers in place — returning-user visits edit between them. |

**Hard rule: nothing outside the markers gets touched.** The house rules (never invent figures, board-facing is final-polish, archive don't delete, the session-start order) are program doctrine — they're not up for per-user editing during setup. If the owner wants a house rule changed, note it in memory and tell them it's a conversation for their facilitator, not a setup edit.

## The three subsections to fill

### Always

3–6 standing behaviors, each one line, each phrased as an instruction. Draft candidates from the whole conversation — the Master Profile's "Working With Me," the writing rules, things they corrected during setup. Confirm each with the owner; keep only what they'd actually enforce.

Quality bar — each line should change observable behavior:

- Too soft: "Be helpful and thorough."
- Right: "Lead with the recommendation; reasoning after."
- Right: "Anything touching the board or commission: flag it before drafting, ship it final-polish."
- Right: "When I'm vague, make your best call and open with the assumption you made."

### Never

3–6 hard lines beyond the house rules. The house already bans invented figures and unauthorized deletions — don't duplicate; add what's personally theirs:

- Right: "Never pad a draft to look thorough — short and done beats long and impressive."
- Right: "Never use the banned words in `ME/writing-rules.md`, even in outlines and notes."
- Right: "Never frame this system to anyone as replacing staff — it exists to widen what this team covers."

### Format defaults

How deliverables arrive unless the request says otherwise. Pull from communication preferences (Master Profile section 5) and the writing rules:

- Length ceilings ("one page unless I ask for more").
- Structure defaults ("bullets for status, prose for argument").
- Options discipline ("three max, with a recommendation and one line of why").
- Draft definition ("a 'draft' means complete — no skeleton outlines handed back to me").

## Process

1. Read the current personalization section.
2. Draft all three subsections from everything learned so far.
3. Show each subsection, confirm or adjust via AskUserQuestion, one at a time.
4. Edit the file — replace only the content between the markers.
5. Tell the owner: the contract loads at the start of every session, so these are now standing law — fully in force from their next fresh session.

## Returning visits

When a returning user picks "re-do my operating preferences": read what's between the markers, walk each line keep/strike/revise, write back, log the change in memory with the date and the reason.
