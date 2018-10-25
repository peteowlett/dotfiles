import os
from google.cloud import bigquery

def get_bigquery(user_query):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/pete/.gsutil/data-warehouse-942b03e59723.json'
    client = bigquery.Client()
    query_job = client.query(user_query)
    results = query_job.result()
    return results.to_dataframe()

