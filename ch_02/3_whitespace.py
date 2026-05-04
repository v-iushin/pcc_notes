# WHITESPACES

print("Python")

print("\tPython")	# \t - tab
print("1\n2\n3")	# \n - new line

print("numbers\n\t1\n\t2\n\t3") # tab + new line

# STRIP() -type methods
language = "  python "
print(language)
print(language.rstrip())	# removes spaces on the right
print(language.lstrip())	# removes spaces on the left
print(language.strip())		# removes spaces on the both sides

word = "\tword"
print(word.strip())		
#! STRIP() removes all types of whitespaces 