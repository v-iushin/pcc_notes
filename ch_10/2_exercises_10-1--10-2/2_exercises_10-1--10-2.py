# 10-1
from pathlib import Path
BASE = Path(__file__).parent
path = (BASE/"learning_python.txt")
contents = path.read_text()
print(contents)
print()
#lines = contents.splitlines()
for line in contents.splitlines():
    print(line)
print()

# 10-2
for line in contents.splitlines():
    line = line.replace("0", "")
    line = line.replace("Python", "C")
    print(line)
print()
