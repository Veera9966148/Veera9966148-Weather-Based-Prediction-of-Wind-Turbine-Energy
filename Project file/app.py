from flask import (
    Flask,
    render_template,
    jsonify
)

from routes.prediction_routes import (
    prediction_bp
)

from routes.dashboard_routes import (
    dashboard_bp
)

from database.db import (
    init_db
)

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

# Initialize database
init_db()

# Register Blueprints
app.register_blueprint(
    prediction_bp
)

app.register_blueprint(
    dashboard_bp
)


# -------------------------
# Home Page
# -------------------------
@app.route("/")
def home():
    return render_template(
        "home.html"
    )


# -------------------------
# Health Check API
# -------------------------
@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "database": "connected",
        "model_loaded": True
    })


# -------------------------
# Application API
# -------------------------
@app.route("/api")
def api():
    return jsonify({
        "application":
            "WindAI Analytics",
        "status":
            "Running"
    })


# -------------------------
# Error Pages
# -------------------------
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({
        "success": False,
        "message": "Page Not Found"
    }), 404


@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success": False,
        "message":
            "Internal Server Error"
    }), 500


# -------------------------
# Run Application
# -------------------------
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
