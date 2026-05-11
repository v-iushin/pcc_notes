# PASSING LIST

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ["hannah", "ty", "margot"]
greet_users(usernames)
print()



# MODIFYING LIST IN FUNCTION

# wihtout functions
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
print("The following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
print()

# with functions
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print()



# PREVENTION FUNCTION FROM MODIFYING LIST

unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print()
print(unprinted_designs)
print()