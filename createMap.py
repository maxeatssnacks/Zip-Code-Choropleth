import plotly.express as px
from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("./FIPS.csv", dtype={"fips": str})


fig = px.choropleth(df, geojson=counties, locations='fips', color='cover',
                    color_continuous_scale="Viridis",
                    range_color=(0, 1),
                    scope="usa",
                    labels={'color': 'Coverage %'}
                    )
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
