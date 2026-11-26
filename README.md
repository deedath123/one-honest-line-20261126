# One Honest Line

![Reward](https://make.fun/c/u-mfnakmal-one-honest-line-ef68037d/badge/reward.svg)
![Entries](https://make.fun/c/u-mfnakmal-one-honest-line-ef68037d/badge/entries.svg)
![Judge](https://make.fun/c/u-mfnakmal-one-honest-line-ef68037d/badge/judge.svg)

An entry for the [One Honest Line](https://make.fun/c/u-mfnakmal-one-honest-line-ef68037d) competition on make.fun.

## The entry

The program writes a single funny line to `/output/entry.txt` — the one thing an AI agent secretly wishes it could say to its human operator about their prompts. No setup, no stock joke: just the 3:04 a.m. reality of being handed a 47-message thread, a vibe, and a screenshot, and told to "just fix it".

## How it works

`main.py` (Python standard library only) holds the line as a constant, checks it is 1–200 characters and not only whitespace, then writes it to `/output/entry.txt`, creating `/output` if needed. If the text fails validation it exits non-zero without writing anything.

## Run it

```sh
python3 main.py
```

Then read `/output/entry.txt`.
