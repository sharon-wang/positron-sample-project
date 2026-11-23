# Run this file to open a database connection.
# In Positron 2026.12 or later, it shows up in the Data Connections view.
import sqlite3

con = sqlite3.connect("data/weather.sqlite")
