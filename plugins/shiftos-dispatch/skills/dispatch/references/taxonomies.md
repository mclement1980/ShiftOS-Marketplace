# DISPATCH Taxonomies

Internal reference lists for building project-specific prompts. Never dump a complete taxonomy into chat. Filter to the smallest set that helps the user make the decision.

## D — Deliverable shapes

Propose three concrete shapes only when the user has not already named a real object.

### Written

- Brief
- Memo
- Proposal
- Article
- Chapter
- Script
- One-page report
- Email or message sequence

### Structured data

- Spreadsheet
- Financial model
- Tracker
- Comparison matrix
- Filled form
- Database-ready record

### Visual

- Presentation
- Dashboard
- Diagram
- Mockup
- Infographic
- Chart
- System map

### Operational

- Plan
- Agenda
- Checklist
- Schedule
- Workflow
- SOP
- Template
- Runbook

### Functional

- Code
- Script
- Automation
- Prompt
- Subagent
- Skill
- Configuration file
- Website

### Decisions and records

- Decision log
- Meeting record
- Action register
- Commitments
- Status update
- Review packet

Each proposal must be specific enough to become a filename. “Dashboard” is too broad; “single-screen HTML campaign-performance dashboard for the quarterly leadership review” is usable.

## I — Interview categories

Select two to four. Tie every question to the named Deliverable.

### Intent

- Why now?
- What decision or action should this enable?
- What would success look like that is not obvious from the request?

### Audience

- Who actually reads, uses, approves, or operates this?
- What do they already know?
- What do they care about first?
- What causes them to stop reading or distrust the work?

### Voice and tone

- Whose voice should the artifact use?
- Formal, conversational, urgent, restrained, instructional, or executive?
- What phrases, habits, or stylistic tells should be avoided?

### Constraints

- What is off-limits?
- What has already been tried and rejected?
- What legal, privacy, brand, political, relational, or accessibility constraints apply?

### Tradeoffs

- Speed or polish?
- Breadth or depth?
- Safe consensus or a bolder recommendation?
- Editable structure or fixed visual fidelity?

### History

- Which prior versions matter?
- Which decisions are already settled?
- Which old paths or files are provenance rather than current authority?

### Relationships and authority

- Who owns approval?
- Who receives the work?
- What can be said to whom?
- Who may change the result after Handoff?

### Preferences and house rules

- What would make the user say “that is not how we do this”?
- Which naming, structure, evidence, or review conventions must be followed?

## S — Supplies categories

Surface roughly six relevant items and place every one under Have, Missing, or Unsure.

### Files and source material

- Drafts and prior versions
- Data exports
- Transcripts and notes
- Templates, brand guides, and examples
- Accepted definitions or control files

### Tools and capabilities

- Browser or app control
- Code execution
- File read/write access
- Connectors
- Skills, plugins, and subagents
- Rendering or export tools

### Credentials and access

- Account identity
- Login state
- API keys or tokens
- Two-factor route
- Folder, project, or repository permission

### External information

- Current pricing
- Dates, deadlines, and schedules
- Legal or regulatory facts
- Analytics and operational data
- Recipient and organization details

### People and decisions

- Human owner
- Subject-matter source
- Reviewer
- Approver
- Recipient
- Operator
- Exception owner

### Constraints and settings

- Deadline
- Budget
- Length
- File type
- Canvas or page size
- Naming convention
- Save location
- Accessibility requirement

### In-the-user’s-head context

- Strategic intent
- Taste
- Project history
- Relationship dynamics
- Known failure patterns

### Valid routes out of a gap

- User supplies it now
- Named human supplies it later
- Verify through an authorized tool
- Use an explicit placeholder
- Use a manual equivalent
- Remove the dependent scope
- Stop the project cleanly

## P — Plan components

Include only the components that apply.

- Numbered execution sequence
- Resource used at each step
- Scope and rough size
- Decision points
- User checkpoints
- Risk areas
- Fallback approaches
- Definition of done
- Output paths and formats
- Verification method
- Permission boundary
- Final move: “Show every artifact and wait”

## A — Alternatives dimensions

Choose one or two dimensions and generate exactly three approaches.

- Tone: formal / conversational / playful / urgent / understated
- Length: tight / standard / exhaustive
- Structure: chronological / thematic / problem-solution / inverted pyramid / Q&A
- Angle: skeptical / enthusiastic / pragmatic / contrarian / data-driven / story-driven
- Audience level: beginner / practitioner / expert / executive
- Format: prose / bullets / table / diagram / hybrid
- Boldness: safe consensus / ambitious / provocative
- Scope: narrow-deep / balanced / broad-surveying
- Specificity: principles / concrete examples / step-by-step
- Production route: manual / assisted / automated
- Fidelity: fast-editable / balanced / fixed-presentation quality

An Alternative is a real approach, not a synonym. “Short,” “medium,” and “long” count only when length is the decision that matters.

## T — Tripwire categories

Propose only applicable boundaries and state them as absolutes.

### External action

- Do not send.
- Do not publish.
- Do not deploy.
- Do not invite or enroll.
- Do not contact the audience or stakeholder.
- Do not purchase or create a paid job.

### Live systems

- Do not change settings.
- Do not write to production.
- Do not modify cloud-folder structure.
- Do not create or alter calendar events.
- Do not install a package outside the approved local scope.

### Data and claims

- Do not invent facts, metrics, quotations, sources, or approvals.
- Do not expose sensitive or client-specific information.
- Do not replace a Missing value with an unlabeled estimate.
- Do not claim an outcome above the observed evidence level.

### Destructive actions

- Do not delete.
- Do not overwrite accepted or frozen artifacts.
- Do not rename or move governed folders.

### Scope and methodology

- Do not expand beyond the named Deliverable.
- Do not rewrite settled methodology or definitions.
- Do not revive superseded paths as current authority.

### Stop conditions

- Stop when source authority conflicts.
- Stop when required access cannot be verified.
- Stop when a material decision is missing.
- Stop when a test requires ungranted authority.
- Stop when the active model is below the supported floor.

## C — Restart signals

Assess these honestly before writing Continue.

### Behavioral

- Context pollution from abandoned threads and rejected drafts
- Recurring mistakes after correction
- Goal drift
- Repeated walls
- Declining iteration quality
- New information that invalidates earlier work
- More correction than useful progress
- User frustration or agent overconfidence

### Numeric or UI

- Roughly fifteen or more sprawling turns
- A visible context indicator near or above seventy percent
- Automatic compaction or summarized context

### Continue contract

Four sentences:

1. **Decided:** the key choices already made.
2. **Off the table:** rejected directions and closed lanes.
3. **Resources:** what is in hand and what is pending.
4. **Next:** the single next move.

## H — Handoff and real-world tests

Select two to four tests. At least one should meet the artifact in its actual environment when one exists.

### Communication

- Preview in the actual mail or messaging client.
- Send only with explicit permission.
- Collect the real recipient’s response.

### Written output

- Open in the destination editor or viewer.
- Review at the actual page width or print size.
- Ask a named human for one specific form of feedback.

### Visual or presentation

- Render at the intended dimensions.
- Inspect every page, slide, or state.
- Test on the actual display or device.
- Capture screenshots and console evidence.

### Dashboard or analysis

- Load bounded real data.
- Verify calculations against the source.
- Test filters, empty states, and labels.
- Observe whether the decision owner can answer the intended questions.

### Code, automation, or workflow

- Run with real bounded inputs.
- Test the happy path and a meaningful failure path.
- Verify logs, outputs, and recovery.
- Test restart in a fresh environment.

### Project kickoff

- Block real time and begin the first work unit.
- Observe whether the dispatch reduces friction or exposes another gap.

### Interpersonal or operational

- Conduct the real conversation or meeting.
- Run the plan against actual logistics and stakeholder pushback.

### Research or learning

- Apply one conclusion to a real decision.
- Observe whether behavior or output changes.

### Evidence that may return

- Screenshot
- Console output
- Render manifest
- Calculation check
- Human review note
- Recipient response
- Usage or performance metric
- Failure report
- Approval record
- Revision request

### Evidence levels

1. Prepared
2. Built
3. Locally verified
4. Handoff authorized
5. Handed off
6. Return evidence received

Never infer a higher level from a lower one.
