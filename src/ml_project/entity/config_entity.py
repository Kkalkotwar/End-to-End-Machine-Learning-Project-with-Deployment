# perparing the data entities

from dataclasses import dataclass
from pathlib import Path

# Below is the data class for data ingestion configuration
# This class is used to define the configuration for data ingestion in a machine learning pipeline.
@dataclass(frozen=True)
class DataIngestionConfig:
    """Data Ingestion Configuration"""
    # Define the attributes of the class
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    """Data Validation Configuration"""
    # Define the attributes of the class
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: Path
    all_schema: dict # Define the schema for the data validation

@dataclass(frozen=True)
class DataTransformationConfig:
    """Data Transformation Configuration"""
    # Define the attributes of the class
    root_dir: Path
    data_path: Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    """Model Training Configuration"""
    # Define the attributes of the class
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    random_state: int
    target_column: str


@dataclass(frozen=True)
class ModelEvaluationConfig:
    """Model Evaluation Configuration"""
    # Define the attributes of the class
    root_dir: Path
    model_path: Path
    test_data_path: Path
    report_path: Path
    all_param: dict
    target_column: str
    mlflow_tracking_uri: str