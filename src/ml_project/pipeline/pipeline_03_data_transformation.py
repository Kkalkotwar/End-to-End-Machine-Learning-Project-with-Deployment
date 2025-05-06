from ml_project import logger
from pathlib import Path
from ml_project.config.configuration import ConfigurationManager
from ml_project.components.data_transformation import DataTransformation


STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    

    # 1 .What we are doing here is checking the status of the data validation step. If it is True, 
    #    we proceed with the data transformation.
    
    # 2. If it is False, we raise an exception. 
    #    This is a good practice to ensure that the data validation step has been completed successfully 
    #    before proceeding with the data transformation step.
    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), 'r') as file:
                status = file.read().split(" ")[-1]
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(data_transformation_config)
                data_transformation.train_test_split()
                print("Data transformation completed successfully.")
            else:
                raise Exception("Data validation failed. Please check the data schema.")
        
        except Exception as e:
            logger.exception(e)
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e