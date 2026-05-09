import pandas as pd
import streamlit as st

# ------------------------------------------------------
st.title("Claude Bootcamp - Day 2")
st.subheader("Friday, May 08, 2026")
st.divider()
st.header("Charting Elements")

# ------------------------------------------------------------------------------------
# Datasets of the file
df1 = pd.read_csv("data/sample.csv")
df2 = pd.read_csv("data/sample_map.csv")

# ------------------------------------------------------------------------------------
# Streamlit line plot
st.subheader("Line Chat")
st.line_chart(df1, x="YEAR", y=["COL_1", "COL 2", "COL-3"])

# Streamlit area chart
st.subheader("Area Chart")
st.area_chart(df1, x="YEAR", y=["COL_1", "COL 2", "COL-3"])

# Streamlit bar chart
st.subheader("Bar Chart")
st.bar_chart(df1, x="YEAR", y=["COL_1", "COL 2", "COL-3"])

# ------------------------------------------------------------------------------------
# Streamlit map
# st.map(df2)
# st.map(df2, width="stretch")

import folium
from streamlit_folium import st_folium

st.divider()
st.subheader("Map")

m = folium.Map(location=[df2["latitude"].mean(), df2["longitude"].mean()], zoom_start=5)

for _, row in df2.iterrows():
    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=8,
        color="crimson",
        fill=True,
        fill_opacity=0.7,
    ).add_to(m)

st_folium(m, use_container_width=True, height=400)


# ------------------------------------------------------------------------------------
# Matplotlib
import matplotlib.pyplot as plt

st.divider()
st.subheader("Matplotlib")

fig, ax = plt.subplots()
ax.plot(df1["YEAR"], df1["COL_1"])
ax.set_title("Figure Title")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
fig.autofmt_xdate()

st.pyplot(fig)
# ------------------------------------------------------------------------------------
