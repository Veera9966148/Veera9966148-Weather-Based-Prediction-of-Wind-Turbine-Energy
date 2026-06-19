import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    DATABASE_PATH = os.getenv(
        "DATABASE_PATH",
        "instance/windai.db"
    )
    DEBUG = os.getenv("DEBUG", "False") == "True"


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
