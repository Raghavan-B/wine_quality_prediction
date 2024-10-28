from src.wine_quality_prediction import logger
from src.wine_quality_prediction.components.model_evaluation import ModelEvaluation
from src.wine_quality_prediction.config.configuration import ConfigurationManager

import os
# os.environ['MLFLOW_TRACKING_URI'] = "https://dagshub.com/Raghavan-B/wine_quality_prediction.mlflow"
# os.environ['MLFLOW_TRACKING_USERNAME'] = "Raghavan-B"
# os.environ['MLFLOW_TRACKING_PASSWORD'] = "7a7b3ed8949e141afa19b16fd13ad5a887d2793a"

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.log_into_mlflow()
