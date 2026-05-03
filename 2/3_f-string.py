# F-STRING

# {} are used to insert variable into f-string

first_name = "ada"
last_name = "lovelace"

first_name = first_name.upper()

full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")

message = f"Goodbye, {full_name.title()}!"
print(message)