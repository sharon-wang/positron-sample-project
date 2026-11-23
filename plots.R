# Run this file to make three plots in the Plots pane.
weather <- read.csv("data/weather.csv", na.strings = c("", "NA"))
weather$date <- as.Date(weather$date)

plot(weather$date, weather$temperature_c, col = factor(weather$station), pch = 19,
     main = "Temperature by station", xlab = "Date", ylab = "Temperature (C)")

barplot(tapply(weather$rain_mm, weather$station, sum, na.rm = TRUE),
        main = "Total rain by station")

hist(weather$temperature_c, main = "Temperature", xlab = "Temperature (C)")
