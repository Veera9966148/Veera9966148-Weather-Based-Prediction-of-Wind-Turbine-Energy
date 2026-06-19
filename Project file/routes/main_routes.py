from flask import Blueprint

main_bp = Blueprint(
    "main",
    __name__
)


@main_bp.route("/")
def home():

    return {
        "application":
        "WindAI Analytics",
        "status":
        "Running"
    }


@main_bp.route("/health")
def health():

    return {
        "status":
        "healthy",
        "model_loaded":
        True,
        "database":
        "connected"
    }
