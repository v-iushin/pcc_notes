# FOR -LOOP

# (for is statement)

magicians = ['alice', 'david', 'carolina']

# for item in list of items: 
#   ...(item)

#! colon (:) is IMPORTANT
#! item - is NOT TEMPORARY variable and can be used later
#! indent (отступ) is important
#! DO NOT indent unnecessary lines

for magician in magicians:
    print(magician)

print()

for magician in magicians:
 print(f"{magician.title()}, that was good!")
 print(f"Do more, {magician.title()}!")

 print("Thank you! \n")
print("Thank you, everyone! \n")

print(f"{magician}")
# any indents can be used
# indents within one for-loop should be same
# empty lines within for-loop are ignored

