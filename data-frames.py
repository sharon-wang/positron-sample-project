# Run this file to fill the Variables pane.
import json

import pandas as pd

# A data frame: opens in the Data Explorer
weather = pd.read_csv("data/weather.csv", parse_dates=["date"])

# A nested dict: opens in the Object Explorer
with open("data/nested.json") as f:
    project = json.load(f)

# A few plain values
station_count = weather["station"].nunique()
warmest = weather["temperature_c"].max()
