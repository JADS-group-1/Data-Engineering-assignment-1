import csv
from sklearn.model_selection import train_test_split
from pandas.core.common import random_state
from sklearn.linear_model import LinearRegression
import pickle
import numpy as np
import os
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials

GCP_CREDENTIALS = {
    'type': 'service_account',
    'client_id': os.environ['TRAINER_CLIENT_ID'],
    'client_email': os.environ['TRAINER_CLIENT_EMAIL'],
    'private_key_id': os.environ['TRAINER_PRIVATE_KEY_ID'],
    'private_key': os.environ['TRAINER_PRIVATE_KEY'],
}

def train_model():
    with open("data/salary.csv", "r") as f:
        reader = csv.reader(f)
        data = [x for x in reader]

    # X should be a matrix, so reshape it to be a matrix
    X = np.array([float(el[0]) for el in data[1:]]).reshape(-1,1)
    y = [float(el[1]) for el in data[1:]]
    
    model = LinearRegression()
    model.fit(X, y)
    return model


def upload_model(model):
    # The GCP API does not support uploading a variable, so it has to be dumped to a file first
    model_filename = "model.tmp.pickle"
    with open(model_filename, "wb") as f:
        pickle.dump(model, f)

    credentials = ServiceAccountCredentials.from_json_keyfile_dict(GCP_CREDENTIALS)
    client = storage.Client(credentials=credentials, project='assignment-1-model')
    bucket = client.get_bucket('model')
    blob = bucket.blob('model.pickle')
    blob.upload_from_filename(model_filename)


if __name__ == '__main__':
    model = train_model()
    upload_model(model)
