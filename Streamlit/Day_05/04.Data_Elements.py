import numpy as np
import pandas as pd
import streamlit as st

# -------------------------------------------------------------
df = pd.read_csv("resources/tips.csv")

st.header("st.dataframe()")
st.caption("Display a DataFrame as an interactive table")

st.text("Shorter Configuracion:")
st.dataframe(data=df, width="content", height="stretch")

st.text("Manual Configuracion:")
st.dataframe(data=df, width=900, height=180)
st.divider()

# -------------------------------------------------------------
# st.static
st.header("st.table")
st.caption("Display a DataFrame as an static table - using `df.head()`")

st.table(data=df.head(), width="content")

num = np.array([1, 2, 3])

# -------------------------------------------------------------
# st.json
st.header("st.json()")
st.caption("Display object or string as a pretty-printted JSON string")

json_values = df.head(3).to_dict()
st.json(body=json_values)
