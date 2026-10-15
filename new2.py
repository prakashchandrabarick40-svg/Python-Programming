import random
import time
import os

width = 70

while True:
    os.system("cls" if os.name == "nt" else "clear")

    for i in range(15):
        position = random.randint(0, width)
        print(" " * position + "⭐")

    print("\n🚀 PYTHON SPACE 🚀")

    time.sleep(0.2)