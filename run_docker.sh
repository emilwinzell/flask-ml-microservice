#!/usr/bin/env bash

# Build image
#change tag for new container registery, gcr.io/bob
docker build --tag=emilwinzell/flask-mlops . 

# List docker images
docker image ls

# Run flask app
docker run -p 0.0.0.0:8080:8080 emilwinzell/flask-mlops