#users_old = ["John", "Sam"]
#print(users_old)

#users1 = users_old[:]
#print(users1)
#for i in range(0,len(users1)):
#    users1[i] = users1[i].lower()
#print(users1)

#users2 = [name.lower() for name in users_old]
#print(users2)

#! only if-elif-else chains

user = input("Username: ")
clea = int(input("Clearance: "))
time = int(input("Hours: "))

#not_work_time = [0, 1, 2, 3, 4, 5, 6, 7,
#                 19, 20, 21, 22, 23]

#if (clea == 1) and (time in not_work_time):
#    print("SECURITY FLAG (1)")

if (clea == 1) and not (8 <= time <= 18):
    print("SECURITY FLAG (1)")

#if (user.lower() == "admin"):
#    print("SECURITY FLAG (admin)")

if ("admin" in user.lower()):
    print("SECURITY FLAG (admin)")

if (user == "root") and (clea == 5):
    print("GRANTED, ADMIN, root user")
elif (time >= 2) and (time <= 4):
    print("MAINTENANCE, time between 2 and 4 ")
elif (clea == 1): 
    print("DENIED, clearance 1")
elif ((clea == 2) or (clea == 3)) and (time >= 8) and (time <= 18):
    print("GRANTED, LIMITED, clearance 2 and 3")
elif ((clea == 4) or (clea == 5)) and (time >= 6) and (time <= 22):
    print("GRANTED, FULL, clearance 4 and 5")
else:
    print("DENIED, wrong time")
