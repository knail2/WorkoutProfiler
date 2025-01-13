# app_config/environment.py

# Logic to detect whether you’re running locally or in Snowflake.
# Example approach: check if certain Snowflake environment variables are set, 
# or you might catch if st.secrets["connection"] is present.