from flask import (
    Blueprint,
    jsonify
)

from database.db import (
    get_prediction_history
)

api_bp = Blueprint(
    "api",
    __name__
)


@api_bp.route("/history")
def history():
    history_data = get_prediction_history()

    return jsonify([
        dict(row)
        for row in history_data
    ])
