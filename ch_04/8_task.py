# the number analyzer

#! no sum(), min(), max(), sorted()

import random

numbers = [n*2 for n in range(-10, 11) if n != 0]
#print(numbers)

random.shuffle(numbers)
print(f"Original list: {numbers}")

max_v = numbers[0]
min_v = numbers[0]
sum_v = 0

for i in numbers:
    if max_v < i:
        max_v = i
    if min_v > i:
        min_v = i
    sum_v = sum_v + i

print(f"Max = {max_v}")
print(f"Min = {min_v}")
print(f"Sum = {sum_v}")
av = sum_v / len(numbers)
print(f"Aver = {av}")

positives = []
for n in numbers:
    if n > 0 and n % 2 == 0:
        positives.append(n)
print(f"Positives: {positives}")

l = len(positives)
rev1 = []
for i in range (1, l+1):
    rev1.append(positives[-i])
print(f"Rev1: {rev1}")

rev2 = positives[::-1]
print(f"Rev2: {rev2}")

#rev2 = positives[:]
#rev2.reverse()
#print(f"Rev2: {rev2}")

t = (numbers[0], numbers[1], numbers[2], numbers[3], numbers[4])
#print(t)

# This gives mistake, avoid :)
# t[0] = 0

thirds = numbers[::3]
print(f"Thirds: {thirds}")

m = 0
if len(thirds) != len(rev1):
    print("Different lengths")
else:
    for i in range(0, len(thirds)):
        if thirds[i] == rev1[i]:
            m = m + 1

if m == len(thirds): print("Same")
else: print("Not same")
# they even have different length







    

#numbers1 = [number*2 for number in range(-10,0)]
#for i in range(1,11):
#    numbers1.append(i*2)
#print(numbers1)

#numbers2 = [n*2 for n in range(-10,0)] + [n*2 for n in range(1,11)]
#print(numbers2)
