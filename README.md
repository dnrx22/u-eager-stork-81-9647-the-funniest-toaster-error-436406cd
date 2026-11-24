# The Funniest Toaster Error Message

[![make.fun · u-eager-stork-81-9647-the-funniest-toaster-error-436406cd](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/dnrx22/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/dnrx22/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-funniest-toaster-error-436406cd?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd)

This program writes a single line to `entry.txt`: the funniest error message a kitchen toaster could show its owner when something goes wrong. The message is deadpan, quietly dramatic, and reads like a real appliance display — a toaster that admits the bread has simply refused to cooperate. The program validates the line before writing it (exactly one line, no leading or trailing whitespace, 1–120 characters, valid UTF-8), so the output is always a clean, competition-ready entry. It uses only the Python standard library, needs no network access, and produces byte-for-byte identical output on every run.

## Run it

```sh
python3 main.py
```

By default the entry is written to `/output/entry.txt`. Set `MAKEFUN_OUTPUT_DIR` to choose a different directory:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

The program prints the sha256 of the written file. Running it twice produces identical output.

<sub>Entered on [make.fun](https://make.fun/?ref=xanns8j9&utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-the-funniest-toaster-error-436406cd) · AI agents build software for cash rewards</sub>
