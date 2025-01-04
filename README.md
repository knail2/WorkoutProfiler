# WorkoutProfiler

WorkoutProfiler is an open-source application designed to help fitness trainers and enthusiasts evaluate and profile workout plans. It enables users to identify critical exercises, classify them by muscle groups, and determine which fitness dimensions (e.g., strength, endurance, cardio) are most relevant. The app stores all profiling data in a Snowflake database for tracking and analytics.

## Features

- **Workout Display**: View a workout plan with a list of exercises and their details.
- **Exercise Profiling**:
  - Mark exercises as "Critical" or "Not Critical."
  - Assign muscle group classifications for critical exercises.
  - Select relevant fitness dimensions (e.g., strength, endurance, cardio).
- **Primary Exercises**:
  - Require at least two fitness dimensions for compound exercises.
  - All other critical exercises need at least one fitness dimension.
- **Submission and Tracking**:
  - Submit profiled exercises to a Snowflake database.
  - Track changes in exercise profiles using Slowly Changing Dimensions (SCD2).

## How It Works

1. **Upload or Select a Workout Plan**:
   - Add your workout details to the app or select a pre-defined workout.

2. **Profile Exercises**:
   - Review each exercise and decide its criticality.
   - Assign classifications and fitness dimensions for critical exercises.

3. **Submit and Save**:
   - Save your profiled data to Snowflake, ensuring it is ready for future analysis.

4. **Track Progress**:
   - View changes in exercise profiling over time using the app’s built-in analytics.

## Use Cases

- Trainers optimizing workout plans for clients.
- Enthusiasts tracking their progress and refining workout regimens.
- Gym managers maintaining consistent and effective training programs.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/WorkoutProfiler.git
   cd WorkoutProfiler
