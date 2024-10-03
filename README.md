# Data Engineering assignment 1
For this assignment we have to create an ML pipeline. We should use python as much as possible, because that is easiest and then we can follow [the example](https://github.com/IndikaKuma/DE2024/tree/main/lab2). 
## Components
- Trainer
	- Contains the model training code, and contains the training data
	- When done, it uploads the trained model to a GCP cloud storage
- Web app
	- Contains both the backend and the frontend. 
		- (This is bad practice, but it is easiest so this is probably best for this simple assignment.)
	- Will serve up the frontend using templates, as done in the example.
	- Will contain a single endpoint for prediction. 
	- This service downloads the prediction model from the GCP cloud storage
- Pipeline
	- Spins up the trainer when the repository updates.

## Details
1 repository, each component has its own folder.

### Pipeline
- The pipeline is defined in `pipeline/cloudbuild.yaml`. This pipeline is a Google Cloud Build pipeline, and its executed on the Google servers.
- Every time the *main* branch updates, the pipeline is triggered.
	- I added this trigger in the Google Cloud Console. (Click [this link](https://console.cloud.google.com/products), search for 'Cloud Build', go to the 'Triggers' tab)
- The pipeline will
	- Dockerize all components
		- Upload the docker images to the GCP artifact registry
	- Spin up the trainer docker image, which will create and upload the model.

### Trainer
- Uses the `scikit-learn` Python package to create a simple linear regression model on [some simple data](./trainer/data/salary.csv).
- I have created this component already, but it is UNTESTED still.
- The model storage format should be [pickle](https://docs.python.org/3/library/pickle.html).
- The storage that we use is Google Cloud Storage.
- Uploading can quite simply be done using the `gcloud` Python package.

### Web app
- Uses Flask
- Uses HTML templates
- On startup, it downloads the model from the Google Cloud Storage and loads the model into memory.

## Running it
The `trainer` and `web-app` components contain Dockerfile's to containerize the application. Both require additional environment variables to run, which should be specified in the `docker run` command. To run the applications locally, you need to have the environment variables set. How to do this, you can find online.
