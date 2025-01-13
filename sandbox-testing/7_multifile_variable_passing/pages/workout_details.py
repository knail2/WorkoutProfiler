import streamlit as st

# Get the workout entry from the URL parameters
workout = st.query_params.get("workout", "not selected")

# Display the workout details
st.title(f"Workout Details: {workout}")
st.write(f"Hello {workout}")
