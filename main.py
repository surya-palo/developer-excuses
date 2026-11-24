"""Write one funny single-line developer excuse to /output/entry.txt.

Stdlib only, no network, deterministic: the same bytes every run.
"""

import os

ENTRY = "All my tests passed \u2014 unfortunately, production wasn't one of them."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
