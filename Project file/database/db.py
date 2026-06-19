import sqlite3
from flask import current_app
from utils.logger import logger


def get_connection():
    return sqlite3.connect(
        current_app.config["DATABASE_PATH"]
    )


def initialize_database():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS predictions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    city TEXT NOT NULL,
                    theoretical_power REAL NOT NULL,
                    wind_speed REAL NOT NULL,
                    predicted_power REAL NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)

            conn.commit()
            logger.info("Database initialized.")

    except Exception as e:
        logger.error(str(e))


def get_total_predictions():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute(
                "SELECT COUNT(*) FROM predictions"
            )

            return cursor.fetchone()[0]

    except Exception as e:
        logger.error(str(e))
        return 0


def get_average_prediction():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute(
                "SELECT AVG(predicted_power) FROM predictions"
            )

            result = cursor.fetchone()[0]

            return round(result or 0, 2)

    except Exception as e:
        logger.error(str(e))
        return 0


def get_prediction_history():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("""
                SELECT
                    city,
                    theoretical_power,
                    wind_speed,
                    predicted_power,
                    created_at
                FROM predictions
                ORDER BY created_at DESC
            """)

            return cursor.fetchall()

    except Exception as e:
        logger.error(str(e))
        return []


def insert_prediction(
    city,
    theoretical_power,
    wind_speed,
    predicted_power
):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO predictions (
                    city,
                    theoretical_power,
                    wind_speed,
                    predicted_power
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    city,
                    theoretical_power,
                    wind_speed,
                    predicted_power
                )
            )

            conn.commit()

    except Exception as e:
        logger.error(str(e))
