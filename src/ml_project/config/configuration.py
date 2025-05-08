from ml_project.constants import *
from ml_project.utils.common import read_yaml, create_directories
from ml_project.entity.config_entity import (DataIngestionConfig,
                                             DataValidationConfig,
                                             DataTransformationConfig,
                                             ModelTrainerConfig)


class ConfigurationManager:
    """Configuration Manager"""
    def __init__(
        self, 
        config_filepath = CONFIG_FILE_PATH, 
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        """Initialize Configuration Manager"""
        # Initialize the ConfigurationManager with file paths for configuration, parameters, and schema.
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)



        # Create directories for artifacts and data ingestion
        create_directories([self.config.artifacts_root])  # Create the artifacts root directory


    # Data Ingestion Configuration
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """Get Data Ingestion Configuration"""
        config = self.config.data_ingestion
        create_directories([config.root_dir])  # Create the data ingestion root directory

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    # Data Validation Configuration
    def get_data_validation_config(self) -> DataValidationConfig:
        """Get Data Validation Configuration"""
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        create_directories([config.root_dir])  # Create the data ingestion root directory

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_dir=config.unzip_data_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema
        )
        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        """Get Data Transformation Configuration"""
        config = self.config.data_transformation

        create_directories([config.root_dir])  # Create the data transformation root directory

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )
        
        return data_transformation_config
    

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        """Get Model Trainer Configuration"""
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        
        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            random_state=params.random_state,
            target_column=schema.name,
        )
        
        return model_trainer_config