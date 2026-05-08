# PASSING ARGUMENTS



# POSITIONAL ARGUMENTS

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("hamster", "harry")
describe_pet("dog", "willie")
print()
# need to be careful with order of arguments



# KEYWORD ARGUMENTS

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type="hamster", pet_name="harry")
describe_pet(pet_name="harry", animal_type="hamster")
print()
# no need to worry about order



# DEFAULT VALUES

#! parameters with a default FOLLOWS
#! parameters without a default
#def describe_pet(animal_type = "dog", pet_name):
def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name="willie")
describe_pet("willie")
describe_pet("harry", "hamster")
print()
# no need to worry another argument



# ARGUMENTS ERRORS

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#describe_pet()
# gives error, missing arguments