# 16-9

from pathlib import Path
import csv
import plotly.express as px

BASE = Path(__file__).parent
path = BASE/"eq_data/world_fires_1_day.csv"

lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

lats, lons, brts = [], [], []
for row in reader:
    lats.append(float(row[0]))
    lons.append(float(row[1]))
    brts.append(float(row[2]))

title = "World Fires"
fig = px.scatter_geo(
    lat=lats, lon=lons, title=title,
    color=brts,
    color_continuous_scale="amp",
    labels={"color":"Brightness"},
    projection="natural earth",
)
fig.show()