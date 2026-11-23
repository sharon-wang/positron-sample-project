"""Generates the sample data files in data/. Run from the repo root: python scripts/make_data.py"""
import csv
import json
import random
import sqlite3
from datetime import date, timedelta

random.seed(2026)

stations = ["Harbour", "Hilltop", "Riverside", "Airport", "Downtown"]
rows = []
start = date(2026, 1, 1)
for i in range(60):
    station = stations[i % len(stations)]
    day = start + timedelta(days=i // len(stations))
    temp = round(random.uniform(-12, 8), 1)
    rain = round(random.uniform(0, 25), 1) if random.random() > 0.15 else None
    windy = random.random() > 0.6
    rows.append({
        "station": station,
        "date": day.isoformat(),
        "temperature_c": temp,
        "rain_mm": rain,
        "windy": "TRUE" if windy else "FALSE",
        "notes": "Sensor check" if i % 17 == 0 else None,
    })

with open("data/weather.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0]))
    writer.writeheader()
    for row in rows:
        writer.writerow({k: ("" if v is None else v) for k, v in row.items()})

con = sqlite3.connect("data/weather.sqlite")
con.executescript("""
DROP TABLE IF EXISTS readings;
DROP TABLE IF EXISTS stations;
CREATE TABLE stations (name TEXT PRIMARY KEY, elevation_m INTEGER, opened INTEGER);
CREATE TABLE readings (station TEXT REFERENCES stations(name), date TEXT, temperature_c REAL, rain_mm REAL, windy INTEGER, notes TEXT);
""")
con.executemany("INSERT INTO stations VALUES (?, ?, ?)", [(s, random.randint(2, 400), random.randint(1950, 2020)) for s in stations])
con.executemany(
    "INSERT INTO readings VALUES (:station, :date, :temperature_c, :rain_mm, :windy = 'TRUE', :notes)",
    rows,
)
con.commit()
con.execute("VACUUM")
con.close()

nested = {
    "project": "Positron sample project",
    "version": 1,
    "stations": [
        {"name": s, "location": {"lat": round(random.uniform(43, 46), 4), "lon": round(random.uniform(-80, -75), 4)}, "sensors": ["temperature", "rain", "wind"]}
        for s in stations
    ],
    "settings": {"units": {"temperature": "C", "rain": "mm"}, "active": True, "tags": None},
}
with open("data/nested.json", "w") as f:
    json.dump(nested, f, indent=2)
    f.write("\n")

print("Wrote data/weather.csv, data/weather.sqlite, data/nested.json")

# A Stata file, for the Data Explorer's extra file formats (Positron 2026.12)
try:
    import pandas as pd

    df = pd.read_csv("data/weather.csv")
    df["windy"] = df["windy"].astype(int)
    df.to_stata("data/weather.dta", write_index=False)
    print("Wrote data/weather.dta")
except ImportError:
    print("Skipped data/weather.dta (needs pandas)")
