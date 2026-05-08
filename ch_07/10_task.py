# TASK

# DUNGEON CRAWLER



#! RANDOM module
# 
# random.***
# 
# randint(m, n)			integer (m, ... n)
# randrange(m, n)		integer (m, ... n-1)
# uniform(1.0, 10.0)	float (1.0, ... 10.0)
# 
# for list list_name
# choice(list_name)				1 item from the list
# choices(list_name, k = n)		n items from the list (reps)
# sample(list_name, k = n)		n items from the list (no reps)
# 
# shuffle(list_name)		modifies the list



import random

user_class = {"warrior": [12, 3, "incoming damage reduced"], "rogue": [10, 2, "50% chance to deal DD"], "mage": [8, 4, "first attack deals DD"]}
# "...": [hp, attack, mod]
rooms = ["monster", "treasure", "trap", "nothing"]
turns = ["explore", "rest", "inventory"]
items = ["add hp", "hp", "hp", "", "", ""]

user = {
    "name": None,
    "class": None,		# class determines hp, attack, mod
    "hp": None,
    "attack": None,
    "mod": None,		# modificator (DD, ...)
    "gold": None,
    "turns_n": None,
    "moves_n": None,
    "inventory": None,
}

print(
    "\n* DUNGEON CRAWLER *"
    "\n\n Available classes:"
    "\n\t 1. warrior - 12 hp, 3 attack"#, melee attacks"
    "\n\t\t incoming damage reduced"
    "\n\t 2. rogue - 10 hp, 2 attack"#, melee attacks"
    "\n\t\t 50% chance to deal double damage (DD)"
    "\n\t 3. mage - 8 hp, 4 attack"#, ranged attacks"
    "\n\t\t first attack deals double damage (DD)"
    "\n (write 'quit' at any time to finish)\n"
)


main = True
while main:
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
            user["class"] = mes.lower()
            user["hp"] = user_class[mes.lower()][0]
            max_hp = user["hp"]
            user["attack"] = user_class[mes.lower()][1]
            attack = user["attack"]
            user["mod"] = user_class[mes.lower()][2]
            user["gold"] = 0
            user["turns_n"] = 0
            user["moves_n"] = 0
            user["inventory"] = []
            u_c = True
        else:
            print(" Wrong class, try again")
    
    # Quit (class)
    if mes.lower() == "quit":
        break
    
    # Info confirmation
    print(
        f"\n Your name: {user["name"]}"
        f"\n Your class: {user["class"].upper()}"
        f"\n Your hp: {user["hp"]}"
        f"\n Your attack: {user["attack"]}"
        f"\n Your modificator: {user["mod"]}"
	)
    mes = input("\n (press any button to continue) ")
    if mes.lower() == "quit":
        break
    
    # Game INFO
    print(
        "\n* INFO *"
        "\n Make 10+ moves and collect 150+ gold to WIN"
        "\n Each turn you are able to:"
        "\n\t explore - move and encounter random event:"
        "\n\t\t monster fight (+item, +gold, -hp)"
        "\n\t\t treasure (+gold)"
        "\n\t\t trap (-hp)"
        "\n\t\t nothing"
        "\n\t rest - restore 3 hp, once in 3 moves"
        "\n\t\t (not more than initial hp)"
        "\n\t inventory - open inventory and use item"
        "\n\t\t 'add hp': restores full hp, +3 to max hp"
        "\n\t\t 'hp': restores full hp"
        "\n (write 'quit' at any time to finish)"
	)
    
    # Game
    rest = 0
    game = True
    while game:
        mes = input("\nMake your turn: ")
        if mes.lower() == "quit":
            break
        elif mes.lower() in turns:
            user["turns_n"] += 1
            if mes.lower() == "explore":
                user["moves_n"] += 1
                rest += 1
                ran = random.choice(rooms)
                if ran == "monster":            # done
                    print("MONSTER")
                    mon_hp = random.randint(4, 6)
                    mon_at = random.randint(2, 4)
                    if user["class"] == "warrior":
                        mon_at -= 1
                    mage_n = 1
                    while True:
                        print("Monster stats:")
                        print(f" hp: {mon_hp}, at: {mon_at}")
                        if user["class"] == "mage":
                            if mage_n == 1:
                                user["attack"] *= 2
                                mage_n = 0
                        if user["class"] == "rogue":
                            user["attack"] *= random.randint(1, 2)
                        print("Your stats:")
                        print(f" hp: {user["hp"]}, at: {user["attack"]}")
                        print("Monster deals damage")
                        user["hp"] -= mon_at
                        print(f"Your current hp: {user["hp"]}")
                        if user["hp"] <= 0:
                            break
                        print("You deal damage")
                        mon_hp -= user["attack"]
                        print(f"Monster's current hp: {mon_hp}")
                        user["attack"] = attack
                        if mon_hp <= 0:
                            item = random.choice(items)
                            if item == "":
                                print("You don't get any item")
                            else:
                                print(f"New item: {item}")
                                user["inventory"].append(item)
                            gold = random.randint(25, 50)
                            print(f"Gold: +{gold}")
                            user["gold"] += gold
                            break
                        #if user["hp"] <= 0:
                        #    break
                elif ran == "treasure":     # done
                    print("MY PRECIOUS")
                    gold = random.randint(25, 50)
                    print(f"Gold: +{gold}")
                    user["gold"] += gold
                elif ran == "trap":         # done
                    print("IT'S A TRAP")
                    damage = random.randint(1, 2)
                    if user["class"] == "warrior":
                        damage -= 1
                    print(f"Damage: -{damage}")
                    user["hp"] -= damage
                else:
                    print("Here is nothing")
            elif mes.lower() == "rest":     # done
                if rest >= 3:
                    print("You are resting, AND")
                    print("your hp restored")
                    user["hp"] += 3
                    if user["hp"] > max_hp:
                        user["hp"] = max_hp
                    rest = 0
                else:
                    print("You are resting, BUT")
                    print("you can restore hp only once in 3 moves")
            else:                           # done
                if user["inventory"]:
                    print(user["inventory"])
                    while True:
                        print(" Choose the item, write its name")
                        print(" If you don't want anything, write '0'")
                        mes = input("Item: ")
                        if mes.lower() == "quit":
                            break
                        elif mes.lower() == "hp":
                            user["hp"] = max_hp
                            user["inventory"].remove("hp")
                            break
                        elif mes.lower() == "add hp":
                            max_hp += 3
                            user["hp"] = max_hp
                            user["inventory"].remove("add hp")
                            break
                        elif mes.lower() == '0':
                            break
                        else:
                            print(" Wrong input, try again")
                else:
                    print("Your inventory is empty")
                if mes.lower() == "quit":
                    break
            if user["hp"] > 0:
                print(" TURN DONE")
                print(f"hp: {user["hp"]}, attack: {user["attack"]}")
                #print(f"Turns: {user["turns_n"]}")
                print(f"Moves: {user["moves_n"]}")
                print(f"Gold: {user["gold"]}")
                print(f"Inventory: {user["inventory"]}")
            else:
                print("You are DEAD")
        else:
            print(" Wrong turn, try again")
        
        if user["hp"] <= 0:
            game = False
        elif user["gold"] >= 150 and user["moves_n"] >= 10:
            print("WINNER")
            game = False
    # End
    main = False
print("END")
print()