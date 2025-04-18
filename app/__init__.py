from flask import Flask
from flask_bootstrap import Bootstrap5
from .routes.main_routes import main

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    bootstrap = Bootstrap5(app)

    return app