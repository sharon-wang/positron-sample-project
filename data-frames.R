# Run this file to fill the Variables pane.

# A data frame: opens in the Data Explorer
weather <- read.csv("data/weather.csv", na.strings = c("", "NA"))
weather$date <- as.Date(weather$date)

# A nested list: opens in the Object Explorer
project <- list(
  project = "Positron sample project",
  stations = list(
    Harbour = list(lat = 44.1, lon = -76.5, sensors = c("temperature", "rain")),
    Hilltop = list(lat = 45.2, lon = -75.7, sensors = c("temperature", "wind"))
  ),
  settings = list(units = list(temperature = "C", rain = "mm"), active = TRUE)
)

# A few plain values
station_count <- length(unique(weather$station))
warmest <- max(weather$temperature_c)
