import datetime

import streamlit as st

# ---------------------------------------------------------------------------
with st.form("Registration"):
    st.header("Registration Form")
    col1, col2, col3 = st.columns(3)
    with col1:
        sel_box = st.selectbox(
            label="",
            options=["Mr", "Mrs", "Miss"],
        )
    with col2:
        f_name = st.text_input(label="First Name")
    with col3:
        l_name = st.text_input(label="Last Name")
    # ---------------------------------------------------------------------------
    designation = st.selectbox(
        label="Designation",
        options=[
            "Software",
            "Sr. Software",
            "Technical Lead",
            "Manager",
            "Sr. Manager",
            "Project Manager",
        ],
    )
    # ---------------------------------------------------------------------------
    start_date = datetime.date(1900, 1, 1)
    ref_date = datetime.date(1980, 4, 11)
    end_date = datetime.date(2005, 12, 31)
    input_date = st.date_input(
        "Date of Birth", value=ref_date, min_value=start_date, max_value=end_date
    )
    # ---------------------------------------------------------------------------
    gender = st.radio(
        label="Select Gender", options=("Male", "Female", "Prefered Not to Say")
    )
    # ---------------------------------------------------------------------------
    age = st.slider(label="Age", min_value=1, value=21, max_value=100)
    # ---------------------------------------------------------------------------
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success("For submitted Successfully")
        st.json(
            {
                "Name": f"{f_name} {l_name}",
                "Age": age,
                "Gender": gender,
                "Date of Birth": input_date,
                "Designation": designation,
            }
        )
