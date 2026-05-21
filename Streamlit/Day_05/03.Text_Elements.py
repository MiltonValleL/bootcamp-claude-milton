# ----------------------------------------------------------
# Text Elements
#   - st.markdown()
#   - st.title()
#   - st.header()
#   - st.subheader()
#   - st.text()
#   - st.caption()
#   - st.code()
#   - st.latex()
# ----------------------------------------------------------
import streamlit as st

# ----------------------------------------------------------
# Markdown
st.markdown("""
# Welcome to Streamlit Crash Course
""")
st.divider()
# ----------------------------------------------------------
st.markdown("""
# Markdown

# For Heading Level -1 or Title use (#)
## For Heading Level -2 or Header use (##)
### For Heading Level -3 or Subheader use (###)
### For Heading Level -4

To create paragraphs, use a blank line to separate one or more lines of text.

---

## Emphasis
making text bold, italic, bold italic
- To **bold text**, add two asterisks or underscores before and after a word or phrase

- To *italicize text*, add one asterisk or underscore before and after a word or phrase.

- Add three asterisks or underscores before and after a word or ***phrase for bold italic***

---

## Blockquotes
To create a blockquote, add a > in front of a paragraph.

>Dorothy followed her through many of the beautiful rooms in her castle.
>>The Witch bade her clean the pots and kettles and sweep the floor and keep the fire fed with wood.

---

## List
### Order List (items with number)
1. First item
2. Second item
3. Third item
4. Fourth item
    1. Intendent Item1
    2. Intendent Item2



### Unordered List

add dashes (-), asterisks (*), or plus signs (+) in front of line items.
- First item
- Second item
- Third item
- Fourth item
    - Indent item 1
    - Indent item 2

---

## Links

To create a link, enclose the link text in brackets and then follow it immediately with the URL in parentheses

My favorite search engine is [Duck Duck Go](https://duckduckgo.com).

## URLs and Email Address

To quickly turn a URL or email address into a link, enclose it in angle brackets.

- <https://www.datascienceanywhere.org>
- <vallemilton@gmail.com>

----

## Images

To add an image, add an exclamation mark (!), followed by alt text in brackets, and the path or URL to the image asset in parentheses.

You can optionally add a title in quotation marks after the path or URL.

![Mountains are beautiful](https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80)

## Math

$$\LARGE \\frac{x^2+7x+17}{x-3}$$

$\LARGE \sum_{n=0}^{10}sin(x) + x^2$
""")
# ----------------------------------------------------------
st.divider()

# Title
st.title("This is Title")
st.caption("Using st.title(), you can display the text in title format")
st.text("written by: G. Sudheer")

# Header
st.header("This is Header")
st.caption("The text inside st.header(), is in header format")
st.text("written by: datascience Anywhere")

# Subheader
st.subheader("This is Subheader")
st.caption("Ths text inside st.subheader(), is in subheader format")
st.text("written by: Milton Valle")

st.divider()

# ----------------------------------------------------------
# Code
st.header("Code")

st.markdown("#### Generate Random Numbers")
body_code = """
import numpy as np

def generate_random(size):
    rand_num = np.random.random(size=size)
    return rand_num

number = generate_random(10)
"""
st.code(body=body_code, language="python")

st.divider()

# ----------------------------------------------------------
# latex
st.header("Latex")

formula = """
a + ax + ax^2 + ax^3 + \cdots + ax^{n-1}= \sum_{k=0}^{n-1} a x^k
"""
st.latex(formula)

st.markdown(
    "For more information on how to write formulas, please visit: [KATEX](https://katex.org/docs/supported.html)"
)
st.divider()
st.divider()
