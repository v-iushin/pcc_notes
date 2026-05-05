# WHILE WITH LISTS AND DICTIONARIES



# MOVING ITEMS FROM ONE LIST TO ANOTHER

unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

#! ch_05/7_...
#! if (empty_list)	False
#! if (list)		True
#! same logic here
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
print()



# REMOVING ALL INSTANCES OF SPECIFIC VALUE

pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)
print()



# FILLING DICTIOANRY WITH INPUT

responses = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    responses[name] = response
    
    repeat = input("Would you like to let another person responsd? (yes / no) ")
    if repeat == "no":
        polling_active = False

print("---Poll Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
print()