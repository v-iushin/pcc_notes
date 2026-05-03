# DICTIONARY

# DICTIONARY is a collection of KEY-VALUE pairs
#
# name = {key_1: value_1, key_2: value_2, ...}
#
# VALUE can be: number, string, list, another dictionary
# basically any object can be VALUE

alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

new_points = alien_0["points"]
print(f"You just earned {new_points} points!")
