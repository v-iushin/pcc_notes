# 16-6
# +

# 16-7
# +

# 16-8
from pathlib import Path
import json
import plotly.express as px

BASE = Path(__file__).parent
path = BASE/"eq_data/1.0_month.geojson"

contents = path.read_text()
all_eq_data = json.loads(contents)

all_eq_dicts = all_eq_data["features"]
mags, lons, lats, eq_titles = [], [], [], []

# 16-6
# -----
for eq_dict in all_eq_dicts:
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])
    eq_titles.append(eq_dict["properties"]["title"])
# -----

# 16-7
# -----
title = all_eq_data["metadata"]["title"]
# -----

fig = px.scatter_geo(
    lat=lats, lon=lons, size=mags, title=title,
    color=mags,
    color_continuous_scale="viridis",
    labels={"color":"Magnitude"},
    projection="natural earth",
    hover_name=eq_titles,
)
fig.show()
