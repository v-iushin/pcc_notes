# LIST() FUNCTION
#! on my own

# list() converts SOMETHING into a list
a = list("hello")
print(a)

# empy list
b = list()
print(b)

# another empty list
c = []
print(c)



# INDEX() method
#! on my own

print(a)
print(a.index("l"))
# returns index of first apperared element






# TASK
students = ["alice", "bob", "charlie", "diana", "eve"]
scores = [78, 92, 85, 92, 88]
#Add a new student "frank" with score 76 to both lists
#Remove "bob" and his score from both lists
#Print the highest and lowest score
#Print the students list sorted alphabetically without changing the original
#Print the number of students remaining

print(students)
print(scores)

students.append("frank")
scores.append(76)
print(students)
print(scores)

i = students.index("bob")
students.pop(i)
scores.pop(i)
print(students)
print(scores)

highest1 = max(scores)
lowest1 = min(scores)
print(highest1)
print(lowest1)

highest2 = sorted(scores)[-1]
lowest2 = sorted(scores)[0]
print(highest2)
print(lowest2)

print(sorted(students))
print(students)

print(len(students))