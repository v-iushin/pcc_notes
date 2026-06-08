from random import randint
from random import choice
import plotly.express as px
import matplotlib.pyplot as plt

class Die:
    """A class representing a single die."""
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

class RandomWalk:
    """A class to generate random walks."""
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):
        """Calculate all points in the walk."""
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            if x_step == 0 and y_step == 0:
                continue
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)



# 15-6
die_1_1 = Die(8)
die_1_2 = Die(8)
results = []
for roll_num in range(200_000):
    result = die_1_1.roll() + die_1_2.roll()
    results.append(result)
frequencies = []
max_result = die_1_1.num_sides + die_1_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
title = "Results (+) of Rolling two D8 200,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()

# 15-7
die_2_1 = Die()
die_2_2 = Die()
die_2_3 = Die()
results = []
for roll_num in range(200_000):
    result = die_2_1.roll() + die_2_2.roll() + die_2_3.roll()
    results.append(result)
frequencies = []
max_result = die_2_1.num_sides + die_2_2.num_sides + die_2_3.num_sides
poss_results = range(3, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
title = "Results (+) of Rolling three D6 200,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()

# 15-8
die_3_1 = Die()
die_3_2 = Die()
results = []
for roll_num in range(200_000):
    result = die_3_1.roll() * die_3_2.roll()
    results.append(result)
frequencies = []
max_result = die_3_1.num_sides * die_3_2.num_sides
poss_results = range(1, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
title = "Results (*) of Rolling two D6 200,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()

# 15-9
die_4_1 = Die()
die_4_2 = Die()
results = []
results = [(die_4_1.roll() * die_4_2.roll()) for roll_num in range(200_000)]
#for roll_num in range(200_000):
#    result = die_4_1.roll() * die_4_2.roll()
#    results.append(result)
frequencies = []
max_result = die_4_1.num_sides * die_4_2.num_sides
poss_results = range(1, max_result + 1)
frequencies = [results.count(value) for value in poss_results]
#max_result = die_4_1.num_sides * die_4_2.num_sides
#poss_results = range(1, max_result + 1)
#for value in poss_results:
#    frequency = results.count(value)
#    frequencies.append(frequency)
title = "Results (*) of Rolling two D6 200,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()



# 15-10

# matplot for dice rolling
die_5_1 = Die()
die_5_2 = Die()
results = []
results = [die_5_1.roll() + die_5_2.roll() for roll_num in range(200_000)]
frequencies = []
max_result = die_5_1.num_sides + die_5_2.num_sides
poss_results = range(2, max_result + 1)
frequencies = [results.count(value) for value in poss_results]
fig, ax = plt.subplots()
ax.bar(poss_results, frequencies)
plt.show()

# ploty for random walk
rw = RandomWalk(50_000)
rw.fill_walk()
fig = px.scatter(x=rw.x_values, y=rw.y_values)
fig.show()
