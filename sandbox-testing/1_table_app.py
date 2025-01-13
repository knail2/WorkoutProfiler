import streamlit as st
import pandas as pd

# Set page config for a clean layout
st.set_page_config(page_title="Exercise Categories", layout="centered")

# Create a custom style for the table
table_style = """
<style>
table {
    font-size: 12px;
    color: #4a4a4a;
    border-collapse: collapse;
    width: 100%;
}
th, td {
    border: 1px solid #333;
    padding: 8px;
    text-align: center;
}
</style>
"""


# Dropdown menu
dropdown = st.selectbox(
    "Select exercise type",
    options=["HIIT", "Endurance", "Hypertrophy", "Cardio"],
    index=1
)

st.markdown(table_style, unsafe_allow_html=True)


# Create the table layout with a dropdown
st.write("<table>", unsafe_allow_html=True)
st.write("<tr><th>Cell 1</th><th>Cell 2</th></tr>\
         <tr><td>Dropdown</td><td>{{dropdown}}</td></tr>\
         </table>", unsafe_allow_html=True)
#st.write("<tr><td>Dropdown</td><td>{{dropdown}}</td></tr>", unsafe_allow_html=True)
#st.write("</table>", unsafe_allow_html=True)

# Button
if st.button("Click Me"):
    st.write(f"You selected: {dropdown}")



# Define the table data
data = [
    ["Row 1, Col 1", "Row 1, Col 2"],
    ["Row 2, Col 1", "Row 2, Col 2"],
    ["Row 3, Col 1", "Row 3, Col 2"],
]

# Convert data to a DataFrame for rendering
df = pd.DataFrame(data, columns=["Column 1", "Column 2"])
