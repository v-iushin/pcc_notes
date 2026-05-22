# READING FROM FILE

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

