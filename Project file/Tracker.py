
# tracker.py
# Wind Energy Project - Production Features
# Developer: Veeresh Kumar

import json
import os
from datetime import datetime


def startup_check():
    print("=" * 40)
    print("Wind Energy Prediction System")
    print("=" * 40)

    errors = []

    if os.path.exists("model.pkl"):
        print("ML Model found")
    else:
        errors.append("model.pkl not found!")

    if os.path.exists("templates"):
        print("Templates folder found")
    else:
        errors.append("Templates folder missing!")

    config = load_config()
    print(f"Config loaded - version: {config.get('version', '1.0')}")

    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        print("Fix errors before starting!")
    else:
        print("All checks passed - Starting app!")

    print("=" * 40)
    return len(errors) == 0


def load_config():
    if os.path.exists("config.json"):
        with open("config.json", "r") as f:
            return json.load(f)
    return {
        "version": "1.0.0",
        "app_name": "Wind Energy Predictor",
        "developer": "Veeresh Kumar",
        "log_predictions": True,
        "max_wind_speed": 120.0
    }


def save_config(key, value):
    config = load_config()
    config[key] = value
    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)
    print(f"Config saved: {key} = {value}")


def log_prediction(wind_speed, temperature, humidity, predicted_kwh):
    config = load_config()

    if not config.get("log_predictions", True):
        return

    entry = {
        "timestamp": datetime.now().isoformat(),
        "inputs": {
            "wind_speed_kmph": wind_speed,
            "temperature_c": temperature,
            "humidity_percent": humidity
        },
        "output": {
            "predicted_kwh": round(predicted_kwh, 2)
        },
        "risk_level": get_risk_level(predicted_kwh)
    }

    with open("predictions.jsonl", "a") as f:
        f.write(json.dumps(entry) + "\n")


def get_risk_level(predicted_kwh):
    if predicted_kwh >= 800:
        return "High Output - Excellent"
    elif predicted_kwh >= 500:
        return "Medium Output - Good"
    elif predicted_kwh >= 200:
        return "Low Output - Average"
    else:
        return "Very Low - Check Turbine"


def save_checkpoint(data):
    checkpoint = {
        "last_prediction": data,
        "saved_at": datetime.now().isoformat()
    }
    with open("checkpoint.json", "w") as f:
        json.dump(checkpoint, f, indent=2)


def load_checkpoint():
    if os.path.exists("checkpoint.json"):
        with open("checkpoint.json") as f:
            return json.load(f)
    return None


def get_stats():
    if not os.path.exists("predictions.jsonl"):
        return {"total_predictions": 0, "message": "No predictions yet"}

    predictions = []
    with open("predictions.jsonl") as f:
        for line in f:
            predictions.append(json.loads(line))

    if not predictions:
        return {"total_predictions": 0}

    outputs = [p["output"]["predicted_kwh"] for p in predictions]

    return {
        "total_predictions": len(predictions),
        "average_kwh": round(sum(outputs) / len(outputs), 2),
        "highest_kwh": round(max(outputs), 2),
        "lowest_kwh": round(min(outputs), 2),
        "last_prediction": predictions[-1]["timestamp"]
    }
