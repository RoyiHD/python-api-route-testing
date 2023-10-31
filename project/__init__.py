from flask import Flask
from project.routes import register_routes


def create_app() -> Flask:
    
    app: Flask = Flask(__name__, static_folder=None)
    register_routes(app)

    return app
