import streamlit as st
import pandas as pd

st.title("Workout App")

# Create the dataframe with workout entries
df = pd.DataFrame({
    'Workout': ['Cardio Blast', 'HIIT Burnout']
})

# Create a new dataframe with hyperlinks
df['Link'] = df['Workout'].apply(lambda x: f'[{x}](pages/workout_details?workout={x.replace(" ", "%20")})')

# Display the dataframe with hyperlinks
st.write("All Workouts:")
st.write(df[['Workout', 'Link']].to_html(escape=False, index=False), unsafe_allow_html=True)