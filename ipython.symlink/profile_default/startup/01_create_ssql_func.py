import os
import pandas
from google.cloud import bigquery

def get_bigquery(user_query):
    client = bigquery.Client()
    query_job = client.query(user_query)
    results = query_job.result()
    return results.to_dataframe()

def get_kobo(user_query):
    try:
        import sshtunnel
    except Exception as e:
        print("You need to install sshtunnel to use this function")
        raise e

    try:
        from sqlalchemy import create_engine
    except Exception as e:
        print("You need to install sqlalchemy to use this function")
        raise e

    private_key_path = os.environ['GITHUB_KEY_PATH']
    server = sshtunnel.SSHTunnelForwarder(
        os.environ['KOBO_HOST'],
        ssh_username='pete',
        ssh_pkey=private_key_path,
        remote_bind_address=('localhost', 5432),
    )

    server.start()
    pg_secret = os.environ['PGPASSWORD']
    local_port = server.local_bind_port
    engine = create_engine(
        'postgresql://styleme:' + str(pg_secret) + '@localhost:' + str(local_port) + '/styleme'
    )
    return pandas.read_sql_query(user_query, con=engine)
