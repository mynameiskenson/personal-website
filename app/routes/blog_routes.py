from flask import Blueprint, render_template, request, url_for
from datetime import datetime
from werkzeug.utils import redirect

from app.forms import CreatePostForm, CommentForm
from app.extensions import db
import requests

# IMPORT MODELS
from app.models.blog_post import BlogPost

blog = Blueprint("blog", __name__)

@blog.app_context_processor
def inject_year():
    return {"year": datetime.now().year}

@blog.route("/post/<int:post_id>", methods=["GET","POST"])
def get_post(post_id):
    cf = CommentForm()
    if request.method == "GET":
        # FOR DEBUGGING
        # result = requests.get("https://api.npoint.io/e50d77e510f3fb462bb2")
        # result.raise_for_status()
        # blogs = result.json()
        # for _post in blogs:
        #     if _post["id"] == post_id:
        #         return render_template("post.html", post = _post, comment_form=cf)

        _post = db.get_or_404(BlogPost, post_id)
        return render_template("post.html", post=_post, comment_form=cf)


@blog.route("/make-post", methods=["POST"])
def add_new_post():
    cpf = CreatePostForm()
    if cpf.validate_on_submit():
        new_post =BlogPost(
            title=cpf.title.data,
            subtitle=cpf.subtitle.data,
            author="Kenson Manduyag",
            created_at=datetime.now(),
            body=cpf.body.data
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("main.blog"))
    return render_template("make-post.html", post_form=cpf)

@blog.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    _post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=_post.title,
        subtitle=_post.subtitle,
        author="Kenson Manduyag",
        created_at=datetime.now(),
        body=_post.body
    )
    if edit_form.validate_on_submit():
        _post.title = edit_form.title.data
        _post.subtitle = edit_form.subtitle.data
        _post.author = "Kenson Manduyag"
        _post.created_at = datetime.now()
        _post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("blog.get_post", post_id=_post.id))
    return render_template("make-post.html", post_form=edit_form, is_edit=True)

@blog.route("/delete-post/<int:post_id>", methods=["GET"])
def delete_post(post_id):
    _post = db.get_or_404(BlogPost, post_id)
    db.session.delete(_post)
    db.session.commit()
    return redirect(url_for("main.blog"))