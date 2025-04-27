from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

# EXTENSIONS
from .extensions import db, migrate, ckeditor, bootstrap

# ROUTES
from .routes.main_routes import main
from .routes.blog_routes import blog

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # INITIALIZE EXTENSIONS
    db.init_app(app)
    migrate.init_app(app, db)
    ckeditor.init_app(app)
    bootstrap.init_app(app)

    # IMPORT MODELS
    with app.app_context():
        from app.models.blog_post import BlogPost
        from app.models.user import User

    app.register_blueprint(main)
    app.register_blueprint(blog)

    return app