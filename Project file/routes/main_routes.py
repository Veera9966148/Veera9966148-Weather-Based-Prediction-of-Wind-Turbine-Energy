from flask import (
    Blueprint,
    render_template,
    jsonify
)

from database.db import (
    get_total_predictions,
    get_average_prediction,
    get_prediction_history
)

main_bp = Blueprint(
    "main",
    __name__
)


@main_bp.route("/")
def home():
    return render_template(
        "home.html"
    )


@main_bp.route("/api")
def api_home():
    return jsonify({
        "application":
        "WindAI Analytics",
        "status":
        "Running"
    })


@main_bp.route("/health")
def health():
    return jsonify({
        "status":
        "healthy",
        "model_loaded":
        True,
        "database":
        "connected"
    })


@main_bp.route("/dashboard")
def dashboard():

    total_predictions = get_total_predictions()
    average_prediction = get_average_prediction()
    prediction_history = get_prediction_history()

    return render_template(
        "dashboard.html",
        total_predictions=total_predictions,
        average_prediction=average_prediction,
        prediction_history=prediction_history
    )
