# Lines starting with "# %%" mark code cells.
# Run Cell, Run Next and Run Above links appear above each cell.

# %%
import pandas as pd

weather = pd.read_csv("data/weather.csv")

# %%
weather.describe()

# %%
weather.groupby("station")["temperature_c"].mean()
