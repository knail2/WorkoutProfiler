import streamlit as st
#from snowflake.snowpark.context import get_active_session
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
import pandas as pd
import numpy as np
import random
import string


# Get the active Snowflake session
# session = get_active_session()

# query = "SELECT * FROM DEMO_DB.BT_RENEWAL_POC_SCHEMA.WORKOUT_DETAILS"

# # Execute the query
# df = session.sql(query).to_pandas()

def create_random_dataframe(rows=4, cols=25):
    """
    Creates a DataFrame with random numbers and random nonsense column names.

    Parameters:
    rows (int): Number of rows in the DataFrame.
    cols (int): Number of columns in the DataFrame.

    Returns:
    pd.DataFrame: DataFrame with random numbers and random column names.
    """
    # Generate random column names
    def random_column_name(length=8):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    column_names = [random_column_name() for _ in range(cols)]

    # Generate random data
    data = np.random.rand(rows, cols)

    # Create and return the DataFrame
    return pd.DataFrame(data, columns=column_names)


df = create_random_dataframe()

# Set up Streamlit
st.title("DCAM Metadata")

# Initialize session state for update_mode
if "update_mode" not in st.session_state:
    st.session_state.update_mode = "MODEL_CHANGED"

# ... (your create_random_dataframe function)

# Set up Streamlit
st.title("DCAM Metadata")
df = create_random_dataframe()

# Configure Ag-Grid
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
gb.configure_side_bar()

# Freeze the first two columns
for i, col in enumerate(df.columns[:2]):
    gb.configure_column(col, pinned='left')

# Add conditional formatting
cellstyle_jscode = JsCode("""
function(params) {
    if (params.value < 0.3) {
        return {
            'color': 'white',
            'backgroundColor': 'red'
        }
    } else if (params.value > 0.7) {
        return {
            'color': 'white',
            'backgroundColor': 'green'
        }
    }
    return {
        'color': 'black',
        'backgroundColor': 'white'
    }
};
""")

gb.configure_columns(df.columns, cellStyle=cellstyle_jscode)

# Add column filter
gb.configure_columns(df.columns, filterable=True)

# Add pagination
gb.configure_pagination(paginationAutoPageSize=True)

# Add row selection
gb.configure_selection('multiple', use_checkbox=True)

gridOptions = gb.build()

# Display the Ag-Grid table
grid_response = AgGrid(
    df, 
    gridOptions=gridOptions, 
    enable_enterprise_modules=True, 
    allow_unsafe_jscode=True, 
    update_mode=st.session_state.update_mode
)

# Display selected rows
selected_rows = grid_response['selected_rows']
st.write("Selected rows:")
st.json(selected_rows)