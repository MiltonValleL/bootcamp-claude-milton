# STREAMLIT PROGRESS *(Spring 1 - Week 1)*

<br><br>

## Thursday, May 07, 2026
1. Today I have installed the Streamlit Python library and Framework.
2. I have learned how to execute **Streamlit** from the terminal.
3. I have learned how to create `Text Elements`.
```Python
import streamlit as st

# -------------------------------------------------------------------------
st.title("Streamlit Progress")


st.header("Text Elements")


st.subheader("How to create a title")


st.markdown("# Header 1")


st.text("This is a very basic text")


# -------------------------------------------------------------------------
# used to creage a division line
st.divider()


st.write("This is a multiple purpose method")

# -------------------------------------------------------------------------
# Generally used for quotes
st.caption("[Machine learning is the] field of study that gives computers
the ability to learn without being explicitly programmed.")


st.code("""import pandas as pd
df = pd.read_csv(my_csv_file)
df.head()""")


st.latex(r"""
    a + ar + a r^2 + a r^3 + \cdots + a r^n =
    \sum_{k=0}^n ar^k =
    a \left(\frac{1-r^{n+1}}{1-r}\right)
""")
# -------------------------------------------------------------------------
```
