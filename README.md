# End-to-End-Machine-Learning-Project-with-Deployment
This is the Repository which contains End-to-End Machine Learning Project Workflow with Deployment.

## WorkFlow

1. Update config.yaml    ------> Inside the Config folder (Not in src folder, it is out of src folder).
2. Update schema.yaml    ------> It's just a file where you mention the columns you have in you data with respect to 
                                 the data types.
3. Update params.yaml    ------> We will be writing all the parameters we wil be using in our project.
                                 Let's say values like "α" , "β" , "γ" which might be used in our process code. 
4. Update the entity     ------> Updating the config_entity.py file in src folder
5. Update the configuration manager in src config -----> Inside the src.config folder ["Configuration.py" file]
6. Update the components ------> Components like "Data Ingestion", "Data Validation", "Data Transformation"...etc. 
7. Update the pipeline   ------> Update and adding the pipeline. Basically integrating all the components with
                                 pipeline {Training pipeline separate and prediction pipeline separate}.
8. Update the main.py    ------> This will be the main.py file update.
9. Update the app.py     ------> Inside app.py we will be writing the UI related functionality, and integrate this
                                 main.py with app.py {User will run the app.py and it will run all the code.}






# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/Kkalkotwar/End-to-End-Machine-Learning-Project-with-Deployment.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n ml_project python=3.8 -y
or 
python -m venv {environment_name}
```

```bash
conda activate mlproj
or
activate the venv by coping the relative path of activate file {.venv\Scripts\activate}
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)
### Using MLFlow tracking from Remote/Experiments of dagshub page.

import dagshub
dagshub.init(repo_owner='kunalkalkotwar21', repo_name='End-to-End-Machine-Learning-Project-with-Deployment', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI= *Your Tracking URI*

export MLFLOW_TRACKING_USERNAME= *Your Tracking Username*

export MLFLOW_TRACKING_PASSWORD= *Your Tracking Password*

```


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model