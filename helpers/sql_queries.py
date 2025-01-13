# Store pre-defined SQL queries here
ALL_WORKOUTS_QUERY = "SELECT * FROM all_workouts"
SPECIFIC_DETAILS_OF_WORKOUT = "SELECT workout_name, exercise_name, exercise_description, critical_exercise_selection, \
                                    exercise_classification, strength, endurance, flexibility, balance, cardio, \
                                    power, primary_movement, profiled_by \
                                FROM workout_details_2 \
                                WHERE current_row = TRUE AND workout_name = " # 'Cardio Blast' for example would be concatenated to this. 'Cardio Blast'  
