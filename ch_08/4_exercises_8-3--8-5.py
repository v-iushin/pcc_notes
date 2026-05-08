# 8-3
def make_shirt(size, text):
    print(f"Shirt in size {size} with text '{text}'.")
make_shirt("M", "hello")
make_shirt(text="hello", size="M")
print()

# 8-4
def make_shirt(size="L", text="I love Python"):
    print(f"Shirt in size {size} with text '{text}'.")
make_shirt()
make_shirt("M")
make_shirt("S", "message")
print()

# 8-5
def describe_city(city, country="Australia"):
    print(f"{city.title()} is in {country.title()}")
describe_city("melbourne")
describe_city("sydney")
describe_city("auckland", "new zealand")
print()
