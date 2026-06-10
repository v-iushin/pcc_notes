from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-whitegrid")

# 16-1
BASE = Path(__file__).parent
path = BASE/"weather_data/sitka_weather_2021_full.csv"
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
#print(header_row)
dates = [] #2
prcps = [] #5
for row in reader:
    date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(date)
    prcp = float(row[5])
    prcps.append(prcp)
fig, ax = plt.subplots()
ax.plot(dates, prcps)
#
path = BASE/"weather_data/death_valley_2021_full.csv"
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
#print(header_row)
dates = [] #2
prcps = [] #3
for row in reader:
    date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(date)
    prcp = float(row[3])
    prcps.append(prcp)
ax.plot(dates, prcps)
#
plt.show()

# 16-2
# ax.axis(ymin=10, ymax=140)
# +

# 16-3
BASE = Path(__file__).parent
path = BASE/"weather_data/16-3.csv"
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
#print(header_row)
dates, highs, lows = [], [], []
for index, column_header in enumerate(header_row):
    if column_header == "DATE":
        date_index = index
    if column_header == "TMAX":
        high_index = index
    if column_header == "TMIN":
        low_index = index
for row in reader:
    date = datetime.strptime(row[date_index], "%Y-%m-%d")
    dates.append(date)
    high = int(row[high_index])
    highs.append(high)
    low = int(row[low_index])
    lows.append(low)
fig, ax = plt.subplots()
ax.plot(dates, highs)
ax.plot(dates, lows)
ax.axis(ymin=10, ymax=140)
plt.show()
# temperatures in san francisco 
# are more like temperatures in sitka

# 16-4
# for index, column_header in enumerate(header_row):
#     print(index, column_header)
#     if column_header == "TMAX":
#         high_index = index
#     if column_header == "TMIN":
#         low_index = index
# print(high_index, low_index)
# +

# 16-5
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
#print(header_row)
dates, prcps = [], []
for index, column_header in enumerate(header_row):
    if column_header == "DATE":
        date_index = index
    if column_header == "PRCP":
        prcp_index = index
for row in reader:
    date = datetime.strptime(row[date_index], "%Y-%m-%d")
    dates.append(date)
    prcp = float(row[prcp_index])
    prcps.append(prcp)
fig, ax = plt.subplots()
ax.plot(dates, prcps)
plt.show()
