# GEOJSON FORMAT

from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
BASE = Path(__file__).parent
path = BASE/"eq_data/eq_data_30_day_m1.geojson"
contents = path.read_text()
#? loads: str -> obj
all_eq_data = json.loads(contents)

'''
# Create a more readable version of the data file.
path = BASE/"eq_data/readable_eq_data.geojson"
#? dumps: obj -> str
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)
'''

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data["features"]
#print(len(all_eq_dicts))
mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"]
    lon = eq_dict["geometry"]["coordinates"][0]
    lat = eq_dict["geometry"]["coordinates"][1]
    eq_title = eq_dict["properties"]["title"]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)
#print(mags[:10])
#print(lons[:5])
#print(lats[:5])

# Mapping earthquakes.
title = "Global Earthquakes"
fig = px.scatter_geo(
    lat=lats, lon=lons, size=mags, title=title,
    color=mags,
    color_continuous_scale="viridis", # amp
    labels={"color":"Magnitude"},
    projection="natural earth",
    hover_name=eq_titles,
)
# for more color scales
# >>> import plotly.express as px
# >>> px.colors.named_colorscales()
fig.show()

