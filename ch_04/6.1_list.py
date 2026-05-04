# MORE FOR LIST
#! on my own

my_foods = ["pizza", "falafel", "carrot cake"]

for value in my_foods:
    print(value)

print(i for i in my_foods)
# gives GENERATOR... hell knows
# its somehow simillar to list comprehensions
# but instead of [] there are ()
# and its like expression that doesnt make a list
# but makes the rule for the list 
# that you can pass to another function
# like sum(), max(), ...




# OPERATOR *

print(*my_foods)
# unpacking operator
# prints each element from the list without []

print(*my_foods, sep="\n")
# separates elements with new lines



# JOIN() METHOD

words = ["hello", "world", "python"]
print(", ".join(words))
print("\n".join(words))
#! only workds with lists of strings
