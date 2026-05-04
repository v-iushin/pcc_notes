people = [
    {"name": "Ada",     "age": 31, "city": "Berlin",    "job": "engineer"},
    {"name": "Bruno",   "age": 25, "city": "Warsaw",    "job": "teacher"},
    {"name": "Cara",    "age": 31, "city": "Berlin",    "job": "designer"},
    {"name": "Dmitri",  "age": 25, "city": "Berlin",    "job": "engineer"},
    {"name": "Eva",     "age": 40, "city": "Warsaw",    "job": "engineer"},
    {"name": "Fatima",  "age": 35, "city": "Lisbon",    "job": "teacher"},
    {"name": "Georg",   "age": 25, "city": "Lisbon",    "job": "designer"},
    {"name": "Hana",    "age": 40, "city": "Berlin",    "job": "teacher"},
    {"name": "Ivan",    "age": 35, "city": "Warsaw",    "job": "designer"},
    {"name": "Julia",   "age": 40, "city": "Lisbon",    "job": "engineer"},
]
'''
# 1
#
# city_roster = {
# 	"city_1": [name_1, name_2, ...],
#	"city_2": [name_3, name_4, ...],
#	...
# }
# name sorted alphabetically
#!
#? 1. list of unique towns
#? 2. list of names for each town
#? 3. combine in dictionary

city_roster = {}

cities = []
for p in people:
    #print(p["city"])
    cities.append(p["city"])
#print(cities)
cities = list(set(cities))
#print(cities)

#! cities = set(p["city"] for p in people)

for c in cities:
    names = []
    for p in people:
        if c == p["city"]:
            names.append(p["name"])
    city_roster[c] = sorted(names)
#print(city_roster)

for city, names_ in city_roster.items():
    print(f"In {city}:")
    for name in names_:
        print(f"\t{name}")
"""
city_roster = {}
for p in people:
    city_roster.setdefault(p["city"], []).append(p["name"])
    print(city_roster)
for city in city_roster:
    city_roster[city].sort()
"""
'''



'''
# 2
#
# job_counter = {
# 	"city_1": {"job_1": n_1, "job_2": n_2, ...}
#	"city_2": {"job_3": n_3, "job_4": n_4, ...}
#	...
# }
#!
#? 1. list of unique towns
#? 2. list of unique jobs
#? 3. ...

job_counter = {}

cities = set(p["city"] for p in people)
#print(cities)

jobs = set(p["job"] for p in people)
#print(jobs)

for c in cities:
    job_number = {}
    for j in jobs:
        n = 0
        for p in people:
            if p["city"] == c and p["job"] == j: 
                n = n + 1
        if n > 0:
            job_number[j] = n
    job_counter[c] = job_number
#print(job_counter)

for city, j_n in job_counter.items():
    print(f"In {city}:")
    for j, n in j_n.items():
        if n == 1:
            print(f"\t{n} {j}")
        else:
            print(f"\t{n} {j}s")
"""
job_counter = {}
for p in people:
    job_counter.setdefault(p["city"], {}).setdefault(p["job"], 0)
    job_counter[p["city"]][p["job"]] += 1
"""
'''



'''
# 3
#
# aver_age = {
# 	"job_1": aver_age_1,
# 	"job_2": aver_age_2,
#	...
# }
# rounded to 1 decimal
#!
#? 1. list of unique jobs
#? 2. ...

aver_age = {}

jobs = set(p["job"] for p in people)
#print(jobs)

for j in jobs:
    age = 0
    n = 0
    for p in people:
        if j == p["job"]:
            age = age + p["age"]
            n = n + 1
    a_age = age / n
    aver_age[j] = round(a_age, 1)
#print(aver_age)

for job, a in aver_age.items():
    print(f"Aver age for {job} is {a}")
"""
totals = {}  # {"engineer": [sum_of_ages, count]}
for p in people:
    job = p["job"]
    totals.setdefault(job, [0, 0])
    totals[job][0] += p["age"]
    totals[job][1] += 1

aver_age = {}
for job, (total, count) in totals.items():
    aver_age[job] = round(total / count, 1)
"""
'''



# 4
#
# cities with NO TWO PEOPLE share same job
#!
#? 1. unique cities and jobs
#? 2. ...
'''
jobs = set(p["job"] for p in people)
cities_1 = list(set(p["city"] for p in people))
#print(jobs, cities_1)

cities = cities_1[:]

c_r = {}

for c in cities_1:
    for j in jobs:
        n = 0
        for p in people:
            if p["city"] == c and p["job"] == j: 
                n = n + 1
            if n == 2:
                c_r[c] = "r"
                break
    if c_r.get(c) == "r":
        cities.remove(c) 

#print(c_r)

print("Cities where no two people share the same job:")
for c in cities:
    print(f"\t{c}")
"""
for c in cities_1:
    remove = False
    for j in jobs:
        ...
        if n == 2:
            remove = True
            break
    if remove:
        cities.remove(c)
"""
"""
oddball_cities = []
for city, job_counts in job_counter.items():
    if all(count == 1 for count in job_counts.values()):
        oddball_cities.append(city)
"""
'''





# 5
#
# elite = {
# 	"city_1": {"oldest": name_1, "jobs": [job_1, job_2, ...]}
# 	"city_2": {"oldest": name_2, "jobs": [job_3, job_4, ...]}
# 	...
# }
# OLDEST, if tie, then alphabetically last
# JOBS, sorted list of unique jobs
#!
#

elite = {}

cities = set(p["city"] for p in people)

for c in cities:
    elite[c] = {}
    jobs = []
    for p in people:
        if c == p["city"]:
            jobs.append(p["job"])
    elite[c]["jobs"] = sorted(set(jobs))
    #print(elite[c])

for c in cities:
    oldest = None
    age = -1
    for p in people:
        if c == p["city"]:
            if p["age"] > age:
                oldest = p["name"]
                age = p["age"]
            elif p["age"] == age:
                if p["name"] > oldest:
                    oldest = p["name"]
                    age = p["age"]
    elite[c]["oldest"] = oldest
    #print(elite[c])

#print(elite)

for c, val in elite.items():
    print(f"In {c}:")
    print(f"\t Jobs: {', '.join(val['jobs'])}")
    print(f"\t Oldest: {val['oldest']}")
