from flask import Blueprint, render_template, request
from datetime import datetime
main = Blueprint("main", __name__)

@main.route("/")
def home():
    _year = datetime.now().year
    return render_template("home.html", year=_year)