# MATPLOTLIB

import matplotlib.pyplot as plt

#! x_values_1 = [1, 2, 3, 4, 5]
#! y_values_1 = [1, 4, 9, 16, 25]
#! line = [1, 2, 3, 4, 5]
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# Styles
# >>> import matplotlib.pyplot as plt
# >>> plt.style.available
plt.style.use("seaborn-v0_8-whitegrid")

# subplots() can generate one or more 
# plots in the same figure (fig here)
# fig represents collection of all plots
# ax represent single plot
# plot() plots data and connects it
# scatter() plots individual points
fig, ax = plt.subplots()
# s - size
#! ax.plot(x_values_1, y_values_1, linewidth=3)
#! ax.scatter(x_values_1, y_values_1, s=100)
#! ax.plot(line)
#ax.scatter(x_values, y_values, color="red", s=10)

# RGB color model
# ax.scatter(x_values, y_values, color=(0, 0.8, 0), s=10)

# colormap
# ONLY FOR SCATTER
# c - associates value sequence with color mapping
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Set tick labels style.
# this one tells not to write 1e6
ax.ticklabel_format(style="plain")

# Set the range for each axis.
# [min_x, max_x, min_y, max_y] 
ax.axis([0, 1100, 0, 1_100_000])

# bellow command opens matplotlib viewer
plt.show()

# bellow command save plot to file
# first arg - file name
# second arg - trims extra whitespaces from plot
# plt.savefig("squares_plot.png", bbox_inches="tight")
