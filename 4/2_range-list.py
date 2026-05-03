# RANGE() FUNCTION

# generates a series of numbers

for value in range(5):
    print(value)
#! range(n+1) gives output 0 ... n
print()

for value in range(1, 5):
    print(value)
#! range(m, n+1) gives output m ... n
print()



# LIST() FUNCTION

numbers = list(range(1, 6))
print(numbers)
print()

even_numbers = list(range(2, 11, 2))
print(even_numbers)
#! range(m, n+1, h) where h is a step size
print()

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
print()