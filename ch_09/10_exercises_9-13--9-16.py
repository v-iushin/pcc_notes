# 9-13
import random as r
class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        rand = r.randint(1, self.sides)
        return f"({self.sides}-sides) {rand}"
die_6 = Die()
for i in range(1, 11):
    rl = die_6.roll_die()
    print(f"roll {i}: {rl}")
print()
die_10 = Die(10)
for i in range(1, 11):
    rl = die_10.roll_die()
    print(f"roll {i}: {rl}")
print()
die_20 = Die(20)
for i in range(1, 11):
    rl = die_20.roll_die()
    print(f"roll {i}: {rl}")
print()

# 9-14
l_list = [1, 2, 3, 4, 5, 
          6, 7, 8, 9, 10, 
          "a", "b", "c", "d", "e"]
#r.shuffle(l_list)
seq = r.sample(l_list, k=4)
print(f"Winning sequence: {seq}")
print()

# 9-15
my_ticket = [1, 2, 3, 4]
n = 0
for i in range(100):
    while True:
        seq = r.sample(l_list, k=4)
        if set(seq) == set(my_ticket):
            break
        else: 
            n += 1
print(f"Avr (pr-100): {n/100}")
print(f"Avr (th-100): {15*14*13*12/(1*2*3*4)}")
print()

# 9-16
import string as s
sym = s.ascii_letters + s.digits + s.punctuation
passwd = r.choices(sym, k=9)
passwd = "".join(passwd)
print(f"Password: {passwd}")
print()