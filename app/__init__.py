from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

from .routes.main_routes import main
from .routes.blog_routes import blog

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    # Import models here
    with app.app_context():
        from app.models.blog_post import BlogPost

    app.register_blueprint(main)
    app.register_blueprint(blog)

    bootstrap = Bootstrap5(app)
    ckeditor = CKEditor(app)

    return app