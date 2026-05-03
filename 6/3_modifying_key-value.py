# MODIFYING VALUES

alien_0 = {"color": "green"}
print(f"The alien is {alien_0["color"]}.")
alien_0["color"] = "yellow"
print(f"The alien is now {alien_0["color"]}.")
print()

alien_0 = {'x_position': 0, "y_position": 25, "speed": "medium"}
print(f"Original x-position: {alien_0["x_position"]}")
# Move the alien to the right
# Determine how far to move the alien
# based on its current speed
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else: x_increment = 3 	# if fast alien
# The new position is the old plus the increment
alien_0['x_position'] = alien_0["x_position"] + x_increment
print(f"New x-position: {alien_0["x_position"]}")
print()



# REMOVING KEY-VALUE PAIRS

# DEL statement
# del name[key]
alien_0 = {"color": "green", "points": 5}
print(alien_0)
del alien_0["points"]
print(alien_0)
print()

# POP() method
#! on my own
# name.pop(key)
alien_0 = {"color": "green", "points": 5}
print(alien_0)
alien_0.pop("points")
print(alien_0)
print()

# CLEAR() method
#! on my own
# name.clear()
# clears whole dictionary
alien_0 = {"color": "green", "points": 5}
print(alien_0)
alien_0.clear()
print(alien_0)
