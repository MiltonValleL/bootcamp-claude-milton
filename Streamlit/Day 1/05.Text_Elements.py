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
    overview, all rather simple."""
)
st.markdown("---")
st.markdown("# Header 1")
st.markdown("## Header 2")
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
st.divider()
st.latex("x = x^3 + 5")

st.latex(r"""
    a + ar + a r^2 + a r^3 + \cdots + a r^n =
    \sum_{k=0}^n ar^k =
    a \left(\frac{1-r^{n+1}}{1-r}\right)
""")
st.divider()

# st.write ---------------------------------------
st.write("This is some text written on 'write()' method...")
