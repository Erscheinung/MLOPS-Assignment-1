# MLOPS-Assignment-1

**To Do:**
- Create new branch for model training using (for example): `git checkout -b feature/model-training`
- Create an actual ML model, train it, track data versions, preprocess (as part of a workflow)
- Hyperparameter tuning, model packaging and packaging into Flask container image for Front-End interactions
- Deploy dockerised model on (preferably GCP) using GKE, set up K8S cluster and create Helm chart for deployments

Install Dependencies (for anaconda or local python env): `pip install dvc torch torchvision pytest flake8`

Build docker container using: `docker build -t mlops-assignment .`

Run docker container using: `docker run mlops-assignment`