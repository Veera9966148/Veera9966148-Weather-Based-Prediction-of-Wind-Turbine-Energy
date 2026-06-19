from flask import Flask, render_template, request, jsonify
from config import Config
from database import init_db
from services.weather_service import get_weather
from services.prediction_service import predict_power

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

app.config.from_object(Config)

# Initialize Database
init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template(
        "dashboard.html",
        temperature=27,
        humidity=65,
        wind_speed=8.2,
        prediction=1520
    )


@app.route("/predict", methods=["GET", "POST"])
def predict():

    weather = None
    prediction = None

    if request.method == "POST":

        city = request.form.get("city")
        theoretical = request.form.get("theoretical_power")
        wind_speed = request.form.get("wind_speed")

        # Get Weather
        if city:
            weather = get_weather(
                city,
                app.config["OPENWEATHER_API_KEY"]
            )

        # Predict Power
        if theoretical and wind_speed:
            try:
                prediction = predict_power(
                    float(theoretical),
                    float(wind_speed)
                )
            except ValueError:
                prediction = "Invalid Input"

    return render_template(
        "predict.html",
        weather=weather,
        prediction=prediction
    )


@app.route("/api/predict", methods=["POST"])
def api_predict():

    data = request.get_json()

    try:
        result = predict_power(
            float(data["theoretical_power"]),
            float(data["wind_speed"])
        )

        return jsonify({
            "success": True,
            "predicted_power": result
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
