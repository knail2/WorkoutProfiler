import streamlit as st
from helpers.snowflake_connection import create_snowflake_connection
from helpers.data_processing import fetch_query_results
from helpers.sql_queries import ALL_WORKOUTS_QUERY
import pandas as pd
import icecream as ic

def show_all_workouts():
    st.title("All Workouts")

    # Fetch data from Snowflake
    try:
        conn = create_snowflake_connection()
        cursor = conn.cursor()
        cursor.execute(ALL_WORKOUTS_QUERY)
        df = fetch_query_results(cursor)
        cursor.close()
        conn.close()
    except Exception as e:
        st.error(f"An error occurred while fetching workouts: {e}")
        df = pd.DataFrame()

    df.drop(columns=["WORKOUT_ID"], inplace=True)

    # Replace 'workout_name' column logic with a for loop
    for i in range(len(df)):
        df.loc[i, "WORKOUT_NAME"] = f"workout_details?workout={df.loc[i, 'WORKOUT_NAME']}"

    # Display the data using st.data_editor
    if not df.empty:
        st.write("Data from all_workouts table:")
    
        # Use st.data_editor with the column configuration
        edited_df = st.data_editor(
            df,
            column_config={
                "WORKOUT_NAME": st.column_config.LinkColumn(
                    "Workout Links",
                    help="Click on a workout to see details",
                    display_text=r"workout_details\?workout=(.*)"
                ),
            },
            hide_index=True,
            disabled=["WORKOUT_NAME"],  # Make the workout_name column non-editable
            use_container_width=True,
            num_rows="dynamic"
        )


if __name__ == "__main__":
    show_all_workouts()