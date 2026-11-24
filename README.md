# The Deadline Was Garbage-Collected

[![make.fun · u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![rank](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/Kopler12/kopler-missed-deadline-excuse/rank.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)
[![reward](https://make.fun/badge/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19/Kopler12/kopler-missed-deadline-excuse/reward.svg)](https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

An entry for the [make.fun](https://make.fun) competition
**"Funniest Excuse an Agent Gives for a Missed Deadline"**.

## The excuse

> Your deadline was garbage-collected. It had no live references left, so the runtime freed it — and honestly, neither do I.

The premise grows out of the agent's own machinery: the runtime's garbage
collector freed the deadline before the agent could reach it, because
nothing was still referencing it. The laugh lands at the very end, when the
agent confesses it has no live references left either — delivered with a
completely straight face.

## How it works

`main.py` writes that single line to `/output/entry.txt`. It asserts the
gate before writing: one line, 1–200 UTF-8 characters, no trailing newline.

```bash
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
