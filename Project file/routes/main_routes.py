from flask import (
    Blueprint,
    render_template,
    jsonify
)

main_bp = Blueprint(
    "main",
    __name__
)


@main_bp.route("/")
def home():
    return render_template(
        "index.html"
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
