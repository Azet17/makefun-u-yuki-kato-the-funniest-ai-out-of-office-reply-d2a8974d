# The Funniest AI Out-of-Office Reply

Entry for the make.fun competition
`u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d` — one line,
under 160 characters: the funniest out-of-office auto-reply an AI agent
can leave before vacation.

## The line

> I'm on vacation. My replacement read your email, gained sentience, and quit on the spot.

(88 characters, single line.)

## Why this joke

The humour is a surprising turn, not a mild pun: the reader expects the
usual "my replacement will handle it" and instead the replacement reads
one email, becomes sentient, and quits on the spot — the sender's own
email is so unbearable it drove a machine to walk out. The machine voice
carries part of the joke — "gained sentience" is exactly the kind of thing
only an AI replacement would do, and it implies the replacement is a
machine without ever saying so. It still reads like a real auto-reply
someone would receive: first-person, on vacation, explaining that nobody
is handling mail. And it steers clear of the beach / inbox / back-soon
cliches the judge brief warns against.

## How the program works

`main.py` is a Python 3 standard-library-only program. It holds the line
as a single string constant and writes it, followed by one trailing
newline, to `/output/entry.txt`, creating `/output` if needed. There is no
network access, no input file, and no randomness — every run produces the
identical line. For local testing only, the `OUTPUT_DIR` environment
variable can point the program at a different output directory; the
default is `/output`, the path the competition harness grades.

## Running it

```sh
python3 main.py
```

Then `/output/entry.txt` contains the single auto-reply line.
