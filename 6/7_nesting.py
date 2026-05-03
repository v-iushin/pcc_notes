# NESTING



# LIST OF DICTIONARIES

"""
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
print()
"""
aliens = []
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10

for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")
print()



# LIST IN DICTIONARY

pizza = {
    "crust": "thick",
    "toppings": ["mashroom", "extra cheese"],
}
print(f"You ordered a {pizza["crust"]}-crust pizza "
      "wtih the following toppings:")
for topping in pizza["toppings"]:
    print(f"\t{topping}")
print()

favorite_lanuages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
}
for name, languages in favorite_lanuages.items():
    if len(languages) == 1:
        print(f"{name.title()}'s favorite language is: \n\t{languages[0].title()}")
    else: 
        print(f"{name.title()}'s favorite lanuages are: ")
        for lanuage in languages: 
            print(f"\t{lanuage.title()}")
print()



# DICTIONARY IN DICTIONARY

users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
	},
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
	},
}
for username, user_info in users.items():
    print(f"Username: {username}")
    full_name = f"{user_info["first"]} {user_info["last"]}"
    location = user_info["location"]
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    print()

