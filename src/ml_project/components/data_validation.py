import pandas as pd
from ml_project import logger
from ml_project.entity.config_entity import DataValidationConfig


class DataValidation:
    """Data Validation"""
    def __init__(self, config: DataValidationConfig):
        """Initialize Data Validation"""
        self.config = config


    def validate_all_columns(self) -> bool:
        try:
            validation_status = True

            data = pd.read_csv(self.config.unzip_data_dir)
            all_columns = list(data.columns)

            all_schema_key = self.config.all_schema.keys()

            for column in all_columns:
                if column not in all_schema_key:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"Column {column} is not in the schema\n")
                else:
                    actual_dtypes = data.dtypes.apply(lambda x: x.name).to_dict()
                    expected_dtypes = self.config.all_schema

                    if actual_dtypes != expected_dtypes:
                        validation_status = False
                        with open(self.config.STATUS_FILE, "w") as f:
                            f.write(f"Column {column} data type mismatch: expected {expected_dtypes}, got {actual_dtypes}\n")
                    else:
                        validation_status = True
                        with open(self.config.STATUS_FILE, "w") as f:
                            f.write(f"All necessary columns are in the schema and data type matches\n")

            return validation_status

        except Exception as e:
            raise e         