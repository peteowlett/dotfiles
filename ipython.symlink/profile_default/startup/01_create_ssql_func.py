import os
import pandas as pd
import snowflake.connector

def get_ssql(query):
    """
    Execute a single SQL statement against snowflake, get
    the results, parse to dataframe and return
    """
    cnx = snowflake.connector.connect(
      user=os.environ['SNOWFLAKE_USERNAME'],
      password=os.environ['SNOWFLAKE_PASSWORD'],
      account=os.environ['SNOWFLAKE_HOST'],
    )

    cursor = cnx.cursor()
    cursor.execute("USE WAREHOUSE RIDER_TRAINING;")
    cursor.execute("USE DATABASE PRODUCTION;")
    cursor.execute("USE SCHEMA RIDER_PLANNING;");

    results = cursor.execute(query).fetchall()
    df = pd.DataFrame(results, columns=[x[0] for x in cursor.description])
    return df
