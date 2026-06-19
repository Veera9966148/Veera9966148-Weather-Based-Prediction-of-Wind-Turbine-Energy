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

            logger.info(
                "Database initialized."
            )

    except Exception as e:
        logger.error(str(e))


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
                INSERT INTO prediction_history(
                    city,
                    theoretical_power,
                    wind_speed,
                    predicted_power
                )
                VALUES(?,?,?,?)
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


def get_history():

    try:
        with get_connection() as conn:

            cursor = conn.cursor()

            cursor.execute("""
            SELECT *
            FROM prediction_history
            ORDER BY id DESC
            """)

            return cursor.fetchall()

    except Exception as e:
        logger.error(str(e))
        return []
