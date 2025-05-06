import os
import pandas as pd
import numpy as np
from ml_project import logger
from sklearn.model_selection import train_test_split
from ml_project.entity.config_entity import DataTransformationConfig

# Our dataset is already clean and in the numeric form .
# Now for the time being we will only be doing the train test split.
# But in case of your project you can add more transformation steps like scaling, PCA, encoding, etc.

class DataTransformation:
    """Data Transformation"""
    def __init__(self, config: DataTransformationConfig):
        """Initialize Data Transformation"""
        self.config = config

    
    def train_test_split(self):
        """Train Test Split"""
        logger.info("Splitting data into train and test sets")
        # Read the data from the data path
        data = pd.read_csv(self.config.data_path)
        
        # Split the data into train and test sets
        train, test = train_test_split(data, test_size=0.2, random_state=42) # 80% train, 20% test
        
        # Save the train and test sets to CSV files
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info("Data split completed")
        logger.info(f"Train data saved to {os.path.join(self.config.root_dir, 'train.csv')}")
        logger.info(f"Test data saved to {os.path.join(self.config.root_dir, 'test.csv')}")

        print(train.shape)
        print(test.shape)