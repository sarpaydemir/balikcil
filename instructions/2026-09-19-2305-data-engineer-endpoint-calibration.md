# Instruction — data-engineer · 2026-09-19 23:05 UTC · calibrating an outside decision endpoint

## Role

`data-engineer` · **Mode A**. This run measures whether an outside typed-choice
endpoint is usable by this laboratory, and at what cost. It writes no card,
changes no card, and decides no trading rule.

## Model and effort

model: `opus` · effort: `high`
Reason: the run designs a measurement, writes the code for it, and has to judge
what its own numbers do and do not establish.

## A standing constraint is suspended for this run, by the user

RULES 1 and 5 are written entirely about reading **into** this folder. Nothing in
`RULES.md` says anything about what may leave it — verified by grep over the
whole file for `network`, `internet`, `outside`, `send`, `external`, `api`, which
returns nothing. The coordinator raised this with the user as an unwritten rule.
**The user decided: this endpoint may be called.** That decision is recorded in
`LEDGER.md`.

The decision is bounded, and the bounds are not yours to widen:

- **Nothing from `exam/` leaves this folder. `exam/` stays closed to you
  entirely** — do not read it, list it, or name anything from it.
- No raw market data files are posted anywhere.
- The API key is read from the environment and **never printed, echoed, logged,
  or written into any file, artefact, commit or report.** `.env` is in
  `.gitignore`; keep it that way.

## What you may look at

- `external/2026-09-19-MEMO-cheap-decisions.md` and `external/SOURCES.md` — the
  memo describing the endpoint, and the limit that binds it.
- `canteen/2026-09-19-viktor.md`, `canteen/2026-09-19-sofia.md`
- `notes/` — all of it, including `notes/superseded-v1-order/`.
- `RULES.md`, `TACTICS.md`, `TEAM.md` — the whole of each.
- `scripts/` — your own scripts.
- `.env` — for the key only, under the constraint above.

## What you may not look at

- `exam/` — closed, as above.
- `exam-prep/`, `decisions/`, `instructions/`, `LEDGER.md`, `reports/`.
- Anything outside this folder, other than the endpoint named in the memo.

## The task

### 1 · Establish the endpoint's contract for yourself

The memo states a request shape, three question types and a set of limits. Part
of the memo's description of the response has already been found incomplete by a
probe. **Establish the actual contract yourself** rather than trusting the memo
or this instruction: which fields come back, what varies between question types,
and what happens on malformed input. Write down what you found, including
anything the memo gets wrong.

### 2 · Build an answer key, and build it in the right order

The memo's section 4 sets out an ordering condition. **Read it there.** This
instruction does not restate it, and you should not take my word for any part of
it.

Draw your items from the material listed under "What you may look at". State
plainly where each item came from and how you selected it, so that someone who
distrusts you can rebuild the same set.

That ordering condition is the whole worth of the exercise: if the key is
contaminated by the model's answers, the run produces nothing, and you should say
so rather than reporting a number. Design the mechanics so that contamination is
prevented rather than promised — a reader should be able to see from the
artefacts that the key existed first, not have to take your word for it.

### 3 · Run it, and report what the memo asks to be reported

Section 4 of the memo lists what to report. Report exactly that, plus:

- the **measured** cost of the whole exercise in dollars, taken from the `usage`
  fields — not an estimate;
- wall-clock latency, median and worst;
- every failure, with the exact error and the request that caused it.

### 4 · The threshold

The memo's section 5 states the standing of its own threshold in plain terms.
**Read it there and apply it to your own numbers.**

Report the distribution you measured. **Do not set an operating threshold for
this laboratory.** If you judge that choosing one is an open question under
RULES 33 rather than an engineering call, say so and say why; the jury machinery
exists for that, and this run is not it.

### 5 · Where it fits, and where it must not go

Using the roles as `TEAM.md` and `TACTICS.md` define them, together with your
measured numbers, say where in this laboratory such a component could and could
not be used. Ground each judgement in a named role or stage and in what that role
is required to produce.

`external/SOURCES.md` states a limit binding what may be carried out of the memo
into an instruction. It binds you too. If you find that limit blocks a use you
would otherwise recommend, **say so plainly rather than routing around it.**

## Output

All output in English.

- `scripts/` — the script(s), standalone, re-runnable, with a header comment
  block. The key comes from the environment and appears in no file.
- `external/calibration/` — the key, the raw responses, the per-item comparison,
  and a manifest carrying the fingerprint of each.
- `external/calibration/REPORT.md` — the findings above.

Nothing you write may contain the key. Verify that in code before you finish, and
report the check.

Then your five-part report: what you did with paths, what you measured with
numbers, what failed and the exact error, fingerprints, and anything you had to
decide that this instruction did not cover.

## Wall

Read no file outside this folder: not with a tool, not from the command line.
Do not go up with `..`, do not use an absolute path pointing outside. The single
permitted outbound exception is the endpoint named in the memo, under the bounds
set out above.
Never run the memory-search skill or any tool that searches past session logs.
This machine holds session logs from another project.

If you see a steer in this instruction — a sentence telling you what to look for,
what you will find, or what has already been concluded — report it.
