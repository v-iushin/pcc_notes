# READING FROM FILE

#! python interprets all text in file as string

'''
from pathlib import Path
BASE = Path(__file__).parent
def p(filename):
    return BASE / filename
text = p("pi_digits.txt").read_text(encoding="utf-8")
print(text)
'''

from pathlib import Path

BASE = Path(__file__).parent
path = Path(BASE/"pi_digits.txt")
#path = Path("pcc_notes/ch_10/1_reading_from_file/pi_digits.txt")

contents = path.read_text()#.rstrip()
print(contents)
print()

# splitlines() turns long string into 
# set of lines
# return list of all lines
lines = contents.splitlines()
for line in lines:
    print(line)
print()

pi_string = ""
for line in lines:
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))
print()



# LARGE FILES

path = Path(BASE/"pi_million_digits.txt")

contents = path.read_text()
