# FUNCTION TEST

# PYTEST

# to update
# python -m pip install --upgrade pip
# python -m pip install --upgrade package_name

# to install
# python -m pip install --user pytest
# python -m pip install --user package_name

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == "q":
        break
    last = input("Please give me a last name: ")
    if last == "q":
        break
    
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")

