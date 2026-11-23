# Lines starting with "# %%" mark code cells.
# Run Cell, Run Next and Run Above links appear above each cell.

# %%
weather <- read.csv("data/weather.csv", na.strings = c("", "NA"))

# %%
summary(weather)

# %%
tapply(weather$temperature_c, weather$station, mean)
