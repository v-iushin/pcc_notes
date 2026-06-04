import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-whitegrid")

# ---

# 15-1
x_values_5 = [1, 2, 3, 4, 5]
y_values_5 = [1, 8, 27, 64, 125]
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]
fig, ax = plt.subplots()
#! ax.plot(x_values_5, y_values_5, color="red")

# 15-2
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=5)

# ---

plt.show()

