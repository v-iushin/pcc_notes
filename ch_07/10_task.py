# TASK

# dungeon crawler
# 
# requirements: 
# 	name, 
# 	class (warrior, mage, rogue)
# each turn: 
# 	explore (random event)
# 	rest (+3 HP, once in 3 turns)
# 	inventory
# 	quit
# random events: 
# 	mosnter fight
# 	treasure
# 	trap
#	nothing
# stats + inventory
# victory: 150+ gold

#! RANDOM module
# 
# random.***
# 
# randint(m, n)			integer (m, ... n)
# randrange(m, n)		integer (m, ... n-1)
# uniform(1.0, 10.0)	float (1.0, ... 10.0)
# 
# list_name
# choice(list_name)				1 item from the list
# choices(list_name, k = n)		n items from the list (reps)
# sample(list_name, k = n)		n items from the list (no reps)
# 
# shuffle(list_name)		modifies the list



user_class = {"warrior": [12, 3, "incoming damage reduced"], "rogue": [10, 2, "random attacks deal DD"], "mage": [8, 4, "first attack deals DD"]}
# "...": [hp, attack, mod]
room = ["monster", "treasure", "trap", "nothing"]
move = ["explore", "rest", "inventory", "quit"]

user = {
    "name": None,
    "class": None,		# class determines hp, attack, mod
    "hp": None,
    "attack": None,
    "mod": None,		# modificator (DD, ...)
    "gold": None,
    "turns_n": None,
    "invent": [],
}

print(
    "\n* DANGEON CRAWLER *"
    "\n\n Available classes:"
    "\n\t 1. warrior - 12 hp, 3 attack"#, melee attacks"
    "\n\t\t incoming damage reduced"
    "\n\t 2. rogue - 10 hp, 2 attack"#, melee attacks"
    "\n\t\t 50% chance to deal double damage (DD)"
    "\n\t 3. mage - 8 hp, 4 attack"#, ranged attacks"
    "\n\t\t first attack deals double damage (DD)"
    "\n (write 'quit' at any time to finish)\n"
)


game = True
while game:
    # Name
    mes = input("Name: ")
    if mes.lower() == "quit":
        break
    else:
        user["name"] = mes
    
    # Class
    u_c = False
    while not u_c:
        mes = input("Class: ")
        if mes.lower() == "quit":
            break
        elif mes.lower() in user_class:
            user["class"] = mes
            user["hp"] = user_class[mes.lower()][0]
            user["attack"] = user_class[mes.lower()][1]
            user["mod"] = user_class[mes.lower()][2]
            u_c = True
        else:
            print("Wrong class, try again.")
    
    # Quit
    if mes.lower() == "quit":
        #print("last")
        break
    
    # Info confirmation
    print(
        f"\nYour name: {user["name"]}"
        f"\nYour class: {user["class"].upper()}"
        f"\nYour hp: {user["hp"]}"
        f"\nYour attack: {user["attack"]}"
        f"\nYour modificator: {user["mod"]}"
	)
    
    # Game INFO
    print(
        "\n INFO"
        "\n Each turn you are able to:"
        "\n\t explore (encounter random event)"
        "\n\t\t monster fight"
        "\n\t\t treasure"
        "\n\t\t trap"
        "\n\t\t nothing"
        "\n\t rest (restore 3 hp, not higher than initial hp)"
        "\n\t open inventory and use item"
        "\n (write 'quit' at any time to finish)\n"
	)
    
    
    
    game = False
print("END")

# each turn: 
# 	explore (random event)
# 	rest (+3 HP, once in 3 turns)
# 	inventory
# 	quit
# random events: 
# 	mosnter fight
# 	treasure
# 	trap
#	nothing