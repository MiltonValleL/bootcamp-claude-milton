import time

import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
#  Writting info on Main Frame
st.subheader("Show a DataFrame on the Main Frame")
st.write("The name of the columns that the DataFrame has are:")

## Load tips.csv
df = pd.read_csv("resources/tips.csv")

cols = tuple(df.columns)
st.write(cols)  # Tuples looks like special chars
st.dataframe(df, width=540, height=140)  # Shows DF
st.divider()

# ---------------------------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------------------------
side_bar = st.sidebar  # Creation
# --------------------------Writting info on Sidebar-------------------------
side_bar.header("Sidebar `st.sidebar`")
side_bar.caption("Elements that added in the sidebar are pinned to the left")
# -----------------Create a Widget on the Sidebar - selectbox----------------
select_col = st.sidebar.selectbox(label="Select a column from the list:", options=cols)
side_bar.write(f"Column Selected: '{select_col}'")


# ---------------------------------------------------------------------------
# COLUMNS
# ---------------------------------------------------------------------------
st.subheader("Columns Layout - `st.columns(N)`")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("#### Column 1")
    st.image("resources/image.jpg")
with col2:
    st.markdown("#### Column 2")
    st.dataframe(df, height=220)
with col3:
    st.markdown("#### Column 3")
    st.dataframe(df[select_col], width=150, height=220)
st.divider()

# ---------------------------------------------------------------------------
# EXPANDER
# ---------------------------------------------------------------------------
st.subheader("Expander Layout `st.expander()`")
# ---------------------------------------------------------------------------
# Method No. 1 - (Assign to a variable)
# =====================================
my_expander = st.expander(label="Did you know that...")
my_expander.write("This content is inside the expander.")
if my_expander.button("Click here"):
    my_expander.success("You just clicked on the Button - CONGRATULATIONS!!!")
    my_expander.image("resources/small_logo.png", width=210)
    my_expander.button("Reset")
else:
    my_expander.warning("I am waiting for a click...")

# ---------------------------------------------------------------------------
# Method No. 2 - Using WITH
# =========================
with st.expander(label="Some explanation of `st.expander`"):
    st.write("""
    An `st.expander` in Streamlit is a **collapsible container** that lets you toggle
    the visibility of a section of content. It is perfect for decluttering your app
    by hiding supplementary data, charts, or widget menus until the user chooses to
    view or interact with them.
    """)
    a, b, c = st.columns(3)
    with b:
        st.image("resources/streamlit_logo.png")
    st.code(
        """
# You create expander with st.write
import streamlit as st
st.expander('This is a Trial/Error')
""",
        language="python",
    )
st.divider()

# ---------------------------------------------------------------------------
# CONTAINERS
# ---------------------------------------------------------------------------
st.subheader("Container Layout `st.container()`")

with st.container():
    st.write(
        """In Streamlit, `st.container()` is a layout tool that lets you group multiple elements together.
        It is especially useful for inserting elements into your app out of order or creating organized
        sections with specific styling."""
    )
    st.image(
        "resources/small_logo.png",
        width=300,
        caption="This image is within the Container",
    )
st.divider()

# ---------------------------------------------------------------------------
# EMPTY
# ---------------------------------------------------------------------------
st.subheader("Empty Layout -  `st.empty`")
st.write(
    """`st.empty()` is a layout tool in Streamlit that creates a single-element placeholder.
    It allows you to reserve a spot in your app and update, replace, or clear its content
    later without rerunning the entire script."""
)

placeholder = st.empty()

for i in range(1, 11):
    placeholder.write(f"This message will dissapear in {10 - i} seconds")
    time.sleep(1)
placeholder.empty()

st.divider()
