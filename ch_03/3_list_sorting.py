# SORTING THE LIST

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)	



# SORT() method
# changes the order permanently
# cant revert to original order

# store items alphabetically
cars.sort()
print(cars)

# store items reverse-alphabetically
cars.sort(reverse=True)
print(cars)



# SORTED() function
# maintains original order
# only displays sorted
cars = ['bmw', 'audi', 'toyota', 'subaru']

# alphabetically
print(cars)
print(sorted(cars))

# reverse-alphabetically
print(cars)
print(sorted(cars,reverse=True))



# REVERSE() method
# reverses original order
# changes permanently
print(cars)
cars.reverse()
print(cars)



# LEN() function
# length of the list (number of items)
print(len(cars))



#! REVERSED() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(list(reversed(cars)))
#! need to wrap reversed() in list()
#! next file about list()