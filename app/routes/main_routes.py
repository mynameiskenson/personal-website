from flask import Blueprint, render_template, request, flash, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from datetime import datetime

from app.forms import LoginForm
from app.extensions import db
import requests

# IMPORT MODELS
from app.models.blog_post import BlogPost
from app.models.user import User

main = Blueprint("main", __name__)

@main.app_context_processor
def inject_year():
    return {"year": datetime.now().year}

@main.route("/")
def home():
    return render_template("home.html")

@main.route("/portfolios")
def portfolios():
    return render_template("portfolios.html")

@main.route("/blog")
def blog():
    # FOR DEBUGGING
    # result = requests.get("https://api.npoint.io/e50d77e510f3fb462bb2")
    # result.raise_for_status()
    # _posts = result.json()

    result = db.session.execute(db.select(BlogPost))
    _posts = result.scalars().all()
    return render_template("blog.html", posts=_posts)

@main.route("/login", methods=["GET", "POST"])
def login():
    lf = LoginForm()
    if request.method == "GET":
        return render_template("login.html", form=lf)
    else:
        if lf.submit.data:
            if lf.validate_on_submit():
                input_email = lf.email.data

                result = db.session.execute(db.select(User).where(User.email == input_email))
                is_user = result.scalar()

                if is_user:
                    is_logged_in = check_password_hash(is_user.password, lf.password.data)

                    if is_logged_in:
                        login_user(is_user)
                        return redirect(url_for("get_all_posts"))
                    else:
                        flash('Invalid credential.')
                        return render_template("login.html", form=lf)
                else:
                    flash('Not registered.')
                    return render_template("login.html", form=lf)
        elif lf.register.data:
            return redirect(url_for("register"))

@main.route("/register", methods=["GET", "POST"])
def register():
    return render_template("portfolios.html")