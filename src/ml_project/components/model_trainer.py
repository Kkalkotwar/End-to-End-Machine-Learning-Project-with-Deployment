# COMPONENT 1: Model Trainer Component
# This component is responsible for training the machine learning model using the provided training data.

import os
import joblib
import pandas as pd
from ml_project import logger
from sklearn.linear_model import ElasticNet
from ml_project.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    """Model Trainer"""
    def __init__(self, config: ModelTrainerConfig):
        """Initialize Model Trainer"""
        self.config = config

    
    def train(self):
        """Train the model"""
        # Load the training data
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        # Separate features and target variable from training and testing data
        X_train = train_data.drop(columns=[self.config.target_column], axis=1)
        y_train = train_data[self.config.target_column]
        X_test = test_data.drop(columns=[self.config.target_column], axis=1)
        y_test = test_data[self.config.target_column]

        # Initialize the ElasticNet model with hyperparameters
        lr = ElasticNet(
            alpha=self.config.alpha,
            l1_ratio=self.config.l1_ratio,
            random_state=self.config.random_state
        )

        # Train the model on the training data
        lr.fit(X_train, y_train)
        
        # Ensure the directory exists
        os.makedirs(self.config.root_dir, exist_ok=True)

        # Save the trained model to a file
        model_path = os.path.join(self.config.root_dir, self.config.model_name)
        # Save the model using joblib
        joblib.dump(lr, model_path)

        logger.info(f"Model trained and saved at: {model_path}")