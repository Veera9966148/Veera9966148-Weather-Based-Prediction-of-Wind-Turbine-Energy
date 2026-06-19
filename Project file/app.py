from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from config import Config
from database.db import init_db
from services.weather_service import get_weather
from services.prediction_service import predict_power

app = Flask(__name__)
app.config.from_object(Config)

init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():

    weather = None
    prediction = None

    if request.method == "POST":

        city = request.form.get("city")
        theoretical = request.form.get(
            "theoretical_power"
        )
        wind_speed = request.form.get(
            "wind_speed"
        )

        if city:
            weather = get_weather(
                city,
                app.config["OPENWEATHER_API_KEY"]
            )

        if theoretical and wind_speed:
            try:
                prediction = predict_power(
                    float(theoretical),
                    float(wind_speed)
                )

            except ValueError:
                prediction = "Invalid Input"

    return render_template(
        "dashboard.html",
        weather=weather,
        prediction=prediction
    )


@app.route("/api/predict", methods=["POST"])
def api_predict():

    data = request.json

    result = predict_power(
        data["theoretical_power"],
        data["wind_speed"]
    )

    return jsonify({
        "predicted_power": result
    })


if __name__ == "__main__":
    app.run(debug=True)
