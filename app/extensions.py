from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_ckeditor import CKEditor
from flask_bootstrap import Bootstrap5

db = SQLAlchemy()
migrate = Migrate()
ckeditor = CKEditor()
bootstrap = Bootstrap5()