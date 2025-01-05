import streamlit as st

def render_exercise_details_page():
    st.title("Exercise Details")

    # Debugging: Print the selected exercise
    st.write(f"Debug: Selected Exercise = {st.session_state.get('selected_exercise')}")

    selected_exercise = st.session_state.get("selected_exercise")

    if not selected_exercise:
        st.write("No exercise selected.")
        return

    # Define images for exercises
    exercise_images = {
        "Push-ups": "https://fitliferegime.com/wp-content/uploads/2022/07/Standard-Push-Ups.png",
        "Pull-ups": "https://www.thebioneer.com/wp-content/uploads/2013/12/pull-ups.jpg",
        "Deadlifts": "https://thefitnessphantom.com/wp-content/uploads/2021/06/Barbell-Deadlift.jpg",
        "Running": "https://hips.hearstapps.com/hmg-prod/images/young-man-jogging-in-the-city-royalty-free-image-1586814705.jpg",
        "Cycling": "https://media.istockphoto.com/id/1142711254/photo/male-athlete-cycling-on-a-road-bike.jpg",
        "Jump Rope": "https://cdn2.coachmag.co.uk/sites/coachmag/files/2019/07/jump-rope.jpg",
    }

    exercise_image = exercise_images.get(selected_exercise)

    st.header(f"Exercise: {selected_exercise}")

    if exercise_image:
        st.image(exercise_image, caption=selected_exercise)
    else:
        st.write("No image available for this exercise.")
