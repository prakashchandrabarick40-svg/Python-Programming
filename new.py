import time

name = input("Enter your name: ")

print("\n✨✨✨ Welcome ✨✨✨")
time.sleep(0.5)

for i in range(3):
    print("🚀 Loading" + "." * (i + 1))
    time.sleep(0.7)

print("\n" + "=" * 35)
print(f"🎉 Hello, {name}! 🎉")
print("💻 Welcome to Python Programming")
print("🔥 Keep Coding, Keep Learning!")
print("=" * 35)