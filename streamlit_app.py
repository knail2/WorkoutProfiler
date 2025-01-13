import streamlit as st
from pages.all_workouts import show_all_workouts

st.set_page_config(
    page_title="Workout Dashboard",
    page_icon=":runner:",
    layout="wide",
)

st.title("Welcome to the Workout Dashboard")
st.markdown("Explore all workouts below.")

# Call the function to show all workouts
show_all_workouts()