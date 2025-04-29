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