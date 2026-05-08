import streamlit as st

# Give you app a title ---------------------------------------
st.title("Hands-On Machine Learning with Scikit-Learn and PyTorch")


# Header ---------------------------------------
st.header("Written by: Aurélien Géron - 2025 Edition")


# Subheader ---------------------------------------
st.subheader("Chapter 1 - The Machine Learning Landscape ")


# Markdown ---------------------------------------
st.markdown(
    """This chapter introduces a lot of fundamental concepts (and jargon)
    that every data scientist should know by heart. It will be a high-level
    overview (it’s the only chapter without much code), all rather simple,
    but my goal is to ensure everything is crystal clear to you before we
    continue on to the rest of the book. So grab a coffee and let’s get started!
    If you are already familiar with machine learning basics, you may want to
    skip directly to Chapter 2. If you are not sure, try to answer all the
    questions listed at the end of the chapter before moving on."""
)
st.markdown("---")
st.markdown("# Header 1")
st.markdown("## Header 2")
st.markdown("### Header 3")
st.markdown("---")


# Caption ---------------------------------------
st.caption(
    "[Machine learning is the] field of study that gives computers the ability to learn without being explicitly programmed."
)
st.caption("—Arthur Samuel, 1959")


# Code Block ---------------------------------------
st.code("""import pandas as pd
df = pd.read_csv(my_csv_file)
df.head()""")


# Preformatted Text ---------------------------------------
st.text(
    "This is a very basic text. Not very useful, but it's ok to know that this method exists."
)


# LaTex ---------------------------------------
st.latex("x = x^3 + 5")


# Divider ---------------------------------------
st.text("Text created above the 'divider()' method.")
st.divider()
st.text("Text created below the 'divider()' method.")

# st.write ---------------------------------------
st.write("This is some text written on 'write()' method...")
