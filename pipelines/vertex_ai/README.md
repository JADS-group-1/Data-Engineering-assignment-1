# How to run the Vertex AI pipeline

You need to have a GCP service account with roles:

- Storage Admin
- Storage Object Admin
- Vertex AI Custom Code Service Agent
- Vertex AI Service Agent

Then generate a key for the service account and download it in JSON form. Place the json file in this folder and name it `credentials.json`.

You also need a storage bucket. This bucket is used for:

- The dataset
- The outputted model
- Intermediary pipeline outputs.

Edit the constants in `pipeline.ipynb` accordingly.
