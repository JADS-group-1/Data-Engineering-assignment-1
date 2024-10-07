# Data Engineering assignment 1
For this assignment we have to create an ML pipeline. We should use python as much as possible, because that is easiest and then we can follow [the example](https://github.com/IndikaKuma/DE2024/tree/main/lab2). 
## Components
- Web app
	- Contains both the backend and the frontend. 
		- (This is bad practice, but it is easiest so this is probably best for this simple assignment.)
	- Will serve up the frontend using templates, as done in the example.
	- Will contain a single endpoint for prediction. 
	- This service downloads the prediction model from the GCP cloud storage
- Pipelines
	- Vertex AI
		- Creates the model and uploads it.
	- CI/CD
		- This pipeline dockerizes the web app and uploads it to the GCP container registry

## Details
1 repository, each component has its own folder.

### Pipelines
- 2 pipelines: The Vertex AI pipeline and the normal CI/CD pipeline. Both are Google pipelines and therefore run on the Google servers
- Every time the *main* branch updates, the pipeline is triggered.
	- I added this trigger in the Google Cloud Console. (Click [this link](https://console.cloud.google.com/products), search for 'Cloud Build', go to the 'Triggers' tab)
- The Vertex AI pipeline is defined in `pipeline/vertex_ai`
	- This creates and uploads the model.
	- Done using [Kubeflow Pipelines DSL](https://cloud.google.com/vertex-ai/docs/pipelines/build-pipeline) 
	- Create components to do the processing
		- Component for data preparation
		- Component for model training
	- The pipeline and its components are built using Python with the KubeFlow library
		- It's compiled to a YAML file.
		- The YAML can be uploaded in the GCP console.
- The CICD pipeline is defined in `pipeline/cloudbuild.yaml`.
	- Will dockerize the web app and upload the image to the GCP container registry
	- Will trigger the Vertex AI Pipeline.
	- Afterwards, it will deploy the web-app Docker image to a Google Cloud Run instance

### Web app
- Uses Flask
- Uses HTML templates
- On startup, it downloads the model from the Google Cloud Storage and loads the model into memory.

## Method
The general division of tasks is as follows:\
Web app -> Eugen\
Vertex AI pipeline -> Mathijs\
CI/CD pipeline -> Yan

This is not set in stone, and we should help each other with each other's tasks.\
We will work with merge requests, to keep the overview. Reviewing should be assigned to Mathijs. This means everyone should work in their own branch.
## Running it
The `trainer` and `web-app` components contain Dockerfile's to containerize the application. Both require additional environment variables to run, which should be specified in the `docker run` command. To run the applications locally, you need to have the environment variables set. How to do this, you can find online.
