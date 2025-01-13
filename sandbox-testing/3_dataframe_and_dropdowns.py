import streamlit as st
import pandas as pd
from snowflake.snowpark.functions import col

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
    
    # Create dropdowns for each row
    updated_data = []
    for _, row in df.iterrows():
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write(row['Exercise'])
        
        with col2:
            classification = st.selectbox(
                f"Classification for {row['Exercise']}",
                options=df['Classification'].unique(),
                key=f"class_{row['Exercise']}",
                index=df['Classification'].unique().tolist().index(row['Classification'])
            )
        
        with col3:
            critical = st.selectbox(
                f"Critical for {row['Exercise']}",
                options=df['Critical'].unique(),
                key=f"crit_{row['Exercise']}",
                index=df['Critical'].unique().tolist().index(row['Critical'])
            )
        
        updated_data.append([row['Exercise'], classification, critical])
    
    # Submit button
    submitted = st.form_submit_button("Submit Profile")

# Handle form submission
if submitted:
    # Create new dataframe with updated data
    new_df = pd.DataFrame(updated_data, columns=['Exercise', 'Classification', 'Critical'])
    
    # Display the new dataframe
    st.write("Updated Exercise Profile:")
    st.dataframe(new_df)
    
    # Insert the new data to Snowflake (mock operation)
    insert_to_snowflake(new_df)

# Display the original data
st.write("Original Data:")
st.dataframe(df)
