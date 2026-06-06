# 15-3
from random import choice
class RandomWalk:
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
    def get_step(self):
        """Determine the direction and distance for each step."""
        # using this approach we still can modify 
        # steps for x and y separately
        x_direction = choice([1, -1])
        #!x_distance = choice([0, 1, 2, 3, 4])
        x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        x_step = x_direction * x_distance
        y_direction = choice([1, -1])
        #!y_distance = choice([0, 1, 2, 3, 4])
        y_distance = choice([0, 1, 2, 3, 4, 5, 6])
        y_step = y_direction * y_distance
        return [x_step, y_step]   
    def fill_walk(self):
        """Calculate all points in the walk."""
        while len(self.x_values) < self.num_points:
            [x_step, y_step] = self.get_step()
            if x_step == 0 and y_step == 0:
                continue
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
import matplotlib.pyplot as plt
rw = RandomWalk(5_000)
rw.fill_walk()
plt.style.use("classic")
fig, ax = plt.subplots(figsize=(15,9))
ax.plot(rw.x_values, rw.y_values, linewidth=1)
ax.set_aspect("equal")
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()

# 15-4
# +

# 15-5
# +
