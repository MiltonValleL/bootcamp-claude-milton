import pandas as pd
import streamlit as st

df = pd.read_csv("data/sample.csv", dtype="int")

# -------------------------------------------------------------
st.title("Claude Bootcamp - Day 2")
st.subheader("Friday, May 08, 2026")
st.divider()

st.header("Displaying Elements")


# -------------------------------------------------------------
# Displaying a DataFrame
# Show DataFrame - Method 1
st.dataframe(df)

# Show DataFrame - Method 2
st.write(df)

# Show DataFrame - Method 3 (static table)
st.table(df)
st.divider()


# -------------------------------------------------------------
# Displaying Metrics
st.metric(label="Metric Label", value=900, delta=-20, delta_color="normal")

st.metric(label="Expenses", value=1050, delta=-36, delta_color="inverse")

st.metric(label="Population", value=12000000, delta=8.5, delta_color="green")
