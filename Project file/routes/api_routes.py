from flask import (
    Blueprint,
    jsonify
)

from database.db import (
    get_history
)

api_bp = Blueprint(
    "api",
    __name__
)


@api_bp.route("/history")
def history():

    return jsonify(
        get_history()
    )
