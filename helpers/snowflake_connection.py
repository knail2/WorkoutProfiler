import streamlit as st
import snowflake.connector
from app_config.environment import get_environment_config


def create_snowflake_connection():
    config = get_environment_config()
    if config["environment"] == "snowflake":
        # No need to connect as app is already in Snowflake
        return None

    import snowflake.connector
    return snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
    )