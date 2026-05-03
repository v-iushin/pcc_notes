# TUPLE

# tuple is immutable (неизменяемый) list
# tuple defines as list but uses this ()
# instead of []

dimensions = (200, 50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])

#! dimensions[0] = 250
#! will give a mistake

# tuple with one element still should include comma
my_t = (3,)
print(my_t)

# loop for tuple same as for list
for dimension in dimensions:
    print(dimension)
print()

# writing over a tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
print()
dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)
# new value to variable with the same name
# can be assigned
