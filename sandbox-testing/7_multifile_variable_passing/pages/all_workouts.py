import pandas as pd
import streamlit as st

# Create the initial dataframe with workout entries
df = pd.DataFrame({
    "workouts": ["Cardio Blast", "HIIT Burnout"]
})

# Create df2 with pre-crafted links
df2 = pd.DataFrame({
    "workouts": df["workouts"],
    #"links": df["workouts"].apply(lambda x: f"workout_details?workout={x.replace(' ', ' ')}")
    "links": df["workouts"].apply(lambda x: f"workout_details?workout={x}")
})

st.title("All Workouts")

edited_df = st.data_editor(
    df2,
    column_config={
        "links": st.column_config.LinkColumn(
            "Workout Links",
            help="Click on a workout to see details",
            #display_text="View {workouts}",
            display_text=r"workout_details\?workout=(.*)"
        ),
    },
    hide_index=True,
    num_rows="dynamic"
)
