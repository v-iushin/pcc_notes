# ERROR CHECKING

from pathlib import Path
import csv

from datetime import datetime

import matplotlib.pyplot as plt

BASE = Path(__file__).parent
path = BASE/"weather_data/death_valley_2021_simple.csv"
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
for index, column_header in enumerate(header_row):
    print(index, column_header)
    if column_header == "TMAX":
        high_index = index
    if column_header == "TMIN":
        low_index = index
print(high_index, low_index)

# Extract dates, and high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = int(row[high_index])
        low = int(row[low_index])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots()
# alpha argument controls transparency
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# Format plot.
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

ax.axis(ymin=10, ymax=140)

plt.show()