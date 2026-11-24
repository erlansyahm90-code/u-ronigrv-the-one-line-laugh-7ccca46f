"""make.fun entry for The One-Line Laugh: writes the single-sentence entry
to /output/entry.txt as exact bytes, with no trailing newline."""

import os

ENTRY = "I bought a standing desk, a posture corrector, and a lumbar pillow, and I now slouch in three different expensive ways."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
