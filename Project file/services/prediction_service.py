import joblib
import numpy as np
from pathlib import Path
from utils.logger import logger


class PredictionService:

    _model = None

    @classmethod
    def load_model(cls):

        if cls._model is None:

            model_path = Path(
                "models/power_prediction.pkl"
            )

            cls._model = joblib.load(
                model_path
            )

            logger.info(
                "ML model loaded."
            )

        return cls._model

    @classmethod
    def predict_power(
            cls,
            theoretical_power,
            wind_speed
    ):

        try:

            if theoretical_power <= 0:
                return {
                    "success": False,
                    "message":
                    "Invalid theoretical power"
                }

            if wind_speed <= 0:
                return {
                    "success": False,
                    "message":
                    "Invalid wind speed"
                }

            model = cls.load_model()

            data = np.array(
                [[
                    theoretical_power,
                    wind_speed
                ]]
            )

            prediction = model.predict(
                data
            )[0]

            return {
                "success": True,
                "prediction":
                round(float(prediction), 2)
            }

        except Exception as e:

            logger.error(str(e))

            return {
                "success": False,
                "message": str(e)
            }
