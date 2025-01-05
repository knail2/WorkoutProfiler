import streamlit as st

def render_workout_details_page():
    st.title("Workout Details")

    # Debugging: Print the selected workout details
    st.write(f"Debug: Selected Workout = {st.session_state.get('selected_workout')}")

    selected_workout = st.session_state.get("selected_workout")

    if not selected_workout:
        st.write("No workout selected.")
        return

    # Define workout-specific exercises
    workouts = {
        "strength_blast": {"name": "Strength Blast", "exercises": ["Push-ups", "Pull-ups", "Deadlifts"]},
        "cardio_burn": {"name": "Cardio Burn", "exercises": ["Running", "Cycling", "Jump Rope"]},
    }

    workout = workouts.get(selected_workout["id"])
    if not workout:
        st.write("Workout not found.")
        return

    st.header(f"Workout: {workout['name']}")

    # Display exercises as buttons
    for exercise in workout["exercises"]:
        if st.button(f"View {exercise}"):
            st.session_state["selected_exercise"] = exercise
            st.session_state["page"] = "Exercise_Details"
            st.experimental_set_query_params(page="Exercise_Details")
