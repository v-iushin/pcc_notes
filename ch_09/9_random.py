# RANDOM MODULE

import random as r

# randint(M, N)
# random number between M and N (including)
print(r.randint(1, 6))
print()

# choice(LIST_NAME)
# return random elemnt from LIST_NAME
players = ["charles", "martina", "michael", "florence", "eli"]
first_up = r.choice(players)
print(first_up)
print()
