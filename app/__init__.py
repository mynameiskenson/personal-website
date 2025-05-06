from flask import Flask
from dotenv import load_dotenv
from sqlalchemy import select

# EXTENSIONS
from .extensions import db, migrate, ckeditor, bootstrap, login_manager

# ROUTES
from .routes.main_routes import main
from .routes.blog_routes import blog

# HELPERS
from .helper import gravatar_url

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    @app.context_processor
    def inject_gravatar():
        return dict(gravatar_url=gravatar_url)

    # INITIALIZE EXTENSIONS
    db.init_app(app)
    migrate.init_app(app, db)
    ckeditor.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    # IMPORT MODELS
    with app.app_context():
        from app.models.blog_post import BlogPost
        from app.models.user import User
        from app.models.comment import Comment

    app.register_blueprint(main)
    app.register_blueprint(blog)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.execute(select(User).where(User.id == user_id)).scalar()

    return app