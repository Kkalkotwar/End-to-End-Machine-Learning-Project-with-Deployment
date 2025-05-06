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