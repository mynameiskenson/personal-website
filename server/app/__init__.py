from dotenv import load_dotenv
from flask import Flask

# EXTENSIONS
from .extensions import db, migrate, cors, ma

def create_app():
    # Load environment variables from .env file
    load_dotenv()

    # Create Flask app instance
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app)

    # Import models to ensure they are registered with SQLAlchemy
    with app.app_context():
        from app.models.post_model import Post
        from app.models.user_model import User
        from app.models.comment_model import Comment

    # Register blueprints
    from .routes.user_routes import user_bp
    from .routes.post_routes import post_bp

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(post_bp, url_prefix='/api/posts')

    return app  