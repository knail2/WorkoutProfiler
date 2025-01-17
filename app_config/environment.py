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
            "stage": session.get_current_stage(),
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
