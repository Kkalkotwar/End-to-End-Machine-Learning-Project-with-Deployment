# ml_project/utils/load_env.py

from dotenv import load_dotenv
import os

def load_environment_variables():
    load_dotenv()  # Loads from .env into os.environ

    # Optionally validate important variables
    required_vars = [
        "MLFLOW_TRACKING_URI",
        "MLFLOW_TRACKING_USERNAME",
        "MLFLOW_TRACKING_PASSWORD"
    ]
    for var in required_vars:
        if not os.getenv(var):
            raise EnvironmentError(f"Missing required env variable: {var}")
