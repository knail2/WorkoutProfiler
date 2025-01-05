import streamlit as st

def render_workouts_page():
    st.title("All Workouts Table of Contents")

    # Check if selected_workout exists in session state
    if "selected_workout" not in st.session_state:
        st.session_state["selected_workout"] = None

    # Define workout information
    workouts = [
        {"name": "Strength Blast", "trainer": "Trainer A", "id": "strength_blast"},
        {"name": "Cardio Burn", "trainer": "Trainer B", "id": "cardio_burn"},
    ]

    # Display workouts as buttons
    for index, workout in enumerate(workouts):
        print("workout_button: {}, workout_id: {}.".format(workout['name'], workout['id']))
        st.write("workout_button: {}, workout_id: {}.".format(workout['name'], workout['id']))
        if st.button(f"View {workout['name']}", key=f"workout_button_{workout['id']}_{index}"):
            st.session_state["selected_workout"] = workout
            st.session_state["page"] = "Workout_Details"
            break
        print("--")
        
    st.write(f"Debug: Page = {st.session_state['page']}")
    st.write(f"Debug: workout Selected = {st.session_state['selected_workout']}")

        # Route to the appropriate page
    if st.session_state["page"] == "All_Workouts_TOC":
        # do nothing
        st.write("passing chickadoo")
        pass
    elif st.session_state["page"] == "Workout_Details":
        from pages.Workout_Details import render_workout_details_page
        render_workout_details_page()
    elif st.session_state["page"] == "Exercise_Details":
        from pages.Exercise_Details import render_exercise_details_page
        render_exercise_details_page()
    else:
        st.write("Page not found.")

