# LIST 2
# MODIFYING, ADDING AND REMOVING ELEMENTS

motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)



# MODIFYING

motorcycle[0] = 'ducati'
print(motorcycle)



# ADDING

# APPEND() is adding to the end of the list
motorcycle.append('honda')
print(motorcycle)

# INSERT() is adding to exact spot by specifying index
motorcycle.insert(0, 'NEW')
print(motorcycle)



# REMOVING

# DEL statement
# cant access after removing
del motorcycle[0]
print(motorcycle)
#! IF KNOW THE INDEX OF ITEM TO DELETE

# POP() method
# removes INDEXED element and gives that element to output
# POP() = POP(-1) - by defaul empty brackets is last element
popped_motorcycle = motorcycle.pop()
# simultaneosuly stores element into new variable and deletes from the list
print(motorcycle)
print(popped_motorcycle)

# REMOVE() method
# in case of knowing value but not knowing index of element
motorcycle.remove('ducati')
print(motorcycle)
# removing only from the list
motorcycle = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycle)
too_expesive = 'ducati'
motorcycle.remove(too_expesive)
print(motorcycle)
print(f"A {too_expesive.title()} is too expensive")

#! REMOVE() deletes only first occurrence of the value
print(motorcycle)
motorcycle.insert(0, 'New')
motorcycle.insert(0, 'New')
print(motorcycle)
motorcycle.remove('New')
print(motorcycle)



# CLEAR() method
#! on my own
#clears whole list
print()
print(motorcycle)
motorcycle.clear()
print(motorcycle)
# emtpy list