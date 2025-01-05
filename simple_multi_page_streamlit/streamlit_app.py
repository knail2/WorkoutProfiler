import streamlit as st

# Initialize session state variables
if "selected_workout" not in st.session_state:
    st.session_state["selected_workout"] = {}

if "selected_exercise" not in st.session_state:
    st.session_state["selected_exercise"] = None

if "page" not in st.session_state:
    st.session_state["page"] = "All_Workouts_TOC"

def main():
    # Debugging: Print the resolved page value
    st.write(f"Debug: Page = {st.session_state['page']}")
    st.session_state["selected_workout"] = {}
    # Route to the appropriate page
    if st.session_state["page"] == "All_Workouts_TOC":
        from pages.All_Workouts_TOC import render_workouts_page
        render_workouts_page()
    elif st.session_state["page"] == "Workout_Details":
        from pages.Workout_Details import render_workout_details_page
        render_workout_details_page()
    elif st.session_state["page"] == "Exercise_Details":
        from pages.Exercise_Details import render_exercise_details_page
        render_exercise_details_page()
    else:
        st.write("Page not found.")

if __name__ == "__main__":
    main()
