NOTE: I have run out of credits in my billing account and was therefore unable to enable kubernetes or run any code. 
I will be requesting more credits and quickly catching up to where I need to be on this project.

ALL FILES IN PROJECT CHECKPOINT FOLDER
PROJECT OPTION 2
Steps for connecting to GCP:
import google.cloud.container_v1 as container
from google.auth import compute_engine
from google.cloud.container_v1 import ClusterManagerClient
from kubernetes import client, config

then use .getCluster() method of ClusterManagerClient to access the cluster using your credentials

This should give us the cluster, then allow us to connect to it through our code. 

The only build/run commands for my project will be python3 course_project.py, or whatever the python name of my file is.
From there the user will have access to whatever functionality they will require, run through GCP.
