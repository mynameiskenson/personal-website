from flask import Blueprint, render_template, request
from datetime import datetime
import requests

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
    result = requests.get("https://api.npoint.io/e50d77e510f3fb462bb2")
    result.raise_for_status()
    _posts = result.json()
    return render_template("blog.html", posts=_posts)