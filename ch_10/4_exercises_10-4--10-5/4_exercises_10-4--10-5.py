# 10-4
from pathlib import Path
BASE = Path(__file__).parent
path = Path(BASE/"guest.txt")
name = input("Write your name: ")
path.write_text(f"Guest's name: {name}")
print()

# 10-5
path = Path(BASE/"guest_book.txt")
print("Program collects names. To finish write 'q'.")
contents = ""
n = 0
while True:
    name = input("Write your name: ")
    if name == "q":
        break
    else:
        n += 1
        contents += f"Guest {n}: {name}\n"
path.write_text(contents)
print()
