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
        user=st.secrets["snowflake"]["user"],
        password=st.secrets["snowflake"]["password"],
        account=st.secrets["snowflake"]["account"],
        warehouse=st.secrets["snowflake"]["warehouse"],
        database=st.secrets["snowflake"]["database"],
        schema=st.secrets["snowflake"]["schema"]
    )