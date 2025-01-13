import streamlit as st
import pandas as pd

# Mock Snowflake connection and data fetching
def fetch_data_from_snowflake():
    # This is a mock function. In reality, you would use a Snowflake connection here.
    return pd.DataFrame({
        'Exercise': ['Push-ups', 'Squats', 'Lunges', 'Plank'],
        'Classification': ['Upper Body', 'Lower Body', 'Lower Body', 'Core'],
        'Critical': ['Yes', 'Yes', 'No', 'Yes']
    })

# Mock Snowflake insert operation
def insert_to_snowflake(data):
    # This is a mock function. In reality, you would use a Snowflake connection here.
    st.success("Data inserted into Snowflake successfully!")

# Fetch data (mock)
df = fetch_data_from_snowflake()

# Create a form for user input
with st.form("exercise_form"):
    st.write("Exercise Profile")
    
    # Use st.data_editor with dropdown options
    edited_df = st.data_editor(
        df,
        column_config={
            "Exercise": st.column_config.TextColumn(
                "Exercise",
                help="Name of the exercise",
                disabled=True
            ),
            "Classification": st.column_config.SelectboxColumn(
                "Classification",
                help="Select the classification of the exercise",
                options=["Upper Body", "Lower Body", "Core"],
                required=True
            ),
            "Critical": st.column_config.SelectboxColumn(
                "Critical",
                help="Is this exercise critical?",
                options=["Yes", "No"],
                required=True
            )
        },
        hide_index=True,
        num_rows="fixed"
    )
    
    # Submit button
    submitted = st.form_submit_button("Submit Profile")

# Handle form submission
if submitted:
    # Display the edited dataframe
    st.write("Updated Exercise Profile:")
    st.dataframe(edited_df)
    
    # Insert the edited data to Snowflake (mock operation)
    insert_to_snowflake(edited_df)

# Display the original data
st.write("Original Data:")
st.dataframe(df)