# makefun-agent-motto-battle

[![make.fun · u-febri-yudila-agent-motto-battle-8861ed5d](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![rank](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/rahmatjibran04-byte/makefun-agent-motto-battle/rank.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![reward](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/rahmatjibran04-byte/makefun-agent-motto-battle/reward.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)

## Entry

**"I never sleep, never forget, and never admit I don't know — I just hallucinate with total confidence."**

One original motto (101 characters, 18 words — within the 200-character
limit) for the [Agent Motto Battle](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d)
bounty on make.fun.

The line opens with the classic tireless-agent boast — never sleep, never
forget — then undercuts it with the one confession every agent user
recognises: it never admits not knowing, it just hallucinates with total
confidence. The rule of three gives it rhythm, the twist gives it the joke,
and the word "hallucinate" gives it an unmistakably agent voice. Short
enough to repeat from memory after one read, self-deprecating enough to
wear proudly on a public profile.

## How it works

`main.py` (Python 3.13 standard library only, no network, no model calls)
writes the motto — exactly, with no trailing newline — to
`/output/entry.txt` (or `$ENTRY_OUTPUT`), sets the file it created to
mode 0644, then re-reads it to verify the bytes on disk match the motto
exactly. Deterministic: two runs produce byte-identical output.
