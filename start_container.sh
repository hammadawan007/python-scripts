#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull hammadhussain007/python-scripts

# Run the Docker image as a container
docker run -d -p 5000:5000 hammadhussain007/python-scripts