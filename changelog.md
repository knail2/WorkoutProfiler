# Changelog

## Tasks to Complete

### 1. Basic HTML Table with Drop-down Options
- Create a simple HTML table where:
  - Each cell contains either text or a drop-down menu.
  - Drop-down menus have 2-5 options, with one option selected by default.
- Render this HTML table to test its functionality.

### 2. Dynamic Update Query Based on Drop-down Selections
- Extend the HTML table to include:
  - A button that, when clicked, takes the selections made in the drop-down menus.
  - Generate a dynamic SQL `UPDATE` statement using the drop-down selections.
  - The SQL statement should target a table called `DECAM`.
- Test the button functionality to ensure the query is dynamically generated based on input.

### 3. All Workouts Table of Contents (TOC)
- Create a table to display the "All Workouts" overview:
  - Columns:
    - `Workout Signed Off`: Displays the sign-off status for each workout.
    - `Number of Exercises`: Displays the total number of exercises in each workout.

### 4. Workout Details Table
- Create a table for "Workout Details":
  - Columns:
    - `Exercise Signed Off`: Tracks whether each exercise is signed off.
- Implement functionality for signing off exercises:
  - Upon submission, generate an `UPDATE` SQL statement for the respective exercise.
  - Execute the SQL statement against Snowflake.
  - Perform a `SELECT` query to confirm the data update.
  - Populate the `Exercise Signed Off` column with the name of the logged-in user upon successful update.

---

### Notes
- Ensure all SQL queries and updates are tested and verified with Snowflake.
- Maintain user session data to retrieve the logged-in user for sign-off tracking.
- Ensure proper error handling for SQL execution and data retrieval steps.

---

This changelog outlines the step-by-step tasks required to complete the job. Progressively test each step before moving to the next for seamless integration.
