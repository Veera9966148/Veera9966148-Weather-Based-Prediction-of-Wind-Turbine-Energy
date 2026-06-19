import joblib
import pandas as pd
from config import Config

model = joblib.load(Config.MODEL_PATH)


def predict_power(theoretical_power, wind_speed):

    input_data = pd.DataFrame(
        [[theoretical_power, wind_speed]],
        columns=["TheoreticalPower", "WindSpeed"]
    )

    prediction = model.predict(input_data)

    return round(float(prediction[0]), 2)
