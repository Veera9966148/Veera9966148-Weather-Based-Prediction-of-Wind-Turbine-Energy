from flask import (
    Blueprint,
    request,
    jsonify,
    render_template
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
    methods=["GET", "POST"]
)
def predict():

    if request.method == "GET":
        return render_template(
            "predict.html"
        )

    try:
        data = request.get_json()

        city = data.get(
            "city",
            ""
        )

        theoretical_power = float(
            data.get(
                "theoretical_power",
                0
            )
        )

        wind_speed = float(
            data.get(
                "wind_speed",
                0
            )
        )

        result = (
            PredictionService
            .predict_power(
                theoretical_power,
                wind_speed
            )
        )

        if result.get(
            "success"
        ):
            insert_prediction(
                city,
                theoretical_power,
                wind_speed,
                result.get(
                    "prediction"
                )
            )

        return jsonify(
            result
        )

    except Exception as e:
        return jsonify({
            "success":
            False,
            "message":
            str(e)
        }), 500
