import time
import os

dragon = [
    "           / \\__",
    "          (    @\\___",
    "          /         O",
    "         /   (_____/",
    "        /_____/   U",
]

position = 0
direction = 1

while True:
    os.system("cls" if os.name == "nt" else "clear")

    for line in dragon:
        print(" " * position + line)

    position += direction

    if position >= 45:
        direction = -1

    if position <= 0:
        direction = 1

    time.sleep(0.08)