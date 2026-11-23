"""Make the AI Judge Laugh: Office Jokes.

Writes one office joke to /output/entry.txt. Stdlib only, deterministic,
no network.
"""

import os

JOKE = (
    "HR just sent a calendar invite called 'Mandatory Fun.' "
    "Ninety minutes, no agenda, and fourteen people are already "
    "arguing about it in the comments."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"wrote /output/entry.txt ({len(JOKE)} characters)")


if __name__ == "__main__":
    main()
