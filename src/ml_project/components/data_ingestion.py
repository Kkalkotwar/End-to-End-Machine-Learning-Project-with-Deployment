import os
import zipfile
from pathlib import Path
from ml_project import logger
import urllib.request as request
from ml_project.utils.common import get_size
from ml_project.entity.config_entity import DataIngestionConfig



class DataIngestion:
    """Data Ingestion"""
    def __init__(self, config: DataIngestionConfig):
        """Initialize Data Ingestion"""
        self.config = config


    def download_file(self):
        """Download file from URL"""
        if not os.path.exists(self.config.local_data_file):

            # Download the file from the source URL to the local data file path
            request.urlretrieve(self.config.source_URL, self.config.local_data_file)
            logger.info(f"Downloading file from {self.config.source_URL} to {self.config.local_data_file}")
            logger.info(f"Downloaded file size: {get_size(Path(self.config.local_data_file))} bytes")
        else:
            logger.info(f"File already exists at {self.config.local_data_file} of size: {get_size(Path(self.config.local_data_file))} bytes. Skipping download.")


    def extract_zip_file(self):
            
        """Extract zip file"""
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"Extracted zip file to {unzip_path}")
        return unzip_path
