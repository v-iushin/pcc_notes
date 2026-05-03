# LOOPING THROUGH A DICTIONARY



# LOOP THROUGH KEY-VALUE PAIRS

user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}
for key, value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}")
    print()
# KEY and VALUE are just variables, can be different
# ITEMS() method returns KEY-VALUE pairs
# print(user_0.items())



# LOOP THOUGH KEYS

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}
for name in favorite_languages.keys():
    print(name.title())
print()
# KEYS() method returns KEYs
# print(favorite_languages.keys())
#! LOOP THROUGH KEYS is deafualt loop
#! so it can be done
#! for name in favorite_languages():
friends = ["phil", "sarah"]
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
print()
# dict[KEY] accesses correspoding VALUE
if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")
print()



# LOOP TRHOUGH KEYS IN ORDER

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
print()



# LOOP THROUGH VALUES

print("The following lanuages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
print()
# VALUES() method returns VALUEs

#! SET() is a collection in which 
#! each item must be unique
#! result is nonrepetitive
lanuage = {"python", "rust", "python"}
print(lanuage)
#! also a SET, like DICTIONARY but without
#! KEY-VALUES pairs