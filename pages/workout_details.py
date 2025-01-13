import streamlit as st
from helpers.snowflake_connection import create_snowflake_connection
from helpers.data_processing import fetch_query_results
from helpers.sql_queries import SPECIFIC_DETAILS_OF_WORKOUT
import pandas as pd

# Debug flag
debug_enabled = st.secrets.get("DEBUG", False)

# Get the workout entry from the URL parameters
workout = st.query_params.get("workout", ["Cardio Blast"])

# Display the workout details
st.title(f"Workout Details: {workout}")

try:
    if debug_enabled:
        st.write("Debug mode is enabled.")
        st.write(f"Workout parameter: {workout}")

    # Connect to Snowflake and execute query
    conn = create_snowflake_connection()
    cursor = conn.cursor()
    query = f"{SPECIFIC_DETAILS_OF_WORKOUT}'{workout}'"

    if debug_enabled:
        st.write(f"Executing SQL Query: {query}")

    cursor.execute(query)
    df = fetch_query_results(cursor)
    cursor.close()
    conn.close()

    if debug_enabled:
        st.write("Query execution completed.")
        #st.write(f"Fetched data: {df}")
        st.data_editor(df)

    if df.empty:
        st.warning("No details available for the selected workout.")
    else:
        # Create a form for user input
        with st.form("exercise_form"):
            st.write("Exercise Profile")
    
            # Configure the column settings
            column_config = {
                "EXERCISE_CLASSIFICATION": st.column_config.SelectboxColumn(
                    "Exercise Classification",
                    options=df['EXERCISE_CLASSIFICATION'].unique(),
                    required=True,
                )
            }
            column_order = [
            "EXERCISE_NAME", "WORKOUT_NAME", "EXERCISE_DESCRIPTION", "EXERCISE_CLASSIFICATION",
            "CRITICAL_EXERCISE_SELECTION", "PRIMARY_MOVEMENT", "STRENGTH", "ENDURANCE",
            "FLEXIBILITY", "BALANCE", "CARDIO", "POWER", "PROFILED_BY"]

            # Display data editor
            edited_df = st.data_editor(
                df,
                column_order=column_order,
                column_config=column_config,
                hide_index=True,
                disabled=["exercise_name", "exercise_description", "profiled_by"],
                use_container_width=True,
            )

            # Submit button
            submitted = st.form_submit_button("Submit Profile")


    # Handle form submission
    if submitted:
        # Display the edited dataframe
        st.write("Updated Exercise Profile:")
        st.dataframe(edited_df)
    

except Exception as e:
    if debug_enabled:
        st.write("Error details:", e)
    st.error(f"An error occurred: {e}")
