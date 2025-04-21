from flask import Blueprint, render_template, request
from datetime import datetime
from app.forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
import requests

blog = Blueprint("blog", __name__)

@blog.app_context_processor
def inject_year():
    return {"year": datetime.now().year}

@blog.route("/post/<int:post_id>", methods=["GET","POST"])
def get_post(post_id):
    cf = CommentForm()
    if request.method == "GET":
        result = requests.get("https://api.npoint.io/e50d77e510f3fb462bb2")
        result.raise_for_status()
        blogs = result.json()

        for _post in blogs:
            if _post["id"] == post_id:
                return render_template("post.html", post = _post, comment_form=cf)

@blog.route("/make-post")
def add_new_post():
    cpf = CreatePostForm()
    return render_template("make-post.html", post_form=cpf)