import requests
from flask import current_app
from utils.logger import logger


def get_weather_by_city(city):

    try:

        key = current_app.config[
            "OPENWEATHER_API_KEY"
        ]

        url = (
            "https://api.openweathermap.org/"
            "data/2.5/weather"
        )

        params = {
            "q": city,
            "appid": key,
            "units": "metric"
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        data = response.json()

        if response.status_code != 200:

            return {
                "success": False,
                "message":
                "Invalid city"
            }

        return {
            "success": True,
            "city": data["name"],
            "temperature":
            data["main"]["temp"],
            "humidity":
            data["main"]["humidity"],
            "wind_speed":
            data["wind"]["speed"],
            "description":
            data["weather"][0]["description"]
        }

    except Exception as e:

        logger.error(str(e))

        return {
            "success": False,
            "message":
            "Weather service unavailable"
        }
