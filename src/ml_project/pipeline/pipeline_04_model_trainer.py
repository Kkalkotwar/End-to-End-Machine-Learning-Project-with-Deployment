from ml_project import logger
from pathlib import Path
from ml_project.config.configuration import ConfigurationManager
from ml_project.components.model_trainer import ModelTrainer

STAGE_NAME = "Model Training stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_training = ModelTrainer(model_trainer_config)
        model_training.train()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
