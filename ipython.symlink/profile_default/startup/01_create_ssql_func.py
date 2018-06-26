from google.cloud import bigquery

def get_bigquery(user_query):
    client = bigquery.Client()
    query_job = client.query(user_query)
    results = query_job.result()
    return(results)

