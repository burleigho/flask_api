## About

The code in this repository builds a FLask application serving three endpoints

```\metrics``` - automatically created by Prometheus Flask Exporter

```\login```   - returning a 200 response

```\secret```  - a secret passed it from a local env var at build time

## Usage

Set env var APP_SECRET to your secret value

```export APP_SECRET={enter your secret value}```

If using Docker to build this application, run the following command

```docker build --secret id=env,env=APP_SECRET .```

It is advisable to tag your image during the build stage using the command below, with a commit ID or unique value to identify your build

```docker build -t {image_name}:{commit_hash} --secret id=env,env=APP_SECRET .```

To run your application locally via Docker using the image name and tag built in the previous step

```docker run -d -p {host_port}:5000 {image_name}:{commit_hash}```

Open a browser and navigate to the following URL susbstituting the endpoint with one of the three listed at the start of this README

```http://localhost:8080/{endpoint}```

To run without Docker and assuming Python is installed, navigate to the app directory and run the following commands to launch a dev server

```pip install -r requirements.txt```

```python app.py```

## Some Improvements

- [] use smaller base image
- [] create Docker Compose for local dev
- [] do not run containers as root, create specific user
- [] create pipelines, including pre-commit hooks, SCA, SAST, testing, image build, image scanning
- [] store images in private repo - GHCR, ECR, etc
- [] run Flask is Production mode

