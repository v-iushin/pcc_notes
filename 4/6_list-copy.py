# LIST COPY

my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
#! need to use slice

my_foods.append("cannoli")
friend_foods.append("ice cream")

print(f"My faforite foods are {my_foods}")
print(f"My friend's favorite foods are {friend_foods}")

#! if we wrote friend_foods = my_foods
#! then we would simply make a new variable
#! that points on the same list

for value in my_foods:
    print(value)