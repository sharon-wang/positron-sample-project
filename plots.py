# Run this file to make three plots in the Plots pane.
import matplotlib.pyplot as plt
import pandas as pd

weather = pd.read_csv("data/weather.csv", parse_dates=["date"])

for station, rows in weather.groupby("station"):
    plt.plot(rows["date"], rows["temperature_c"], label=station)
plt.title("Temperature by station")
plt.legend()
plt.show()

weather.groupby("station")["rain_mm"].sum().plot.bar(title="Total rain by station")
plt.show()

plt.scatter(weather["temperature_c"], weather["rain_mm"])
plt.title("Temperature vs rain")
plt.xlabel("Temperature (C)")
plt.ylabel("Rain (mm)")
plt.show()
