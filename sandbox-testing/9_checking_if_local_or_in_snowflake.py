import streamlit as st
from snowflake.snowpark.context import get_active_session

def is_snowflake_environment():
    """
    Detect if the app is running inside the Snowflake environment.
    """
    try:
        # Attempt to get the active Snowflake session
        get_active_session()
        return True
    except Exception:
        # If an exception occurs, it means we're not in the Snowflake environment
        return False

def get_environment_config():
    """
    Get configuration details based on the detected environment (Snowflake or local).
    """
    if is_snowflake_environment():
        # Inside Snowflake environment
        session = get_active_session()
        return {
            "environment": "snowflake",
            "database": session.get_current_database(),
            "schema": session.get_current_schema(),
            "use_snowflake_connector": False,  # Connector not required within Snowflake
        }
    else:
        # Local environment
        return {
            "environment": "local",
            "database": None,
            "schema": None,
            "stage": None,
            "use_snowflake_connector": True,
        }

# Streamlit app main function
def main():
    st.title("Environment Detector")

    # Get the environment configuration
    config = get_environment_config()

    # Display the detected environment and relevant details
    st.subheader("Current Environment")
    st.write(f"Environment: **{config['environment']}**")

    if config["environment"] == "snowflake":
        st.subheader("Snowflake Details")
        st.write(f"Database: **{config['database']}**")
        st.write(f"Schema: **{config['schema']}**")
        st.write(f"Use Snowflake Connector: **{config['use_snowflake_connector']}**")
    else:
        st.subheader("Local Environment")
        st.write("Running in local mode.")
        st.write(f"Use Snowflake Connector: **{config['use_snowflake_connector']}**")

if __name__ == "__main__":
    main()
