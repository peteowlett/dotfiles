import os
import joblib
import tempfile
from google.cloud import storage


def dump_obj_to_gs(
        obj,
        obj_name,
        bucket_name='user-workspaces',
        folder_name='user_pete_owlett/obj_store/'
    ):
    """Uploads a python object to a bucket using joblib."""

    # Dump to object to a tempfile
    savedir = tempfile.mkdtemp()
    filename = obj_name + '.joblib'
    local_filepath = os.path.join(savedir, filename)
    joblib.dump(obj, local_filepath)

    # Upload it to GS
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    destination_blob_name = os.path.join(folder_name, filename)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(local_filepath)

    print('File {} uploaded to {}.'.format(
        obj_name,
        destination_blob_name,
    ))


def load_obj_from_gs(
        obj_name,
        bucket_name='user-workspaces',
        folder_name='user_pete_owlett/obj_store/',
    ):
    """Downloads a python object from a bucket using joblib."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    filename = obj_name + '.joblib'
    source_blob_name = os.path.join(folder_name, filename)
    blob = bucket.blob(source_blob_name)

    savedir = tempfile.mkdtemp()
    local_filepath = os.path.join(savedir, filename)
    blob.download_to_filename(local_filepath)

    return joblib.load(local_filepath)
