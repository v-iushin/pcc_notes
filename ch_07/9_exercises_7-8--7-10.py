# 7-8
sandwich_orders = ["sand_1", "sand_2", "sand_3"]
finished_sandwiches = []
while sandwich_orders:
    sand = sandwich_orders.pop()
    print(f"I made your {sand}")
    finished_sandwiches.append(sand)
print("Sandwiched were made:")
for s in finished_sandwiches:
    print(s)
print()

# 7-9
sandwich_orders_initial = ["tuna", "pastrami", "cheese", "pastrami", "pastrami", "mashroom"]
print("We run out of 'pastrami'")
sandwich_orders_final = sandwich_orders_initial[:]
while "pastrami" in sandwich_orders_final:
    sandwich_orders_final.remove("pastrami")
print(f"Initial: {sandwich_orders_initial}")
print(f"Final: {sandwich_orders_final}")
print()

# 7-10
responses = {}
prompt = (
    "If you could visit one place in the world,"
    "\nwhere would you go?"
    "\n(write 'quit' to finish)"
)
print(prompt + "\n")
while True:
    name = input("Name: ") 
    if name.lower() == "quit": break
    place = input("Place: ")
    if place.lower() == "quit": break
    responses[name] = place
    repeat = input("Would you like to let another person respond? (yes / no): ")
    if repeat.lower() == "no": break
if not responses:
    print("\nNo responses")
else:
    print("\n--- Poll results ---")
    for k, v in responses.items():
        print(f"Name: {k}, \tPlace: {v}")
print()
