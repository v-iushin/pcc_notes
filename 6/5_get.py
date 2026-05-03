# GET() METHOD

# name.get(KEY, DEFAULT-value)
# if KEY exists, corresponding VALUE returned
# if KEY doesnt exist, DEFAULT-value returned

alien_0 = {"color": "green", "speed": "slow"}

# print(alien_0["points"])
#! mistake, "points" doesnt exist

point_value = alien_0.get("points", "No point value assigned.")
print(point_value)

point_value = alien_0.get("points")
print(point_value)
#! if there no DEFAULT-value assigned and KEY doesnt exist
#! GET() will return None

