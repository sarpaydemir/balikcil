#!/usr/bin/env bash
# Balıkçıl · PreToolUse hook on Bash — closes the command-line read hole.
#
# RULES 5 says the settings cannot block file reads from the command line. A hook
# can. This one refuses Bash commands that reach for the old project or for past
# session logs.
#
# NARROW ON PURPOSE, and narrowed once already. The first version matched the
# bare word "freqtrade_hyperopt" anywhere in the command, and it immediately
# blocked a legitimate write: a ledger entry that *mentioned* the old path while
# recording that the memory path had been fixed. Writing about a path is not
# reading it, and LEDGER.md and settings.json legitimately contain that name
# (the move record and the deny list).
#
# So the match now requires the name to look like a real filesystem reference —
# preceded by a slash, which covers /home/user/..., ../..., and ~/... forms.
#
# Residual gap, stated rather than hidden: `cd /home/user && cat
# freqtrade_hyperopt/FILE` would slip through, because the name carries no
# leading slash there. This hook is defence in depth, not the only control. The
# primary ones are the agent definitions forbidding it, the Read() deny rules in
# settings.json, and the fact that only data-engineer has Bash at all.
#
# Anything not matched passes silently (exit 0, no output).

set +e
INPUT=$(cat)

# Pull the command out of the tool input without needing jq.
CMD=$(printf '%s' "$INPUT" | python3 -c '
import json,sys
try:
    d = json.load(sys.stdin)
    print(d.get("tool_input", {}).get("command", ""))
except Exception:
    print("")
' 2>/dev/null)

[ -z "$CMD" ] && exit 0

deny() {
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"%s"}}\n' "$1"
  exit 0
}

case "$CMD" in
  */freqtrade_hyperopt*)
    deny "Balikcil wall (RULES 1): the old project path is closed. Read nothing outside this folder." ;;
  */research_factory*)
    deny "Balikcil wall (RULES 1): the old project path is closed." ;;
  */.claude/projects*)
    deny "Balikcil wall (RULES 1): past session logs are closed. This machine holds the old project's transcripts." ;;
  *read-memories*)
    deny "Balikcil wall (RULES 1): read-memories searches past session logs and is never run in this laboratory." ;;
esac

exit 0
