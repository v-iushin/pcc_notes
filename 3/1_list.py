# LIST 1
# GENERAL THINGS

# list: NAME[e1, e2, e3, ...]
#! empty list: NAME[]

bicycle = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycle)
# printning whole list

print(bicycle[0])	# printing 1st element

# [0] - 1st, [1] - 2nd, ..., [n] - (n+1)th

#! [-1] - last, [-2] - second last, ...
print(bicycle[-1])

print(bicycle[-(-3)])
print(bicycle[3])
# logic: -(-) = +

# element from the list = variable
print(f"{bicycle[0]}")