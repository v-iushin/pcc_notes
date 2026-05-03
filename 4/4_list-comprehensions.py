# LIST COMPREHENSIONS

squares_1 = []
for value in range(1, 11):
    squares_1.append(value**2)
print(squares_1)
print()
# regular way

squares_2 = [value**2 for value in range(1, 11)]
print(squares_2)
# smart way

#! name = [(j(i)) for (i) in range(m, n+1)]




# exercise 4-7
print()
print()
 
thirds_1 = [i for i in range(3, 31, 3)]
thirds_2 = list(range(3, 31, 3))
print(thirds_1)
print(thirds_2)


for number in thirds_1:
    print(number)
print()
for number in thirds_2:
    print(number)
print()