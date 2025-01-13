import pandas as pd

def fetch_query_results(cursor):
    """Fetch results from a Snowflake cursor and return as a Pandas DataFrame."""
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    return pd.DataFrame(data, columns=columns)