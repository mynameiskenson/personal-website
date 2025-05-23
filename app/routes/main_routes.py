from flask import Blueprint, render_template, request, flash, url_for
from sqlalchemy import select, desc
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime

from app.forms import LoginForm, RegisterForm
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

    page = request.args.get("page", 1, type=int)
    result = db.session.query(BlogPost).order_by(desc(BlogPost.created_at))
    pagination = result.paginate(page=page, per_page=3, error_out=False)
    return render_template("blog.html", pagination=pagination)

@main.route("/login", methods=["GET", "POST"])
def login():
    lf = LoginForm()
    if request.method == "GET":
        return render_template("login.html", form=lf)
    else:
        if lf.validate_on_submit():
            input_email = lf.email.data

            result = db.session.execute(db.select(User).where(User.email == input_email))
            is_user = result.scalar()

            if is_user:
                is_logged_in = check_password_hash(is_user.password, lf.password.data)

                if is_logged_in:
                    login_user(is_user)
                    return redirect(url_for("main.blog"))
                else:
                    flash('Invalid credential.')
                    return render_template("login.html", form=lf)
            else:
                flash('Not registered.')
                return render_template("login.html", form=lf)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.home"))

@main.route("/register", methods=["GET", "POST"])
def register():
    rf = RegisterForm()
    if request.method == "POST":
        if rf.validate_on_submit():
            result = db.session.execute(select(User).where(User.email == rf.email.data))
            is_exist = result.scalars().all()

            if not is_exist:
                new_user = User(
                    name=rf.name.data,
                    email=rf.email.data,
                    password=generate_password_hash(rf.password.data, method="pbkdf2:sha256", salt_length=8)
                )
                db.session.add(new_user)
                db.session.commit()

                login_user(new_user)
                return redirect(url_for("main.blog"))
            else:
                flash("You've already signed up with that email, log in instead!")
                return redirect(url_for("main.login"))

    return render_template("register.html", form=rf)