# Open this file and select Run Streamlit App in Terminal at the top right of the editor.
import pandas as pd
import streamlit as st

st.title("Weather stations")

weather = pd.read_csv("data/weather.csv", parse_dates=["date"])
station = st.selectbox("Station", sorted(weather["station"].unique()))
rows = weather[weather["station"] == station]

st.line_chart(rows, x="date", y="temperature_c")
st.dataframe(rows)
