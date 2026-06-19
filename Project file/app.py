from flask import Flask

from config import (
    DevelopmentConfig
)

from database.db import (
    initialize_database
)

from routes.main_routes import (
    main_bp
)

from routes.prediction_routes import (
    prediction_bp
)

from routes.api_routes import (
    api_bp
)


def create_app():

    app = Flask(__name__)

    app.config.from_object(
        DevelopmentConfig
    )

    app.register_blueprint(
        main_bp
    )

    app.register_blueprint(
        prediction_bp
    )

    app.register_blueprint(
        api_bp
    )

    with app.app_context():
        initialize_database()

    @app.errorhandler(404)
    def not_found(error):

        return {
            "success": False,
            "message":
            "Page not found"
        }, 404

    @app.errorhandler(500)
    def server_error(error):

        return {
            "success": False,
            "message":
            "Internal server error"
        }, 500

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
