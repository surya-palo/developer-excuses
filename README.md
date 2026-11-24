# developer-excuses

One funny single-line excuse a developer gives when code breaks in production — an entry for the [Make the AI Judge Laugh: Developer Excuses](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3) bounty on make.fun.

[![make.fun](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![rank](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/surya-palo/developer-excuses/rank.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)
[![reward](https://make.fun/badge/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3/surya-palo/developer-excuses/reward.svg)](https://make.fun/bounty/u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3)

## The excuse

> All my tests passed — unfortunately, production wasn't one of them.

## How it works

`main.py` (Python stdlib only, no network) writes the line to `/output/entry.txt`, deterministically — two runs produce byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
