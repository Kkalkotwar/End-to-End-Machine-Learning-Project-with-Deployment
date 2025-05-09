import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from ml_project.utils.common import save_json
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import joblib
from ml_project.entity.config_entity import ModelEvaluationConfig

class ModelEvaluation:
    """Model Evaluation"""
    def __init__(self, config: ModelEvaluationConfig):
        """Initialize Model Evaluation"""
        self.config = config

    def eval_report(self, actual, predict):
        """Evaluation Report"""
        r2 = r2_score(actual, predict)
        rmse = np.sqrt(mean_squared_error(actual, predict))
        mae = mean_absolute_error(actual, predict)

        return r2, rmse, mae
    
    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        target_column = str(self.config.target_column)

        test_x = test_data.drop([target_column], axis=1)
        test_y = test_data[[target_column]]

        mlflow.set_registry_uri(self.config.mlflow_tracking_uri)
        tracking_uri_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        with mlflow.start_run():
            predicted_quantity = model.predict(test_x)
            (r2, rmse, mae) = self.eval_report(test_y, predicted_quantity)
            
            # Saving matrices as local
            scores = {
                "r2": r2,
                "rmse": rmse,
                "mae": mae
            }
            save_json(path = Path(self.config.report_path), data=scores)

            mlflow.log_params(self.config.all_param)
            
            # Logging metrics into mlflow
            mlflow.log_metrics({
                "r2": r2,
                "rmse": rmse,
                "mae": mae
            })

            # Model registry does not support local filesystem
            if tracking_uri_type_store != 'file':

                # Register the model in the MLflow Model Registry
                # There are other ways to use the Model Registry, which depends on the use case.
                # Please refer to the MLflow documentation for more details.
                # https://www.mlflow.org/docs/latest/model-registry.html#registering-a-model
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
            else:
                mlflow.sklearn.log_model(model, "model")        