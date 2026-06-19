import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "windai-secret")
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    DATABASE_PATH = BASE_DIR / "database" / "predictions.db"
    MODEL_PATH = BASE_DIR / "models" / "power_prediction.pkl"
