from flask import Blueprint, render_template, request
from datetime import datetime
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
    return render_template("blog.html")