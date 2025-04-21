from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from .routes.main_routes import main
from .routes.blog_routes import blog

def create_app():
    app = Flask(__name__)

    app.register_blueprint(main)
    app.register_blueprint(blog)

    bootstrap = Bootstrap5(app)
    ckeditor = CKEditor(app)

    app.config['SECRET_KEY'] = ''
    return app