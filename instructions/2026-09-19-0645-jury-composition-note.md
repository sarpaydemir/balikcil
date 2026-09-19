# Instruction record — jury · 2026-09-19 06:45 UTC · the zero-trade contracts

## Why this file exists

RULES 4: the full copy of every instruction is kept. This file records the
composition of the first jury and the preamble each juror received. The body of
the question is the file
`instructions/2026-09-19-0640-juror-zero-trade-contracts.md`, sent verbatim
after the preamble below.

## The deviation, named

RULES 33–35 create two new roles, `juror` and `referee`, and the definitions
were written to `.claude/agents/juror.md` and `.claude/agents/referee.md`.
**Neither loads in the session that wrote them** — the harness reads the agent
registry at session start, and both were refused with
`Agent type 'juror' not found`.

So the first jury sits with three **existing** definitions instead, chosen so
that the three are genuinely different instruments rather than three copies of
one:

| juror | definition | why this one |
|---|---|---|
| 1 | `skeptic` | its whole job is attacking a claim |
| 2 | `canteen-chair` | its whole job is holding a position together from evidence |
| 3 | `data-engineer` | it knows what the archive rows physically are |

All three definitions state that `RULES.md` and `TACTICS.md` are authoritative
and win over their own text, and `RULES.md` now carries rules 33–35. Serving on
a jury is therefore not a contradiction of `data-engineer`'s "stop and ask"
clause: that clause forbids filling a gap **alone**, which is the same thing
rules 33–35 forbid.

**From the next session onward the purpose-built `juror` and `referee`
definitions are used and this substitution ends.**

**The referee does not sit yet.** `referee` does not load either, and no
existing definition is a fit: `exam-candidate` cannot read a file,
`reporter` cannot conclude, and the general-purpose agents carry `Bash`, which
would break the structural rule that only `data-engineer` has it. Under
RULES 35 an unratified outcome is not an outcome, so **the question stays open
until the referee sits**, and everything resting on the present answer is
provisional until then. That is recorded in `LEDGER.md` rather than quietly
carried.

## The preamble each juror received

Juror 1 (`skeptic`):

> You are sitting as **juror 1** of three under RULES 33–35, not in your usual
> role. Three jurors answer this question independently and a referee ratifies
> the outcome. You will never see the other two answers. Your own definition
> says `RULES.md` wins where it differs from your definition, and RULES 33–35
> is what puts you here. Write your answer to
> `decisions/2026-09-19-zero-trade-contracts/juror-1.md` and write nothing else
> anywhere. Answer in the four parts: answer in one sentence; what it rests on
> with the file and line quoted; the strongest case against your own answer;
> confidence 1–5 and what would change your mind. An answer citing nothing does
> not count (RULES 34). You may not decide a trading rule, a threshold, a
> score, or a change to a rule in `RULES.md`.

Juror 2 (`canteen-chair`): identical, with "juror 2" and `juror-2.md`.

Juror 3 (`data-engineer`): identical, with "juror 3" and `juror-3.md`, plus:

> In this run you run **no script and download nothing.** You read, and you
> write one file.

## The body

Sent verbatim after the preamble, from
`instructions/2026-09-19-0640-juror-zero-trade-contracts.md`.
