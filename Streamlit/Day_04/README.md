# STREAMLIT PROGRESS *(Spring 1 - Day 4)*

<br><br>

## Sunday, May 10, 2026
<br>

Today I have worked on my first Capstone Project

```Python
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------
st.title("Claude Bootcamp - Day 4")
st.subheader("Sunday, May 10, 2026 - Capstone Project NO.1")
st.divider()

# ---------------------------------------------------------------------
# Show the data table
st.title("Population of Canada")
st.write(
    "Source table can be found [here](https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1710000901)"
)

df = pd.read_csv("data/quarterly_canada_population.csv")
with st.expander("See full data table"):
    st.write(df)

# ---------------------------------------------------------------------
# Creating the form for user input
with st.form("population_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("Choose a starting date")
        start_q = st.selectbox(
            label="Quarter", options=["Q1", "Q2", "Q3", "Q4"], index=2, key="start_q"
        )
        start_year = st.slider(
            label="Year",
            min_value=1991,
            max_value=2023,
            value=1991,
            step=1,
            key="start_year",
        )
    with col2:
        st.write("Choose an end date")
        end_q = st.selectbox(
            label="Quarter", options=["Q1", "Q2", "Q3", "Q4"], index=0, key="end_q"
        )
        end_year = st.slider(
            label="Year",
            min_value=1991,
            max_value=2023,
            value=2023,
            step=1,
            key="end_year",
        )
    with col3:
        st.write("Choose a location")
        location = st.selectbox(
            label="Choose a location", options=df.columns[1:], index=0, key="location"
        )

    submit_btn = st.form_submit_button(label="Analyze", type="primary")


# ---------------------------------------------------------------------
# Evaluating the user input
if start_year > end_year:
    st.error("Dates don't work. 'Start Year' must come before 'End Year'.")
    eval = False
if start_year == end_year:
    if start_q >= end_q:
        st.error("Dates don't work. 'Start Quarter' must come before 'End Quarter'.")
        eval = False
# ===========================================
start_row = f"{start_q} {start_year}"
end_row = f"{end_q} {end_year}"
# ===========================================
if start_row not in df["Quarter"].values:
    st.error(f"Start date {start_row} is not available in the data.")
    eval = False
else:
    result_start = df.loc[df["Quarter"] == start_row, location].values[0]

if end_row not in df["Quarter"].values:
    st.error(f"End date {end_row} is not available in the data.")
    eval = False
else:
    result_end = df.loc[df["Quarter"] == end_row, location].values[0]


# ---------------------------------------------------------------------
# Creting Tabs
if submit_btn and eval:
    tab1, tab2 = st.tabs(["Population Change", "Compare"])
    with tab1:
        st.header(
            f"Population change from {start_q} {start_year} to {end_q} {end_year} ({location})"
        )

        col1, col2 = st.columns(2)
        with col1:
            st.metric(label=f"{start_row}", value=result_start)
            delta_result = (result_end / result_start) - 1
            st.metric(
                label=f"{end_row}",
                value=result_end,
                delta=f"{delta_result:.2%}",
                delta_color="normal",
            )
        with col2:
            start_index = df.loc[df["Quarter"] == start_row].index.item()
            end_index = df.loc[df["Quarter"] == end_row].index.item()
            filtered_df = df.iloc[start_index : end_index + 1]

            fig, ax = plt.subplots()
            ax.plot(filtered_df["Quarter"], filtered_df[location])
            ax.set_title(f"{location}")
            ax.set_xlabel("Quarter")
            ax.set_ylabel("Population")
            ax.set_xticks(
                [filtered_df["Quarter"].iloc[0], filtered_df["Quarter"].iloc[-1]]
            )
            fig.autofmt_xdate()
            st.pyplot(fig)

    with tab2:
        st.subheader("Compare with other locations")
        all_locations = st.multiselect(
            "Choose other locations", options=df.columns[1:], default=[location]
        )

        fig, ax = plt.subplots()
        for each in all_locations:
            ax.plot(filtered_df["Quarter"], filtered_df[each], label=each)
        ax.set_xlabel("Quarter")
        ax.set_ylabel("Population")
        ax.set_xticks([filtered_df["Quarter"].iloc[0], filtered_df["Quarter"].iloc[-1]])
        st.pyplot(fig)
```
