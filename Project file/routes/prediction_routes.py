from flask import (
    Blueprint,
    request,
    jsonify
)

from services.prediction_service import (
    PredictionService
)

from database.db import (
    insert_prediction
)

prediction_bp = Blueprint(
    "prediction",
    __name__
)


@prediction_bp.route(
    "/predict",
    methods=["POST"]
)
def predict():

    data = request.get_json()

    city = data.get("city")
    theoretical_power = float(
        data.get("theoretical_power")
    )

    wind_speed = float(
        data.get("wind_speed")
    )

    result = (
        PredictionService
        .predict_power(
            theoretical_power,
            wind_speed
        )
    )

    if result["success"]:

        insert_prediction(
            city,
            theoretical_power,
            wind_speed,
            result["prediction"]
        )

    return jsonify(result)
