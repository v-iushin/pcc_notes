# MULTIPLE CONDITIONS



# AND
# checking whether two conditions 
# are both true

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)	# False

age_1 = 22
print((age_0 >= 21) and (age_1 >= 21))	# True
# also parantheses can be use, but not necessary
# (...) and (...)
print()



# OR

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)	# True

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)	# False